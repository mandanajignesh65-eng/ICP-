"""Realistic synthetic Zoho CRM export with known, planted patterns.

Used to test the whole pipeline and dashboard without a live CRM. The planted
patterns (e.g. SaaS + 51-200 employees + referrals win more) let us check that
the analysis actually finds what is there. Includes messy values, duplicates,
missing data and a leakage field on purpose.
"""
from __future__ import annotations

from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from .storage import Store

RNG = np.random.default_rng(7)
NOW = datetime(2026, 9, 1)

INDUSTRIES = {  # name: (share, win effect)
    "Software/SaaS": (0.24, 1.0), "IT Services": (0.16, 0.5), "Financial Services": (0.10, 0.3),
    "Manufacturing": (0.14, -0.6), "Healthcare": (0.08, 0.0), "Education": (0.08, -0.4),
    "Retail": (0.10, -0.8), "Logistics": (0.06, -0.2), "Real Estate": (0.04, -0.5),
}
MESSY = {"Software/SaaS": ["saas", "Software / SaaS", "Software/SaaS "], "IT Services": ["IT services", "it services"]}
COUNTRIES = {"India": (0.58, 0.0), "United States": (0.18, 0.4), "United Arab Emirates": (0.09, 0.2),
             "United Kingdom": (0.08, 0.1), "Singapore": (0.07, 0.0)}
CITIES = {"India": ["Mumbai", "Bengaluru", "Delhi", "Pune", "Ahmedabad", "Hyderabad"],
          "United States": ["New York", "San Francisco", "Austin"], "United Arab Emirates": ["Dubai", "Abu Dhabi"],
          "United Kingdom": ["London", "Manchester"], "Singapore": ["Singapore"]}
SOURCES = {"Website": (0.25, 0.2), "Referral": (0.12, 1.0), "Cold Call": (0.15, -0.7), "LinkedIn": (0.16, 0.0),
           "Partner": (0.08, 0.6), "Trade Show": (0.09, -0.1), "Google Ads": (0.15, -0.3)}
TITLES = {  # title: win effect
    "CEO": 0.3, "Founder": 0.3, "Co-Founder & CEO": 0.3, "CTO": 0.2, "VP Sales": 0.5, "VP of Sales": 0.5,
    "Head of Sales": 0.5, "Head of Marketing": 0.3, "Director of Operations": 0.2, "Sales Manager": 0.1,
    "Marketing Manager": 0.0, "IT Manager": -0.1, "Operations Executive": -0.6, "Sales Executive": -0.6,
    "Business Development Executive": -0.5, "Intern": -1.0,
}
OPEN_STAGES = ["Qualification", "Needs Analysis", "Proposal/Price Quote", "Negotiation/Review"]
LOSS_REASONS = ["Price", "Chose competitor", "No budget", "No decision / went dark", "Missing feature", "Bad timing"]
USERS = [("4000001", "Aarav Shah"), ("4000002", "Priya Nair"), ("4000003", "Rohan Mehta"),
         ("4000004", "Sara Khan"), ("4000005", "Vikram Rao")]


def _pick(d: dict, n: int) -> np.ndarray:
    keys = list(d)
    p = np.array([v[0] for v in d.values()])
    return RNG.choice(keys, size=n, p=p / p.sum())


def _ids(prefix: int, n: int) -> list[str]:
    return [str(prefix * 10**9 + i) for i in range(1, n + 1)]


