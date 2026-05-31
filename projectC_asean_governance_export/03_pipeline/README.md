# 03 · Pipeline

End-to-end code. Each subfolder is a stage; each module is importable and has a `__main__` entrypoint so it can also be run directly.

| Folder | Role | Stage in `04_methodology.md` |
|--------|------|------------------------------|
| `scrapers/` | Fetch raw documents from official sources | Stage 2 |
| `preprocessing/` | OCR, language detection, metadata extraction, dedup | Stage 3 |
| `frame_extraction/` | Build dictionary; extract frames from outward corpus | Stages 1 + 4 |
| `validation/` | Inter-annotator metrics, recall/precision against gold | Stage 5 |
| `utils/` | Shared helpers: HTTP client, LLM runner, logging, hashing | All |

## Design rules

1. **Pure functions over stateful classes** where possible.
2. **Every external call is logged** via `utils/llm_runner.py` or `utils/http_client.py` — never instantiate `requests.get` or `anthropic.Client()` directly in stage code.
3. **Determinism**: random seeds and model temperature are read from a single `config.toml` at the repo root (added when first stage is implemented).
4. **Idempotence**: every stage is rerunnable — output keyed by content hash of inputs + code version + prompt hash.
5. **Errors are loud**: stages do not swallow exceptions on data anomalies; they raise and write a debug record.

## Status

| Stage | File | Status | Owner |
|-------|------|--------|-------|
| Frame-dictionary builder | `frame_extraction/build_dictionary.py` | scaffold | MX |
| Frame extractor | `frame_extraction/extract.py` | scaffold | MX |
| MFA scraper | `scrapers/mfa_readouts.py` | scaffold | MX |
| MOFCOM scraper | `scrapers/mofcom_agreements.py` | scaffold | MX |
| CIDCA scraper | `scrapers/cidca_pubs.py` | scaffold | MX |
| GDI scraper | `scrapers/gdi_materials.py` | scaffold | MX |
| WB scraper | `scrapers/wb_projects.py` | scaffold | MX |
| ADB scraper | `scrapers/adb_projects.py` | scaffold | MX |
| Preprocessing | `preprocessing/clean.py` | scaffold | MX |
| LLM runner | `utils/llm_runner.py` | scaffold | MX |
| HTTP client | `utils/http_client.py` | scaffold | MX |
| Validation | `validation/iaa.py` | scaffold | MX |

## How to run

(Once implemented; currently scaffolds raise `NotImplementedError`.)

```bash
# Stage 1: build dictionary from domestic db
uv run python -m 03_pipeline.frame_extraction.build_dictionary \
    --db ../../output_v3/research_enhanced.db \
    --out 02_data/domestic_dict/domestic_frame_dictionary.json

# Stage 2: fetch MFA readouts
uv run python -m 03_pipeline.scrapers.mfa_readouts \
    --since 2013-01-01 --until 2026-04-30 --out 02_data/raw/mfa

# Stage 4: extract frames over the cleaned outward corpus
uv run python -m 03_pipeline.frame_extraction.extract \
    --corpus 02_data/processed/asean_corpus_clean.parquet \
    --dict 02_data/domestic_dict/domestic_frame_dictionary.json \
    --out 04_analysis/frame_extraction_results.parquet
```
