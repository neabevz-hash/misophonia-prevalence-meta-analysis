# Поля для регистрации в PROSPERO (к протоколу v1.0 от 2026-10-10)

**2026-10-10: зарегистрировать нельзя.** Новая форма PROSPERO принимает только обзоры вмешательств, «Review of incidence or prevalence» помечен «coming soon». Обзор зарегистрирован на OSF (10.17605/OSF.IO/39MQ2). Если PROSPERO откроет обзоры распространённости до начала выписывания данных, регистрируем по полям ниже.

Регистрирует автор: https://www.crd.york.ac.uk/PROSPERO/ → Login → Register a review (нужен аккаунт). Тексты ниже вставляются в поля формы как есть. В новой форме PROSPERO поля сгруппированы по разделам, поэтому порядок здесь примерный. Если какого-то поля в форме нет, его пропускаем. Полный протокол прикладываем ссылкой на регистрацию OSF (поле «Availability of full protocol» или аналог).

**Порядок:**
1. Протокол v1.0 заморожен (git-тег `misophonia-prereg-v1.0`).
2. Регистрация на OSF — по `registration/osf.md`. OSF даёт ссылку и DOI.
3. Форма PROSPERO — сразу после OSF, со ссылкой на OSF. Номер CRD пришлите мне, я впишу его в протокол и README.

Регистрацию PROSPERO принимает, пока не началось выписывание данных. Отбор я начинаю после регистрации на OSF и отправки формы в PROSPERO.

**Стадия обзора:** финальный поиск начат 2026-10-10 после регистрации на OSF. В поле стадий: preliminary searches — completed; formal searches — started (или completed, если я уже сообщил, что поиск закончен); всё остальное — not started.

---

**Review title.** Prevalence of misophonia across case definitions and populations: a systematic review and meta-analysis

**Condition or domain being studied.** Misophonia: a disorder of decreased tolerance to specific sounds, or stimuli associated with them, that evoke strong negative emotional, physiological and behavioural responses not seen in most people (consensus definition, Swedo et al., 2022). It is not classified in ICD-11 or DSM-5-TR. Older names: selective sound sensitivity syndrome, soft sound sensitivity.

**Rationale for the review.** Single-study estimates of clinically significant misophonia range from about 5% in probability samples of adults in Germany and the USA to 49% in UK medical students. Much of this spread appears definitional: at least ten instruments are in use, with different cut-offs and labels. The only systematic review of misophonia prevalence (Gowda & Prabhu, 2024; 12 studies) did not pool estimates or analyse sources of variation. Two prevalence reviews registered in PROSPERO (CRD42021267820, CRD42024598262) state no intention to publish and are not published. A pooled, definition-aware estimate is needed for clinical services, for the debate on diagnostic criteria and for planning research.

**Review objectives.** (1) To estimate the prevalence of clinically significant misophonia (questionnaire cut-off for clinical significance, or diagnosis by interview) in non-clinical populations. (2) To estimate prevalence at three case-definition levels (symptom level; clinically significant by validated cut-off; diagnosed by interview) and quantify how much between-study variance the case definition and instrument explain. (3) To estimate prevalence by population type (probability general-population samples, other general-population samples, university students, children and adolescents) and in clinical groups. (4) To examine heterogeneity by age, sex composition, continent (Asia vs other regions) and country income, survey mode, disclosure of the study topic at recruitment, risk of bias and year. (5) To estimate the female-to-male odds ratio of clinically significant misophonia.

**Searches.** PubMed, Europe PMC (including preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org, Authorea), OpenAlex, Semantic Scholar, DataCite (theses, posters, repository deposits), OpenAIRE and CORE (repository aggregators), SciELO and, if its search servers can be reached from our network, LILACS (BVS). Forward citation search of the development papers of ten misophonia instruments (A-MISO-S, MQ, AMISOS-R, MisoQuest, S-Five, DMQ, BMQ-R, DVMSQ, SMS-Adolescent, SMS-Adult) through OpenAlex. Backward and forward citation searching of included studies and relevant reviews. Theses via DataCite, OpenAlex, OpenAIRE and CORE. Google Scholar (two queries, first 200 records each, via Publish or Perish; only records not already found are screened). Condition terms only (misophonia and synonyms in English, Portuguese, Spanish, Italian, Turkish, German, French, Russian, Japanese, Korean), no date or language limits, no prevalence filter. Search strings and code are in the full protocol. A pilot search on 9 October 2026 found 1,245 unique records to screen and all 12 studies of an independent seed set; with DataCite and OpenAIRE added (10 October 2026), 1,335.

**Search for unpublished studies.** Yes: preprints, theses, conference abstracts; corresponding authors contacted for missing counts.

**Language restrictions.** None; non-English full texts are machine-translated and the numbers checked against the original tables.

**Date restrictions.** None.

**Population — included.** People of any age who were not recruited on the basis of misophonia or sound sensitivity: general population, students, school pupils, workers, other non-clinical samples (main analysis); clinical samples recruited for another condition (psychiatric, neurodevelopmental, audiological), analysed separately by condition.

**Population — excluded.** Samples recruited because of misophonia, sound sensitivity, self-identified misophonia or interest in misophonia (misophonia clinics, support groups, treatment trials for misophonia).

**Intervention(s) / exposure(s).** Not applicable (prevalence review). Condition identified by a misophonia-specific self- or informant-report instrument, a clinical interview, or explicit diagnostic criteria. Excluded: measures of noise sensitivity, hyperacusis, sensory over-responsivity or decreased sound tolerance without a misophonia-specific case definition.

**Comparator(s) / control.** Not applicable.

