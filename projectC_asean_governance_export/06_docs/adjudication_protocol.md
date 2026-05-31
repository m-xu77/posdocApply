# Adjudication Protocol

Used in Stage 5 when coder A and coder B disagree on a paragraph in the 400-document gold sample.

## Rules

1. **Adjudicator is blind to LLM output** for that paragraph at the time of decision.
2. **Frame-presence disagreement** (one coder says ≥ 1 frame, the other says none): adjudicator decides presence; if presence, picks frame_id(s).
3. **Frame-identity disagreement** (both say frames but disagree which): adjudicator picks one or marks both as valid. If both valid, the dictionary entry pair is flagged in `manual_review_notes.md` for refinement (signature/contrast phrases may be too overlapping).
4. **"Uncertain" from either coder + the other not-uncertain**: adjudicator decides; uncertainty noted in `notes` of `adjudicated.csv`.
5. **Both uncertain**: paragraph excluded from gold; replacement drawn from the same stratum.

## Documentation

Every adjudicated row in `adjudicated.csv` carries:

- `paragraph_id`
- `final_frame_ids`
- `disagreement_type` ∈ {presence, identity, uncertain_single, uncertain_both, no_disagreement}
- `dictionary_refinement_flag` (bool)
- `adjudicator_note` (free text)

## Who adjudicates

PI is default adjudicator for v1. A second senior collaborator (CCCW associate) cross-reviews 20% of adjudicated rows; disagreement rate reported in the published methods section.
