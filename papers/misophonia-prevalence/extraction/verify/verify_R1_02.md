# Проверка выписывания — файл 2 из 10

Черновик заполнил ИИ (Claude Opus 5.5) по полному тексту; у каждого значения указано место и цитата. Проверяете вы, один проход.

**Как проверять выборку:**
1. Откройте полный текст по ссылке у исследования.
2. **Ключевые числа** — сверить с таблицей или текстом статьи всегда: в таблице оценок шкала, порог, уровень, случаи и n; под таблицей n_analysed, population, sampling.
3. Остальные поля и пункты JBI: проверить, что значение есть в цитате и место указано верно.
4. Неверное — исправьте строкой в блоке «Правки» этой выборки (по одной правке на строку):
   - `n_analysed = 1400`, `sampling = convenience` — поле выборки;
   - `E2.cases = 103`, `E2.level = L1` — поле оценки E2 (subgroup, instrument, threshold, level, cases, n, time_frame, primary_for_authors и др.);
   - `E2 удалить` — убрать оценку;
   - `+ оценка: subgroup=all; instrument=MQ; threshold=MSS>=7; level=L2; cases=50; n=300; location=Table 2` — добавить оценку;
   - `jbi_6 = no` — пункт JBI;
   - `выборка удалить: причина` — если это не отдельная выборка или её нельзя брать;
   - после `#` — комментарий для Claude.
5. Когда выборка проверена, напишите `да` после «Проверено:».

**Подсказки в файле:** «⚠ Проверка скриптом» — места, где скрипт нашёл повод присмотреться (уровень не совпадает с Таблицей 1, n оценки не равно n выборки, числа расходятся с независимым проходом ИИ по полному тексту, L2 по самодельным вопросам). «Расхождения в тексте» — ошибки самих авторов, которые нашёл ИИ (например, процент не равен случаи/n); в этом случае ИИ берёт числа из таблицы статьи. Посчитанные ИИ значения (суммы полос, % × n) выделены строкой **расчёт**.

**Уровни** (Таблица 1 и правила G1–G12, `forms/table1_completion.md`): L1 — симптомы; L2 — клинически значимый порог; L3 — интервью с критериями; L0 — любой «раздражающий звук»; E3 — порог по распределению той же выборки; E2 — не специфично для мизофонии; NR — определение не установить. L0, E3, E2 и NR в объединение не идут, но в таблицы статьи попадают.
**population:** gp_probability, gp_other, university_students, medical_students, school_pupils, workers, other_nonclinical, clinical. **sampling:** probability, census, quota, convenience, snowball, NR.

---

## ST011 · Gülsoy 2026 · Nursing open

Основной отчёт R0077: [текст](../../fulltext/text/R0077.txt) — «Misophonia Levels and Care Behaviours in Intensive Care Nurses: A Descriptive, Cross-Sectional and Relational Study.» — [DOI](https://doi.org/10.1002/nop2.70504)
Расхождения в тексте: The count of 58 with MSS>=7 is given only in the Discussion. It does not appear in Results or in any table, and the authors call 58/131 'the majority'. 58 is also the number of participants with children in Table 1. The age SD (3.50) does not fit 21/131 (16%) being aged 36-50 with a mean of 29.86. In Table 2 the maximum for Emotions and Behaviours is 25, and the maximum for the total is 68 while the subscale maxima are 28 and 25. The authors say they used stratified random sampling but also describe the participants as volunteers who agreed to take part. Table 3 has internal errors, for example totals that are lower than their subscales for weekly working hours and education.
Заметка ИИ: One sample and one L2 estimate (MQ MSS>=7, Turkish version validated): 58/131.

### ST011-1 · ICU nurses, Sivas Cumhuriyet University Hospital, Turkey, n=131
Отчёты: R0077 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **58 / 131** | 44.3 | Discussion | «58 of the participants scored 7 and above in the section of the misophonia scale that determines clinical severity. These findings indicate that the majority of the participants had misophonic sensitivity.» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2, recommended); у авторов: «clinically significant misophonia; 'misophonic sensitivity'»; главная у авторов: no; период: current; заметка: Reported only in the Discussion; 58/131 = 44.3%. Authors call this 'the majority', which it isn't. Authors' primary outcomes are mean scores and correlation; no prevalence is labelled as the main estimate.

**Ключевые поля выборки:**
- **n_analysed: 131** — Table 1; Discussion — «n = 131»
- **population: workers** — Materials and Methods — «the sample of the study consists of intensive care nurses»
- **sampling: probability** — Materials and Methods — «The sample of the study consisted of 131 nurses who agreed to participate in the study without any limitations. The sample was selected by the stratified random sampling method.»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Materials and Methods — «all the nurses working in the paediatric and adult ICU in a Sivas Cumhuriyet University Application and Research Hospital»
- setting: workplace (intensive care units of one university hospital) — Materials and Methods — «there have a total of 10 different ICU from 3 different types of intensive care, including paediatric, newborn, and adult»
- data_years: 2023 — Application of Data Collection Tools — «The study was conducted between September 1, 2023 and September 15, 2023.»
- design: cross-sectional — Materials and Methods — «The research is descriptive, cross-sectional, and relational study type.»
- topic_disclosed: yes — Application of Data Collection Tools — «It was explained to the participants that the concept of misophonia, which is not very well known and may impair the quality of care of the study, will contrib…»
- inclusion_exclusion: ICU nurses who could speak and understand Turkish and gave written consent; incomplete questionnaires to be excluded (none were) — Research Inclusion/Exclusion Criteria — «Intensive care nurses who could speak and understand Turkish and had a written consent form participated in the study voluntarily.»
- n_invited: NR — Materials and Methods — «The universe of the research consisted of all the nurses working in the paediatric and adult ICU»
- n_responded: 131 — Results — «The study consisted of 131 intensive care nurses to participate in the study.»
- response_rate: NR — NA
- age_mean: 29.86 — Table 1 — «Age (X = 29.86 ± 3.50)»
- age_sd: 3.50 — Table 1 — «Age (X = 29.86 ± 3.50)»
- age_min: NR — Table 1 — «20–35 | 110 | 83.96»
- age_max: NR — Table 1 — «36–50 | 21 | 16.04»
- age_group: adults — Table 1 — «20–35 | 110 | 83.96 ... 36–50 | 21 | 16.04»
- pct_female: 69.50 — Table 1 — «Female | 91 | 69.50»
- informant: self — Application of Data Collection Tools — «The intensive care nurses completed the forms independently within two days»
- mode: paper — Application of Data Collection Tools — «The forms were handed over to the intensive care nurses in envelopes for them to complete in hard copy.»
- instruments: Misophonia Questionnaire (Wu et al. 2014), Turkish version (Deniz Sakarya & Çakmak 2022), incl. Misophonia Severity Scale — Misophonia Scale section — «The Misophonia Scale, developed by Wu et al. (2014)... The Turkish validity of the scale was made by Deniz Sakarya and Çakmak in 2022»
- instrument_validated_in_language: yes — Misophonia Scale section — «The Turkish validity of the scale was made by Deniz Sakarya and Çakmak in 2022 and the Cronbach Alpha internal consistency coefficient of the scale was found t…»
- pub_status: journal — Header — «Nursing open; DOI: 10.1002/nop2.70504»
- language: English — Full text — «Misophonia Levels and Care Behaviours in Intensive Care Nurses: A Descriptive, Cross-Sectional and Relational Study»
- funding_coi: Funding: nothing to report; no conflicts of interest declared — Funding; Conflicts of Interest — «The authors have nothing to report. ... The authors declare no conflicts of interest.»
- notes: Sampling: the authors say they used stratified random sampling but also describe the participants as nurses who volunteered or agreed. The size of the frame (total ICU nurses) is not reported, so the code 'probability' rests only on the authors' statement. The prevalence count (58 with MSS>=7) appears only in the Discussion, not in Results or the tables. 58 is also the number with children in Table 1, which may be a coincidence or an error. An age SD of 3.50 is not plausible with a mean of 29.86 and 16% aged 36-50. The sentence about alpha is ambiguous ('In this study, it was stated...above 0…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Target is ICU nurses of this hospital; frame = all nurses in its ICUs. — Materials and Methods — «The universe of the research consisted of all the nurses working in the paediatric and adult ICU»
2. способ отбора: **unclear** — Stratified random sampling claimed, but participants were volunteers who agreed; frame size and selection procedure not described. — Materials and Methods — «131 nurses who agreed to participate in the study without any limitations. The sample was selected by the stratified random sampling method.»
3. размер выборки: **no** — n = 131 < 385. — Results — «The study consisted of 131 intensive care nurses»
4. описание выборки и условий: **yes** — Age, sex, setting, country (Sivas hospital) and dates reported. — Table 1; Application of Data Collection Tools — «Female | 91 | 69.50 ... conducted between September 1, 2023 and September 15, 2023»
5. охват (пропуски): **yes** — No missing or incomplete forms. — Research Exclusion Criteria — «since there were no missing or unanswered forms, all questionnaires were included in the study»
6. валидность определения случая: **yes** — MQ Severity Scale >=7, Turkish version with published validation. — Misophonia Scale section; Discussion — «Markings of 7 and above in this section represent clinically significant misophonia (Wu et al. 2014). The Turkish validity of the scale was made by Deniz Sakar…»
7. единое надёжное измерение: **yes** — Same paper questionnaire for all; internal consistency reported. — Misophonia Scale section — «In this study, it was stated that the Cronbach alpha value calculated for the total scale and sub-dimensions was above 0.90.»
8. статистика (числитель и знаменатель): **yes** — Numerator 58 and denominator 131 clear; CI calculable though not given. — Discussion — «58 of the participants scored 7 and above in the section of the misophonia scale that determines clinical severity»
9. отклик: **unclear** — Number of nurses approached / total ICU nurses not reported; response rate unknown. — Materials and Methods — «The sample of the study consisted of 131 nurses who agreed to participate in the study»

Правки:
- 

Проверено: да
---

## ST012 · Hansen 2026 · Human brain mapping

