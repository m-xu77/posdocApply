"""
Redraw key figures using data_year (not pub_year) and the paper's P1/P2/P3 phases.

Figures produced:
  fig1_annual_events.png             — annual event count with phase shading + Bai-Perron K=3 breaks
  fig2_actor_stacked_area.png        — actor-type composition stacked area, data_year axis
  fig3_diversity_with_breaks.png     — Shannon entropy with break markers and phases
  fig4_entry_mechanism_heatmap.png   — entry_mechanism × actor_type, data_year-filtered
  fig5_local_share_trajectory.png    — local-government share with 2017 single break marked

All figures use the paper's P1 (2009–2012), P2 (2013–2019), P3 (2020–2022) boundaries.
"""
from __future__ import annotations

import math
import sqlite3
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
DB = ROOT / "output_v3" / "research_enhanced.db"
OUT = Path(__file__).resolve().parent.parent / "figures_new"
OUT.mkdir(exist_ok=True)

plt.rcParams["font.family"] = ["Arial Unicode MS", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 130

YEARS = list(range(2009, 2023))
P1, P2, P3 = (2009, 2012), (2013, 2019), (2020, 2022)
PHASE_COLORS = {"P1": "#d9d9d9", "P2": "#bdbdbd", "P3": "#969696"}

ACTOR_ORDER = [
    "中央政府", "地方政府", "国有企业", "科研机构", "民营企业",
    "金融机构", "人民团体", "民主党派", "社会组织", "其他",
]
ACTOR_EN = {
    "中央政府": "Central state", "地方政府": "Local state",
    "国有企业": "SOE", "科研机构": "Research inst.", "民营企业": "Private firms",
    "金融机构": "Finance", "人民团体": "Mass orgs",
    "民主党派": "Democratic parties", "社会组织": "Social orgs", "其他": "Other",
}

ACTION_GOV = {"协调监督", "培训赋能", "人员派驻", "政策制定", "能力建设"}
ACTION_INFRA = {"基础设施建设", "项目实施", "资金拨付"}

ENTRY_ORDER = ["定点帮扶", "行业援助", "东西协作", "社会参与", "市场进入", "政策驱动", "其他"]
ENTRY_EN = {
    "定点帮扶": "Designated pairing",
    "行业援助": "Sectoral assistance",
    "东西协作": "East-west pairing",
    "社会参与": "Social participation",
    "市场进入": "Market entry",
    "政策驱动": "Policy-driven",
    "其他": "Other",
}


def shade_phases(ax):
    for (lo, hi), tag in [(P1, "P1"), (P2, "P2"), (P3, "P3")]:
        ax.axvspan(lo - 0.5, hi + 0.5, color=PHASE_COLORS[tag], alpha=0.25, zorder=0)


def fig1_annual_events():
    con = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT data_year, COUNT(*) AS n FROM action_events "
        "WHERE data_year BETWEEN 2009 AND 2022 GROUP BY data_year",
        con,
    )
    con.close()
    df = df.set_index("data_year").reindex(YEARS).fillna(0)

    fig, ax = plt.subplots(figsize=(9, 4.6))
    shade_phases(ax)
    ax.plot(YEARS, df["n"], marker="o", color="#08519c", lw=2)
    ax.set_title("Annual action-event count, 2009–2022 (data_year)")
    ax.set_ylabel("events / year")
    ax.set_xlabel("Year")

    # Bai-Perron K=3 breaks (from §1 of methodology log)
    for b in (2014, 2018, 2020):
        ax.axvline(b - 0.5, color="red", ls="--", lw=1.2, alpha=0.85)

    # Phase labels
    for (lo, hi), tag in [(P1, "P1\n2009-2012"), (P2, "P2\n2013-2019"), (P3, "P3\n2020-2022")]:
        ax.text((lo + hi) / 2, ax.get_ylim()[1] * 0.93, tag,
                ha="center", va="top", fontsize=9, color="#444")

    ax.legend(
        handles=[
            plt.Line2D([], [], color="red", ls="--", label="Bai-Perron K=3 break"),
        ],
        loc="upper left",
    )
    plt.tight_layout()
    out = OUT / "fig1_annual_events.png"
    plt.savefig(out)
    plt.close()
    print(f"  → {out.name}")


def fig2_actor_stacked():
    con = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT data_year, actor_type, COUNT(*) AS n FROM action_events "
        "WHERE data_year BETWEEN 2009 AND 2022 AND actor_type IS NOT NULL "
        "GROUP BY data_year, actor_type",
        con,
    )
    con.close()
    piv = df.pivot(index="data_year", columns="actor_type", values="n").fillna(0)
    piv = piv.reindex(YEARS).fillna(0)
    piv = piv[[c for c in ACTOR_ORDER if c in piv.columns]]
    share = piv.div(piv.sum(axis=1), axis=0) * 100

    fig, ax = plt.subplots(figsize=(10, 5.2))
    colors = plt.cm.tab10(np.linspace(0, 1, len(piv.columns)))
    labels = [ACTOR_EN.get(c, c) for c in piv.columns]
    ax.stackplot(YEARS, share.T.values, labels=labels, colors=colors, alpha=0.92)
    ax.set_ylim(0, 100)
    ax.set_title("Actor-type composition (within-year share %), 2009–2022")
    ax.set_xlabel("Year (data_year)")
    ax.set_ylabel("Share of yearly events (%)")
    # phase boundaries
    ax.axvline(2012.5, color="black", ls=":", lw=1, alpha=0.7)
    ax.axvline(2019.5, color="black", ls=":", lw=1, alpha=0.7)
    ax.text(2010.5, 102, "P1", ha="center", fontsize=10)
    ax.text(2016, 102, "P2", ha="center", fontsize=10)
    ax.text(2021, 102, "P3", ha="center", fontsize=10)
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=9, frameon=False)
    plt.tight_layout()
    out = OUT / "fig2_actor_stacked_area.png"
    plt.savefig(out)
    plt.close()
    print(f"  → {out.name}")


