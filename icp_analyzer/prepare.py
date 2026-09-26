"""Clean, type and join the raw CRM export into analysis-ready tables.

Outputs (all in the same DuckDB file):
  clean_accounts, clean_contacts, clean_deals, clean_leads, clean_activities,
  clean_stage_history, deal_wide (one row per deal with every attribute),
  feature_catalog (what every deal_wide column is), cleaning_log (every value we changed).
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

from .storage import Store

NUMERIC_TYPES = {"currency", "double", "integer", "bigint", "decimal", "percent", "long", "autonumber_numeric"}
DATE_TYPES = {"date", "datetime"}
ID_TYPES = {"lookup", "ownerlookup", "userlookup", "multiselectlookup", "multiuserlookup"}
TEXT_TYPES = {"text", "textarea", "email", "phone", "website", "autonumber", "profileimage", "fileupload", "imageupload"}
CATEGORY_TYPES = {"picklist", "multiselectpicklist", "boolean"}

LEGAL_SUFFIXES = r"\b(private|pvt|limited|ltd|llp|llc|inc|incorporated|corp|corporation|co|company|gmbh|plc|pte|sa|bv)\b"


# ---------------------------------------------------------------- helpers
def col(df: pd.DataFrame, *candidates: str) -> str | None:
    """First column that exists (case-insensitive)."""
    lower = {c.lower(): c for c in df.columns}
    for c in candidates:
        if c.lower() in lower:
            return lower[c.lower()]
    return None


def to_dt(s: pd.Series) -> pd.Series:
    out = pd.to_datetime(s, errors="coerce", utc=True, format="mixed")
    return out.dt.tz_convert(None)


def to_num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s.astype(str).str.replace(r"[^\d.\-eE]", "", regex=True).replace("", np.nan), errors="coerce")


def band(values: pd.Series, edges: list[float], labels: list[str]) -> pd.Series:
    return pd.cut(values, bins=edges, labels=labels, right=True).astype("object")


EMP_EDGES = [0, 10, 50, 200, 500, 1000, 5000, np.inf]
EMP_LABELS = ["1-10", "11-50", "51-200", "201-500", "501-1000", "1001-5000", "5000+"]


def nice_quartile_bands(values: pd.Series) -> pd.Series:
    """Split amounts into ~4 bands with rounded, human-readable edges."""
    v = values.dropna()
    if v.nunique() < 4:
        return pd.Series(np.nan, index=values.index, dtype="object")
    qs = v.quantile([0.25, 0.5, 0.75]).tolist()

    def nice(x):
        if x <= 0:
            return 0
        mag = 10 ** max(int(np.floor(np.log10(x))) - 1, 0)
        return round(x / mag) * mag

    edges = sorted(set([nice(q) for q in qs]))
    bins = [-np.inf] + edges + [np.inf]
    labels = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        if lo == -np.inf:
            labels.append(f"≤ {fmt_num(hi)}")
        elif hi == np.inf:
            labels.append(f"> {fmt_num(lo)}")
        else:
            labels.append(f"{fmt_num(lo)}–{fmt_num(hi)}")
    return pd.cut(values, bins=bins, labels=labels).astype("object")


def fmt_num(x: float) -> str:
    for div, suf in ((1e7, "Cr"), (1e5, "L"), (1e3, "K")):
        if abs(x) >= div:
            return f"{x / div:.3g}{suf}"
    return f"{x:.0f}"


class Cleaner:
    """Types columns from Zoho field metadata and normalises messy categorical values."""

    def __init__(self, store: Store):
        meta = store.read("meta_fields")
        self.types: dict[tuple[str, str], str] = {}
        self.labels: dict[tuple[str, str], str] = {}
        self.custom: dict[tuple[str, str], bool] = {}
        for r in meta.itertuples():
            self.types[(r.module, r.api_name)] = (r.data_type or "").lower()
            self.labels[(r.module, r.api_name)] = r.label or r.api_name
            self.custom[(r.module, r.api_name)] = bool(r.custom)
        self.log_rows: list[dict] = []

    def kind(self, module: str, field: str, s: pd.Series) -> str:
        t = self.types.get((module, field), "")
        if field == "Id" or t in ID_TYPES or field.endswith("_Id") or field.endswith(".id"):
            return "id"
        if t in NUMERIC_TYPES:
            return "numeric"
        if t in DATE_TYPES:
            return "date"
        if t in CATEGORY_TYPES:
            return "category"
        if t in TEXT_TYPES:
            return "text"
        # unknown type: infer from content
        v = s.dropna().astype(str)
        if v.empty:
            return "text"
        if to_num(v).notna().mean() > 0.95 and v.str.len().median() < 12:
            return "numeric"
        if v.str.match(r"^\d{4}-\d{2}-\d{2}").mean() > 0.95:
            return "date"
        return "category" if v.nunique() <= max(30, 0.05 * len(v)) else "text"

    def clean(self, module: str, df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, str]]:
        df = df.copy()
        df.columns = [c[:-3] if c.endswith(".id") else c for c in df.columns]
        kinds = {}
        for c in df.columns:
            k = self.kind(module, c, df[c])
            kinds[c] = k
            if k == "numeric":
                df[c] = to_num(df[c])
            elif k == "date":
                df[c] = to_dt(df[c])
            elif k == "id":
                df[c] = df[c].astype("string").str.strip().replace({"": pd.NA, "nan": pd.NA})
            elif k == "category":
                df[c] = self.normalise(module, c, df[c])
            else:
                df[c] = df[c].astype("string").str.strip().replace({"": pd.NA})
        return df, kinds

    def normalise(self, module: str, field: str, s: pd.Series) -> pd.Series:
        """Merge spelling/case/spacing variants of the same value; log every change."""
        raw = s.astype("string").str.strip().str.replace(r"\s+", " ", regex=True).replace({"": pd.NA, "-None-": pd.NA})
        key = raw.str.lower().str.replace(r"[^a-z0-9]", "", regex=True)
        counts = pd.DataFrame({"raw": raw, "key": key}).dropna().value_counts().reset_index(name="n")
        canonical = counts.sort_values("n", ascending=False).drop_duplicates("key").set_index("key")["raw"]
        out = key.map(canonical)
        orig = s.astype("string")
        changed = pd.DataFrame({"orig": orig, "new": out}).dropna()
        changed = changed[changed["orig"] != changed["new"]]
        for (o, n), cnt in changed.value_counts().items():
            self.log_rows.append({"module": module, "field": field, "original": o, "cleaned": n, "records": int(cnt)})
        return out.astype("object")


# ---------------------------------------------------------------- title → function / seniority
FUNCTION_RULES = [
    ("Founder / CEO", r"\b(founder|ceo|chief executive|owner|managing director|\bmd\b|proprietor|president)\b"),
    ("Sales", r"\b(sales|business development|\bbd\b|bdm|account executive|\bae\b|revenue|cro)\b"),
    ("Marketing", r"\b(marketing|growth|brand|demand gen|cmo|content|seo)\b"),
    ("Technology / IT", r"\b(cto|cio|it\b|technology|engineering|developer|software|tech|infrastructure|data)\b"),
    ("Operations", r"\b(operations|ops|coo|supply chain|logistics|admin)\b"),
    ("Finance", r"\b(finance|cfo|accounts|accounting|controller)\b"),
    ("HR / People", r"\b(hr|human resources|people|talent|recruit|chro)\b"),
    ("Product", r"\b(product|cpo)\b"),
    ("Customer Success / Support", r"\b(customer success|support|service|cx)\b"),
    ("Procurement", r"\b(procurement|purchase|purchasing|buyer|sourcing)\b"),
]
SENIORITY_RULES = [
    ("C-level / Founder", r"\b(founder|ceo|cto|cfo|coo|cmo|cio|cro|chro|cpo|chief|owner|president|managing director|\bmd\b)\b"),
    ("VP / Head", r"\b(vp|vice president|head|svp|evp)\b"),
    ("Director", r"\b(director|gm|general manager)\b"),
    ("Manager / Lead", r"\b(manager|lead|supervisor)\b"),
    ("Intern / Trainee", r"\b(intern|trainee|student|apprentice)\b"),
    ("Individual contributor", r"\b(executive|associate|specialist|analyst|engineer|representative|officer|coordinator|consultant)\b"),
]


def classify_title(title) -> tuple[str, str]:
    if not isinstance(title, str) or not title.strip():
        return "Unknown", "Unknown"
    t = title.lower()
    func = next((name for name, rx in FUNCTION_RULES if re.search(rx, t)), "Other")
    sen = next((name for name, rx in SENIORITY_RULES if re.search(rx, t)), "Other")
    return func, sen


# ---------------------------------------------------------------- outcome
def stage_outcomes(store: Store, stages: pd.Series) -> dict[str, str]:
    pick = store.read("meta_picklist")
    mapping: dict[str, str] = {}
    if not pick.empty:
        st = pick[(pick["module"] == "Deals") & (pick["field"] == "Stage")]
        for r in st.itertuples():
            ft = str(r.forecast_type or r.forecast_category or "").lower()
            val = r.display_value
            if "won" in ft or ft == "closed":
                mapping[val] = "Won"
            elif "lost" in ft or "omitted" in ft:
                mapping[val] = "Lost"
            elif ft:
                mapping[val] = "Open"
            elif pd.notna(r.probability):
                p = float(r.probability)
                mapping[val] = "Won" if p >= 100 else ("Lost" if p <= 0 else "Open")
    for s in stages.dropna().unique():  # fallback by name
        if s not in mapping:
            low = s.lower()
            mapping[s] = "Won" if "won" in low else ("Lost" if "lost" in low or "dead" in low or "closed" in low else "Open")
    return mapping


# ---------------------------------------------------------------- main
def prepare(store: Store, log=print) -> None:
    cl = Cleaner(store)
    users = store.read("meta_users")
    user_names = dict(zip(users["id"].astype(str), users["full_name"])) if not users.empty else {}
    catalog: list[dict] = []

    def load(module):
        df = store.read(f"raw_{module}")
        if df.empty:
            return df, {}
        df, kinds = cl.clean(module, df)
        if "Owner" in df.columns:
            df["Owner_Name"] = df["Owner"].map(user_names).fillna(df["Owner"])
            kinds["Owner_Name"] = "category"
        return df, kinds

    # ----- accounts
    acc, acc_kinds = load("Accounts")
    if not acc.empty:
        name_c = col(acc, "Account_Name")
        acc["name_key"] = (acc[name_c].astype(str).str.lower().str.replace(LEGAL_SUFFIXES, "", regex=True)
                           .str.replace(r"[^a-z0-9]", "", regex=True)) if name_c else pd.NA
        web_c = col(acc, "Website")
        acc["domain"] = (acc[web_c].astype("string").str.lower().str.replace(r"^(https?://)?(www\.)?", "", regex=True)
                         .str.split("/").str[0]) if web_c else pd.NA
        acc["is_duplicate"] = acc.duplicated("name_key", keep="first") & acc["name_key"].ne("")
        emp_c = col(acc, "Employees", "No_of_Employees")
        acc["employee_band"] = band(acc[emp_c], EMP_EDGES, EMP_LABELS) if emp_c else np.nan
        acc_kinds.update(employee_band="category")
    store.write("clean_accounts", acc)

    # ----- contacts
    con, con_kinds = load("Contacts")
    if not con.empty:
        title_c = col(con, "Title", "Designation", "Job_Title")
        fs = con[title_c].map(classify_title) if title_c else pd.Series([("Unknown", "Unknown")] * len(con))
        con["function"] = [f for f, _ in fs]
        con["seniority"] = [s for _, s in fs]
    store.write("clean_contacts", con)

    # ----- activities (calls, meetings, tasks) — one table
    acts = []
    for module, typ, when_cands in (("Calls", "Call", ("Call_Start_Time", "Created_Time")),
                                    ("Events", "Meeting", ("Start_DateTime", "Created_Time")),
                                    ("Tasks", "Task", ("Due_Date", "Closed_Time", "Created_Time"))):
        df, _ = load(module)
        if df.empty:
            continue
        when_c = col(df, *when_cands)
        acts.append(pd.DataFrame({
            "activity_id": df[col(df, "Id")],
            "type": typ,
            "when": df[when_c] if when_c else pd.NaT,
            "related_id": df[col(df, "What_Id")] if col(df, "What_Id") else pd.NA,
            "related_module": df[col(df, "$se_module", "se_module")] if col(df, "$se_module", "se_module") else pd.NA,
            "contact_id": df[col(df, "Who_Id")] if col(df, "Who_Id") else pd.NA,
            "owner": df["Owner_Name"] if "Owner_Name" in df else pd.NA,
        }))
    activities = pd.concat(acts, ignore_index=True) if acts else pd.DataFrame(
        columns=["activity_id", "type", "when", "related_id", "related_module", "contact_id", "owner"])
    store.write("clean_activities", activities)

    # ----- deals
    deals, deal_kinds = load("Deals")
    if deals.empty:
        log("No deals found — skipping deal analysis tables.")
        store.write("cleaning_log", pd.DataFrame(cl.log_rows))
        return
    stage_c = col(deals, "Stage")
    outcome_map = stage_outcomes(store, deals[stage_c])
    deals["outcome"] = deals[stage_c].map(outcome_map).fillna("Open")
    deals["is_won"] = (deals["outcome"] == "Won").astype(int)
    created_c, close_c = col(deals, "Created_Time"), col(deals, "Closing_Date")
    amount_c = col(deals, "Amount")
    deals["created"] = deals[created_c]
    deals["closed_on"] = deals[close_c] if close_c else pd.NaT
    closed = deals["outcome"] != "Open"
    deals["cycle_days"] = np.where(closed, (deals["closed_on"] - deals["created"]).dt.days.clip(lower=0), np.nan)
    deals["age_days"] = (pd.Timestamp.now() - deals["created"]).dt.days
    if amount_c:
        deals = deals.rename(columns={amount_c: "amount"})
    else:
        deals["amount"] = np.nan
    deals["amount_band"] = nice_quartile_bands(deals["amount"])
    deals["created_quarter"] = deals["created"].dt.to_period("Q").astype(str).replace("NaT", pd.NA)
    deals["created_month"] = deals["created"].dt.to_period("M").astype(str).replace("NaT", pd.NA)

    # activities per deal, counting only activities up to the close date (no leakage from post-sale work)
    deal_acts = activities[activities["related_id"].isin(deals["Id"])].merge(
        deals[["Id", "created", "closed_on", "outcome"]], left_on="related_id", right_on="Id", how="left")
    before = deal_acts["outcome"].eq("Open") | deal_acts["when"].isna() | (deal_acts["when"] <= deal_acts["closed_on"] + pd.Timedelta(days=1))
    excluded_after_close = int((~before).sum())
    deal_acts = deal_acts[before]
    agg = deal_acts.pivot_table(index="related_id", columns="type", values="activity_id", aggfunc="count", fill_value=0)
    agg.columns = [f"n_{c.lower()}s" for c in agg.columns]
    agg["n_activities"] = agg.sum(axis=1)
    first = deal_acts.groupby("related_id")["when"].min()
    deals = deals.merge(agg, left_on="Id", right_index=True, how="left")
    for c in ("n_calls", "n_meetings", "n_tasks", "n_activities"):
        if c not in deals:
            deals[c] = 0
        deals[c] = deals[c].fillna(0)
    deals["days_to_first_activity"] = (deals["Id"].map(first) - deals["created"]).dt.days.clip(lower=0)
    deals["activities_per_week"] = deals["n_activities"] / (deals["cycle_days"].fillna(deals["age_days"]).clip(lower=7) / 7)

    # stage history: furthest stage reached and the stage a lost deal died at
    hist = store.read("raw_Stage_History")
    if not hist.empty:
        hist["Modified_Time"] = to_dt(hist["Modified_Time"]) if "Modified_Time" in hist else pd.NaT
        hist["Duration_Days"] = to_num(hist["Duration_Days"]) if "Duration_Days" in hist else np.nan
        hist["outcome"] = hist["Stage"].map(outcome_map).fillna("Open")
        store.write("clean_stage_history", hist)
        open_h = hist[hist["outcome"] == "Open"].sort_values("Modified_Time")
        deals["last_open_stage"] = deals["Id"].map(open_h.groupby("deal_id")["Stage"].last())

    store.write("clean_deals", deals)

    # ----- leads
    leads, _ = load("Leads")
    if not leads.empty:
        conv_c = col(leads, "Converted__s", "$converted", "Converted")
        status_c = col(leads, "Lead_Status")
        conv = leads[conv_c].astype(str).str.lower().isin(["true", "1", "yes"]) if conv_c else pd.Series(False, index=leads.index)
        if status_c:
            conv |= leads[status_c].astype(str).str.lower().eq("converted")
        leads["converted"] = conv.astype(int)
        emp_c = col(leads, "No_of_Employees", "Employees")
        leads["employee_band"] = band(leads[emp_c], EMP_EDGES, EMP_LABELS) if emp_c else np.nan
        title_c = col(leads, "Designation", "Title")
        if title_c:
            fs = leads[title_c].map(classify_title)
            leads["function"], leads["seniority"] = [f for f, _ in fs], [s for _, s in fs]
    store.write("clean_leads", leads)

    # ----- deal_wide: one row per deal, every attribute we know, with a catalog describing each column
    wide = pd.DataFrame({"deal_id": deals["Id"], "outcome": deals["outcome"], "is_won": deals["is_won"],
                         "amount": deals["amount"], "cycle_days": deals["cycle_days"],
                         "created": deals["created"], "closed_on": deals["closed_on"]})

    def add(name, series, source, kind, label, custom=False, module=None, field=None):
        wide[name] = series.values
        catalog.append({"feature": name, "source": source, "kind": kind, "label": label, "custom": custom,
                        "module": module, "field": field})

    skip_deal = {"Id", stage_c, "outcome", "is_won", "created", "closed_on", "amount", "cycle_days", "Owner",
                 "Probability", "Expected_Revenue", "Deal_Name", "Modified_Time", "Last_Activity_Time"}
    derived = {"amount_band", "created_quarter", "created_month", "age_days", "n_calls", "n_meetings", "n_tasks",
               "n_activities", "days_to_first_activity", "activities_per_week", "last_open_stage"}
    for c in deals.columns:
        if c in skip_deal or c in derived:
            continue
        k = deal_kinds.get(c, "text")
        if k in ("category", "numeric", "date", "text"):
            add(f"deal.{c}", deals[c], "Deal", k, cl.labels.get(("Deals", c), c).replace("_", " "),
                cl.custom.get(("Deals", c), False), "Deals", c)

    acc_c = col(deals, "Account_Name")
    if acc_c and not acc.empty:
        acc_idx = acc.set_index("Id")
        emp_raw = col(acc, "Employees", "No_of_Employees")
        skip_acc = {"Id", "name_key", "is_duplicate", "Owner", "Owner_Name", emp_raw}  # raw headcount duplicates the size band
        nice = {"employee_band": "Company size", "domain": "Domain"}
        for c in acc.columns:
            if c in skip_acc or c.endswith("_Time"):
                continue
            k = acc_kinds.get(c, "text")
            if k in ("category", "numeric", "text"):
                label = nice.get(c) or cl.labels.get(("Accounts", c), c).replace("_", " ")
                add(f"account.{c}", deals[acc_c].map(acc_idx[c]), "Account", k, "Account · " + label,
                    cl.custom.get(("Accounts", c), False), "Accounts", c)

    ct_c = col(deals, "Contact_Name")
    if ct_c and not con.empty:
        con_idx = con.set_index("Id")
        for c, label in (("function", "Contact · Function"), ("seniority", "Contact · Seniority")):
            add(f"contact.{c}", deals[ct_c].map(con_idx[c]), "Contact", "category", label)
        title_c = col(con, "Title", "Designation")
        if title_c:
            add("contact.title", deals[ct_c].map(con_idx[title_c]), "Contact", "text", "Contact · Title")

    # source "Deal" = who/what the deal is; source "Activity" = how it was sold (process, not ICP)
    for c, label, kind, source in (
            ("amount_band", "Deal size band", "category", "Deal"),
            ("created_quarter", "Created quarter", "category", "Deal"),
            ("n_calls", "Calls (before close)", "numeric", "Activity"),
            ("n_meetings", "Meetings (before close)", "numeric", "Activity"),
            ("n_tasks", "Tasks (before close)", "numeric", "Activity"),
            ("n_activities", "All activities (before close)", "numeric", "Activity"),
            ("days_to_first_activity", "Days to first activity", "numeric", "Activity"),
            ("activities_per_week", "Activities per week", "numeric", "Activity")):
        if c in deals:
            add(f"derived.{c}", deals[c], source, kind, label)

    store.write("deal_wide", wide)
    store.write("feature_catalog", pd.DataFrame(catalog))
    store.write("cleaning_log", pd.DataFrame(cl.log_rows, columns=["module", "field", "original", "cleaned", "records"]))
    store.write("prepare_info", pd.DataFrame([{"activities_excluded_after_close": excluded_after_close,
                                               "deals": len(deals), "closed_deals": int(closed.sum())}]))
    log(f"Prepared: {len(deals):,} deals ({int(closed.sum()):,} closed), {len(catalog)} candidate signals, "
        f"{len(cl.log_rows)} value fixes, {excluded_after_close} post-close activities excluded")