Основной отчёт R0082: [текст](../../fulltext/text/R0082.txt) — «Selective Disruption of Salience-Network Anterior Insula Connectivity in Misophonia: A Disorder-Specific Neural Signature.» — [DOI](https://doi.org/10.1002/hbm.70468)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R0941 (ST071): Both University of Oklahoma students with the MQ (777 vs 343); R0082 calls its data 'collected for other purposes' and does not say it reuses Norris et al. 2022
Расхождения в тексте: Oklahoma: 1009 consented, 23% removed, which gives 777 (1009 × 0.77 = 777). Checks: 147/776 = 18.9% (reported 19%); 240/777 = 30.9% (reported 31%). The results text says 'above the cutoff of 30' and 'above the cutoff of 7', but the Method and model sections define misophonia as MSS ≥ 7 and MQ total ≥ 30. These were taken as ≥. Table 1 gender adds to 186 + 580 + 11 = 777. WAND: 31/162 = 19.1% before quality control; 29/153 = 19.0% after 9 participants were excluded for fMRI quality control. 31 − 29 = 2 above-cut-off cases among the excluded participants (inferred, not stated).
Заметка ИИ: This is a neuroimaging study with prevalence data as a by-product. Oklahoma (USA university students, MQ English) gives L2 estimates. For the WAND UK sample, misophonia was predicted from the AASP, so its estimates are E2 (G9): listed, not pooled. Possible overlap of the Oklahoma sample with R0941 (ST071) is flagged in the notes.

### ST012-1 · University of Oklahoma students, online survey, USA, n=777
Отчёты: R0082 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **147 / 776** | 18.9 | Method, Misophonia | «Self-reported severity ranged from zero to 15 (mean = 4.4), with 147 (19%) falling above the cutoff of 7, consistent with reported prevalence in other college samples» |
| E2 | all | MQ · MQ total (Symptom + Emotions-and-Behaviors) >=30 | **L2** | **240 / 777** | 30.9 | Method, Misophonia | «Participants ranged in their total MQ scores between zero and 63 (mean = 24.4), with 240 (31%) scoring above the cutoff of 30.» |

- E1: источник порога: developer paper; правило: MQ row; L2 MSS >=7 (recommended, G11); у авторов: «"clinical" misophonia»; главная у авторов: no; период: current; заметка: Text says 'above the cutoff of 7'; Method uses '≥ 7' for misophonia definition. Denominator 776 (one missing severity item, 99.9%). Authors do not label it as the main estimate.
- E2: источник порога: validation paper; правило: MQ row; L2 total >=30; у авторов: «likely indicates the presence of misophonia»; главная у авторов: no; период: current; заметка: Cut-off from Möllmann et al. 2023. Text says 'above the cutoff of 30'; Results define misophonia as MQ total ≥ 30.

**⚠ Проверка скриптом (обратите внимание):**
- E2: n оценки не равно n_analysed выборки (776): проверьте знаменатель

**Ключевые поля выборки:**
- **n_analysed: 776** — Method, Misophonia — «99.9% (N = 776) responding to the single severity item»
- **population: university_students** — Method, Oklahoma Sample — «recruited from the Psychology department research pool and the general university population via mass email»
- **sampling: convenience** — Method, Oklahoma Sample — «recruited from the Psychology department research pool and the general university population via mass email»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — Method, Oklahoma Sample — «These data (hereafter "Oklahoma dataset") were collected for other purposes at the University of Oklahoma»
- setting: university (psychology research pool and general university population via mass email) — Method, Oklahoma Sample — «include 777 individuals recruited from the Psychology department research pool and the general university population via mass email»
- data_years: NR — Method, Oklahoma Sample — «Data collection was approved by the University of Oklahoma Institutional Review Board (IRB#16450)»
- design: cross-sectional — Method, Oklahoma Sample — «participants completed an online survey containing a variety of misophonia, clinical, and demographic assessments»
- topic_disclosed: NR — Method, Oklahoma Sample — «participants completed an online survey containing a variety of misophonia, clinical, and demographic assessments»
- inclusion_exclusion: Consented participants; removed if failing attention checks, straight-lining, or not completing the majority of questions — Method, Oklahoma Sample — «23% of respondents were removed for failing attention checks, providing the same answer for all questions, or for not completing the majority of questions»
- n_invited: NR — Method, Oklahoma Sample — «the general university population via mass email»
- n_responded: 1009 — Method, Oklahoma Sample — «In total, 1009 participants consented to the survey»
- response_rate: NR — Method, Oklahoma Sample — «In total, 1009 participants consented to the survey»
- age_mean: 19.4 — Table 1 — «Mean | 30 years | 19.4 years»
- age_sd: 3.3 — Table 1 — «SD | 10.9 years | 3.3 years»
- age_min: 18 — Table 1 — «Range | 18.3–63.7 years | 18–63 years»
- age_max: 63 — Table 1 — «Range | 18.3–63.7 years | 18–63 years»
- age_group: adults — Table 1 — «Range | 18.3–63.7 years | 18–63 years»
- pct_female: 74.6 — Table 1 — «Female | 104 | 64.2 | 580 | 74.6»
- informant: self — Abstract — «a second adult self-report sample from Oklahoma (N = 777)»
- mode: online — Method, Oklahoma Sample — «participants completed an online survey»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), English: Symptom Scale, Emotions and Behaviors Scale, Misophonia Severity Scale — Method, Misophonia — «All participants in the Oklahoma dataset completed the Misophonia Questionnaire (MQ) (Wu et al. 2014).»
- instrument_validated_in_language: yes — Method, Misophonia — «All participants in the Oklahoma dataset completed the Misophonia Questionnaire (MQ) (Wu et al. 2014).»
- pub_status: journal — Citation header — «Human brain mapping; DOI: 10.1002/hbm.70468»
- language: English — Full text — «Selective Disruption of Salience-Network Anterior Insula Connectivity in Misophonia: A Disorder-Specific Neural Signature»
- funding_coi: Réseau en Bio-Imagerie du Quebec, FRQS, Killam Trusts, OU Data Institute for Societal Challenges seed funding; no conflicts of interest declared — Funding; Conflicts of Interest — «This work was supported by Réseau en Bio-Imagerie du Quebec, Fonds de Recherche du Québec—Santé, Killam Trusts, and seed funding from the OU Data Institute for…»
- notes: Possible overlap with R0941 (ST071): both University of Oklahoma students with the MQ (777 vs 343); R0082 calls its data 'collected for other purposes' and does not say it reuses Norris et al. 2022. Data collection years not reported. Of 1009 consenting, 23% (~232) were removed for quality/incompleteness. Study is a neuroimaging paper; Oklahoma sample used to train a model predicting MQ total from AASP. Text says 'above the cutoff' (30; 7) while the Method uses '≥ 7' and '≥ 30'; operators assumed >=. n_analysed set to 776 (MSS item); MQ total denominator 777. Neither estimate explicitly calle…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Frame was the psychology research pool plus mass email to the university population; unclear whether it covers all enrolled students. — Method, Oklahoma Sample — «recruited from the Psychology department research pool and the general university population via mass email»
2. способ отбора: **no** — Volunteer opt-in from a research pool and mass email (convenience). — Method, Oklahoma Sample — «recruited from the Psychology department research pool and the general university population via mass email»
3. размер выборки: **yes** — n = 776/777 >= 385. — Method, Misophonia — «100% of participants (N = 777) responding to each of the 17 subscale items and 99.9% (N = 776) responding to the single severity item»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection missing. — Table 1; Method, Oklahoma Sample — «Oklahoma dataset (N = 777) ... Mean | 19.4 years»
5. охват (пропуски): **no** — 23% of consenting respondents removed (partly for not completing most questions) and not handled; MQ missingness among retained only 0.1%. — Method, Oklahoma Sample — «In total, 1009 participants consented to the survey; 23% of respondents were removed for failing attention checks, providing the same answer for all questions,…»
6. валидность определения случая: **yes** — Primary L2 definition MQ Severity Scale >= 7, English original (Wu et al. 2014). — Method, Misophonia — «Scores seven or greater are suggested to indicate "clinical" misophonia (Wu et al. 2014; Möllmann et al. 2023).»
7. единое надёжное измерение: **unclear** — Same instrument, online mode and threshold for all, but no internal consistency reported in this report. — Method, Misophonia — «All participants in the Oklahoma dataset completed the Misophonia Questionnaire (MQ) (Wu et al. 2014).»
8. статистика (числитель и знаменатель): **yes** — Counts and denominators given (147/776; 240/777); CI calculable. — Method, Misophonia — «with 240 (31%) scoring above the cutoff of 30. Self-reported severity ranged from zero to 15 (mean = 4.4), with 147 (19%) falling above the cutoff of 7»
9. отклик: **no** — Mass-email/pool recruitment with no denominator of invited people; no non-response handling. — Method, Oklahoma Sample — «In total, 1009 participants consented to the survey»

Правки:
- 

Проверено: да
### ST012-2 · WAND neuroimaging database, general adult population, Wales (UK), n=162
Отчёты: R0082 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | other · predicted MQ total >=30 (MQ total predicted from 30 AASP items via regression) | **E2** | **31 / 162** | 19.1 | Results, Application of Model to WAND | «participants ranged in their predicted MQ scores between 8.9 and 45.1 (mean = 24.2), with 31 (19%) scoring above the cutoff of 30» |
| E2 | all (after fMRI quality control) | other · predicted MQ total >=30 (MQ total predicted from AASP) | **E2** | **29 / 153** | 19.0 | Results, Anterior Insula Connectivity Changes ... | «labeling participants with predicted MQ total scores ≥ 30 as "patients" (N = 29) and MQ total scores < 30 as "controls" (N = 124) (Möllmann et al. 2023)» |

- E1: источник порога: validation paper; правило: G9: misophonia score predicted from a non-misophonia instrument (MQ predicted from AASP); у авторов: «clinical definition of misophonia»; главная у авторов: no; период: current; заметка: Cut-off 30 from Möllmann et al. 2023. Authors say the percentage matches prior UK prevalence; not explicitly called the main estimate. 'above' vs '≥' wording.
- E2: источник порога: validation paper; правило: G9: misophonia score predicted from a non-misophonia instrument; у авторов: «"patients"»; главная у авторов: no; период: current; **расчёт: n = 29 patients + 124 controls = 153**; заметка: Subset after excluding 9 participants for fMRI quality issues; same definition as the 31/162 estimate.

**Ключевые поля выборки:**
- **n_analysed: 162** — Results, Application of Model to WAND — «In the WAND dataset, participants ranged in their predicted MQ scores between 8.9 and 45.1 (mean = 24.2), with 31 (19%) scoring above the cutoff of 30»
- **population: gp_other** — Abstract — «comprising participants recruited from the general adult population and assessed for sensory sensitivity, anxiety, depression, and autistic traits»
- **sampling: NR** — Abstract — «comprising participants recruited from the general adult population»

**Остальные поля:**
- clinical_group: NA — NA
- country: GBR — Limitations and Future Directions — «the sample was of "healthy" adults from the general population in the UK»
- setting: community (volunteers in open-access Welsh Advanced Neuroimaging Database, Cardiff University) — Method, WAND Sample; Ethics Statement — «The Welsh Advanced Neuroimaging Database (WAND) is a newly released open-access, large-scale, multimodal dataset»
- data_years: NR — Method, WAND Sample — «The Welsh Advanced Neuroimaging Database (WAND) is a newly released open-access, large-scale, multimodal dataset (McNabb et al. 2025).»
- design: other — Method, WAND Sample — «The entire dataset comprises 178 adults enrolled across eight unimodal sessions of neuroimaging, cognitive tasks, and questionnaire assessments.»
- topic_disclosed: no — Method, Oklahoma Sample — «Since the WAND dataset did not explicitly provide a misophonia questionnaire to participants»
- inclusion_exclusion: WAND adults who completed both 3T functional MRI and trait questionnaires (162 of 178) — Method, WAND Sample — «only participants who completed both the 3T functional MRI and trait questionnaires were included in analyses, resulting in 162 individuals»
- n_invited: NR — Method, WAND Sample — «The entire dataset comprises 178 adults»
- n_responded: 178 — Method, WAND Sample — «The entire dataset comprises 178 adults enrolled across eight unimodal sessions»
- response_rate: NR — Method, WAND Sample — «The entire dataset comprises 178 adults»
- age_mean: 30 — Table 1 — «Mean | 30 years | 19.4 years»
- age_sd: 10.9 — Table 1 — «SD | 10.9 years | 3.3 years»
- age_min: 18.3 — Table 1 — «Range | 18.3–63.7 years»
- age_max: 63.7 — Table 1 — «Range | 18.3–63.7 years»
- age_group: adults — Table 1 — «Range | 18.3–63.7 years»
- pct_female: 64.2 — Table 1 — «Female | 104 | 64.2»
- informant: self — Method, Sensory Sensitivity — «All participants in both the WAND and the Oklahoma datasets completed the Adolescent/Adult Sensory Profile (AASP)»
- mode: NR — Method, Sensory Sensitivity — «Assessments in the WAND dataset were completed in full by all respondents.»
- instruments: No direct misophonia measure; MQ total score predicted from 30 items of the Adolescent/Adult Sensory Profile (AASP, English) via a regression model trained in the Oklahoma sample — Method, Deriving a Misophonia Score — «we built a general linear regression model in the Oklahoma dataset that could predict misophonia (MQ total score) from one's sensory profile (AASP); the model …»
- instrument_validated_in_language: no — Results, Prediction Accuracy of Model in Oklahoma Sample — «Classification of the Oklahoma test set into individuals with misophonia (MQ total ≥ 30) versus controls (MQ < 30) was accomplished by the model with 0.48 sens…»
- pub_status: journal — Citation header — «Human brain mapping; DOI: 10.1002/hbm.70468»
- language: English — Full text — «Selective Disruption of Salience-Network Anterior Insula Connectivity in Misophonia»
- funding_coi: Réseau en Bio-Imagerie du Quebec, FRQS, Killam Trusts, OU Data Institute seed funding; no conflicts of interest declared — Funding; Conflicts of Interest — «This work was supported by Réseau en Bio-Imagerie du Quebec, Fonds de Recherche du Québec—Santé, Killam Trusts ... The authors declare no conflicts of interest.»
- notes: Misophonia not measured directly: MQ total predicted from AASP (model sensitivity 0.48, specificity 0.90 in Oklahoma test set) -> E2 by rule G9; listed, not pooled. Secondary analysis of open dataset (McNabb et al. 2025); recruitment method and data years not described in this report. 31/162 above the cut-off before fMRI quality control; 29/153 'patients' after 9 exclusions.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Sampling frame of WAND not described in this report. — Abstract — «comprising participants recruited from the general adult population»
2. способ отбора: **unclear** — Recruitment method not described. — Abstract — «comprising participants recruited from the general adult population»
3. размер выборки: **no** — n = 162 < 385. — Method, WAND Sample — «resulting in 162 individuals»
4. описание выборки и условий: **unclear** — Age, sex, country and setting reported; dates missing. — Table 1; Limitations — «WAND dataset (N = 162) ... Female | 104 | 64.2»
5. охват (пропуски): **yes** — 162 of 178 (91%) had fMRI and questionnaires; AASP complete for all. — Method, WAND Sample; Sensory Sensitivity — «Assessments in the WAND dataset were completed in full by all respondents.»
6. валидность определения случая: **no** — Misophonia score predicted from a non-misophonia instrument (AASP); no validated misophonia measure. — Limitations and Future Directions — «the participants with neuroimaging data used in this study were not directly assessed for misophonia; misophonia scores were predicted using a linear regressio…»
7. единое надёжное измерение: **unclear** — Same AASP-based model for all, but no reliability reported. — Results, Application of Model to WAND — «we applied this model to the AASP responses in the WAND dataset»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (31/162); CI calculable. — Results, Application of Model to WAND — «with 31 (19%) scoring above the cutoff of 30»
9. отклик: **unclear** — Response/participation rate not reported. — Method, WAND Sample — «The entire dataset comprises 178 adults»

Правки:
- 

Проверено: да
---

## ST013 · Jafari 2026 · Journal of Affective Disorders Reports

Основной отчёт R0094: [текст](../../fulltext/text/R0094.txt) · [PDF](../../fulltext/pdf/R0094.pdf) — «Hyperacusis, misophonia, and mental health in young adults in Canada: Estimated prevalence and associated factors» — [DOI](https://doi.org/10.1016/j.jadr.2026.101170)
Расхождения в тексте: 1) Prevalence of at least mild misophonia: 24.50% (abstract, 3.1, 4.1), 24.60% with Wilson CI (2.4.1), and Table 3 n1 = 139 (139/606 = 22.9%). Cases are not printed. Table 3 does not state its denominator, and it also disagrees with Table 1 for tinnitus (71 vs 77) and with the text for hyperacusis (49 vs 8.60% x 606 = 52). Because Table 3 is not a prevalence table and its denominator may differ, the derived 148 (24.50% x 606) is used; the reviewer should decide whether 139 should replace it. 2) Age range 18-32 in the results contradicts eligibility 19-32. 3) Percent female is 77.05% in Table 1 and 77.10% in the text; the table value is used. 4) The abstract says 12.70% constant tinnitus; Table 1 says 77/606 = 12.71%.
Заметка ИИ: MAQ bands in this study are version A (subclinical 0-11, mild 12-24, moderate 25-37), giving L1 >= 12 and L2 >= 25. The ROC-anchored >= 24 was not reported. The breakdown by band (Fig. 1F) is not given in the text, and no prevalence is given by sex or age.

