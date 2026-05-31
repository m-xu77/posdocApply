# Headline statistics drawn from `output_v3/research_enhanced.db`

Generated 2026-05-31 from `action_events` (n = 25,358; data_year ∈ [2009, 2022]).

## Overall

- Total action events: **25,358**
- Years covered: 2009–2022 (14 years)
- Organizations identified: 717 (organizations table) across 16 populated org_class categories
- Source: nationwide yearbook corpus, LLM-extracted via the `src_v3/` pipeline

## Events per data year

| Year | n |
|---|---|
| 2009 | 66 |
| 2010 | 855 |
| 2011 | 897 |
| 2012 | 1,006 |
| 2013 | 950 |
| 2014 | 1,612 |
| 2015 | 944 |
| 2016 | 1,732 |
| 2017 | 1,756 |
| 2018 | 2,310 |
| 2019 | 2,771 |
| 2020 | 3,234 |
| 2021 | 3,399 |
| 2022 | 3,826 |

## Three-phase aggregation

| Phase | Years | n | n/year |
|-------|-------|---|--------|
| P1 — pilot decentralized | 2009–2012 | 2,824 | 706 |
| P2 — targeted poverty alleviation (脱贫攻坚) | 2013–2019 | 12,075 | 1,725 |
| P3 — completion + post-2020 consolidation | 2020–2022 | 10,459 | 3,486 |

Per-year volume scales ≈ 5× from P1 to P3.

## Actor composition by phase (count and within-phase share)

| Actor type | P1 n (%) | P2 n (%) | P3 n (%) |
|------------|----------|----------|----------|
| 中央政府 (Central state) | 932 (33.0) | 2,832 (23.5) | 2,958 (28.3) |
| 地方政府 (Local state) | 716 (25.4) | 1,655 (13.7) | 652 (6.2) |
| 国有企业 (SOE) | 417 (14.8) | 2,622 (21.7) | 2,464 (23.6) |
| 科研机构 (Research institutes) | 7 (0.2) | 1,588 (13.2) | 2,157 (20.6) |
| 民营企业 (Private firms) | 76 (2.7) | 1,028 (8.5) | 758 (7.2) |
| 金融机构 (Finance) | 180 (6.4) | 707 (5.9) | 420 (4.0) |
| 人民团体 (Mass orgs) | 141 (5.0) | 593 (4.9) | 248 (2.4) |
| 社会组织 (Social orgs) | 231 (8.2) | 363 (3.0) | 415 (4.0) |
| 民主党派 (Democratic parties) | 94 (3.3) | 359 (3.0) | 193 (1.8) |
| 其他 (Other) | 30 (1.1) | 328 (2.7) | 194 (1.9) |

**Headline shifts**:
- **Local government share collapses**: 25.4% → 13.7% → 6.2%. A 19.2-pp drop across 14 years.
- **Research-institute share explodes**: 0.2% → 13.2% → 20.6%.
- **SOE share grows**: 14.8% → 21.7% → 23.6%.
- **Central state remains dominant** in absolute count but proportionally stable around 25–33%.
- **Civic actors** (mass orgs + social orgs + democratic parties) collectively decline from 16.5% to 8.2%.

## Entry-mechanism share by phase

| Entry mechanism | P1 % | P2 % | P3 % |
|------|------|------|------|
| 定点帮扶 (designated pairing) | 37.5 | 3.2 | 50.0 |
| 行业援助 (sectoral assistance) | 26.8 | 17.6 | 6.7 |
| 政策驱动 (policy-driven) | 20.5 | 4.9 | 3.3 |
| 社会参与 (social participation) | 7.1 | 74.2 | 1.7 |
| 东西协作 (east-west pairing) | 4.9 | 0.0 | 3.1 |
| 市场进入 (market entry) | 3.3 | 0.0 | 0.9 |
| 其他 | 0.0 | 0.0 | 34.2 |

