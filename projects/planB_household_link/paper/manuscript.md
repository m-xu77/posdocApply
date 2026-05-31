---
title: "State-Led Multi-Actor Coordination: An Organizational-Ecology Account of China's Anti-Poverty Governance, 2009–2022"
author:
  - Mengnan Xu
affiliation:
  - Beijing Normal University (PhD); CCCW, University of Hong Kong (postdoctoral applicant)
keywords:
  - Chinese governance
  - organizational ecology
  - poverty alleviation
  - implementation studies
  - text-as-data
version: "0.1 — working paper, 2026-05-31"
abstract: |
  China's 2013–2020 *精准扶贫* (targeted poverty alleviation) campaign is widely
  understood as a state-led mobilization. Yet the field still lacks a
  systematic, organization-level account of *who, in what combination, by what
  mechanism* actually implemented the campaign. Drawing on a newly constructed
  database of 25,358 implementation-action events extracted from fourteen
  consecutive volumes of the State Council's official yearbook *China Yearbook
  of Poverty Alleviation and Development* (2009–2022) via a versioned large-
  language-model pipeline, this paper builds a province-year panel of
  organizational-ecology indicators — Shannon diversity, central-local
  composition, sectoral mix, and entry-mechanism shares — for thirty
  mainland provinces. Three findings emerge. First, organizational diversity
  rose monotonically through the campaign and peaked, with a sharp
  structural break (Chow F = 15.9 at 2020), at the very moment the campaign
  was declared completed; the *implementation regime* was at its most
  organizationally plural at the campaign's endpoint, not its launch.
  Second, the central-government share of implementation traces a *U*:
  high at campaign initiation, suppressed through the multi-actor
  mobilization phase, and recentralized post-2021. Third, the six
  pre-defined *entry mechanisms* are mapped near-bijectively onto actor
  types: East–West pairing is 100% local-government; sectoral assistance
  is 70% central; market entry is 66% state-owned-enterprise. The result is
  a typology of *state-led multi-actor coordination* that is empirically
  distinct from donor-driven, NGO-driven, or project-based development
  governance. The paper closes by sketching a forthcoming companion study
  that links these provincial ecologies to household-welfare effects
  estimated from the China Family Panel Studies (CFPS).
---

# 1 Introduction

In the comparative-development literature, the implementation phase of large
poverty-reduction programs has long been treated as an organizational
black box. From the World Bank–era donor-driven model to NGO-led
project finance, the analytical convention is to specify the *funder*
and the *recipient*, count the dollars, and read off the welfare
effect. The intermediating organizational structure — *who actually
shows up, in what combination, with what division of labor* — is
collapsed into a residual.

China's 2013–2020 *精准扶贫* campaign refuses this collapse. By the time
the State Council declared the rural population free of absolute
poverty in February 2021, the operational record listed central
ministries, twenty-nine East–West-paired provincial governments, more
than three hundred state-owned enterprises and central banks,
hundreds of universities and research institutes, all eight
state-recognized minor parties (民主党派), the eight "people's
organizations" (人民团体), and a long tail of social organizations and
private firms as implementation participants. The standard reading —
"the Party did it" — fails to specify *what the Party did*, organizationally.
This paper aims to specify it.

I make three contributions.

**Empirical.** I introduce, document, and release a province-year panel of
organizational-ecology indicators covering all thirty mainland Chinese
provinces over fourteen consecutive years (2009–2022). The underlying
event corpus is constructed from a versioned large-language-model
extraction pipeline applied to the State Council's official yearbook
series; the extraction's prompt versioning, model identifiers,
re-extraction provenance, and review status are all carried in the
schema so that the corpus can be audited and rebuilt. To my
knowledge no comparable dataset of Chinese anti-poverty
implementation exists at this granularity.

**Theoretical.** I argue that the organizational regime visible in
this panel constitutes an analytically distinct mode of development
governance — *state-led multi-actor coordination* — that does not
reduce to donor-driven aid, NGO-driven projectization, or
state-monopolist command. The defining feature is a near-bijective
mapping of entry mechanisms onto actor types, combined with a
diversity profile that *rises* over the campaign and *peaks at
campaign completion*.

**Methodological.** I show how a large-language-model–constructed
event corpus can be made publication-ready by combining
prompt-versioned extraction, deterministic geographic
standardization (GB/T 2260), fractional-weight aggregation of
multi-region events, and explicit pre-registration of the downstream
inferential design. The methodological pipeline is the *demonstrandum*
of a broader claim: that LLM-mediated text-as-data work in Chinese
governance studies can meet the evidence standards of *China
Quarterly* and *Governance* if its provenance discipline is
sufficiently strong.

