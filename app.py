"""ICP Analyzer dashboard.  Run:  python cli.py dashboard   (or: streamlit run app.py -- --db data/crm.duckdb)"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from icp_analyzer import analysis as A
from icp_analyzer import insights as IN
from icp_analyzer import ui
from icp_analyzer.config import default_db_path
from icp_analyzer.signals import scan
from icp_analyzer.stats import numeric_bins, order_values, range_key
from icp_analyzer.storage import Store
from icp_analyzer.ui import card, note, pct, plot

st.set_page_config(page_title="ICP Analyzer", layout="wide", initial_sidebar_state="collapsed")
ui.inject()


# ------------------------------------------------------------------ data
def db_arg() -> Path:
    p = argparse.ArgumentParser()
    p.add_argument("--db", type=Path, default=default_db_path())
    args, _ = p.parse_known_args(sys.argv[1:])
    return args.db


@st.cache_data(show_spinner="Loading CRM data…")
def load(path: str, mtime: float) -> dict:
    store = Store(path, read_only=True)
    names = ["deal_wide", "feature_catalog", "clean_deals", "clean_accounts", "clean_contacts", "clean_leads",
             "clean_activities", "clean_stage_history", "cleaning_log", "meta_fields", "meta_picklist", "meta_org",
             "meta_extract_log", "prepare_info"]
    data = {n: store.read(n) for n in names}
    data["raw"] = {t[4:]: store.read(t) for t in store.tables() if t.startswith("raw_") and t != "raw_Stage_History"}
    store.close()
    return data


@st.cache_data(show_spinner="Analyzing every field…")
def run_scan(wide, catalog, min_n):
    return scan(wide, catalog, min_n=min_n)


@st.cache_data(show_spinner=False)
def run_answers(wide, _sig, min_n):
    return IN.all_answers(_sig, wide, min_n)


path = db_arg()
if not path.exists():
    st.error(f"No data at `{path}`. Run `python cli.py demo` or `python cli.py all`.")
    st.stop()
D = load(str(path), path.stat().st_mtime)
if D["clean_deals"].empty:
    st.error("No deals found. Run `python cli.py prepare` after extracting.")
    st.stop()

org = D["meta_org"].iloc[0].to_dict() if not D["meta_org"].empty else {}
currency = org.get("currency") or ""
stage_order = (D["meta_picklist"].query("module == 'Deals' and field == 'Stage'").sort_values("sequence")["display_value"].tolist()
               if not D["meta_picklist"].empty else [])


def money(x) -> str:
    if pd.isna(x):
        return "—"
    symbols = {"INR": "₹", "Indian Rupee": "₹", "USD": "$", "US Dollar": "$", "EUR": "€", "Euro": "€",
               "GBP": "£", "Pound Sterling": "£", "AED": "AED ", "UAE Dirham": "AED ", "SGD": "S$", "Singapore Dollar": "S$"}
    sym = symbols.get(currency, (currency + " ") if currency and len(currency) <= 4 else "")
    for div, suf in ((1e7, " Cr"), (1e5, " L"), (1e3, "K")):
        if abs(x) >= div:
            return f"{sym}{x / div:,.1f}{suf}"
    return f"{sym}{x:,.0f}"


# ------------------------------------------------------------------ header + filters
deals_all = D["clean_deals"]
head_l, head_r = st.columns([5, 1], vertical_alignment="bottom")
with head_r:
    with st.popover("Filters", use_container_width=True):
        dmin, dmax = deals_all["created"].min().date(), deals_all["created"].max().date()
        date_range = st.date_input("Deals created", (dmin, dmax), min_value=dmin, max_value=dmax)
        owners = sorted(deals_all["Owner_Name"].dropna().unique()) if "Owner_Name" in deals_all else []
        sel_owners = st.multiselect("Owner", owners, placeholder="All owners")
        pipes = sorted(deals_all["Pipeline"].dropna().unique()) if "Pipeline" in deals_all else []
        sel_pipes = st.multiselect("Pipeline", pipes, placeholder="All pipelines") if len(pipes) > 1 else []
        type_c = "Type" if "Type" in deals_all else None
        has_new = bool(type_c) and deals_all[type_c].astype(str).str.contains("new", case=False).any()
        new_only = st.toggle("New customers only", value=has_new, disabled=not has_new,
                             help="On: only deals to win NEW customers — what an ICP is about. Deals with existing clients "
                                  "(upsell/renewal) win far more often and would inflate every number.")
        stages = sorted(deals_all["Stage"].dropna().unique()) if "Stage" in deals_all else []
        junkish = [s for s in stages if any(w in s.lower() for w in ("junk", "spam", "duplicate", "test"))]
        skip_stages = st.multiselect("Leave out stages", stages, default=junkish,
                                     help="Deals in these stages are removed from every chart — e.g. Junk deals "
                                          "that were never real opportunities and would otherwise count as losses.")
        min_n = st.slider("Minimum deals per group", 5, 50, 10,
                          help="Smaller groups are merged into 'Other' so tiny samples can't mislead.")

mask = pd.Series(True, index=deals_all.index)
if isinstance(date_range, tuple) and len(date_range) == 2:
    mask &= deals_all["created"].dt.date.between(*date_range)
if sel_owners:
    mask &= deals_all["Owner_Name"].isin(sel_owners)
if sel_pipes:
    mask &= deals_all["Pipeline"].isin(sel_pipes)
if skip_stages:
    mask &= ~deals_all["Stage"].isin(skip_stages)
if new_only:
    mask &= deals_all["Type"].astype(str).str.contains("new", case=False)
deals = deals_all[mask]
wide = D["deal_wide"][D["deal_wide"]["deal_id"].isin(deals["Id"])]
sig = run_scan(wide, D["feature_catalog"], min_n)
base = sig["base_rate"]
ov = A.revenue_overview(deals)
fields = sig["fields"]
usable = fields[fields["strength"] != "Leakage suspected"] if not fields.empty else fields

with head_l:
    st.markdown(f"<div class='hero-title'>{org.get('company_name', 'CRM')}</div>"
                f"<div class='hero-sub'>{sig['closed']:,} closed deals{' to new customers' if new_only else ''} · "
                f"average win rate {pct(base)}</div>",
                unsafe_allow_html=True)

SECTIONS = ["Summary", "Best customers", "Lead sources", "Pipeline", "Sales process", "Buyers", "All fields", "Data quality"]
section = st.segmented_control("Section", SECTIONS, default="Summary", key="section", label_visibility="collapsed") or "Summary"
answers = run_answers(wide, sig, min_n)

if sig["closed"] < 30:
    st.warning(f"Only {sig['closed']} closed deals in this selection. Treat patterns as hypotheses.")


def group_values(feature: str, frame: pd.DataFrame) -> pd.Series:
    s = frame[feature]
    if pd.api.types.is_numeric_dtype(s) and s.nunique() > 8:
        s = numeric_bins(s)
    return s.astype("object").fillna("(blank)").astype(str)


# ================================================================== SUMMARY
if section == "Summary":
    cyc = f"{ov['median_cycle_won']:.0f} days" if pd.notna(ov["median_cycle_won"]) else "—"
    ui.kpis([
        ("Win rate", pct(ov["win_rate"]), f"{ov['won']:,} won of {ov['won'] + ov['lost']:,} closed"),
        ("Won revenue", money(ov["won_revenue"]), f"{ov['won']:,} customers won"),
        ("Average won deal", money(ov["avg_won_deal"]), f"typical: {money(ov['median_won_deal'])}"),
        ("Time to close", cyc, "typical won deal"),
        ("Open pipeline", money(ov["open_pipeline"]), f"{ov['open']:,} deals still open"),
    ])
    concl = IN.conclusions(answers, base, money)
    c1, c2 = st.columns(2)
    with c1:
        with card("Focus on", "Customer types that win clearly more often than your average — or bring much more money per deal."):
            ui.conclusion_list(concl["focus"], "good", "No customer type stands out yet.")
    with c2:
        with card("Deprioritize", "Customer types that win clearly less often than average. Spend less sales time here."):
            ui.conclusion_list(concl["avoid"], "bad", "No customer type is clearly weak.")

    with card("Your ideal customer, at a glance", "For each question, the groups to target (green) and to avoid (red). "
              "Open “Best customers” for the full picture behind each line."):
        rows = []
        for key, a in answers.items():
            cardf = a["card"]
            good = cardf[cardf["verdict"] == "Focus"].sort_values("rate", ascending=False)
            bad = cardf[cardf["verdict"] == "Deprioritize"].sort_values("rate")
            if good.empty and bad.empty:
                continue
            chips = "".join(f"<span class='chip good'><b>{r.label}</b><span class='r'>{r.rate:.0%}</span></span>" for r in good.itertuples())
            chips += "".join(f"<span class='chip bad'><b>{r.label}</b><span class='r'>{r.rate:.0%}</span></span>" for r in bad.itertuples())
            rows.append(f"<div class='icp-row'><div class='k'>{a['question'].name}</div><div class='chips'>{chips}</div></div>")
        st.markdown("".join(rows) or "<p class='card-sub'>Not enough data yet.</p>", unsafe_allow_html=True)
        note("Percent = how often deals from that group are won. Only groups with enough deals and a clear difference are shown.")

    if concl["fix"]:
        with card("Make these answers stronger", "Missing CRM data limits how sure the analysis can be."):
            ui.conclusion_list(concl["fix"], "fix", "")

# ================================================================== BEST CUSTOMERS
elif section == "Best customers":
    if not answers:
        ui.empty("Not enough data to compare customer types.")
    else:
        names = {a["question"].name: k for k, a in answers.items()}
        pick = st.pills("Question", list(names), default=list(names)[0], label_visibility="collapsed") or list(names)[0]
        a = answers[names[pick]]
        alts = a["alternatives"]
        if len(alts) > 1:
            labels = [f"{r.label} ({r.coverage:.0%} filled)" for r in alts.itertuples()]
            choice = st.selectbox("CRM field used", labels, index=0,
                                  help="Several CRM fields can answer the same question. The best-filled one is picked by default.")
            chosen = alts.iloc[labels.index(choice)]["feature"]
            if chosen != a["feature"]:
                a = IN.answer(a["question"], sig, wide, min_n, feature=chosen) or a
        cardf = a["card"]
        q = a["question"]
        good = cardf[cardf["verdict"] == "Focus"].sort_values("rate", ascending=False)
        bad = cardf[cardf["verdict"] == "Deprioritize"].sort_values("rate")
        parts = []
        if len(good):
            parts.append("Best: " + ", ".join(f"<b>{r.label}</b> ({r.rate:.0%})" for r in good.head(3).itertuples()))
        if len(bad):
            parts.append("Weakest: " + ", ".join(f"<b>{r.label}</b> ({r.rate:.0%})" for r in bad.head(3).itertuples()))
        main = cardf[~cardf["value"].isin(["(blank)", "Other (rare values)"])]
        with card(q.question, f"Based on the CRM field “{a['label']}”, recorded on {a['coverage']:.0%} of closed deals. "
                  f"Average win rate: {base:.0%}."):
            st.markdown(f"<p class='takeaway'>{' · '.join(parts) or 'No group is clearly better or worse than average.'}</p>",
                        unsafe_allow_html=True)
            natural_order = main["value"].map(range_key).notna().all()
            ui.verdict_bars(order_values(main) if natural_order else main.sort_values("rate", ascending=False), base)
            note("Green = focus · Grey = about average · Red = deprioritize. The thin line shows how sure we are "
                 "(shorter = more certain).")

        c1, c2 = st.columns([3, 2])
        with c1:
            with card("How often vs how much", "Right = wins more often. Higher = bigger deals. Top-right groups are the most valuable. "
                      "Bubble size = number of deals."):
                m = main[main["n"] >= min_n].dropna(subset=["avg_deal"])
                if m.empty:
                    ui.empty("No deal values recorded.")
                else:
                    fig = go.Figure(go.Scatter(
                        x=m["rate"], y=m["avg_deal"], mode="markers+text", text=m["label"], textposition="top center",
                        textfont=dict(size=11, color=ui.INK_2),
                        marker=dict(size=np.sqrt(m["n"]) * 4 + 6, color=[ui.VERDICT.get(v, ui.MUTED) for v in m["verdict"]],
                                    opacity=.6, line=dict(width=0)),
                        customdata=m[["n", "days_to_close"]].values,
                        hovertemplate="<b>%{text}</b><br>Win rate %{x:.0%}<br>Typical deal %{y:,.0f}<br>%{customdata[0]} deals · "
                                      "%{customdata[1]:.0f} days to close<extra></extra>"))
                    fig.add_vline(x=base, line_width=1, line_dash="dot", line_color=ui.INK_3)
                    fig.update_layout(xaxis=dict(tickformat=".0%", title="Win rate", showgrid=True, gridcolor="#F0F0F3"),
                                      yaxis=dict(title="Typical won deal"))
                    plot(fig, 400)
        with c2:
            with card("Where the revenue comes from", "Share of all won revenue from each group."):
                r2 = main[main["revenue"] > 0].sort_values("revenue").tail(10)
                if r2.empty:
                    ui.empty()
                else:
                    fig = go.Figure(go.Bar(x=r2["revenue"], y=r2["label"], orientation="h", marker_color=ui.BLUE,
                                           text=[f"{x:.0%}" for x in r2["revenue_share"]], textposition="outside",
                                           cliponaxis=False, textfont=dict(color=ui.INK_2),
                                           hovertemplate="%{y}<br>%{x:,.0f}<extra></extra>"))
                    fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showticklabels=False))
                    plot(fig, 400)

        with card("The full scorecard", "Value per opportunity = win rate × typical won deal: what one new deal of this type is "
                  "worth on average, before you know whether it closes. It combines how often and how much."):
            view = cardf[["label", "n", "rate", "avg_deal", "value_per_opp", "days_to_close", "revenue_share", "verdict"]]
            st.dataframe(view.sort_values("value_per_opp", ascending=False), hide_index=True, use_container_width=True, column_config={
                "label": "Group", "n": "Closed deals", "rate": st.column_config.NumberColumn("Win rate", format="percent"),
                "avg_deal": st.column_config.NumberColumn("Typical won deal", format="%.0f"),
                "value_per_opp": st.column_config.NumberColumn("Value per opportunity", format="%.0f"),
                "days_to_close": st.column_config.NumberColumn("Days to close", format="%.0f"),
                "revenue_share": st.column_config.NumberColumn("Share of revenue", format="percent"), "verdict": "Verdict"})

        if len(answers) >= 2:
            with card("Two questions together", "Win rate for each combination — e.g. which industries win within each company size. "
                      f"Blank cells have fewer than {min_n} deals."):
                qn = [answers[k]["question"].name for k in answers]
                c1, c2 = st.columns(2)
                qa = c1.selectbox("Rows", qn, index=0)
                qb = c2.selectbox("Columns", qn, index=1)
                fa, fb = answers[names[qa]], answers[names[qb]]
                closed = wide[wide["outcome"].isin(["Won", "Lost"])]
                ga, gb = group_values(fa["feature"], closed), group_values(fb["feature"], closed)
                sub = pd.DataFrame({"a": ga, "b": gb, "y": closed["is_won"]})
                sub = sub[(sub["a"] != "(blank)") & (sub["b"] != "(blank)")]
                sub = sub[sub["a"].isin(sub["a"].value_counts().head(10).index) & sub["b"].isin(sub["b"].value_counts().head(8).index)]
                if sub.empty or sub["a"].nunique() < 2 or sub["b"].nunique() < 2:
                    ui.empty("Not enough overlap between these two.")
                else:
                    piv = sub.pivot_table(index="a", columns="b", values="y", aggfunc=["mean", "count"])
                    rate, cnt = piv["mean"], piv["count"]

                    def natural(labels):
                        return sorted(labels, key=range_key) if all(range_key(l) is not None for l in labels) else list(labels)
                    rate = rate.loc[natural(rate.index), natural(rate.columns)]
                    cnt = cnt.loc[rate.index, rate.columns]
                    shown = rate.where(cnt >= min_n)
                    txt = shown.map(lambda v: "" if pd.isna(v) else f"{v:.0%}")
                    fig = go.Figure(go.Heatmap(z=shown.values, x=[str(c) for c in shown.columns], y=[str(i) for i in shown.index],
                                               text=txt.values, texttemplate="%{text}", textfont=dict(size=12),
                                               colorscale=ui.DIVERGING, zmid=base, zmin=0, zmax=1, xgap=3, ygap=3,
                                               customdata=cnt.values, showscale=False,
                                               hovertemplate="%{y} × %{x}<br>Win rate %{z:.0%}<br>%{customdata} deals<extra></extra>"))
                    fig.update_layout(xaxis=dict(side="top", showgrid=False), yaxis=dict(showgrid=False, autorange="reversed"))
                    plot(fig, max(320, 44 * len(shown) + 80))

# ================================================================== ALL FIELDS
elif section == "All fields":
    shown_f = usable[usable["source"].isin(["Account", "Contact", "Deal"])]
    other_f = usable[~usable["source"].isin(["Account", "Contact", "Deal"])]
    with card("Every customer field, ranked by how much it matters",
              f"For explorers: all {len(shown_f)} customer and deal fields in the CRM, tested against {sig['closed']:,} closed deals. "
              "A longer bar means winners and losers look more different on that field. Dark blue = clear pattern, "
              "light = weak, grey = no real pattern."):
        if shown_f.empty:
            ui.empty()
        else:
            u = shown_f.iloc[::-1]
            fig = go.Figure(go.Bar(
                x=u["effect"], y=u["label"], orientation="h",
                marker_color=[ui.STRENGTH.get(s, ui.MUTED) for s in u["strength"]],
                customdata=np.stack([u["strength"], u["coverage"]], axis=1),
                hovertemplate="<b>%{y}</b><br>%{customdata[0]} pattern<br>Filled on %{customdata[1]:.0%} of deals<extra></extra>"))
            fig.update_layout(xaxis=dict(title="How much it matters", showticklabels=False), yaxis=dict(showgrid=False))
            plot(fig, max(320, 26 * len(u) + 60))
    with card("Look inside any field", "Win rate for each value. Green = clearly better than average, red = clearly worse."):
        if not usable.empty:
            pick = st.selectbox("Field", usable["label"].tolist(), label_visibility="collapsed")
            feat = usable.loc[usable["label"] == pick, "feature"].iloc[0]
            t = sig["values"][sig["values"]["feature"] == feat]
            ui.rate_bars(order_values(t), base)
            with st.expander("Show numbers"):
                st.dataframe(t[["value", "n", "won", "rate", "confidence"]], hide_index=True, use_container_width=True,
                             column_config={"value": "Value", "n": "Deals", "won": "Won",
                                            "rate": st.column_config.NumberColumn("Win rate", format="percent"),
                                            "confidence": "How sure"})
    with st.expander("Fields kept out of the ICP (sales team, deal progress, time) and why"):
        if len(other_f):
            st.dataframe(other_f[["label", "source"]].rename(columns={"label": "Field", "source": "Group"}),
                         hide_index=True, use_container_width=True)
        leaks = fields[fields["strength"] == "Leakage suspected"] if not fields.empty else fields
        if len(leaks):
            st.markdown("**Filled only after a deal is decided** — these would falsely “predict” the outcome:")
            st.dataframe(leaks[["label", "leakage"]].rename(columns={"label": "Field", "leakage": "Why excluded"}),
                         hide_index=True, use_container_width=True)

# ================================================================== PIPELINE
elif section == "Pipeline":
    sf = A.stage_funnel(D["clean_stage_history"], deals, stage_order)
    op = A.open_pipeline(deals, stage_order)
    c1, c2 = st.columns(2)
    with c1:
        with card("How far closed deals got", "Share of closed deals that reached each stage."):
            if sf.empty:
                ui.empty("Stage history not extracted. Run: python cli.py extract --stage-history")
            else:
                fig = go.Figure(go.Funnel(y=sf["stage"], x=sf["deals_reached"], textinfo="value+percent initial",
                                          marker=dict(color=ui.BLUE), connector=dict(fillcolor="#EEF4FC"),
                                          textfont=dict(color="white")))
                plot(fig, 330)
    with c2:
        with card("Open pipeline", "Value sitting in each stage today."):
            if op.empty:
                ui.empty("No open deals.")
            else:
                fig = go.Figure(go.Bar(x=op["Stage"], y=op["amount"], marker_color=ui.MUTED, text=op["deals"].astype(str) + " deals",
                                       textposition="outside", cliponaxis=False, textfont=dict(color=ui.INK_2)))
                plot(fig, 330)
    if not sf.empty:
        with card("Time spent in each stage", "Median days. When lost deals linger much longer, that stage is where they quietly die."):
            fig = go.Figure()
            fig.add_bar(x=sf["stage"], y=sf["median_days_won"], name="Won", marker_color=ui.GREEN)
            fig.add_bar(x=sf["stage"], y=sf["median_days_lost"], name="Lost", marker_color=ui.RED)
            fig.update_layout(barmode="group", yaxis_title="Days")
            plot(fig, 300)
    la = A.loss_analysis(deals)
    c1, c2 = st.columns(2)
    with c1:
        with card("Why deals are lost"):
            if "reasons" in la:
                r = la["reasons"].iloc[::-1]
                fig = go.Figure(go.Bar(x=r["deals"], y=r["reason"], orientation="h",
                                       marker_color=[ui.MUTED if "no reason" in x else ui.RED for x in r["reason"]]))
                fig.update_layout(yaxis=dict(showgrid=False))
                plot(fig, max(260, 34 * len(r) + 60))
            else:
                ui.empty("No loss-reason field found.")
    with c2:
        with card("Where lost deals stopped"):
            if "died_at" in la:
                d = la["died_at"]
                d = d.assign(o=d["stage"].map({s: i for i, s in enumerate(stage_order)}).fillna(99)).sort_values("o")
                fig = go.Figure(go.Bar(x=d["stage"], y=d["deals"], marker_color=ui.RED))
                plot(fig, 300)
            else:
                ui.empty("Needs stage history.")
    if "competitors" in la:
        with card("Win rate by competitor recorded"):
            ui.rate_bars(order_values(la["competitors"]), base)

    c1, c2 = st.columns(2)
    closed = deals[deals["outcome"].isin(["Won", "Lost"])]
    with c1:
        with card("How long deals take", "Days from created to closed. Green = won, red = lost."):
            fig = go.Figure()
            for name, color in (("Lost", ui.RED), ("Won", ui.GREEN)):
                fig.add_histogram(x=closed.loc[closed["outcome"] == name, "cycle_days"], name=name, marker_color=color,
                                  opacity=.55, nbinsx=35)
            fig.update_layout(barmode="overlay", bargap=.05, xaxis_title="Days")
            plot(fig, 320)
    with c2:
        with card("How concentrated revenue is", "Share of won revenue coming from the biggest customers."):
            rc = A.revenue_concentration(deals, D["clean_accounts"])
            if rc.empty:
                ui.empty()
            else:
                fig = go.Figure(go.Scatter(x=rc["account_pct"], y=rc["cum_share"], mode="lines", line=dict(color=ui.BLUE, width=2.5),
                                           fill="tozeroy", fillcolor="rgba(0,113,227,.08)",
                                           hovertemplate="Top %{x:.0%} of customers → %{y:.0%} of revenue<extra></extra>"))
                fig.update_layout(xaxis=dict(tickformat=".0%", title="Customers, biggest first"), yaxis=dict(tickformat=".0%"))
                plot(fig, 320)
                top20 = rc.loc[rc["account_pct"] <= .2, "cum_share"].max()
                if pd.notna(top20):
                    note(f"The biggest 20% of customers bring {top20:.0%} of all won revenue.")

# ================================================================== LEADS
elif section == "Lead sources":
    leads = D["clean_leads"]
    if "source" in answers:
        a = answers["source"]
        with card("Which lead sources turn into customers", f"Win rate of deals by where they came from (field “{a['label']}”). "
                  f"Average: {base:.0%}. Green = focus, red = deprioritize."):
            main = a["card"][~a["card"]["value"].isin(["(blank)", "Other (rare values)"])].sort_values("rate", ascending=False)
            ui.verdict_bars(main, base)
    s2r = A.source_to_revenue(leads, deals)
    if not s2r.empty:
        with card("Lead sources", "Each source by lead conversion and deal win rate. Bubble size = won revenue."):
            s = s2r.dropna(subset=["win_rate"])
            has_conv = "lead_conversion" in s
            fig = go.Figure(go.Scatter(
                x=s["lead_conversion"] if has_conv else s["deals"], y=s["win_rate"], text=s["source"],
                mode="markers+text", textposition="top center", textfont=dict(size=11, color=ui.INK_2),
                marker=dict(size=np.sqrt(s["revenue"].fillna(0) / max(s["revenue"].max(), 1)) * 60 + 8, color=ui.INDIGO,
                            opacity=.5, line=dict(width=0)),
                customdata=s[["deals", "revenue"]].fillna(0).values,
                hovertemplate="<b>%{text}</b><br>Win rate %{y:.0%}<br>%{customdata[0]:.0f} deals · revenue %{customdata[1]:,.0f}<extra></extra>"))
            fig.add_hline(y=base, line_width=1, line_dash="dot", line_color=ui.INK_3)
            fig.update_layout(xaxis=dict(tickformat=".0%" if has_conv else ",", title="Lead → deal conversion" if has_conv else "Deals",
                                         showgrid=True, gridcolor="#F0F0F3"),
                              yaxis=dict(tickformat=".0%", title="Deal win rate"))
            plot(fig, 420)
    if not leads.empty:
        opts = {"Source": "Lead_Source", "Industry": "Industry", "Company size": "employee_band", "Country": "Country",
                "Function": "function", "Seniority": "seniority", "Owner": "Owner_Name"}
        opts = {k: v for k, v in opts.items() if v in leads}
        c1, c2 = st.columns([3, 2])
        with c1:
            with card("Lead conversion", f"{len(leads):,} leads · {leads['converted'].mean():.0%} converted to a deal"):
                pick = st.selectbox("By", list(opts), label_visibility="collapsed")
                lt = A.lead_funnel(leads, opts[pick])
                lt = lt[(lt["n"] >= min_n) & (lt["value"] != "(blank)")]
                ui.rate_bars(order_values(lt), leads["converted"].mean(), label="Conversion")
        with c2:
            with card("New leads per month"):
                if "Created_Time" in leads:
                    lc = leads.groupby(leads["Created_Time"].dt.to_period("M")).size()
                    fig = go.Figure(go.Bar(x=lc.index.astype(str), y=lc.values, marker_color=ui.INDIGO))
                    plot(fig, 360)

# ================================================================== BUYERS
elif section == "Buyers":
    c1, c2 = st.columns(2)
    for col, feat, title in ((c1, "contact.seniority", "By seniority"), (c2, "contact.function", "By function")):
        with col:
            with card(title, "Main contact on the deal."):
                t = A.role_table(wide, feat)
                t = t[(t["n"] >= min_n) & (t["value"] != "Unknown")] if not t.empty else t
                ui.rate_bars(t.sort_values("rate", ascending=False) if not t.empty else t, base)
    t = A.role_table(wide, "contact.title")
    if not t.empty:
        with card("Titles on won deals", "Most common job titles among won deals, with their win rate."):
            tt = t[t["n"] >= max(3, min_n // 2)].sort_values("won", ascending=False).head(12).iloc[::-1]
            fig = go.Figure(go.Bar(x=tt["won"], y=tt["value"], orientation="h",
                                   marker_color=[ui.DIRECTION.get(d, ui.MUTED) for d in tt["direction"]],
                                   text=[f"{r:.0%} win rate" for r in tt["rate"]], textposition="outside", cliponaxis=False,
                                   textfont=dict(color=ui.INK_2, size=12)))
            fig.update_layout(xaxis_title="Won deals", yaxis=dict(showgrid=False))
            plot(fig, max(300, 32 * len(tt) + 60))

# ================================================================== SALES MOTION
elif section == "Sales process":
    cmp = A.activity_compare(deals)
    if not cmp.empty and {"Won", "Lost"} <= set(cmp.columns):
        items = []
        for k in ("Meetings", "Calls", "Days to first activity"):
            if k in cmp.index:
                items.append((k + " (median)", f"{cmp.loc[k, 'Won']:.0f}", f"won  ·  {cmp.loc[k, 'Lost']:.0f} for lost"))
        ui.kpis(items)
    c1, c2 = st.columns(2)
    with c1:
        with card("Meetings before close"):
            ui.rate_bars(A.activity_buckets(deals, "n_meetings"), base)
    with c2:
        with card("Speed of first touch"):
            ui.rate_bars(A.activity_buckets(deals, "days_to_first_activity"), base)
    c1, c2 = st.columns(2)
    with c1:
        with card("Calls before close"):
            ui.rate_bars(A.activity_buckets(deals, "n_calls"), base)
    with c2:
        with card("Activity mix"):
            acts = D["clean_activities"]
            mix = acts[acts["related_id"].isin(deals["Id"])].groupby("type").size() if not acts.empty else pd.Series(dtype=int)
            if mix.empty:
                ui.empty()
            else:
                fig = go.Figure(go.Pie(labels=mix.index, values=mix.values, hole=.62, sort=False,
                                       marker=dict(colors=[ui.BLUE, ui.INDIGO, ui.TEAL]), textinfo="label+percent"))
                fig.update_layout(showlegend=False)
                plot(fig, 300)
    note("Only activities logged before each deal closed are counted. These show how to sell, not who to sell to — "
         "and longer deals naturally collect more activity.")

# ================================================================== DATA QUALITY
elif section == "Data quality":
    fh = A.field_health(D["raw"], D["meta_fields"])
    kf = A.key_field_health(fh)
    hs = A.health_summary(D["clean_accounts"], D["clean_contacts"], deals_all, D["clean_leads"], kf)
    ui.kpis([("Health score", f"{hs['health_score']}", "out of 100"),
             ("Duplicate accounts", f"{hs['duplicate_accounts']}", "same company entered twice"),
             ("Stale open deals", f"{hs.get('stale_open_deals', 0)}", "past close date or over a year old"),
             ("Lost without reason", pct(hs.get("lost_without_reason_pct")), "of lost deals"),
             ("Deals without amount", pct(hs.get("deals_without_amount_pct")), "of all deals")])
    with card("Key fields", "How complete the fields that matter most for ICP analysis are. Emptier fields give weaker conclusions."):
        k = kf.assign(label=kf["module"] + " · " + kf["field"].str.replace("__s", "").str.replace("_", " "),
                      filled=kf["filled_pct"].fillna(0)).sort_values("filled", ascending=False)
        colors = {"Good": ui.GREEN, "Usable": "#8FD9A8", "Weak": ui.ORANGE, "Unusable": ui.RED, "Not in CRM": ui.MUTED}
        fig = go.Figure(go.Bar(x=k["filled"], y=k["label"], orientation="h", marker_color=[colors[s] for s in k["status"]],
                               text=[("not in CRM" if s == "Not in CRM" else f"{f:.0%}") for f, s in zip(k["filled"], k["status"])],
                               textposition="outside", cliponaxis=False, textfont=dict(color=ui.INK_2),
                               customdata=k["why"], hovertemplate="%{y}<br>%{customdata}<extra></extra>"))
        fig.update_layout(xaxis=dict(tickformat=".0%", range=[0, 1.12]), yaxis=dict(showgrid=False))
        plot(fig, 34 * len(k) + 60)
    info = D["prepare_info"]
    if not info.empty and info["activities_excluded_after_close"].iloc[0]:
        note(f"{int(info['activities_excluded_after_close'].iloc[0]):,} activities logged after their deal closed were "
             "excluded from activity analysis.")
    with st.expander("Every field in every module"):
        mod = st.selectbox("Module", sorted(fh["module"].unique()))
        st.dataframe(fh[fh["module"] == mod].drop(columns="module").sort_values("filled_pct"), hide_index=True,
                     use_container_width=True, column_config={
                         "filled_pct": st.column_config.ProgressColumn("Filled", format="percent", min_value=0, max_value=1),
                         "top_share": st.column_config.NumberColumn("Top value share", format="percent")})
    with st.expander("Values merged during cleaning"):
        cl = D["cleaning_log"]
        st.dataframe(cl, hide_index=True, use_container_width=True) if not cl.empty else st.caption("No messy values found.")
    with st.expander("Possible duplicate accounts"):
        acc = D["clean_accounts"]
        if "is_duplicate" in acc and acc["is_duplicate"].any():
            keys = acc.loc[acc["is_duplicate"], "name_key"]
            st.dataframe(acc[acc["name_key"].isin(keys)][["Account_Name", "Id"]].sort_values("Account_Name"),
                         hide_index=True, use_container_width=True)
        else:
            st.caption("None found.")
    with st.expander("Download cleaned data"):
        tables = {"Deals — all attributes": wide, "Deals": deals, "Accounts": D["clean_accounts"], "Contacts": D["clean_contacts"],
                  "Leads": D["clean_leads"], "Activities": D["clean_activities"], "Signal values": sig["values"]}
        name = st.selectbox("Table", list(tables))
        st.download_button("Download CSV", tables[name].to_csv(index=False).encode(),
                           file_name=name.lower().replace(" — ", "_").replace(" ", "_") + ".csv")
