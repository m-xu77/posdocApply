# Plan D — Reproducible LLM Pipelines for Chinese Governance Document Analysis

**优先级**：★★★（凭证型产出，与方向 A 同步推进，作为申请阶段的"工程信誉"）
**对接 CCCW Track**：(3) AI methods for social science
**目标产出**：一篇方法论 note + 一个开源 GitHub 工具包
**版本**：2026-05-31 初稿

---

## 一、研究问题

### 1.1 核心问题
社科领域大量研究开始用 LLM 处理中文政策文档、年鉴、领导讲话，但绝大多数 pipeline **不可复现、不可审计、不可对比**——prompt 不公开、模型版本不记录、抽取结果无 confidence 标定、无人工校验流程。

本 note 提出一个 **可复现 LLM 文档分析的最小可行规范 (MVR: Minimum Viable Reproducibility)**，并用扶贫年鉴 25,358 条事件抽取的实际数据展示该规范的落地形态。

### 1.2 论文要回答的方法论问题
1. **Prompt versioning**：如何跟踪 prompt 的迭代？版本与抽取结果如何挂钩？
2. **Run reproducibility**：同一份文档在不同时间、不同模型、不同 prompt 下抽取结果差异多大？
3. **Confidence calibration**：LLM 自报的 confidence 与实际错误率是否对齐？
4. **Human-in-the-loop**：什么样的最小人工校验流程能保证 95% 准确率而不破产？

### 1.3 贡献
- 给计算社会科学社区一个 **可操作的 reference architecture**
- 把工业级的 ML pipeline 工程实践（来自 Apple/AOI 经验）翻译为社科研究规范
- 提供一个 benchmark dataset，后续研究可以对比

---

## 二、数据基础（已就位）

### 2.1 实际 pipeline 代码
- `src_v3/00_build_sources.py` — 文档/页面索引
- `src_v3/01_extract_toc.py` — 目录抽取
- `src_v3/02_classify_toc.py` — rules-based TOC 分类
- `src_v3/03_build_orgs.py` — 组织实体抽取与去重
- `src_v3/05_extract_actions.py` — LLM action 抽取
- `src_v3/06_enhance_research.py` — 后处理增强

### 2.2 数据库的"reproducibility infrastructure"
- `extraction_runs` 表 — 每次跑批的 run_id、模型、参数
- `prompt_versions` 表 — prompt 版本表
- `extraction_log` 表 — 详细日志
- `action_events.review_status` — auto / verified / corrected / rejected
- `action_events.confidence` — high / medium / low
- `action_events.raw_llm_json` — 原始 LLM 输出留底

这套基础设施本身就是论文的核心展示物。

---

## 三、方法

### 3.1 论文骨架
1. **Introduction**：社科 LLM 应用的 reproducibility crisis
2. **The MVR specification**：六条规范
   - prompt versioning (semver-style)
   - run identifier with full provenance
   - raw LLM output retention
   - schema-validated structured output
   - confidence labeling protocol
   - human review escalation rules
3. **Case study**：用扶贫年鉴 25,358 条事件展示
4. **Calibration experiments**：confidence vs error rate
5. **Cross-model comparison**：GPT-5 / Claude Opus 4.7 / Qwen3 / DeepSeek-V4 抽取结果一致率
6. **Recommendations**

### 3.2 需要补做的实验
1. **Cross-model replication**：选 500 个文档，用 3 个不同模型跑同样 prompt，计算抽取一致率
2. **Prompt sensitivity**：选 200 个文档，用 5 个语义相同但表述不同的 prompt 跑，看结果差异
3. **Confidence calibration**：人工标注 1000 条 ground truth，画 reliability diagram
4. **Cost-quality tradeoff**：报告每万条抽取的 API 成本 vs 准确率

### 3.3 开源工具包
把这套规范打包成一个 Python library：
- `gov_llm_extract` (tentative name)
- 提供 `ExtractionRun`, `PromptVersion`, `ReviewQueue` 三个核心抽象
- README + 教程 notebook + 完整 demo（用脱敏后的年鉴片段）

---

## 四、行动清单

### 阶段 1：申请前（now → 2026-05-10）
**目标**：把 GitHub repo 公开，README 写清楚，CV 上挂链接——形成"工程信誉"

- [ ] 整理 `src_v3/` 代码，剥离与项目 A 共用的核心
- [ ] 写 README（架构图 + 快速上手 + 数据库 schema 说明）
- [ ] 选 2–3 张架构图（pipeline 流程 / DB schema / run lineage）
- [ ] 公开 GitHub repo（可先设为 limited public）
- [ ] CV 加一行 "Open-source toolkit for reproducible LLM-based governance document analysis: github.com/..."

### 阶段 2：入职后第 1–3 月
**目标**：完成 cross-model 与 confidence calibration 实验

- [ ] 选择 500 文档 benchmark 集
- [ ] 跑 3 模型 × 5 prompt 矩阵
- [ ] 人工标注 1000 条 ground truth
- [ ] 出 reliability diagram + cost-quality 图

### 阶段 3：入职后第 3–6 月
**目标**：写完 working paper 并投稿

- [ ] 写 introduction 和 specification
- [ ] 写 case study
- [ ] 写 calibration experiments
- [ ] 投稿 *Sociological Methods & Research* 或 *Political Analysis*

---

## 五、目标期刊

| 期刊 | 影响因子 | 匹配度 | 备注 |
|---|---|---|---|
| Sociological Methods & Research | 高 | ★★★★★ | 方法论顶刊 |
| Political Analysis | 顶 | ★★★★ | 计量方法 + 数据基础设施 |
| Journal of Computational Social Science | 中 | ★★★★ | 新兴 CSS 顶刊 |
| PS: Political Science & Politics | 中 | ★★★ | 方法论 note 友好 |
| Big Data & Society | 中 | ★★★ | 跨学科 |

---

## 六、关键风险与对策

| 风险 | 对策 |
|---|---|
| LLM 厂商版本快速迭代导致实验过时 | 报告时锁定具体 model ID + 时间戳 |
| 开源 repo 的法律/版权问题（年鉴文本） | 公开代码 + 公开 schema + 私有数据，只放脱敏 demo |
| 方法论 note 被认为"工程而非研究" | 在 intro 明确定位为 measurement methodology，呼应 Grimmer & Stewart 的 text-as-data 传统 |
| 与方向 A 的产出顺序冲突 | 方向 D 的 GitHub 是申请前必做；论文可放到方向 A 之后 |

---

## 七、交付物清单

- [ ] GitHub repo 公开（含 README、架构图、demo notebook）
- [ ] benchmark dataset（500 文档 + 1000 标注）
- [ ] cross-model / cross-prompt 实验数据
- [ ] working paper draft（≥ 6000 words，方法论 note 长度）
- [ ] CV 上的链接和一句话描述
- [ ] PS 第三段（已写）的具体支撑材料
