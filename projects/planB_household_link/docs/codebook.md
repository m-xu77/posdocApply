# Plan B — Codebook

Variable definitions for the processed datasets.

---

## `data/interim/events_geo.parquet`

Long-format event-province table. One row per (event, resolved province).

| field | type | description |
|---|---|---|
| event_id | int | foreign key to `action_events.id` |
| data_year | int | year the action took place (per yearbook coding) |
| pub_year | int | year the source yearbook was published |
| actor_type | str | 14-cat enum: 中央政府, 地方政府, 国有企业, 金融机构, … |
| actor_gov_level | str | empty in the current extraction (see decisions.md D-003) |
| action_type | str | 12-cat enum: 资金拨付, 人员派驻, 项目实施, … |
| governance_mechanism | str | 5-cat enum: 行政指令, 市场激励, 协作共治, 社会动员, 混合机制 |
| entry_mechanism | str | 7-cat enum: 定点帮扶, 行业援助, 东西协作, 社会参与, 市场进入, 政策驱动, 其他 |
| resource_type | str | 8-cat enum |
| value_num | float | raw numeric value of resource (unit NOT normalized) |
| value_unit | str | unit string (元/万元/亿元/…) |
| region | str | original free-text region string from the DB |
| admin_level | str | empty in current extraction |
| target_type | str | 4-cat enum: 贫困县, 贫困村, 贫困户, 特定群体 |
| province_token | str | the province-name token resolved from `region` (e.g., "云南") |
| province_code | str | 2-char GB/T 2260 provincial code (e.g., "53") |
| province_name | str | full province name (e.g., "云南省") |
| region_group | str | NBS 4-cat: 东北 / 东部 / 中部 / 西部 |
| multi_region_n | int | number of resolved provinces in this event's region string |
| weight | float | 1 / multi_region_n; used in all aggregations |

---

## `data/processed/province_ecology_panel.parquet`

Balanced (province × year) panel. 31 provinces × 14 years = 434 rows.

| field | type | description |
|---|---|---|
| province_code | str | GB/T 2260 |
| province_name | str | full name |
| region_group | str | NBS 4-cat |
| data_year | int | 2009–2022 |
| n_events | float | weighted event count (sum of `weight` in the panel cell) |
| n_raw_rows | int | unweighted event-province row count |
| shannon_actor | float | Shannon entropy (nats) of actor_type distribution; '__unknown__' excluded |
| hhi_actor | float | Herfindahl-Hirschman of actor_type distribution |
| n_actor_types | int | count of distinct actor_types observed in the cell |
| central_share | float | weighted share of events with `actor_type == 中央政府` |
| local_share | float | weighted share of events with `actor_type == 地方政府` |
| central_local_ratio | float | central_share / max(local_share, 1e-9) |
| social_share | float | share of {社会组织, 人民团体, 民主党派} |
| soe_finance_share | float | share of {国有企业, 金融机构} |
| university_share | float | share of {高等院校, 科研机构} |
| private_share | float | share of {民营企业, 电商平台} |
| dominant_actor | str | most-common actor_type by weight in the cell |
| entry_pairing_share | float | share of `entry_mechanism == 东西协作` |
| entry_fixed_share | float | share of `entry_mechanism == 定点帮扶` |
| entry_social_share | float | share of `entry_mechanism == 社会参与` |
| entry_market_share | float | share of `entry_mechanism == 市场进入` |
| entry_policy_share | float | share of `entry_mechanism == 政策驱动` |
| total_value_num | float | sum of weighted `value_num` — **NOT** unit-normalized; do not use without Stage 04 |

---

## Categorical reference

### NBS 4-group region partition

| group | provinces (codes) |
|---|---|
| 东北 | 21 辽宁, 22 吉林, 23 黑龙江 |
| 东部 | 11 北京, 12 天津, 13 河北, 31 上海, 32 江苏, 33 浙江, 35 福建, 37 山东, 44 广东, 46 海南 |
| 中部 | 14 山西, 34 安徽, 36 江西, 41 河南, 42 湖北, 43 湖南 |
| 西部 | 15 内蒙古, 50 重庆, 51 四川, 52 贵州, 53 云南, 54 西藏, 61 陕西, 62 甘肃, 63 青海, 64 宁夏, 65 新疆, 45 广西 |

### Actor-type partitions (for `02_province_ecology_panel.py`)

| partition | members |
|---|---|
| CENTRAL_TYPES | {中央政府} |
| LOCAL_GOV_TYPES | {地方政府} |
| SOCIAL_TYPES | {社会组织, 人民团体, 民主党派} |
| SOE_FIN_TYPES | {国有企业, 金融机构} |
| UNIV_TYPES | {高等院校, 科研机构} |
| PRIVATE_TYPES | {民营企业, 电商平台} |
