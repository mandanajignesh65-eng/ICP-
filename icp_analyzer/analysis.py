"""All non-signal analyses: data health, revenue, pipeline, losses, leads, activities, roles, trends, ICP draft.

Every function takes DataFrames and returns DataFrames/dicts, so the dashboard
(or a report, or an API later) can render them.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .stats import rate_table

KEY_FIELDS = [  # (module, candidate columns, why it matters)
    ("Accounts", ["Industry"], "Core ICP dimension"),
    ("Accounts", ["Employees", "No_of_Employees"], "Company size"),
    ("Accounts", ["Billing_Country", "Country"], "Geography"),
    ("Accounts", ["Annual_Revenue"], "Company revenue"),
    ("Accounts", ["Website"], "Needed for enrichment"),
    ("Contacts", ["Title", "Designation"], "Buyer personas"),
    ("Contacts", ["Email"], "Reachability"),
    ("Deals", ["Amount"], "Deal economics"),
    ("Deals", ["Lead_Source"], "Channel analysis"),
    ("Deals", ["Closing_Date"], "Sales cycle"),
    ("Deals", ["Contact_Name"], "Buyer on the deal"),
    ("Deals", ["Account_Name"], "Company on the deal"),
    ("Deals", ["Reason_For_Loss__s", "Loss_Reason", "Reason_for_Loss"], "Why deals are lost"),
    ("Leads", ["Lead_Source"], "Lead channel"),
    ("Leads", ["Industry"], "Lead ICP fit"),
]


# ------------------------------------------------------------------ data health
def field_health(raw: dict[str, pd.DataFrame], meta_fields: pd.DataFrame) -> pd.DataFrame:
    rows = []
    labels = {(r.module, r.api_name): (r.label, r.data_type, r.custom) for r in meta_fields.itertuples()} if not meta_fields.empty else {}
    for module, df in raw.items():
        n = len(df)
        for c in df.columns:
            s = df[c].replace("", np.nan)
            filled = s.notna().sum()
            vc = s.value_counts()
            label, dtype, custom = labels.get((module, c), (c, None, None))
            rows.append({"module": module, "field": c, "label": label, "type": dtype, "custom": custom,
                         "filled_pct": filled / n if n else 0, "filled": int(filled), "records": n,
                         "distinct": int(s.nunique()), "top_value": vc.index[0] if len(vc) else None,
                         "top_share": vc.iloc[0] / filled if filled else np.nan})
    return pd.DataFrame(rows)


def key_field_health(fh: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for module, cands, why in KEY_FIELDS:
        m = fh[(fh["module"] == module) & fh["field"].str.lower().isin([c.lower() for c in cands])]
        if m.empty:
            rows.append({"module": module, "field": cands[0], "why": why, "filled_pct": np.nan, "status": "Not in CRM"})
            continue
        r = m.sort_values("filled_pct", ascending=False).iloc[0]
        pct = r["filled_pct"]
        status = "Good" if pct >= 0.8 else ("Usable" if pct >= 0.5 else ("Weak" if pct >= 0.2 else "Unusable"))
        rows.append({"module": module, "field": r["field"], "why": why, "filled_pct": pct, "status": status})
    return pd.DataFrame(rows)


def health_summary(accounts, contacts, deals, leads, key_fields: pd.DataFrame) -> dict:
    out = {}
    out["duplicate_accounts"] = int(accounts["is_duplicate"].sum()) if "is_duplicate" in accounts else 0
    email = next((c for c in ("Email",) if c in contacts), None)
    out["duplicate_contact_emails"] = int(contacts[email].dropna().str.lower().duplicated().sum()) if email else 0
    lemail = "Email" if "Email" in leads else None
    out["duplicate_lead_emails"] = int(leads[lemail].dropna().str.lower().duplicated().sum()) if lemail else 0
    if not deals.empty:
        open_d = deals[deals["outcome"] == "Open"]
        now = pd.Timestamp.now()
        out["open_deals"] = len(open_d)
        out["stale_open_deals"] = int(((open_d["closed_on"] < now - pd.Timedelta(days=30)) | (open_d["age_days"] > 365)).sum())
        lost = deals[deals["outcome"] == "Lost"]
        reason = next((c for c in ("Reason_For_Loss__s", "Loss_Reason", "Reason_for_Loss") if c in deals), None)
        out["lost_without_reason_pct"] = float(lost[reason].isna().mean()) if reason and len(lost) else np.nan
        out["deals_without_amount_pct"] = float(deals["amount"].isna().mean())
        acc = next((c for c in ("Account_Name",) if c in deals), None)
        out["deals_without_account_pct"] = float(deals[acc].isna().mean()) if acc else np.nan
    kf = key_fields["filled_pct"].fillna(0)
    completeness = kf.mean() if len(kf) else 0
    penalty = min(0.2, out.get("duplicate_accounts", 0) / max(len(accounts), 1)) + \
        min(0.15, out.get("stale_open_deals", 0) / max(out.get("open_deals", 1), 1) * 0.15)
    out["health_score"] = round(max(0, completeness - penalty) * 100)
    return out


# ------------------------------------------------------------------ revenue & cycle
def revenue_overview(deals: pd.DataFrame) -> dict:
    won = deals[deals["outcome"] == "Won"]
    lost = deals[deals["outcome"] == "Lost"]
    closed = len(won) + len(lost)
    return {
        "deals": len(deals), "closed": closed, "won": len(won), "lost": len(lost),
        "open": int((deals["outcome"] == "Open").sum()),
        "win_rate": len(won) / closed if closed else np.nan,
        "won_revenue": won["amount"].sum(),
        "avg_won_deal": won["amount"].mean(), "median_won_deal": won["amount"].median(),
        "median_cycle_won": won["cycle_days"].median(), "median_cycle_lost": lost["cycle_days"].median(),
        "open_pipeline": deals.loc[deals["outcome"] == "Open", "amount"].sum(),
    }


def revenue_concentration(deals: pd.DataFrame, accounts: pd.DataFrame) -> pd.DataFrame:
    won = deals[deals["outcome"] == "Won"]
    acc_c = "Account_Name" if "Account_Name" in won else None
    if not acc_c or won.empty:
        return pd.DataFrame()
    by = won.groupby(acc_c)["amount"].sum().sort_values(ascending=False).reset_index()
    names = accounts.set_index("Id")["Account_Name"] if "Account_Name" in accounts else pd.Series(dtype=str)
    by["account"] = by[acc_c].map(names).fillna(by[acc_c])
    by["cum_share"] = by["amount"].cumsum() / by["amount"].sum()
    by["account_pct"] = np.arange(1, len(by) + 1) / len(by)
    return by


def segment_value(wide: pd.DataFrame, feature: str) -> pd.DataFrame:
    """Per segment: deals, win rate, avg won deal, revenue, cycle — i.e. where the money is."""
    closed = wide[wide["outcome"].isin(["Won", "Lost"])]
    g = closed[feature].astype("object").fillna("(blank)").astype(str)
    t = rate_table(g, closed["is_won"])
    won = closed[closed["is_won"] == 1]
    wg = won[feature].astype("object").fillna("(blank)").astype(str)
    t["avg_won_deal"] = t["value"].map(won.groupby(wg)["amount"].mean())
    t["won_revenue"] = t["value"].map(won.groupby(wg)["amount"].sum()).fillna(0)
    t["median_cycle_won"] = t["value"].map(won.groupby(wg)["cycle_days"].median())
    t["revenue_share"] = t["won_revenue"] / t["won_revenue"].sum() if t["won_revenue"].sum() else np.nan
    t["expected_value_per_deal"] = t["rate"] * t["avg_won_deal"].fillna(0)
    return t


# ------------------------------------------------------------------ pipeline & losses
def open_pipeline(deals: pd.DataFrame, stage_order: list[str]) -> pd.DataFrame:
    o = deals[deals["outcome"] == "Open"]
    if o.empty:
        return pd.DataFrame()
    t = o.groupby("Stage").agg(deals=("Id", "count"), amount=("amount", "sum"), median_age=("age_days", "median")).reset_index()
    t["order"] = t["Stage"].map({s: i for i, s in enumerate(stage_order)}).fillna(99)
    return t.sort_values("order").drop(columns="order")


def pipeline_forecast(deals: pd.DataFrame, history: pd.DataFrame, picklist: pd.DataFrame, stage_order: list[str]) -> dict:
    """Open pipeline by stage, weighted two ways:
    - Zoho's probability: the % the sales team set for each stage in Zoho settings
    - Actual history: of past closed deals that reached this stage, the share that was won
    Also flags stale deals (close date passed or open for over a year)."""
    now = pd.Timestamp.now()
    o = deals[deals["outcome"] == "Open"].copy()
    if o.empty:
        return {}
    st = picklist[(picklist["module"] == "Deals") & (picklist["field"] == "Stage")] if not picklist.empty else pd.DataFrame()
    prob = dict(zip(st["display_value"], pd.to_numeric(st["probability"], errors="coerce") / 100)) if not st.empty else {}
    hist_rate, hist_n = {}, {}
    if not history.empty:
        closed = deals[deals["outcome"].isin(["Won", "Lost"])][["Id", "is_won"]]
        h = history.merge(closed, left_on="deal_id", right_on="Id").drop_duplicates(["deal_id", "Stage"])
        grp = h.groupby("Stage")["is_won"]
        hist_rate, hist_n = grp.mean().to_dict(), grp.size().to_dict()
    o["stale"] = (o["closed_on"] < now) | (o["age_days"] > 365)
    t = o.groupby("Stage").agg(deals=("Id", "count"), amount=("amount", "sum"), stale=("stale", "sum"),
                               no_amount=("amount", lambda s: int((~(s > 0)).sum())),
                               median_age=("age_days", "median")).reset_index()
    t["zoho_prob"] = t["Stage"].map(prob)
    t["actual_rate"] = t["Stage"].map(hist_rate)
    t["history_n"] = t["Stage"].map(hist_n)
    t["zoho_weighted"] = t["amount"] * t["zoho_prob"].fillna(0)
    t["actual_weighted"] = t["amount"] * t["actual_rate"].fillna(0)
    t["order"] = t["Stage"].map({s: i for i, s in enumerate(stage_order)}).fillna(99)
    t = t.sort_values("order").drop(columns="order")
    fresh = o[~o["stale"]]
    top = o.sort_values("amount", ascending=False).head(10)
    return {"stages": t, "total": o["amount"].sum(), "zoho": t["zoho_weighted"].sum(), "actual": t["actual_weighted"].sum(),
            "stale_n": int(o["stale"].sum()), "stale_amount": o.loc[o["stale"], "amount"].sum(),
            "fresh_n": len(fresh), "fresh_amount": fresh["amount"].sum(),
            "fresh_actual": (fresh["amount"] * fresh["Stage"].map(hist_rate).fillna(0)).sum(),
            "top": top, "top10_share": top["amount"].sum() / o["amount"].sum() if o["amount"].sum() else np.nan}


def stage_funnel(history: pd.DataFrame, deals: pd.DataFrame, stage_order: list[str]) -> pd.DataFrame:
    """How many closed deals reached each stage, and the win rate of those that did."""
    if history.empty:
        return pd.DataFrame()
    closed = deals[deals["outcome"].isin(["Won", "Lost"])][["Id", "is_won"]]
    h = history.merge(closed, left_on="deal_id", right_on="Id")
    rows = []
    open_stages = [s for s in stage_order if s in set(history["Stage"]) and s in set(h.loc[h["outcome"] == "Open", "Stage"])]
    for s in open_stages:
        ids = h.loc[h["Stage"] == s, "deal_id"].unique()
        sub = closed[closed["Id"].isin(ids)]
        dur = h.loc[h["Stage"] == s].groupby("is_won")["Duration_Days"].median()
        rows.append({"stage": s, "deals_reached": len(sub), "reach_pct": len(sub) / len(closed) if len(closed) else np.nan,
                     "win_rate_after": sub["is_won"].mean() if len(sub) else np.nan,
                     "median_days_won": dur.get(1, np.nan), "median_days_lost": dur.get(0, np.nan)})
    return pd.DataFrame(rows)


def loss_analysis(deals: pd.DataFrame) -> dict:
    lost = deals[deals["outcome"] == "Lost"]
    reason = next((c for c in ("Reason_For_Loss__s", "Loss_Reason", "Reason_for_Loss") if c in deals), None)
    out = {"lost": len(lost)}
    if reason:
        out["reasons"] = lost[reason].fillna("(no reason given)").value_counts().rename_axis("reason").reset_index(name="deals")
        if "last_open_stage" in lost:
            out["reason_by_stage"] = pd.crosstab(lost["last_open_stage"].fillna("(unknown)"), lost[reason].fillna("(no reason)"))
    if "last_open_stage" in lost:
        out["died_at"] = lost["last_open_stage"].fillna("(unknown)").value_counts().rename_axis("stage").reset_index(name="deals")
    comp = next((c for c in deals.columns if "competitor" in c.lower()), None)
    if comp:
        closed = deals[deals["outcome"].isin(["Won", "Lost"])]
        out["competitors"] = rate_table(closed[comp].fillna("(none recorded)"), closed["is_won"])
    return out


# ------------------------------------------------------------------ leads
def lead_funnel(leads: pd.DataFrame, feature: str) -> pd.DataFrame:
    if leads.empty or feature not in leads:
        return pd.DataFrame()
    return rate_table(leads[feature], leads["converted"])


def source_to_revenue(leads: pd.DataFrame, deals: pd.DataFrame) -> pd.DataFrame:
    """Lead source: lead volume -> conversion -> deals -> win rate -> revenue."""
    src_l = "Lead_Source" if "Lead_Source" in leads else None
    src_d = "Lead_Source" if "Lead_Source" in deals else None
    if not src_d:
        return pd.DataFrame()
    closed = deals[deals["outcome"].isin(["Won", "Lost"])]
    t = closed.groupby(closed[src_d].fillna("(blank)")).agg(
        deals=("Id", "count"), won=("is_won", "sum"), revenue=("amount", lambda s: s[closed.loc[s.index, "is_won"] == 1].sum()))
    t["win_rate"] = t["won"] / t["deals"]
    t["avg_won_deal"] = t["revenue"] / t["won"].replace(0, np.nan)
    if src_l:
        lv = leads.groupby(leads[src_l].fillna("(blank)")).agg(leads=("Id", "count"), converted=("converted", "sum"))
        lv["lead_conversion"] = lv["converted"] / lv["leads"]
        t = t.join(lv, how="outer")
    return t.reset_index().rename(columns={"index": "source", src_d: "source"}).sort_values("revenue", ascending=False)


# ------------------------------------------------------------------ activities
ACT_BUCKETS = {"n_meetings": ([-1, 0, 1, 2, 4, np.inf], ["0", "1", "2", "3-4", "5+"]),
               "n_calls": ([-1, 0, 2, 5, 10, np.inf], ["0", "1-2", "3-5", "6-10", "11+"]),
               "n_activities": ([-1, 0, 3, 7, 15, np.inf], ["0", "1-3", "4-7", "8-15", "16+"]),
               "days_to_first_activity": ([-1, 0, 2, 7, 14, np.inf], ["Same day", "1-2 days", "3-7 days", "8-14 days", "15+ days"])}


def activity_buckets(deals: pd.DataFrame, metric: str) -> pd.DataFrame:
    closed = deals[deals["outcome"].isin(["Won", "Lost"])]
    if metric not in closed:
        return pd.DataFrame()
    edges, labels = ACT_BUCKETS[metric]
    b = pd.cut(closed[metric], bins=edges, labels=labels).astype("object")
    t = rate_table(b, closed["is_won"])
    t["order"] = t["value"].map({l: i for i, l in enumerate(labels)}).fillna(99)
    return t.sort_values("order").drop(columns="order")


def activity_compare(deals: pd.DataFrame) -> pd.DataFrame:
    closed = deals[deals["outcome"].isin(["Won", "Lost"])]
    cols = [c for c in ("n_calls", "n_meetings", "n_tasks", "n_activities", "days_to_first_activity", "cycle_days") if c in closed]
    t = closed.groupby("outcome")[cols].median().T
    t.index = [c.replace("n_", "").replace("_", " ").capitalize() for c in t.index]
    return t


# ------------------------------------------------------------------ buyer roles
def role_table(wide: pd.DataFrame, feature: str) -> pd.DataFrame:
    closed = wide[wide["outcome"].isin(["Won", "Lost"])]
    if feature not in closed:
        return pd.DataFrame()
    return rate_table(closed[feature], closed["is_won"])


# ------------------------------------------------------------------ trends
def monthly_trend(deals: pd.DataFrame) -> pd.DataFrame:
    created = deals.groupby(deals["created"].dt.to_period("M")).size().rename("created")
    won = deals[deals["outcome"] == "Won"]
    won_m = won.groupby(won["closed_on"].dt.to_period("M")).agg(won=("Id", "count"), won_revenue=("amount", "sum"))
    t = pd.concat([created, won_m], axis=1).fillna(0)
    t.index = t.index.astype(str)
    return t.reset_index(names="month")


def cohort_win_rate(deals: pd.DataFrame) -> pd.DataFrame:
    closed = deals[deals["outcome"].isin(["Won", "Lost"])]
    t = rate_table(closed["created_quarter"], closed["is_won"])
    return t.sort_values("value")


# ------------------------------------------------------------------ plain-English findings & ICP draft
def pct(x) -> str:
    return "—" if pd.isna(x) else f"{x:.0%}"


def top_moves(sig: dict, sources=("Account", "Contact", "Deal"), limit: int = 10, per_field: int = 2,
              min_conf=("High", "Medium")) -> pd.DataFrame:
    """Values that move the win rate most (non-leaky fields, confident, biggest gap from average first)."""
    f, v, base = sig["fields"], sig["values"], sig["base_rate"]
    if f.empty or v.empty:
        return pd.DataFrame()
    good = f[f["strength"].isin(["Strong", "Moderate", "Weak"]) & f["source"].isin(sources)]["feature"]
    rows = v[v["feature"].isin(good) & v["confidence"].isin(min_conf) & v["direction"].isin(["Better", "Worse"])
             & ~v["value"].isin(["(blank)", "Other (rare values)", "Filled"])].copy()
    rows["gap"] = (rows["rate"] - base).abs()
    rows = rows.sort_values("gap", ascending=False).groupby("feature").head(per_field)
    return rows.head(limit)


def findings(sig: dict, sources=("Account", "Contact", "Deal"), limit: int = 8, min_conf=("High", "Medium")) -> list[str]:
    """Top plain-English findings (HTML), one per field."""
    base = sig["base_rate"]
    rows = top_moves(sig, sources, limit, per_field=1, min_conf=min_conf)
    out = []
    for r in rows.itertuples():
        up = r.rate > base
        icon = "▲" if up else "▼"
        color = "#2E9D6A" if up else "#D1495B"
        out.append(f"<span style='color:{color}'>{icon}</span> <b>{r.label}: {r.value}</b> — "
                   f"<b style='color:{color}'>{pct(r.rate)}</b> win rate vs {pct(base)} average "
                   f"<span style='opacity:.7'>({r.lift:.1f}×, {r.n} deals, {r.confidence.lower()} confidence)</span>")
    return out


def icp_draft(sig: dict, include_sources=("Account", "Contact", "Deal")) -> pd.DataFrame:
    """Values that are confidently better (include) or worse (avoid) than average, per ICP field."""
    f, v, base = sig["fields"], sig["values"], sig["base_rate"]
    if f.empty or v.empty:
        return pd.DataFrame()
    ok = f[f["strength"].isin(["Strong", "Moderate", "Weak"]) & f["source"].isin(include_sources)]
    rows = v[v["feature"].isin(ok["feature"]) & v["confidence"].isin(["High", "Medium"])
             & v["direction"].isin(["Better", "Worse"]) & ~v["value"].isin(["(blank)", "Other (rare values)", "Filled"])]
    out = rows.assign(verdict=np.where(rows["direction"] == "Better", "✅ Target", "⛔ Avoid / deprioritise"))
    out = out.merge(ok[["feature", "strength"]], on="feature")
    return out[["label", "value", "verdict", "rate", "lift", "n", "share_of_wins", "confidence", "strength"]] \
        .sort_values(["verdict", "lift"], ascending=[False, False]).reset_index(drop=True)
