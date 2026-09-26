# ICP Analyzer — CRM signal analysis

Connect a Zoho CRM (read-only), pull every module and field, clean it, and test **every field against won vs lost deals** to see what actually predicts a win. The results are shown in a visual dashboard you can use to decide the Ideal Customer Profile (ICP).

## What you get

| Dashboard tab | What it answers |
|---|---|
| 📋 Summary | KPIs, strongest findings in plain English, and an ICP draft (target / avoid) built from your own won/lost data |
| 🩺 Data health | How complete and trustworthy each field is, duplicates, stale deals, values merged during cleaning |
| 📡 Signals | Every field ranked by how strongly it separates won from lost deals, with a drill-down per field |
| 🧭 Segments & combos | Combinations of traits that win (decision-tree segments) and a two-field win-rate heatmap |
| 💰 Revenue & cycle | Revenue, deal size, and cycle length by segment; revenue concentration |
| 🔻 Pipeline & losses | Open pipeline, stage funnel, where lost deals die, loss reasons, competitors |
| 🎯 Leads & sources | Lead volume → conversion → deals → revenue per source; conversion by any lead field |
| 📞 Activities | Meetings, calls, and speed of first touch on won vs lost deals (process signals, not ICP) |
| 👤 Buyer roles | Win rate by contact seniority, function, and exact title (seeds for personas) |
| 📈 Trends | Monthly deals and revenue, win rate by quarter |
| 🗂 Data | Browse and download every cleaned table |

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

### Try it with demo data first (no Zoho needed)

```bash
python cli.py --db data/demo.duckdb demo
python cli.py --db data/demo.duckdb dashboard
```

The demo CRM has patterns planted on purpose (e.g. SaaS and referrals win more, Retail and cold calls win less), plus messy values, duplicates, and a leakage field. You can check that the analysis finds them.

### Connect Zoho CRM (read-only)

1. `copy .env.example .env`. Set `ZOHO_DC=in` for zoho.in accounts.
2. Open the Zoho API console (`https://api-console.zoho.in`) → **Add Client → Self Client**. Copy the **Client ID** and **Client Secret** into `.env` and save.
3. `python cli.py connect`. It shows the scopes to paste in the console's **Generate Code** tab, asks for the code (hidden input), saves the refresh token to `.env`, and tests the connection.
   The grant code and the refresh token both start with `1000.`. Never paste the grant code into `.env` yourself.
4. `python cli.py check` tests the connection and shows record counts.
5. `python cli.py all --stage-history` extracts everything and prepares it.
6. `python cli.py dashboard`

The scopes are read-only (`ZohoCRM.modules.READ`, `settings.READ`, `users.READ`, `org.READ`, `bulk.READ`), so the tool **cannot change anything** in the CRM. API usage comes from the CRM's own daily credits. Each Bulk Read job costs 50 credits. `--stage-history` costs one API call per deal.

## How the analysis works (and why you can trust it)

- **Raw → clean → analysis.** Raw exports are stored untouched (`raw_*` tables). Cleaning types each field from Zoho's own field metadata and merges spelling/case variants. Every change is logged (`cleaning_log`).
- **Outcome.** Won/Lost/Open comes from each deal stage's forecast type in Zoho, with a fallback based on the stage name.
- **Every field is tested.** For each field (standard and custom, from deals, accounts, contacts, and derived activity counts) the tool computes:
  - the win rate per value, with a **95% Wilson confidence range** (honest for small samples)
  - **lift** vs the average
  - **effect size** (Cramér's V)
  - **q-value**: the chi-square p-value corrected with Benjamini–Hochberg, because many fields are tested at once
- **Confidence labels.** "High" needs 30+ deals AND a range that doesn't overlap the average. "Too few" appears below 5 deals.
- **Leakage protection.** Fields filled only after a deal closes (e.g. onboarding date, loss reason) would look like perfect predictors. They are detected and excluded. Activities logged after the close date are not counted.
- **Who vs how.** Account, contact, and deal traits define the ICP. Activity counts describe how deals were worked and are kept separate.
- **Segments.** A shallow, cross-validated decision tree (at least 3% of deals per segment) finds winning trait combinations. AUC shows how predictive they are.

## Commands

```
python cli.py demo | auth-url | exchange-code CODE | check | extract [--notes] [--stage-history] | prepare | all | dashboard
python -m pytest tests        # end-to-end tests on demo data
```

## Data safety

This repo is public. Credentials (`.env`) and all CRM data (`data/`, `*.duckdb`, `*.csv`) are git-ignored and must never be committed.
