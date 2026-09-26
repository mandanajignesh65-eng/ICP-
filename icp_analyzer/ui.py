"""Design system for the dashboard: calm, light, Apple-like. Colors, type, chart template, components."""
from __future__ import annotations

from contextlib import contextmanager
from itertools import count

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

# ---------------------------------------------------------------- tokens
BG = "#F5F5F7"
CARD = "#FFFFFF"
INK = "#1D1D1F"
INK_2 = "#6E6E73"
INK_3 = "#86868B"
HAIR = "#E8E8ED"
BLUE = "#0071E3"
GREEN = "#34C759"
GREEN_INK = "#248A3D"
RED = "#FF3B30"
RED_INK = "#D70015"
ORANGE = "#FF9500"
INDIGO = "#5E5CE6"
TEAL = "#30B0C7"
MUTED = "#D2D2D7"
FONT = "Inter, -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif"

DIRECTION = {"Better": GREEN, "Worse": RED, "Not different": MUTED, "Too few": "#E5E5EA"}
SOURCE = {"Account": BLUE, "Contact": INDIGO, "Deal": TEAL, "Activity": "#AEAEB2", "Process": "#C7C7CC",
          "Team": ORANGE, "Time": "#D1D1D6"}
STRENGTH = {"Strong": BLUE, "Moderate": "#5AA2F0", "Weak": "#B7D4F7", "No clear signal": "#E5E5EA"}
DIVERGING = [[0, "#FF3B30"], [0.35, "#FFB3AE"], [0.5, "#F2F2F7"], [0.65, "#A8E6B8"], [1, "#248A3D"]]

pio.templates["clean"] = go.layout.Template(layout=dict(
    font=dict(family=FONT, size=13, color=INK),
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    colorway=[BLUE, INDIGO, TEAL, ORANGE, GREEN, RED, "#AEAEB2"],
    margin=dict(l=8, r=16, t=8, b=8),
    xaxis=dict(showgrid=False, zeroline=False, linecolor=HAIR, ticks="", automargin=True, tickfont=dict(color=INK_3, size=12),
               title=dict(font=dict(color=INK_3, size=12))),
    yaxis=dict(showgrid=True, gridcolor="#F0F0F3", zeroline=False, linecolor="rgba(0,0,0,0)", ticks="", automargin=True,
               tickfont=dict(color=INK_2, size=12), title=dict(font=dict(color=INK_3, size=12))),
    hoverlabel=dict(bgcolor="white", bordercolor=HAIR, font=dict(family=FONT, color=INK, size=12)),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0, font=dict(color=INK_2, size=12),
                bgcolor="rgba(0,0,0,0)", title=dict(text="")),
    barcornerradius=5, bargap=0.35,
))
pio.templates.default = "clean"
CHART_CONFIG = {"displayModeBar": False}

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"], .stMarkdown, button, input, textarea, select {{ font-family: {FONT} !important; }}
.stApp {{ background: {BG}; }}
header[data-testid="stHeader"] {{ background: transparent; height: 0; }}
[data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none; }}
.block-container, [data-testid="stMainBlockContainer"] {{ max-width: 1240px; padding: 2.2rem 2rem 4rem; }}
h1, h2, h3, h4 {{ color: {INK}; letter-spacing: -0.02em; }}
p, li {{ color: {INK}; }}
[class*="st-key-card"] {{ background: {CARD}; border-radius: 18px; padding: 22px 24px 16px;
    box-shadow: 0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.04); }}
.card-title {{ font-size: 1.02rem; font-weight: 600; color: {INK}; margin: 0; letter-spacing: -0.01em; }}
.card-sub {{ font-size: .85rem; color: {INK_3}; margin: .15rem 0 .4rem; line-height: 1.4; }}
.hero-title {{ font-size: 2.3rem; font-weight: 700; letter-spacing: -0.035em; color: {INK}; margin: 0; line-height: 1.1; }}
.hero-sub {{ font-size: 1.02rem; color: {INK_2}; margin: .35rem 0 0; }}
.kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 14px; margin: 0 0 14px; }}
.kpi {{ background: {CARD}; border-radius: 18px; padding: 18px 20px;
        box-shadow: 0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.04); }}
