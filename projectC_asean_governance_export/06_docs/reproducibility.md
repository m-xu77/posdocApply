# Reproducibility Statement

This project is built so that an external reviewer or future operator can re-create every published claim from the seeds, hashes, and prompts on file.

## Determinism

- Random seed: `20260531` everywhere (`numpy.random.default_rng`, sampling, splitting).
- LLM temperature: `0.0`, top_p `1.0`, seed `20260531` where supported.
- Provider-supplied non-determinism (e.g., slight variation across calls) is logged and bounded by the H7 cross-model agreement check.

## Versioning

- Code: git commit hash recorded in every artifact's metadata.
- Dictionary: semver in `domestic_frame_dictionary.json:meta.version`.
- Corpus: dated tarballs with sha256.
- Models: provider-supplied version string captured in every `LLMResponse`.

## Prompts

- All prompts versioned in `03_pipeline/frame_extraction/prompts/v{n}_*.txt`.
- Each LLM call records `prompt_hash` (sha256 of the rendered prompt + model + parameters).

## Logs

- `02_data/raw/retrieval_log.jsonl` — every fetched URL.
- `04_analysis/llm_call_log.jsonl` — every LLM call, with hashes and token counts.
- `tasks/run_logs/<stage>_<YYYYMMDD>.jsonl` — per-stage execution logs.

## Reproduction tiers

| Tier | What we provide | What you do |
|------|------------------|-------------|
| Code | This repo | run as in `pipeline_doc.md` |
| Inputs (small) | Dictionary, prompts, country covariates | same |
| Inputs (large) | URLs + sha256s for the corpus | re-fetch from sources; integrity-check against our sha256 |
| Outputs | Document-level frame counts (parquet) | inspect / replot directly |

## What we explicitly cannot guarantee

- Source-site changes (URLs moved, docs taken down) over time.
- Future LLM provider behavior changes (Anthropic / OpenAI / Qwen may deprecate model versions).
- Recipient-side material availability in CLMV official sites.

Our mitigation is to publish content-hashes for every document in the analyzed corpus so that if a re-fetch finds different content, the divergence is visible.
