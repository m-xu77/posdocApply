"""
Plan B — Stage 01: Region standardization.

Reads action_events from output_v3/research.db, parses the free-text `region`
column (which contains 0..N comma-separated Chinese province names), maps each
token to a GB/T 2260 two-digit provincial code, and writes a long-format
event-province table to data/interim/events_geo.parquet.

Outputs
-------
- data/interim/events_geo.parquet   long-format (event_id, province_code, ...)
- data/interim/events_unresolved.parquet  rows whose region token didn't map
- output/logs/01_standardize_region_<ts>.log
- output/tables/01_region_coverage.md  coverage summary

Determinism: this script is a pure function of the input DB; no randomness.
"""

from __future__ import annotations

import datetime as dt
import logging
import re
import sqlite3
from pathlib import Path

import pandas as pd

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parents[2]
DB_PATH = REPO_ROOT / "output_v3" / "research.db"

INTERIM_DIR = PROJECT_ROOT / "data" / "interim"
LOG_DIR = PROJECT_ROOT / "output" / "logs"
TABLE_DIR = PROJECT_ROOT / "output" / "tables"

for d in (INTERIM_DIR, LOG_DIR, TABLE_DIR):
    d.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------
# GB/T 2260 provincial codes — mainland China (31 PLAs, excl. HK/Macau/TW
# which do not appear in the source).
# --------------------------------------------------------------------------

# Map Chinese short-name -> (code, full_name, region_group, level)
# region_group follows National Bureau of Statistics standard 4-region split:
#   东部 / 中部 / 西部 / 东北
# This is the conventional group used in poverty-alleviation East-West pairing.
PROVINCE_LOOKUP: dict[str, dict] = {
    "北京":   {"code": "11", "name": "北京市",       "group": "东部"},
    "天津":   {"code": "12", "name": "天津市",       "group": "东部"},
    "河北":   {"code": "13", "name": "河北省",       "group": "东部"},
    "山西":   {"code": "14", "name": "山西省",       "group": "中部"},
    "内蒙古": {"code": "15", "name": "内蒙古自治区", "group": "西部"},
    "辽宁":   {"code": "21", "name": "辽宁省",       "group": "东北"},
    "吉林":   {"code": "22", "name": "吉林省",       "group": "东北"},
    "黑龙江": {"code": "23", "name": "黑龙江省",     "group": "东北"},
    "上海":   {"code": "31", "name": "上海市",       "group": "东部"},
    "江苏":   {"code": "32", "name": "江苏省",       "group": "东部"},
    "浙江":   {"code": "33", "name": "浙江省",       "group": "东部"},
    "安徽":   {"code": "34", "name": "安徽省",       "group": "中部"},
    "福建":   {"code": "35", "name": "福建省",       "group": "东部"},
    "江西":   {"code": "36", "name": "江西省",       "group": "中部"},
    "山东":   {"code": "37", "name": "山东省",       "group": "东部"},
    "河南":   {"code": "41", "name": "河南省",       "group": "中部"},
    "湖北":   {"code": "42", "name": "湖北省",       "group": "中部"},
    "湖南":   {"code": "43", "name": "湖南省",       "group": "中部"},
    "广东":   {"code": "44", "name": "广东省",       "group": "东部"},
    "广西":   {"code": "45", "name": "广西壮族自治区","group": "西部"},
    "海南":   {"code": "46", "name": "海南省",       "group": "东部"},
    "重庆":   {"code": "50", "name": "重庆市",       "group": "西部"},
    "四川":   {"code": "51", "name": "四川省",       "group": "西部"},
    "贵州":   {"code": "52", "name": "贵州省",       "group": "西部"},
    "云南":   {"code": "53", "name": "云南省",       "group": "西部"},
    "西藏":   {"code": "54", "name": "西藏自治区",   "group": "西部"},
    "陕西":   {"code": "61", "name": "陕西省",       "group": "西部"},
    "甘肃":   {"code": "62", "name": "甘肃省",       "group": "西部"},
    "青海":   {"code": "63", "name": "青海省",       "group": "西部"},
    "宁夏":   {"code": "64", "name": "宁夏回族自治区","group": "西部"},
    "新疆":   {"code": "65", "name": "新疆维吾尔自治区","group": "西部"},
}

# Whether to treat the East/Central/West/Northeast partition as the canonical
# poverty-alleviation pairing space.
DELIM_PATTERN = re.compile(r"[、,，;；/]")


# --------------------------------------------------------------------------
# Logging
# --------------------------------------------------------------------------

def _make_logger() -> logging.Logger:
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"01_standardize_region_{ts}.log"
    logger = logging.getLogger("planB.01")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    fh = logging.FileHandler(log_path, encoding="utf-8")
    sh = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    fh.setFormatter(fmt)
    sh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.info("log file: %s", log_path)
    return logger