.kpi .l {{ font-size: .8rem; color: {INK_3}; font-weight: 500; }}
.kpi .v {{ font-size: 1.9rem; font-weight: 600; letter-spacing: -0.03em; color: {INK}; margin: .2rem 0 .1rem; }}
.kpi .s {{ font-size: .8rem; color: {INK_3}; min-height: 1.1em; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: .3rem; }}
.chip {{ display: inline-flex; align-items: baseline; gap: 6px; padding: 7px 12px; border-radius: 999px;
         background: #F5F5F7; font-size: .88rem; color: {INK}; }}
.chip b {{ font-weight: 600; }}
.chip .f {{ color: {INK_3}; font-size: .78rem; }}
.chip.good .r {{ color: {GREEN_INK}; font-weight: 600; }}
.chip.bad .r {{ color: {RED_INK}; font-weight: 600; }}
.seg {{ display: grid; grid-template-columns: 70px 1fr 180px; gap: 16px; align-items: center; padding: 14px 4px;
        border-bottom: 1px solid {HAIR}; }}
.seg:last-child {{ border-bottom: none; }}
.seg .rate {{ font-size: 1.5rem; font-weight: 600; letter-spacing: -0.02em; text-align: right; }}
.seg .meta {{ font-size: .8rem; color: {INK_3}; margin-top: 4px; }}
.seg .cond {{ display: inline-block; padding: 3px 10px; margin: 2px 6px 2px 0; border-radius: 8px; background: #F5F5F7; font-size: .86rem; }}
.bar {{ height: 6px; background: #F0F0F3; border-radius: 3px; overflow: hidden; }}
.bar > div {{ height: 100%; border-radius: 3px; }}
.note {{ font-size: .82rem; color: {INK_3}; margin: .6rem 0 0; }}
.stat {{ font-size: 2.6rem; font-weight: 600; letter-spacing: -0.03em; color: {INK}; line-height: 1; }}
.stat-l {{ font-size: .82rem; color: {INK_3}; margin-top: .3rem; }}
div[data-testid="stSegmentedControl"] {{ margin: 1.4rem 0 1.2rem; }}
div[data-testid="stExpander"] details {{ border: none; background: transparent; }}
div[data-testid="stExpander"] summary {{ color: {INK_2}; font-size: .88rem; }}
[data-testid="stPopover"] button {{ border-radius: 999px; }}
</style>
"""

_ids = count()


def inject():
    st.markdown(CSS, unsafe_allow_html=True)


@contextmanager
def card(title: str | None = None, sub: str | None = None):
    with st.container(key=f"card_{next(_ids)}"):
        if title:
            st.markdown(f"<p class='card-title'>{title}</p>" + (f"<p class='card-sub'>{sub}</p>" if sub else ""),
                        unsafe_allow_html=True)
        yield


def kpis(items: list[tuple[str, str, str]]):
    st.markdown("<div class='kpis'>" + "".join(
        f"<div class='kpi'><div class='l'>{l}</div><div class='v'>{v}</div><div class='s'>{s}</div></div>"
        for l, v, s in items) + "</div>", unsafe_allow_html=True)


def note(text: str):
    st.markdown(f"<p class='note'>{text}</p>", unsafe_allow_html=True)


def plot(fig: go.Figure, height: int | None = None):
    fig.update_layout(paper_bgcolor=CARD, plot_bgcolor=CARD)  # charts live on white cards
    if height:
        fig.update_layout(height=height)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG, theme=None)


def empty(msg="Not enough data yet."):
    st.markdown(f"<p class='card-sub' style='padding:1.5rem 0'>{msg}</p>", unsafe_allow_html=True)


# ---------------------------------------------------------------- charts
def pct(x) -> str:
    return "—" if pd.isna(x) else f"{x:.0%}"


def rate_bars(t: pd.DataFrame, base: float, label: str = "Win rate", max_rows: int = 14, height: int | None = None):
    """Horizontal bars of a rate per value, colored by whether it is confidently better/worse than average."""
    if t is None or t.empty:
        return empty()
    t = t.head(max_rows).iloc[::-1]
    fig = go.Figure(go.Bar(
        x=t["rate"], y=t["value"].astype(str), orientation="h",
        marker_color=[DIRECTION.get(d, MUTED) for d in t["direction"]],
        text=[pct(r) for r in t["rate"]], textposition="outside", cliponaxis=False,
        textfont=dict(color=INK_2, size=12),
        error_x=dict(type="data", symmetric=False, array=(t["ci_hi"] - t["rate"]).clip(lower=0),
                     arrayminus=(t["rate"] - t["ci_lo"]).clip(lower=0), color="rgba(0,0,0,.18)", thickness=1.2, width=0),
        customdata=t[["n", "won", "confidence"]].values,
        hovertemplate="<b>%{y}</b><br>" + label + " %{x:.0%}<br>%{customdata[1]} of %{customdata[0]} deals"
                      "<br>Confidence: %{customdata[2]}<extra></extra>"))
    if pd.notna(base):
        fig.add_vline(x=base, line_width=1, line_dash="dot", line_color=INK_3)
        fig.add_annotation(x=base, y=1, yref="paper", yanchor="bottom", text=f"avg {base:.0%}", showarrow=False,
                           font=dict(size=11, color=INK_3))
    xmax = min(1.0, float(max(t["ci_hi"].max(), t["rate"].max())) + 0.12)
    fig.update_layout(xaxis=dict(tickformat=".0%", range=[0, xmax], showgrid=True, gridcolor="#F0F0F3"),
                      yaxis=dict(showgrid=False), bargap=0.4)
    plot(fig, height or max(220, 34 * len(t) + 60))


def lift_chart(rows: pd.DataFrame, base: float):
    """Diverging bars: how many points above/below the average win rate each trait sits."""
    if rows.empty:
        return empty("No confident patterns yet.")
    r = rows.assign(diff=rows["rate"] - base).sort_values("diff")
    labels = [f"{l.split(' · ')[-1]}  ·  <b>{v}</b>" for l, v in zip(r["label"], r["value"])]
    fig = go.Figure(go.Bar(
        x=r["diff"], y=labels, orientation="h", marker_color=[GREEN if d > 0 else RED for d in r["diff"]],
        text=[f"{x:.0%}" for x in r["rate"]], textposition="outside", cliponaxis=False, textfont=dict(color=INK_2, size=12),
        customdata=r[["n", "confidence", "lift"]].values,
        hovertemplate="%{y}<br>Win rate %{text} (%{customdata[2]:.1f}× average)<br>%{customdata[0]} deals · "
                      "%{customdata[1]} confidence<extra></extra>"))
    lim = float(r["diff"].abs().max()) * 1.35
    fig.update_layout(xaxis=dict(range=[-lim, lim], tickformat="+.0%", showgrid=True, gridcolor="#F0F0F3",
                                 title="Win rate vs average (percentage points)"),
                      yaxis=dict(showgrid=False, automargin=True), bargap=0.45)
    fig.add_vline(x=0, line_width=1, line_color=MUTED)
    plot(fig, max(260, 36 * len(r) + 70))


def chips(rows: pd.DataFrame, kind: str):
    if rows.empty:
        return empty("Nothing confident yet.")
    html = "".join(f"<span class='chip {kind}'><span class='f'>{l.split(' · ')[-1]}</span><b>{v}</b>"
                   f"<span class='r'>{pct(r)}</span></span>" for l, v, r in zip(rows["label"], rows["value"], rows["rate"]))
    st.markdown(f"<div class='chips'>{html}</div>", unsafe_allow_html=True)


def segments(rules: pd.DataFrame, base: float):
    html = []
    for r in rules.itertuples():
        color = GREEN_INK if r.win_rate > base else RED_INK
        fill = GREEN if r.win_rate > base else RED
        conds = "".join(f"<span class='cond'>{c}</span>" for c in r.conditions) or "<span class='cond'>All deals</span>"
        html.append(f"<div class='seg'><div class='rate' style='color:{color}'>{r.win_rate:.0%}</div>"
                    f"<div>{conds}<div class='meta'>{r.won} won of {r.deals} deals · {r.lift:.1f}× average</div></div>"
                    f"<div class='bar'><div style='width:{r.win_rate * 100:.0f}%;background:{fill}'></div></div></div>")
    st.markdown("".join(html), unsafe_allow_html=True)
