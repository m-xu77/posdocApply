"""MOFCOM cooperation-agreement scraper.

Targets:
  - mofcom.gov.cn 双边经贸合作 / CLMV country pages.
  - Bilateral commercial-cooperation press releases.

Scaffold only.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path


def scrape(*, since: date, until: date, out_dir: Path) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
