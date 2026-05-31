"""Raw -> cleaned corpus pipeline.

For each fetched document:
  1. Detect format (HTML / PDF / DOCX).
  2. Extract main-content text (BeautifulSoup main-content selectors per source;
     pymupdf for PDF; OCR fallback via PaddleOCR/Tesseract).
  3. Detect language; translate non-zh/non-en docs via DeepL.
  4. Extract metadata (publisher, agency, date, target country, doc type).
  5. Deduplicate via SimHash (Hamming distance <= 3 -> collapse).
  6. Write to `02_data/processed/asean_corpus_clean.parquet`.

Scaffold only.
"""
from __future__ import annotations

from pathlib import Path


def clean(*, raw_root: Path, out_path: Path) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