### ST013-1 · Young adults, Halifax (Dalhousie University campuses + social media/email), Canada, n=606
Отчёты: R0094 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MAQ · MAQ>=12 (mild or more; version A bands) | **L1** | **148 / 606** | 24.4 | Abstract p.1; Results 3.1 p.4; 2.4.1 p.4 | «24.50% of participants reported mild or greater misophonia symptoms» |
| E2 | all | MAQ · MAQ>=25 (moderate or more; version A bands) | **L2** | **52 / 606** | 8.6 | Abstract p.1; Results 3.1 pp.4-5 | «24.50% reported at least mild misophonia, including 8.60% with moderate or greater severity» |

- E1: источник порога: validation paper; правило: MAQ row, version A L1 >=12; G1 cumulative; у авторов: «at least mild misophonia»; главная у авторов: yes; период: NR; **расчёт: 24.50% x 606 = 148.47 -> 148**; заметка: Section 2.4.1 gives 24.60% (95% CI 21.30-28.20%), i.e. about 149/606. Table 3 gives a misophonia index group of n1 = 139 (22.9%) on an unclear denominator. The source of the severity bands is not cited; the paragraph cites Cervin et al. 2023.
- E2: источник порога: validation paper; правило: MAQ row, version A L2 >=25; G1 cumulative; у авторов: «moderate or greater symptom severity»; главная у авторов: no; период: NR; **расчёт: 8.60% x 606 = 52.12 -> 52**; заметка: Band cut-off not anchored (JBI 6 = no); falls under sensitivity analysis 2.

**Ключевые поля выборки:**
- **n_analysed: 606** — Page 4, 3.1; Table 1 — «data from 606 participants with complete questionnaires were included in the analysis»
- **population: gp_other** — Page 4, 3.1; Page 8, 4.4 — «64.40% were university students»
- **sampling: convenience** — Page 2, 2.2 Participants — «Participants were recruited using a multi-method strategy that included study flyers ... social media announcements, and email outreach.»

