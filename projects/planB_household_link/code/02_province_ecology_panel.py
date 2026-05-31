"""
Plan B — Stage 02: Province × year organizational-ecology panel.

Reads data/interim/events_geo.parquet (output of stage 01) and constructs a
balanced (province, year) panel of organizational-ecology indicators:

    - n_events               weighted event count
    - shannon_actor          Shannon entropy of actor_type distribution
    - hhi_actor              Herfindahl-Hirschman index of actor_type
    - n_actor_types          count of distinct actor_type observed
    - central_share          weighted share of events with actor_gov_level == '中央'
    - local_share            weighted share of events with actor_gov_level in {'省','市','县','乡'}
    - central_local_ratio    central_share / max(local_share, eps)
    - social_share           weighted share of actor_type in {'社会组织','人民团体','基金会'-like, 民主党派}
    - soe_finance_share      weighted share of actor_type in {'国有企业','金融机构'}
    - university_share       weighted share of actor_type in {'高等院校','科研机构'}
    - dominant_actor         most-common actor_type by weight
    - entry_pairing_share    share of entry_mechanism == '东西协作'
    - entry_fixed_share      share of entry_mechanism == '定点帮扶'
    - entry_social_share     share of entry_mechanism == '社会参与'
    - total_value_yuan       sum of value_num (treating value_unit ad-hoc — see notes)

Indicators are computed with weight = 1/multi_region_n so a 3-province
event contributes 1/3 to each. Years span 2009–2022 (the data range).

Output: data/processed/province_ecology_panel.parquet
"""

from __future__ import annotations

import datetime as dt
import logging
import math
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

INTERIM_DIR = PROJECT_ROOT / "data" / "interim"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
LOG_DIR = PROJECT_ROOT / "output" / "logs"
TABLE_DIR = PROJECT_ROOT / "output" / "tables"

for d in (PROCESSED_DIR, LOG_DIR, TABLE_DIR):
    d.mkdir(parents=True, exist_ok=True)

EPS = 1e-9

# Actor-type partitions used in indicator construction.
# Note: actor_gov_level is empty across the whole DB (data-quality issue
# inherited from upstream extraction), so the central/local cut is derived
# from actor_type directly. This is documented in docs/decisions.md.
CENTRAL_TYPES = {"中央政府"}
LOCAL_GOV_TYPES = {"地方政府"}
SOCIAL_TYPES = {"社会组织", "人民团体", "民主党派"}
SOE_FIN_TYPES = {"国有企业", "金融机构"}
UNIV_TYPES = {"高等院校", "科研机构"}
PRIVATE_TYPES = {"民营企业", "电商平台"}


def _make_logger() -> logging.Logger:
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"02_province_ecology_panel_{ts}.log"
    logger = logging.getLogger("planB.02")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    fh = logging.FileHandler(log_path, encoding="utf-8")
    sh = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    fh.setFormatter(fmt)
    sh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger


def shannon(weights: pd.Series) -> float:
    """Weighted Shannon entropy in nats; 0 for empty / single-category."""
    total = weights.sum()
    if total <= 0:
        return 0.0
    p = weights / total
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def hhi(weights: pd.Series) -> float:
    total = weights.sum()
    if total <= 0:
        return 0.0
    p = weights / total
    return float((p * p).sum())


def weighted_share(df: pd.DataFrame, mask: pd.Series) -> float:
    total = df["weight"].sum()
    if total <= 0:
        return 0.0
    return float(df.loc[mask, "weight"].sum() / total)


