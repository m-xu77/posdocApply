# 01 · Research Questions

**Document status**: v0.1 — locked for design phase
**Last updated**: 2026-05-31

---

## 1. Master question

> **When the Chinese state speaks about development in ASEAN, does it speak as Beijing speaks about poverty at home — and if so, who within the state speaks that way, toward which country, at which time?**

Reframed for empirical traction:

> Does China's outward development discourse toward Cambodia, Laos, Myanmar, and Vietnam between 2013 and 2026 systematically reproduce the *frame inventory* used in China's domestic poverty-governance discourse between 2009 and 2022? If yes, how is that reproduction stratified by (a) bureaucratic actor, (b) target country, and (c) the three policy junctures of 2013 (BRI launch), 2018 (CIDCA founding), and 2021 (GDI launch)?

## 2. Four sub-questions

### RQ1 — Frame transplantation

> To what extent do frames from China's *domestic* poverty-governance discourse (e.g., 定点帮扶, 产业扶贫, 基础设施先行, 多主体动员) appear in the outward GDI/BRI/SSC corpus, and at what density?

- Operationalization: per-document **frame density** = frame mentions per 1,000 tokens.
- Aggregation: by year × actor × target country.
- Identification strategy: contrast frame density in outward corpus vs. (a) the World Bank / ADB corpus for the same four states (donor counterfactual), (b) Chinese MFA discourse on *non-ASEAN* recipients (regional placebo).

### RQ2 — Bureaucratic divergence

> Do MFA, MOFCOM, CIDCA, and central SOEs deploy the same frame mix, or are they internally divergent? Which agency leads in *governance frames* vs. *infrastructure frames*?

- Operationalization: agency × frame profile vectors; cosine similarity matrix; chi-square independence test of (agency, frame) joint distribution.
- Theoretical stake: contests the convenient fiction of a unitary "Beijing" voice. Builds on Jakobson & Knox (2010), Lampton (2014), and the more recent work on CIDCA's institutional positioning (Liu & Tan 2023; Hong 2024).

### RQ3 — Country differentiation

> Are Cambodia, Laos, Myanmar, and Vietnam — four states differently positioned vis-à-vis China — receiving systematically different frame mixes? Does the frame mix track political-economic dependency, regime alignment, or border-security salience?

- Country covariates: aid-per-capita from China (AidData), regime type (V-Dem), trade dependency, border length, ethnic-Chinese diaspora share.
- Identification: country fixed effects + frame-density panel regression on lagged covariates.

### RQ4 — Temporal discontinuity

> Are the three policy junctures (2013 BRI launch, 2018 CIDCA founding, 2021 GDI launch) reflected as structural breaks in frame density, frame diversity, and the governance-to-infrastructure ratio?

- Operationalization: Bai-Perron (2003) multiple-breakpoint test on monthly frame-density series; ITS regression around each juncture.
- Theoretical stake: distinguishes *organizational reshuffling* (CIDCA) from *paradigm renaming* (GDI).

## 3. Boundary conditions

- **Corpus scope**: Documents published *by* official PRC actors (MFA, MOFCOM, CIDCA, central SOEs with foreign-aid mandate, GDI Friends Group materials) *about* development engagement with one or more of CLMV between 2013-01-01 and 2026-04-30.
- **Language scope**: Chinese, English, Khmer, Lao, Burmese, Vietnamese. Non-Chinese/English docs translated via DeepL + verified by native speakers for the validation sample.
- **Exclusion**: classified materials, internal CCP documents, leaked materials, paywalled academic articles.

## 4. Why these four ASEAN states

CLMV is the analytically clean cut: all four are continental-Southeast-Asia mainland-China-bordering or near-bordering, all four are part of the Mekong sub-regional cooperation, all four are net recipients of Chinese development engagement, and the four span the full range of regime alignment from Cambodia (highly aligned) → Laos (aligned) → Myanmar (volatile) → Vietnam (hedging). Excluding the maritime ASEAN-5 reduces confounding from South China Sea disputes.

## 5. What this project deliberately does *not* claim

- It does **not** measure effectiveness, uptake, or recipient-country reception of the frames.
- It does **not** claim that outward frames cause policy adoption in CLMV.
- It does **not** evaluate whether the frames are normatively desirable.

These boundaries are kept tight to keep the methodological contribution unambiguous and to leave Track-(1) ASEAN-domain specialists their natural turf.

## 6. From RQs to publishable claims

| RQ | Headline claim form |
|----|---------------------|
| RQ1 | "We document, for the first time, that X% of China's outward development discourse toward CLMV maps onto a domestic frame dictionary built from 25,358 anti-poverty events." |
| RQ2 | "Bureaucratic agencies do not speak with one voice: CIDCA's frame profile is Y standard deviations from MFA's, with the governance-to-infrastructure ratio Z times higher." |
| RQ3 | "Frame mix is country-differentiated and tracks regime alignment more than trade dependency." |
| RQ4 | "2018 (CIDCA) is the strongest structural break; 2013 (BRI) and 2021 (GDI) are weaker, suggesting bureaucratic reorganization matters more than paradigm renaming." |

These are *targets*, not predictions. The empirics will move them.

## 7. Open issues to revisit

- [ ] Should the dictionary also include *anti-frames* (e.g., "no political conditionality") to capture explicit contrast with OECD-DAC discourse?
- [ ] Should recipient-country official reception (CLMV foreign-ministry statements) be added as an outcome layer, or kept as future work?
- [ ] How to handle joint statements (signed by China + CLMV co-author)? Probably code as "diplomatic-co-produced" subset.
