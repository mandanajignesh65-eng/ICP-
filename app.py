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
from icp_analyzer.config import default_db_path
from icp_analyzer.signals import drivers, scan
from icp_analyzer.stats import numeric_bins, order_values, range_key, rate_table
from icp_analyzer.storage import Store

WON, LOST, OPEN, NEUTRAL, ACCENT = "#2E9D6A", "#D1495B", "#9AA5B1", "#B8C0CC", "#3B6FD8"
DIR_COLORS = {"Better": WON, "Worse": LOST, "Not different": NEUTRAL, "Too few": "#E3E7EC"}
SOURCE_COLORS = {"Account": "#3B6FD8", "Contact": "#8A5CD1", "Deal": "#1F9E9A", "Activity": "#9AA5B1"}
STRENGTH_ICON = {"Strong": "🟢 Strong", "Moderate": "🟡 Moderate", "Weak": "⚪ Weak",
                 "No clear signal": "· None", "Leakage suspected": "⚠️ Leakage"}

st.set_page_config(page_title="ICP Analyzer", page_icon="📊", layout="wide")
st.markdown("""<style>
.block-container {padding-top: 1.5rem; max-width: 1400px;}
div[data-testid="stMetricValue"] {font-size: 1.6rem;}
.finding {padding: .55rem .8rem; border-left: 3px solid #3B6FD8; background: rgba(59,111,216,.07); margin-bottom: .4rem; border-radius: 4px;}
.seg {display: grid; grid-template-columns: 64px 1fr 160px; gap: .8rem; align-items: center; padding: .6rem .8rem;
       border: 1px solid rgba(128,128,128,.22); border-radius: 8px; margin-bottom: .45rem;}
.seg-rate {font-size: 1.35rem; font-weight: 700; text-align: right;}
.chip {display: inline-block; padding: .12rem .5rem; margin: .1rem .25rem .1rem 0; border-radius: 999px;
       background: rgba(59,111,216,.12); font-size: .85rem;}
.seg-meta {font-size: .78rem; opacity: .65; margin-top: .2rem;}
.seg-bar {height: 8px; background: rgba(128,128,128,.18); border-radius: 4px; overflow: hidden;}
.seg-bar > div {height: 100%;}
.finding.proc {border-left-color: #9AA5B1; background: rgba(154,165,177,.08);}
.kpis {display: grid; grid-template-columns: repeat(auto-fit, minmax(135px, 1fr)); gap: .75rem; margin: .25rem 0 1rem;}
.kpi {padding: .8rem 1rem; border: 1px solid rgba(128,128,128,.25); border-radius: 8px;}
.k-label {font-size: .8rem; opacity: .7;}
.k-value {font-size: 1.55rem; font-weight: 600; margin: .1rem 0;}
.k-sub {font-size: .78rem; opacity: .6; min-height: 1em;}
.warn {padding: .55rem .8rem; border-left: 3px solid #E0A100; background: rgba(224,161,0,.08); margin-bottom: .4rem; border-radius: 4px;}
</style>""", unsafe_allow_html=True)


# ------------------------------------------------------------------ data loading
def db_arg() -> Path:
    p = argparse.ArgumentParser()
    p.add_argument("--db", type=Path, default=default_db_path())
    args, _ = p.parse_known_args(sys.argv[1:])
    return args.db


@st.cache_data(show_spinner="Loading CRM data…")
def load(path: str, mtime: float) -> dict[str, pd.DataFrame]:
    store = Store(path, read_only=True)
    names = ["deal_wide", "feature_catalog", "clean_deals", "clean_accounts", "clean_contacts", "clean_leads",
             "clean_activities", "clean_stage_history", "cleaning_log", "meta_fields", "meta_picklist", "meta_org",
             "meta_users", "meta_modules", "meta_extract_log", "prepare_info"]
    data = {n: store.read(n) for n in names}
    data["raw"] = {t[4:]: store.read(t) for t in store.tables() if t.startswith("raw_") and t != "raw_Stage_History"}
    store.close()
    return data


@st.cache_data(show_spinner="Scanning every field for signals…")
def run_scan(wide: pd.DataFrame, catalog: pd.DataFrame, min_n: int):
    return scan(wide, catalog, min_n=min_n)


@st.cache_data(show_spinner=False)
def run_drivers(wide: pd.DataFrame, fields: pd.DataFrame, sources: tuple):
    return drivers(wide, fields[fields["source"].isin(sources)])


path = db_arg()
if not path.exists():
    st.error(f"No data found at `{path}`. Run `python cli.py demo` (sample data) or `python cli.py all` (Zoho).")
    st.stop()
