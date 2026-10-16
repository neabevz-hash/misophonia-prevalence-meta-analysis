# Проверка выписывания — файл 4 из 10

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

## ST031 · Rinaldi 2025 · Child psychiatry and human development

Основной отчёт R0393: [текст](../../fulltext/text/R0393.txt) — «Mental Health Difficulties in Children who Develop Misophonia: An Examination of ADHD, Depression & Anxiety.» — [DOI](https://doi.org/10.1007/s10578-023-01569-y)
Приложен R0811: [текст](../../fulltext/text/R0811.txt) — «Misophonia, self-harm and suicidal ideation.»
Связь отчётов: ALSPAC 'Life at 28+' wave, Sussex Screener for Misophonia: both report 333 of 4,253
Расхождения в тексте: The main report R0393 and the attached report R0811 (Methods, Participants) give identical figures: 4253 respondents (1452 male, 2798 female, 3 unknown) and 333 misophonics (77 male, 256 female) vs 3920 non-misophonics (1375 male, 2542 female, 3 unknown). The internal sums check out: 77+1375=1452; 256+2542=2798; 333+3920=4253. Both reports describe the SSfM classification rule in the same way. Neither report gives the number of participants who agreed with the characterisation but rated the disruption 'not at all', so an L1 estimate (agreement only) cannot be derived.
Заметка ИИ: Design is coded as cross-sectional, but the screening was a follow-up wave of the ALSPAC birth cohort. Sampling is coded census and population gp_probability because of the original population-based recruitment; the reviewer may prefer gp_other given the heavy attrition (4253 respondents vs 14,901 alive at 1 year). 'Validated in language = yes' rests only on the convergent/divergent validity evidence in this same report, the source cited for the SSfM in Table 1. time_frame is NR because the SSfM wording gives no reference period.

### ST031-1 · ALSPAC 'Life at 28+' wave, Avon birth cohort, GBR, n=4253
Отчёты: R0393 (main); R0811

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SSfM · SSfM: agrees with misophonia characterisation AND rates disruption of daily life at least 'very mildly' (rejects 'not at all') | **L2** | **333 / 4253** | 7.8 | Methods, Participants | «Our participants with returned data were 4253 adults aged 28 ... this group contained 333 adults with misophonia (77 male and 256 female) and 3920 without misophonia» |
| E2 | female | SSfM · SSfM: agrees with misophonia characterisation AND rates disruption of daily life at least 'very mildly' (rejects 'not at all') | **L2** | **256 / 2798** | 9.1 | Methods, Participants | «2798 female-at-birth ... this group contained 333 adults with misophonia (77 male and 256 female)» |
| E3 | male | SSfM · SSfM: agrees with misophonia characterisation AND rates disruption of daily life at least 'very mildly' (rejects 'not at all') | **L2** | **77 / 1452** | 5.3 | Methods, Participants | «comprising 1452 males-at-birth ... 333 adults with misophonia (77 male and 256 female)» |

- E1: источник порога: developer paper; правило: SSfM row L2 (agrees + disruption >= very mildly); adhoc rule reaction plus impairment; у авторов: «misophonics»; главная у авторов: no; период: NR; заметка: 333/4253 = 7.8%. The authors use this as a group classification and do not present it as a prevalence estimate. The same figures appear in R0811. SSfM: JBI 6 = no; excluded in sensitivity analysis 2.
- E2: источник порога: developer paper; правило: SSfM row L2 (agrees + disruption >= very mildly); у авторов: «misophonics»; главная у авторов: no; период: NR; заметка: Sex at birth. 256/2798 = 9.1%.
- E3: источник порога: developer paper; правило: SSfM row L2 (agrees + disruption >= very mildly); у авторов: «misophonics»; главная у авторов: no; период: NR; заметка: Sex at birth. 77/1452 = 5.3%.

**Ключевые поля выборки:**
- **n_analysed: 4253** — Methods, Participants — «this group contained 333 adults with misophonia (77 male and 256 female) and 3920 without misophonia (1375 male, 2542 female, 3 unknown)»
- **population: gp_probability** — Methods, Participants — «The initial number of pregnancies enrolled was 14,541, with an additional 913 eligible pregnancies added retrospectively in subsequent waves.»
- **sampling: census** — Methods, Participants — «Pregnant women who were resident in Avon, UK with expected dates of delivery from 1st April 1991 to 31st December 1992 were invited to take part in the study.»

**Остальные поля:**
- clinical_group: NA — NA
- country: GBR — Methods, Participants — «Pregnant women who were resident in Avon, UK with expected dates of delivery from 1st April 1991 to 31st December 1992 were invited to take part in the study.»
- setting: community (population-based birth cohort, ALSPAC 'Children of the 90s', Avon, UK; follow-up wave at age 28) — Methods, Participants — «as part of the "Life at 28+" wave of data collection, in over 4000 of the active remaining respondents from the index cohort (known as the 'Children of the 90s…»
- data_years: 2020-2021 — Methods, Participants — «we screened for misophonia almost three decades later in Dec 2020- Feb 2021 as part of the "Life at 28+" wave»
- design: cross-sectional — Methods, Participants; Procedure — «Our SSfM (misophonia screener) was administered as part of ALSPAC's "Life at 28+" wave of data collection.»
- topic_disclosed: no — Procedure — «Our SSfM (misophonia screener) was administered as part of ALSPAC's "Life at 28+" wave of data collection.»
- inclusion_exclusion: ALSPAC index cohort members (born 1991-92 in Avon) still active at the 'Life at 28+' wave who returned screener data; no other exclusions stated — Methods, Participants — «Our participants with returned data were 4253 adults aged 28»
- n_invited: NR — Methods, Participants — «in over 4000 of the active remaining respondents from the index cohort»
- n_responded: 4253 — Methods, Participants — «Our participants with returned data were 4253 adults aged 28»
- response_rate: NR — Methods, Participants — «in over 4000 of the active remaining respondents from the index cohort»
- age_mean: 28.8 — Methods, Participants — «1452 males-at-birth (mean age in months 345.81; SD 5.94), 2798 female-at-birth (mean age in months 345.49; SD 6.04) and 3 with no information about sex-at-birt…»
- age_sd: NR — Methods, Participants — «(mean age in months 345.81; SD 5.94) ... (mean age in months 345.49; SD 6.04)»
- age_min: NR — NA
- age_max: NR — NA
- age_group: adults — Methods, Participants — «Our participants with returned data were 4253 adults aged 28»
- pct_female: 65.8 — Methods, Participants — «4253 adults aged 28, comprising 1452 males-at-birth ..., 2798 female-at-birth ... and 3 with no information about sex-at-birth»
- informant: self — Procedure — «Participants completed the screener online in digital form, with a pencil-and-paper version made available where requested.»
- mode: mixed — Procedure — «Participants completed the screener online in digital form, with a pencil-and-paper version made available where requested.»
- instruments: Sussex Screener for Misophonia (SSfM), English — Materials — «Sussex Screener for Misophonia (SSfM). We developed and administered this written screener as a measure for adult misophonia.»
- instrument_validated_in_language: yes — Materials — «In summary, our screener has both convergent and divergent validity»
- pub_status: journal — Header — «venue: Child psychiatry and human development; DOI: 10.1007/s10578-023-01569-y»
- language: English — Full text — «Mental Health Difficulties in Children who Develop Misophonia: An Examination of ADHD, Depression & Anxiety»
- funding_coi: Misophonia Research Fund and Harrods Creek Donor Advised Fund; ALSPAC core support from UK MRC, Wellcome (217065/Z/19/Z) and University of Bristol; authors declare no competing interests — Funding; Competing Interests — «This research was supported by a grant from the Misophonia Research Fund and the Harrods Creek Donor Advised Fund.»
- notes: The same sample (333/4253) is reported in R0811 and in the other linked reports from the 'Life at 28+' SSfM wave; extract it once. The screening was one follow-up wave of a birth cohort, with heavy attrition from the original cohort (14,901 alive at 1 year). The number invited to the wave is not reported. age_mean was derived from the sex-specific means in months: (1452×345.81 + 2798×345.49 + 3×338.67)/4253 = 345.59 months = 28.8 years. pct_female = 2798/4253. The SSfM validity evidence (convergent/divergent only) is published in this same report. The 3 participants of unknown sex are non-mis…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Frame is the ALSPAC birth cohort, all eligible pregnancies in Avon 1991-92, which matches the cohort/general population the study describes. — Methods, Participants — «Pregnant women who were resident in Avon, UK with expected dates of delivery from 1st April 1991 to 31st December 1992 were invited to take part in the study.»
2. способ отбора: **yes** — Cohort recruited by inviting all eligible pregnancies in the area (census); screener given to the active remaining cohort, not to self-selected misophonics. Attrition is handled under item 9. — R0811, Discussion — «we have the distinct advantage of testing randomly sampled participants (as far as misophonia is concerned) since we did not rely on misophonics to self-refer»
3. размер выборки: **yes** — n = 4253 >= 385. — Methods, Participants — «Our participants with returned data were 4253 adults aged 28»
4. описание выборки и условий: **yes** — Age, sex, setting (ALSPAC, Avon), country and dates are all reported. — Methods, Participants — «we screened for misophonia almost three decades later in Dec 2020- Feb 2021 as part of the "Life at 28+" wave»
5. охват (пропуски): **unclear** — Only participants 'with returned data' are reported; missing or incomplete screener data are not described. — Methods, Participants — «Our participants with returned data were 4253 adults aged 28»
6. валидность определения случая: **no** — Case definition is SSfM (agreement plus disruption at least 'very mildly'); it has only convergent/divergent validity, with no interview or ROC anchoring. — Materials — «Misophonics were classified as those agreeing with our characterisation of misophonia, but also rejecting 'not at all' for its detriment to daily life»
7. единое надёжное измерение: **no** — Online with a paper version on request and no check of mode equivalence; no reliability reported for the SSfM. — Procedure — «Participants completed the screener online in digital form, with a pencil-and-paper version made available where requested.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are clear (333/4253, also by sex), so a CI can be calculated. — Methods, Participants — «this group contained 333 adults with misophonia (77 male and 256 female) and 3920 without misophonia»
9. отклик: **no** — The number invited to the 28+ wave is not reported. 4253 respondents is about 29% of the 14,901 cohort members alive at 1 year, and non-response is not handled. — Methods, Participants — «These 15,454 pregnancies resulted in 15,589 foetuses, of which 14,901 were alive at 1 year of age.»

Правки:
- 

Проверено: да
---

## ST032 · Sahin 2025 · Frontiers in neurology

Основной отчёт R0399: [текст](../../fulltext/text/R0399.txt) — «Assessing misophonia as a potential comorbidity in migraine patients compared to controls: a cross-sectional study.» — [DOI](https://doi.org/10.3389/fneur.2025.1545520)
Расхождения в тексте: The prevalences agree with the counts: 92/205 = 44.9% and 36/205 = 17.6% (Abstract; Table 1). Internal inconsistencies, none of which affect the prevalence counts: (1) Table 1, family history of migraine: MG-w-M is 61 (66.3%) under Group 2 but 31 (33.7%) under Group 3, and 31 + 43 = 74, which does not match the MG total of 131. (2) Table 2, MOH: the MG value is 29 (63.0), but the subgroups give 28 + 25 = 53. (3) The Discussion says 58.7% of MG-wo-M had moderate or severe disability, while Table 2 gives (27 + 28)/113 = 48.7%. (4) Table 1 history of anxiety: MG-wo-M is printed as 9 (8.08); 9/113 = 7.96%. (5) The Y-BOCS-SR bands overlap (severe 21-31), which is irrelevant here. Figure 1 (participant flow) and Figure 4 (misophonia distribution) are not in the text provided.
Заметка ИИ: Two samples were extracted: migraine patients (clinical, migraine) and separately recruited healthy controls (hospital staff and patients' relatives). Both use the Turkish MQ with Misophonia Severity Scale >= 7 (L2). Sex subgroup counts were derived from Table 1. Clinical subgroups by migraine type and aura come from Table 2. The MQ was self-completed during a face-to-face session with a neurology resident. By rule G7 the level stays L2. Mode is coded as face-to-face interview and informant as self. JBI item 3 for the patient sample uses the n >= 139 clinical threshold; a reviewer should chec…

### ST032-1 · Migraine patients, Acibadem Maslak Hospital neurology clinic, Istanbul, TUR, n=205
Отчёты: R0399 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **92 / 205** | 44.9 | Table 1; Abstract | «MG-w-Mn = 92 / CG-w-Mn = 36 ... (44.9% vs. 17.6%)» |
| E2 | female | MQ · MSS>=7 | **L2** | **85 / 173** | 49.1 | Table 1 | «Female sex a, n (%) / 173 (84.4) / 173 (84.4) / ... / 85 (92.4) / 34 (94.4)» |
| E3 | male | MQ · MSS>=7 | **L2** | **7 / 32** | 21.9 | Table 1 | «Female sex a, n (%) / 173 (84.4) ... MG-w-Mn = 92 ... 85 (92.4)» |
| E4 | episodic migraine | MQ · MSS>=7 | **L2** | **67 / 159** | 42.1 | Table 2 | «EM / 159 (77.6) / 67 (72.8) / 92 (81.4)» |
| E5 | chronic migraine | MQ · MSS>=7 | **L2** | **25 / 46** | 54.3 | Table 2 | «CM / 46 (22.4) / 25 (27.2) / 21 (18.6)» |
| E6 | migraine with aura | MQ · MSS>=7 | **L2** | **34 / 53** | 64.2 | Table 2 | «Presence of aura / 53 (25.8) / 34 (37.0) / 19 (16.8)» |
| E7 | migraine without aura | MQ · MSS>=7 | **L2** | **58 / 152** | 38.2 | Table 2 | «Presence of aura / 53 (25.8) / 34 (37.0) / 19 (16.8)» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2 recommended); у авторов: «clinically significant misophonia»; главная у авторов: yes; период: NR; заметка: 44.9% reported in abstract
- E2: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; **расчёт: cases = females in MG-w-M (85, Table 1); n = females in MG (173, Table 1)**
- E3: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; **расчёт: cases = 92 - 85 = 7; n = 205 - 173 = 32 (Table 1)**
- E4: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR
- E5: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR
- E6: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR
- E7: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; **расчёт: cases = 92 - 34 = 58; n = 205 - 53 = 152 (Table 2)**

**Ключевые поля выборки:**
- **n_analysed: 205** — Results, Sociodemographic features — «A total of 205 migraine patients (MG) and 205 healthy controls (CG) were included in the analyses.»
- **population: clinical** — Inclusion and exclusion criteria — «A diagnosis of migraine (episodic or chronic; with or without aura) confirmed by expert neurologists specializing in headache disorders»
- **sampling: NR** — Methods, Study population — «Figure 1 illustrates the participant flow throughout the study.»

**Остальные поля:**
- clinical_group: other: migraine (ICHD-3) — Inclusion and exclusion criteria — «according to the International Classification of Headache Disorders, 3rd edition (ICHD-3)»
- country: TUR — Methods, Study population — «data were collected from 205 migraine patients and 205 healthy controls at Acibadem Maslak Hospital's Neurology Clinic»
- setting: clinic (tertiary headache centre, hospital neurology clinic) — Strengths and limitations — «This study was conducted in a tertiary headache center»
- data_years: 2022-2023 — Methods, Study population — «between September 1, 2022, and May 30, 2023»
- design: cross-sectional — Methods, Study population — «In this cross-sectional study, data were collected from 205 migraine patients»
- topic_disclosed: NR — Methods — «Written informed consent was obtained from all participants.»
- inclusion_exclusion: Age 18-65, literate, ICHD-3 migraine confirmed by headache specialists; excluded major neurological disorders, psychiatric hospitalisation past year, substance use disorder or psychotropics past 30 days, pregnancy/lactation, severe medical illness — Inclusion and exclusion criteria — «Participants were eligible for inclusion if they were between 18 and 65 years of age, literate, capable of providing informed consent»
- n_invited: NR — Methods — «Figure 1 illustrates the participant flow throughout the study.»
- n_responded: NR — Methods — «Figure 1 illustrates the participant flow throughout the study.»
- response_rate: NR — Methods — «Figure 1 illustrates the participant flow throughout the study.»
- age_mean: 36.5 — Table 1 — «Age (years) b, (Mean, SD) 95% CI | 36.5 (9.4)»
- age_sd: 9.4 — Table 1 — «Age (years) b, (Mean, SD) 95% CI | 36.5 (9.4)»
- age_min: NR — Inclusion and exclusion criteria — «between 18 and 65 years of age»
- age_max: NR — Inclusion and exclusion criteria — «between 18 and 65 years of age»
- age_group: adults — Inclusion and exclusion criteria — «between 18 and 65 years of age»
- pct_female: 84.4 — Table 1 — «Female sex a, n (%) | 173 (84.4)»
- informant: self — Assessments — «sufficient cognitive and language abilities to complete self-report questionnaires reliably»
- mode: face-to-face interview — Assessments — «All participants completed a standardized battery of assessments during a 20-min face-to-face interview conducted by a single neurology resident.»
- instruments: Misophonia Questionnaire (MQ), Turkish version (revised factor structure) — Misophonia questionnaire — «In this study, the MQ was applied following this revised structure.»
- instrument_validated_in_language: yes — Misophonia questionnaire — «In the Turkish validation and reliability study, exploratory and confirmatory factor analyses revealed that the 'Misophonia Emotions and Behaviors' part divide…»
- pub_status: journal — Header — «Frontiers in neurology; DOI: 10.3389/fneur.2025.1545520»
- language: English — Full text — «Assessing misophonia as a potential comorbidity in migraine patients compared to controls: a cross-sectional study»
- funding_coi: No funding; no conflicts of interest declared — Funding Statement; Conflict of interest — «no financial support was received for the research and/or publication of this article»
- notes: Clinical sample recruited for migraine at a tertiary headache centre. The text does not say whether patients were recruited consecutively; participant flow is shown only in Figure 1, which is not available. The MQ was completed during a face-to-face session with a neurology resident. Clinical subgroup counts by migraine type and aura come from Table 2.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Study claims to describe individuals with migraine; frame is a single tertiary headache centre only. — Strengths and limitations — «This study was conducted in a tertiary headache center, where a high proportion of patients are typically on prophylactic treatment.»
2. способ отбора: **unclear** — How patients were selected (consecutive or not) is not described in text. — Methods, Study population — «Figure 1 illustrates the participant flow throughout the study.»
3. размер выборки: **yes** — Clinical sample n=205 >= 139. — Results — «A total of 205 migraine patients (MG)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Methods; Table 1 — «Acibadem Maslak Hospital's Neurology Clinic between September 1, 2022, and May 30, 2023»
5. охват (пропуски): **yes** — No missing data reported. — Statistical analysis — «The final dataset was complete, with no missing data.»
6. валидность определения случая: **yes** — MQ Misophonia Severity Scale >=7, Turkish validated version. — Misophonia questionnaire — «Those with a score of ≥7 on the Misophonia Severity Scale were classified as having clinically significant misophonia»
7. единое надёжное измерение: **yes** — Same instrument, mode and threshold for all; Turkish validation and reliability study cited as source. — Assessments; Misophonia questionnaire — «All participants completed a standardized battery of assessments during a 20-min face-to-face interview conducted by a single neurology resident.»
8. статистика (числитель и знаменатель): **yes** — Numerator 92 and denominator 205 clear; CI calculable. — Table 1; Abstract — «MG-w-Mn = 92 ... MG-wo-Mn = 113»
9. отклик: **unclear** — Number approached/declined not reported. — Methods — «Figure 1 illustrates the participant flow throughout the study.»

Правки:
- 

Проверено: да
### ST032-2 · Healthy controls (hospital staff, administrative staff, patients' relatives), Acibadem Maslak Hospital, TUR, n=205
Отчёты: R0399 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **36 / 205** | 17.6 | Table 1; Abstract | «CG-w-Mn = 36 ... (44.9% vs. 17.6%)» |
| E2 | female | MQ · MSS>=7 | **L2** | **34 / 173** | 19.7 | Table 1 | «Female sex a, n (%) / 173 (84.4) / 173 (84.4) / ... / 85 (92.4) / 34 (94.4)» |
| E3 | male | MQ · MSS>=7 | **L2** | **2 / 32** | 6.2 | Table 1 | «173 (84.4) ... CG-w-Mn = 36 ... 34 (94.4)» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2 recommended); у авторов: «clinically significant misophonia»; главная у авторов: yes; период: NR; заметка: 17.6% reported in abstract
- E2: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; **расчёт: cases = females in CG-w-M (34, Table 1); n = females in CG (173, Table 1)**
- E3: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; **расчёт: cases = 36 - 34 = 2; n = 205 - 173 = 32 (Table 1)**

**Ключевые поля выборки:**
- **n_analysed: 205** — Results — «205 healthy controls (CG) were included in the analyses»
- **population: other_nonclinical** — Inclusion and exclusion criteria — «recruited from hospital personnel, administrative staff, and the non-migraine-affected relatives of patients»
- **sampling: convenience** — Inclusion and exclusion criteria — «recruited from hospital personnel, administrative staff, and the non-migraine-affected relatives of patients, matched for age and sex distribution to the MG»

**Остальные поля:**
- clinical_group: NA — Inclusion and exclusion criteria — «No lifetime history of migraine or frequent other primary headache disorders.»
- country: TUR — Methods, Study population — «205 healthy controls at Acibadem Maslak Hospital's Neurology Clinic»
- setting: clinic (hospital: staff and patients' relatives) — Inclusion and exclusion criteria — «Participants in the CG were recruited from hospital personnel, administrative staff, and the non-migraine-affected relatives of patients»
- data_years: 2022-2023 — Methods, Study population — «between September 1, 2022, and May 30, 2023»
- design: cross-sectional — Methods, Study population — «In this cross-sectional study»
- topic_disclosed: NR — Methods — «Written informed consent was obtained from all participants.»
- inclusion_exclusion: Age 18-65, literate; no lifetime migraine or frequent other primary headache; same exclusions as patients; age- and sex-matched to MG — Inclusion and exclusion criteria — «For the Control Group (CG): No lifetime history of migraine or frequent other primary headache disorders.»
- n_invited: NR — Methods — «Figure 1 illustrates the participant flow throughout the study.»
- n_responded: NR — Methods — «Figure 1 illustrates the participant flow throughout the study.»
- response_rate: NR — Methods — «Figure 1 illustrates the participant flow throughout the study.»
- age_mean: 36.5 — Table 1 — «Age (years) b, (Mean, SD) 95% CI | 36.5 (9.4) | 36.5 (10.0)»
- age_sd: 10.0 — Table 1 — «36.5 (9.4) | 36.5 (10.0)»
- age_min: NR — Inclusion and exclusion criteria — «between 18 and 65 years of age»
- age_max: NR — Inclusion and exclusion criteria — «between 18 and 65 years of age»
- age_group: adults — Inclusion and exclusion criteria — «between 18 and 65 years of age»
- pct_female: 84.4 — Table 1 — «Female sex a, n (%) | 173 (84.4) | 173 (84.4)»
- informant: self — Assessments — «complete self-report questionnaires reliably»
- mode: face-to-face interview — Assessments — «All participants completed a standardized battery of assessments during a 20-min face-to-face interview conducted by a single neurology resident.»
- instruments: Misophonia Questionnaire (MQ), Turkish version (revised factor structure) — Misophonia questionnaire — «In this study, the MQ was applied following this revised structure.»
- instrument_validated_in_language: yes — Misophonia questionnaire — «In the Turkish validation and reliability study, exploratory and confirmatory factor analyses revealed»
- pub_status: journal — Header — «Frontiers in neurology; DOI: 10.3389/fneur.2025.1545520»
- language: English — Full text — «Assessing misophonia as a potential comorbidity in migraine patients compared to controls: a cross-sectional study»
- funding_coi: No funding; no conflicts of interest declared — Funding Statement; Conflict of interest — «no financial support was received for the research and/or publication of this article»
- notes: Control group recruited separately from the patients (hospital staff, administrative staff and patients' relatives) and matched to the migraine group on age and sex. The authors acknowledge selection bias. Because sex was matched by design, the sex-specific rates reflect the matching.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Healthy controls drawn from hospital staff and patients' relatives, not a frame of the general population. — Strengths and limitations — «The control group was selected from hospital staff and relatives of patients, which introduces potential selection bias.»
2. способ отбора: **no** — Convenience recruitment, matched on age and sex. — Inclusion and exclusion criteria — «recruited from hospital personnel, administrative staff, and the non-migraine-affected relatives of patients, matched for age and sex distribution»
3. размер выборки: **no** — n=205 < 385. — Results — «205 healthy controls (CG) were included in the analyses»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Methods; Table 1 — «between September 1, 2022, and May 30, 2023»
5. охват (пропуски): **yes** — No missing data. — Statistical analysis — «The final dataset was complete, with no missing data.»
6. валидность определения случая: **yes** — MQ MSS >=7, Turkish validated version. — Misophonia questionnaire — «Those with a score of ≥7 on the Misophonia Severity Scale were classified as having clinically significant misophonia»
7. единое надёжное измерение: **yes** — Same instrument, mode and threshold for all; Turkish validation and reliability study cited. — Assessments — «All participants completed a standardized battery of assessments during a 20-min face-to-face interview conducted by a single neurology resident.»
8. статистика (числитель и знаменатель): **yes** — 36/205 clear; CI calculable. — Table 1; Abstract — «CG-w-Mn = 36 ... (44.9% vs. 17.6%)»
9. отклик: **unclear** — Number approached not reported. — Methods — «Figure 1 illustrates the participant flow throughout the study.»

Правки:
- 

Проверено: да
---

## ST033 · Valsa 2025 · Neuroscience Research Notes

Основной отчёт R0431: [текст](../../fulltext/text/R0431.txt) · [PDF](../../fulltext/pdf/R0431.pdf) — «Estimation of prevalence and severity of misophonia in adults from India» — [DOI](https://doi.org/10.31117/neuroscirn.v8i3.417)
Расхождения в тексте: 1) Methods (p.3) print the MAQ mild band as '12-14'. The moderate band starts at 25, so mild was read as 12-24 (version A bands). 2) There is no 'severe' (38-50) column in Table 1 or count in the Results. The band percentages sum to about 100% (81.30+14.95+2.80+0.93), so the severe band was taken as 0. 3) The Discussion (p.4) says '0.93% had extremely severe misophonia, 9.34% had moderate misophonia, and 5.60% had mild misophonia'. This contradicts the Results and Table 1 (mild 14.95%, N=16; moderate 2.80%, N=3); Table 1 and the Results were used. 4) Text and Table 1 call the top band 'highly severe' and also 'extremely severe'. 5) Sex band counts back-calculate exactly (female 61/10/2/1 of 74; male 26/6/1/0 of 33) and sum to the overall 87/16/3/1. 6) Urban/rural bands are inconsistent: urban 82.43+16.41+1.35 = 100.19%, and 16.41% x 74 is not an integer. Rural (27/3/2/1 of 33) plus urba…
Заметка ИИ: One sample, 12 estimates: L0, L1 (>=12), L2 (>=25) and L2 (>=38) for all, female and male. Band percentages were converted to counts of the misophonia cases (74 female, 33 male). Not extracted: ear-problem and hearing-loss figures (11.21% and 4.67% of those with misophonia), because they are given as a share of cases, not as prevalence within those subgroups. Appendix A (the questionnaire) was not in the text supplied, so the time frame is NR. Page 4 has a mismatched running header ('ISSUE 1 | ARTICLE 364').

