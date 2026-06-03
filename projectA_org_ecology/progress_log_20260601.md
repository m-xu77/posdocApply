# Progress Log — projectA · 2026-06-01

**Session goal**: replace placeholder numbers in §5.7 (robustness) and §6.2 (alt-coding) with values computed directly from the database, in response to user's question about analysis tooling.

## Summary

Five robustness checks were re-run. Two checks were modified or discarded because the underlying database does not support them as originally described. Three checks produced real values; one differed materially in magnitude from the placeholder; one was discarded; one was substituted with a weaker available check. All headline patterns of the paper are preserved.

## Detailed corrections

### Check 1 — Page-count normalization
- **Placeholder**: P1→P3 per-page ratio 1.3× (paper said "explains some but not most of the increase").
- **Verified**: P1→P3 per-page ratio **4.03×** (placeholder was off by 3× in the wrong direction).
- **Recipe**: SUM of `yearbooks.total_pages` by phase mapped from data_year + 1; events from `action_events`.
- **Phase pages**: P1 = 3,884; P2 = 7,309; P3 = 3,572.
- **Phase events/page**: P1 = 0.727; P2 = 1.652; P3 = 2.929.
- **Headline impact**: the intensification signal is essentially undiminished by yearbook-length normalization; the original placeholder substantially understated this.

### Check 2 — Confidence stratification
- **Placeholder**: subset n = 9,217 with `confidence='high'`.
- **Reality**: `confidence='high'` rows = 0. Distribution is `medium` 25,211 / `low` 147.
- **Substitution**: low-confidence-exclusion check (removes only 147 rows / 0.58% of sample).
- **Verified result**: actor shares change by ≤ 0.4 pp on any category; pattern preserved but check is weak.
- **Flagged in paper**: "this is a weak check; a stronger version awaits a human-reviewed stratified sample."

### Check 3 — Publication-lag
- **Placeholder**: exclude `|pub_year - data_year| > 2` (claimed 1,134 rows excluded).
- **Reality**: every row has `pub_year - data_year = 1` exactly, by yearbook convention. Zero rows to exclude. Check is not feasible in this corpus.
- **Action**: removed from §5.7; moved to appendix §C.4 as a "discarded check" with the substantive concern documented as a planned cross-corpus test.

### Check 4 — Alternative diversity indices
- **Placeholder**: Inverse Simpson 5.0 (2013) / 7.4 (2018) / 7.1 (2022) / 3.6 (2023).
- **Verified**: 4.3 / 6.4 / 5.8 / 3.3 (computed on distinct-`actor_std` per (pub_year, actor_type) cells using fresh `pandas` script).
- **Headline impact**: trajectory and peak year preserved; magnitudes shifted by 0.5–1.0 units.

### Check 5 — §6.2 alt-coding (exclude 协调监督)
- **Placeholder**: 39.6% governance vs 25.0% infrastructure.
- **Verified**: **43.8% governance vs 29.0% infrastructure** (denominator 18,133 events).
- **Headline impact**: gap is 14.8 pp, slightly wider than the placeholder's 14.6 pp. Direction preserved.

## How the numbers were obtained this session

- **Tool**: `sqlite3` CLI for headline aggregates; one-shot `pandas` script for diversity indices (recipe in `analysis_notes/headline_statistics.md`).
- **Not used**: Stata. Not used anywhere in this project.
- **Languages**: Python (pandas, networkx, matplotlib for the pre-existing `src_v3/analysis/`) + SQL (for new aggregates this session).
- **Pre-existing infrastructure**: `src_v3/02_extract_actions.py` produces the action_events table via rules-based regex on yearbook page text (not LLM); `06_enhance_research.py` adds LLM-filled governance/entry mechanism fields; `analysis/ch{3,4,5}_*.py` produced the `output_v3/figures/` and `output_v3/tables/` artifacts referenced in the paper.

## Files updated this session

- `paper_drafts/working_paper_v1.md` — §5.7 and §6.2 rewritten with verified numbers; word count now 8,534 (body 8,066).
- `paper_drafts/supplementary_appendix.md` — §C completely rewritten with the 2026-06-01 re-run.
- This file.

## What remains genuinely unaddressed

- **Bai-Perron formal break test** — still deferred. Plan: monthly aggregation + seasonal pre-whitening + `ruptures` library.
- **Stratified human re-coding sample** for a strong confidence check.
- **Provincial-yearbook cross-corpus check** for the documentation-artifact concern.
- **Hand-audit of the post-2018 research-institute spike** (~50 events) to discipline the recoding-artifact alternative explanation.

These are all flagged in the paper's §6.3 (Limits) and §5.7 prefatory note.

## Methodological note for future audits

In the future, every paper-tier numeric claim should be paired with the exact SQL or Python recipe that produced it, captured before being written into prose. The §5.7 errors arose because I drafted prose with plausible-looking numbers before running the underlying queries; the correct workflow is the reverse.