D = load(str(path), path.stat().st_mtime)
if D["clean_deals"].empty:
    st.error("No deals in this database. Run `python cli.py prepare` after extracting.")
    st.stop()

org = D["meta_org"].iloc[0] if not D["meta_org"].empty else {}
currency = org.get("currency") or ""
stage_order = D["meta_picklist"].query("module == 'Deals' and field == 'Stage'").sort_values("sequence")["display_value"].tolist() \
    if not D["meta_picklist"].empty else []


def money(x) -> str:
    if pd.isna(x):
        return "—"
    for div, suf in ((1e7, " Cr"), (1e5, " L"), (1e3, " K")):
        if abs(x) >= div:
            return f"{currency} {x / div:,.2f}{suf}".strip()
    return f"{currency} {x:,.0f}".strip()


# ------------------------------------------------------------------ sidebar filters
with st.sidebar:
    st.markdown(f"### 📊 ICP Analyzer\n**{org.get('company_name', 'CRM')}**")
    st.caption(f"Data file: `{path.name}` · extracted {str(org.get('extracted_at', ''))[:10]}")
    deals_all = D["clean_deals"]
    dmin, dmax = deals_all["created"].min().date(), deals_all["created"].max().date()
    date_range = st.date_input("Deals created between", (dmin, dmax), min_value=dmin, max_value=dmax)
    owners = sorted(deals_all["Owner_Name"].dropna().unique()) if "Owner_Name" in deals_all else []
    sel_owners = st.multiselect("Deal owner", owners, placeholder="All owners")
    pipes = sorted(deals_all["Pipeline"].dropna().unique()) if "Pipeline" in deals_all else []
    sel_pipes = st.multiselect("Pipeline", pipes, placeholder="All pipelines") if len(pipes) > 1 else []
    min_n = st.slider("Minimum deals per group", 5, 50, 10,
                      help="Groups smaller than this are merged into 'Other' so tiny samples can't mislead you.")
    st.divider()
    st.caption("Won = green · Lost = red · Open = grey. Every rate shows its sample size and a 95% confidence range.")

mask = pd.Series(True, index=deals_all.index)
if isinstance(date_range, tuple) and len(date_range) == 2:
    mask &= deals_all["created"].dt.date.between(*date_range)
if sel_owners:
    mask &= deals_all["Owner_Name"].isin(sel_owners)
if sel_pipes:
    mask &= deals_all["Pipeline"].isin(sel_pipes)
deals = deals_all[mask]
wide = D["deal_wide"][D["deal_wide"]["deal_id"].isin(deals["Id"])]
catalog = D["feature_catalog"]
sig = run_scan(wide, catalog, min_n)
base = sig["base_rate"]
ov = A.revenue_overview(deals)


# ------------------------------------------------------------------ chart helpers
def rate_chart(t: pd.DataFrame, title: str = "", base_rate: float | None = None, height: int | None = None, label="win rate"):
    if t.empty:
        st.info("Not enough data.")
        return
    t = t.copy()
    t["text"] = [f"{r:.0%}  ·  n={n}" for r, n in zip(t["rate"], t["n"])]
    t = t.iloc[::-1]
    fig = go.Figure(go.Bar(
        x=t["rate"], y=t["value"].astype(str), orientation="h", text=t["text"], textposition="outside",
        marker_color=[DIR_COLORS.get(d, NEUTRAL) for d in t["direction"]],
        error_x=dict(type="data", symmetric=False, array=t["ci_hi"] - t["rate"], arrayminus=t["rate"] - t["ci_lo"],
                     color="rgba(0,0,0,.35)", thickness=1),
        hovertemplate="%{y}<br>" + label + " %{x:.1%}<extra></extra>"))
    b = base if base_rate is None else base_rate
    if pd.notna(b):
        fig.add_vline(x=b, line_dash="dash", line_color="#555", annotation_text=f"average {b:.0%}", annotation_position="top")
    fig.update_layout(title=title, height=height or max(260, 34 * len(t) + 90), margin=dict(l=10, r=40, t=50 if title else 30, b=10),
                      xaxis=dict(tickformat=".0%", range=[0, min(1, max(t["ci_hi"].max(), t["rate"].max()) + .15)], title=label),
                      yaxis=dict(title=""), plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)


