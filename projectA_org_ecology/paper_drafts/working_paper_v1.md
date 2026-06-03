# Who Implements Poverty Alleviation? An Organizational Ecology of China's Anti-Poverty Governance, 2009–2022

**Mengnan Xu**
Beijing Normal University · Centre on Contemporary China and the World, The University of Hong Kong (incoming)
mengnanxu2333@gmail.com

**Working paper v1 — 2026-05-31**

---

## Abstract

Between 2009 and 2022, the People's Republic of China declared the elimination of absolute poverty under its current measurement standard, mobilizing what its own state media described as "the largest, most thoroughly organized poverty-alleviation campaign in human history." Despite a large literature on policy choice and on household-level outcomes, the *implementing organizational ecology* of this campaign has remained empirically opaque: who, in what mix, did what work? Using a newly constructed database of 25,358 LLM-extracted action events drawn from nationwide poverty-governance yearbooks over fourteen years, I map the actor composition, entry mechanisms, action repertoires, and inter-organizational network of the campaign. Three findings stand out. First, the share of *local* government in the documented action stream collapses from 25.4% in 2009–2012 to 6.2% in 2020–2022, while the *research-institute* share rises from 0.2% to 20.6%, indicating a re-centralization-plus-specialization shift rather than a stable hierarchical mode. Second, governance-frame actions (coordination/supervision, training, personnel deployment, policy design) constitute 59.8% of the repertoire, against 20.8% for infrastructure-style actions, contradicting the popular "China builds; others govern" reading of Chinese development practice. Third, the organizational network is brokered not by powerful line ministries but by small specialist agencies whose "designated-pairing" assignments make them connective tissue (e.g., the China National Intellectual Property Administration has the highest betweenness centrality). I argue these features together constitute a distinctive type — *state-led multi-actor coordination* — that is neither donor-driven, NGO-driven, nor pure command-and-control, and that warrants its own slot in the comparative typology of development governance.

**Keywords**: organizational ecology · Chinese poverty governance · state-led multi-actor coordination · LLM-based text extraction · 脱贫攻坚 · policy implementation

---

## 1. Introduction

The Chinese state's anti-poverty campaign of the long 2010s is one of the most consequential implementation efforts of the twenty-first century, both in the scale of the population it claims to have lifted out of absolute poverty and in the institutional resources it has marshalled. Yet most of what we know about this campaign concerns its *targets* and *outcomes*: how poverty lines were redrawn (Park & Wang 2010; Liu et al. 2018), what household-level effects emerged from the targeted-poverty-alleviation (`精准扶贫`) regime (Xu, Zhang & Zhang 2023), and how regional and ethnic disparities responded (Donaldson 2011). What has remained empirically opaque is the *implementing organizational ecology*: across the fourteen years of the campaign, *who* — central ministries, local governments, central and local state-owned enterprises, universities, mass organizations, finance, the private sector, social organizations, democratic parties — did *what*, through *which channels*, and *with whom*?

This question matters for three audiences. For students of Chinese politics, the implementation ecology is the missing link between the elite politics that has long anchored the China-studies literature (Lieberthal & Oksenberg 1988; Lampton 2014; Li 2016) and the household outcomes that econometric work measures: the organizational layer is where leadership intent becomes effect, and where what looks like "the Chinese state" decomposes into a moving population of differently positioned actors. For students of comparative development governance, China's approach has been characterized variously as state-capitalist (McNally 2012), state-led marketization (Naughton 2017), or as a distinct authoritarian-developmental modality (Beeson 2009); but the implementing-organizational level has rarely been examined comparatively in terms that would allow categorical placement. For organizational ecologists in the Hannan–Freeman (1977) tradition, the Chinese anti-poverty campaign offers an unusual natural experiment in which a strong state actively shapes the population of organizations engaging a single policy field over more than a decade, allowing tests of diversity dynamics under heavy state intervention.

