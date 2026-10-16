# Protocol: Prevalence of misophonia across case definitions and populations — a systematic review and meta-analysis

**Version 1.0, frozen on 2026-10-10** (git tag `misophonia-prereg-v1.0`) before the final search and before any title/abstract screening. Structured by PRISMA-P 2015 (Moher et al., 2015; Shamseer et al., 2015); item numbers in brackets. Registered on OSF with the Generalized Systematic Review Registration form (van den Akker et al., 2023) and in PROSPERO. Every reference was verified by DOI via Crossref on 2026-10-09 or 2026-10-10. Changes from the draft v0.1 are listed at the end.

---

## Administrative information

**[1] Title.** Prevalence of misophonia across case definitions and populations: a systematic review and meta-analysis.

**[2] Registration.** OSF, registered on 2026-10-10 at 14:57 UTC with the Generalized Systematic Review Registration form, together with the protocol, forms, search and screening code, the AI screener prompt and the pilot search logs: https://osf.io/39mq2, DOI [10.17605/OSF.IO/39MQ2](https://doi.org/10.17605/OSF.IO/39MQ2) (project https://osf.io/7y69r). PROSPERO: not possible. On 2026-10-10 its new registration form accepted only intervention reviews, with "Review of incidence or prevalence" marked "coming soon" (`deviations.md`). If PROSPERO opens prevalence reviews before data extraction starts, the review is registered there too. Adding these identifiers and this note is the only change made to this file after freezing.

**[3a] Author and contact.** Martin Rekhert, MA student in clinical psychology, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com.

**[3b] Contributions.** Single author (R1): conceptualisation, eligibility decisions at every stage, data extraction, risk-of-bias appraisal, interpretation, final manuscript. An AI assistant (Claude Opus 5.5, Anthropic; run through Claude Code) is used as a tool for the tasks listed in §9–§11 and §15 (search code, de-duplication, draft screening labels, draft full-text decisions, draft extraction and risk-of-bias ratings, analysis code, translation, text drafts) and disclosed in the Methods and in the AI declaration. Every AI output is a draft: R1 checks each AI label, extracted value and rating against the source and accepts or overrides it, so all final decisions are R1's. No other person takes part unless named in §11b (optional second human for calibration).

**[4] Amendments.** Any change after registration is dated, justified and logged in `deviations.md`, reported in the PROSPERO record and in the paper.

**[5] Support.** No funding. No sponsor. No conflicts of interest.

---

## Introduction

**[6] Rationale.**

Misophonia is a disorder of decreased tolerance to specific sounds, or stimuli associated with them, that evoke strong negative emotional, physiological and behavioural responses not seen in most people (consensus definition: Swedo et al., 2022). It is not classified in ICD-11 or DSM-5-TR. Research has grown quickly (Malik et al., 2026), but basic epidemiology is unsettled. Single-study estimates of "clinically significant" misophonia range from about 5% in probability samples of adults in Germany and the USA (Jakubovski et al., 2022; Dixon et al., 2024) to 49% of UK medical students (Naylor et al., 2021). Between these lie 6% to 20% in university students (Wu et al., 2014; Zhou et al., 2017), 12.8% by interview in Ankara (Kılıç et al., 2021) and 18.4% in a UK quota sample (Vitoratou et al., 2023).

Much of this spread is probably definitional. Studies use at least ten instruments (A-MISO-S, AMISOS-R, MQ, MisoQuest, S-Five, DMQ, DVMSQ, BMQ-R, SMS, MAQ), different cut-offs on the same instrument and different labels for the same cut-off. The 49.1% of Naylor et al. (2021), for example, counts "mild" A-MISO-S scores as clinically significant; moderate or higher scores in the same sample give about 12%.

The only systematic review of misophonia prevalence (Gowda & Prabhu, 2024) synthesised 12 English-language studies of non-clinical samples narratively (5% to 34.67%), without a pooled estimate or any analysis of what drives the variation. Two reviews of misophonia prevalence registered in PROSPERO (CRD42021267820; CRD42024598262) state no intention to publish and have not been published. Neighbouring reviews cover misophonia in autism (Aldakhil & Shaik, 2025), psychiatric comorbidity in misophonia and hyperacusis (Rodrigues & Aazh, 2025), associated factors (Koroglu & Durat, 2026) and the overlap with obsessive–compulsive disorder (Spallarossa et al., 2026); none pools the prevalence of misophonia itself.

A pooled, definition-aware estimate matters for clinicians and services planning for a condition that patients increasingly bring to them, for the ongoing debate on diagnostic criteria, and for sample-size planning in future research.

**[7] Objectives.**

Review question (CoCoPop; Munn et al., 2015):
- **Condition:** misophonia, identified by a misophonia-specific instrument, a clinical interview or explicit diagnostic criteria.
- **Context:** any country, setting and year.
- **Population:** people of any age who were *not* selected for misophonia or sound sensitivity. Non-clinical samples form the main analysis: general population, students, workers, school pupils. Clinical samples (people with other psychiatric, neurodevelopmental or audiological conditions) are analysed separately.

Objectives:
1. **Primary.** Estimate the prevalence of clinically significant misophonia (levels L2/L3, §13) in non-clinical populations.
2. Estimate the prevalence at each case-definition level: L1 symptom level, L2 clinically significant by questionnaire cut-off, L3 diagnosed by interview. Quantify how much of the between-study variance the case definition and the instrument explain.
3. Estimate prevalence by population type (probability-based general-population samples, other general-population samples, university students, children and adolescents) and in clinical groups.
4. Examine other sources of heterogeneity: age, sex composition, continent (Asia vs other regions) and country income, survey mode, disclosure of the study topic at recruitment, risk of bias, year.
5. Estimate the sex difference (odds ratio, female vs male) in clinically significant misophonia.

The review is descriptive and tests no confirmatory hypotheses. Expectations stated in advance, to be checked rather than tested: prevalence decreases from L1 to L2 to L3; the case-definition level and the instrument explain a large share of the between-study variance; non-probability samples, samples recruited with the topic disclosed and student samples give higher estimates than probability samples of the general population; prevalence is higher in women than in men.