def rate_df_view(t: pd.DataFrame, rate_name="Win rate"):
    view = t[["value", "n", "won", "rate", "ci_lo", "ci_hi", "lift", "share_of_wins", "direction", "confidence"]].rename(columns={
        "value": "Value", "n": "Deals", "won": "Won", "rate": rate_name, "ci_lo": "Range low", "ci_hi": "Range high",
        "lift": "Lift vs avg", "share_of_wins": "Share of wins", "direction": "Vs average", "confidence": "Confidence"})
    st.dataframe(view, hide_index=True, use_container_width=True, column_config={
        rate_name: st.column_config.ProgressColumn(format="percent", min_value=0, max_value=1),
        "Range low": st.column_config.NumberColumn(format="percent"), "Range high": st.column_config.NumberColumn(format="percent"),
        "Lift vs avg": st.column_config.NumberColumn(format="%.2f×"),
        "Share of wins": st.column_config.NumberColumn(format="percent")})


def explain(text: str):
    st.caption("ℹ️ " + text)


# ------------------------------------------------------------------ tabs
tabs = st.tabs(["📋 Summary", "🩺 Data health", "📡 Signals", "🧭 Segments & combos", "💰 Revenue & cycle",
                "🔻 Pipeline & losses", "🎯 Leads & sources", "📞 Activities", "👤 Buyer roles", "📈 Trends", "🗂 Data"])

# ============ SUMMARY
with tabs[0]:
    st.subheader("What the CRM says")
    cycle_w = f"{ov['median_cycle_won']:.0f} days" if pd.notna(ov["median_cycle_won"]) else "—"
    cycle_l = f"lost deals: {ov['median_cycle_lost']:.0f} days" if pd.notna(ov["median_cycle_lost"]) else ""
    kpis = [("Deals", f"{ov['deals']:,}", f"{ov['open']:,} still open"),
            ("Win rate (closed)", A.pct(ov["win_rate"]), f"{ov['won']:,} won · {ov['lost']:,} lost"),
            ("Won revenue", money(ov["won_revenue"]), ""),
            ("Avg won deal", money(ov["avg_won_deal"]), f"median {money(ov['median_won_deal'])}"),
            ("Median cycle (won)", cycle_w, cycle_l),
            ("Open pipeline", money(ov["open_pipeline"]), "")]
    st.markdown("<div class='kpis'>" + "".join(
        f"<div class='kpi'><div class='k-label'>{l}</div><div class='k-value'>{v}</div><div class='k-sub'>{s}</div></div>"
        for l, v, s in kpis) + "</div>", unsafe_allow_html=True)

    if sig["closed"] < 30:
        st.markdown(f"<div class='warn'>Only <b>{sig['closed']}</b> closed deals in this selection — treat every pattern as a hypothesis.</div>", unsafe_allow_html=True)

    left, right = st.columns([3, 2])
    with left:
        st.markdown("#### 🎯 Who wins — customer & deal traits")
        items = A.findings(sig)
        if not items:
            st.info("No confident patterns yet — more closed deals or better-filled fields are needed.")
        for f in items:
            st.markdown(f"<div class='finding'>{f}</div>", unsafe_allow_html=True)
        explain("Only non-leaky fields with medium/high confidence: enough deals AND a 95% range that doesn't overlap the average.")
        proc = A.findings(sig, sources=("Activity",), limit=4)
        if proc:
            st.markdown("#### 📞 How wins happen — sales process")
            for f in proc:
                st.markdown(f"<div class='finding proc'>{f}</div>", unsafe_allow_html=True)
            explain("Process signals guide how to sell (e.g. meeting targets). They are not part of the ICP.")
    with right:
        st.markdown("#### 📡 Signal strength by field")
        f = sig["fields"]
        top = f[f["strength"].isin(["Strong", "Moderate", "Weak"])].head(14)
        if not top.empty:
            fig = px.bar(top.iloc[::-1], x="effect", y="label", orientation="h", color="source",
                         color_discrete_map=SOURCE_COLORS,
                         labels={"effect": "Effect size (Cramér's V)", "label": ""}, height=max(300, 30 * len(top) + 80))
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), legend_title_text="", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
        explain("How strongly each field separates won from lost (0 = not at all). 'Activity' = how you sold, not who bought.")

    st.markdown("#### 🎯 ICP draft from your own won/lost data")
    draft = A.icp_draft(sig)
    if draft.empty:
        st.info("No values are confidently better or worse than average yet.")
    else:
        st.dataframe(draft.rename(columns={"label": "Field", "value": "Value", "verdict": "Verdict", "rate": "Win rate",
                                           "lift": "Lift", "n": "Deals", "share_of_wins": "Share of wins",
                                           "confidence": "Confidence", "strength": "Field strength"}),
                     hide_index=True, use_container_width=True, column_config={
                         "Win rate": st.column_config.ProgressColumn(format="percent", min_value=0, max_value=1),
                         "Lift": st.column_config.NumberColumn(format="%.2f×"),
                         "Share of wins": st.column_config.NumberColumn(format="percent")})
        explain("Target = win rate confidently above average; Avoid = confidently below. Based only on company, contact and deal attributes (not sales activity).")

    leaks = sig["fields"][sig["fields"]["strength"] == "Leakage suspected"]
    if not leaks.empty:
        with st.expander(f"⚠️ {len(leaks)} field(s) excluded as leakage (filled only after a deal closes)"):
            st.dataframe(leaks[["label", "leakage", "coverage"]], hide_index=True, use_container_width=True)