### ST033-1 · Online survey of adults aged 30-50, India, n=341
Отчёты: R0431 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MAQ · 'misophonia' = MAQ score above an unstated threshold inside the subclinical band (0-11); includes 87 subclinical scorers | **L0** | **107 / 341** | 31.4 | Page 3, Results; Page 4, Table 1 | «out of 341 subjects, the prevalence of misophonia was approximately 31.37% (N=107)... 81.30% (N=87) had sub-clinical misophonia» |
| E2 | all | MAQ · MAQ>=12 (mild or more) | **L1** | **20 / 341** | 5.9 | Page 3, Results | «only one had a highly severe degree of misophonia (0.93%)... 2.80% had a moderate degree of misophonia (N=3)... and 14.95% had a mild degree (N=16)» |
| E3 | all | MAQ · MAQ>=25 (moderate or more) | **L2** | **4 / 341** | 1.2 | Page 3, Results | «only one had a highly severe degree of misophonia (0.93%)... 2.80% had a moderate degree of misophonia (N=3)» |
| E4 | all | MAQ · MAQ>=38 (severe or more) | **L2** | **1 / 341** | 0.3 | Page 3, Results; Page 4, Table 1 | «Among those with misophonia, only one had a highly severe degree of misophonia (0.93%)» |
| E5 | female | MAQ · 'misophonia' = MAQ score above an unstated threshold inside the subclinical band (0-11) | **L0** | **74 / 232** | 31.9 | Page 4, Table 1 | «Female 232 74 31.89 82.43 13.51 2.70 1.35» |
| E6 | female | MAQ · MAQ>=12 (mild or more) | **L1** | **13 / 232** | 5.6 | Page 4, Table 1 | «Female 232 74 31.89 82.43 13.51 2.70 1.35» |
| E7 | female | MAQ · MAQ>=25 (moderate or more) | **L2** | **3 / 232** | 1.3 | Page 4, Table 1 | «Female 232 74 31.89 82.43 13.51 2.70 1.35» |
| E8 | female | MAQ · MAQ>=38 (severe or more) | **L2** | **1 / 232** | 0.4 | Page 4, Table 1 | «Female 232 74 31.89 82.43 13.51 2.70 1.35» |
| E9 | male | MAQ · 'misophonia' = MAQ score above an unstated threshold inside the subclinical band (0-11) | **L0** | **33 / 109** | 30.3 | Page 4, Table 1 | «Male 109 33 30.27 78.78 18.18 3.03 0.00» |
| E10 | male | MAQ · MAQ>=12 (mild or more) | **L1** | **7 / 109** | 6.4 | Page 4, Table 1 | «Male 109 33 30.27 78.78 18.18 3.03 0.00» |
| E11 | male | MAQ · MAQ>=25 (moderate or more) | **L2** | **1 / 109** | 0.9 | Page 4, Table 1 | «Male 109 33 30.27 78.78 18.18 3.03 0.00» |
| E12 | male | MAQ · MAQ>=38 (severe or more) | **L2** | **0 / 109** | 0.0 | Page 4, Table 1 | «Male 109 33 30.27 78.78 18.18 3.03 0.00» |

