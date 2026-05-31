"""Shared HTTP client. Every scraper fetches through `fetch()`.

The client enforces per-host rate limits, retries with exponential backoff,
records every request to `02_data/raw/retrieval_log.jsonl`, and stamps an
identifying User-Agent. Real implementation pending.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


USER_AGENT = (
    "ProjectC-AcademicResearchBot/0.1 "
    "(HKU-CCCW postdoc project on China-ASEAN development discourse; "
    "contact: mengnanxu2333@gmail.com)"
)
DEFAULT_MIN_INTERVAL_S = 2.0
DEFAULT_MAX_RETRIES = 4
RETRIEVAL_LOG = Path("02_data/raw/retrieval_log.jsonl")


@dataclass
class FetchResult:
    url: str
    status: int
    body_bytes: bytes
    sha256: str
    fetched_at: str
    headers: dict[str, str]


def fetch(
    url: str,
    *,
    timeout: float = 30.0,
    min_interval_s: float = DEFAULT_MIN_INTERVAL_S,
    max_retries: int = DEFAULT_MAX_RETRIES,
    expected_content_type: Optional[str] = None,
) -> FetchResult:
    """Single rate-limited fetch with logging. Not yet implemented."""
    raise NotImplementedError("Implement when first scraper is wired up.")


if __name__ == "__main__":
    raise SystemExit("This module is a library, not a script.")