The remainder of the paper proceeds as follows. Section 2 situates
the argument in three literatures: organizational ecology, Chinese
governance studies, and computational text-as-data. Section 3 describes
the source corpus and the extraction pipeline. Section 4 specifies
the panel construction. Section 5 presents the three core findings.
Section 6 develops the typology of *state-led multi-actor
coordination*. Section 7 sketches the companion household-effects
study (Plan B in the project's working file). Section 8 concludes.

# 2 Three literatures

## 2.1 Organizational ecology

The starting point is Hannan and Freeman (1977, 1989). Their core
move — treating populations of organizations as the unit of evolutionary
analysis — has anchored four decades of work on niche width, density
dependence, and inertia (Carroll & Hannan 2000). The framework was
developed largely from US firm and voluntary-sector data, and the
literature's standard intuition is that *diversity arises from
competition under fixed resources*. The Chinese case suggests the
opposite causal direction: *diversity arises from coordinated
mobilization under abundant state direction*. This is not a
falsification but a boundary extension. Organizational ecology has long
acknowledged "environmental imprinting" (Stinchcombe 1965) without
specifying what happens when the imprinter is a single, capable, and
strategically active state. Anti-poverty governance under the CCP
since 2013 is the modal observation in this empirical niche, and
this paper offers a structured way to read it.

Three concepts from the organizational-ecology tradition do useful
work here. *Niche width* — the breadth of resources or tasks an
organizational form can survive on — translates directly into the
Shannon entropy of `actor_type` once a coherent task domain (here,
poverty implementation) is fixed. *Resource partitioning* (Carroll
1985) describes how generalist and specialist forms coexist as a
total resource pool grows; the Chinese case lets us observe this
partitioning under the special condition of resource expansion
driven by a single political principal. *Imprinting* (Stinchcombe
1965; Marquis & Tilcsik 2013) describes how the founding conditions
of an organizational population shape its later structure; for the
poverty-implementation population the *founding moment* is not a
single year but the 2013 *脱贫攻坚* declaration, and one of the
paper's findings is that imprinting on that founding moment is
weaker than the population-ecology literature would predict — the
diversification dynamic occurs *during* the campaign, not at its
launch.

The broader empirical literature on state-driven organizational
populations — Skocpol's (1992) account of US welfare-state
provision, Schneiberg's (2002) study of cooperative insurance,
Whetten and Bozeman's (1991) public-organization theory — has
prepared the conceptual ground but has not had a single case where
the founding state is large, capable, ideologically coherent across
seven decades, and operates in a textually documented mobilization
mode. The Chinese anti-poverty regime is that case.

## 2.2 Chinese governance studies

The Chinese-governance literature offers three relevant streams.

Elite-politics studies, exemplified by Li Cheng's multi-decade
leadership databank (Li 2001, 2008, 2016), have built the standard
empirical method for treating Chinese politics as a *measurable*
phenomenon: enumerate the leaders, code their attributes, follow them
through time. The genius of that method is its refusal to read the
party-state as either a black box (the "China watching" tradition) or
a transparent rationalist actor (the modernization tradition). Instead,
it treats elite politics as a *population* and reads its evolution
demographically: cohort by cohort, attribute by attribute. The
current paper extends that move *downward* — from politburo cohorts
to implementation organizations — by adopting the same disciplines
(enumerate the participants, code their attributes, follow them
through time) at the operational tier. Where Li Cheng's databank
specifies the top of the implementation chain, the present panel
specifies its base. The two are mutually illuminating: leadership
turnover at the top is undecodable without organizational
mobilization at the base, and organizational mobilization at the
base is undecodable without political clock at the top.

Cadre-incentive studies (Edin 2003; Landry 2008; Shih, Adolph &
Liu 2012; Wang 2022) document how the central state steers the
periphery through appointment, performance contracts, and target
responsibility systems (*目标责任制*). This literature has done
excellent work on the *signal* — what the center is trying to
elicit. The present argument is complementary: holding cadre
incentives fixed, the *organizational substrate* through which
incentives are converted into implementation itself varies
systematically across provinces and across years. The mobilization
is not merely a bureaucratic affair routed through prefectural
party committees — it is an organizationally plural one routed
through line ministries, central banks, universities, SOEs, minor
parties, mass organizations, and a long tail of civil-society
participants under tight political tutelage.

Campaign-style governance (Heilmann & Perry 2011; Looney 2020;
Perry 2017) is the closest framing in the literature. The standard
account reads the 2013–2020 *脱贫攻坚战* as a return to Mao-era
mobilization techniques (targeted enthusiasm, mass-line
participation, set-piece declarations) layered on top of a
modernized bureaucracy. The framing is useful and the present paper
inherits it. The contribution here is to give the campaign a
quantitative organizational shape: how many actor types appear, in
what mixture, with what entry-mechanism logic, and with what
temporal dynamic. The reader will see that the *campaign* and the
*organizational ecology* are not synonyms — the latter has a distinct
dynamic, peaking after the former is declared complete. The
implication for campaign-governance theory is that the campaign's
analytical primacy needs to be qualified: *what looks like the end of
the campaign is the apex of the ecology it built.*

A fourth, smaller, stream — state-business relations under Xi
(Pearson, Rithmire & Tsai 2021; Heilmann 2018) — frames the
post-2013 organizational mobilization as a recomposition of
state–firm relations under tighter political direction. The present
panel is consistent with that framing: the SOE-and-finance share is
the stable workhorse of the system (0.20–0.29 across all years),
and the rise of central-state engagement post-2021 coincides with
the broader state-strengthening turn after the 2018 constitutional
amendment and the 2021 *共同富裕* (common prosperity) campaign.

## 2.3 Computational text-as-data

The third literature is the one this paper most directly extends.
Large-language-model extraction is now standard in social-science
text-as-data work (Grimmer, Roberts & Stewart 2022; Ornstein et al.
2024). The norm in that literature is to treat the LLM as a black-box
classifier and report inter-rater–style agreement on a hand-coded
sample. The norm is not yet enough for top-tier publication in
Chinese governance studies, where reviewers are reasonably skeptical of
*meaning slippage* between Chinese source text and English-language
analytical categories. This paper adopts a stricter discipline:
prompt versioning (every extracted row carries a prompt-version
identifier), schema enforcement (a controlled vocabulary of fourteen
actor types, twelve action types, seven entry mechanisms, five
governance mechanisms, four target types), and explicit review-status
tracking (auto / verified / corrected / rejected). The corpus is
re-buildable.

# 3 Source corpus

## 3.1 The yearbook

The *Chinese Yearbook of Poverty Alleviation and Development*
(中国扶贫开发年鉴) is the authoritative official annual on the
state's organized anti-poverty work. It was published from 2009
through 2023 under the editorial direction of (variously) the State
Council Leading Group Office for Poverty Alleviation and Development
(国务院扶贫办) — and, from 2022, the National Administration for Rural
Revitalization (国家乡村振兴局). Each annual volume runs to roughly
six hundred to one thousand printed pages and contains sectoral
chapters, organizational reports, regional summaries, and a corpus
of named-organization action records.

The yearbook is a *primary state source*. Its function in the Chinese
political system is documentary and ceremonial — to record who
participated and what they did — not analytical or polemic. For
present purposes that is precisely what is wanted. The bias is not
about whether to record participation but about *which* participations
to record at all; a sub-bureaucratic civic group running a rural
literacy session is invisible to the yearbook even if the central
state is. The paper's claims are scoped accordingly: the panel
describes the organizational ecology *as officially recorded* in the
top-line state archive of Chinese anti-poverty implementation.

## 3.2 The LLM extraction pipeline

The full pipeline is in the project repository (`src_v3/`); the
high-level stages are:

1. **OCR and segmentation** of scanned yearbook pages where digital text
   is unavailable.
2. **Table-of-contents classification** into a controlled vocabulary
   that distinguishes organizational-report sections from analytical
   chapters and statistical appendices.
3. **Action-event extraction** from organizational-report sections via
   a versioned LLM prompt that emits a strict JSON schema covering the
   actor, the action, the resource (if numeric), the governance and
   entry mechanisms, the spatial region, and the time window. Every
   emitted row carries `source_file`, `pdf_page_num`, `pub_year`,
   `data_year`, `run_id`, `prompt_version_id`, `llm_model`,
   `raw_llm_json`, and `raw_excerpt` — so that the extraction is
   fully auditable.
4. **Organization deduplication** through an alias table mapping
   surface strings to canonical organizational identities.
5. **Review-status tagging** (auto / verified / corrected / rejected).

The corpus released with this paper contains 25,358 action events,
717 distinct canonical organizations across seventeen organizational
classes, and 3,093 classified table-of-contents entries.

## 3.3 What the corpus does and does not represent

A documentary corpus is a particular kind of empirical witness, and
the reader is owed a clear statement of what this one represents.

The yearbook's *publication scope* is the totality of organized
anti-poverty work *that the state's central editorial committee
chose to record for posterity*. This is neither the totality of
poverty-reduction activity in China during the period (much
spontaneous market and migration-driven poverty reduction is
invisible to the yearbook) nor the totality of state-organized
anti-poverty activity (programs not yet politically prominent at
the moment of editorial selection may be under-represented).
What the yearbook does represent, comprehensively, is the
*organizationally addressable surface* of the campaign — the set
of participations that an institutional actor at any level of the
state would identify with and want recorded as part of its
contribution. The empirical object of the present paper is exactly
this organizationally addressable surface.

Two consequences follow. First, the panel is best read as a measure
of *what the state has organized*, not *what the population has
experienced*. The companion paper (Plan B) handles the
state-organized → population-experienced linkage through CFPS-based
heterogeneity analysis. Second, year-on-year variation in the
yearbook's coverage is a substantive (not nuisance) parameter: the
editorial expansion of 2016 onward is itself a campaign
phenomenon, and is treated as such in the structural-break tests.

# 4 The province-year ecology panel

## 4.1 Region standardization

The yearbook's `region` field is free Chinese text, often listing
multiple provinces separated by 、 to record an East-West pairing or
a central-ministry assignment spanning several Western provinces. I
tokenize on `、，,;；/`, map each token to the GB/T 2260 two-digit
provincial code, and explode multi-province rows into the long-format
table `events_geo` with weight $w = 1/n$ where $n$ is the number of
provinces named. Of the 25,358 source events, 9,855 (38.9%) have a
resolvable region (the rest carry `region IS NULL`, typically because
the action is recorded at the central or sectoral rather than
provincial level). Of the resolved events, 3,250 (32.9%) name more
than one province — a fingerprint of the East-West pairing system.
All thirty mainland provinces appear in the corpus; no
non-mainland tokens (台湾, 香港, 澳门) appear.

## 4.2 Indicator construction

For each (province × year) cell I compute the following indicators (weighted by $w$ throughout):

* **n_events** — total event count.
* **shannon_actor** — Shannon entropy of the distribution over fourteen
  actor types (`actor_type`), excluding `__unknown__`.
* **central_share, local_share** — share of events with
  `actor_type ∈ {中央政府}` and `{地方政府}`, respectively. (The DB
  field `actor_gov_level`, intended to carry the central/省/市/县/乡
  partition, is uniformly empty in the present extraction — a
  data-quality issue inherited from the upstream prompt; the
  central/local cut is therefore derived from `actor_type` directly.
  This decision is logged in `docs/decisions.md` entry D-003.)
* **social_share, soe_finance_share, university_share, private_share**
  — sectoral shares.
* **entry_pairing_share, entry_fixed_share, entry_social_share,
  entry_market_share, entry_policy_share** — share of the five
  primary entry mechanisms among events with a non-null
  `entry_mechanism`.

The balanced panel has 31 provinces × 14 years = 434 rows × 23
columns. Years for which a province records zero events are kept as
explicit zero rows rather than dropped, so that downstream analysis
can distinguish *no recorded activity* from *missing observation*.

# 5 Findings

## 5.1 Diversity rises, and peaks at the campaign endpoint

The first finding is the simplest and the most important. Figure 1
displays Shannon entropy of `actor_type` by province and year,
grouped by NBS region (东北, 东部, 中部, 西部).

The national, event-weighted Shannon series rises from 1.27 nats in
2009 to 1.78 nats in 2020 — a 40% increase — and then drops sharply
to 1.20 in 2022. A Chow test for a single break in the linear-trend
specification yields F = 15.9 at a hypothesized 2020 break (df 2, 10;
5% critical value ≈ 4.10), F = 5.9 at 2016, and a non-significant
F = 0.72 at 2013. The interpretation is twofold. First, the
diversification of implementation was *not* synchronous with the
campaign's political launch. The 2013 *脱贫攻坚战* declaration moved
the central state's political clock but did not yet move the
organizational substrate. Second, by the time the 2020 全面脱贫
declaration arrived, the organizational substrate had become
profoundly plural — only to retract in 2022 as the campaign's
implementing apparatus was wound down or absorbed into the
*乡村振兴* (rural revitalization) successor program.

Read together: the *organizational ecology peaks where the campaign
ends.* The mobilization regime was at its plural maximum at the very
moment political attention shifted away.

[Figure 1 about here: `output/figures/fig01_shannon_heatmap.png`]

## 5.2 The U-shape of central engagement

The second finding concerns *who* was implementing across the
campaign. Figure 2 displays the event-weighted shares of six actor
groups (central government, local government, social organizations,
SOE-and-finance, universities-and-research, private firms) over
2009–2022.

The central-government share traces a U. It is 0.45 in 2009 (the
top-down initiation period when central ministries dominate the
documentary record), declines to a trough of 0.14 in 2014, hovers
between 0.20 and 0.25 through the 2016–2021 mobilization phase, and
rebounds sharply to 0.42 in 2022. The trough corresponds to the peak
multi-actor mobilization window; the rebound corresponds to the
post-completion consolidation, in which top-line implementation
narrative returned to central organs.

Two countervailing trends complete the picture. The
*university-and-research* share rises monotonically from 0.02 in
2009 to 0.25 in 2022 — a structural shift consistent with the
*高校扶贫* policy expansion and the broader role of universities as
implementation partners. The *SOE-and-finance* share oscillates
around 0.20–0.29 with no monotonic trend, marking SOEs and central
banks as the stable workhorses of the implementation system. The
*social-organization* share remains modest and declines after 2017
(from 0.18 in 2016 to 0.09 in 2022), inconsistent with a narrative
of expanding civil-society participation and consistent with the
broader regulatory tightening of the same period.

[Figure 2 about here: `output/figures/fig02_central_local_timeseries.png`]

## 5.3 Entry mechanisms are near-bijectively assigned to actor types

The third finding is the cleanest. The cross-tabulation of
`entry_mechanism` by `actor_type` (Table 2 in the appendix) shows
that the six pre-defined entry mechanisms do not appear to be
generic implementation vocabulary — each is, in practice, mapped to
a small set of actor types.

* **东西协作** (East-West pairing): **100%** local government.
  This is the system's clearest organizational signature: pairing is,
  by design, an inter-provincial-government affair.
* **政策驱动** (policy-driven): **98%** local government.
* **行业援助** (sectoral assistance): **70%** central government, 14%
  人民团体, 8% SOE/finance. Sectoral assistance is the central state's
  organizational instrument.
* **市场进入** (market entry): **66%** state-owned enterprises, 34%
  private firms. This is the only entry mechanism that mixes the
  SOE and private populations meaningfully.
* **定点帮扶** (designated-pairing assistance): broadly distributed —
  26% SOEs, 22% universities/research, 21% central, 12% private, 9%
  finance, 4% minor parties. *Designated pairing is the
  campaign's main multi-actor coordination zone.*
* **社会参与** (social participation): broadly distributed —
  25% SOEs, 16% universities, 14% central, 11% private, 11% local
  government, 7% social organizations, 5% finance. *Social
  participation is the campaign's main horizontally-coordinated
  zone.*

The first three mechanisms are *organizationally narrow*: they are
the routinized expressions of a particular actor's role. The last
three mechanisms are *organizationally broad*: they are the system's
coordination instruments.

[Figure 3 about here: `output/figures/fig03_event_volume_by_group.png`]

## 5.4 Regional disaggregation: where the ecology lives

Figure 3 displays the volume of weighted action events by NBS region
group over 2009–2022. Three observations stand out.

First, the absolute scale of recorded implementation activity
grows by a factor of twenty-two over the panel: from 65 weighted
events in 2009 to 1,431 in 2022. The growth is not linear. There is
a notable jump between 2009 and 2010 (the campaign's documentary
ramp-up under the *2011–2020 Outline*), a flat plateau through 2015,
and an accelerating climb after 2018 culminating in the 2022 peak.
The post-2018 acceleration is consistent with the *脱贫攻坚战* entering
its declared "final battle" phase.

Second, the regional composition is dominated by the West and the
East. The West (云南, 贵州, 甘肃, 陕西, 四川, 重庆, 广西, etc.) accumulates
4,577 weighted events over the panel — the destination side of the
implementation chain. The East (北京, 上海, 广东, 浙江, 江苏, 山东, 河北,
天津, 福建, 海南) accumulates 3,257 weighted events — the source side
of the implementation chain, including Beijing's role as the central
state's coding bucket. The Central and Northeast regions are smaller,
with 1,703 and 319 weighted events respectively. The
center-to-periphery flow that defines Chinese poverty implementation
is empirically legible at the aggregate.

Third, the top-15 provinces by total weighted events (Table 1) recapitulate
the documentary geography of the campaign. Beijing leads with 1,283
weighted events, reflecting both its substantive role and the
coding bucket effect for events recorded at national rather than
provincial level. Yunnan, Guizhou, Gansu, Hebei, and Shaanxi follow,
each above 400 weighted events. The mean Shannon diversity in
Beijing (1.83), Guizhou (1.67), Yunnan (1.60), Shaanxi (1.60), and
Gansu (1.61) is well above the panel mean of approximately 1.3,
indicating that the recipient provinces did not absorb a uniform
implementation regime — they absorbed an organizationally plural one.

| Rank | Province | Region | Weighted events (2009–2022) | Mean Shannon |
|---|---|---|---|---|
| 1 | 北京市 | 东部 | 1,283.4 | 1.83 |
| 2 | 云南省 | 西部 | 814.7 | 1.60 |
| 3 | 贵州省 | 西部 | 762.6 | 1.67 |
| 4 | 甘肃省 | 西部 | 560.7 | 1.61 |
| 5 | 河北省 | 东部 | 526.6 | 1.55 |
| 6 | 陕西省 | 西部 | 447.8 | 1.60 |
| 7 | 山西省 | 中部 | 333.8 | 1.32 |
| 8 | 重庆市 | 西部 | 330.7 | 1.58 |
| 9 | 广西壮族自治区 | 西部 | 311.2 | 1.54 |
| 10 | 浙江省 | 东部 | 306.0 | 1.13 |
| 11 | 河南省 | 中部 | 298.0 | 1.37 |
| 12 | 湖北省 | 中部 | 289.2 | 1.44 |
| 13 | 湖南省 | 中部 | 279.4 | 1.38 |
| 14 | 青海省 | 西部 | 270.6 | 1.37 |
| 15 | 安徽省 | 中部 | 268.7 | 1.37 |

**Table 1**: Top-15 provinces by total weighted events, 2009–2022.

The ratio of Shannon diversity to event count tells a sharper
story than either alone. Beijing's high diversity is partly an
artifact of central-state coding. The substantively striking cases
are the *recipient* provinces — Guizhou, Yunnan, Gansu, Shaanxi —
which each carry a Shannon entropy above 1.60 over the period.
These provinces are the actual sites where multi-actor coordination
was implemented; their high diversity reflects the fact that the
state mobilized roughly the *same* organizationally plural ecology
into each of them, regardless of their specific bilateral
East-partner.

## 5.4a A note on the 2022 retraction

The 2022 retraction in Shannon diversity — from 1.69 nats in 2021
to 1.20 in 2022 — deserves a closer look. The candidate explanations
fall into three families.

The first is *administrative reorganization*. In April 2021, the
State Council Leading Group Office for Poverty Alleviation and
Development was reconstituted as the National Administration for
Rural Revitalization, and the 2022 yearbook is the first under the
new editorial leadership. Editorial conventions changed; the
proportion of records framed at the central-government level rose
from 0.20 in 2021 to 0.42 in 2022. The retraction is partly an
artifact of editorial recentralization rather than a substantive
contraction of multi-actor participation on the ground.

The second is *campaign-end consolidation*. The formal *脱贫攻坚战*
was declared completed in February 2021. The 2022 record reflects a
period of campaign reporting *after* the operative implementation
window had passed; the action events recorded are those of the
consolidation phase, in which fewer actor types were genuinely
active. On this reading, the retraction is real and reflects the
post-campaign rebalance toward routine bureaucratic management.

The third is *successor program substitution*. The successor *乡村振兴*
(rural revitalization) program has a different organizational logic —
centered on sustainable-industry development and infrastructure —
that re-channels participation away from the poverty-specific
mobilization architecture. Many of the universities, social
organizations, and SOEs that appeared in the 2018–2020 records may
be operating under different administrative classifications in the
2022 cycle.

The three explanations are not mutually exclusive and likely all
contribute. Adjudicating between them requires the additional
documentary apparatus of the *Rural Revitalization Yearbook* series,
which the project's next extraction round will incorporate. For the
present paper, the empirical fact — sharp 2022 retraction with
correlated central-share rebound — stands on its own as a
description of the post-campaign administrative cycle.

## 5.5 What the cross-tabulation rules out

The entry-mechanism × actor-type cross-tabulation in Section 5.3
also rules out two readings that recur in the literature.

It rules out the *fragmented authoritarianism* reading (Lieberthal &
Oksenberg 1988), at least for this campaign. If the implementation
were fragmented across rival ministries each pulling their own
entry mechanism, we would expect entry-mechanism columns to be
spread across many actor types with no obvious assignment logic.
Instead the columns are sharply concentrated: 100% of East-West
pairing is local government, 98% of policy-driven activity is local
government, 70% of sectoral assistance is central government, 66% of
market entry is SOEs. The implementation regime is differentiated
but not fragmented — it is partitioned by political design.

It rules out the *NGO-marketization* reading (Spires 2011; Hsu &
Hasmath 2014). If the campaign had drawn substantively on the
emerging Chinese third sector, we would expect the social-organization
share to rise alongside diversity. Instead, the social-organization
share *declines* from 0.18 in 2016 to 0.09 in 2022, and the
*社会参与* entry-mechanism column itself is dominated by SOEs (25%),
universities (16%), and central organs (14%) — not by social
organizations as such (7%). The Chinese campaign's organizational
plurality is *not* a civil-society plurality. It is a plurality of
state-coordinated state-adjacent populations.

# 6 Typology: state-led multi-actor coordination

Pulling these three findings together yields a typology that may be of
interest beyond the Chinese case.

Define a development-implementation regime by the joint pattern of
*who participates*, *how participants enter the implementation
system*, and *how diversity moves with the campaign clock*. Four
modal regimes can be distinguished:

| Regime | Donor-driven | NGO-driven | State-monopolist | State-led multi-actor |
|---|---|---|---|---|
| Funder | Bilateral / multilateral agency | Foundation / membership | National treasury | National treasury + cross-actor mobilization |
| Implementer base | Recipient-country ministry + contractor | Civil society | Single line ministry | All organizational sectors in mapped roles |
| Entry mechanism | Project tender | Programmatic grant | Bureaucratic assignment | **Differentiated**: pairing, sectoral aid, designated, market, social |
| Diversity over time | Donor-cycle (3–5 yr) | Funding-cycle | Constant | **Monotone-rising; peaks at campaign endpoint** |
| Documentary tier | Project evaluation reports | Foundation reports | State plans | Official yearbooks |

The Chinese *state-led multi-actor coordination* regime is empirically
specific: each of its mechanisms is *organizationally addressed* to a
defined sector of the state's mobilization population, and the
mobilization population *expands* in step with the campaign rather
than rotating with funding cycles or remaining static under a single
ministry.

This typology should be read as the paper's substantive proposition:
not "China is different" but "this organizational profile is the
empirical thing that should be in the typology." The relevant
comparison cases — Brazil's *Bolsa Família* implementation network,
India's MGNREGA delivery system, the EU structural-funds
implementation chain — would each occupy a different cell, and the
present panel construction can be re-applied to them with the
appropriate documentary base.

## 6.0 Engagement with the international-development literature

The typology proposed here can be read as a sympathetic critique of
two contemporary debates in international development.

The first is the *aid-effectiveness* debate (Easterly 2006; Banerjee
& Duflo 2011; Pritchett, Woolcock & Andrews 2010). The standard
analytical move in that literature is to focus on the *project* as
the unit of analysis — to ask whether a given conditional cash
transfer or microcredit intervention worked. The implicit
organizational counterfactual is "no project" rather than "a
different organizational regime." The present typology suggests
that the project-vs-no-project counterfactual under-specifies the
space of possibilities. *Project-based donor-driven implementation*
is itself a regime, with its own implementation ecology, and its
welfare effects are inseparable from that ecology. The Chinese
state-led multi-actor coordination regime is what the welfare
effect literature would call a *bundle*; the standard randomization
machinery is poorly suited to bundle evaluation, and the field has
been honest about that limitation (Deaton 2010; Heckman 2020). The
present panel offers one structured way to read the bundle.

The second is the *capable-states* debate (Acemoglu & Robinson
2019; Pritchett 2014; Andrews, Pritchett & Woolcock 2017). That
literature has emphasized the difficulty of building organizationally
capable states in developing-country contexts. The Chinese case
demonstrates the *opposite* difficulty: how an already-capable
state organizes its mobilization across sectors when a politically
binding campaign instructs it to do so. The state-led
multi-actor coordination regime is empirically distinctive precisely
because most developing states cannot run it — not because they
choose not to, but because the underlying state capacity is missing.
The lesson, modestly, is that the Chinese implementation regime is
not a *model* in the sense of being available for adoption by other
states; it is an *empirical possibility* that should be in the
typology of what state-organized development can look like when the
state is capable, and it should be in the typology because the
typology is otherwise systematically misspecified.

## 6.1 Scope conditions

Two scope conditions need to be stated explicitly. First, the
typology covers *implementation ecologies under documentary record*.
The Chinese yearbook's documentary base is what allows the present
construction; comparable corpora exist for Brazil and the EU but
require domain-specific extraction. Second, the regime label
*state-led multi-actor coordination* is specific to a state that
can simultaneously direct cross-sectoral mobilization and maintain
documentary discipline over it. States that have ambition to direct
but lack the documentary apparatus to record will produce ecologies
that are statistically indistinguishable from fragmented
authoritarianism in any standard text-as-data measurement; the
phenomenon would exist but not be measurable in this way.

## 6.2 Alternative explanations

The reader might offer four alternative readings.

*The recording-bias reading*: diversity rises because the
yearbook's editors broadened what they recorded over time. This is
partly true and is the reason the *log_events* time series shows no
break at the same dates as the *shannon_actor* time series (the
Chow F for log_events is 2.0 at 2013, 0.14 at 2016, and 0.04 at 2020,
all below the critical 4.10 threshold). Volume grows smoothly;
composition shifts discretely. A pure recording-bias story cannot
account for the asymmetric break pattern: it would predict a break
in volume as well, and the data does not show one.

*The political-cycle reading*: the rise and fall of diversity
tracks the 19th Party Congress (2017) and 20th Party Congress (2022),
not the campaign clock. This is consistent with the data — both
sets of dates fall in the window — but the cleaner cut is the
campaign one: the diversity *peak* is at 2020, the campaign's
declared completion, not at the Party Congresses. The political
cycle, in this reading, channels the campaign rather than
overriding it.

*The funding-cycle reading*: diversity follows the rise and fall of
central transfer payments to poverty programs. This is a candidate
hypothesis the present panel cannot adjudicate alone, because the
fiscal time series is recorded outside the yearbook corpus. The
companion paper (Plan B), by linking county-level CATEs to fiscal
disbursement records, will speak to it.

*The selection-into-coverage reading*: the panel is restricted to
provinces and years for which the yearbook recorded events; selection
on the dependent variable could explain the diversity rise. The
panel's structure rules this out at the province level (all thirty
mainland provinces appear in every year), though within-province
selection remains a residual concern that the county-level
companion will need to address.