---

## Methods

### [8] Eligibility criteria

**Study designs.** Cross-sectional surveys; the baseline wave of cohort studies; screening phases of experimental or clinical studies; psychometric validation studies; any other design that reports how many people in an unselected sample met a misophonia case definition. Case–control comparisons contribute only if they report the screening of an unselected pool, for example "of 500 screened students, 60 met the MQ criterion".

**Inclusion criteria.**
- I1. The sample (or a reported subsample) was not recruited on the basis of misophonia, sound sensitivity, self-identified misophonia or interest in misophonia.
- I2. Misophonia was assessed with a misophonia-specific self- or informant-report instrument, a clinical interview, or explicit diagnostic criteria. Non-validated or ad hoc items are eligible, are coded as such, and are tested in sensitivity analyses.
- I3. The study reports the number or proportion of participants meeting at least one misophonia case definition together with the denominator, or enough data to derive them. When these are missing, the corresponding author is contacted once, with one reminder after two weeks.
- I4. Any language, any publication year, any publication status: journal article, preprint, thesis or dissertation, conference abstract with sufficient data.

**Exclusion criteria.**
- E1. Samples recruited for misophonia or sound sensitivity: misophonia clinics, misophonia support groups and websites, self-declared misophonia, treatment trials for misophonia. Their prevalence is undefined.
- E2. Measures of general noise sensitivity, hyperacusis, sensory over-responsivity or "decreased sound tolerance" without a misophonia-specific case definition (for example, the Weinstein Noise Sensitivity Scale, Khalfa's Hyperacusis Questionnaire, Adult/Adolescent Sensory Profile).
- E3. Case definitions derived from the distribution of the same sample, such as the top 10% of scores or mean + 1 SD. Prevalence under such a rule is fixed by construction. These estimates are recorded but not pooled.
- E4. Reviews, editorials, case reports and case series, qualitative studies without counts.
- E5. Duplicate reports of the same sample. Reports are linked, and the most complete one supplies the data.

### [9] Information sources

Turan University has no access to Scopus, Web of Science, PsycINFO or Embase. Coverage relies on large open indexes and on citation searching:

- **PubMed**, including non-MEDLINE records and the MeSH supplementary concept "misophonia".
- **Europe PMC**: MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org and Authorea.
- **OpenAlex**: the Crossref corpus, institutional repositories, dissertations, non-indexed and non-English journals.
- **Semantic Scholar**.
- **DataCite**: theses, conference posters and other repository deposits with DOIs. Added on 2026-10-10, before registration, after R1's Google Scholar check found a 2025 doctoral thesis on misophonia measures (University of Surrey; DataCite DOI) that none of the pilot sources contained. A test query on 2026-10-10 returned 330 records, 63 of which were not in the five pilot sources; most of them are theses, posters and conference abstracts.
- **OpenAIRE Graph** and **CORE**: aggregators of institutional and subject repositories, for theses, conference objects and repository copies, searched through their public APIs.
  - They replace BASE and OATD, planned at first. BASE (proof-of-work bot check) and OATD (Cloudflare check) block automated access, and R1 could not open them either. BASE's own API admits only registered IP addresses. Of other thesis portals, NDLTD was offline and DART-Europe is behind a Cloudflare check (2026-10-10).
  - Test on 2026-10-10: OpenAIRE returned 1,096 records, 70 of them found by no other source, many of them theses in Turkish, Norwegian, Swedish, Spanish and Italian. CORE returned 969 hits for "misophonia" in titles or abstracts. Without an API key it serves about ten requests per ten minutes, so its full retrieval runs only in the final search.
- **SciELO** Search and **LILACS** through the BVS portal, for Portuguese- and Spanish-language studies.
  - SciELO is searched in a browser and the result list recorded (7 records on 2026-10-09 and 2026-10-10, 6 of them already in the pilot set).
  - The BVS search servers refused connections from our network on 2026-10-09 and 2026-10-10. The portal's home page loads, and the BVS API requires a key. R1 tries the search once from a mobile network before screening starts. If it is still unreachable, LILACS is not searched directly. SciELO and OpenAlex cover part of its journals, and the omission is reported as a limitation.
- **Citation searching:**
  - **instrument-citation search:** all records citing the development papers of ten misophonia instruments (§10), through OpenAlex;
  - **backward:** reference lists of included studies and of the reviews above, through OpenAlex `referenced_works` and by hand;
  - **forward:** records citing included studies, through OpenAlex.
- **Grey literature:** theses through DataCite, OpenAlex, OpenAIRE and CORE; preprints through Europe PMC, OpenAlex and DataCite; conference abstracts and posters through OpenAlex, Europe PMC, DataCite and OpenAIRE.
- **Google Scholar:** two queries (`misophonia prevalence`; `misophonia "cut-off" OR "clinically significant"`), the first 200 results of each (Haddaway et al., 2015), retrieved by R1 with Publish or Perish (Harzing), because Google Scholar blocks automated access. The export is de-duplicated against the database set by script, and only new records are screened.

All manual exports are converted to the common record format by `search/import_manual.py` and pass through the same de-duplication as the database records.

The search is validated against an independent seed set: the 12 studies included by Gowda & Prabhu (2024), listed with DOIs in `search/seed_set.csv` and checked by `search/recall.py`. The pilot search of 2026-10-09 retrieved 12 of 12 (§10), and so did the check run of 2026-10-10. Recall on the seed set is reported again for the final search.

### [10] Search strategy

Searches use the condition concept only, with no prevalence filter. Prevalence data often sit in validation and experimental studies whose abstracts do not mention prevalence. The search has no date or language limits. Strings are reported per PRISMA-S (Rethlefsen et al., 2021); the code is `search/search.py`.

**PubMed**
```
misophonia[All Fields] OR misophon*[tw] OR "selective sound sensitivity"[tw] OR misokinesia[tw]
OR "decreased sound tolerance"[tw] OR "sound intolerance"[tw] OR "sound tolerance disorder*"[tw]
OR "misophonia"[Supplementary Concept]
```

**Europe PMC**
```
(TITLE_ABS:misophon* OR KW:misophon* OR TITLE_ABS:"selective sound sensitivity" OR TITLE_ABS:misokinesia
 OR TITLE_ABS:"decreased sound tolerance" OR TITLE_ABS:"sound intolerance" OR TITLE_ABS:"sound tolerance disorder"
 OR TITLE_ABS:"sound tolerance disorders" OR TITLE_ABS:misofonia OR TITLE_ABS:mizofoni OR TITLE_ABS:misophonie)
```

**OpenAlex** (title and abstract)
```
title_and_abstract.search: misophonia | misophonic | misophonics | "selective sound sensitivity" | misokinesia
 | "decreased sound tolerance" | "sound intolerance" | "sound tolerance disorder" | "sound tolerance disorders"
 | misofonia | misofonía | mizofoni | misophonie | мизофония | ミソフォニア | 미소포니아
```

**Semantic Scholar** (bulk search)
```
misophonia | misophonic | "selective sound sensitivity" | misokinesia | "decreased sound tolerance"
 | "sound intolerance" | misofonia | mizofoni | misophonie
```

**DataCite** (REST API, `query` parameter)
```
titles.title:T OR descriptions.description:T OR subjects.subject:T, where
T = (misophon* OR misofon* OR mizofon* OR "selective sound sensitivity" OR misokinesia
     OR "decreased sound tolerance" OR "sound intolerance" OR "sound tolerance disorder" OR "sound tolerance disorders")
```

**LILACS / BVS and SciELO:** `misofonia OR misophonia OR misofonía`, all indexes.

**OpenAIRE Graph** (API v1, `researchProducts`, `type=publication`; the API allows at most four OR operators per query, so three queries are pooled)
```
misophonia OR misophonic OR misofonia OR misofonía OR mizofoni
misophonie OR misokinesia OR "selective sound sensitivity" OR "decreased sound tolerance" OR "sound intolerance"
"sound tolerance disorder" OR "sound tolerance disorders"
```

**CORE** (API v3, title or abstract; one query per term, because the API rejects OR lists inside field queries)
```
title:T OR abstract:T, for each T in: misophonia, misophonic, misofonia, misofonía, mizofoni, misophonie, misokinesia,
"selective sound sensitivity", "decreased sound tolerance", "sound intolerance", "sound tolerance disorder", "sound tolerance disorders"
```

**Google Scholar** (Publish or Perish, keywords field, 200 results each): `misophonia prevalence`; `misophonia "cut-off" OR "clinically significant"`.

**Instrument-citation search (OpenAlex `cites:`).** Records citing:
- A-MISO-S (Schröder et al., 2013);
- MQ (Wu et al., 2014);
- AMISOS-R (Jager et al., 2020);
- MisoQuest (Siepsiak, Śliwerski & Dragan, 2020);
- S-Five (Vitoratou et al., 2021);
- DMQ (Rosenthal et al., 2021);
- BMQ-R (Remmert et al., 2022);
- DVMSQ (Williams et al., 2022);
- SMS-Adolescent (Rinaldi et al., 2022);
- SMS-Adult (Simner et al., 2024).

The consensus definition (Swedo et al., 2022) was dropped after the pilot: it is widely cited as a Delphi exemplar, and all 22 records reaching the pilot only through it were off-topic.

**Pilot search (2026-10-09; log in `search/runs/2026-10-09-pilot/`):**

| Source | Records |
| --- | --- |
| PubMed | 478 |
| Europe PMC | 527 |
| OpenAlex | 1,134 |
| Semantic Scholar | 790 |
| Instrument citations | 1,500 |
| **Total** | **4,429** |

- After de-duplication: 1,323 unique records (merged on DOI, PMID and exact title; SciELO language versions of one article share a record).
- Removed automatically before screening: 78 records that every source labels as a non-study type (peer-review reports, errata, tables and figures deposited separately, book reviews, dictionary entries). Rule in `search/dedup.py`.
- To screen: **1,245** records, of which 79 reached the set only through instrument citations.
- Recall on the seed set: 12 of 12. Two seed studies were found only by OpenAlex and Semantic Scholar.

**Checks after the pilot (2026-10-10), before registration.**
- PubMed returned 480 hits, but the pilot parser kept 478: two book chapters (StatPearls) were dropped. The parser now reads book records too.
- DataCite, OpenAIRE and CORE were added (§9).
- De-duplication was tightened for supplementary files and repository versions (§11a).
- Pilot records plus DataCite and OpenAIRE under the v1.0 rules: 5,857 records, 1,434 unique, 99 removed automatically, **1,335 to screen**, 132 of them only through DataCite or OpenAIRE; recall on the seed set 12 of 12 (`search/runs/2026-10-10-check/`). CORE was not part of the check (§9).

**Final search.** Run with the v1.0 code after the OSF registration and before screening starts; dates, record counts and software versions are recorded in `search_log.json` and `manual/`. The raw exports of the final search are archived with the data release, because the databases change and the search cannot be re-run identically. If more than six months pass between the final search and submission, an update search is run with the same strings, and only new records are screened, by the same procedure.

### [11] Study records

**[11a] Data management.**
- Records, decisions, extraction data and analysis code are kept in a git repository; every screening and extraction file is committed with a date.
- De-duplication (`search/dedup.py`):
  - records are merged on DOI (ignoring version suffixes such as `.v2`, `/v1`, `_v1` and SciELO language suffixes), then PMID, then the exact normalised title with years within ±1, unless the two records carry different DOIs;
  - records from pointer sources (DataCite, OpenAIRE, CORE, Google Scholar, hand searching) and article components (figshare deposits, "Additional file 1 of …", "Supplementary tables from …") are attached to the database record with the same title (for components, the title of the parent article) and years within ±1;
  - near-identical titles are flagged, not merged. A preprint and its published version therefore stay linked as two reports of one study.
- Removed automatically before screening ("removed by automation tools", PRISMA 2020): records that every source types as a non-study record. These are peer-review reports, errata, retraction notices, paratext, book reviews, dictionary entries, datasets, figures, tables, images, software, audiovisual material, study registrations, patents and grant records.
- At submission, the data and code are released on GitHub with a Zenodo DOI.

**[11b] Selection process.**
- **Title and abstract: AI-drafted labels, every record verified by R1.**
  1. **Blind calibration.** Before seeing any AI label, R1 screens a random 10% of the records (`screening/calibration.py`: ⌈0.10 × N⌉ records, `random.Random(20261010).sample` over the sorted record IDs, shown in the sampled order). Labels are include / unsure / exclude, with a reason for exclusion. R1 sees the title, abstract, year, venue, record type, language and DOI link; author names are not shown. R1's calibration decisions are exported and committed before any AI label is shown.
  2. **AI draft.** An LLM (Claude Opus 5.5, `claude-opus-5-5`, effort high, through headless Claude Code; fixed prompt with these eligibility criteria, frozen with the protocol in `screening/llm_screener_prompt.md`) labels every record, one call per record: include / unsure / exclude, a reason code and a one-sentence note. The prompt instructs it to choose "unsure" whenever in doubt. It runs while R1 calibrates. When it finishes, the SHA-256 of the label file is committed. The file itself is committed after R1's calibration decisions, so it can be checked that the labels did not change after unblinding. A record the AI fails to label after three attempts is screened by R1 without a label.
  3. **Verification.** R1 reviews every record with the AI label visible and accepts or overrides it. For calibration records, R1 also sees their own blind label and resolves any difference. R1's decision is final. Records that R1 finally marks include or unsure go to full-text screening.
  4. **Safeguard against anchoring on the AI.** If, in the calibration sample, the AI labels "exclude" any record that R1 labelled include or unsure (an AI false negative), R1 re-screens all AI-"exclude" records outside the calibration sample with the AI label hidden, in a random order. Every record R1 then marks include or unsure goes to full text.
  - **Tool.** R1 screens in Markdown files generated by `screening/screen_md.py`. Each record is one block: title, abstract, year, venue, record type, language, DOI link. Under it is a decision line, where R1 types a code: `+` include, `?` unsure, `-1`…`-7` exclude with a reason; in verification files, `=` accepts the AI label shown above the line. Anything after the code is a note.
    - The calibration file and the blind re-screening files contain no AI labels.
    - Each file is committed blank before R1 starts and committed again when R1 finishes; the commits time-stamp the decisions.
    - The same script parses the files into CSV and lists records without a valid code.
  - **Reported:**
    - calibration agreement between R1 (blind) and the AI: Cohen's κ for the three labels; κ and Gwet's AC1 (Gwet, 2008) for "full text" (include or unsure) vs exclude; AI sensitivity and specificity against R1 with Clopper–Pearson 95% CIs;
    - the number of AI labels R1 overrode during verification, by direction;
    - whether the safeguard was triggered, and how many records the blind re-screening moved to full text;
    - after full-text screening, the number of included studies whose records the AI had labelled exclude.
  - **Rationale.** Single-reviewer screening misses about 13% of eligible studies on average (Waffenschmidt et al., 2019). LLM screeners reach high sensitivity on title–abstract screening (Oami et al., 2024). Verification with a blind calibration sample keeps the human in control and measures the AI's error rate on this dataset.
  - **Optional second human.** If a fellow student volunteers and actually screens the same calibration sample blind, human–human κ is reported. Volunteers are acknowledged by name only with their written consent; otherwise they are described without names. Their decisions are kept in the open data under a code (R2). No other role is planned for other people, and none is reported unless the work was done.
- **Full text.**
  - Full texts are obtained through open-access versions (Unpaywall, PMC, repositories, author pages) or by request to the authors.
  - Non-English texts are machine-translated by the AI assistant (Jackson et al., 2019); R1 checks the numbers against the original tables.
  - The AI assistant reads each full text and drafts a proposal: eligible or not, the primary exclusion reason, and where the case counts are (page, table, quote).
  - R1 checks each proposal against the text and decides, recording one primary exclusion reason per study (PRISMA 2020; Page et al., 2021).
  - Reports whose full text cannot be obtained after the author request and one reminder are listed as "reports not retrieved".
- **Linking reports.** Multiple reports of one sample are linked, and the sample is counted once.
- **AI prompts after title/abstract screening.** The prompts for full-text proposals, extraction drafts and risk-of-bias drafts are written before full-text screening, piloted on five studies, frozen and committed before use. Any later change is dated in `deviations.md`.

**[11c] Data collection process.**
- **Form.** Two linked tables (`forms/samples.csv`, one row per independent sample; `forms/estimates.csv`, one row per case definition × sample × subgroup; codebook `forms/extraction_codebook.md`), piloted on five studies before use.
- **AI draft.** The AI assistant pre-fills every field and gives the source location (page, table or quote) for each value. The draft is stored unchanged (`extraction/draft/`).
- **Verification.** R1 verifies every field against the source and accepts or corrects it; the verified values go to the two tables.
  - The key items — sample size, case counts for each case definition, instrument, threshold, population type — are always checked against the source table, never accepted from the draft unseen.
  - We report the proportion of AI-drafted values that R1 corrected, overall and for the key items, by comparing the stored draft with the verified tables.
- Corresponding authors are contacted for missing counts (one e-mail and one reminder).
- **Checks.** Scripted consistency checks (cases ≤ n; subgroup counts add up to the total; percentages match counts within rounding). Retractions and expressions of concern are checked through Crossref (Retraction Watch data) at extraction.

### [12] Data items

Recorded per study:
- report details;
- country and setting;
- years of data collection;
- design;
- sampling method: probability, census, quota/online panel, convenience, snowball;
- whether misophonia or sounds were named in recruitment;
- population type and, for clinical groups, the diagnosis;
- inclusion and exclusion criteria;
- number invited, number responding, number analysed;
- age (mean, SD, range);
- percentage female;
- for each instrument: version, language and whether it was validated in that language;
- mode: online, paper or interview;
- informant: self, parent or clinician;
- time frame: current or lifetime;
- for every case definition: threshold, number of cases and denominator, overall and by sex;
- funding and conflicts of interest.

The full list with coding rules is in `forms/extraction_codebook.md`.

### [13] Outcomes and prioritisation

**Outcome.** Proportion of participants meeting a misophonia case definition (cases / N).

**Case-definition levels.** The mapping of instruments and thresholds to levels (Table 1; full version with sources in `forms/instrument_thresholds.csv`) is fixed with the protocol and applied regardless of the label used by study authors.

| Level | Definition | Examples |
| --- | --- | --- |
| L0 trigger sensitivity | any reported distressing or bothersome trigger sound, without severity | "at least one distressing sound" (Kılıç et al., 2021: 78.9%); "sensitivity to misophonia sounds" (Dixon et al., 2024: 78.5%) — **described, not pooled** |
| L1 symptom level | misophonia of at least mild severity on a validated scale; self-identified misophonia; frequency-based single questions ("often/always" reactions) | A-MISO-S ≥ 5 ("mild" or more); MAQ ≥ 12 |
| L2 clinically significant | a self-report cut-off that the instrument's developers or a validation study define as clinically significant, moderate or higher, or derived against clinical interview; criterion-based algorithms requiring distress or impairment | MQ Misophonia Severity Scale ≥ 7 (Wu et al., 2014); A-MISO-S ≥ 10 ("moderate" or more; Schröder et al., 2013); MisoQuest ≥ 61 of 70 (Siepsiak, Sobczak, et al., 2020); S-Five ≥ 87 of 250 (Vitoratou et al., 2023); SMS-Adult ≥ 50.5 (Simner et al., 2024); DVMSQ algorithm (Williams et al., 2022) |
| L3 diagnosed | clinician or structured/semi-structured interview applying explicit diagnostic criteria (Schröder et al., 2013; Jager et al., 2020; Swedo et al., 2022; study-specific criteria stated in full) | Misophonia Interview Schedule (Kılıç et al., 2021); face-to-face interview (Siepsiak, Sobczak, et al., 2020: 8.5%) |

Instruments without a published clinical cut-off (for example, BMQ-R; Remmert et al., 2022) contribute to L1 only, unless a later validation study supplies an interview-anchored cut-off. Before extraction starts, Table 1 is completed for every instrument found in the included studies. The completion uses only the instruments' development and validation papers, never the prevalence results of the included studies. The completed version is logged in `deviations.md` as a clarification, not a change of rule.

**Primary outcome.** Prevalence of clinically significant misophonia (L2 or L3) in non-clinical populations.

**Secondary outcomes:**
- prevalence at L1 and at L3 separately;
- prevalence in each clinical group;
- odds ratio for L2/L3 misophonia in females vs males.

**One estimate per sample for each analysis.**
- Primary outcome (L2/L3): the L3 estimate if the sample has one, else the L2 estimate.
- Level-specific analyses (L1, L2 and L3 separately, and sensitivity analysis 10): the estimate at that level.
- Within a level, in this order:
  1. the instrument the authors designate as primary;
  2. otherwise, the threshold recommended in Table 1;
  3. if several estimates still remain, the one with the median logit prevalence (with an even number, the lower of the two middle values).
- Whole-sample estimates are used in all pooled analyses. Subgroup estimates (by sex or age band) enter only the analyses that need them: the sex difference and the age moderator.

All estimates enter the multilevel moderator analysis (§15b).

### [14] Risk of bias in individual studies

- **Tool.** JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data, nine items (Munn et al., 2014, 2015). Each item is rated yes / no / unclear with decision rules adapted to misophonia (`forms/rob_jbi.md`):
  - item 1 — sampling frame;
  - item 2 — sampling: probability or census = yes;
  - item 3 — sample size, judged against the precision for an expected prevalence of 10% ± 3 percentage points (n ≥ 385);
  - item 6 — valid identification: validated instrument with a validated cut-off, or interview = yes;
  - item 7 — standard measurement for all participants;
  - item 9 — response rate ≥ 60%, or non-response handled.
- **Raters.** The AI assistant drafts each rating with a supporting quote; R1 verifies every item against the paper and decides.
- **No summary score.** Items are reported individually, and items 2, 6 and 9 drive the sensitivity analyses.

### [15] Data synthesis

**[15a] Narrative synthesis.**
- Characteristics of studies and estimates are tabulated by population and case-definition level.
- An evidence map shows instruments × thresholds × levels.
- L0 estimates and estimates excluded under E3 are listed, not pooled.

**[15b] Meta-analysis.**
- **Primary model.** Random-effects binomial–normal generalised linear mixed model on the logit scale: random-intercept logistic regression; `metafor::rma.glmm`, `measure = "PLO"`, ML estimation. This model is preferred over inverse-variance pooling of transformed proportions, which is biased for small or extreme proportions, and over the Freeman–Tukey double arcsine back-transformation, which can mislead (Stijnen et al., 2010; Schwarzer et al., 2019; Lin & Chu, 2020).
- **Reported:**
  - pooled prevalence with 95% CI and 95% prediction interval (IntHout et al., 2016);
  - τ² on the logit scale;
  - I². Heterogeneity in prevalence meta-analyses is expected; we interpret the prediction interval rather than I² (Migliavaca et al., 2022).
- **Minimum data.** A pooled estimate needs at least three independent samples.
- **Subgroups** (non-clinical samples):
  - case-definition level (L1 / L2 / L3);
  - population type: probability general population / other general population / university students / school children and adolescents / other non-clinical;
  - age group: children under 13 / adolescents 13–17 / adults;
  - continent: Asia / Europe / Americas / other. Many misophonia prevalence studies come from Asian countries (India, Türkiye, Iran, China, Japan, Saudi Arabia), so Asia vs other regions is pre-specified.
  - Clinical groups are pooled per diagnosis when k ≥ 3: OCD, anxiety disorders, depressive disorders, bipolar disorder, ADHD, autism, Tourette syndrome and tic disorders, tinnitus, hyperacusis, hearing loss, other.
- **Moderator analysis using all estimates.**
  - Three-level model: estimates nested in samples nested in studies. `lme4::glmer` with binomial likelihood and nested random intercepts; as a check, `metafor::rma.mv` on logits with cluster-robust inference (Van den Noortgate et al., 2013; Cheung, 2014; Pustejovsky & Tipton, 2022).
  - Fixed effects: case-definition level, instrument within L2, population type, probability sampling, mean age, percentage female, continent (WHO region as an alternative coding), country income group (World Bank), survey mode, topic disclosed at recruitment, JBI items 2, 6 and 9, publication status, year of data collection.
  - A pre-specified multivariable model contains level, population type and probability sampling; the other moderators are exploratory and tested one at a time, each only when k ≥ 10.
  - If a variance component is estimated at zero (singular fit), that level is dropped and the simpler model is reported.
- **Sex difference.** Log odds ratio (female vs male) per sample; random-effects model, REML with Hartung–Knapp adjustment; 95% CI and prediction interval.

**[15c] Sensitivity analyses** (on the primary outcome):
1. only probability or census samples;
2. only validated instruments with a validated cut-off (JBI item 6 = yes);
3. response rate ≥ 60% or not applicable;
4. excluding samples where the study topic was disclosed at recruitment;
5. excluding preprints, theses and conference abstracts;
6. excluding samples with n < 100;
7. inverse-variance random-effects pooling of logits (REML, Hartung–Knapp) instead of the GLMM;
8. a different estimate-selection rule: the highest and the lowest threshold per sample;
9. leave-one-out and influence diagnostics (studentised residuals, Cook's distance);
10. L2 only (excluding L3).

**[15d] If pooling is not appropriate**, for example fewer than three samples in a stratum, estimates are presented in tables and forest plots without a pooled value.

**Software.** R 4.6.1 with metafor, lme4 and clubSandwich for the analysis; package versions are recorded in `analysis/sessionInfo.txt`. Python 3.12 for search, de-duplication, the decision files and the AI runner; Claude Code 2.1.289 (headless) for the AI drafts, with the version stored with every AI output; git for version control. Windows 11.

### [16] Meta-biases

- Funnel-plot asymmetry tests are unreliable for proportions (Hunter et al., 2014) and are not used as inference.
- Instead we plot logit prevalence against its standard error, regress prevalence on 1/√n, and compare peer-reviewed with grey-literature estimates.
- Selective reporting within studies is checked by comparing the case definitions announced in the methods with those reported.

### [17] Confidence in cumulative evidence

Certainty in the main pooled estimates is graded with GRADE adapted for event rates (Iorio et al., 2015). Downgrading:
- **risk of bias:** the share of weight from studies with "no" on JBI items 2, 6 or 9;
- **inconsistency:** width of the prediction interval;
- **imprecision:** CI half-width above 5 percentage points;
- **indirectness:** case definitions far from the consensus definition, and populations from few regions;
- **publication bias.**

Results are presented in a summary-of-findings table.

---

## Load for the human reviewer (fixed in advance)

Based on the pilot search; the final numbers are reported in the PRISMA flow diagram.

| Stage | Who | Approximate volume |
| --- | --- | --- |
| Title and abstract screening | R1 | about 130 records blind (calibration), then about 1,350 AI-labelled records to accept or override; if the safeguard triggers, all AI-excluded records outside the calibration sample again, blind (likely the majority of the list) |
| Full-text screening | R1 | about 200–350 reports, each with an AI proposal and the location of the numbers |
| Data extraction | R1 verifies an AI draft | about 70–110 studies, ~35 fields each, every value with its source location |
| Risk of bias | R1 verifies an AI draft | 9 items per included study, each with a quote |
| Author contacts | R1 sends, AI assistant drafts | about 10–20 e-mails |

No further human coding rounds are planned. There is no second human reviewer (unless a volunteer does the optional calibration). This is a limitation, partly offset by verification of every AI draft, the blind calibration sample and the anchoring safeguard.

---

## Changes from draft v0.1 (2026-10-09)

- DataCite, OpenAIRE and CORE added as sources; BASE and OATD dropped (bot checks; R1 could not open them either); LILACS through BVS only if its search servers can be reached; manual exports imported by script (§9, §10).
- PubMed book records parsed (2 records were lost in the pilot) (§10).
- De-duplication: version DOIs, supplementary files and pointer-source records; more non-study record types removed automatically (§11a).
- Calibration sample fixed (seed 20261010, ⌈10%⌉); AI labels committed by hash before unblinding; agreement measures, safeguard scope and reporting specified; screening in Markdown decision files (§11b).
- Full-text, extraction and risk-of-bias prompts to be piloted and frozen before use; AI extraction drafts stored for the corrections statistic (§11b, §11c).
- Estimate-selection rules written per analysis (§13).
- Forms: the extraction codebook and the JBI rules now describe the AI-draft-plus-verification procedure instead of independent double extraction.

---

## References

- Aldakhil, A. F., & Shaik, R. A. (2025). Misophonia in autism: A systematic review of prevalence, clinical features, and comorbidities. *Research in Developmental Disabilities, 161*, 105005. https://doi.org/10.1016/j.ridd.2025.105005
- Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses: A structural equation modeling approach. *Psychological Methods, 19*(2), 211–229. https://doi.org/10.1037/a0032968
- Dixon, L. J., Schadegg, M. J., Clark, H. L., Sevier, C. J., & Witcraft, S. M. (2024). Prevalence, phenomenology, and impact of misophonia in a nationally representative sample of U.S. adults. *Journal of Psychopathology and Clinical Science, 133*(5), 403–412. https://doi.org/10.1037/abn0000904
- Gowda, V., & Prabhu, P. (2024). Prevalence of misophonia in adolescents and adults across the globe: A systematic review. *Indian Journal of Otolaryngology and Head & Neck Surgery, 76*(5), 4614–4622. https://doi.org/10.1007/s12070-024-04946-8
- Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology, 61*(1), 29–48. https://doi.org/10.1348/000711006X126600
- Haddaway, N. R., Collins, A. M., Coughlin, D., & Kirk, S. (2015). The role of Google Scholar in evidence reviews and its applicability to grey literature searching. *PLOS ONE, 10*(9), e0138237. https://doi.org/10.1371/journal.pone.0138237
- Hunter, J. P., Saratzis, A., Sutton, A. J., Boucher, R. H., Sayers, R. D., & Bown, M. J. (2014). In meta-analyses of proportion studies, funnel plots were found to be an inaccurate method of assessing publication bias. *Journal of Clinical Epidemiology, 67*(8), 897–903. https://doi.org/10.1016/j.jclinepi.2014.03.003
- IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open, 6*(7), e010247. https://doi.org/10.1136/bmjopen-2015-010247
- Iorio, A., Spencer, F. A., Falavigna, M., Alba, C., Lang, E., Burnand, B., et al. (2015). Use of GRADE for assessment of evidence about prognosis: Rating confidence in estimates of event rates in broad categories of patients. *BMJ, 350*, h870. https://doi.org/10.1136/bmj.h870
- Jackson, J. L., Kuriyama, A., Anton, A., Choi, A., Fournier, J.-P., Geier, A.-K., et al. (2019). The accuracy of Google Translate for abstracting data from non–English-language trials for systematic reviews. *Annals of Internal Medicine, 171*(9), 677–679. https://doi.org/10.7326/M19-0891
- Jager, I., de Koning, P., Bost, T., Denys, D., & Vulink, N. (2020). Misophonia: Phenomenology, comorbidity and demographics in a large sample. *PLOS ONE, 15*(4), e0231390. https://doi.org/10.1371/journal.pone.0231390
- Jakubovski, E., Müller, A., Kley, H., de Zwaan, M., & Müller-Vahl, K. (2022). Prevalence and clinical correlates of misophonia symptoms in the general population of Germany. *Frontiers in Psychiatry, 13*, 1012424. https://doi.org/10.3389/fpsyt.2022.1012424
- Kılıç, C., Öz, G., Avanoğlu, K. B., & Aksoy, S. (2021). The prevalence and characteristics of misophonia in Ankara, Turkey: Population-based study. *BJPsych Open, 7*(5), e144. https://doi.org/10.1192/bjo.2021.978
- Koroglu, S., & Durat, G. (2026). Factors associated with misophonia: A systematic review. *Revista Colombiana de Psiquiatría (English ed.), 55*(1), 70–80. https://doi.org/10.1016/j.rcpeng.2026.06.001
- Lin, L., & Chu, H. (2020). Meta-analysis of proportions using generalized linear mixed models. *Epidemiology, 31*(5), 713–717. https://doi.org/10.1097/EDE.0000000000001232
- Malik, M. R., Kumar, K., Hegde, S., Ravi, R., Gunjawate, D. R., & Kalaiah, M. K. (2026). Exploring research trends in decreased sound tolerance: A preliminary scientometric review. *Acta Psychologica, 265*, 106669. https://doi.org/10.1016/j.actpsy.2026.106669
- Migliavaca, C. B., Stein, C., Colpani, V., Barker, T. H., Ziegelmann, P. K., Munn, Z., Falavigna, M., & PERSyst. (2022). Meta-analysis of prevalence: I² statistic and how to deal with heterogeneity. *Research Synthesis Methods, 13*(3), 363–367. https://doi.org/10.1002/jrsm.1547
- Moher, D., Shamseer, L., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. *Systematic Reviews, 4*, 1. https://doi.org/10.1186/2046-4053-4-1
- Munn, Z., Moola, S., Lisy, K., Riitano, D., & Tufanaru, C. (2015). Methodological guidance for systematic reviews of observational epidemiological studies reporting prevalence and cumulative incidence data. *International Journal of Evidence-Based Healthcare, 13*(3), 147–153. https://doi.org/10.1097/XEB.0000000000000054
- Munn, Z., Moola, S., Riitano, D., & Lisy, K. (2014). The development of a critical appraisal tool for use in systematic reviews addressing questions of prevalence. *International Journal of Health Policy and Management, 3*(3), 123–128. https://doi.org/10.15171/ijhpm.2014.71
- Naylor, J., Caimino, C., Scutt, P., Hoare, D. J., & Baguley, D. M. (2021). The prevalence and severity of misophonia in a UK undergraduate medical student population and validation of the Amsterdam Misophonia Scale. *Psychiatric Quarterly, 92*(2), 609–619. https://doi.org/10.1007/s11126-020-09825-3
- Oami, T., Okada, Y., & Nakada, T. (2024). Performance of a large language model in screening citations. *JAMA Network Open, 7*(7), e2420496. https://doi.org/10.1001/jamanetworkopen.2024.20496
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71
- Pustejovsky, J. E., & Tipton, E. (2022). Meta-analysis with robust variance estimation: Expanding the range of working models. *Prevention Science, 23*(3), 425–438. https://doi.org/10.1007/s11121-021-01246-3
- Remmert, N., Schmidt, K. M. B., Mussel, P., Hagel, M. L., & Eid, M. (2022). The Berlin Misophonia Questionnaire Revised (BMQ-R): Development and validation of a symptom-oriented diagnostical instrument for the measurement of misophonia. *PLOS ONE, 17*(6), e0269428. https://doi.org/10.1371/journal.pone.0269428
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, 39. https://doi.org/10.1186/s13643-020-01542-z
- Rinaldi, L. J., Smees, R., Ward, J., & Simner, J. (2022). Poorer well-being in children with misophonia: Evidence from the Sussex Misophonia Scale for Adolescents. *Frontiers in Psychology, 13*, 808379. https://doi.org/10.3389/fpsyg.2022.808379
- Rodrigues, A. L. M., & Aazh, H. (2025). Psychiatric comorbidities in hyperacusis and misophonia: A systematic review. *Audiology Research, 15*(4), 101. https://doi.org/10.3390/audiolres15040101
- Rosenthal, M. Z., Anand, D., Cassiello-Robbins, C., Williams, Z. J., Guetta, R. E., Trumbull, J., & Kelley, L. D. (2021). Development and initial validation of the Duke Misophonia Questionnaire. *Frontiers in Psychology, 12*, 709928. https://doi.org/10.3389/fpsyg.2021.709928
- Schröder, A., Vulink, N., & Denys, D. (2013). Misophonia: Diagnostic criteria for a new psychiatric disorder. *PLOS ONE, 8*(1), e54706. https://doi.org/10.1371/journal.pone.0054706
- Schwarzer, G., Chemaitelly, H., Abu-Raddad, L. J., & Rücker, G. (2019). Seriously misleading results using inverse of Freeman-Tukey double arcsine transformation in meta-analysis of single proportions. *Research Synthesis Methods, 10*(3), 476–483. https://doi.org/10.1002/jrsm.1348
- Shamseer, L., Moher, D., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: Elaboration and explanation. *BMJ, 349*, g7647. https://doi.org/10.1136/bmj.g7647
- Siepsiak, M., Śliwerski, A., & Dragan, W. Ł. (2020). Development and psychometric properties of MisoQuest—A new self-report questionnaire for misophonia. *International Journal of Environmental Research and Public Health, 17*(5), 1797. https://doi.org/10.3390/ijerph17051797
- Siepsiak, M., Sobczak, A. M., Bohaterewicz, B., Cichocki, Ł., & Dragan, W. Ł. (2020). Prevalence of misophonia and correlates of its symptoms among inpatients with depression. *International Journal of Environmental Research and Public Health, 17*(15), 5464. https://doi.org/10.3390/ijerph17155464
- Simner, J., Rinaldi, L. J., & Ward, J. (2024). An automated online measure for misophonia: The Sussex Misophonia Scale for Adults. *Assessment, 31*(8), 1598–1614. https://doi.org/10.1177/10731911241234104
- Spallarossa, C., Figini, C., Motaghilotf, P., Politi, P., & Fusar Poli, L. (2026). Relationship between misophonia and obsessive-compulsive disorder: Systematic review and meta-analysis [Conference abstract]. *European Psychiatry, 69*(S1), S558–S559. https://doi.org/10.1192/j.eurpsy.2026.11075
- Stijnen, T., Hamza, T. H., & Özdemir, P. (2010). Random effects meta-analysis of event outcome in the framework of the generalized linear mixed model with applications in sparse data. *Statistics in Medicine, 29*(29), 3046–3067. https://doi.org/10.1002/sim.4040
- Swedo, S. E., Baguley, D. M., Denys, D., Dixon, L. J., Erfanian, M., Fioretti, A., et al. (2022). Consensus definition of misophonia: A Delphi study. *Frontiers in Neuroscience, 16*, 841816. https://doi.org/10.3389/fnins.2022.841816
- van den Akker, O. R., Peters, G.-J. Y., Bakker, C. J., Carlsson, R., Coles, N. A., Corker, K. S., Feldman, G., Moreau, D., Nordström, T., Pickering, J. S., Riegelman, A., Topor, M. K., van Veggel, N., Yeung, S. K., Call, M., Mellor, D. T., & Pfeiffer, N. (2023). Increasing the transparency of systematic reviews: Presenting a generalized registration form. *Systematic Reviews, 12*, 170. https://doi.org/10.1186/s13643-023-02281-7
- Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594. https://doi.org/10.3758/s13428-012-0261-6
- Vitoratou, S., Hayes, C., Uglik-Marucha, N., Pearson, O., Graham, T., & Gregory, J. (2023). Misophonia in the UK: Prevalence and norms from the S-Five in a UK representative sample. *PLOS ONE, 18*(3), e0282777. https://doi.org/10.1371/journal.pone.0282777
- Vitoratou, S., Uglik-Marucha, N., Hayes, C., & Gregory, J. (2021). Listening to people with misophonia: Exploring the multiple dimensions of sound intolerance using a new psychometric tool, the S-Five, in a large sample of individuals identifying with the condition. *Psych, 3*(4), 639–662. https://doi.org/10.3390/psych3040041
- Waffenschmidt, S., Knelangen, M., Sieben, W., Bühn, S., & Pieper, D. (2019). Single screening versus conventional double screening for study selection in systematic reviews: A methodological systematic review. *BMC Medical Research Methodology, 19*, 132. https://doi.org/10.1186/s12874-019-0782-0
- Williams, Z. J., Cascio, C. J., & Woynaroski, T. G. (2022). Psychometric validation of a brief self-report measure of misophonia symptoms and functional impairment: The Duke-Vanderbilt Misophonia Screening Questionnaire. *Frontiers in Psychology, 13*, 897901. https://doi.org/10.3389/fpsyg.2022.897901
- Wu, M. S., Lewin, A. B., Murphy, T. K., & Storch, E. A. (2014). Misophonia: Incidence, phenomenology, and clinical correlates in an undergraduate student sample. *Journal of Clinical Psychology, 70*(10), 994–1007. https://doi.org/10.1002/jclp.22098
- Zhou, X., Wu, M. S., & Storch, E. A. (2017). Misophonia symptoms among Chinese university students: Incidence, associated impairment, and clinical correlates. *Journal of Obsessive-Compulsive and Related Disorders, 14*, 7–12. https://doi.org/10.1016/j.jocrd.2017.05.001
- Registrations cited: PROSPERO CRD42021267820 and CRD42024598262 (https://www.crd.york.ac.uk/PROSPERO/view/<number>).