# ============ DATA HEALTH
with tabs[1]:
    fh = A.field_health(D["raw"], D["meta_fields"])
    kf = A.key_field_health(fh)
    hs = A.health_summary(D["clean_accounts"], D["clean_contacts"], deals_all, D["clean_leads"], kf)
    c = st.columns(5)
    c[0].metric("Data health score", f"{hs['health_score']}/100")
    c[1].metric("Duplicate accounts", hs["duplicate_accounts"])
    c[2].metric("Stale open deals", hs.get("stale_open_deals", 0), help="Open deals past close date by 30+ days or older than a year")
    c[3].metric("Lost deals without reason", A.pct(hs.get("lost_without_reason_pct")))
    c[4].metric("Deals without amount", A.pct(hs.get("deals_without_amount_pct")))
    explain("If a field is mostly empty, conclusions from it are weak. Fix the red ones first to make the analysis sharper.")

    st.markdown("#### Key fields for ICP analysis")
    color = {"Good": WON, "Usable": "#7FB77E", "Weak": "#E0A100", "Unusable": LOST, "Not in CRM": NEUTRAL}
    kf["label"] = kf["module"] + " · " + kf["field"]
    fig = px.bar(kf.fillna({"filled_pct": 0}), x="filled_pct", y="label", orientation="h", color="status",
                 color_discrete_map=color, hover_data=["why"], labels={"filled_pct": "Filled", "label": ""},
                 height=40 * len(kf) + 60)
    fig.update_layout(xaxis_tickformat=".0%", margin=dict(l=10, r=10, t=10, b=10), yaxis={"categoryorder": "total ascending"},
                      plot_bgcolor="rgba(0,0,0,0)", legend_title_text="")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Every field in every module")
    mod = st.selectbox("Module", sorted(fh["module"].unique()))
    st.dataframe(fh[fh["module"] == mod].drop(columns="module").sort_values("filled_pct"), hide_index=True,
                 use_container_width=True, column_config={
                     "filled_pct": st.column_config.ProgressColumn("Filled", format="percent", min_value=0, max_value=1),
                     "top_share": st.column_config.NumberColumn("Top value share", format="percent")})
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Values merged during cleaning")
        cl = D["cleaning_log"]
        st.dataframe(cl, hide_index=True, use_container_width=True) if not cl.empty else st.caption("No messy values found.")
        explain("Spelling / case / spacing variants merged into one value, so counts aren't split.")
    with c2:
        st.markdown("#### Possible duplicate accounts")
        acc = D["clean_accounts"]
        if "is_duplicate" in acc and acc["is_duplicate"].any():
            keys = acc.loc[acc["is_duplicate"], "name_key"]
            st.dataframe(acc[acc["name_key"].isin(keys)][["Account_Name", "name_key", "Id"]].sort_values("name_key"),
                         hide_index=True, use_container_width=True)
        else:
            st.caption("None found.")
    info = D["prepare_info"]
    if not info.empty and info["activities_excluded_after_close"].iloc[0]:
        st.caption(f"🛡️ {int(info['activities_excluded_after_close'].iloc[0]):,} activities logged after their deal closed were excluded from activity signals (they'd fake a 'more activity = win' pattern).")

