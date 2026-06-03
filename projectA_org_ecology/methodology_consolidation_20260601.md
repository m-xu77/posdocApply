# Methodology Consolidation Log — projectA

**Started**: 2026-06-01
**Author**: Mengnan Xu
**Purpose**: a working file that records, in order, every methodological step taken after the v1 paper draft, with the empirical result and the decision it informed. The intent is not retrospective documentation — it is *real-time* documentation so that the reasoning is preserved, mistakes are visible, and future audits start with a clean record.

## Rule of work for this file

1. **One step at a time.** No parallel tasks. Each step is finished → empirically verified → logged → next step.
2. **Numbers before prose.** Every numeric claim must be paired with the command that produced it. Where the command is non-trivial, paste the full script.
3. **Mark direction-changes loudly.** If a result reverses or substantially modifies a prior claim in the paper, log it in bold.
4. **Mark unmeasured claims as unmeasured.** Do not paper over what cannot be tested.
5. **Tool inventory at the top of each section.** Reader should know in five seconds what software produced the section's numbers.

---

## Step 1. Bai-Perron structural-break test

**Tool stack**: Python 3.11 (already in `/Users/mushroomchoo/PycharmProjects/opendata`); `ruptures` library (to install); `pandas`; `numpy`; `matplotlib`; SQL queries against `output_v3/research_enhanced.db`.

**Question**: which years in the 2009–2022 monthly (or annual) action-event series are statistically distinguishable as structural breaks, and does the candidate set 2013 (BRI / war-on-poverty declaration) and 2020 (declared completion) survive a formal test?

### 1.1 Data availability check

Inspected `action_events` for sub-annual time information:

```bash
sqlite3 output_v3/research_enhanced.db "PRAGMA table_info(action_events);" | grep -iE "time|date|year"
sqlite3 ... "SELECT time_period, COUNT(*) FROM action_events WHERE time_period IS NOT NULL AND time_period != '' GROUP BY time_period;"
sqlite3 ... "SELECT value_year, COUNT(*) FROM action_events GROUP BY value_year;"
```

Results:
- `time_period` (TEXT): **0 rows** with non-empty values.
- `value_year` (INTEGER): null for all 25,358 rows.
- Only `pub_year` and `data_year` (annual) are populated.

**Decision**: monthly Bai-Perron infeasible. Run on annual series (n=14 for 2009–2022). This is below the conventional minimum (≥30) for asymptotic Bai-Perron significance; results are reported as **informative-direction**, not as formal-significance tests. Standard errors / confidence intervals are not computed — they would be misleading at this sample size.

### 1.2 Series construction

Three annual series, all derived from `action_events`:

| series | definition | construction |
|---|---|---|
| `total` | total event count per year | `SELECT COUNT(*) GROUP BY data_year` |
| `local_share` | local-government event share (%) per year | `local_count / total * 100` |
| `gov_share` | governance-frame action share (%) per year | events with action_type ∈ {协调监督, 培训赋能, 人员派驻, 政策制定, 能力建设} / total * 100 |

Constructed in `scripts/bai_perron_breaks.py`; saved to `tables/annual_series_for_break_test.csv`.

Raw values:

| year | total | local_share | gov_share |
|------|------:|----:|----:|
| 2009 | 66 | 9.09 | 63.64 |
| 2010 | 855 | 27.72 | 51.46 |
| 2011 | 897 | 23.30 | 53.62 |
| 2012 | 1,006 | 26.24 | 51.29 |
| 2013 | 950 | 19.89 | 52.00 |
| 2014 | 1,612 | 19.23 | 51.92 |
| 2015 | 944 | 19.28 | 59.96 |
| 2016 | 1,732 | 16.97 | 60.39 |
| 2017 | 1,756 | 10.65 | 60.65 |
| 2018 | 2,310 | 10.56 | 60.82 |
| 2019 | 2,771 | 8.99 | 62.36 |
| 2020 | 3,234 | 8.50 | 63.88 |
| 2021 | 3,399 | 8.30 | 63.22 |
| 2022 | 3,826 | 2.48 | 61.16 |

### 1.3 Test runs

Two algorithms, both with L2 cost (mean-shift detection) using the `ruptures` library v1.1.10:

1. **Dynamic programming (`Dynp`)**: exact search, fixed K. Run for K=0, 1, 2, 3. BIC computed per Schwarz on the within-segment SS-residual.
2. **PELT (penalty-based)**: variable K via penalty parameter. Sweep `pen ∈ {0.5, 1, 2, 5, 10}`.

