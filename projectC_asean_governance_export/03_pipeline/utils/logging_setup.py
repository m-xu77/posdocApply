"""Project-wide structured logging.

Sets up a logger that writes JSON lines to a per-stage log file in
`tasks/run_logs/<stage>_<YYYYMMDD>.jsonl`, with console mirror at INFO.
Real implementation pending.
"""
from __future__ import annotations

import logging
from pathlib import Path


def get_logger(stage_name: str, *, log_dir: Path = Path("tasks/run_logs")) -> logging.Logger:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("This module is a library, not a script.")