- E1: источник порога: study's own; правило: MAQ row; L0 = sum inside subclinical band (could also be NR under G6, because the exact threshold is not stated); у авторов: «prevalence of misophonia»; главная у авторов: yes; период: NR; заметка: Headline estimate. 87 of the 107 cases fall in the subclinical band (0-11), so the threshold lies inside the subclinical range but is never stated.
- E2: источник порога: developer paper; правило: MAQ row, version A (L1 >=12); G1 sum of bands; у авторов: «mild, moderate, highly severe misophonia»; главная у авторов: no; период: NR; **расчёт: mild 16 + moderate 3 + highly severe 1 (severe band 0) = 20**; заметка: The Methods print the mild band as 12-14 (typo; the moderate band starts at 25, so mild = 12-24). Table 1 has no 'severe' column; the band percentages add to about 100%, so severe = 0.
- E3: источник порога: developer paper; правило: MAQ row, version A (L2 >=25); G1 sum of bands; у авторов: «moderate or highly severe misophonia»; главная у авторов: no; период: NR; **расчёт: moderate 3 + highly severe 1 (severe 0) = 4**; заметка: Band cut-off without anchoring (JBI 6 = no; excluded in sensitivity analysis 2).
- E4: источник порога: developer paper; правило: MAQ row, version A; G2 threshold above L2 cut-off; G1 sum of bands; у авторов: «highly severe misophonia»; главная у авторов: no; период: NR; **расчёт: severe band 0 (not reported, percentages sum to ~100%) + highly severe 1 = 1**; заметка: No severe band column in Table 1.
- E5: источник порога: study's own; правило: MAQ row; L0 = sum inside subclinical band (G6 possible); у авторов: «misophonia»; главная у авторов: no; период: NR
- E6: источник порога: developer paper; правило: MAQ row, version A (L1 >=12); G1 sum of bands; у авторов: «mild, moderate, extremely severe misophonia»; главная у авторов: no; период: NR; **расчёт: Of 74 female cases: mild 13.51% x 74 = 10.0 -> 10; moderate 2.70% x 74 = 2.0 -> 2; highly severe 1.35% x 74 = 1.0 -> 1; 10+2+1 = 13**; заметка: Band percentages are of the 74 cases, not of the 232 women.
- E7: источник порога: developer paper; правило: MAQ row, version A (L2 >=25); G1 sum of bands; у авторов: «moderate or extremely severe misophonia»; главная у авторов: no; период: NR; **расчёт: moderate 2.70% x 74 = 2.0 -> 2; highly severe 1.35% x 74 = 1.0 -> 1; 2+1 = 3**
- E8: источник порога: developer paper; правило: MAQ row, version A; G2; G1 sum of bands; у авторов: «extremely severe misophonia»; главная у авторов: no; период: NR; **расчёт: highly severe 1.35% x 74 = 1.0 -> 1; severe band 0**
- E9: источник порога: study's own; правило: MAQ row; L0 = sum inside subclinical band (G6 possible); у авторов: «misophonia»; главная у авторов: no; период: NR
- E10: источник порога: developer paper; правило: MAQ row, version A (L1 >=12); G1 sum of bands; у авторов: «mild or moderate misophonia»; главная у авторов: no; период: NR; **расчёт: Of 33 male cases: mild 18.18% x 33 = 6.0 -> 6; moderate 3.03% x 33 = 1.0 -> 1; highly severe 0; 6+1 = 7**
- E11: источник порога: developer paper; правило: MAQ row, version A (L2 >=25); G1 sum of bands; у авторов: «moderate misophonia»; главная у авторов: no; период: NR; **расчёт: moderate 3.03% x 33 = 1.0 -> 1; highly severe 0.00% -> 0; 1+0 = 1**
- E12: источник порога: developer paper; правило: MAQ row, version A; G2; G1 sum of bands; у авторов: «highly severe misophonia»; главная у авторов: no; период: NR; **расчёт: highly severe 0.00% x 33 = 0; severe band 0**

**Ключевые поля выборки:**
- **n_analysed: 341** — Page 4, Table 1 — «Overall 341 107 31.37»
- **population: gp_other** — Page 3, 2.2 Subjects — «341 adults from all over India with diverse cultural, educational, linguistic, and economic backgrounds»
- **sampling: convenience** — Page 3, 2.3 The survey — «The researchers did not specifically pick the survey participants; rather, they self-selected, meaning they decided to participate voluntarily.»

**Остальные поля:**
- clinical_group: NA — Page 3, 2.2 Subjects — «341 adults from all over India»
- country: IND — Page 3, 2.2 Subjects — «The total participants in the study were 341 adults from all over India»
- setting: community adults recruited through an open online survey (Google Forms), all over India — Page 3, 2.3 The survey — «An online survey was conducted wherein the participants filled out the Misophonia Assessment Questionnaire (MAQ) using Google Forms.»
- data_years: NR — Page 3, 2.1 Ethical consideration — «Ethical Institutional Review Board (REF/SH/IRB/2023/12)»
- design: cross-sectional — Page 3, 2.3 The survey — «An online survey was conducted wherein the participants filled out the Misophonia Assessment Questionnaire (MAQ) using Google Forms.»
- topic_disclosed: NR — Page 3, 2.3 The survey — «The researchers did not specifically pick the survey participants; rather, they self-selected»
- inclusion_exclusion: Age 30-50 years; studied English to 12th standard; able to use Google Forms. No exclusion criteria stated (participants with otological problems or hearing loss were included). — Page 3, 2.3 The survey — «Participants selected for this study are in the age range of 30 – 50 years, studied English till 12th standard, and were able to use Google Forms to respond to…»
- n_invited: NR — Page 3, 2.3 The survey — «they self-selected, meaning they decided to participate voluntarily»
- n_responded: NR — Page 3, 2.2 Subjects — «The total participants in the study were 341 adults»
- response_rate: NR — Page 3, 2.3 The survey — «they self-selected, meaning they decided to participate voluntarily»
- age_mean: 39.48 — Page 3, 2.2 Subjects — «The participants ranged from 30 to 50 years, with a mean age of 39.48 and a standard deviation of 5.91.»
- age_sd: 5.91 — Page 3, 2.2 Subjects — «with a mean age of 39.48 and a standard deviation of 5.91»
- age_min: 30 — Page 3, 2.2 Subjects — «The participants ranged from 30 to 50 years»
- age_max: 50 — Page 3, 2.2 Subjects — «The participants ranged from 30 to 50 years»
- age_group: adults — Page 3, 2.2 Subjects — «The participants ranged from 30 to 50 years»
- pct_female: 68 — Page 3, 2.2 Subjects — «There were 232 female participants (68%) and 109 male participants (32%).»
- informant: self — Page 3, 2.3 The survey — «It is a self-rating questionnaire with a four-point Likert-type rating scale»
- mode: online — Page 3, 2.3 The survey — «participants filled out the Misophonia Assessment Questionnaire (MAQ) using Google Forms»
- instruments: MAQ (Misophonia Assessment Questionnaire, Johnson, revised by Dozier 2015), English version, 21 items, 0-63 — Page 3, 2.3 The survey — «The Misophonia Assessment Questionnaire by Marsha Johnson and revised by Tom Dozier (2015) was used ... The MAQ is a 21-item questionnaire»
- instrument_validated_in_language: NR — Page 3, 2.3; Page 6, 4.1 — «The Misophonia Assessment Questionnaire by Marsha Johnson and revised by Tom Dozier (2015) was used to assess the severity»
- pub_status: journal — Page 1, header — «NEUROSCIENCE RESEARCH NOTES ... Received: 9 December 2024; Accepted: 23 June 2025; Published: 21 September 2025»
- language: English — Full text — «Estimation of prevalence and severity of misophonia in adults from India»
- funding_coi: Funding not reported; authors declare no conflict of interest. — Page 7, Conflicts of Interest — «Conflicts of Interest: The authors declare no conflict of interest.»
- notes: 1) The authors' headline 'misophonia' prevalence (31.37%, 107/341) counts 87 subclinical scorers (MAQ 0-11) as cases, and the threshold for being a case is never stated. Coded L0; G6 (NR) is an alternative. 2) Band counts are of the 107 cases, not of the whole sample, and were converted to cumulative counts over 341. 3) MAQ band version A (0-11/12-24/25-37/38-50/51-63) is attributed to Johnson/Dozier 2015, and no validation of the version used is cited. 4) The same group (AIISH Mysuru, Prabhu) ran other Indian prevalence surveys of students (Aryal & Prabhu 2022; Patel et al. 2023; Sujeeth et …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is adults aged 30-50 in India; the frame was self-selected Google Forms users proficient in English, which is only part of that population. — Page 3, 2.3; Page 6, 4.1 — «The current study considered only participants who were proficient in English. Hence, the study findings cannot be generalised to the non-English-speaking popu…»
2. способ отбора: **no** — Voluntary self-selection into an open online survey. — Page 3, 2.3 The survey — «The researchers did not specifically pick the survey participants; rather, they self-selected, meaning they decided to participate voluntarily.»
3. размер выборки: **no** — n = 341, below 385. — Page 3, 2.2 Subjects — «The total participants in the study were 341 adults»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported, but dates of data collection are missing (one item missing). — Page 3, 2.2 Subjects — «The participants ranged from 30 to 50 years, with a mean age of 39.48 ... There were 232 female participants (68%) and 109 male participants (32%).»
5. охват (пропуски): **unclear** — Incomplete responses and missing data are not reported. — Page 3, 2.2-2.4 — «Total scores were calculated for each individual, and the severity of misophonia was estimated.»
6. валидность определения случая: **no** — No L3. The L2 definition is MAQ >=25 (version A moderate band), a band cut-off with no anchoring; no validation of the version used is cited. The authors' primary 'misophonia' definition includes the subclinical band an… — Page 3, 2.3 The survey — «participants were categorised into subclinical (0-11), mild (12-14), moderate (25-37), severe (38-50), and highly severe (51-63)»
7. единое надёжное измерение: **unclear** — Same instrument, mode and banding for everyone, but no internal consistency is reported in this sample or a cited source. — Page 3, 2.3 The survey — «An online survey was conducted wherein the participants filled out the Misophonia Assessment Questionnaire (MAQ) using Google Forms.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are given (107/341), band counts can be traced, and a CI can be calculated (none reported). The case threshold of the headline estimate is not stated. — Page 4, Table 1 — «Overall 341 107 31.37 81.30 14.95 2.80 0.93»
9. отклик: **no** — Open online survey with no denominator of invited people; non-response not handled. — Page 3, 2.3 The survey — «they self-selected, meaning they decided to participate voluntarily»

Правки:
- 

Проверено: да
---

## ST034 · Yamazawa 2025 · The Japanese journal of psychology

