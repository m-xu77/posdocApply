"""Stage 4 — extract frame mentions across the outward corpus.

For each (document, model in ensemble):
  1. Chunk text into <=2000-token segments with 200-token overlap.
  2. Send chunk + dictionary labels + signature phrases to the LLM with a
     standard extraction prompt (versioned in ./prompts/v{n}.txt).
  3. Parse LLM JSON output: list of {frame_id, span, confidence}.
  4. Deduplicate overlapping spans within document, prefer higher confidence.
  5. Sum to document-level counts; compute density per 1000 tokens.
  6. Write rows to `04_analysis/frame_extraction_results.parquet`.

Scaffold only.
"""
from __future__ import annotations

from pathlib import Path


def extract(*, corpus_path: Path, dict_path: Path, out_path: Path, models: tuple[str, ...]) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