**Остальные поля:**
- clinical_group: NA — NA
- country: CAN — Page 2, 2.2 Participants — «study flyers displayed across Dalhousie University campuses in Halifax, Nova Scotia, Canada, social media announcements, and email outreach»
- setting: university (campus flyers at Dalhousie University) plus social media and email outreach; community young adults, mostly students — Page 2, 2.2 Participants; Page 4, 3.1 — «recruited using a multi-method strategy that included study flyers displayed across Dalhousie University campuses ... social media announcements, and email out…»
- data_years: NR — Page 2, 2.2 Participants — «The study received ethical approval from the Dalhousie University Research Ethics Board (REB file #2025-8228).»
- design: cross-sectional — Page 8, 4.4 — «the cross-sectional design precludes conclusions about temporal or causal relationships»
- topic_disclosed: NR — Page 2, 2.2 — «Participants were recruited using a multi-method strategy that included study flyers»
- inclusion_exclusion: Age 19-32; no confirmed neuropsychiatric disorders; able to read and understand English. Only participants with complete questionnaires analysed (606 of 726). — Page 2, 2.2; Page 4, 3.1 — «Eligibility criteria included age between 19 and 32, having no confirmed neuropsychiatric disorders, and being able to read and understand English.»
- n_invited: NR — Page 2, 2.2 — «study flyers ... social media announcements, and email outreach»
- n_responded: 726 — Page 4, 3.1 — «A total of 726 participants took part in this study, and data from 606 participants with complete questionnaires were included in the analysis.»
- response_rate: NR — Page 4, 3.1 — «A total of 726 participants took part in this study, and data from 606 participants with complete questionnaires were included»
- age_mean: 20.08 — Page 4, 3.1 — «Participants ranged in age from 18 to 32 years (mean = 20.08 ± 3.86 years)»
- age_sd: 3.86 — Page 4, 3.1 — «(mean = 20.08 ± 3.86 years)»
- age_min: 18 — Page 4, 3.1 — «Participants ranged in age from 18 to 32 years»
- age_max: 32 — Page 4, 3.1 — «Participants ranged in age from 18 to 32 years»
- age_group: adults — Page 4, 3.1 — «Participants ranged in age from 18 to 32 years»
- pct_female: 77.05 — Table 1 — «Gender Woman 467 77.05»
- informant: self — Page 2, 2.1 — «completed a demographic form and validated self-report screening instruments for hyperacusis, misophonia, anxiety, and depression»
- mode: mixed — Page 2, 2.2 — «Data were collected either electronically using REDCap ... or on paper for in-person participation.»
- instruments: Misophonia Assessment Questionnaire (MAQ), 21 items, English — Page 3, 2.3.3 — «The MAQ is a 21-item self-report measure that assesses the frequency and severity of misophonia-related emotional and social impacts (Cervin et al., 2023).»
- instrument_validated_in_language: yes — Page 3, 2.3.3 — «Although the MAQ was formally evaluated in youth populations, it has also been used in adult samples»
- pub_status: journal — Page 1, header — «Journal of Affective Disorders Reports 26 (2026) 101170»
- language: English — Full text — «Hyperacusis, misophonia, and mental health in young adults in Canada: Estimated prevalence and associated factors»
- funding_coi: Dalhousie University Research Establishment Funds (R36503); NSERC Discovery Grants (R41534, R41535). No competing interests. — Page 9, Funding source; Declaration of competing interest — «supported by the Dalhousie University Research Establishment Funds (Grant # R36503) and the Natural Sciences and Engineering Research Council of Canada (NSERC)…»
- notes: Cases are not printed as counts; derived from percentages x 606. The prevalence figures disagree with each other: 24.50% (abstract, results, discussion), 24.60% (Wilson CI, sec. 2.4.1), and Table 3 misophonia index n1 = 139 (22.9% of 606). Table 3 also differs from Table 1 for tinnitus (71 vs 77) and from the text for hyperacusis (49 vs about 52), so its denominator is unclear. The age range (18-32) contradicts the eligibility rule (19-32). The MAQ English validation was in youth (Cervin 2023); the adult use has no stated validation. Population coded gp_other because recruitment was not limit…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The target is young adults in Canada, but the frame was campus flyers, social media and email at one university. — Page 2, 2.2 — «study flyers displayed across Dalhousie University campuses in Halifax, Nova Scotia, Canada, social media announcements, and email outreach»
2. способ отбора: **no** — Volunteer opt-in convenience recruitment. — Page 2, 2.2 — «Participants were recruited using a multi-method strategy»
3. размер выборки: **yes** — n = 606, which is at least 385. — Page 4, 3.1 — «data from 606 participants with complete questionnaires were included in the analysis»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; the dates of data collection are not. — Page 4, 3.1; Table 1 — «Participants ranged in age from 18 to 32 years (mean = 20.08 ± 3.86 years), and more than two-thirds identified as women (77.10%).»
5. охват (пропуски): **no** — 120 of 726 (16.5%) were excluded for incomplete questionnaires, with no handling of the missing data. — Page 4, 3.1 — «A total of 726 participants took part in this study, and data from 606 participants with complete questionnaires were included in the analysis.»
6. валидность определения случая: **no** — The primary definitions are MAQ severity-band cut-offs (>=12, >=25) without interview or ROC anchoring; >=24 was not used. — Page 3, 2.3.3 — «Severity categories are classified as subclinical (0-11), mild (12-24), moderate (25-37), severe (38-50), and extreme (51-63).»
7. единое надёжное измерение: **no** — Same instrument and threshold for all and alpha = 0.906 in the sample, but online and paper modes were mixed with no comparison. — Page 2, 2.2; Page 4, 3.1 — «Data were collected either electronically using REDCap ... or on paper for in-person participation.»
8. статистика (числитель и знаменатель): **unclear** — A Wilson CI is given, but no counts are printed and the figures are inconsistent (24.50% vs 24.60% vs Table 3 n = 139). — Page 4, 2.4.1; Table 3 — «24.60% (95% CI: 21.30%–28.20%) for at least mild misophonia»
9. отклик: **no** — Open recruitment with no denominator of invited people, and non-response not handled. — Page 2, 2.2 — «study flyers ... social media announcements, and email outreach»

Правки:
- 

Проверено: да
---

## ST014 · Küçükkelepçe 2026 · The Psychiatric quarterly

Основной отчёт R0118: [текст](../../fulltext/text/R0118.txt) · [PDF](../../fulltext/pdf/R0118.pdf) — «Prevalence of Misophonia in High School Students: A Cross Sectional Study.» — [DOI](https://doi.org/10.1007/s11126-026-10264-9)
Расхождения в тексте: The counts check out: the Table 3 bands add up to 1006 (168+338+359+89+52). Moderate+severe+very severe = 500, which matches the clinically significant count. Table 4 sex counts (345+155) and grade counts (79+87+229+105) each add up to 500. Severe+very severe = 141/1006 = 14.0%, which matches the 14% in the Discussion. The abstract says the study looked at 'children presenting to a public hospital for any reason'. This contradicts the Methods, which describe recruitment in six schools. The text speaks of 'second year' vs 'third and fourth years' of high school, while the tables use 9th-12th grade. Page 10 says prevalence is higher in 'first-year' students, which fits the 9th-grade Table 4 figure (63.2%). Reference 18 is cited for two different Turkish prevalence figures: 21% in the Introduction and 38% in the Discussion. The 35 non-participants include both absentees and excluded studen…
Заметка ИИ: There is one sample. Its primary estimate is MQ Severity Scale >=7: 500/1006, level L2. The report never gives the MSS band cut-points. The L1 estimate (>=4, n=838) and the >=10 estimate (n=141) assume the standard Wu et al. bands, so please check them. Age is not reported. The grade subgroups are extracted as age-band proxies.

### ST014-1 · High school students, Kahta district (Adıyaman), Türkiye, n=1006
Отчёты: R0118 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **500 / 1006** | 49.7 | Page 10, Table 3; Page 5, Results | «Clinically significant misophonia 500 (49.7)» |
| E2 | all | MQ · MSS>=4 (mild or more; band boundaries not printed in report) | **L1** | **838 / 1006** | 83.3 | Page 10, Table 3 | «Mild 338 (33.6) Moderate 359 (35.7) Severe 89 (8.8) Very Severe 52 (5.2)» |
| E3 | all | MQ · MSS>=10 (severe or more; band boundaries not printed in report) | **L2** | **141 / 1006** | 14.0 | Page 10, Table 3; Page 12, Discussion | «When cases with only severe or very severe sound sensitivity are considered in our sample, the prevalence drops to 14%» |
| E4 | female | MQ · MSS>=7 | **L2** | **345 / 680** | 50.7 | Page 11, Table 4 | «Female 335 (49.3) 345 (50.7) 0.344» |
| E5 | male | MQ · MSS>=7 | **L2** | **155 / 326** | 47.5 | Page 11, Table 4 | «Male 171 (52.5) 155 (47.5)» |
| E6 | 9th grade | MQ · MSS>=7 | **L2** | **79 / 125** | 63.2 | Page 11, Table 4 | «9th grade 46 (36.8) 79 (63.2) 0.002» |
| E7 | 10th grade | MQ · MSS>=7 | **L2** | **87 / 161** | 54.0 | Page 11, Table 4 | «10th grade 74 (46) 87 (54)» |
| E8 | 11th grade | MQ · MSS>=7 | **L2** | **229 / 507** | 45.2 | Page 11, Table 4 | «11th grade 278 (54.8) 229 (45.2)» |
| E9 | 12th grade | MQ · MSS>=7 | **L2** | **105 / 213** | 49.3 | Page 11, Table 4 | «12th grade 108 (50.7) 105 (49.3)» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 recommended L2; у авторов: «clinically significant misophonia»; главная у авторов: yes; период: NR; заметка: Equals moderate 359 + severe 89 + very severe 52 = 500. The 7+ threshold is stated without a citation; it is Wu et al. 2014's band.
- E2: источник порога: developer paper; правило: MQ row; MSS >=4 L1; G1 sum of bands; у авторов: «mild or more sound sensitivity»; главная у авторов: no; период: NR; **расчёт: 338 + 359 + 89 + 52 = 838 from Table 3**; заметка: Assumes the 'mild' band starts at MSS 4 (Wu et al. bands); the report does not print the band cut-points.
- E3: источник порога: developer paper; правило: MQ row; G2 threshold above L2 cut-off; G1 sum of bands; у авторов: «severe or very severe sound sensitivity»; главная у авторов: no; период: NR; **расчёт: 89 + 52 = 141 from Table 3**; заметка: Assumes the 'severe' band starts at MSS 10 (Wu et al. bands).
- E4: источник порога: developer paper; правило: MQ row; MSS >=7 recommended L2; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR
- E5: источник порога: developer paper; правило: MQ row; MSS >=7 recommended L2; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR
- E6: источник порога: developer paper; правило: MQ row; MSS >=7 recommended L2; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; заметка: Grade used as a proxy for age band; ages not reported.
- E7: источник порога: developer paper; правило: MQ row; MSS >=7 recommended L2; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; заметка: Grade used as a proxy for age band; ages not reported.
- E8: источник порога: developer paper; правило: MQ row; MSS >=7 recommended L2; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; заметка: Grade used as a proxy for age band; ages not reported.
- E9: источник порога: developer paper; правило: MQ row; MSS >=7 recommended L2; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; заметка: Grade used as a proxy for age band; ages not reported.

**Ключевые поля выборки:**
- **n_analysed: 1006** — Page 10, Table 3 — «No clinically significant misophonia 506 (50.3) Clinically significant misophonia 500 (49.7)»
- **population: school_pupils** — Page 3, Study Design and Participants — «The study sample consisted of high school students enrolled in six different high schools in Kahta»
- **sampling: convenience** — Page 3, Study Design and Participants — «Schools were selected from different regions of the district, and students included from a variety of grades. Eight classes were selected from each school»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Page 3, Study Design and Participants — «six different high schools in Kahta, a district in the southeastern province of Adıyaman, Türkiye»
- setting: school (six high schools in Kahta district, Adıyaman province) — Page 3, Study Design and Participants — «high school students enrolled in six different high schools in Kahta, a district in the southeastern province of Adıyaman, Türkiye»
- data_years: 2025 — Page 3, Study Design and Participants — «between February 15 and April 30, 2025»
- design: cross-sectional — Page 3, Study Design and Participants — «This study was designed as an observational, descriptive, and cross-sectional investigation.»
- topic_disclosed: NR — Page 3, Study Design and Participants — «Participants completed a Sociodemographic Data Form and the Misophonia Questionnaire, both of which were administered by previously trained data collectors»
- inclusion_exclusion: Students in 8 selected classes per school (all grades), with informed consent from student and guardian; excluded chronic illness (e.g., epilepsy) and foreign nationals — Page 3, Study Design and Participants; Page 4, Ethical Appr… — «Students with chronic illnesses such as epilepsy, and foreign nationals were excluded from the study.»
- n_invited: 1041 — Page 3, Study Design and Participants — «A total of 35 students did not take part due to absence on the day of data collection or because they met the exclusion criteria. ... A total of 1,006 students»
- n_responded: 1006 — Page 3, Study Design and Participants — «A total of 1,006 students who met the inclusion criteria and provided informed consent were included in the study.»
- response_rate: 95 — Page 3, Study Design and Participants — «Approximately 95% of students in the selected classrooms participated in the study.»
- age_mean: NR — Not reported
- age_sd: NR — Not reported
- age_min: NR — Not reported
- age_max: NR — Not reported
- age_group: adolescents — Page 1, Keywords; Page 6, Table 1 (Grade) — «Keywords Misophonia · Adolescent · Epidemiology · Prevalence»
- pct_female: 67.6 — Page 5, Results — «A total of 1,006 high school students participated in the study, with 67.6% (n = 680) identifying as female.»
- informant: self — Page 10, Discussion — «the reliance on self-report surveys and the lack of clinical evaluations may have contributed to the high prevalence rates observed»
- mode: NR — Page 10, Discussion; Page 3 — «the data collection was conducted through in-person administration of questionnaires in school settings»
- instruments: Misophonia Questionnaire (MQ), Turkish version (Deniz Sakarya & Çakmak), incl. Symptom Scale, Emotions and Behaviors subscales and Misophonia Severity Scale — Page 4, Misophonia Questionnaire (MQ) — «Initially developed by Wu et al. and adapted into Turkish by Deniz Sakarya and Çakmak, the MQ evaluates the presence of misophonia symptoms»
- instrument_validated_in_language: yes — Page 4, Misophonia Questionnaire (MQ) — «The Turkish version demonstrated strong internal consistency with a Cronbach's alpha of 0.89 ... and test-retest reliability of 0.78 [18].»
- pub_status: journal — Page 1, header — «Psychiatric Quarterly https://doi.org/10.1007/s11126-026-10264-9»
- language: English — Full text — «Prevalence of Misophonia in High School Students: A Cross Sectional Study»
- funding_coi: No study funding (open access funding by TÜBİTAK); authors declare no competing interests — Page 15, Funding; Competing interests — «Open access funding provided by the Scientific and Technological Research Council of Türkiye (TÜBİTAK). This study did not receive any funding. ... The authors…»
- notes: Age not reported at all (only grades 9-12); age_group 'adolescents' inferred from high-school setting and keyword, some 12th graders may be 18. n_invited 1041 derived as 1006 + 35 non-participants (35 includes both absentees and excluded students); response rate as reported (~95%). Mode: in-person administration by trained data collectors in schools; paper vs. electronic not stated. Abstract wrongly describes sample as 'children presenting to a public hospital for any reason', whereas Methods describe school-based recruitment. MSS band boundaries (normal/mild/moderate/severe/very severe) not …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is high school students in Türkiye; the frame was selected classes in six schools of a single district. — Page 14, Limitations — «restriction to schools in a single district limit the generalizability of the findings to the broader adolescent population»
2. способ отбора: **no** — Schools and classes were picked non-randomly (by region/grade coverage); no probability sampling described, though nearly all pupils in the selected classes took part. — Page 3, Study Design and Participants — «Schools were selected from different regions of the district ... Eight classes were selected from each school, ensuring that classes from each grade level were…»
3. размер выборки: **yes** — n = 1006 >= 385. — Page 3 — «all eligible students (n = 1,006) were included in the analysis»
4. описание выборки и условий: **unclear** — Sex, setting, country and dates are reported; age is not reported. — Page 3; Page 5, Results — «with 67.6% (n = 680) identifying as female»
5. охват (пропуски): **yes** — MSS bands account for all 1006 participants; no missing misophonia data. — Page 10, Table 3 — «Normal 168 (16.7) Mild 338 (33.6) Moderate 359 (35.7) Severe 89 (8.8) Very Severe 52 (5.2)»
6. валидность определения случая: **yes** — Primary estimate is MQ Severity Scale >=7 in the Turkish MQ version, which has a published adaptation. — Page 4, Misophonia Questionnaire (MQ) — «A score of 7 or higher on this item indicates clinically significant misophonia.»
7. единое надёжное измерение: **yes** — Same instrument and threshold for everyone, given by trained data collectors; reliability of the Turkish version reported from the source. — Page 3; Page 4 — «administered by previously trained data collectors by the researchers ... The Turkish version demonstrated strong internal consistency with a Cronbach's alpha …»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (500/1006), so a CI can be calculated; no weighting design. — Page 5, Results — «Overall, 49.7% of the participants (n = 500) were identified as having clinically significant levels of misophonia.»
9. отклик: **yes** — About 95% of students in the selected classes took part. — Page 3 — «Approximately 95% of students in the selected classrooms participated in the study.»

Правки:
- 

Проверено: да
---

## ST015 · Pfeiffer 2026 · BMC psychiatry

Основной отчёт R0150: [текст](../../fulltext/text/R0150.txt) — «Misophonia in a large treatment-seeking child and adolescent sample in mental health care in Germany and Austria.» — [DOI](https://doi.org/10.1186/s12888-026-07979-1)
Расхождения в тексте: The Measures section gives the cut-off as 'a total sum score of 49 or higher'. Results and the Table 2 note say '> 49'. The case range in Table 4 (49-153) shows that >=49 was applied. The denominator also varies: Table 1 gives N=214 and Table 4 gives N=211 (66+145), because the authors excluded the 3 participants with no sounds and no Part 2. 193 of 214 reported at least one sound, so 21 reported none. Only 3 skipped Part 2, which suggests about 18 with no sound still completed Part 2, against the stated skip rule. Table 1 subgroup gender counts add up to 120 females and 68 males in the 211 analysed, out of 121 and 70 in total.
Заметка ИИ: Under rule G10, the primary estimate uses 214 as the denominator (66/214). The authors' own figure is 66/211 = 31.28%. Funding and COI statements were not part of the supplied text. Supplementary materials (age distribution, Tables S1/S2/B) were not available.

### ST015-1 · Treatment-seeking children and adolescents, 4 child/adolescent mental health sites, Germany and Austria, n=214
Отчёты: R0150 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SMS-Adolescent · SMS-A Part 2 >=49 (text also says '> 49'; case range 49-153) | **L2** | **66 / 214** | 30.8 | Results, Characteristics of repetitive sounds; Table 4; Sta… | «A sub-sample of n = 66 participants (31.28%) met the SMS-A cutoff criterion of > 49 indicating probable misophonia.» |
| E2 | female | SMS-Adolescent · SMS-A Part 2 >=49 | **L2** | **42 / 121** | 34.7 | Table 1 | «female ... 121 (56.54) / 42 (63.63) / 78 (53.79)» |
| E3 | male | SMS-Adolescent · SMS-A Part 2 >=49 | **L2** | **13 / 70** | 18.6 | Table 1 | «male ... 70 (32.71) / 13 (19.69) / 55 (37.93)» |
| E4 | all | SMS-Adolescent · >=1 (misophonia-relevant) repetitive sound endorsed on SMS-A Part 1 | **L0** | **193 / 214** | 90.2 | Results, Characteristics of repetitive sounds | «Regarding (misophonia-relevant) repetitive sounds, n = 193 (90.19%) reported at least one sound (see Table 2).» |

- E1: источник порога: developer paper; правило: SMS-Adolescent row: L2 >=49 in samples other than Multisense; G10 denominator; у авторов: «probable misophonia; above the clinical cut-off»; главная у авторов: yes; период: NR; **расчёт: G10: the 3 participants who reported no sound and skipped Part 2 counted as non-cases: 211 + 3 = 214; 66/214 = 30.84%. Authors: 66/211 = 31.28%.**; заметка: Authors' denominator is 211 (Table 4). The German SMS-A has not been validated; excluded in sensitivity analysis 2. Possible misophonia referrals (~10-15) may inflate the estimate.
- E2: источник порога: developer paper; правило: SMS-Adolescent row; G10 denominator; у авторов: «probable misophonia»; главная у авторов: no; период: NR; **расчёт: Cases from the with-misophonia column of Table 1 (42); n = all females in the total sample (121); 42/121 = 34.7%. 42 + 78 = 120, so 1 female was among the 3 no…**; заметка: Prevalence by sex not reported by the authors; derived from Table 1.
- E3: источник порога: developer paper; правило: SMS-Adolescent row; G10 denominator; у авторов: «probable misophonia»; главная у авторов: no; период: NR; **расчёт: Cases from the with-misophonia column of Table 1 (13); n = all males in the total sample (70); 13/70 = 18.6%. 13 + 55 = 68, so 2 males were among the 3 non-com…**; заметка: Derived from Table 1.
- E4: источник порога: study's own; правило: Trigger endorsement only (adhoc row L0 rule); у авторов: «bothered by at least one (misophonia-relevant) repetitive sound»; главная у авторов: no; период: NR; заметка: Trigger endorsement only; listed, not pooled.

**Ключевые поля выборки:**
- **n_analysed: 214** — Table 1; Table 4 — «Total sampleN = 214»
- **population: clinical** — Participants — «sought and/ or received treatment for any mental health problem at one of the participating child and adolescent mental health care facilities»
- **sampling: convenience** — Procedure — «Children and adolescents, along with their legal guardians, were approached by trained project staff before, during or after their regular outpatient or inpatient assessment or treatment session.»

**Остальные поля:**
- clinical_group: mixed_psychiatric — Participants — «sought and/ or received treatment for any mental health problem»
- country: MULTI: DEU, AUT — Procedure — «recruited in outpatient and inpatient settings from four different sites in Germany and Austria»
- setting: clinic: child and adolescent psychiatry/psychotherapy outpatient and inpatient services (Ulm, Bielefeld, Calw/Böblingen/Weil der Stadt, Vienna) — Procedure — «recruited in outpatient and inpatient settings from four different sites in Germany and Austria»
- data_years: 2022-2024 — Procedure — «between November 2022 and January 2024»
- design: cross-sectional — Method — «anonymous questionnaire survey with children and adolescents from a general mental health care treatment seeking population in a cross-sectional study design w…»
- topic_disclosed: NR — Limitations (10) — «The response rate for participation and the exact wording used in solicitation of participants were not systematically recorded.»
- inclusion_exclusion: Age 10-21; seeking/receiving treatment for any mental health problem at a participating facility; German proficiency; written consent (plus guardians if <16). No exclusion criteria. — Participants — «(1) were between 10 and 21 years old, (2) sought and/ or received treatment for any mental health problem ... There were no exclusion criteria.»
- n_invited: NR — Limitations (10) — «The response rate for participation ... were not systematically recorded.»
- n_responded: 214 — Participants; Results — «Altogether N = 214 children and adolescents were included in the study.»
- response_rate: NR — Limitations (10) — «The response rate for participation and the exact wording used in solicitation of participants were not systematically recorded.»
- age_mean: 14.73 — Table 1 — «M = 14.73(SD = 2.16, range = 10–21)»
- age_sd: 2.16 — Table 1 — «M = 14.73(SD = 2.16, range = 10–21)»
- age_min: 10 — Table 1 — «M = 14.73(SD = 2.16, range = 10–21)»
- age_max: 21 — Table 1 — «M = 14.73(SD = 2.16, range = 10–21)»
- age_group: mixed — Participants; Table 1 — «were between 10 and 21 years old»
- pct_female: 56.54 — Table 1 — «female ... 121 (56.54)»
- informant: self — Limitations (2) — «this study only used self-report data due to feasibility reasons»
- mode: paper — Procedure — «The data was collected in paper-pencil format together with trained project staff.»
- instruments: Sussex Misophonia Scale for Adolescents (SMS-A), German translation (Part 1 sound checklist; Part 2 39 symptom items); self-generated questions on onset, coping, context — Measures — «The questionnaire was translated for this project in accordance with current translation guidelines by the WHO [26] ... The German version of the measure has n…»
- instrument_validated_in_language: no — Measures; Limitations (3) — «The German version of the measure has not been validated yet.»
- pub_status: journal — Header — «Year: 2026; venue: BMC psychiatry; DOI: 10.1186/s12888-026-07979-1»
- language: English — Full text — «Misophonia in a large treatment-seeking child and adolescent sample in mental health care in Germany and Austria»
- funding_coi: NR (funding and conflict-of-interest statements not included in the supplied text) — Full text — «NR»
- notes: Two of the four sites offered specific misophonia outpatient consultations. Assessors estimated that about 10-15 participants may have been referred for this expertise; they cannot be identified or removed, so prevalence may be modestly overestimated. Authors' prevalence: 66/211 = 31.28% (they excluded 3 participants with no sounds and no Part 2). Under G10 those 3 are non-cases, so the extracted denominator is 214. The SMS-A cut-off of 49 is the 90th percentile of the Multisense sample in Rinaldi et al. 2022. That is an external sample here, so the estimate is not E3. Prevalence by age band …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Four sites, two with known misophonia consultations, do not cover treatment-seeking youth in German/Austrian mental health care. — Limitations (1) — «Two out of the four study sites offered specific outpatient consultations for misophonia, which may have led some families to seek assessment at these centers»
2. способ отбора: **no** — Patients approached by staff and volunteered; not consecutive or random. — Procedure — «were approached by trained project staff ... They were informed about the study and invited to participate.»
3. размер выборки: **no** — n = 214 < 385 (whole sample, not a clinical subgroup). — Results — «The study sample comprised N = 214 children and adolescents.»
4. описание выборки и условий: **yes** — Age, sex, setting, countries and dates all reported. — Table 1; Procedure — «between November 2022 and January 2024»
5. охват (пропуски): **yes** — 1 participant excluded for missing data, 3 with no Part 2; item-level imputation; missing <10%. — Statistical analysis — «One participant was excluded ... n = 3 cases had to be excluded from the sub-sample analysis»
6. валидность определения случая: **no** — SMS-Adolescent >=49 is a percentile-based cut-off with no anchoring, and the German version has not been validated. — Measures — «The German version of the measure has not been validated yet.»
7. единое надёжное измерение: **yes** — Same paper self-report instrument and threshold for everyone; alpha reported in sample. — Measures — «The self-report of misophonic symptoms demonstrated excellent internal consistency (Cronbach’s α = 0.97) in this study.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given (66 of 211); CI calculable. — Results; Table 4 — «A sub-sample of n = 66 participants (31.28%) met the SMS-A cutoff criterion»
9. отклик: **unclear** — Response rate not recorded. — Limitations (10) — «The response rate for participation ... were not systematically recorded.»

Правки:
- 

Проверено: да
---

## ST016 · Prabhu 2026 · Research Square

Основной отчёт R0158: [текст](../../fulltext/text/R0158.txt) · [PDF](../../fulltext/pdf/R0158.pdf) — «Prevalence and Demographic Influences of Misokinesia and Misophonia in Adults in India» — [DOI](https://doi.org/10.21203/rs.3.rs-5659312/v1)
Расхождения в тексте: Internal inconsistency: the reported co-occurrence of misophonia and misokinesia (8.89%, about 40/450) is higher than the misokinesia prevalence (5.34%, about 24/450). This is impossible if both figures are 'any' prevalence. 5.34% x 450 = 24.03, and 24/450 = 5.33%, so the misokinesia percentage does not match a whole count exactly. 16.89% x 450 = 76.0, which matches 76/450 exactly. One possibility is that 16.89% and 5.34% are 'only one condition' figures, which would make any misophonia 116/450 (25.8%). The text does not confirm this. There are no tables. Figures 1-2 are scatter plots of score against age, with no counts.
Заметка ИИ: One sample, one estimate at level NR. The preprint does not state which MAQ threshold, or whether the screen alone, defines misophonia. No counts, CIs, sex-specific figures, data-collection dates or recruitment method are reported. A reviewer should check whether a published journal version gives the case definition and counts.

### ST016-1 · Online survey of adults, India (Mysore-based), n=450
Отчёты: R0158 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MAQ · not stated: yes/no screen positive and MAQ completed (MAQ bands 0-11 subclinical, 12-24 mild, ...); exact threshold for 'misophonia' not given | **NR** | **76 / 450** | 16.9 | Page 2, Abstract; Page 5, Results | «The study found that 16.89% of participants experienced misophonia, highlighting its prevalence among Indian adults with normal hearing.» |

- E1: источник порога: study's own; правило: MAQ row; G6 definition not determinable (two-stage design, G10); у авторов: «experienced misophonia; prevalence of misophonia»; главная у авторов: yes; период: NR; **расчёт: 16.89% x 450 = 76.0 -> 76 (76/450 = 16.89%)**; заметка: Case definition unclear: it could be screen-positive alone or a MAQ band (e.g., >=12 mild). Because co-occurrence (8.89%) is higher than misokinesia (5.34%), 16.89% may mean 'misophonia only'. If so, any misophonia would be 76 + 40 = 116/450 (25.8%). Not resolvable from the text.

**Ключевые поля выборки:**
- **n_analysed: 450** — Page 2, Abstract; Page 5, Results — «included 450 adults (240 females and 210 males) aged 18-50 years»
- **population: gp_other** — Page 4, Participants and Study Design — «All participants were adults aged between 18 and 50 years and reported normal hearing with no history of otological complaints»
- **sampling: NR** — Page 4, Participants and Study Design — «Researchers recruited 450 participants, comprising 210 males and 240 females, representing diverse regions across India.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: IND — Page 4, Participants and Study Design — «Researchers recruited 450 participants, comprising 210 males and 240 females, representing diverse regions across India.»
- setting: community adults recruited online (Google Forms survey; study run from Mysore) — Page 4, Participants and Study Design; Data Collection and … — «was conducted in Mysore using a cross-sectional survey design ... Data was collected via an online survey distributed through Google Forms.»
- data_years: NR — NR — «NR»
- design: cross-sectional — Page 4, Participants and Study Design — «conducted in Mysore using a cross-sectional survey design»
- topic_disclosed: NR — Page 4, Data Collection and Procedure — «Participants completed standardized questionnaires to assess misokinesia and misophonia symptoms»
- inclusion_exclusion: Adults 18-50 y with self-reported normal hearing and no otological complaints; excluded known auditory or visual disorders, cognitive impairments, or primary complaints such as hearing loss — Page 4, Participants and Study Design — «Individuals with known auditory or visual disorders, cognitive impairments, or primary complaints like hearing loss were excluded to maintain a focused sample.»
- n_invited: NR — NR — «NR»
- n_responded: 450 — Page 4, Participants and Study Design — «Researchers recruited 450 participants»
- response_rate: NR — NR — «NR»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: 18 — Page 4, Participants and Study Design — «All participants were adults aged between 18 and 50 years»
- age_max: 50 — Page 4, Participants and Study Design — «All participants were adults aged between 18 and 50 years»
- age_group: adults — Page 4, Participants and Study Design — «All participants were adults aged between 18 and 50 years»
- pct_female: 53.3 — Page 4, Participants and Study Design — «450 participants, comprising 210 males and 240 females»
- informant: self — Page 4, Data Collection and Procedure — «Participants completed standardized questionnaires to assess misokinesia and misophonia symptoms»
- mode: online — Page 4, Data Collection and Procedure — «Data was collected via an online survey distributed through Google Forms.»
- instruments: yes/no screening question on negative responses to auditory triggers (ad hoc); Misophonia Assessment Questionnaire (MAQ, Johnson & Dozier 2013; language version not stated, presumably English) given to screen-positives — Page 4, Assessment of Misophonia — «Participants were first asked a yes/no question on whether they experienced negative emotional or physiological responses to specific auditory triggers. Those …»
- instrument_validated_in_language: NR — Page 4, Assessment of Misophonia — «administered the Misophonia Assessment Questionnaire (MAQ) by M. Johnson [12]»
- pub_status: preprint — Page 1 — «Research Article ... Posted Date: January 6th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-5659312/v1»
- language: English — Page 1-9 — «Prevalence and Demographic Influences of Misokinesia and Misophonia in Adults in India»
- funding_coi: Funding NR; no competing interests reported — Page 1 — «Additional Declarations: No competing interests reported.»
- notes: Two-stage design: yes/no screen, then MAQ (bands version A: subclinical 0-11, mild 12-24, moderate 25-37, severe 38-50, extreme 51-63) for screen-positives only (p. 4). The case definition behind 16.89% is not stated (screen-positive alone, or a MAQ band such as >=12?). Number completing MAQ and band counts are not reported. Females reported as having higher prevalence, but no sex-specific figures given, so no subgroup estimates. Possible overlap: the authors (Prabhu, Karupaiah) published other Indian student prevalence surveys (refs 6, 8, 9); this sample is described as adults from various r…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target population is adults in India; no sampling frame is described beyond an online Google Forms survey. — Page 4, Participants and Study Design — «Researchers recruited 450 participants ... representing diverse regions across India.»
2. способ отбора: **unclear** — Recruitment method is not described. The online Google Forms survey suggests non-probability opt-in sampling, but this is not stated. — Page 4, Data Collection and Procedure — «Data was collected via an online survey distributed through Google Forms.»
3. размер выборки: **yes** — n = 450, which is at least 385. — Page 4 — «Researchers recruited 450 participants»
4. описание выборки и условий: **unclear** — Age range, sex, country and setting are reported; dates of data collection are missing. — Page 4 — «comprising 210 males and 240 females ... adults aged between 18 and 50 years»
5. охват (пропуски): **unclear** — Missing data and MAQ completion among screen-positives are not reported. — Page 5, Results — «The study found that 16.89% of participants experienced misophonia»
6. валидность определения случая: **unclear** — The threshold defining misophonia (screen alone or a MAQ band) is not stated, and the MAQ language version and its validation are not reported. — Page 4, Assessment of Misophonia — «Those who reported misophonia symptoms were administered the Misophonia Assessment Questionnaire (MAQ)»
7. единое надёжное измерение: **unclear** — Everyone took the same online screen and MAQ, but no reliability is reported and the case definition is unclear. — Page 4 — «Participants completed standardized questionnaires to assess misokinesia and misophonia symptoms»
8. статистика (числитель и знаменатель): **no** — Only percentages are given, with no counts or CI. The case definition is unclear, and the figures are internally inconsistent (co-occurrence 8.89% is higher than misokinesia 5.34%). — Page 5, Results — «16.89% of participants experienced misophonia ... Misokinesia ... 5.34% ... 8.89% of the sample experienced both misophonia and misokinesia»
9. отклик: **no** — Open online survey with no denominator of invited people and no handling of non-response. — Page 4, Data Collection and Procedure — «Data was collected via an online survey distributed through Google Forms.»

Правки:
- 

Проверено: да
---

## ST017 · Qurrah-tul-ain 2026 · Pakistan Journal of Social Science Review

Основной отчёт R0161: [текст](../../fulltext/text/R0161.txt) · [файл](../../fulltext/manual/R0161.docx) — «Demographic Determinants of Misophonia Severity: The Role of Age, Gender, Education, and Socioeconomic Status» — [DOI](https://doi.org/10.5281/zenodo.21774385)
Расхождения в тексте: 1) Sample size: the Abstract says 2,021 recruited; the Sample section says N=2000; the Procedure says 12 were excluded for psychosis, leaving N=2000 (2021-12=2009, not 2000). 2) Sampling: the Sample section and Abstract say 'random sampling technique'; the Procedure says 'convenience sampling methodology'. 3) Age: the Procedure says 16-25 years; Table 1 says 17-22 (M=19.06, SD=1.30), probably for the analytic subsample. 4) The instrument is called 'Duke Misophonia Scale (DMS; Rosenthal et al., 2021)' and 'Misophonia Scale'; it is coded as DMQ. 5) The inclusion criteria contradict each other ('students who exhibited misophonic symptoms were included' vs 'Healthy participants'). 6) The Procedure mentions the OCI-R and ASI-3, but they are not described in Measures.
Заметка ИИ: No prevalence percentage or case definition is reported. Both count-based estimates are level NR (G6). The reviewer should check whether a companion Urdu DMQ validation report from the same N=2000/428 sample exists.