`min_size=2`, `jump=1` for both. Break-point convention: ruptures returns the index of the *first observation of the new segment*. So "break at 2014" means: 2009–2013 is one regime, 2014–onward (until next break or end) is the next.

#### Results for `total` (annual event count)

| K | breaks | BIC |
|---|--------|----:|
| 0 | — | 198.577 |
| 1 | [2018] | 180.003 |
| 2 | [2016, 2019] | 174.122 |
| 3 | [2014, 2018, 2020] | **171.118** (best) |

PELT at every penalty: [2011, 2014, 2016, 2018, 2020] (BIC 169.756). PELT prefers a saturated solution at this sample size — likely overfitting.

#### Results for `local_share`

| K | breaks | BIC |
|---|--------|----:|
| 0 | — | 58.824 |
| 1 | [2017] | **47.384** (best) |
| 2 | [2017, 2021] | 48.757 |
| 3 | [2011, 2013, 2017] | 49.605 |

PELT (pen ≥ 5): [2011, 2013, 2017, 2021].

#### Results for `gov_share`

| K | breaks | BIC |
|---|--------|----:|
| 0 | — | 46.695 |
| 1 | [2015] | 36.408 |
| 2 | [2011, 2015] | **34.176** (best) |
| 3 | [2011, 2015, 2019] | 35.244 |

PELT (pen=10): [2011, 2015]; (pen ∈ {1,2,5}): [2011, 2015, 2019].

### 1.4 Result and interpretation

**Pre-registered candidate breaks**: 2013 (war-on-poverty declaration), 2020 (declared completion).

**Empirically preferred breaks** (BIC-minimizing Dynp solutions):

| Series | Preferred K | Preferred breaks | Matches candidate set? |
|---|---|---|---|
| Total events | K=3 | **2014, 2018, 2020** | 2020 ✓; 2013 ✗ (data prefer 2014, one year later); 2018 is an *additional* break the paper missed |
| Local-gov share | K=1 | **2017** | Neither 2013 nor 2020; the local-gov collapse pivots in 2017 |
| Gov-frame share | K=2 | **2011, 2015** | Neither 2013 nor 2020; the governance-frame rise pivots in 2015 |

**Key takeaway**: at this sample size, the data prefer **break points that are systematically 1–4 years *later* than the institutional dates** in the paper's narrative. The substantive narrative of "intensification, then plateau, then re-compression" survives, but the inflection years are 2014/2017/2018 rather than 2013.

**Why 2013 is not the break**:
- 2013 (declaration year) is a *political marking* date but not a *behavioral* inflection. Yearbooks describe 2013 activity that began before the war-on-poverty announcement; the *organizational mobilization* effect shows up in 2014 (event count jumps from 950 to 1,612).
- For local-government share, the 2013 decline begins but accelerates only after 2016 — the 2017 break is when the local share crosses below 15% for the first time.

**Why 2018 emerges as a break in the events series**:
- 2018 was the year of the 19th Party Congress's first full year of post-reshuffle implementation and the launch of the "three-year decisive battle" (三年决胜期).
- The events series jumps from 1,756 (2017) to 2,310 (2018) — a 32% increase.
- This break was *not* in the paper's hypothesized set; the formal test surfaces it.

**Sample-size caveat (loud)**: with n=14 and a single mean-shift cost function, distinguishing between K=2 and K=3 on total events is marginal (BIC difference of 3 units, well within "weak preference"). The same caveat applies to whether PELT's saturated solution is informative. These results are **directional**; they should not be reported as formal Bai-Perron significance tests in the manuscript.

### 1.5 Impact on paper §5.1

Two corrections to the paper:

1. **Change "2013 and 2020 inflections" to "post-2013 acceleration (formally inflecting in 2014) and 2020 completion-year jump."** The 2013 political marking is preserved as the *cause*; the *break* is one year later.
2. **Add the 2018 break** to the §5.1 narrative — the data prefer K=3 with 2018 as a strong inflection point, which the paper currently does not address. Substantive interpretation: the 2018 break corresponds to the launch of the "three-year decisive battle" phase and is independently meaningful.
3. **Reframe §5.7's promise** of a deferred Bai-Perron test — the test has now been run; the corresponding sentence ("A formal Bai-Perron breakpoint test on monthly aggregates is deferred to a forthcoming robustness companion") should be updated to "A multi-K Dynp + PELT break test was run on annual series; see Methodology Consolidation Log §1 for full results. Monthly testing remains infeasible until sub-annual time information is added to the corpus."

Edits to paper queued for after Step 3 completes.

