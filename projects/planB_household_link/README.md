# Plan B — From Household Effects to Implementation Variation

**Working title**: *"Whose Implementation? How Organizational Ecologies of Chinese Anti-Poverty Governance Shape Household Welfare, 2010–2022."*

**Version**: 2026-05-31 (project bootstrap)
**Status**: data infrastructure phase
**Lead**: Mengnan Xu (mengnanxu2333@gmail.com)
**Target output**: 1 working paper → *World Development* / *Journal of Development Economics* (short paper) / *Governance*
**Companion track**: CCCW Postdoc Application Project 1 (with Plan A as the structural twin)

---

## 1. Research charter

### 1.1 Position

This project sits at the intersection of three research traditions:

- **Chinese political-leadership / governance studies** (the *Li Cheng* axis at CCCW) — taking organizational composition and central-local coordination as first-class explananda rather than control variables.
- **Household poverty empirics** (the *Li Shi* / CHIP axis) — taking household welfare and vulnerability dynamics as the dependent variables of governance.
- **Computational text-as-data + causal identification** — using the LLM-extracted organizational-ecology database (`output_v3/research.db`, 25,358 action events, 717 organizations, 14 years) as the bridge.

The signature claim: *China's poverty effect cannot be understood as "the policy worked" — it must be understood as a vector of implementation regimes whose composition is empirically observable and causally tractable.*

### 1.2 Calibration to the Li Cheng / Li Shi benchmark

This project commits to operating at a level peer to the field's leaders, not as imitation but as method:

| Standard | Li Cheng's discipline | Li Shi's discipline | Our application |
|---|---|---|---|
| Data construction | Multi-decade leader biographic databank | Multi-wave CHIP household survey | Multi-year, structured action-event ledger from State-Council yearbooks |
| Unit of analysis | Politburo / Central Committee cohorts | Income deciles, regional households | Province × year organizational ecologies |
| Inferential mode | Cohort comparison, longitudinal mapping | Decomposition, inequality estimation | Heterogeneity-in-CATE on ecology features |
| Theory–data integration | "Technocrats", "factions", "princelings" — concepts grounded in data | "Migrant-resident", "transient poverty" — concepts grounded in data | "Implementation regimes", "central-local bonding" — concepts grounded in data |
| Output standard | Brookings monograph + *China Quarterly* / *Asian Survey* articles | *Journal of Development Economics*, *World Development*, *Review of Income and Wealth* | Same journal tier targeted |

The dual benchmark forces both political-organizational sophistication (Li Cheng) and rigorous household-causal identification (Li Shi). Neither alone is enough.

### 1.3 Research questions

**RQ1 (structure → effect)**
Does organizational diversity (Shannon entropy on `actor_type`) at the provincial level associate with larger / more durable household poverty-reduction effects?

**RQ2 (mechanism → effect)**
Among entry mechanisms — *定点帮扶 / 东西协作 / 社会参与 / 市场进入 / 政策驱动 / 行业援助* — which best predicts reductions in household vulnerability conditional on baseline poverty?

**RQ3 (composition → effect)**
Are provinces dominated by central state organs and SOEs systematically different from provinces with denser social-org / university / private participation, after controlling for fiscal capacity?

**RQ4 (durability)**
Conditional on the 2020 全面脱贫 announcement, which organizational ecologies sustained the anti-return-to-poverty effect in 2021–2022?

---

## 2. Data assets

### 2.1 In place

| Asset | Source | Status |
|---|---|---|
| `action_events` (25,358 rows) | `output_v3/research.db` | ready; needs region standardization |
| `organizations` (717 rows, 17 types) | `output_v3/research.db` | ready |
| `toc_entries` (3,093 rows) | `output_v3/research.db` | ready |
| CFPS seven-wave household panel (2010–2022) | dissertation work | external; pipeline reused |
| Staggered-DID CATE estimates | dissertation work | external; need re-extraction at county/province granularity |

### 2.2 Needs build

| Asset | Owner | Blocking? |
|---|---|---|
| Region → GB/T 2260 admin-code map | this project (`code/01_standardize_region.py`) | **yes, blocks all aggregation** |
| Province × year ecology panel | this project (`code/02_province_ecology_panel.py`) | yes, blocks merge |
| County × year ecology panel | this project (`code/03_county_ecology_panel.py`) | yes, blocks county merge |
| County coverage diagnostic | this project (`code/04_coverage_diagnostic.py`) | yes, gates external validity claims |
| Province- and county-CATE extracts (from dissertation pipeline) | external (dissertation repo) | yes for second-stage |

