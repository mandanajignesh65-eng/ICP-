"""Read-only Zoho CRM API client (REST v8 + Bulk Read v8)."""
from __future__ import annotations

import io
import time
import zipfile

import pandas as pd
import requests

from ..config import Settings

API_VERSION = "v8"


class ZohoError(RuntimeError):
    pass


# Plain-English explanations for Zoho's OAuth error codes
AUTH_HELP = {
    "invalid_code": ("The value in ZOHO_REFRESH_TOKEN is not a valid refresh token. It is probably the one-time "
                     "grant code from the Zoho console (they look alike). Fix: run  python cli.py connect  "
                     "and paste a freshly generated code."),
    "invalid_client": ("Zoho does not recognise ZOHO_CLIENT_ID / ZOHO_CLIENT_SECRET for this data center. "
                       "Check both values in .env and that ZOHO_DC matches your Zoho URL (zoho.in -> in)."),
    "invalid_client_secret": "ZOHO_CLIENT_SECRET is wrong. Copy it again from the Self Client in the Zoho API console.",
    "access_denied": "Zoho refused access. Make sure the user who generated the code can see the CRM data.",
}


def auth_error(code: str, context: str) -> ZohoError:
    return ZohoError(f"{context}: {code}. {AUTH_HELP.get(code, 'Check ZOHO_DC and the credentials in .env.')}")


class ZohoClient:
    def __init__(self, settings: Settings, log=print):
        missing = [k for k in ("client_id", "client_secret", "refresh_token") if not getattr(settings, k)]
        if missing:
            hint = " Run  python cli.py connect  to create it." if missing == ["refresh_token"] else ""
            raise ZohoError(f"Missing in .env: {', '.join('ZOHO_' + m.upper() for m in missing)}.{hint}")
        self.s = settings
        self.log = log
        self.session = requests.Session()
        self._token: str | None = None
        self._token_expiry = 0.0
        self.api_domain = settings.api_domain

    # ---------- auth ----------
    def _access_token(self) -> str:
        if self._token and time.time() < self._token_expiry - 60:
            return self._token
        r = self.session.post(
            f"{self.s.accounts_url}/oauth/v2/token",
            params={
                "refresh_token": self.s.refresh_token,
                "client_id": self.s.client_id,
                "client_secret": self.s.client_secret,
                "grant_type": "refresh_token",
            },
            timeout=30,
        )
        data = r.json()
        if "access_token" not in data:
            raise auth_error(str(data.get("error", data)), "Could not log in to Zoho")
        self._token = data["access_token"]
        self._token_expiry = time.time() + int(data.get("expires_in", 3600))
        self.api_domain = data.get("api_domain", self.api_domain)
        return self._token

    # ---------- low level ----------
    def _request(self, method: str, path: str, *, params=None, json=None, raw=False, retries=5):
        url = path if path.startswith("http") else f"{self.api_domain}{path}"
        for attempt in range(retries):
            headers = {"Authorization": f"Zoho-oauthtoken {self._access_token()}"}
            r = self.session.request(method, url, params=params, json=json, headers=headers, timeout=120)
            if r.status_code == 401 and "OAUTH_SCOPE_MISMATCH" in r.text:
                raise ZohoError(f"{method} {path}: the Zoho code was generated without a scope this step needs. "
                                "Run  python cli.py connect  and generate the code with all 5 scopes it shows.")
            if r.status_code == 401 and attempt == 0:
                self._token = None  # expired token: refresh once
                continue
            if r.status_code in (429, 500, 502, 503, 504):
                wait = min(60, 2 ** attempt * 2)
                self.log(f"  Zoho returned {r.status_code}, retrying in {wait}s...")
                time.sleep(wait)
                continue
            if r.status_code == 204:
                return None if not raw else b""
            if r.status_code >= 400:
                raise ZohoError(f"{method} {path} -> {r.status_code}: {r.text[:500]}")
            return r.content if raw else r.json()
        raise ZohoError(f"{method} {path} failed after {retries} attempts")

    def get(self, path: str, **params):
        return self._request("GET", f"/crm/{API_VERSION}{path}", params=params or None)

    # ---------- metadata ----------
    def org(self) -> dict:
        data = self.get("/org") or {}
        return (data.get("org") or [{}])[0]

    def modules(self) -> list[dict]:
        return (self.get("/settings/modules") or {}).get("modules", [])

    def fields(self, module: str) -> list[dict]:
        return (self.get("/settings/fields", module=module) or {}).get("fields", [])

    def users(self) -> list[dict]:
        out, page = [], 1
        while True:
            data = self.get("/users", type="AllUsers", page=page, per_page=200) or {}
            out += data.get("users", [])
            if not data.get("info", {}).get("more_records"):
                return out
            page += 1

    def count(self, module: str) -> int | None:
        try:
            return (self.get(f"/{module}/actions/count") or {}).get("count")
        except ZohoError:
            return None

    # ---------- REST records (for modules Bulk Read does not support, e.g. Notes) ----------
    def records(self, module: str, fields: list[str], max_records: int | None = None) -> pd.DataFrame:
        rows, token, page = [], None, 1
        while True:
            params = {"fields": ",".join(fields[:50]), "per_page": 200}
            if token:
                params["page_token"] = token
            else:
                params["page"] = page
            data = self.get(f"/{module}", **params) or {}
            rows += data.get("data", [])
            info = data.get("info", {})
            if not info.get("more_records") or (max_records and len(rows) >= max_records):
                break
            token = info.get("next_page_token")
            page += 1
        return pd.json_normalize(rows, sep=".") if rows else pd.DataFrame()

    def related(self, module: str, record_id: str, related: str, fields: list[str]) -> list[dict]:
        data = self.get(f"/{module}/{record_id}/{related}", fields=",".join(fields), per_page=200) or {}
        return data.get("data", [])

    # ---------- Bulk Read ----------
    def bulk_read(self, module: str, poll_seconds: int = 5, timeout_minutes: int = 60) -> pd.DataFrame:
        """Export every record and every field of a module. Handles >200k records via paging."""
        frames, page, page_token, use_token = [], 1, None, False
        while True:
            query: dict = {"module": {"api_name": module}}
            # Zoho rejects sending page and page_token together; ask by page number first, token as fallback.
            if use_token and page_token:
                query["page_token"] = page_token
            else:
                query["page"] = page
            try:
                job = self._request("POST", f"/crm/bulk/{API_VERSION}/read", json={"query": query})
            except ZohoError:
                if page > 1 and page_token and not use_token:
                    use_token = True
                    continue
                raise
            job_id = job["data"][0]["details"]["id"]
            deadline = time.time() + timeout_minutes * 60
            while True:
                status = self._request("GET", f"/crm/bulk/{API_VERSION}/read/{job_id}")["data"][0]
                state = status.get("state")
                if state == "COMPLETED":
                    break
                if state == "FAILURE" or time.time() > deadline:
                    raise ZohoError(f"Bulk read of {module} failed (state={state})")
                time.sleep(poll_seconds)
            result = status.get("result", {})
            if result.get("count", 0):
                content = self._request("GET", f"/crm/bulk/{API_VERSION}/read/{job_id}/result", raw=True)
                frames.append(_csv_from_zip(content))
            if not result.get("more_records"):
                break
            page_token = result.get("next_page_token")
            page += 1
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def _csv_from_zip(content: bytes) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(content)) as z:
        name = next(n for n in z.namelist() if n.lower().endswith(".csv"))
        with z.open(name) as f:
            # Keep everything as text here; typing happens in the cleaning step using field metadata.
            return pd.read_csv(f, dtype=str, keep_default_na=False, na_values=[""])