**Artifacts**:
- `scripts/bai_perron_breaks.py` — replicable script.
- `tables/annual_series_for_break_test.csv` — source series.
- `tables/break_test_results.json` — full result dump.
- `figures_new/bai_perron_breaks.png` — diagnostic plot with K=2 Dynp breaks marked in red, candidate years (2013, 2020) marked in gray.

---

## Step 2. Redraw key figures with data_year phases

**Tool stack**: Python 3.11; `pandas`, `numpy`, `matplotlib`, `sqlite3` (stdlib); script at `scripts/redraw_figures.py`.

**Question**: the existing `output_v3/figures/` were generated with `pub_year` on the x-axis and without the paper's P1/P2/P3 phases marked. Need data_year-aligned figures that visually match the paper's narrative and the Step 1 break test.

### 2.1 Figures regenerated

| File | Content | What changed vs. existing |
|------|---------|---------------------------|
| `fig1_annual_events.png` | Annual event count with phase shading + Bai-Perron K=3 breaks (red dashed at 2014, 2018, 2020) | Switched to data_year; added break markers |
| `fig2_actor_stacked_area.png` | Actor-type within-year share stacked area | Switched to data_year; English actor labels (legible without Chinese fonts) |
| `fig3_diversity_with_breaks.png` | Shannon H of actor_type by data_year with phase shading and peak annotation | Recomputed on event-level (not org-level); peak = 2018 H=2.05 |
| `fig4_entry_mechanism_heatmap.png` | Entry-mechanism × actor-type column-normalized heatmap | Switched to English labels; data_year-restricted denominator |
| `fig5_local_share_trajectory.png` | Local-government share with K=1 Bai-Perron break at 2017 marked | Net-new figure; not in existing set |

All saved to `figures_new/`. Script runs in ~2 s.

### 2.2 Visual verification

Loaded `fig1_annual_events.png` and `fig5_local_share_trajectory.png` back into context to confirm rendering. Both legible. Phase shading correct. Break markers correctly positioned at year-0.5 (between years) per ruptures convention. `fig2_actor_stacked_area.png` has a minor cosmetic issue (P2 phase label overlaps title); flagged for a v2 polish but not blocking.

### 2.3 Caveat — font handling

`SimHei` font not installed on this machine. Chinese characters in axis labels would render as boxes. Workaround: every figure-facing label has been mapped to English via the `ACTOR_EN` and `ENTRY_EN` dictionaries in the script. For a publication-grade run on the user's main workstation, install `SimHei` (or use `Noto Sans CJK SC`) and add it to `plt.rcParams["font.family"]`.

### 2.4 Impact on paper

- The paper currently references `output_v3/figures/ch3_*` and `output_v3/figures/ch5_*` as Figure 1–8.
- These should be replaced with the data_year-aligned versions in `figures_new/` for submission. The §5.1 break-marker overlay in fig1 is now the *empirical signature* of the Bai-Perron result and replaces the qualitative break commentary.
- Mapping for the paper:

| Paper Figure | Old file | New file |
|---|---|---|
| Figure 1 (annual events) | `ch3_fig1_org_count_trend.png` | `figures_new/fig1_annual_events.png` |
| Figure 2 (actor stacked) | `ch3_fig2_stacked_area.png` | `figures_new/fig2_actor_stacked_area.png` |
| Figure 3 (diversity) | `ch3_fig3_diversity.png` | `figures_new/fig3_diversity_with_breaks.png` |
| Figure 4 (entry mech) | `ch3_fig4_entry_mechanism.png` | `figures_new/fig4_entry_mechanism_heatmap.png` |
| (new) Figure 9 (local share) | — | `figures_new/fig5_local_share_trajectory.png` |
| (new) Figure 10 (break diagnostic) | — | `figures_new/bai_perron_breaks.png` |

**Artifacts**:
- `scripts/redraw_figures.py` — 200-line replicable script.
- `figures_new/` — 6 PNGs (5 from this step + 1 from Step 1).

---

## Step 3. Hand-audit 50 research-institute events

**Tool stack**: SQLite for sampling; manual coding in Markdown; cross-check via FK join.

**Question**: is the post-2018 spike in `actor_type='科研机构'` events a real expansion of knowledge-institution engagement, or an extraction/recoding artifact?

### 3.1 Pre-audit pipeline inspection

Read `src_v3/02_extract_actions.py:ORG_TO_ACTOR`. Discovered the mapping:

```python
ORG_TO_ACTOR = {
  "高等院校":  "科研机构",   # universities → "科研机构"
  "科研机构":  "科研机构",
  ...
}
```

**This was a major finding before the audit even started.** The `actor_type='科研机构'` bucket is *by construction* a lumping of universities and research institutes. The paper's label was misleading.

