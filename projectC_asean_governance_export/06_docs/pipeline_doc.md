# Pipeline Operator Manual

How a fresh operator (RA, collaborator, future-PI) reproduces the project end to end.

---

## 0. Prerequisites

- Python 3.11+, `uv` installed.
- API keys for Anthropic, OpenAI, Qwen (optional: OpenRouter as multiplexer).
- DeepL API key for non-zh/en translation.
- A clone of `opendata/` with `output_v3/research_enhanced.db` populated.
- 50 GB free disk for raw + processed corpora.

## 1. Environment

```bash
cd posdocApplyResearch/projectC_asean_governance_export
uv venv
uv pip install -e .
cp .env.example .env  # fill in API keys
```

## 2. Build the domestic frame dictionary (Stage 1)

```bash
uv run python -m 03_pipeline.frame_extraction.build_dictionary \
  --db ../../output_v3/research_enhanced.db \
  --out 02_data/domestic_dict/domestic_frame_dictionary.json
```

Expected runtime: 2–4 h (LLM-bound). Output validated against the JSON schema.

## 3. Manual dictionary review

PI annotates 50 randomly chosen frames in `manual_review_notes.md`. Re-run merges and revisions.

## 4. Pilot scrape (Stage 2, pilot subset)

```bash
for src in mfa mofcom cidca; do
  uv run python -m 03_pipeline.scrapers.${src}_$( [[ $src == mfa ]] && echo readouts || ([[ $src == mofcom ]] && echo agreements || echo pubs) ) \
    --since 2020-01-01 --until 2021-12-31 --out 02_data/raw/$src
done
```

This produces the 1,000-doc pilot referenced in `plan_C_asean_export.md`.

## 5. Preprocessing (Stage 3)

```bash
uv run python -m 03_pipeline.preprocessing.clean \
  --raw-root 02_data/raw \
  --out 02_data/processed/asean_corpus_clean.parquet
```

## 6. Frame extraction (Stage 4)

```bash
uv run python -m 03_pipeline.frame_extraction.extract \
  --corpus 02_data/processed/asean_corpus_clean.parquet \
  --dict 02_data/domestic_dict/domestic_frame_dictionary.json \
  --out 04_analysis/frame_extraction_results.parquet \
  --models claude-opus-4-7 gpt-5 qwen3-72b
```

Expected runtime on pilot (1k docs × 3 models): 6–12 h.

## 7. Validation (Stage 5)

1. Sample 400 paragraphs (stratified): `04_analysis/notebooks/09_robustness_dictionary_coverage.ipynb` Cell 1.
2. Two coders annotate using the codebook.
3. Adjudication.
4. Compute IAA + recall/precision:
   ```bash
   uv run python -m 03_pipeline.validation.iaa \
     --coder-a 02_data/annotation/coder_A.csv \
     --coder-b 02_data/annotation/coder_B.csv \
     --adjudicated 02_data/annotation/adjudicated.csv \
     --llm-outputs 04_analysis/frame_extraction_results.parquet \
     --report 02_data/annotation/iaa_report.md
   ```

## 8. Analyses (Stage 6)

Run notebooks 01 → 06 in order. Each writes its figures and tables to `05_output/`.

## 9. Robustness (Stage 7)

Notebooks 07 → 09. Spotlight any results that move materially across LLM choice or prompt phrasing.

## 10. Manuscript (Stage 8)

Draft built incrementally in `05_output/paper_drafts/`. Each headline result has exactly one figure and one table; the appendix carries the rest.
