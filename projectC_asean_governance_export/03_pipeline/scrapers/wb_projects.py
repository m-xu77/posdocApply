"""World Bank project-document scraper (CLMV).

Targets:
  - projects.worldbank.org documents API filtered to KHM/LAO/MMR/VNM.
  - PAD / ICR / press releases retrieved as PDF.

Scaffold only.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path


def scrape(*, since: date, until: date, out_dir: Path) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
