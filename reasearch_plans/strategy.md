# CCCW Postdoc 申请：岗位画像-个人背景-数据资产 综合策略

**目标岗位**：Postdoctoral Fellow, Centre on Contemporary China and the World (CCCW), HKU
**Ref**：535079
**截止**：May 10, 2026
**版本**：2026-05-31 初稿

---

## 一、CCCW Postdoctoral Fellow 岗位人才画像

### 1.1 岗位定位（来自 `jd/cccw_postdoc.md`）

挂靠 **HKU Centre on Contemporary China and the World（CCCW）**，1 年期可续，明确要求承担 **原创研究 + 数据收集与分析 + 报告撰写** 三大核心任务，研究方向限定在三条赛道：

| Track | 研究方向 | 岗位侧重 |
|---|---|---|
| (1) | ASEAN 国家研究 | 区域研究 / 中国与东南亚关系 |
| (2) | 中国政治领导与治理 (Chinese political leadership and governance) | CCCW 主任 Li Cheng 的旗舰方向 |
| (3) | AI methods for social science | 中心战略级方法学方向 |

### 1.2 岗位想要的人才画像

综合 JD 的"硬要求 + 软要求"和 CCCW 的实际研究取向，理想候选人是一个 **"政治学/治理研究 × 计算社会科学 × 国际/区域视野"** 的复合型青年学者：

**硬性资格**
- 政治学、国际关系、经济学或相关学科 PhD
- 对中国政治、经济、社会、中美关系及更广泛的国际事务（**尤其 ASEAN**）有"demonstrated understanding"
- 有 **学术论文发表记录**
- 掌握 **AI tools for social science research**
- **中英双语**学术写作能力

**软性画像（从语义推断）**
- "highly analytical and rigorously trained"——**实证/计量训练扎实**，不是纯理论或纯叙事研究者
- 能 **独立设计研究方法、组织数据收集**——意味着候选人需要能 own 一个研究项目从 0 到 1
- 能配合"organize events / prepare reports"——具备 policy-facing 的沟通能力
- 1 年合同 + 可续——倾向找 **能快速产出、研究方向已经成型** 的人，而不是还要"找题目"的人

### 1.3 需要的领域知识与研究技能

**领域知识（Domain）**
1. 中国政治学核心议题：党国体制、政策过程、央地关系、领导层动态、治理能力
2. 中国发展研究：扶贫、产业政策、社会治理、国家-市场-社会关系
3. 国际发展 / 中国对外发展合作：BRI、GDI、South-South Cooperation、ASEAN 中国关系
4. 比较政治视角：能把中国经验放到国际发展/全球治理的理论坐标里

**研究技能（Method）**
1. **因果识别 / 政策评估**：DID、IV、面板数据等（评估"治理效果"的标配）
2. **文本即数据 (text-as-data)**：政策文本、领导讲话、官方文档的大规模分析
3. **NLP / LLM 在社科中的应用**：信息抽取、frame analysis、policy diffusion 建模
4. **大规模数据基础设施**：构建可复现 pipeline、结构化数据库、网络/空间分析
5. **学术写作与发表**：英文期刊导向

---

## 二、个人相关背景

### 2.1 背景的三个支柱

**(A) 政治学/公共管理博士训练**
- 北师大公共管理博士（2018–2026），导师张秀兰
- 博士论文：用 CFPS 七轮面板（2010–2022）+ staggered DID + 三阶段最小二乘脆弱性估计评估精准扶贫，已通过外审、5 月答辩
- 议题正好落在 Track (2)：扶贫是 CCP 治理能力的"教科书级"案例

**(B) 一作 SSCI 论文 + 合作发表**
- 一作：*Poor and Lazy* (JCC 2022, SSCI Q1)——中产阶级对贫困的污名化
- 合作：BMJ Open 2019、Health 2019（烟草控制政策评估）
- 满足"record of publishing academic research papers"

**(C) Apple Intelligence + AOI 的工业级 AI 工程经验**
- Apple AI Engineer（2025.6–2026.3）：production-grade LLM/RAG/NLP pipeline
- AOI（2026.4–）：full-pipeline 数据采集与分析系统
- 这是 **唯一能让你在社科 postdoc 池里形成绝对差异化** 的标签——直接对应 Track (3) "AI methods for social science"

### 2.2 当前数据资产（来自 `output_v3/`）

已经构建出一个具有发表潜力的原始数据库：

