"""
Bai-Perron-style structural break analysis on annual action-event series.

Inputs:  output_v3/research_enhanced.db
Outputs: stdout report; saved series CSV + breaks JSON + diagnostic plot.

Method:
  - Annual aggregation by data_year, 2009-2022 (14 obs).
  - Three series tested:
      (A) total event count per year
      (B) local-government share (%) per year
      (C) governance-frame share (%) per year
  - Two break algorithms run as cross-checks:
      (1) Dynamic programming (exact, requires fixed K)
      (2) PELT (penalty-based, returns variable K)
  - For dynamic programming, K=1, K=2, K=3; report BIC for each.
  - For PELT, sweep penalty values 0.5, 1, 2, 5; report breakpoints.
  - Compare to pre-registered candidate years {2013, 2018, 2020}.

Caveats:
  - N=14 is below the conventional minimum (>=30) for asymptotic Bai-Perron
    significance. Treat results as informative-direction, not as confirmatory tests.
"""
from __future__ import annotations

import json
import math
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import ruptures as rpt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
DB = ROOT / "output_v3" / "research_enhanced.db"
OUT_DIR = Path(__file__).resolve().parent.parent / "tables"
FIG_DIR = Path(__file__).resolve().parent.parent / "figures_new"
FIG_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)

YEARS = list(range(2009, 2023))  # 2009-2022 inclusive

GOV_FRAME = {"协调监督", "培训赋能", "人员派驻", "政策制定", "能力建设"}


def load_series() -> pd.DataFrame:
    con = sqlite3.connect(DB)
    df = pd.read_sql(
        """
        SELECT data_year, actor_type, action_type
        FROM action_events
        WHERE data_year BETWEEN 2009 AND 2022
        """,
        con,
    )
    con.close()

    out = pd.DataFrame({"year": YEARS}).set_index("year")
    out["total"] = df.groupby("data_year").size().reindex(YEARS).fillna(0)
    out["local_n"] = (
        df[df["actor_type"] == "地方政府"]
        .groupby("data_year")
        .size()
        .reindex(YEARS)
        .fillna(0)
    )
    out["gov_frame_n"] = (
        df[df["action_type"].isin(GOV_FRAME)]
        .groupby("data_year")
        .size()
        .reindex(YEARS)
        .fillna(0)
    )
    out["local_share"] = out["local_n"] / out["total"] * 100
    out["gov_share"] = out["gov_frame_n"] / out["total"] * 100
    return out


def bic(signal: np.ndarray, breaks: list[int]) -> float:
    """Schwarz-BIC for a piecewise-constant model."""
    n = len(signal)
    bps = [0] + breaks + [n]
    rss = 0.0
    for i in range(len(bps) - 1):
        seg = signal[bps[i] : bps[i + 1]]
        if len(seg) > 0:
            rss += float(np.sum((seg - seg.mean()) ** 2))
    k_params = len(breaks) + 1
    if rss <= 0:
        rss = 1e-9
    return n * math.log(rss / n) + k_params * math.log(n)


def run_dynp(signal: np.ndarray, k_max: int = 3) -> dict:
    """Exact dynamic-programming search for K=1..k_max breaks (L2 cost)."""
    algo = rpt.Dynp(model="l2", min_size=2, jump=1).fit(signal)
    results = {}
    for k in range(1, k_max + 1):
        bkps = algo.predict(n_bkps=k)
        # ruptures returns indices INCLUDING n as the final point; drop it.
        internal_bkps = [b for b in bkps if b < len(signal)]
        years = [YEARS[b] for b in internal_bkps]
        results[f"K{k}"] = {
            "break_indices": internal_bkps,
            "break_years": years,
            "bic": round(bic(signal, internal_bkps), 3),
        }
    # baseline K=0
    results["K0"] = {"break_indices": [], "break_years": [], "bic": round(bic(signal, []), 3)}
    return results


def run_pelt(signal: np.ndarray, pen_grid=(0.5, 1, 2, 5, 10)) -> dict:
    """PELT penalty sweep."""
    algo = rpt.Pelt(model="l2", min_size=2, jump=1).fit(signal)
    results = {}
    for pen in pen_grid:
        bkps = algo.predict(pen=float(pen))
        internal_bkps = [b for b in bkps if b < len(signal)]
        years = [YEARS[b] for b in internal_bkps]
        results[f"pen_{pen}"] = {
            "break_indices": internal_bkps,
            "break_years": years,
            "bic": round(bic(signal, internal_bkps), 3),
        }
    return results


def analyze(name: str, signal: np.ndarray) -> dict:
    print(f"\n=== Series: {name} (n={len(signal)}) ===")
    print(f"values: {[round(float(x), 2) for x in signal]}")
    dynp = run_dynp(signal, k_max=3)
    pelt = run_pelt(signal)
    print("\n  Dynp (exact, fixed K):")
    for k, v in dynp.items():
        print(f"    {k:>3}  breaks at {str(v['break_years']):<30}  BIC={v['bic']}")
    print("\n  PELT (penalty sweep):")
    for k, v in pelt.items():
        print(f"    {k:>10}  breaks at {str(v['break_years']):<30}  BIC={v['bic']}")
    return {"series": name, "values": signal.tolist(), "dynp": dynp, "pelt": pelt}


def plot_breaks(series: pd.DataFrame, all_results: list[dict]) -> None:
    fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)
    series_names = ["total", "local_share", "gov_share"]
    titles = [
        "Annual action-event count",
        "Local-government share (%) per year",
        "Governance-frame action share (%) per year",
    ]
    for ax, name, title, result in zip(axes, series_names, titles, all_results):
        ax.plot(YEARS, series[name].values, marker="o", lw=1.5)
        ax.set_title(title)
        ax.set_ylabel("count" if name == "total" else "%")
        # Mark best-K=2 Dynp breaks
        bk = result["dynp"]["K2"]["break_years"]
        for b in bk:
            ax.axvline(b, color="red", ls="--", lw=1)
        # Mark candidate years
        for cand in (2013, 2020):
            ax.axvline(cand, color="gray", ls=":", lw=0.8, alpha=0.6)
    axes[-1].set_xlabel("Year")
    plt.tight_layout()
    out = FIG_DIR / "bai_perron_breaks.png"
    plt.savefig(out, dpi=160)
    print(f"\nSaved figure → {out}")


def main():
    series = load_series()
    series.to_csv(OUT_DIR / "annual_series_for_break_test.csv")
    print(f"Series saved → {OUT_DIR / 'annual_series_for_break_test.csv'}")
    print(series.round(2).to_string())

    results = []
    for name, title in [
        ("total", "Total events"),
        ("local_share", "Local-government share"),
        ("gov_share", "Governance-frame share"),
    ]:
        sig = series[name].values.astype(float)
        results.append(analyze(title, sig))

    with open(OUT_DIR / "break_test_results.json", "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved → {OUT_DIR / 'break_test_results.json'}")

    plot_breaks(series, results)


if __name__ == "__main__":
    main()
