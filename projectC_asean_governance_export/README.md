# Project C — Does China Export Its Poverty Governance Model?

**An LLM-Based Cross-Border Frame Analysis of GDI / BRI / South-South Cooperation Documents toward ASEAN, 2013–2026**

> Working title for the journal article submission:
> *"Frames in Transit: Tracing the Cross-Border Travel of China's Poverty-Governance Repertoire to ASEAN, 2013–2026"*

**Author**: Mengnan Xu (徐梦楠)
**Institutional home (target)**: Centre on Contemporary China and the World (CCCW), HKU
**CCCW track alignment**: (1) ASEAN + (3) AI methods for social science
**Status**: Design phase (initialized 2026-05-31)
**Repository version**: v0.1.0 (scaffolding)

---

## 1. Why this project matters

International-development scholarship has spent a decade asking whether China is exporting an "alternative governance model" via the Belt and Road Initiative (BRI), the Global Development Initiative (GDI), and South-South Cooperation. The literature is split between two stylized claims:

- **"Infrastructure-only"** (e.g., Brautigam 2009; Hameiri & Jones 2018): China exports financing and hardware, not institutions.
- **"Beijing Consensus / governance export"** (Ramo 2004; Halper 2010): China is propagating a distinctive political-economic model.

Both camps argue almost exclusively from *project portfolios* (what was built, where, with what money). What is missing is a **frame-level**, **cross-border**, **actor-disaggregated**, **time-resolved** test: does the *language* through which the Chinese state describes its development engagement abroad systematically reproduce the *language* it uses for domestic poverty governance? If so, by which bureaucratic actor, toward which ASEAN country, in which years?

This project answers that question by treating Chinese domestic poverty-governance discourse (2009–2022) as a **frame dictionary** built from a 25,358-event organizational-ecology database, and applying LLM-based frame extraction to a 3,000–8,000-document corpus of China's outward development texts toward Cambodia, Laos, Myanmar, and Vietnam. The result is the first systematic, reproducible, agency-labeled measurement of the **governance-to-infrastructure ratio** in China's outward developmental discourse.

## 2. What is new

| Dimension | Prior literature | This project |
|---|---|---|
| Unit of analysis | Project / loan / country-year aggregates | Document × bureaucratic actor × frame |
| Frame source | Researcher-imposed typology | Empirically grounded in 25,358 domestic action events |
| Bureaucratic resolution | Aggregate "China" | MFA / MOFCOM / CIDCA / SOEs disaggregated |
| Temporal resolution | Pre/post BRI binaries | Continuous 2013–2026 with 2013/2018/2021 breakpoints |
| Comparison | Single-donor narrative | China vs. World Bank / ADB in same four ASEAN states |
| Reproducibility | Closed coding | Open frame dictionary, open prompts, open pipeline |

## 3. Theoretical hooks

1. **Cross-border frame travel** (Snow, Benford 2000; Béland & Cox 2013) — how do *domestic* policy frames migrate to *international* discourse?
2. **Institutional diffusion vs. material transfer** (Weyland 2009; Heilmann & Shih 2013) — is China's outward engagement diffusing institutions or only goods?
3. **Bureaucratic politics in Chinese foreign policy** (Jakobson & Knox 2010; Lampton 2014) — which agency frames the outward narrative, and do their frames diverge?
4. **South-South cooperation as a discursive field** (Mawdsley 2012; Gray & Gills 2016) — does China occupy a distinct rhetorical position vs. OECD-DAC donors?

See `00_design/02_theoretical_framework.md` for the full chain.

## 4. Repository layout

```
projectC_asean_governance_export/
├── README.md                      # this file
├── 00_design/                     # research questions, theory, hypotheses, methods, ethics
├── 01_literature/                 # five lit-review pillars + bibtex
├── 02_data/                       # raw, processed, frame dictionary, metadata, annotation
├── 03_pipeline/                   # scrapers, preprocessing, frame extraction, validation, utils
├── 04_analysis/                   # notebooks per analytic question
├── 05_output/                     # figures, tables, paper drafts, slides
├── 06_docs/                       # codebook, pipeline docs, reproducibility statement
└── tasks/                         # dated progress logs
```

Every numbered directory has its own `README.md` documenting purpose and contents.

## 5. Five things this repo will produce

1. **`domestic_frame_dictionary.json`** — 17 organization × 11 action × 7 entry-mechanism frame patterns with semantic fingerprints and validated keyword/phrase signatures.
2. **`asean_corpus/`** — 3,000–8,000 fully cited, deduplicated, OCR'd documents with full metadata (publisher, date, target country, document type, language).
3. **`frame_extraction_results.parquet`** — document-level frame counts, densities, governance-to-infrastructure ratios, with model-version columns for sensitivity analysis.
4. **Journal article** — ≥ 9,000-word working paper, target outlets *International Affairs*, *China Quarterly*, *Journal of Contemporary China*, *Third World Quarterly*.
5. **Open GitHub repo + CCCW workshop deck** — full pipeline, prompts, fixed seeds, replication notebooks.

## 6. Connection to existing assets

- **`src_v3/`** — the LLM-driven pipeline that produced the domestic 25,358-event database. Frame-dictionary stage reuses that infrastructure (`03_pipeline/frame_extraction/` extends `src_v3/05_extract_actions.py`).
- **`output_v3/`** — domestic action_events / organizations / toc_entries tables. Source of truth for the frame dictionary.
- **`reasearch_plans/plan_C_asean_export.md`** — the strategic plan; this repo is its execution.

## 7. Reproducibility commitments

- Every model call goes through a deterministic wrapper (`03_pipeline/utils/llm_runner.py`) that records model id, prompt hash, temperature, seed.
- Frame extraction uses ≥ 2 LLM families (Claude Opus 4.7 + GPT-5 + Qwen3) in ensemble; agreement matrices published.
- Inter-annotator agreement (Cohen's κ ≥ 0.7) on a stratified 400-document validation sample.
- All scraped URLs, retrieval dates, and HTTP response headers archived in `02_data/raw/retrieval_log.jsonl`.

## 8. How to read this repo

If you have **15 minutes**: read this README + `00_design/01_research_questions.md`.
If you have **1 hour**: add `00_design/02_theoretical_framework.md` + `00_design/04_methodology.md`.
If you are **replicating**: start at `06_docs/reproducibility.md`.

## 9. License and ethics

Code: MIT. Curated corpus: CC BY 4.0 (only documents that are already published on official PRC / WB / ADB websites are redistributed; otherwise stable URLs are provided). See `00_design/05_research_ethics.md`.

---

*Last updated: 2026-05-31*
