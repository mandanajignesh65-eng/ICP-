"""Package everything for sharing: an Excel workbook of the analysis, every raw Zoho table and every cleaned
table as CSV, and a README — zipped into one file.

The analysis uses the same defaults as the dashboard: Junk deals left out, deals marked as existing-client
business left out (deals with no type are kept).
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

import pandas as pd

from . import analysis as A
from . import insights as IN
from .signals import scan
from .storage import Store

EXISTING_RX = r"exist|upsell|up-sell|renew|expan|cross|add-on|addon"
JUNK_RX = r"junk|spam|duplicate|test"


def default_filter(deals: pd.DataFrame) -> pd.Series:
    keep = ~deals["Stage"].fillna("").str.contains(JUNK_RX, case=False) if "Stage" in deals else pd.Series(True, index=deals.index)
    if "Type" in deals:
        keep &= ~deals["Type"].fillna("").astype(str).str.contains(EXISTING_RX, case=False)
    return keep


def _strip(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html)


def build_workbook(store: Store, path: Path, log=print) -> None:
    deals_all = store.read("clean_deals")
    wide_all = store.read("deal_wide")
    catalog = store.read("feature_catalog")
    accounts = store.read("clean_accounts")
    leads = store.read("clean_leads")
    org = store.read("meta_org").iloc[0].to_dict() if store.has("meta_org") else {}
    deals = deals_all[default_filter(deals_all)]
    wide = wide_all[wide_all["deal_id"].isin(deals["Id"])]
    sig = scan(wide, catalog, min_n=10)
    base = sig["base_rate"]
    answers = IN.all_answers(sig, wide, 10)

    def money(x):
        return "" if pd.isna(x) else f"₹{x / 1e5:,.1f} L" if x < 1e7 else f"₹{x / 1e7:,.2f} Cr"

    concl = IN.conclusions(answers, base, money)
    ov = A.revenue_overview(deals)
    stage_order = []
    pick = store.read("meta_picklist")
    if not pick.empty:
        stage_order = pick.query("module == 'Deals' and field == 'Stage'").sort_values("sequence")["display_value"].tolist()
    fc = A.pipeline_forecast(deals, store.read("clean_stage_history"), pick, stage_order)
    acc_name = accounts.set_index("Id")["Account_Name"] if "Account_Name" in accounts else pd.Series(dtype=str)
    acc_ind = accounts.set_index("Id")["Industry"] if "Industry" in accounts else pd.Series(dtype=str)

    with pd.ExcelWriter(path, engine="xlsxwriter") as xw:
        wb = xw.book
        h1 = wb.add_format({"bold": True, "font_size": 16})
        h2 = wb.add_format({"bold": True, "font_size": 12, "font_color": "#0071E3"})
        wrap = wb.add_format({"text_wrap": True, "valign": "top"})
        pctf = wb.add_format({"num_format": "0%"})
        inr = wb.add_format({"num_format": "₹#,##0"})
        header = wb.add_format({"bold": True, "bg_color": "#F2F2F7", "border": 0, "text_wrap": True, "valign": "top"})

        def sheet(name, df, pct_cols=(), inr_cols=(), widths=None):
            df = df.copy()
            df.to_excel(xw, sheet_name=name, index=False, startrow=0)
            ws = xw.sheets[name]
            for j, c in enumerate(df.columns):
                ws.write(0, j, c, header)
                w = (widths or {}).get(c) or min(45, max(10, int(df[c].astype(str).str.len().quantile(0.9)) + 2 if len(df) else 12, len(str(c)) + 2))
                fmt = pctf if c in pct_cols else inr if c in inr_cols else None
                ws.set_column(j, j, w, fmt)
            ws.freeze_panes(1, 0)
            ws.autofilter(0, 0, max(len(df), 1), max(len(df.columns) - 1, 0))

        # ---- Read me
        ws = wb.add_worksheet("Read me")
        ws.set_column(0, 0, 26)
        ws.set_column(1, 1, 110, wrap)
        ws.write(0, 0, f"{org.get('company_name', 'CRM')} — ICP & CRM analysis", h1)
        ws.write(1, 0, f"Data pulled from Zoho CRM on {str(org.get('extracted_at', ''))[:10]}. "
                       f"Analysis covers {sig['closed']:,} closed deals (Junk and existing-client deals left out).")
        rows = [
            ("How to read it", ""),
            ("Win rate", "Won deals ÷ (won + lost deals). Open deals are not counted — they are not decided yet."),
            ("Focus / Deprioritize", "A group is 'Focus' when its win rate is clearly above the average (or its value per "
                                     "opportunity is 1.5× average with enough wins); 'Deprioritize' when clearly below."),
            ("Value per opportunity", "Win rate × typical (median) won deal: what one new deal of that type is worth on average."),
            ("Realistic pipeline", "Open deal value × how often past deals at that stage were actually won."),
            ("Money", "All amounts are in Indian Rupees; USD deals converted with Zoho's own exchange rate."),
            ("", ""),
            ("Sheets", ""),
            ("Summary", "Headline numbers and plain-English conclusions: who to focus on, who to deprioritize, what data to fix."),
            ("Best customers", "Scorecard for each question (industry, company size, market, lead source, buyer…)."),
            ("Lead sources", "Deals, win rate and revenue per lead source, plus lead-to-deal conversion."),
            ("Pipeline forecast", "Open pipeline by stage: Zoho's stage % vs what actually happened historically."),
            ("Open deals", "Every open deal with stage, value, expected close, stale flag and realistic value."),
            ("Won deals", "Every won deal in the analysis."),
            ("Data quality", "How complete the fields that matter most are."),
            ("", ""),
            ("Files next to this workbook", ""),
            ("raw_data/", "Every table exactly as exported from Zoho (one CSV per module). Opens in Excel."),
            ("cleaned_data/", "The same data cleaned: typed values, merged spelling variants, rupee amounts, "
                              "Won/Lost/Open outcome, activities linked to deals."),
        ]
        for i, (k, v) in enumerate(rows, start=3):
            ws.write(i, 0, k, h2 if v == "" else None)
            ws.write(i, 1, v, wrap)

        # ---- Summary
        ws = wb.add_worksheet("Summary")
        ws.set_column(0, 0, 4)
        ws.set_column(1, 1, 120, wrap)
        ws.write(0, 1, "Headline numbers", h2)
        heads = [f"Win rate: {ov['win_rate']:.0%}  ({ov['won']:,} won of {ov['won'] + ov['lost']:,} closed deals)",
                 f"Won revenue: {money(ov['won_revenue'])}",
                 f"Typical won deal: {money(ov['median_won_deal'])}  (average {money(ov['avg_won_deal'])})",
                 f"Typical time to close a won deal: {ov['median_cycle_won']:.0f} days",
                 f"Open pipeline: {money(ov['open_pipeline'])}  across {ov['open']:,} open deals"]
        if fc:
            heads.append(f"Realistic open pipeline (by historical win odds): {money(fc['actual'])}; "
                         f"stale deals: {fc['stale_n']:,} worth {money(fc['stale_amount'])}")
        r = 1
        for h in heads:
            ws.write(r, 1, h)
            r += 1
        for title, items in (("Focus on", concl["focus"]), ("Deprioritize", concl["avoid"]), ("Make the answers stronger", concl["fix"])):
            r += 1
            ws.write(r, 1, title, h2)
            r += 1
            for it in items or ["—"]:
                ws.write(r, 1, "• " + _strip(it), wrap)
                r += 1

        # ---- Best customers
        cards = []
        for key, a in answers.items():
            c = a["card"].copy()
            c.insert(0, "Question", a["question"].question)
            c.insert(1, "CRM field", a["label"])
            cards.append(c)
        if cards:
            bc = pd.concat(cards, ignore_index=True)
            bc = bc[["Question", "CRM field", "label", "n", "won", "rate", "avg_deal", "value_per_opp", "days_to_close",
                     "revenue", "revenue_share", "verdict"]].rename(columns={
                         "label": "Group", "n": "Closed deals", "won": "Won", "rate": "Win rate", "avg_deal": "Typical won deal",
                         "value_per_opp": "Value per opportunity", "days_to_close": "Days to close", "revenue": "Won revenue",
                         "revenue_share": "Share of revenue", "verdict": "Verdict"})
            sheet("Best customers", bc, pct_cols=("Win rate", "Share of revenue"),
                  inr_cols=("Typical won deal", "Value per opportunity", "Won revenue"))

        # ---- Lead sources
        s2r = A.source_to_revenue(leads, deals)
        if not s2r.empty:
            s2r = s2r.rename(columns={"source": "Lead source", "deals": "Closed deals", "won": "Won", "revenue": "Won revenue",
                                      "win_rate": "Deal win rate", "avg_won_deal": "Average won deal", "leads": "Leads",
                                      "converted": "Leads converted", "lead_conversion": "Lead → deal conversion"})
            sheet("Lead sources", s2r, pct_cols=("Deal win rate", "Lead → deal conversion"), inr_cols=("Won revenue", "Average won deal"))

        # ---- Pipeline
        if fc:
            p = fc["stages"].rename(columns={
                "deals": "Open deals", "amount": "Total value", "stale": "Stale deals", "no_amount": "No amount entered",
                "median_age": "Typical age (days)", "zoho_prob": "Zoho stage %", "actual_rate": "Actual historical win %",
                "history_n": "Past deals at this stage", "zoho_weighted": "Value × Zoho %", "actual_weighted": "Value × actual %"})
            sheet("Pipeline forecast", p, pct_cols=("Zoho stage %", "Actual historical win %"),
                  inr_cols=("Total value", "Value × Zoho %", "Value × actual %"))
            o = deals[deals["outcome"] == "Open"].copy()
            now = pd.Timestamp.now()
            hist = fc["stages"].set_index("Stage")["actual_rate"]
            o["Company"] = o["Account_Name"].map(acc_name) if "Account_Name" in o else ""
            o["Industry"] = o["Account_Name"].map(acc_ind) if "Account_Name" in o else ""
            o["Stale"] = ((o["closed_on"] < now) | (o["age_days"] > 365)).map({True: "Yes", False: ""})
            o["Realistic value"] = o["amount"] * o["Stage"].map(hist).fillna(0)
            cols = {"Deal_Name": "Deal", "Company": "Company", "Industry": "Industry", "Stage": "Stage", "amount": "Value",
                    "Realistic value": "Realistic value", "closed_on": "Expected close", "age_days": "Days open",
                    "Stale": "Stale", "Owner_Name": "Owner", "Lead_Source2": "Lead source", "Lead_Source": "Lead source"}
            o = o[[c for c in cols if c in o]].rename(columns=cols).sort_values("Value", ascending=False)
            o = o.loc[:, ~o.columns.duplicated()]
            o["Expected close"] = pd.to_datetime(o["Expected close"]).dt.date
            sheet("Open deals", o, inr_cols=("Value", "Realistic value"))

        # ---- Won deals
        w = deals[deals["outcome"] == "Won"].copy()
        w["Company"] = w["Account_Name"].map(acc_name) if "Account_Name" in w else ""
        w["Industry"] = w["Account_Name"].map(acc_ind) if "Account_Name" in w else ""
        cols = {"Deal_Name": "Deal", "Company": "Company", "Industry": "Industry", "amount": "Value (₹)", "Currency": "Currency",
                "amount_original": "Value (original currency)", "closed_on": "Closed", "cycle_days": "Days to close",
                "Owner_Name": "Owner", "Lead_Source2": "Lead source", "Lead_Source": "Lead source", "Type": "Type"}
        w = w[[c for c in cols if c in w]].rename(columns=cols).sort_values("Value (₹)", ascending=False)
        w = w.loc[:, ~w.columns.duplicated()]
        w["Closed"] = pd.to_datetime(w["Closed"]).dt.date
        sheet("Won deals", w, inr_cols=("Value (₹)",))

        # ---- Data quality
        raw = {t[4:]: store.read(t) for t in store.tables() if t.startswith("raw_") and t != "raw_Stage_History"}
        kf = A.key_field_health(A.field_health(raw, store.read("meta_fields")))
        kf = kf.rename(columns={"module": "Module", "field": "Field", "why": "Why it matters", "filled_pct": "Filled", "status": "Status"})
        sheet("Data quality", kf, pct_cols=("Filled",))
    log(f"  workbook: {path.name}")


def export(store: Store, out_dir: Path, log=print) -> Path:
    org = store.read("meta_org").iloc[0].to_dict() if store.has("meta_org") else {}
    name = re.sub(r"[^A-Za-z0-9]+", "_", str(org.get("company_name") or "crm")).strip("_")
    stamp = datetime.now().strftime("%Y-%m-%d")
    folder = out_dir / f"{name}_CRM_export_{stamp}"
    if folder.exists():
        shutil.rmtree(folder)
    (folder / "raw_data").mkdir(parents=True)
    (folder / "cleaned_data").mkdir()

    build_workbook(store, folder / f"{name} - ICP analysis.xlsx", log)

    tables = store.tables()
    for t in sorted(tables):
        if t.startswith("raw_"):
            df = store.read(t)
            df.to_csv(folder / "raw_data" / f"{t[4:]}.csv", index=False, encoding="utf-8-sig")
            log(f"  raw_data/{t[4:]}.csv  ({len(df):,} rows)")
    for t, nice in (("clean_deals", "deals"), ("deal_wide", "deals_with_all_attributes"), ("clean_accounts", "accounts"),
                    ("clean_contacts", "contacts"), ("clean_leads", "leads"), ("clean_activities", "activities"),
                    ("clean_stage_history", "stage_history"), ("cleaning_log", "values_merged_during_cleaning")):
        if t in tables:
            store.read(t).to_csv(folder / "cleaned_data" / f"{nice}.csv", index=False, encoding="utf-8-sig")

    att_dir = Path(store.path).parent / "attachments"
    if att_dir.exists() and any(att_dir.rglob("*")):
        shutil.copytree(att_dir, folder / "attachments")
        n_files = sum(1 for f in (folder / "attachments").rglob("*") if f.is_file())
        log(f"  attachments/  ({n_files:,} files)")

    (folder / "README.txt").write_text(
        f"{org.get('company_name', 'CRM')} — Zoho CRM export and ICP analysis\n"
        f"Data pulled from Zoho on {str(org.get('extracted_at', ''))[:10]}.\n\n"
        f"1. '{name} - ICP analysis.xlsx' — start here. The 'Read me' sheet explains every tab.\n"
        "2. raw_data/ — every Zoho module exactly as exported (CSV, opens in Excel).\n"
        "   Calls has ~280,000 rows; open it in Excel or Google Sheets (both handle it).\n"
        "3. cleaned_data/ — the same data cleaned and linked (amounts in rupees, Won/Lost/Open outcome, etc.).\n\n"
        "4. attachments/ — every file attached to CRM records, in folders by module and record id\n"
        "   (raw_data/Attachments.csv lists them with their parent record).\n"
        "5. raw_data/Deal_Emails.csv — emails logged on deals; Visits.csv — website visits; Notes.csv — rep notes;\n"
        "   Actions_Performed.csv — automation log; Leads_Converted.csv — leads that became deals.\n\n"
        "Cannot be exported through Zoho's API (Zoho limitation): the custom file-upload modules\n"
        "(Contract, NDA, PAN Card, GST Certificate, MSA, PO, SOW...) and Email Analytics.\n"
        "Vendors: no permission for the connected user.\n\n"
        "This export contains customer, contact and document data — share it privately only.\n", encoding="utf-8")

    zip_path = shutil.make_archive(str(folder), "zip", root_dir=folder.parent, base_dir=folder.name)
    log(f"Export ready: {zip_path}")
    return Path(zip_path)
