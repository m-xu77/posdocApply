"""
Plan B — Stage 04: Supplementary analyses for the manuscript.

(1) Bai-Perron / Chow-style structural break tests at 2013 and 2020 for the
    national time series of Shannon entropy and central_share.
(2) entry_mechanism × actor_type cross-tab (weighted), with raw and
    column-normalized variants — substitute for full correspondence analysis
    while keeping dependencies minimal.

Outputs:
- output/tables/04_structural_break.md
- output/tables/04_entry_actor_crosstab.md
- output/tables/04_summary_stats.md
"""

from __future__ import annotations

import datetime as dt
import logging
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parents[2]
DB_PATH = REPO_ROOT / "output_v3" / "research.db"
INTERIM_DIR = PROJECT_ROOT / "data" / "interim"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
TABLE_DIR = PROJECT_ROOT / "output" / "tables"
LOG_DIR = PROJECT_ROOT / "output" / "logs"
for d in (TABLE_DIR, LOG_DIR):
    d.mkdir(parents=True, exist_ok=True)


def _make_logger() -> logging.Logger:
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"04_supplementary_{ts}.log"
    logger = logging.getLogger("planB.04")
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


def chow_test(y: np.ndarray, x: np.ndarray, break_idx: int) -> dict:
    """Chow test for a single break at break_idx in a simple OLS y = a + b*x.

    Returns F-statistic, df, and a one-line interpretation. p-value is left
    out to avoid a scipy dependency; user can read the F directly.
    """
    n = len(y)
    if break_idx <= 2 or break_idx >= n - 2:
        return {"F": float("nan"), "df": (np.nan, np.nan), "note": "too few obs"}
    # Pooled
    X = np.column_stack([np.ones_like(x), x])
    b_pool, *_ = np.linalg.lstsq(X, y, rcond=None)
    e_pool = y - X @ b_pool
    SSR_pool = float((e_pool ** 2).sum())
    # Pre
    Xp, yp = X[:break_idx], y[:break_idx]
    bp, *_ = np.linalg.lstsq(Xp, yp, rcond=None)
    ep = yp - Xp @ bp
    SSR_pre = float((ep ** 2).sum())
    # Post
    Xq, yq = X[break_idx:], y[break_idx:]
    bq, *_ = np.linalg.lstsq(Xq, yq, rcond=None)
    eq = yq - Xq @ bq
    SSR_post = float((eq ** 2).sum())

    k = 2  # intercept + slope
    num = (SSR_pool - SSR_pre - SSR_post) / k
    den = (SSR_pre + SSR_post) / (n - 2 * k)
    F = num / den if den > 0 else float("nan")
    return {"F": F, "df": (k, n - 2 * k), "note": ""}


def national_timeseries(panel: pd.DataFrame) -> pd.DataFrame:
    # weighted by n_events
    def wm(col):
        d = panel.copy()
        d["w"] = d["n_events"]
        return (d.groupby("data_year").apply(
            lambda s: (s[col] * s["w"]).sum() / max(s["w"].sum(), 1e-9), include_groups=False
        ).rename(col))

    cols = ["shannon_actor", "central_share", "local_share",
            "social_share", "soe_finance_share", "university_share"]
    ts = pd.concat([wm(c) for c in cols], axis=1).reset_index()
    ts["log_events"] = np.log(
        panel.groupby("data_year")["n_events"].sum().reindex(ts["data_year"]).values + 1
    )
    return ts


def structural_break_section(panel: pd.DataFrame, out_path: Path) -> None:
    ts = national_timeseries(panel)
    years = ts["data_year"].to_numpy().astype(float)

    rows = []
    for col in ["shannon_actor", "central_share", "log_events"]:
        y = ts[col].to_numpy()
        for break_year in (2013, 2016, 2020):
            if break_year not in ts["data_year"].values:
                continue
            idx = int(np.where(years == break_year)[0][0])
            res = chow_test(y, years, idx)
            rows.append({
                "series": col,
                "break_year": break_year,
                "F": round(res["F"], 3) if not np.isnan(res["F"]) else None,
                "df_num": res["df"][0],
                "df_den": res["df"][1],
            })

    df = pd.DataFrame(rows)
    lines = [
        "# Plan B — Stage 04 structural-break diagnostics",
        "",
        "Chow F-statistics for a single break at the indicated year on national "
        "weighted time-series (linear trend baseline). F-statistic critical "
        "values (5%): for `df_den ≈ 10` and `df_num = 2`, F_crit ≈ 4.10. "
        "Values above the critical threshold suggest a structural break.",
        "",
        df.to_markdown(index=False),
        "",
        "## National time-series (weighted by event count)",
        "",
        ts.round(3).to_markdown(index=False),
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def entry_actor_crosstab(out_path: Path) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(
            "SELECT actor_type, entry_mechanism FROM action_events "
            "WHERE actor_type IS NOT NULL AND entry_mechanism IS NOT NULL",
            conn,
        )
    ct = pd.crosstab(df["actor_type"], df["entry_mechanism"], margins=True, margins_name="Σ")
    col_norm = pd.crosstab(df["actor_type"], df["entry_mechanism"], normalize="columns").round(3)

    lines = [
        "# Plan B — Stage 04 entry_mechanism × actor_type structure",
        "",
        f"N = {len(df):,} non-null events.",
        "",
        "## Raw counts",
        "",
        ct.to_markdown(),
        "",
        "## Column-normalised (each entry_mechanism column sums to 1)",
        "",
        col_norm.to_markdown(),
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def summary_stats(panel: pd.DataFrame, out_path: Path) -> None:
    desc = (
        panel[[
            "n_events", "shannon_actor", "hhi_actor", "n_actor_types",
            "central_share", "local_share", "central_local_ratio",
            "social_share", "soe_finance_share", "university_share", "private_share",
            "entry_pairing_share", "entry_fixed_share", "entry_social_share",
        ]]
        .describe(percentiles=[0.25, 0.5, 0.75])
        .round(3)
        .T
        .reset_index()
        .rename(columns={"index": "indicator"})
    )
    lines = [
        "# Plan B — Stage 04 summary statistics (province-year panel)",
        "",
        f"Unit of observation: province × year, N = {len(panel)} (31 × 14).",
        "",
        desc.to_markdown(index=False),
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    logger = _make_logger()
    panel = pd.read_parquet(PROCESSED_DIR / "province_ecology_panel.parquet")
    structural_break_section(panel, TABLE_DIR / "04_structural_break.md")
    logger.info("wrote structural break diagnostics")
    entry_actor_crosstab(TABLE_DIR / "04_entry_actor_crosstab.md")
    logger.info("wrote entry × actor crosstab")
    summary_stats(panel, TABLE_DIR / "04_summary_stats.md")
    logger.info("wrote summary stats")


if __name__ == "__main__":
    main()
