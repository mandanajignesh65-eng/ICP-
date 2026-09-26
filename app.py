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
from icp_analyzer import ui
from icp_analyzer.config import default_db_path
from icp_analyzer.signals import drivers, scan
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
def run_drivers(wide, fields, sources):
    return drivers(wide, fields[fields["source"].isin(sources)])


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
        dtypes = sorted(deals_all["Type"].dropna().unique()) if "Type" in deals_all else []
        sel_types = st.multiselect("Deal type", dtypes, placeholder="All deal types",
                                   help="Pick 'New Business' to learn who becomes a NEW customer — expansion deals "
                                        "with existing clients win far more often and can inflate the picture.") if dtypes else []
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
if sel_types:
    mask &= deals_all["Type"].isin(sel_types)
deals = deals_all[mask]
wide = D["deal_wide"][D["deal_wide"]["deal_id"].isin(deals["Id"])]
sig = run_scan(wide, D["feature_catalog"], min_n)
base = sig["base_rate"]
ov = A.revenue_overview(deals)
fields = sig["fields"]
usable = fields[fields["strength"] != "Leakage suspected"] if not fields.empty else fields

with head_l:
    st.markdown(f"<div class='hero-title'>{org.get('company_name', 'CRM')}</div>"
                f"<div class='hero-sub'>{sig['closed']:,} closed deals analyzed · average win rate {pct(base)}</div>",
                unsafe_allow_html=True)

SECTIONS = ["Overview", "Signals", "Segments", "Revenue", "Pipeline", "Leads", "Buyers", "Sales motion", "Data quality"]
section = st.segmented_control("Section", SECTIONS, default="Overview", key="section", label_visibility="collapsed") or "Overview"

if sig["closed"] < 30:
    st.warning(f"Only {sig['closed']} closed deals in this selection. Treat patterns as hypotheses.")


def group_values(feature: str, frame: pd.DataFrame) -> pd.Series:
    s = frame[feature]
    if pd.api.types.is_numeric_dtype(s) and s.nunique() > 8:
        s = numeric_bins(s)
    return s.astype("object").fillna("(blank)").astype(str)


# ================================================================== OVERVIEW
if section == "Overview":
    cyc = f"{ov['median_cycle_won']:.0f} days" if pd.notna(ov["median_cycle_won"]) else "—"
    ui.kpis([
        ("Win rate", pct(ov["win_rate"]), f"{ov['won']:,} won · {ov['lost']:,} lost"),
        ("Won revenue", money(ov["won_revenue"]), f"{ov['deals']:,} deals total"),
        ("Average deal", money(ov["avg_won_deal"]), f"median {money(ov['median_won_deal'])}"),
        ("Sales cycle", cyc, "median for won deals"),
        ("Open pipeline", money(ov["open_pipeline"]), f"{ov['open']:,} open deals"),
    ])

    with card("What moves the win rate",
              "Customer and deal traits that win confidently more (green) or less (red) than average. Hover for sample sizes."):
        ui.lift_chart(A.top_moves(sig, limit=12, per_field=2), base)

    draft = A.icp_draft(sig)
    c1, c2 = st.columns(2)
    with c1:
        with card("Ideal customer", "Traits with a win rate confidently above average."):
            ui.chips(draft[draft["verdict"].str.contains("Target")] if not draft.empty else draft, "good")
    with c2:
        with card("Deprioritize", "Traits with a win rate confidently below average."):
            ui.chips(draft[draft["verdict"].str.contains("Avoid")] if not draft.empty else draft, "bad")

    c1, c2 = st.columns(2)
    with c1:
        with card("Strongest signals", "How strongly each customer or deal field separates won from lost deals."):
            top = usable[usable["strength"].isin(["Strong", "Moderate", "Weak"]) & (usable["source"] != "Activity")].head(10).sort_values("effect")
            if top.empty:
                ui.empty()
            else:
                fig = go.Figure(go.Bar(x=top["effect"], y=top["label"], orientation="h",
                                       marker_color=[ui.SOURCE.get(s, ui.MUTED) for s in top["source"]],
                                       hovertemplate="%{y}<br>Effect size %{x:.2f}<extra></extra>"))
                fig.update_layout(xaxis=dict(title="Effect size", range=[0, max(0.3, top["effect"].max() * 1.15)]),
                                  yaxis=dict(showgrid=False))
                plot(fig, max(260, 30 * len(top) + 60))
                note("Blue: company · Purple: contact · Teal: deal")
    with c2:
        with card("Momentum", "Deals created and won each month."):
            mt = A.monthly_trend(deals)
            fig = go.Figure()
            fig.add_scatter(x=mt["month"], y=mt["created"], name="Created", mode="lines", line=dict(color=ui.MUTED, width=2),
                            fill="tozeroy", fillcolor="rgba(210,210,215,.25)")
            fig.add_scatter(x=mt["month"], y=mt["won"], name="Won", mode="lines", line=dict(color=ui.GREEN, width=2.5),
                            fill="tozeroy", fillcolor="rgba(52,199,89,.12)")
            fig.update_layout(hovermode="x unified")
            plot(fig, 330)

    leaks = fields[fields["strength"] == "Leakage suspected"] if not fields.empty else fields
    if len(leaks):
        note(f"{len(leaks)} field(s) excluded because they are only filled after a deal closes: "
             + ", ".join(leaks["label"]) + ".")

