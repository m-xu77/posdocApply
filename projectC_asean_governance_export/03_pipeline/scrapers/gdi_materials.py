"""GDI Friends Group / training-materials scraper.

Targets:
  - GDI official portals where available.
  - UN ECOSOC archives that mirror GDI submissions.

Scaffold only.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path


def scrape(*, since: date, until: date, out_dir: Path) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
