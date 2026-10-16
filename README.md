# Prevalence of misophonia across case definitions and populations: data and code

This repository contains the records, decisions, extracted data and analysis code for

> Rekhert, M. (2026). *Prevalence of misophonia across case definitions and populations: A systematic review and meta-analysis* [Manuscript submitted for publication]. Preprint: forthcoming

- Registration (OSF, 10 October 2026, before the final search): https://doi.org/10.17605/OSF.IO/39MQ2
- Archived release (Zenodo): forthcoming
- Author: Martin Rekhert, Higher School of Psychology, Turan University, Almaty, Kazakhstan (ORCID [0009-0001-2402-2031](https://orcid.org/0009-0001-2402-2031))

## The review in brief

- **Question.** How common is misophonia when each instrument and cut-off is assigned in advance to a case-definition level: L1 symptom level, L2 clinically significant (validated cut-off or criterion algorithm), L3 diagnosis by interview?
- **Search.** 10 October 2026: PubMed, Europe PMC, OpenAlex, Semantic Scholar, citations of the development papers of ten instruments (OpenAlex), DataCite, OpenAIRE, CORE, SciELO and Google Scholar, no language limits; 7,885 records, 1,508 after de-duplication. Citation searching of the included studies on 15 October 2026.
- **Selection.** One reviewer (the author) decided every record and report. An AI assistant (Claude Opus 5.5, `claude-opus-5-5`, through Claude Code 2.1.289 with fixed prompts and no tools) drafted screening labels, full-text proposals and extraction forms. The screening prompt was registered; a blind calibration sample and a pre-specified safeguard checked the AI labels.
- **Included.** 120 reports, 96 studies, 125 independent samples, 146,885 participants, 565 estimates.
- **Analysis.** Random-effects binomial–normal GLMMs (`metafor::rma.glmm`), three-level logistic models (`lme4`) with cluster-robust checks (`clubSandwich`), GRADE for event rates.
- **Main result.** Clinically significant misophonia (L2/L3) in non-clinical samples: 11.9% (95% CI 9.0–15.6; 61 samples; 95% PI 1.2–59.6%).

## Repository layout

All study files are under `papers/misophonia-prevalence/`.

| Path | Contents |
| --- | --- |
| `protocol.md` | Registered protocol v1.0 (frozen 10 October 2026, git tag `misophonia-prereg-v1.0` in the working repository) |
| `deviations.md` | Every change and clarification after registration, dated (Supplementary File S3) |
| `registration/` | OSF registration texts and the script that built the registered package |
| `search/` | Search, import and de-duplication scripts; `runs/2026-10-10/`: search log, raw exports (zip), unique records, screening list (CSV, RIS), recall check against the seed set; `runs/2026-10-15-citations/`: citation searching |
| `screening/` | AI screening prompt and runner, AI labels with the prompt hash, blind calibration, safeguard re-screening, verification worksheets and the final decisions (`decisions/tiab_final.csv`) |
| `fulltext/` | Retrieval script and log (open access only), full-text prompt and AI proposals, the reviewer's worksheets and decisions (`decisions/ft_R1.csv`, `ft_R1_chase.csv`), PRISMA counts |
| `extraction/` | Study map (reports → studies), extraction prompt and runner, AI drafts (`draft/`), the reviewer's verification worksheets (`verify/`) and verified values (`decisions/`), quote and correction audits, retraction check, `finalize.py` |
| `forms/` | Extraction codebook, case-definition levels (`instrument_thresholds.csv`, rules `table1_completion.md`), JBI rules, and the two analysis tables `samples.csv` and `estimates.csv` |
| `analysis/` | `analysis.R` (all analyses), `prisma.R`, `descriptives.py`, country lookup and World Bank income groups by year (OGHIST); `results/` and `figures/` as reported |
| `manuscript/` | Scripts for Tables 1–4 (`make_tables.py` → `tables.md`) and Supplementary Files S1–S7 (`make_supplement.py` → `supplement/`) |
| `harness/` | `llmaudit`: the Claude Code judge runner used for the AI drafts, agreement statistics (κ, AC1) |

Reviewer worksheets (`*.md` under `screening/`, `fulltext/decisions/`, `extraction/verify/`) have instructions in Russian, the reviewer's working language; records, AI drafts and decisions are in English, and every decision is also in a CSV file.

Not included: full texts and PDFs of the reports (copyright), saved Google Scholar pages (they show account details; the parsed records are in the raw exports), API keys.

## Reproducing the analysis

The analysis runs from the released files and needs no API access. Tested with Python 3.12 and R 4.6.1 (metafor 5.2.1, lme4 2.0.6, clubSandwich 0.7.0, dplyr, readr, ggplot2, jsonlite).

```bash
# verified extraction -> analysis tables (forms/samples.csv, forms/estimates.csv)
python papers/misophonia-prevalence/extraction/finalize.py --run 2026-10-10 --draft extract_2026-10-15
# meta-analysis -> analysis/results/, analysis/figures/
Rscript papers/misophonia-prevalence/analysis/analysis.R
Rscript papers/misophonia-prevalence/analysis/prisma.R
python papers/misophonia-prevalence/analysis/descriptives.py
# Tables 1-4 and Supplementary Files S1-S7
python papers/misophonia-prevalence/manuscript/make_tables.py
python papers/misophonia-prevalence/manuscript/make_supplement.py
```

Run the commands from the repository root. The release was checked by running them in a clean copy: the analysis tables, all result files, Tables 1–4 and Supplementary Files S1–S7 came out identical.

Re-running the search, retrieval or the AI drafts needs network access and keys (`.env.example`): `OPENALEX_API_KEY` and `CORE_API_KEY` for the search, and `CLAUDE_CODE_OAUTH_TOKEN` (output of `claude setup-token`) for the Claude Code runs. Python packages for those steps: `httpx`, `lxml`, `pyyaml`, `jsonschema` (`pip install -e harness`).

## Licenses and citation

Code (`*.py`, `*.R`, `harness/`): MIT (`LICENSE`). Data and documents: CC BY 4.0 (`LICENSE-DATA.md`); bibliographic records, abstracts and quotations from the included reports remain with their copyright holders. Please cite the article and this repository (`CITATION.cff`).
