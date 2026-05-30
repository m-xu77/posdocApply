# Plan E — Political Campaigns as Organizational Mobilization: The 2013–2020 Targeted Poverty Alleviation Campaign

**优先级**：★★★（与 Li Cheng 研究框架对接最紧密的方向，作为 Project 1 的政治学 framing 补强）
**对接 CCCW Track**：(2) Chinese political leadership and governance
**目标产出**：一篇英文期刊文章
**版本**：2026-05-31 初稿

---

## 一、研究问题

### 1.1 核心问题
脱贫攻坚战是习近平时代最具代表性的 **运动式治理 (campaign-style governance)** 的案例。数据库覆盖 **运动启动前 (2009–2012) / 运动中 (2013–2020) / 收尾 (2021–2022)** 三个完整阶段，可以作为 **党国体制大规模组织动员能力** 的实证案例研究。

回答：**在一次政治运动中，党国体制如何把横跨 17 类组织、覆盖 14 年的多主体力量同步动员起来？这种动员的可持续性如何？**

### 1.2 子问题
1. **动员强度**：以"事件密度 × 主体多样性 × 跨级耦合"为指标，运动期间的动员强度比运动前/后高多少？
2. **动员节奏**：运动是单次跃升还是多波次推进？2015 中央扶贫工作会议、2017 十九大、2020 全面脱贫四个时点的动员特征如何？
3. **组织响应顺序**：哪些组织最早响应（先锋）？哪些响应滞后（追随）？组织响应顺序是否揭示党国动员的"传导链"？
4. **运动后效**：2020 全面脱贫宣告后，各类组织是 **退场** 还是 **转型 (transition to rural revitalization)**？哪些组织类型呈现"长效嵌入"？

### 1.3 理论贡献
- 对 Li Cheng 的精英政治研究做 **基层组织响应** 维度的补充
- 对运动式治理理论（周雪光、冯仕政、Heilmann）做 **量化实证** 补强
- 提出"campaign mobilization capacity"的可测量指标体系

---

## 二、数据基础（已就位）

### 2.1 数据库
- action_events 完整覆盖 2009–2022 三阶段
- 已有 17 类组织、人民团体 21 个、民主党派 16 个、央/地党政机关 295 个、央企 109 个——构成完整的"党国动员对象图谱"
- `entry_mechanism` 中的"政策驱动 (1523 条)"、"定点帮扶 (6679 条)" 直接反映动员强度

### 2.2 关键政治时点（pre-coded）
- 2013-11 十八届三中全会（运动启动前奏）
- 2015-11 中央扶贫开发工作会议（运动战役级启动）
- 2016-12 "十三五"脱贫攻坚规划
- 2017-10 十九大（"打赢脱贫攻坚战"写入党章）
- 2020-12 全面脱贫宣告
- 2021-04 国家乡村振兴局成立（运动转型节点）

---

## 三、方法

### 3.1 主分析：动员强度时间序列
- 构建三个核心指标：
  - **Event density**: events_per_year / total_orgs_active
  - **Actor multiplicity**: distinct actor_type 数 + Shannon entropy
  - **Cross-level coupling**: 同一事件中"中央 × 省 × 市 × 县"耦合度
- 按月/季度绘制三个指标的时间序列
- 在六个关键政治时点处标注，做断点检验

### 3.2 组织响应顺序分析
- 对每类组织 (17 类 org_class)，计算其在"运动期 vs 非运动期"的事件密度变化率
- 计算"首次大幅参与"的时点（用 changepoint detection）
- 排序：哪些组织是"先锋"（如央企、人民团体）？哪些是"追随"（如民营企业、社会组织）？
- 用 hazard model 估计组织响应的时间分布

### 3.3 运动转型分析
- 比较 2020-12 前后的组织退出/留存模式
- 哪类组织"转型乡村振兴"成功？哪类组织"运动结束即退场"？
- 与"国家乡村振兴局成立"是否相关？

### 3.4 比较视角（可选）
- 与其他 Xi 时代运动（环保攻坚、反腐、共同富裕）做组织动员模式比较
- 但限于数据，只在 discussion 部分定性比较

---

## 四、行动清单

### 阶段 1：申请前（now → 2026-05-10）
**目标**：在 PS 第四段（"研究 Li Cheng 的程序"）补一句具体的 campaign mobilization 表述

- [ ] 跑通运动期 vs 非运动期的事件密度对比图
- [ ] 在 PS 中补一句"specific subproject on campaign mobilization"

### 阶段 2：入职后第 9–12 月
**目标**：完成 working paper draft

- [ ] 文献综述（运动式治理 + Xi 时代政治学）
- [ ] 跑动员强度三指标 + 断点检验
- [ ] 跑组织响应顺序分析
- [ ] 跑运动转型分析
- [ ] 写完 working paper

### 阶段 3：入职后第二年（若续聘）
- [ ] 投稿 *China Quarterly* 或 *Modern China*
- [ ] 与 CCCW 内 Li Cheng 团队的研究对接：是否可以做 elite politics × organizational mobilization 联合分析

---

## 五、目标期刊

| 期刊 | 影响因子 | 匹配度 | 备注 |
|---|---|---|---|
| China Quarterly | 高 | ★★★★★ | 中国研究旗舰，campaign 主题契合 |
| Modern China | 高 | ★★★★★ | campaign 研究传统强 |
| Journal of Contemporary China | 中 | ★★★★ | 已有发表 |
| China Journal | 中 | ★★★★ | campaign + 政治学 |
| Governance | 高 | ★★★ | 治理理论视角 |

---

## 六、关键风险与对策

| 风险 | 对策 |
|---|---|
| "运动式治理"框架已被过度研究 | 强调"组织生态视角下的运动量化"是新贡献 |
| 与 Li Cheng 风格的对接被认为牵强 | 在 intro 明确：本文研究 leadership-level decision → grassroots organizational response 的因果传导 |
| 时间序列断点的政治意义被过度解读 | 同时报告 quantitative break + qualitative narrative，避免单一统计推断 |
| 数据库只覆盖扶贫一项运动，无法跨运动比较 | 把跨运动比较放在 discussion，明确为 future work |

---

## 七、交付物清单

- [ ] 动员强度三指标时间序列 + 断点检验
- [ ] 组织响应顺序数据集
- [ ] 运动转型分析数据集
- [ ] working paper draft（≥ 8000 words）
- [ ] notebook 保存在 `output_v3/notebooks/E_*.ipynb`
- [ ] PS 中的简短表述
