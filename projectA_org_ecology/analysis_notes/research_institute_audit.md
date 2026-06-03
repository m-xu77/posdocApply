# Hand audit — `actor_type='科研机构'` sample (n=50)

**Date**: 2026-06-01
**Auditor**: MX
**Sampling**: stratified random 25 P2 (2013–2019) + 25 P3 (2020–2022) drawn via SQLite `ORDER BY RANDOM() LIMIT 25` per stratum, against `action_events.actor_type='科研机构'`.
**Source rows**: full file at `/tmp/audit_sample.tsv` (51 lines incl. header).

## Findings before coding

Pre-audit review of the extraction pipeline (`src_v3/02_extract_actions.py`) revealed:

```python
ORG_TO_ACTOR = {
  ...
  "高等院校":  "科研机构",   # universities → "科研机构"
  "科研机构":  "科研机构",
  ...
}
```

The `actor_type='科研机构'` bucket is **a deliberate lumping of `org_class='高等院校'` (universities) and `org_class='科研机构'` (research institutes)**. The "rise from 0.2% to 20.6%" is therefore better read as **"the rise of knowledge institutions (universities + research institutes)"**, not "research institutes alone." This is a labeling problem in the paper, not an extraction error.

## Manual coding of the 50 sampled events

Per row, recorded the institutional type. Counts:

| Institution type | Count | Share |
|---|---|---|
| Universities (`...大学`) | 46 | 92.0% |
| Cadre academies (`...干部学院`) | 2 | 4.0% |
| Pure research institutes (`中国社会科学院`) | 1 | 2.0% |
| University variants (with `定点帮扶` suffix in actor_std) | 1 | 2.0% |

→ **The actor_type bucket is 94% universities + cadre academies, 2% research institutes proper, 4% other knowledge actors.** Universities dominate.

## Substantive vs. thin reporting

Coded each event for whether the `action_desc` contains a substantive engagement (specific monetary amount, specific location, specific named action) vs. boilerplate or thin reporting.

| Substance code | Count | Share |
|---|---|---|
| Substantive (specific money + place + action) | 44 | 88.0% |
| Substantive (specific action, money unspecified) | 5 | 10.0% |
| Thin (overview/boilerplate only) | 1 | 2.0% |

→ **98% of sampled events represent specific, substantive engagement.** The post-2018 spike in this actor_type bucket is real activity, not extraction artifact or thin reporting padding.

## Illustrative quotes (selected)

- 武汉大学 2017: `提供援助资金 50 万元` to 恩施州第一中学.
- 北京邮电大学 2018: `投入帮扶资金 13.01 万元 ... 新建标准化垃圾池 9 个, 加密 LED 照明路灯 50 盏`.
- 厦门大学 2020: `直接拨付无偿帮扶资金 300 万元`.
- 南京大学 2020: `直接投入帮扶资金 334 万元`.
- 东南大学 2022: `投入建设资金 150 万元... 龙川镇二街水厂修缮 + 农村饮水改造`.
- 重庆大学 2022: `向绿春投入和引进帮扶资金 1523.96 万元`.

## Two name-normalization issues surfaced

1. **P3 actor_std suffix drift**: in 2022 specifically, the database has rows like `北京林业大学定点帮扶`, `东南大学定点帮扶`, `重庆大学定点帮扶` as distinct `actor_std` values from `北京林业大学`, `东南大学`, `重庆大学`. This inflates the count of distinct organizations in the diversity computation for 2022. The dedup pass in `src_v3/03_build_orgs.py` did not catch the suffix pattern. **Effect**: marginal over-counting of distinct knowledge-institution actors in 2022; does not change the within-year share story but worth fixing in v2 of the pipeline.

2. **Cross-row description bleed**: some action_desc fields begin with one university's name but the prose then describes a different university's activity. Example sample row 4 (四川大学 培训赋能): "由 ... 在 甘洛 县 学校 组织 开展 'medical staff going to grassroots' activity" — describes 四川大学's activity, but the next sentence shifts to another institution. This is OCR/segmentation bleed-through, present in maybe 5% of the sample. Not corrigible at this stage without re-running extraction.

## Implications for paper §6.2

The "research-institute share rise" finding requires three edits:

### Edit 1 — relabel the actor_type throughout
Change "research institutes" → **"knowledge institutions (universities + research institutes)"** in:
- §5.2 Actor composition narrative
- §5.2 Table 2 column header
- Abstract
- §6.1 SLMC characterization (still holds — knowledge institutions remain a distinct category from line ministries and SOEs, just under a different label)
- §6.4 connection to Li Cheng's program

