# Plan B — From Household Effects to Implementation Variation

**优先级**：★★★★★（主推方向之一，与方向 A 合并为 Project 1）
**对接 CCCW Track**：(2) Chinese political leadership and governance
**目标产出**：一篇英文期刊文章（development / governance 双取向）
**版本**：2026-05-31 初稿

---

## 一、研究问题

### 1.1 核心问题
博士论文用 CFPS 户层面板做了 staggered DID，识别出精准扶贫的因果效应——但 **政策效果具有显著的省际/县际异质性**。该异质性来源于 **实施变异 (implementation variation)**：哪些组织参与了？以什么组合参与？资源如何分配？

把扶贫组织生态数据库聚合到省/县级，与 CFPS 户层面 outcome 做匹配，回答：**"哪些组织参与结构带来了更好的减贫与抗返贫效果？"**

### 1.2 子问题
1. **结构-效果对应**：组织多样性高的地区是否带来更可持续的减贫？
2. **机制-效果对应**：定点帮扶 vs 东西协作 vs 社会参与，哪种 entry_mechanism 对脆弱性 (vulnerability) 的降低更显著？
3. **资源-效果对应**：央企/金融机构主导的地区，与社会组织/高校主导的地区，household outcome 是否系统性不同？
4. **可持续性**：哪类组织结构在 2020 全面脱贫后仍然延续治理效应（抗返贫）？

### 1.3 理论贡献
- 把 PS 第六段提出的 **"the methodological gap"** 完整补上：从"政策有效果"上升到"哪种实施结构带来何种效果"
- 在国际发展研究中建立 **"治理结构 → 户层面福利"** 的可识别因果链
- 综合体现：因果识别（DID）+ NLP/LLM（数据构建）+ 治理理论（解释）

---

## 二、数据基础

### 2.1 已有
- **CFPS 七轮面板（2010–2022）**：博士论文已用，户层面 outcome + 县/省 ID
- **action_events 表 (25,358 条)**：已有 `region` 字段（省/市/县），`admin_level` 字段
- 博士论文的 DID 设定、treatment 标识、vulnerability 估计 pipeline

### 2.2 需要新做的数据工作
1. **action_events 的省/县级聚合**：
   - 按 region 聚合，构建 (province, year) × (actor_type / entry_mechanism / action_type) 矩阵
   - 县级聚合需要先把 region 字段标准化到 GB/T 2260 行政区划码
2. **省/县级"组织生态指标"**：
   - 组织多样性（Shannon entropy on actor_type）
   - 央地比 (central-local ratio)
   - 社会参与占比
   - 主导组织类型 (dominant actor)
3. **CFPS-生态数据库 匹配**：
   - 按 county code 或 province code 把生态指标 merge 到户层面
   - 处理覆盖不全的县（缺失插补 vs 排除）

### 2.3 可能的数据扩展
- 国家统计局县级年鉴：补充财政、人口、产业结构等 covariates
- 国务院扶贫办（后改国家乡村振兴局）官网公布的"定点帮扶县名单"，作为 implementation intensity 工具变量

---

## 三、方法

### 3.1 主分析：异质性回归
- **第一步**：复用博士论文 DID 设定，提取每个县的处理效应估计（CATE）
- **第二步**：把 CATE 作为 outcome，回归在县级组织生态指标上：
  - `CATE_c = β0 + β1·diversity_c + β2·central_local_ratio_c + β3·social_pct_c + X_c·γ + ε_c`
- **第三步**：用 entropy balancing / coarsened exact matching 处理省际差异

### 3.2 中介分析
- 探索"组织生态 → 中介变量（如资金到达、培训覆盖、产业引入） → household outcome"
- 用 action_events 中的 `value_num`、`resource_type` 字段构建中介变量

### 3.3 工具变量识别（强化版）
- 利用 **东西协作配对** 的"行政指派"性质（央定，非地方自选）作为外生变化
- 工具：东西协作配对省份的相对发达程度差距
- 这正是 PS 提到的"causal identification strategy robust to staggered treatment timing"的延伸

### 3.4 稳健性
- 不同的多样性指数
- 不同时间窗口（仅 2013–2020 vs 全期）
- 排除"特殊试点县"
- Placebo test：用 2010 前的虚假处理时间

---

## 四、行动清单

### 阶段 1：申请前（now → 2026-05-10）
**目标**：在 PS 中明确写出"已有 CFPS 数据 + 已有组织生态数据库 + 计划合并分析"

- [ ] 标准化 action_events.region 到行政区划码（核心阻断点）
- [ ] 跑通省级聚合 + 1 张省级组织多样性热图
- [ ] 在 PS 中明确写出 Project 1 的两个 component（方向 A + B）

### 阶段 2：入职后第 3–6 月
**目标**：完成完整县级匹配 + 跑出第一稿回归结果

- [ ] 完成县级行政区划标准化
- [ ] 与博士论文 CATE 估计结果 merge
- [ ] 跑第一稿异质性回归
- [ ] 跑工具变量回归
- [ ] 写 method + results

### 阶段 3：入职后第 6–9 月
**目标**：完整 working paper，投稿

- [ ] 写 introduction / literature review（与方向 A 共用部分）
- [ ] 中介分析
- [ ] 全套稳健性
- [ ] 投稿 *World Development* 或 *Journal of Development Economics* (短篇/Letter)

---

## 五、目标期刊

| 期刊 | 影响因子 | 匹配度 | 备注 |
|---|---|---|---|
| World Development | 高 | ★★★★★ | development 顶刊 |
| Journal of Development Economics | 顶 | ★★★★ | 计量取向，门槛极高 |
| Governance | 高 | ★★★★ | 治理结构-效果链条 |
| Studies in Comparative International Development | 中 | ★★★★ | SCID 适合该题 |
| World Bank Economic Review | 高 | ★★★ | development 应用题 |

---

## 六、关键风险与对策

| 风险 | 对策 |
|---|---|
| 县级行政区划标准化耗时 | 申请前先把省级跑通；县级作为 milestone 2 |
| CFPS 县样本覆盖与生态数据库重合度低 | 做 coverage diagnostic + 报告对内推断范围 |
| 异质性 CATE 的估计本身误差大 | 用 R-learner / DR-learner 等 ML-based 估计稳健性 |
| 工具变量外生性争议 | 备 alternative IV：邻省脱贫率、灾害冲击 |

---

## 七、交付物清单

- [ ] 标准化的行政区划-生态指标数据集（CSV）
- [ ] 异质性回归 notebook（保存在 `output_v3/notebooks/B_*.ipynb`）
- [ ] working paper draft（≥ 10000 words）
- [ ] CFPS-action_events 合并 pipeline 代码（与方向 A repo 共享）
- [ ] PS 中的项目段落更新
