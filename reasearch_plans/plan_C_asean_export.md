# Plan C — Does China Export Its Poverty Governance Model? An LLM-Based Textual Analysis of GDI/BRI Documents toward ASEAN

**优先级**：★★★★（Project 2：补 Track (1) ASEAN 短板的核心抓手）
**对接 CCCW Track**：(1) ASEAN countries + (3) AI methods for social science
**目标产出**：一篇英文期刊文章 + 一份开放语料库
**版本**：2026-05-31 初稿

---

## 一、研究问题

### 1.1 核心问题
中国是否通过 **GDI (Global Development Initiative)**、**South-South Cooperation**、**BRI** 把国内扶贫治理模式（多主体动员、定点帮扶、基础设施优先）系统性地向 ASEAN 国家输出？输出的是 **"基础设施"** 还是 **"治理制度"**？不同的中国国家行为体（MFA, MOFCOM, 商务部国际发展合作署 CIDCA, 央企）在对外发展话语中是 **frame 一致** 还是 **frame 分化**？

### 1.2 子问题
1. **frame 移植度**：domestic poverty governance 的 frame（如"定点帮扶""产业扶贫""基础设施先行"）在对外语境中以何种密度、何种语境出现？
2. **bureaucratic divergence**：MFA / MOFCOM / CIDCA / 央企的对外发展话语是否一致？哪些 actor 推动"治理输出"，哪些止步于"项目输出"？
3. **国别差异**：柬、老、缅、越四国接收的中国话语是否系统性不同？是否与中国对该国的战略定位相关？
4. **时间演化**：2013（BRI 提出）/ 2018（CIDCA 成立）/ 2021（GDI 提出）三个时点是否形成话语断点？

### 1.3 理论贡献
- 回答国际发展研究的核心未解问题：**China exports institutions or merely infrastructure?**
- 在方法论上推进 **agency-labeled frame analysis** ——把中国话语研究从"宏观 frame"细化到"bureaucratic actor × frame"
- 给"中国式发展治理"理论提供 cross-border 实证支撑

---

## 二、数据基础

### 2.1 国内端（已就位）
- action_events 的 17 类组织 × 11 类 action × 7 类 entry_mechanism 编码体系——这是"国内 frame 字典"的来源
- 已验证的 LLM pipeline（`src_v3/05_extract_actions.py` 等）可以迁移

### 2.2 ASEAN 端（需要新采集）
**核心语料**：
1. **MFA readouts**：外交部网站"领导人活动""中国与东盟关系"专题 readouts，2013–2026
2. **MOFCOM cooperation agreements**：商务部"双边经贸合作"专栏的协议/谅解备忘录
3. **CIDCA materials**：国家国际发展合作署官网的项目公告、白皮书、training materials
4. **GDI training materials**：GDI 官网 + 培训项目文档
5. **双边协定文本**：柬埔寨、老挝、缅甸、越南四国与中国签订的发展合作类协定（中英文）

**外围语料（对照组）**：
- 同期 World Bank / ADB 在四国的项目文档（作为 donor-driven 模型对照）
- 四国本国政府的"接收方"发展话语（英文/官方语言）

### 2.3 估算规模
- 国内端 frame 字典：基于 25,358 条 action_events 抽取
- ASEAN 语料预估：3,000–8,000 份文档，1,500–4,000 万字

---

## 三、方法

### 3.1 阶段 1：国内 frame 字典构建
- 从 action_events 提取 (action_type, entry_mechanism, action_desc) 三元组
- 用 LLM 自动生成每类 frame 的"语义指纹"（关键短语、句法模板）
- 人工 validation：随机抽 200 条，标注是否符合该 frame
- 输出：`domestic_frame_dictionary.json`

### 3.2 阶段 2：ASEAN 语料采集与清洗
- 爬虫/手工采集上述 5 类语料
- 文档 OCR + 元数据抽取（发布机构、日期、目标国、协议类型）
- 中英文双语处理（部分文档需翻译）
- 输出：`asean_corpus/` 目录 + 元数据 CSV

