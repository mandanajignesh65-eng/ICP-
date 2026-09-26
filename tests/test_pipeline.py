"""End-to-end checks on synthetic data with known, planted patterns."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from icp_analyzer import analysis as A  # noqa: E402
from icp_analyzer.demo import write_demo  # noqa: E402
from icp_analyzer.prepare import classify_title, prepare  # noqa: E402
from icp_analyzer.signals import drivers, scan  # noqa: E402
from icp_analyzer.stats import rate_table, wilson  # noqa: E402
from icp_analyzer.storage import Store  # noqa: E402


@pytest.fixture(scope="module")
def db(tmp_path_factory):
    path = tmp_path_factory.mktemp("icp") / "demo.duckdb"
    store = Store(path)
    write_demo(store, log=lambda *_: None)
    prepare(store, log=lambda *_: None)
    store.close()
    return path


@pytest.fixture(scope="module")
def sig(db):
    s = Store(db, read_only=True)
    out = scan(s.read("deal_wide"), s.read("feature_catalog"))
    out["wide"] = s.read("deal_wide")
    s.close()
    return out


def test_wilson_interval_is_honest_for_small_samples():
    lo, hi = wilson([1], [2])
    assert lo[0] < 0.1 and hi[0] > 0.9  # 1 of 2 tells you almost nothing


def test_rate_table_marks_small_groups():
    t = rate_table(pd.Series(["a"] * 3 + ["b"] * 100), pd.Series([1, 1, 1] + [0] * 100))
    assert t.set_index("value").loc["a", "confidence"] == "Too few"


def test_title_classifier():
    assert classify_title("VP of Sales") == ("Sales", "VP / Head")
    assert classify_title("Co-Founder & CEO")[1] == "C-level / Founder"
    assert classify_title(None) == ("Unknown", "Unknown")


def test_outcomes_and_cleaning(db):
    s = Store(db, read_only=True)
    deals = s.read("clean_deals")
    assert set(deals["outcome"]) == {"Won", "Lost", "Open"}
    assert "amount" in deals and deals["amount"].notna().mean() > 0.9
    log = s.read("cleaning_log")
    assert (log["cleaned"] == "Software/SaaS").any()  # spelling variants merged
    assert s.read("clean_accounts")["is_duplicate"].sum() >= 15  # planted duplicates found
    s.close()


def test_planted_patterns_are_found(sig):
    v = sig["values"].set_index(["feature", "value"])
    assert v.loc[("account.Industry", "Software/SaaS"), "direction"] == "Better"
    assert v.loc[("account.Industry", "Retail"), "direction"] == "Worse"
    assert v.loc[("deal.Lead_Source", "Referral"), "direction"] == "Better"
    assert v.loc[("deal.Lead_Source", "Cold Call"), "direction"] == "Worse"
    f = sig["fields"].set_index("feature")
    assert f.loc["account.Industry", "strength"] in ("Strong", "Moderate")


def test_leakage_is_excluded(sig):
    f = sig["fields"].set_index("feature")
    assert f.loc["deal.Onboarding_Date", "strength"] == "Leakage suspected"
    assert f.loc["deal.Reason_For_Loss__s", "strength"] == "Leakage suspected"
    draft = A.icp_draft(sig)
    assert not draft["label"].str.contains("Onboarding|Reason", regex=True).any()


def test_drivers_produce_segments(sig):
    d = drivers(sig["wide"], sig["fields"][sig["fields"]["source"] != "Activity"])
    assert not d["rules"].empty and d["auc"] > 0.55


def test_dashboard_renders_without_errors(db, monkeypatch):
    from streamlit.testing.v1 import AppTest
    monkeypatch.setattr(sys, "argv", ["app.py", "--db", str(db)])
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=300)
    at.run()
    assert not at.exception, [e.message for e in at.exception]
    for section in ["Best customers", "Lead sources", "Pipeline", "Sales process", "Buyers", "All fields", "Data quality"]:
        at.session_state["section"] = section
        at.run()
        assert not at.exception, (section, [e.message for e in at.exception])


def test_business_answers_find_planted_patterns(sig):
    from icp_analyzer import insights as IN
    answers = IN.all_answers(sig, sig["wide"], 10)
    assert {"industry", "source", "size"} <= set(answers)
    ind = answers["industry"]["card"].set_index("value")
    assert ind.loc["Software/SaaS", "verdict"] == "Focus"
    assert ind.loc["Retail", "verdict"] == "Deprioritize"
    src = answers["source"]["card"].set_index("value")
    assert src.loc["Referral", "verdict"] == "Focus"
    concl = IN.conclusions(answers, sig["base_rate"], lambda x: f"{x:.0f}")
    assert concl["focus"] and concl["avoid"]
