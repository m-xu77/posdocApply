# Codebook

This document defines every variable in every artifact the project produces.

## 1. Frame-dictionary entry

Schema: `02_data/domestic_dict/domestic_frame_dictionary.schema.json`.

| Field | Type | Definition | Allowed values / range |
|-------|------|------------|------------------------|
| `frame_id` | str | Stable slug for the frame | `[a-z0-9_]+`, unique |
| `actor_type` | str | Source actor type | 17 organization types from `output_v3` |
| `action_type` | str | Source action type | 11 categories |
| `entry_mechanism` | str | Source entry mechanism | 7 categories |
| `label_zh` / `label_en` | str | Short human-readable label | ≤ 15 chars zh / ≤ 8 words en |
| `diagnostic_zh` / `_en` | str | Snow–Benford diagnostic | 1–2 sentences |
| `prognostic_zh` / `_en` | str | Snow–Benford prognostic | 1–2 sentences |
| `signature_phrases_zh` | array[str] | Distinctive phrases | 8–15 items |
| `contrast_phrases_zh` | array[str] | Look-alike phrases that are NOT this frame | 3–5 items |
| `n_source_events` | int | Events in source cell | ≥ 5 (sparse cells excluded) |
| `is_governance_frame` | bool | Per H3 governance-frame rule | true ⇔ action_type ∈ {policy_design, supervision, mobilization, training, evaluation} |
| `is_infrastructure_frame` | bool | Per H3 infrastructure-frame rule | true ⇔ action_type ∈ {project_construction, asset_transfer, financing} |
| `manual_reviewed` | bool | PI has reviewed | default false |
| `merge_candidates` | array[str] | Near-duplicate frame_ids flagged by embedding | cosine ≥ 0.92 |

A frame can be neither governance nor infrastructure (e.g., a frame about mobilization that is logistical). Both flags `false` is valid.

## 2. Document metadata row

`02_data/metadata/doc_metadata.parquet`.

| Field | Type | Definition |
|-------|------|------------|
| `doc_id` | str | sha256(url + fetched_at) truncated to 16 chars |
| `url` | str | Canonical URL |
| `fetched_at` | datetime UTC | When the scraper retrieved it |
| `sha256` | str | sha256 of the raw bytes |
| `publisher` | str | Hosting organization (e.g., "fmprc.gov.cn") |
| `agency` | enum | {MFA, MOFCOM, CIDCA, SOE, GDI, WB, ADB, CLMV_GOV, OTHER} |
| `target_country` | enum | {KH, LA, MM, VN, MULTI, NONE} |
| `pub_date` | date | Publication date extracted from page |
| `doc_type` | enum | {readout, agreement, training_material, treaty, policy_paper, project_doc, press_release, other} |
| `lang` | str | ISO 639-1 |
| `word_count` | int | Token count of cleaned text |
| `raw_path` | str | Path under `02_data/raw/` |
| `clean_path` | str | Path under `02_data/processed/` |
| `notes` | str | Free text |

## 3. Frame-extraction result row

`04_analysis/frame_extraction_results.parquet`.

| Field | Type | Definition |
|-------|------|------------|
| `doc_id` | str | FK → `doc_metadata.doc_id` |
| `model_id` | enum | {claude-opus-4-7, gpt-5, qwen3-72b} |
| `model_version` | str | Provider-supplied version string at call time |
| `prompt_hash` | str | sha256 of the rendered prompt |
| `frame_id` | str | FK → dictionary |
| `count` | int | Span hits in the document |
| `density` | float | count × 1000 / word_count |
| `mean_confidence` | float | Mean of per-span confidences in [0, 1] |
| `extracted_at` | datetime UTC | Call timestamp |

## 4. Annotation row

`02_data/annotation/coder_*.csv`.

See `02_data/annotation/codebook_for_annotators.md` for the operational rules and the CSV schema.

## 5. Country-year covariates

`02_data/metadata/country_year_covariates.csv`.

| Field | Source | Notes |
|-------|--------|-------|
| `china_aid_per_capita_usd` | AidData v3 | USD constant |
| `trade_dep_china_share` | UN Comtrade | export+import to China / total |
| `vdem_polyarchy` | V-Dem v15 | electoral democracy index |
| `regime_alignment_index` | constructed | weighted UN-GA voting agreement + bilateral comprehensive-partnership level |

The construction recipe for the alignment index is in `04_analysis/notebooks/04_country_comparison.ipynb` Section 2.
