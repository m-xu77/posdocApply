# Pillar 5 — Comparative Donor Discourse: DAC vs South-South

**Role in project**: counterfactual / contrast. Without a comparison, "China speaks X way" is uninterpretable. WB / ADB provide a DAC-discourse baseline; this pillar grounds that contrast.

---

## Core references

### Mawdsley, E. (2012). *From Recipients to Donors: Emerging Powers and the Changing Development Landscape*. Zed Books.

- **Argument**: South-South cooperation discourse is grammatically distinct from DAC discourse — emphasizes solidarity, mutual benefit, non-interference, demonstration.
- **Use**: theoretical anchor for the WB/ADB-vs-China comparison; supplies a set of *expected* discursive differences against which we test our LLM findings.

### Gray, K. & Gills, B.K. (2016). "South-South cooperation and the rise of the Global South." *Third World Quarterly* 37 (4): 557–574.

- **Argument**: situates SSC as both ideological and material.
- **Use**: theoretical anchor.

### Bracho, G. (2017). "The troubled relationship of the emerging powers and the effective development cooperation agenda." DIE Discussion Paper.

- **Use**: empirical anchor on the SSC-vs-DAC institutional politics.

### Quadir, F. (2013). "Rising donors and the new narrative of 'South-South' cooperation: what prospects for changing the landscape of development assistance programmes?" *Third World Quarterly* 34 (2): 321–338.

- **Use**: complement to Mawdsley.

### Eyben, R. (2013). "Struggles in Paris: the DAC and the purposes of development aid." *European Journal of Development Research* 25 (1): 78–91.

- **Use**: DAC-side perspective; useful for interpreting frame contrasts.

### Carmody, P. (2016). *The New Scramble for Africa*. Polity.

- **Use**: comparative empirics on emerging-donor engagement.

### Asmus, G., Fuchs, A. & Müller, A. (2024 or recent). "China's BRI lending in comparison to traditional donors." *Journal of Comparative Economics* (verify).

- **Use**: financial-side comparison; sanity-check our discursive-side finding.

## How the comparison corpus is sampled

For each WB / ADB project in CLMV during 2013–2026:

- Project-appraisal document (PAD)
- Project-completion report (ICR)
- Any speech / press release tagged to the project

Matched approximately to Chinese outward documents by sector (infrastructure / health / agriculture / poverty / capacity-building) and year. Matched-sample analysis reported as a robustness check; full-corpus comparison is the primary contrast.

## Hypothesized contrasts (priors)

| Frame family | China outward (expected) | WB / ADB (expected) |
|--------------|--------------------------|---------------------|
| Conditionality / accountability | low density | high density |
| Demonstration / mutual learning | high density | low density |
| Project monitoring / KPIs | moderate density | high density |
| Political non-interference | high density (explicit) | absent or implicit |
| Poverty governance institutions | high density | high density |

If the LLM extraction reproduces these priors, that's a sanity check; if it inverts them, that is an interesting finding to interrogate.
