# 02 · Data

This folder is the project's data layer. Two operating principles:

1. **Nothing here is in git** by default except the directory README, the codebook scaffold, and metadata templates. Raw + processed corpora live locally; large derivatives sit on storage outside git. See `.gitignore`.
2. **Every dataset is traceable**: every file has a sibling `*.meta.json` recording source, date pulled, checksum, transformation chain back to a raw object.

## Layout

```
02_data/
├── raw/                    # Untouched fetched documents (HTML/PDF/DOCX) by source
│   ├── mfa/
│   ├── mofcom/
│   ├── cidca/
│   ├── gdi/
│   ├── treaties/
│   ├── wb/
│   ├── adb/
│   ├── clmv_recipient/
│   └── retrieval_log.jsonl     # one line per fetched URL: ts, url, status, sha256
├── processed/              # Cleaned text + extracted metadata
│   ├── asean_corpus_clean.parquet
│   ├── comparison_corpus_clean.parquet
│   └── per_source/
├── domestic_dict/          # Frame dictionary derived from output_v3 action_events
│   ├── domestic_frame_dictionary.json   # canonical artifact
│   ├── domestic_frame_dictionary.schema.json
│   ├── build_log.jsonl
│   └── manual_review_notes.md
├── metadata/               # CSV templates and consolidated metadata
│   ├── doc_metadata_template.csv
│   ├── doc_metadata.parquet            # produced by preprocessing
│   └── country_year_covariates.csv     # AidData + V-Dem + WB joins
└── annotation/             # Human-coded validation
    ├── stratified_sample_400.csv       # the 400-paragraph gold set
    ├── codebook_for_annotators.md
    ├── coder_A.csv
    ├── coder_B.csv
    ├── adjudicated.csv
    └── iaa_report.md
```

## Source-of-truth statement

| Asset | Source of truth |
|-------|------------------|
| Domestic frames | `output_v3/research_enhanced.db` → `action_events` table |
| Outward corpus | Fetched URLs in `retrieval_log.jsonl` (re-fetchable) |
| Country covariates | AidData v3, V-Dem v15 (versions pinned in metadata) |
| Frame dictionary | `domestic_dict/domestic_frame_dictionary.json` (versioned) |

## Versioning

- Frame dictionary: semver. `v0.x` while pre-pilot; `v1.0` when first H8 validation passes.
- Corpus snapshots: dated tarballs (`asean_corpus_YYYYMMDD.tar.zst`) kept on local storage, hashed in this README's snapshot table.

## Snapshot table

| Date | Asset | SHA256 (prefix) | Notes |
|------|-------|------------------|-------|
| — | — | — | none yet |
