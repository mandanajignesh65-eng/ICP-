# ICP Analyzer — CRM signal analysis

Connect a Zoho CRM (read-only), pull every module and field, clean it, and test **every field against won vs lost deals** to see what actually predicts a win. The results are shown in a visual dashboard you can use to decide the Ideal Customer Profile (ICP).

## What you get

The dashboard answers business questions, not fields. By default it looks at **deals to new customers**, and leaves out Junk deals (both can be changed under Filters).

| Section | Question it answers |
|---|---|
| Summary | Who should we focus on, who should we deprioritize, and what data is missing? |
| Best customers | For each question (industry, company size, market, lead source, buyer): which groups win more often, pay more, and close faster? |
| Lead sources | Which channels produce deals that close, and how leads convert |
| Pipeline | How far deals get, where they stall, why they're lost, how long deals take, how concentrated revenue is |
| Sales process | How won deals were worked: meetings, calls, speed of first contact |
| Buyers | Which job levels and functions are on won deals |
| All fields | Every customer field in the CRM, ranked, for exploring |
| Data quality | How complete and clean the CRM data is |

Each group gets a verdict:
- **Focus:** the win rate is clearly above average, or the value per opportunity (win rate × typical won deal) is at least 1.5× average, backed by enough wins.
- **Deprioritize:** the win rate is clearly below average.
- **Average:** no clear difference either way.
- **Too little data:** too few deals to judge.

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
