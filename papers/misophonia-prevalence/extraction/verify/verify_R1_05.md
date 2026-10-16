# Проверка выписывания — файл 5 из 10

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

## ST041 · Ertürk 2024 · International journal of developmental disabilities

Основной отчёт R0528: [текст](../../fulltext/text/R0528.txt) · [PDF](../../fulltext/pdf/R0528.pdf) — «Examining the correlation between misophonia symptoms and autistic traits in general population.» — [DOI](https://doi.org/10.1080/20473869.2023.2165231)
Расхождения в тексте: Table 1 band counts sum correctly: total 191+184+63+7=445; female 99+109+37+4=249; male 92+75+26+3=196. Table 4 gives female n=246, against 249 in the text and Table 1. Table 4 also prints identical AQ totals for females and males (19.81 ± 6.86), probably a typesetting error. The title and abstract say 'general population', but Methods describe medical faculty students. The AMISOS-R section says 'validity and reliability of the AQ in the Turkish population (Cakiroglu et al. 2022)'; this is a typo for AMISOS-R. Minus signs appear lost in Table 5 and in the t statistics in the text. The paper gives AMISOS-R band labels without numeric cut-points.
Заметка ИИ: The study is correlational, and the authors name no primary prevalence estimate. Cumulative estimates come from Table 1 bands. The recommended L2 cut-off (AMISOS-R >=24) cannot be derived, so the L2 estimates rest on the moderate band (>=21). Data years and sampling method are not reported.

### ST041-1 · Medical faculty students, Süleyman Demirel University, Isparta, Turkey (n=445)
Отчёты: R0528 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | AMISOS-R · AMISOS-R >=11 (mild or more; numeric cut not printed, band label only) | **L1** | **254 / 445** | 57.1 | Page 4, Table 1 | «Total (n) 191 184 63 7 445» |
| E2 | all | AMISOS-R · AMISOS-R >=21 (moderate or more; numeric cut not printed, band label only) | **L2** | **70 / 445** | 15.7 | Page 4, Table 1 | «Total (n) 191 184 63 7 445» |
| E3 | all | AMISOS-R · AMISOS-R >=31 (severe and extreme; numeric cut not printed) | **L2** | **7 / 445** | 1.6 | Page 4, Table 1 | «Total (n) 191 184 63 7 445» |
| E4 | female | AMISOS-R · AMISOS-R >=11 (mild or more) | **L1** | **150 / 249** | 60.2 | Page 4, Table 1 | «Female (n) 99 109 37 4 249» |
| E5 | female | AMISOS-R · AMISOS-R >=21 (moderate or more) | **L2** | **41 / 249** | 16.5 | Page 4, Table 1 | «Female (n) 99 109 37 4 249» |
| E6 | female | AMISOS-R · AMISOS-R >=31 (severe and extreme) | **L2** | **4 / 249** | 1.6 | Page 4, Table 1 | «Female (n) 99 109 37 4 249» |
| E7 | male | AMISOS-R · AMISOS-R >=11 (mild or more) | **L1** | **104 / 196** | 53.1 | Page 4, Table 1 | «Male (n) 92 75 26 3 196» |
| E8 | male | AMISOS-R · AMISOS-R >=21 (moderate or more) | **L2** | **29 / 196** | 14.8 | Page 4, Table 1 | «Male (n) 92 75 26 3 196» |
| E9 | male | AMISOS-R · AMISOS-R >=31 (severe and extreme) | **L2** | **3 / 196** | 1.5 | Page 4, Table 1 | «Male (n) 92 75 26 3 196» |

- E1: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; G1 sum of bands; у авторов: «mild misophonia or more»; главная у авторов: no; период: NR; **расчёт: 184 + 63 + 7 from Table 1 total row**; заметка: 57.1%
- E2: источник порога: validation paper; правило: AMISOS-R row; L2 >=21; G1 sum of bands; у авторов: «moderate and severe misophonia or more»; главная у авторов: no; период: NR; **расчёт: 63 + 7 from Table 1 total row**; заметка: 15.7%; recommended >=24 not available
- E3: источник порога: validation paper; правило: AMISOS-R row; G2 above L2 cut-off; top band; у авторов: «severe and extreme misophonia»; главная у авторов: no; период: NR; заметка: 1.6%; top band, so already cumulative
- E4: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; G1 sum of bands; у авторов: «mild misophonia or more»; главная у авторов: no; период: NR; **расчёт: 109 + 37 + 4 from Table 1 female row**
- E5: источник порога: validation paper; правило: AMISOS-R row; L2 >=21; G1 sum of bands; у авторов: «moderate and severe misophonia or more»; главная у авторов: no; период: NR; **расчёт: 37 + 4 from Table 1 female row**
- E6: источник порога: validation paper; правило: AMISOS-R row; G2 above L2 cut-off; top band; у авторов: «severe and extreme misophonia»; главная у авторов: no; период: NR
- E7: источник порога: validation paper; правило: AMISOS-R row; L1 >=11; G1 sum of bands; у авторов: «mild misophonia or more»; главная у авторов: no; период: NR; **расчёт: 75 + 26 + 3 from Table 1 male row**
- E8: источник порога: validation paper; правило: AMISOS-R row; L2 >=21; G1 sum of bands; у авторов: «moderate and severe misophonia or more»; главная у авторов: no; период: NR; **расчёт: 26 + 3 from Table 1 male row**
- E9: источник порога: validation paper; правило: AMISOS-R row; G2 above L2 cut-off; top band; у авторов: «severe and extreme misophonia»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 445** — Page 3, Results; Page 4, Table 1 — «The study included 445 individuals between the ages of 18 and 28»
- **population: medical_students** — Page 2, Method, Participants — «500 students between the ages of 18 and 28 at the Isparta Süleyman Demirel University Faculty of Medicine»
- **sampling: NR** — Page 2, Method, Participants — «The Amsterdam Misophonia Scale-Revised (AMISOS-R) and the Autism Spectrum Quotient (AQ) were administered to 500 students»

**Остальные поля:**
- clinical_group: NA — Page 2, Method, Participants — «The criteria for exclusion from the study were: (1) the existence of a psychiatric disorder»
- country: TUR — Page 2, Method, Participants — «administered to 500 students between the ages of 18 and 28 at the Isparta Süleyman Demirel University Faculty of Medicine»
- setting: university (Faculty of Medicine, Süleyman Demirel University, Isparta) — Page 2, Method, Participants — «administered to 500 students between the ages of 18 and 28 at the Isparta Süleyman Demirel University Faculty of Medicine»
- data_years: NR — Page 2, Method — «The SDU ethics committee approved the study protocol (2022/18-251).»
- design: cross-sectional — Page 2, Method — «Self-report questionnaires were utilized to evaluate the severity of misophonia symptoms and autistic traits.»
- topic_disclosed: NR — Page 2, Method, Participants — «After reading the consent form, The Amsterdam Misophonia Scale-Revised (AMISOS-R) and the Autism Spectrum Quotient (AQ) were administered»
- inclusion_exclusion: Students aged 18-28 at the Faculty of Medicine; excluded: psychiatric disorder, history of psychotropic medication, hearing problems (self-reported) — Page 2, Method, Participants — «(1) the existence of a psychiatric disorder (e.g. depression, bipolar disorder, anxiety disorder, ADHD), (2) a history of taking psychotropic medications, (3) …»
- n_invited: 500 — Page 3, Results — «500 participants were given scales; however, 12 declined to participate, and 43 were excluded based on the exclusion criteria»
- n_responded: 488 — Page 3, Results — «500 participants were given scales; however, 12 declined to participate»
- response_rate: 97.6 — Page 3, Results — «500 participants were given scales; however, 12 declined to participate»
- age_mean: 20.72 — Page 3, Results — «The mean age of the women was 20.71 ± 1.86 and the mean age of the men was 20.73 ± 2.16»
- age_sd: NR — Page 3, Results — «The mean age of the women was 20.71 ± 1.86 and the mean age of the men was 20.73 ± 2.16»
- age_min: 18 — Page 3, Results — «445 individuals between the ages of 18 and 28»
- age_max: 28 — Page 3, Results — «445 individuals between the ages of 18 and 28»
- age_group: adults — Page 3, Results — «445 individuals between the ages of 18 and 28»
- pct_female: 56 — Page 3, Results — «including 249 females (56%) and 196 males (44%)»
- informant: self — Page 1, Abstract — «Self-report questionnaires were utilized to evaluate the severity of misophonia symptoms and autistic traits.»
- mode: NR — Page 2, Method — «We used an interview form to gather information about the socio-demographic characteristics»
- instruments: AMISOS-R (presumably Turkish version, Cakiroglu et al. 2022; language not explicitly stated) — Page 2, Instruments — «The Amsterdam Misophonia Scale-Revised Form is a self-report instrument that measures the presence and severity of symptoms in response to particular auditory …»
- instrument_validated_in_language: yes — Page 2, Instruments, AMISOS-R — «Cakıroglu et al. analyzed the validity and reliability of the AQ in the Turkish population (Cakiroglu et al. 2022).»
- pub_status: journal — Page 1, header — «International Journal of Developmental Disabilities 2024 VOL. 70 NO. 7 1166»
- language: English — Full text — «Examining the correlation between misophonia symptoms and autistic traits in general population»
- funding_coi: No funding; no conflicts of interest declared — Page 6, Funding; Disclosure statement — «Funding was not received for the study. ... The authors report that there were no potential conflicts of interest.»
- notes: Title says 'general population' but the sample is students of one Faculty of Medicine. Overall age mean 20.72 derived as the n-weighted mean of the sex-specific means: (249x20.71+196x20.73)/445. The numeric AMISOS-R band cut-points are not printed; the band labels match the standard key (0-10, 11-20, 21-30, 31-40). The AMISOS-R validity sentence says 'AQ' by typo but cites Cakiroglu et al. 2022 (Turkish AMISOS-R validation). Data years NR (ethics approval 2022/18-251). Table 2 gives single trigger items from the AMISOS-R checklist ('In comparison to others, I am sensitive to: eating sounds' 2…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The claimed target is the general population, but the frame is students of a single medical faculty. — Title; Page 2, Participants — «administered to 500 students between the ages of 18 and 28 at the Isparta Süleyman Demirel University Faculty of Medicine»
2. способ отбора: **unclear** — The method used to select the 500 students is not described. — Page 2, Participants — «The Amsterdam Misophonia Scale-Revised (AMISOS-R) and the Autism Spectrum Quotient (AQ) were administered to 500 students»
3. размер выборки: **yes** — n=445 is at least 385. — Page 3, Results — «The study included 445 individuals»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — Page 3, Results — «including 249 females (56%) and 196 males (44%). The mean age of the women was 20.71 ± 1.86»
5. охват (пропуски): **yes** — All 445 included participants are classified in Table 1; no missing misophonia data. — Page 4, Table 1 — «Total (n) 191 184 63 7 445»
6. валидность определения случая: **no** — The highest-level definition available is L2 on AMISOS-R >=21 (moderate band), which is not anchored; the anchored >=24 cut-off is not reported. — Page 4, Table 1 — «Moderate and severe misophonia ... Total (n) ... 63»
7. единое надёжное измерение: **yes** — Everyone completed the same self-report AMISOS-R; reliability from the cited Turkish validation (internal consistency not reported in this sample). — Page 2, Instruments — «Cakıroglu et al. analyzed the validity and reliability of the AQ in the Turkish population (Cakiroglu et al. 2022).»
8. статистика (числитель и знаменатель): **yes** — Band counts and denominator are given in Table 1, so a CI can be calculated. — Page 4, Table 1 — «Total (n) 191 184 63 7 445»
9. отклик: **yes** — 488 of 500 took part (97.6%). — Page 3, Results — «500 participants were given scales; however, 12 declined to participate»

Правки:
- 

Проверено: да
---

## ST042 · Horsfall 2024 · Digital Commons @ Butler University

Основной отчёт R0555: [текст](../../fulltext/text/R0555.txt) — «Misophonia Development from Onset to College Age»
Расхождения в тексте: The text says 'Of the 71 participants', but the DMQ Impairment bands (50 mild + 10 moderate + 1 severe) add up to 61. The other 10 are not accounted for. The text says the Impairment subscale has 12 items, but Appendix B lists 11. The female/male percentages (94.3 + 5.6) sum to 99.9. '0.01% with autism' is not possible with n=71. The Abstract says DMQ is 'a diagnostic test for level of severity', but only the Impairment subscale was scored. t(68) for the self-diagnosis comparison implies about 70 cases, not 71.
Заметка ИИ: I set the DMQ Impairment moderate+ estimate to L2. The study's bands shifted by -12 (1-5 scoring to 0-4) match the published DMQ Impairment ranges exactly (>=14 moderate, >=39 severe). JBI 6 = no because Impairment bands are not on the anchored list. topic_disclosed = NR: the thesis title names misophonia, but the SONA advertisement is not reported. A reviewer may prefer 'yes'. age_group = NR because no ages are given (college undergraduates).

### ST042-1 · Butler University undergraduates (SONA pool), USA, n=71
Отчёты: R0555 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DMQ · DMQ Impairment (12 items scored 1-5) >=26 (moderate or severe); equals >=14 on the published 0-48 metric | **L2** | **11 / 71** | 15.5 | Horsfall 9, Results: Duke Misophonia Questionnaire | «Our clinical impairment scale was as follows; mild (12-25), moderate (26-50), and severe (51-60). Of the 71 participants, 50 participants scored as mild, 10 were moderate, and only 1 was severe.» |
| E2 | all | DMQ · DMQ Impairment (1-5 scoring) >=51 (severe); equals >=39 on the published 0-48 metric | **L2** | **1 / 71** | 1.4 | Horsfall 9 | «Of the 71 participants, 50 participants scored as mild, 10 were moderate, and only 1 was severe.» |
| E3 | all | DMQ · DMQ Impairment (1-5 scoring) >=12 (mild or more; 12 is the scale minimum) | **L0** | **61 / 71** | 85.9 | Horsfall 9 | «mild (12-25), moderate (26-50), and severe (51-60). Of the 71 participants, 50 participants scored as mild, 10 were moderate, and only 1 was severe.» |
| E4 | all | adhoc · self-identified misophonia (yes/no item, after a definition was shown) | **L1** | **27 / 71** | 38.0 | Horsfall 7-8, Participants; Horsfall 13 | «after being provided a comprehensive definition of what misophonia is, 27 of the participants selected that they believe they have misophonia.» |
| E5 | all | adhoc · 'Do sounds or noises ever bother you?' = yes | **L0** | **27 / 71** | 38.0 | Horsfall 13 | «To the question, "do sounds or noises ever bother you?" Twenty-seven participants answered yes.» |

- E1: источник порога: study's own; правило: DMQ row (Impairment total >=14); G1 sum of bands; G2/G3 mean-item comparison (26/12-1 = 14/12 = 1.17); у авторов: «moderate + severe clinical impairment»; главная у авторов: no; период: NR; **расчёт: 10 moderate + 1 severe = 11**; заметка: Denominator unclear: the bands sum to 61, not 71, so 10 participants are unclassified (alternative: 11/61). Scoring is non-standard (1-5 per item); the Appendix lists 11 items, not 12. Not the DMQ development sample, so not E3.
- E2: источник порога: study's own; правило: DMQ row (Impairment total >=39); G2; у авторов: «severe»; главная у авторов: no; период: NR; заметка: Denominator unclear (bands sum to 61).
- E3: источник порога: study's own; правило: DMQ row; G1 sum of bands; G2 floor of the scale / minimal-mild range, so L0; у авторов: «mild + moderate + severe»; главная у авторов: no; период: NR; **расчёт: 50 + 10 + 1 = 61**; заметка: Not a real case definition, because 12 is the lowest possible score. Listed only. 10 of 71 unclassified.
- E4: источник порога: study's own; правило: adhoc row; self-identification = L1 (used only if no scale-based L1); у авторов: «self-diagnosed misophonia»; главная у авторов: yes; период: current; заметка: Authors used this as their misophonia classification: 'our data relied on the self-diagnosis question'. The t-test df=68 suggests about 70 answered.
- E5: источник порога: study's own; правило: adhoc row; any bothersome sound = L0; у авторов: «bothered by sounds»; главная у авторов: no; период: lifetime; заметка: Not misophonia-specific. Listed only.

**Ключевые поля выборки:**
- **n_analysed: 71** — Horsfall 7, Participants; Horsfall 9 — «only 71 responses were complete and valid»
- **population: university_students** — Horsfall 7, Method — «to gather information from college students on misophonia»
- **sampling: convenience** — Horsfall 7, Method: Recruitment — «Recruitment for this survey was done completely online and on SONA.»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — Horsfall 18, Discussion — «Music is well integrated into our educational system in the US»
- setting: university (Butler University; online survey via the SONA undergraduate research participant system of the psychology department) — Horsfall 7, Method: Recruitment; Horsfall 18 — «distributed on Butler's SONA system for undergraduate research. Recruitment for this survey was done completely online and on SONA.»
- data_years: NR — Method — «The survey was created utilizing Butler Qualtrics software and distributed on Butler's SONA system for undergraduate research.»
- design: cross-sectional — Horsfall 7, Method: Recruitment — «A mixed method survey was conducted to gather information from college students on misophonia.»
- topic_disclosed: NR — Horsfall 7, Method: Recruitment — «A mixed method survey was conducted to gather information from college students on misophonia.»
- inclusion_exclusion: Butler undergraduates on SONA who consented; only complete and valid responses analysed (criteria for validity not stated) — Horsfall 7, Participants — «In total, 80 people initiated the survey, but only 71 responses were complete and valid.»
- n_invited: NR — Method — «Recruitment for this survey was done completely online and on SONA.»
- n_responded: 80 — Horsfall 7, Participants — «In total, 80 people initiated the survey»
- response_rate: NR — Method — «Recruitment for this survey was done completely online and on SONA.»
- age_mean: NR — Participants — «Of the participants, 5.6% were male- and 94.3% were female-identifying.»
- age_sd: NR — Participants
- age_min: NR — Participants
- age_max: NR — Participants
- age_group: NR — Participants — «to gather information from college students on misophonia»
- pct_female: 94.3 — Horsfall 7, Participants — «Of the participants, 5.6% were male- and 94.3% were female-identifying.»
- informant: self — Horsfall 18, Discussion — «we relied on participants to self-report their symptoms and experiences»
- mode: online — Horsfall 7, Method — «The survey was created utilizing Butler Qualtrics software ... Recruitment for this survey was done completely online»
- instruments: Duke Misophonia Questionnaire (DMQ, English, Duke Center v1.3 form; Impairment subscale scored 1-5 per item); ad hoc items in English (self-identified misophonia 'Do you think you have misophonia?'; 'Do sounds or noises ever bother you?') — Horsfall 8, Survey; Appendix A — «The Duke Misophonia Questionnaire (Duke Center for Misophonia and Emotion Regulation, 2021): A 100 question survey ... Do you think you have misophonia?»
- instrument_validated_in_language: NR — Horsfall 8, Survey; References — «Duke Center for Misophonia and Emotion Regulation. Duke Misophonia Questionnaire (DMQ). May 31, 2021.»
- pub_status: thesis — Title page — «Undergraduate Honors Thesis Collection ... 5-2024 Misophonia Development from Onset to College Age Hope Horsfall»
- language: English — Full text — «Misophonia is a newly recognized disorder, defined as the hatred of specific trigger sounds»
- funding_coi: NR — Full text
- notes: Undergraduate honors thesis. Age and data-collection years not reported (DMQ form 'Accessed March, 2023' suggests 2023, not stated). DMQ Impairment scored by the study 1-5 per item over 12 items (range 12-60), not the published 0-4 scoring; the Appendix lists only 11 Impairment items. The study's bands (mild 12-25, moderate 26-50, severe 51-60) equal the published DMQ Impairment ranges 0-13 / 14-38 / 39-48 shifted by +12, but the thesis does not say so. DMQ bands sum to 61, not 71. Topic disclosure: the thesis title and survey content name misophonia, but the SONA listing text is not given. S…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is the psychology department SONA pool, which covers only part of the college student population. — Horsfall 18, Discussion — «the study was disseminated through the SONA website of the psychology department, which predominantly comprises female students»
2. способ отбора: **no** — Volunteers opted in through SONA (convenience). — Horsfall 7, Recruitment — «Recruitment for this survey was done completely online and on SONA.»
3. размер выборки: **no** — n=71, below 385. — Horsfall 7, Participants — «only 71 responses were complete and valid»
4. описание выборки и условий: **no** — Sex, setting and country are reported; age and dates are missing. — Horsfall 7, Participants — «Of the participants, 5.6% were male- and 94.3% were female-identifying.»
5. охват (пропуски): **no** — 9 of 80 starters were excluded, and only 61 of 71 fall in a DMQ impairment band (about 14% unclassified). This is not handled. — Horsfall 7; Horsfall 9 — «Of the 71 participants, 50 participants scored as mild, 10 were moderate, and only 1 was severe.»
6. валидность определения случая: **no** — Primary definition (L2) is a modified DMQ Impairment band (moderate+). These bands are percentile-based and not anchored by interview or ROC. Scoring was modified, and no validation was cited. — Horsfall 9 — «Our clinical impairment scale was as follows; mild (12-25), moderate (26-50), and severe (51-60).»
7. единое надёжное измерение: **unclear** — Everyone had the same online instrument, but no reliability was reported. — Horsfall 8, Results — «each participant was required to complete the Duke Misophonia Questionnaire»
8. статистика (числитель и знаменатель): **no** — The band counts (61) do not match the stated denominator (71), and no CIs are given. — Horsfall 9 — «Of the 71 participants, 50 participants scored as mild, 10 were moderate, and only 1 was severe.»
9. отклик: **no** — Open SONA online survey with no denominator of invited people and no handling of non-response. — Horsfall 7 — «In total, 80 people initiated the survey»

Правки:
- 

Проверено: да
---

## ST043 · Mahzouni 2024 · Multisensory research

Основной отчёт R0583: [текст](../../fulltext/text/R0583.txt) — «Positive Attributable Visual Sources Attenuate the Impact of Trigger Sounds in Misophonia.» — [DOI](https://doi.org/10.1163/22134808-bja10137)
Не выписано ИИ: Misophonia group (31 recruited, 26 analysed): misophonic participants interviewed in a previous study (Samermit et al., 2022) and recruited via ads because of misophonia. Excluded under E1 (recruited because of misophonia). p. 5, Section 2.1: "We recruited 31 misophonic participants who were interviewed in a previous study (Samermit et al., 2022)."
Расхождения в тексте: Control-group means differ between Table 1 and the text in Section 3.1: A-MISO-S 3.87 (2.50) in Table 1 vs 3.64 (2.50) in the text; MQ sensitivity 15.10 (10.79) vs 14.32 (10.54); MQ severity 2.71 (2.16) vs 2.58 (2.20). DMQ means agree (0.82 (0.28)). The text says controls were excluded if they scored "higher than 1.5". The Figure 1 legend says retained controls "scored lower than 1.5". How a score of exactly 1.5 was handled is unclear. Table 1 gives the A-MISO-S range as "(0 to 4)" and the MQ sensitivity range as "(0 to 4)", which do not match the reported means and appear to be labelling errors.
Заметка ИИ: This is an experimental study with a misophonia group and a control group. Only the control group (psychology-pool students) is eligible. Its only prevalence-relevant figure is the 7 of 38 controls excluded for DMQ symptom severity >1.5. That threshold is the study's own and lies below the anchored 1.8 cut-off, so it is coded L1 by G3. A reviewer should confirm that this exclusion count may be used as a prevalence estimate at all.

### ST043-1 · UCSC psychology research pool controls, USA, n=38 screened (31 retained)
Отчёты: R0583 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DMQ · DMQ symptom severity (mean of affective, physiological, cognitive items, 0-4) >1.5 | **L1** | **7 / 38** | 18.4 | p. 5, Section 2.1 | «We also recruited 38 naive participants ... We excluded seven control participants who scored higher than 1.5 in the DMQ symptom severity scale» |

- E1: источник порога: study's own; правило: DMQ row; G3 (study-defined threshold below the L2 cut-off of 1.8; no published L1); у авторов: «NR (exclusion criterion for the control group)»; главная у авторов: no; период: NR; заметка: Used only as an exclusion criterion, not presented as prevalence. The count at the recommended DMQ >=1.8 is not reported. 7/38 = 18.4%.

**Ключевые поля выборки:**
- **n_analysed: 38** — p. 5, Section 2.1 — «recruited 38 naive participants ... We excluded seven control participants who scored higher than 1.5»
- **population: university_students** — p. 5, Section 2.1 — «psychology research pool at the University of California Santa Cruz (UCSC) ... received course credit»
- **sampling: convenience** — p. 5, Section 2.1 — «recruited 38 naive participants from the psychology research pool ... who received course credit for their participation»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — p. 5, Section 2.1 — «We also recruited 38 naive participants from the psychology research pool at the University of California Santa Cruz (UCSC) as the control group.»
- setting: university (psychology research participant pool, UC Santa Cruz) — p. 5, Section 2.1 — «38 naive participants from the psychology research pool at the University of California Santa Cruz (UCSC) as the control group»
- data_years: NR — NR — «NR»
- design: screening phase of experiment — p. 5, Section 2.1 — «We excluded seven control participants who scored higher than 1.5 in the DMQ symptom severity scale»
- topic_disclosed: NR — p. 5, Section 2.1 — «We also recruited 38 naive participants from the psychology research pool»
- inclusion_exclusion: Psychology research pool participants; excluded from control group if DMQ symptom severity >1.5 (7 excluded) — p. 5, Section 2.1 — «We excluded seven control participants who scored higher than 1.5 in the DMQ symptom severity scale; thus, the control group included a total of 31 participants»
- n_invited: NR — NR — «NR»
- n_responded: 38 — p. 5, Section 2.1 — «We also recruited 38 naive participants»
- response_rate: NR — NR — «NR»
- age_mean: 21.55 — p. 5, Section 2.1 — «the control group included a total of 31 participants (26 females, three males, and two others, ages 18 to 61; M = 21.55, SD = 7.80)»
- age_sd: 7.80 — p. 5, Section 2.1 — «ages 18 to 61; M = 21.55, SD = 7.80»
- age_min: 18 — p. 5, Section 2.1 — «ages 18 to 61»
- age_max: 61 — p. 5, Section 2.1 — «ages 18 to 61»
- age_group: adults — p. 5, Section 2.1 — «ages 18 to 61»
- pct_female: 83.9 — p. 5, Section 2.1 — «31 participants (26 females, three males, and two others»
- informant: self — p. 6, Section 2.3 — «participants filled out several questionnaires, including three misophonia questionnaires: the DMQ, Amsterdam Misophonia Scale (A-MISO-S), and MQ»
- mode: online — p. 6, Section 2.3 — «Participants completed the experiment via Qualtrics.»
- instruments: DMQ (English); A-MISO-S (English); MQ (English) — p. 6, Section 2.3; p. 8, Sections 2.4.2-2.4.4 — «three misophonia questionnaires: the DMQ, Amsterdam Misophonia Scale (A-MISO-S), and MQ»
- instrument_validated_in_language: yes — p. 8, Section 2.4.2 — «The DMQ is a self-report questionnaire that has been psychometrically validated to measure misophonic experiences across several different dimensions (Rosentha…»
- pub_status: journal — p. 1, header — «Multisensory Research (2024) DOI:10.1163/22134808-bja10137 ... Peer reviewed»
- language: English — whole text — «Positive Attributable Visual Sources Attenuate the Impact of Trigger Sounds in Misophonia»
- funding_coi: NR (no funding or COI statement in text); participants received course credit — p. 5, Section 2.1 — «who received course credit for their participation»
- notes: Experimental study, not a prevalence study. Only the control group is eligible; the only prevalence-type information is the count of controls excluded for DMQ symptom severity >1.5 (7/38). Age, sex (26F/3M/2 other; pct_female = 26/31) and scale scores describe only the 31 retained controls, not the 38 screened. No counts above A-MISO-S or MQ thresholds reported. Mode: Qualtrics; lab vs remote not stated. Misophonia group (recruited from the earlier Samermit et al. 2022 sample) excluded under E1.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Psychology research pool covers only part of the UCSC student population; no target population stated — p. 5, Section 2.1 — «38 naive participants from the psychology research pool at the University of California Santa Cruz»
2. способ отбора: **no** — Volunteer convenience sample from a course-credit research pool — p. 5, Section 2.1 — «who received course credit for their participation»
3. размер выборки: **no** — n = 38 < 385 — p. 5, Section 2.1 — «We also recruited 38 naive participants»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported (age/sex only for the 31 retained); data collection dates missing — p. 5, Section 2.1 — «31 participants (26 females, three males, and two others, ages 18 to 61; M = 21.55, SD = 7.80)»
5. охват (пропуски): **unclear** — Missing misophonia data not reported — p. 5, Section 2.1 — «We excluded seven control participants who scored higher than 1.5 in the DMQ symptom severity scale»
6. валидность определения случая: **no** — Study's own DMQ cut-off >1.5, below the anchored 1.8 cut-off and without its own published basis — p. 5, Section 2.1 — «We excluded seven control participants who scored higher than 1.5 in the DMQ symptom severity scale»
7. единое надёжное измерение: **yes** — Same self-report DMQ via Qualtrics for all; Cronbach's alpha reported for the control group — p. 10, Section 3.1 — «In the control group, the Cronbach alpha was 0.91 for the DMQ symptom severity scale»
8. статистика (числитель и знаменатель): **yes** — Numerator (7) and denominator (38) are clear; CI can be calculated, though none is reported — p. 5, Section 2.1 — «We also recruited 38 naive participants ... We excluded seven control participants who scored higher than 1.5»
9. отклик: **unclear** — Number of pool members invited or exposed to the study is not reported — p. 5, Section 2.1 — «We also recruited 38 naive participants from the psychology research pool»

Правки:
- 

Проверено: да
---

## ST044 · Mednicoff 2024 · Philosophical transactions of the Royal Society of London. Series B, Biological…

Основной отчёт R0585: [текст](../../fulltext/text/R0585.txt) — «Misophonia reactions in the general population are correlated with strong emotional reactions to other everyday sensory-emotional experiences.» — [DOI](https://doi.org/10.1098/rstb.2023.0253)
Расхождения в тексте: The A-MISO-S band counts (91+95+72+17+3) sum to 278, matching the final sample. Table 1 gender counts (93+166+7+3+4+2+3) also sum to 278. The ethics section says no ethical approval was required, but the Methods state UNLV IRB approval.
Заметка ИИ: The authors report no prevalence. All estimates are derived from the A-MISO-S severity-band counts and are not the authors' primary outcome. Recruitment was partly enriched for misophonia, so the reviewer should check eligibility.

### ST044-1 · Online mixed-recruitment adult sample (UNLV pool + social media), mainly USA, n=278
Отчёты: R0585 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **92 / 278** | 33.1 | Methods, Misophonia self-report | «10–14 moderate (n = 72), 15–19 severe (n = 17) and 20–24 extreme (n = 3)» |
| E2 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **187 / 278** | 67.3 | Methods, Misophonia self-report | «5–9 mild (n = 95), 10–14 moderate (n = 72), 15–19 severe (n = 17) and 20–24 extreme (n = 3)» |
| E3 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **20 / 278** | 7.2 | Methods, Misophonia self-report | «15–19 severe (n = 17) and 20–24 extreme (n = 3)» |

- E1: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate or more (moderate/severe/extreme bands)»; главная у авторов: no; период: NR; **расчёт: 72 + 17 + 3 = 92 (moderate + severe + extreme bands)**; заметка: Self-completed A-MISO-S; the sample is partly enriched via misophonia-related ads and groups.
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «mild or more»; главная у авторов: no; период: NR; **расчёт: 95 + 72 + 17 + 3 = 187**
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G2 above L2 cut-off; у авторов: «severe or more»; главная у авторов: no; период: NR; **расчёт: 17 + 3 = 20**; заметка: Stricter than the recommended L2 cut-off.

**Ключевые поля выборки:**
- **n_analysed: 278** — Methods, Participants — «resulting in a final sample of 278 participants (table 1)»
- **population: gp_other** — Methods, Participants — «Participants were recruited from the UNLV Psychology Participant Pool (20.9%), university listservers (9%), snowball sampling ... Reddit pages (39.2%), Facebook groups (5.8%)»
- **sampling: convenience** — Methods, Participants — «snowball sampling with family and friends of the lab (21.6%), or advertisements posted on personal and lab social media pages (2.5%), Reddit pages (39.2%), Facebook groups (5.8%) and misophonia support/advocacy groups (1%)»

**Остальные поля:**
- clinical_group: NA — NA
- country: MULTI: USA, CAN, other (16.5% unspecified) — Table 1 — «current country United States | 209 | 75.2 Canada | 23 | 8.3 other | 46 | 16.5»
- setting: online (UNLV psychology participant pool, university listservs, snowball, social media, Reddit, Facebook groups, misophonia support groups) — Methods, Participants — «Participants were recruited from the UNLV Psychology Participant Pool (20.9%), university listservers (9%), snowball sampling with family and friends of the la…»
- data_years: 2021-2023 — Methods, Participants — «A total of 301 people were initially recruited for this study from October 2021 to July 2023»
- design: cross-sectional — Methods, Apparatus and procedure — «This study was implemented online using the online survey builder Qualtrics»
- topic_disclosed: yes — Methods, Participants (after Table 1) — «The first, general advertisement described the study as investigating emotional responses to meaningful sounds in the world. The second specifically mentioned …»
- inclusion_exclusion: Adults >=18, proficient English, healthy, normal/corrected hearing and vision; excluded failed attention/headphone-quiet checks (n=16) and sound-loading problems (n=7) — Methods, Participants — «at least 18 years of age, spoke English proficiently, were healthy ... We excluded participants who failed attention and headphone/quiet testing location check…»
- n_invited: NR — NA
- n_responded: 301 — Methods, Participants — «A total of 301 people were initially recruited for this study»
- response_rate: NR — NA
- age_mean: 30.7 — Table 1 — «mean | 30.7»
- age_sd: 13.3 — Table 1 — «standard deviation | 13.3»
- age_min: 18 — Table 1 — «range | 18–76»
- age_max: 76 — Table 1 — «range | 18–76»
- age_group: adults — Methods, Participants — «self-reported that they were at least 18 years of age»
- pct_female: 59.7 — Table 1 — «female | 166 | 59.7»
- informant: self — Methods, Misophonia self-report — «Participants then completed the Amsterdam Misophonia Scale (A-MISO-S)»
- mode: online — Methods, Apparatus and procedure — «This study was implemented online using the online survey builder Qualtrics»
- instruments: A-MISO-S (English, self-report, preceded by a definition of misophonia); 26-item trigger checklist (ad hoc, no case definition); video reactions task — Methods, Misophonia self-report — «Participants then completed the Amsterdam Misophonia Scale (A-MISO-S), which presents six items, each yielding a score from 0–4»
- instrument_validated_in_language: NR — Methods, Misophonia self-report; Endnote — «This survey was initiated prior to the publication of the consensus definition of misophonia [3] and prior to publication of several validation studies of miso…»
- pub_status: journal — Header — «Philosophical transactions of the Royal Society of London. Series B, Biological sciences»
- language: English — Full text — «Misophonia reactions in the general population are correlated with strong emotional reactions to other everyday sensory–emotional experiences»
- funding_coi: Misophonia Research Fund grant to E.E.H.; no competing interests declared — Funding; Conflict of interest declaration — «This work was supported by a Misophonia Research Fund grant awarded to E.E.H. ... We declare we have no competing interests.»
- notes: Not a prevalence study; A-MISO-S band counts are given only descriptively. Recruitment was partly enriched for misophonia: 1% came from misophonia support/advocacy groups, and misophonia-specific ads ran on Reddit/Facebook groups about misophonia/ASMR/chills (Reddit 39.2%). These subsets are not reported separately, so they cannot be excluded; prevalence is likely inflated. Participants saw a definition of misophonia before the A-MISO-S. The A-MISO-S was self-completed (originally clinician-rated). Country is mostly USA. The ethics statement is contradictory (UNLV IRB approval vs 'did not req…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Claims to describe the general population but the frame is a university pool, social media and interest groups — Methods, Participants — «Participants were recruited from the UNLV Psychology Participant Pool (20.9%), university listservers (9%), snowball sampling ... Reddit pages (39.2%)»
2. способ отбора: **no** — Convenience/snowball volunteer opt-in recruitment — Methods, Participants — «snowball sampling with family and friends of the lab (21.6%), or advertisements posted on personal and lab social media pages»
3. размер выборки: **no** — n = 278 < 385 — Methods, Participants — «resulting in a final sample of 278 participants»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported — Table 1; Methods, Participants — «from October 2021 to July 2023 (see table 1 for demographic information regarding age, sex, etc.)»
5. охват (пропуски): **yes** — A-MISO-S band counts sum to the full analysed sample (278); 23/301 (7.6%) excluded for data-quality reasons — Methods, Misophonia self-report — «0–4 subclinical (n = 91), 5–9 mild (n = 95), 10–14 moderate (n = 72), 15–19 severe (n = 17) and 20–24 extreme (n = 3)»
6. валидность определения случая: **unclear** — A-MISO-S >=10 is an anchored cut-off, but no published validation of the self-report English version is cited (only Schröder 2013) — Methods, Misophonia self-report — «According to Schröder et al. [84], overall scores are interpreted as follows»
7. единое надёжное измерение: **unclear** — Same online instrument for all, but no A-MISO-S reliability is reported (omega given only for Gold-MSI) — Methods, Musicality and background measures — «we used the overall Gold-MSI score (ω = 0.94)»
8. статистика (числитель и знаменатель): **yes** — Band counts and denominator are clear; CI calculable — Methods, Misophonia self-report — «10–14 moderate (n = 72), 15–19 severe (n = 17) and 20–24 extreme (n = 3)»
9. отклик: **no** — Open online recruitment with no denominator of invited people; no non-response handling — Methods, Participants — «all other participants were volunteers who received no compensation»

Правки:
- 

Проверено: да
---

## ST045 · Silva 2024 · Healthcare (Basel, Switzerland)

Основной отчёт R0625: [текст](../../fulltext/text/R0625.txt) — «Assessing Misophonia in Young Adults: The Prevalence and Psychometric Validation of the MisoQuest Questionnaire.» — [DOI](https://doi.org/10.3390/healthcare12181888)
Приложен R0522: [текст](../../fulltext/text/R0522.txt) — «Prevalência de Misofonia em estudantes de graduação do IFG, campus Goiânia»
Связь отчётов: Federal Institute of Goias students: both cite ethics approval 5.631.371; the 322 undergraduates of R0522 are probably part of the 549 students of R0625
Расхождения в тексте: 1) The main estimate, 4.5% of 549, does not match an integer count: 24/549 = 4.37% and 25/549 = 4.55%. cases = 25 (rounded). 2) R0522 gives the self-declared share as both 56.5% and 56.8%. 3) R0522: '99.7%' of those answering 'don't know'/'no' scored below 61. With about 140 such people, this does not match an integer count. 4) The abstract and Discussion give the three-factor CFA as RMSEA = 0.037, but Results say RMSEA = 0.001 and SRMR = 0.037. 5) The power analysis says the one-factor CFA used 274 participants and the three-factor CFA used 549. Section 3.2.1 says CFA was run on a 274-person subset. 6) The text says MisoQuest has low sensitivity, so prevalence may be underestimated.
Заметка ИИ: There is one sample, coded L2 on MisoQuest >=61. Points for the reviewer to check: the population code (a mix of high-school and undergraduate students), topic_disclosed (NR: students were told the research objectives, but the wording of the invitation is not given), and JBI 6. The Brazilian version is validated only in this report.

### ST045-1 · Students (technical/high school, adult education and undergraduate), Federal Institute of Goias, Brazil, n=549
Отчёты: R0625 (main); R0522

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MisoQuest · MisoQuest total >=61 | **L2** | **25 / 549** | 4.6 | 3.1; Abstract; 4. Discussion | «we assessed misophonia using the MisoQuest tool, with scores ranging from 14 to 70 and a predefined cutoff value of 61 [14,22]. Considering this value, 4.5% of the participants were positive for misophonia.» |
| E2 | undergraduates (R0522, n=322) | adhoc · self-declared misophonic (self-identification item) | **L1** | **182 / 322** | 56.5 | R0522, Resultados e Discussão | «Foram recrutados 322 estudantes, dos quais 56,5% se autodeclararam misofônicos. [322 students were recruited, of whom 56.5% self-declared misophonic.]» |
| E3 | undergraduates (R0522, n=322) | MisoQuest · MisoQuest total >=61 | **L2** | **NR / 322** |  | R0522, Resultados e Discussão | «8,2% dos que se autodeclaram misofônicos tiveram diagnóstico confirmado pelo Misoquest [8.2% of self-declarers had diagnosis confirmed by MisoQuest]; 99,7% dos indivíduos que responderam ‘não sei’ e ‘não’ apresentaram s…» |

- E1: источник порога: developer paper; правило: MisoQuest row; L2 >=61; у авторов: «positive for misophonia»; главная у авторов: yes; период: current; **расчёт: 4.5% x 549 = 24.7 -> 25**; заметка: No count printed; 25/549 = 4.55%, 24/549 = 4.37%; 4.5% may be truncated, or the denominator may differ. Reviewer to check Figure 2 histogram.
- E2: источник порога: study's own; правило: adhoc row; L1 self-identified misophonia; у авторов: «se autodeclararam misofônicos [self-declared misophonic]»; главная у авторов: no; период: NR; **расчёт: 56.5% x 322 = 181.9 -> 182**; заметка: From the attached conference abstract; the subset is probably included in the 549. Later in the same text it is 56.8% (56.8% x 322 = 183). Self-identification item; the sample has a scale-based estimate.
- E3: источник порога: developer paper; правило: MisoQuest row; L2 >=61; у авторов: «diagnóstico confirmado pelo Misoquest [diagnosis confirmed by MisoQuest]»; главная у авторов: no; период: current; заметка: Count over all 322 not given. About 8.2% x 182 self-declarers = 15, plus at most about 0-1 of the non-declarers (99.7% below 61 does not match an integer of about 140). Roughly 15/322 = 4.7%. Not computed as cases because of these inconsistencies.

**Ключевые поля выборки:**
- **n_analysed: 549** — 3.1; 4. Discussion — «Among the 549 participants... 4.5% were identified as positive for misophonia based on the MisoQuest score with a cutoff value of 61»
- **population: university_students** — 2.2. Participants — «In total, this study enrolled 549 students from both technical and undergraduate programs»
- **sampling: convenience** — 2.2. Participants — «The research team visited students in their respective classes, inviting them to participate in the study... Undergraduate students ... were contacted, invited, and instructed about the research through course and class groups.»

**Остальные поля:**
- clinical_group: NA — NA
- country: BRA — 2.2. Participants — «Federal Institute of Education, Science, and Technology in Goias, Brazil»
- setting: school/university: Federal Institute of Education, Science, and Technology in Goias (integrated high-school technical courses, Adult and Youth Education, undergraduate courses); R0522: campus Goiânia — 2.2. Participants; R0522, Metodologia — «This study enrolled students from technical and undergraduate programs at the Federal Institute of Education, Science, and Technology in Goias, Brazil.»
- data_years: 2022-2023 — 2.3. Online Assessments — «The MisoQuest was made available to participants during the period between 15 September 2022 and 15 August 2023.»
- design: cross-sectional — 2.1. Design — «We conducted a cross-sectional study to investigate the prevalence of misophonia.»
- topic_disclosed: NR — 2.2. Participants — «students were informed about the research objectives and the procedures for accessing and completing the online questionnaire»
- inclusion_exclusion: Students of technical (integrated high school, AYE) and undergraduate programmes; excluded physical or intellectual limitations or known mental disorders; minors needed parental consent — 2.2. Participants — «Exclusion criteria included individuals with physical, intellectual limitations, or known mental disorders.»
- n_invited: NR — 2.2. Participants — «The research team visited students in their respective classes, inviting them to participate in the study.»
- n_responded: 549 — 3.1 — «A total of 549 students (mean = 23.2 years old, SD = 9.3) were enrolled in our study»
- response_rate: NR — NA
- age_mean: 23.2 — 3.1 — «A total of 549 students (mean = 23.2 years old, SD = 9.3)»
- age_sd: 9.3 — 3.1 — «(mean = 23.2 years old, SD = 9.3)»
- age_min: 13 — 2.2. Participants — «The first modality comprises young individuals aged between 13 and 18 years»
- age_max: NR — NA
- age_group: mixed — 2.2. Participants — «technical course participants aged between 13 and 18 years for those in the integrated high school modality, and over 18 years in the Adult and Youth Education…»
- pct_female: 51.9 — 3.1 — «comprising 285 females, 260 males, and 4 individuals who did not disclose their gender»
- informant: self — 2.3. Online Assessments — «The MisoQuest, a recently developed self-report questionnaire»
- mode: online — 2.3. Online Assessments; R0522, Metodologia — «The MisoQuest was administered through online forms.»
- instruments: MisoQuest, Brazilian Portuguese (translated and back-translated by the authors); R0522 (undergraduate subset): self-declaration of misophonia item (Portuguese) — 2.3. Online Assessments; R0522, Resultados — «The Brazilian Portuguese version was derived from the original English version provided by the creators of the MisoQuest [22]. Two translations were conducted»
- instrument_validated_in_language: yes — Abstract; 5. Conclusions — «This study aimed to examine the psychometric properties of the Brazilian version of the MisoQuest... The Brazilian version of the MisoQuest is a reliable and v…»
- pub_status: journal — Header — «Healthcare (Basel, Switzerland); DOI: 10.3390/healthcare12181888»
- language: English — Full text — «Assessing Misophonia in Young Adults: The Prevalence and Psychometric Validation of the MisoQuest Questionnaire»
- funding_coi: NR (no funding or COI statement in the supplied text); ethics approval 5.631.371 — 2.2. Participants — «as approved by the Research Ethics Committee (reference number: 5.631.371)»
- notes: pct_female derived: 285/549 = 51.9%. The Brazilian MisoQuest is validated only in this report (EFA/CFA, alpha); the >=61 cut-off has no criterion validation in Portuguese. There were two recruitment channels: class visits for technical students and course/class groups for undergraduates. It is one study with the same instrument and period, and results are reported only pooled, so it is treated as one sample. The sizes of the technical and undergraduate subgroups are not given in R0625. Overlap: R0522 (conference abstract, same ethics approval 5.631.371) reports 322 undergraduates at campus Go…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target is students of the Federal Institute of Goias; frame (which classes, campuses, courses were visited or contacted) is not described — 2.2. Participants — «The research team visited students in their respective classes, inviting them to participate in the study.»
2. способ отбора: **no** — Volunteer opt-in after class visits and course-group messages; no probability sampling — 2.2. Participants — «Undergraduate students ... were contacted, invited, and instructed about the research through course and class groups.»
3. размер выборки: **yes** — n = 549 >= 385 — 3.1 — «A total of 549 students»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported — 2.2; 2.3; 3.1 — «(mean = 23.2 years old, SD = 9.3)... 285 females, 260 males»
5. охват (пропуски): **unclear** — Missing data and exclusions not reported — 3.1 — «A total of 549 students ... were enrolled in our study»
6. валидность определения случая: **yes** — MisoQuest >=61 (developer cut-off). The Brazilian version is validated in this same report (structure, alpha), with no criterion validation of the cut-off in Portuguese; reviewer to confirm — 2.3; 3.1 — «A total score equal to or exceeding 61 signifies a detection of misophonia [22].»
7. единое надёжное измерение: **yes** — Same online MisoQuest and threshold for all; Cronbach's alpha 0.93 in sample — 3.2.4 — «The resulting alpha coefficient was 0.93, indicating excellent reliability.»
8. статистика (числитель и знаменатель): **unclear** — Only a percentage given (4.5%) with no count or CI; 4.5% of 549 does not match an integer count (24 = 4.4%, 25 = 4.6%) — 3.1 — «Considering this value, 4.5% of the participants were positive for misophonia.»
9. отклик: **no** — Number invited not reported; no response rate or non-response handling — 2.2. Participants — «students were informed about the research objectives and the procedures for accessing and completing the online questionnaire»

Правки:
- 

Проверено: да
---

## ST046 · Simner 2024 · Assessment

Основной отчёт R0626: [текст](../../fulltext/text/R0626.txt) — «An Automated Online Measure for Misophonia: The Sussex Misophonia Scale for Adults.» — [DOI](https://doi.org/10.1177/10731911241234104)
Не выписано ИИ: 143 self-declared misophonics recruited from online misophonia communities (Facebook, Twitter) - E1 (recruited because of misophonia). Pooled whole-sample estimates mixing both streams (SMS-Misophonics 165/466; MQ-defined misophonics 198/486) were not extracted because they include the E1 group.
Расхождения в тексте: The reported specificity of 86.2% implies a 13.8% positive rate among controls, but Table A2 gives 45/329 = 13.7% (284/329 = 86.3% specificity). The difference is small and probably due to rounding or the ROC denominator. The counts agree with the totals: 358 - 29 missing = 329 = 45 + 284; whole sample 165 + 301 = 466 = 501 - 35 missing. Implied self-declared misophonics above threshold = 165 - 45 = 120 of 137 (87.6%), which is consistent with the 87.5% sensitivity. Table A1/A2 factor labels (Factor 2 = Intersocial reactivity, Factor 3 = Life consequences) are swapped relative to the text; this does not affect prevalence.
Заметка ИИ: One eligible sample: the general-population/student comparison stream. The prevalence estimate comes from the scale-development (ROC derivation) sample, so it is flagged under G8.

### ST046-1 · General population/local student comparison group, SMS-Adult development study, GBR (inferred), n=358 (329 analysed)
Отчёты: R0626 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SMS-Adult · SMS-Adult Part 2 total >50.5 (>=51) | **L2** | **45 / 329** | 13.7 | Table A2 title; Discussion | «45 People From the General Population Identified as Misophonic Using our SMS-Adult, and 284 Identified as Non-Misophonic ... Our 86% specificity means 14% of our general population sample were considered to have misopho…» |

- E1: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; G8 derivation-sample flag; у авторов: «SMS-Misophonics (clinically significant misophonia)»; главная у авторов: no; период: NR; **расчёт: n = 45 + 284 from Table A2 title (= 358 - 29 missing)**; заметка: 45/329 = 13.7%. The cut-off was derived by ROC in this report, with this group as the controls (G8 flag). The authors present the 14% as consistent with expected prevalence. No breakdown by sex or age for this stream. Part 2 items ask 'How often do these things happen to you?' with no stated period.

**Ключевые поля выборки:**
- **n_analysed: 329** — Table A2 title — «45 People From the General Population Identified as Misophonic Using our SMS-Adult, and 284 Identified as Non-Misophonic»
- **population: university_students** — Participants — «recruited from the general population and local student population ... The latter took part in exchange for course credit.»
- **sampling: convenience** — Participants — «The remaining 358 were recruited from the general population and local student population ... The latter took part in exchange for course credit.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: GBR — The Automated Interface section — «our portal has been approved for wider use by the Sussex University Science and Technology Ethics Committee»
- setting: university (local student population and general population; online, for course credit) — Participants — «The remaining 358 were recruited from the general population and local student population ... The latter took part in exchange for course credit.»
- data_years: NR — NR — «NR»
- design: validation study — Abstract — «Receiver operator characteristics show our questionnaire to be “excellent” and “good-to-excellent” at classifying misophonia»
- topic_disclosed: no — Participants — «There was no self-selection bias for this comparison group, and they did not know the topic of the study before deciding to participate.»
- inclusion_exclusion: Adults recruited as the general-population/student comparison stream; 29 could not be classified because of missing SMS data — Output: Results Screens (footnote 5) — «N = 29 from the general population (28 female, 1 male) and n = 6 self-referred misophonics (all female) could not be classified due to missing data»
- n_invited: NR — NR — «NR»
- n_responded: 358 — Participants — «The remaining 358 were recruited from the general population and local student population»
- response_rate: NR — NR — «NR»
- age_mean: NR — Participants — «(295 females, Mage = 21.58, SD = 9.36; 53 males, Mage = 19.70, SD = 6.34; five nonbinary, Mage = 22.00 SD = 2.55; five did not report demographics)»
- age_sd: NR — Participants — «295 females, Mage = 21.58, SD = 9.36; 53 males, Mage = 19.70, SD = 6.34»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- age_group: adults — Participants — «In total, we tested 501 adults»
- pct_female: 82.4 — Participants — «The remaining 358 were recruited from the general population and local student population (295 females»
- informant: self — Summary and Limitations — «our data are based on self-report»
- mode: online — Materials and Procedure — «Participants completed our study remotely, using our in-house testing platform, the Misophonia Hub»
- instruments: SMS-Adult (English, developed in this report); MQ (English; Wu et al. 2014) — Materials and Procedure; The Misophonia Questionnaire — «consisted of our two target questionnaires ... The MQ (Wu et al., 2014) is the most widely cited questionnaire»
- instrument_validated_in_language: yes — Introduction; ROC Analysis — «its scores have also been validated in three additional published papers, in both adults (Rinaldi et al., 2023; Simner et al., 2021) and adolescents»
- pub_status: journal — Header — «Year: 2024; venue: Assessment; DOI: 10.1177/10731911241234104»
- language: English — Full text — «An Automated Online Measure for Misophonia: The Sussex Misophonia Scale for Adults»
- funding_coi: REAM foundation, Misophonia Research Fund (to J.S. and J.W.); no conflicts of interest declared — Footnotes — «Authors received funding from the REAM foundation, Misophonia Research Fund initiative awarded to authors J.S. and J.W.»
- notes: Population code is a judgement call: the text says 'general population and local student population', but all took part for course credit (mean ages ~20-22), so coded university_students; gp_other is possible. Country not stated; GBR inferred from the Sussex University ethics committee. No overall age mean, only by sex: F 21.58 (SD 9.36, n=295), M 19.70 (n=53), nonbinary 22.00 (n=5); weighted mean ~21.3 (derived, not entered). pct_female = 295/358; among the 329 analysed it is 267/329 = 81.2%. The SMS-Adult cut-off (50.5) was ROC-derived in this report with this group as controls (G8 flag). M…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is local students/community volunteers taking part for course credit, which is only part of the general population the 14% is compared with — Participants — «recruited from the general population and local student population ... The latter took part in exchange for course credit.»
2. способ отбора: **no** — Convenience sample of volunteers taking part for course credit; no probability sampling — Participants — «The latter took part in exchange for course credit.»
3. размер выборки: **no** — Analysed n = 329 (358 recruited), below 385 — Table A2 title — «45 People From the General Population Identified as Misophonic Using our SMS-Adult, and 284 Identified as Non-Misophonic»
4. описание выборки и условий: **no** — Age (by sex), sex and setting are reported; data-collection dates are missing and the country is not stated explicitly (only inferable from Sussex University) — Participants — «295 females, Mage = 21.58, SD = 9.36; 53 males, Mage = 19.70, SD = 6.34»
5. охват (пропуски): **yes** — 29/358 (8.1%) not classifiable because of missing data, which is 10% or less — Output: Results Screens (footnote 5) — «N = 29 from the general population (28 female, 1 male) ... could not be classified due to missing data»
6. валидность определения случая: **yes** — SMS-Adult >=50.5 in English, ROC-validated (cut-off derived in this same sample; G8 flag) — ROC Analysis — «This established a cutoff score threshold for misophonia at 50.5 (out of 156), which successfully identifies 87.5% of misophonics while excluding 86.2% of cont…»
7. единое надёжное измерение: **yes** — Same online instrument and threshold for everyone; Cronbach's alpha reported for all factors — Exploratory Factor Analysis — «Internal reliability of all factors was very high with Cronbach’s alpha estimates (Cronbach, 1951) of .98, .94, .91, .92, and .95 for Factors 1 to 5»
8. статистика (числитель и знаменатель): **yes** — Numerator 45 and denominator 329 are clear from Table A2; a CI can be calculated — Table A2 title — «45 People From the General Population Identified as Misophonic Using our SMS-Adult, and 284 Identified as Non-Misophonic»
9. отклик: **unclear** — Participants were sent a URL by email, but the number invited and the response rate are not reported — Materials and Procedure — «Participants were sent a URL via email to take part, and the study began with ethical consents.»

Правки:
- 

Проверено: да
---

## ST047 · Skarżyński 2024 · Journal of hearing science

Основной отчёт R0629: [текст](../../fulltext/text/R0629.txt) · [PDF](../../fulltext/pdf/R0629.pdf) — «7TH INTERNATIONAL CONFERENCE ON HYPERACUSIS AND MISOPHONIA, 15–17 SEPTEMBER 2024, WARSAW, POLAND» — [DOI](https://doi.org/10.17430/jhs/192761)
Не выписано ИИ: E1 (recruited for misophonia or sound sensitivity): Campbell & Feeley (12 misophonia + 12 controls); Öztürk Özdeş HINT (8 misophonia patients + 8 controls); Siepsiak children (90, misophonia + control group); Siepsiak cognitive reappraisal pilot (23) and RCT (108); Remmert M-BAT; Banyra sexual life (88 misophonics + partners + controls); Banyra management (293 with sound hypersensitivity; 81 = 27.6% with A-MISO-S mean 9.6); Öztürk Özdeş depression (12 DST patients); Raymond & Butler (44 with / 95 without misophonia); Black et al. (140; Prolific plus misophonia newsletters, no prevalence); Lodol et al. No misophonia estimate: Jacquemin De Oorzaak (data collection ongoing); Raj-Koziak/Gos (10…
Расхождения в тексте: Goebel et al.: the STI categories add up to 99.4% (60% HC; 15% phonophobia/misophonia; 24.4% without HC). This may be rounding, or the categories may not be mutually exclusive. Cases were derived from 15% of 216. Sanfins et al.: 48% of 60 = 28.8, which is not an integer, so the percentage is rounded or the denominator differs. 8.3% of 60 = 4.98, which fits 5/60. No tables are available; all values come from abstract text.
Заметка ИИ: R0629 is a book of conference abstracts (ICHM7, J Hear Sci 2024;14(3):65–87). No abstract reports a misophonia-specific prevalence in an eligible sample. Two samples were extracted, both with non-poolable estimates only. Goebel et al. (tinnitus inpatients) has the STI 'phonophobia/misophonia' category, which is E2 under rule G9. Sanfins et al. (schoolchildren) is about hyperacusis and sound intolerance and does not name misophonia; it has L0 and E2 estimates only. The reviewer may prefer to exclude Sanfins entirely. Countries are inferred from author affiliations.

### ST047-1 · Goebel et al.: tinnitus inpatients, Germany (inferred from affiliations), n=216
Отчёты: R0629 (main; abstract 'Hyperacusis Questionnaire (Mini-HQ9)', Goebel G. et al.)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | interview · STI category 'phonophobia/misophonia' | **E2** | **32 / 216** | 14.8 | Page 10, Material and method | «We retrospectively evaluated 216 tinnitus-inpatients ... with the evaluated Structured Tinnitus Interview (STI, Goebel and Hiller, 2002): 60% HC; 15% phonophobia/misophonia; 24.4% without HC.» |

- E1: источник порога: developer paper; правило: interview row; G9 merged phonophobia/misophonia category (STI); у авторов: «phonophobia/misophonia»; главная у авторов: no; период: NR; **расчёт: 15% x 216 = 32.4 -> 32**; заметка: Not specific to misophonia (E2): listed, not pooled. It is unclear whether the categories are mutually exclusive, since they add up to 99.4%.

**Ключевые поля выборки:**
- **n_analysed: 216** — Page 10, Material and method — «We retrospectively evaluated 216 tinnitus-inpatients»
- **population: clinical** — Page 10, Material and method — «216 tinnitus-inpatients»
- **sampling: NR** — Page 10, Material and method — «We retrospectively evaluated 216 tinnitus-inpatients»

**Остальные поля:**
- clinical_group: tinnitus — Page 10, Material and method — «216 tinnitus-inpatients (47% women, age 49 ± 10)»
- country: DEU — Page 10, author affiliations — «4 Schön Klinik Roseneck, Prien, Germany»
- setting: clinic (tinnitus inpatients; hospital for behavioral medicine inferred from affiliations, not stated for the sample) — Page 10, Material and method — «We retrospectively evaluated 216 tinnitus-inpatients (47% women, age 49 ± 10)»
- data_years: NR — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»
- design: validation study — Page 10, Material and method — «At T1 and T2, we evaluated the sensitivity to change of the individual items of GÜF and HQ ... factor analysis, internal consistency, retest reliability»
- topic_disclosed: NR — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»
- inclusion_exclusion: Tinnitus inpatients, evaluated retrospectively; no other criteria reported — Page 10, Material and method — «We retrospectively evaluated 216 tinnitus-inpatients»
- n_invited: NR — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»
- n_responded: NR — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»
- response_rate: NR — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»
- age_mean: 49 — Page 10, Material and method — «(47% women, age 49 ± 10)»
- age_sd: 10 — Page 10, Material and method — «(47% women, age 49 ± 10)»
- age_min: NR — Page 10 — «(47% women, age 49 ± 10)»
- age_max: NR — Page 10 — «(47% women, age 49 ± 10)»
- age_group: NR — Page 10 — «(47% women, age 49 ± 10)»
- pct_female: 47 — Page 10, Material and method — «(47% women, age 49 ± 10)»
- informant: clinician — Page 10, Material and method — «with the evaluated Structured Tinnitus Interview (STI, Goebel and Hiller, 2002)»
- mode: face-to-face interview — Page 10, Material and method — «with the evaluated Structured Tinnitus Interview (STI, Goebel and Hiller, 2002)»
- instruments: Structured Tinnitus Interview (STI, Goebel & Hiller 2002), 'phonophobia/misophonia' category (language version NR); no misophonia-specific measure — Page 10, Material and method — «Structured Tinnitus Interview (STI, Goebel and Hiller, 2002): 60% HC; 15% phonophobia/misophonia; 24.4% without HC»
- instrument_validated_in_language: NR — Page 10, Material and method — «the evaluated Structured Tinnitus Interview (STI, Goebel and Hiller, 2002)»
- pub_status: conference — Page 1; Page 2 header — «The “Journal of Hearing Science” is pleased to publish the abstracts submitted for the 7th International Conference on Hyperacusis and Misophonia»
- language: English — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»
- funding_coi: NR — Page 10 — «NR»
- notes: This is a conference abstract. Misophonia is not measured separately: STI merges phonophobia and misophonia (E2, rule G9). The STI categories add up to 99.4% (60 + 15 + 24.4). The authors' affiliations (Prien, Bad Arolsen, Göttingen, Marburg) suggest the sample is from Germany, but the abstract does not say so. Data years are not reported.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — The frame (which clinic, which period) is not described beyond 'tinnitus inpatients'. — Page 10, Material and method — «We retrospectively evaluated 216 tinnitus-inpatients»
2. способ отбора: **unclear** — The sampling method is not described (it is not stated whether patients were consecutive). — Page 10, Material and method — «We retrospectively evaluated 216 tinnitus-inpatients»
3. размер выборки: **yes** — Clinical sample with n=216, which is at least 139 (the clinical threshold). Below 385 if the general threshold were applied. — Page 10 — «216 tinnitus-inpatients»
4. описание выборки и условий: **unclear** — Age, sex and setting are reported and the country can be inferred from affiliations; data collection dates are missing. — Page 10 — «216 tinnitus-inpatients (47% women, age 49 ± 10)»
5. охват (пропуски): **unclear** — Missing data are not reported. — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»
6. валидность определения случая: **no** — The only estimate is the STI category 'phonophobia/misophonia', which is not specific to misophonia (E2). — Page 10 — «15% phonophobia/misophonia»
7. единое надёжное измерение: **unclear** — The same interview was used for everyone, but its reliability for this category is not reported. — Page 10 — «with the evaluated Structured Tinnitus Interview (STI, Goebel and Hiller, 2002)»
8. статистика (числитель и знаменатель): **unclear** — Only a rounded percentage is given. The numerator has to be derived (15% x 216 = 32.4), and the categories add up to 99.4%. — Page 10 — «60% HC; 15% phonophobia/misophonia; 24.4% without HC»
9. отклик: **unclear** — Retrospective record evaluation; the number of eligible patients and the response rate are not reported. — Page 10 — «We retrospectively evaluated 216 tinnitus-inpatients»

Правки:
- 

Проверено: да
### ST047-2 · Sanfins et al.: schoolchildren, Brazil, n=60 (parent online questionnaire)
Отчёты: R0629 (main; poster 'What would be the factors linked to hyperacusia in schools?', Sanfins M.D. et al.)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · annoyance from certain sounds (any; ad hoc questionnaire item) | **L0** | **29 / 60** | 48.3 | Page 24, Results | «The findings of the current study revealed that 48% of the students assessed experience annoyance from certain sounds» |
| E2 | all | adhoc · auditory hypersensitivity / sound intolerance (ad hoc; compared with parents' opinion) | **E2** | **5 / 60** | 8.3 | Page 24, Results and Conclusions | «revealed that 8.3% of children exhibited hypersensitivity ... The findings indicated that 8.3% of schoolchildren have a sound intolerance.» |

- E1: источник порога: study's own; правило: adhoc row; L0 any bothersome sound; у авторов: «experience annoyance from certain sounds»; главная у авторов: no; период: NR; **расчёт: 48% x 60 = 28.8 -> 29**; заметка: Parent and/or child report (unclear). Not specific to misophonia; L0, listed, not pooled.
- E2: источник порога: study's own; правило: adhoc row; G9 not misophonia-specific (general sound intolerance/hyperacusis); у авторов: «sound intolerance / hypersensitivity»; главная у авторов: yes; период: NR; **расчёт: 8.3% x 60 = 4.98 -> 5**; заметка: Parent report combined with the child's self-perception. The definition is framed as hyperacusis/sound intolerance, not misophonia.

**Ключевые поля выборки:**
- **n_analysed: 60** — Page 23, Methods — «involving the evaluation of 60 youngsters of both genders»
- **population: school_pupils** — Page 23, Objectives — «examine the occurrence of sound intolerance and identify the related factors in school-aged children»
- **sampling: NR** — Page 23, Methods — «involving the evaluation of 60 youngsters of both genders»

**Остальные поля:**
- clinical_group: NA — Page 23 — «school-aged children»
- country: BRA — Page 23, affiliations — «1 Department of Audiology and Speech Pathology, Universidade Federal de São Paulo (UNIFESP), São Paulo, Brazil»
- setting: school (schoolchildren; questionnaire completed by parents online) — Page 23, Objectives/Methods — «identify the related factors in school-aged children ... completed by parents and/or guardians via the virtual platform»
- data_years: NR — Page 23 — «conducted as a cross-sectional, prospective, and descriptive observational study»
- design: cross-sectional — Page 23, Methods — «The present investigation was conducted as a cross-sectional, prospective, and descriptive observational study»
- topic_disclosed: NR — Page 24 — «The inquiries centered on sociodemographic information on past and present health, as well as auditory well-being.»
- inclusion_exclusion: School-aged children; no criteria reported — Page 23, Methods — «involving the evaluation of 60 youngsters of both genders»
- n_invited: NR — Page 23 — «involving the evaluation of 60 youngsters of both genders»
- n_responded: 60 — Page 23, Methods — «involving the evaluation of 60 youngsters of both genders»
- response_rate: NR — Page 23 — «involving the evaluation of 60 youngsters»
- age_mean: NR — Page 23 — «school-aged children»
- age_sd: NR — Page 23 — «school-aged children»
- age_min: NR — Page 23 — «school-aged children»
- age_max: NR — Page 23 — «school-aged children»
- age_group: NR — Page 23 — «school-aged children»
- pct_female: NR — Page 23 — «60 youngsters of both genders»
- informant: mixed — Page 23-24, Methods — «completed by parents and/or guardians via the virtual platform ... the children were also inquired about their self-perception of tinnitus, hearing, and hypers…»
- mode: online — Page 23, Methods — «completed by parents and/or guardians via the virtual platform»
- instruments: Ad hoc parent questionnaire on sound annoyance and hypersensitivity (language version NR); no misophonia measure — Page 23, Methods — «The evaluation was conducted via a questionnaire that was completed by parents and/or guardians via the virtual platform.»
- instrument_validated_in_language: NR — Page 23 — «via a questionnaire»
- pub_status: conference — Page 1 — «The “Journal of Hearing Science” is pleased to publish the abstracts submitted for the 7th International Conference on Hyperacusis and Misophonia»
- language: English — Page 23 — «involving the evaluation of 60 youngsters of both genders»
- funding_coi: NR — Page 23-24 — «NR»
- notes: Conference poster abstract about hyperacusis and sound intolerance. Misophonia is not named. Its eligibility is doubtful and the reviewer should confirm it. Only L0 and E2 estimates are available. Parents and/or guardians completed the questionnaire, and the children were also asked, so the informant for each estimate is unclear. An extra figure ('in 15% of them, the discomfort is triggered by more than five auditory stimuli') was not extracted because its denominator is ambiguous.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — The sampling frame (schools, catchment) is not described. — Page 23 — «involving the evaluation of 60 youngsters of both genders»
2. способ отбора: **unclear** — The sampling method is not described. — Page 23 — «involving the evaluation of 60 youngsters of both genders»
3. размер выборки: **no** — n=60 is below 385. — Page 23 — «60 youngsters»
4. описание выборки и условий: **no** — Age, sex distribution and dates are not reported. — Page 23 — «60 youngsters of both genders»
5. охват (пропуски): **unclear** — Missing data are not reported. — Page 23 — «involving the evaluation of 60 youngsters»
6. валидность определения случая: **no** — Ad hoc items about sound annoyance or hypersensitivity; not specific to misophonia. — Page 24 — «8.3% of children exhibited hypersensitivity»
7. единое надёжное измерение: **unclear** — Same online questionnaire for all, but the informant mix (parent or child) is unclear and no reliability is reported. — Page 23-24 — «completed by parents and/or guardians ... the children were also inquired»
8. статистика (числитель и знаменатель): **unclear** — Only percentages are given. The counts have to be derived, and 48% of 60 is not an integer. — Page 24 — «48% of the students assessed experience annoyance from certain sounds»
9. отклик: **unclear** — The number invited and the response rate are not reported. — Page 23 — «60 youngsters»

Правки:
- 

Проверено: да
---

## ST048 · Sujeeth 2024 · Indian journal of otolaryngology and head and neck surgery : official publicati…

Основной отчёт R0636: [текст](../../fulltext/text/R0636.txt) · [PDF](../../fulltext/pdf/R0636.pdf) — «Estimation of Prevalence of Misophonia Among High School Students in India.» — [DOI](https://doi.org/10.1007/s12070-023-04382-0)
Расхождения в тексте: (1) The headline 34.67% (abstract and results) equals (109+94+4)/597 = 207/597, so it includes the mild band. The methods, however, say mild cases were only 'at risk' and that 'moderate and above' count as misophonia. Moderate or more = 98/597 = 16.4% is not reported as a percentage. (2) The severity percentages (52.65% mild, 45.41% moderate, 1.93% severe) are shares of the 207 cases (109/207, 94/207, 4/207), not of the 597 students, although the abstract wording suggests otherwise. (3) Bands have a gap: sub-clinical '<10' and mild '11-21' leave score 10 unassigned. (4) Age: the text gives both 'mean age was 15 years' and 'the mean was 15.12', with SD = 5, which is implausible for an age range of 14-16. (5) The Discussion compares this all-severity prevalence with the 15.85% moderate-to-severe prevalence among college students, which is not a like-for-like comparison. Table 1 counts add…
Заметка ИИ: Single-sample school study using MAQ version B bands. The L1 estimate (>=11) is the authors' headline; the L2 estimate (>=22) uses an unanchored band cut-off (JBI 6 = no). Sampling frame, recruitment, response rate, data years and the MAQ language version are not reported.

### ST048-1 · High school students, India, n=597 (MAQ)
Отчёты: R0636 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MAQ · MAQ>=11 (mild or more; report bands: sub-clinical <10, mild 11-21, moderate 22-42, severe 43-63) | **L1** | **207 / 597** | 34.7 | Page 2, Table 1; Results; Abstract | «approximately 34.67% of the participants exhibiting symptoms of this disorder ... Mild Misophonia 62 47 109 Moderate Misophonia 50 44 94 Severe Misophonia 02 02 4» |
| E2 | all | MAQ · MAQ>=22 (moderate or more) | **L2** | **98 / 597** | 16.4 | Page 2, Method; Table 1 | «individuals with moderate and above degrees were considered as individuals with misophonia ... Moderate Misophonia 50 44 94 Severe Misophonia 02 02 4» |
| E3 | all | MAQ · MAQ>=43 (severe) | **L2** | **4 / 597** | 0.7 | Page 2, Table 1 | «Severe Misophonia 02 02 4» |
| E4 | male | MAQ · MAQ>=11 (mild or more) | **L1** | **114 / 328** | 34.8 | Page 2, Table 1 | «Mild Misophonia 62 47 109 Moderate Misophonia 50 44 94 Severe Misophonia 02 02 4 Total 328 269 597» |
| E5 | female | MAQ · MAQ>=11 (mild or more) | **L1** | **93 / 269** | 34.6 | Page 2, Table 1 | «Mild Misophonia 62 47 109 Moderate Misophonia 50 44 94 Severe Misophonia 02 02 4 Total 328 269 597» |
| E6 | male | MAQ · MAQ>=22 (moderate or more) | **L2** | **52 / 328** | 15.9 | Page 2, Table 1 | «Moderate Misophonia 50 44 94 Severe Misophonia 02 02 4 Total 328 269 597» |
| E7 | female | MAQ · MAQ>=22 (moderate or more) | **L2** | **46 / 269** | 17.1 | Page 2, Table 1 | «Moderate Misophonia 50 44 94 Severe Misophonia 02 02 4 Total 328 269 597» |
| E8 | male | MAQ · MAQ>=43 (severe) | **L2** | **2 / 328** | 0.6 | Page 2, Table 1 | «Severe Misophonia 02 02 4» |
| E9 | female | MAQ · MAQ>=43 (severe) | **L2** | **2 / 269** | 0.7 | Page 2, Table 1 | «Severe Misophonia 02 02 4» |

- E1: источник порога: developer paper; правило: MAQ row, version B, L1 >=11; G1 sum of bands; у авторов: «prevalence of misophonia (includes mild; methods call mild 'at risk')»; главная у авторов: yes; период: NR; **расчёт: 109 + 94 + 4 from Table 1 = 207; 207/597 = 34.67%, matching the reported value**; заметка: Headline estimate in the abstract and results. The methods say only moderate or above counts as misophonia, which contradicts the headline. A score of 10 is unassigned in the bands. Source of the bands not cited (attributed to MAQ by Johnson/Dozier).
- E2: источник порога: developer paper; правило: MAQ row, version B, L2 >=22; G1 sum of bands; у авторов: «individuals with misophonia (moderate and above)»; главная у авторов: no; период: NR; **расчёт: 94 + 4 from Table 1 = 98; 98/597 = 16.4%**; заметка: This matches the authors' definition of misophonia in the methods, but they do not report it as a percentage. Band cut-off not anchored (JBI 6 = no; excluded in sensitivity analysis 2).
- E3: источник порога: developer paper; правило: MAQ row, version B; G2 threshold above L2 cut-off -> L2; G1 top band is cumulative; у авторов: «Severe misophonia»; главная у авторов: no; период: NR; заметка: The reported 1.93% severe is 4/207 (a share of cases), not of the sample; 4/597 = 0.67%.
- E4: источник порога: developer paper; правило: MAQ row, version B, L1 >=11; G1 sum of bands; у авторов: «prevalence of misophonia»; главная у авторов: no; период: NR; **расчёт: 62 + 50 + 2 from Table 1 (males) = 114**; заметка: First column = males.
- E5: источник порога: developer paper; правило: MAQ row, version B, L1 >=11; G1 sum of bands; у авторов: «prevalence of misophonia»; главная у авторов: no; период: NR; **расчёт: 47 + 44 + 2 from Table 1 (females) = 93**; заметка: Second column = females.
- E6: источник порога: developer paper; правило: MAQ row, version B, L2 >=22; G1 sum of bands; у авторов: «individuals with misophonia (moderate and above)»; главная у авторов: no; период: NR; **расчёт: 50 + 2 from Table 1 (males) = 52**
- E7: источник порога: developer paper; правило: MAQ row, version B, L2 >=22; G1 sum of bands; у авторов: «individuals with misophonia (moderate and above)»; главная у авторов: no; период: NR; **расчёт: 44 + 2 from Table 1 (females) = 46**
- E8: источник порога: developer paper; правило: MAQ row, version B; G2 above L2 cut-off -> L2; у авторов: «Severe misophonia»; главная у авторов: no; период: NR
- E9: источник порога: developer paper; правило: MAQ row, version B; G2 above L2 cut-off -> L2; у авторов: «Severe misophonia»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 597** — Page 2, Table 1 — «Total 328 269 597»
- **population: school_pupils** — Page 2, Method — «597 high school students with diverse backgrounds»
- **sampling: NR** — Page 2, Method — «The number of participants included in the study was 597 high school students with diverse backgrounds.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: IND — Page 1, Abstract — «aiming to shed light on the unique challenges faced by this demographic in India»
- setting: school (high schools; schools and city not named; study conducted at All India Institute of Speech and Hearing, Mysore) — Page 2, Method; Page 3, Acknowledgements — «The number of participants included in the study was 597 high school students with diverse backgrounds.»
- data_years: NR — Page 2, Method — «NR»
- design: cross-sectional — Page 2, Introduction — «This study aims to fill this research gap by investigating the prevalence, gender differences, and severity of misophonia in high school students in India.»
- topic_disclosed: NR — Page 3, Compliance with Ethical Standards — «All the procedures were explained to the participants, and informed consent was taken from all the participants of the study.»
- inclusion_exclusion: High school students aged 14-16; no history or signs of psychological or otological problems; not on medication — Page 2, Method — «The participants did not have any history or signs and symptoms of psychological or otological problems; neither were under medications.»
- n_invited: NR — Page 2, Method — «NR»
- n_responded: NR — Page 2, Method — «NR»
- response_rate: NR — Page 2, Method — «NR»
- age_mean: 15 — Page 2, Method — «the mean age was 15 years, the SD = 5, the mean was 15.12»
- age_sd: 5 — Page 2, Method — «the mean age was 15 years, the SD = 5»
- age_min: 14 — Page 2, Method — «The age range of participants was 14 to 16 years.»
- age_max: 16 — Page 2, Method — «The age range of participants was 14 to 16 years.»
- age_group: adolescents — Page 2, Method — «The age range of participants was 14 to 16 years.»
- pct_female: 45.06 — Page 2, Table 1 — «Males Females Total ... Total 328 269 597»
- informant: self — Page 2, Method — «The questionnaire was self-administered with the assistance of parents or caregivers.»
- mode: paper — Page 2, Method — «Every student was provided with a copy of the questionnaire. They were instructed to read questions carefully and mark their answers (frequency of problems) in…»
- instruments: MAQ (Misophonia Assessment Questionnaire, Johnson, revised by Dozier 2013; 21 items 0-3; language version not stated) — Page 2, Method — «The Misophonia Assessment Questionnaire (MAQ) by Dr. Marsha Johnson, revised by Tom Dozier, 2013 was administered to all the participants.»
- instrument_validated_in_language: NR — Page 2, Method — «The MAQ questionnaire has 21 questions, with four descriptive options corresponding to the score»
- pub_status: journal — Page 1, header — «Indian Journal of Otolaryngology and Head & Neck Surgery (2024) 76:1678–1681»
- language: English — Full text — «Estimation of Prevalence of Misophonia Among High School Students in India»
- funding_coi: No funding; authors report no conflicts of interest — Page 3, Funding; Conflict of Interest — «There is no funding by any agency for the manuscript. ... The authors report no conflicts of interest.»
- notes: pct_female computed as 269/597. Age reporting is contradictory: 'mean age was 15 years, the SD = 5, the mean was 15.12'. SD 5 is implausible for an age range of 14-16. Students completed the questionnaire with help from parents or caregivers. The MAQ language version (English or translation) is not stated. The MAQ bands leave a score of 10 unassigned (sub-clinical <10, mild 11-21). The paper does not cite a source for the bands. The bands match version B in Table 1 (mild/moderate 22/severe 43). Same research group (Prabhu) as the Indian college-student studies (Aryal & Prabhu 2022; Patel et a…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — The target is high school students in India, but the sampling frame (which schools, how they were chosen) is not described. — Page 2, Method — «The number of participants included in the study was 597 high school students with diverse backgrounds.»
2. способ отбора: **unclear** — The method of selecting participants is not described. — Page 2, Method — «The number of participants included in the study was 597 high school students with diverse backgrounds.»
3. размер выборки: **yes** — n=597 >= 385. — Page 2, Table 1 — «Total 328 269 597»
4. описание выборки и условий: **unclear** — Age, sex, country and school setting are reported; the dates of data collection are missing. — Page 2, Method — «Among 597 students, the number of female students was 269 ... The age range of participants was 14 to 16 years.»
5. охват (пропуски): **unclear** — Missing data and exclusions are not reported; all 597 appear in Table 1, but the number approached is unknown. — Page 2, Table 1 — «Total 328 269 597»
6. валидность определения случая: **no** — The L2 definition (MAQ >=22, moderate band) is a severity-band cut-off without anchoring. The authors' headline estimate is MAQ >=11 (L1 band). The language version and its validation are not reported. — Page 2, Method — «grouped based on their scores as Sub-clinical (score < 10), Mild (score 11–21), Moderate (22–42), or Severe (43–63)»
7. единое надёжное измерение: **unclear** — The same instrument, paper mode and bands were used for everyone. Parental assistance varied, and no reliability is reported. — Page 2, Method — «The questionnaire was self-administered with the assistance of parents or caregivers.»
8. статистика (числитель и знаменатель): **yes** — Table 1 gives counts by band and sex with the denominator; CIs are calculable (none reported). — Page 2, Table 1 — «No Misophonia 214 176 390 Mild Misophonia 62 47 109 Moderate Misophonia 50 44 94 Severe Misophonia 02 02 4»
9. отклик: **unclear** — The number invited and the response rate are not reported. — Page 2, Method — «The number of participants included in the study was 597 high school students»

Правки:
- 

Проверено: да
---

## ST049 · White 2024 · University of Tasmania

Основной отчёт R0651: [текст](../../fulltext/text/R0651.txt) · [PDF](../../fulltext/pdf/R0651.pdf) — «Could you sit still? Misokinesia, study preference and comorbidity with misophonia» — [DOI](https://doi.org/10.25959/25698009)
Расхождения в тексте: Misophonia counts in Table 1 match the text (47/185 = 25.4%). The age bands add to 47/185 and gender to 47/185 (41+2+4). Errors in the report, all outside the misophonia counts: (1) The female misokinesia rate is printed as 17 (14.8%), but 17/145 = 11.7%. The Discussion says 12% of females, and gives the whole-sample misokinesia rate as 10.3% where Table 1 has 10.2%. (2) Some SMpS SD cells in Table 1 (OCD, Anxiety, Depression, all age bands) repeat the SMkS SD and have no SMpS mean, so they look like table errors. (3) The 41-50 misophonia rate is printed as 17%; 3/17 = 17.6%. (4) The text says 'six $50 gift vouchers' (p.12), but the information sheet says 'one of ten $50 gift cards' (p.51). (5) The odds ratio is given as 144 times in the text (p.19) and 108 times in the Discussion, while OR = 189.53. These are misokinesia figures and are not used.
Заметка ИИ: One sample was extracted: an Honours thesis (University of Tasmania, 2023). Misophonia was defined by SMS-Adult Part 2 >=51 (L2), with subgroup estimates by gender, student status, self-reported diagnosis and age band. The study's main aim was misokinesia. Data collection years are not reported. The survey was shared with a second Honours project (Jessica Coad), so another report on the same data may exist.

### ST049-1 · University of Tasmania students and public volunteers, online survey, Australia, n=185
Отчёты: R0651 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SMS-Adult · SMS Part 2 >=51 (passing threshold 50.5) | **L2** | **47 / 185** | 25.4 | Page 22, Table 1; Page 28-29, Discussion | «Whole Sample 185 (100%) 19 (10.2%) 47 (25.4%)» |
| E2 | female | SMS-Adult · SMS Part 2 >=51 | **L2** | **41 / 145** | 28.3 | Page 22, Table 1 | «Female 145 (78%) 17 (14.8%) 41 (28.3%)» |
| E3 | male | SMS-Adult · SMS Part 2 >=51 | **L2** | **2 / 35** | 5.7 | Page 22, Table 1 | «Male 35 (19%) 1 (3.7%) 2 (5.7%)» |
| E4 | non-binary | SMS-Adult · SMS Part 2 >=51 | **L2** | **4 / 5** | 80.0 | Page 22, Table 1 | «Non-binary 5 (3%) 1 (20%) 4 (80%)» |
| E5 | university students | SMS-Adult · SMS Part 2 >=51 | **L2** | **40 / 148** | 27.0 | Page 22, Table 1 | «Student 148 (80%) 16 (10.8%) 40 (27%)» |
| E6 | non-students | SMS-Adult · SMS Part 2 >=51 | **L2** | **7 / 37** | 18.9 | Page 22, Table 1 | «Non-student 37 (20%) 3 (8.1%) 7 (18.9%)» |
| E7 | self-reported previous mental health diagnosis | SMS-Adult · SMS Part 2 >=51 | **L2** | **26 / 65** | 40.0 | Page 22, Table 1 | «Previous mental health diagnosis a 65 (35%) 14 (21.5%) 26 (40%)» |
| E8 | ADHD (self-reported diagnosis) | SMS-Adult · SMS Part 2 >=51 | **L2** | **7 / 18** | 38.9 | Page 22, Table 1 | «ADHD a 18 (10%) 7 (38.8%) 7 (38.8%)» |
| E9 | ASD (self-reported diagnosis) | SMS-Adult · SMS Part 2 >=51 | **L2** | **7 / 8** | 87.5 | Page 22, Table 1 | «ASD a 8 (4%) 4 (50%) 7 (87.5%)» |
| E10 | OCD (self-reported diagnosis) | SMS-Adult · SMS Part 2 >=51 | **L2** | **2 / 5** | 40.0 | Page 22, Table 1 | «OCD a 5 (3%) 2 (40%) 2 (40%)» |
| E11 | anxiety (self-reported diagnosis) | SMS-Adult · SMS Part 2 >=51 | **L2** | **17 / 37** | 45.9 | Page 22, Table 1 | «Anxiety a 37 (20%) 9 (24.3%) 17 (45.9%» |
| E12 | depression (self-reported diagnosis) | SMS-Adult · SMS Part 2 >=51 | **L2** | **11 / 26** | 42.3 | Page 22, Table 1 | «Depression a 26 (14%) 5 (19.2%) 11 (42.3%)» |
| E13 | 18-30 | SMS-Adult · SMS Part 2 >=51 | **L2** | **34 / 129** | 26.4 | Page 22, Table 1 | «18 - 30 129 (70%) 12 (9%) 34 (26.3%)» |
| E14 | 31-40 | SMS-Adult · SMS Part 2 >=51 | **L2** | **8 / 28** | 28.6 | Page 22, Table 1 | «31 - 40 28 (15%) 4 (14%) 8 (28.6%)» |
| E15 | 41-50 | SMS-Adult · SMS Part 2 >=51 | **L2** | **3 / 17** | 17.6 | Page 22, Table 1 | «41 – 50 17 (9%) 1 (6%) 3 (17%)» |
| E16 | 51-60 | SMS-Adult · SMS Part 2 >=51 | **L2** | **2 / 10** | 20.0 | Page 22, Table 1 | «51 – 60 10 (5%) 2 (20%) 2 (20%)» |
| E17 | 61-99 | SMS-Adult · SMS Part 2 >=51 | **L2** | **0 / 1** | 0.0 | Page 22, Table 1 | «61 - 99 1 (1%) 0 (0%) 0 (0%)» |

- E1: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «meeting the threshold for misophonia»; главная у авторов: no; период: NR; заметка: Authors' primary outcome is misokinesia; this is the only whole-sample misophonia estimate (25.4%, n = 47).
- E2: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E3: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E4: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E5: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E6: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E7: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR; заметка: Diagnosis self-reported (optional item).
- E8: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR; заметка: Self-reported prior diagnosis.
- E9: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR; заметка: Self-reported prior diagnosis.
- E10: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR; заметка: Self-reported prior diagnosis.
- E11: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR; заметка: Self-reported prior diagnosis.
- E12: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR; заметка: Self-reported prior diagnosis.
- E13: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E14: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E15: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR; заметка: 3/17 = 17.6%; printed as 17%.
- E16: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR
- E17: источник порога: developer paper; правило: SMS-Adult row; L2 >=50.5; у авторов: «misophonia rate»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 185** — Page 17, Participants; Page 22, Table 1 — «Our final sample consisted of N = 185 participants.»
- **population: gp_other** — Page 17, Participants — «Of our sample, 148 (80%) were current university students. Undergraduate psychology students received one-hour of research credit ... Other university students and members of the public were entered into a draw»
- **sampling: convenience** — Page 19, Procedure — «Participants were recruited through social media, the School of Psychological Sciences SONA system, and through flyers placed on advertisement boards around the university campus.»

**Остальные поля:**
- clinical_group: NA — NA
- country: AUS — Page 19, Procedure; Page 32, Discussion — «Participants were recruited through social media, the School of Psychological Sciences SONA system, and through flyers placed on advertisement boards around th…»
- setting: university (University of Tasmania: SONA pool, campus flyers) plus social media (members of the public); online survey — Page 17, Participants; Page 19, Procedure — «Of our sample, 148 (80%) were current university students. ... Other university students and members of the public were entered into a draw»
- data_years: NR — Page 2, Statement of Sources — «Joshua White, (12/10/2023)»
- design: cross-sectional — Page 21, Design and Analysis — «This was a cross-sectional study with between and within subjects' variables.»
- topic_disclosed: yes — Page 56, Appendix F (Information Sheet); Page 19-20, Proced… — «You are invited to participate in a research study examining people's sensitivities to sounds and repetitive visual movements in their environments.»
- inclusion_exclusion: Aged >=18, English fluency, normal or corrected-to-normal hearing and vision; excluded: withdrew before completion (75), rescinded (1), failed attention checks (6) — Page 17, Participants — «We applied exclusion criteria which required all participants to be 18 years or older, possess English fluency, and have normal to corrected to normal hearing …»
- n_invited: NR — NA
- n_responded: 267 — Page 17, Participants — «We recruited a total of 267 participants for our study; 75 withdrew before completing the study, 1 rescinded their results, and 6 failed attention checks.»
- response_rate: NR — NA
- age_mean: 28.24 — Page 17, Participants — «Participants were aged between 18 – 64 years (M = 28.24, SD = 10.47).»
- age_sd: 10.47 — Page 17, Participants — «Participants were aged between 18 – 64 years (M = 28.24, SD = 10.47).»
- age_min: 18 — Page 17, Participants — «Participants were aged between 18 – 64 years»
- age_max: 64 — Page 17, Participants — «Participants were aged between 18 – 64 years»
- age_group: adults — Page 17, Participants — «Participants were aged between 18 – 64 years»
- pct_female: 78.4 — Page 17, Participants — «This final sample included 145 (78%) female, 35 (19%) male and 5 (3%) non-binary participants.»
- informant: self — Page 18, Materials — «This study was an online questionnaire using Qualtrics.»
- mode: online — Page 18, Materials — «This study was an online questionnaire using Qualtrics.»
- instruments: Sussex Misophonia Scale (SMS-Adult; called SMpS) Part 1 and Part 2, English; (also an adapted Sussex Misokinesia Scale, SMkS, not a misophonia measure) — Page 18, Materials — «Participants completed four sections: demographic questions, the Sussex Misophonia Scale Part 1 and Part 2 by Rinaldi et al. (2021), and a modified version of …»
- instrument_validated_in_language: yes — Page 16, Rationale and Aims; Page 18-19, Materials — «a more recent, psychometrically validated misophonia scale called the Sussex Misophonia Scale (SMS) (Rinaldi et al., 2021)»
- pub_status: thesis — Page 1, title page — «A report submitted as a partial requirement for the degree of Bachelor of Psychological Sciences with Honours at the University of Tasmania, 2023.»
- language: English — Whole report — «Could you sit still? Misokinesia, study preference and comorbidity with misophonia»
- funding_coi: Funded by the School of Psychological Sciences, College of Health and Medicine, University of Tasmania; COI not reported — Page 56, Appendix F — «The study is funded by the School of Psychological Sciences – College of Health and Medicine, at the University of Tasmania.»
- notes: Honours thesis. The main focus is misokinesia (SMkS >=51: 19/185); misokinesia estimates are not extracted. Data collection dates are not stated (thesis dated 12/10/2023). Possible overlap: the same survey served two Honours projects (Joshua White and Jessica Coad, Appendix F), so check for a Coad 2023 thesis on the same data. Recruitment flyers did not mention misophonia, but the information sheet shown before consent named sensitivities to sounds and visual movements; topic_disclosed is coded yes on that basis. SMS Part 1 was collected, but the case definition uses only the Part 2 score (>=…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is SONA pool, campus flyers and social media; covers only part of university students or the general population — Page 19, Procedure — «Participants were recruited through social media, the School of Psychological Sciences SONA system, and through flyers placed on advertisement boards around th…»
2. способ отбора: **no** — Volunteer convenience sampling — Page 19, Procedure — «Participants were recruited through social media, the School of Psychological Sciences SONA system, and through flyers»
3. размер выборки: **no** — n = 185 < 385 — Page 17, Participants — «Our final sample consisted of N = 185 participants.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country (University of Tasmania) reported; dates of data collection missing — Page 17, Participants — «Participants were aged between 18 – 64 years (M = 28.24, SD = 10.47).»
5. охват (пропуски): **no** — 82 of 267 recruited (31%) excluded, 75 for withdrawing before completion; not handled — Page 17, Participants — «We recruited a total of 267 participants for our study; 75 withdrew before completing the study, 1 rescinded their results, and 6 failed attention checks. Thes…»
6. валидность определения случая: **yes** — SMS-Adult Part 2 >=50.5 (score >=51), English original version — Page 18-19, Materials — «A passing threshold for misophonia is 50.5, meaning a score of 51 or higher is indicative of misophonia (Rinaldi et al., 2021).»
7. единое надёжное измерение: **yes** — Same online instrument and threshold for all; scale described as psychometrically validated in its source (reliability not reported in this sample; reviewer to check source) — Page 16, Rationale and Aims; Page 21, Design and Analysis — «we categorised participants with scores greater than or equal to 51 on the SMpS and SMkS as having misophonia or misokinesia respectively.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (47/185); CI not given but calculable — Page 22, Table 1 — «Whole Sample 185 (100%) 19 (10.2%) 47 (25.4%)»
9. отклик: **no** — Open recruitment with no denominator of invited people; no non-response handling — Page 19, Procedure — «Participants were directed to the Qualtrics survey via a hyperlink (SONA, social media) or QR code (flyer).»

Правки:
- 

Проверено: да
---

## ST050 · ÇEVİK 2024 · KTO Karatay University Institutional Archive

Основной отчёт R0664: [текст](../../fulltext/text/R0664.txt) — «Yetişkinlerde Hiperakuzi, Mizofoni Ve Fonofobinin Sosyo-Demografik Değişkenler Açısından İncelenmesi: Konya Örneği»
Расхождения в тексте: 1) Percent female: 62.3% in Tablo 11 but 62.2% in the Discussion (p. 97); the table value is used. 2) Age: the text and the Özet give 18-65 and Tablo 11 gives a 41-65 band, but the questionnaire form (Ek 2) shows the option '41-60'. 3) Tablo 54 is titled 'Yaş Grupları' (age groups) but reports place of residence, and its Genel total row gives 'Yok 21,2%' against 21.5% elsewhere. 4) Tablo 61 (phonophobia × hearing loss) repeats the numbers of Tablo 59 (hyperacusis). Not used here. 5) In Tablo 41 (ANOVA) the Factor 1 and Factor 2 rows repeat the 'Genel' means. Not used here. 6) The text under Tablo 48 refers to 'Fonofobi' (phonophobia) in a misophonia table. 7) Factor labels do not match item content: Factor 1 'Duygusal' (emotional) holds the impairment items M1-M5, and Factor 2 'Fonksiyonel/Sosyal' (functional/social) holds the reaction items M6-M14. 8) The text applies the ≥4 cut-off to…
Заметка ИИ: The main estimate is DSTS-S (ASTÖ-T) misophonia ≥4: 314/400 (78.5%), level L1, rated JBI 6 = no. Factor-subscale estimates are coded L1 under rule G3. The recall period is 'son 7 gün' (last 7 days), coded 'current'. The PDF has no '=== Page N ===' markers, so locations use the thesis's printed page numbers.

### ST050-1 · Online community adults, Konya, Türkiye (n=400)
Отчёты: R0664 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **314 / 400** | 78.5 | p. 58, Tablo 21 | «Mizofoni Var 314 78,5 Yok 86 21,5 Toplam 400 100,0» |
| E2 | female | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **208 / 249** | 83.5 | p. 66, Tablo 30 (Genel) | «Genel Kadın n 41 208 249 % 16,5 83,5» |
| E3 | male | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **106 / 151** | 70.2 | p. 66, Tablo 30 (Genel) | «Erkek n 45 106 151 % 29,8 70,2» |
| E4 | 18-25 | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **133 / 163** | 81.6 | p. 74, Tablo 42 (Genel) | «Genel 18-25 n 30 133 163 % 18,4 81,6» |
| E5 | 26-40 | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **85 / 112** | 75.9 | p. 74, Tablo 42 (Genel) | «26-40 n 27 85 112 % 24,1 75,9» |
| E6 | 41-65 | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **96 / 125** | 76.8 | p. 74, Tablo 42 (Genel) | «41-65 n 29 96 125 % 23,2 76,8» |
| E7 | self-reported doctor-diagnosed hearing loss | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **22 / 26** | 84.6 | p. 94, Tablo 63 (Genel) | «Genel Var n 4 22 26 % 15,4 84,6» |
| E8 | no self-reported hearing loss | DSTS-S · DSTS-S misophonia subscale total ≥4 | **L1** | **292 / 374** | 78.1 | p. 94, Tablo 63 (Genel) | «Yok n 82 292 374 % 21,9 78,1» |
| E9 | all | DSTS-S · DSTS-S misophonia Factor 1 ('Duygusal Yakınmalar', items M1-M5) ≥4 | **L1** | **169 / 400** | 42.2 | p. 66, Tablo 30 (Faktör 1) | «Faktör 1 (Duygusal Yakınmalar) ... Toplam n 231 169 400 % 57,8 42,3» |
| E10 | female | DSTS-S · DSTS-S misophonia Factor 1 ≥4 | **L1** | **120 / 249** | 48.2 | p. 66, Tablo 30 (Faktör 1) | «Kadın n 129 120 249 % 51,8 48,2» |
| E11 | male | DSTS-S · DSTS-S misophonia Factor 1 ≥4 | **L1** | **49 / 151** | 32.5 | p. 66, Tablo 30 (Faktör 1) | «Erkek n 102 49 151 % 67,5 32,5» |
| E12 | 18-25 | DSTS-S · DSTS-S misophonia Factor 1 ≥4 | **L1** | **75 / 163** | 46.0 | p. 74, Tablo 42 (Faktör 1) | «18-25 n 88 75 163 % 54,0 46,0» |
| E13 | 26-40 | DSTS-S · DSTS-S misophonia Factor 1 ≥4 | **L1** | **41 / 112** | 36.6 | p. 74, Tablo 42 (Faktör 1) | «26-40 n 71 41 112 % 63,4 36,6» |
| E14 | 41-65 | DSTS-S · DSTS-S misophonia Factor 1 ≥4 | **L1** | **53 / 125** | 42.4 | p. 74, Tablo 42 (Faktör 1) | «41-65 n 72 53 125 % 57,6 42,4» |
| E15 | self-reported doctor-diagnosed hearing loss | DSTS-S · DSTS-S misophonia Factor 1 ≥4 | **L1** | **15 / 26** | 57.7 | p. 94, Tablo 63 (Faktör 1) | «Faktör 1 (Duygusal Yakınmalar) Var n 11 15 26 % 42,3 57,7» |
| E16 | no self-reported hearing loss | DSTS-S · DSTS-S misophonia Factor 1 ≥4 | **L1** | **154 / 374** | 41.2 | p. 94, Tablo 63 (Faktör 1) | «Yok n 220 154 374 % 58,8 41,2» |
| E17 | all | DSTS-S · DSTS-S misophonia Factor 2 ('Fonksiyonel/Sosyal Yakınmalar', items M6-M14) ≥4 | **L1** | **306 / 400** | 76.5 | p. 66, Tablo 30 (Faktör 2) | «Faktör 2 (Fonksiyonel/Sosyal Yakınmalar) ... Toplam n 94 306 400 % 23,5 76,5» |
| E18 | female | DSTS-S · DSTS-S misophonia Factor 2 ≥4 | **L1** | **202 / 249** | 81.1 | p. 66, Tablo 30 (Faktör 2) | «Kadın n 47 202 249 % 18,9 81,1» |
| E19 | male | DSTS-S · DSTS-S misophonia Factor 2 ≥4 | **L1** | **104 / 151** | 68.9 | p. 66, Tablo 30 (Faktör 2) | «Erkek n 47 104 151 % 31,1 68,9» |
| E20 | 18-25 | DSTS-S · DSTS-S misophonia Factor 2 ≥4 | **L1** | **129 / 163** | 79.1 | p. 74, Tablo 42 (Faktör 2) | «18-25 n 34 129 163 % 20,9 79,1» |
| E21 | 26-40 | DSTS-S · DSTS-S misophonia Factor 2 ≥4 | **L1** | **82 / 112** | 73.2 | p. 74, Tablo 42 (Faktör 2) | «26-40 n 30 82 112 % 26,8 73,2» |
| E22 | 41-65 | DSTS-S · DSTS-S misophonia Factor 2 ≥4 | **L1** | **95 / 125** | 76.0 | p. 74, Tablo 42 (Faktör 2) | «41-65 n 30 95 125 % 24,0 76,0» |
| E23 | self-reported doctor-diagnosed hearing loss | DSTS-S · DSTS-S misophonia Factor 2 ≥4 | **L1** | **22 / 26** | 84.6 | p. 94, Tablo 63 (Faktör 2) | «Faktör 2 (Fonksiyonel/ Sosyal Yakınmalar) Var n 4 22 26 % 15,4 84,6» |
| E24 | no self-reported hearing loss | DSTS-S · DSTS-S misophonia Factor 2 ≥4 | **L1** | **284 / 374** | 75.9 | p. 94, Tablo 63 (Faktör 2) | «Yok n 90 284 374 % 24,1 75,9» |

- E1: источник порога: developer paper; правило: DSTS-S row; L1 ≥4 developers' screening cut-off; у авторов: «Mizofonisi olan [has misophonia]»; главная у авторов: yes; период: current; заметка: 78.5%. Items refer to the last 7 days ('son 7 gününüzü düşünerek').
- E2: источник порога: developer paper; правило: DSTS-S row; L1 ≥4; у авторов: «Mizofoni Var»; главная у авторов: no; период: current
- E3: источник порога: developer paper; правило: DSTS-S row; L1 ≥4; у авторов: «Mizofoni Var»; главная у авторов: no; период: current
- E4: источник порога: developer paper; правило: DSTS-S row; L1 ≥4; у авторов: «Mizofoni Var»; главная у авторов: no; период: current
- E5: источник порога: developer paper; правило: DSTS-S row; L1 ≥4; у авторов: «Mizofoni Var»; главная у авторов: no; период: current
- E6: источник порога: developer paper; правило: DSTS-S row; L1 ≥4; у авторов: «Mizofoni Var»; главная у авторов: no; период: current; заметка: Top age option on the questionnaire form reads '41-60'.
- E7: источник порога: developer paper; правило: DSTS-S row; L1 ≥4; у авторов: «Mizofoni Var»; главная у авторов: no; период: current; заметка: Hearing loss is self-reported (diagnosed by a doctor). This group was found in the sample, not recruited for it.
- E8: источник порога: developer paper; правило: DSTS-S row; L1 ≥4; у авторов: «Mizofoni Var»; главная у авторов: no; период: current
- E9: источник порога: study's own; правило: DSTS-S row; G3 factor subscale threshold without published basis -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current; заметка: Factor 1 items are life-impact/impairment items, even though the factor is labelled 'emotional'. The ≥4 rule for the subscale is implied by the text under Tablo 30.
- E10: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current
- E11: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current
- E12: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current
- E13: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current
- E14: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current
- E15: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current
- E16: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 1)»; главная у авторов: no; период: current
- E17: источник порога: study's own; правило: DSTS-S row; G3 factor subscale threshold without published basis -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current; заметка: Factor 2 items are emotional-reaction items, even though the factor is labelled 'functional/social'.
- E18: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current
- E19: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current
- E20: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current
- E21: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current
- E22: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current
- E23: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current
- E24: источник порога: study's own; правило: DSTS-S row; G3 -> L1; у авторов: «Mizofoni Var (Faktör 2)»; главная у авторов: no; период: current

**Ключевые поля выборки:**
- **n_analysed: 400** — p. 58, Tablo 21 — «Mizofoni Var 314 78,5 Yok 86 21,5 Toplam 400 100,0»
- **population: gp_other** — p. 36-37, 3.4 — «kolayda örnekleme yöntemi ile seçilen ve gönüllü olarak ankete katılmayı kabul eden 400 kişi [400 people selected by convenience sampling who voluntarily agreed to the survey]»
- **sampling: convenience** — p. vi, Özet; p. 37, 3.4 — «Katılımcılar, kolayda örnekleme ve kartopu yöntemleri ile 18-65 yaş aralığındaki kişilerden seçilmiştir. [Participants aged 18-65 were selected by convenience sampling and snowball methods.]»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: TUR — p. 36-37, 3.4 — «Araştırma Konya ilinde yapılmıştır. [The research was conducted in Konya province.]»
- setting: community (online survey of adults living in Konya province) — p. 37, 3.5 — «Oluşturulan anket formu internet aracılığı ile katılımcılara ulaştırılmış ve cevapları alınmıştır. [The questionnaire was delivered to participants via the int…»
- data_years: NR — Whole text — «Konya, Temmuz 2024 [Konya, July 2024] (thesis date only; data collection dates not reported)»
- design: cross-sectional — p. 36, 3.2 — «Çalışmada, kişilerde bu üç rahatsızlıktan herhangi birinin bulunup bulunmadığı ve bu rahatsızlıkların sosyo-demografik değişkenlerden etkilenip etkilenmediği i…»
- topic_disclosed: yes — p. 116, Ek 2 (questionnaire instructions) — «Sayın Katılımcı; bu ölçeğin amacı seslerden rahatsız olma probleminizin belirlenmesine yardımcı olmaktır. [Dear participant, the aim of this scale is to help i…»
- inclusion_exclusion: Aged 18-65, living in Konya province, voluntarily agreed to take part; no exclusion criteria reported — p. 36-37, 3.4 — «araştırmaya dahil olma kriterine uygun 18-65 yaş aralığında olan ... gönüllü olarak ankete katılmayı kabul eden 400 kişi [400 people aged 18-65 meeting the inc…»
- n_invited: NR — p. 37, 3.4 — «gönüllü olarak ankete katılmayı kabul eden 400 kişi [400 people who voluntarily agreed to the survey]»
- n_responded: 400 — p. 52, Tablo 11 — «Cinsiyet Kadın 249 62,3 Erkek 151 37,8 Toplam 400 100,0»
- response_rate: NR — p. 37, 3.5 — «Oluşturulan anket formu internet aracılığı ile katılımcılara ulaştırılmış [The form was delivered via the internet] (number invited not reported)»
- age_mean: NR — p. 52, Tablo 11 — «Yaş 18-25 163 40,8 26-40 112 28,0 41-65 125 31,3 (age collected in bands only)»
- age_sd: NR — p. 52, Tablo 11 — «Yaş 18-25 163 40,8 26-40 112 28,0 41-65 125 31,3»
- age_min: 18 — p. vi, Özet — «18-65 yaş aralığındaki kişilerden seçilmiştir [selected from people aged 18-65]»
- age_max: 65 — p. vi, Özet — «18-65 yaş aralığındaki kişilerden seçilmiştir [selected from people aged 18-65]»
- age_group: adults — p. 52, Tablo 11 — «Yaş 18-25 163 40,8 26-40 112 28,0 41-65 125 31,3»
- pct_female: 62.3 — p. 52, Tablo 11 — «Cinsiyet Kadın 249 62,3 Erkek 151 37,8 Toplam 400»
- informant: self — p. 116, Ek 2 — «Her madde için ‘hiçbir zaman, bazen, genellikle ve her zaman’ yanıtlarından birini seçiniz. [For each item choose never, sometimes, usually or always.]»
- mode: online — p. vi, Özet — «Anket formu katılımcılara online olarak ulaştırılmış ve cevapları alınmıştır. [The questionnaire was delivered online and answers received.]»
- instruments: Decreased Sound Tolerance Scale-Screening (DSTS-S / ASTÖ-T), misophonia subscale (14 items, 0-3), Turkish original — p. 37, 3.5 — «Alluşoğlu (2022) tarafından geliştirilen ASTÖ-T ölçeği ... Mizofoni boyutunda 14 ifade bulunmaktadır. [ASTÖ-T developed by Alluşoğlu (2022) ... 14 items in the…»
- instrument_validated_in_language: yes — p. 97, Tartışma; Kaynaklar p. 106 — «Türkçe olarak geliştirilmiş ilk tarama ölçeği olan ASTÖ-T [ASTÖ-T, the first screening scale developed in Turkish]; Alluşoğlu, S., & Aksoy, S. (2022). The reli…»
- pub_status: thesis — Title page — «TEZLİ YÜKSEK LİSANS PROGRAMI ... Yüksek Lisans Tezi [Master's thesis programme ... Master's thesis]»
- language: Turkish — Whole text — «YETİŞKİNLERDE HİPERAKUZİ, MİZOFONİ VE FONOFOBİNİN SOSYO-DEMOGRAFİK DEĞİŞKENLER AÇISINDAN İNCELENMESİ: KONYA ÖRNEĞİ»
- funding_coi: NR (no funding or conflict-of-interest statement) — p. ii-v, front matter — «ETİK BEYAN ... bilimsel etik kuralları çerçevesinde elde ettiğimi [ethics declaration only; no funding statement]»
- notes: Master's thesis, KTO Karatay University, 2024. Convenience plus snowball sampling via online form. Many participants were students (23.3%) and audiologists/audiometrists (7.5%; Tablo 12). Age was collected in bands only, and the questionnaire form (Ek 2) shows the top band as '41-60' while the text says 41-65. The authors call the ≥4 cut-off 'Mizofoni var' (misophonia present); the 78.5% prevalence reflects a low screening cut-off. The cited Turkish studies (Alluşoğlu 2020 development thesis; Coşkun 2023 thesis; Kılıç et al. 2021) are separate samples, and no overlap is known. The ethics comm…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is Konya adults aged 18-65 (about 1.54 million). The frame is online, internet-reached volunteers, and it over-represents students and audiologists. — p. 36-37, 3.4 — «araştırmanın evrenini, Konya il sınırları içerisinde yaşayan ... yaklaşık 1.540.000 (TÜİK, 2024) kişi oluşturmaktadır [population: about 1,540,000 people livin…»
2. способ отбора: **no** — Convenience and snowball sampling with volunteer opt-in. — p. vi, Özet — «Katılımcılar, kolayda örnekleme ve kartopu yöntemleri ile ... seçilmiştir. [selected by convenience and snowball methods]»
3. размер выборки: **yes** — n=400 ≥ 385. — p. 58, Tablo 21 — «Mizofoni Var 314 78,5 Yok 86 21,5 Toplam 400»
4. описание выборки и условий: **unclear** — Age bands, sex, setting and country are reported; dates of data collection are missing. — p. 52, Tablo 11 — «Cinsiyet Kadın 249 62,3 Erkek 151 37,8 ... Yaş 18-25 163 40,8»
5. охват (пропуски): **yes** — All 400 respondents appear in every misophonia table, with no missing data shown. — p. 58, Tablo 21; p. 66, Tablo 30 — «Toplam n 86 314 400»
6. валидность определения случая: **no** — Primary definition is DSTS-S misophonia ≥4, a screening cut-off set for sensitivity (L1). — p. 58, text under Tablo 21 — «Mizofoni ölçeğinden aldığı toplam puan 4 ve üzerinde ise kişinin Mizofonisinin olduğu kabul edilmektedir. [Misophonia is accepted if the total score is 4 or ab…»
7. единое надёжное измерение: **yes** — Same instrument, online mode and threshold for all participants; Cronbach's alpha 0.957 in this sample. — p. 40, Tablo 2 — «Mizofoni Ölçeği (Genel) 0,957 14»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are explicit (314/400), so a CI can be calculated; no design weights are needed. — p. 58, Tablo 21 — «Mizofoni Var 314 78,5 Yok 86 21,5 Toplam 400 100,0»
9. отклик: **no** — Open online survey with no denominator of people invited; non-response is not addressed. — p. 37, 3.5 — «Oluşturulan anket formu internet aracılığı ile katılımcılara ulaştırılmış ve cevapları alınmıştır.»

Правки:
- 

Проверено: да