def _ts(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S+05:30")


def _emp_effect(e: float) -> float:
    if np.isnan(e):
        return 0.0
    if e <= 10: return -0.9
    if e <= 50: return 0.2
    if e <= 200: return 0.7
    if e <= 1000: return 0.1
    return -0.3


def build(n_accounts: int = 650, n_deals: int = 1100, n_leads: int = 2600) -> dict[str, pd.DataFrame]:
    owners = [u[0] for u in USERS]

    # ---------- Accounts ----------
    acc_ids = _ids(5, n_accounts)
    industry = _pick(INDUSTRIES, n_accounts)
    country = _pick(COUNTRIES, n_accounts)
    employees = np.round(np.exp(RNG.normal(4.2, 1.4, n_accounts))).clip(2, 20000)
    emp_missing = RNG.random(n_accounts) < 0.22
    ind_display = [RNG.choice(MESSY[i]) if i in MESSY and RNG.random() < 0.15 else i for i in industry]
    ind_missing = RNG.random(n_accounts) < 0.12
    acc_created = [NOW - timedelta(days=int(d)) for d in RNG.integers(60, 900, n_accounts)]
    names = [f"{RNG.choice(['Nova','Apex','Blue','Zen','Quantum','Pixel','Vertex','Orbit','Nimbus','Iron','Swift','Bright'])}"
             f"{RNG.choice(['soft','tech','labs','works','systems','ware','logic','hub','ly'])} {i}" for i in range(n_accounts)]
    accounts = pd.DataFrame({
        "Id": acc_ids, "Account_Name": names,
        "Industry": [None if m else v for v, m in zip(ind_display, ind_missing)],
        "Employees": [None if m else str(int(e)) for e, m in zip(employees, emp_missing)],
        "Annual_Revenue": [str(int(e * RNG.uniform(20000, 60000))) if RNG.random() > 0.4 else None for e in employees],
        "Billing_Country": country,
        "Billing_City": [RNG.choice(CITIES[c]) for c in country],
        "Account_Type": RNG.choice(["Prospect", "Customer", "Partner", "Competitor"], n_accounts, p=[.6, .3, .07, .03]),
        "Website": [f"www.{n.split()[0].lower()}{n.split()[1]}.com" for n in names],
        "Rating": RNG.choice(["Hot", "Warm", "Cold", None], n_accounts, p=[.2, .3, .2, .3]),
        "Owner": RNG.choice(owners, n_accounts), "Created_Time": [_ts(d) for d in acc_created],
    })
    # planted duplicates (same company entered twice)
    dup = accounts.sample(18, random_state=1).copy()
    dup["Id"] = _ids(6, len(dup))
    dup["Account_Name"] = dup["Account_Name"].str.upper() + " Pvt Ltd"
    accounts = pd.concat([accounts, dup], ignore_index=True)

    # ---------- Contacts ----------
    contacts = []
    cid = iter(_ids(7, 5000))
    acc_contacts: dict[str, list[tuple[str, str]]] = {}
    for a in accounts.itertuples():
        for _ in range(RNG.integers(1, 5)):
            t = RNG.choice(list(TITLES)) if RNG.random() > 0.1 else None
            c = next(cid)
            acc_contacts.setdefault(a.Id, []).append((c, t))
            fn, ln = RNG.choice(["Amit", "Neha", "John", "Fatima", "Li", "Karan", "Emma", "Ravi", "Sofia"]), \
                RNG.choice(["Patel", "Singh", "Smith", "Ali", "Tan", "Iyer", "Brown", "Das"])
            contacts.append({"Id": c, "First_Name": fn, "Last_Name": ln, "Title": t,
                             "Email": f"{fn.lower()}.{ln.lower()}{c[-3:]}@example.com" if RNG.random() > .08 else None,
                             "Account_Name": a.Id, "Lead_Source": RNG.choice(list(SOURCES)),
                             "Owner": a.Owner, "Created_Time": a.Created_Time})
    contacts = pd.DataFrame(contacts)

    # ---------- Deals ----------
    deal_ids = _ids(8, n_deals)
    acc_idx = RNG.integers(0, n_accounts, n_deals)  # deals only on original (non-duplicate) accounts
    source = _pick(SOURCES, n_deals)
    deals, history, calls, events, tasks = [], [], [], [], []
    call_ids, event_ids, task_ids = iter(_ids(11, 99999)), iter(_ids(12, 99999)), iter(_ids(13, 99999))
    for k, did in enumerate(deal_ids):
        a = accounts.iloc[acc_idx[k]]
        contact_id, title = acc_contacts[a.Id][RNG.integers(0, len(acc_contacts[a.Id]))]
        logit = -1.1 + INDUSTRIES[industry[acc_idx[k]]][1] + COUNTRIES[a.Billing_Country][1] \
            + SOURCES[source[k]][1] + _emp_effect(employees[acc_idx[k]]) + TITLES.get(title, 0) * 0.8 \
            + RNG.normal(0, 0.6)
        p_win = 1 / (1 + np.exp(-logit))
        created = NOW - timedelta(days=int(RNG.integers(5, 720)))
        age = (NOW - created).days
        closed = age > 25 and RNG.random() < 0.85
        won = closed and RNG.random() < p_win
        emp = employees[acc_idx[k]]
        amount = float(np.round(max(20000, emp * RNG.uniform(800, 2500)) * RNG.uniform(0.6, 1.4), -3))
        amount = min(amount, 4_000_000)
        if closed:
            cycle = int(np.clip(RNG.lognormal(3.6 if won else 3.3, 0.5), 5, age))
            close_dt = created + timedelta(days=cycle)
            if won:
                stage, reached = "Closed Won", len(OPEN_STAGES)
            else:
                reached = int(RNG.choice([1, 2, 3, 4], p=[.25, .25, .35, .15]))
                stage = "Closed Lost to Competition" if RNG.random() < .25 else "Closed Lost"
        else:
            reached = int(RNG.integers(1, 5))
            stage = OPEN_STAGES[reached - 1]
            close_dt = NOW + timedelta(days=int(RNG.integers(5, 90)))
            cycle = age
        engaged = 1.6 if won else (0.8 if closed else 1.0)
        first_touch = created + timedelta(days=float(RNG.exponential(1.5 if won else 4)))
        deals.append({
            "Id": did, "Deal_Name": f"{a.Account_Name} - {RNG.choice(['Annual', 'Pilot', 'Expansion', 'Platform'])}",
            "Account_Name": a.Id, "Contact_Name": contact_id, "Amount": str(amount) if RNG.random() > .05 else None,
            "Stage": stage, "Closing_Date": close_dt.strftime("%Y-%m-%d"),
            "Created_Time": _ts(created), "Modified_Time": _ts(min(close_dt, NOW)),
            "Lead_Source": source[k] if RNG.random() > .07 else None,
            "Type": RNG.choice(["New Business", "Existing Business"], p=[.8, .2]),
            "Owner": a.Owner, "Pipeline": "Standard (Standard)",
            "Probability": "100" if won else ("0" if closed else str(10 * reached + 10)),
            "Reason_For_Loss__s": RNG.choice(LOSS_REASONS) if closed and not won and RNG.random() > .3 else None,
            "Use_Case": RNG.choice(["Lead Generation", "Customer Support", "Analytics", None], p=[.4, .3, .2, .1]),
            "Competitor_Name": RNG.choice(["RivalCRM", "Freshworks", "In-house", None], p=[.2, .2, .1, .5]),
            "Onboarding_Date": (close_dt + timedelta(days=7)).strftime("%Y-%m-%d") if won else None,  # leakage
        })
        # stage history
        t = created
        for i in range(reached):
            dur = int(RNG.integers(2, 20))
            history.append({"deal_id": did, "Stage": OPEN_STAGES[i], "Duration_Days": str(dur),
                            "Modified_Time": _ts(t), "Amount": str(amount), "Probability": str(10 * i + 20)})
            t += timedelta(days=dur)
        if closed:
            history.append({"deal_id": did, "Stage": stage, "Duration_Days": "", "Modified_Time": _ts(close_dt),
                            "Amount": str(amount), "Probability": "100" if won else "0"})
        # activities between creation and close (+ a few after close, which the analysis must ignore)
        end = min(close_dt, NOW)
        span = max((end - created).days, 1)
        def when(first=False):
            return first_touch if first else created + timedelta(days=float(RNG.uniform(0, span)))
        for j in range(RNG.poisson(4 * engaged)):
            calls.append({"Id": next(call_ids), "Subject": "Call", "Call_Type": RNG.choice(["Outbound", "Inbound"], p=[.8, .2]),
                          "Call_Start_Time": _ts(when(j == 0)), "Call_Duration": f"{RNG.integers(1, 40)}:00",
                          "What_Id": did, "$se_module": "Deals", "Who_Id": contact_id, "Owner": a.Owner})
        for _ in range(RNG.poisson(1.8 * engaged)):
            start = when()
            events.append({"Id": next(event_ids), "Event_Title": "Demo / Meeting", "Start_DateTime": _ts(start),
                           "End_DateTime": _ts(start + timedelta(minutes=45)), "What_Id": did, "$se_module": "Deals",
                           "Who_Id": contact_id, "Owner": a.Owner})
        for _ in range(RNG.poisson(2)):
            tasks.append({"Id": next(task_ids), "Subject": "Follow up", "Status": RNG.choice(["Completed", "Not Started"]),
                          "Due_Date": when().strftime("%Y-%m-%d"), "What_Id": did, "$se_module": "Deals",
                          "Who_Id": contact_id, "Owner": a.Owner})
        if won and RNG.random() < .5:  # post-close onboarding call -> must not count as a signal
            calls.append({"Id": next(call_ids), "Subject": "Onboarding", "Call_Type": "Outbound",
                          "Call_Start_Time": _ts(close_dt + timedelta(days=10)), "Call_Duration": "30:00",
                          "What_Id": did, "$se_module": "Deals", "Who_Id": contact_id, "Owner": a.Owner})
    deals = pd.DataFrame(deals)

    # ---------- Leads ----------
    lead_source = _pick(SOURCES, n_leads)
    lead_ind = _pick(INDUSTRIES, n_leads)
    conv_p = np.array([0.12 + 0.1 * SOURCES[s][1] + 0.05 * INDUSTRIES[i][1] for s, i in zip(lead_source, lead_ind)]).clip(.02, .6)
    converted = RNG.random(n_leads) < conv_p
    status = np.where(converted, "Converted",
                      RNG.choice(["Not Contacted", "Contacted", "Attempted to Contact", "Junk Lead",
                                  "Not Qualified", "Pre-Qualified", "Lost Lead"], n_leads))
    leads = pd.DataFrame({
        "Id": _ids(9, n_leads), "Company": [f"Lead Co {i}" for i in range(n_leads)],
        "Last_Name": RNG.choice(["Patel", "Singh", "Smith", "Ali"], n_leads),
        "Lead_Source": lead_source, "Industry": lead_ind, "Lead_Status": status,
        "No_of_Employees": [str(int(x)) for x in np.round(np.exp(RNG.normal(4, 1.4, n_leads))).clip(1, 20000)],
        "Country": _pick(COUNTRIES, n_leads), "Designation": RNG.choice(list(TITLES), n_leads),
        "Owner": RNG.choice(owners, n_leads), "Converted__s": np.where(converted, "true", "false"),
        "Created_Time": [_ts(NOW - timedelta(days=int(d))) for d in RNG.integers(1, 720, n_leads)],
    })

    raw = {"Accounts": accounts, "Contacts": contacts, "Deals": deals, "Leads": leads,
           "Calls": pd.DataFrame(calls), "Events": pd.DataFrame(events), "Tasks": pd.DataFrame(tasks)}
    return raw | {"_history": pd.DataFrame(history)}


FIELD_TYPES = {
    "Amount": "currency", "Annual_Revenue": "currency", "Employees": "integer", "No_of_Employees": "integer",
    "Probability": "integer", "Closing_Date": "date", "Onboarding_Date": "date", "Due_Date": "date",
    "Created_Time": "datetime", "Modified_Time": "datetime", "Call_Start_Time": "datetime",
    "Start_DateTime": "datetime", "End_DateTime": "datetime", "Owner": "ownerlookup",
    "Account_Name": "lookup", "Contact_Name": "lookup", "What_Id": "lookup", "Who_Id": "lookup",
    "Email": "email", "Website": "website", "Converted__s": "boolean",
    "Industry": "picklist", "Stage": "picklist", "Lead_Source": "picklist", "Type": "picklist",
    "Billing_Country": "text", "Billing_City": "text", "Account_Type": "picklist", "Rating": "picklist",
    "Reason_For_Loss__s": "picklist", "Use_Case": "picklist", "Competitor_Name": "picklist",
    "Lead_Status": "picklist", "Country": "text", "Designation": "text", "Title": "text",
    "Call_Type": "picklist", "Status": "picklist", "Pipeline": "picklist",
}
CUSTOM = {"Use_Case", "Competitor_Name", "Onboarding_Date"}
LOOKUPS = {"Account_Name": "Accounts", "Contact_Name": "Contacts"}


def write_demo(store: Store, log=print) -> None:
    raw = build()
    history = raw.pop("_history")
    field_rows = []
    for module, df in raw.items():
        store.write(f"raw_{module}", df)
        for col in df.columns:
            dtype = "text" if (module, col) == ("Accounts", "Account_Name") else FIELD_TYPES.get(col, "text")
            field_rows.append({"module": module, "api_name": col, "label": col.replace("__s", "").replace("_", " ").replace("$", ""),
                               "data_type": dtype, "json_type": None,
                               "custom": col in CUSTOM,
                               "lookup_module": LOOKUPS.get(col) if module in ("Deals", "Contacts") else None})
    store.write("raw_Stage_History", history)
    store.write("meta_fields", pd.DataFrame(field_rows))
    stages = OPEN_STAGES + ["Closed Won", "Closed Lost", "Closed Lost to Competition"]
    ftype = {"Closed Won": "Closed Won", "Closed Lost": "Closed Lost", "Closed Lost to Competition": "Closed Lost"}
    store.write("meta_picklist", pd.DataFrame([{
        "module": "Deals", "field": "Stage", "display_value": s, "actual_value": s, "sequence": i + 1,
        "forecast_type": ftype.get(s, "Open"), "forecast_category": None,
        "probability": 100 if s == "Closed Won" else (0 if s.startswith("Closed") else 10 * i + 20),
    } for i, s in enumerate(stages)]))
    store.write("meta_users", pd.DataFrame([{"id": i, "full_name": n, "email": None, "role": "Sales",
                                             "profile": "Standard", "status": "active"} for i, n in USERS]))
    store.write("meta_org", pd.DataFrame([{"company_name": "DEMO COMPANY (synthetic data)", "currency": "INR",
                                           "country": "India", "time_zone": "Asia/Kolkata", "edition": "demo",
                                           "extracted_at": NOW.isoformat()}]))
    store.write("meta_modules", pd.DataFrame([{"api_name": m, "label": m, "generated_type": "default",
                                               "api_supported": True, "records": len(df), "selected": True}
                                              for m, df in raw.items()]))
    log("Demo CRM written: " + ", ".join(f"{m} {len(df):,}" for m, df in raw.items()))