# --------------------------------------------------------------------------
# Core
# --------------------------------------------------------------------------

def load_events(db_path: Path) -> pd.DataFrame:
    cols = [
        "id", "data_year", "pub_year",
        "actor_type", "actor_gov_level",
        "action_type", "governance_mechanism", "entry_mechanism",
        "resource_type", "value_num", "value_unit",
        "region", "admin_level", "target_type",
        "confidence", "review_status",
    ]
    sql = f"SELECT {', '.join(cols)} FROM action_events"
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(sql, conn)
    df = df.rename(columns={"id": "event_id"})
    return df


def tokenize_region(s: str | None) -> list[str]:
    if s is None or not isinstance(s, str):
        return []
    parts = [p.strip() for p in DELIM_PATTERN.split(s)]
    return [p for p in parts if p]


def standardize(df: pd.DataFrame, logger: logging.Logger) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (events_geo_long, unresolved)."""
    long_rows: list[dict] = []
    unresolved: list[dict] = []

    for row in df.itertuples(index=False):
        tokens = tokenize_region(row.region)
        if not tokens:
            long_rows.append({
                **row._asdict(),
                "province_token": None,
                "province_code": None,
                "province_name": None,
                "region_group": None,
                "multi_region_n": 0,
                "weight": 0.0,
            })
            continue

        resolved = []
        for tok in tokens:
            entry = PROVINCE_LOOKUP.get(tok)
            if entry is None:
                unresolved.append({
                    "event_id": row.event_id,
                    "raw_region": row.region,
                    "token": tok,
                })
            else:
                resolved.append((tok, entry))

        if not resolved:
            long_rows.append({
                **row._asdict(),
                "province_token": None,
                "province_code": None,
                "province_name": None,
                "region_group": None,
                "multi_region_n": 0,
                "weight": 0.0,
            })
            continue

        n = len(resolved)
        for tok, entry in resolved:
            long_rows.append({
                **row._asdict(),
                "province_token": tok,
                "province_code": entry["code"],
                "province_name": entry["name"],
                "region_group": entry["group"],
                "multi_region_n": n,
                "weight": 1.0 / n,
            })

    long_df = pd.DataFrame(long_rows)
    unresolved_df = pd.DataFrame(unresolved)

    logger.info("input events: %d", len(df))
    logger.info("long-format rows: %d", len(long_df))
    logger.info("rows with province_code: %d", long_df["province_code"].notna().sum())
    logger.info("rows without resolvable region: %d",
                (long_df["province_code"].isna()).sum())
    logger.info("unresolved tokens (distinct): %d",
                unresolved_df["token"].nunique() if not unresolved_df.empty else 0)
    return long_df, unresolved_df


def write_coverage_table(long_df: pd.DataFrame, out_path: Path) -> None:
    total = len(long_df["event_id"].unique())
    has_geo = long_df.loc[long_df["province_code"].notna(), "event_id"].nunique()
    multi = (
        long_df.loc[long_df["province_code"].notna()]
        .groupby("event_id")["province_code"].nunique()
        .gt(1).sum()
    )
    by_year = (
        long_df.loc[long_df["province_code"].notna()]
        .groupby("data_year")["event_id"].nunique()
        .rename("events_with_geo")
        .reset_index()
    )
    by_group = (
        long_df.loc[long_df["province_code"].notna()]
        .groupby("region_group")["weight"].sum()
        .rename("weighted_events")
        .reset_index()
    )

    lines = [
        "# Plan B — Stage 01 region-standardization coverage",
        "",
        f"- Distinct events in DB: **{total}**",
        f"- Events with at least one resolved province: **{has_geo}** ({has_geo/total:.1%})",
        f"- Events spanning ≥2 provinces: **{multi}**",
        "",
        "## Events with resolved geography, by data_year",
        "",
        by_year.to_markdown(index=False),
        "",
        "## Weighted event count, by region group",
        "",
        by_group.to_markdown(index=False),
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    logger = _make_logger()
    logger.info("loading events from %s", DB_PATH)
    df = load_events(DB_PATH)
    logger.info("loaded %d events", len(df))

    long_df, unresolved_df = standardize(df, logger)

    long_path = INTERIM_DIR / "events_geo.parquet"
    long_df.to_parquet(long_path, index=False)
    logger.info("wrote %s (%d rows)", long_path, len(long_df))

    unresolved_path = INTERIM_DIR / "events_unresolved.parquet"
    unresolved_df.to_parquet(unresolved_path, index=False)
    logger.info("wrote %s (%d rows)", unresolved_path, len(unresolved_df))

    coverage_path = TABLE_DIR / "01_region_coverage.md"
    write_coverage_table(long_df, coverage_path)
    logger.info("wrote %s", coverage_path)


if __name__ == "__main__":
    main()
