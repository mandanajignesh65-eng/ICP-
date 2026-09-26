"""Thin DuckDB wrapper. One local file holds raw extracts, metadata and cleaned tables."""
from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd


class Store:
    def __init__(self, path: Path | str, read_only: bool = False):
        self.path = Path(path)
        if not read_only:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self.con = duckdb.connect(str(self.path), read_only=read_only)

    def write(self, name: str, df: pd.DataFrame) -> None:
        if df is None or df.shape[1] == 0:  # nothing to store (e.g. an empty module): drop any stale copy
            self.con.execute(f'DROP TABLE IF EXISTS "{name}"')
            return
        # DuckDB column names are case-insensitive: make "Amount" and "amount" distinct instead of silently merging
        seen, cols = set(), []
        for c in map(str, df.columns):
            new, i = c, 2
            while new.lower() in seen:
                new, i = f"{c}__{i}", i + 1
            seen.add(new.lower())
            cols.append(new)
        if cols != list(map(str, df.columns)):
            df = df.set_axis(cols, axis=1)
        self.con.register("_tmp_df", df)
        self.con.execute(f'CREATE OR REPLACE TABLE "{name}" AS SELECT * FROM _tmp_df')
        self.con.unregister("_tmp_df")

    def read(self, name: str) -> pd.DataFrame:
        if not self.has(name):
            return pd.DataFrame()
        return self.con.execute(f'SELECT * FROM "{name}"').df()

    def sql(self, query: str) -> pd.DataFrame:
        return self.con.execute(query).df()

    def has(self, name: str) -> bool:
        return name in self.tables()

    def tables(self) -> list[str]:
        return [r[0] for r in self.con.execute("SELECT table_name FROM information_schema.tables").fetchall()]

    def close(self) -> None:
        self.con.close()