# ============ SIGNALS
with tabs[2]:
    st.subheader("Signal scanner — every field vs won/lost")
    explain(f"{len(sig['fields'])} fields tested on {sig['closed']:,} closed deals (average win rate {A.pct(base)}). "
            "Effect size = how strongly the field separates winners from losers. q-value = chance the pattern is noise, "
            "corrected for testing many fields at once (below 0.05 = reliable).")
    f = sig["fields"].copy()
    src = st.multiselect("Show sources", sorted(f["source"].unique()), default=sorted(f["source"].unique()),
                         help="Account/Contact/Deal = who the customer is. Activity = how the deal was worked.")
    f = f[f["source"].isin(src)]
    f["Strength"] = f["strength"].map(STRENGTH_ICON)
    f["Best value"] = [f"{v} ({r:.0%}, n={n})" if v else "—" for v, r, n in zip(f["best_value"], f["best_rate"], f["best_n"])]
    f["Worst value"] = [f"{v} ({r:.0%}, n={n})" if v else "—" for v, r, n in zip(f["worst_value"], f["worst_rate"], f["worst_n"])]
    st.dataframe(f[["Strength", "label", "source", "effect", "q_value", "coverage", "Best value", "Worst value", "custom", "leakage"]],
                 hide_index=True, use_container_width=True, height=420, column_config={
                     "label": "Field", "source": "Source", "custom": "Custom field",
                     "effect": st.column_config.ProgressColumn("Effect size", format="%.2f", min_value=0, max_value=1),
                     "q_value": st.column_config.NumberColumn("q-value", format="%.3f"),
                     "coverage": st.column_config.ProgressColumn("Filled", format="percent", min_value=0, max_value=1),
                     "leakage": "Leakage reason"})
    st.markdown("#### Drill into a field")
    options = f["label"].tolist()
    if options:
        pick = st.selectbox("Field", options)
        feat = f.loc[f["label"] == pick, "feature"].iloc[0]
        t = sig["values"][sig["values"]["feature"] == feat]
        rate_chart(order_values(t), f"Win rate by {pick}")
        rate_df_view(t)
    if not sig["skipped"].empty:
        with st.expander(f"{len(sig['skipped'])} field(s) not testable"):
            st.dataframe(sig["skipped"], hide_index=True, use_container_width=True)

# ============ SEGMENTS & COMBOS
with tabs[3]:
    st.subheader("Which combinations of traits win?")
    inc_act = st.toggle("Include sales-activity signals", value=False,
                        help="Off = only who the customer is (ICP). On = also how the deal was worked.")
    sources = ("Account", "Contact", "Deal", "Activity") if inc_act else ("Account", "Contact", "Deal")
    dr = run_drivers(wide, sig["fields"], sources)
    if dr["rules"].empty:
        st.info("Not enough closed deals or signals to find segments.")
    else:
        c1, c2 = st.columns([1, 3])
        c1.metric("Predictive power (AUC)", f"{dr['auc']:.2f}" if pd.notna(dr["auc"]) else "—",
                  help="0.5 = no better than a coin flip, 0.7 = useful, 0.8+ = strong. Cross-validated, so it's honest.")
        with c2:
            explain("A shallow decision tree splits closed deals into segments using the strongest signals. Each row is a segment "
                    "you can target (top) or avoid (bottom). Segments are at least 3% of deals so they're not flukes.")
        html = []
        for r in dr["rules"].itertuples():
            color = WON if r.win_rate > base else LOST
            chips = "".join(f"<span class='chip'>{c}</span>" for c in r.conditions) or "<span class='chip'>All deals</span>"
            html.append(f"<div class='seg'><div class='seg-rate' style='color:{color}'>{r.win_rate:.0%}</div>"
                        f"<div class='seg-body'>{chips}<div class='seg-meta'>{r.won} won of {r.deals} deals · {r.lift:.2f}× average</div></div>"
                        f"<div class='seg-bar'><div style='width:{r.win_rate * 100:.0f}%;background:{color}'></div></div></div>")
        st.markdown("".join(html), unsafe_allow_html=True)

    st.markdown("#### Two-field heatmap")
    hf = sig["fields"][sig["fields"]["strength"] != "Leakage suspected"]
    icp_first = pd.concat([hf[hf["source"] != "Activity"], hf[hf["source"] == "Activity"]])
    cat_feats = icp_first["label"].tolist()
    if len(cat_feats) >= 2:
        c1, c2 = st.columns(2)
        fa = c1.selectbox("Rows", cat_feats, index=0)
        fb = c2.selectbox("Columns", cat_feats, index=1)
        ka = sig["fields"].loc[sig["fields"]["label"] == fa, "feature"].iloc[0]
        kb = sig["fields"].loc[sig["fields"]["label"] == fb, "feature"].iloc[0]
        closed = wide[wide["outcome"].isin(["Won", "Lost"])]
        def grp(k):
            s = closed[k]
            return (numeric_bins(s) if pd.api.types.is_numeric_dtype(s) and s.nunique() > 8 else s).astype("object").fillna("(blank)").astype(str)
        ga, gb = grp(ka), grp(kb)
        topa, topb = ga.value_counts().head(10).index, gb.value_counts().head(10).index
        sub = pd.DataFrame({"a": ga, "b": gb, "y": closed["is_won"]})
        sub = sub[sub["a"].isin(topa) & sub["b"].isin(topb)]
        piv = sub.pivot_table(index="a", columns="b", values="y", aggfunc=["mean", "count"])
        rate, cnt = piv["mean"], piv["count"]

        def natural(labels):
            keys = [range_key(l) for l in labels]
            return sorted(labels, key=lambda l: range_key(l)) if all(k is not None for k in keys) else list(labels)
        rows_o, cols_o = natural(rate.index), natural(rate.columns)
        rate, cnt = rate.loc[rows_o, cols_o], cnt.loc[rows_o, cols_o]
        txt = rate.map(lambda v: "" if pd.isna(v) else f"{v:.0%}") + cnt.map(lambda v: "" if pd.isna(v) else f"<br>n={int(v)}")
        rate = rate.where(cnt >= min_n)
        fig = go.Figure(go.Heatmap(z=rate.values, x=rate.columns.astype(str), y=rate.index.astype(str), text=txt.values,
                                   texttemplate="%{text}", colorscale="RdYlGn", zmid=base, zmin=0, zmax=1,
                                   colorbar=dict(title="Win rate", tickformat=".0%")))
        fig.update_layout(height=max(350, 45 * len(rate) + 120), margin=dict(l=10, r=10, t=20, b=10))
        st.plotly_chart(fig, use_container_width=True)
        explain(f"Cells with fewer than {min_n} deals are blank (too small to trust). Green = above-average win rate.")

