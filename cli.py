"""Command line: connect Zoho, extract, prepare, and open the dashboard.

  python cli.py demo                 # load synthetic CRM data (no Zoho needed)
  python cli.py connect              # guided Zoho connection: paste a grant code, token saved, connection tested
  python cli.py auth-url             # print the scopes to use when creating the grant code
  python cli.py exchange-code CODE   # turn a Self Client grant code into a refresh token (saved to .env)
  python cli.py check                # test the Zoho connection
  python cli.py extract [--notes] [--stage-history]
  python cli.py prepare              # clean + model the data
  python cli.py dashboard            # open the visual dashboard
  python cli.py all                  # extract + prepare
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import requests

from icp_analyzer.config import ROOT, SCOPES, get_settings
from icp_analyzer.storage import Store


def cmd_demo(args):
    from icp_analyzer.demo import write_demo
    from icp_analyzer.prepare import prepare
    store = Store(args.db)
    write_demo(store)
    prepare(store)
    store.close()
    print(f"\nDemo data ready in {args.db}. Run:  python cli.py dashboard --db {args.db}")


def cmd_auth_url(args):
    s = get_settings()
    print("1. Open the Zoho API console for your data center:")
    print(f"   {s.accounts_url.replace('accounts', 'api-console')}")
    print("2. Add Client -> Self Client -> copy Client ID and Client Secret into .env")
    print("3. Generate Code tab -> paste these scopes (read-only):")
    print(f"   {SCOPES}")
    print("   Time duration: 10 minutes. Description: ICP analyzer")
    print("4. Copy the generated code and run:  python cli.py exchange-code <CODE>")


CODE_HELP = {
    "invalid_code": "The code is expired, was already used, or belongs to another data center. "
                    "Codes work once and only for the time you picked (e.g. 10 minutes). Generate a new one.",
    "invalid_client": "ZOHO_CLIENT_ID / ZOHO_CLIENT_SECRET in .env don't match this Self Client or data center.",
}


def _exchange(code: str) -> str:
    """Trade a one-time grant code for a long-lived refresh token and save it to .env."""
    s = get_settings()
    if not (s.client_id and s.client_secret):
        sys.exit("Set ZOHO_CLIENT_ID and ZOHO_CLIENT_SECRET in .env first (from the Self Client in the Zoho API console).")
    r = requests.post(f"{s.accounts_url}/oauth/v2/token", params={
        "grant_type": "authorization_code", "client_id": s.client_id,
        "client_secret": s.client_secret, "code": code.strip()}, timeout=30).json()
    token = r.get("refresh_token")
    if not token:
        err = str(r.get("error", r))
        if "access_token" in r:
            err = "no refresh token returned — this code was probably already exchanged once"
        sys.exit(f"\nZoho did not accept the code: {err}\n{CODE_HELP.get(err, '')}")
    env = ROOT / ".env"
    lines = [l for l in env.read_text().splitlines() if not l.startswith("ZOHO_REFRESH_TOKEN=")] if env.exists() else []
    lines.append(f"ZOHO_REFRESH_TOKEN={token}")
    env.write_text("\n".join(lines) + "\n")
    import os
    os.environ["ZOHO_REFRESH_TOKEN"] = token
    print("Refresh token saved to .env (this file is never committed).")
    return token


def cmd_exchange(args):
    _exchange(args.code)
    print("Now run:  python cli.py check")


def cmd_connect(args):
    """Guided setup: shows the steps, asks for the grant code (hidden), saves the token, tests the connection."""
    from getpass import getpass
    s = get_settings()
    if not (s.client_id and s.client_secret):
        cmd_auth_url(args)
        sys.exit("\nFirst put ZOHO_CLIENT_ID and ZOHO_CLIENT_SECRET in .env, save it, then run  python cli.py connect  again.")
    console = s.accounts_url.replace("accounts", "api-console")
    print(f"1. Open {console}  -> your Self Client -> 'Generate Code' tab")
    print(f"2. Scope (paste exactly):\n   {SCOPES}")
    print("3. Time duration: 10 minutes · Description: ICP analyzer · Create")
    print("4. Copy the code and paste it below (input is hidden; right-click or Ctrl+V to paste, then Enter)\n")
    code = getpass("Grant code: ")
    if not code.strip():
        sys.exit("No code entered.")
    _exchange(code)
    print()
    cmd_check(args)


def _client():
    from icp_analyzer.zoho.client import ZohoClient
    return ZohoClient(get_settings())


def cmd_check(args):
    c = _client()
    org = c.org()
    print(f"Connected to: {org.get('company_name')}  (data center: {get_settings().dc})")
    mods = [m for m in c.modules() if m.get("api_supported")]
    print(f"{len(mods)} API-accessible modules. Record counts:")
    for name in ("Leads", "Accounts", "Contacts", "Deals", "Calls", "Events", "Tasks"):
        print(f"  {name:10s} {c.count(name)}")


def cmd_extract(args):
    from icp_analyzer.zoho.extract import discover, extract
    c, store = _client(), Store(args.db)
    print("Discovering CRM structure...")
    discover(c, store)
    print("Extracting data (Bulk Read)...")
    extract(c, store, modules=args.modules, notes=args.notes, stage_history=args.stage_history)
    store.close()


def cmd_prepare(args):
    from icp_analyzer.prepare import prepare
    store = Store(args.db)
    prepare(store)
    store.close()


def cmd_dashboard(args):
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(ROOT / "app.py"), "--", "--db", str(Path(args.db).resolve())], cwd=ROOT)


def main():
    p = argparse.ArgumentParser(description="ICP CRM analyzer")
    p.add_argument("--db", type=Path, default=get_settings().db_path, help="DuckDB file (default data/crm.duckdb)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("demo").set_defaults(fn=cmd_demo)
    sub.add_parser("auth-url").set_defaults(fn=cmd_auth_url)
    e = sub.add_parser("exchange-code")
    e.add_argument("code")
    e.set_defaults(fn=cmd_exchange)
    sub.add_parser("connect", help="Guided Zoho connection (recommended)").set_defaults(fn=cmd_connect)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    for name, fn in (("extract", cmd_extract), ("all", None)):
        x = sub.add_parser(name)
        x.add_argument("--modules", nargs="*", help="Only these modules (default: all relevant)")
        x.add_argument("--notes", action="store_true", help="Also pull Notes (REST API)")
        x.add_argument("--stage-history", action="store_true", help="Pull deal stage history (1 API call per deal)")
        x.set_defaults(fn=fn or (lambda a: (cmd_extract(a), cmd_prepare(a))))
    sub.add_parser("prepare").set_defaults(fn=cmd_prepare)
    sub.add_parser("dashboard").set_defaults(fn=cmd_dashboard)
    args = p.parse_args()
    from icp_analyzer.zoho.client import ZohoError
    try:
        args.fn(args)
    except ZohoError as e:  # show Zoho problems as a clear message, not a traceback
        sys.exit(f"\n{e}")


if __name__ == "__main__":
    main()
