"""Inter-annotator agreement and dictionary coverage metrics (Stage 5).

Inputs:
  - `02_data/annotation/coder_A.csv`
  - `02_data/annotation/coder_B.csv`
  - `02_data/annotation/adjudicated.csv`
  - LLM-extracted frames over the same 400 paragraphs.

Outputs:
  - `02_data/annotation/iaa_report.md` with:
      - Cohen's kappa (frame presence)
      - Krippendorff's alpha (frame identity)
      - Confusion matrix per frame
      - Dictionary recall + precision against adjudicated gold

Scaffold only.
"""
from __future__ import annotations

from pathlib import Path


def compute(
    *,
    coder_a: Path,
    coder_b: Path,
    adjudicated: Path,
    llm_outputs: Path,
    report_path: Path,
) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
