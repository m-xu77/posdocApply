"""MFA readout scraper.

Targets:
  - fmprc.gov.cn — country pages for Cambodia/Laos/Myanmar/Vietnam.
  - "Leaders' Activities" sub-pages where relevant.
  - "China-ASEAN Relations" thematic page.

Discipline:
  - All requests go through `03_pipeline.utils.http_client.fetch`.
  - Output layout: `02_data/raw/mfa/<country>/<YYYY>/<sha256>.html`.
  - Metadata appended to `02_data/raw/mfa/index.jsonl`.

Scaffold only. Not yet implemented.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path


def scrape(
    *,
    since: date,
    until: date,
    out_dir: Path,
    countries: tuple[str, ...] = ("KH", "LA", "MM", "VN"),
) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