def compute_panel(geo: pd.DataFrame, logger: logging.Logger) -> pd.DataFrame:
    geo = geo.loc[geo["province_code"].notna()].copy()
    geo["actor_type"] = geo["actor_type"].fillna("__unknown__")
    geo["actor_gov_level"] = geo["actor_gov_level"].fillna("__unknown__")
    geo["entry_mechanism"] = geo["entry_mechanism"].fillna("__unknown__")
    logger.info("geo-resolved rows: %d", len(geo))

    group_cols = ["province_code", "province_name", "region_group", "data_year"]
    records: list[dict] = []

    for keys, sub in geo.groupby(group_cols, dropna=False, sort=True):
        prov_code, prov_name, region_group, year = keys
        w = sub["weight"]
        total_w = float(w.sum())

        actor_weights = sub.groupby("actor_type")["weight"].sum()
        # exclude '__unknown__' from entropy of actor_type
        actor_weights_known = actor_weights.drop("__unknown__", errors="ignore")

        dominant_actor = (
            actor_weights_known.idxmax() if not actor_weights_known.empty else None
        )

        central_mask = sub["actor_type"].isin(CENTRAL_TYPES)
        local_mask = sub["actor_type"].isin(LOCAL_GOV_TYPES)
        central_s = weighted_share(sub, central_mask)
        local_s = weighted_share(sub, local_mask)

        rec = {
            "province_code": prov_code,
            "province_name": prov_name,
            "region_group": region_group,
            "data_year": int(year),
            "n_events": total_w,
            "n_raw_rows": int(len(sub)),
            "shannon_actor": shannon(actor_weights_known),
            "hhi_actor": hhi(actor_weights_known),
            "n_actor_types": int((actor_weights_known > 0).sum()),
            "central_share": central_s,
            "local_share": local_s,
            "central_local_ratio": central_s / max(local_s, EPS),
            "social_share": weighted_share(sub, sub["actor_type"].isin(SOCIAL_TYPES)),
            "soe_finance_share": weighted_share(sub, sub["actor_type"].isin(SOE_FIN_TYPES)),
            "university_share": weighted_share(sub, sub["actor_type"].isin(UNIV_TYPES)),
            "private_share": weighted_share(sub, sub["actor_type"].isin(PRIVATE_TYPES)),
            "dominant_actor": dominant_actor,
            "entry_pairing_share": weighted_share(sub, sub["entry_mechanism"] == "东西协作"),
            "entry_fixed_share":   weighted_share(sub, sub["entry_mechanism"] == "定点帮扶"),
            "entry_social_share":  weighted_share(sub, sub["entry_mechanism"] == "社会参与"),
            "entry_market_share":  weighted_share(sub, sub["entry_mechanism"] == "市场进入"),
            "entry_policy_share":  weighted_share(sub, sub["entry_mechanism"] == "政策驱动"),
            "total_value_num": float(sub["value_num"].fillna(0).mul(sub["weight"]).sum()),
        }
        records.append(rec)

    panel = pd.DataFrame.from_records(records)
    panel = panel.sort_values(["province_code", "data_year"]).reset_index(drop=True)
    return panel


def balance_panel(panel: pd.DataFrame) -> pd.DataFrame:
    """Cross-product of provinces × years observed in the data, fill zeros."""
    provinces = panel[["province_code", "province_name", "region_group"]].drop_duplicates()
    years = pd.DataFrame({"data_year": sorted(panel["data_year"].unique())})
    grid = provinces.merge(years, how="cross")
    full = grid.merge(panel, how="left",
                      on=["province_code", "province_name", "region_group", "data_year"])
    fill_zero = [
        "n_events", "n_raw_rows", "shannon_actor", "hhi_actor", "n_actor_types",
        "central_share", "local_share", "central_local_ratio",
        "social_share", "soe_finance_share", "university_share", "private_share",
        "entry_pairing_share", "entry_fixed_share", "entry_social_share",
        "entry_market_share", "entry_policy_share", "total_value_num",
    ]
    for c in fill_zero:
        full[c] = full[c].fillna(0)
    return full.sort_values(["province_code", "data_year"]).reset_index(drop=True)


def write_summary(panel: pd.DataFrame, out_path: Path) -> None:
    by_year = (
        panel.groupby("data_year")
        .agg(n_provinces_active=("n_events", lambda x: int((x > 0).sum())),
             total_events=("n_events", "sum"),
             mean_shannon=("shannon_actor", "mean"),
             mean_central_share=("central_share", "mean"),
             mean_pairing_share=("entry_pairing_share", "mean"))
        .round(3)
        .reset_index()
    )
    top_prov = (
        panel.groupby(["province_code", "province_name", "region_group"])
        .agg(total_events=("n_events", "sum"),
             mean_shannon=("shannon_actor", "mean"))
        .sort_values("total_events", ascending=False)
        .round(3)
        .head(15)
        .reset_index()
    )

    lines = [
        "# Plan B — Stage 02 province-year ecology panel summary",
        "",
        f"- Panel shape: **{panel.shape[0]} rows × {panel.shape[1]} cols** "
        f"({panel['province_code'].nunique()} provinces × "
        f"{panel['data_year'].nunique()} years)",
        "",
        "## By year",
        "",
        by_year.to_markdown(index=False),
        "",
        "## Top 15 provinces by total weighted events",
        "",
        top_prov.to_markdown(index=False),
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    logger = _make_logger()
    geo_path = INTERIM_DIR / "events_geo.parquet"
    logger.info("reading %s", geo_path)
    geo = pd.read_parquet(geo_path)
    logger.info("rows: %d", len(geo))

    panel = compute_panel(geo, logger)
    panel = balance_panel(panel)

    out = PROCESSED_DIR / "province_ecology_panel.parquet"
    panel.to_parquet(out, index=False)
    logger.info("wrote %s (%d rows)", out, len(panel))

    write_summary(panel, TABLE_DIR / "02_province_panel_summary.md")
    logger.info("wrote summary table")


if __name__ == "__main__":
    main()