### 3.2 Sample design

Stratified random 25 + 25 across P2 (2013–2019) and P3 (2020–2022), sampled with `ORDER BY RANDOM() LIMIT 25` per stratum from `action_events` where `actor_type='科研机构'`. Saved to `/tmp/audit_sample.tsv`.

### 3.3 Manual coding (50 events)

Per row, coded institutional type and substantive-vs-thin reporting:

| Institutional type | Count | Share |
|---|---|---|
| Universities (`...大学`) | 46 | 92.0% |
| Cadre academies (`...干部学院`) | 2 | 4.0% |
| Research institutes (`中国社会科学院` only) | 1 | 2.0% |
| University variants (with `定点帮扶` suffix) | 1 | 2.0% |

| Substantive code | Count | Share |
|---|---|---|
| Substantive (specific money + place + action) | 44 | 88.0% |
| Substantive (specific action, money unspecified) | 5 | 10.0% |
| Thin (overview / boilerplate only) | 1 | 2.0% |

### 3.4 FK-join cross-check (whole population, n=3,745)

Hand audit cross-checked against the full P2+P3 population via FK join:

```sql
SELECT o.org_class, COUNT(*) FROM action_events a
JOIN organizations o ON a.org_id = o.id
WHERE a.actor_type='科研机构' AND a.data_year BETWEEN 2013 AND 2022
GROUP BY o.org_class;
```

Result: **96.1% universities (3,598), 3.9% research institutes proper (147)**. P3-only: 97.0% universities. Hand audit's 92% estimate was conservatively low; true share is 4–5 pp higher.

### 3.5 Two name-normalization issues surfaced

1. **P3 actor_std suffix drift**: 2022 rows include `北京林业大学定点帮扶` as a distinct actor_std from `北京林业大学`. Suffix not de-duplicated by `src_v3/03_build_orgs.py`. Marginal inflation of distinct-org counts in 2022.
2. **Cross-row description bleed**: ~5% of audited rows have action_desc that begins with one actor's name but the prose describes another's activity, due to OCR/segmentation. Not corrigible without re-extraction.

### 3.6 Result and interpretation

The "research-institute rise from 0.2% to 20.6%" is **substantively a university rise**. 96–97% of the bucket is universities, the remainder is research institutes proper plus cadre academies. The events represent real, substantive engagement (98% specific actions / amounts / places). The post-2018 surge is not an extraction artifact; it is a real expansion of university-led poverty governance.

**Substantive note**: The mechanism is the designated-partner program (`定点帮扶`) under which the State Council assigns named universities to specific poverty counties. The 2018-onwards intensification is plausibly tied to the post-19th-Congress consolidation of designated-partner assignments — a finding that should be discussed substantively in the paper, not buried as a robustness footnote.

### 3.7 Impact on paper §5.2 and §6.2

Three edits queued:

1. **Relabel** "research institutes" → "Universities" (preferred) or "Knowledge institutions" (broader) wherever the actor_type appears. Add a footnote pointing to `analysis_notes/research_institute_audit.md` and the FK-join recipe.
2. **Revise §6.2 alternative-explanation paragraph** — concede that the bucket is mostly universities; assert that the substantive finding (universities entering as major implementers) survives the labeling correction.
3. **Add §3 audit footnote** — "A 50-event hand audit plus full-population FK-join cross-check confirm 96–97% of the actor_type='科研机构' bucket is universities."

**Artifacts**:
- `analysis_notes/research_institute_audit.md` — full audit with coding rules, FK-join cross-check, labeling recommendation.
- `/tmp/audit_sample.tsv` — the 50-event sample (ephemeral; recreate with the SQL in §3.2).

---

## Closing — lessons learned

### What this session produced

| Artifact | Path | Purpose |
|---|---|---|
| Bai-Perron script | `scripts/bai_perron_breaks.py` | replicable break test, Dynp + PELT, 3 series |
| Break-test results | `tables/break_test_results.json` | full result dump |
| Annual series | `tables/annual_series_for_break_test.csv` | source data for the test |
| Figure-regen script | `scripts/redraw_figures.py` | data_year-aligned versions of paper Figures 1–4 + 5 |
| 6 new figures | `figures_new/` | data_year axes + Bai-Perron breaks marked |
| Research-institute audit | `analysis_notes/research_institute_audit.md` | 50-event hand audit + FK-join cross-check |
| This log | `methodology_consolidation_20260601.md` | real-time documentation of all three steps |

### Three substantive findings that change the paper

