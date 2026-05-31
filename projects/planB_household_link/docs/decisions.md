# Plan B — Decision Log

A versioned log of design choices and the reasoning. Every entry includes date, the decision, the reason, and (where relevant) the alternative considered.

---

## 2026-05-31 — Project bootstrap

### D-001  Folder structure: numbered-stage pipeline in `code/`

- **Decision**: One Python script per stage, prefixed `NN_`. No notebooks until the inferential phase.
- **Reason**: deterministic CLI execution; trivial to run end-to-end; trivial to drop into CI; trivial for collaborators to reproduce.
- **Alternative considered**: Jupyter notebooks throughout. Rejected — notebooks are great for exploration, terrible for the production pipeline phase.

### D-002  Long-format event-province table with weight 1/n

- **Decision**: Multi-province events (e.g., 上海、云南、贵州) explode into N rows with weight $1/n$ each.
- **Reason**: Preserves the multi-province signal (East-West pairing is often coded this way); preserves total event count under summation; is the standard in spatial aggregation.
- **Alternative considered**: (i) Discard multi-province events — loses ~3,250 of 9,855 geo-resolved events. (ii) Assign full weight to each — double-counts. Both rejected.
- **Robustness commitment**: equal-weight ($w=1$ per province) and $w = 1/\sqrt{n}$ are part of the robustness battery (see `analysis_plan.md` §5).

### D-003  Central/local cut from `actor_type`, not `actor_gov_level`

- **Decision**: Derive `central_share` and `local_share` from `actor_type ∈ {中央政府, 地方政府}`.
- **Reason**: `actor_gov_level` is empty across all 25,358 rows — a confirmed data-quality issue in the upstream LLM extraction.
- **Alternative considered**: Re-extract `actor_gov_level` from the source text. Deferred — the `actor_type` cut is sufficient for the descriptive phase and survives as the primary specification.
- **Follow-up**: Open a ticket against `src_v3/02_extract_actions.py` to populate `actor_gov_level` from `actor` string parsing (e.g., 省、市 suffix detection).

### D-004  Geographic coverage: province-only in Phase 0

- **Decision**: Phase 0 builds the province × year panel. County-level standardization is deferred to Phase 1.
- **Reason**: The DB's `region` column has zero entries containing 县 or 市 substrings — county-level signal must be reconstructed from the section path / report unit, which is non-trivial.
- **Implication**: CFPS county-CATE merge cannot happen until Phase 1 county standardization is built. The PS-ready descriptive figures and the second-stage *outline* can proceed at province level.

### D-005  NBS 4-region partition as the canonical "region group"

- **Decision**: 东北 / 东部 / 中部 / 西部 per NBS standard.
- **Reason**: Matches the East-West poverty-pairing logic and is the standard adopted in *China Quarterly* / *CER* / *WD* papers on Chinese regional inequality.
- **Alternative considered**: NBS 6-region split (further dividing East/Central). Rejected — adds dimensionality without illuminating poverty-alleviation organization.

### D-006  Unit-normalization for `value_num` is deferred

- **Decision**: Stage 02's `total_value_num` is **not** unit-normalized; it sums raw numeric values regardless of unit. The field is included for descriptive use only and is **explicitly excluded** from headline indicators until Stage 04 normalizes 元 / 万元 / 亿元 / 万 → 元.
- **Reason**: Naive summation conflates 元 and 万元 — a single 1亿元 event would dwarf a hundred 100万元 events, biasing the cross-province ranking.
- **Follow-up**: Stage 04 will read `value_unit` and apply the canonical multiplier table.

### D-007  Random seed: 20260531

- **Decision**: All randomized operations use `SEED = 20260531`.
- **Reason**: Project-wide reproducibility. The date encodes the project birth.

### D-008  No external pkgs without an entry here

- **Decision**: Every external Python dependency added to the project (beyond pandas, numpy, matplotlib, pyarrow, sqlite3) must be logged here with a justification.
- **Reason**: Maintains a reproducible environment; prevents drift.
