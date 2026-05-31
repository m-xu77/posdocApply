# 02 · Theoretical Framework

**Document status**: v0.1 — chain of reasoning locked for design phase
**Last updated**: 2026-05-31

---

## 1. The puzzle the framework must answer

Why would a state systematically reproduce its *domestic* policy frames in its *outward* developmental discourse? And why, conditional on doing so, would different bureaucratic agencies of the same state reproduce *different* frames?

The framework chains four bodies of theory to give both a positive answer (when frames travel) and a stratification mechanism (who moves which frames).

## 2. Theoretical chain

### Layer 1 — Frames as analytic objects (Snow–Benford → Béland–Cox)

Frames are interpretive schemata that organize causal claims about a policy problem ("what is the problem", "who is responsible", "what counts as a solution"). Snow and Benford's diagnostic / prognostic / motivational decomposition gives the *internal structure* of a frame; Béland and Cox's "ideational turn" gives the *political work* a frame does (mobilization, legitimation, institutional anchoring).

**Implication for measurement**: a frame is not a keyword. It is a tuple of (problem definition, agent of action, action repertoire). The frame dictionary in this project is built as exactly such a tuple, derived from the (organization × action × entry_mechanism) coding of the domestic 25,358-event corpus.

### Layer 2 — Why frames travel across borders (Weyland; Sharman; Stone)

Cross-border frame travel is a special case of policy diffusion. Weyland (2009) distinguishes four diffusion mechanisms — *coercion, competition, learning, emulation*. Sharman (2008) adds *symbolic emulation* (adopting the *language* without the *practice*). Stone (2008) emphasizes the role of *transfer agents* (consultants, IOs, training networks).

**Implication for hypothesis design**: if China is in *learning* mode, outward frames will be carefully tailored to recipient absorptive capacity (variation across CLMV). If China is in *symbolic export* mode, outward frames will be largely invariant across recipients and time. RQ3 is the test of this distinction.

### Layer 3 — Why agencies within one state diverge (Allison; Halperin; Jakobson–Knox; Lampton)

Allison's bureaucratic-politics model (Model III) says state behavior is a vector sum of agency interests. For Chinese foreign policy specifically:

- **MFA** is the *diplomatic legitimator* — frames optimized for international audience.
- **MOFCOM** is the *commercial-diplomatic broker* — frames optimized for bilateral economic agreements.
- **CIDCA** (founded 2018) is the *developmental-diplomatic coordinator* — frames are still institutionally young, hypothesized to be the *most explicit on domestic-style governance frames* because that is CIDCA's identity claim within the bureaucracy.
- **Central SOEs** are the *project executors* — frames hypothesized to be the most infrastructure-heavy.

**Implication for measurement**: agency-labeled frame vectors should be measurably distinct; CIDCA should be a frame outlier.

### Layer 4 — Why South-South cooperation discourse has its own grammar (Mawdsley; Gray–Gills; Bracho)

OECD-DAC donor discourse is built around the *needs–delivery* dyad (recipient need, donor delivery, conditionality, accountability). South-South cooperation discourse — including but not limited to China's — emphasizes *horizontal solidarity, mutual benefit, non-interference, demonstration*. This is what makes the *governance-to-infrastructure ratio* legible: in DAC discourse, governance frames are *conditionality* frames; in SSC discourse, governance frames are *demonstration* frames.

**Implication for the comparative analysis (RQ1 placebo)**: the World Bank / ADB corpus is not just a baseline — it is a *grammatical alternative*. The contrast quantifies what is distinctly Chinese vs. what is generic developmental-bureaucratic.

## 3. From theory to four central propositions