def fig3_diversity_with_breaks():
    """Shannon entropy on actor_type counts per data_year, with phase shading and break markers."""
    con = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT data_year, actor_type, COUNT(*) AS n FROM action_events "
        "WHERE data_year BETWEEN 2009 AND 2022 AND actor_type IS NOT NULL "
        "GROUP BY data_year, actor_type",
        con,
    )
    con.close()

    def H(s):
        p = s / s.sum()
        p = p[p > 0]
        return float(-(p * p.apply(math.log)).sum())

    H_by_year = df.groupby("data_year").apply(
        lambda g: H(g["n"]), include_groups=False
    )
    H_by_year = H_by_year.reindex(YEARS)

    fig, ax = plt.subplots(figsize=(9, 4.6))
    shade_phases(ax)
    ax.plot(YEARS, H_by_year.values, marker="o", color="#2c7fb8", lw=2)
    ax.set_title("Shannon entropy of actor_type distribution by data_year")
    ax.set_ylabel("Shannon H")
    ax.set_xlabel("Year")
    # peak label
    yr_max = int(H_by_year.idxmax())
    h_max = float(H_by_year.max())
    ax.annotate(
        f"peak\n{yr_max}: H={h_max:.2f}",
        xy=(yr_max, h_max),
        xytext=(yr_max - 4, h_max - 0.15),
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
        fontsize=9,
    )
    plt.tight_layout()
    out = OUT / "fig3_diversity_with_breaks.png"
    plt.savefig(out)
    plt.close()
    print(f"  → {out.name}")
    return H_by_year


def fig4_entry_mech_heatmap():
    """Entry-mechanism × actor-type heatmap (full sample, data_year 2009-2022)."""
    con = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT actor_type, entry_mechanism, COUNT(*) AS n FROM action_events "
        "WHERE data_year BETWEEN 2009 AND 2022 "
        "AND actor_type IS NOT NULL AND entry_mechanism IS NOT NULL "
        "GROUP BY actor_type, entry_mechanism",
        con,
    )
    con.close()
    piv = df.pivot(index="entry_mechanism", columns="actor_type", values="n").fillna(0)
    piv = piv.reindex(index=ENTRY_ORDER)
    piv = piv[[c for c in ACTOR_ORDER if c in piv.columns]]
    # Column-normalize to within-actor percentage
    col_pct = piv.div(piv.sum(axis=0), axis=1) * 100

    fig, ax = plt.subplots(figsize=(9, 4.4))
    im = ax.imshow(col_pct.values, cmap="YlGnBu", aspect="auto")
    ax.set_xticks(range(len(col_pct.columns)))
    ax.set_xticklabels([ACTOR_EN.get(c, c) for c in col_pct.columns], rotation=35, ha="right")
    ax.set_yticks(range(len(col_pct.index)))
    ax.set_yticklabels([ENTRY_EN.get(c, c) for c in col_pct.index])
    for i in range(len(col_pct.index)):
        for j in range(len(col_pct.columns)):
            v = col_pct.values[i, j]
            if v > 0:
                ax.text(j, i, f"{v:.0f}", ha="center", va="center",
                        color="white" if v > 40 else "black", fontsize=8)
    ax.set_title("Entry-mechanism share within actor-type column (%)")
    cb = plt.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
    cb.set_label("% within column")
    plt.tight_layout()
    out = OUT / "fig4_entry_mechanism_heatmap.png"
    plt.savefig(out)
    plt.close()
    print(f"  → {out.name}")


def fig5_local_share():
    """Local-government share trajectory with single-break (2017) overlay."""
    con = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT data_year, "
        "SUM(CASE WHEN actor_type='地方政府' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) * 100 AS local_share "
        "FROM action_events WHERE data_year BETWEEN 2009 AND 2022 GROUP BY data_year",
        con,
    )
    con.close()
    df = df.set_index("data_year").reindex(YEARS)

    fig, ax = plt.subplots(figsize=(9, 4.6))
    shade_phases(ax)
    ax.plot(YEARS, df["local_share"], marker="o", color="#e6550d", lw=2)
    ax.axvline(2017 - 0.5, color="red", ls="--", lw=1.5,
               label="Bai-Perron K=1 break: 2017")
    ax.set_title("Local-government share (%) per data_year")
    ax.set_ylabel("local-state share of yearly events (%)")
    ax.set_xlabel("Year")
    ax.legend(loc="upper right")
    plt.tight_layout()
    out = OUT / "fig5_local_share_trajectory.png"
    plt.savefig(out)
    plt.close()
    print(f"  → {out.name}")


def main():
    print(f"Writing figures to {OUT}/")
    fig1_annual_events()
    fig2_actor_stacked()
    fig3_diversity_with_breaks()
    fig4_entry_mech_heatmap()
    fig5_local_share()
    print("Done.")


if __name__ == "__main__":
    main()