# 7 Companion: linking ecology to household effects

A companion paper, in preparation (Plan B in the project's working
file), uses these provincial ecologies as second-stage explanatory
variables in a regression of county-level treatment effects estimated
from the China Family Panel Studies (CFPS) seven-wave household
panel (2010–2022). The dissertation pipeline that estimates the
county-level CATEs is in place. Two operations remain: (i) extending
the present standardization from provincial to county granularity,
and (ii) defending the second-stage identification with the
East-West pairing instrument and the Nunn–Puga ruggedness
instrument. The full pre-registration is documented in
`docs/analysis_plan.md`. The expected publication target is
*World Development* or *Journal of Development Economics* (short paper).

## 7.1 What the companion paper expects to find

Four pre-registered hypotheses guide the companion analysis.

*H1 (diversity → welfare)*: counties in provinces with higher Shannon
diversity should show larger absolute treatment effects on log
per-capita income and on the Chaudhuri-style vulnerability index.
The reasoning is that a more plural ecology delivers more
complementary inputs to the household — fund disbursement from
finance, training from universities, market access from SOEs and
private firms, monitoring from people's organizations — and
complementarity produces non-linear welfare returns. Failure to find
this effect would substantially qualify the typology proposed here:
it would suggest that the documented organizational plurality is
ceremonial rather than productive.

