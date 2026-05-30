# Plan A — Organizational Ecology of China's Anti-Poverty Governance, 2009–2022

**优先级**：★★★★★（主推方向之一）
**对接 CCCW Track**：(2) Chinese political leadership and governance + (3) AI methods for social science
**目标产出**：一篇英文期刊文章 + 一份可在 PS / CV 中引用的 working paper draft
**版本**：2026-05-31 初稿

---

## 一、研究问题

### 1.1 核心问题
中国扶贫治理体系中，不同类型组织（中央政府、地方政府、央/地国企、高校、金融机构、社会组织、民企）在 2009–2022 这 14 年间的参与结构如何演化？这种"多主体协同"是否构成一种区别于 donor-driven / NGO-driven 模式的 **国家主导多元治理 (state-led multi-actor coordination)**？

### 1.2 子问题
1. **结构演化**：不同 actor_type 的相对权重如何随时间变化？是单调演进还是阶段性跃迁？
2. **机制差异**：定点帮扶、行业援助、东西协作、社会参与、市场进入、政策驱动六类 entry_mechanism 在不同年份/不同组织类型中的相对权重如何？
3. **角色分化**：央企 vs 地方国企、高校 vs 科研机构、人民团体 vs 社会组织——这些"看似同类"的主体在 action_type 分布上是否实质性分化？
4. **协同网络**：组织间协作网络的密度、中心度、模块化如何随时间变化？是否在 2013 年（脱贫攻坚战启动）和 2020 年（全面脱贫）出现结构性断点？

### 1.3 理论贡献
- 对国际发展研究：补充传统 donor / NGO / project-based 模型之外的 **"国家组织化发展治理"** 类型
- 对中国政治学：把 Li Cheng 的精英政治-领导层研究下沉到 **基层实施组织生态**
- 对组织生态理论 (Hannan & Freeman)：在国家强干预语境下检验 organizational diversity 的演化机制

---

## 二、数据基础（已就位）

### 2.1 数据库
- **`organizations` 表**：717 个组织 × 17 个 org_class
- **`action_events` 表**：25,358 条 × 14 年 × 10 actor_type × 11 action_type × 7 entry_mechanism
- 已有四维表：actor_type × year × action_type × entry_mechanism

### 2.2 已就位的分析输出
- `ch3_fig1_org_count_trend.png` — 组织数量年度趋势
- `ch3_fig2_stacked_area.png` — 各类组织参与堆叠面积
- `ch3_fig3_diversity.png` — 组织多样性指数
- `ch3_fig4_entry_mechanism.png` — 进入机制分布
- `ch3_fig5_action_by_actor.png` — 各 actor 的行动类型结构
- `ch5_fig2_collab_network.png` + `ch5_tab2_centrality_top20.csv` — 协作网络

### 2.3 需要新做的数据工作
- 组织生态多样性指数（Shannon / Simpson / Blau）的逐年序列
- entry_mechanism 与 action_type 的联合时间序列（哪些进入机制承载哪些行动）
- 协作网络的逐年快照（density / modularity / assortativity）
- 央企/地方国企/高校 三个子集的独立分析

---

## 三、方法

### 3.1 主分析
1. **描述性时间序列**：actor_type × year 的事件计数与份额；做出明确的"阶段划分图"（pre-2013 / 2013–2020 / 2021–2022）
2. **组织多样性演化**：Shannon entropy on actor_type and on org_class，按年绘制
3. **机制-行动联合分析**：构建 entry_mechanism × action_type 的列联表，每年一张，做对应分析 (correspondence analysis) 看演化轨迹
4. **协作网络分析**：以 collaborators 字段构建年度二模/一模网络，计算 density / clustering / assortativity by actor_type
5. **断点检验**：用 structural break test 检验 2013 / 2020 是否为时间序列断点

### 3.2 稳健性
- 文档/页面权重处理：避免某些年份年鉴更厚导致事件数偏多——按页面数归一化
- 不同 confidence 等级的事件分别跑（low/medium/high）
- 把 `pub_year - data_year` 差异显著的样本剔除做稳健性

### 3.3 因果推断（可选 extension）
- 用 2013 脱贫攻坚战启动作为 shock，做 ITS (interrupted time series) 评估组织生态结构变化
- 用央地财政转移的省际差异作为工具，估计"国家投入"对"社会组织参与"的挤入/挤出效应

---

## 四、行动清单

### 阶段 1：申请前（now → 2026-05-10）
**目标**：跑出 abstract + 3 张关键图，作为 PS / CV 的凭证

- [ ] 跑通 actor_type × year 的事件计数与份额矩阵
- [ ] 计算并绘制 Shannon entropy 时间序列
- [ ] 重做 ch3_fig2_stacked_area，按"政策阶段"加竖线标注
- [ ] 写 250 字 abstract（含 contribution + finding）
- [ ] 选 3 张关键图放入 PS 附录或 CV 链接
- [ ] 在 PS 第三段把这个 project 明确写为 "Project 1"

### 阶段 2：入职后第 1–3 月
**目标**：完成 working paper 投稿稿

- [ ] 撰写 literature review（国际发展 + 组织生态 + 中国扶贫治理）
- [ ] 完成全部稳健性检验
- [ ] 完成协作网络逐年分析
- [ ] 跑断点检验 + ITS
- [ ] 写完 method / results / discussion
- [ ] 第一稿投 *China Quarterly* 或 *Governance*

### 阶段 3：入职后第 3–6 月
**目标**：根据审稿意见修改，或转投

- [ ] 处理审稿意见
- [ ] 如被拒，转投 *Journal of Contemporary China* / *China Review* / *Public Administration*

---

## 五、目标期刊

| 期刊 | 影响因子 | 匹配度 | 备注 |
|---|---|---|---|
| China Quarterly | 高 | ★★★★★ | 中国研究旗舰 |
| Governance | 高 | ★★★★★ | 治理理论顶刊 |
| Journal of Contemporary China | 中 | ★★★★ | 已有发表记录 |
| China Review | 中 | ★★★★ | HKU CCCW 友好 |
| Public Administration | 高 | ★★★ | PA 视角 |

---

## 六、关键风险与对策

| 风险 | 对策 |
|---|---|
| 数据来源单一（仅年鉴） | 在方法学节明确 scope 限制；后续接 ASEAN/双边文档语料拓展 |
| 多样性指标被审稿人质疑 | 同时报告 Shannon / Simpson / Blau 三个指标 |
| 因果推断弱 | 把方向 A 定位为 descriptive / typological，因果留给方向 B |
| 与 Li Cheng 的研究框架对接不清 | 在 intro 明确：本文研究的是"领导决策—基层组织生态"的传导环节 |

---

## 七、交付物清单

- [ ] working paper draft（≥ 8000 words）
- [ ] 一套可复现 notebook（保存在 `output_v3/notebooks/A_*.ipynb`）
- [ ] 5–7 张主图 + 2–3 张稳健性附图
- [ ] GitHub repo 上线（与方向 D 共用）
- [ ] PS 中的项目段落（已部分写好，需要更新数据细节）
