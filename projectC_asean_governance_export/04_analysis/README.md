# 04 · Analysis

Notebooks live in `notebooks/`. Each maps to a research question and a hypothesis from `00_design/03_hypotheses.md`. Convention: notebook number = analysis order, not file-system order.

| # | Notebook | Tests | Inputs | Outputs |
|---|----------|-------|--------|---------|
| 00 | `00_power_simulation.ipynb` | none (planning) | dictionary, pilot 200 docs | min-n estimates per (agency × year) cell |
| 01 | `01_descriptive_overview.ipynb` | RQ1 setup | `asean_corpus_clean.parquet` | corpus-size tables, time-coverage plot, doc-type breakdown |
| 02 | `02_frame_density.ipynb` | H1 | extraction results | per-doc / per-corpus density, bootstrap CIs, transplantation share |
| 03 | `03_bureaucratic_comparison.ipynb` | H2, H3 | extraction + agency labels | agency × frame heatmap, cosine matrix, GIR boxplots |
| 04 | `04_country_comparison.ipynb` | H4, H5 | extraction + covariates | country × frame heatmap, panel OLS |
| 05 | `05_temporal_breakpoints.ipynb` | H6 | monthly aggregates | Bai-Perron + ITS regressions |
| 06 | `06_donor_comparison.ipynb` | RQ1 placebo | China vs WB/ADB extraction | matched-sample comparison, frame contrasts |
| 07 | `07_robustness_model_sensitivity.ipynb` | H7 | three models' outputs | pairwise Spearman ρ |
| 08 | `08_robustness_prompt_sensitivity.ipynb` | meta | three prompts on 500-doc subset | sensitivity bounds |
| 09 | `09_robustness_dictionary_coverage.ipynb` | H8 | gold annotations | recall / precision |

## Output discipline

- Every notebook saves figures to `../05_output/figures/` and tables to `../05_output/tables/` with stable filenames keyed by hypothesis (`fig_h3_gir_boxplot.pdf`).
- `papermill` parameterizes notebooks for re-execution across model variants.
- Notebook outputs are cleared before commit (`nbstripout` recommended).

## Reading order for an external reader

If reviewing the paper alongside the repo:

1. README at root + `00_design/01_research_questions.md` + `01_descriptive_overview.ipynb`.
2. Then for each headline claim, jump to its notebook (H1 → `02_`, H3 → `03_`, etc.).
3. Robustness in 07–09 backstops every claim.

## Folder roles

`descriptive/`, `bureaucratic_comparison/`, `temporal/`, `comparative/` hold helper modules (functions used by multiple notebooks) and intermediate parquet outputs that are not the final results.