### 3.3 阶段 3：Frame 抽取与分类
- 用 frame 字典 + LLM-based zero-shot classification，对每份文档抽取 frame 命中
- 关键指标：frame_density (per 1000 words), frame_diversity (Shannon on frame counts), governance_to_infrastructure_ratio
- Validation：双标注者 kappa ≥ 0.7

### 3.4 阶段 4：分析
1. **描述性**：每类 frame 在四国语料中的相对频率
2. **bureaucratic comparison**：MFA / MOFCOM / CIDCA 三组的 frame profile 差异（卡方 / 距离矩阵）
3. **时间序列**：年度 frame density 变化 + 2013/2018/2021 断点检验
4. **比较组**：与 World Bank / ADB 文档的 frame 对比，量化"中国 frame 独特性"
5. **国别比较**：四国接收的 frame 组合差异

### 3.5 稳健性
- LLM 模型版本敏感性（GPT-5 / Claude Opus 4.7 / Qwen3 比较）
- 不同 prompt 表述
- 排除高频通用词后的 frame density

---

## 四、行动清单

### 阶段 1：申请前（now → 2026-05-10）
**目标**：在 PS 中已经写明这个 project；申请阶段不需要新数据

- [x] PS 第二个 project 段落已经写好（行 102–122）
- [ ] 准备一段 200 字 pitch 用于面试

### 阶段 2：入职后第 6–9 月
**目标**：完成阶段 1（国内 frame 字典）+ 启动阶段 2（语料采集）

- [ ] 构建 domestic_frame_dictionary.json
- [ ] LLM 帮助抽取 frame 语义指纹
- [ ] 人工 validation 200 条
- [ ] 启动 MFA / MOFCOM / CIDCA 爬虫
- [ ] 完成 1000 份 pilot 文档采集与清洗

### 阶段 3：入职后第 9–12 月
**目标**：完成 pilot 分析，提交中期报告

- [ ] 完成阶段 3 frame 抽取
- [ ] 跑 pilot 描述性分析（500 文档）
- [ ] 写中期报告（CCCW 内部）
- [ ] 在 CCCW workshop 上 present pilot 结果

### 阶段 4：第二年（若续聘）
- [ ] 完成全量语料
- [ ] 跑全套分析
- [ ] 写 working paper
- [ ] 投稿 *International Affairs* / *China Quarterly*

---

## 五、目标期刊

| 期刊 | 影响因子 | 匹配度 | 备注 |
|---|---|---|---|
| International Affairs | 高 | ★★★★★ | IR + 中国对外政策旗舰 |
| China Quarterly | 高 | ★★★★★ | 中国研究旗舰 |
| Journal of Contemporary China | 中 | ★★★★ | 已有发表 |
| Third World Quarterly | 中 | ★★★★ | South-South 主题契合 |
| World Development | 高 | ★★★ | development 视角 |

---

## 六、关键风险与对策

| 风险 | 对策 |
|---|---|
| 部分敏感语料不可公开获取 | 锁定纯公开语料（MFA / MOFCOM / GDI 官网），明确 scope |
| 中文 frame 直译到英文/越南语后失真 | 双语 frame 字典 + 本地母语者 validation |
| ASEAN 区域专长不足导致 framing 不准 | 与 CCCW 内 ASEAN 研究同事合作；引用区域研究文献 |
| LLM 抽取的可重复性 | 用 fixed seed + 多模型 ensemble + 公开 prompt |
| ASEAN 国别专家审稿可能挑战实证细节 | 以"方法论 + 跨国比较"立题，避免做单国深度 case |

---

## 七、交付物清单

- [ ] domestic_frame_dictionary.json + 文档
- [ ] asean_corpus/ 完整语料（带元数据）
- [ ] frame 抽取 notebook（保存在 `output_v3/notebooks/C_*.ipynb`）
- [ ] working paper draft（≥ 9000 words）
- [ ] 开源 GitHub repo（与方向 D 共用基础设施）
- [ ] CCCW workshop slides