### ST017-1 · College and university students, Pakistan, N=2000 (Urdu DMQ)
Отчёты: R0161 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DMQ · 'elevated levels of misophonia' / 'met the criteria for Misophonia' on Urdu DMQ; criterion not stated | **NR** | **428 / 2000** | 21.4 | Methodology, Procedure; Sample | «In light of the findings, individuals demonstrating elevated levels of misophonia (n = 428) were determined and chosen for additional analytical scrutiny.» |
| E2 | all | DMQ · symptom/trigger frequency >=4-7 times per week (applied after the unstated 'elevated' selection, apparently within the n=428) | **NR** | **196 / 2000** | 9.8 | Methodology, Procedure; Abstract | «After applying these inclusion and exclusion criteria, the final analytical sample consisted of 196 participants.» |

- E1: источник порога: study's own; правило: DMQ row; G6 definition not determinable; у авторов: «elevated levels of misophonia»; главная у авторов: no; период: NR; заметка: 428/2000 = 21.4% (not reported by the authors). The Sample section says: 'Participants who met the criteria for Misophonia were retained for further screening.' The criteria are not stated. The denominator may be 2000, or 2009 (2021-12).
- E2: источник порога: study's own; правило: DMQ row; G6 / G10 (first-stage criterion not stated); у авторов: «final analytical sample»; главная у авторов: no; период: NR; заметка: The denominator is unclear. The Procedure section implies the filter was applied to the n=428; the Abstract implies it was applied to all remaining participants. The filter kept those reporting 4-7 times/week, 2-5 times/day or 6+ times/day; the frequency item is not specified. This was an analytic …

