# Регистрация на OSF: пошагово и тексты полей

Шаблон — **Generalized Systematic Review Registration** (v6 на OSF; van den Akker et al., 2023, https://doi.org/10.1186/s13643-023-02281-7). Поля формы сняты через API OSF 2026-10-10: 61 текстовое поле, все обязательные, и 2 поля для файлов. Тексты ниже на английском, вставляются как есть. Названия полей совпадают с формой.

## Шаги

1. **Проект.** https://osf.io → *Create new project*:
   - Title: `Prevalence of misophonia across case definitions and populations: systematic review and meta-analysis`;
   - Storage location: любое (по умолчанию).
2. **Файлы.** В проекте откройте *Files → OSF Storage* и загрузите из `registration/osf_package/`:
   - `Rekhert_misophonia_protocol_v1.0.pdf` — протокол;
   - `misophonia-prereg-v1.0.zip` — весь пакет: протокол, формы, скрипты поиска и отбора, промпт скринера, логи пилота, README;
   - `llm_screener_prompt.md` и `extraction_codebook.md` — отдельно, их просят поля с файлами.
3. **Регистрация.** Вкладка проекта *Registrations* → *New registration* → шаблон **Generalized Systematic Review Registration** → *Create draft*.
4. **Метаданные** (первая страница черновика):
   - Title — как у проекта;
   - Description — абзац «Description» ниже;
   - Category — *Project*;
   - License — *CC-By Attribution 4.0 International*;
   - Subjects — *Social and Behavioral Sciences → Psychology → Clinical Psychology* и *Medicine and Health Sciences → Psychiatry and Psychology*;
   - Tags — слова из «Tags» ниже;
   - Contributors — только вы.
5. **Поля формы.** Пять страниц, по разделам ниже. В два поля с файлами прикрепите `llm_screener_prompt.md` (Screening → после *Screener instructions*) и `extraction_codebook.md` (Extraction → после *Extractor instructions*).
6. **Отправка.** *Review* → *Register* → **Make registration public immediately** (без эмбарго). Через несколько минут OSF заархивирует файлы и пришлёт письмо.
7. **Мне:** ссылку на регистрацию (`https://osf.io/xxxxx`) и DOI (`10.17605/OSF.IO/XXXXX`). Я впишу их в протокол, README и поля PROSPERO.

Дальше — PROSPERO по `registration/prospero.md`, в поле о полном протоколе — DOI с OSF.

---

## Metadata

**Description.** Protocol (v1.0, frozen 2026-10-10) of a systematic review and meta-analysis of the prevalence of misophonia. Estimates are pooled separately for each case-definition level (symptom level; clinically significant by a validated questionnaire cut-off; diagnosed by interview) in non-clinical and clinical populations, and the review examines how much of the between-study variation (about 5% to 49%) the instrument and the cut-off explain. An AI assistant (Claude Opus 5.5) drafts screening labels, full-text proposals, extraction and risk-of-bias ratings; the author verifies every draft after a blind calibration on a random 10% of records. The files contain the protocol, extraction forms, search and de-duplication code, the frozen AI screener prompt and the pilot search logs.

**Tags.** misophonia; prevalence; epidemiology; meta-analysis; systematic review; case definition; sound sensitivity; decreased sound tolerance; LLM-assisted screening

---

## Review Methods

**Type of review**
Systematic review and meta-analysis of prevalence (proportions), with meta-regression of sources of heterogeneity. The protocol follows PRISMA-P 2015; the review will be reported per PRISMA 2020 and PRISMA-S. Review question framed with CoCoPop (Condition, Context, Population; Munn et al., 2015). Risk of bias: JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data. Certainty: GRADE adapted for event rates. Full protocol: Rekhert_misophonia_protocol_v1.0.pdf in this project.

**Review stages**
Preparation (novelty check, protocol, pilot search) → Registration (OSF, then PROSPERO) → Final search → Title/abstract screening: blind calibration by the reviewer on a random 10% of records, AI draft labels for all records, verification of every record by the reviewer, conditional blind re-screening of AI-excluded records → Full-text screening (AI proposal, reviewer decision) → Pilot extraction on five studies (prompts and form frozen; any change logged) → Extraction and risk of bias (AI draft, reviewer verification of every value) → Synthesis → Reporting.

**Current review stage**
Preparation completed. A pilot search was run on 2026-10-09 (five automated sources, 1,245 records to screen; all 12 studies of an independent seed set retrieved), and test queries of three added sources (DataCite, OpenAIRE, CORE) on 2026-10-10. No screening, full-text reading, data extraction or analysis has started. The final search is run after this registration. This is the first registration of the review.

**Start date**
2026-10-09 (pilot search).

**End date**
Planned: 2027-04-30.

**Background**
Misophonia is a disorder of decreased tolerance to specific sounds, or stimuli associated with them, that evoke strong negative emotional, physiological and behavioural responses (consensus definition: Swedo et al., 2022). It is not classified in ICD-11 or DSM-5-TR. Single-study estimates of "clinically significant" misophonia range from about 5% in probability samples of adults in Germany and the USA to 49% in UK medical students. Much of this spread appears definitional: at least ten instruments are in use (A-MISO-S, AMISOS-R, MQ, MisoQuest, S-Five, DMQ, DVMSQ, BMQ-R, SMS, MAQ), with different cut-offs and different labels for the same cut-off. For example, 49.1% in Naylor et al. (2021) counts "mild" A-MISO-S scores as clinically significant; moderate or higher scores in the same sample give about 12%. The only systematic review of misophonia prevalence (Gowda & Prabhu, 2024; 12 English-language studies of non-clinical samples) synthesised estimates narratively, without a pooled estimate or analysis of what drives the variation. Two prevalence reviews registered in PROSPERO (CRD42021267820, CRD42024598262) state no intention to publish and are unpublished. Neighbouring reviews cover misophonia in autism, psychiatric comorbidity in misophonia and hyperacusis, associated factors, and the overlap with OCD; none pools the prevalence of misophonia itself. This review adds pooled, definition-aware estimates in non-clinical and clinical populations, an analysis of how much the instrument and cut-off explain, and a search that includes non-English studies, theses, preprints and prevalence data hidden in validation and experimental studies.

**Primary research question(s)**
What is the prevalence of clinically significant misophonia in non-clinical populations, where "clinically significant" means level L2 (a questionnaire cut-off defined by the instrument's developers or a validation study as clinically significant, moderate or higher, or anchored on clinical interview; or a criterion-based algorithm requiring distress or impairment) or level L3 (diagnosis by clinical or structured interview with explicit criteria)? Instrument thresholds are mapped to levels in advance (protocol Table 1, forms/instrument_thresholds.csv), whatever label the study authors use.

**Secondary research question(s)**
(1) Prevalence at each case-definition level separately: L1 (symptom level, at least mild on a validated scale, self-identified misophonia, frequency-based items), L2 and L3. (2) How much of the between-study variance do the case-definition level and the instrument explain? (3) Prevalence by population type: probability general-population samples, other general-population samples, university students, school children and adolescents, other non-clinical samples. (4) Prevalence in clinical groups recruited for another condition (OCD, anxiety, depression, bipolar disorder, ADHD, autism, Tourette syndrome/tics, tinnitus, hyperacusis, hearing loss, other), pooled per diagnosis when at least three samples exist. (5) Heterogeneity by age, sex composition, continent (Asia vs other regions) and country income group, survey mode, disclosure of the study topic at recruitment, risk of bias, publication status and year of data collection. (6) The female-to-male odds ratio of L2/L3 misophonia.

**Expectations / hypotheses**
This is a descriptive review without confirmatory hypotheses. Expectations stated in advance, to be checked rather than tested: prevalence decreases from L1 to L2 to L3; the case-definition level and the instrument explain a large share of the between-study variance; non-probability samples, samples recruited with the study topic disclosed, and student samples show higher estimates than probability samples of the general population; women show higher prevalence than men. Context that may colour our interpretation: the author is a clinical psychology student without prior publications on misophonia or ties to any instrument's developers; many studies come from Asian countries, which is why Asia vs other regions is a pre-specified subgroup.

**Dependent variable(s) / outcome(s) / main variables**
Proportion of participants meeting a misophonia case definition (cases / N), recorded separately for every case definition reported in a sample (instrument, version, threshold) and mapped to levels L0–L3. Primary: prevalence of L2/L3 misophonia in non-clinical samples. Secondary: L1, L2 and L3 separately; prevalence in each clinical group; log odds ratio female vs male. L0 (any distressing trigger sound, without severity) and estimates defined by the distribution of the same sample (e.g., top 10%) are tabulated, not pooled.

**Independent variable(s) / intervention(s) / treatment(s)**
Not applicable (prevalence review; no intervention or comparator). The variables expected to explain prevalence differences are listed under covariates.

**Additional variable(s) / covariate(s)**
Moderators (protocol §15b): case-definition level; instrument (within L2); population type; probability vs non-probability sampling; mean age and age group (children <13, adolescents 13–17, adults); percentage female; continent (UN M49; WHO region as an alternative coding); World Bank country income group in the year of data collection; survey mode (online, paper, interview); whether misophonia or sounds were named at recruitment; JBI items 2 (sampling), 6 (valid identification) and 9 (response rate); publication status (journal vs preprint, thesis, abstract); year of data collection. Also extracted: country, setting, design, informant (self, parent, clinician), time frame, instrument language and validation status, response rate, funding and conflicts of interest.

**Software**
Python 3.12 (search via the PubMed E-utilities, Europe PMC, OpenAlex, Semantic Scholar and DataCite APIs; de-duplication; calibration sampling) — search/search.py, search/import_manual.py, search/dedup.py, screening/calibration.py. Publish or Perish (Harzing) for Google Scholar. screening/screen_md.py writes the Markdown decision files and parses them. Claude Code 2.1.289 in headless mode running Claude Opus 5.5 (claude-opus-5-5) for AI draft labels and drafts (screening/llm_screen.py; the version is stored with every output). R 4.6.1 with metafor, lme4 and clubSandwich for the analysis (package versions recorded in analysis/sessionInfo.txt). git for version control. Windows 11.

**Funding**
None. The review is unfunded.

**Conflicts of interest**
None. The author has no financial or professional interest in any misophonia instrument, service or treatment.

**Overlapping authorships**
None. The author has not authored or co-authored any study likely to be included.

---

## Search Strategy

**Databases**
PubMed (including non-MEDLINE records and the MeSH supplementary concept "misophonia"); Europe PMC (MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org, Authorea); OpenAlex; Semantic Scholar; DataCite; OpenAIRE Graph; CORE; SciELO; LILACS (via BVS, if its search servers can be reached; see Miscellaneous search strategy details); Google Scholar. The author's university has no access to Scopus, Web of Science, PsycINFO or Embase.

**Interfaces**
PubMed — NCBI E-utilities API; Europe PMC — REST API; OpenAlex — API (title_and_abstract.search and cites: filters); Semantic Scholar — Graph API bulk search; DataCite — REST API (query parameter); OpenAIRE Graph — API v1 (researchProducts); CORE — API v3 (search/works); SciELO — SciELO Search web interface; LILACS — BVS portal (pesquisa.bvsalud.org); Google Scholar — Publish or Perish (Harzing; version recorded at the search). API searches run from search/search.py; web searches are done by hand and their exports imported with search/import_manual.py.

**Grey literature**
Theses through DataCite, OpenAlex, OpenAIRE and CORE (repository aggregators); preprints through Europe PMC, OpenAlex and DataCite; conference abstracts and posters through OpenAlex, Europe PMC, DataCite and OpenAIRE; Google Scholar (first 200 results of two queries, searched by the author with Publish or Perish because Google Scholar blocks automated access). BASE and OATD were planned but block automated access with bot checks and could not be opened by the author either; OpenAIRE and CORE, which harvest the same kinds of repositories, replace them. Authors of eligible studies are contacted for missing counts.

**Inclusion and exclusion criteria**
Framework: CoCoPop. Inclusion: (I1) the sample, or a reported subsample, was not recruited on the basis of misophonia, sound sensitivity, self-identified misophonia or interest in misophonia; (I2) misophonia was assessed with a misophonia-specific self- or informant-report instrument, a clinical interview or explicit diagnostic criteria (ad hoc items are eligible, coded as such and tested in sensitivity analyses); (I3) the number or proportion meeting at least one misophonia case definition is reported with its denominator, or can be derived (authors are contacted when missing); (I4) any language, year and publication status (journal article, preprint, thesis, conference abstract with sufficient data). Designs: cross-sectional surveys, baseline waves of cohorts, psychometric validation studies, screening phases of experimental or clinical studies, case–control studies only if they report the screening of an unselected pool. Exclusion: (E1) samples recruited for misophonia or sound sensitivity (misophonia clinics, support groups, self-declared misophonia, misophonia treatment trials); (E2) measures of noise sensitivity, hyperacusis, sensory over-responsivity or decreased sound tolerance without a misophonia-specific case definition; (E3) case definitions derived from the distribution of the same sample (recorded, not pooled); (E4) reviews, editorials, case reports and series, qualitative studies without counts; (E5) duplicate reports of the same sample (linked; the most complete report supplies the data). The search itself uses only the condition concept, with no prevalence, design, date or language filter.

**Query strings**
PubMed: misophonia[All Fields] OR misophon*[tw] OR "selective sound sensitivity"[tw] OR misokinesia[tw] OR "decreased sound tolerance"[tw] OR "sound intolerance"[tw] OR "sound tolerance disorder*"[tw] OR "misophonia"[Supplementary Concept]
Europe PMC: (TITLE_ABS:misophon* OR KW:misophon* OR TITLE_ABS:"selective sound sensitivity" OR TITLE_ABS:misokinesia OR TITLE_ABS:"decreased sound tolerance" OR TITLE_ABS:"sound intolerance" OR TITLE_ABS:"sound tolerance disorder" OR TITLE_ABS:"sound tolerance disorders" OR TITLE_ABS:misofonia OR TITLE_ABS:mizofoni OR TITLE_ABS:misophonie)
OpenAlex: title_and_abstract.search: misophonia | misophonic | misophonics | "selective sound sensitivity" | misokinesia | "decreased sound tolerance" | "sound intolerance" | "sound tolerance disorder" | "sound tolerance disorders" | misofonia | misofonía | mizofoni | misophonie | мизофония | ミソフォニア | 미소포니아
Semantic Scholar: misophonia | misophonic | "selective sound sensitivity" | misokinesia | "decreased sound tolerance" | "sound intolerance" | misofonia | mizofoni | misophonie
DataCite: titles.title:T OR descriptions.description:T OR subjects.subject:T, with T = (misophon* OR misofon* OR mizofon* OR "selective sound sensitivity" OR misokinesia OR "decreased sound tolerance" OR "sound intolerance" OR "sound tolerance disorder" OR "sound tolerance disorders")
SciELO and LILACS/BVS: misofonia OR misophonia OR misofonía (all indexes)
OpenAIRE Graph (type=publication; at most four OR operators per query, so three queries pooled): misophonia OR misophonic OR misofonia OR misofonía OR mizofoni | misophonie OR misokinesia OR "selective sound sensitivity" OR "decreased sound tolerance" OR "sound intolerance" | "sound tolerance disorder" OR "sound tolerance disorders"
CORE (one query per term, title or abstract): title:T OR abstract:T for T in misophonia, misophonic, misofonia, misofonía, mizofoni, misophonie, misokinesia, "selective sound sensitivity", "decreased sound tolerance", "sound intolerance", "sound tolerance disorder", "sound tolerance disorders"
Google Scholar (Publish or Perish, keywords field, first 200 results each): misophonia prevalence; misophonia "cut-off" OR "clinically significant"
Instrument-citation search (OpenAlex cites:): every record citing the development paper of A-MISO-S (10.1371/journal.pone.0054706), MQ (10.1002/jclp.22098), AMISOS-R (10.1371/journal.pone.0231390), MisoQuest (10.3390/ijerph17051797), S-Five (10.3390/psych3040041), DMQ (10.3389/fpsyg.2021.709928), BMQ-R (10.1371/journal.pone.0269428), DVMSQ (10.3389/fpsyg.2022.897901), SMS-Adolescent (10.3389/fpsyg.2022.808379), SMS-Adult (10.1177/10731911241234104).

**Search validation procedure**
Recall is checked against an independent seed set: the 12 studies included by Gowda & Prabhu (2024). The pilot search (2026-10-09) retrieved all 12; two of them only through OpenAlex and Semantic Scholar. Recall on the seed set is reported again for the final search. The strings were also checked against the author's Google Scholar queries of 2026-10-10, which led to adding DataCite (a 2025 doctoral thesis found only there).

**Other search strategies**
Instrument-citation search (descendancy from the development papers of ten misophonia instruments, see query strings): whoever measured misophonia almost always cites one of them; in the pilot, 79 records reached the set only this way. Backward citation searching (ascendancy) of included studies and relevant reviews through OpenAlex referenced_works and by hand; forward citation searching (descendancy) of included studies through OpenAlex. Records found this way are screened by the same procedure.

**Procedures to contact authors**
When an eligible study does not report the number of cases or the denominator for a case definition, or the full text cannot be obtained, the corresponding author is e-mailed once, with one reminder after two weeks. The AI assistant drafts the e-mails; the author sends them. Only the existence, date and outcome of each contact are shared, not the correspondence.

**Results of contacting authors**
Reported in the paper and the supplementary material: number of authors contacted, number who replied, number who supplied data, and which estimates rest on author-supplied data.

**Search expiration and repetition**
If more than six months pass between the final search and submission, the search is updated with the same strings and code; only new records are screened, by the same procedure. No living review is planned.

**Search strategy justification**
Prevalence data on misophonia often sit in validation, correlational and experimental studies whose abstracts do not mention prevalence, so the search uses only the condition concept and no prevalence filter, and adds a citation search of instrument development papers. Without subscription databases, coverage relies on large open indexes: OpenAlex covers the Crossref corpus, repositories and non-English journals; DataCite adds theses and posters with DOIs; OpenAIRE and CORE add repository theses and copies in many languages; SciELO (and LILACS, if reachable) add Latin American journals; Google Scholar adds grey literature. The seed-set recall check measures what this strategy may miss. Author contact is limited to one e-mail and one reminder to keep the burden proportionate.

**Miscellaneous search strategy details**
All automated searches run from search/search.py, which logs query strings, dates, record counts and timings (search_log.json). Manual exports are converted by search/import_manual.py and logged with SHA-256 hashes. De-duplication (search/dedup.py) merges records on DOI (ignoring version suffixes), PMID and the exact normalised title with years within ±1. It attaches supplementary-file and pointer-source records to their database records, and flags near-identical titles without merging them. Records that every source types as non-study records (peer-review reports, errata, datasets, figures, registrations and similar) are removed automatically and counted in PRISMA. The raw exports of the final search are archived with the data release. The pilot search log is in this project. LILACS: the BVS search servers refused connections from the author's network on 2026-10-09 and 2026-10-10, and the BVS API requires a key; the author tries once from a mobile network before screening, and if it fails LILACS is not searched directly (part of its journals are covered by SciELO and OpenAlex), which is reported as a limitation.

---

## Screening

**Screening stages**
(1) De-duplication by script (search/dedup.py, see search details). (2) Title and abstract screening. Before seeing any AI label, the reviewer (R1, the author) screens a random 10% of records blind: ⌈0.10 × N⌉ records drawn with random.Random(20261010).sample over the sorted record IDs (screening/calibration.py). In parallel, an AI (Claude Opus 5.5 with a fixed prompt) labels every record include / unsure / exclude with a reason code and a note. R1 then reviews every record with the AI label visible and accepts or overrides it; R1's decision is final. If the AI labelled exclude any calibration record that R1 labelled include or unsure, R1 re-screens all AI-excluded records outside the calibration sample with the labels hidden. Records that R1 marks include or unsure go to full text. (3) Full-text screening: the AI drafts a proposal (eligible or not, primary exclusion reason, location of the case counts); R1 checks it against the text and decides. Stages 2 and 3 are AI-assisted and human-decided: a computer supervised by a human.

**Screened fields / blinding**
Title, abstract, year, venue, record type, language and DOI link are visible at title/abstract screening; author names are not shown, but the reviewer may open the DOI link. AI labels are hidden during the calibration and during the conditional blind re-screening; the decision files for these stages do not contain the labels. R1's calibration decisions are committed to the repository before any AI label is shown. The SHA-256 of the AI label file is committed when the AI run finishes, and the file itself after R1's calibration decisions. The AI sees only the record (title, year, venue, record type, abstract) with an opaque running number, never R1's decisions.

**Used exclusion criteria**
Title/abstract stage: the record clearly is (a) a review, editorial, commentary or letter without data; (b) a case report or series; (c) a study whose participants were all recruited because of misophonia or sound sensitivity (unless an unselected pool was screened); (d) a study measuring only hyperacusis, tinnitus, noise sensitivity, sensory over-responsivity or decreased sound tolerance without anything misophonia-specific; (e) qualitative, animal or purely theoretical; (f) not about misophonia. When in doubt, the record goes to full text. Full-text stage: E1–E5 above, plus no extractable count of cases with a denominator after author contact (I3 not met); one primary reason is recorded per excluded report.

**Screener instructions**
The AI screener's fixed prompt and JSON schema are in screening/llm_screener_prompt.md (attached; frozen with protocol v1.0). R1 applies the same eligibility criteria (protocol §8) with the rule "when in doubt, unsure". At title/abstract screening R1 labels include / unsure / exclude and, for exclusions, one reason: review/commentary; case report; sample recruited for misophonia; no misophonia-specific measure; qualitative or not empirical; off-topic; other.

**Screening reliability**
One human screener (R1) and one AI. Agreement in the blind calibration sample is reported: Cohen's κ for the three labels; κ and Gwet's AC1 for "full text" (include or unsure) vs exclude; AI sensitivity and specificity against R1 with Clopper–Pearson 95% CIs. Also reported: the number of AI labels R1 overrode, by direction; whether the anchoring safeguard was triggered; and, after full-text screening, the number of included studies whose records the AI had labelled exclude. If a fellow student volunteers and actually screens the same calibration sample blind, human–human κ is reported (code R2). No other screener is planned.

**Screening reconciliation procedure**
There is no second human to reconcile with. R1 resolves every difference between their own label and the AI label during verification, against the record (and the full text when needed); R1's decision is final. In the calibration sample, R1 sees their own blind label and the AI label side by side during verification.

**Sampling and sample size**
All eligible studies are included; there is no sampling of studies. Only the calibration sample is sampled: ⌈10%⌉ of the screening list, by the seeded procedure above. A pooled estimate requires at least three independent samples; strata with fewer are reported in tables and forest plots without pooling. Moderators other than the pre-specified multivariable model are tested only with at least 10 samples.

**Screening procedure justification**
Single-reviewer screening misses about 13% of eligible studies on average (Waffenschmidt et al., 2019). With no second human reviewer available, an AI drafts every label: LLM screeners reach high sensitivity on title–abstract screening (Oami et al., 2024). The human remains the decision-maker. The blind calibration sample measures the AI's error rate on this dataset before R1 sees any label, and the safeguard (blind re-screening of all AI-excluded records after any AI false negative) protects against R1 simply agreeing with the machine. The hash commitment of the AI labels makes the order of events checkable.

**Data management and sharing**
Search records (records_unique.jsonl, screening.csv, screening.ris), the raw exports of the final search, R1's calibration and verification decision files (Markdown, with their git history) and the parsed decisions (CSV), the AI labels with model, prompt hash and Claude Code version (JSONL), and the full-text decisions with reasons (CSV) are kept in a git repository and released on GitHub with a Zenodo DOI at submission. No embargo or access conditions.

**Miscellaneous screening details**
R1 screens in Markdown files generated by screening/screen_md.py: one block per record with a decision line, where R1 types + (include), ? (unsure), -1 to -7 (exclude with a reason) or, in verification files, = (accept the AI label shown); anything after the code is a note. Each file is committed blank before R1 starts and again when R1 finishes, and the script parses the files into CSV and lists records without a valid code. Non-English full texts are machine-translated by the AI assistant; R1 checks the numbers against the original tables. Multiple reports of one sample are linked, and the sample is counted once.

---

## Extraction

**Entities to extract**
Per sample (forms/samples.csv): report identifiers; publication status; language; country (and continent, WHO region and World Bank income group derived from it); setting; years of data collection; design; sampling method (probability, census, quota/online panel, convenience, snowball); whether misophonia or sounds were named at recruitment; population type and, for clinical samples, the diagnosis; inclusion and exclusion criteria; numbers invited, responding and analysed; response rate; age (mean, SD, range, age group); percentage female; informant; mode; instruments with language version and validation status; funding and conflicts of interest; JBI items 1–9 with notes; author contact. Per estimate (forms/estimates.csv): subgroup (all, female, male, age band, clinical subgroup); instrument; threshold exactly as applied; threshold source; authors' label; level (L0–L3 by protocol Table 1); time frame; cases; denominator; whether derived from a percentage; weighted percentage if reported; whether the authors call it primary; location in the report (page, table, figure).

**Extraction stages**
(1) Pilot on five studies: the extraction prompt and form are tested, then frozen and committed; any rule added goes to deviations.md. (2) Extraction: the AI assistant pre-fills every field with its source location (page, table or quote); the draft is stored unchanged. (3) Verification: R1 checks every field against the source and accepts or corrects it; key fields (sample size, case counts, instrument, threshold, population type, sampling) always against the source table. (4) Risk of bias: the AI drafts each JBI rating with a quote; R1 verifies every item. All stages are AI-assisted and human-decided.

**Extractor instructions**
forms/extraction_codebook.md (attached): field definitions, codes and rules (e.g., if text and table disagree, take the table; pool raw counts, record weighted percentages separately; extract each severity band as its own estimate; parent- and self-report separately; clinical subsamples inside community surveys as subgroup estimates). Thresholds are mapped to levels by forms/instrument_thresholds.csv; JBI decision rules are in forms/rob_jbi.md.

**Extractor masking**
None. The extractor is the author, who knows the research questions; masking is not feasible in a single-author review. The level mapping of instruments and thresholds is fixed in advance (protocol Table 1) so that it cannot be adjusted to the results.

**Extraction reliability**
One human extractor (R1) verifying an AI draft of every value; no independent human double extraction. We report the proportion of AI-drafted values that R1 corrected, overall and for the key fields, by comparing the stored drafts with the verified tables.

**Extraction reconciliation procedure**
R1 resolves every difference between the AI draft and the source by checking the source; R1's value is final. If the source is ambiguous, the corresponding author is contacted (one e-mail, one reminder); otherwise the value is coded NR and the ambiguity noted.

**Extraction procedure justification**
Single-author review without a second human extractor. Pre-filling by the AI with a source location for every value, and verification of every value by R1, gives each number two independent looks: the AI's reading and R1's check against the source. Key numbers are always checked against the source table. The corrections statistic shows how much the drafts needed fixing.

**Data management and sharing**
The AI drafts (JSON), the verified tables (CSV: samples.csv, estimates.csv), risk-of-bias ratings and author-contact log are kept in the git repository and released on GitHub with a Zenodo DOI at submission, under CC BY 4.0, with a codebook. No embargo.

**Miscellaneous extraction details**
Unknown values are coded NR, not applicable NA. Counts derived from percentages are rounded (cases = round(% × n / 100)) and flagged. Before extraction starts, protocol Table 1 is completed for every instrument found in the included studies, using only the instruments' development and validation papers, never the prevalence results of the included studies; the completion is logged as a clarification.

---

## Synthesis and Quality Assessment

**Planned data transformations**
Counts and denominators are analysed on the logit scale (log odds of being a case). Percentages without counts are converted to counts. Instrument thresholds are mapped to case-definition levels L0–L3 by protocol Table 1. Country is mapped to continent (UN M49), WHO region and World Bank income group in the year of data collection. Sex differences are expressed as log odds ratios (female vs male) from the sex-specific counts. One estimate per sample is selected per analysis by the rules in protocol §13 (L3 over L2 for the primary outcome; within a level, the authors' primary instrument, then the threshold recommended in Table 1, then the median logit).

**Missing data**
Missing counts or denominators: the corresponding author is contacted once with one reminder; if no data arrive, the estimate is not pooled and the study is listed among studies without extractable counts. Missing moderator values are coded NR; moderator analyses use the samples with data, and the number of samples is reported for each. No imputation.

**Data validation**
Key numbers are always checked against the source table; internal consistency checks by script (cases ≤ n, subgroup counts summing to the total, percentages matching counts within rounding); duplicate samples across reports are linked; retractions and expressions of concern are checked through Crossref/Retraction Watch data at extraction; influential estimates are examined with leave-one-out, studentised residuals and Cook's distance.

**Quality assessment**
JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data (nine items; Munn et al., 2014, 2015) with decision rules adapted to misophonia (forms/rob_jbi.md); items reported individually, no summary score; items 2 (sampling), 6 (valid identification) and 9 (response rate) define sensitivity analyses and enter as moderators. Certainty of the main pooled estimates: GRADE adapted for event rates (Iorio et al., 2015), downgrading for risk of bias, inconsistency (prediction interval), imprecision (CI half-width above 5 percentage points), indirectness and publication bias; summary-of-findings table.

**Synthesis plan**
Primary model: random-effects binomial–normal generalised linear mixed model on the logit scale (metafor::rma.glmm, measure = "PLO", ML), preferred over inverse-variance pooling of transformed proportions and over the Freeman–Tukey double arcsine. Reported: pooled prevalence with 95% CI and 95% prediction interval, τ² and I² (the prediction interval is interpreted, not I²). A pooled estimate needs at least three independent samples. Subgroups (non-clinical samples): case-definition level (L1/L2/L3); population type; age group (<13, 13–17, adults); continent (Asia / Europe / Americas / other). Clinical groups pooled per diagnosis when k ≥ 3. Moderators: three-level binomial model with all estimates (estimates within samples within studies; lme4::glmer, nested random intercepts), checked with metafor::rma.mv on logits with cluster-robust inference. The pre-specified multivariable model contains level, population type and probability sampling; the other moderators are exploratory, tested one at a time, each only when k ≥ 10. A variance component estimated at zero is dropped and the simpler model reported. Sex difference: random-effects log odds ratios (REML, Hartung–Knapp), with 95% CI and prediction interval. Tiers: primary = pooled L2/L3 prevalence in non-clinical samples; secondary = level-specific, population-type and clinical-group estimates and the sex difference; exploratory = single-moderator analyses. If a part of the plan cannot be executed (e.g., fewer than three samples), estimates are tabulated and shown in forest plots without pooling, and the reason is reported.

**Criteria for conclusions / inference criteria**
No significance thresholds drive the conclusions. Prevalence is interpreted through point estimates with 95% CIs and, for heterogeneity, 95% prediction intervals; moderator effects through their estimates and CIs (95%), with exploratory moderators labelled as such. Certainty of each main estimate is stated with GRADE.

**Synthesist blinding**
None. The synthesist is the author, who knows the research questions. The analysis plan, estimate-selection rules and level mapping are fixed in this registration before any data are extracted.

**Synthesis reliability**
One synthesist (the author). The analysis code is drafted by the AI assistant, checked by the author, and released; all results are reproducible from the released data and code.

**Synthesis reconciliation procedure**
Not applicable (one synthesist).

**Publication bias analyses**
Funnel-plot asymmetry tests are unreliable for proportions (Hunter et al., 2014) and are not used for inference. Instead: a plot of logit prevalence against its standard error, a regression of prevalence on 1/√n, and a comparison of peer-reviewed with grey-literature estimates. Selective reporting within studies is checked by comparing the case definitions announced in the methods with those reported.

**Sensitivity analyses / robustness checks**
On the primary outcome: (1) only probability or census samples; (2) only validated instruments with a validated cut-off (JBI item 6 = yes); (3) response rate ≥ 60% or not applicable; (4) excluding samples where the study topic was disclosed at recruitment; (5) excluding preprints, theses and conference abstracts; (6) excluding samples with n < 100; (7) inverse-variance random-effects pooling of logits (REML, Hartung–Knapp) instead of the GLMM; (8) the highest and the lowest threshold per sample instead of the selection rule; (9) leave-one-out and influence diagnostics; (10) L2 only (excluding L3).

**Synthesis procedure justification**
The binomial–normal GLMM models within-study binomial variation exactly and avoids the bias of transformed proportions for small or extreme prevalences (Stijnen et al., 2010; Lin & Chu, 2020) and the misleading Freeman–Tukey back-transformation (Schwarzer et al., 2019). Prediction intervals describe the spread expected in a new population (IntHout et al., 2016), which matters more than I² in prevalence meta-analyses (Migliavaca et al., 2022). The three-level model uses every reported estimate without double-counting samples. The case-definition level is the key moderator because the instruments and cut-offs are the main suspected source of the 5%–49% spread.

**Synthesis data management and sharing**
R scripts, their outputs, sessionInfo and the analysis data (CSV) are released on GitHub with a Zenodo DOI at submission, under open licences (code MIT, data CC BY 4.0). No embargo.

**Miscellaneous synthesis details**
Every change to this plan after registration is dated, justified and logged in deviations.md, and reported in the paper. The AI assistant's role is disclosed in the Methods and in the AI declaration.