Основной отчёт R0446: [текст](../../fulltext/text/R0446.txt) · [PDF](../../fulltext/pdf/R0446.pdf) — «A study of the prevalence of auditory hypersensitivity in university students: Aspects of hyperacusis and misophonia» — [DOI](https://doi.org/10.4992/jjpsy.96.23333)
Приложен R0660: [текст](../../fulltext/text/R0660.txt) · [PDF](../../fulltext/pdf/R0660.pdf) — «Hyperacusis and Misophonia»
Связь отчётов: Japanese university students (n = 439, 2023): article R0446 and convention abstract R0660
Расхождения в тексте: The English abstract gives a 7.2% comorbidity rate for hyperacusis and misophonia. The Results, the Discussion and R0660 give 7.3% (n=32); 32/439 = 7.29%. The 440 respondents were 257 male and 183 female; the 439 analysed were 256 male and 183 female. R0660 (convention abstract, 2024) gives the same n, prevalence (40%, n=176) and cut-off as the main report. It describes the aim as studying '一般成人' [general adults], but the sample is university students. It cites Wu et al. as 2013, while the main report cites 2014. In Table 3 the age t-test p value (.099 for t=0.087) looks inconsistent, but this does not affect prevalence.
Заметка ИИ: There is one eligible sample. The prevalence estimate uses MQ Symptom Scale >=14, which is L1 under Table 1, so JBI 6 = no. The MQ Misophonia Severity Scale was not reported, so no L2 estimate is available.

### ST034-1 · University students, private university in Tokyo (psychology classes), Japan, n=439
Отчёты: R0446 (main); R0660

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ Symptom Scale >=14 | **L1** | **176 / 439** | 40.1 | Page 3, 結果; abstract (Page 1) | «音嫌悪症尺度のカットオフ値を超える割合は40%（n=176），音過敏症尺度と音嫌悪症尺度双方のカットオフ値を超える割合は7.3%（n=32）であった。» |

- E1: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 = L1 (G2); у авторов: «音嫌悪症尺度のカットオフ値を超える割合 [proportion exceeding the misophonia scale cut-off]; 'preva…»; главная у авторов: yes; период: NR; заметка: 176/439 = 40.1%. Cut-off attributed to Wu et al. 2014. No prevalence by sex reported (only mean scores by sex, Table 3). Comorbid hyperacusis plus misophonia (32/439, 7.3%) is not a separate misophonia case definition.

**Ключевые поля выборки:**
- **n_analysed: 439** — Page 2, 方法 対象者と手続き — «すべての項目に回答していた439 名（男性256 名，女性183 名，平均年齢19.57 歳（SD=1.35））を分析対象とした。»
- **population: university_students** — Page 2, 方法 対象者と手続き — «心理学の授業を履修する大学生440 名 [440 university students taking psychology classes]»
- **sampling: convenience** — Page 2, 方法 対象者と手続き — «調査対象者は都内の私立大学で心理学の授業を履修する大学生440 名 [participants were 440 students taking psychology classes at a private university in Tokyo]»

**Остальные поля:**
- clinical_group: NA — Page 1, abstract — «in a non-clinical sample of 439 individuals»
- country: JPN — Page 2, 方法 対象者と手続き — «調査対象者は都内の私立大学で心理学の授業を履修する大学生440 名 [participants were 440 students taking psychology classes at a private university in Tokyo]»
- setting: university (psychology classes at one private university in Tokyo) — Page 2, 方法 対象者と手続き — «都内の私立大学で心理学の授業を履修する大学生 [university students taking psychology classes at a private university in Tokyo]»
- data_years: 2023 — Page 2, 方法 対象者と手続き — «調査は2023 年7 月から10 月にかけて行われた。[The survey was conducted from July to October 2023.]»
- design: cross-sectional — Page 1, abstract — «We conducted an investigation of the prevalence and interrelationship of these conditions in a non-clinical sample of 439 individuals using self-reported measu…»
- topic_disclosed: NR — Page 3, 倫理的配慮 — «調査にはGoogle フォームを用い，初めに調査目的と以下の倫理的配慮を説明した。[Google Forms was used; the survey purpose and ethical considerations were explained first.]»
- inclusion_exclusion: Students taking psychology classes at one private university in Tokyo; only those who answered all items were analysed (439 of 440) — Page 2, 方法 対象者と手続き — «すべての項目に回答していた439 名（男性256 名，女性183 名，平均年齢19.57 歳（SD=1.35））を分析対象とした。[439 who answered all items were analysed]»
- n_invited: NR — Page 2, 方法 対象者と手続き — «調査対象者は都内の私立大学で心理学の授業を履修する大学生440 名（男性257 名，女性183 名）»
- n_responded: 440 — Page 2, 方法 対象者と手続き — «大学生440 名（男性257 名，女性183 名）であり，すべての項目に回答していた439 名»
- response_rate: NR — Page 2, 方法 対象者と手続き — «調査対象者は都内の私立大学で心理学の授業を履修する大学生440 名»
- age_mean: 19.57 — Page 2, 方法 対象者と手続き — «平均年齢19.57 歳（SD=1.35）»
- age_sd: 1.35 — Page 2, 方法 対象者と手続き — «平均年齢19.57 歳（SD=1.35）»
- age_min: NR — Page 2, 方法 — «平均年齢19.57 歳（SD=1.35）»
- age_max: NR — Page 2, 方法 — «平均年齢19.57 歳（SD=1.35）»
- age_group: adults — Page 2, 方法 対象者と手続き — «大学生…平均年齢19.57 歳（SD=1.35） [university students, mean age 19.57]»
- pct_female: 41.7 — Page 2, 方法 対象者と手続き; Table 3 — «439 名（男性256 名，女性183 名»
- informant: self — Page 1, abstract — «using self-reported measures»
- mode: online — Page 3, 倫理的配慮 — «調査にはGoogle フォームを用い [Google Forms was used for the survey]»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), Japanese version (Tada et al. 2022): Symptom Scale 7 items + Emotions and Behaviors Scale 10 items (MSS not reported) — Page 2, 質問項目 — «Wu et al.（2014）の音嫌悪症尺度（Misophonia Questionnaire: 以下，MQ とする）の日本語版（多田他，2022）を用いた。»
- instrument_validated_in_language: NR — Page 2, 質問項目 — «MQ とする）の日本語版（多田他，2022）を用いた。[the Japanese version of the MQ (Tada et al., 2022) was used]»
- pub_status: journal — Page 1, header — «心理学研究2025 年 第96 巻第3 号 pp. 193-199 研究報告»
- language: Japanese (English abstract) — Page 1 — «大学生における聴覚過敏の保有率に関する検討»
- funding_coi: Chuo University special research grant and JSPS KAKENHI 22K04477; authors declare no conflicts of interest — Page 6, 利益相反 and footnote 1 — «本論文に関して，開示すべき利益相反に関する事項はない。本研究は，中央大学特定課題研究費と科研費（22K04477）の支援を受け，実施された。»
- notes: pct_female derived: 183/439 = 41.7%. Age min/max not reported; age_group coded as adults because participants are university students (mean 19.57). The Japanese MQ is cited to Tada et al. 2022 (a study of ASMR, misophonia and autistic traits); the reviewer should check whether that paper includes a psychometric validation of the Japanese MQ. Cronbach alpha in this sample: MQ total .86, Symptom .77, E&B .81. R0660 (JPA 2024 convention abstract) reports the same sample with identical figures. Tada et al. 2022 (Japanese, n=180) is a separate sample, not overlapping. The other studies in the pape…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target population is Japanese university students; the frame covers only students in psychology classes at one private Tokyo university — Page 2, 方法; Page 6, limitations — «本研究の限界点として調査対象者が都内の大学生に限られた点»
2. способ отбора: **no** — Convenience sample of students in psychology classes; no random selection — Page 2, 方法 対象者と手続き — «調査対象者は都内の私立大学で心理学の授業を履修する大学生440 名»
3. размер выборки: **yes** — n = 439 >= 385 — Page 2, 方法 — «すべての項目に回答していた439 名…を分析対象とした。»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported — Page 2, 方法 — «調査は2023 年7 月から10 月にかけて行われた。…439 名（男性256 名，女性183 名，平均年齢19.57 歳（SD=1.35））»
5. охват (пропуски): **yes** — Only 1 of 440 respondents excluded for incomplete answers (<10%) — Page 2, 方法 — «大学生440 名…すべての項目に回答していた439 名…を分析対象とした。»
6. валидность определения случая: **no** — The primary definition is MQ Symptom Scale >=14, a cut-off without clinical anchoring (listed as no) — Page 2, 質問項目 — «Wu et al.（2014）により音嫌悪症状尺度の得点において14 点がカットオフ値とされ，本研究においてもこれに準拠した。»
7. единое надёжное измерение: **yes** — Same instrument, online mode and threshold for all; Cronbach alpha reported in this sample — Table 3 — «Symptom 10.60 (5.89) 12.61 (5.61) 3.587 .001 .77»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (176/439); CI calculable — Page 3, 結果 — «音嫌悪症尺度のカットオフ値を超える割合は40%（n=176）»
9. отклик: **unclear** — Number of students invited or enrolled in the classes not reported; response rate unknown — Page 2, 方法 — «調査対象者は都内の私立大学で心理学の授業を履修する大学生440 名»

Правки:
- 

Проверено: да
---

## ST035 · Aazh 2024 · Brain sciences

