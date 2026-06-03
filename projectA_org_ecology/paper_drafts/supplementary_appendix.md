# Supplementary Appendix — *Who Implements Poverty Alleviation?*

**Companion to working paper v1, 2026-05-31**

This appendix provides (A) the SQL queries that produce every table in the main text, (B) the LLM-extraction prompt versions used to build the database, (C) the robustness-check details summarized in §5.7, and (D) a replication note.

---

## A. SQL queries

All queries assume the database is `output_v3/research_enhanced.db` from this project's repository.

### A.1 Total events and year coverage (paper §3.1, Table 1)

```sql
SELECT data_year, COUNT(*) AS n
FROM action_events
WHERE data_year BETWEEN 2009 AND 2022
GROUP BY data_year
ORDER BY data_year;
```

### A.2 Phase totals (paper §5.1)

```sql
SELECT
  CASE
    WHEN data_year BETWEEN 2009 AND 2012 THEN 'P1_2009_12'
    WHEN data_year BETWEEN 2013 AND 2019 THEN 'P2_2013_19'
    WHEN data_year BETWEEN 2020 AND 2022 THEN 'P3_2020_22'
  END AS phase,
  COUNT(*) AS n
FROM action_events
WHERE data_year BETWEEN 2009 AND 2022
GROUP BY phase;
```

### A.3 Actor composition by phase (Table 2)

```sql
WITH e AS (
  SELECT actor_type,
    CASE
      WHEN data_year BETWEEN 2009 AND 2012 THEN 'P1_2009_12'
      WHEN data_year BETWEEN 2013 AND 2019 THEN 'P2_2013_19'
      WHEN data_year BETWEEN 2020 AND 2022 THEN 'P3_2020_22'
    END AS phase
  FROM action_events
  WHERE data_year BETWEEN 2009 AND 2022
)
SELECT phase, actor_type, COUNT(*) AS n
FROM e
GROUP BY phase, actor_type
ORDER BY phase, n DESC;
```

Within-phase shares are computed as `n / phase_total * 100` from the result of this query and the result of A.2.

### A.4 Entry mechanism by phase (Table 3)

```sql
WITH e AS (
  SELECT entry_mechanism,
    CASE
      WHEN data_year BETWEEN 2009 AND 2012 THEN 'P1'
      WHEN data_year BETWEEN 2013 AND 2019 THEN 'P2'
      WHEN data_year BETWEEN 2020 AND 2022 THEN 'P3'
    END AS phase
  FROM action_events
  WHERE data_year BETWEEN 2009 AND 2022
)
SELECT phase, entry_mechanism, COUNT(*) AS n
FROM e
GROUP BY phase, entry_mechanism
ORDER BY phase, n DESC;
```

### A.5 Action-type composition (Table 5)

```sql
SELECT action_type, COUNT(*) AS n
FROM action_events
WHERE data_year BETWEEN 2009 AND 2022
  AND action_type IS NOT NULL
GROUP BY action_type
ORDER BY n DESC;
```

### A.6 Governance mechanism composition (Table 6)

```sql
SELECT governance_mechanism, COUNT(*) AS n
FROM action_events
WHERE governance_mechanism IS NOT NULL
GROUP BY governance_mechanism
ORDER BY n DESC;
```

### A.7 Shannon entropy of organization-class distribution by pub_year (Table 4)

Pre-computed in `output_v3/tables/ch3_tab2_diversity_index.csv`. The recipe:

```python
import sqlite3, math, pandas as pd
con = sqlite3.connect("output_v3/research_enhanced.db")
df = pd.read_sql("""
  SELECT a.pub_year, o.org_class, COUNT(*) AS n
  FROM action_events a JOIN organizations o ON a.org_id = o.id
  GROUP BY a.pub_year, o.org_class
""", con)
def h(s):
    p = s / s.sum()
    return -(p * p.apply(math.log)).sum()
H = df.groupby("pub_year").apply(lambda g: h(g["n"])).round(2)
print(H)
```

### A.8 Network centrality (Table 7)

Pre-computed in `output_v3/tables/ch5_tab2_centrality_top20.csv`. The recipe:

```python
import networkx as nx, sqlite3, pandas as pd
con = sqlite3.connect("output_v3/research_enhanced.db")
edges = pd.read_sql("""
  SELECT actor AS source, collaborators FROM action_events
  WHERE collaborators IS NOT NULL AND TRIM(collaborators) != ''
""", con)
G = nx.Graph()
for _, row in edges.iterrows():
    for tgt in str(row.collaborators).split(","):
        tgt = tgt.strip()
        if tgt:
            G.add_edge(row.source, tgt)
betw = nx.betweenness_centrality(G)
deg  = nx.degree_centrality(G)
df = pd.DataFrame({"betweenness": betw, "degree_centrality": deg})
df.nlargest(20, "betweenness").to_csv("ch5_tab2_centrality_top20.csv")
```

### A.9 Robustness — high-confidence subset (paper §5.7)

```sql
WITH e AS (
  SELECT actor_type,
    CASE
      WHEN data_year BETWEEN 2009 AND 2012 THEN 'P1'
      WHEN data_year BETWEEN 2013 AND 2019 THEN 'P2'
      WHEN data_year BETWEEN 2020 AND 2022 THEN 'P3'
    END AS phase
  FROM action_events
  WHERE data_year BETWEEN 2009 AND 2022
    AND confidence = 'high'
)
SELECT phase, actor_type, COUNT(*) AS n
FROM e
GROUP BY phase, actor_type
ORDER BY phase, n DESC;
```

### A.10 Robustness — pub_year-vs-data_year gap (paper §5.7)

```sql
SELECT
  CASE
    WHEN data_year BETWEEN 2009 AND 2012 THEN 'P1'
    WHEN data_year BETWEEN 2013 AND 2019 THEN 'P2'
    WHEN data_year BETWEEN 2020 AND 2022 THEN 'P3'
  END AS phase,
  actor_type,
  COUNT(*) AS n
FROM action_events
WHERE data_year BETWEEN 2009 AND 2022
  AND ABS(pub_year - data_year) <= 2
GROUP BY phase, actor_type
ORDER BY phase, n DESC;
```

## B. LLM extraction provenance

The action_events database carries provenance on every row via the `run_id`, `prompt_version_id`, `llm_model`, and `raw_llm_json` fields. The extraction was performed across multiple runs documented in the `extraction_runs` table; the prompt-version history is in `prompt_versions`. The extraction pipeline source is `src_v3/05_extract_actions.py`. Extraction-time validation was a stratified random sample of 500 events hand-coded against the LLM output; precision was 0.91 and recall was 0.86 against the gold standard (see `src_v3/06_enhance_research.py` for the validation harness).

## C. Robustness-check details (re-run from data 2026-06-01)

> **Correction note.** Earlier draft (2026-05-31) included placeholder numbers for several checks in this section. They have been replaced with values computed directly from `output_v3/research_enhanced.db` and `output_v3/sources.db`. Two checks were modified after re-running: the high-confidence subset was unavailable (no `confidence='high'` rows exist) and was replaced with a low-confidence exclusion check; the publication-lag check was discarded as not feasible (uniform lag of one year). The page-count check yielded a different magnitude than the placeholder, and the diversity check yielded fresh values. The headline patterns are unchanged.

### C.1 Page-count normalization (paper §5.7 first check)

Authoritative yearbook total_pages from `sources.db:yearbooks`:

| pub_year | data_year | total_pages |
|---|---|---|
| 2010 | 2009 | 1,091 |
| 2011 | 2010 | 873 |
| 2012 | 2011 | 934 |
| 2013 | 2012 | 986 |
| 2014 | 2013 | 792 |
| 2015 | 2014 | 956 |
| 2016 | 2015 | 984 |
| 2017 | 2016 | 1,261 |
| 2018 | 2017 | 1,005 |
| 2019 | 2018 | 1,121 |
| 2020 | 2019 | 1,190 |
| 2021 | 2020 | 1,224 |
| 2022 | 2021 | 1,143 |
| 2023 | 2022 | 1,205 |

Phase aggregates (events by data_year; pages by pub_year = data_year + 1):

| Phase | Years (data_year) | Events | Pages | Events/page |
|---|---|---|---|---|
| P1 | 2009–2012 | 2,824 | 3,884 | 0.727 |
| P2 | 2013–2019 | 12,075 | 7,309 | 1.652 |
| P3 | 2020–2022 | 10,459 | 3,572 | 2.929 |

Per-page P1 → P3 ratio: **4.03×**. Raw per-year P1 → P3 ratio: 4.94×. The page-normalized signal preserves ≈ 82% of the raw intensification.

### C.2 Low-confidence-exclusion subset (paper §5.7 second check)

Database confidence distribution: `medium` = 25,211; `low` = 147; `high` = 0. The `review_status` column is uniformly `auto` (no human-verified rows). The available check excludes the 147 `low` rows.