| # | Proposition (informal) | Drawn from |
|---|------------------------|------------|
| P1 | Domestic poverty-governance frames are reproduced at non-trivial density in outward Chinese GDI/BRI/SSC discourse toward CLMV. | Layers 1 + 2 |
| P2 | The frame mix differs systematically across MFA / MOFCOM / CIDCA / SOEs; CIDCA exhibits the highest governance-to-infrastructure ratio. | Layer 3 |
| P3 | The frame mix differs systematically across CLMV; the variation tracks regime-alignment more strongly than trade dependency. | Layer 2 (learning vs. symbolic) |
| P4 | The 2018 CIDCA founding is a stronger structural break in the frame series than either 2013 BRI launch or 2021 GDI launch. | Layer 3 (institutional anchoring matters) |

Formal, testable versions are in `03_hypotheses.md`.

## 4. What makes this contribution distinct

The literature on China's outward development discourse currently sits in three camps:

- **Qualitative discourse analysts** (Mawdsley 2012; Carmody 2016): rich, but n is small and reproducibility is weak.
- **Quantitative aid-portfolio analysts** (Dreher et al., AidData program): rigorous, but blind to discourse.
- **NLP-on-policy-texts** (Ash & Hansen 2023; Wilkerson & Casas 2017): rigorous and reproducible, but typically applied to legislative speech, not cross-border bureaucratic discourse.

This project occupies an unfilled cell: *cross-border bureaucratic discourse, with a domestic-grounded dictionary, agency- and country-disaggregated, and reproducible end-to-end.* That cell is the contribution.

## 5. Anchors in CCCW's intellectual program

- The CCCW Director's program emphasizes elite-and-institutional analysis of Chinese politics (Li 2016, 2020). This project adapts that lens — *who within the Chinese state speaks, and how* — and ports it from domestic elite analysis to outward bureaucratic discourse.
- CCCW Track (1) requires substantive ASEAN content; the CLMV focus delivers that without claiming area-studies expertise that this project does not have.
- CCCW Track (3) requires AI-methods work; the frame-dictionary + LLM-extraction + ensemble-validation pipeline is the methods contribution.

## 6. Risks to the framework

| Risk | Why it matters | Mitigation |
|------|----------------|------------|
| Frame dictionary "overfits" to domestic discourse and undercounts genuine outward innovations. | Would understate Chinese discursive creativity in outward contexts. | Add an open-ended "novel frame discovery" pass on outward corpus; report the fraction of outward content the dictionary misses. |
| Agencies' apparent divergence reflects *publication-channel* differences (MFA publishes more press-readouts; CIDCA publishes more program docs) rather than ideational divergence. | Confound between actor and document genre. | Genre fixed effects in the regression; report agency-within-genre comparison. |
| 2018 break is actually due to 19th Party Congress reshuffles, not CIDCA specifically. | Causal attribution to CIDCA founding becomes fragile. | Report joint test; do not over-claim mechanism beyond what the discontinuity supports. |

## 7. Bibliographic anchors

(Full BibTeX in `01_literature/bibtex/framework.bib` once compiled.)

Snow, D.A. & Benford, R.D. (2000). Framing processes and social movements. *Annual Review of Sociology*.
Béland, D. & Cox, R.H. (2013). The politics of policy paradigms. *Governance*.
Weyland, K. (2009). *Bounded Rationality and Policy Diffusion*. Princeton UP.
Sharman, J.C. (2008). Power and discourse in policy diffusion. *International Studies Quarterly*.
Stone, D. (2008). Global public policy, transnational policy communities. *Policy Studies Journal*.
Allison, G.T. (1971). *Essence of Decision*. Little, Brown.
Lampton, D.M. (2014). *Following the Leader*. UC Press.
Jakobson, L. & Knox, D. (2010). New foreign policy actors in China. SIPRI.
Mawdsley, E. (2012). *From Recipients to Donors*. Zed Books.
Gray, K. & Gills, B.K. (2016). South-South cooperation and the rise of the Global South. *Third World Quarterly*.
Ash, E. & Hansen, S. (2023). Text algorithms in economics. *Annual Review of Economics*.
Wilkerson, J. & Casas, A. (2017). Large-scale computerized text analysis in political science. *Annual Review of Political Science*.
Li, C. (2016). *Chinese Politics in the Xi Jinping Era*. Brookings.