**Study design — included.** Cross-sectional surveys; baseline waves of cohorts; psychometric validation studies; screening phases of experimental or clinical studies that report case counts in an unselected pool; theses, preprints and conference abstracts with sufficient data. Any language, any year.

**Study design — excluded.** Reviews, editorials, case reports and series, qualitative studies without counts; case definitions derived from the distribution of the same sample (e.g., top 10%), whose prevalence is fixed by construction.

**Context.** Any country, setting and year.

**Main outcome(s).** Prevalence (proportion) of clinically significant misophonia (level L2: a cut-off defined by the instrument's developers or a validation study as clinically significant, moderate or higher, or anchored on clinical interview; or level L3: diagnosis by clinical or structured interview with explicit criteria) in non-clinical populations. Instrument thresholds are mapped to levels in advance (full protocol, Table 1), regardless of the label used by study authors. Measure of effect: proportion with 95% CI and 95% prediction interval.

**Additional outcome(s).** Prevalence at the symptom level (L1) and at the interview level (L3) separately; prevalence in each clinical group; odds ratio (female vs male) for L2/L3 misophonia.

**Data extraction (selection and coding).** One reviewer (the author) makes every decision; an AI assistant (Claude Opus 5.5 through Claude Code; the title/abstract prompt is frozen with the protocol, later prompts are piloted on five studies and frozen before use) prepares drafts that the reviewer verifies one by one. Title/abstract: the reviewer first screens a seeded random 10% of records blind (calibration; seed 20261010); in parallel the AI labels every record (include/unsure/exclude with a reason), and the hash of the AI label file is committed before the calibration is unblinded; the reviewer then reviews every record with the AI label visible and accepts or overrides it. If the AI labels exclude any calibration record that the reviewer labelled include or unsure, the reviewer re-screens all AI-excluded records with labels hidden. Agreement (kappa, Gwet's AC1, AI sensitivity and specificity), overrides and whether the safeguard was triggered are reported. Full text: the AI proposes eligibility, exclusion reason and the location of case counts; the reviewer decides. Extraction: the AI pre-fills the piloted form with a source location for every value; the reviewer verifies every value against the source (sample size, case counts, instrument, threshold and population always against the source table). Authors are contacted once, with one reminder, for missing counts.

**Risk of bias (quality) assessment.** JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data (nine items), with decision rules adapted to misophonia. The AI assistant drafts each rating with a supporting quote; the reviewer verifies every item and decides. Items reported individually (no summary score); items on sampling, valid case identification and response rate define the sensitivity analyses.

**Strategy for data synthesis.** Random-effects binomial-normal generalised linear mixed model (logit link; metafor rma.glmm) with 95% CI and 95% prediction interval; at least three independent samples per pooled estimate. One estimate per sample per analysis (interview-based if available, else the authors' primary instrument, else the threshold recommended in the protocol, else the median). A three-level binomial model using all estimates (estimates within samples within studies) tests moderators: case-definition level, instrument, population type, probability sampling, age, sex composition, continent and country income, mode, topic disclosure, risk-of-bias items, publication status and year of data collection. Pre-specified multivariable model: level, population type, probability sampling; the other moderators are exploratory, tested only with at least 10 samples. Sex difference: random-effects log odds ratios (REML, Hartung–Knapp). Certainty: GRADE adapted for event rates.

**Analysis of subgroups or subsets.** Case-definition level (L1/L2/L3); population type; age group (children <13, adolescents 13–17, adults); continent (Asia / Europe / Americas / other); clinical groups by diagnosis (OCD, anxiety, depression, bipolar disorder, ADHD, autism, Tourette syndrome/tics, tinnitus, hyperacusis, hearing loss, other) when k ≥ 3.

**Sensitivity analyses.** Restriction to probability or census samples; to validated instruments with validated cut-offs; to response rate ≥60%; excluding samples where misophonia/sounds were named at recruitment; excluding preprints, theses and abstracts; excluding n < 100; inverse-variance pooling of logits instead of GLMM; highest and lowest threshold per sample; leave-one-out and influence diagnostics; L2 only.

**Reporting bias assessment.** Funnel-plot tests are not used for proportions. Instead: plot of logit prevalence against standard error, regression of prevalence on 1/√n, peer-reviewed vs grey literature, and comparison of announced and reported case definitions.

**Certainty assessment.** GRADE adapted for event rates (Iorio et al., 2015): risk of bias, inconsistency (prediction interval), imprecision, indirectness, publication bias.

**Review team.** Martin Rekhert, Turan University, Almaty, Kazakhstan; ORCID 0009-0001-2402-2031; mrexert@gmail.com (named contact, guarantor).

**Funding.** None.

**Conflicts of interest.** None.

**Country.** Kazakhstan.

**Stage of the review.** Preliminary searches: completed (pilot search 9 October 2026; DataCite test 10 October 2026). Formal searches: started on 10 October 2026, after the OSF registration (automated sources and SciELO done or running; the Google Scholar export pending) — если к моменту отправки я скажу, что поиск закончен, отметьте completed, 10 October 2026. Piloting of the study selection process: not started. Formal screening of search results against eligibility criteria: not started. Data extraction: not started. Risk of bias (quality) assessment: not started. Data analysis: not started.

**Review timeline.** Start: 9 October 2026 (pilot search). Anticipated completion: 30 April 2027 (дата нужна только для формы, как и в OSF).

**Availability of full protocol.** Full protocol v1.0, forms, search and screening code, AI screener prompt and pilot search logs are registered on OSF: https://doi.org/10.17605/OSF.IO/39MQ2 (registration https://osf.io/39mq2).

**Publication intention.** The review will be published in English in a peer-reviewed journal; a preprint will be posted on submission.

**Keywords.** misophonia; prevalence; epidemiology; meta-analysis; sound sensitivity; decreased sound tolerance; case definition
