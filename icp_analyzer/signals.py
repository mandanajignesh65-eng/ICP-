"""Signal scanner: test every field against the deal outcome (won vs lost).

For each field it answers: does this field separate winners from losers, how
strongly, how sure are we, and which values are better or worse than average.
Leakage (fields only filled after a deal closes) is detected and excluded.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

from .stats import _fmt, association, fdr, mann_whitney, numeric_bins, rate_table

LEAKY_NAME = re.compile(
    r"(won|lost|loss|reason|onboard|contract|invoice|payment|paid|signed|renewal|churn|clos|"
    r"purchase.?order|kick.?off|go.?live|implementation|handover|probability|expected.?revenue|forecast|"
    r"duration|cycle|competitor)", re.I)
MAX_CATEGORIES = 30


def closed_deals(wide: pd.DataFrame) -> pd.DataFrame:
    return wide[wide["outcome"].isin(["Won", "Lost"])].copy()


def _as_groups(s: pd.Series, kind: str, min_n: int) -> tuple[pd.Series | None, str | None]:
    """Turn a raw column into groups to compare. Returns (groups, skip_reason)."""
    coverage = s.notna().mean()

    def presence():
        # dates / free text: the only testable thing is whether the field is filled
        if coverage > 0.95:
            return None, "Always filled — nothing to compare"
        return s.notna().map({True: "Filled", False: "(blank)"}), None

    if kind == "date":
        return presence()
    if kind == "numeric":
        if s.nunique(dropna=True) <= 1:
            return None, "Only one value"
        return numeric_bins(s), None
    v = s.astype("object")
    uniq = v.nunique(dropna=True)
    if uniq <= 1:
        return None, "Only one value"
    if kind == "text" and uniq > MAX_CATEGORIES:
        return presence()
    if uniq > MAX_CATEGORIES * 3:
        return None, f"Too many distinct values ({uniq})"
    counts = v.value_counts()
    rare = counts[counts < min_n].index
    return v.where(~v.isin(rare), "Other (rare values)"), None


def scan(wide: pd.DataFrame, catalog: pd.DataFrame, min_n: int = 10) -> dict[str, pd.DataFrame]:
    df = closed_deals(wide)
    y = df["is_won"]
    base = y.mean() if len(df) else np.nan
    fields, values, skipped = [], [], []
    for r in catalog.itertuples():
        s = df[r.feature]
        coverage = s.notna().mean() if len(s) else 0
        if coverage < 0.05:
            skipped.append({"feature": r.feature, "label": r.label, "reason": f"Almost empty ({coverage:.0%} filled)"})
            continue
        groups, reason = _as_groups(s, r.kind, min_n)
        if groups is None:
            skipped.append({"feature": r.feature, "label": r.label, "reason": reason})
            continue
        groups = groups.astype("object").fillna("(blank)")
        p, v = association(groups, y)
        t = rate_table(groups, y, base)

        # leakage checks
        fill_won = s[y == 1].notna().mean() if (y == 1).any() else 0
        fill_lost = s[y == 0].notna().mean() if (y == 0).any() else 0
        leak = []
        if abs(fill_won - fill_lost) >= 0.5:
            leak.append(f"filled for {fill_won:.0%} of won vs {fill_lost:.0%} of lost deals")
        elif fill_won >= 0.08 and fill_won >= 4 * max(fill_lost, 0.005) and r.source != "Activity":
            leak.append(f"mostly filled on won deals ({fill_won:.0%} of won vs {fill_lost:.0%} of lost) — likely entered after the sale")
        if r.source not in ("Account", "Contact", "Activity") and (LEAKY_NAME.search(str(r.field or "")) or LEAKY_NAME.search(str(r.label))):
            leak.append("name suggests it is set when/after the deal closes")
        if r.source == "Account" and re.search(r"(account_type|customer_status|lifecycle|stage|client_status)", str(r.field or ""), re.I):
            leak.append("account status (e.g. 'Customer') is updated after a sale")
        if v > 0.8:
            leak.append("separates won/lost almost perfectly")

        mw = mann_whitney(s[y == 1], s[y == 0]) if r.kind == "numeric" else np.nan
        real = t[~t["value"].isin(["(blank)", "Other (rare values)"]) & (t["n"] >= min_n)]
        best = real.sort_values("shrunk_lift", ascending=False).head(1)
        worst = real.sort_values("shrunk_lift").head(1)
        fields.append({
            "feature": r.feature, "label": r.label, "source": r.source, "kind": r.kind, "custom": r.custom,
            "coverage": coverage, "n": int(s.notna().sum()), "groups": len(t), "p_value": p, "effect": v,
            "p_numeric": mw, "leakage": "; ".join(leak) or None,
            "best_value": best["value"].iloc[0] if len(best) else None,
            "best_rate": best["rate"].iloc[0] if len(best) else np.nan,
            "best_n": int(best["n"].iloc[0]) if len(best) else 0,
            "worst_value": worst["value"].iloc[0] if len(worst) else None,
            "worst_rate": worst["rate"].iloc[0] if len(worst) else np.nan,
            "worst_n": int(worst["n"].iloc[0]) if len(worst) else 0,
        })
        t.insert(0, "feature", r.feature)
        t.insert(1, "label", r.label)
        values.append(t)

    fields = pd.DataFrame(fields)
    if not fields.empty:
        fields["q_value"] = fdr(fields["p_value"])
        fields["strength"] = [_strength(q, e, lk) for q, e, lk in zip(fields["q_value"], fields["effect"], fields["leakage"])]
        order = {"Strong": 0, "Moderate": 1, "Weak": 2, "No clear signal": 3, "Leakage suspected": 4}
        fields["_o"] = fields["strength"].map(order)
        fields = fields.sort_values(["_o", "effect"], ascending=[True, False]).drop(columns="_o").reset_index(drop=True)
    values = pd.concat(values, ignore_index=True) if values else pd.DataFrame()
    return {"fields": fields, "values": values, "skipped": pd.DataFrame(skipped), "base_rate": base, "closed": len(df)}


def _strength(q, effect, leak) -> str:
    if isinstance(leak, str) and leak:
        return "Leakage suspected"
    if pd.isna(q):
        return "No clear signal"
    if q < 0.05 and effect >= 0.25:
        return "Strong"
    if q < 0.05 and effect >= 0.12:
        return "Moderate"
    if q < 0.10:
        return "Weak"
    return "No clear signal"


def drivers(wide: pd.DataFrame, fields: pd.DataFrame, max_features: int = 12, depth: int = 3) -> dict:
    """Shallow decision tree over the strongest non-leaky signals -> readable segment rules."""
    df = closed_deals(wide)
    use = fields[fields["strength"].isin(["Strong", "Moderate", "Weak"])].head(max_features)
    if len(df) < 40 or use.empty:
        return {"rules": pd.DataFrame(), "auc": np.nan, "features": []}
    X = pd.DataFrame(index=df.index)
    for r in use.itertuples():
        s = df[r.feature]
        if r.kind == "numeric":
            X[f"{r.label}"] = s.fillna(s.median())
        else:
            vals = s.astype("object").fillna("(blank)")
            for val, cnt in vals.value_counts().items():
                if cnt >= 10 and val != "(blank)":
                    X[f"{r.label} = {val}"] = (vals == val).astype(int)
    if X.empty:
        return {"rules": pd.DataFrame(), "auc": np.nan, "features": []}
    y = df["is_won"].values
    leaf = max(15, int(0.03 * len(df)))
    tree = DecisionTreeClassifier(max_depth=depth, min_samples_leaf=leaf, random_state=0)
    try:
        auc = float(np.mean(cross_val_score(tree, X, y, cv=5, scoring="roc_auc")))
    except ValueError:
        auc = np.nan
    tree.fit(X, y)
    base = y.mean()
    rules = []
    t = tree.tree_

    def walk(node, conds):
        if t.children_left[node] == -1:
            n = int(t.n_node_samples[node])
            idx = tree.apply(X) == node
            won = int(y[idx].sum())
            rules.append({"segment": " · ".join(conds) or "All deals", "conditions": conds, "deals": n, "won": won,
                          "win_rate": won / n, "lift": (won / n) / base if base else np.nan})
            return
        name, thr = X.columns[t.feature[node]], t.threshold[node]
        binary = set(np.unique(X[name])) <= {0, 1}
        if binary and " = " in name:
            field, val = name.split(" = ", 1)
            left, right = f"{field} ≠ {val}", f"{field} = {val}"
        else:
            left, right = f"{name} ≤ {_fmt(thr)}", f"{name} > {_fmt(thr)}"
        walk(t.children_left[node], conds + [left])
        walk(t.children_right[node], conds + [right])

    walk(0, [])
    rules = pd.DataFrame(rules).sort_values("win_rate", ascending=False).reset_index(drop=True)
    return {"rules": rules, "auc": auc, "features": list(X.columns)}
