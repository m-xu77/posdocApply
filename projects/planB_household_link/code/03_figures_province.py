"""
Plan B — Stage 03: Publication-grade provincial figures.

Renders three figures from data/processed/province_ecology_panel.parquet:

    fig01_shannon_heatmap.{pdf,png}
        Province × year heatmap of Shannon entropy of actor_type.
        Provinces ordered by NBS region group (东北, 东部, 中部, 西部)
        then by mean diversity. A reader should be able to read the
        story of the 2013–2020 organizational diversification of the
        Chinese anti-poverty campaign off this single figure.

    fig02_central_local_timeseries.{pdf,png}
        Mean (across provinces) central_share, local_share, and
        social_share over 2009–2022. Highlights the composition shift.

    fig03_event_volume_by_group.{pdf,png}
        Stacked-area weighted-event count by NBS region group, year.

The figures are calibrated for one-column journal width (3.5 in).
"""

from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager

matplotlib.use("Agg")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
FIG_DIR = PROJECT_ROOT / "output" / "figures"
LOG_DIR = PROJECT_ROOT / "output" / "logs"
for d in (FIG_DIR, LOG_DIR):
    d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Chinese-font handling
# ---------------------------------------------------------------------------
CJK_CANDIDATES = [
    "PingFang SC", "Hiragino Sans GB", "STSong",
    "Heiti SC", "Songti SC", "Source Han Sans CN", "Noto Sans CJK SC",
]


def _set_cjk_font() -> str | None:
    available = {f.name for f in font_manager.fontManager.ttflist}
    for cand in CJK_CANDIDATES:
        if cand in available:
            matplotlib.rcParams["font.sans-serif"] = [cand] + matplotlib.rcParams["font.sans-serif"]
            matplotlib.rcParams["axes.unicode_minus"] = False
            return cand
    return None


def _make_logger() -> logging.Logger:
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"03_figures_province_{ts}.log"
    logger = logging.getLogger("planB.03")
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


# ---------------------------------------------------------------------------
# Figure 1: Shannon heatmap
# ---------------------------------------------------------------------------

GROUP_ORDER = ["东北", "东部", "中部", "西部"]


def fig_shannon_heatmap(panel: pd.DataFrame, out_dir: Path, cjk: str | None) -> None:
    pivot = panel.pivot_table(
        index=["region_group", "province_name"],
        columns="data_year",
        values="shannon_actor",
        aggfunc="mean",
    )
    mean_div = panel.groupby(["region_group", "province_name"])["shannon_actor"].mean()
    order = (
        mean_div.reset_index()
        .assign(group_rank=lambda d: d["region_group"].map(
            {g: i for i, g in enumerate(GROUP_ORDER)}))
        .sort_values(["group_rank", "shannon_actor"], ascending=[True, False])
    )
    pivot = pivot.loc[list(zip(order["region_group"], order["province_name"]))]

    fig, ax = plt.subplots(figsize=(7.2, 8.0), dpi=200)
    im = ax.imshow(pivot.values, aspect="auto", cmap="YlGnBu",
                   vmin=0, vmax=float(np.nanmax(pivot.values)))

    ax.set_xticks(range(pivot.shape[1]))
    ax.set_xticklabels([str(y) for y in pivot.columns], rotation=0, fontsize=8)
    ax.set_yticks(range(pivot.shape[0]))
    ylabels = [
        f"{prov}  ({grp})" for grp, prov in pivot.index
    ]
    ax.set_yticklabels(ylabels, fontsize=8)

    # group separators
    group_changes = []
    last = None
    for i, (grp, _) in enumerate(pivot.index):
        if grp != last:
            group_changes.append(i)
            last = grp
    for gc in group_changes[1:]:
        ax.axhline(gc - 0.5, color="white", lw=1.0)

    cb = plt.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
    cb.set_label("Shannon entropy of actor_type (nats)", fontsize=9)

    ax.set_title(
        "Provincial organizational-actor diversity, 2009–2022\n"
        "(weighted Shannon entropy of actor_type across action events)",
        fontsize=10, pad=10,
    )
    ax.set_xlabel("Year (data_year)", fontsize=9)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"fig01_shannon_heatmap.{ext}", bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2: Central/local/social shares — temporal composition