Основной отчёт R0468: [текст](../../fulltext/text/R0468.txt) — «The Sound Sensitivity Symptoms Questionnaire Version 2.0 (SSSQ2) as a Screening Tool for Assessment of Hyperacusis, Misophonia and Noise Sensitivity: Factor An…» — [DOI](https://doi.org/10.3390/brainsci15010016)
Не выписано ИИ: There is no separately recruited misophonia group. However, part of the single sample came through patient support groups for tinnitus and sound intolerance (a possible E1 issue). That part cannot be separated from the university staff and students, so the whole sample was extracted and flagged. The test-retest subsample (n=154) is part of the same sample and is not extracted separately.
Расхождения в тексте: The AMISOS-R bands (91 + 154 + 160 + 46) sum to 451, which matches N=451. The percentages match the counts: 360/451 = 79.8%, 206/451 = 45.7%, 46/451 = 10.2%. MisoQuest: 98/451 = 21.7%, which matches. The text writes 'AMISOS-A' once and 'AMISO-R' once for the AMISOS-R. The Discussion and Conclusions say 'loudness hyperacusis (sum of items 1 and 2)', but the Methods say items 1 and 3. This does not affect the misophonia extraction.
Заметка ИИ: Only the text was supplied, without Tables 1-7. Please check Table 2 for the MisoQuest cut-off and the instrument language versions. Please check Table 4 for the SSSQ2 item 4 endorsement rates, which could give an SSSQ4 estimate. The study is a psychometric validation; no prevalence estimate is the authors' primary result.

### ST035-1 · University of Surrey staff/students plus tinnitus and sound-intolerance support groups, online survey, GBR, n=451
Отчёты: R0468 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MisoQuest · MisoQuest score indicating 'significant misophonia' (cut-off not stated in the report) | **NR** | **98 / 451** | 21.7 | 3.1 Characteristics of the Study Population | «Based on scores for MisoQuest, 21.7% of patients (N = 98) had significant misophonia.» |
| E2 | all | AMISOS-R · AMISOS-R>=11 (mild or more; band boundaries not printed in the report) | **L1** | **360 / 451** | 79.8 | 3.1 Characteristics of the Study Population | «20.2% of patients (N = 91) had no misophonia (i.e., had sub-clinical symptoms), 34.1% (N = 154) had a mild misophonia, 35.5% (N = 160) had a moderate misophonia, and 10.2% (N = 46) had a severe to extreme misophonia» |
| E3 | all | AMISOS-R · AMISOS-R>=21 (moderate or more; band boundaries not printed in the report) | **L2** | **206 / 451** | 45.7 | 3.1 Characteristics of the Study Population | «35.5% (N = 160) had a moderate misophonia, and 10.2% (N = 46) had a severe to extreme misophonia» |
| E4 | all | AMISOS-R · AMISOS-R>=31 (severe to extreme; band boundaries not printed in the report) | **L2** | **46 / 451** | 10.2 | 3.1 Characteristics of the Study Population | «10.2% (N = 46) had a severe to extreme misophonia» |

- E1: источник порога: developer paper; правило: MisoQuest row; G6 (cut-off not stated); у авторов: «significant misophonia»; главная у авторов: no; период: NR; заметка: The cut-off is not stated. If the reviewer confirms (e.g., in Table 2) that the developer cut-off >=61 (Siepsiak 2020, ref 25) was used, recode to L2 with threshold 'MisoQuest>=61'. The MisoQuest language version is not stated.
- E2: источник порога: validation paper; правило: AMISOS-R row; G1 sum of bands (mild + moderate + severe to extreme); у авторов: «mild, moderate, or severe to extreme misophonia»; главная у авторов: no; период: NR; **расчёт: 154 + 160 + 46 = 360 (mild + moderate + severe to extreme), Section 3.1**; заметка: The text says 'AMISOS-A' (typo for AMISOS-R). Band boundaries are not given. The labels match the standard key (0-10 subclinical, 11-20 mild, 21-30 moderate to severe, 31-40 severe to extreme). Bands sum to 451.
- E3: источник порога: validation paper; правило: AMISOS-R row (>=21 listed under L2); G1 sum of bands; у авторов: «moderate or severe to extreme misophonia»; главная у авторов: no; период: NR; **расчёт: 160 + 46 = 206 (moderate + severe to extreme), Section 3.1**; заметка: Unanchored band cut-off (JBI 6 = no). The authors label the band 'moderate' rather than 'moderate to severe'.
- E4: источник порога: validation paper; правило: AMISOS-R row; G2 (threshold above the L2 cut-off); G1 top band; у авторов: «severe to extreme misophonia»; главная у авторов: no; период: NR; заметка: Stricter than the anchored cut-off (>=24).

**Ключевые поля выборки:**
- **n_analysed: 451** — 3.1 Characteristics of the Study Population — «MisoQuest, HIQ, AMISOS-R ... 49 (SD = 12, N = 451), 9.6 (SD = 6.1, N = 451), 18.8 (SD = 9.2, N = 451)»
- **population: other_nonclinical** — 2.3; 4. Discussion — «Another limitation is that the study population was largely non-clinical»
- **sampling: convenience** — 2.3 Study Design and Participants — «The survey was emailed to students and staff members at the University of Surrey and was shared with various patient support groups relevant to tinnitus and sound intolerance via email and social media platforms.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: GBR — 2.3 Study Design and Participants; 1. Introduction — «The survey was emailed to students and staff members at the University of Surrey ... developed at Hashir International Institute (HII), United Kingdom»
- setting: university (Surrey students and staff by email) plus online patient support groups for tinnitus and sound intolerance (email and social media) — 2.3 Study Design and Participants — «The survey was emailed to students and staff members at the University of Surrey and was shared with various patient support groups relevant to tinnitus and so…»
- data_years: NR — NR — «NR»
- design: validation study — 2.3 Study Design and Participants — «This was a psychometric study with cross-sectional survey design.»
- topic_disclosed: NR — 2.3 Study Design and Participants — «An online survey was developed using the Qualtrics platform»
- inclusion_exclusion: NR beyond age 18+ (observed range); anyone completing the online survey — Abstract — «A total of 451 people completed the online survey.»
- n_invited: NR — NR — «NR»
- n_responded: 451 — 2.3 Study Design and Participants — «A total of 451 people completed the online survey, of which 154 individuals completed the survey twice.»
- response_rate: NR — NR — «NR»
- age_mean: 36.5 — 3.1 Characteristics of the Study Population — «The average age of the participants was 36.5 years (standard deviation, SD = 12.8 years, range 18 to 86 years)»
- age_sd: 12.8 — 3.1 Characteristics of the Study Population — «standard deviation, SD = 12.8 years»
- age_min: 18 — 3.1 Characteristics of the Study Population — «range 18 to 86 years»
- age_max: 86 — 3.1 Characteristics of the Study Population — «range 18 to 86 years»
- age_group: adults — 3.1 Characteristics of the Study Population — «range 18 to 86 years»
- pct_female: 60.3 — 3.1 Characteristics of the Study Population — «60.3% were female»
- informant: self — 2.3 Study Design and Participants — «several validated self-report questionnaires were included in the online survey»
- mode: online — 2.3 Study Design and Participants — «An online survey was developed using the Qualtrics platform»
- instruments: MisoQuest (language version not stated; presumably English); AMISOS-R (language version not stated; presumably English); SSSQ2 item 4 (misophonia item, English) — 2.3 Study Design and Participants; 2.2 — «MisoQuest [25], the Amsterdam Misophonia Scale Revised (AMISO-R) [26] ... Item 4 asks about misophonia.»
- instrument_validated_in_language: NR — 2.3 Study Design and Participants — «several validated self-report questionnaires were included in the online survey»
- pub_status: journal — Header — «Year: 2024; venue: Brain sciences; DOI: 10.3390/brainsci15010016»
- language: English — Full text — «The Sound Sensitivity Symptoms Questionnaire Version 2.0 (SSSQ2) as a Screening Tool for Assessment of Hyperacusis, Misophonia and Noise Sensitivity»
- funding_coi: NR (not in the supplied text) — NR — «NR»
- notes: POSSIBLE E1 ISSUE: part of the single sample was recruited through patient support groups for tinnitus and sound intolerance. These cannot be separated from the university staff and students, and the report does not give the split. The reviewer should decide whether the sample is eligible. Psychometric validation of the SSSQ2. A retest subsample of 154 is part of the same sample. The authors call participants 'patients' throughout. Table 4 (SSSQ2 item endorsement rates, including item 4, misophonia) is not in the supplied text. Check Table 4 for an SSSQ4 estimate (item 4 >=2 = L1; score 1 = L…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame (one university's mailing lists plus tinnitus and sound-intolerance support groups) does not cover a defined general population and over-represents people with sound sensitivity. — 2.3 Study Design and Participants — «The survey was emailed to students and staff members at the University of Surrey and was shared with various patient support groups relevant to tinnitus and so…»
2. способ отбора: **no** — Volunteer opt-in convenience sampling via email and social media. — 2.3 Study Design and Participants — «was shared with various patient support groups relevant to tinnitus and sound intolerance via email and social media platforms»
3. размер выборки: **yes** — n=451 is at least 385. — 2.3 Study Design and Participants — «A total of 451 people completed the online survey»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — 3.1 Characteristics of the Study Population — «The average age of the participants was 36.5 years ... and 60.3% were female.»
5. охват (пропуски): **yes** — MisoQuest and AMISOS-R were available for all 451 respondents. — 3.1 Characteristics of the Study Population — «MisoQuest, HIQ, AMISOS-R ... 49 (SD = 12, N = 451), 9.6 (SD = 6.1, N = 451), 18.8 (SD = 9.2, N = 451)»
6. валидность определения случая: **no** — The pooled primary definition is the AMISOS-R moderate band (>=21), which has no anchoring. The MisoQuest 'significant misophonia' cut-off is not stated, and language validation is not reported. — 3.1 Characteristics of the Study Population — «35.5% (N = 160) had a moderate misophonia, and 10.2% (N = 46) had a severe to extreme misophonia»
7. единое надёжное измерение: **unclear** — Everyone used the same online instruments, but reliability of MisoQuest and AMISOS-R is not reported for this sample in the supplied text; alpha is given for the SSSQ2 only. — 3.3 Reliability — «Both Cronbach’s α and McDonald’s ω estimate for the SSSQ2 were 0.80»
8. статистика (числитель и знаменатель): **yes** — Counts and the denominator (451) are given, so CIs can be calculated. — 3.1 Characteristics of the Study Population — «Based on scores for MisoQuest, 21.7% of patients (N = 98) had significant misophonia.»
9. отклик: **no** — Open online survey with no denominator of invited people and no handling of non-response. — 2.3 Study Design and Participants — «A total of 451 people completed the online survey»

Правки:
- 

Проверено: да
---

## ST036 · Almadani 2024 · Medicine

Основной отчёт R0476: [текст](../../fulltext/text/R0476.txt) — «Prevalence of misophonia and its association with depression and obsessive-compulsive disorder among medical students.» — [DOI](https://doi.org/10.1097/md.0000000000040217)
Расхождения в тексте: Text and tables agree on the A-MISO-S counts: 264 + 83 + 21 + 3 + 0 = 371; 107 = 83 + 21 + 3. The Table 4 columns sum to the Table 2 band counts (264/83/21/3). Problems found: (1) The age-of-onset question has n = 152, but 157 reported ever experiencing misophonia. (2) In Table 6, the PHQ-9 cells for psychotropic medication = No read '241 (40) | 104 (60)'. The percentages are wrong: 241/345 = 69.9%. (3) In Table 6, the PHQ-9 and OCD cells for family history appear shifted between rows: the 'No' row PHQ-9 cells sum to 169, which is the 'I do not know' n. These are not misophonia counts. (4) The authors label A-MISO-S 5-24 'clinical misophonia', but by Table 1 this is L1.
Заметка ИИ: Main estimate (authors' choice): A-MISO-S>=5, 107/371 (L1). L2 estimate: A-MISO-S>=10, 24/371, derived from bands. The A-MISO-S language version is not stated, so instrument_validated_in_language = NR and JBI 6 = unclear. n_invited and response rate are NR: the survey was open via social media, and the eligible population was estimated at about 1494.

### ST036-1 · KSU medical students, Riyadh, Saudi Arabia, n=371
Отчёты: R0476 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **107 / 371** | 28.8 | Table 2 | «Clinical misophonia(score, 5–24) / 107 (28.84)» |
| E2 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **24 / 371** | 6.5 | Table 2 | «Moderate misophonia(score, 10–14) / 21 (5.66) Severe misophonia(score, 15–19) / 3 (0.81) Extreme misophonia(score, 20–24) / 0 (0.00)» |
| E3 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **3 / 371** | 0.8 | Table 2 | «Severe misophonia(score, 15–19) / 3 (0.81) Extreme misophonia(score, 20–24) / 0 (0.00)» |
| E4 | all | adhoc · self-reported ever experienced misophonia (yes/no item) | **L1** | **157 / 371** | 42.3 | Table 1 | «Ever experienced misophonia / No / 214 / 57.68 Yes / 157 / 42.32» |
| E5 | female | A-MISO-S · A-MISO-S>=5 | **L1** | **56 / 137** | 40.9 | Table 6 | «Female / 81 (59.1) / 56 (40.9)» |
| E6 | male | A-MISO-S · A-MISO-S>=5 | **L1** | **51 / 234** | 21.8 | Table 6 | «Sex / Male / 183 (78.2) / 51 (21.8)» |
| E7 | likely OCD (OCI-R>=21) | A-MISO-S · A-MISO-S>=5 | **L1** | **54 / 115** | 47.0 | Table 4 | «Likely OCD / 61 (23.1) / 36 (43.4) / 16 (76.2) / 2 (66.7)» |
| E8 | likely OCD (OCI-R>=21) | A-MISO-S · A-MISO-S>=10 | **L2** | **18 / 115** | 15.7 | Table 4 | «Likely OCD / 61 (23.1) / 36 (43.4) / 16 (76.2) / 2 (66.7)» |
| E9 | depression (PHQ-9>=10) | A-MISO-S · A-MISO-S>=5 | **L1** | **55 / 123** | 44.7 | Table 4 | «Moderate / 45 (17) / 24 (28.9) / 9 (42.9) / 2 (66.7) Moderately severe / 15 (5.7) / 7 (8.5) / 7 (33.3) / 0 (0) Severe / 8 (3) / 5 (6) / 0 (0) / 1 (33.3)» |
| E10 | depression (PHQ-9>=10) | A-MISO-S · A-MISO-S>=10 | **L2** | **19 / 123** | 15.4 | Table 4 | «Moderate / 45 (17) / 24 (28.9) / 9 (42.9) / 2 (66.7) Moderately severe / 15 (5.7) / 7 (8.5) / 7 (33.3) / 0 (0) Severe / 8 (3) / 5 (6) / 0 (0) / 1 (33.3)» |
| E11 | self-reported diagnosed mental health condition | A-MISO-S · A-MISO-S>=5 | **L1** | **24 / 58** | 41.4 | Table 6 | «Diagnosed with a mental health condition / No / 230 (73.5) / 83 (26.5) / .022 * / ... Yes / 34 (58.6) / 24 (41.4)» |

- E1: источник порога: developer paper; правило: A-MISO-S row; >=5 = L1 (mild or more); G1; у авторов: «clinical misophonia»; главная у авторов: yes; период: current; заметка: Authors label >=5 'clinical'; by Table 1 this is L1.
- E2: источник порога: developer paper; правило: A-MISO-S row; >=10 L2 recommended; G1 sum of bands; у авторов: «moderate, severe or extreme misophonia»; главная у авторов: no; период: current; **расчёт: 21 (moderate) + 3 (severe) + 0 (extreme) from Table 2**
- E3: источник порога: developer paper; правило: A-MISO-S row; >=15 above L2 cut-off; G1, G2; у авторов: «severe or extreme misophonia»; главная у авторов: no; период: current; **расчёт: 3 (severe) + 0 (extreme) from Table 2**
- E4: источник порога: study's own; правило: adhoc row; self-identified misophonia = L1 (used only if no scale-based L1; here A-MISO-S>=5 exists); у авторов: «had previously experienced misophonia»; главная у авторов: no; период: lifetime; заметка: Item wording and any definition shown are not reported ('ever experienced misophonic-related symptoms'). If the item only asked about any trigger, the reviewer may reclassify as L0.
- E5: источник порога: developer paper; правило: A-MISO-S row; >=5 = L1; у авторов: «clinical misophonia»; главная у авторов: no; период: current
- E6: источник порога: developer paper; правило: A-MISO-S row; >=5 = L1; у авторов: «clinical misophonia»; главная у авторов: no; период: current
- E7: источник порога: developer paper; правило: A-MISO-S row; >=5 = L1; G1 sum of bands; у авторов: «mild, moderate or severe misophonia»; главная у авторов: no; период: current; **расчёт: 36 (mild) + 16 (moderate) + 2 (severe) in the Likely OCD row of Table 4; n = 61 + 54 = 115**; заметка: Subgroup defined by OCI-R screening cut-off, not a diagnosis.
- E8: источник порога: developer paper; правило: A-MISO-S row; >=10 L2; G1 sum of bands; у авторов: «moderate or severe misophonia»; главная у авторов: no; период: current; **расчёт: 16 (moderate) + 2 (severe) in the Likely OCD row of Table 4**; заметка: Subgroup defined by OCI-R screening cut-off; n < 139.
- E9: источник порога: developer paper; правило: A-MISO-S row; >=5 = L1; G1 sum of bands; у авторов: «mild, moderate or severe misophonia»; главная у авторов: no; период: current; **расчёт: Mild misophonia 24+7+5=36; moderate 9+7+0=16; severe 2+0+1=3; total 55. n = 123 (subclinical 45+15+8=68; 68+55=123)**; заметка: Subgroup defined by PHQ-9 screening (>=10), not a diagnosis; n < 139.
- E10: источник порога: developer paper; правило: A-MISO-S row; >=10 L2; G1 sum of bands; у авторов: «moderate or severe misophonia»; главная у авторов: no; период: current; **расчёт: Moderate misophonia 9+7+0=16 + severe 2+0+1=3 = 19, among PHQ-9>=10 rows of Table 4**; заметка: Subgroup defined by PHQ-9 screening; n < 139.
- E11: источник порога: developer paper; правило: A-MISO-S row; >=5 = L1; у авторов: «clinical misophonia»; главная у авторов: no; период: current; заметка: Mixed self-reported diagnoses (depression 40, anxiety 18, OCD 10, etc.).

**Ключевые поля выборки:**
- **n_analysed: 371** — Table 2 — «Clinical misophonia(score, 5–24) | 107 (28.84)»
- **population: medical_students** — 2.1 Study design, setting, and participants — «all medical students, both male and female, enrolled in the first through fifth years at KSU Medical College»
- **sampling: convenience** — 5. Strengths and limitations — «Another limitation is that convenience sampling was used to recruit participants.»

**Остальные поля:**
- clinical_group: NA — NA
- country: SAU — 2.1 Study design, setting, and participants — «all medical students, both male and female, enrolled in the first through fifth years at KSU Medical College in Riyadh, SA»
- setting: university (King Saud University Medical College, Riyadh); online survey distributed via social media — 2.1 Study design, setting, and participants — «The research team distributed the study tool electronically ... between November 19 and December 07, 2023 via social media channels, such as WhatsApp.»
- data_years: 2023 — 2.1 Study design, setting, and participants — «between November 19 and December 07, 2023 via social media channels, such as WhatsApp»
- design: cross-sectional — 2.1 Study design, setting, and participants — «A quantitative cross-sectional study was conducted among the targeted population»
- topic_disclosed: NR — 2.3.1 Ethical consideration — «An explanation of confidentiality and data anonymity was provided to the participants, along with information on the study's scope»
- inclusion_exclusion: Included: KSU medical students years 1-5. Excluded: communication barriers; preparatory or internship year. — 2.1 Study design, setting, and participants — «The exclusion criteria encompassed students with any communication barriers and those who were in the preparatory or internship year at the time of the study.»
- n_invited: NR — 2.1 Study design, setting, and participants — «the number of medical students at KSU Medical College was estimated to be approximately 1494»
- n_responded: 371 — 3. Results — «A total of 371 individuals participated in the study.»
- response_rate: NR — 2.1 Study design, setting, and participants — «the number of medical students at KSU Medical College was estimated to be approximately 1494»
- age_mean: 21.14 — Table 1 — «Age | Mean (SD) | 21.14 (1.59)»
- age_sd: 1.59 — Table 1 — «Age | Mean (SD) | 21.14 (1.59)»
- age_min: NR — NR
- age_max: NR — NR
- age_group: adults — Table 1; 3. Results — «The mean age of the participants was 21.14 years, SD = 1.59 years.»
- pct_female: 36.93 — Table 1 — «Female | 137 | 36.93»
- informant: self — 2.2 Study instruments — «The A-MISO-S is a self-report scale that measures the presence and severity of symptoms»
- mode: online — 2.1 Study design, setting, and participants — «The research team distributed the study tool electronically»
- instruments: A-MISO-S (language version not stated); ad hoc item 'ever experienced misophonic-related symptoms' (research-team questionnaire) — 2.2 Study instruments — «a questionnaire developed by the research team, the Amsterdam Misophonia Scale (A-MISO-S) ... It further assessed if they had ever experienced misophonic-relat…»
- instrument_validated_in_language: NR — 2.2 Study instruments — «Previous studies demonstrated the validity of the scale, with Cronbach's alpha values of 0.838,[19] 0.89,[4] and 0.814.[18]»
- pub_status: journal — Header — «Year: 2024; venue: Medicine; DOI: 10.1097/md.0000000000040217»
- language: English — Full text — «Prevalence of misophonia and its association with depression and obsessive-compulsive disorder among medical students»
- funding_coi: Funded by Deanship of Scientific Research, King Saud University (SABIC Psychological Health Research and Applications Chair). COI not reported in text provided. — Acknowledgments — «The authors extend their appreciation to the Deanship of Scientific Research, King Saud University, for funding through the Vice Deanship of Scientific Researc…»
- notes: The authors call A-MISO-S 5-24 'clinical misophonia' (citing [20]); by Table 1 this is L1. The language version of the A-MISO-S (Arabic or English) is not stated. The eligible population was estimated at about 1494 students (371/1494 ≈ 24.8%, not reported as a response rate). Table 6 has errors in some PHQ-9/OCD cells (see consistency_notes). No overlap with other studies is apparent.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target is KSU medical students (years 1-5), but the survey was spread via social-media channels; how well these channels covered all students is not described. — 2.1 Study design, setting, and participants — «distributed the study tool electronically ... via social media channels, such as WhatsApp»
2. способ отбора: **no** — Convenience sampling, as the authors state. — 5. Strengths and limitations — «convenience sampling was used to recruit participants»
3. размер выборки: **no** — n = 371 < 385. — 3. Results — «A total of 371 individuals participated in the study.»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are all reported. — 2.1; Table 1 — «KSU Medical College in Riyadh, SA ... between November 19 and December 07, 2023; Age | Mean (SD) | 21.14 (1.59); Female | 137 | 36.93»
5. охват (пропуски): **yes** — A-MISO-S categories cover all 371 participants (264 + 107 = 371), so no misophonia data are missing among respondents. — Table 2 — «Subclinical misophonia(score, 0–4) | 264 (71.16) ... Clinical misophonia(score, 5–24) | 107 (28.84)»
6. валидность определения случая: **unclear** — Rated on L2 A-MISO-S>=10 (anchored cut-off). The language version used (English or Arabic) is not stated, so validation in that language cannot be checked. The authors' primary definition (>=5) is an unanchored band cut… — 2.2; 2.3 — «The cutoff points used for the 3 scales were as follows: a score of ≥ 10 for the PHQ-9,[25] ≥ 5 for the A-MISO-S,[20] and ≥ 21 for the OCI-R.»
7. единое надёжное измерение: **yes** — Everyone completed the same online self-report A-MISO-S with the same threshold; Cronbach's alpha is cited from source studies. — 2.2 Study instruments — «Previous studies demonstrated the validity of the scale, with Cronbach's alpha values of 0.838,[19] 0.89,[4] and 0.814.[18]»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator (371) are clear for each band, so a CI can be calculated. — Table 2 — «Out of 371 students, 107 (28.84%) had clinical misophonia.»
9. отклик: **no** — Open survey via social media with no count of people invited. 371 of about 1494 eligible students (~25%) took part, and non-response was not handled. — 2.1 Study design, setting, and participants — «the number of medical students at KSU Medical College was estimated to be approximately 1494»

Правки:
- 

Проверено: да
---

## ST037 · Ay 2024 · Frontiers in psychology

Основной отчёт R0484: [текст](../../fulltext/text/R0484.txt) — «The mediating role of anxiety in the relationship between misophonia and quality of life: findings from the validated Turkish version of MisoQuest.» — [DOI](https://doi.org/10.3389/fpsyg.2024.1361645)
Расхождения в тексте: The abstract and Table 1 agree on n = 548 (mean age 28.06 ± 9.36) and n = 117 (mean age 25.50 ± 6.31). The only prevalence figure, 2% with MisoQuest >=61, is in the Discussion and covers the two samples combined, N = 665 = 548 + 117. Cases were derived as 13 from the rounded 2% (the true value could be about 10-16). Table 1 percentages for female sex are rounded (437/548 = 79.7%; 100/117 = 85.5%).
Заметка ИИ: Two separately recruited online samples were extracted. The combined prevalence estimate (L2, MisoQuest >=61) is attached to sample 1 and flagged as pooled over both samples. A reviewer should decide whether to treat it as one combined-sample estimate. The authors may hold per-sample counts (open data on figshare: 10.6084/m9.figshare.24903288.v2).

### ST037-1 · Turkish MisoQuest validation sample, online via social media, Turkey, n=548
Отчёты: R0484 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all (samples 1 and 2 combined, N = 665) | MisoQuest · MisoQuest>=61 | **L2** | **13 / 665** | 2.0 | Discussion, paragraph 3 | «In our study, misophonia was detected in 2% of the total sample (N = 665) according to this cut-off value.» |

- E1: источник порога: developer paper; правило: MisoQuest row; L2 >=61; у авторов: «misophonia was detected»; главная у авторов: no; период: NR; **расчёт: 2% x 665 = 13.3 -> 13 (the rounded 2% is consistent with about 10-16 cases)**; заметка: The estimate pools two separately recruited samples (548 validation + 117 anxiety/QoL sample); no per-sample counts are reported. 'This cut-off value' refers to MisoQuest >=61 (Siepsiak et al. 2020b). The authors give it only in the Discussion and do not call it a main estimate.

**Ключевые поля выборки:**
- **n_analysed: 548** — Methods, Participants; Table 1 — «For the Turkish adaptation of MisoQuest, 548 participants aged 18–63 were included in the study.»
- **population: gp_other** — Limitations — «the target sample of this study was individuals from the normal population»
- **sampling: convenience** — Methods, Participants; Limitations — «The questionnaire was delivered to the participants online via social media applications.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: TUR — Introduction (last paragraph); Ethics statement — «the present study aims to evaluate the psychometric properties of MisoQuest in the Turkish population»
- setting: online (social media), community volunteers — Methods, Participants — «The questionnaire was delivered to the participants online via social media applications.»
- data_years: NR — Methods — «NR»
- design: validation study — Methods, Participants — «For the Turkish adaptation of MisoQuest, 548 participants aged 18–63 were included in the study.»
- topic_disclosed: NR — Methods — «NR»
- inclusion_exclusion: Aged 18-63; excluded self-reported psychiatric diagnoses and hearing problems — Methods, Participants — «Participants with self-reported psychiatric diagnoses and hearing problems were excluded.»
- n_invited: NR — Methods — «NR»
- n_responded: NR — Methods — «NR»
- response_rate: NR — Methods — «NR»
- age_mean: 28.06 — Table 1 — «M = 28.06, SD = 9.36Range = 18–63»
- age_sd: 9.36 — Table 1 — «M = 28.06, SD = 9.36Range = 18–63»
- age_min: 18 — Table 1 — «Range = 18–63»
- age_max: 63 — Table 1 — «Range = 18–63»
- age_group: adults — Methods, Participants — «548 participants aged 18–63»
- pct_female: 79.7 — Table 1 — «Female | 437 (80)»
- informant: self — Limitations — «using the online self-report method in data collection may cause recruitment bias»
- mode: online — Methods, Participants — «The questionnaire was delivered to the participants online via social media applications.»
- instruments: MisoQuest (Turkish version, translated from Polish in this study) — Methods, Procedure — «MisoQuest, originally written in Polish, was translated from Polish to Turkish by a native Turkish translator who speaks Polish fluently.»
- instrument_validated_in_language: yes — Conclusion — «the validity and reliability of the MisoQuest in Turkish was evaluated, and it was shown that the Turkish version of the questionnaire has good psychometric pr…»
- pub_status: journal — Header — «Year: 2024; venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2024.1361645»
- language: English — Full text — «The mediating role of anxiety in the relationship between misophonia and quality of life: findings from the validated Turkish version of MisoQuest»
- funding_coi: No funding; no conflicts of interest declared — Funding Statement; Conflict of interest — «The author(s) declare that no financial support was received for the research, authorship, and/or publication of this article.»
- notes: pct_female computed 437/548 = 79.7% (table prints 80). The only prevalence figure (2% with MisoQuest >=61) is reported for the two samples combined (N = 665 = 548 + 117), not per sample; it is recorded here only, to avoid double counting. The Turkish validation is in this same report: CFA found a 3-factor structure (the original has 1 factor), and the >=61 cut-off was not re-anchored in Turkish. Data collection dates not reported.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is the Turkish/normal population, but the frame was social-media users only — Methods, Participants — «The questionnaire was delivered to the participants online via social media applications.»
2. способ отбора: **no** — Online volunteer opt-in convenience sampling — Limitations — «using the online self-report method in data collection may cause recruitment bias»
3. размер выборки: **yes** — n = 548 (combined estimate N = 665), both >= 385 — Methods, Participants — «548 participants aged 18–63 were included in the study»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; data collection dates missing — Table 1; Methods — «M = 28.06, SD = 9.36Range = 18–63 ... Female | 437 (80)»
5. охват (пропуски): **unclear** — Missing data and the number of incomplete responses are not reported — Methods — «548 participants aged 18–63 were included in the study»
6. валидность определения случая: **yes** — MisoQuest >=61, in a Turkish version validated in this report; caveat: different factor structure, and the cut-off was not re-anchored in Turkish — Discussion — «misophonia was detected in 2% of the total sample (N = 665) according to this cut-off value»
7. единое надёжное измерение: **yes** — Same online self-report instrument for everyone; Cronbach's alpha 0.90 in this sample — Results, Reliability analysis — «The Cronbach's alpha value for the entire questionnaire is 0.90.»
8. статистика (числитель и знаменатель): **no** — Only a rounded percentage (2%) for the combined samples is given; no numerator, no per-sample figure, no CI — Discussion — «misophonia was detected in 2% of the total sample (N = 665)»
9. отклик: **no** — Open online survey with no denominator of invited people — Methods, Participants — «The questionnaire was delivered to the participants online via social media applications.»

Правки:
- 

Проверено: да
### ST037-2 · Turkish anxiety/quality-of-life sample, online, Turkey, n=117
Отчёты: R0484 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |


**Ключевые поля выборки:**
- **n_analysed: 117** — Methods, Participants; Table 1 — «the study continued with 117 people»
- **population: gp_other** — Limitations — «the target sample of this study was individuals from the normal population»
- **sampling: convenience** — Methods, Participants; Limitations — «using the online self-report method in data collection may cause recruitment bias»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: TUR — Introduction (last paragraph) — «the present study aims to evaluate the psychometric properties of MisoQuest in the Turkish population»
- setting: online, community volunteers — Methods, Participants — «The MisoQuest, State–Trait Anxiety Inventory (STAI) and 36-item Short-Form Health Survey (SF-36) scales were delivered online to the participants at this stage.»
- data_years: NR — Methods — «NR»
- design: cross-sectional — Methods, Participants — «data were collected from a different sample of 122 participants to evaluate the relationship between misophonia and state–trait anxiety and quality of life»
- topic_disclosed: NR — Methods — «NR»
- inclusion_exclusion: Adults 18-46; 5 excluded for self-reported anxiety disorder (3) or panic disorder (2) — Methods, Participants — «three people were excluded because they stated that they were diagnosed with anxiety disorder and two people were diagnosed with panic disorder, and the study …»
- n_invited: NR — Methods — «NR»
- n_responded: 122 — Methods, Participants — «Of the 122 people who participated in the study»
- response_rate: NR — Methods — «NR»
- age_mean: 25.50 — Table 1 — «M = 25.50, SD = 6.31Range = 18–46»
- age_sd: 6.31 — Table 1 — «M = 25.50, SD = 6.31Range = 18–46»
- age_min: 18 — Table 1 — «Range = 18–46»
- age_max: 46 — Table 1 — «Range = 18–46»
- age_group: adults — Table 1 — «Range = 18–46»
- pct_female: 85.5 — Table 1 — «Female | 437 (80) | 100 (86)»
- informant: self — Limitations — «using the online self-report method in data collection»
- mode: online — Methods, Participants — «were delivered online to the participants at this stage»
- instruments: MisoQuest (Turkish version) — Methods, Participants — «The MisoQuest, State–Trait Anxiety Inventory (STAI) and 36-item Short-Form Health Survey (SF-36) scales were delivered online»
- instrument_validated_in_language: yes — Conclusion — «the Turkish version of the questionnaire has good psychometric properties»
- pub_status: journal — Header — «Year: 2024; venue: Frontiers in psychology»
- language: English — Full text — «The mediating role of anxiety in the relationship between misophonia and quality of life»
- funding_coi: No funding; no conflicts of interest declared — Funding Statement; Conflict of interest — «no financial support was received for the research»
- notes: Recruited separately from the 548-person validation sample ('a different sample'). No prevalence is reported for this sample alone; it contributes 117 people to the combined 2% (N = 665) estimate, which is recorded under the validation sample. No estimate is extracted here to avoid double counting. pct_female computed 100/117 = 85.5% (table prints 86).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is the Turkish normal population; the frame was online respondents only — Methods, Participants — «scales were delivered online to the participants at this stage»
2. способ отбора: **no** — Online volunteer convenience sampling — Limitations — «using the online self-report method in data collection may cause recruitment bias»
3. размер выборки: **no** — n = 117 < 385 — Methods, Participants — «the study continued with 117 people»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates missing — Table 1 — «M = 25.50, SD = 6.31Range = 18–46 ... 100 (86)»
5. охват (пропуски): **unclear** — Exclusions by diagnosis are reported, but missing misophonia data are not — Methods, Participants — «Of the 122 people who participated in the study, three people were excluded»
6. валидность определения случая: **yes** — MisoQuest >=61 (the combined estimate), Turkish version validated in this report; cut-off not re-anchored in Turkish — Discussion — «misophonia was detected in 2% of the total sample (N = 665) according to this cut-off value»
7. единое надёжное измерение: **yes** — Same online instrument for everyone; reliability reported in the validation sample and the source study — Results, Reliability analysis; Measurement tools — «The Cronbach's alpha value for the entire questionnaire is 0.90.»
8. статистика (числитель и знаменатель): **no** — No per-sample prevalence; the combined percentage has no numerator — Discussion — «misophonia was detected in 2% of the total sample (N = 665)»
9. отклик: **no** — Open online survey with no denominator of invited people — Methods, Participants — «scales were delivered online to the participants at this stage»

Правки:
- 

Проверено: да
---

## ST038 · Babalola 2024 · PsyArXiv

Основной отчёт R0485: [текст](../../fulltext/text/R0485.txt) · [PDF](../../fulltext/pdf/R0485.pdf) — «Misophonia is associated with heightened emotion evocation by music» — [DOI](https://doi.org/10.31234/osf.io/jzydf)
Расхождения в тексте: The high-group threshold is described as 'above 10' but labelled 'Moderate misophonia symptoms' (Schröder band 10-14), so it is ambiguous whether >=10 or >10 was used. The low-group threshold 'under 4' is labelled 'Subclinical' (band 0-4). Demographics (Table 1) cover only the 98 main-study participants. The A-MISO-S alpha is reported with r(96), which suggests it was computed in the 98 main-study participants rather than all 300 screened.
Заметка ИИ: This is a quasi-experimental MTurk study with a 300-person A-MISO-S pre-screen. It reports no prevalence: the screening score distribution and the number passing quality checks are not given. One A-MISO-S estimate is listed with cases and n as NR. The raw data on OSF might allow the counts to be recovered.

### ST038-1 · MTurk/CloudResearch online screening sample, country NR, n=300
Отчёты: R0485 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S >10 (text says 'above 10', labelled 'Moderate') | **L2** | **NR / NR** |  | Method, Participants, p. 7; Participant Inclusion, p. 15 | «From this initial screening, 111 participants (low misophonia: n = 67; high misophonia: n = 44) were invited to complete the main study» |

- E1: источник порога: developer paper; правило: A-MISO-S row; G2 (>=10 or >10 both at/above L2 cut-off); у авторов: «high misophonia (Moderate misophonia symptoms)»; главная у авторов: no; период: NR; заметка: Not a prevalence estimate. 44 people were invited to the high group from those who passed the quality checks (number unknown) and possibly after demographic matching. So 44/300 (14.7%) is at most a lower bound, and the true count of screened people above threshold is not reported.

**Ключевые поля выборки:**
- **n_analysed: NR** — Participant Inclusion, pp. 14-15 — «There were five primary considerations for participants who completed the initial screening to be invited to participate in the main study.»
- **population: gp_other** — Method, Participants, p. 8 — «All participants were recruited from Amazon Mechanical Turk via CloudResearch»
- **sampling: convenience** — Method, Participants, p. 8 — «All participants were recruited from Amazon Mechanical Turk via CloudResearch (Litman, 2017)»

**Остальные поля:**
- clinical_group: NA — NA
- country: NR — Method, Participants, p. 8 — «All participants were recruited from Amazon Mechanical Turk via CloudResearch (Litman, 2017)»
- setting: online panel (Amazon Mechanical Turk via CloudResearch) — Method, Participants, p. 8 — «All participants were recruited from Amazon Mechanical Turk via CloudResearch (Litman, 2017), with all participants successfully passing internally administere…»
- data_years: NR — Procedure, p. 14 — «Eligible participants had 30 days to complete the main study from its launch, which occurred 4 days after the initial screening.»
- design: screening phase of experiment — Method, Participants, p. 7 — «We recruited 300 participants for the initial misophonia screening. Participant eligibility for the main study was determined based on responses to the Amsterd…»
- topic_disclosed: NR — Materials, Screening, p. 8 — «Prior to completing the A-MISO-S, participants were provided with a definition of misophonia and were asked (1) whether they experience misophonia»
- inclusion_exclusion: MTurk workers passing CloudResearch attention checks; for main-study invitation: passed 2 attention checks, completion time >=2 min, no skipped items, acceptable A-MISO-S free response; low group A-MISO-S <4, high group >10 — Participant Inclusion, pp. 14-15 — «To be invited to the low misophonia group, participants had to score under 4 (defined as Subclinical misophonia symptoms). To be invited to the high misophonia…»
- n_invited: NR — Method, Participants, p. 7 — «We recruited 300 participants for the initial misophonia screening.»
- n_responded: 300 — Method, Participants, p. 7 — «We recruited 300 participants for the initial misophonia screening.»
- response_rate: NR — NA
- age_mean: NR — Table 1, p. 32 — «Age (Years) 37.31 (9.08) 37.25 (9.75)»
- age_sd: NR — Table 1, p. 32 — «Age (Years) 37.31 (9.08) 37.25 (9.75)»
- age_min: NR — NA
- age_max: NR — NA
- age_group: adults — Table 1, p. 32 — «Age (Years) 37.31 (9.08) 37.25 (9.75)»
- pct_female: NR — Table 1, p. 32 — «Women 43% 45%»
- informant: self — Materials, Screening, p. 8 — «Self-reported misophonia was assessed via the A-MISO-S (Schröder et al., 2013).»
- mode: online — Materials, Screening, p. 9 — «The screening assessment was administered in Qualtrics (Provo, UT).»
- instruments: A-MISO-S (English, 6 Likert items + free response); single self-report item on experiencing misophonia (1-5, after definition shown) — Materials, Screening, p. 8 — «asked (1) whether they experience misophonia on a scale from 1 (Definitely no) to 5 (Definitely yes) and (2) whether they had heard of misophonia prior to part…»
- instrument_validated_in_language: NR — Materials, Screening, p. 8 — «In the present study, the six Likert-type questions of the A-MISO-S displayed excellent reliability, α = .94»
- pub_status: preprint — Header (venue) — «venue: PsyArXiv; DOI: 10.31234/osf.io/jzydf»
- language: English — Full text — «Misophonia is associated with heightened emotion evocation by music»
- funding_coi: Centre for Undergraduate Research Learning Fellowship, Huron University (to OB); authors report no conflict of interest — Acknowledgements; Disclosure of Interest, p. 23 — «This research was supported by a Centre for Undergraduate Research Learning Fellowship, awarded by Huron University to OB. ... The authors report no conflict o…»
- notes: Quasi-experimental study; the 300-person screen was used only to form low/high groups. Country is not stated (MTurk). Age and sex are reported only for the 98 main-study completers: mean age 37.31 (low group) and 37.25 (high group); women 43% and 45%. The number passing the quality checks is not reported. Raw data reportedly on OSF (10.17605/OSF.IO/X2UDK); not checked. The single self-identification item (1-5) has no reported distribution.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is MTurk/CloudResearch workers, which covers only part of any general population; target population not defined. — Method, Participants, p. 8 — «All participants were recruited from Amazon Mechanical Turk via CloudResearch»
2. способ отбора: **no** — Opt-in non-probability online panel. — Method, Participants, p. 8 — «All participants were recruited from Amazon Mechanical Turk via CloudResearch»
3. размер выборки: **no** — n = 300 screened, below 385. — Method, Participants, p. 7 — «We recruited 300 participants for the initial misophonia screening.»
4. описание выборки и условий: **no** — Age and sex are reported only for the 98 people in the main study, not for the screened sample; country and dates are not reported. — Table 1, p. 32; Method, p. 8 — «Comparison of low and high misophonia groups on misophonia screening questionnaire (A-MISO-S) and demographic variables»
5. охват (пропуски): **unclear** — Participants were excluded for attention checks, speed, skipped items and suspicious free responses, but the number excluded is not reported. — Participant Inclusion, p. 14 — «participants could not have skipped questions, as this either invalidated the calculation of their misophonia score»
6. валидность определения случая: **unclear** — A-MISO-S 'above 10' (strictly >10, i.e. stricter than the anchored >=10) is labelled 'Moderate' (>=10), so the threshold is ambiguous. Published validation of the English version is not cited. — Participant Inclusion, p. 15 — «To be invited to the high misophonia group, participants had to score above 10 (defined as Moderate misophonia symptoms).»
7. единое надёжное измерение: **yes** — Everyone took the same online A-MISO-S; internal consistency is reported (alpha .94), but apparently in the 98 main-study participants. — Materials, Screening, p. 8 — «the six Likert-type questions of the A-MISO-S displayed excellent reliability, α = .94»
8. статистика (числитель и знаменатель): **no** — No prevalence is reported; the number of screened participants at or above the threshold and the denominator after exclusions are not given. — Method, Participants, p. 7 — «111 participants (low misophonia: n = 67; high misophonia: n = 44) were invited to complete the main study»
9. отклик: **no** — Open MTurk recruitment with no denominator of people invited; non-response not handled. — Method, Participants, p. 7 — «We recruited 300 participants for the initial misophonia screening.»

Правки:
- 

Проверено: да
---

## ST039 · Brueijs 2024 · Center for Open Science

Основной отчёт R0506: [текст](../../fulltext/text/R0506.txt) · [PDF](../../fulltext/pdf/R0506.pdf) — «Decreased sound tolerance as a transdiagnostic feature of neurodiversity with loudness hyperacusis as a central player: A psychometric Bayesian analysis» — [DOI](https://doi.org/10.31219/osf.io/t6y2w)
Расхождения в тексте: Table 3 does not print subgroup denominators. Back-calculating gives n ≈ 170 with hyperacusis: 87/0.512, 24/0.141 and 62/0.365 are all consistent with 170. That leaves 242 without hyperacusis (412 − 170). Two printed percentages do not fit these denominators. First, moderate phonophobia: 91/170 = 53.5%, but 53.3% is printed. Second, no-hyperacusis misophonia: 11/242 = 4.5%, but 4.6% is printed. The other no-hyperacusis percentages fit 242: 9/242 = 3.7% and 6/242 = 2.5%. The authors do not report a whole-sample misophonia prevalence; 98/412 (23.8%) is derived. The abstract says 26% autistic and 24% ADHD, while the methods say the sample was 'about 40%' enriched for autism or ADHD. The counts (64 + 57 + 43 = 164/412 = 39.8%) agree with 40%.
Заметка ИИ: Extracted as one sample. The autism/ADHD-filtered recruitment streams cannot be separated in the report. The reviewer should decide whether this enriched panel counts as gp_other or should be treated as partly clinical. The estimates by hyperacusis status are extracted as subgroups found within the sample, defined by the IHS questionnaire. The combined 'misophonia and moderate phonophobia' row is not extracted because it is not a misophonia-only case definition.

### ST039-1 · Prolific online adults enriched for autism/ADHD, country NR, n=412
Отчёты: R0506 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DMQ · DMQ Composite Symptom Severity total >=41.4 | **L2** | **98 / 412** | 23.8 | Table 3; Page 6 | «Misophonia 87 (51.2%) 11 (4.6%) ... Clinical misophonia defined as DMQ Composite Symptoms score ≥ 41.4.» |
| E2 | IHS hyperacusis (IHS total >=56) | DMQ · DMQ Composite Symptom Severity total >=41.4 | **L2** | **87 / 170** | 51.2 | Table 3 | «Misophonia 87 (51.2%) 11 (4.6%)» |
| E3 | no IHS hyperacusis (IHS total <56) | DMQ · DMQ Composite Symptom Severity total >=41.4 | **L2** | **11 / 242** | 4.5 | Table 3 | «Misophonia 87 (51.2%) 11 (4.6%)» |

- E1: источник порога: developer paper; правило: DMQ row; Symptom Severity total >=41.4 (L2); G10 screen-negatives coded 0; у авторов: «clinical misophonia»; главная у авторов: no; период: NR; **расчёт: 87 (hyperacusis yes) + 11 (hyperacusis no) from Table 3 = 98; n = final sample of 412**; заметка: The authors do not report a whole-sample prevalence (98/412 = 23.8%). The denominator assumes all 412 had DMQ and IHS data (EFA N = 412). The sample is enriched for autism/ADHD.
- E2: источник порога: developer paper; правило: DMQ row; Symptom Severity total >=41.4 (L2); у авторов: «clinical misophonia»; главная у авторов: no; период: NR; **расчёт: n back-calculated: 87/0.512 = 169.9 -> 170 (consistent with 24/0.141 and 62/0.365)**; заметка: Subgroup defined by a questionnaire score (IHS >=56), not by a diagnosis; denominator not printed.
- E3: источник порога: developer paper; правило: DMQ row; Symptom Severity total >=41.4 (L2); у авторов: «clinical misophonia»; главная у авторов: no; период: NR; **расчёт: n = 412 - 170 = 242; 11/242 = 4.5% vs printed 4.6% (11/240 = 4.6%)**; заметка: The denominator is uncertain (240-242); the printed 4.6% does not exactly match 11/242.

**Ключевые поля выборки:**
- **n_analysed: 412** — Page 6, Participants — «The final sample included 412 participants.»
- **population: gp_other** — Page 6, Participants — «The sample was transdiagnostic but enriched in individuals diagnosed with autism or ADHD (about 40% of total sample)»
- **sampling: convenience** — Page 6, Participants — «enriched in individuals diagnosed with autism or ADHD (about 40% of total sample) by running parallel identical recruitment advertisements additionally filtered on these diagnoses.»

**Остальные поля:**
- clinical_group: NA — Page 6, Participants — «Of these, 64 had an autism diagnosis without ADHD, 57 had ADHD without autism, and 43 had a dual diagnosis.»
- country: NR — Page 6, Procedure — «country of origin, country of residence, and whether they had children.»
- setting: online panel (Prolific.co; study hosted on Gorilla.sc) — Page 5, Participants; Page 6, Procedure — «Adult participants with and without neurodevelopmental diagnoses were recruited via Prolific.co.»
- data_years: NR — Methods — «NR»
- design: cross-sectional — Page 22, Limitations — «The cross-sectional design precludes causal inference.»
- topic_disclosed: NR — Page 6, Procedure — «Prospective participants clicked on the advertisement on Prolific and were directed to an informed consent page preceding the study.»
- inclusion_exclusion: Inclusion: 18+, fluent English, Prolific approval rate 100%, >=10 prior submissions, willing to report diagnoses. Exclusion: hearing impairment, neurodegenerative/neurological disease, head trauma with loss of consciousness, schizophrenia/psychosis, genetic syndromes, failed attention check. — Page 5-6, Participants — «Inclusion criteria were 18+ years old, fluent English, good track record on Prolific ... Exclusion criteria were known hearing impairment, neurodegenerative or…»
- n_invited: NR — Page 6, Participants — «NR»
- n_responded: 440 — Page 6, Participants — «Out of 440 participants completing the study, two participants were excluded»
- response_rate: NR — Page 6, Participants — «NR»
- age_mean: NR — Page 13, Results; Table 1 — «median age of 28 years (IQR = 12.0, range 18–68)»
- age_sd: NR — Page 13, Results — «median age of 28 years (IQR = 12.0, range 18–68)»
- age_min: 18 — Page 13, Results — «median age of 28 years (IQR = 12.0, range 18–68)»
- age_max: 68 — Page 13, Results — «median age of 28 years (IQR = 12.0, range 18–68)»
- age_group: adults — Page 2, Abstract — «Adults 18–68 years old (n = 412)»
- pct_female: 54.1 — Table 1 — «Female sex assigned at birth 54.1%»
- informant: self — Page 2, Abstract — «self-reported symptoms of loudness hyperacusis, misophonia, and phonophobia»
- mode: online — Page 2, Abstract — «We administered web-based questionnaires»
- instruments: Duke Misophonia Questionnaire (DMQ) trigger checklist + Composite Symptom Severity subscale, English (response options to the 'no specific sounds' item changed to True/False for me) — Page 9-10, Misophonia symptoms — «The Symptoms subscales of the Duke Misophonia Questionnaire (DMQ) (Rosenthal et al., 2021) was used to quantify misophonia symptom severity.»
- instrument_validated_in_language: yes — Page 10, Misophonia symptoms — «which discriminated between subclinical and clinical levels of misophonia with a specificity of 91% and sensitivity of 100% in the original study (Rosenthal et…»
- pub_status: preprint — Page 1, header — «PREPRINT»
- language: English — Full text — «Decreased sound tolerance as a transdiagnostic feature of neurodiversity with loudness hyperacusis as a central player»
- funding_coi: NR (the preprint has no funding or competing-interest statement; ethics details were removed for blind review) — Page 5, Methods — «<ethics details temporarily removed due to double-blind peer review>»
- notes: The sample was deliberately enriched for autism/ADHD through parallel diagnosis-filtered Prolific ads (26% autism, 24.3% ADHD). The recruitment streams cannot be separated in the report, so the sample is extracted as one. Prevalence is likely higher than in the general population. The authors give no whole-sample misophonia prevalence, only Table 3 split by IHS hyperacusis status; the whole-sample count is derived (87 + 11). DMQ skip logic: participants who endorsed 'no specific sounds bother me' were coded 0 and count as non-cases (G10). Preprint on OSF, 2024; check for a later journal versi…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is Prolific users with diagnosis-filtered enrichment; it does not cover adults in general. — Page 5-6, Participants — «Adult participants with and without neurodevelopmental diagnoses were recruited via Prolific.co.»
2. способ отбора: **no** — Volunteer opt-in online panel, with targeted enrichment for autism/ADHD. — Page 6, Participants — «by running parallel identical recruitment advertisements additionally filtered on these diagnoses.»
3. размер выборки: **yes** — n = 412, which is >= 385. — Page 6, Participants — «The final sample included 412 participants.»
4. описание выборки и условий: **no** — Age, sex and setting are reported, but country and data-collection dates are not. — Page 13, Table 1 — «The sample was sex-balanced with a median age of 28 years (IQR = 12.0, range 18–68).»
5. охват (пропуски): **unclear** — Missing DMQ data are not explicitly reported. The EFA uses N=412, which suggests complete data, but Table 3 does not state its denominators. — Supplementary Table 5 — «Exploratory factor analysis of the 23 DMQ Symptoms items (N = 412).»
6. валидность определения случая: **yes** — DMQ Symptom Severity total >=41.4 (anchored cut-off from Rosenthal 2021), original English version. One screening item's response options were slightly modified. — Page 10, Misophonia symptoms — «We used a total score of ≥ 41.4 on the Composite Symptoms scale as a cut-off for clinical levels of misophonia»
7. единое надёжное измерение: **yes** — Same online instrument and threshold for everyone; Cronbach's alpha reported in this sample. — Page 10, Misophonia symptoms — «The Cronbach’s α was 0.968 (0.963–0.972).»
8. статистика (числитель и знаменатель): **unclear** — Counts and percentages are given only by hyperacusis subgroup. Denominators are not printed, some percentages are inconsistent, and no whole-sample prevalence is reported. — Table 3 — «Misophonia 87 (51.2%) 11 (4.6%)»
9. отклик: **no** — Open Prolific recruitment: no denominator of invited people and no handling of non-response. — Page 6, Participants — «Out of 440 participants completing the study»

Правки:
- 

Проверено: да
---

## ST040 · Dewan 2024 · Schizophrenia research

Основной отчёт R0524: [текст](../../fulltext/text/R0524.txt) · [PDF](../../fulltext/pdf/R0524.pdf) — «Aberrant salience signaling in auditory processing in schizophrenia: Evidence for abnormalities in both sensory processing and emotional reactivity.» — [DOI](https://doi.org/10.1016/j.schres.2024.09.026)
Расхождения в тексте: Text and tables agree on group sizes (SZ 30, HV 28; t-tests df 56). pct_female was computed from Table 1: SZ 11/30 = 36.7%; HV 11/28 = 39.3%. Authors say 'very few participants exhibited true misophonia' and mention 'low rates of misophonia in the two participant groups', but give no definition and no count. So no estimate could be extracted for that statement. The MQ Severity Scale is called SRSS here and is reported only as means.
Заметка ИИ: Case-control MRI study of 30 schizophrenia outpatients and 28 matched healthy volunteers. Only MQ means are reported, plus one count from an item-level rule (at least one Emotions-and-Behaviors item rated 'always': 4/30 SZ, 0/28 HV). That rule is extracted at level NR and should not be pooled. Mode of administration, recruitment, dates and age range are not reported.

### ST040-1 · Schizophrenia/schizoaffective outpatients, Maryland, USA, n=30
Отчёты: R0524 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · >=1 MQ Emotions-and-Behaviors item rated 4 ('always') | **NR** | **4 / 30** | 13.3 | Pages 5-6, Results, Misophonia Questionnaire | «four participants with SZ gave at least one item from the MQ Emotional Behavior section a rating of 4, meaning that they "always" engage in the respective avoidant/emotional behavior in response to a misophonia trigger …» |

- E1: источник порога: study's own; правило: MQ row; G3/G2 cannot place a single-item rule on the scale metric; G6 not determinable; у авторов: «"always" engage in the respective avoidant/emotional behavior in response to a …»; главная у авторов: no; период: NR; заметка: Authors don't present this as a misophonia case definition. A single E&B item at 4 gives a scale mean of only about 0.57, below any MQ cut-off. A reviewer might instead consider L1 under the ad hoc frequency rule. MSS-based counts (e.g. MSS>=7) were not reported; only mean SRSS 4.741 (SD 3.717).

**Ключевые поля выборки:**
- **n_analysed: 30** — Table 1; Page 5, Results — «SZ (N=30)»
- **population: clinical** — Page 4, Methods, Participants — «Thirty people with a diagnosis of schizophrenia or schizoaffective disorder (collectively termed SZ)»
- **sampling: NR** — Page 4, Methods, Participants — «Thirty people with a diagnosis of schizophrenia or schizoaffective disorder (collectively termed SZ) ... provided written informed consent»

**Остальные поля:**
- clinical_group: psychosis (schizophrenia or schizoaffective disorder) — Page 4, Methods, Participants — «Diagnosis of schizophrenia or schizoaffective disorder in participants was confirmed using the Structured Clinical Interview for DSM-IV-R Disorders»
- country: USA — Page 4, Methods, Participants — «protocols approved by the Institutional Review Board of the University of Maryland School of Medicine (Protocol HP-00051996), with a reliance by the Maryland D…»
- setting: clinic (chronic psychiatric outpatients; University of Maryland / Maryland Psychiatric Research Center) — Page 4, Methods, Participants — «All SZ participants were chronic outpatients on stable antipsychotic medication regimens (no changes for four weeks).»
- data_years: NR — NA
- design: other — Page 4, Methods, Participants — «Thirty people with a diagnosis of schizophrenia or schizoaffective disorder (collectively termed SZ) and 28 demographically-matched healthy volunteers (HV) ...…»
- topic_disclosed: NR — NA
- inclusion_exclusion: SCID-confirmed schizophrenia/schizoaffective disorder; chronic outpatients on antipsychotics unchanged for 4 weeks; excluded pregnancy and past substance dependence; completed MRI behavioural task — Page 4, Methods, Participants — «Additional exclusionary criteria included: pregnancy and admission of past substance dependence.»
- n_invited: NR — NA
- n_responded: NR — NA
- response_rate: NR — NA
- age_mean: 43.98 — Table 1 — «Age (Years) 43.98 (12.26)»
- age_sd: 12.26 — Table 1 — «Age (Years) 43.98 (12.26)»
- age_min: NR — NA
- age_max: NR — NA
- age_group: NR — Table 1 — «Age (Years) 43.98 (12.26)»
- pct_female: 36.7 — Table 1 — «Sex at Birth 11 F, 19 M»
- informant: self — Page 4, Assessment: Self-report measures — «we had participants complete the MQ (Wu, et al., 2014)»
- mode: NR — Page 4, Assessment: Self-report measures — «we had participants complete the MQ (Wu, et al., 2014), based on our familiarity with this instrument.»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), English (Symptom Scale, Emotions-and-Behaviors Scale, Severity Scale reported as SRSS 0-15) — Pages 4-5, Assessment: Self-report measures — «The MQ has two sections, labeled "misophonia symptoms" and "misophonia emotional behavior". ... The third section of the MQ, labeled "self-reported sound sensi…»
- instrument_validated_in_language: yes — Page 4; Page 12 references — «Wu MS, Lewin AB, Murphy TK, & Storch EA (2014). Misophonia: Incidence, Phenomenology, and Clinical Correlates in an Undergraduate Student Sample.»
- pub_status: journal — Page 1, header — «Published in final edited form as: Schizophr Res. 2024 December ; 274: 329–336.»
- language: English — Full text — «Aberrant Salience Signaling in Auditory Processing in Schizophrenia»
- funding_coi: University of Maryland MPower funds, PRISM award, NIH 1R01MH115031; DLK consults for Alkermes, Karuna, Janssen; no financial COI declared — Page 10, Role of the Funding Source; Page 1, Declaration of… — «This study was partially funded MPower funds from the University of Maryland ... JAW's participation was supported by NIH grant 1R01MH115031.»
- notes: Separately recruited from the HV sample in the same report. Case-control MRI study, not a prevalence study. The age range is not reported, so age_group is NR, although the mean age is 44. pct_female = 11/30. The authors' claim of 'low rates of misophonia' has no definition or count.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Recruitment frame for outpatients not described — Page 4, Methods, Participants — «All SZ participants were chronic outpatients on stable antipsychotic medication regimens»
2. способ отбора: **unclear** — Sampling method not described (likely volunteers for an MRI study) — Page 4, Methods, Participants — «provided written informed consent ... and successfully completed a behavioral task in the MRI scanner»
3. размер выборки: **no** — n=30, below 139 for a clinical group — Table 1 — «SZ (N=30)»
4. описание выборки и условий: **unclear** — Age, sex, setting, country reported; dates of data collection missing — Table 1; Page 4 — «Age (Years) 43.98 (12.26); Sex at Birth 11 F, 19 M»
5. охват (пропуски): **yes** — MQ comparisons use all 58 participants (df 56), so no missing MQ data — Page 5, Results — «did have higher misophonia emotional behavior (t56=4.889, p<0.001)»
6. валидность определения случая: **no** — Only count-based definition is a study-defined item-level rule (any MQ E&B item rated 4), not a listed validated cut-off — Page 5, Results — «four participants with SZ gave at least one item from the MQ Emotional Behavior section a rating of 4»
7. единое надёжное измерение: **unclear** — Same instrument for all, but mode and reliability not reported — Page 4, Assessment: Self-report measures — «we had participants complete the MQ (Wu, et al., 2014)»
8. статистика (числитель и знаменатель): **yes** — Numerator (4) and denominator (30) clear; CI calculable — Page 5, Results; Table 1 — «four participants with SZ gave at least one item from the MQ Emotional Behavior section a rating of 4»
9. отклик: **unclear** — Number approached and response rate not reported — Page 4, Methods, Participants — «Thirty people with a diagnosis of schizophrenia or schizoaffective disorder ... provided written informed consent»

Правки:
- 

Проверено: да
### ST040-2 · Healthy volunteers (matched controls), Maryland, USA, n=28
Отчёты: R0524 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · >=1 MQ Emotions-and-Behaviors item rated 4 ('always') | **NR** | **0 / 28** | 0.0 | Pages 5-6, Results, Misophonia Questionnaire | «four participants with SZ gave at least one item from the MQ Emotional Behavior section a rating of 4 ... This was true for no HVs.» |

- E1: источник порога: study's own; правило: MQ row; single-item rule not placeable on scale metric (G2/G3); G6; у авторов: «"always" engage in the respective avoidant/emotional behavior in response to a …»; главная у авторов: no; период: NR; заметка: Not presented as a misophonia case definition. Only means reported otherwise (SRSS 2.478, SD 2.213).

**Ключевые поля выборки:**
- **n_analysed: 28** — Table 1 — «HV (N=28)»
- **population: other_nonclinical** — Page 4, Methods, Participants — «as was the absence of Axis I and Axis II diagnoses in HVs»
- **sampling: NR** — Page 4, Methods, Participants — «28 demographically-matched healthy volunteers (HV) provided written informed consent»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — Page 4, Methods, Participants — «protocols approved by the Institutional Review Board of the University of Maryland School of Medicine (Protocol HP-00051996)»
- setting: community (healthy volunteers for a research centre MRI study) — Page 4, Methods, Participants — «28 demographically-matched healthy volunteers (HV)»
- data_years: NR — NA
- design: other — Page 4, Methods, Participants — «28 demographically-matched healthy volunteers (HV) ... successfully completed a behavioral task in the MRI scanner.»
- topic_disclosed: NR — NA
- inclusion_exclusion: Healthy volunteers demographically matched to SZ group; absence of Axis I/II diagnoses confirmed by SCID; excluded pregnancy and past substance dependence; completed MRI task — Page 4, Methods, Participants — «as was the absence of Axis I and Axis II diagnoses in HVs. Additional exclusionary criteria included: pregnancy and admission of past substance dependence.»
- n_invited: NR — NA
- n_responded: NR — NA
- response_rate: NR — NA
- age_mean: 43.42 — Table 1 — «Age (Years) ... 43.42 (10.97)»
- age_sd: 10.97 — Table 1 — «Age (Years) ... 43.42 (10.97)»
- age_min: NR — NA
- age_max: NR — NA
- age_group: NR — Table 1 — «43.42 (10.97)»
- pct_female: 39.3 — Table 1 — «Sex at Birth ... 11 F, 17 M»
- informant: self — Page 4, Assessment: Self-report measures — «we had participants complete the MQ (Wu, et al., 2014)»
- mode: NR — Page 4 — «we had participants complete the MQ (Wu, et al., 2014)»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), English — Pages 4-5, Assessment: Self-report measures — «To assess sensitivity and behavior responses to misophonia trigger sounds, we had participants complete the MQ (Wu, et al., 2014)»
- instrument_validated_in_language: yes — Page 12 references — «Wu MS, Lewin AB, Murphy TK, & Storch EA (2014). Misophonia: Incidence, Phenomenology, and Clinical Correlates in an Undergraduate Student Sample.»
- pub_status: journal — Page 1, header — «Published in final edited form as: Schizophr Res. 2024 December ; 274: 329–336.»
- language: English — Full text — «Aberrant Salience Signaling in Auditory Processing in Schizophrenia»
- funding_coi: University of Maryland MPower funds, PRISM award, NIH 1R01MH115031; DLK consults for Alkermes, Karuna, Janssen; no financial COI declared — Page 10; Page 1 — «JAW's participation was supported by NIH grant 1R01MH115031.»
- notes: Control group recruited separately and matched to the SZ group. Screened free of Axis I/II disorders, so not a general-population sample. pct_female = 11/28. The age range is not reported.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Recruitment frame for healthy volunteers not described — Page 4, Methods, Participants — «28 demographically-matched healthy volunteers (HV)»
2. способ отбора: **unclear** — Sampling method not described; volunteers matched to patients — Page 4, Methods, Participants — «28 demographically-matched healthy volunteers (HV) provided written informed consent»
3. размер выборки: **no** — n=28 < 385 — Table 1 — «HV (N=28)»
4. описание выборки и условий: **unclear** — Age, sex, setting, country reported; dates missing — Table 1 — «Age (Years) 43.42 (10.97); 11 F, 17 M»
5. охват (пропуски): **yes** — MQ analyses include all participants (df 56) — Page 5, Results — «HVs (M = 0.857, SD = 0.782; t56=0.554, p=0.582)»
6. валидность определения случая: **no** — Only count is a study-defined item-level rule, not a validated cut-off — Pages 5-6, Results — «This was true for no HVs.»
7. единое надёжное измерение: **unclear** — Same instrument for all; mode and reliability not reported — Page 4 — «we had participants complete the MQ (Wu, et al., 2014)»
8. статистика (числитель и знаменатель): **yes** — 0/28 traceable; CI calculable — Pages 5-6, Results; Table 1 — «This was true for no HVs.»
9. отклик: **unclear** — Response rate not reported — Page 4 — «28 demographically-matched healthy volunteers (HV) provided written informed consent»

Правки:
- 

Проверено: да