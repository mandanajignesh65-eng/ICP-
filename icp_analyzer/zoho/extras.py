"""Everything Zoho's Bulk Read cannot export: website visits, automation log, the attachment list,
emails logged on deals, and (optionally) the attached files themselves.

Emails and files are fetched in parallel (worker threads, well under Zoho's concurrency limit).
Database writes happen only on the main thread.
"""
from __future__ import annotations

import json
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from ..storage import Store
from .client import ZohoClient, ZohoError

REST_MODULES = ["Visits", "Actions_Performed", "Attachments"]
WORKERS = 5  # per job; emails + files run together = 10 concurrent calls (Professional limit is 15)


def _log_rows(store: Store, rows: list[dict]) -> None:
    log_df = pd.DataFrame(rows)
    log_df["extracted_at"] = datetime.now(timezone.utc).isoformat()
    prev = store.read("meta_extract_log")
    if not prev.empty:
        log_df = pd.concat([prev[~prev["module"].isin(log_df["module"])], log_df], ignore_index=True)
    store.write("meta_extract_log", log_df)


class Progress:
    def __init__(self, label: str, total: int, log, every: int):
        self.label, self.total, self.log, self.every = label, total, log, every
        self.done, self.lock = 0, threading.Lock()

    def tick(self, extra: str = ""):
        with self.lock:
            self.done += 1
            if self.done % self.every == 0 or self.done == self.total:
                self.log(f"    {self.label}: {self.done:,}/{self.total:,} {extra}")


def extract_extras(client: ZohoClient, store: Store, emails: bool = True, files: bool = False,
                   files_dir: Path | None = None, log=print) -> None:
    rows = []
    for m in REST_MODULES:
        try:
            df = client.records_all_fields(m)
            if not df.empty:
                df = df.astype(str).replace({"None": None, "nan": None})
            store.write(f"raw_{m}", df)
            log(f"  {m}: {len(df):,} records")
            rows.append({"module": m, "rows": len(df), "columns": df.shape[1], "method": "rest", "error": None})
        except ZohoError as e:
            log(f"  ! {m} failed: {e}")
            rows.append({"module": m, "rows": 0, "columns": 0, "method": "rest", "error": str(e)[:300]})

    deal_ids = store.read("raw_Deals")["Id"].dropna().astype(str).tolist() if emails and store.has("raw_Deals") else []
    prev_emails = store.read("raw_Deal_Emails")
    checked = store.read("meta_email_checked")
    done = set(checked["deal_id"].astype(str)) if not checked.empty else set()
    if not done and not prev_emails.empty:  # fetched before this tracker existed
        done = set(prev_emails["deal_id"].astype(str))
    deal_ids = [d for d in deal_ids if d not in done]  # resume: skip deals already fetched (even with 0 emails)
    att = store.read("raw_Attachments") if files and store.has("raw_Attachments") else pd.DataFrame()
    files_dir = files_dir or Path("data/attachments")

    with ThreadPoolExecutor(max_workers=2) as jobs:  # emails and files at the same time
        f_emails = jobs.submit(_deal_emails, client, deal_ids, log) if deal_ids else None
        f_files = jobs.submit(_attachment_files, client, att, files_dir, log) if not att.empty else None
        email_df = f_emails.result() if f_emails else None
        saved, failed = f_files.result() if f_files else (None, 0)

    if email_df is not None:
        new_emails, ok_ids = email_df
        keep = prev_emails[~prev_emails["deal_id"].isin(ok_ids)] if not prev_emails.empty else pd.DataFrame()
        email_df = pd.concat([keep, new_emails], ignore_index=True) if len(keep) or len(new_emails) else pd.DataFrame()
        store.write("raw_Deal_Emails", email_df)
        store.write("meta_email_checked", pd.DataFrame({"deal_id": sorted(done | set(ok_ids))}))
        log(f"  Deal emails: {len(email_df):,} total · deals checked: {len(done | set(ok_ids)):,}")
        rows.append({"module": "Deal_Emails", "rows": len(email_df), "columns": email_df.shape[1], "method": "rest", "error": None})
    if saved is not None:
        store.write("meta_attachment_files", saved)
        log(f"  Files saved: {len(saved):,} · failed: {failed:,} → {files_dir}")
        rows.append({"module": "Attachment_Files", "rows": len(saved), "columns": 0, "method": "rest",
                     "error": f"{failed} failed" if failed else None})
    _log_rows(store, rows)


def _deal_emails(client: ZohoClient, ids: list[str], log) -> pd.DataFrame:
    log(f"  Emails on {len(ids):,} deals ({WORKERS} in parallel)...")
    prog = Progress("emails (deals checked)", len(ids), log, 500)
    out, errors, ok_ids = [], 0, []

    def one(deal_id):
        return deal_id, client.emails("Deals", deal_id)

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(one, d) for d in ids]
        for f in as_completed(futures):
            try:
                deal_id, items = f.result()
                ok_ids.append(deal_id)
                out += [{"deal_id": deal_id, **{k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in e.items()}}
                        for e in items]
            except ZohoError:
                errors += 1
            prog.tick(f"({len(out):,} emails)")
    if errors:
        log(f"  ! {errors} deals' emails could not be read — re-run `python cli.py extras --files` to resume")
    return (pd.DataFrame(out).astype(str) if out else pd.DataFrame()), ok_ids


def _attachment_files(client: ZohoClient, att: pd.DataFrame, files_dir: Path, log) -> tuple[pd.DataFrame, int]:
    pid = next((c for c in ("Parent_Id.id", "Parent_Id") if c in att.columns), None)
    pmod = next((c for c in ("$se_module", "Parent_Id.module.api_name", "se_module") if c in att.columns), None)
    name_c = next((c for c in ("File_Name", "$file_name") if c in att.columns), None)
    if not (pid and pmod):
        log(f"  ! attachment list has no parent columns: {list(att.columns)[:15]}")
        return pd.DataFrame(), len(att)
    log(f"  Downloading {len(att):,} attached files ({WORKERS} in parallel)...")
    prog = Progress("files", len(att), log, 200)

    def one(rec):
        module, parent, aid = rec.get(pmod), rec.get(pid), rec.get("id")
        if not (module and parent and aid):
            return None
        fname = re.sub(r'[\\/:*?"<>|]+', "_", str(rec.get(name_c) or aid))[:150]
        target = files_dir / str(module) / str(parent) / f"{aid}_{fname}"
        if not target.exists():
            content = client.download_attachment(str(module), str(parent), str(aid))
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        return {"attachment_id": aid, "module": module, "record_id": parent, "file": fname, "path": str(target),
                "bytes": target.stat().st_size}

    saved, failed = [], 0
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(one, r) for r in att.to_dict("records")]
        for f in as_completed(futures):
            try:
                r = f.result()
                if r:
                    saved.append(r)
                else:
                    failed += 1
            except Exception:
                failed += 1
            prog.tick()
    return pd.DataFrame(saved), failed
