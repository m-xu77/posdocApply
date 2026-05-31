# Plan B — Analysis Plan (pre-registration-style)

**Version**: 0.1 (2026-05-31, project bootstrap)
**Status**: living document — versioned changes are logged in `decisions.md`.
**Posture**: This is written **before** running the second-stage regressions on real CFPS-merged data. Any deviation triggers a `decisions.md` entry and is reported in the paper.

---

## 1. Research questions, in formal terms

Let $i$ index households, $c$ index counties (≈ CFPS PSU), $p$ index provinces, and $t$ index years (2010, 2012, 2014, 2016, 2018, 2020, 2022 — the seven CFPS waves).

Let $\tau_c$ denote the causal effect of poverty-alleviation treatment exposure on a household-welfare outcome at the county level (the CATE — Conditional Average Treatment Effect — estimated from the dissertation's staggered DID pipeline). The treatment is the *精准扶贫* designation, with staggered roll-in 2013–2015 and treatment intensity 2014–2020.

Let $E_{p,t} \in \mathbb{R}^k$ denote the vector of organizational-ecology indicators constructed in `code/02_province_ecology_panel.py` (or the county-level analog in `code/03_county_ecology_panel.py`).

The pre-registered hypotheses, in the form $H_j: \mathbb{E}[\tau_c \mid E_p] = f_j(E_p)$:

- **H1 (diversity)**: counties in provinces with higher Shannon-entropy organizational ecologies have **larger** absolute treatment effects on log per-capita income and on the vulnerability index.
- **H2 (central-local)**: the relationship between central-government share and household effect is **non-monotone** (inverted-U), peaking at moderate central engagement.
- **H3 (social participation)**: higher *社会组织 / 团体* participation share has a **positive** effect on durability — i.e., 2020–2022 retention of household gains.
- **H4 (East-West pairing)**: counties whose province was assigned a high-development East partner in the canonical 2016 pairing list have **larger** effects, conditional on baseline poverty rate.

---

## 2. Identification

### 2.1 First stage: CATE estimation

The dissertation already supplies $\hat{\tau}_c$ from a staggered DID with two-way fixed effects (Callaway–Sant'Anna or Borusyak–Jaravel–Spiess to avoid the negative-weight problem in TWFE). This analysis plan inherits that identification.

Reusable artifacts from the dissertation:
- Treatment indicator $D_{c,t}$ (per-county roll-in year)
- Outcome panel: log income per capita, log consumption, vulnerability index (3-stage least squares per Chaudhuri 2003)
- Estimated $\hat{\tau}_c$ with cluster-robust SE

### 2.2 Second stage: ecology → effect

The main specification is a cross-sectional regression of $\hat{\tau}_c$ on county-aggregated ecology:

$$
\hat{\tau}_c = \alpha + \beta_1 \cdot \text{shannon}_{p(c)} + \beta_2 \cdot \text{central\_share}_{p(c)} + \beta_3 \cdot \text{social\_share}_{p(c)} + X_c' \gamma + \epsilon_c
$$

where $X_c$ contains pre-treatment county controls (baseline poverty rate, log GDP per capita 2010, log population, distance to provincial capital).

**Critical inferential adjustment**: $\hat{\tau}_c$ is itself a *generated regressor* — OLS standard errors will be too small. Two corrections:
1. Bootstrap the full pipeline (1,000 reps): re-estimate the CATE in each bootstrap, then re-run the second stage.
2. Murphy–Topel SE correction as a sanity check.

### 2.3 Identification of the second-stage coefficient

The second stage does **not** identify a causal effect of ecology on household welfare from OLS alone — ecology is endogenous to county characteristics. Three identification strategies:

- **IV-1 (East-West pairing)**: the **assigned East partner province's GDP per capita** as instrument for the soe_finance_share and central_share of the Western province. Exogeneity defense: the pairing was determined by Beijing (1996 establishment; 2016 canonical re-assignment) on geographic-coverage logic, not on Western-county dynamics. First-stage strength: target F > 10.
- **IV-2 (yearbook coverage shock)**: 2016 expansion of yearbook coverage as a shifter of *measured* ecology richness, conditional on year FE. (Weaker; reported as a sensitivity, not primary.)
- **IV-3 (terrain ruggedness)**: ruggedness index (Nunn-Puga style) as instrument for whether a county received a *central* state organ's *定点帮扶* designation — central organs were disproportionately assigned to the most-remote counties. Used for the central_share component only.

Robustness:
- **Coarsened exact matching** on pre-2013 covariates as a non-IV alternative.
- **Entropy balancing** (Hainmueller 2012) to balance moments of pre-period $X_c$ across high- vs low-diversity counties.

---

## 3. Mediation

Pre-registered mediation chain:

$$
\text{ecology}_{p,t} \to \text{resource flow}_{c,t} \to \text{household outcome}_{i,c,t}
$$

Mediator candidates (constructed from `action_events`):
- Per-capita fund value (`value_num`, with unit normalization to RMB / 万元)
- Per-capita training count (`action_type == 培训赋能`)
- Per-capita infrastructure events (`action_type == 基础设施建设`)
- Per-capita industry-introduction events (`action_type == 产业引入`)

Methods:
- Imai-Keele-Yamamoto sensitivity analysis (rather than naive Baron-Kenny).
- Report total / direct / indirect effects with bootstrapped CI.
- Cluster errors at the prefecture level (above county, below province) to absorb local spatial correlation.

---

## 4. Heterogeneity

Pre-registered heterogeneity cuts, each tested with both interaction terms and stratified samples:

1. **Region group**: 东北 / 东部 / 中部 / 西部 (NBS 4-group).
2. **Pre-2013 county poverty status**: "国家级贫困县" vs not.
3. **Topography**: mountainous (defined by NBS ruggedness > median) vs plain.
4. **Han / minority majority**: ethnic-minority autonomous county vs not.
5. **Distance from prefectural seat**: above / below median.

Each cut has a pre-registered direction of expected effect. Failure to find an effect in the *expected* direction is reported, not hidden.

---

## 5. Robustness battery

Run **all** of the following on the headline result; report in the appendix:

| Test | Variant | Why |
|---|---|---|
| Diversity measure | HHI; effective-number-of-types | Shannon is one choice; test invariance |
| Central/local cut | actor_type only vs include SOEs as central | Definitional sensitivity |
| Weighting | multi-region 1/n vs equal vs 1/√n | Aggregation choice sensitivity |
| Time window | 2009–2022 vs 2013–2020 | Restrict to the formal campaign window |
| Province FE | with vs without | Test against unobserved province heterogeneity |
| Year FE | with vs without | Test against macro shocks |
| Treatment definition | dissertation-canonical vs alternative roll-in | Robustness to dissertation choices |
| Outcome | per-capita income vs consumption vs vulnerability | Outcome-definition sensitivity |
| Inference | OLS clustered SE vs wild-cluster bootstrap | Few-cluster correction |
| Sample | drop top-1% leverage counties vs full | Influential-observation robustness |
| Placebo (time) | pretend 2009 = treatment year | Should yield null |
| Placebo (outcome) | run on a not-credibly-affected outcome | Should yield null |

---

## 6. Coverage and external-validity scope

Before any inferential claim, this project requires a published **coverage diagnostic**:

- For each CFPS PSU (county), record (a) total number of action events identified in the database, (b) number of distinct actor_types observed, (c) span of years observed.
- Report the fraction of CFPS households whose county has ≥10 events and ≥3 actor types observed. The inferential population is **only** those households. The rest are reported but explicitly out of scope.

This is the *Li Shi rule*: never claim more than the sampled frame can support.

---

## 7. Data-quality decisions

Documented in `decisions.md`. Highlights so far:

- `actor_gov_level` is empty across the DB; the central/local indicators are derived from `actor_type` (中央政府 / 地方政府) instead. *(2026-05-31)*
- Multi-province events are exploded long-format with weight $1/n$ across provinces. Alternative weighting schemes are part of the robustness battery. *(2026-05-31)*
- `value_unit` is heterogeneous (元 / 万元 / 亿元) and not yet normalized — `total_value_num` in the current panel is therefore **NOT** comparable across rows. Stage 04 will introduce a unit-normalization step.

---

## 8. Reporting standards

- Every regression table: point estimate, OLS-cluster SE, wild-cluster-bootstrap SE, and the corresponding p-values for both.
- Every figure: include the underlying numbers in a companion CSV in `output/tables/`.
- All code: deterministic random seeds (`SEED = 20260531` for the project).
- All bootstraps: 1,000 reps unless explicitly noted.

---

## 9. Open questions for advisors

For Zhang Xiulan (BNU dissertation chair):
- Should we re-run the staggered DID with Borusyak–Jaravel–Spiess (BJS) or stick with the dissertation's Callaway–Sant'Anna?
- Are the original CATE estimates exportable at the county level, or only at the province level?

For Robert Walker (international advisor):
- Recommended framing for the Western audience: organizational ecology (Hannan-Freeman) vs implementation studies (Pressman-Wildavsky / Hupe) vs governance regimes (Hood / Bevir)?

For Xiaoxin Xu (CCCW connection):
- Whether the CCCW seminar audience would expect explicit comparison with Li Cheng's leadership-databank methodology in the introduction — i.e., framing the action_events database as a CCP-implementation analog of Li Cheng's cadre databank.

---

## 10. Open dependencies

- [ ] County-level region standardization (currently we have province only)
- [ ] CFPS county-CATE export from the dissertation repo
- [ ] Value-unit normalization (`value_num` × `value_unit` → RMB)
- [ ] Coverage diagnostic table

These block the move from descriptive (current state) to inferential (Phase 2 deliverable).
