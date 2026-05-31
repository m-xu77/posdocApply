# Pillar 4 — Text-as-Data and LLM Methods for Policy / Discourse Analysis

**Role in project**: methods precedent. Justifies the LLM-extraction + dictionary-validation hybrid and locates it in the methodological state of the art.

---

## Core references

### Grimmer, J. & Stewart, B.M. (2013). "Text as data: the promise and pitfalls of automatic content analysis methods for political texts." *Political Analysis* 21 (3): 267–297.

- **Use**: canonical methodological anchor; cite for the discipline of validating automated text analysis.

### Wilkerson, J. & Casas, A. (2017). "Large-scale computerized text analysis in political science: opportunities and challenges." *Annual Review of Political Science* 20: 529–544.

- **Use**: survey baseline.

### Ash, E. & Hansen, S. (2023). "Text algorithms in economics." *Annual Review of Economics* 15: 659–688.

- **Use**: connects to causal-identification literature; useful for the panel-regression section.

### Laver, M., Benoit, K. & Garry, J. (2003). "Extracting policy positions from political texts using words as data." *American Political Science Review* 97 (2): 311–331.

- **Use**: precedent for dictionary-based extraction, with all the well-known criticisms; the LLM upgrade is the methodological move.

### Bonikowski, B. & Nelson, L.K. (2022). "From ends to means: the promise of computational text analysis for theoretically driven sociological research." *Sociological Methods & Research* 51 (4): 1469–1491.

- **Use**: theoretically driven NLP — exactly our register.

### Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z. & Yang, D. (2024). "Can large language models transform computational social science?" *Computational Linguistics*.

- **Use**: state of the art on LLMs for CSS; the ensemble-validation playbook.

### Argyle, L.P., Busby, E.C., Fulda, N., Gubler, J.R., Rytting, C. & Wingate, D. (2023). "Out of one, many: using language models to simulate human samples." *Political Analysis* 31 (3): 337–351.

- **Use**: LLMs as annotation tools, with appropriate caution about bias.

### Pham, V.H. et al. (recent). "Multilingual LLM annotation in low-resource languages." (verify cite)

- **Use**: motivates the CLMV-language validation step.

### Roberts, M.E., Stewart, B.M. & Tingley, D. (2014). "stm: R package for structural topic models." (and related STM papers)

- **Use**: methodological neighbor we explicitly do *not* use — explain why frame-dictionary + LLM is preferred for our theoretical question.

## Methodological commitments derived from this pillar

1. **Validation is non-negotiable**: gold-standard human annotation of at least 400 documents.
2. **Ensemble**: at least two LLM families; report agreement matrices.
3. **Pre-registered dictionary**: the dictionary is built before outward-corpus collection completes, removing a major researcher-degrees-of-freedom risk.
4. **Open prompts + fixed seeds**: exact prompts, model versions, hash-pinned.

## Methodological choices we deliberately decline

- **Pure topic modeling** (LDA, STM): unsupervised topics rarely map cleanly onto theoretically motivated frames.
- **Pure embedding similarity**: lacks the diagnostic / prognostic decomposition we need.
- **Hand-coding only**: cannot scale to 5,000 docs.

## Open methodological questions

- [ ] Should embeddings + LLM be combined (retrieval-augmented frame extraction)?
- [ ] How best to handle near-translation overlap between Chinese-language original and machine-translated CLMV-language documents?