### 2.3 Stretch / later

- 国务院扶贫办 "定点帮扶县" official list (instrument candidate)
- 县级年鉴 fiscal / demographic covariates
- East-West pairing canonical assignment list

---

## 3. Project folder layout

```
planB_household_link/
├── README.md                — this file
├── code/                    — versioned Python; one numbered script per stage
│   ├── 01_standardize_region.py
│   ├── 02_province_ecology_panel.py
│   ├── 03_county_ecology_panel.py
│   ├── 04_coverage_diagnostic.py
│   ├── 05_figures_province.py
│   └── …
├── data/
│   ├── raw/                 — GB/T 2260 lookup, external lists
│   ├── interim/             — events_geo.parquet, partial joins
│   └── processed/           — province_ecology_panel.parquet, etc.
├── output/
│   ├── figures/             — publication-grade PDFs/PNGs
│   ├── tables/              — TeX-ready / Markdown tables
│   └── logs/                — run logs, coverage reports
├── paper/                   — manuscript (Markdown → LaTeX)
├── refs/                    — BibTeX, key papers
└── docs/
    ├── analysis_plan.md     — pre-registration-style spec
    ├── codebook.md          — variable definitions
    └── decisions.md         — design-choice log
```

### 3.1 Code discipline

- Every script is **idempotent** and **deterministic** (random seeds fixed where relevant).
- Every script writes a **log** to `output/logs/<script>_<timestamp>.log` recording inputs, row counts, and runtime.
- Every script is callable as a standalone module: `python code/02_province_ecology_panel.py`.
- Numbered prefixes encode the DAG; later scripts read only the parquet outputs of earlier ones, never the raw DB directly (after stage 01).

### 3.2 Empirical discipline

- Treat every estimate with two errors: a coverage error and an identification error. Report both.
- For every dimension on which we cut data, run a placebo cut.
- No effect claim without a robustness battery defined in `docs/analysis_plan.md` **before** running it.

---

## 4. Roadmap

### Phase 0 — Bootstrap (this commit, 2026-05-31)

- [x] Project folder structure
- [x] Research charter (this README)
- [ ] Region standardization pipeline
- [ ] Province-year ecology panel
- [ ] One diagnostic figure (Shannon diversity heatmap)
- [ ] Analysis plan v0.1

### Phase 1 — Pre-application (→ 2026-06-30)

- [ ] County standardization (best-effort; flag failures)
- [ ] Coverage diagnostic (county-level overlap with CFPS PSU list)
- [ ] Second-stage regression skeleton (with simulated CATE)
- [ ] Project pitch paragraph for CCCW PS (linked from `application/cccw_personal_statement.md`)

### Phase 2 — Working paper (Q3 2026 – Q1 2027)

- [ ] CFPS-CATE re-extraction at county granularity
- [ ] Province + county merged dataset
- [ ] Main heterogeneity regressions + IV
- [ ] Mediation: ecology → resource flow → household outcome
- [ ] Full robustness battery
- [ ] Draft → internal review (Zhang / Walker / Xu) → submission

### Phase 3 — Submission and revision (Q2 2027 onward)

- [ ] *World Development* submission
- [ ] R&R cycle
- [ ] Companion piece (with Plan A) coordinated

---

## 5. Quality bars

A submission-ready manuscript must satisfy **all** of:

1. **Identification**: at least one IV strategy survives weak-instrument tests; staggered-DID assumption is explicitly defended.
2. **Measurement**: every ecology indicator has a robustness alternative (e.g., Shannon → HHI; central-local ratio with/without SOEs).
3. **Coverage**: external-validity scope explicitly bounded by the county-overlap diagnostic.
4. **Theory**: claims framed in terms of *organizational ecology* + *Chinese governance* literatures, not as a generic empirical exercise.
5. **Replicability**: full pipeline runs end-to-end from `output_v3/research.db` and CFPS source files in < 1 hour on a laptop.
6. **Visual**: every key result has a publication-grade figure where the figure alone communicates the finding.

---

## 6. Related documents

- `posdocApplyResearch/reasearch_plans/plan_B_household_link.md` — original plan
- `posdocApplyResearch/reasearch_plans/strategy.md` — overall application strategy
- `posdocApplyResearch/reasearch_plans/plan_A_org_ecology.md` — sibling project (Project 1 companion)
- `output_v3/research.db` — source DB
- `src_v3/` — extraction pipeline (upstream of this project)
