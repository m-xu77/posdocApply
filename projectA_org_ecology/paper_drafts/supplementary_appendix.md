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

## C. Robustness-check details

### C.1 Page-count normalization (paper §5.7 first check)

Yearbook page counts (central yearbook series only):

| Phase | Years | Total pages | Events per page |
|---|---|---|---|
| P1 | 2010–2013 (pub_year) | ~1,200 | 2.35 |
| P2 | 2014–2020 (pub_year) | ~3,000 | 4.03 |
| P3 | 2021–2023 (pub_year) | ~2,400 | 4.36 |

Per-page increase P1→P3: 1.85×; per-year increase: 4.94×. The page-count account explains ≈ 37% of the volume signal; the residual is substantive.

### C.2 High-confidence subset (paper §5.7 second check)

The high-confidence subset (n = 9,217) preserves the headline patterns:

| Actor type | Full P1 % | High-conf P1 % | Full P3 % | High-conf P3 % |
|---|---|---|---|---|
| Central state | 33.0 | 35.2 | 28.3 | 30.1 |
| Local state | 25.4 | 24.1 | 6.2 | 6.8 |
| SOE | 14.8 | 13.5 | 23.6 | 22.4 |
| Research institutes | 0.2 | 0.3 | 20.6 | 19.4 |

Directional findings unchanged.

### C.3 Compilation-lag subset (paper §5.7 third check)

Excluding rows with `|pub_year - data_year| > 2` removes 1,134 rows (4.5% of sample). The within-phase actor shares change by ≤ 0.7 percentage points on any actor; the local-government collapse and research-institute rise are preserved.

### C.4 Alternative diversity indices (paper §5.7 fourth check)

| pub_year | Shannon H | Simpson 1−D | Inverse Simpson |
|---|---|---|---|
| 2013 | 1.72 | 0.80 | 4.99 |
| 2018 | 2.04 | 0.86 | 7.36 |
| 2022 | 2.02 | 0.86 | 7.13 |
| 2023 | 1.40 | 0.72 | 3.62 |

The three indices trace the same shape: rise to peak around 2017–2018, plateau, sharp compression in 2023.

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
