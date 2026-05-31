"""CIDCA publications scraper.

Targets:
  - cidca.gov.cn 项目动态 / 政策法规 / 国别合作.
  - China International Development Cooperation white papers (where mirrored).

Scaffold only.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path


def scrape(*, since: date, until: date, out_dir: Path) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
