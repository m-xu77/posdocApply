# Annotators' Codebook — Validation Sample (n = 400 paragraphs)

**Audience**: PI + RA (lead annotator) + adjudicator.
**Goal**: produce a gold-standard set against which dictionary recall + precision are measured (H8).

---

## 1. The task in one sentence

For each paragraph, decide (a) whether it carries any frame from the domestic frame dictionary, and (b) if yes, which frame_id(s).

## 2. Sampling design

- 400 paragraphs total.
- Stratified across 4 agencies × 4 countries × 4 year buckets (2013–15, 2016–18, 2019–21, 2022–26) ≈ 6.25 per cell.
- Paragraphs are 80–250 tokens; longer paragraphs are split at the nearest sentence boundary.

## 3. Step-by-step coding rules

1. **Read the whole paragraph** before deciding.
2. **Multiple frames allowed** if more than one is clearly carried.
3. **A frame is "carried" when** the paragraph (a) names or unambiguously describes the diagnostic and (b) gestures at the prognostic articulated in the dictionary entry.
4. **A signature phrase alone is not sufficient** if the larger meaning is contradictory or generic.
5. **When unsure, mark `uncertain`** and add a one-sentence note; do not guess.
6. **Translation paragraphs**: if the doc is in a CLMV language, code from the original (with translation as aid). If only the translation is available, code from it but flag the row.

## 4. Output schema (per coder CSV)

| column | type | meaning |
|--------|------|---------|
| `paragraph_id` | str | matches sampled-paragraph id |
| `coder_id` | str | A / B / adjudicator |
| `frame_ids` | str | pipe-separated frame_ids; empty if none |
| `uncertain` | int | 0/1 |
| `notes` | str | free text |
| `coded_at` | datetime | UTC iso |

## 5. Adjudication

Where coder A and coder B disagree:

- **Frame-presence disagreement** (one says any frame, the other says none): adjudicator decides.
- **Frame-identity disagreement** (both say a frame but disagree on which): adjudicator picks one or marks both as plausible (the dictionary entry is then flagged for refinement).
- Adjudicator decisions become `adjudicated.csv`; the disagreement record is preserved.

## 6. Inter-annotator agreement

- Cohen's κ on frame-presence (binary).
- Krippendorff's α on frame-identity (multi-label).
- Both reported in `iaa_report.md`.

## 7. Time budget

Target 60–90 paragraphs per coder per day; ~5 working days each.
