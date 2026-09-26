"""Settings loaded from environment / .env file."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

# Zoho data centers: (accounts server, API domain)
DATA_CENTERS = {
    "in": ("https://accounts.zoho.in", "https://www.zohoapis.in"),
    "com": ("https://accounts.zoho.com", "https://www.zohoapis.com"),
    "eu": ("https://accounts.zoho.eu", "https://www.zohoapis.eu"),
    "com.au": ("https://accounts.zoho.com.au", "https://www.zohoapis.com.au"),
    "jp": ("https://accounts.zoho.jp", "https://www.zohoapis.jp"),
    "ca": ("https://accounts.zohocloud.ca", "https://www.zohoapis.ca"),
    "sa": ("https://accounts.zoho.sa", "https://www.zohoapis.sa"),
}

# Read-only scopes: the tool can never modify the CRM.
SCOPES = ",".join([
    "ZohoCRM.modules.READ",
    "ZohoCRM.settings.READ",
    "ZohoCRM.users.READ",
    "ZohoCRM.org.READ",
    "ZohoCRM.bulk.READ",
])


@dataclass(frozen=True)
class Settings:
    dc: str
    client_id: str
    client_secret: str
    refresh_token: str
    db_path: Path

    @property
    def accounts_url(self) -> str:
        return DATA_CENTERS[self.dc][0]

    @property
    def api_domain(self) -> str:
        return DATA_CENTERS[self.dc][1]


def get_settings() -> Settings:
    dc = os.getenv("ZOHO_DC", "in").strip()
    if dc not in DATA_CENTERS:
        raise ValueError(f"ZOHO_DC must be one of {sorted(DATA_CENTERS)}, got {dc!r}")
    return Settings(
        dc=dc,
        client_id=os.getenv("ZOHO_CLIENT_ID", "").strip(),
        client_secret=os.getenv("ZOHO_CLIENT_SECRET", "").strip(),
        refresh_token=os.getenv("ZOHO_REFRESH_TOKEN", "").strip(),
        db_path=default_db_path(),
    )


def default_db_path() -> Path:
    return Path(os.getenv("ICP_DB_PATH", ROOT / "data" / "crm.duckdb"))
