"""Small, well-understood statistics used everywhere. No black boxes."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats as st
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.proportion import proportion_confint


def wilson(k, n):
    """95% Wilson confidence interval for a rate. Honest for small samples."""
    k, n = np.asarray(k, float), np.asarray(n, float)
    lo, hi = proportion_confint(k, np.where(n == 0, 1, n), alpha=0.05, method="wilson")
    return np.where(n == 0, np.nan, lo), np.where(n == 0, np.nan, hi)


def shrunk_rate(k, n, prior: float, strength: float = 10.0):
    """Pull small-sample rates toward the overall average (empirical-Bayes style)."""
    return (np.asarray(k, float) + prior * strength) / (np.asarray(n, float) + strength)


def confidence(n: int, lo: float, hi: float, base: float) -> str:
    if n < 5:
        return "Too few"
    separated = lo > base or hi < base
    if n >= 30 and separated:
        return "High"
    if n >= 15 and separated:
        return "Medium"
    return "Low"


def direction(lo: float, hi: float, base: float) -> str:
    if lo > base:
        return "Better"
    if hi < base:
        return "Worse"
    return "Not different"


def rate_table(group: pd.Series, outcome: pd.Series, base: float | None = None) -> pd.DataFrame:
    """Win (or conversion) rate per group value with CI, lift and confidence."""
    df = pd.DataFrame({"value": group.astype("object").fillna("(blank)").astype(str), "y": outcome.astype(float)})
    base = df["y"].mean() if base is None else base
    t = df.groupby("value")["y"].agg(n="count", won="sum").reset_index()
    t["won"] = t["won"].astype(int)
    t["lost"] = t["n"] - t["won"]
    t["rate"] = t["won"] / t["n"]
    t["ci_lo"], t["ci_hi"] = wilson(t["won"], t["n"])
    t["lift"] = t["rate"] / base if base else np.nan
    t["shrunk_lift"] = shrunk_rate(t["won"], t["n"], base) / base if base else np.nan
    total_won = t["won"].sum()
    t["share_of_wins"] = t["won"] / total_won if total_won else np.nan
    t["share_of_deals"] = t["n"] / t["n"].sum()
    t["confidence"] = [confidence(n, lo, hi, base) for n, lo, hi in zip(t["n"], t["ci_lo"], t["ci_hi"])]
    t["direction"] = [direction(lo, hi, base) if n >= 5 else "Too few" for n, lo, hi in zip(t["n"], t["ci_lo"], t["ci_hi"])]
    return t.sort_values("n", ascending=False).reset_index(drop=True)


def association(group: pd.Series, outcome: pd.Series) -> tuple[float, float]:
    """Chi-square p-value and Cramér's V (0 = no relationship, 1 = perfect)."""
    ct = pd.crosstab(group.astype(str), outcome)
    if ct.shape[0] < 2 or ct.shape[1] < 2:
        return np.nan, 0.0
    chi2, p, _, _ = st.chi2_contingency(ct, correction=False)
    n = ct.values.sum()
    v = float(np.sqrt(chi2 / (n * (min(ct.shape) - 1)))) if n else 0.0
    return float(p), v


def fdr(pvals: pd.Series) -> pd.Series:
    """Benjamini-Hochberg: controls false discoveries when testing many fields at once."""
    out = pd.Series(np.nan, index=pvals.index)
    ok = pvals.notna()
    if ok.sum():
        out[ok] = multipletests(pvals[ok], method="fdr_bh")[1]
    return out


def mann_whitney(a: pd.Series, b: pd.Series) -> float:
    a, b = a.dropna(), b.dropna()
    if len(a) < 5 or len(b) < 5:
        return np.nan
    return float(st.mannwhitneyu(a, b, alternative="two-sided").pvalue)


def numeric_bins(s: pd.Series, q: int = 5) -> pd.Series:
    """Quantile bins with readable labels, keeping order."""
    v = s.dropna()
    if v.nunique() <= 8:
        return s.map(lambda x: np.nan if pd.isna(x) else _fmt(x))
    try:
        cats = pd.qcut(s, q=q, duplicates="drop")
    except ValueError:
        return s.map(lambda x: np.nan if pd.isna(x) else _fmt(x))
    # label each bin by the real min–max inside it (not the padded qcut edges)
    rng = s.groupby(cats, observed=True).agg(["min", "max"])
    labels = {c: (_fmt(r["min"]) if r["min"] == r["max"] else f"{_fmt(r['min'])}–{_fmt(r['max'])}")
              for c, r in rng.iterrows()}
    return cats.map(labels).astype("object")


_SUFFIX = {"K": 1e3, "L": 1e5, "Cr": 1e7}


def range_key(label: str) -> float | None:
    """Numeric sort key for labels like '12–23', '1.2L–3L', '≤ 34K', '> 2.8L', '51-200', '5000+'."""
    import re
    m = re.search(r"(-?\d+(?:\.\d+)?)\s*(Cr|K|L)?", str(label))
    if not m:
        return None
    v = float(m.group(1)) * _SUFFIX.get(m.group(2) or "", 1)
    s = str(label).strip()
    return v - 0.5 if s.startswith("≤") else (v + 0.5 if s.startswith(">") else v)


def order_values(t: pd.DataFrame) -> pd.DataFrame:
    """Natural order for numeric ranges; otherwise highest rate first. Blank/Other always last."""
    special = t["value"].isin(["(blank)", "Other (rare values)"])
    keys = t.loc[~special, "value"].map(range_key)
    if len(keys) and keys.notna().all():
        main = t[~special].assign(_k=keys).sort_values("_k").drop(columns="_k")
    else:
        main = t[~special].sort_values("rate", ascending=False)
    return pd.concat([main, t[special]])


def _fmt(x) -> str:
    x = float(x)
    if abs(x) >= 1e7:
        return f"{x / 1e7:.3g}Cr"
    if abs(x) >= 1e5:
        return f"{x / 1e5:.3g}L"
    if abs(x) >= 1e3:
        return f"{x / 1e3:.3g}K"
    return f"{x:.0f}" if x == int(x) else f"{x:.1f}"
