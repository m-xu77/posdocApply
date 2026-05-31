# 04 · Methodology

**Document status**: v0.1 — methods locked for design phase, awaiting pilot data
**Last updated**: 2026-05-31

> This document gives the full chain from raw documents to publishable claims. Each stage points to the code module that will implement it.

---

## 1. Methodological overview

```
[ Domestic action_events (n=25,358) ]
         │
         ▼
[ Stage 1: Frame dictionary construction ]  ──▶  domestic_frame_dictionary.json
         │
         ▼
[ Stage 2: Outward corpus collection ]  ──▶  asean_corpus/ (3k–8k docs)
         │
         ▼
[ Stage 3: Document preprocessing ]  ──▶  asean_corpus_clean.parquet
         │
         ▼
[ Stage 4: Frame extraction (ensemble) ]  ──▶  frame_extraction_results.parquet
         │                                       (one row per document × model)
         ▼
[ Stage 5: Validation (κ, recall, precision) ]  ──▶  validation_report.md
         │
         ▼
[ Stage 6: Analyses for H1–H6 ]  ──▶  notebooks/04_analysis/*.ipynb
         │
         ▼
[ Stage 7: Robustness (H7, H8, sensitivity) ]  ──▶  robustness_report.md
         │
         ▼
[ Stage 8: Manuscript ]  ──▶  05_output/paper_drafts/working_paper_v1.md
```

## 2. Stage-by-stage detail

### Stage 1 — Frame dictionary construction

**Source**: `output_v3/research_enhanced.db` → `action_events` table (n = 25,358; 2009–2022).

**Procedure**:

1. **Group** action_events by the 17 actor_type × 11 action_type × 7 entry_mechanism combinations (max 1,309 cells; expect ~300 populated).
2. **Sample** up to 80 `action_desc` strings per non-empty cell (stratified by year to avoid era bias).
3. **LLM frame-summarization pass** (Claude Opus 4.7 as primary, GPT-5 as cross-check): for each cell, produce
   - a 1–2 sentence *frame label* (Snow–Benford diagnostic+prognostic),
   - a list of 8–15 *signature phrases* (Chinese, with English glosses),
   - a list of 3–5 *contrast phrases* (what this frame is NOT — disambiguates against neighboring cells).
4. **Manual review**: PI annotates 50 randomly selected cells; corrects labels where the LLM has over-generalized or merged distinct frames.
5. **Frame-clustering check**: embed each cell's signature phrases using a multilingual sentence encoder (e.g., `bge-m3`), compute pairwise cosine; cells with cosine ≥ 0.92 are flagged for merge review.
6. **Output**: `domestic_frame_dictionary.json` — JSON schema in `06_docs/codebook.md`.

**Code**: `03_pipeline/frame_extraction/build_dictionary.py`.

### Stage 2 — Outward corpus collection

**Five core sources** (in priority order):

| # | Source | URL pattern | Expected docs | Crawler module |
|---|--------|-------------|---------------|----------------|
| 1 | MFA readouts on CLMV | `fmprc.gov.cn` — 国家与地区 → CLMV pages, 领导人活动 | 600–1,200 | `scrapers/mfa_readouts.py` |
| 2 | MOFCOM cooperation agreements | `mofcom.gov.cn` — 双边经贸合作; CLMV country pages | 400–900 | `scrapers/mofcom_agreements.py` |
| 3 | CIDCA materials | `cidca.gov.cn` — 项目动态, 政策法规, 国别合作 | 300–700 | `scrapers/cidca_pubs.py` |
| 4 | GDI Friends Group + training materials | `gdi.gov.cn` (where available); UN ECOSOC archives | 100–300 | `scrapers/gdi_materials.py` |
| 5 | Bilateral agreements (treaty texts) | China treaty database; CLMV foreign-ministry treaty pages | 200–500 | `scrapers/bilateral_treaties.py` |

**Comparison corpus**:

| # | Source | Purpose | Crawler module |
|---|--------|---------|----------------|
| 6 | World Bank project docs in CLMV | DAC-discourse counterfactual | `scrapers/wb_projects.py` |
| 7 | ADB project docs in CLMV | DAC-discourse counterfactual | `scrapers/adb_projects.py` |
| 8 | CLMV foreign-ministry statements on China | Recipient-side mirror (descriptive use only) | `scrapers/clmv_recipient.py` |

**Crawl discipline**:

- All requests through a shared session in `utils/http_client.py` with `User-Agent` identifying the research project and contact email.
- Rate limit: ≤ 1 request / 2 s per host, exponential backoff on 4xx/5xx.
- Every fetched URL appended to `02_data/raw/retrieval_log.jsonl` with timestamp, HTTP status, content hash.
- No JavaScript-rendered scraping until rendered-content needs are confirmed; default to plain HTTP.
- No login-gated or paywalled content.

### Stage 3 — Preprocessing

**Pipeline** (`03_pipeline/preprocessing/`):

