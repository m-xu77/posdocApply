# 03 · Testable Hypotheses

**Document status**: v0.1 — pre-registered before any outward-corpus collection begins
**Last updated**: 2026-05-31

> Each hypothesis is paired with: the data it speaks to, the test, the decision rule, what would falsify it, and the prior-belief prediction (so we can later detect hindsight-bias drift).

---

## H1 — Frame transplantation is non-trivial

**Statement**: At least 30% of tokens in the outward CLMV corpus fall within frames that exist in the domestic frame dictionary, controlling for generic developmental boilerplate.

- **Test**: dictionary-matched-token share, computed per document, mean across the corpus.
- **Decision rule**: H1 supported if 95% bootstrap CI lower bound > 25%.
- **Falsification**: lower-bound CI ≤ 15% would imply outward discourse is largely sui generis.
- **Prior belief**: 40–55% (moderate-to-strong reproduction).

## H2 — Bureaucratic agencies diverge in frame mix

**Statement**: The (agency × frame) joint distribution is statistically distinguishable from agency-independent baseline.

- **Test 1 (overall)**: chi-square test of independence on (agency, frame) contingency table after collapsing rare frames (<1% column share).
- **Test 2 (pairwise)**: pairwise cosine similarity between agency frame-profile vectors; bootstrap CI from document-level resampling.
- **Decision rule**: H2 supported if (a) overall chi-square p < 0.001 with effect size Cramér's V ≥ 0.15, AND (b) at least one pairwise agency cosine similarity < 0.85.
- **Falsification**: All pairwise cosines > 0.95.
- **Prior belief**: H2 holds; CIDCA most distinct.

## H3 — CIDCA is the governance-frame outlier

**Statement**: CIDCA documents have a higher *governance-to-infrastructure ratio* (GIR) than each of MFA, MOFCOM, and central-SOE documents, with non-overlapping bootstrap CIs.

- **Operationalization of GIR**:
  - *governance frames*: subset of dictionary frames whose domestic codings are dominated by `action_type ∈ {policy_design, supervision, mobilization, training, evaluation}` and `entry_mechanism ∈ {党政体系, 联席会议, 督查考核}`.
  - *infrastructure frames*: subset dominated by `action_type ∈ {project_construction, asset_transfer, financing}` and `entry_mechanism ∈ {项目立项, 资金拨付}`.
  - GIR = governance-frame density / (infrastructure-frame density + ε).
- **Test**: bootstrap-CI overlap test on document-level GIR by agency.
- **Decision rule**: H3 supported if CIDCA's 95% CI lies entirely above each of the other three agencies' CIs.
- **Falsification**: CIDCA's CI overlaps MFA's substantially or lies below MOFCOM's.
- **Prior belief**: H3 holds in direction; statistical separation is uncertain because of CIDCA's smaller corpus.

## H4 — Country mix differs

**Statement**: The frame mix per recipient country is statistically distinguishable across the four CLMV states.

- **Test**: chi-square on (country, frame) table; PERMANOVA on document-level frame composition vectors with country as treatment.
- **Decision rule**: supported if p < 0.001 and Cramér's V ≥ 0.10.
- **Falsification**: V < 0.05.
- **Prior belief**: H4 holds but effect is small; alignment-driven not size-driven.

## H5 — Alignment dominates dependency as a driver of country variation

**Statement**: Within a frame-density panel regression (frame share regressed on country-year covariates), the V-Dem regime-alignment composite has a larger standardized coefficient than the lagged trade-dependency or aid-per-capita variables.

- **Test**: panel OLS with year and frame fixed effects, country-clustered SEs.
- **Decision rule**: standardized β(alignment) > 1.5 × max(standardized β(other covariates)).
- **Falsification**: dependency dominates.
- **Prior belief**: weak prior; this is genuinely uncertain.

## H6 — 2018 CIDCA founding is the dominant structural break

**Statement**: In a Bai–Perron multiple-breakpoint test on the monthly aggregate governance-frame-density series for the whole outward corpus, 2018Q1–Q2 yields the largest reduction in residual sum of squares among the three pre-registered candidate dates (2013Q3–Q4, 2018Q1–Q2, 2021Q3–Q4).

- **Test**: Bai–Perron with maximum 3 breaks, trimming parameter 0.15.
- **Decision rule**: 2018 break is the largest if its RSS reduction is at least 1.2× the next-largest candidate's.
- **Falsification**: 2013 or 2021 dominates, or no significant break.
- **Prior belief**: 2018 dominates, but 2021 may be a close second due to GDI rebranding.

## H7 — Robustness to LLM choice

**Statement**: Frame-count rank order across documents is stable across at least two of {Claude Opus 4.7, GPT-5, Qwen3} extractions; Spearman ρ ≥ 0.85 between any two models on the validation set.

- **Test**: pairwise Spearman ρ on validation-set frame counts.
- **Decision rule**: supported if all three pairwise ρ ≥ 0.80, with at least two ≥ 0.85.
- **Falsification**: any pairwise ρ < 0.65.
- **Prior belief**: holds; this is a sanity check on the measurement layer.

## H8 — Frame dictionary coverage is high

**Statement**: On a stratified random sample of 400 outward-corpus paragraphs, manually coded "is-frame-bearing", the dictionary recall ≥ 0.85 and precision ≥ 0.80.

- **Test**: recall and precision against gold annotation.
- **Decision rule**: supported if both thresholds met.
- **Falsification**: recall < 0.70 or precision < 0.65.
- **Prior belief**: precision likely high; recall is the risk.

---

## Pre-registration commitments

- This document is dated 2026-05-31, before any outward corpus collection has begun beyond the 2.1 pilot referenced in `plan_C_asean_export.md`.
- Modifications after first outward-corpus document is collected must be versioned and justified in `tasks/preregistration_amendments.md`.
- Decision rules are committed; the analyst pre-commits to publishing falsifying results.

## Summary table

| H | What it tests | Headline metric | Decision rule |
|---|---------------|-----------------|---------------|
| H1 | Frame transplantation | Token-share matched | 95% CI LB > 25% |
| H2 | Agency divergence (overall) | Cramér's V; cosine | V ≥ 0.15 AND ≥ 1 cosine < 0.85 |
| H3 | CIDCA governance-outlier | Bootstrap CI on GIR | CIDCA CI above others |
| H4 | Country differentiation | Cramér's V; PERMANOVA | V ≥ 0.10 |
| H5 | Alignment > dependency | Standardized β | β(align) > 1.5×β(other) |
| H6 | 2018 break dominance | Bai–Perron RSS | 2018 RSS-Δ ≥ 1.2× next |
| H7 | Model-robustness | Pairwise Spearman ρ | all ≥ 0.80; ≥ 2 ≥ 0.85 |
| H8 | Dictionary coverage | Recall, precision | R ≥ 0.85, P ≥ 0.80 |