- **organizations 表**：717 个组织，已分类到 17 个组织类型（央/地党政、央/地国企、国有/商业金融、高校、科研、人民团体、民主党派、基金会、社团、民/外企、媒体、军队武警）
- **action_events 表**：25,358 条扶贫行动事件，覆盖 **2009–2022，14 个年份**，10 类 actor_type、11 类 action_type、7 类 entry_mechanism
- **toc_entries 表**：3,093 条目录条目，已分类
- 已生成的图表：组织数量趋势、多样性指数、进入机制、按 actor 的行动结构、资金趋势、治理机制热图、省际空间分布、组织协作网络（top20 中心度）

这套数据已经直接对应 PS 里所说的"organizational ecology database + replicable computational pipeline"。

---

## 三、五个研究方向（按优先级排序）

把 JD 三条赛道与数据 / 技能逐项匹配，下面是 **最能体现岗位要求技能、且数据已经基本就位** 的五个方向：

| 方向 | 标题 | 对接 Track | 优先级 | 数据状态 | 详细 plan |
|---|---|---|---|---|---|
| A | Who Implements Poverty Alleviation? An Organizational Ecology, 2009–2022 | (2)+(3) | ★★★★★ | 已就位 | `plan_A_org_ecology.md` |
| B | From Household Effects to Implementation Variation | (2) | ★★★★★ | 部分就位 | `plan_B_household_link.md` |
| C | Does China Export Its Poverty Governance Model? ASEAN-facing LLM analysis | (1)+(3) | ★★★★ | 需新采集 | `plan_C_asean_export.md` |
| D | Reproducible LLM Pipelines for Chinese Governance Document Analysis | (3) | ★★★ | 已就位 | `plan_D_method_note.md` |
| E | Political Campaigns as Organizational Mobilization | (2) | ★★★ | 已就位 | `plan_E_campaign_mobilization.md` |

---

## 四、综合策略

### 4.1 一句话定位

> 用扶贫组织生态数据库为实证基础，做 **"中国发展治理的组织化形态"** 研究，方法上以 LLM-based 文本分析 + 因果识别为双轮——既覆盖 CCCW Track (2)，又把 Track (3) 做到工业级，最后用方向 C 把 ASEAN 短板补上。

### 4.2 申请材料的组织

把上述方向 **打包成两个具体的 postdoc project pitch**：

1. **Project 1（主推）= 方向 A + B 合并**
   "Organizational Ecology of Chinese Anti-Poverty Governance and Its Household-Level Effects, 2009–2022"
   ——对接 Track (2) + Track (3)

2. **Project 2（扩展）= 方向 C**
   "Travels of China's Development Governance Model: An LLM-Based Frame Analysis of GDI/BRI Documents toward ASEAN"
   ——补 Track (1) 短板，呼应 CCCW 的国际化叙事

方向 D 和 E 作为副产品 / 申请前的"凭证型"产出（GitHub repo + working paper draft）。

### 4.3 短板与补救

| 短板 | 补救 |
|---|---|
| ASEAN 区域研究无积累 | 用方向 C 把 ASEAN 当"应用语境"而非"区域专长"，强调方法迁移性 |
| 中美关系 / 国际关系无发表 | 在 PS 中不主张这块，把研究锁定在治理 + 发展合作交叉 |
| 1 篇 SSCI 一作偏少 | 方向 D 的方法论 note + 方向 A 的 working paper 同步推进，强化"产出潜力"信号 |

### 4.4 执行节奏（申请前 vs 入职后）

**申请前（now → 2026-05-10 截止前）**
- 方向 A：跑通 working paper draft（至少 abstract + 一张关键图） → 进入 PS / CV
- 方向 D：GitHub repo 公开 + README 写清楚 → CV 上挂链接
- 其余三个方向：只需在 PS 中明确写成"will pursue at CCCW"

**入职后（2026-09 → 2027-09）第 1 年节奏**
- 月 1–3：方向 A working paper 投稿
- 月 3–6：方向 B 数据对接（聚合到省/县 + CFPS 匹配）
- 月 6–9：方向 C ASEAN 语料采集 + pilot 分析
- 月 9–12：方向 E（campaign mobilization）撰写 + 中期报告

---

## 五、文档索引

- `strategy.md` — 本文件
- `plan_A_org_ecology.md` — 方向 A 详细 action plan
- `plan_B_household_link.md` — 方向 B 详细 action plan
- `plan_C_asean_export.md` — 方向 C 详细 action plan
- `plan_D_method_note.md` — 方向 D 详细 action plan
- `plan_E_campaign_mobilization.md` — 方向 E 详细 action plan
- `doc_thesis_plan.md` — 既有：博士论文与博士后定位
- `postdoc_research_plan.md` — 既有：博士后阶段提升方向