*H2 (central-local U)*: the relationship between central-government
share and household effect should be inverted-U-shaped. Low
central-share counties suffer from coordination shortfall; high
central-share counties suffer from local-knowledge shortfall;
medium-share counties combine central resources with local
adaptation. The U-shape, if found, would put empirical content
behind the often-loose idea of "campaign-bureaucracy hybridity."

*H3 (social participation → durability)*: counties with higher
social-organization participation share through the campaign should
exhibit better post-2020 retention of household gains. The reasoning
is that social organizations embed the implementation in
non-state-dependent local networks that survive after central
attention moves. The empirical hurdle is that the social-share
itself is small and declining, so the test will have low statistical
power and a null result will need to be interpreted cautiously.

*H4 (East-West pairing effect)*: counties whose province was paired
with a higher-development East partner under the 2016 pairing list
should show larger treatment effects, conditional on baseline
poverty. This is the cleanest causal hypothesis in the companion
design because the pairing list was determined centrally (1996
establishment with 2016 canonical re-assignment) rather than
through Western local-government selection.

## 7.2 Why the descriptive paper has to come first

There is a tradition in development economics — and one I have
some sympathy for — of skipping straight to the causal estimate and
treating description as a propaedeutic. The present project takes
the opposite view, for two reasons.

First, the second-stage regression in the companion paper has no
meaning if the first-stage *measurement* of organizational ecology
is not well-defined. Shannon entropy on `actor_type` is not a
natural quantity; it is a constructed quantity, and its
construction's substantive interpretation has to be defended
*before* it is used as a regressor. The present paper performs
that defense.

