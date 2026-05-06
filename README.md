# Postdoc Application Workspace

博士后申请管理仓库，包含职位 JD、简历、研究计划及各申请材料。

---

## 目录结构

```
posdocApply/
├── jd/                          # 职位描述
│   └── cccw_postdoc.md          # HKU CCCW 博士后（Ref. 535079）
│
├── applications/                # 各职位申请材料（每岗位一个子目录）
│   └── cccw_hku/
│       └── cv_academic.tex      # 学术简历（LaTeX，针对 CCCW JD 定制）
│
├── resume2/                     # 原始简历素材
│   └── SDE__Monica__Mengnan__Xu__BMHC_version/
│       ├── main.tex
│       ├── particulars.tex      # 个人信息、经历、教育数据
│       └── utilities.tex
│
├── reasearch_plans/             # 研究计划笔记（张老师建议）
│   ├── doc_thesis_plan.md       # 博士论文定位与结构建议
│   └── postdoc_research_plan.md # 博士后阶段研究方向
│
└── tasks/                       # 待办与项目笔记
    ├── tasks_0505.md            # 近期任务清单（2025-05-05）
    └── pa_ngo_db.md             # 扶贫组织生态数据库架构（张老师建议）
```

---

## 当前申请进度

| 职位 | 机构 | 截止日期 | 状态 |
|------|------|----------|------|
| Postdoctoral Fellow (Ref. 535079) | HKU — CCCW | 2026-05-10 | 简历已完成，待补充 cover letter |

---

## 核心研究定位

**博士论文：** 中国扶贫组织生态数据库（2000–2020）——研究中国式发展治理知识体系的形成、组织参与机制及其国际发展意义。

**博士后匹配方向（CCCW）：**
- Chinese political leadership & governance → 扶贫治理、国家能力、组织动员
- AI methods for social science → NLP 流水线、LLM、文本分析、ML

---

## 编译简历

需要本地安装 LaTeX（推荐 MacTeX）：

```bash
brew install --cask mactex   # 首次安装
cd applications/cccw_hku
pdflatex cv_academic.tex
pdflatex cv_academic.tex     # 运行两次以生成正确页码
```

---

## 待完成事项

- [ ] `cv_academic.tex` — 填入实际论文/会议发表记录
- [ ] `cv_academic.tex` — 填入论文导师姓名
- [ ] 撰写 Personal Statement（英文，描述研究经历与博士后计划）
- [ ] 准备三位推荐人名单及邮箱
- [ ] ASEAN 相关文献调研（参见 `tasks/tasks_0505.md`）
- [ ] 扶贫贫困村数据收集方案推进（参见 `tasks/pa_ngo_db.md`）