1. **Format detection**: HTML / PDF / DOCX.
2. **Text extraction**: HTML → BeautifulSoup main-content extraction (custom selectors per source); PDF → `pymupdf` then OCR fallback (`paddleocr` for Chinese, `tesseract` for English/Vietnamese).
3. **Language ID + translation**: `langdetect`; non-Chinese/English docs translated via DeepL API; both original and translation retained.
4. **Metadata extraction**: publisher (from URL + page chrome), date (regex + LLM fallback), target country (LLM-classified from title + first paragraph), document type (one of: press readout / agreement / training material / treaty / policy paper / project doc).
5. **Deduplication**: SimHash on normalized text; near-duplicates (Hamming distance ≤ 3) collapsed; one canonical kept.
6. **Output**: `asean_corpus_clean.parquet` (one row per document) with columns `doc_id, url, fetched_at, publisher, agency, target_country, pub_date, doc_type, lang, raw_text, en_text, word_count, sha256`.

### Stage 4 — Frame extraction (ensemble)

**Per-document pass** (`03_pipeline/frame_extraction/extract.py`):

For each document × each model in `{claude-opus-4-7, gpt-5, qwen3}`:

1. Chunk text into ≤ 2,000-token segments with 200-token overlap.
2. For each chunk, send a prompt that contains: (a) the frame dictionary entries (just labels + signature phrases), (b) the chunk text, (c) instruction to extract frame mentions with their (start, end) spans and a confidence score.
3. Deduplicate spans within document; sum to document-level counts.
4. Compute frame density = (matched tokens / total tokens) × 1,000.

**Prompt versioning**: each prompt stored in `03_pipeline/frame_extraction/prompts/v{n}.txt`; hash recorded with each model output.

**Output**: `frame_extraction_results.parquet` with columns `doc_id, model_id, prompt_hash, frame_id, count, density, mean_confidence`.

### Stage 5 — Validation

**Three validation layers**:

1. **Dictionary coverage** (H8): stratified random sample of 400 outward-corpus paragraphs across (agency × country × year). Two coders (PI + RA) annotate each as frame-bearing (and which frame) vs. not. Compute recall and precision of the dictionary; inter-annotator Cohen's κ.
2. **Inter-coder agreement** target: κ ≥ 0.70 on frame-presence; ≥ 0.60 on frame-identity.
3. **LLM cross-model agreement** (H7): pairwise Spearman ρ on document-level frame counts.

**Adjudication procedure** for coder disagreements: third reviewer (CCCW research associate / collaborator) decides; protocol in `06_docs/adjudication_protocol.md`.

### Stage 6 — Core analyses

Each in its own notebook in `04_analysis/notebooks/`:

| # | Notebook | RQ / H | Outputs |
|---|----------|--------|---------|
| 1 | `01_descriptive_overview.ipynb` | RQ1 / H1 | Corpus size table, time coverage plot, document-type breakdown |
| 2 | `02_frame_density.ipynb` | H1 | Frame-density bootstrap CIs, transplantation share |
| 3 | `03_bureaucratic_comparison.ipynb` | H2, H3 | Agency × frame heatmap, cosine matrix, GIR boxplots |
| 4 | `04_country_comparison.ipynb` | H4, H5 | Country × frame heatmap, panel regression |
| 5 | `05_temporal_breakpoints.ipynb` | H6 | Monthly time series, Bai–Perron, ITS |
| 6 | `06_donor_comparison.ipynb` | RQ1 placebo | China vs WB/ADB frame profiles |

### Stage 7 — Robustness

- **Model sensitivity** (H7): all analyses re-run on each LLM's output; report median + bounds across models.
- **Prompt sensitivity**: 3 alternative prompt phrasings on a 500-doc subset; report Spearman ρ.
- **Drop high-frequency words**: re-run with top-100 generic developmental phrases removed.
- **Genre fixed-effects**: re-run H2/H3 within each `doc_type`.
- **Time-window trimming**: re-run H6 with 2020–21 (COVID) excluded.

### Stage 8 — Manuscript

Target structure (≥ 9,000 words):

1. Introduction (1,200 w)
2. Theoretical framework + hypotheses (2,000 w)
3. Data and methods (1,500 w; technical appendix linked)
4. Results in four sections corresponding to H1, H2–H3, H4–H5, H6 (3,000 w)
5. Discussion + alternative explanations (1,000 w)
6. Conclusion + policy implications (500 w)
7. Appendix: dictionary, prompts, robustness tables, replication note

## 3. Computational environment

- Python 3.11; package manager `uv` (lockfile in repo root).
- Heavy lifting on a CCCW shared GPU node when available; otherwise OpenRouter / direct API for LLM calls.
- All notebooks committed with cleared outputs; `papermill` for parameter sweeps.
- Random seeds fixed: `numpy.random.default_rng(20260531)`, model `temperature=0`, `top_p=1`.

## 4. Statistical-power note

With ~5,000 outward documents, n per (agency × year) cell averages ~30. Power simulation (in `04_analysis/notebooks/00_power_simulation.ipynb` — to be written first thing post-pilot) will confirm whether H3 in particular has ≥ 0.8 power at expected effect sizes.

## 5. What is intentionally out of scope

- Causal claims about adoption outcomes in CLMV.
- Sentiment / valence analysis (left for downstream work).
- Within-document temporal-ordering effects (frames extracted as bag-of-frames, not as narrative arcs).
- Multimodal analysis of images / video in source materials.

## 6. Cross-references

- Codebook: `06_docs/codebook.md`
- Adjudication protocol: `06_docs/adjudication_protocol.md`
- Reproducibility statement: `06_docs/reproducibility.md`
- Pre-registration: this document + `03_hypotheses.md`