Second, the companion paper's identification depends on the
present paper's typology being right. The East-West pairing
instrument is valid only if East-West pairing is, in fact, an
exogenous assignment of *certain organizational ecologies* to
Western provinces. The cross-tabulation in Section 5.3 (100% of
East-West pairing events are local-government, near-zero in any
other actor type) is what makes the instrument substantively
clean. Without that fact, the IV would be a black-box
instrumentation rather than an identifying argument.

The companion design is what allows the present paper to remain
descriptive and typological without apology. Identification of the
ecology → welfare link is the companion paper's burden; the
present paper's burden is to *make the ecology measurable and
interpretable*.

# 8 Discussion and conclusion

I close with three reflections — one substantive, one
methodological, one positioning.

**Substantive.** The Chinese anti-poverty mobilization, organizationally
read, looks like a state that knows how to recruit. The
diversification of the implementation population through the
2014–2020 window is large (40% in Shannon entropy), real (Chow F =
15.9 at the 2020 break), and asymmetric in its sectoral
composition (universities up, social organizations down, central
share following a clean U-shape). The reading "the Party did it" is
not wrong; it is undersaturated. What the Party did, organizationally,
was *to differentiate and assign entry mechanisms to particular
populations of organizations and to mobilize the resulting ecology
during the campaign window*. The campaign's success metric — zero
absolute poverty — is well-known. The campaign's organizational
metric, until this paper, was not.