# ---------------------------------------------------------------------------

def fig_central_local_timeseries(panel: pd.DataFrame, out_dir: Path) -> None:
    # weighted mean by n_events to avoid province-size distortion
    def w_mean(col: str) -> pd.Series:
        d = panel.copy()
        d["w"] = d["n_events"]
        d["wx"] = d[col] * d["w"]
        g = d.groupby("data_year").agg(num=("wx", "sum"), den=("w", "sum"))
        return (g["num"] / g["den"]).rename(col)

    cols = ["central_share", "local_share", "social_share",
            "soe_finance_share", "university_share", "private_share"]
    ts = pd.concat([w_mean(c) for c in cols], axis=1).reset_index()

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=200)
    labels = {
        "central_share": "Central gov. (中央政府)",
        "local_share": "Local gov. (地方政府)",
        "social_share": "Social orgs (社会组织 / 团体)",
        "soe_finance_share": "SOEs + Finance",
        "university_share": "Universities + Research",
        "private_share": "Private firms",
    }
    palette = {
        "central_share": "#b22222",
        "local_share": "#1f78b4",
        "social_share": "#33a02c",
        "soe_finance_share": "#ff7f00",
        "university_share": "#6a3d9a",
        "private_share": "#a6761d",
    }
    for c in cols:
        ax.plot(ts["data_year"], ts[c], marker="o", label=labels[c],
                color=palette[c], lw=1.6, ms=4)
    ax.set_ylabel("Weighted share of action events", fontsize=9)
    ax.set_xlabel("Year (data_year)", fontsize=9)
    ax.set_title(
        "Composition of poverty-alleviation implementation, 2009–2022\n"
        "(share of action events by actor type, weighted by event volume)",
        fontsize=10, pad=8,
    )
    ax.set_ylim(0, max(ts[cols].to_numpy().max() * 1.15, 0.6))
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=7.5, ncol=2, loc="upper right", frameon=False)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"fig02_central_local_timeseries.{ext}", bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 3: Stacked-area event volume by NBS region group
# ---------------------------------------------------------------------------

def fig_event_volume_by_group(panel: pd.DataFrame, out_dir: Path) -> None:
    g = panel.groupby(["data_year", "region_group"])["n_events"].sum().unstack(fill_value=0)
    g = g[[c for c in GROUP_ORDER if c in g.columns]]

    fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=200)
    palette = {"东北": "#a6cee3", "东部": "#1f78b4", "中部": "#b2df8a", "西部": "#e31a1c"}
    ax.stackplot(g.index, [g[c].values for c in g.columns],
                 labels=list(g.columns),
                 colors=[palette[c] for c in g.columns],
                 alpha=0.85)
    ax.set_xlabel("Year (data_year)", fontsize=9)
    ax.set_ylabel("Weighted action-event count", fontsize=9)
    ax.set_title(
        "Volume of identified anti-poverty action events, by NBS region group",
        fontsize=10, pad=8,
    )
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    ax.grid(True, alpha=0.25)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"fig03_event_volume_by_group.{ext}", bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    logger = _make_logger()
    cjk = _set_cjk_font()
    logger.info("CJK font: %s", cjk or "NOT FOUND — glyphs may render as boxes")

    panel = pd.read_parquet(PROCESSED_DIR / "province_ecology_panel.parquet")
    logger.info("loaded panel: %s", panel.shape)

    fig_shannon_heatmap(panel, FIG_DIR, cjk)
    logger.info("wrote fig01_shannon_heatmap")
    fig_central_local_timeseries(panel, FIG_DIR)
    logger.info("wrote fig02_central_local_timeseries")
    fig_event_volume_by_group(panel, FIG_DIR)
    logger.info("wrote fig03_event_volume_by_group")


if __name__ == "__main__":
    main()