# ================================================================== SIGNALS
elif section == "Signals":
    with card("Every field, ranked", f"{len(usable)} fields tested against {sig['closed']:,} closed deals. "
              "Longer bar = stronger separation between won and lost. Faded = not statistically reliable. "
              "Team (who sold it), Process (how far the deal moved) and Time fields are shown for context "
              "but never used for the ICP."):
        if usable.empty:
            ui.empty()
        else:
            u = usable.iloc[::-1]
            fig = go.Figure(go.Bar(
                x=u["effect"], y=u["label"], orientation="h",
                marker_color=[ui.STRENGTH.get(s, ui.MUTED) for s in u["strength"]],
                customdata=np.stack([u["strength"], u["q_value"].fillna(1), u["coverage"]], axis=1),
                hovertemplate="<b>%{y}</b><br>Effect %{x:.2f} · %{customdata[0]}<br>q-value %{customdata[1]:.3f}"
                              "<br>Filled %{customdata[2]:.0%}<extra></extra>"))
            fig.update_layout(xaxis=dict(title="Effect size (0 = none, 1 = perfect)"), yaxis=dict(showgrid=False))
            plot(fig, max(320, 26 * len(u) + 60))

    with card("Look inside a field", "Win rate for each value. The thin line is the 95% confidence range."):
        if not usable.empty:
            pick = st.selectbox("Field", usable["label"].tolist(), label_visibility="collapsed")
            feat = usable.loc[usable["label"] == pick, "feature"].iloc[0]
            t = sig["values"][sig["values"]["feature"] == feat]
            ui.rate_bars(order_values(t), base)
            with st.expander("Show numbers"):
                st.dataframe(t[["value", "n", "won", "rate", "ci_lo", "ci_hi", "lift", "confidence"]], hide_index=True,
                             use_container_width=True, column_config={
                                 "value": "Value", "n": "Deals", "won": "Won",
                                 "rate": st.column_config.NumberColumn("Win rate", format="percent"),
                                 "ci_lo": st.column_config.NumberColumn("Low", format="percent"),
                                 "ci_hi": st.column_config.NumberColumn("High", format="percent"),
                                 "lift": st.column_config.NumberColumn("Lift", format="%.2f×"), "confidence": "Confidence"})

    with st.expander("Excluded fields"):
        leaks = fields[fields["strength"] == "Leakage suspected"] if not fields.empty else fields
        if len(leaks):
            st.dataframe(leaks[["label", "leakage"]].rename(columns={"label": "Field", "leakage": "Why excluded"}),
                         hide_index=True, use_container_width=True)
        if not sig["skipped"].empty:
            st.dataframe(sig["skipped"][["label", "reason"]].rename(columns={"label": "Field", "reason": "Not testable"}),
                         hide_index=True, use_container_width=True)

# ================================================================== SEGMENTS
elif section == "Segments":
    inc_act = st.toggle("Include sales activity", value=False, help="Off: only who the customer is. On: also how the deal was worked.")
    srcs = ("Account", "Contact", "Deal", "Activity") if inc_act else ("Account", "Contact", "Deal")
    dr = run_drivers(wide, fields, srcs)
    with card("Winning combinations", "Groups of deals that share traits, found by a shallow decision tree. "
              "Each group holds at least 3% of deals, so none is a fluke."):
        if dr["rules"].empty:
            ui.empty("Not enough closed deals or signals to form segments.")
        else:
            ui.segments(dr["rules"], base)
            if pd.notna(dr["auc"]):
                strength = "strong" if dr["auc"] >= .8 else ("useful" if dr["auc"] >= .7 else ("modest" if dr["auc"] >= .6 else "weak"))
                note(f"Predictive power (cross-validated AUC): {dr['auc']:.2f} — {strength}. 0.5 is a coin flip.")

    with card("Two traits together", f"Win rate for every combination. Blank cells have fewer than {min_n} deals."):
        opts = pd.concat([usable[usable["source"] != "Activity"], usable[usable["source"] == "Activity"]])["label"].tolist()
        if len(opts) >= 2:
            c1, c2 = st.columns(2)
            fa = c1.selectbox("Rows", opts, index=0)
            fb = c2.selectbox("Columns", opts, index=1)
            ka = usable.loc[usable["label"] == fa, "feature"].iloc[0]
            kb = usable.loc[usable["label"] == fb, "feature"].iloc[0]
            closed = wide[wide["outcome"].isin(["Won", "Lost"])]
            ga, gb = group_values(ka, closed), group_values(kb, closed)
            sub = pd.DataFrame({"a": ga, "b": gb, "y": closed["is_won"]})
            sub = sub[sub["a"].isin(ga.value_counts().head(10).index) & sub["b"].isin(gb.value_counts().head(8).index)]
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