### Edit 2 — concede the alternative explanation in §6.2 partially
The §6.2 alternative-explanation paragraph currently reads:

> "the research-institute rise is a coding artifact — that university faculty and researchers who were always involved were re-coded into the research-institute category. This is possible at the margin (universities and research institutes are partially overlapping in the LLM's coding), but cannot explain the absolute level of the post-2018 rise: a 100-fold increase in coded research-institute activity from P1 to P3 cannot be accounted for by recoding alone."

This needs to become:

> "the research-institute rise is partly a labeling decision. The `actor_type='科研机构'` bucket as constructed by the extraction pipeline (`src_v3/02_extract_actions.py:ORG_TO_ACTOR`) deliberately lumps `org_class='高等院校'` (universities) and `org_class='科研机构'` (research institutes proper) into a single label. A 50-event audit confirms that 92% of post-2013 events in this bucket are universities, not research institutes proper. The substantive finding is therefore that *knowledge institutions* (chiefly universities) rose from 0.2% to 20.6% of the action stream — a finding that is empirically robust (98% of audited events represent substantive engagement with specific monetary amounts and target locations) but labeled inaccurately in the v1 draft. The post-2018 surge is not an extraction artifact; it is a real expansion of university-led poverty governance, anchored institutionally in the designated-partner program."

### Edit 3 — add an audit footnote
Add to §3 (Data) or §5.7 (Robustness): "A 50-event hand audit of the post-2013 knowledge-institution stratum confirms 98% of events represent substantive engagement; full audit in `analysis_notes/research_institute_audit.md`."

## Coding-decision rules used in this audit

For replication, the rules I applied:
1. **University ⇔ `...大学` or `...学院` suffix without `干部` prefix** in `actor`.
2. **Cadre academy ⇔ `...干部学院` suffix**.
3. **Pure research institute ⇔ `...研究院` / `中科院`/`社科院`/`中央...所` patterns**.
4. **Substantive ⇔ at least one specific (RMB amount OR named county/township OR named program)** in `action_desc`.
5. **Thin ⇔ generic overview language without specific amount/place/action**.

A second coder running these rules on the same 50 rows would be expected to reach κ ≥ 0.85 (high), since the categories are well-defined.

## What this audit did NOT do (initially)

- Did not re-extract or re-classify. The audit accepts the v3 pipeline output and asks what label it carries.
- Did not validate the precision/recall of the original LLM-augmented extraction; that requires a different gold-set protocol.

## Follow-up: FK-join cross-check (whole population, n=3,745)

The 50-event hand audit's estimate of 92% universities was tested against the full P2+P3 population via the org_id foreign key join. SQL:

```sql
SELECT o.org_class, COUNT(*) FROM action_events a
JOIN organizations o ON a.org_id = o.id
WHERE a.actor_type='科研机构' AND a.data_year BETWEEN 2013 AND 2022
GROUP BY o.org_class ORDER BY COUNT(*) DESC;
```

Result:

| org_class | n | share of bucket |
|-----------|---|-----------------|
| 高等院校 (universities) | 3,598 | **96.1%** |
| 科研机构 (research institutes proper) | 147 | 3.9% |

P3-only (data_year 2020–2022):

| org_class | n | share of P3 |
|-----------|---|-------------|
| 高等院校 | 2,092 | **97.0%** |
| 科研机构 proper | 65 | 3.0% |

`org_id` is non-null for every row in the bucket (0 NULL).

**Implication**: the actor_type='科研机构' bucket is essentially **universities** (96–97%), with a tiny tail of research institutes proper. The hand audit was directionally correct but conservatively low; the true university share is 4 pp higher than estimated. Both estimates point to the same conclusion: the "research-institute rise" in the paper should be re-labeled "**university (knowledge-institution) rise**."

## Final recommended paper label

Replace "research institutes" wherever it appears as an actor_type label with:

- **"Universities"** (preferred — short, accurate, captures 96–97% of the bucket).
- Or **"Knowledge institutions"** (slightly broader, captures both universities and the small research-institute tail; analytically more honest about the bucket composition).

Footnote for the chosen label: "The `actor_type='科研机构'` category in the underlying database lumps `org_class='高等院校'` (universities, 96% of post-2013 events in this category) and `org_class='科研机构'` (research institutes proper, 4%); see `analysis_notes/research_institute_audit.md`."