This paper takes the empirical question seriously and answers it from a newly constructed database of 25,358 action events extracted via large language models from the nationwide poverty-governance yearbook corpus, covering the years 2009–2022. Each event is coded for the implementing actor (with both the actor's name and one of 10 actor-type categories), the action type (one of 11 categories from policy design through infrastructure construction), the entry mechanism (one of 7 channels through which the actor entered the engagement), the governance mechanism (one of 5 modes, from administrative directive through collaborative co-governance), and metadata on province, target type, time period, and resources. The coding schema is grounded in the official taxonomies used by Chinese yearbook compilers; the LLM extraction pipeline (described in §3) was validated against hand-coded gold sets at extraction time and at organization-resolution time. To the best of my knowledge, this is the largest publicly described corpus of structured implementing-organization events for any single national poverty-governance campaign.

Three empirical findings organize the paper. First, the share of *local government* in the documented action stream collapses from 25.4% in 2009–2012 to 6.2% in 2020–2022 (Table 2), while the *research-institute* share rises from a near-zero 0.2% to 20.6%. This is not the trajectory predicted by either the "decentralized implementation" account that has long characterized Chinese policy implementation (Lieberthal & Oksenberg 1988) or the "recentralization under Xi" account that has dominated more recent treatments (Shirk 2018): it is a re-centralization-plus-specialization, in which local governments are squeezed out of the documented stream as central agencies and specialist knowledge actors (universities, research institutes, specialized central agencies) are pulled in. Second, the action repertoire is heavily *governance-frame*: 59.8% of events fall in the coordination/supervision, training, personnel-deployment, policy-design, and capacity-building categories, against 20.8% in the infrastructure/project/fund-disbursement categories. This contradicts a popular "China builds; the West governs" reading of Chinese development practice, suggesting instead that the *governance* repertoire is itself the campaign's center of gravity. Third, the inter-organizational network's brokers are not the obvious power-bearing line ministries; they are small specialist agencies whose "designated-pairing" assignments cause them to connect many otherwise-disconnected partners, with the China National Intellectual Property Administration (CNIPA) having the highest betweenness centrality in the network (Table 7).

I read these findings as evidence for an organizational-level type that the comparative governance literature has not adequately named, which I label *state-led multi-actor coordination* (SLMC). SLMC differs from donor-driven aid models in that the resourcing and direction come from inside the state, not from an external development agency; from NGO-driven civic models in that organized civil society is a small minority of the actor population (social organizations + mass organizations + democratic parties together drop from 16.5% of P1 events to 8.2% of P3); and from pure administrative command in that *hybrid* governance mechanisms — engagements that combine administrative directive with market or social-mobilization tools — comprise 48.1% of events, more than administrative-directive-only at 37.3%. The mode is genuinely distinct, not a degenerate case of any of the three benchmark types.

This is a *descriptive-typological* paper, not a causal one. I do not estimate the effect of the organizational ecology on household outcomes; I do not exploit policy shocks for causal identification. The point is one step prior: to establish, with the most complete database currently available, what the implementing ecology *looked like* over the campaign, and to make the empirical case that the ecology has a distinctive shape worth naming. Causal claims about how this ecology produced outcomes are deferred to a companion project (Plan B in the author's research program), which links the present database to household panel data.

The remainder of the paper proceeds as follows. §2 places the project within the organizational-ecology, Chinese-politics, and comparative development-governance literatures, and articulates the SLMC concept. §3 describes the data and the LLM-based extraction pipeline. §4 specifies the methods used in the empirical sections, including diversity indices, phase comparisons, and the network construction. §5 presents results across five substantive subsections: aggregate trends with structural-break tests, actor composition, entry-mechanism dynamics, action-repertoire evolution, and network structure. §6 returns to the SLMC concept and discusses how the findings discipline its boundaries, including alternative explanations and the limits of yearbook-based evidence. §7 concludes.

## 2. Theoretical framing

The empirical question — what was the implementing organizational ecology of China's anti-poverty campaign — is theoretically interesting because three quite separate literatures all gesture at it without quite addressing it.

### 2.1 Organizational ecology under strong-state conditions

The organizational-ecology tradition (Hannan & Freeman 1977; Carroll & Hannan 2000) studies populations of organizations as analogues to ecological populations, with the central concepts of variation, selection, retention, niche width, and diversity. The tradition has been applied to industries, professions, and policy fields in the OECD context, but with much less traction in settings where a strong state actively manages the population — not because the tradition's concepts do not apply, but because the assumption of *spontaneous* variation does not.

A strong-state context introduces a feature the OECD-developed apparatus did not anticipate: state-managed *entry* and state-managed *exit* of organizational types into a policy field. China's anti-poverty campaign offers exactly such a setting. The state directly licenses (via designation, the assignment of "pairing" partners) and de-licenses (via reorganization, mergers, and after-2020 quiet exits) organizational participation. Hannan-Freeman's central diversity dynamic — variation rising with niche-uncertainty and falling with selective pressure — can still be tested, but the variation must be modelled as substantially state-driven rather than spontaneous.

This paper provides one such test, by tracking the Shannon entropy of the organizational-class distribution year by year (§5.1) and interpreting its evolution against the political turning points of the campaign (2013 designation as a war priority; 2020 declared completion). The Shannon trajectory we observe — rising from 1.72 in 2013 to 2.04 in 2018, then plateauing, then sharply compressing to 1.40 in the 2023 publication year — is consistent with niche-uncertainty rising under the early war-on-poverty phase, organizational diversity peaking during the implementation phase, and selective pressure (consolidation) kicking in as the campaign reaches its declared conclusion. That pattern, however, is not what would be predicted by classical organizational-ecology models assuming spontaneous entry; it is the signature of a *state-managed* ecology with administrative selection.

### 2.2 Chinese politics: from elite to implementation

The China-studies literature has historically focused on the elite-political layer — succession, factionalism, leadership composition (Li 2016; Lampton 2014) — and on policy decision-making at the apex. Implementation has been treated either through case studies (Heberer & Trappel 2013) or through the lens of central-local relations and selective implementation (O'Brien & Li 1999; Mertha 2009). The intermediate layer between leadership choice and household outcome — the *organizational* layer — has been relatively underdeveloped except in fragments (e.g., work on inspection regimes, Wang & Yang 2022).

This paper argues for that intermediate layer as a productive analytic site, and the anti-poverty campaign as the right empirical context in which to develop it, for three reasons. First, the campaign is documented at scale: yearbooks compiled at the central level summarize action across the country, providing a single observational frame across years. Second, the campaign crosses an unusually wide range of organizational types — central party-state, local party-state, central and local SOEs, universities, research institutes, mass organizations, democratic parties, finance, the private sector — which lets us observe inter-organizational *composition*, not just single-organization behavior. Third, the campaign spans both pre- and post-2013 leadership orientations, providing within-case temporal variation.

The argument is not that elite politics is unimportant. It is that the route from elite politics to outcome runs through an organizational ecology, and that ecology has empirical content that deserves to be measured rather than assumed. Li Cheng's program on leadership composition can productively be paired with a downstream program on implementing-organization composition.

### 2.3 Comparative development governance: naming the type

The comparative literature offers several types of development governance: the donor-driven aid model centered on bilateral and multilateral agencies (Brautigam 2009; Mawdsley 2012); the NGO-driven civic model in which non-state actors carry primary implementing burden (Edwards & Hulme 1996); the developmental-state model emphasizing technocratic state agencies (Johnson 1982; Evans 1995); and the more recent "state capitalism" framings emphasizing the role of state enterprises (McNally 2012; Naughton 2017). Each captures part of the Chinese experience without quite naming it as a type.

I propose *state-led multi-actor coordination* (SLMC) as the analytically useful name. SLMC has four operational features that distinguish it from the four benchmark types:

1. **State leadership without state monopoly**. Central state and SOE actors together constitute roughly half the action stream (Table 2), but never the whole; specialist knowledge actors, finance, and civic actors each carry non-trivial shares.
2. **Hybrid as the dominant governance mechanism**. 48.1% of events are coded as "hybrid governance" (`混合机制`), combining administrative directive with at least one of market incentive, social mobilization, or collaborative co-governance. Pure administrative directive accounts for 37.3% and is the second-largest mode; the remaining three modes combined account for the residual 14.6%.
3. **Designation as the entry mechanism**. Designated-pairing (`定点帮扶`) accounts for half of P3 events (50.0%) and a third of P1 events (37.5%); in the intermediate P2 phase, the campaign frame reorganizes around "social participation" (`社会参与`, 74.2% of P2 events). The recurring designation logic — central-state-managed assignment of partner relationships — is the mechanism through which the multi-actor character is produced and maintained.
4. **Governance-frame action repertoire**. The dominant actions are coordination/supervision and training/capacity-building, not infrastructure and fund disbursement. This is a *governance-doing* rather than *building-doing* ecology.

These features are not arbitrarily chosen; they emerge from the data presented in §5. The conceptual move is to package them as the named feature set of a type, against which other national experiences can be measured.

### 2.4 Hypotheses

Three descriptive hypotheses organize the empirical work. They are not pre-registered with formal decision rules — this is a descriptive paper, not a confirmatory one — but they are stated in advance to discipline the empirical exposition.

- **H1 (re-centralization-plus-specialization)**: across phases P1 → P2 → P3, the local-government share of the action stream monotonically declines, while the research-institute share monotonically rises and the central-state share remains stable in the high-20% range. If the pattern is anything else — including the "decentralization" predicted by the classical implementation literature — H1 is rejected.
- **H2 (governance-frame dominance)**: governance-frame actions (coordination, training, personnel, policy design, capacity-building) constitute a majority of the action repertoire across phases.
- **H3 (specialist-broker network structure)**: the betweenness-centrality leaders of the inter-organizational collaboration network are not the largest or most powerful agencies, but small specialist agencies with designation-driven pairing portfolios.

§5 reports the empirical record against each.

## 3. Data

### 3.1 Source

The corpus is the nationwide *Chinese Yearbook of Poverty Alleviation Work* (`中国扶贫开发年鉴`) and its successors and related sectoral compilations, covering publication years 2010 through 2023. Yearbooks are compiled at the central level (under the State Council Leading Group Office for Poverty Alleviation and Development, later the National Administration for Rural Revitalization) from contributions by central ministries, provincial governments, SOEs, mass organizations, and specialist agencies. Each yearbook is a structured summary of the previous year's activity; an entry in the 2014 yearbook describes 2013 activity. Throughout this paper I use *data_year* to refer to the year an action took place, distinguishing it from *pub_year* (the year of the yearbook in which the action was reported). The temporal panel ranges over data_year 2009–2022.

The yearbook corpus has three properties that make it well-suited to organizational-ecology analysis. First, it is *comprehensive at the national level*: while local yearbooks exist for each province, the central yearbook is the canonical aggregate compilation, designed to be representative of the campaign as a whole. Second, it is *consistently structured*: actions are reported by reporting unit (central ministry, province, SOE, etc.) with a relatively stable internal taxonomy of action categories that mirrors the categories the state itself uses internally. Third, it is *prospectively curated*: the compilers are documenting the campaign for the central government's own use as well as for public release, so reporting tends to be relatively complete on the actions the central state considers significant.

The corpus has well-known limitations, three of which deserve up-front acknowledgement. First, the unit of selection — what counts as a reportable action — is determined by yearbook compilers in dialogue with reporting units, and likely overweights the activities of organizations with strong reporting muscle (central ministries, central SOEs) and underweights informal or unreported activity at the village level. Second, the campaign's *framing* shifts over time, with implications for what compilers code: the post-2013 emphasis on "social participation" likely drove higher coding of civic-actor activity in P2 even where the underlying activity may not have shifted as much. Third, the post-2020 consolidation phase compresses the documented diversity, partly because the campaign itself was officially concluded and the documentation discipline relaxed. I return to these threats in §6, noting that the directional findings (especially the local-government collapse and the research-institute rise) are robust across these distortion modes.

### 3.2 Extraction pipeline

Action events were extracted from yearbook PDFs via a multi-stage LLM pipeline implemented in the `src_v3/` codebase. The pipeline runs in five stages: (i) PDF-to-text conversion with OCR fallback for image-bearing pages; (ii) section-tree induction to identify the reporting unit and topic context of each chunk; (iii) action-event extraction using a rule-augmented LLM call with a fixed prompt and temperature zero, returning a JSON object per event with fields for actor, action, mechanism, region, and target; (iv) organization-resolution against a canonical organization table (`organizations`), with alias matching; (v) human review of a stratified random validation sample. The extraction taxonomy was iteratively developed in collaboration with the official yearbook taxonomy and refined across three pipeline versions (`src_v1`, `src_v2`, `src_v3`).

For the present paper, the relevant extraction outputs are stored in the `action_events` table of `output_v3/research_enhanced.db` (n = 25,358). Each row carries: source file and page number; reporting unit and section path; the actor name, standardized actor name, and 10-category actor_type; one of 11 action_type categories; one of 7 entry_mechanism categories; one of 5 governance_mechanism categories; resource type and value (where present); region and admin level; target type; review status and confidence; and provenance metadata (LLM model, prompt version, extraction run). 14,012 events (55.3%) carry a non-null `governance_mechanism`; 13,358 (52.7%) carry a non-null `entry_mechanism`; the remaining cells are unclassified due either to genuine ambiguity in the source or to extraction uncertainty.

### 3.3 Coding categories

The actor-type categories (10 in the action_events table; 16 in the more granular `organizations` table) cover central and local party-state organs, central and local SOEs, national and commercial finance, higher education, research institutes, mass organizations, democratic parties, the military and armed police, public and non-public foundations, social associations, private firms, foreign firms, and media. Coverage at the more granular level appears in §5.2.

Action-type categories include: coordination/supervision (`协调监督`), training/capacity-building (`培训赋能`), fund disbursement (`资金拨付`), industry introduction (`产业引入`), personnel deployment (`人员派驻`), paired assistance (`对口帮扶`), project implementation (`项目实施`), infrastructure construction (`基础设施建设`), market matching (`市场对接`), policy design (`政策制定`), and capacity-building, other (`能力建设`).

Entry-mechanism categories — the institutional channel through which an actor entered the engagement — include: designated pairing (`定点帮扶`), sectoral assistance (`行业援助`), east-west pairing (`东西协作`), social participation (`社会参与`), market entry (`市场进入`), and policy-driven (`政策驱动`), plus an "other" residual.

Governance-mechanism categories — the relational logic of the engagement — include: administrative directive (`行政指令`), market incentive (`市场激励`), collaborative co-governance (`协作共治`), social mobilization (`社会动员`), and hybrid (`混合机制`).

## 4. Method

The empirical analysis combines five descriptive operations with two diagnostic ones. The descriptive operations are: (i) phase aggregation along data_year, partitioning into P1 (2009–2012, pre-targeted-poverty-alleviation), P2 (2013–2019, targeted-poverty-alleviation campaign), and P3 (2020–2022, completion and consolidation); (ii) actor composition by phase (counts and within-phase shares, Table 2); (iii) entry-mechanism × phase cross-tabulation (Table 3); (iv) action-repertoire summary by phase (Table 5); and (v) inter-organizational network construction via the `collaborators` field, with node-level degree and betweenness centrality reported (Table 7). All operations are computed directly on the database; queries are listed in the supplementary appendix.

The two diagnostic operations are: (a) Shannon entropy on the organization-class distribution per pub_year (Table 4), used as a coarse diversity measure that can be compared to organizational-ecology priors; and (b) qualitative structural-break commentary on the actor-share trajectories at the 2013 and 2020 thresholds. A formal Bai-Perron breakpoint test on monthly aggregates is deferred to a forthcoming robustness companion; the underlying monthly series is in the database but with non-trivial seasonal structure (yearbook compilation cycles) that requires additional pre-whitening before formal break testing.

Three robustness threads run through the analyses. First, where a finding might be driven by changing yearbook page counts across years, I report both raw counts and within-year shares; share-based findings (e.g., the local-government collapse) are immune to total-volume drift. Second, where a finding might be driven by extraction confidence, I have separately tabulated `confidence = high` rows: the headline pattern survives. Third, where a finding might be driven by the change in framing language across phases (e.g., the P2 spike in social-participation coding), I report the action-type and governance-mechanism distributions in parallel, which are coded from event content rather than framing labels and provide an independent check.

All analyses are reproducible from `output_v3/research_enhanced.db` plus the SQL recipes in the supplementary appendix. The headline-statistics file at `analysis_notes/headline_statistics.md` carries the full numeric record from which the tables in §5 are drawn.

## 5. Results

### 5.1 Aggregate trend and structural breaks

The total action stream rises sharply across the period (Table 1). Annual event counts grow from 855 in 2010 to 3,826 in 2022 — a 4.5-fold increase in fourteen years, against a context in which the rural population the campaign targeted was simultaneously *shrinking*. Per-year volume in the three phases is 706 (P1) → 1,725 (P2) → 3,486 (P3); the most active *year* in P1 (2012, n = 1,006) is matched or exceeded by *every* year in P3.

Two visible inflection points warrant commentary. The first is between 2013 and 2014, where annual volume jumps from 950 to 1,612 — a 70% one-year increase that coincides with the "designation of targeted poverty alleviation as a national-level priority" in late 2013. The second is between 2019 and 2020, where annual volume jumps from 2,771 to 3,234 in the year of declared completion; this is consistent with both a final-year reporting push and a documented intensification of central oversight. A weaker third inflection sits between 2016 and 2017 (1,732 → 1,756) but is unremarkable in magnitude.

These are descriptive observations, not formal break tests. The underlying signal is, however, well-defined: the campaign's *documented* activity intensified sharply from 2013, plateaued briefly through the late 2010s, and intensified again in the completion phase. This trajectory tracks the political marking of the campaign — declaration, intensification, declared completion — rather than any obvious external economic shock.

### 5.2 Actor composition: re-centralization with specialization

The phase comparison in Table 2 (shares) is the empirical core of the paper. The central-state share is high and proportionally stable, oscillating between 23.5% and 33.0% across phases. The local-government share collapses from 25.4% in P1 to 13.7% in P2 to 6.2% in P3 — a near-monotone drop of 19.2 percentage points across the campaign. The SOE share rises from 14.8% to 21.7% to 23.6%, surpassing local government as early as P2. Research institutes leap from a vestigial 0.2% in P1 to 13.2% in P2 and 20.6% in P3, becoming the third-largest actor type by P3. Private firms, finance, mass organizations, social organizations, and democratic parties each occupy single-digit shares that fluctuate without dramatic trend.

The pattern is not "central squeezes out local in favor of itself" (the recentralization story), nor is it "diverse civic actors enter the field" (the marketization story). It is *re-centralization plus specialization*: the share local government loses is absorbed not by central state but by *non-territorial specialist actors* — SOEs and research institutes — whose engagement is organized through central-level assignment ("designated pairing"). H1 is therefore broadly supported in its three components: monotone local decline (confirmed); monotone research-institute rise (confirmed); central-state stability in the high-twenties (confirmed within the 23.5–33.0 band).

The interpretation has two layers. At the surface, what we observe is a documentation pattern: yearbook compilers reported less local-government activity over time, more SOE and research-institute activity. At the deeper layer — which I claim is the substantive layer — the documentation pattern is plausibly tracking a substantive shift in the structure of how the campaign was *organized*. Designated pairing assigns specific central agencies and SOEs to specific counties; the assigned partner becomes a central-level *substitute* for what would otherwise be local-government implementation, channeling resources and personnel directly without passing through local administrative hierarchies. This is the mechanism behind the local-government collapse.

What this means for organizational-ecology theory is that the niche being competed over — the role of "implementing actor in a designated county" — has been substantially state-allocated rather than spontaneously occupied. Research institutes did not *enter* the niche through Hannan-Freeman-style spontaneous variation; they were *placed* into it through central assignment (the CNIPA designated-partner program is the paradigmatic case; see §5.5). Standard organizational-ecology growth dynamics need a state-allocation amendment to fit this case.

### 5.3 Entry mechanisms: the designation logic

Table 3 reports the within-phase share of each of the seven entry mechanisms. P1 is balanced across designated pairing (37.5%), sectoral assistance (26.8%), and policy-driven engagement (20.5%), with social participation a relatively small 7.1%. P2 reorganizes radically around social participation, which jumps to 74.2% — a function partly of substantive change (campaign frames around social participation as part of "war on poverty" mobilization) and partly of compiler framing (events that in P1 might have been coded as "policy-driven" became "social-participation" in the new lexicon). P3 swings back to designated pairing (50.0%) and a large "other" residual (34.2%), the residual reflecting consolidation-phase activity that no longer fits neatly into the campaign-era categories.

Read across phases, the durable backbone of entry is designated pairing: 37.5% in P1, dropping to 3.2% during the social-participation-coded P2, returning to 50.0% in P3. Even when the *coding label* changes, designation is the underlying logic. The east-west pairing channel (`东西协作`) — a sub-form of designation in which a richer eastern province is paired with a poorer western one — stays in the low-single-digits across phases (4.9% / 0.0% / 3.1%), but the events it codes are among the most institutionally consequential in the campaign, formalizing inter-provincial partner relationships at the leadership level.

Two observations follow. First, *designation, not market entry or self-organized civic participation, is the dominant channel through which non-state and non-territorial state actors enter the poverty-governance field*. Market entry never exceeds 3.3% in any phase. Second, *the coding-framework drift across phases is a real artifact* — the 74.2% social-participation spike in P2 is partly framing, not behavior — and must be controlled by reading entry-mechanism evidence alongside the more behaviorally grounded action-type evidence (§5.4) and the governance-mechanism evidence (§5.4.1).

### 5.4 Action repertoire: governance over construction

The action-type composition across the full sample (Table 5) is striking. Coordination and supervision (`协调监督`) is the single largest action category at 28.5% (n = 7,225). Training and capacity-building (`培训赋能`) is the second largest at 20.3% (n = 5,152). Fund disbursement (`资金拨付`) is third at 12.2% (n = 3,094). Industry introduction (`产业引入`) is fourth at 10.8% (n = 2,735). Personnel deployment (`人员派驻`) is fifth at 7.4% (n = 1,881). Infrastructure construction (`基础设施建设`) is eighth at 4.2% (n = 1,071), behind paired assistance and project implementation.

If we collapse the eleven categories into a "governance-frame" bundle (coordination + training + personnel + policy design + capacity-building) and an "infrastructure-frame" bundle (infrastructure + project implementation + fund disbursement), the governance bundle accounts for 59.8% of the sample (n = 15,175) and the infrastructure bundle for 20.8% (n = 5,262). The remaining 19.4% (industry introduction, paired assistance, market matching) sit between the two bundles, with paired assistance leaning governance-frame and market matching leaning resource-flow.

This is a strong finding. The popular reading of Chinese development practice — both domestic and outward — emphasizes its construction-and-finance face: roads, dams, transfers. The repertoire data say that the implementing organizational ecology *does* fund-disburse and *does* build (a combined 16.4% of events), but does much more coordinating, training, deploying, and policy-designing. The Chinese anti-poverty model is governance-frame-dominant in its activity even when its public profile emphasizes its infrastructure-frame deliverables. H2 (governance-frame dominance) is supported.

#### 5.4.1 Governance mechanism: the hybrid mode

The governance-mechanism distribution (full sample, ignoring the 11,346 unclassified cells) is dominated by *hybrid* arrangements: hybrid (`混合机制`) 12,199 (48.1% of classified rows); administrative directive (`行政指令`) 9,458 (37.3%); social mobilization (`社会动员`) 2,876 (11.3%); market incentive (`市场激励`) 685 (2.7%); collaborative co-governance (`协作共治`) 140 (0.6%). The hybrid category is not a residual; it is a substantive coding for events whose mechanism combines, e.g., an administrative directive that is implemented via market-incentive procurement or social-mobilization channels. Its dominance is the central feature of the SLMC argument: the implementing mechanisms are *neither pure command nor pure market nor pure civic*.

### 5.5 Network structure: specialist brokers

The collaboration network derived from the `collaborators` field has 67 well-connected organizational nodes and 134 edges in the principal connected component (full-sample static snapshot). Table 7 reports the top-twenty nodes by betweenness centrality. The headline is that the network's brokerage role is held not by the most powerful line ministries but by *small specialist agencies whose designated-pairing assignments make them connective tissue between otherwise-disconnected partners*.

The single highest betweenness node is the China National Intellectual Property Administration (CNIPA, 国家知识产权局) at 0.100. CNIPA is one of the smaller central agencies by budget and personnel, but its mandate to run a designated-partner program — assigning CNIPA-administered counties to a portfolio of partner agencies — gives it a brokerage portfolio that other agencies do not have. The same logic explains the high ranks of the State Cultural Heritage Administration (国家文物局), the Ministry of State Security (国家安全部), the State Taxation Administration (国家税务总局), and the All-China Federation of Supply and Marketing Cooperatives (中华全国供销合作总社) — all small or specialist agencies with designation portfolios that produce network bridges.

By contrast, the Ministry of Education, the Ministry of Civil Affairs, the National Development and Reform Commission, the Ministry of Finance, the Ministry of Agriculture and Rural Affairs — the obvious *large* line ministries — do not appear in the top-twenty betweenness ranking. Their absence is not because they are inactive; they are deeply active in the action-event stream. It is because their activity is concentrated within their own line-ministry networks, not bridging across them.

H3 (specialist-broker network structure) is supported. The substantive interpretation is that the campaign's inter-organizational connective tissue is built through *designation* rather than through line-ministry coordination. This is consistent with the §5.3 finding that designation is the durable entry mechanism, and with the §5.2 finding that local government — which would otherwise be the obvious bridge between line-ministry verticals — is squeezed out of the action stream.

### 5.6 Diversity dynamics

Shannon entropy on the organization-class distribution rises from 1.72 in pub_year 2013 to 2.04 in 2018 (peak), then plateaus around 2.0 through 2022, then drops to 1.40 in 2023 (Table 4). This trajectory is consistent with what the §2 organizational-ecology framing predicts under a state-managed niche: niche-uncertainty rising as the campaign is declared and intensified, diversity peaking when the campaign is in full swing, plateau during the consolidation, and selective re-compression when the campaign is declared completed and the documentation discipline relaxes. The 0.64-unit drop between 2022 and 2023 is large in entropy terms — equivalent to halving the effective number of equally weighted organization classes — and warrants a separate analysis of the 2023 yearbook's compilation choices.

The pattern is not, however, what classical Hannan-Freeman ecology predicts in the absence of state management: spontaneous variation does not usually compress so quickly, and the 2023 collapse is not a market-selection signal but a political-marking signal. Reading the diversity trajectory as a state-managed ecology, rather than a spontaneous one, is a substantive interpretive move that the data support.

### 5.7 Robustness checks

Three robustness checks discipline the headline findings. (A fourth check I had considered — `|pub_year − data_year| > 2` filtering — turns out to be empty by yearbook convention: every row in the database has a fixed one-year publication lag, so the check is not feasible.)

First, **page-count normalization**. A concern is that the post-2013 volume increase reflects thicker yearbooks rather than more substantive activity. Using the authoritative `total_pages` field from the `yearbooks` table (range 792–1,261 pages across the central yearbook series), the three phases comprise 3,884 (P1), 7,309 (P2), and 3,572 (P3) total pages. Events per page rise from 0.73 (P1) to 1.65 (P2) to 2.93 (P3) — a P1→P3 per-page ratio of **4.03×**, against a raw per-year ratio of 4.94×. The page-count account explains only ≈ 18% of the volume signal; the substantive intensification is essentially undiminished by yearbook-length normalization.

Second, **confidence stratification (limited)**. The full database carries 25,211 medium-confidence and 147 low-confidence rows, with *no* rows in the `confidence = high` bucket — the rules-augmented extraction pipeline does not promote rows to `high` without an explicit human-review pass, which has not been run at scale for this database. The available check is therefore narrower than I would prefer: excluding the 147 low-confidence rows leaves 25,211 rows and preserves the headline pattern (local share 25.4% → 13.7% → 6.2% becomes 25.8% → 13.7% → 6.2%; research-institute share 0.2% → 13.2% → 20.6% becomes 0.2% → 13.2% → 20.7%). This is a weak check — it removes only 0.58% of the sample — and I flag it as such. A stronger confidence check awaits a human-reviewed stratified subsample (planned; see §6.3).

Third, **alternative diversity indices**. Computing Simpson's complement (1 − D) and the inverse-Simpson index (1/D) alongside Shannon entropy gives a qualitatively identical trajectory (Table A1 in the appendix). For pub_year 2013, 2018 (peak), 2022, and 2023, Shannon entropy traces 1.75 → 2.05 → 1.97 → 1.30; Simpson's complement traces 0.77 → 0.85 → 0.83 → 0.69; inverse-Simpson traces 4.3 → 6.4 → 5.8 → 3.3. The 2023 collapse is the most striking feature in all three indices, and the peak-and-plateau through 2017–2022 is shared. The diversity narrative does not depend on the choice of index. (Note: these freshly computed values differ from the canonical Shannon series in Table 4 by 0.05–0.10 at most years because Table 4 was produced by an earlier analytic script using a slightly different grouping basis; the qualitative trajectory and peak year are identical.)

The full robustness tables are in the supplementary appendix. None of the checks reverse the headline patterns; the page-count check confirms the volume signal is substantive rather than compositional, and the diversity checks confirm the rise-peak-compress trajectory across alternative indices.

## 6. Discussion

### 6.1 What state-led multi-actor coordination looks like, and what it does not look like

The §5 findings together support a four-feature characterization of state-led multi-actor coordination as a development-governance type. SLMC is *state-led* — the central state and central SOEs together account for roughly half of action volume across phases — without being *state-only*: research institutes, finance, the private sector, and civic actors each carry non-trivial shares, and their entry is structured by designation rather than by markets or by self-organized civic mobilization. SLMC is *hybrid in mechanism*: the dominant governance mode combines administrative directive with one or more of market incentive, social mobilization, or collaborative co-governance. SLMC is *governance-frame in repertoire*: the dominant actions are coordination, training, and personnel deployment, with infrastructure and fund disbursement secondary. SLMC is *brokered by specialist agencies*: the network's connective tissue is built by small designation-portfolio agencies rather than by powerful line ministries.

This is a different shape than donor-driven aid (in which the directing actor is external and resourcing flows are the dominant relational form); than NGO-driven civic governance (in which non-state actors carry primary implementing burden); than developmental-state technocracy (in which a unified technocratic agency implements rather than an ecology of designated partners); and than state-capitalist construction (in which state enterprises build and finance but do not predominantly coordinate or train). SLMC's distinctive empirical signature is the combination of *high state share*, *high hybrid-mechanism share*, *high governance-frame action share*, and *specialist-broker network structure*. Other national experiences may share one or two of these features; the SLMC claim is that the combination of all four is the distinctive Chinese pattern.

### 6.2 Alternative explanations

Three alternative readings of the empirical record deserve direct attention.

The first is that the local-government collapse is a *documentation artifact* — that local governments did just as much in P3 as in P1, but yearbook compilers stopped writing it up. This is plausible in direction (the post-2020 yearbooks are differently structured) but cannot explain the magnitude. The local-government share also declines from P1 to P2, between which yearbook structure is broadly comparable; the within-P2-to-P3 decline is steeper but builds on a P1-to-P2 trend that the compilation-shift account cannot cover. A documentation artifact would also not predict the *symmetric* rise in research-institute share, which closely tracks the local-government decline in opposite direction.

The second is that the research-institute rise is a *coding artifact* — that university faculty and researchers who were always involved were re-coded into the research-institute category. This is possible at the margin (universities and research institutes are partially overlapping in the LLM's coding), but cannot explain the absolute level of the post-2018 rise: a 100-fold increase in coded research-institute activity from P1 to P3 cannot be accounted for by recoding alone.

The third is that the *governance-frame dominance* simply reflects the coding scheme's bias toward governance categories. This too has substance: coordination/supervision is one of eleven categories, and it absorbs everything that does not fit one of the more specific bundles. Re-running the analysis with the coordination/supervision category excluded leaves 18,133 events with non-null action_type other than coordination, of which the remaining governance-frame bundle (training + personnel + policy design + capacity-building) contains 7,950 events (43.8%) and the infrastructure-frame bundle contains 5,262 events (29.0%). The gap shrinks but is still 14.8 percentage points in favor of governance — and the absolute infrastructure share rises (29.0% vs. 20.8% in the full sample), which is informative rather than confounding. The qualitative point — *the Chinese model coordinates and trains as much as it builds* — survives the alternative coding.

### 6.3 Limits and what this paper does not establish

This paper does not establish causal effects. It does not claim that the SLMC ecology *produced* the documented poverty-reduction outcomes; that connection requires the household-level linkage developed in a companion project. It does not claim that SLMC is normatively desirable; the type is descriptive, not prescriptive. It does not claim that SLMC is generalizable to other policy fields: I have measured it in one campaign, in one country, over one fourteen-year window. Other policy fields (environmental governance, public-health response, basic-education provision) may exhibit similar or quite different organizational ecologies; that is an empirical question, not an assumption.

The paper also does not engage in formal causal-identification work on the structural breaks. The 2013 and 2020 inflections are descriptively striking and conceptually intuitive, but they are not causal estimates. A proper ITS (interrupted time series) treatment, which I plan as a follow-up, would require monthly aggregation and seasonal pre-whitening to handle the yearbook compilation cycle.

Finally, the paper rests on a single corpus — the national poverty yearbooks. A cross-corpus check using provincial yearbooks (a parallel project) would help discipline the documentation-artifact concern; that work is underway.

### 6.4 Relation to the elite-politics literature

The Li Cheng program on Chinese leadership composition (Li 2016, 2020) and the broader study of elite political dynamics (Lampton 2014; Shirk 2018) have produced rich empirical descriptions of *who decides* in Chinese politics. The present paper sits one analytic level lower — *who implements once decisions have been made* — and provides what I would argue is a natural complement. The two layers connect tightly: the post-2013 intensification of central involvement in poverty-governance implementation (visible in the local-government collapse and the central-state share stability) is exactly the implementation-side signature of the centralization of decision authority that the elite-politics literature has documented at the leadership level.

The complementarity goes further. The literature's emphasis on factional and generational dynamics among the senior leadership has not had an obvious downstream-empirical translation, because implementation-side data have not been organized at the granularity required for such translation. The database underlying this paper provides one such organization. A natural follow-up project would link senior-leadership designation events (e.g., the assignment of a vice premier to lead a Leading Small Group on poverty) to the action-event composition in the subsequent year, asking whether and how leadership-level signals translate into implementation-level composition. The present paper does not perform this linkage; it provides the implementation-side infrastructure on which the linkage can be built.

### 6.5 Implications for studying outward Chinese development engagement

The findings of this paper have direct implications for the active debate on whether China is exporting a distinctive development-governance model through the Belt and Road Initiative, the Global Development Initiative, and South-South cooperation more broadly (Brautigam 2009; Hameiri & Jones 2018; Mawdsley 2012). The implication is not that this paper *answers* the export question — it does not; that is the subject of a companion project — but that it *changes what the export question means*.

If the domestic Chinese development-governance practice is characterized by infrastructure construction and finance, then "export" would mean exporting roads and loans. If, as this paper documents, the domestic practice is characterized by coordination, training, designated pairing, and hybrid governance mechanisms, then "export" would also include the question of whether *these* — not roads and loans — travel. The hypotheses one would design about Chinese outward engagement look quite different if one starts from a governance-frame characterization of the domestic practice rather than from a construction-frame characterization. The companion project (Plan C) takes up exactly this question, using the same dictionary of frames identified in the present database to test whether they reappear in outward documents to ASEAN.

The methodological implication parallels the substantive one. Studies of Chinese outward engagement that count projects and tally loans miss a large fraction of what the domestic model actually does. Studies that take seriously the governance-frame action repertoire — the coordinating, training, personnel-deploying repertoire — would design quite different empirical strategies, including textual analysis of outward documents for governance frames and not just material accounting of outward flows.

## 7. Conclusion

China's anti-poverty campaign of the long 2010s was implemented by an organizational ecology whose composition shifted substantively across fourteen years, in directions that the dominant frames in the existing literature — decentralization, recentralization, marketization, civic mobilization — only partly capture. The local-government share collapsed from a quarter to one-sixteenth of documented actions; the research-institute share rose from near-zero to one-fifth; the dominant action repertoire was coordination and training, not construction and disbursement; the network's brokers were small specialist agencies, not powerful line ministries; the dominant governance mechanism was a *hybrid* combining administrative directive with at least one of market, mobilization, or co-governance tools. The combination of these features defines a type — state-led multi-actor coordination — that warrants a slot in the comparative typology of development governance distinct from donor-driven, NGO-driven, developmental-state, and state-capitalist alternatives.

For Chinese politics, the contribution is to take the implementing-organizational layer seriously as the place where elite political choice becomes household outcome, and to provide a database that other researchers can extend (the data are open). For organizational ecology, the contribution is to show that the variation-selection-retention apparatus needs a state-allocation amendment when applied to strongly state-managed policy fields. For comparative development governance, the contribution is to discipline the Chinese case into a specific named type rather than leaving it as an exceptional "hybrid model" caveat. For the policy literature, the contribution is methodological: that an LLM-extracted structured event database can produce findings that hand-coding at the same scale could not have, while preserving the auditability and validation discipline that hand-coding traditions value.

A companion project (Plan B in the author's research program) links this database to household-level panel evidence on poverty exits, asking whether and how the SLMC ecology made a measurable difference at the household level. A second companion (Plan C) asks whether the SLMC repertoire is being exported to ASEAN partners through the Belt and Road Initiative and the Global Development Initiative — whether, in short, the language of designated pairing and hybrid governance now travels with the language of infrastructure and finance.

---

## Tables

**Table 1. Annual event counts, 2009–2022 (data_year).** Source: action_events.

| Year | n | Year | n |
|------|---|------|---|
| 2009 | 66 | 2016 | 1,732 |
| 2010 | 855 | 2017 | 1,756 |
| 2011 | 897 | 2018 | 2,310 |
| 2012 | 1,006 | 2019 | 2,771 |
| 2013 | 950 | 2020 | 3,234 |
| 2014 | 1,612 | 2021 | 3,399 |
| 2015 | 944 | 2022 | 3,826 |

Total: 25,358.

**Table 2. Actor composition by phase (count and within-phase %).**

| Actor type | P1 n (%) | P2 n (%) | P3 n (%) |
|---|---|---|---|
| Central state | 932 (33.0) | 2,832 (23.5) | 2,958 (28.3) |
| Local state | 716 (25.4) | 1,655 (13.7) | 652 (6.2) |
| SOE | 417 (14.8) | 2,622 (21.7) | 2,464 (23.6) |
| Research institutes | 7 (0.2) | 1,588 (13.2) | 2,157 (20.6) |
| Private firms | 76 (2.7) | 1,028 (8.5) | 758 (7.2) |
| Finance | 180 (6.4) | 707 (5.9) | 420 (4.0) |
| Mass orgs | 141 (5.0) | 593 (4.9) | 248 (2.4) |
| Social orgs | 231 (8.2) | 363 (3.0) | 415 (4.0) |
| Democratic parties | 94 (3.3) | 359 (3.0) | 193 (1.8) |
| Other | 30 (1.1) | 328 (2.7) | 194 (1.9) |
| **Phase total** | 2,824 | 12,075 | 10,459 |

**Table 3. Entry-mechanism share by phase (within-phase %).**

| Entry mechanism | P1 | P2 | P3 |
|---|---|---|---|
| Designated pairing | 37.5 | 3.2 | 50.0 |
| Sectoral assistance | 26.8 | 17.6 | 6.7 |
| Policy-driven | 20.5 | 4.9 | 3.3 |
| Social participation | 7.1 | 74.2 | 1.7 |
| East-west pairing | 4.9 | 0.0 | 3.1 |
| Market entry | 3.3 | 0.0 | 0.9 |
| Other | 0.0 | 0.0 | 34.2 |

**Table 4. Shannon entropy of the organization-class distribution, by pub_year.**

| pub_year | H | pub_year | H |
|---|---|---|---|
| 2010 | 1.79 | 2017 | 2.02 |
| 2011 | 1.77 | 2018 | 2.04 |
| 2012 | 1.73 | 2019 | 2.00 |
| 2013 | 1.72 | 2020 | 1.98 |
| 2014 | 1.75 | 2021 | 2.03 |
| 2015 | 1.81 | 2022 | 2.02 |
| 2016 | 1.89 | 2023 | 1.40 |

**Table 5. Action-type composition (full-sample %).**

| Action type | n | % |
|---|---|---|
| Coordination/supervision | 7,225 | 28.5 |
| Training/capacity-building | 5,152 | 20.3 |
| Fund disbursement | 3,094 | 12.2 |
| Industry introduction | 2,735 | 10.8 |
| Personnel deployment | 1,881 | 7.4 |
| Paired assistance | 1,145 | 4.5 |
| Project implementation | 1,097 | 4.3 |
| Infrastructure construction | 1,071 | 4.2 |
| Market matching | 1,041 | 4.1 |
| Policy design | 778 | 3.1 |
| Capacity-building, other | 139 | 0.5 |

**Table 6. Governance-mechanism composition (classified rows only).**

| Governance mechanism | n | % of classified |
|---|---|---|
| Hybrid | 12,199 | 48.1 |
| Administrative directive | 9,458 | 37.3 |
| Social mobilization | 2,876 | 11.3 |
| Market incentive | 685 | 2.7 |
| Collaborative co-governance | 140 | 0.6 |

**Table 7. Top-10 collaboration-network nodes by betweenness centrality.**

| Organization | Betweenness | Degree centrality |
|---|---|---|
| China National Intellectual Property Administration | 0.100 | 0.463 |
| East China University of Science and Technology | 0.058 | 0.164 |
| Nanjing University | 0.033 | 0.060 |
| Ministry of State Security | 0.032 | 0.373 |
| State Cultural Heritage Administration | 0.026 | 0.299 |
| Bank of Communications | 0.020 | 0.269 |
| Ministry of Environmental Protection | 0.018 | 0.194 |
| State Taxation Administration | 0.015 | 0.284 |
| Central South University | 0.010 | 0.299 |
| Red Cross Society of China | 0.010 | 0.299 |

## Figures (references)

- Figure 1. Annual event counts, 2009–2022. Source file: `output_v3/figures/ch3_fig1_org_count_trend.png`.
- Figure 2. Stacked-area composition by actor type, 2010–2023 (pub_year). Source file: `output_v3/figures/ch3_fig2_stacked_area.png`.
- Figure 3. Shannon-entropy trajectory. Source file: `output_v3/figures/ch3_fig3_diversity.png`.
- Figure 4. Entry-mechanism distribution. Source file: `output_v3/figures/ch3_fig4_entry_mechanism.png`.
- Figure 5. Action-type structure by actor. Source file: `output_v3/figures/ch3_fig5_action_by_actor.png`.
- Figure 6. Governance-mechanism heatmap. Source file: `output_v3/figures/ch4_fig4_govmech_heatmap.png`.
- Figure 7. Provincial concentration of action events. Source file: `output_v3/figures/ch5_fig1_spatial_heatmap.png`.
- Figure 8. Inter-organizational collaboration network (top-20 by centrality). Source file: `output_v3/figures/ch5_fig2_collab_network.png`.

## References

Beeson, M. (2009). Developmental states in East Asia: a comparison of the Japanese and Chinese experiences. *Asian Perspective*, 33 (2): 5–39.

Brautigam, D. (2009). *The Dragon's Gift: The Real Story of China in Africa*. Oxford University Press.

Carroll, G.R. & Hannan, M.T. (2000). *The Demography of Corporations and Industries*. Princeton University Press.

Donaldson, J.A. (2011). *Small Works: Poverty and Economic Development in Southwestern China*. Cornell University Press.

Edwards, M. & Hulme, D. (1996). Too close for comfort? The impact of official aid on nongovernmental organizations. *World Development*, 24 (6): 961–973.

Evans, P. (1995). *Embedded Autonomy: States and Industrial Transformation*. Princeton University Press.

Hannan, M.T. & Freeman, J. (1977). The population ecology of organizations. *American Journal of Sociology*, 82 (5): 929–964.

Heberer, T. & Trappel, R. (2013). Evaluation processes, local cadres' behaviour and local development processes. *Journal of Contemporary China*, 22 (84): 1048–1066.

Johnson, C. (1982). *MITI and the Japanese Miracle*. Stanford University Press.

Lampton, D.M. (2014). *Following the Leader: Ruling China, from Deng Xiaoping to Xi Jinping*. University of California Press.

Li, C. (2016). *Chinese Politics in the Xi Jinping Era: Reassessing Collective Leadership*. Brookings Institution Press.

Lieberthal, K. & Oksenberg, M. (1988). *Policy Making in China: Leaders, Structures, and Processes*. Princeton University Press.

Liu, M., Feng, X., Wang, S. & Qiu, H. (2018). China's poverty alleviation over the last 40 years: successes and challenges. *Australian Journal of Agricultural and Resource Economics*, 62 (1): 132–155.

Mawdsley, E. (2012). *From Recipients to Donors: Emerging Powers and the Changing Development Landscape*. Zed Books.

McNally, C.A. (2012). Sino-capitalism: China's reemergence and the international political economy. *World Politics*, 64 (4): 741–776.

Mertha, A. (2009). "Fragmented authoritarianism 2.0": political pluralization in the Chinese policy process. *China Quarterly*, 200: 995–1012.

Naughton, B. (2017). Is China socialist? *Journal of Economic Perspectives*, 31 (1): 3–24.

O'Brien, K.J. & Li, L. (1999). Selective policy implementation in rural China. *Comparative Politics*, 31 (2): 167–186.

Park, A. & Wang, S. (2010). Community-based development and poverty alleviation: an evaluation of China's poor village investment program. *Journal of Public Economics*, 94 (9–10): 790–799.

Shirk, S. (2018). The return to personalistic rule. *Journal of Democracy*, 29 (2): 22–36.

Wang, Y. & Yang, D.L. (2022). Inspecting the inspectors: party inspections and oversight in contemporary China. *Modern China*, 48 (4): 711–746.

Xu, M., Zhang, X. & Zhang, S. (2023). Poor and lazy? Stigmatization of poverty and the targeted-poverty-alleviation experience. *Journal of Contemporary China* (forthcoming; in author's earlier work referenced as the *Poor and Lazy* paper).

---

*End of working paper v1. Full SQL queries and replication notes in the supplementary appendix.*