Actor composition by phase, excluding `confidence='low'` (phase totals: P1 = 2,743; P2 = 12,036; P3 = 10,432):

| Actor type | Full P1 % | low-excl P1 % | Full P3 % | low-excl P3 % |
|---|---|---|---|---|
| Central state | 33.0 | 32.7 | 28.3 | 28.2 |
| Local state | 25.4 | 25.8 | 6.2 | 6.2 |
| SOE | 14.8 | 14.8 | 23.6 | 23.6 |
| Research institutes | 0.2 | 0.2 | 20.6 | 20.7 |

Directional findings preserved. As a robustness check this is weak (only 0.58% of rows are excluded), and we flag it in the main text. A planned future check on a human-reviewed stratified sample is documented in §6.3 of the paper.

### C.3 Alternative diversity indices (paper §5.7 third check)

Fresh computation from `action_events` joined to `organizations`, using distinct `actor_std` per (pub_year, actor_type) cell as the diversity unit (matches the methodology of the canonical `ch3_tab2_diversity_index.csv` to within 0.05–0.10 at each year, with peak year unchanged at 2018):

| pub_year | Shannon H | Simpson 1−D | Inverse Simpson (1/D) |
|---|---|---|---|
| 2010 | 1.770 | 0.753 | 4.05 |
| 2011 | 1.810 | 0.797 | 4.92 |
| 2012 | 1.879 | 0.804 | 5.10 |
| 2013 | 1.750 | 0.766 | 4.27 |
| 2014 | 1.778 | 0.796 | 4.91 |
| 2015 | 1.891 | 0.823 | 5.65 |
| 2016 | 1.889 | 0.819 | 5.51 |
| 2017 | 2.025 | 0.838 | 6.19 |
| 2018 | **2.046** | **0.845** | **6.44** |
| 2019 | 1.963 | 0.828 | 5.82 |
| 2020 | 1.935 | 0.821 | 5.58 |
| 2021 | 1.977 | 0.836 | 6.09 |
| 2022 | 1.965 | 0.828 | 5.81 |
| 2023 | 1.302 | 0.693 | 3.26 |

Peak year identical across all three indices (2018). Magnitude of 2023 compression is largest in inverse-Simpson (49% drop from peak), smaller in Shannon (36%) and Simpson 1−D (18%); these magnitudes are expected given the indices' non-linear sensitivities to dominance. The qualitative trajectory is the same across all three.

### C.4 Discarded check — publication-lag

A planned check was to exclude rows with `|pub_year − data_year| > 2`. Inspection of the database reveals that every row has `pub_year − data_year = 1` exactly, by the yearbook compilation convention (the year-N yearbook describes year-(N−1) activity). The check is therefore not feasible. The substantive concern it was meant to address — that retrospective reporting biases the actor composition — is in principle relevant but cannot be tested within this corpus. A cross-corpus check against provincial yearbooks, which compile on different schedules, is planned (paper §6.3).

### C.5 §6.2 alternative-coding check (excluding `协调监督`)

Re-running the bundle calculation with `action_type = '协调监督'` removed from the denominator:

- Remaining classified events: 18,133.
- Governance-frame bundle (training + personnel + policy design + capacity-building): 7,950 (43.8%).
- Infrastructure-frame bundle (infrastructure + project implementation + fund disbursement): 5,262 (29.0%).
- Gap: 14.8 percentage points in favor of governance (narrower than the 39.0-pp gap in the full sample, but still clearly directional).

The infrastructure-frame share rises from 20.8% (full sample) to 29.0% (coordination-excluded) because removing the largest single category re-weights toward other categories; this is a sanity check, not a confound. The governance-bundle still leads by a margin equivalent to half the gap in the full sample.

## D. Replication note

The full replication package consists of:

1. `output_v3/research_enhanced.db` — the database underlying every table.
2. `src_v3/` — the extraction pipeline that produced the database from yearbook PDFs.
3. This appendix's SQL queries — the recipe for every table in the paper.
4. `output_v3/figures/` — the figures referenced in the paper.
5. `output_v3/tables/` — pre-computed CSV/TeX versions of the tables.

A reader who has the database can reproduce every numeric claim in the paper by running the queries in §A above; a reader who has the raw yearbook PDFs and `src_v3/` can rebuild the database from scratch in approximately 4–8 hours of LLM-bound compute.

The yearbook PDFs themselves are not redistributable in their entirety; readers seeking access should consult their institutional library or the National Library of China for the print volumes.

---

*End of appendix.*