# ============ REVENUE & CYCLE
with tabs[4]:
    st.subheader("Where the money is")
    seg_opts = sig["fields"][sig["fields"]["source"].isin(["Account", "Contact", "Deal"]) &
                             (sig["fields"]["strength"] != "Leakage suspected")]
    if not seg_opts.empty:
        pick = st.selectbox("Break revenue down by", seg_opts["label"].tolist(), key="rev_seg")
        feat = seg_opts.loc[seg_opts["label"] == pick, "feature"].iloc[0]
        col_feat = wide[feat]
        w2 = wide.copy()
        if pd.api.types.is_numeric_dtype(col_feat) and col_feat.nunique() > 8:
            w2[feat] = numeric_bins(col_feat)
        sv = A.segment_value(w2, feat)
        sv = sv[sv["n"] >= min_n].sort_values("won_revenue", ascending=False)
        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(sv, x="value", y="won_revenue", labels={"value": pick, "won_revenue": f"Won revenue ({currency})"},
                         color_discrete_sequence=[ACCENT], title="Won revenue by segment")
            fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = px.scatter(sv, x="rate", y="avg_won_deal", size="n", text="value", title="Win rate vs deal size (bubble = deals)",
                             labels={"rate": "Win rate", "avg_won_deal": f"Avg won deal ({currency})"})
            fig.update_traces(textposition="top center", marker_color=ACCENT)
            fig.add_vline(x=base, line_dash="dash", line_color="#888")
            fig.update_layout(xaxis_tickformat=".0%", margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
        explain("Top-right of the bubble chart = segments that win often AND pay well — the heart of your ICP. "
                "'Expected value per deal' below = win rate × average won deal.")
        st.dataframe(sv[["value", "n", "rate", "avg_won_deal", "won_revenue", "revenue_share", "median_cycle_won", "expected_value_per_deal"]],
                     hide_index=True, use_container_width=True, column_config={
                         "value": pick, "n": "Closed deals", "rate": st.column_config.ProgressColumn("Win rate", format="percent", min_value=0, max_value=1),
                         "avg_won_deal": st.column_config.NumberColumn("Avg won deal", format="%.0f"),
                         "won_revenue": st.column_config.NumberColumn("Won revenue", format="%.0f"),
                         "revenue_share": st.column_config.NumberColumn("Revenue share", format="percent"),
                         "median_cycle_won": st.column_config.NumberColumn("Median cycle (days)", format="%.0f"),
                         "expected_value_per_deal": st.column_config.NumberColumn("Expected value / deal", format="%.0f")})

    c1, c2 = st.columns(2)
    with c1:
        closed = deals[deals["outcome"].isin(["Won", "Lost"])]
        fig = px.histogram(closed, x="cycle_days", color="outcome", barmode="overlay", nbins=40, opacity=.65,
                           color_discrete_map={"Won": WON, "Lost": LOST}, title="Sales cycle length (days)",
                           labels={"cycle_days": "Days from created to close"})
        fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)", legend_title_text="")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        rc = A.revenue_concentration(deals, D["clean_accounts"])
        if not rc.empty:
            fig = px.line(rc, x="account_pct", y="cum_share", title="Revenue concentration",
                          labels={"account_pct": "Share of won accounts (largest first)", "cum_share": "Share of won revenue"})
            fig.update_traces(line_color=ACCENT)
            fig.update_layout(xaxis_tickformat=".0%", yaxis_tickformat=".0%", margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
            top20 = rc.loc[rc["account_pct"] <= 0.2, "cum_share"].max()
            st.plotly_chart(fig, use_container_width=True)
            if pd.notna(top20):
                explain(f"The top 20% of customers bring {top20:.0%} of won revenue.")
    if not rc.empty:
        with st.expander("Top customers by won revenue"):
            st.dataframe(rc[["account", "amount", "cum_share"]].head(25), hide_index=True, use_container_width=True)

# ============ PIPELINE & LOSSES
with tabs[5]:
    st.subheader("Pipeline flow and why deals are lost")
    c1, c2 = st.columns(2)
    with c1:
        op = A.open_pipeline(deals, stage_order)
        if not op.empty:
            fig = px.bar(op, x="Stage", y="amount", text="deals", title="Open pipeline by stage (label = deals)",
                         color_discrete_sequence=[OPEN], labels={"amount": f"Amount ({currency})"})
            fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
    with c2:
        sf = A.stage_funnel(D["clean_stage_history"], deals, stage_order)
        if not sf.empty:
            fig = go.Figure(go.Funnel(y=sf["stage"], x=sf["deals_reached"], textinfo="value+percent initial", marker_color=ACCENT))
            fig.update_layout(title="Closed deals: how far they got", margin=dict(l=10, r=10, t=40, b=10))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Stage history not extracted. Run `python cli.py extract --stage-history` to see where deals drop off.")
    if not sf.empty:
        st.dataframe(sf, hide_index=True, use_container_width=True, column_config={
            "reach_pct": st.column_config.NumberColumn("Reached", format="percent"),
            "win_rate_after": st.column_config.ProgressColumn("Win rate once here", format="percent", min_value=0, max_value=1),
            "median_days_won": st.column_config.NumberColumn("Median days in stage (won)", format="%.0f"),
            "median_days_lost": st.column_config.NumberColumn("Median days in stage (lost)", format="%.0f")})
        explain("If lost deals sit much longer in a stage than won deals, that stage is where deals quietly die.")
    la = A.loss_analysis(deals)
    c1, c2 = st.columns(2)
    with c1:
        if "reasons" in la:
            fig = px.bar(la["reasons"].iloc[::-1], x="deals", y="reason", orientation="h", title="Loss reasons",
                         color_discrete_sequence=[LOST], labels={"reason": ""})
            fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
    with c2:
        if "died_at" in la:
            fig = px.bar(la["died_at"], x="stage", y="deals", title="Stage where lost deals stopped", color_discrete_sequence=[LOST])
            fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
    if "reason_by_stage" in la:
        with st.expander("Loss reason × stage"):
            st.dataframe(la["reason_by_stage"], use_container_width=True)
    if "competitors" in la:
        st.markdown("#### Win rate by competitor recorded")
        rate_chart(la["competitors"])

# ============ LEADS & SOURCES
with tabs[6]:
    st.subheader("Lead sources: volume → conversion → revenue")
    leads = D["clean_leads"]
    s2r = A.source_to_revenue(leads, deals)
    if not s2r.empty:
        st.dataframe(s2r, hide_index=True, use_container_width=True, column_config={
            "win_rate": st.column_config.ProgressColumn("Deal win rate", format="percent", min_value=0, max_value=1),
            "lead_conversion": st.column_config.ProgressColumn("Lead → deal conversion", format="percent", min_value=0, max_value=1),
            "revenue": st.column_config.NumberColumn("Won revenue", format="%.0f"),
            "avg_won_deal": st.column_config.NumberColumn("Avg won deal", format="%.0f")})
        explain("A source with many leads but low conversion and low win rate is expensive noise. Few leads + high win rate = invest more.")
    if not leads.empty:
        opts = [c for c in ("Lead_Source", "Industry", "employee_band", "Country", "function", "seniority", "Lead_Status", "Owner_Name") if c in leads]
        c1, c2 = st.columns([1, 2])
        pick = c1.selectbox("Lead conversion by", opts)
        lt = A.lead_funnel(leads, pick)
        lt = lt[lt["n"] >= min_n] if pick != "Lead_Status" else lt
        with c2:
            st.metric("Leads", f"{len(leads):,}", f"{leads['converted'].mean():.0%} converted", delta_color="off")
        rate_chart(order_values(lt), f"Lead conversion rate by {pick}", base_rate=leads["converted"].mean(), label="conversion rate")
        lc = leads.groupby(leads["Created_Time"].dt.to_period("M")).size().rename("leads").reset_index() if "Created_Time" in leads else pd.DataFrame()
        if not lc.empty:
            lc["Created_Time"] = lc["Created_Time"].astype(str)
            fig = px.bar(lc, x="Created_Time", y="leads", title="Leads created per month", color_discrete_sequence=[ACCENT])
            fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)", xaxis_title="")
            st.plotly_chart(fig, use_container_width=True)