The "P2 social participation surge" is real but partly reflects yearbook compilers' choice of framing during the war-on-poverty period. The P3 shift back to 定点帮扶 is the consolidation logic. (Robustness check needed: re-weight by yearbook page count.)

## Governance-mechanism counts (full sample)

| Governance mechanism | n |
|------|---|
| 混合机制 (hybrid) | 12,199 |
| 行政指令 (administrative directive) | 9,458 |
| 社会动员 (social mobilization) | 2,876 |
| 市场激励 (market incentive) | 685 |
| 协作共治 (collaborative co-governance) | 140 |

48.1% of events are categorized as "hybrid"; 37.3% as administrative directive; the residual three categories together account for 14.6%. This is consistent with the "state-led multi-actor coordination" thesis: not pure command, not pure market, dominated by hybrid arrangements.

## Action-type composition (full sample)

| Action type | n |
|------|---|
| 协调监督 (coordination/supervision) | 7,225 |
| 培训赋能 (training/capacity-building) | 5,152 |
| 资金拨付 (fund disbursement) | 3,094 |
| 产业引入 (industry introduction) | 2,735 |
| 人员派驻 (personnel deployment) | 1,881 |
| 对口帮扶 (paired assistance) | 1,145 |
| 项目实施 (project implementation) | 1,097 |
| 基础设施建设 (infrastructure) | 1,071 |
| 市场对接 (market matching) | 1,041 |
| 政策制定 (policy design) | 778 |
| 能力建设 (capacity-building, other) | 139 |

The five governance-heavy actions (协调监督 + 培训赋能 + 人员派驻 + 政策制定 + 能力建设) total 15,175 (59.8%); infrastructure + project implementation + fund disbursement total 5,262 (20.8%). The Chinese model is governance-frame-heavy in its repertoire.

## Shannon diversity (organization mix; pub_year as reported)

| pub_year | H |
|---|---|
| 2010 | 1.79 |
| 2011 | 1.77 |
| 2012 | 1.73 |
| 2013 | 1.72 |
| 2014 | 1.75 |
| 2015 | 1.81 |
| 2016 | 1.89 |
| 2017 | 2.02 |
| 2018 | 2.04 (peak) |
| 2019 | 2.00 |
| 2020 | 1.98 |
| 2021 | 2.03 |
| 2022 | 2.02 |
| 2023 | 1.40 (recompression) |

Diversity rose from 1.72 (2013) to 2.04 (2018), then plateaued; the 2023 recompression coincides with post-脱贫攻坚 consolidation.

## Spatial concentration

Top-7 provinces (out of 31) by event count:

| Province | n |
|---|---|
| 北京 (Beijing) | 1,723 |
| 贵州 (Guizhou) | 1,149 |
| 云南 (Yunnan) | 1,139 |
| 甘肃 (Gansu) | 875 |
| 河北 (Hebei) | 768 |
| 陕西 (Shaanxi) | 679 |
| 广西 (Guangxi) | 562 |

Beijing's high count reflects MFA/central-actor activity reported with Beijing as origin; Guizhou/Yunnan/Gansu are the heaviest *targeted* provinces — the three contiguous-poverty zones.

## Network centrality (top 10)

| Org | Degree centrality | Betweenness |
|---|---|---|
| 国家知识产权局 (CNIPA) | 0.463 | 0.100 |
| 华东理工大学 | 0.164 | 0.058 |
| 南京大学 | 0.060 | 0.033 |
| 国家安全部 | 0.373 | 0.032 |
| 国家文物局 | 0.299 | 0.026 |
| 交通银行 | 0.269 | 0.020 |
| 环境保护部 | 0.194 | 0.018 |
| 国家税务总局 | 0.284 | 0.015 |
| 中南大学 | 0.299 | 0.010 |
| 中国红十字会总会 | 0.299 | 0.010 |

CNIPA is the betweenness-broker of the network — a small central agency that connects many otherwise-disconnected partners. This is a non-obvious finding (the CNIPA "designated-partner" assignment program is the bureaucratic mechanism behind it).