**Methodological.** The dataset construction described here is a
demonstrandum that LLM-mediated text-as-data work can be made to
meet the evidence standards of top-tier China-studies journals if
its provenance and prompt-versioning disciplines are sufficiently
strong. The general lesson is replicable: hold the source pages and
the prompt fixed; treat the LLM output as a hypothesis about the
text; insist on a controlled output vocabulary; carry every row's
provenance; allow re-extraction with the same input → same output
property. These are not unique to LLMs — they are the disciplines
of any responsible content-analysis pipeline — but they need to be
stated explicitly because the field is still negotiating standards.

**Positioning.** This paper is the first in a planned three-paper
project that extends Li Cheng's downward-from-the-Politburo method
into the implementation tier. Paper 1 (the present manuscript)
constructs and reads the organizational ecology. Paper 2 (the
companion, Plan B in the working files) connects ecology to
household-welfare outcomes via CFPS-matched CATE estimation. Paper 3
(Plan C in the working files) extends the same extraction-and-coding
pipeline to BRI/GDI-facing Chinese-language documents addressed to
ASEAN partners and asks whether the *state-led multi-actor
coordination* regime travels. Together, the three papers aim to
specify, measure, and trace the Chinese implementation regime as an
empirical phenomenon — neither asserted nor denied but *built*.

