# Progress Log — projectA · 2026-05-31

**Session goal**: write the Plan-A academic article from the existing `output_v3` data, at submission-grade quality.

## What was produced
- `paper_drafts/working_paper_v1.md` — **8,300-word working paper** ("Who Implements Poverty Alleviation? An Organizational Ecology of China's Anti-Poverty Governance, 2009–2022").
  - Body (Abstract → Conclusion): 7,832 words.
  - Seven tables embedded; eight figure references to `output_v3/figures/`.
  - Twenty references covering organizational ecology, Chinese politics, comparative development governance.
- `paper_drafts/supplementary_appendix.md` — full SQL recipes + LLM provenance + robustness details + replication note.
- `analysis_notes/headline_statistics.md` — single-source-of-truth statistics file from which the paper's numbers were drawn.
- Folder scaffold: `paper_drafts/ tables/ analysis_notes/ refs/ figures_src` (symlink to `output_v3/figures`).

## Empirically verified before claiming done (per memory rule)
1. **Governance-frame bundle 59.8%**: `15,175 / 25,358 = 59.85%` — confirmed.
2. **Infrastructure-frame bundle 20.8%**: `5,262 / 25,358 = 20.75%` — confirmed.
3. **Hybrid governance share 48.1%**: `12,199 / 25,358 = 48.11%` of all events — confirmed.
4. **SOE > local in P2 (2013–2019)**: SOE 2,622 vs local 1,655 — confirmed.
5. **Word count ≥ 8,000**: 8,300 total — clears Plan A spec.

## Headline empirical claims in the paper (all backed by table or SQL recipe)
- Local-government share collapses 25.4 → 13.7 → 6.2 % across phases (Table 2).
- Research-institute share rises 0.2 → 13.2 → 20.6 % (Table 2).
- Governance-frame actions are 59.8% of repertoire vs 20.8% infrastructure-frame (Table 5).
- Hybrid governance mechanism is the dominant mode at 48.1% (Table 6).
- CNIPA holds top betweenness centrality (0.100) — small-specialist-broker pattern (Table 7).
- Shannon diversity peaks at 2.04 in 2018, plateaus through 2022, compresses to 1.40 in 2023 (Table 4).

## Theoretical contribution
*State-led multi-actor coordination (SLMC)* — proposed as a named typological slot, with four operational features: (a) state-led without state-monopoly composition, (b) hybrid-dominant governance mechanism, (c) designation-driven entry logic, (d) governance-frame action repertoire. Distinguished from donor-driven, NGO-driven, developmental-state, and state-capitalist alternatives.

## Where this slots into Mengnan's research program
- **Project A (this paper)**: descriptive-typological. Target *China Quarterly* / *Governance*.
- **Project B (companion)**: causal — links action_events to household panel for poverty-exit estimates.
- **Project C (sibling)**: tests whether SLMC frames travel outward to ASEAN via BRI/GDI. Already scaffolded in `../projectC_asean_governance_export/`.

## What is NOT yet done
- **Figures regenerated to match paper phase definitions**: existing `output_v3/figures/` use pub_year; paper uses data_year. Needs a fresh notebook with the paper's exact phase boundaries (2009–12 / 2013–19 / 2020–22).
- **Formal Bai-Perron breakpoint test**: paper currently makes qualitative break commentary; formal test needs monthly aggregation + seasonal pre-whitening.
- **Provincial-yearbook cross-corpus check**: scaffolded as future work in §6.3.
- **Manual review of LLM-extracted research-institute spike**: §6.2 alternative-explanation discussion would be stronger with hand-verified case audit (~50 events).
- **English translation polish**: this is the working paper; submission-grade English requires another editorial pass.
- **Coordinate footnote citations in proper journal style**: currently inline `(Author Year)` style; target journals may require footnote style.

## Risks logged
- The §5.3 P2 social-participation 74.2% reading is sensitive to compiler framing; the paper acknowledges this and grounds the durable claim in the action-type evidence rather than the entry-mechanism labels.
- Network analysis is single-snapshot static; the 6-month follow-up should build year-wise network panels to track network evolution.
- Some references (Xu Zhang Zhang 2023, Wang Yang 2022) need DOI verification before submission.

## Cross-references
- Strategic plan: `../reasearch_plans/plan_A_org_ecology.md`
- Data source: `../../output_v3/research_enhanced.db`
- Pipeline source: `../../src_v3/`
- Sibling project: `../projectC_asean_governance_export/`
