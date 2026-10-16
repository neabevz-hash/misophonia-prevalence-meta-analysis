# Проверка выписывания — файл 9 из 10

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

## ST081 · Ferrer-Torres 2021 · Frontiers in psychiatry

Основной отчёт R1040: [текст](../../fulltext/text/R1040.txt) — «Confinement and the Hatred of Sound in Times of COVID-19: A Molotov Cocktail for People With Misophonia.» — [DOI](https://doi.org/10.3389/fpsyt.2021.627044)
Расхождения в тексте: The abstract and Table 1 (Sep-Dec 2019) give 342 participants with 119 M+ (35%): women 82/224 (37%), men 37/118 (31%). The Results Phase II text gives 'positive in 114 of the 325 participants (35%)', which matches the Table 1 Mar-Jun 2020 column (114:211; women 79:133; men 35:78, i.e., 113 men). Both sets of figures use the same pre-August-2019 diagnoses. The 342 denominator was used because it is the full sample. The abstract calls the sample 'adults', but the minimum age is 16 and the inclusion criteria allow minors aged 16 and over. Table 1 has a typo in Advancing the visit, women M+:M- ('4.2', probably 4:2). The Discussion says 96% of M+ kept their visits; Table 1 gives 14 M+ cancellations out of 114 (about 88% kept).
Заметка ИИ: There is one eligible sample: outpatients of a medical psychology centre with mixed psychiatric and psychosomatic presentations. The study did not report how A-MISO-S was administered (self-report or clinician) or in which language. The only case definition is A-MISO-S >=5 (L1).

### ST081-1 · Medical psychology centre patients, Barcelona, ESP, n=342
Отчёты: R1040 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **119 / 342** | 34.8 | Table 1 (Sep-Dec 2019 column); Abstract | «Sample of participants (n, %) / 342 (100) ... M+: M- / 119:223 ... (%M+: %M-) / (35:65)» |
| E2 | female | A-MISO-S · A-MISO-S>=5 | **L1** | **82 / 224** | 36.6 | Table 1 (Sep-Dec 2019, Women) | «224 (65) ... M+: M- / 119:223 / 82:142 ... (37:63)» |
| E3 | male | A-MISO-S · A-MISO-S>=5 | **L1** | **37 / 118** | 31.4 | Table 1 (Sep-Dec 2019, Men) | «118 (35) ... M+: M- / 119:223 / 82:142 / 37:81 ... (31:69)» |

- E1: источник порога: developer paper; правило: A-MISO-S row; >=5 mild or more = L1 (G2); у авторов: «diagnosed with misophonia (M+)»; главная у авторов: yes; период: current; заметка: Alternative in Results Phase II: 114/325 (35%) for patients present in Mar-Jun 2020 quarter (same diagnoses, subset).
- E2: источник порога: developer paper; правило: A-MISO-S row; >=5 mild or more = L1 (G2); у авторов: «diagnosed with misophonia (M+)»; главная у авторов: no; период: current; заметка: 2020 quarter: 79/212 (37%).
- E3: источник порога: developer paper; правило: A-MISO-S row; >=5 mild or more = L1 (G2); у авторов: «diagnosed with misophonia (M+)»; главная у авторов: no; период: current; заметка: 2020 quarter: 35/113 (31%).

**Ключевые поля выборки:**
- **n_analysed: 342** — Table 1 — «Sample of participants (n, %) | 342 (100) | 224 (65) | 118 (35)»
- **population: clinical** — Results, Phase II — «only 2% of them initially went to the center to be treated for this problem since most of them (98%) were admitted due to other psychological or psychosomatic problems»
- **sampling: NR** — Materials and Methods, Subjects — «This study was carried out with a total sample of 342 people regularly attending a Medical and Psychological Center»

**Остальные поля:**
- clinical_group: mixed_psychiatric — Results, Phase II — «most of them (98%) were admitted due to other psychological or psychosomatic problems and were unaware of misophonia»
- country: ESP — Materials and Methods, Subjects — «a total sample of 342 people regularly attending a Medical and Psychological Center in the city of Barcelona (Spain)»
- setting: clinic (outpatient medical psychology centre, Barcelona) — Materials and Methods, Subjects — «342 people regularly attending a Medical and Psychological Center in the city of Barcelona (Spain)»
- data_years: 2019-2020 (A-MISO-S in diagnostic battery before August 2019; records Sep-Dec 2019 and Mar-Jun 2020) — Subjects; Phase II — «diagnostic test battery before August 2019»
- design: cross-sectional — Procedure, Phase I — «A retrospective analysis of 2RC of the participants was carried out to compare the quarter of the pandemic (March 11 to June 29, 2020) with the last quarter of…»
- topic_disclosed: NR — Materials and Methods, Subjects — «agreement to participate in the study»
- inclusion_exclusion: Incl: patients >16 y regularly attending the centre, diagnostic battery before Aug 2019, consent. Excl: <16, blind, profound deafness, refusal; those holding social gatherings/leisure outside home during confinement discarded. — Materials and Methods, Subjects — «Women and men over 16 years of age that signed (legal tutors, in the case of minors) the informed consent; diagnostic test battery before August 2019; agreemen…»
- n_invited: NR — NA
- n_responded: NR — NA
- response_rate: NR — NA
- age_mean: 44.66 — Results, Demographic data — «a mean age of 44.66 ± 14.09 years (min 16, max 89 years)»
- age_sd: 14.09 — Results, Demographic data — «a mean age of 44.66 ± 14.09 years (min 16, max 89 years)»
- age_min: 16 — Results, Demographic data — «(min 16, max 89 years)»
- age_max: 89 — Results, Demographic data — «(min 16, max 89 years)»
- age_group: mixed — Results, Demographic data; Subjects — «(min 16, max 89 years)»
- pct_female: 65.5 — Table 1 — «342 (100) | 224 (65) | 118 (35)»
- informant: self — Misophonia Scale — «The participants were classified as diagnosed with misophonia (M+ > = 5) or not (M- < = 4), according to the A-MISO-S»
- mode: NR — Misophonia Scale — «according to the A-MISO-S = Amsterdam misophonia scale (13)»
- instruments: A-MISO-S (language version not reported) — Misophonia Scale — «according to the A-MISO-S = Amsterdam misophonia scale (13)»
- instrument_validated_in_language: NR — Misophonia Scale — «according to the A-MISO-S = Amsterdam misophonia scale (13)»
- pub_status: journal — Header — «Frontiers in psychiatry; DOI: 10.3389/fpsyt.2021.627044»
- language: English — Full text — «Confinement and the Hatred of Sound in Times of COVID-19: A Molotov Cocktail for People With Misophonia»
- funding_coi: Funding NR; authors declare no commercial or financial conflict of interest — Conflict of Interest — «the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest»
- notes: The report does not say who completed the A-MISO-S (patient or clinician) or how it was given. It was part of the centre's diagnostic battery. Informant is coded 'self' only by default and may have been clinician. The abstract calls the sample 'adults', but the minimum age is 16. The main prevalence is 119/342 (Table 1, 2019 quarter). The Phase II text gives 114/325 for patients still attending in the 2020 quarter, using the same diagnoses. The M+ group was later studied in Phase II but was not recruited separately. Patients who socialised during confinement were excluded, which may have chan…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target is patients of the centre; frame = regularly attending patients, but post-hoc exclusions (socialising during confinement) and size of the patient pool not described. — Materials and Methods, Subjects — «During the study, those people who during confinement and self-confinement carried out social gatherings or leisure activities outside the family home were dis…»
2. способ отбора: **unclear** — Unclear whether all eligible patients were included (census) or only consenting volunteers; numbers of eligible/refusing not given. — Materials and Methods, Subjects — «a total sample of 342 people regularly attending a Medical and Psychological Center»
3. размер выборки: **yes** — Clinical sample n=342 >= 139 (but below 385, the general threshold; reviewer to confirm which applies). — Table 1 — «Sample of participants (n, %) | 342 (100)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Results, Demographic data — «The sample of 342 participants had a 65:35 W: M ratio and a mean age of 44.66 ± 14.09 years»
5. охват (пропуски): **yes** — All 342 classified M+ or M- (119+223). — Table 1 — «M+: M- | 119:223»
6. валидность определения случая: **no** — Primary definition A-MISO-S >=5 is a severity-band cut-off without anchoring (L1); language version validation not reported. — Misophonia Scale — «classified as diagnosed with misophonia (M+ > = 5) or not (M- < = 4), according to the A-MISO-S»
7. единое надёжное измерение: **unclear** — Same instrument and threshold for all, but mode not reported and no reliability reported. — Misophonia Scale — «according to the A-MISO-S = Amsterdam misophonia scale (13)»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given (119/342); CI calculable. — Table 1 — «M+: M- | 119:223 | 82:142 | 37:81»
9. отклик: **unclear** — Participation/refusal numbers not reported. — Materials and Methods, Subjects — «agreement to participate in the study»

Правки:
- 

Проверено: да
---

## ST082 · Jaswal 2021 · Scientific reports

Основной отчёт R1056: [текст](../../fulltext/text/R1056.txt) — «Misokinesia is a sensitivity to seeing others fidget that is prevalent in the general population.» — [DOI](https://doi.org/10.1038/s41598-021-96430-4)
Приложен R1055: [текст](../../fulltext/text/R1055.txt) · [PDF](../../fulltext/pdf/R1055.pdf) — «A Common Human Problem Has a Name: Misokinesia»
Связь отчётов: Misokinesia samples (pilot 2,751; Study 1 650; Study 2 765): Research Square preprint R1055 and Scientific Reports article R1056
Расхождения в тексте: R1056 and R1055 give the same numbers for all three samples. Small differences: in the kinetic-cue subset R1056 says '1 gender' and R1055 says '1 agender'; R1055 Table 4 has no percentages. Sex subgroup counts do not sum to the totals: pilot misophonia 1118+280=1398 vs 1406; Study 1 MpAQ 366+83=449 vs 460; Study 2 yes/no 120+204=324 vs 325. The gaps are presumably participants of other or undeclared gender. Study 2 female MpAQ>=2: 188/244=77.0%, but 77.1% is printed. The Study 2 Methods say 'questionnaires ... described above in Study 2' (probably Study 1). The abstract's '4100 participants' does not match 2751+650+765=4166.
Заметка ИИ: Both reports are about misokinesia; the misophonia measures are secondary, so primary_for_authors = no throughout. I coded the yes/no misophonia item as L1 (an intensity item: 'strong negative feelings'). It is borderline with L0 because it asks 'ever' with no frequency, so the reviewer should confirm. MpAQ>=2 is L0 under the MAQ row. No funding statement appears in the texts provided.

### ST082-1 · Pilot study: UBC psychology undergraduates, Canada, n=2751
Отчёты: R1056 (main); R1055

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · yes to single item: ever strong negative feelings, thoughts or physical reactions to specific or repetitive sounds (mouth/body sounds) | **L1** | **1406 / 2751** | 51.1 | R1056, Pilot study | «for the misophonia sensitivity question, a total of 1406 students (or 51.1%) responded yes» |
| E2 | female | adhoc · yes to single item: ever strong negative feelings, thoughts or physical reactions to specific or repetitive sounds | **L1** | **1118 / 2028** | 55.1 | R1056, Pilot study | «a total of 1118 females (or 55.1%) and 280 males (or 39.9%) responded yes to the misophonia sensitivity question» |
| E3 | male | adhoc · yes to single item: ever strong negative feelings, thoughts or physical reactions to specific or repetitive sounds | **L1** | **280 / 701** | 39.9 | R1056, Pilot study | «280 males (or 39.9%) responded yes to the misophonia sensitivity question» |

- E1: источник порога: study's own; правило: adhoc row; intensity item ('strong negative feelings') -> L1; у авторов: «misophonia sensitivity»; главная у авторов: no; период: lifetime; заметка: Borderline L1/L0: the item asks 'ever', with no frequency; the authors call it a deliberately liberal criterion. The authors' primary outcome is misokinesia.
- E2: источник порога: study's own; правило: adhoc row; intensity item -> L1; у авторов: «misophonia sensitivity»; главная у авторов: no; период: lifetime; заметка: n = 2028 females, from the sample description; 1118/2028 = 55.1% matches.
- E3: источник порога: study's own; правило: adhoc row; intensity item -> L1; у авторов: «misophonia sensitivity»; главная у авторов: no; период: lifetime; заметка: n = 701 males, from the sample description; 280/701 = 39.9% matches.

**Ключевые поля выборки:**
- **n_analysed: 2751** — R1056, Pilot study — «a total of 1406 students (or 51.1%) responded yes»
- **population: university_students** — R1056, Pilot study — «students enrolled in undergraduate courses in the Department of Psychology at the University of British Columbia»
- **sampling: convenience** — R1056, Pilot study — «recruited through the Human Subject Pool (HSP) on-line study recruitment portal ... reimbursed 0.5 extra course credits»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: CAN — R1056, Pilot study — «students enrolled in undergraduate courses in the Department of Psychology at the University of British Columbia (UBC)»
- setting: university (online Human Subject Pool portal, Department of Psychology, UBC) — R1056, Pilot study — «recruited through the Human Subject Pool (HSP) on-line study recruitment portal for students enrolled in undergraduate courses in the Department of Psychology»
- data_years: NR — R1056, Pilot study — «NR»
- design: cross-sectional — R1056, Pilot study — «Our pilot study involved administering on an on-line questionnaire that asked two yes/no questions.»
- topic_disclosed: NR — R1056, Pilot study — «NR»
- inclusion_exclusion: Undergraduates in UBC psychology courses via HSP portal; no other criteria reported — R1056, Pilot study — «students enrolled in undergraduate courses in the Department of Psychology at the University of British Columbia (UBC)»
- n_invited: NR — R1056, Pilot study — «NR»
- n_responded: 2751 — R1056, Pilot study — «A total of 2751 individuals (ages 17–66; Median = 20, SD = 3.27; 2028 female, 701 male, 3 trans-gender, 19 declined to identify) were recruited»
- response_rate: NR — R1056, Pilot study — «NR»
- age_mean: NR — R1056, Pilot study — «ages 17–66; Median = 20, SD = 3.27»
- age_sd: 3.27 — R1056, Pilot study — «Median = 20, SD = 3.27»
- age_min: 17 — R1056, Pilot study — «ages 17–66»
- age_max: 66 — R1056, Pilot study — «ages 17–66»
- age_group: mixed — R1056, Pilot study — «ages 17–66; Median = 20»
- pct_female: 73.7 — R1056, Pilot study — «2028 female, 701 male, 3 trans-gender, 19 declined to identify»
- informant: self — R1056, Pilot study — «on-line questionnaire that asked two yes/no questions»
- mode: online — R1056, Pilot study — «administering on an on-line questionnaire»
- instruments: Ad hoc single yes/no misophonia sensitivity question (English) — R1056, Pilot study — «Do you ever have strong negative feelings, thoughts, or physical reactions to specific or repetitive sounds, such as those from the mouth»
- instrument_validated_in_language: no — R1056, Limitations — «we used a simple yes/no question ... using a deliberately liberal criteria»
- pub_status: journal — R1056 header — «Year: 2021; venue: Scientific reports; DOI: 10.1038/s41598-021-96430-4»
- language: English — R1056 full text — «Misokinesia is a sensitivity to seeing others fidget that is prevalent in the general population»
- funding_coi: NR (ethics approval by UBC Behavioural Research Ethics Board reported) — R1056, Pilot study — «All protocols were approved by the UBC Behavioural Research Ethics Board»
- notes: The study's main aim was misokinesia; the misophonia item is secondary. pct_female computed as 2028/2751. Age SD is reported next to the median; the mean is not reported. Recruited from the same UBC HSP pool as Study 1; possible participant overlap is not addressed, and pilot dates are not reported. The authors say the item was not designed to give a definitive misophonia prevalence. Sex subgroup counts (1118+280=1398) do not sum to 1406 (other or undeclared gender).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is a psychology-course subject pool at one university, while the claims refer to the general / non-clinical population — R1056, Pilot study — «students enrolled in undergraduate courses in the Department of Psychology at the University of British Columbia»
2. способ отбора: **no** — Volunteer opt-in through the subject pool for course credit — R1056, Pilot study — «recruited through the Human Subject Pool (HSP) on-line study recruitment portal ... reimbursed 0.5 extra course credits»
3. размер выборки: **yes** — n=2751 >= 385 — R1056, Pilot study — «A total of 2751 individuals»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection missing — R1056, Pilot study — «ages 17–66; Median = 20, SD = 3.27; 2028 female, 701 male»
5. охват (пропуски): **unclear** — Missing responses not reported — R1056, Pilot study — «a total of 1406 students (or 51.1%) responded yes»
6. валидность определения случая: **no** — Ad hoc single yes/no item — R1056, Pilot study — «Do you ever have strong negative feelings, thoughts, or physical reactions to specific or repetitive sounds»
7. единое надёжное измерение: **unclear** — Same online item for everyone, but no reliability information — R1056, Pilot study — «administering on an on-line questionnaire that asked two yes/no questions»
8. статистика (числитель и знаменатель): **yes** — Count and denominator given; CI calculable — R1056, Pilot study — «a total of 1406 students (or 51.1%) responded yes»
9. отклик: **no** — Opt-in subject pool with no denominator of invited people — R1056, Pilot study — «recruited through the Human Subject Pool (HSP) on-line study recruitment portal»

Правки:
- 

Проверено: да
### ST082-2 · Study 1: UBC undergraduates, lab study, Canada, n=650
Отчёты: R1056 (main); R1055

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MAQ · MpAQ sum >=2 | **L0** | **460 / 650** | 70.8 | R1056, Prevalence and variability | «a total of 460 students (or 70.8%) reported a sum score of 2 or more on the MpAQ» |
| E2 | female | MAQ · MpAQ sum >=2 | **L0** | **366 / 514** | 71.2 | R1056, Prevalence and variability | «a total of 366 females (or 71.2%) and 83 males (or 66.9%) reported a sum score of 2 or more on the MpAQ» |
| E3 | male | MAQ · MpAQ sum >=2 | **L0** | **83 / 124** | 66.9 | R1056, Prevalence and variability | «83 males (or 66.9%) reported a sum score of 2 or more on the MpAQ» |

- E1: источник порога: study's own; правило: MAQ row; G2 below L1 cut-off (MpAQ >=2 listed as L0); у авторов: «non-minimal misophonia sensitivity»; главная у авторов: no; период: NR; заметка: L0, not pooled. The authors' primary outcome is misokinesia (MkAQ).
- E2: источник порога: study's own; правило: MAQ row; G2 (L0); у авторов: «non-minimal misophonia sensitivity»; главная у авторов: no; период: NR; заметка: n = 514 females, from Participants; 366/514 = 71.2% matches.
- E3: источник порога: study's own; правило: MAQ row; G2 (L0); у авторов: «non-minimal misophonia sensitivity»; главная у авторов: no; период: NR; заметка: n = 124 males, from Participants; 83/124 = 66.9% matches.

**Ключевые поля выборки:**
- **n_analysed: 650** — R1056, Study 1 Participants — «leaving a final sample of 650 individuals»
- **population: university_students** — R1056, Study 1 Participants — «recruited through the UBC HSP on-line study recruitment portal»
- **sampling: convenience** — R1056, Study 1 Participants — «recruitment goal of running as many participants as possible during the fall, 2019 semester»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: CAN — R1056, Study 1 Participants — «recruited through the UBC HSP on-line study recruitment portal»
- setting: university (laboratory at UBC; recruited via Human Subject Pool) — R1056, Study 1 Participants — «Participants completed the tasks in a quiet room with only the researcher present»
- data_years: 2019 — R1056, Study 1 Participants — «running as many participants as possible during the fall, 2019 semester at UBC»
- design: cross-sectional — R1056, Study 1 Procedures — «each participant performed two behavioral tasks ... Following completion of these tasks, they then filled out a set of questionnaires»
- topic_disclosed: NR — R1056, Study 1 — «NR»
- inclusion_exclusion: Self-reported free of neurological problems, fluent in English, normal vision; excluded if MkAQ/MpAQ incomplete or behavioural task not completed (39) — R1056, Study 1 Participants — «Data from 39 of these participants were excluded for either leaving the MkAQ or MpAQ incomplete, or not completing the behavioural task»
- n_invited: NR — R1056, Study 1 Participants — «NR»
- n_responded: 689 — R1056, Study 1 Participants — «A total of 689 individuals were recruited»
- response_rate: NR — R1056, Study 1 — «NR»
- age_mean: NR — R1056, Study 1 Participants — «the age range was 18–44, with 594 between the ages of 18–24»
- age_sd: NR — R1056, Study 1 Participants — «NR»
- age_min: 18 — R1056, Study 1 Participants — «the age range was 18–44»
- age_max: 44 — R1056, Study 1 Participants — «the age range was 18–44»
- age_group: adults — R1056, Study 1 Participants — «the age range was 18–44»
- pct_female: 79.1 — R1056, Study 1 Participants — «650 individuals (514 females, 124 males, 2 non-binary, 1 agender, 9 declined to answer»
- informant: self — R1056, Questionnaires — «Participants filled out four online questionnaires in total through Qualtrics»
- mode: online — R1056, Questionnaires — «Participants filled out four online questionnaires in total through Qualtrics»
- instruments: MpAQ (Misophonia Assessment Questionnaire, Johnson/Dozier; English; 21 items 0-3, sum 0-63); MkAQ is a misokinesia analogue, not a misophonia measure — R1056, Prevalence and variability — «the MkAQ asks 21 different questions ... Mirroring analysis of the MpAQ»
- instrument_validated_in_language: no — R1056, Limitations — «we chose to adapt the unvalidated MpAQ to develop MkAQ»
- pub_status: journal — R1056 header — «venue: Scientific reports»
- language: English — R1056 full text — «Study 1»
- funding_coi: NR (UBC ethics approval reported) — R1056, Study 1 Participants — «All protocols were approved by the UBC Behavioural Research Ethics Board»
- notes: The only misophonia definition is MpAQ sum >=2, which lies inside the subclinical band (L0, not pooled). pct_female computed as 514/650. Questionnaires were completed online in the lab after the behavioural tasks. Same UBC HSP pool as the pilot; possible overlap is not addressed. The authors note that their MAQ cut-offs may not converge with those of other studies.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Psychology subject pool at one university; claims refer to the general population — R1056, Study 1 Participants — «recruited through the UBC HSP on-line study recruitment portal»
2. способ отбора: **no** — Volunteer opt-in for course credit — R1056, Study 1 Participants — «received 0.5 extra course credits»
3. размер выборки: **yes** — n=650 >= 385 — R1056, Study 1 Participants — «a final sample of 650 individuals»
4. описание выборки и условий: **yes** — Age bands, sex, setting, country (UBC) and dates (fall 2019) reported — R1056, Study 1 Participants — «during the fall, 2019 semester at UBC ... 514 females, 124 males ... the age range was 18–44»
5. охват (пропуски): **yes** — 39/689 (5.7%) excluded for incomplete questionnaires or task — R1056, Study 1 Participants — «Data from 39 of these participants were excluded for either leaving the MkAQ or MpAQ incomplete»
6. валидность определения случая: **no** — MpAQ sum >=2 is inside the subclinical band, and the authors call the MpAQ unvalidated — R1056, Prevalence and variability — «those with a sum score of 2 or more (or reporting non-minimal misokinesia/misophonia sensitivity)»
7. единое надёжное измерение: **unclear** — Same instrument and mode for everyone; no reliability reported — R1056, Questionnaires — «Participants filled out four online questionnaires in total through Qualtrics»
8. статистика (числитель и знаменатель): **yes** — Count and denominator given; CI calculable — R1056, Prevalence and variability — «a total of 460 students (or 70.8%) reported a sum score of 2 or more on the MpAQ»
9. отклик: **no** — Opt-in subject pool, no denominator of invited people — R1056, Study 1 Participants — «recruited through the UBC HSP on-line study recruitment portal»

Правки:
- 

Проверено: да
### ST082-3 · Study 2: Amazon MTurk adults, country NR, n=765
Отчёты: R1056 (main); R1055

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · yes to single item: ever strong negative feelings, thoughts or physical reactions to specific or repetitive sounds | **L1** | **325 / 765** | 42.5 | R1056, Study 2 Results | «for our misophonia question, a total of 325 participants (or 42.5%) responded yes» |
| E2 | female | adhoc · yes to single item: ever strong negative feelings, thoughts or physical reactions to specific or repetitive sounds | **L1** | **120 / 244** | 49.2 | R1056, Study 2 Results | «a total of 120 females (or 49.2%) and 204 males (or 39.5%) responded yes to the misophonia question» |
| E3 | male | adhoc · yes to single item: ever strong negative feelings, thoughts or physical reactions to specific or repetitive sounds | **L1** | **204 / 516** | 39.5 | R1056, Study 2 Results | «204 males (or 39.5%) responded yes to the misophonia question» |
| E4 | female | MAQ · MpAQ sum >=2 | **L0** | **188 / 244** | 77.0 | R1056, Study 2 Results | «a total of 188 females (or 77.1%) and 397 males (or 76.9%) reported a sum score of 2 or more on the MpAQ» |
| E5 | male | MAQ · MpAQ sum >=2 | **L0** | **397 / 516** | 76.9 | R1056, Study 2 Results | «397 males (or 76.9%) reported a sum score of 2 or more on the MpAQ» |

- E1: источник порога: study's own; правило: adhoc row; intensity item -> L1; у авторов: «misophonia sensitivity»; главная у авторов: no; период: lifetime; заметка: Borderline L1/L0 ('ever', no frequency). The authors' primary outcome is misokinesia.
- E2: источник порога: study's own; правило: adhoc row; intensity item -> L1; у авторов: «misophonia sensitivity»; главная у авторов: no; период: lifetime; заметка: n = 244 females, from Methods.
- E3: источник порога: study's own; правило: adhoc row; intensity item -> L1; у авторов: «misophonia sensitivity»; главная у авторов: no; период: lifetime; заметка: n = 516 males, from Methods.
- E4: источник порога: study's own; правило: MAQ row; G2 below L1 cut-off (L0); у авторов: «sum score of 2 or more on the MpAQ»; главная у авторов: no; период: NR; заметка: 188/244 = 77.0%, but 77.1% is printed. Whole-sample count not reported.
- E5: источник порога: study's own; правило: MAQ row; G2 below L1 cut-off (L0); у авторов: «sum score of 2 or more on the MpAQ»; главная у авторов: no; период: NR; заметка: 397/516 = 76.9% matches.

**Ключевые поля выборки:**
- **n_analysed: 765** — R1056, Study 2 Methods — «This resulted in a final sample of 765 participants»
- **population: gp_other** — R1056, Study 2 Discussion — «to assess the prevalence rate for misokinesia sensitivities in a non-student, non-clinically-defined population»
- **sampling: convenience** — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk (MTurk)»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: NR — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk (MTurk)»
- setting: online panel (Amazon Mechanical Turk) — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk (MTurk)»
- data_years: NR — R1056, Study 2 — «NR»
- design: cross-sectional — R1056, Study 2 Methods — «we asked participants the two questions described above in our pilot study ... and (2) participants completed the four questionnaires»
- topic_disclosed: NR — R1056, Study 2 — «NR»
- inclusion_exclusion: Adults on MTurk; 242 excluded for failing three attention checks — R1056, Study 2 Methods — «242 of these participants failed a set of three separate attention checks included in our study protocol and were not included in analyses»
- n_invited: NR — R1056, Study 2 — «NR»
- n_responded: 1007 — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk»
- response_rate: NR — R1056, Study 2 — «NR»
- age_mean: NR — R1056, Study 2 Methods — «age range = 18–93, median = 32 years»
- age_sd: NR — R1056, Study 2 Methods — «NR»
- age_min: 18 — R1056, Study 2 Methods — «age range = 18–93»
- age_max: 93 — R1056, Study 2 Methods — «age range = 18–93»
- age_group: adults — R1056, Study 2 Methods — «age range = 18–93, median = 32 years»
- pct_female: 31.9 — R1056, Study 2 Methods — «765 participants (N = 244 females, 516 males, 3 non-binary, 2 trans gender»
- informant: self — R1056, Study 2 Methods — «we asked participants the two questions described above in our pilot study»
- mode: online — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk (MTurk)»
- instruments: Ad hoc single yes/no misophonia sensitivity question (English); MpAQ (Misophonia Assessment Questionnaire; English) — R1056, Study 2 Methods — «participants completed the four questionnaires (demographics, MkAQ, MpAQ, State and Trait Anxiety Inventory)»
- instrument_validated_in_language: no — R1056, Limitations — «we used a simple yes/no question ... using a deliberately liberal criteria»
- pub_status: journal — R1056 header — «venue: Scientific reports»
- language: English — R1056 full text — «Study 2»
- funding_coi: NR (UBC ethics approval; participants paid USD 1.50) — R1056, Study 2 Methods — «Participants were reimbursed $1.50 USD for their participation.»
- notes: The country of the MTurk workers is not stated. pct_female computed as 244/765. The whole-sample MpAQ >=2 count is not reported, only counts by sex (188 F + 397 M = 585 of the 760 with binary sex); not derived. The Methods say the questionnaires were 'described above in Study 2' (probably meaning Study 1). The main estimate for this review is the yes/no item (L1).

**Риск смещения (JBI):**
1. рамка выборки: **no** — MTurk workers used to describe the general population — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk (MTurk)»
2. способ отбора: **no** — Online non-probability opt-in panel — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk (MTurk)»
3. размер выборки: **yes** — n=765 >= 385 — R1056, Study 2 Methods — «a final sample of 765 participants»
4. описание выборки и условий: **no** — Country and dates of data collection missing — R1056, Study 2 Methods — «N = 244 females, 516 males, 3 non-binary, 2 trans gender; age range = 18–93, median = 32 years»
5. охват (пропуски): **unclear** — 24% (242/1007) excluded for failed attention checks (a quality exclusion); missing misophonia item data not reported — R1056, Study 2 Methods — «242 of these participants failed a set of three separate attention checks ... and were not included in analyses»
6. валидность определения случая: **no** — Main definition is an ad hoc yes/no item; MpAQ >=2 is subclinical — R1056, Study 2 Results — «for our misophonia question, a total of 325 participants (or 42.5%) responded yes»
7. единое надёжное измерение: **unclear** — Same online item for everyone; no reliability reported — R1056, Study 2 Methods — «we asked participants the two questions described above in our pilot study»
8. статистика (числитель и знаменатель): **yes** — Count and denominator given for the main estimate; CI calculable — R1056, Study 2 Results — «a total of 325 participants (or 42.5%) responded yes»
9. отклик: **no** — Open online panel with no denominator of invited people — R1056, Study 2 Methods — «We recruited 1007 adults from Amazon Mechanical Turk (MTurk)»

Правки:
- 

Проверено: да
---

## ST083 · Kılıç 2021 · BJPsych open

Основной отчёт R1062: [текст](../../fulltext/text/R1062.txt) — «The prevalence and characteristics of misophonia in Ankara, Turkey: population-based study.» — [DOI](https://doi.org/10.1192/bjo.2021.978)
Расхождения в тексте: Age: the inclusion criterion says residents 'aged >15 years', but the age range is reported as 15–88, and the youngest Table 1 band is 15–24. Response figures: the text gives 86.4% of target households contacted (259/300 = 86.3%) and interviews completed with 76.1% of contacted households. At the individual level, 528/710 = 74.4% agreed; adding the 15 telephone interviews gives 543/710 = 76.5% (the value used here). Two interviews were dropped, leaving 541. Some Table 1 column percentages do not match the full denominators, which suggests a few missing values on covariates: family history 97 (18.1) where 97/541 = 17.9%; tinnitus 177 (37.6) where 177/472 = 37.5%. The past-contact percentage differs between Table 1 (27.4% in non-misophonia) and the text (28.7%). For psychotropic use, Table 1 gives 11.1% and the text gives 11.2%. These differences do not affect the misophonia counts (69/54…
Заметка ИИ: The primary estimate is L3, 69/541 (12.8%), past month, based on the study's own interview criteria, which are new and not validated. Clinical-subgroup prevalences for self-reported psychiatrist-diagnosed ADHD, OCD, bipolar disorder and similar conditions are not extracted. They are given only as percentages within the misophonia and non-misophonia groups (e.g., ADHD 20.3% vs 7.3%), and back-calculation does not give consistent integer counts (7.3% of 472 = 34.5), so the denominators are uncertain. The reviewer should check the supplement (diagnostic flowchart) and Fig. 1, which were not supp…

### ST083-1 · Ankara city-centre household sample, Turkey, n=541
Отчёты: R1062 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | interview · interview: study's proposed criteria (MIS): ≥1 MCL sound moderate/high + high anger, disgust or distress + ≥1 coping strategy often/always + ≥1 interference item yes | **L3** | **69 / 541** | 12.8 | Abstract; Correlates of misophonia; Table 1 | «The current misophonia diagnosis prevalence was 12.8% (n = 69 of 541)» |
| E2 | female | interview · interview: study's proposed criteria (MIS) | **L3** | **51 / 314** | 16.2 | Table 1 | «Gender, female** / 51 (73.9) / 263 (55.7) / 314 (58.0)» |
| E3 | male | interview · interview: study's proposed criteria (MIS) | **L3** | **18 / 227** | 7.9 | Table 1; Results | «Total / 69 (12.8) ... Gender, female** / 51 (73.9) ... 314 (58%) were female and 227 (42%) were male» |
| E4 | 15-24 | interview · interview: study's proposed criteria (MIS) | **L3** | **21 / 106** | 19.8 | Table 1 | «15–24 / 21 (30.4) / 85 (18.0) / 106 (19.6)» |
| E5 | 25-44 | interview · interview: study's proposed criteria (MIS) | **L3** | **26 / 163** | 16.0 | Table 1 | «25–44 / 26 (37.7) / 137 (29.0) / 163 (30.1)» |
| E6 | 45-64 | interview · interview: study's proposed criteria (MIS) | **L3** | **20 / 195** | 10.3 | Table 1 | «45–64 / 20 (29.0) / 175 (37.1) / 195 (36.0)» |
| E7 | >=65 | interview · interview: study's proposed criteria (MIS) | **L3** | **2 / 77** | 2.6 | Table 1 | «≥65 / 2 (2.9) / 75 (15.9) / 77 (14.2)» |
| E8 | history of tinnitus | interview · interview: study's proposed criteria (MIS) | **L3** | **30 / 207** | 14.5 | Table 1 | «History of tinnitus / 30 (43.5) / 177 (37.6) / 207 (38.3)» |
| E9 | all | interview · ≥1 MCL sound rated moderate or high (MSC ≥1) | **L0** | **427 / 541** | 78.9 | Abstract; Results | «In all, 427 (78.9%) participants scored one or more MCL item as moderate or high.» |

- E1: источник порога: study's own; правило: interview row; criteria stated in full in the report, applied by trained interviewers -> L3; у авторов: «current misophonia diagnosis»; главная у авторов: yes; период: past month; заметка: MCL covers the previous month. Duration criterion not assessed. The criteria require impairment.
- E2: источник порога: study's own; правило: interview row; L3; у авторов: «misophonia»; главная у авторов: no; период: past month; заметка: 16.2%
- E3: источник порога: study's own; правило: interview row; L3; у авторов: «misophonia»; главная у авторов: no; период: past month; **расчёт: cases 69 − 51 = 18; n 541 − 314 = 227 (Table 1 / Results)**
- E4: источник порога: study's own; правило: interview row; L3; у авторов: «misophonia»; главная у авторов: no; период: past month; заметка: Includes 42 participants aged <18
- E5: источник порога: study's own; правило: interview row; L3; у авторов: «misophonia»; главная у авторов: no; период: past month
- E6: источник порога: study's own; правило: interview row; L3; у авторов: «misophonia»; главная у авторов: no; период: past month
- E7: источник порога: study's own; правило: interview row; L3; у авторов: «misophonia»; главная у авторов: no; период: past month
- E8: источник порога: study's own; правило: interview row; L3; у авторов: «misophonia»; главная у авторов: no; период: past month; заметка: Self-reported history of tinnitus, found within the sample. Column percentages suggest a few missing values (177/472 = 37.5%, printed 37.6).
- E9: источник порога: study's own; правило: interview row: items recording only a trigger = L0; у авторов: «reported at least one sound that was distressing»; главная у авторов: no; период: past month; заметка: Trigger only; listed, not pooled

**Ключевые поля выборки:**
- **n_analysed: 541** — Method, Sample; Table 1 — «In all, two interviews were excluded because of incomplete data. The final sample included 541 individuals (Fig. 1).»
- **population: gp_probability** — Method, Sample — «a random sample representative of the general population of the centre of Ankara, Turkey»
- **sampling: probability** — Method, Sample; Procedure — «In total, 60 starting points (bus stops) were randomly selected, for which five households each were visited (for a total of 300 households). The target sample, therefore, was all people aged >15 years living in the 300 households.»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Method, Sample — «This cross-sectional study included a random sample representative of the general population of the centre of Ankara, Turkey.»
- setting: community (household survey, Ankara city centre) — Abstract, Method — «We used a household sample (N = 541) of all residents aged >15 years, living in 300 homes randomly selected in Ankara city centre, Turkey.»
- data_years: 2015 — Method, Sample — «Data were collected in 2015.»
- design: cross-sectional — Method, Sample — «This cross-sectional study included a random sample representative of the general population of the centre of Ankara, Turkey.»
- topic_disclosed: NR — Procedure — «At the start of each interview session (both in person and via telephone), text was read aloud to the eligible respondent.»
- inclusion_exclusion: All consenting household members aged >15 years in selected households; excluded: conditions with communication problems (intellectual disability, speech or hearing problems, dementia); 2 excluded for incomplete data — Method, Sample — «All consenting household members aged >15 years were considered eligible. Exclusion criteria included any conditions associated with communication problems (in…»
- n_invited: 710 — Method, Sample — «Among the 710 residents aged >15 years living in the remaining 259 households, 528 (74.4%) agreed to participate»
- n_responded: 543 — Method, Sample — «528 (74.4%) agreed to participate ... 70 people ... could not be contacted in person ... but 15 of them agreed to be participate via telephone»
- response_rate: 76.5 — Method, Sample — «Among the 710 residents aged >15 years ... 528 (74.4%) agreed to participate ... 15 of them agreed to be participate via telephone»
- age_mean: 43.5 — Results — «Mean age of the participants was 43.5 (s.d. 18.2, range 15–88) years»
- age_sd: 18.2 — Results — «Mean age of the participants was 43.5 (s.d. 18.2, range 15–88) years»
- age_min: 15 — Results — «Mean age of the participants was 43.5 (s.d. 18.2, range 15–88) years»
- age_max: 88 — Results — «Mean age of the participants was 43.5 (s.d. 18.2, range 15–88) years»
- age_group: mixed — Results — «range 15–88) years and 42 (7.8%) were aged <18 years»
- pct_female: 58.0 — Results; Table 1 — «The study included 541 participants, of which 314 (58%) were female and 227 (42%) were male.»
- informant: self — Procedure — «Interviews were conducted at the respondents’ homes by nine trained interviewers, including three psychiatry registrars.»
- mode: mixed — Procedure — «All interviews were conducted face to face, except for 15 that were conducted via the telephone.»
- instruments: Misophonia Interview Schedule (MIS) with Misophonia Checklist (MCL), semi-structured interview developed for this study; administration language not stated — Method, Assessments — «the Misophonia Interview Schedule15 (MIS), a semi-structured interview developed for the current study, was administered. The MIS includes the Misophonia Check…»
- instrument_validated_in_language: no — Method, Assessments — «a semi-structured interview developed for the current study ... The MCL was developed for this study by the researchers»
- pub_status: journal — Header — «Venue: BJPsych open; DOI: 10.1192/bjo.2021.978»
- language: English — Full text — «The prevalence and characteristics of misophonia in Ankara, Turkey: population-based study»
- funding_coi: No specific grant; declaration of interest: none — Funding; Declaration of interest — «This research received no specific grant from any funding agency, commercial or not-for-profit sectors. ... Declaration of interest None.»
- notes: The diagnostic criteria were proposed by the authors and developed for this study; they include impairment but no duration criterion. Mode response rate: 74.4% (528/710) as reported; 76.5% (543/710) when the 15 telephone interviews are included. A further 41 of 300 households refused, and household-level non-response is not in the denominator. The interviewers were trained lay interviewers plus psychiatry registrars. Ref 15 (MIS/MCL) may be a related report from the same dataset; check for overlap with other ST entries by Kılıç/Öz. There is no survey weighting and no adjustment for household …

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Target population is residents >15 y of Ankara city centre; bus stops spread across the city in proportion to population density were used as frame because no household register was available — Method, Sample — «As a registry of all households was not available at the time of the study, a sampling consultant suggested using bus stops as the sampling frame. Public buses…»
2. способ отбора: **yes** — Bus stops picked at random, then a random-route walk with all residents >15 of each household; quasi-probability (the 'first five available households' rule adds some selection) — Procedure — «moving in a predefined direction (walking a spiral route heading north), the first five available households were selected. Consequently, 300 randomly selected…»
3. размер выборки: **yes** — n = 541 ≥ 385 — Method, Sample — «The final sample included 541 individuals»
4. описание выборки и условий: **yes** — Age, sex, setting, country and year of data collection reported — Method; Results — «Data were collected in 2015. ... 314 (58%) were female ... Mean age of the participants was 43.5»
5. охват (пропуски): **yes** — Only 2 of 543 interviews dropped for incomplete data (<10%) — Method, Sample — «In all, two interviews were excluded because of incomplete data.»
6. валидность определения случая: **yes** — L3: explicit diagnostic criteria stated in the report, applied by trained interviewers in a semi-structured interview (criteria are new and not validated) — Proposed diagnostic criteria — «to meet this criterion, one or more of the 51 MCL items should be scored as moderate or high. ... we required an MCL score of high for any of these three emoti…»
7. единое надёжное измерение: **no** — 15 interviews were by telephone and the rest face to face, with no check of mode equivalence; no inter-rater reliability given for the diagnosis (MCL alpha only) — Procedure; Assessments — «All interviews were conducted face to face, except for 15 that were conducted via the telephone. ... The reliability indices of the MCL are excellent (Cronbach…»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are clear (69/541), so a CI can be calculated; no CI or design-based adjustment for household clustering — Correlates of misophonia — «the prevalence of misophonia in the study population (N = 541) was 12.8% (n = 69)»
9. отклик: **yes** — Individual response 74.4% in participating households (543/710 = 76.5% including telephone); 41 of 300 households (13.6%) refused — Method, Sample — «Among the 300 households contacted, 41 (13.6%) refused to participate ... 528 (74.4%) agreed to participate»

Правки:
- 

Проверено: да
---

## ST084 · Loch 2021 · Universität Regensburg

Основной отчёт R1066: [текст](../../fulltext/text/R1066.txt) · [PDF](../../fulltext/pdf/R1066.pdf) — «Misophonie bei psychiatrischen Erkrankungen» — [DOI](https://doi.org/10.5283/epub.51124)
Расхождения в тексте: Screening counts agree: Abb. 11 bands 14+17+13+12+4 = 60, which matches the 60 who met the item criteria; 60-14 = 46 positive (23.7%). Text '16 at least severe' = 12+4. The screening percentages in Abb. 14 (17.4/19.6/28.3/26/8.7% of 46) give 8/9/13/12/4, consistent with Abb. 11 (3-4 = 17). The sexes add up: 20+26 = 46; 85+109 = 194. The Abb. 12 positive + negative counts equal the Abb. 9 totals for every diagnostic group. The Abb. 13 caption says n=102, but the F3 subtype counts (1+14+35+71) sum to 121, matching Abb. 9/10 and 62.4% of 194; the caption n looks wrong. In Abb. 13 the positives (0+4+6+23 = 33) match the F3 positives in Abb. 12. The MAQ bands 2+6+9+7+3 = 27 match the completers; the text says 'about 70% at least moderate' = 19/27 = 70.4%, and '37% severe to extreme' = 10/27. MAQ band cut points appear only in Abb. 5 (an image) and are not in the extracted text.
Заметка ИИ: The primary estimate is the ad hoc Kurztest Misophonie (reaction plus impairment >=3/10), coded L2 under the adhoc-row rule that names this test, with JBI 6 = no. The MAQ estimates are coded level NR (G10) because 19 of the 46 screen-positives did not complete the MAQ; their cases and n are given among the 27 completers for information only. The time frame for the screener is coded 'current' because the impairment item is in the present tense; the full screener items (Abb. 3) are not in the extracted text.

### ST084-1 · Psychiatric inpatients, Klinik für Psychiatrie Bamberg, Germany, n=194
Отчёты: R1066 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · Kurztest Misophonie (self-completed): Q1 (sound intolerance) yes AND Q2 (irritation/disgust) or Q3 (anger) yes AND impairment item >=3/10 | **L2** | **46 / 194** | 23.7 | Page 26, 3.1; Page 36, 4.1; Page 42, 5 | «46 Patienten (23,7%) wiesen ein positives Screening auf [46 patients (23.7%) had a positive screen]» |
| E2 | all | adhoc · Kurztest Misophonie (self-completed): Q1 yes AND Q2 or Q3 yes, regardless of impairment rating | **L1** | **60 / 194** | 30.9 | Page 24, 3.1 | «60 Patienten (30,9%) bejahten die erste Frage des Kurztest Misophonie ... und beantworteten mindestens eine der beiden weiteren Fragen ebenfalls mit „Ja“ [60 (30.9%) answered Q1 yes and at least one further question yes]» |
| E3 | all | adhoc · Kurztest Misophonie (self-completed): reaction criteria AND impairment >=4/10 (mild or more) | **L2** | **38 / 194** | 19.6 | Page 29, Abb. 14; Page 24, Abb. 11 | «Screening: subklinisch 17,4; mild 19,6; moderat 28,3; schwer 26; extrem 8,7 (Angaben in Prozent) [percent of 46 screen-positives]» |
| E4 | all | adhoc · Kurztest Misophonie (self-completed): reaction criteria AND impairment >=5/10 (moderate or more) | **L2** | **29 / 194** | 14.9 | Page 24, Abb. 11 | «0-2: 14; 3-4: 17; 5-6: 13; 7-8: 12; 9-10: 4 (Schweregrad Kurztest Misophonie)» |
| E5 | all | adhoc · Kurztest Misophonie (self-completed): reaction criteria AND impairment >=7/10 (severe or more) | **L2** | **16 / 194** | 8.2 | Page 26, 3.1; Abb. 11 | «16 Patienten (34,8% der Patienten mit positivem Screening) beurteilten ihr Leben als mindestens schwer durch die Misophonie beeinträchtigt [16 rated their life at least severely impaired]» |
| E6 | all | adhoc · Kurztest Misophonie (self-completed): reaction criteria AND impairment >=9/10 (extreme) | **L2** | **4 / 194** | 2.1 | Page 24, Abb. 11 | «9-10: 4 (Schweregrad Kurztest Misophonie)» |
| E7 | all | MAQ · Screen positive AND MAQ >=12 (mild or more, version A bands) | **NR** | **25 / 27** | 92.6 | Page 26, 3.2.1 | «bei 7,4% (2 Teilnehmer) der Schweregrad „subklinisch“, bei 22,2% (6 Teilnehmer) „mild“, 33,3% (9 Teilnehmer) „moderat“, 25,9% (7 Teilnehmer) „schwer“ und bei 11,1% (3 Teilnehmer) „extrem“» |
| E8 | all | MAQ · Screen positive AND MAQ >=25 (moderate or more, version A bands) | **NR** | **19 / 27** | 70.4 | Page 26, 3.2.1; Page 42, 5 | «Etwa 70% der Betroffenen wiesen eine mindestens moderat ausgeprägte Misophonie auf [about 70% had at least moderate misophonia]» |
| E9 | all | MAQ · Screen positive AND MAQ >=38 (severe or more, version A bands) | **NR** | **10 / 27** | 37.0 | Page 37, 4.2; Page 26, 3.2.1 | «Ein großer Anteil, 37% der Befragten ... wies eine schwere bis extreme Misophonie auf [37% had severe to extreme misophonia]» |
| E10 | all | MAQ · Screen positive AND MAQ >=51 (extreme, version A bands) | **NR** | **3 / 27** | 11.1 | Page 26, 3.2.1 | «bei 11,1% (3 Teilnehmer) „extrem“» |
| E11 | female | adhoc · Kurztest Misophonie (self-completed): Q1 yes AND Q2 or Q3 yes AND impairment >=3/10 | **L2** | **26 / 109** | 23.9 | Page 26, 3.1 | «26 weiblich (23,9% der Frauen) [26 female (23.9% of women)]» |
| E12 | male | adhoc · Kurztest Misophonie (self-completed): Q1 yes AND Q2 or Q3 yes AND impairment >=3/10 | **L2** | **20 / 85** | 23.5 | Page 26, 3.1 | «Davon waren 20 Patienten männlich (23,5% der Männer) [20 male (23.5% of men)]» |
| E13 | F1 substance use disorders | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **19 / 60** | 31.7 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F1 auffällig 19, unaufällig 41; Abb. 9: F1 60» |
| E14 | F2 schizophrenia/psychotic disorders | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **2 / 24** | 8.3 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F2 auffällig 2, unaufällig 22; Abb. 9: F2 24» |
| E15 | F3 affective disorders | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **33 / 121** | 27.3 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F3 auffällig 33, unaufällig 88; Abb. 9: F3 121» |
| E16 | F30 manic episode | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **0 / 1** | 0.0 | Page 28, Abb. 13; Page 25, Abb. 10 | «F30: manische Episode auffällig 0, unauffällig 1» |
| E17 | F31 bipolar affective disorder | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **4 / 14** | 28.6 | Page 28, Abb. 13; Page 25, Abb. 10 | «F31: bipolare affektive Störung auffällig 4, unauffällig 10; Abb. 10: F31 14» |
| E18 | F32 depressive episode | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **6 / 35** | 17.1 | Page 28, Abb. 13; Page 25, Abb. 10 | «F32: depressive Episode auffällig 6, unauffällig 29; Abb. 10: F32 35» |
| E19 | F33 recurrent depressive disorder | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **23 / 71** | 32.4 | Page 28, Abb. 13; Page 25, Abb. 10 | «F33: rezidivierende depressive Störung auffällig 23, unauffällig 48; Abb. 10: F33 71» |
| E20 | F4 neurotic, stress-related and somatoform disorders | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **11 / 42** | 26.2 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F4 auffällig 11, unaufällig 31; Abb. 9: F4 42» |
| E21 | F6 personality and behavioural disorders | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **5 / 14** | 35.7 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F6 auffällig 5, unaufällig 9; Abb. 9: F6 14» |
| E22 | F0 organic mental disorders | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **0 / 5** | 0.0 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F0 auffällig 0, unaufällig 5» |
| E23 | F5 behavioural syndromes with physical factors | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **1 / 3** | 33.3 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F5 auffällig 1, unaufällig 2» |
| E24 | F7 intellectual disability | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **0 / 3** | 0.0 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F7 auffällig 0, unaufällig 3» |
| E25 | F9 childhood-onset behavioural/emotional disorders | adhoc · Kurztest Misophonie positive screen (reaction + impairment >=3/10, self-completed) | **L2** | **0 / 3** | 0.0 | Page 27, Abb. 12; Page 25, Abb. 9 | «Abb. 12: F9 auffällig 0, unaufällig 3» |

- E1: источник порога: study's own; правило: adhoc row; L2 rule (reaction plus impairment, Kurztest Misophonie with impairment >=3/10); у авторов: «positives Screening; Prävalenz von 23,7%»; главная у авторов: yes; период: current; заметка: Authors' prevalence estimate. Authors call impairment score 3 'subklinisch'.
- E2: источник порога: study's own; правило: adhoc row; L1 (ad hoc reaction items, no impairment requirement); у авторов: «bejahten die erste Frage ... und beantworteten mindestens eine der beiden weite…»; главная у авторов: no; период: current; заметка: 14 of these 60 rated impairment 0-2, so screen-negative.
- E3: источник порога: study's own; правило: adhoc row; L2 rule; G1 sum of bands; у авторов: «mild or more (mild/moderat/schwer/extrem)»; главная у авторов: no; период: current; **расчёт: Subclinical (score 3) = 17.4% x 46 = 8.0 -> 8 (Abb. 14); 46 - 8 = 38 (= 9 mild + 13 moderate + 12 severe + 4 extreme)**; заметка: Abb. 11 combines scores 3-4 (n=17); split from Abb. 14 percentages.
- E4: источник порога: study's own; правило: adhoc row; L2 rule; G1 sum of bands; у авторов: «moderat or more»; главная у авторов: no; период: current; **расчёт: 13 (5-6) + 12 (7-8) + 4 (9-10) from Abb. 11**
- E5: источник порога: study's own; правило: adhoc row; L2 rule; G1 sum of bands; у авторов: «mindestens schwer beeinträchtigt»; главная у авторов: no; период: current; заметка: Consistent with Abb. 11: 12 + 4.
- E6: источник порога: study's own; правило: adhoc row; L2 rule; G1 (top band is cumulative); у авторов: «extrem»; главная у авторов: no; период: current
- E7: источник порога: developer paper; правило: MAQ row (version A, 5 bands); G1; G10 -> NR because 19 of 46 screen-positives did not complete the MAQ; у авторов: «mild or more»; главная у авторов: no; период: current; **расчёт: 6 mild + 9 moderate + 7 severe + 3 extreme = 25 of 27 MAQ completers**; заметка: Denominator is MAQ completers only (27 of 46 screen-positives); not determinable over the 194 screened (lower bound 25/194). Band cut points are shown in Abb. 5, not in the text; version A assumed from the 5 bands subclinical-extreme.
- E8: источник порога: developer paper; правило: MAQ row (version A); G1; G10 -> NR; у авторов: «mindestens moderat ausgeprägte Misophonie»; главная у авторов: no; период: current; **расчёт: 9 moderate + 7 severe + 3 extreme = 19 of 27**; заметка: Among MAQ completers only; lower bound over screened 19/194.
- E9: источник порога: developer paper; правило: MAQ row (version A); G1; G10 -> NR; у авторов: «schwere bis extreme Misophonie»; главная у авторов: no; период: current; **расчёт: 7 severe + 3 extreme = 10 of 27 (authors: 37%)**; заметка: Among MAQ completers only.
- E10: источник порога: developer paper; правило: MAQ row (version A); G1; G10 -> NR; у авторов: «extrem»; главная у авторов: no; период: current; заметка: Among MAQ completers only.
- E11: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «positives Screening»; главная у авторов: no; период: current
- E12: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «positives Screening»; главная у авторов: no; период: current
- E13: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current; заметка: Cases from Abb. 12, n from Abb. 9 (19+41=60). Multiple diagnoses possible.
- E14: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current; заметка: Multiple diagnoses possible.
- E15: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current; заметка: Includes bipolar (F31) and mania (F30). Abb. 13 caption gives n=102, but subtype counts sum to 121.
- E16: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E17: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E18: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E19: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E20: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current; заметка: Mixed anxiety/OCD/PTSD/somatoform group; not broken down.
- E21: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E22: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E23: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E24: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current
- E25: источник порога: study's own; правило: adhoc row; L2 rule; у авторов: «auffälliges Screening»; главная у авторов: no; период: current

**⚠ Проверка скриптом (обратите внимание):**
- E1, E3, E4, E5, E6, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25: самодельные вопросы на L2: верно, только если требуются и реакция, и нарушения
- E7, E8, E9, E10: n оценки не равно n_analysed выборки (194): проверьте знаменатель

**Ключевые поля выборки:**
- **n_analysed: 194** — Page 26, 3.1 — «46 Patienten (23,7%) wiesen ein positives Screening auf [46 patients (23.7%) screened positive]»
- **population: clinical** — Page 14, 2.2 — «alle Patienten ab einem Alter von 18 Jahren, die über die Zentrale Patientenaufnahme stationär aufgenommen wurden [all patients aged 18+ admitted as inpatients]»
- **sampling: census** — Page 14, 2.2; Page 36, 4 — «Jeder Patient bekam bei Aufnahme in die Klinik einen Screening-Fragebogen ausgehändigt, der auf freiwilliger Basis ausgefüllt werden konnte [every patient got a screening questionnaire on admission, to be completed voluntarily]»

**Остальные поля:**
- clinical_group: mixed_psychiatric — Page 24, 3.1; Page 25, Abb. 9 — «Mit 62,4% waren „affektive Störungen“ (F3) am häufigsten vertreten. 30,9% ... (F1) und 21,6% ... (F4) [affective disorders 62.4%, substance 30.9%, neurotic 21.…»
- country: DEU — Page 14, 2.1 — «an der Klinik für Psychiatrie, Psychosomatik und Psychotherapie Bamberg [at the Clinic for Psychiatry, Psychosomatics and Psychotherapy Bamberg]»
- setting: clinic: psychiatric inpatient admissions (central patient admission), single centre, Bamberg — Page 14, 2.1-2.2 — «Die Rekrutierung der Probanden erfolgte über die Zentrale Patientenaufnahme. Jeder Patient bekam bei Aufnahme in die Klinik einen Screening-Fragebogen ausgehän…»
- data_years: 2019-2020 — Page 14, 2.1 — «im Zeitraum vom 16. Dezember 2019 bis zum 6. März 2020 durchgeführt [carried out from 16 December 2019 to 6 March 2020]»
- design: cross-sectional — Page 14, 2.1 — «Die Untersuchung erfolgte als monozentrische Querschnittsstudie in Form von Fragebögen [single-centre cross-sectional questionnaire study]»
- topic_disclosed: yes — Page 14, 2.3.1 — «Dieser „Kurztest Misophonie“ ... erläuterte knapp worum es sich bei Misophonie handelt [this 'short test misophonia' briefly explained what misophonia is]»
- inclusion_exclusion: Inpatients aged >=18 admitted via central admission who agreed to participate; dementia the only exclusion (3 patients removed post hoc based on discharge diagnosis) — Page 14, 2.2; Page 19, 2.3.4 — «Demenz-Diagnosen stellten das einzige Ausschlusskriterium dar. [dementia diagnoses were the only exclusion criterion]»
- n_invited: NR — Page 14, 2.2 — «Jeder Patient bekam bei Aufnahme in die Klinik einen Screening-Fragebogen ausgehändigt [every patient received a questionnaire; number of admissions not report…»
- n_responded: 194 — Page 24, 3.1 — «Es wurden insgesamt 194 Patienten im Alter von 18 bis 87 Jahren gescreent [a total of 194 patients aged 18 to 87 were screened]»
- response_rate: NR — Page 14, 2.2 — «der auf freiwilliger Basis ausgefüllt werden konnte [could be completed voluntarily]»
- age_mean: 46.7 — Page 24, 3.1 — «Das durchschnittliche Alter betrug 46,7 Jahre (Standardabweichung 16,3 Jahre) [mean age 46.7 years (SD 16.3)]»
- age_sd: 16.3 — Page 24, 3.1 — «(Standardabweichung 16,3 Jahre) [SD 16.3 years]»
- age_min: 18 — Page 24, 3.1 — «194 Patienten im Alter von 18 bis 87 Jahren [194 patients aged 18 to 87]»
- age_max: 87 — Page 24, 3.1 — «194 Patienten im Alter von 18 bis 87 Jahren [194 patients aged 18 to 87]»
- age_group: adults — Page 24, 3.1 — «im Alter von 18 bis 87 Jahren [aged 18 to 87]»
- pct_female: 56.2 — Page 24, 3.1 — «davon waren 109 weiblich (56,2%) und 85 männlich (43,8%) [109 female (56.2%), 85 male (43.8%)]»
- informant: self — Page 38, 4.7 — «handelte es sich um eine rein subjektive Befragung [it was a purely subjective (self-report) survey]»
- mode: paper — Page 14, 2.2; Page 14, 2.3.1 — «einen Screening-Fragebogen ausgehändigt [handed a screening questionnaire]; ein weiterer dreiseitiger Fragebogen ... ausgehändigt [a further three-page questio…»
- instruments: Kurztest Misophonie (study's modification of the Misophonia Institute 'Test for Misophonia', German translation by the authors, plus 0-10 impairment item); Misophonia Assessment Questionnaire (MAQ, Johnson/Dozier 2013), German translation by the authors (stage 2, screen-positives only) — Page 14, 2.1 and 2.3.1; Page 15, 2.3.2 — «Sowohl die Screening-Fragen des Misophonie-Instituts, als auch das „Misophonia Assessment Questionnaire“ wurden aus dem Englischen Original ins Deutsche überse…»
- instrument_validated_in_language: no — Page 14, 2.1; Page 22, 2.4.1 — «wurden aus dem Englischen Original ins Deutsche übersetzt und anschließend von einem staatlich geprüften Übersetzer korrigiert [translated into German and corr…»
- pub_status: thesis — Page 1 — «Inaugural – Dissertation zur Erlangung des Doktorgrades der Medizin [inaugural dissertation for the degree of doctor of medicine]»
- language: German — Whole text — «MISOPHONIE BEI PSYCHIATRISCHEN ERKRANKUNGEN [misophonia in psychiatric disorders]»
- funding_coi: NR (no funding or conflict of interest statement); participants not paid — Page 14, 2.2 — «Es erfolgte keine Vergütung der Patienten für die Teilnahme an der Studie. [patients were not paid for participating]»
- notes: Doctoral thesis (Universität Regensburg); ethics approval from Universität Bamberg. Two-stage design: everyone was screened with the Kurztest, and the MAQ was given only to screen-positives. Only 27 of the 46 screen-positives completed it, so MAQ-based prevalence over all screened is not determinable (G10). The Kurztest items (Abb. 3) are not reproduced in the extracted text; their content is described in 2.3.1. It is unclear whether n=194 is counted before or after the 3 post hoc dementia exclusions (most likely after). Patients with several discharge diagnoses count in several diagnostic gr…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Target population is the clinic's adult psychiatric inpatients; the frame was all admissions via central admission — Page 14, 2.2 — «Jeder Patient bekam bei Aufnahme in die Klinik einen Screening-Fragebogen ausgehändigt [every patient received a screening questionnaire on admission]»
2. способ отбора: **yes** — All consecutive admissions in the period were offered screening (census of the frame); participation was voluntary — Page 36, 4 — «wurden alle Patienten der psychiatrischen Klinik in Bamberg ... während des Aufnahmeprozederes mittels des Misophonie Kurztests ... gescreent [all patients wer…»
3. размер выборки: **no** — n=194, below 385 — Page 24, 3.1 — «Es wurden insgesamt 194 Patienten ... gescreent [194 patients screened in total]»
4. описание выборки и условий: **yes** — Age, sex, diagnoses, setting, location and dates all reported — Page 14, 2.1; Page 24, 3.1 — «Das durchschnittliche Alter betrug 46,7 Jahre ... 109 weiblich (56,2%) [mean age 46.7; 109 female]»
5. охват (пропуски): **unclear** — Missing or incomplete screening questionnaires not reported; the primary estimate uses all 194 screened — Page 24, 3.1 — «Es wurden insgesamt 194 Patienten ... gescreent [194 patients screened in total]»
6. валидность определения случая: **no** — Primary estimate comes from an ad hoc screener (Kurztest Misophonie with impairment >=3/10), with no validation in German — Page 16, 2.3.1 — «Für ein positives Screening-Ergebnis musste Frage 1 obligat mit „Ja“ ... Außerdem war ein subjektiver Schweregrad von mindestens „3“ ... vonnöten. [Q1 yes, one…»
7. единое надёжное измерение: **unclear** — Same paper screener and threshold for everyone, but no reliability reported — Page 14, 2.3.1 — «gefolgt von drei dichotom-nominal-skalierten Fragen mit den Antwortmöglichkeiten „Ja“ und „Nein“ [followed by three yes/no questions]»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (46/194); CI calculable — Page 26, 3.1 — «46 Patienten (23,7%) wiesen ein positives Screening auf [46 patients (23.7%) screened positive]»
9. отклик: **unclear** — Number of admitted or invited patients not reported, so response rate unknown — Page 14, 2.2 — «der auf freiwilliger Basis ausgefüllt werden konnte [could be completed voluntarily]»

Правки:
- 

Проверено: да
---

## ST085 · Naylor 2021 · The Psychiatric quarterly

Основной отчёт R1071: [текст](../../fulltext/text/R1071.txt) — «The Prevalence and Severity of Misophonia in a UK Undergraduate Medical Student Population and Validation of the Amsterdam Misophonia Scale.» — [DOI](https://doi.org/10.1007/s11126-020-09825-3)
Расхождения в тексте: The Table 2 bands add up to the denominator: 171+124+40+1+0 = 336. The >=5 count (165/336 = 49.1%) matches the text. Subclinical is 51% in Table 2 and the abstract but 50.9% in the text, a rounding difference. The Table 2 95% CI for moderate is printed as '0.091–0.017', probably a typo (upper bound likely about 0.157). Table 1 item frequencies: item 5 ('control') adds to 333, not 336 (106+114+73+36+4). The means printed for items 3 and 4 (1.10 and 0.80) look swapped against their frequency distributions (about 0.80 and 1.10). The scale is called '7-item', and the text says six items are scored, with a free-text final item. Table 3 is not symmetric (0.356 vs 0.346 for items 3/5). The abstract says moderate 12% and severe 0.3%, matching Table 2.
Заметка ИИ: There is one sample. The estimates are cumulative sums of the A-MISO-S bands from Table 2. The authors' primary estimate is >=5 ('clinically significant'), which is L1. The recommended L2 estimate is >=10: 41/336. JBI item 6 is rated on the L2 definition. Whether the English A-MISO-S counts as validated rests on this report's own factor analysis, so the reviewer should check it.

### ST085-1 · University of Nottingham medical students, GBR, n=336
Отчёты: R1071 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **165 / 336** | 49.1 | Table 2; Results | «Overall, 49.1% (95% CI 0.44–0.55) of the 336 respondents had clinically significant misophonia (scores in the mild to extreme categories (total score: 5–24))» |
| E2 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **41 / 336** | 12.2 | Table 2 | «Moderate (Total Score 10–14) / 40 (12%) ... Severe (Total Score 15–19) / 1 (0.3%) ... Extreme (Total Score 20–24) / 0 (0%)» |
| E3 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **1 / 336** | 0.3 | Table 2 | «Severe (Total Score 15–19) / 1 (0.3%) / 0.00–0.016 Extreme (Total Score 20–24) / 0 (0%)» |
| E4 | all | A-MISO-S · A-MISO-S>=20 | **L2** | **0 / 336** | 0.0 | Table 2; Abstract | «Extreme (Total Score 20–24) / 0 (0%) / 0.00–0.011 (One-sided 97.5% confidence interval)» |

- E1: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; >=5 = L1; у авторов: «clinically significant misophonia»; главная у авторов: yes; период: current; **расчёт: 124 + 40 + 1 + 0 from Table 2 = 165; text reports 49.1% (165/336 = 49.1%)**; заметка: Authors call >=5 'clinically significant'; Table 1 codes it as L1 (cf. Naylor et al. 2021 note).
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; >=10 = L2 (recommended); у авторов: «moderate or more»; главная у авторов: no; период: current; **расчёт: 40 (moderate) + 1 (severe) + 0 (extreme) from Table 2 = 41**; заметка: Recommended L2 definition (G11).
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G2 above L2 cut-off; у авторов: «severe or more»; главная у авторов: no; период: current; **расчёт: 1 (severe) + 0 (extreme) from Table 2 = 1**
- E4: источник порога: developer paper; правило: A-MISO-S row; G1 top band; G2 above L2 cut-off; у авторов: «extreme»; главная у авторов: no; период: current; заметка: Abstract: 'No extreme cases were seen.'

**Ключевые поля выборки:**
- **n_analysed: 336** — Table 2; Results — «Overall, 49.1% (95% CI 0.44–0.55) of the 336 respondents had clinically significant misophonia»
- **population: medical_students** — Participants — «Criteria for inclusion were that participants spoke English, were aged over 18 years and were University of Nottingham medical students.»
- **sampling: convenience** — Participants — «The study was advertised in person (at lectures), by poster advertisement, and on social media sites.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: GBR — Participants — «Participants were recruited from the School of Medicine at the University of Nottingham.»
- setting: university (medical school, University of Nottingham) — Participants — «Participants were recruited from the School of Medicine at the University of Nottingham.»
- data_years: 2019 — Procedure — «Data collection was done between the 22nd of October 2019 and the 4th of November 2019.»
- design: cross-sectional — Design — «A cross-sectional study was used to examine the prevalence of misophonia.»
- topic_disclosed: yes — Participants; Discussion (limitations) — «Selection bias may have affected the results as there is an approximate 40% increase in likelihood for people to cooperate with a study if they are interested …»
- inclusion_exclusion: English-speaking, aged over 18, University of Nottingham medical students; advised not to take part if they might have a severe negative emotional response to the questionnaire content — Participants — «Criteria for inclusion were that participants spoke English, were aged over 18 years and were University of Nottingham medical students. Participants were advi…»
- n_invited: NR — Participants — «The study was advertised in person (at lectures), by poster advertisement, and on social media sites.»
- n_responded: 336 — Results, Descriptive Statistics — «Data was obtained from 336 participants who completed the questionnaire.»
- response_rate: NR — NA — «NR»
- age_mean: NR — Discussion (limitations) — «No data was collected in the respondents age, ethnicity, nor gender.»
- age_sd: NR — Discussion (limitations) — «No data was collected in the respondents age, ethnicity, nor gender.»
- age_min: NR — Participants — «were aged over 18 years»
- age_max: NR — Discussion (limitations) — «No data was collected in the respondents age, ethnicity, nor gender.»
- age_group: adults — Participants — «Criteria for inclusion were that participants spoke English, were aged over 18 years»
- pct_female: NR — Discussion (limitations) — «No data was collected in the respondents age, ethnicity, nor gender.»
- informant: self — Materials — «The Amsterdam Misophonia Scale (A-miso-S) is a 7-item subjective, self-report measure»
- mode: online — Design — «An optional, anonymous, closed online questionnaire was used to assess misophonia prevalence and severity.»
- instruments: A-MISO-S (English) — Materials — «The Amsterdam Misophonia Scale (A-miso-S) is a 7-item subjective, self-report measure which uses a 5-point Likert scale»
- instrument_validated_in_language: yes — Abstract; Factor Structure of the A-Miso-S — «This study has provided new information on misophonia and validity of the A-Miso-S questionnaire in a sample population of UK undergraduate medical students.»
- pub_status: journal — Header — «The Psychiatric quarterly; DOI: 10.1007/s11126-020-09825-3»
- language: English — Full text — «The Prevalence and Severity of Misophonia in a UK Undergraduate Medical Student Population and Validation of the Amsterdam Misophonia Scale»
- funding_coi: Funded by the University of Nottingham; four authors supported by NIHR Biomedical Research Programme; COI stated as N/A — Funding; Acknowledgments; Conflict of Interest — «Funded by the University of Nottingham. ... CC. PS. DJ and DB are supported by the UK National Institute for Health (NIHR) Biomedical Research Programme.»
- notes: Age and sex were not collected for respondents; the 73% female and 97% aged 18-24 describe the whole Nottingham medical student population, not the sample. Topic disclosure is inferred: the misophonia questionnaire was linked from the adverts and the authors discuss self-selection by interest; the advert wording is not quoted. English A-MISO-S validity rests on this report's own factor analysis (alpha 0.814); no separate English validation is cited, so the reviewer should check. Repeat responses could not be ruled out. The authors' 'clinically significant' cut-off (>=5) is L1 under Table 1.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The title claims UK medical students, but recruitment came from one medical school through adverts, with no enrolment list used as the frame — Title; Participants — «Participants were recruited from the School of Medicine at the University of Nottingham. The study was advertised in person (at lectures), by poster advertisem…»
2. способ отбора: **no** — Volunteer opt-in (convenience) sampling via adverts — Participants — «The study was advertised in person (at lectures), by poster advertisement, and on social media sites.»
3. размер выборки: **no** — n = 336 < 385 — Results — «Data was obtained from 336 participants who completed the questionnaire.»
4. описание выборки и условий: **no** — Setting, country and dates are reported, but age and sex of the sample are not (two items missing) — Discussion (limitations) — «No data was collected in the respondents age, ethnicity, nor gender.»
5. охват (пропуски): **yes** — No missing misophonia data among the 336 completers — Analytical Strategy — «There was no missing data to account for.»
6. валидность определения случая: **yes** — Rated on the L2 definition A-MISO-S >=10 (anchored cut-off). English version validated psychometrically in this report; the reviewer should check whether that is enough — Materials; Table 2 — «Scores are categorised into ranges of sub-clinical (0–4), mild [5–9], moderate [10–14], severe [15–19] and extreme [20–24].»
7. единое надёжное измерение: **yes** — Same online self-report A-MISO-S for all participants; Cronbach's alpha reported in this sample — Factor Structure of the A-Miso-S — «A value of 0.814 was obtained for Chronbach’s alpha, this is a measure of agreement across all questions in the questionnaire, I.e. internal consistency.»
8. статистика (числитель и знаменатель): **yes** — Band counts and the denominator are given, with 95% CIs (one CI has a typo) — Table 2 — «Prevalence of clinically significant misophonia was presented as a proportion with 95% confidence interval»
9. отклик: **no** — Open advertised online survey; number invited and response rate not reported; no handling of non-response — Participants — «Advertisements provided participants with a link for anonymous participation in the online questionnaire»

Правки:
- 

Проверено: да
---

## ST086 · Rosenthal 2021 · Frontiers in psychology

Основной отчёт R1086: [текст](../../fulltext/text/R1086.txt) — «Development and Initial Validation of the Duke Misophonia Questionnaire.» — [DOI](https://doi.org/10.3389/fpsyg.2021.709928)
Приложен R0489: [текст](../../fulltext/text/R0489.txt) · [PDF](../../fulltext/pdf/R0489.pdf) — «Development and Initial Validation of the Duke Misophonia Questionnaire»
Связь отчётов: Duke Misophonia Questionnaire development: the ResearchGate record R0489 carries the text of the Frontiers article R1086 (same MTurk Phase 2 sample, n = 424)
Не выписано ИИ: Phase 1a interview: individuals with misophonia (n=10), screened on MQ (mean item >2 and MSS >=7), recruited via the Center's research list and website (E1). Phase 1a interview: family members of people with misophonia (n=10), recruited because of misophonia in the family (E1). Phase 1b item-feedback study: new participants (n=10) who met 'clinical misophonia' on the MQ (E1). Expert panel: professional experts, no data reported (not a sample).
Расхождения в тексте: R0489 contains the same Frontiers article text as R1086; I found no numeric differences. Inside the report: (1) The MQ single severity item is called the 'Impairment Subscale' in Measures/Results and the 'severity scale' elsewhere. (2) Phase 1 screening used mean item '>2' on the MQ Symptom and E&B scales plus MSS >=7. The Phase 2 conservative criterion uses '≥2' on E&B only plus MSS >=7 (n=21). (3) The DMQ Impairment severe range is 39-48 in Results and 39-49 in the Discussion. (4) Sex in Table 1 is 54.5% male / 45.5% female; gender identity is 53.3% male / 45.3% female. pct_female uses sex. (5) The Limitations name A-MISO-S as a measure for future studies, although it was given in this study. (6) 67 + 357 = 424 matches 15.8% (67/424 = 15.80%).
Заметка ИИ: One eligible sample: the MTurk Phase 2 community sample (n=424). Main L2 estimate: MQ MSS >=7, 67/424. Counts for DMQ >=1.8 are not reported (approximate back-calculation is in the note only). The DMQ Impairment-range estimates are E3 because they come from percentiles of this development sample. Data years and funding are not reported.

### ST086-1 · MTurk community adults, USA, n=424 (DMQ development Phase 2)
Отчёты: R1086 (main); R0489

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **67 / 424** | 15.8 | Results (first paragraph); Convergence With Existing Misoph… | «Sixty-seven participants (15.8%) reported "clinically significant symptoms" on the MQ (i.e., ≥ 7 on the impairment subscale (Wu et al., 2014).» |
| E2 | all | MQ · MSS>=7 and MQ Emotions-and-Behaviors mean item score >=2 | **L2** | **21 / 424** | 5.0 | Results, Convergence With Existing Misophonia Scales | «the criterion for determining clinical misophonia status was modified to include individuals with an average item score ≥ 2 on the MQ Emotions and Behaviors Scale and ≥7 on the MQ Severity Scale (n = 21).» |
| E3 | all | DMQ · DMQ Symptom Severity mean item score >=1.8 (total >=41.4) | **L2** | **NR / 424** |  | Results, Convergence With Existing Misophonia Scales; Discu… | «Youden's J index indicated an optimal mean score cut point of 1.8 (total score of 41.4), resulting in a specificity and sensitivity of 0.91 and 1, respectively.» |
| E4 | all | DMQ · DMQ Impairment total >=14 (moderate or more) | **E3** | **67 / 424** | 15.8 | Results, Range for DMQ Impairment Scale Scores | «Scores between 0 and 6 on MQ severity scale ... corresponded with a mean item score of 1.08 on the DMQ Impairment Scale (84.20% of participants scored in this range).» |
| E5 | all | DMQ · DMQ Impairment total >=39 (severe to very severe) | **E3** | **5 / 424** | 1.2 | Results, Range for DMQ Impairment Scale Scores | «The cut point of 10 on the MQ severity scale ... corresponded with a mean item score of 3.17 on the DMQ Impairment scale (with 98.82% participants scoring up to this cut-point).» |
| E6 | all | adhoc · bothered by at least one sound/sight (did not select 'I am not bothered by any sounds') | **L0** | **389 / 424** | 91.7 | Results (after Table 1); Table 2 | «For participants (n = 35) who responded "I am not bothered by any sounds or sights at are as associated with sounds,"» |

- E1: источник порога: developer paper; правило: MQ row; L2 MSS >=7 (recommended); у авторов: «clinically significant symptoms»; главная у авторов: yes; период: NR; заметка: Not a prevalence study; the MQ severity item is called the 'Impairment Subscale' in this paper. Also: '≥ 7 suggests clinical misophonia [n = 67]'.
- E2: источник порога: study's own; правило: MQ row; L2 'MSS >=7 and Emotions-and-Behaviors mean >=2' (G4 combined, both L2); у авторов: «clinical misophonia (conservative criterion)»; главная у авторов: no; период: NR; заметка: This is the Rosenthal et al. 2021 criterion used as reference for the DMQ ROC. Denominator 424 assumed (whole analysed sample).
- E3: источник порога: developer paper; правило: DMQ row; L2 Symptom Severity mean >=1.8; G8 derivation sample (flag); у авторов: «cut point for clinical severity»; главная у авторов: no; период: current; заметка: Count above cut-off not reported. Approximate back-calculation (not entered): 21 true positives + (1-0.91) x 403 non-cases ≈ 36 false positives → about 57/424 (range about 55-59 because specificity is rounded). Cut-off derived by ROC in this same sample (G8).
- E4: источник порога: percentile of this sample; правило: DMQ row; Impairment ranges percentile-based in development sample → E3 (G5); у авторов: «moderate impairment or more»; главная у авторов: no; период: current; **расчёт: (100 - 84.20)% = 15.80% x 424 = 66.99 -> 67**; заметка: Ranges were set on percentiles matched to MQ severity bands, so the share above the moderate cut-off equals the MQ >=7 share by construction. Unclear whether 84.20% refers to the DMQ or the MQ distribution.
- E5: источник порога: percentile of this sample; правило: DMQ row; Impairment ranges percentile-based in development sample → E3 (G5); у авторов: «severe to very severe impairment»; главная у авторов: no; период: current; **расчёт: (100 - 98.82)% = 1.18% x 424 = 5.00 -> 5**; заметка: Share above the cut-point inferred as 100 - 98.82; whether the boundary is inclusive is unclear. Discussion gives severe range as 39-49, Results 39-48.
- E6: источник порога: study's own; правило: adhoc row; any bothersome sound → L0; у авторов: «NR (sound-type item endorsement)»; главная у авторов: no; период: current; **расчёт: 424 - 35 not bothered = 389 (Table 2: 8.3% not bothered)**; заметка: Not presented by the authors as a case definition; listed only as L0 description. Reviewer may drop.

**Ключевые поля выборки:**
- **n_analysed: 424** — Method, Data Integrity Check — «a final sample of 424 participants (53%) passed the stringent data integrity checks and were included in the analyses»
- **population: gp_other** — Abstract — «In Phase 2, a large community sample of adults (n = 424) completed DMQ candidate items and other measures»
- **sampling: convenience** — Method, Participants — «a widely-used crowdsourcing platform that produces data of a similar or higher quality compared to other convenience samples»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — Method, Participants — «potential participants were unobtrusively screened for eligibility criteria of being between 18 and 65 years of age, English fluency and current residence in t…»
- setting: online panel (Amazon Mechanical Turk) — Method, Participants — «Participants (N = 800) were recruited through Amazon's Mechanical Turk (MTurk), a widely-used crowdsourcing platform»
- data_years: NR — Method — «NR»
- design: validation study — Abstract — «the primary purpose of this study was to develop and psychometrically validate a self-report measure of misophonia, the Duke Misophonia Questionnaire (DMQ)»
- topic_disclosed: NR — Method, Participants — «potential participants were unobtrusively screened for eligibility criteria»
- inclusion_exclusion: Age 18-65, English fluency, US residence, MTurk acceptance ratio >=95%; excluded if failed reCAPTCHA or any of 3 attention checks — Method, Participants; Data Integrity Check — «Participants were included only if they had a history on this platform of providing good quality responses (i.e., had an acceptance ratio > = 95%)... only part…»
- n_invited: NR — Method, Participants — «Participants (N = 800) were recruited through Amazon's Mechanical Turk (MTurk)»
- n_responded: 800 — Method, Data Integrity Check — «Of the 800 individuals initially recruited, a final sample of 424 participants (53%) passed the stringent data integrity checks»
- response_rate: NR — Method, Data Integrity Check — «Of the 800 individuals initially recruited, a final sample of 424 participants (53%) passed the stringent data integrity checks»
- age_mean: 37.7 — Table 1 — «Age (mean, SD) | 35 (12.8) | 46.6 (6.6) | 35.3 (12.0) | 37.7 (11.1)»
- age_sd: 11.1 — Table 1 — «Age (mean, SD) | ... | 37.7 (11.1)»
- age_min: 18 — Method, Participants — «eligibility criteria of being between 18 and 65 years of age»
- age_max: 65 — Method, Participants — «eligibility criteria of being between 18 and 65 years of age»
- age_group: adults — Method, Participants — «eligibility criteria of being between 18 and 65 years of age»
- pct_female: 45.5 — Table 1 — «Female | 5 (50) | 7 (70) | 5 (50) | 193 (45.5)»
- informant: self — Method, Measures — «In the current study, this measure was administered as a self-report questionnaire rather than a clinical interview.»
- mode: online — Method, Participants; Data Integrity Check — «recruited through Amazon's Mechanical Turk (MTurk)... Google's reCAPTCHA was used to eliminate automated responses»
- instruments: MQ (English); A-MISO-S (English, self-report); MAQ (English); MAS-I (English); MCRS (English); MERS (English); DMQ candidate item pool (English, developed in this study) — Method, Measures — «Misophonia Questionnaire (MQ; Wu et al., 2014)... Amsterdam Misophonia Scale (A-MISO-S... Misophonia Activation Scale (MAS-I... Misophonia Assessment Questionn…»
- instrument_validated_in_language: yes — Method, Measures — «Initial validation of the MQ demonstrated good internal consistency (α = 0.86–0.89; Wu et al., 2014).»
- pub_status: journal — R0489, Page 1 — «ORIGINAL RESEARCH published: 29 September 2021 doi: 10.3389/fpsyg.2021.709928»
- language: English — Full text — «Development and Initial Validation of the Duke Misophonia Questionnaire»
- funding_coi: Funding NR. COI: MR is a Member of the Scientific Advisory Board for the Misophonia Research Fund; others declare none. — Conflict of Interest — «MR is a Member of the Scientific Advisory Board for the Misophonia Research Fund. The remaining authors declare that the research was conducted in the absence …»
- notes: R0489 (ResearchGate) is the same Frontiers article text and the same sample; no values differ. Age min/max are the eligibility limits; the observed range is NR. 376 of 800 recruited (47%) were excluded for failing data-integrity checks; there is no invited denominator. The paper calls the MQ severity item the 'Impairment Subscale'. The DMQ cut-offs (Symptom Severity >=1.8; Impairment ranges) were derived in this same sample (G8 / G5). MQ data appear complete for all 424 (357 + 67). Overlap with other Duke/Rosenthal MTurk studies (e.g., Cassiello-Robbins et al. 2020/2021) is not stated; check.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is MTurk workers, only part of the US adult community — Method, Participants — «Participants (N = 800) were recruited through Amazon's Mechanical Turk (MTurk)»
2. способ отбора: **no** — Non-probability online crowdsourcing convenience sample — Method, Participants — «produces data of a similar or higher quality compared to other convenience samples»
3. размер выборки: **yes** — n = 424 >= 385 — Method, Data Integrity Check — «a final sample of 424 participants (53%) passed the stringent data integrity checks»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection not reported — Table 1; Method, Participants — «Age (mean, SD) ... 37.7 (11.1)»
5. охват (пропуски): **no** — 376 of 800 recruited (47%) excluded after data-integrity checks, with no comparison of excluded vs included; MQ data complete among the 424 — Method, Data Integrity Check — «Of the 800 individuals initially recruited, a final sample of 424 participants (53%) passed the stringent data integrity checks»
6. валидность определения случая: **yes** — Primary estimate MQ Severity >=7 (L2), English MQ with published validation (Wu 2014) — Method, Measures — «A cut score of seven ("Moderate") or higher on the Impairment Subscale indicates clinically significant misophonia symptomology (Wu et al., 2014).»
7. единое надёжное измерение: **yes** — Same online self-report MQ for all; alpha reported in sample — Method, Measures — «Reliability for the MQ total score in the current sample was excellent (α = 0.90).»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (67/424); CI calculable — Results — «Sixty-seven participants (15.8%) reported "clinically significant symptoms" on the MQ»
9. отклик: **no** — Open MTurk recruitment with no invited denominator; no non-response handling — Method, Participants — «Participants (N = 800) were recruited through Amazon's Mechanical Turk (MTurk)»

Правки:
- 

Проверено: да
---

## ST087 · Sarıgedik 2021 · Psychiatry and Behavioral Sciences

Основной отчёт R1090: [текст](../../fulltext/text/R1090.txt) · [PDF](../../fulltext/pdf/R1090.pdf) — «A Study on Validation of Amsterdam Misophonia Scale in Turkish and Misophonia's Prevalence in Turkish High School/College Student Population» — [DOI](https://doi.org/10.5455/pbs.20210509040627)
Расхождения в тексте: 1) In Table 1 the Total column swaps the sex percentages (Female 1034 '13', Male 154 '87'). The text says 1034 (87%) female, which matches 1034/1188, so pct_female = 87. 2) Table 1 gives 18+ University 552 as '53.8'%; 552/866 = 63.7%. 3) The text gives OCD n=12 as '0.1 %'; 12/1188 = 1.0%. 4) The Discussion gives 57.2% of adolescents at mild or higher; Table 5 gives 186/322 = 57.8% (subclinical 42.2%). Table 5 is used. 5) The Discussion gives 17.2% of adolescents at moderate or higher; Table 5 gives 55/322 = 17.1%. 6) The Discussion cites 'Table 5' for Cronbach's alpha, which is in Table 4. 7) 919 answered the 'most disturbing sound' item, reported as 78.4%, but 919/1188 = 77.4%. Table 3 percentages imply a denominator of about 945. 8) Table 5 totals match the text (527/497/152/12) and add up to 1188. Each item in Table 2 also adds up to 1188.
Заметка ИИ: The report has one eligible sample: an online convenience sample of Turkish high school and university students recruited via social media (n=1188). The primary estimate, as stated by the authors, is A-MISO-S >=10 (L2): 164/1188 = 13.8%. Estimates are also extracted for >=5 (L1) and >=15, for the whole sample and by age group (<18, >=18). No prevalence is given by sex. The Turkish A-MISO-S was validated in this same report (factor analysis and alpha only), so JBI 6 = yes should be checked.

### ST087-1 · Turkish high school and university students, online social-media convenience sample, TUR, n=1188
Отчёты: R1090 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **164 / 1188** | 13.8 | Page 4, Table 5; Abstract | «Moderate (10-14) ... 152 12.8 Severe (15-19) ... 12 1 Extreme (20-24) ... 0 0; Moderate or more severe misophonia symptoms were seen in 13.8% of participants.» |
| E2 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **661 / 1188** | 55.6 | Page 4, Table 5 | «Of the participants, 527 (44.4%) were subclinic, 497 (41.8%) had mild, 152 (12.8%) had moderate and 12 (1%) had severe misophonia.» |
| E3 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **12 / 1188** | 1.0 | Page 4, Table 5 | «12 (1%) had severe misophonia. Nobody has been identified with extreme misophonia.» |
| E4 | under 18 | A-MISO-S · A-MISO-S>=10 | **L2** | **55 / 322** | 17.1 | Page 4, Table 5; Page 6, Discussion | «Moderate (10-14) 50 15.5 ... Severe (15-19) 5 1.6; 17.2% of adolescents ... had moderate and severe misophonia symptoms» |
| E5 | under 18 | A-MISO-S · A-MISO-S>=5 | **L1** | **186 / 322** | 57.8 | Page 4, Table 5; Page 5, Discussion | «Mild (Score 5-9) 131 40.7 ... Moderate (10-14) 50 15.5 ... Severe (15-19) 5 1.6; 57.2 % of the adolescent group ... showed mild or higher misophonia symptoms» |
| E6 | under 18 | A-MISO-S · A-MISO-S>=15 | **L2** | **5 / 322** | 1.6 | Page 4, Table 5 | «Severe (15-19) 5 1.6 ... Extreme (20-24) 0 0» |
| E7 | 18 and over | A-MISO-S · A-MISO-S>=10 | **L2** | **109 / 866** | 12.6 | Page 4, Table 5; Page 6, Discussion | «Moderate (10-14) ... 102 11.8 Severe (15-19) ... 7 0.8; 12.6% of adults had moderate and severe misophonia symptoms» |
| E8 | 18 and over | A-MISO-S · A-MISO-S>=5 | **L1** | **475 / 866** | 54.8 | Page 4, Table 5; Page 5, Discussion | «Mild (Score 5-9) ... 366 42.3 ... 102 11.8 ... 7 0.8; 54.8% of the adult group showed mild or higher misophonia symptoms» |
| E9 | 18 and over | A-MISO-S · A-MISO-S>=15 | **L2** | **7 / 866** | 0.8 | Page 4, Table 5 | «Severe (15-19) ... 7 0.8 ... Extreme (20-24) ... 0 0» |

- E1: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (moderate+severe+extreme); у авторов: «moderate or more severe misophonia symptoms»; главная у авторов: yes; период: current; **расчёт: 152 + 12 + 0 from Table 5 (Total); 164/1188 = 13.8%**; заметка: Time frame of the scale: now and the past week (7 days).
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (mild+moderate+severe+extreme); у авторов: «mild or higher misophonia symptoms»; главная у авторов: no; период: current; **расчёт: 497 + 152 + 12 + 0 from Table 5 (Total); 661/1188 = 55.6%**
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (severe+extreme); G2 above L2 cut-off; у авторов: «severe misophonia»; главная у авторов: no; период: current; **расчёт: 12 + 0 from Table 5 (Total)**
- E4: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (moderate+severe+extreme); у авторов: «moderate and severe misophonia symptoms»; главная у авторов: no; период: current; **расчёт: 50 + 5 + 0 from Table 5 (Under 18); 55/322 = 17.1%**; заметка: Authors report 17.2%; counts give 17.1% (15.5 + 1.6 = 17.1). Age band roughly 15-17.
- E5: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (mild+moderate+severe+extreme); у авторов: «mild or higher misophonia symptoms»; главная у авторов: no; период: current; **расчёт: 131 + 50 + 5 + 0 from Table 5 (Under 18); 186/322 = 57.8%**; заметка: Discussion says 57.2%; Table 5 counts give 57.8% (100 - 42.2).
- E6: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (severe+extreme); G2; у авторов: «severe misophonia»; главная у авторов: no; период: current; **расчёт: 5 + 0 from Table 5 (Under 18)**
- E7: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (moderate+severe+extreme); у авторов: «moderate and severe misophonia symptoms»; главная у авторов: no; период: current; **расчёт: 102 + 7 + 0 from Table 5 (18 years and older); 109/866 = 12.6%**
- E8: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (mild+moderate+severe+extreme); у авторов: «mild or higher misophonia symptoms»; главная у авторов: no; период: current; **расчёт: 366 + 102 + 7 + 0 from Table 5 (18 years and older); 475/866 = 54.8%**
- E9: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (severe+extreme); G2; у авторов: «severe misophonia»; главная у авторов: no; период: current; **расчёт: 7 + 0 from Table 5 (18 years and older)**

**Ключевые поля выборки:**
- **n_analysed: 1188** — Page 4, Table 5 — «Total (n=1188)»
- **population: school_pupils** — Page 3, Table 1 — «Highschool 318 99.4 314 36.2 634 53.4 University / Master / Doctorate 2 0.6 552 53.8 554 46.6»
- **sampling: convenience** — Page 2, Methods — «Access to the participants was provided with convenience sampling method via social media»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Title; Page 6, Discussion — «we found that in the Turkish population, 17.2% of adolescents and 12.6% of adults had moderate and severe misophonia symptoms»
- setting: online (social media pages used by high school and university students); students — Page 2, Methods — «Access to the participants was provided with convenience sampling method via social media, through the pages frequently used by high school and university stud…»
- data_years: 2020 — Page 2, Methods — «collected from a total of 1188 high school and university students between December 21-30, 2020»
- design: validation study — Abstract, Objective — «This study aims to validate Amsterdam Misophonia Scale (A-MISO-S) into Turkish and detect prevalence in the young population.»
- topic_disclosed: yes — Page 2, Methods; Page 5, Discussion — «they were first informed about the purpose of the study ... those who volunteered to participate in the study on misophonia were more sensitive to it»
- inclusion_exclusion: High school and university students reached via social media who gave online consent and completed the scale; no other criteria reported — Page 2, Methods; Page 3, Results — «The mean age of 1188 people who participated in our study and completed the scale was 18.9 ± 2.4 years»
- n_invited: NR — Page 2, Methods — «Access to the participants was provided with convenience sampling method via social media»
- n_responded: 1188 — Page 3, Results — «The mean age of 1188 people who participated in our study and completed the scale»
- response_rate: NR — Page 2, Methods — «sent to the participants online»
- age_mean: 18.9 — Page 3, Results — «was 18.9 ± 2.4 years»
- age_sd: 2.4 — Page 3, Results — «was 18.9 ± 2.4 years»
- age_min: 15 — Page 5, Discussion; Abstract — «this research provides information including misophonia in the 15-18 year-old age group»
- age_max: NR — NR
- age_group: mixed — Page 3, Table 1 — «Under 18 years (n=322) 18 years and older (n=866)»
- pct_female: 87 — Page 3, Results — «1034 (87 %) of them are female»
- informant: self — Page 2, Measures; Page 6, limitations — «the fact that no clinical interview was conducted and the self-report method was used»
- mode: online — Abstract, Methods — «Turkish version of A-MISO-S and socio-demographic questionnaire was applied online.»
- instruments: A-MISO-S, Turkish version (translated and back-translated in this study; full Turkish text in appendix) — Page 2, Methods/Measures; Pages 8-9 — «the scale was independently translated by three language experts and two Turkish researchers. Then, the Turkish version was retranslated into English»
- instrument_validated_in_language: yes — Page 2, Measures; Page 6-7, Conclusion — «Turkish validity and reliability of it is not established yet. ... This study revealed that the Turkish version of the A-MISO-S scale is valid and reliable in …»
- pub_status: journal — Page 1, header — «Psychiatry and Behavioral Sciences 2021;11(4):258-266»
- language: English — Page 1 — «A Study on Validation of Amsterdam Misophonia Scale in Turkish and Misophonia's Prevalence in Turkish High School/College Student Population»
- funding_coi: No funding; authors declare no conflicts of interest — Page 7 — «Conflict of Interest: The authors have no conflicts of interest to declare. Funding: The authors declared that this study had received no financial support.»
- notes: The Turkish A-MISO-S validation is this report itself (single-factor EFA, Cronbach alpha 0.838; no criterion validation against interview), so validity of the Turkish version rests on the same sample. Population code: 53.4% high school, 46.6% university students; 314 of the 866 participants aged 18+ are coded as high school (oddly). Recruitment via student social-media pages, not through schools. Authors say self-selection of people sensitive to sounds may have inflated prevalence. No prevalence by sex or psychiatric status (only mean scores). Page 1 has leftover header lines with an unrelate…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is Turkish high school/university students ('general young population'); the frame was student social-media pages, which covers only part of it — Page 2, Methods; Page 6 — «via social media, through the pages frequently used by high school and university students ... provides information about the general young population»
2. способ отбора: **no** — Convenience sampling via social media, voluntary opt-in — Page 2, Methods — «Access to the participants was provided with convenience sampling method via social media»
3. размер выборки: **yes** — n = 1188 >= 385 — Page 4, Table 5 — «Total (n=1188)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates all reported — Page 2-3, Methods/Results — «between December 21-30, 2020 ... mean age ... 18.9 ± 2.4 years; 1034 (87 %) of them are female»
5. охват (пропуски): **unclear** — Only people who completed the scale are described; how many started the survey and dropped out is not reported — Page 3, Results — «1188 people who participated in our study and completed the scale»
6. валидность определения случая: **yes** — Primary estimate is A-MISO-S >=10 (L2) using the Turkish version validated in this report (structural validity and reliability only; flag) — Abstract; Page 4, Table 5 — «Moderate or more severe misophonia symptoms were seen in 13.8% of participants.»
7. единое надёжное измерение: **yes** — Same self-report online instrument and thresholds for everyone; Cronbach alpha reported in the sample — Page 4 — «A value of 0.838 was obtained for Cronbach's alpha which is conducted for internal consistency»
8. статистика (числитель и знаменатель): **yes** — Band counts and denominators in Table 5; no CI given for prevalence but one can be calculated; no weights needed — Page 4, Table 5 — «Moderate (10-14) ... 152 12.8 Severe (15-19) ... 12 1»
9. отклик: **no** — Open online survey with no denominator of invited people; response rate not calculable and not handled — Page 2, Methods — «Access to the participants was provided with convenience sampling method via social media»

Правки:
- 

Проверено: да
---

## ST088 · Vitoratou 2021 · Audiology research

Основной отчёт R1101: [текст](../../fulltext/text/R1101.txt) — «Item Response Theory Investigation of Misophonia Auditory Triggers.» — [DOI](https://doi.org/10.3390/audiolres11040051)
Не выписано ИИ: Misophonia specific sample (MS), n = 613 (incl. test-retest subsample N = 42): recruited through misophonia support groups on social media (Facebook, Reddit), and all identified as having misophonia. Excluded as E1 (recruited because of misophonia).
Расхождения в тексте: The MNS self-identification counts are internally consistent: 106 + 54 + 42 = 202, and 52.5 + 26.7 + 20.8 = 100%. MNS gender adds up to 98.5% (77.2 + 16.8 + 4.5), so 1.5% is unaccounted for. The female share in the M+ and M− subgroups (84.8% and 84.6%) is higher than the 77.2% for the whole MNS. Section 2.5 says the test-retest results are in Table 2, but they are actually in Table 1. These points do not affect the prevalence numbers.
Заметка ИИ: One eligible sample (MNS, n = 202) with one L1 ad hoc self-identification estimate (106/202). The S-Five, MQ and A-MISO-S were given, but no scale-based case counts are reported here; they may be in the S-Five validation report (Vitoratou et al.), which comes from the same study and may share participants.

### ST088-1 · Misophonia non-specific sample (MNS), general social-media call, S-Five study wave 2, n=202
Отчёты: R1101 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-identified misophonia (yes/no/unsure item; 'yes') | **L1** | **106 / 202** | 52.5 | 3.1 Sample: Demographic and Clinical Characteristics | «In the MNS, 106 (52.5%) individuals stated that they identified as having misophonia, 54 (26.7%) stated that they do not have misophonia, and 42 (20.8%) said they were unsure if they had misophonia.» |

- E1: источник порога: study's own; правило: adhoc row: self-identified misophonia -> L1 (no scale-based L1 estimate reported, G11); у авторов: «identified as having misophonia»; главная у авторов: no; период: current; заметка: A further 42 (20.8%) were unsure. The authors do not present this as a prevalence estimate. The topic was disclosed (sound-sensitivity study), so self-selection is likely to inflate the figure.

**Ключевые поля выборки:**
- **n_analysed: 202** — 3.1 — «In the MNS, 106 (52.5%) individuals stated that they identified as having misophonia, 54 (26.7%) stated that they do not have misophonia, and 42 (20.8%) said they were unsure»
- **population: gp_other** — 2.1 Sample — «came from a general call in social media by the authors»
- **sampling: convenience** — 2.1 Sample — «came from a general call in social media by the authors (using both personal and professional handles)»

**Остальные поля:**
- clinical_group: NA — NA
- country: NR — 2.1 Sample; Institutional Review Board Statement — «came from a general call in social media by the authors (using both personal and professional handles)»
- setting: online: general call on social media (authors' personal and professional handles) — 2.1 Sample — «The second sample, hereafter the misophonia non-specific sample (MNS), came from a general call in social media by the authors»
- data_years: NR — Institutional Review Board Statement — «REC Reference Number: HR-19/20-17173 and date of approval 5 February 2020»
- design: validation study — 2.2 Measures — «This study was part of a larger study validating a new tool for measuring misophonia, the selective sound sensitivity syndrome scale (S-Five)»
- topic_disclosed: yes — 2.1 Sample — «Data were collected from two populations as part of the Selective Sound Sensitivity Syndrome Study [22] during the second sampling wave.»
- inclusion_exclusion: Aged >=18 and fluent in English; excluded: severe learning disability — 2.1 Sample — «Inclusion criteria were being at least 18 years old and fluent in English. Having a severe learning disability was the only exclusion criterion.»
- n_invited: NR — 2.1 Sample — «came from a general call in social media»
- n_responded: 202 — 3.1 — «The mean age of the misophonia non-specific sample (MNS; N = 202)»
- response_rate: NR — 2.1 Sample — «came from a general call in social media»
- age_mean: 33.8 — 3.1 — «was 33.8 years (sd = 11.5, median = 31, min = 18 and max = 71 years)»
- age_sd: 11.5 — 3.1 — «(sd = 11.5, median = 31, min = 18 and max = 71 years)»
- age_min: 18 — 3.1 — «min = 18 and max = 71 years»
- age_max: 71 — 3.1 — «min = 18 and max = 71 years»
- age_group: adults — 2.1 Sample — «Inclusion criteria were being at least 18 years old»
- pct_female: 77.2 — 3.1 — «77.2% identified as "female", 16.8% as "male" and 4.5% as "other"»
- informant: self — Abstract — «completed self-report measures»
- mode: online — 2.1 Sample — «All participants completed online forms after reading an information sheet about the study»
- instruments: Self-identification item 'Do you identify as having misophonia?' (yes/no/unsure), English; S-Five (English); MQ (English); A-MISO-S (English); 35-item trigger list (FITS/TES), English. Only the self-identification item yields a misophonia frequency in this report — 2.2 Measures — «included two more tools to assess misophonia, the Misophonia Questionnaire (MQ) [12] the Amsterdam Misophonia Scale (A-MISO-S) [11]... "Do you identify as havi…»
- instrument_validated_in_language: no — 2.2 Measures — «To establish whether someone self-identified as having misophonia, we asked "Do you identify as having misophonia?"»
- pub_status: journal — Header — «Venue: Audiology research; DOI: 10.3390/audiolres11040051»
- language: English — Full text — «Item Response Theory Investigation of Misophonia Auditory Triggers»
- funding_coi: BRC for Mental Health at SLaM NHS FT and King's College London; Wellcome Trust (102176/B/13/Z). No conflict of interest declared. — Funding; Conflicts of Interest — «funded or partially funded by the Biomedical Research Centre for Mental Health at South London and Maudsley NHS Foundation Trust and King's College London... W…»
- notes: Sample from the second wave of the Selective Sound Sensitivity Syndrome (S-Five) study (ref 22, Vitoratou et al.), so it may overlap with the general-population sample of the S-Five validation report. Check for double counting. The S-Five, MQ and A-MISO-S were given, but this report gives no scale-based case counts, so the only estimate is self-identification. The authors call these 'pilot data' and say the sample is not representative (recruited via social media). Country of participants is not reported (King's College London study). Gender adds up to 98.5% (1.5% unaccounted).

**Риск смещения (JBI):**
1. рамка выборки: **no** — A social-media call covers only social-media users reached by the authors, not the general population — 2.1 Sample; 4. Discussion — «Future studies would also benefit from using samples representative of the general population, rather than recruited via social media, as in the present study.»
2. способ отбора: **no** — Volunteer opt-in convenience sample — 2.1 Sample — «came from a general call in social media by the authors (using both personal and professional handles)»
3. размер выборки: **no** — n = 202 < 385 — 3.1 — «misophonia non-specific sample (MNS; N = 202)»
4. описание выборки и условий: **no** — Age, sex and setting are reported, but country and dates of data collection are not — 3.1 — «The mean age of the misophonia non-specific sample (MNS; N = 202) was 33.8 years»
5. охват (пропуски): **yes** — All 202 answered the self-identification item (106 + 54 + 42 = 202) — 3.1 — «106 (52.5%) ... 54 (26.7%) ... and 42 (20.8%) said they were unsure»
6. валидность определения случая: **no** — Ad hoc self-identification item — 2.2 Measures — «"Do you identify as having misophonia?", with the option of yes, no or unsure»
7. единое надёжное измерение: **unclear** — Same online item for everyone, but no reliability reported for the self-identification item (test-retest only for trigger items in the MS sample) — 2.1; 2.5 — «All participants completed online forms»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (106/202); CI calculable; no weighting needed — 3.1 — «In the MNS, 106 (52.5%) individuals stated that they identified as having misophonia»
9. отклик: **no** — Open online social-media call with no denominator of people invited — 2.1 Sample — «came from a general call in social media by the authors»

Правки:
- 

Проверено: да
---

## ST089 · Assunção 2020 · Estudo Geral (Universidad de Coimbra)

Основной отчёт R1137: [текст](../../fulltext/text/R1137.txt) · [PDF](../../fulltext/pdf/R1137.pdf) — «THE RELATION BETWEEN MISOPHONIA AND DEPRESSIVE SYMPTOMS: OBSERVATIONAL STUDY»
Приложен R1146: [текст](../../fulltext/text/R1146.txt) · [PDF](../../fulltext/pdf/R1146.pdf) — «Misophonia: Coping Mechanisms and Impact on Daily Life»
Связь отчётов: Two Coimbra master's theses on the same 44 patients (primary care, Aveiro; psychiatric outpatients, Coimbra; Oct-Nov 2018)
Не выписано ИИ: No group was recruited for misophonia. The pilot group used to test the Portuguese A-MISO-S trial version is not extracted because it has no data and its size is not reported ("Investigators applied this trial version to a group of people"). The second part of R1146, which covers only the 11 participants with A-MISO-S >=5, is not a separate sample.
Расхождения в тексте: The two settings were recruited separately (family physician invited patients in primary care; the investigator approached psychiatric outpatients), so they are extracted as two samples. The authors' main figure is for both combined: 11/44 (25%) at A-MISO-S>=5. Combined counts from Table II: none 22, 1-4 11, 5-9 8, 10-14 3, >=15 0, which gives >=1 22/44, >=10 3/44 and >=15 0/44. Sex subgroups are reported only combined: female 10/36, male 1/8. Depression subgroups are also only combined: HAM-D 0-7 gives 5/26, HAM-D>=8 gives 6/18. If the reviewer prefers to treat this as one sample, these are the figures to use. The setting counts in R1137 Tables II and IV agree with R1146 Table III (primary care 15/3/2, secondary care 18/5/1). R1146 states the weekdays the other way round ("Mondays to Fridays in secondary... Mondays to Thursdays on secondary"); R1137 gives primary care Mon-Fri and psych…
Заметка ИИ: Both theses report the same 44 participants interviewed in Oct-Nov 2018, so there is a single study with no double counting. A-MISO-S was given by an interviewer in a Portuguese version translated for this study and not validated.

### ST089-1 · Primary care attenders, USF Barrinha, Aveiro, Portugal, n=20
Отчёты: R1137 (main); R1146

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=1 (score >0) | **L0** | **12 / 20** | 60.0 | Table IV, p.13 | «Subclinic [1-4] 7 35 ... Mild [5-9] 3 15 ... Moderate [10-14] 2 10 ... Severe [15-19] 0 0 ... Extreme [20-24] 0 0» |
| E2 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **5 / 20** | 25.0 | Results p.12; Table IV p.13 | «Of people from primary healthcare group, ... 25% (n=5) reveal clinically significant misophonic symptoms.» |
| E3 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **2 / 20** | 10.0 | Table IV, p.13 | «Moderate [10-14] 2 10 ... Severe [15-19] 0 0 ... Extreme [20-24] 0 0» |
| E4 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **0 / 20** | 0.0 | Table IV, p.13 | «Severe [15-19] 0 0 ... Extreme [20-24] 0 0» |

- E1: источник порога: study's own; правило: A-MISO-S row; G2 below L1 cut-off (subclinical range) -> L0; G1 sum of bands; у авторов: «people who affirm reacting negatively to misophonic sounds»; главная у авторов: no; период: past month; **расчёт: Subclinic 7 + mild 3 + moderate 2 + severe 0 + extreme 0 from Table IV**; заметка: The >0 definition is used in Table IX for correlations
- E2: источник порога: developer paper; правило: A-MISO-S row; L1 >=5; у авторов: «clinically significant misophonic symptoms»; главная у авторов: yes; период: past month; заметка: Interviewer-administered (G7). The authors' main estimate is for both settings combined (11/44).
- E3: источник порога: developer paper; правило: A-MISO-S row; L2 >=10; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: past month; **расчёт: Moderate 2 + severe 0 + extreme 0 from Table IV**
- E4: источник порога: developer paper; правило: A-MISO-S row; G2 above L2 cut-off -> L2; G1 sum of bands; у авторов: «severe or more»; главная у авторов: no; период: past month; **расчёт: Severe 0 + extreme 0 from Table IV**; заметка: A-MISO-S>=20 is also 0/20

**Ключевые поля выборки:**
- **n_analysed: 20** — Table IV, p.13 — «Total 20 100»
- **population: other_nonclinical** — Methods, Sample and recruitment p.9 — «in primary health care, that could represent general population»
- **sampling: convenience** — Methods, p.10 — «In the primary healthcare institution, their attributed Family Physician invited available patients to participate.»

**Остальные поля:**
- clinical_group: NA — NA
- country: PRT — Methods, Sample and recruitment, p.10 — «Data were collected between October 2018 and November 2018 in primary healthcare in Aveiro and secondary care in Coimbra.»
- setting: clinic: primary health care (family health unit, USF Barrinha, Aveiro) — p.10; Acknowledgments p.22 — «in primary healthcare in Aveiro ... Unidade de Saúde Familiar da Barrinha»
- data_years: 2018 — Methods, p.10 — «Data were collected between October 2018 and November 2018»
- design: cross-sectional — Title page / Methods p.10 — «The relation between Misophonia and depressive symptoms: observational study»
- topic_disclosed: yes — Methods, Instruments p.10; Appendix I p.25 — «In a first instance, patients were elucidated on what Misophonia is, trigger sounds examples, and reactions to them.»
- inclusion_exclusion: Included: >=18 years, Portuguese nationality. Excluded: communication inability, severe cognitive deficits, psychosis. — Methods, p.10 — «The inclusion criteria included ≥ 18 years old people and portuguese nationality. Exclusion criteria used were communication inability, severe cognitive defici…»
- n_invited: NR — NR
- n_responded: 20 — Results, p.11 — «n=20 (45%) in primary healthcare»
- response_rate: NR — NR
- age_mean: NR — Table I, p.11 — «Age Mean=48 ... Range = 19-74 (whole sample n=44 only)»
- age_sd: NR — Table I, p.11 — «1SD = ±16,9»
- age_min: NR — Table I, p.11 — «Range = 19-74»
- age_max: NR — Table I, p.11 — «Range = 19-74»
- age_group: adults — Methods, p.10 — «The inclusion criteria included ≥ 18 years old people»
- pct_female: NR — Table I, p.11 — «Gender Female 36 82»
- informant: self — Methods p.9; R1146 p.12 — «this scale was transformed into an instrument to be completed by the researcher»
- mode: face-to-face interview — Methods, Instruments p.10; Ethics p.10 — «The study was based on a structured clinical interview (Appendix II). ... Interviews were performed in doctor's offices»
- instruments: A-MISO-S, Portuguese interviewer-administered version translated/back-translated by the study team; adapted checklist items from MAQ, MCR, MER and MIS (Portuguese, given only if A-MISO-S >=5; R1146) — Methods p.9; R1146, p.10-12 — «we obtained a final Portuguese language version of the scale»
- instrument_validated_in_language: no — Methods, p.9 — «A-MISO-S is a non-validated scale, therefore there is no portuguese version.»
- pub_status: thesis — Page 1 — «MESTRADO INTEGRADO EM MEDICINA – TRABALHO FINAL»
- language: English (abstract also in Portuguese; appendices in Portuguese) — Pages 4-6, 26-33 — «ABSTRACT ... RESUMO»
- funding_coi: NR (no funding or COI statement) — Acknowledgments p.22 — «I also show my gratitude to the Unidade Psiquiátrica Privada de Coimbra and to Unidade de Saúde Familiar da Barrinha»
- notes: Master's thesis (title page dated Feb 2019). Same 44 participants as R1146 (Cruz, coping thesis); the results agree. Demographics are reported only for the combined 44 (mean age 48, SD 16.9, range 19-74; 82% female). 20% of this group were on psychiatric medication; 25% (5/20) had HAM-D>=8. The authors' main figure is combined across both settings (11/44, 25%); sex subgroups are also only combined (female 10/36, male 1/8). Two interviewers (medical students).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Available patients of a single family health unit; does not cover the general population the authors claim it represents. — Methods p.9-10 — «their attributed Family Physician invited available patients to participate»
2. способ отбора: **no** — Convenience: available patients invited on days of researcher availability. — Methods p.10 — «from Monday to Friday, and in the second from Monday to Thursday, according to the availability of researchers»
3. размер выборки: **no** — n=20 < 385. — Results p.11 — «n=20 (45%) in primary healthcare»
4. описание выборки и условий: **no** — Setting, country and dates given, but age and sex are reported only for the combined 44, not for this sample. — Table I p.11 — «Table I - Demographic data of the sample (n=44).»
5. охват (пропуски): **yes** — All 20 participants have A-MISO-S data. — Table IV p.13 — «Total 20 100»
6. валидность определения случая: **no** — The L2 definition (A-MISO-S>=10) is used in a Portuguese version with no published validation. — Methods p.9 — «A-MISO-S is a non-validated scale, therefore there is no portuguese version.»
7. единое надёжное измерение: **yes** — Same scripted interview and thresholds for everyone; Cronbach alpha 0.835 reported (two interviewers). — Table X p.17 — «Cronbach's Alpha 0,835»
8. статистика (числитель и знаменатель): **yes** — Band counts and denominator given; CI calculable. — Table IV p.13 — «25% (n=5) reveal clinically significant misophonic symptoms»
9. отклик: **unclear** — Number invited or refusing not reported. — Methods p.10 — «Family Physician invited available patients to participate»

Правки:
- 

Проверено: да
### ST089-2 · Psychiatric outpatients, private psychiatric unit, Coimbra, Portugal, n=24
Отчёты: R1137 (main); R1146

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=1 (score >0) | **L0** | **10 / 24** | 41.7 | Table IV, p.13 | «Subclinic [1-4] 4 17 ... Mild [5-9] 5 21 ... Moderate [10-14] 1 4 ... Severe [15-19] 0 0 ... Extreme [20-24] 0 0» |
| E2 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **6 / 24** | 25.0 | Results p.12; Table IV p.13 | «of people from psychiatric outpatient setting, ... 25% (n=6) present clinically significant misophonic symptoms» |
| E3 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **1 / 24** | 4.2 | Table IV, p.13 | «Moderate [10-14] 1 4 ... Severe [15-19] 0 0 ... Extreme [20-24] 0 0» |
| E4 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **0 / 24** | 0.0 | Table IV, p.13 | «Severe [15-19] 0 0 ... Extreme [20-24] 0 0» |

- E1: источник порога: study's own; правило: A-MISO-S row; G2 below L1 cut-off -> L0; G1 sum of bands; у авторов: «people who affirm reacting negatively to misophonic sounds»; главная у авторов: no; период: past month; **расчёт: Subclinic 4 + mild 5 + moderate 1 + severe 0 + extreme 0 from Table IV**
- E2: источник порога: developer paper; правило: A-MISO-S row; L1 >=5; у авторов: «clinically significant misophonic symptoms»; главная у авторов: yes; период: past month; заметка: Interviewer-administered (G7). The authors' main estimate is combined (11/44).
- E3: источник порога: developer paper; правило: A-MISO-S row; L2 >=10; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: past month; **расчёт: Moderate 1 + severe 0 + extreme 0 from Table IV**
- E4: источник порога: developer paper; правило: A-MISO-S row; G2 above L2 cut-off -> L2; G1; у авторов: «severe or more»; главная у авторов: no; период: past month; **расчёт: Severe 0 + extreme 0 from Table IV**; заметка: A-MISO-S>=20 is also 0/24

**Ключевые поля выборки:**
- **n_analysed: 24** — Table IV p.13 — «Total 24 100»
- **population: clinical** — Methods p.9 — «in psychiatric outpatient setting»
- **sampling: convenience** — Methods p.10 — «In psychiatric healthcare, the distribution was made only by the investigator before or after participants appointments.»

**Остальные поля:**
- clinical_group: mixed_psychiatric — Results p.12, p.14 — «100% of people from psychiatric outpatient setting group ... were taking psychiatric medication»
- country: PRT — Methods p.10 — «in primary healthcare in Aveiro and secondary care in Coimbra»
- setting: clinic: psychiatric outpatient (secondary care; Unidade Psiquiátrica Privada de Coimbra) — p.9-10; Acknowledgments p.22 — «in psychiatric outpatient setting, where would be expected to find higher rates of people with depressive symptoms»
- data_years: 2018 — Methods p.10 — «Data were collected between October 2018 and November 2018»
- design: cross-sectional — Title page — «The relation between Misophonia and depressive symptoms: observational study»
- topic_disclosed: yes — Methods p.10; Appendix I p.25 — «Título do Estudo: Misofonia - a relação com sintomas depressivos, mecanismos de coping e impacto na vida diária [Study title: Misophonia - the relation with de…»
- inclusion_exclusion: Included: >=18 years, Portuguese nationality. Excluded: communication inability, severe cognitive deficits, psychosis. — Methods p.10 — «Exclusion criteria used were communication inability, severe cognitive deficits, and psychosis.»
- n_invited: NR — NR
- n_responded: 24 — Results p.11 — «n=24 (55%) were interviewed in psychiatric outpatient setting»
- response_rate: NR — NR
- age_mean: NR — Table I p.11 — «Age Mean=48 (whole sample n=44 only)»
- age_sd: NR — Table I p.11 — «1SD = ±16,9»
- age_min: NR — Table I p.11 — «Range = 19-74»
- age_max: NR — Table I p.11 — «Range = 19-74»
- age_group: adults — Methods p.10 — «The inclusion criteria included ≥ 18 years old people»
- pct_female: NR — Table I p.11 — «Gender Female 36 82»
- informant: self — Methods p.9 — «this scale was transformed into an instrument to be completed by the researcher»
- mode: face-to-face interview — Methods p.10 — «The study was based on a structured clinical interview (Appendix II).»
- instruments: A-MISO-S, Portuguese interviewer-administered version translated/back-translated by the study team; adapted checklist items from MAQ, MCR, MER and MIS (Portuguese, given only if A-MISO-S >=5; R1146) — Methods p.9; R1146, p.10-12 — «we obtained a final Portuguese language version of the scale»
- instrument_validated_in_language: no — Methods p.9 — «A-MISO-S is a non-validated scale, therefore there is no portuguese version.»
- pub_status: thesis — Page 1 — «MESTRADO INTEGRADO EM MEDICINA – TRABALHO FINAL»
- language: English (abstract also in Portuguese; appendices in Portuguese) — Pages 4-6, 26-33 — «ABSTRACT ... RESUMO»
- funding_coi: NR (no funding or COI statement) — Acknowledgments p.22 — «I also show my gratitude to the Unidade Psiquiátrica Privada de Coimbra»
- notes: Same 44 participants as R1146. Diagnoses are not reported; 54% (13/24) had HAM-D>=8; all were on psychiatric medication; psychosis was excluded. Demographics are reported only for the combined 44. The authors' main figure is combined (11/44); sex and depression subgroups are only combined (female 10/36, male 1/8; HAM-D 0-7: 5/26 at >=5; HAM-D>=8: 6/18 at >=5).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Patients of one private psychiatric unit seen on days the researchers were available; not consecutive patients. — Methods p.10 — «from Monday to Thursday, according to the availability of researchers»
2. способ отбора: **no** — Convenience distribution by the investigator. — Methods p.10 — «the distribution was made only by the investigator before or after participants appointments»
3. размер выборки: **no** — n=24 < 139 (clinical). — Results p.11 — «n=24 (55%) were interviewed in psychiatric outpatient setting»
4. описание выборки и условий: **no** — Age and sex reported only for combined 44, not for this sample. — Table I p.11 — «Table I - Demographic data of the sample (n=44).»
5. охват (пропуски): **yes** — All 24 have A-MISO-S data. — Table IV p.13 — «Total 24 100»
6. валидность определения случая: **no** — The L2 definition (A-MISO-S>=10) is used in a Portuguese version with no published validation. — Methods p.9 — «A-MISO-S is a non-validated scale, therefore there is no portuguese version.»
7. единое надёжное измерение: **yes** — Same scripted interview for all; Cronbach alpha 0.835. — Table X p.17 — «Cronbach's Alpha 0,835»
8. статистика (числитель и знаменатель): **yes** — Band counts and denominator given. — Table IV p.13 — «25% (n=6) present clinically significant misophonic symptoms»
9. отклик: **unclear** — Number approached or refusing not reported. — Methods p.10 — «the distribution was made only by the investigator before or after participants appointments»

Правки:
- 

Проверено: да
---

## ST090 · Cassiello-Robbins 2020 · Frontiers in psychology

Основной отчёт R1139: [текст](../../fulltext/text/R1139.txt) — «A Preliminary Investigation of the Association Between Misophonia and Symptoms of Psychopathology and Personality Disorders.» — [DOI](https://doi.org/10.3389/fpsyg.2020.519681)
Расхождения в тексте: The threshold is worded inconsistently: 'scores below 34 ... low' and 'scores above 34 ... high' leave a score of exactly 34 unassigned, but the next clause, 'individuals with this score, or higher', means >=34. Group sizes 19 + 30 = 49 match the analysed n. Table 1 notes df = 46 for the PD-symptoms t-test, so one participant is missing SCID-II symptom data; MQ data are complete for all 49.
Заметка ИИ: There is one estimate: the study's own MQ total >=34 'high misophonia' group, 19/49. Because 34 is above the anchored MQ total >=30, it is coded L2, but JBI 6 = no because the threshold is stricter than the anchored cut-off. The sample is small and drawn from a clinic specialising in PD treatment.

### ST090-1 · Community adults, Duke outpatient clinic, USA, n=49
Отчёты: R1139 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ total (Symptom + Emotions-and-Behaviors) >=34 | **L2** | **19 / 49** | 38.8 | Data Analytic Plan; Self-Report | «individuals with this score, or higher, would have an average score of 2 or higher ... between the high (n = 19) and low misophonia groups (n = 30)» |

- E1: источник порога: study's own; правило: MQ row; G2/G3 threshold above L2 cut-off total >=30; у авторов: «high misophonia symptoms»; главная у авторов: yes; период: NR; заметка: The boundary wording is ambiguous ('below 34' low vs 'above 34' high), but the text adds 'this score, or higher', so >=34 is taken. Used as a grouping variable for comparisons, not presented as a prevalence. 19/49 = 38.8%.

**Ключевые поля выборки:**
- **n_analysed: 49** — Participants — «Forty-nine participants were drawn from a larger study»
- **population: gp_other** — Participants — «the purpose of the larger study from which these data were derived was to gather information about emotion regulation and sensory processing from a general community sample.»
- **sampling: convenience** — Procedures — «Interested participants contacted the clinic, completed a phone screen to ensure they did not meet exclusion criteria»

**Остальные поля:**
- clinical_group: NA — Participants — «participants were not required to meet specific diagnostic or demographic criteria»
- country: USA — Procedures — «The Duke University Medical Center Institutional Review Board approved all procedures»
- setting: community (adults recruited via local listserv notices and clinic flyers; assessed at an academic medical center outpatient clinic specialising in personality disorder treatment) — Procedures; Discussion — «Recruitment for the larger study consisted of local list serve notices and clinic flyers in an academic medical center outpatient clinic.»
- data_years: NR — Methods — «NR»
- design: cross-sectional — Participants — «Forty-nine participants were drawn from a larger study examining the relationship between symptoms of psychopathology and sensory processing dysfunction in adu…»
- topic_disclosed: NR — Participants; Procedures — «a larger study examining the relationship between symptoms of psychopathology and sensory processing dysfunction in adults»
- inclusion_exclusion: Adults >=18 who completed the MQ; excluded if current mania or psychotic disorder — Participants — «Participants were excluded from the study if they were under age 18 or met criteria for current mania or psychotic disorder.»
- n_invited: NR — Methods — «NR»
- n_responded: NR — Participants — «Participants were included in the current analyses if they completed the Misophonia Questionnaire»
- response_rate: NR — Procedures — «All participants who provided consent completed study procedures.»
- age_mean: 27.02 — Participants — «The average age of participants included in these analyses was 27.02 years (SD = 8.75).»
- age_sd: 8.75 — Participants — «27.02 years (SD = 8.75)»
- age_min: NR — Participants — «Participants were excluded from the study if they were under age 18»
- age_max: NR — Participants — «NR»
- age_group: adults — Participants — «Participants were excluded from the study if they were under age 18»
- pct_female: 85.7 — Participants — «Participants primarily identified as female (n = 42)»
- informant: self — Procedures — «Participants also completed a battery of self-report questionnaires regarding emotional functioning, sensory processing, and psychiatric symptoms.»
- mode: NR — Procedures — «All procedures took place at the outpatient clinic.»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), English — Measures — «The MQ is a 17-item, three-part, questionnaire that evaluates the presence of misophonia symptoms»
- instrument_validated_in_language: yes — Measures — «In its initial validation the MQ showed good internal consistency (α = 0.86–0.89).»
- pub_status: journal — Citation — «Frontiers in psychology; DOI: 10.3389/fpsyg.2020.519681»
- language: English — Full text — «A Preliminary Investigation of the Association Between Misophonia and Symptoms of Psychopathology and Personality Disorders»
- funding_coi: Funded by Wallace Research Foundation; MR scientific advisor for BehaVR and Odin and on advisory board of Misophonia Research Fund — Footnotes; Conflict of Interest — «MR is a scientific advisor for BehaVR and Odin. He also sits on the scientific advisory board for the Misophonia Research Fund.»
- notes: pct_female derived: 42/49 = 85.7%. Country inferred from the Duke University Medical Center IRB. The parent study (McMahon et al. 2019) was on psychopathology and sensory processing dysfunction, so other reports of the parent study may overlap with this sample. The authors say participants came from a facility specialising in PD treatment, so the sample may be enriched for psychopathology (GAD 32.7%, MDD 18.4%). The sample was not recruited for misophonia, but the parent study concerned sensory processing; what the invitation said is not reported. Mode of questionnaire completion (paper or co…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Listserv notices and clinic flyers at one PD-specialised outpatient clinic do not cover the general community population — Procedures; Discussion — «participants were recruited from a facility specializing in treatment of PDs.»
2. способ отбора: **no** — Volunteer opt-in convenience recruitment — Procedures — «Interested participants contacted the clinic, completed a phone screen»
3. размер выборки: **no** — n = 49 < 385 — Participants — «Forty-nine participants»
4. описание выборки и условий: **unclear** — Age, sex, setting and (implicitly) country reported; data collection dates missing — Participants; Procedures — «The average age of participants included in these analyses was 27.02 years (SD = 8.75).»
5. охват (пропуски): **unclear** — Only MQ completers included; number of parent-study participants without MQ not reported — Participants — «Participants were included in the current analyses if they completed the Misophonia Questionnaire (MQ; Wu et al., 2014), which was an addition to the larger st…»
6. валидность определения случая: **no** — MQ total >=34 is a study-defined threshold stricter than the anchored MQ total >=30 cut-off — Data Analytic Plan — «The score of 34 was chosen because (a) there is no empirically derived or consensus standard for misophonia symptom severity on the MQ»
7. единое надёжное измерение: **yes** — Same MQ and threshold for all; alpha reported in sample — Measures — «Reliability in this study was also good (α = 0.93).»
8. статистика (числитель и знаменатель): **yes** — Numerator 19 and denominator 49 clear; CI calculable — Self-Report — «between the high (n = 19) and low misophonia groups (n = 30)»
9. отклик: **unclear** — Number contacted/invited not reported; no response rate — Procedures — «All participants who provided consent completed study procedures.»

Правки:
- 

Проверено: да