# ============ ACTIVITIES
with tabs[7]:
    st.subheader("How won deals were worked vs lost deals")
    explain("Only activities logged before the deal closed are counted. These are process signals — they tell you how to sell, not who to sell to.")
    cmp = A.activity_compare(deals)
    if not cmp.empty:
        st.dataframe(cmp.rename(columns={"Won": "Median — won", "Lost": "Median — lost"}), use_container_width=True)
    c1, c2 = st.columns(2)
    with c1:
        rate_chart(A.activity_buckets(deals, "n_meetings"), "Win rate by number of meetings")
    with c2:
        rate_chart(A.activity_buckets(deals, "days_to_first_activity"), "Win rate by speed of first touch")
    c1, c2 = st.columns(2)
    with c1:
        rate_chart(A.activity_buckets(deals, "n_calls"), "Win rate by number of calls")
    with c2:
        acts = D["clean_activities"]
        if not acts.empty:
            mix = acts[acts["related_id"].isin(deals["Id"])].groupby("type").size().reset_index(name="count")
            fig = px.pie(mix, names="type", values="count", title="Activity mix", hole=.5)
            fig.update_layout(margin=dict(l=10, r=10, t=40, b=10))
            st.plotly_chart(fig, use_container_width=True)
    explain("Careful: longer deals naturally collect more activities. Use this to set process targets (e.g. '2+ meetings'), not to define the ICP.")