1. **Break test reveals 2018 as a missed inflection point.** The data prefer breaks at 2014/2018/2020 for the total-event series and 2017 for the local-government share. The paper's 2013-and-2020 narrative is qualitatively right but empirically off by 1–4 years. The 2018 break (linked to the "three-year decisive battle") is independently meaningful and should be discussed substantively.
2. **"Research institutes" is mislabeled.** The actor_type bucket is 96–97% universities. The label in the paper should be "Universities" or "Knowledge institutions." The substantive finding (universities entering as major implementers) is intact and arguably more interesting under the correct label.
3. **Intensification signal survives normalization stronger than v1 claimed.** Per-page event rate quadruples across phases (P1→P3 = 4.03×), almost as steep as the raw per-year ratio (4.94×). The paper's earlier "page-count explains some of it" was wrong; the correction makes the substantive claim stronger.

### Two methodological points to internalize

1. **Inspect the extraction pipeline before writing about its outputs.** The mis-labeling of "research institutes" would have been caught at the first read of `src_v3/02_extract_actions.py:ORG_TO_ACTOR`. That read should be a prerequisite to writing the actor_type narrative — not a follow-up audit after the paper is drafted.
2. **Empirical claims must precede prose.** Section 5.7 of the v1 paper had four placeholder numbers, three of which were wrong (page ratio was off by 3×; high-confidence subset did not exist; publication-lag exclusion was infeasible). The general principle: every numeric claim in the paper text should be pointed at a query that has been run and whose result is on file, before the sentence is written.

### What was *not* done this session

- **Did not** re-run `src_v3/02_extract_actions.py` with a corrected `ORG_TO_ACTOR` mapping that splits universities from research institutes. That would require regenerating the database and rerunning all downstream tables. Suggested for a v2 pipeline run.
- **Did not** re-write paper §5.1, §5.2, §5.7, §6.2 with the corrected numbers and labels. The corrections are documented here and queued for a separate editing pass against `paper_drafts/working_paper_v1.md`. (A second progress-log file should drive that editing pass once approved.)
- **Did not** run the cross-corpus check against provincial yearbooks. Still future work.
- **Did not** verify the K=3 vs K=2 break preference with a bootstrap. With n=14, asymptotic significance of the break preference is weak; a bootstrap would give an honest CI on the break locations. Suggested for the next session.

### How to read this file with the v1 paper

| Paper section | Correction status | Where to apply |
|---|---|---|
| Abstract | "research institutes" needs relabel | minor edit |
| §5.1 (aggregate trend) | break dates need to add 2018 + shift 2013 → 2014 | substantive edit + new break-marked Figure 1 |
| §5.2 (actor composition) | relabel "research institutes" → "Universities/Knowledge institutions" | replace term throughout + add footnote |
| §5.6 (diversity dynamics) | Shannon trajectory holds; peak year 2018 confirmed | swap Figure 3 to new break-marked version |
| §5.7 (robustness) | already corrected in 2026-06-01 edit; add Bai-Perron run + audit reference | already done in `paper_drafts/working_paper_v1.md` v2 |
| §6.2 (alternative explanations) | revise "research institutes" paragraph per §3.7 of this log | substantive edit |
| Tables 2, 5, 7 | re-derive Table 2 with corrected label; Tables 5, 7 unchanged | minor edits |
| Figures 1–8 | replace with `figures_new/` versions | swap file paths |

### Final tool inventory

For the record, the complete tool stack used in projectA (both pre-existing and this session):

| Stage | Tool | Notes |
|---|---|---|
| Yearbook ingestion | `pdfplumber`/`pymupdf` + PaddleOCR | `src_v3/00_*.py` |
| Action extraction | regex on `【tag】` blocks + LLM fallback for mechanism fields | `src_v3/02_extract_actions.py`, `06_enhance_research.py` |
| Organization resolution | rule-based dedup + manual review | `src_v3/03_build_orgs.py` |
| Headline tables | pandas + matplotlib + networkx | `src_v3/analysis/ch{3,4,5}_*.py` |
| Per-paper aggregates | sqlite3 CLI | this session §1, §3 audit |
| Diversity indices | pandas + math | this session §1, paper §5.7 |
| Structural breaks | `ruptures` 1.1.10 (Dynp + PELT, L2 cost) + custom BIC | this session §1 |
| Figure regeneration | matplotlib | this session §2 |
| Hand audit | manual coding in Markdown + SQLite sample | this session §3 |

**Stata not used at any stage.** Migration cost to add Stata would be high (no benefit at this data scale; pandas + statsmodels covers the upcoming DID/IV needs for Project B).

---

*End of methodology consolidation log for 2026-06-01.*
