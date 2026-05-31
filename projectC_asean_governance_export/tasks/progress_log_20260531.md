# Progress Log — 2026-05-31

**Session goal**: scaffold Plan C as a CCCW-grade research project ready to onboard collaborators.

## What was created today

### Top-level
- `README.md` — project north-star (motivation, contribution, layout, reproducibility commitments).
- `pyproject.toml` — Python project metadata.
- `.gitignore`, `.env.example` — repo hygiene.

### `00_design/` (intellectual foundation; design phase v0.1)
- `01_research_questions.md` — master Q + 4 sub-questions, boundary conditions, what is *not* claimed.
- `02_theoretical_framework.md` — four-layer chain: framing → diffusion → bureaucratic politics → SSC grammar.
- `03_hypotheses.md` — 8 pre-registered hypotheses (H1–H8) with explicit decision rules and falsifiers.
- `04_methodology.md` — 8-stage pipeline from raw docs to manuscript.
- `05_research_ethics.md` — data redistribution policy + scope boundaries + sensitivities.

### `01_literature/`
- README with five-pillar plan + status tracker.
- `pillar_1_policy_diffusion.md` — frame travel, ideational diffusion.
- `pillar_2_china_aid_bri_gdi.md` — empirical landscape on Chinese outward engagement.
- `pillar_3_china_asean.md` — CLMV regional grounding.
- `pillar_4_text_as_data_llm.md` — methods precedent.
- `pillar_5_comparative_donor_discourse.md` — DAC-vs-SSC contrast.
- `bibtex/full.bib` — seeded with ~15 high-priority citations.

### `02_data/`
- README + folder skeleton (raw / processed / domestic_dict / metadata / annotation).
- `domestic_dict/domestic_frame_dictionary.schema.json` — JSON schema for the dictionary.
- `domestic_dict/domestic_frame_dictionary.json` — schema-conformant placeholder (v0.0.0).
- `metadata/doc_metadata_template.csv` + `country_year_covariates.csv` headers.
- `annotation/codebook_for_annotators.md` — operational rules for the 400-paragraph gold sample.

### `03_pipeline/`
- README documenting design rules (deterministic, idempotent, loud).
- `utils/`: `http_client.py`, `llm_runner.py`, `logging_setup.py` — typed scaffolds.
- `scrapers/`: six scrapers (MFA, MOFCOM, CIDCA, GDI, WB, ADB) — typed scaffolds.
- `preprocessing/clean.py` — typed scaffold.
- `frame_extraction/`: `build_dictionary.py`, `extract.py` — typed scaffolds.
- `frame_extraction/prompts/`: `v1_extract.txt`, `v1_build_dict.txt` — versioned prompts.
- `validation/iaa.py` — typed scaffold.

### `04_analysis/`
- README mapping notebooks 00–09 to hypotheses, with input/output spec.
- `notebooks/README.md`.

### `05_output/`
- README + `paper_drafts/working_paper_v0_skeleton.md` — manuscript section plan.

### `06_docs/`
- README.
- `codebook.md` — every variable in every artifact.
- `pipeline_doc.md` — operator manual to reproduce end-to-end.
- `reproducibility.md` — determinism / versioning / prompts / logs commitments.
- `adjudication_protocol.md` — coder-disagreement procedure.

## What was verified empirically (per the memory rule)
- All 13 pipeline `.py` modules compile cleanly via `py_compile` (no syntax errors in the scaffolds).
- Dictionary schema and placeholder JSON parse cleanly and have the expected key sets.
- Folder tree present and laid out as specified by the README §4.

## What is NOT yet done (next session)
- **Power simulation notebook** — write `notebooks/00_power_simulation.ipynb` to confirm the H3 effect is detectable at expected agency-cell n.
- **Pilot dictionary build** — wire `utils/llm_runner.py` to Anthropic + OpenAI + Qwen and run `build_dictionary.py` on the 25,358-event base to produce dictionary v0.5.
- **Pilot scrape (Q1)** — wire `mfa_readouts.py` to fetch the 2020–2021 pilot window for one country (Cambodia) to validate the scrape discipline before scaling.
- **Power simulation results** — feed back into `00_design/03_hypotheses.md` (decision rules may shift if effect size or n changes).
- **Annotator recruitment** — identify and brief a second coder for the 400-paragraph gold sample.

## Risks logged
- The CIDCA portal historically has unstable HTML; scraper resilience needs to be verified early.
- Some MOFCOM bilateral-agreement pages are JS-rendered; revisit if BeautifulSoup-only crawl misses material.
- Qwen3 API rate limits may not support large-batch ensemble runs; fallback is to drop Qwen to a 20% spot-check role rather than full ensemble.

## Decisions made today
- **Folder layout**: numbered 00–06 + tasks/ to keep reading order obvious.
- **Frame-dictionary key**: (actor_type × action_type × entry_mechanism) is the unit, with separate flags for governance / infrastructure frames.
- **Validation n**: 400 paragraphs is the gold-set target (stratified 4 × 4 × 4 = 64 cells × ~6 paragraphs).
- **Pre-registration**: design and hypothesis docs dated 2026-05-31; any subsequent change must be amended in `tasks/preregistration_amendments.md`.

## Cross-references
- Strategic plan: `../reasearch_plans/plan_C_asean_export.md`
- Overall strategy doc: `../reasearch_plans/strategy.md`
- Domestic data source: `../../output_v3/research_enhanced.db`
- Pipeline this builds on: `../../src_v3/`
