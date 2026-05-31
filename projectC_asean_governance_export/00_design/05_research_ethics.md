# 05 · Research Ethics, Data Use, and Scope Limitations

**Document status**: v0.1
**Last updated**: 2026-05-31

---

## 1. Why this matters

This project analyzes publicly available official communications of state actors. There are no human subjects in the IRB sense. There are nonetheless real ethical questions about (a) what is fair to scrape, (b) how to handle materials whose status is ambiguous (training decks circulated on official sites but not formally "public"), and (c) how to publish results that touch on bilateral political relations.

## 2. Three commitments

1. **Only sources that are unambiguously published.** Anything behind login, anything explicitly marked 内部 / restricted, anything obtained via FOI-equivalent will be excluded from the redistributed corpus. Stable URLs are provided so others can verify; cached copies are kept locally for reproducibility but not redistributed.
2. **No claims about individuals.** The unit of analysis is the agency, not the individual official. No diplomat or minister is named in results except in attributed quotations from their own public statements.
3. **Symmetric treatment of comparison donors.** Identical methods are applied to WB and ADB documents. Findings are framed comparatively, not normatively.

## 3. Data redistribution policy

| Material | Re-distributed in repo? | Why |
|----------|--------------------------|-----|
| Domestic frame dictionary | Yes (CC BY 4.0) | Derivative analytical product, not raw content |
| Outward corpus metadata + URLs + content hashes | Yes (CC BY 4.0) | Replicability requires URL inventory |
| Outward corpus full text | **No** — kept locally, never pushed | Avoids any redistribution-license ambiguity |
| Outward corpus *paragraph snippets* used in paper figures | Yes, with attribution | Fair-use, scholarly quotation |
| Annotation gold standard | Yes, with annotator IDs anonymized | Standard practice |
| LLM prompts | Yes | Replicability |
| Model outputs (frame counts per doc) | Yes | Replicability |

## 4. CLMV recipient-state materials

We collect a small recipient-side mirror (CLMV foreign-ministry statements on China) for descriptive purposes only (Stage 2 source #8 in `04_methodology.md`). These are used to:

- Cross-check publication dates of jointly attended events.
- Sanity-check that our corpus captures the encounters the recipient state itself reports.

They are **not** used as outcomes or as a parallel frame analysis in v1 of the paper; that would require area-studies depth this project does not yet have.

## 5. Sensitivities to manage in writing

- The paper's headline framing avoids the loaded "China exports authoritarianism" register, which both overstates the project's evidentiary scope and short-circuits its scholarly contribution. Preferred register: *frame travel*, *discursive reproduction*, *bureaucratic stratification of outward discourse*.
- When discussing Cambodia / Laos specifically, we explicitly flag that high frame-density does not imply uptake; it implies what Chinese state actors broadcast, not what recipients adopt.

## 6. Authorship and credit

- Sole-authored unless a CCCW collaborator contributes substantively at the design or analysis stage.
- All RA contributions to annotation are listed in the Acknowledgements; lead annotator may be offered second authorship if their contribution extends to coding-rule development.

## 7. Funding and conflict of interest

No external funding at design phase. Any CCCW research-fund support will be disclosed in the final manuscript. PI has no commercial relationships with any of the state actors studied.

## 8. Scope and decision dates

- **Corpus freeze date**: 2027-06-30 — anything published after this date is excluded from the v1 analysis.
- **Re-extraction trigger**: a new model major version (e.g., Claude Opus 5) requires re-running the ensemble on a 200-doc benchmark to decide whether to re-extract the full corpus.
- **Embargo handling**: if any source removes a document, the local cached copy is retained for replication purposes only and is not redistributed; the analysis result based on it is footnoted.

## 9. What to do if the framework is misused

If results are taken out of context (e.g., "study proves China is exporting authoritarianism"), the published methodology section is the primary defense; the explicit non-claims in `01_research_questions.md` §5 are the secondary defense. We will respond once on the record to gross misreadings and otherwise let the methods speak.