**Ключевые поля выборки:**
- **n_analysed: 2000** — Methodology, Procedure — «the remaining eligible participants were enlisted for the principal study, culminating in a final sample of 2000 participants (N = 2000)»
- **population: university_students** — Methodology, Procedure — «The sample encompassed both male and female students within the age range of 16 to 25 years, who were recruited from various colleges and universities»
- **sampling: convenience** — Methodology, Procedure (conflicts with Sample section and Abstract) — «recruited from various colleges and universities through a convenience sampling methodology»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: PAK — Abstract — «demographic determinants of misophonia severity among Pakistani university students»
- setting: university (various colleges and universities; cities/regions not stated) — Methodology, Procedure — «who were recruited from various colleges and universities through a convenience sampling methodology»
- data_years: NR — NR — «NR»
- design: cross-sectional — Methodology, Research Design — «A cross-sectional study was conducted to collect the data.»
- topic_disclosed: NR — NR — «NR»
- inclusion_exclusion: Excluded: psychotic symptoms on PSYRATS (n=12), cognitive deficits (learning disability, dementia), alcohol/drug abuse; healthy students without hearing disability or medical/psychological history — Methodology, Exclusion Criteria; Procedure — «A cumulative total of 12 participants were excluded at this stage due to the identification of psychotic symptoms.»
- n_invited: NR — NR — «NR»
- n_responded: 2021 — Abstract — «A total of 2,021 students were recruited using a random sampling technique.»
- response_rate: NR — NR — «NR»
- age_mean: 19.06 — Table 1 — «Age | 19.06 | 1.3 | 17-22»
- age_sd: 1.3 — Table 1 — «Age | 19.06 | 1.3 | 17-22»
- age_min: 16 — Methodology, Procedure — «students within the age range of 16 to 25 years»
- age_max: 25 — Methodology, Procedure — «students within the age range of 16 to 25 years»
- age_group: mixed — Methodology, Procedure — «students within the age range of 16 to 25 years»
- pct_female: NR — Methodology, Procedure — «The sample encompassed both male and female students»
- informant: self — Limitations — «the reliance on self-report measures may be susceptible to influences of social desirability or response biases»
- mode: NR — NR — «NR»
- instruments: Duke Misophonia Questionnaire (called 'Duke Misophonia Scale'/'Misophonia Scale'), Urdu translated version — Methodology, Sample; Measures — «Urdu translated version of Misophonia Scale was administed on a large sample was recruited (N = 2000).»
- instrument_validated_in_language: NR — Methodology, Sample — «The final refined sample (n = 428) were then used to establish the reliability and validity of the scale.»
- pub_status: journal — Header — «Pakistan Journal of Social Science Review»
- language: English — Full text — «Demographic Determinants of Misophonia Severity: The Role of Age, Gender, Education, and Socioeconomic Status»
- funding_coi: NR — NR — «NR»
- notes: The instrument is the DMQ (Rosenthal et al. 2021), called 'Duke Misophonia Scale', with 86 items. The Urdu translation has no cited published validation; the text says the n=428 subsample was used to establish the scale's reliability and validity, so a separate validation report from the same sample may exist (possible overlap). Age mean and SD (19.06, 1.3; range 17-22) are from Table 1 and probably describe the analytic subsample (196 or 428), not N=2000. Sex distribution is not reported. The main analysis is a regression on 196 participants; no prevalence percentage is reported. n_invited i…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — The frame (which colleges or universities, which regions) is not described for the target of Pakistani university students. — Methodology, Procedure — «recruited from various colleges and universities»
2. способ отбора: **no** — The Procedure section states convenience sampling, which contradicts the 'random sampling' claim in the Sample section and Abstract; no random selection method is described. — Methodology, Procedure; Sample — «recruited from various colleges and universities through a convenience sampling methodology»
3. размер выборки: **yes** — N=2000 is at least 385. — Methodology, Procedure — «a final sample of 2000 participants (N = 2000)»
4. описание выборки и условий: **no** — Sex distribution and dates of data collection are not reported; the setting is only vaguely described. — Methodology, Procedure — «The sample encompassed both male and female students within the age range of 16 to 25 years»
5. охват (пропуски): **unclear** — Missing data on the misophonia measure are not reported. — NR — «NR»
6. валидность определения случая: **unclear** — The threshold for 'elevated levels of misophonia' is not stated, and the Urdu DMQ has no cited published validation. — Methodology, Procedure — «individuals demonstrating elevated levels of misophonia (n = 428) were determined and chosen for additional analytical scrutiny»
7. единое надёжное измерение: **unclear** — The same instrument was used for all participants and alpha is reported (.92, probably in the analytic subsample), but the mode of administration and the case threshold are not reported. — Table 1 — «Misophonia Total | 83.32 | 14.5 | 54-140 | .92»
8. статистика (числитель и знаменатель): **unclear** — Counts (428/2000) are given but no percentage or CI; the case definition is not stated; the denominator is inconsistent (2021 recruited minus 12 excluded does not equal 2000). — Abstract; Methodology, Procedure — «A cumulative total of 12 participants were excluded at this stage due to the identification of psychotic symptoms.»
9. отклик: **unclear** — The number invited and the response rate are not reported. — NR — «NR»

Правки:
- 

Проверено: да
---

## ST018 · Rappoldt 2026 · Child psychiatry and human development

Основной отчёт R0164: [текст](../../fulltext/text/R0164.txt) — «Psychometric Validation of the New Misophonia Screening List-Child and Youth and AMISOS-Y (Dutch Child- and Parent-Report Versions) for Assessing Misophonia in…» — [DOI](https://doi.org/10.1007/s10578-024-01781-4)
Не выписано ИИ: Clinical sample (N = 95 youth, 94 with child report; 95 parents): children referred to Amsterdam UMC for assessment and treatment of misophonia and recruited for the CBT/PMT RCT (NL-OMON20775). Excluded as E1 (recruited because of misophonia).
Расхождения в тексте: Child report: Table 1 initial control N = 256, final N = 197; the text says 59 scored >=10; 256 - 59 = 197, so the figures agree. Specificity 77.0% = 197/256 (76.95%), which confirms that the positive rate equals 1 - specificity. Parent report: initial N = 59, 3 removed, final N = 56 (consistent). The 3 removed parent dyads' 'scores aligned with the child-reported scores', so they are presumably among the 59 child-report positives. The sex derivation (36 + 23 = 59; 2 + 1 = 3) matches. The text describes the initial 256 as 'participants without misophonia' even though 59 scored above the cut-off. The clinical sample is given as 95 in the Introduction and Participants sections, and 94 analysed for the child report.
Заметка ИИ: There is one eligible sample: the school-based control group. Its prevalence-type estimates come only from the controls removed as scoring at or above the MSL-CY cut-offs. The authors do not present these as prevalence. The cut-offs were derived by ROC in this report (G8 flag). Data collection years and funding are not reported in the text provided.

### ST018-1 · School control group, primary and secondary schools, Netherlands, n=256 (child report) / 59 (parent report)
Отчёты: R0164 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MSL-CY · MSL-CY child report (11 items) >=10 | **L2** | **59 / 256** | 23.0 | Results, Phase 2; Table 1 | «With a cutoff score of 9.98 (i.e., 10), the sensitivity was 96.8%, and the specificity 77.0% ... From the initial control group, 59 participants scored equal to or higher than the cutoff of 10 (indicating possible false…» |
| E2 | female | MSL-CY · MSL-CY child report (11 items) >=10 | **L2** | **36 / 162** | 22.2 | Table 1 | «Girls (N, %) / 72 (76.6%) / 162 (63.3%)* / 126 (64.0%)*» |
| E3 | male | MSL-CY · MSL-CY child report (11 items) >=10 | **L2** | **23 / 94** | 24.5 | Table 1 | «Boys (N, %) / 22 (23.4%) / 94 (36.7%)* / 71 (36.0%)*» |
| E4 | all (parent report) | MSL-CY · MSL-CY parent report (11 items) >=9 | **L2** | **3 / 59** | 5.1 | Results, Phase 2; Table 1 | «From the initial control group, 3 parents scored equal to or greater than the cutoff of 9, and were removed from further analyses ... This resulted in the final control group of N = 56 parents» |
| E5 | female (parent report) | MSL-CY · MSL-CY parent report (11 items) >=9 | **L2** | **2 / 36** | 5.6 | Table 1 | «Girls (N, %) ... 73 (76.8%) / 36 (61.0%)* / 34 (60.7%)*» |
| E6 | male (parent report) | MSL-CY · MSL-CY parent report (11 items) >=9 | **L2** | **1 / 23** | 4.3 | Table 1 | «Boys (N, %) ... 22 (23.2%) / 23 (39.0%)* / 22 (39.3%)*» |

- E1: источник порога: developer paper; правило: MSL-CY row, child report >=10 (L2); G8 derivation-sample flag; у авторов: «clinically significant misophonia (scorers treated as 'possible false negatives…»; главная у авторов: no; период: NR; заметка: Self (child) report. 59/256 = 23.0%. Cut-off derived by ROC in this same report (G8). Authors present no prevalence estimate. Controls excluded beforehand for IQ<85 / misophonia treatment (counts NR).
- E2: источник порога: developer paper; правило: MSL-CY row, child report >=10 (L2); G8 flag; у авторов: «clinically significant misophonia ('possible false negatives')»; главная у авторов: no; период: NR; **расчёт: Girls initial control 162 minus girls final control 126 = 36 removed for scoring >=10 (Table 1)**; заметка: Self (child) report. Derived from the difference between initial and final control groups; removal was only for scoring >=10 (256-59=197).
- E3: источник порога: developer paper; правило: MSL-CY row, child report >=10 (L2); G8 flag; у авторов: «clinically significant misophonia ('possible false negatives')»; главная у авторов: no; период: NR; **расчёт: Boys initial control 94 minus boys final control 71 = 23 (Table 1); 36 + 23 = 59**; заметка: Self (child) report. Derived from initial vs final control group difference.
- E4: источник порога: developer paper; правило: MSL-CY row, parent report >=9 (L2); G8 flag; у авторов: «clinically significant misophonia ('possible false negatives')»; главная у авторов: no; период: NR; заметка: Parent report. Denominator = initial parent control group N = 59 (Table 1). 3/59 = 5.1%. Cut-off derived in same report (G8).
- E5: источник порога: developer paper; правило: MSL-CY row, parent report >=9 (L2); G8 flag; у авторов: «clinically significant misophonia ('possible false negatives')»; главная у авторов: no; период: NR; **расчёт: Girls initial parent control 36 minus final 34 = 2 (Table 1)**; заметка: Parent report. Derived from initial vs final parent control groups.
- E6: источник порога: developer paper; правило: MSL-CY row, parent report >=9 (L2); G8 flag; у авторов: «clinically significant misophonia ('possible false negatives')»; главная у авторов: no; период: NR; **расчёт: Boys initial parent control 23 minus final 22 = 1 (Table 1)**; заметка: Parent report. Derived from initial vs final parent control groups.

**Ключевые поля выборки:**
- **n_analysed: 256** — Table 1; Results, Phase 2 — «Initial control groupb (N = 256)»
- **population: school_pupils** — Methods, Control Group — «Included were children from the general population ... Recruitment took place in primary and secondary (including vocational) schools»
- **sampling: convenience** — Methods, Control Group — «Informed consents were either handed out by teachers or by the research assistants, and collected afterwards by the research assistants (or by e-mail).»

**Остальные поля:**
- clinical_group: NA — NA
- country: NLD — Methods, Control Group — «Recruitment took place in primary and secondary (including vocational) schools, from rural and urban regions in the North and South of the Netherlands»
- setting: school (primary and secondary, including vocational, schools; rural and urban, North and South Netherlands) — Methods, Control Group — «Recruitment took place in primary and secondary (including vocational) schools, from rural and urban regions in the North and South of the Netherlands, by trai…»
- data_years: NR — Methods — «referred by their general practitioner to our academic center for assessment and treatment of misophonia before January 2023»
- design: validation study — Introduction, The Current Study — «presenting an extensive iterative validation study of two newly developed questionnaires, containing parallel child- and parent-reported versions»
- topic_disclosed: NR — Methods, Control Group — «Informed consents were either handed out by teachers or by the research assistants»
- inclusion_exclusion: Aged 8-18, written informed consent (children 12+ and parents of children <16). Excluded: misophonia treatment in past year, estimated IQ <85, unable to read/write Dutch; also clinically significant misophonia (applied after screening: the 59 scoring >=10 were removed post hoc). — Methods, Control Group — «Exclusion criteria were: (1) meeting criteria for misophonia on a clinically significant level (see Statistical analyses), (2) having received treatment for mi…»
- n_invited: NR — Methods, Control Group — «Informed consents were either handed out by teachers or by the research assistants»
- n_responded: 256 — Participants, Control Group — «We collected an initial sample of 256 participants without misophonia, of which 197 participants aged 8–18 years old ... were included»
- response_rate: NR — NA
- age_mean: 13.8 — Table 1 (child report, initial control group) — «Age of child (M, SD) | 13.2 (2.4) | 13.8 (3.7) | 14.3 (3.5)*»
- age_sd: 3.7 — Table 1 (child report, initial control group) — «Age of child (M, SD) | 13.2 (2.4) | 13.8 (3.7) | 14.3 (3.5)*»
- age_min: 8 — Methods, Control Group — «(1) were aged between 8 and 18 years»
- age_max: 18 — Methods, Control Group — «(1) were aged between 8 and 18 years»
- age_group: mixed — Methods, Control Group — «(1) were aged between 8 and 18 years»
- pct_female: 63.3 — Table 1 (child report, initial control group) — «Girls (N, %) | 72 (76.6%) | 162 (63.3%)*»
- informant: mixed — Methods, Control Group — «Child-reported questionnaires were assessed on paper in the classroom ... Parent-reported questionnaires were taken home in a closed envelope»
- mode: paper — Methods, Control Group — «Child-reported questionnaires were assessed on paper in the classroom ... Parent-reported questionnaires were taken home in a closed envelope and could be retu…»
- instruments: Misophonia Screening List—Child and Youth (MSL-CY), Dutch, child and parent report; AMISOS-Y, Dutch, child and parent report — Measures — «The Misophonia Screening List—Child and Youth (parallel child and parent version) contains 13 statements ... The AMISOS-Y (parallel child and parent version)»
- instrument_validated_in_language: yes — Title; Results, Phase 2 — «Psychometric Validation of the New Misophonia Screening List—Child and Youth and AMISOS-Y (Dutch Child- and Parent-Report Versions)»
- pub_status: journal — Header — «Year: 2026; venue: Child psychiatry and human development; DOI: 10.1007/s10578-024-01781-4»
- language: English — Full text — «Psychometric Validation of the New Misophonia Screening List—Child and Youth and AMISOS-Y (Dutch Child- and Parent-Report Versions)»
- funding_coi: NR — NA
- notes: This is the MSL-CY development/validation report (Rappoldt et al.). The cut-offs (child >=10, parent >=9) were derived by ROC in this report, using this control group against the clinical sample: flag G8 (positive rate 59/256 = 23.0% = 1 - specificity 77.0%). The authors treat those scoring above the cut-off as 'possible false negatives' and remove them; they claim no prevalence. Children excluded before screening (IQ <85, misophonia treatment in past year) and those with >=3 missing items were removed; counts NR. The parent-report subsample (n=59) is younger (M 10.7) than the child-report sa…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is the general youth population; frame is a selection of schools in parts of the Netherlands. — Methods, Control Group — «Recruitment took place in primary and secondary (including vocational) schools, from rural and urban regions in the North and South of the Netherlands»
2. способ отбора: **no** — Consent-based convenience recruitment through schools; no random selection. — Methods, Control Group — «Informed consents were either handed out by teachers or by the research assistants, and collected afterwards by the research assistants (or by e-mail).»
3. размер выборки: **no** — n = 256 (child report) and 59 (parent report), below 385. — Table 1 — «Initial control groupb (N = 256)»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection not reported. — Table 1; Methods, Control Group — «Age of child (M, SD) | 13.2 (2.4) | 13.8 (3.7) ... Girls (N, %) | 72 (76.6%) | 162 (63.3%)*»
5. охват (пропуски): **unclear** — Respondents with >=3 missing items were excluded, but the number excluded is not reported. — Measures — «If an individual had three or more missing items, the individual's data were excluded from further analysis.»
6. валидность определения случая: **yes** — MSL-CY child report >=10, Dutch version validated in this report (ROC against clinical cases); cut-off derived in same sample (G8 flag). — Results, Phase 2 — «With a cutoff score of 9.98 (i.e., 10), the sensitivity was 96.8%, and the specificity 77.0%»
7. единое надёжное измерение: **yes** — Same instrument, paper mode and threshold for all controls; Cronbach's alpha reported. — Results, Reliability Analysis — «the reliability analysis of the combined group showed high internal consistency on the child-reported (α = 0.958) and parent-reported (α = 0.957) version»
8. статистика (числитель и знаменатель): **yes** — Numerator (59) and denominator (256) are explicit; CI calculable. — Results, Phase 2 — «From the initial control group, 59 participants scored equal to or higher than the cutoff of 10»
9. отклик: **unclear** — Number of pupils/parents invited and response rate not reported. — Methods, Control Group — «Informed consents were either handed out by teachers or by the research assistants, and collected afterwards by the research assistants (or by e-mail).»

Правки:
- 

Проверено: да
---

## ST019 · Smit 2026 · Journal of autism and developmental disorders

Основной отчёт R0196: [текст](../../fulltext/text/R0196.txt) · [PDF](../../fulltext/pdf/R0196.pdf) — «Misophonia Symptoms in Autistic Adults.» — [DOI](https://doi.org/10.1007/s10803-025-07184-1)
Приложен R0195: [текст](../../fulltext/text/R0195.txt) · [PDF](../../fulltext/pdf/R0195.pdf) — «Misophonia symptoms in autistic adults»
Связь отчётов: medRxiv preprint (R0195) and article (R0196): same 1,050 autistic adults of the Netherlands Autism Register
Расхождения в тексте: 1) Age: the text gives M=46.8, SD=13.6 and Table 1 gives M=46.9, SD=13.6. The table value is used. 2) Table 1 'none' co-occurring row: 427 + 94 = 521, which does not match the printed total of 512. Copied as printed. 3) Table 1 ethnicity rows look swapped between columns: Dutch shows 302 (<21) and 513 (>=21), which cannot fit 266 total cases. Not extracted. 4) The text gives 25.3% (>20) and Table 1 gives 266 (25%); 266/1050 = 25.3%, so these agree. Female share among cases is 68% in the text and 180/266 = 67.7% in the table, also consistent. 5) The >=24 count (141) appears only in a footnote to Table 2. 6) The full text of R0196 is the same as preprint R0195.
Заметка ИИ: One clinical sample (autism). The recommended L2 estimate is AMISOS-R>=24 (141/1050). The authors' primary estimate is >=21 (266/1050). The AMISOS-R language version is not stated, so instrument_validated_in_language is NR and JBI 6 is unclear.