# ================================================================== REVENUE
elif section == "Revenue":
    seg_opts = usable[usable["source"].isin(["Account", "Contact", "Deal"])]
    if seg_opts.empty:
        ui.empty()
    else:
        pick = st.selectbox("Break down by", seg_opts["label"].tolist())
        feat = seg_opts.loc[seg_opts["label"] == pick, "feature"].iloc[0]
        w2 = wide.copy()
        w2[feat] = group_values(feat, w2)
        sv = A.segment_value(w2, feat)
        sv = sv[(sv["n"] >= min_n) & (sv["value"] != "(blank)")]
        c1, c2 = st.columns([3, 2])
        with c1:
            with card("Win rate × deal size", "Top-right is the sweet spot: wins often and pays well. Bubble size = number of deals."):
                fig = go.Figure(go.Scatter(
                    x=sv["rate"], y=sv["avg_won_deal"], mode="markers+text", text=sv["value"], textposition="top center",
                    textfont=dict(size=11, color=ui.INK_2),
                    marker=dict(size=np.sqrt(sv["n"]) * 4 + 6, color=ui.BLUE, opacity=.55, line=dict(width=0)),
                    customdata=sv[["n", "won_revenue"]].values,
                    hovertemplate="<b>%{text}</b><br>Win rate %{x:.0%}<br>Avg deal %{y:,.0f}<br>%{customdata[0]} deals<extra></extra>"))
                fig.add_vline(x=base, line_width=1, line_dash="dot", line_color=ui.INK_3)
                fig.update_layout(xaxis=dict(tickformat=".0%", title="Win rate", showgrid=True, gridcolor="#F0F0F3"),
                                  yaxis=dict(title="Average won deal"))
                plot(fig, 420)
        with c2:
            with card("Share of won revenue", pick):
                s2 = sv.sort_values("won_revenue", ascending=True).tail(10)
                fig = go.Figure(go.Bar(x=s2["won_revenue"], y=s2["value"], orientation="h", marker_color=ui.BLUE,
                                       text=[f"{x:.0%}" for x in s2["revenue_share"]], textposition="outside",
                                       cliponaxis=False, textfont=dict(color=ui.INK_2),
                                       hovertemplate="%{y}<br>%{x:,.0f}<extra></extra>"))
                fig.update_layout(yaxis=dict(showgrid=False), xaxis=dict(showticklabels=False))
                plot(fig, 420)

    c1, c2 = st.columns(2)
    closed = deals[deals["outcome"].isin(["Won", "Lost"])]
    with c1:
        with card("Sales cycle", "Days from created to closed."):
            fig = go.Figure()
            for name, color in (("Lost", ui.RED), ("Won", ui.GREEN)):
                fig.add_histogram(x=closed.loc[closed["outcome"] == name, "cycle_days"], name=name, marker_color=color,
                                  opacity=.55, nbinsx=35)
            fig.update_layout(barmode="overlay", bargap=.05, xaxis_title="Days")
            plot(fig, 320)
    with c2:
        with card("Revenue concentration", "Share of won revenue from the largest customers."):
            rc = A.revenue_concentration(deals, D["clean_accounts"])
            if rc.empty:
                ui.empty()
            else:
                fig = go.Figure(go.Scatter(x=rc["account_pct"], y=rc["cum_share"], mode="lines", line=dict(color=ui.BLUE, width=2.5),
                                           fill="tozeroy", fillcolor="rgba(0,113,227,.08)",
                                           hovertemplate="Top %{x:.0%} of customers → %{y:.0%} of revenue<extra></extra>"))
                fig.update_layout(xaxis=dict(tickformat=".0%", title="Customers, largest first"), yaxis=dict(tickformat=".0%"))
                plot(fig, 320)
                top20 = rc.loc[rc["account_pct"] <= .2, "cum_share"].max()
                if pd.notna(top20):
                    note(f"The top 20% of customers bring {top20:.0%} of won revenue.")

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

# ================================================================== LEADS
elif section == "Leads":
    leads = D["clean_leads"]
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
elif section == "Sales motion":
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