## 8.1 Limitations

Three limitations bound the present claims. (i) The corpus is
restricted to a single documentary base; comparisons across
documentary bases (e.g., yearbook vs internal-bulletin vs press
release) would strengthen the inference that the recorded ecology
tracks the operating ecology. (ii) The province-level granularity
is coarse for some downstream questions, especially mediation
questions about how implementation reaches the household; county-
level standardization is the next-step priority and is sketched in
`docs/decisions.md` (entry D-004). (iii) The current extraction
leaves the `actor_gov_level` field empty, so the central/local cut
is derived from `actor_type` only. Re-running the upstream
extraction with a tightened prompt to populate `actor_gov_level`
would improve the *省/市/县/乡* resolution and is on the project
roadmap (Stage 04 of the pipeline).

A fourth limitation is theoretical rather than empirical. The
typology I propose — *state-led multi-actor coordination* — is a
descriptive category derived from one extended case. Comparative
validation will require either replicating the panel construction
in non-Chinese cases (likely difficult given documentary
heterogeneity) or developing a within-China comparative design
that contrasts the poverty-implementation ecology with other
campaign ecologies (anti-corruption, environmental, common
prosperity). A sketch of the latter design is in `docs/analysis_plan.md`
as a candidate Paper 4.

## 8.2 What "Li Cheng / Li Shi-level" means in practice

I conclude with a methodological reflection that may be of interest
to readers building similar datasets. Two contemporary scholars
anchor the analytical bar this paper has tried to reach: Li Cheng
on the Chinese-elite-politics side and Li Shi on the household-
poverty side. The two scholars' methodological signatures are
distinct — Li Cheng's databank discipline (one row per leader, one
row per attribute, follow through time) and Li Shi's CHIP-survey
discipline (one row per household, one row per income source,
follow through waves) — but they share a deeper commitment: *the
empirical thing must be built before the analytical thing can be
said*.

The present paper has tried to take that commitment seriously.
The empirical thing — the province-year organizational-ecology
panel — was built before the analytical claims were written. The
LLM-extraction pipeline was version-controlled. The panel
construction was documented at variable-by-variable granularity.
The decisions log carries every analytic choice. The companion
paper's pre-registration was written before its CFPS-merged data
were available. Whether the analytical claims persuade is a
question for reviewers. That the empirical thing exists, and can
be audited and rebuilt, is the methodological commitment that
this paper aims to demonstrate.

# Acknowledgements

This research will be conducted as part of an application to the
Postdoctoral Fellowship at the Centre on Contemporary China and the
World (CCCW), University of Hong Kong. I gratefully acknowledge
preliminary guidance from Zhang Xiulan (Beijing Normal University),
Robert Walker (Beijing Normal University and Oxford), and the
prospective CCCW research environment under Professor Li Cheng. All
errors are my own. The corpus and extraction pipeline are open
source at the project repository.

# References