### ST019-1 · Netherlands Autism Register, autistic adults, NLD, n=1050
Отчёты: R0196 (main); R0195

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | AMISOS-R · AMISOS-R>=24 | **L2** | **141 / 1050** | 13.4 | Page 6, Table 2 footnote † | «†For Jakobovski, we recalculated prevalences in the current data to scores of 24+ (141 cases)» |
| E2 | all | AMISOS-R · AMISOS-R>=21 | **L2** | **266 / 1050** | 25.3 | Page 4, Table 1; Page 5, Results | «Total 1050 784 (75%) 266 (25%) ... In total, 25.3% scored >20 on the AMISOS-R.» |
| E3 | female | AMISOS-R · AMISOS-R>=21 | **L2** | **180 / 610** | 29.5 | Page 4, Table 1 | «Female 610 58% 430 180» |
| E4 | male | AMISOS-R · AMISOS-R>=21 | **L2** | **82 / 427** | 19.2 | Page 4, Table 1 | «Male 427 41% 345 82» |
| E5 | other sex/gender | AMISOS-R · AMISOS-R>=21 | **L2** | **4 / 13** | 30.8 | Page 4, Table 1 | «Other 13 1% 9 4» |
| E6 | no co-occurring diagnosis | AMISOS-R · AMISOS-R>=21 | **L2** | **94 / 512** | 18.4 | Page 4, Table 1 | «none 512 52% 427 94» |
| E7 | any co-occurring diagnosis | AMISOS-R · AMISOS-R>=21 | **L2** | **155 / 481** | 32.2 | Page 4, Table 1 | «any 481 48% 326 155» |
| E8 | ADHD | AMISOS-R · AMISOS-R>=21 | **L2** | **42 / 154** | 27.3 | Page 4, Table 1 | «ADHD* 154 32% 112 42» |
| E9 | mood disorders | AMISOS-R · AMISOS-R>=21 | **L2** | **92 / 230** | 40.0 | Page 4, Table 1 | «Mood Disorders* 230 48% 138 92» |
| E10 | anxiety disorders | AMISOS-R · AMISOS-R>=21 | **L2** | **40 / 131** | 30.5 | Page 4, Table 1 | «Anxiety Disorders* 131 27% 91 40» |
| E11 | PTSD | AMISOS-R · AMISOS-R>=21 | **L2** | **70 / 142** | 49.3 | Page 4, Table 1 | «PTSD* 142 30% 72 70» |

- E1: источник порога: validation paper; правило: AMISOS-R row; >=24 recommended L2 (G11); у авторов: «recalculated to scores of 24+ for comparison with Jakubovski et al.»; главная у авторов: no; период: NR; заметка: Denominator 1050 assumed (the whole sample with AMISOS-R). This is the recommended L2 threshold for selection.
- E2: источник порога: validation paper; правило: AMISOS-R row; >=21 L2 (moderate to severe or more), G1/G2; у авторов: «clinical cutoff of 21 (moderate symptoms)»; главная у авторов: yes; период: NR; заметка: The authors give no source for the >=21 cut-off. Band cut-off without anchoring (JBI 6 = no for this definition).
- E3: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR; заметка: Table 1 labels this row 'Gender'; the text says sex was analysed.
- E4: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR
- E5: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR
- E6: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR; заметка: Internal inconsistency: 427 + 94 = 521, not the row total of 512. Copied as printed.
- E7: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR; заметка: Co-occurring diagnoses are self-reported.
- E8: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR; заметка: Self-reported co-occurring diagnosis in autistic adults; categories not mutually exclusive.
- E9: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR; заметка: Self-reported; categories not mutually exclusive.
- E10: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR; заметка: Self-reported; categories not mutually exclusive. n below 139.
- E11: источник порога: validation paper; правило: AMISOS-R row; >=21 L2; у авторов: «moderate symptoms»; главная у авторов: no; период: NR; заметка: Self-reported; categories not mutually exclusive.

**Ключевые поля выборки:**
- **n_analysed: 1050** — Page 4, Table 1 — «Total 1050 784 (75%) 266 (25%)»
- **population: clinical** — Page 3, Participants — «All participants were diagnosed by healthcare professionals (psychologists of psychiatrists) working independently from the current study, based on DSM-IV-TR or DSM-5 criteria.»
- **sampling: convenience** — Page 1, Acknowledgements — «Special thanks to the volunteer participants at the Netherlands Autism Register.»

**Остальные поля:**
- clinical_group: autism — Page 3, Participants — «All participants were diagnosed by healthcare professionals ... based on DSM-IV-TR or DSM-5 criteria.»
- country: NLD — Page 3, Methods, Participants — «The study was conducted within the Netherlands Autism Register (NAR)»
- setting: autism register (Netherlands Autism Register, volunteer participants) — Page 1, Acknowledgements; Page 3, Participants — «Special thanks to the volunteer participants at the Netherlands Autism Register.»
- data_years: NR — Page 5, Procedure — «Participant enrolment and data collection procedures of the Netherlands Autism Register are described elsewhere (Scheeren et al., 2021).»
- design: cross-sectional — Page 3, Methods — «A total of 1050 participants (610 females, 427 males, 13 others), aged 16–85 years (M = 46.8, SD = 13.6), completed the misophonia questionnaire.»
- topic_disclosed: NR — Page 3, Methods — «For details of the NAR procedures, see Scheeren et al. (2022).»
- inclusion_exclusion: NAR participants with a professional DSM-IV-TR/DSM-5 autism diagnosis who completed the AMISOS-R; no other criteria reported — Page 3, Participants — «All participants were diagnosed by healthcare professionals ... based on DSM-IV-TR or DSM-5 criteria. ... completed the misophonia questionnaire.»
- n_invited: NR — Page 3, Participants — «For details of the NAR procedures, see Scheeren et al. (2022).»
- n_responded: 1050 — Page 3, Participants — «A total of 1050 participants ... completed the misophonia questionnaire.»
- response_rate: NR — Page 3, Participants — «A total of 1050 participants ... completed the misophonia questionnaire.»
- age_mean: 46.9 — Page 4, Table 1 — «Age 1050 M=46.9»
- age_sd: 13.6 — Page 4, Table 1 — «SD=13.6»
- age_min: 16 — Page 3, Participants — «aged 16–85 years»
- age_max: 85 — Page 3, Participants — «aged 16–85 years»
- age_group: mixed — Page 3, Participants — «aged 16–85 years (M = 46.8, SD = 13.6)»
- pct_female: 58.1 — Page 4, Table 1; Page 3 — «1050 participants (610 females, 427 males, 13 others)»
- informant: self — Page 2, Abstract — «Autistic adults (N=1050) filled out the Amsterdam Misophonia Scale-Revised (AMISOS-R)»
- mode: NR — Page 3, Questionnaires — «Demographic information was collected through self-report»
- instruments: AMISOS-R (language version not stated; Dutch register) — Page 3, Questionnaires — «The Amsterdam Misophonia Scale-Revised (AMISOS-R) is an update of the A-Miso-S questionnaire developed by Schröder et al. (2013)»
- instrument_validated_in_language: NR — Page 3, Questionnaires — «The questionnaire demonstrated good reliability (α = .93) and internal validity (r = .87, p < .01; Jager et al. 2020).»
- pub_status: journal — Job metadata — «venue: Journal of autism and developmental disorders; DOI: 10.1007/s10803-025-07184-1»
- language: English — Full text — «Misophonia symptoms in autistic adults»
- funding_coi: Funding: ZonMw Grant #60-63600-98-834; conflicts of interest NR — Page 1, Acknowledgements — «Funding provided by ZonMw, Grant #60-63600-98-834.»
- notes: The full text supplied as main report R0196 is the same as the medRxiv preprint R0195 (it carries medRxiv headers), so the two texts do not differ. The text does not say which language version of the AMISOS-R was used; the SPQ is explicitly the Dutch version. The source cited for psychometrics is Jager et al. 2020. Age 46.8 in the text vs 46.9 in Table 1 (table used). Age range 16-85 includes adolescents, although the paper calls the sample adults. Table 1 says 'Gender' but the text says analyses used sex. The NAR is a longitudinal register; this is one cross-sectional wave. Pre-registered as…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is a volunteer register of autistic people, which covers only part of the autistic adult population of the Netherlands. — Page 1, Acknowledgements — «Special thanks to the volunteer participants at the Netherlands Autism Register.»
2. способ отбора: **no** — Volunteer opt-in register, not a probability sample. — Page 1, Acknowledgements — «volunteer participants at the Netherlands Autism Register»
3. размер выборки: **yes** — n=1050, above 385 (and above 139 for a clinical group). — Page 3, Participants — «A total of 1050 participants ... completed the misophonia questionnaire.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — Page 3, Participants; Page 5, Procedure — «Participant enrolment and data collection procedures of the Netherlands Autism Register are described elsewhere»
5. охват (пропуски): **unclear** — Only completers of the misophonia questionnaire are reported. The number of NAR respondents without AMISOS-R data is not given. — Page 3, Participants — «A total of 1050 participants ... completed the misophonia questionnaire.»
6. валидность определения случая: **unclear** — The preferred L2 definition is AMISOS-R>=24, which is anchored, but the language version is not stated. The authors' primary threshold, >=21, is an unanchored band cut-off and would rate no. Rate yes only if a validated… — Page 3, Questionnaires; Page 6, Table 2 footnote — «For Jakobovski, we recalculated prevalences in the current data to scores of 24+ (141 cases)»
7. единое надёжное измерение: **yes** — Everyone completed the same self-report AMISOS-R with the same threshold; reliability is cited from the source paper. — Page 3, Questionnaires — «The questionnaire demonstrated good reliability (α = .93) and internal validity (r = .87, p < .01; Jager et al. 2020).»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are clear (266/1050), so a CI can be calculated; no weighting is needed. — Page 4, Table 1; Page 5, Results — «In total, 25.3% scored >20 on the AMISOS-R.»
9. отклик: **unclear** — No response rate is given, and the number of register members invited is not reported. — Page 5, Procedure — «Participant enrolment and data collection procedures of the Netherlands Autism Register are described elsewhere (Scheeren et al., 2021).»