# ============ BUYER ROLES
with tabs[8]:
    st.subheader("Who is the buyer on won deals? (persona seeds)")
    explain("Based on the main contact on each deal. Titles are grouped into function and seniority automatically.")
    c1, c2 = st.columns(2)
    with c1:
        t = A.role_table(wide, "contact.seniority")
        rate_chart(t[t["n"] >= min_n].sort_values("rate", ascending=False) if not t.empty else t, "Win rate by contact seniority")
    with c2:
        t = A.role_table(wide, "contact.function")
        rate_chart(t[t["n"] >= min_n].sort_values("rate", ascending=False) if not t.empty else t, "Win rate by contact function")
    t = A.role_table(wide, "contact.title")
    if not t.empty:
        st.markdown("#### Exact titles")
        rate_df_view(t[t["n"] >= max(3, min_n // 2)].sort_values("won", ascending=False))

# ============ TRENDS
with tabs[9]:
    st.subheader("Trends over time")
    mt = A.monthly_trend(deals)
    fig = go.Figure()
    fig.add_bar(x=mt["month"], y=mt["created"], name="Deals created", marker_color=OPEN)
    fig.add_bar(x=mt["month"], y=mt["won"], name="Deals won", marker_color=WON)
    fig.update_layout(barmode="group", title="Deals created vs won per month", margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(mt, x="month", y="won_revenue", title=f"Won revenue by close month ({currency})", color_discrete_sequence=[WON])
        fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)", xaxis_title="")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        cw = A.cohort_win_rate(deals)
        if not cw.empty:
            fig = go.Figure(go.Scatter(x=cw["value"], y=cw["rate"], mode="lines+markers+text", text=[f"n={n}" for n in cw["n"]],
                                       textposition="top center", line_color=ACCENT,
                                       error_y=dict(type="data", symmetric=False, array=cw["ci_hi"] - cw["rate"], arrayminus=cw["rate"] - cw["ci_lo"])))
            fig.update_layout(title="Win rate by quarter the deal was created", yaxis_tickformat=".0%",
                              margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True)
            explain("Recent quarters may look worse only because their deals haven't closed yet.")

# ============ DATA
with tabs[10]:
    st.subheader("Browse and download the cleaned data")
    tables = {"Deals (one row per deal, all attributes)": wide, "Deals (cleaned)": deals, "Accounts": D["clean_accounts"],
              "Contacts": D["clean_contacts"], "Leads": D["clean_leads"], "Activities": D["clean_activities"],
              "Signal values": sig["values"], "Signal fields": sig["fields"]}
    name = st.selectbox("Table", list(tables))
    df = tables[name]
    st.caption(f"{len(df):,} rows × {df.shape[1]} columns")
    st.dataframe(df.head(2000), use_container_width=True)
    st.download_button("Download CSV", df.to_csv(index=False).encode(), file_name=f"{name.split(' (')[0].lower()}.csv")
    ex = D["meta_extract_log"]
    if not ex.empty:
        with st.expander("Extraction log"):
            st.dataframe(ex, hide_index=True, use_container_width=True)
