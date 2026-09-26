"""Business-level answers on top of the signal scan.

The raw scan tests every CRM field. People don't think in fields; they think in questions:
"which industries buy?", "how big are our customers?", "which lead sources work?".
This module maps each question to the best-filled CRM field that answers it, scores every
segment on the three things that make a customer type attractive (how often it wins, how much
it pays, how fast it closes) and turns the result into plain-English conclusions.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .signals import _as_groups, closed_deals
from .stats import rate_table

SPECIAL = {"(blank)", "Other (rare values)", "Filled"}
# Shown for context but never recommended: deal amounts are often typed in during the sale, so they partly
# reflect how far a deal got rather than who the customer is.
CONTEXT_ONLY = {"deal_size"}


@dataclass(frozen=True)
class Question:
    key: str
    name: str          # short tab label
    question: str      # what it answers
    pattern: str       # regex on field name + label


QUESTIONS = [
    Question("industry", "Industry", "Which industries buy from you?", r"industr|vertical|sector"),
    Question("size", "Company size", "How big are the companies that buy?",
             r"employee|company.?size|company.?type|account.?size|headcount|employee_band"),
    Question("market", "Market", "Which markets buy?", r"country|region|currency|territory|geo\b|billing_state"),
    Question("source", "Lead source", "Where do winning deals come from?", r"lead.?source|source|channel|campaign|referr"),
    Question("deal_type", "New vs existing", "New customers or existing ones?", r"^type$|deal.?type|business.?type"),
    Question("deal_size", "Deal size", "Which deal sizes close?", r"amount_band|deal size"),
    Question("use_case", "Use case", "What do they buy it for?", r"use.?case|product|solution|plan\b|service"),
    Question("buyer", "Buyer", "Who is the buyer?", r"seniority|function"),
]


def candidates(q: Question, sig: dict, min_n: int) -> pd.DataFrame:
    """CRM fields that answer a question, best first (filled most often, then most informative)."""
    f, v = sig["fields"], sig["values"]
    if f.empty:
        return f
    rx = re.compile(q.pattern, re.I)
    ok = f[(f["strength"] != "Leakage suspected") & f["source"].isin(["Account", "Deal", "Contact"])].copy()
    ok = ok[[bool(rx.search(f"{r.feature.split('.', 1)[-1]} {r.label}")) for r in ok.itertuples()]]
    usable = []
    for r in ok.itertuples():
        vals = v[(v["feature"] == r.feature) & ~v["value"].isin(SPECIAL) & (v["n"] >= min_n)]
        usable.append(len(vals) >= 2)
    ok = ok[usable]
    if ok.empty:
        return ok
    ok["score"] = ok["coverage"] + 0.3 * ok["effect"].fillna(0)
    return ok.sort_values("score", ascending=False)


def scorecard(wide: pd.DataFrame, feature: str, kind: str, min_n: int) -> pd.DataFrame:
    """One row per segment: deals, win rate, deal size, speed, value per opportunity, verdict."""
    closed = closed_deals(wide)
    if closed.empty:
        return pd.DataFrame()
    groups, _ = _as_groups(closed[feature], kind, min_n)
    if groups is None:
        return pd.DataFrame()
    groups = groups.astype("object").fillna("(blank)").astype(str)
    base = closed["is_won"].mean()
    t = rate_table(groups, closed["is_won"], base)
    won = closed[closed["is_won"] == 1]
    paid = won[won["amount"] > 0]
    wg, pg = groups.loc[won.index], groups.loc[paid.index]
    # typical (median) won deal: one giant deal can't make a whole group look attractive
    t["avg_deal"] = t["value"].map(paid.groupby(pg)["amount"].median())
    t["days_to_close"] = t["value"].map(won.groupby(wg)["cycle_days"].median())
    t["revenue"] = t["value"].map(paid.groupby(pg)["amount"].sum()).fillna(0)
    total_rev = t["revenue"].sum()
    t["revenue_share"] = t["revenue"] / total_rev if total_rev else np.nan
    overall_deal = paid["amount"].median()
    t["value_per_opp"] = t["rate"] * t["avg_deal"].fillna(overall_deal)
    overall_value = base * overall_deal if pd.notna(overall_deal) else np.nan
    t["verdict"] = [_verdict(r, overall_value, min_n) for r in t.itertuples()]
    t["label"] = t["value"].replace({"(blank)": "Not recorded", "Other (rare values)": "Other (small groups)"})
    return t


def _verdict(r, overall_value: float, min_n: int) -> str:
    if r.value in SPECIAL:
        return "—"
    if r.n < min_n:
        return "Too little data"
    rich = (pd.notna(overall_value) and pd.notna(r.value_per_opp) and r.value_per_opp >= 1.5 * overall_value
            and r.won >= 5 and r.n >= max(min_n, 20))  # value-based focus needs enough wins to trust the deal size
    if r.direction == "Better" or (rich and r.direction != "Worse"):
        return "Focus"
    if r.direction == "Worse":
        return "Deprioritize"
    return "Average"


def answer(q: Question, sig: dict, wide: pd.DataFrame, min_n: int, feature: str | None = None) -> dict | None:
    """Everything needed to show one question: chosen field, alternatives, scorecard."""
    cands = candidates(q, sig, min_n)
    if cands.empty:
        return None
    row = cands[cands["feature"] == feature].iloc[0] if feature in set(cands["feature"]) else cands.iloc[0]
    card = scorecard(wide, row["feature"], row["kind"], min_n)
    if card.empty:
        return None
    return {"question": q, "feature": row["feature"], "label": row["label"], "coverage": row["coverage"],
            "strength": row["strength"], "alternatives": cands[["feature", "label", "coverage"]], "card": card}


def all_answers(sig: dict, wide: pd.DataFrame, min_n: int) -> dict[str, dict]:
    out = {}
    for q in QUESTIONS:
        a = answer(q, sig, wide, min_n)
        if a:
            out[q.key] = a
    return out


def conclusions(answers: dict[str, dict], base: float, money) -> dict[str, list[str]]:
    """Plain-English 'focus / deprioritize / fix' statements, strongest first."""
    focus, avoid, fix = [], [], []
    for key, a in answers.items():
        if key in CONTEXT_ONLY:
            continue
        card, q = a["card"], a["question"]
        name = q.name.lower()
        good = card[card["verdict"] == "Focus"].sort_values("rate", ascending=False).head(3)
        bad = card[card["verdict"] == "Deprioritize"].sort_values("rate").head(3)
        for r in good.itertuples():
            extra = f", typical deal {money(r.avg_deal)}" if pd.notna(r.avg_deal) else ""
            focus.append((r.rate / base if base else 0,
                          f"<b>{r.label}</b> <span class='muted'>({name})</span> — wins <b>{r.rate:.0%}</b> of deals "
                          f"vs {base:.0%} average{extra} · {r.n} deals"))
        for r in bad.itertuples():
            avoid.append((base / r.rate if r.rate else 99,
                          f"<b>{r.label}</b> <span class='muted'>({name})</span> — wins only <b>{r.rate:.0%}</b> "
                          f"vs {base:.0%} average · {r.n} deals"))
        if a["coverage"] < 0.6:
            fix.append(f"<b>{q.name}</b> is recorded on only {a['coverage']:.0%} of deals (field “{a['label']}”). "
                       f"Filling it in would make this answer much more reliable.")
    focus = [s for _, s in sorted(focus, key=lambda x: -x[0])][:7]
    avoid = [s for _, s in sorted(avoid, key=lambda x: -x[0])][:6]
    return {"focus": focus, "avoid": avoid, "fix": fix}