Правки:
- 

Проверено: да
---

## ST020 · Temeltürk 2026 · BMC Pediatrics

Основной отчёт R0204: [текст](../../fulltext/text/R0204.txt) · [PDF](../../fulltext/pdf/R0204.pdf) — «Misophonia in adolescents: clinical correlates and associations with autism-related behavioral characteristics within a clinical context» — [DOI](https://doi.org/10.1186/s12887-026-07387-0)
Расхождения в тексте: 1) Table 1 prints 'Normal 106 (52)', but 106/200 = 53%; the other bands (60 = 30%, 24 = 12%, 10 = 5%) are correct, and 106+60+24+10 = 200. 2) The text says 94 (47%) cases, 60 mild and 34 moderate-to-severe; this matches Table 1 (24 moderate + 10 severe = 34). 3) Sex direction conflicts: 72.3% of Misophonia (+) were female, and the discussion says females were more likely to have misophonia. But the regression (male = 0, female = 1) reports 'Female sex was associated with a lower likelihood of misophonia (OR = 0.41)', so the coding or wording is probably wrong. The female (68/123) and male (26/77) counts I derived reproduce the reported chi2 = 8.80. 4) Text and Table 4 give the Block 1 chi2 as 8.92 and Wald as 8.63; these are different statistics, so this is not an error. 5) Reference [27] is cited both for the CBCL autism composite and for the Turkish AMISOS-R validation (Cakiroglu et a…
Заметка ИИ: There is one eligible sample. The authors' main estimate is AMISOS-R >=11, 94/200, which is L1. L2 estimates come only from unanchored severity bands: >=21 (34/200) and >=31 (10/200). No count is available for the anchored cut-off >=24. The sampling method and response rate are not reported. Clinical-subgroup counts come from Table 2 (Misophonia + plus Misophonia - gives the subgroup n).

### ST020-1 · Child and adolescent psychiatry outpatients, Ankara, Türkiye, n=200
Отчёты: R0204 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | AMISOS-R · AMISOS-R>=11 | **L1** | **94 / 200** | 47.0 | Page 8, Results; Table 1 | «misophonia was identified in 94 participants (47%), of whom 60 were classified as having mild misophonia and 34 as having moderate-to-severe misophonia» |
| E2 | all | AMISOS-R · AMISOS-R>=21 | **L2** | **34 / 200** | 17.0 | Page 8, Results; Table 1 | «34 as having moderate-to-severe misophonia ... Moderate 24 (12) Severe 10 (5)» |
| E3 | all | AMISOS-R · AMISOS-R>=31 | **L2** | **10 / 200** | 5.0 | Table 1 | «Severe 10 (5)» |
| E4 | female | AMISOS-R · AMISOS-R>=11 | **L1** | **68 / 123** | 55.3 | Page 8, Results | «a significantly higher proportion of females was observed in the Misophonia (+) group (72.3%) than in the Misophonia (–) group (p = .004, χ² = 8.80» |
| E5 | male | AMISOS-R · AMISOS-R>=11 | **L1** | **26 / 77** | 33.8 | Page 8, Results; Table 1 | «Misophonia (+) (n = 94) ... females ... (72.3%); Male 77 (38.5)» |
| E6 | ADHD | AMISOS-R · AMISOS-R>=11 | **L1** | **44 / 108** | 40.7 | Table 2 | «ADHD a 44 (46.8) 64 (60.4)» |
| E7 | MDD | AMISOS-R · AMISOS-R>=11 | **L1** | **45 / 76** | 59.2 | Table 2 | «MDD a 45 (47.9) 31 (29.2)» |
| E8 | anxiety | AMISOS-R · AMISOS-R>=11 | **L1** | **29 / 64** | 45.3 | Table 2 | «Anxiety disorder a 29 (30.9) 35 (33)» |
| E9 | specific learning disorder | AMISOS-R · AMISOS-R>=11 | **L1** | **10 / 25** | 40.0 | Table 2 | «SLD a 10 (10.6) 15 (14.2)» |
| E10 | OCD | AMISOS-R · AMISOS-R>=11 | **L1** | **8 / 12** | 66.7 | Table 2 | «OCD b 8 (8.5) 4 (3.8)» |
| E11 | conduct disorder | AMISOS-R · AMISOS-R>=11 | **L1** | **4 / 8** | 50.0 | Table 2 | «Conduct disorder b 4 (4.3) 4 (3.8)» |
| E12 | communication disorder | AMISOS-R · AMISOS-R>=11 | **L1** | **3 / 6** | 50.0 | Table 2 | «Communication disorder b 3 (3.2) 3 (2.8)» |
| E13 | eating disorder | AMISOS-R · AMISOS-R>=11 | **L1** | **4 / 5** | 80.0 | Table 2 | «Eating disorder b 4 (4.3) 1 (0.9)» |

- E1: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; G1 sum of bands 60+24+10; у авторов: «Misophonia (+) (mild, moderate or severe)»; главная у авторов: yes; период: NR; заметка: Equals Table 1 bands mild 60 + moderate 24 + severe 10 = 94.
- E2: источник порога: validation paper; правило: AMISOS-R row; L2 >=21 (moderate to severe or more); G1 sum of bands 24+10; у авторов: «moderate-to-severe misophonia»; главная у авторов: no; период: NR; заметка: Unanchored band threshold (JBI 6 = no).
- E3: источник порога: validation paper; правило: AMISOS-R row; G2 threshold above L2 cut-off -> L2; у авторов: «severe»; главная у авторов: no; период: NR; заметка: Top band (31-40).
- E4: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: 72.3% x 94 = 67.96 -> 68; consistent with reported chi2 = 8.80**; заметка: Recomputed chi2 with 68/123 vs 26/77 = 8.80, matching the paper.
- E5: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: 94 - 68 female cases = 26; n = 77 males**
- E6: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 44 (Miso+) + 64 (Miso-) = 108, Table 2**; заметка: Diagnosis by K-SADS-PL-DSM-5; clinical subgroup n < 139.
- E7: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 45 + 31 = 76, Table 2**; заметка: Clinical subgroup n < 139.
- E8: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 29 + 35 = 64, Table 2**; заметка: Clinical subgroup n < 139.
- E9: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 10 + 15 = 25, Table 2**; заметка: Clinical subgroup n < 139.
- E10: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 8 + 4 = 12, Table 2**; заметка: Clinical subgroup n < 139.
- E11: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 4 + 4 = 8, Table 2**; заметка: Clinical subgroup n < 139.
- E12: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 3 + 3 = 6, Table 2**; заметка: Clinical subgroup n < 139.
- E13: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; у авторов: «Misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 4 + 1 = 5, Table 2**; заметка: Clinical subgroup n < 139.

**Ключевые поля выборки:**
- **n_analysed: 200** — Page 8, Results; Table 1 — «According to the AMISOS-R assessment, misophonia was identified in 94 participants (47%)»
- **population: clinical** — Page 5; Page 7, Results — «192 participants (96%) had been diagnosed with a psychiatric disorder»
- **sampling: NR** — Page 5, Participants and procedure — «The study included 200 adolescents (77 boys and 123 girls) aged 12–18 years who attended a child and adolescent psychiatry outpatient clinic»

**Остальные поля:**
- clinical_group: mixed_psychiatric — Page 7-8, Results; Table 1 — «ADHD in 108 participants (54%), MDD in 76 participants (38%), anxiety disorders in 64 participants (32%), specific learning disorder (SLD) in 25 participants (…»
- country: TUR — Page 2, affiliations; Page 5-6, Methods — «Ankara University Faculty of Medicine, Department of Child and Adolescent Psychiatry, Ankara, Türkiye»
- setting: clinic: child and adolescent psychiatry outpatient clinic (single centre) — Page 5, Participants and procedure; Page 14, Limitations — «who attended a child and adolescent psychiatry outpatient clinic between April 2024 and April 2025»
- data_years: 2024-2025 — Page 5, Participants and procedure — «attended a child and adolescent psychiatry outpatient clinic between April 2024 and April 2025»
- design: cross-sectional — Page 12, Discussion — «given the cross-sectional design of the present study»
- topic_disclosed: NR — Page 5, Participants and procedure — «After obtaining written informed consent from the parents or legal guardians of all participants, and written assent from all participating adolescents»
- inclusion_exclusion: Inclusion: age 12-18, normal cognitive functioning and/or IQ >80. Exclusion: prior diagnosis of ASD, psychotic disorder or neurological disease; comorbid medical conditions (e.g., otolaryngological), uncorrected hearing/visual impairment, unwillingness to participate. — Page 5, Participants and procedure — «Participants with a previously established diagnosis of ASD, psychotic disorder, or neurological disease were excluded from the study.»
- n_invited: NR — Page 5 — «The study included 200 adolescents»
- n_responded: NR — Page 5 — «The study included 200 adolescents»
- response_rate: NR — NA — «Exclusion criteria also included ... lack of willingness to participate in the study.»
- age_mean: 14.56 — Table 1 — «Child age (years) 14.56 ± 1.57 (12-18)»
- age_sd: 1.57 — Table 1 — «Child age (years) 14.56 ± 1.57 (12-18)»
- age_min: 12 — Table 1 — «Child age (years) 14.56 ± 1.57 (12-18)»
- age_max: 18 — Table 1 — «Child age (years) 14.56 ± 1.57 (12-18)»
- age_group: mixed — Page 5 — «200 adolescents (77 boys and 123 girls) aged 12–18 years»
- pct_female: 61.5 — Table 1; Page 7 — «123 (61.5%) were female and 77 (38.5%) were male»
- informant: self — Page 6, Instruments; Page 15, Limitations — «Misophonia symptoms were also assessed exclusively via self-report measures»
- mode: NR — Page 6, Instruments — «The AMISOS-R is a self-administered instrument developed to evaluate the presence and intensity of symptoms»
- instruments: AMISOS-R (Turkish version implied; Turkish validation cited, language of administration not stated explicitly) — Page 6-7, Instruments — «The adaptation and validation study conducted in a Turkish adolescent population indicates that the AMISOS-R demonstrates robust psychometric properties ... (C…»
- instrument_validated_in_language: yes — Page 7, Instruments; ref 27 — «The adaptation and validation study conducted in a Turkish adolescent population indicates that the AMISOS-R demonstrates robust psychometric properties»
- pub_status: journal — Page 1 — «BMC Pediatrics ... Accepted: 20 July 2026 ... We are providing an unedited version of this manuscript to give early access»
- language: English — whole text — «Misophonia in adolescents: clinical correlates and associations with autism-related behavioral characteristics within a clinical context»
- funding_coi: No funding; authors declare no competing interests. — Page 16, Declarations — «The authors received no financial support for the research, authorship, and/or publication of this article.»
- notes: Article in press (unedited accepted manuscript). Sampling method (consecutive or not) not described. Participants with formal ASD diagnosis excluded. Trigger frequencies (e.g., eating sounds 56.0% of whole sample, Figure 1) are trigger-only data, not a case definition; not extracted as estimates. The cited Turkish AMISOS-R validation (ref 27, Cakiroglu et al. 2022) is a general Turkish population study; the text calls it an adolescent validation. Ref [27] is also cited for the CBCL autism composite (citation error). Authors' primary estimate (>=11, mild or more) is L1; L2 estimates on band th…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Target population is adolescents attending a psychiatric outpatient clinic; the frame is attendees of that clinic over one year (ASD/psychosis excluded). — Page 5, Participants and procedure — «aged 12–18 years who attended a child and adolescent psychiatry outpatient clinic between April 2024 and April 2025»
2. способ отбора: **unclear** — Method of selecting participants among attendees (consecutive vs convenience) not described. — Page 5 — «The study included 200 adolescents (77 boys and 123 girls) aged 12–18 years who attended a child and adolescent psychiatry outpatient clinic»
3. размер выборки: **no** — n = 200 < 385. — Page 7, Results — «Among the total sample of 200 participants»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Page 5; Table 1 — «200 adolescents (77 boys and 123 girls) aged 12–18 years ... between April 2024 and April 2025»
5. охват (пропуски): **yes** — All 200 included participants classified on AMISOS-R (bands sum to 200). — Table 1 — «Normal 106 (52) Mild 60 (30) Moderate 24 (12) Severe 10 (5)»
6. валидность определения случая: **no** — Highest-level (L2) definitions are AMISOS-R band thresholds >=21/>=31 without interview/ROC anchoring; primary author estimate >=11 is also an unanchored band. — Page 7, Instruments — «normal/subclinical (0-10 points), mild (11-20 points), moderate (21-30 points), and severe (31-40 points)»
7. единое надёжное измерение: **yes** — Same instrument and threshold for all; internal consistency reported from the Turkish validation source. — Page 7, Instruments — «exhibiting high internal consistency (Cronbach’s α = .92) and strong test–retest reliability (r = .89)»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (94/200); CI not given but calculable. — Page 8, Results — «misophonia was identified in 94 participants (47%)»
9. отклик: **unclear** — Number approached/refusals not reported. — Page 5 — «lack of willingness to participate in the study»

Правки:
- 

Проверено: да