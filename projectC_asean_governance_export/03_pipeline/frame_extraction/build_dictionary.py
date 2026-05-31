"""Stage 1 — build domestic frame dictionary from output_v3.action_events.

Inputs:
  - `output_v3/research_enhanced.db` containing the `action_events` table.

Procedure (per `00_design/04_methodology.md` Stage 1):
  1. Group action_events into (actor_type x action_type x entry_mechanism) cells.
  2. Sample up to 80 action_desc strings per non-empty cell, stratified by year.
  3. For each cell, call the LLM (via utils.llm_runner) to produce:
       - frame label (zh + en)
       - diagnostic + prognostic articulation
       - 8-15 signature phrases (zh)
       - 3-5 contrast phrases (zh)
  4. Mark cells as governance / infrastructure frames per the rule in
     `00_design/03_hypotheses.md` H3.
  5. Compute pairwise embedding cosine for merge-candidate flagging.
  6. Validate against the dictionary JSON schema before writing.

Output:
  - `02_data/domestic_dict/domestic_frame_dictionary.json` v1.0

Scaffold only.
"""
from __future__ import annotations

from pathlib import Path


def build(
    *,
    db_path: Path,
    out_path: Path,
    max_samples_per_cell: int = 80,
    min_events_for_cell: int = 5,
) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Wire to CLI when implemented.")
