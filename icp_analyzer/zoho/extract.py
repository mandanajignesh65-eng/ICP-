"""Discover the CRM structure and export all data into the local store."""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone

import pandas as pd

from ..storage import Store
from .client import ZohoClient, ZohoError

# Modules the analysis uses. Custom modules are added automatically.
CORE_MODULES = [
    "Leads", "Accounts", "Contacts", "Deals", "Calls", "Events", "Tasks",
    "Campaigns", "Products", "Quotes", "Sales_Orders", "Invoices",
]
BULK_UNSUPPORTED = {"Notes", "Attachments", "Emails", "Visits", "Actions_Performed"}
STAGE_HISTORY_FIELDS = ["Stage", "Amount", "Probability", "Duration_Days", "Modified_Time", "Closing_Date"]
NOTE_FIELDS = ["Note_Title", "Note_Content", "Parent_Id", "Created_Time", "Owner"]


def discover(client: ZohoClient, store: Store, log=print) -> pd.DataFrame:
    """Save org, modules, fields (+ picklists) and users. Returns the module overview."""
    org = client.org()
    store.write("meta_org", pd.DataFrame([{
        "company_name": org.get("company_name"), "currency": org.get("currency"),
        "country": org.get("country"), "time_zone": org.get("time_zone"),
        "edition": (org.get("license_details") or {}).get("paid_type"),
        "extracted_at": datetime.now(timezone.utc).isoformat(),
    }]))
    log(f"Org: {org.get('company_name')}")

    modules = client.modules()
    mod_rows = [{
        "api_name": m.get("api_name"), "label": m.get("plural_label") or m.get("module_name"),
        "generated_type": m.get("generated_type"), "api_supported": bool(m.get("api_supported")),
    } for m in modules]
    mod_df = pd.DataFrame(mod_rows)

    targets = select_modules(mod_df)
    field_rows, pick_rows = [], []
    counts = {}
    for name in targets:
        try:
            fields = client.fields(name)
        except ZohoError as e:
            log(f"  ! could not read fields for {name}: {e}")
            continue
        counts[name] = client.count(name)
        for f in fields:
            lookup = (f.get("lookup") or {}).get("module") or {}
            field_rows.append({
                "module": name, "api_name": f.get("api_name"), "label": f.get("field_label"),
                "data_type": f.get("data_type"), "json_type": f.get("json_type"),
                "custom": bool(f.get("custom_field")), "lookup_module": lookup.get("api_name"),
            })
            for p in f.get("pick_list_values") or []:
                pick_rows.append({
                    "module": name, "field": f.get("api_name"),
                    "display_value": p.get("display_value"), "actual_value": p.get("actual_value"),
                    "sequence": p.get("sequence_number"),
                    "forecast_type": p.get("forecast_type"), "forecast_category": _name(p.get("forecast_category")),
                    "probability": p.get("probability"),
                })
    mod_df["records"] = mod_df["api_name"].map(counts)
    mod_df["selected"] = mod_df["api_name"].isin(targets)
    store.write("meta_modules", mod_df)
    store.write("meta_fields", pd.DataFrame(field_rows))
    store.write("meta_picklist", pd.DataFrame(pick_rows))

    users = client.users()
    store.write("meta_users", pd.DataFrame([{
        "id": str(u.get("id")), "full_name": u.get("full_name"), "email": u.get("email"),
        "role": _name(u.get("role")), "profile": _name(u.get("profile")), "status": u.get("status"),
    } for u in users]))
    log(f"Discovered {len(targets)} modules, {len(field_rows)} fields, {len(users)} users")
    return mod_df[mod_df["selected"]]


def select_modules(mod_df: pd.DataFrame) -> list[str]:
    ok = mod_df[mod_df["api_supported"]]
    core = [m for m in CORE_MODULES if m in set(ok["api_name"])]
    custom = ok[(ok["generated_type"] == "custom") & ~ok["api_name"].isin(BULK_UNSUPPORTED)]["api_name"].tolist()
    return core + [c for c in custom if c not in core]


def extract(client: ZohoClient, store: Store, modules: list[str] | None = None,
            notes: bool = False, stage_history: bool = False, max_history: int = 3000, log=print) -> None:
    mod_df = store.read("meta_modules")
    if mod_df.empty:
        discover(client, store, log)
        mod_df = store.read("meta_modules")
    targets = modules or mod_df[mod_df["selected"]]["api_name"].tolist()

    log_rows = []
    for name in targets:
        t0 = time.time()
        try:
            df = client.bulk_read(name)
            store.write(f"raw_{name}", df)
            log(f"  {name}: {len(df):,} records, {df.shape[1]} fields ({time.time() - t0:.0f}s)")
            log_rows.append({"module": name, "rows": len(df), "columns": df.shape[1], "method": "bulk", "error": None})
        except ZohoError as e:
            log(f"  ! {name} failed: {e}")
            log_rows.append({"module": name, "rows": 0, "columns": 0, "method": "bulk", "error": str(e)[:300]})

    if notes:
        try:
            df = client.records("Notes", NOTE_FIELDS)
            store.write("raw_Notes", df)
            log(f"  Notes: {len(df):,} records")
            log_rows.append({"module": "Notes", "rows": len(df), "columns": df.shape[1], "method": "rest", "error": None})
        except ZohoError as e:
            log(f"  ! Notes failed: {e}")

    if stage_history and store.has("raw_Deals"):
        deals = store.read("raw_Deals")
        ids = deals["Id"].dropna().astype(str).tolist()[:max_history]
        log(f"  Stage history for {len(ids):,} deals (1 API call each)...")
        rows = []
        for i, deal_id in enumerate(ids, 1):
            try:
                for h in client.related("Deals", deal_id, "Stage_History", STAGE_HISTORY_FIELDS):
                    h = {k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in h.items()}
                    rows.append({"deal_id": deal_id, **h})
            except ZohoError as e:
                log(f"  ! stage history stopped at deal {i}: {e}")
                break
            if i % 250 == 0:
                log(f"    {i:,}/{len(ids):,}")
        store.write("raw_Stage_History", pd.DataFrame(rows).astype(str) if rows else pd.DataFrame())
        log_rows.append({"module": "Stage_History", "rows": len(rows), "columns": 0, "method": "rest", "error": None})

    log_df = pd.DataFrame(log_rows)
    log_df["extracted_at"] = datetime.now(timezone.utc).isoformat()
    store.write("meta_extract_log", log_df)


def _name(v):
    if isinstance(v, dict):
        return v.get("name") or v.get("display_value")
    return v