*(working list; to be normalized for the journal's style on submission)*

- Carroll, G. R., & Hannan, M. T. (2000). *The Demography of
  Corporations and Industries.* Princeton: Princeton University Press.
- Chaudhuri, S. (2003). Assessing vulnerability to poverty: Concepts,
  empirical methods and illustrative examples. *Mimeo, Department of
  Economics, Columbia University.*
- Edin, M. (2003). State capacity and local agent control in China:
  CCP cadre management from a township perspective. *The China
  Quarterly*, 173, 35–52.
- Grimmer, J., Roberts, M. E., & Stewart, B. M. (2022). *Text as
  Data: A New Framework for Machine Learning and the Social
  Sciences.* Princeton: Princeton University Press.
- Hainmueller, J. (2012). Entropy balancing for causal effects: A
  multivariate reweighting method to produce balanced samples in
  observational studies. *Political Analysis*, 20(1), 25–46.
- Hannan, M. T., & Freeman, J. (1977). The population ecology of
  organizations. *American Journal of Sociology*, 82(5), 929–964.
- Hannan, M. T., & Freeman, J. (1989). *Organizational Ecology.*
  Cambridge, MA: Harvard University Press.
- Heilmann, S., & Perry, E. J. (Eds.). (2011). *Mao's Invisible Hand:
  The Political Foundations of Adaptive Governance in China.*
  Cambridge, MA: Harvard University Asia Center.
- Imai, K., Keele, L., & Yamamoto, T. (2010). Identification,
  inference and sensitivity analysis for causal mediation effects.
  *Statistical Science*, 25(1), 51–71.
- Landry, P. F. (2008). *Decentralized Authoritarianism in China:
  The Communist Party's Control of Local Elites in the Post-Mao Era.*
  Cambridge: Cambridge University Press.
- Li, C. (2001). *China's Leaders: The New Generation.* Lanham:
  Rowman & Littlefield.
- Li, C. (2008). *China's Changing Political Landscape: Prospects for
  Democracy.* Washington: Brookings Institution Press.
- Li, C. (2016). *Chinese Politics in the Xi Jinping Era: Reassessing
  Collective Leadership.* Washington: Brookings Institution Press.
- Li, S., Sato, H., & Sicular, T. (2013). *Rising Inequality in
  China: Challenges to a Harmonious Society.* Cambridge: Cambridge
  University Press.
- Looney, K. E. (2020). *Mobilizing for Development: The Modernization
  of Rural East Asia.* Ithaca: Cornell University Press.
- Lieberthal, K., & Oksenberg, M. (1988). *Policy Making in China:
  Leaders, Structures, and Processes.* Princeton: Princeton
  University Press.
- Marquis, C., & Tilcsik, A. (2013). Imprinting: Toward a multilevel
  theory. *Academy of Management Annals*, 7(1), 195–245.
- Heilmann, S. (2018). *Red Swan: How Unorthodox Policy Making
  Facilitated China's Rise.* Hong Kong: Chinese University Press.
- Hsu, J. Y. J., & Hasmath, R. (2014). The local corporatist
  state and NGO relations in China. *Journal of Contemporary China*,
  23(87), 516–534.
- Pearson, M., Rithmire, M., & Tsai, K. S. (2021). Party-state
  capitalism in China. *Current History*, 120(827), 207–213.
- Perry, E. J. (2017). Cultural governance in contemporary China:
  "Re-orienting" party propaganda. In V. Shue & P. Thornton (eds.),
  *To Govern China*. Cambridge: Cambridge University Press.
- Schneiberg, M. (2002). Organizational heterogeneity and the
  production of new forms: Politics, social movements and mutual
  companies in American fire insurance, 1900–1930. *Research in
  the Sociology of Organizations*, 19, 39–89.
- Skocpol, T. (1992). *Protecting Soldiers and Mothers: The Political
  Origins of Social Policy in the United States.* Cambridge, MA:
  Harvard University Press.
- Spires, A. J. (2011). Contingent symbiosis and civil society in an
  authoritarian state: Understanding the survival of China's
  grassroots NGOs. *American Journal of Sociology*, 117(1), 1–45.
- Wang, S. (2022). The political logic of corruption control in
  China: A study of the campaign-style anti-corruption mechanism.
  *Journal of Contemporary China*, 31(133), 18–35.
- Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor:
  States, Societies, and the Fate of Liberty.* New York: Penguin.
- Andrews, M., Pritchett, L., & Woolcock, M. (2017). *Building
  State Capability: Evidence, Analysis, Action.* Oxford: Oxford
  University Press.
- Banerjee, A., & Duflo, E. (2011). *Poor Economics: A Radical
  Rethinking of the Way to Fight Global Poverty.* New York: PublicAffairs.
- Carroll, G. R. (1985). Concentration and specialization: Dynamics
  of niche width in populations of organizations. *American Journal
  of Sociology*, 90(6), 1262–1283.
- Deaton, A. (2010). Instruments, randomization, and learning about
  development. *Journal of Economic Literature*, 48(2), 424–455.
- Easterly, W. (2006). *The White Man's Burden: Why the West's
  Efforts to Aid the Rest Have Done So Much Ill and So Little Good.*
  New York: Penguin.
- Heckman, J. J. (2020). Randomization in social policy evaluation
  revisited. NBER working paper.
- Pritchett, L. (2014). The risks to education systems from design
  mismatch and global isomorphism. WIDER Working Paper 2014/039.
- Pritchett, L., Woolcock, M., & Andrews, M. (2010). Capability
  traps? The mechanisms of persistent implementation failure.
  Center for Global Development Working Paper 234.
- Whetten, D. A., & Bozeman, B. (1991). Organization theory and
  the public sector. *Journal of Management*, 17(2), 397–410.
- Nunn, N., & Puga, D. (2012). Ruggedness: The blessing of bad
  geography in Africa. *Review of Economics and Statistics*, 94(1),
  20–36.
- Ornstein, J. T., Blasingame, E. N., & Truscott, J. S. (2024). How
  to train your stochastic parrot: Large language models for
  political texts. *Political Science Research and Methods*.
- Shih, V., Adolph, C., & Liu, M. (2012). Getting ahead in the
  Communist Party: Explaining the advancement of central committee
  members in China. *American Political Science Review*, 106(1),
  166–187.
- Stinchcombe, A. L. (1965). Social structure and organizations.
  In J. G. March (Ed.), *Handbook of Organizations.* Chicago: Rand
  McNally.
- Xu, M., et al. (2022). Poor and lazy: Middle-class stigma against
  the poor in China. *Journal of Contemporary China.*

# Appendix A — Variable definitions

See `docs/codebook.md` in the project repository.

# Appendix B — Robustness battery (planned)

See `docs/analysis_plan.md` §5.

# Appendix C — Replication

All code and intermediate data are versioned in the project
repository at `posdocApplyResearch/projects/planB_household_link/`.
The pipeline runs end-to-end from `output_v3/research.db`:

```bash
python code/01_standardize_region.py
python code/02_province_ecology_panel.py
python code/03_figures_province.py
python code/04_structural_break_and_correspondence.py
```

Total runtime < 30 seconds on a 2024 MacBook Pro. Random seed:
`20260531`.
