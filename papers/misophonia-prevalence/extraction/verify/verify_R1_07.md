# Проверка выписывания — файл 7 из 10

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

## ST061 · Aazh 2022 · Frontiers in neuroscience

Основной отчёт R0851: [текст](../../fulltext/text/R0851.txt) — «Audiological and Other Factors Predicting the Presence of Misophonia Symptoms Among a Clinical Population Seeking Help for Tinnitus and/or Hyperacusis.» — [DOI](https://doi.org/10.3389/fnins.2022.900065)
Расхождения в тексте: Abstract, Results and Conclusions all give 23% (59/257). The item distribution (149/49/21/38) agrees: 21 + 38 = 59. The Discussion gives 42% with 'some symptoms', and the counts agree: 49 + 21 + 38 = 108, 108/257 = 42.0%. Group sizes vary by analysis: Table 2 gives Miso Cat 0 n = 198 (age row), while the hearing-loss text says 'Among the 190 patients in Miso Cat 0'. This is because the denominators differ by variable, not a contradiction about the misophonia classification. The female/male counts were derived from rounded percentages (61% and 52%). Their back-calculated total, 139, matches the reported female n of 139.
Заметка ИИ: Single clinical sample from a UK audiology clinic. Misophonia was measured with one unvalidated item (SSSQ item 4); the primary estimate is L1 (SSSQ4>=2), and an L0 estimate (>=1) is also listed. Reviewer: check eligibility, because the population includes patients seeking help for hyperacusis, which is a sound-sensitivity condition, although the sample was not recruited for misophonia.

### ST061-1 · Tinnitus and Hyperacusis Therapy Specialist Clinic, Royal Surrey NHS FT, Guildford, GBR, n=257
Отчёты: R0851 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SSSQ4 · SSSQ4>=2 (7-14 days in last 2 weeks) | **L1** | **59 / 257** | 23.0 | Results, Comparison of Miso Cat 0 and Miso Cat 1; Methods, … | «Overall, 23% of patients (59/257) were classified as Miso Cat 1.» |
| E2 | all | SSSQ4 · SSSQ4>=1 (2-14 days in last 2 weeks) | **L0** | **108 / 257** | 42.0 | Results, Audiological and Psychological Factors; Discussion | «Of 257 patients, SSSQ4 scores of 0, 1, 2, and 3 were obtained for 149 (58%), 49 (19%), 21 (8%) and 38 (15%), respectively.» |
| E3 | female | SSSQ4 · SSSQ4>=2 (7-14 days in last 2 weeks) | **L1** | **36 / 139** | 25.9 | Results, Comparison of Miso Cat 0 and Miso Cat 1; Methods; … | «The percentage of females was 61% for Miso Cat 1 and 52% for Miso Cat 0» |
| E4 | male | SSSQ4 · SSSQ4>=2 (7-14 days in last 2 weeks) | **L1** | **23 / 118** | 19.5 | Results, Comparison of Miso Cat 0 and Miso Cat 1; Methods | «The percentage of females was 61% for Miso Cat 1 and 52% for Miso Cat 0 ... Fifty four percent (139/257) were female.» |

- E1: источник порога: study's own; правило: SSSQ4 row: >=2 = L1 (frequency rule of adhoc row); у авторов: «frequent symptoms of misophonia (Miso Cat 1); 'classified as having misophonia'»; главная у авторов: yes; период: past month; заметка: Recall period is the last 2 weeks (coded past month). Consistent with the item distribution: 21 (score 2) + 38 (score 3) = 59.
- E2: источник порога: study's own; правило: SSSQ4 row: score 1 (2-6 days) is L0; G1 sum of bands; у авторов: «some symptoms of misophonia»; главная у авторов: no; период: past month; **расчёт: 49 + 21 + 38 = 108 (scores 1, 2, 3) of 257**; заметка: Discussion: '42% of patients ... presented with some symptoms of misophonia' (108/257 = 42.0%). L0: listed, not pooled.
- E3: источник порога: study's own; правило: SSSQ4 row: >=2 = L1; у авторов: «Miso Cat 1»; главная у авторов: no; период: past month; **расчёт: 61% x 59 = 35.99 -> 36; female n = 139 (Methods). Check: 52% x 198 Miso Cat 0 = 102.96 -> 103; 36 + 103 = 139**; заметка: Derived from percentages within Miso Cat groups; 36/139 = 25.9%.
- E4: источник порога: study's own; правило: SSSQ4 row: >=2 = L1; у авторов: «Miso Cat 1»; главная у авторов: no; период: past month; **расчёт: 59 - 36 female = 23; n = 257 - 139 = 118**; заметка: Assumes non-female = male (no other sex categories reported); 23/118 = 19.5%.

**Ключевые поля выборки:**
- **n_analysed: 257** — Results, Comparison of Miso Cat 0 and Miso Cat 1 — «Overall, 23% of patients (59/257) were classified as Miso Cat 1.»
- **population: clinical** — Abstract — «among a population seeking help for tinnitus and/or hyperacusis at an audiology clinic (n = 257)»
- **sampling: census** — Methods, Study Design and Patients — «Data were included for all patients who attended the THTSC seeking help for tinnitus and/or hyperacusis in 2019-2020 and who answered a question assessing symptoms of misophonia (n = 257)»

**Остальные поля:**
- clinical_group: other: tinnitus and/or hyperacusis (audiology clinic patients) — Abstract — «a population seeking help for tinnitus and/or hyperacusis at an audiology clinic»
- country: GBR — Methods, Study Design and Patients — «conducted at the Tinnitus and Hyperacusis Therapy Specialist Clinic (THTSC), RSFT, Guildford, United Kingdom»
- setting: clinic: NHS audiology specialist clinic for tinnitus and hyperacusis — Methods, Study Design and Patients — «all patients who attended the THTSC seeking help for tinnitus and/or hyperacusis in 2019-2020»
- data_years: 2019-2020 — Methods, Study Design and Patients — «seeking help for tinnitus and/or hyperacusis in 2019-2020»
- design: cross-sectional — Methods, Study Design and Patients — «This was a retrospective cross-sectional study»
- topic_disclosed: no — Methods, Study Design and Patients — «Administration of the self-report questionnaires (including the question about misophonia) and audiological measurements included in this study were part of th…»
- inclusion_exclusion: All patients attending THTSC for tinnitus and/or hyperacusis in 2019-2020 who answered the misophonia item (SSSQ item 4); questionnaires at first visit before treatment — Methods, Study Design and Patients — «Data were included for all patients who attended the THTSC seeking help for tinnitus and/or hyperacusis in 2019-2020 and who answered a question assessing symp…»
- n_invited: NR — Methods, Study Design and Patients — «Data were included for all patients who attended the THTSC ... and who answered a question assessing symptoms of misophonia (n = 257)»
- n_responded: 257 — Methods, Study Design and Patients — «who answered a question assessing symptoms of misophonia (n = 257)»
- response_rate: NR — Methods, Study Design and Patients — «who answered a question assessing symptoms of misophonia (n = 257)»
- age_mean: 53 — Methods, Study Design and Patients — «The mean age of the patients was 53 years (SD = 16 years) (age range = 17 - 97 years).»
- age_sd: 16 — Methods, Study Design and Patients — «The mean age of the patients was 53 years (SD = 16 years)»
- age_min: 17 — Methods, Study Design and Patients — «(age range = 17 - 97 years)»
- age_max: 97 — Methods, Study Design and Patients — «(age range = 17 - 97 years)»
- age_group: mixed — Methods, Study Design and Patients — «(age range = 17 - 97 years)»
- pct_female: 54 — Methods, Study Design and Patients — «Fifty four percent (139/257) were female.»
- informant: self — Methods, Study Design and Patients — «Patients completed the questionnaires in the clinic waiting area without involvement of their audiologist.»
- mode: NR — Methods, Study Design and Patients — «Patients completed the questionnaires in the clinic waiting area without involvement of their audiologist.»
- instruments: SSSQ item 4 (Sound Sensitivity Symptoms Questionnaire, English) - single item — Methods, Assessment of Misophonia Symptoms — «Item 4 of the Sound Sensitivity Symptoms Questionnaire (SSSQ) (Aazh et al., 2022a) was used to identify patients with symptoms of misophonia.»
- instrument_validated_in_language: no — Discussion (limitations) — «Also, the validity and reliability of using SSSQ4 to assess the frequency of reported misophonia symptoms have not been evaluated.»
- pub_status: journal — Header — «Frontiers in neuroscience; DOI: 10.3389/fnins.2022.900065»
- language: English — Full text — «Audiological and Other Factors Predicting the Presence of Misophonia Symptoms Among a Clinical Population Seeking Help for Tinnitus and/or Hyperacusis»
- funding_coi: Partially funded by a grant to AD from the Edith Abramson Clayman Family Philanthropic Fund; authors declare no conflict of interest — Funding; Conflict of Interest — «This research was partially supported via a grant to AD by the Edith Abramson Clayman Family Philanthropic Fund.»
- notes: Retrospective clinical audit data. No validated misophonia measure was used: only SSSQ item 4, a single item on how often in the last 2 weeks the patient felt anger or anxiety at eating, breathing or tapping sounds. Patients sought help for tinnitus and/or hyperacusis. Hyperacusis is a sound-sensitivity condition, so the reviewer should confirm eligibility; the sample was not recruited for misophonia, so it is treated as a clinical sample. The number of clinic attendees who did not answer the item is not reported. Mode (paper or electronic) is not stated; questionnaires were completed in the …

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Target population is patients seeking help for tinnitus/hyperacusis at this clinic; frame is all attendees 2019-2020. — Methods, Study Design and Patients — «Data were included for all patients who attended the THTSC seeking help for tinnitus and/or hyperacusis in 2019-2020»
2. способ отбора: **yes** — All consecutive attendees who answered the item were included (census of clinic records). — Methods, Study Design and Patients — «Data were included for all patients who attended the THTSC ... and who answered a question assessing symptoms of misophonia (n = 257)»
3. размер выборки: **no** — n = 257 < 385. — Abstract — «(n = 257)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Methods, Study Design and Patients — «The mean age of the patients was 53 years (SD = 16 years) (age range = 17 - 97 years). Fifty four percent (139/257) were female.»
5. охват (пропуски): **unclear** — Only patients who answered the item were included; the number of attendees without the item is not reported. — Methods, Study Design and Patients — «and who answered a question assessing symptoms of misophonia (n = 257)»
6. валидность определения случая: **no** — Single ad hoc frequency item (SSSQ4); its validity has not been evaluated. — Discussion (limitations) — «Misophonia was assessed based on only one question (item 4 of the SSSQ).»
7. единое надёжное измерение: **unclear** — Same item and setting for all, but no reliability reported for the single item. — Discussion (limitations) — «the validity and reliability of using SSSQ4 to assess the frequency of reported misophonia symptoms have not been evaluated»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear; CI calculable. — Results, Comparison of Miso Cat 0 and Miso Cat 1 — «Overall, 23% of patients (59/257) were classified as Miso Cat 1.»
9. отклик: **unclear** — Number of attendees in 2019-2020 (the invited denominator) is not reported. — Methods, Study Design and Patients — «all patients who attended the THTSC ... and who answered a question assessing symptoms of misophonia (n = 257)»

Правки:
- 

Проверено: да
---

## ST062 · Aazh 2022 · Journal of the American Academy of Audiology

Основной отчёт R0854: [текст](../../fulltext/text/R0854.txt) — «The Effectiveness of Unguided Internet-Based Cognitive Behavioral Therapy for Tinnitus for Patients with Tinnitus Alone or Combined with Hyperacusis and/or Mis…» — [DOI](https://doi.org/10.1055/a-2087-0262)
Расхождения в тексте: The abstract and Results agree: 12 with hyperacusis, 5 with misophonia (all within the hyperacusis group), 28 in total. 16 tinnitus-alone + 12 hyperacusis = 28, consistent. Sex: 17 male, so 11 female (derived). The 95% CI for the SAD-T difference is given as 0.35–4.6 in Results and 0.3–4.6 in Discussion; this is a minor difference and does not affect the misophonia estimates.
Заметка ИИ: Small intervention study (pre-post evaluation of an online tinnitus CBT programme). Misophonia was found with one ad hoc self-identification item, so the estimate is L1 with JBI 6 = no. Country is not reported. Only programme completers were analysed, and the number of people who started the programme is unknown.

### ST062-1 · iCBT(T) tinnitus programme completers, online, country NR, n=28
Отчёты: R0854 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-identified misophonia (yes/no item 'Do you have misophonia?' with definition shown) | **L1** | **5 / 28** | 17.9 | Results, Characteristics of the Participants; Table 1 Q11 | «Based on their responses to questions 10 and 11 listed in Table 1, 12 participants reported experiencing hyperacusis and 5 reported misophonia.» |
| E2 | hyperacusis (self-reported, tinnitus + hyperacusis) | adhoc · self-identified misophonia (yes/no item with definition shown) | **L1** | **5 / 12** | 41.7 | Results, Characteristics of the Participants | «12 participants reported experiencing hyperacusis and 5 reported misophonia. All participants who reported misophonia also reported hyperacusis.» |
| E3 | tinnitus alone (no self-reported hyperacusis) | adhoc · self-identified misophonia (yes/no item with definition shown) | **L1** | **0 / 16** | 0.0 | Results, Characteristics of the Participants; Pre- and Post… | «All participants who reported misophonia also reported hyperacusis. ... the 16 participants with tinnitus alone» |

- E1: источник порога: study's own; правило: adhoc row: self-identified misophonia with definition shown -> L1; у авторов: «reported misophonia»; главная у авторов: no; период: current; заметка: Prevalence was not an aim of the study. 5/28 = 17.9%. All 5 also reported hyperacusis.
- E2: источник порога: study's own; правило: adhoc row: self-identified misophonia -> L1; у авторов: «reported misophonia»; главная у авторов: no; период: current; **расчёт: All 5 participants with misophonia also reported hyperacusis (n=12) -> 5/12**; заметка: Hyperacusis subgroup defined by a self-report single item (Q10).
- E3: источник порога: study's own; правило: adhoc row: self-identified misophonia -> L1; у авторов: «reported misophonia»; главная у авторов: no; период: current; **расчёт: 28 - 12 with hyperacusis = 16; all 5 misophonia cases had hyperacusis -> 0/16**

**Ключевые поля выборки:**
- **n_analysed: 28** — Results, Characteristics of the Participants — «All 28 participants reported having bothersome tinnitus.»
- **population: clinical** — Results, Characteristics of the Participants — «All 28 participants reported having bothersome tinnitus.»
- **sampling: convenience** — Method, Study Design and Participants — «28 consecutive participants who completed the iCBT(T) program ... The participants were self-selected rather than being recruited by the authors.»

**Остальные поля:**
- clinical_group: tinnitus — Results, Characteristics of the Participants — «All 28 participants reported having bothersome tinnitus.»
- country: NR — Method, Study Design and Participants; Results — «Presumably, the participants found the program via internet search or were directed to the iCBT(T) website by audiologists who were aware of the program.»
- setting: online: self-selected users of an unguided internet CBT programme for tinnitus (no clinic recruitment) — Method, Study Design and Participants — «The participants were self-selected rather than being recruited by the authors.»
- data_years: 2020 — Method, Study Design and Participants — «28 consecutive participants who completed the iCBT(T) program between October and December 2020»
- design: cross-sectional — Abstract; Method, Study Design and Participants — «This was an exploratory study with a retrospective cross-sectional design using anonymized data from 28 consecutive participants»
- topic_disclosed: no — Title; Method — «a specific unguided iCBT program for tinnitus with seven self-help modules»
- inclusion_exclusion: People with tinnitus who completed the unguided iCBT(T) programme (Oct-Dec 2020) and answered the assessment questions; non-completers not included — Abstract; Discussion — «The data for 28 people with tinnitus who completed the iCBT(T) program and answered a series of questions about their tinnitus and hearing status were included…»
- n_invited: NR — Discussion — «We do not know how many people started the program without finishing it.»
- n_responded: 28 — Method, Study Design and Participants — «anonymized data from 28 consecutive participants who completed the iCBT(T) program»
- response_rate: NR — Discussion — «We do not know how many people started the program without finishing it.»
- age_mean: 52 — Results, Characteristics of the Participants — «Their average age was 52 years (SD, 16.5 years; range, 18–75 years)»
- age_sd: 16.5 — Results, Characteristics of the Participants — «Their average age was 52 years (SD, 16.5 years; range, 18–75 years)»
- age_min: 18 — Results, Characteristics of the Participants — «range, 18–75 years»
- age_max: 75 — Results, Characteristics of the Participants — «range, 18–75 years»
- age_group: adults — Results, Characteristics of the Participants — «range, 18–75 years»
- pct_female: 39.3 — Results, Characteristics of the Participants — «and 17 were male»
- informant: self — Method, Other Questions — «They responded by selecting from a range of response options.»
- mode: online — Method, Study Design and Participants — «Anonymous demographic data ... were imported from their answers to the questions in the iCBT(T) initial and final assessment modules.»
- instruments: Single ad hoc yes/no item 'Do you have misophonia?' with a definition shown (English), in the iCBT(T) assessment module — Table 1, Assessment module, question 11 — «11- Do you have misophonia? Misophonia is a strong emotional reaction to certain sounds, such as sounds created by chewing food, swallowing, tapping, breathing…»
- instrument_validated_in_language: no — Discussion — «we relied on the single questions that were used in the iCBT(T) assessment module to detect hyperacusis and misophonia. ... this is not ideal.»
- pub_status: journal — Header — «Journal of the American Academy of Audiology»
- language: English — Full text — «The Effectiveness of Unguided Internet-Based Cognitive Behavioral Therapy for Tinnitus»
- funding_coi: Funding NR. The authors developed the iCBT(T) programme they evaluated. — Discussion — «Another limitation of this study is the fact it was conducted by the developers of the iCBT(T) program»
- notes: Intervention study (pre-post) of an online tinnitus CBT programme. The misophonia data come from the baseline assessment module, and only programme completers are included, so there is selection bias. pct_female derived: 28 - 17 male = 11 female; 11/28 = 39.3%. Country not stated: the ethics approval is from the University of Surrey (UK), and support organisations in the UK, USA and Australia were listed. The first author's group (Aazh et al.) publishes other tinnitus/hyperacusis clinic samples; this sample of online programme users is separately recruited.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is only completers of one self-found online programme, not people with tinnitus in general. — Method, Study Design and Participants — «Presumably, the participants found the program via internet search or were directed to the iCBT(T) website by audiologists»
2. способ отбора: **no** — Self-selected volunteers; only completers included. — Method, Study Design and Participants — «The participants were self-selected rather than being recruited by the authors.»
3. размер выборки: **no** — n = 28, below 139. — Abstract — «The data for 28 people with tinnitus who completed the iCBT(T) program»
4. описание выборки и условий: **unclear** — Age, sex, setting and dates are reported; country is not. — Results, Characteristics of the Participants — «Their average age was 52 years (SD, 16.5 years; range, 18–75 years) and 17 were male.»
5. охват (пропуски): **yes** — All 28 included participants answered the misophonia item. — Results, Characteristics of the Participants — «Based on their responses to questions 10 and 11 listed in Table 1, 12 participants reported experiencing hyperacusis and 5 reported misophonia.»
6. валидность определения случая: **no** — Ad hoc single self-identification item. — Discussion — «we relied on the single questions that were used in the iCBT(T) assessment module to detect hyperacusis and misophonia. ... this is not ideal.»
7. единое надёжное измерение: **unclear** — Everyone got the same online item, but no reliability was reported for the misophonia item. — Method, Other Questions — «The questions were related to: whether they had hearing difficulties, hyperacusis, and misophonia»
8. статистика (числитель и знаменатель): **yes** — Numerator (5) and denominator (28) are clear, so a CI can be calculated. — Results, Characteristics of the Participants — «12 participants reported experiencing hyperacusis and 5 reported misophonia.»
9. отклик: **no** — Number who started the programme is unknown; non-completers are not handled. — Discussion — «We do not know how many people started the program without finishing it. This may have led to selection bias»

Правки:
- 

Проверено: да
---

## ST063 · Aryal 2022 · Neuroscience Research Notes

Основной отчёт R0858: [текст](../../fulltext/text/R0858.txt) · [PDF](../../fulltext/pdf/R0858.pdf) — «Misophonia: Prevalence, impact and co-morbidity among Mysore University students in India - A survey» — [DOI](https://doi.org/10.31117/neuroscirn.v5i4.161)
Расхождения в тексте: (1) The headline 23.28% (48 cases) does not match 48/170 = 28.24%; Table 3 counts (38+10+0=48) were used. (2) 81 self-reported cases are given as both 47.6% (correct for /170) and 48.27%. (3) The gender chi-square is .58 in the text, but Table 5 gives value 1.100 with p .58. (4) Table 1 ear problems: 9 + 166 = 175 ≠ 170. (5) The MAQ mean of 3.09 (SD 7.18) among the 81 cannot be reconciled with the band counts: the minimum possible mean from the bands is about 3.65. (6) The sampling is called 'convenient', yet p.4 says participants were 'taken randomly'. (7) MAQ authorship is attributed to Wu et al. 2014 on p.7 but to Johnson/Dozier on p.3.
Заметка ИИ: Two-stage design: A-MISO-S and MAQ were completed only by the 81 people who self-reported misophonia. Combined definitions are coded as instrument 'multiple' (G4), with denominator 170 (G10). The authors' primary estimate is A-MISO-S >=5 (L1). The L2 estimate is A-MISO-S >=10: 10/170.

### ST063-1 · Mysore University students, India, online survey, n=170
Отчёты: R0858 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-reported misophonia (subjective experience; brief description of misophonia shown in form) | **L1** | **81 / 170** | 47.6 | Page 4, Section 3.2 | «Among 170 participants who responded to the survey, 81 (47.6%) reported having misophonia based on their subjective experience.» |
| E2 | all | multiple · self-reported misophonia screen AND A-MISO-S>=5 | **L1** | **48 / 170** | 28.2 | Page 4, Section 3.4; Page 5, Table 3 | «only 48 (23.28%) reported clinically significant misophonia that warrants treatment.» |
| E3 | all | multiple · self-reported misophonia screen AND A-MISO-S>=10 | **L2** | **10 / 170** | 5.9 | Page 5, Table 3 | «10-14 10 (5.88%) Moderate ... 15-19 0 (0%) Severe» |
| E4 | all | multiple · self-reported misophonia screen AND A-MISO-S>=15 | **L2** | **0 / 170** | 0.0 | Page 5, Table 3; Page 4, Section 3.4 | «15-19 0 (0%) Severe; The maximum score obtained was 14» |
| E5 | all | multiple · self-reported misophonia screen AND MAQ>=12 (Version A, mild or more) | **L1** | **16 / 170** | 9.4 | Page 5, Table 3 and text | «9.41% of participants among 170 participants had clinically significant misophonia» |
| E6 | all | multiple · self-reported misophonia screen AND MAQ>=25 (Version A, moderate or more) | **L2** | **6 / 170** | 3.5 | Page 5, Table 3 | «25-37 4 (2.35%) Moderate; 38-50 2 (1.18%) Severe» |
| E7 | all | multiple · self-reported misophonia screen AND MAQ>=38 (Version A, severe or more) | **L2** | **2 / 170** | 1.2 | Page 5, text and Table 3 | «The score of two participants (1.18%) ranged from 38-50 and were classified as severe misophonia.» |
| E8 | female | adhoc · self-reported misophonia (subjective experience) | **L1** | **68 / 138** | 49.3 | Page 4, Section 3.2; Page 4, Table 1 | «Among 81 (47.6%) participants who reported misophonia, 13 (16.05%) were male, and 68 (83.95%) were female.» |
| E9 | male | adhoc · self-reported misophonia (subjective experience) | **L1** | **13 / 32** | 40.6 | Page 4, Section 3.2; Page 4, Table 1 | «Among 81 (47.6%) participants who reported misophonia, 13 (16.05%) were male, and 68 (83.95%) were female.» |

- E1: источник порога: study's own; правило: adhoc row; self-identified misophonia -> L1; у авторов: «reported having misophonia based on their subjective experience»; главная у авторов: no; период: NR; заметка: Elsewhere described as 'reported a problem of irritation with the sounds' (p.4, 3.3), which would be L0; and as 48.27% (p.4, 3.4). Sample has scale-based L1 estimates, so self-identification is secondary.
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (5-9 + 10-14 + 15-19); G4 screen AND scale; G10 denominator all screened; у авторов: «clinically significant misophonia that warrants treatment»; главная у авторов: yes; период: NR; заметка: 48/170 = 28.2%, not 23.28% as reported; authors' percentage cannot be traced.
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (10-14 + 15-19); G4; G10; у авторов: «Moderate Misophonia»; главная у авторов: no; период: NR; **расчёт: 10 (10-14) + 0 (15-19) from Table 3**; заметка: Maximum A-MISO-S score in sample was 14.
- E4: источник порога: developer paper; правило: A-MISO-S row; G1; G2 stricter than L2 cut-off; G4; G10; у авторов: «Severe»; главная у авторов: no; период: NR; **расчёт: 0 (15-19); no 20-24 band; max score 14**
- E5: источник порога: developer paper; правило: MAQ row, Version A; G1 sum of bands (12-24 + 25-37 + 38-50); G4; G10; у авторов: «clinically significant misophonia, which warrants treatment»; главная у авторов: no; период: NR; **расчёт: 10 + 4 + 2 from Table 3 = 16; 16/170 = 9.41% matches text**; заметка: Band source is attributed to the MAQ but no citation is given for the bands. Reported MAQ mean 3.09 (SD 7.18) is inconsistent with the band counts.
- E6: источник порога: developer paper; правило: MAQ row, Version A; G1 sum of bands (25-37 + 38-50); G4; G10; у авторов: «moderate misophonia»; главная у авторов: no; период: NR; **расчёт: 4 + 2 from Table 3 = 6**; заметка: MAQ band cut-off has no anchoring (JBI 6 = no; excluded in sensitivity analysis 2).
- E7: источник порога: developer paper; правило: MAQ row, Version A; G1 (38-50; no 51-63 reported); G2; G4; G10; у авторов: «severe misophonia»; главная у авторов: no; период: NR; **расчёт: 2 (38-50) + 0 (51-63; max score 42)**
- E8: источник порога: study's own; правило: adhoc row; self-identified misophonia -> L1; у авторов: «reported misophonia»; главная у авторов: no; период: NR; заметка: Denominator 138 females from Table 1. A-MISO-S/MAQ results not given by sex.
- E9: источник порога: study's own; правило: adhoc row; self-identified misophonia -> L1; у авторов: «reported misophonia»; главная у авторов: no; период: NR; заметка: Denominator 32 males from Table 1.

**Ключевые поля выборки:**
- **n_analysed: 170** — Page 3, Section 2.1 — «only 170 participants were considered for analysis.»
- **population: university_students** — Page 2, Section 2.0 — «among Mysore University's undergraduates and post-graduate students. Data was obtained from 172 participants»
- **sampling: convenience** — Page 3, Section 2.1 — «distributed the final version of the questionnaire as an e-survey in the form of Google forms to university students using various social platforms, such as WhatsApp, and Gmail, using convenient sampling methods.»

**Остальные поля:**
- clinical_group: NA — NA
- country: IND — Page 1, title — «among Mysore University students in India»
- setting: university (University of Mysore undergraduate and postgraduate students; online survey distributed via WhatsApp and Gmail) — Page 2, Section 2.0; Page 3, Section 2.1 — «A descriptive cross-sectional study was undertaken among Mysore University's undergraduates and post-graduate students.»
- data_years: 2021 — Page 2, Section 2.0 — «The study was conducted over a period of three months, from October 2021 to December 2021.»
- design: cross-sectional — Page 2, Section 2.0 — «A descriptive cross-sectional study was undertaken among Mysore University's undergraduates and post-graduate students.»
- topic_disclosed: yes — Page 3, Section 2.1 — «A brief description of misophonia was included in the Google form.»
- inclusion_exclusion: Mysore University students aged 18-30, literate with good English competency; non-consenters (2) and incomplete surveys excluded — Page 2, Section 2.0; Page 3, Sections 2.1 and 2.3 — «Because two participants refused to consent, they were removed from the study, and only 170 participants were considered for analysis.»
- n_invited: NR — NR
- n_responded: 172 — Page 3, Section 2.1 — «The poll received responses from 172 Mysore university students aged 18 to 30.»
- response_rate: NR — NR
- age_mean: 22 — Page 2, Section 2.0 — «with a mean age of 22 years and a standard deviation of 2.5 years.»
- age_sd: 2.5 — Page 2, Section 2.0 — «with a mean age of 22 years and a standard deviation of 2.5 years.»
- age_min: 18 — Page 2, Section 2.0 — «The participants were all between 18 and 30 years»
- age_max: 30 — Page 2, Section 2.0 — «The participants were all between 18 and 30 years»
- age_group: adults — Page 2, Section 2.0 — «The participants were all between 18 and 30 years»
- pct_female: 81.2 — Page 4, Table 1 — «Male Female 32 (18.8%) 138 (81.2%)»
- informant: self — Page 3, Section 2.1 — «distributed the final version of the questionnaire as an e-survey in the form of Google forms»
- mode: online — Page 3, Section 2.1 — «as an e-survey in the form of Google forms»
- instruments: self-reported misophonia question (ad hoc, English); A-MISO-S (English); MAQ (English) — Page 3, Section 2.1 — «There is a lack of misophonia questionnaires in the native Indian language, so the English version of these two questionnaires was used in the study.»
- instrument_validated_in_language: yes — Page 3, Section 2.1 — «Translation and validation of this questionnaire are done in several languages, such as English and Turkish ... (Naylor et al., 2021; Sarigedik & Gulle, 2021).»
- pub_status: journal — Page 1, header — «NEUROSCIENCE RESEARCH NOTES ... Received: 7 April 2022; Accepted: 1 August 2022; Published: 24 October 2022»
- language: English — Page 1 — «Misophonia: Prevalence, impact and co-morbidity among Mysore University students in India - A survey»
- funding_coi: Funding NR; authors report no conflicts of interest — Page 8, Conflicts of Interest — «Conflicts of Interest: The authors report no conflicts of interest.»
- notes: Two-stage design: only the 81 who self-reported misophonia completed A-MISO-S and MAQ. Screen-negatives (89) are counted as non-cases, with denominator 170 (G10). Table 3 band percentages use 170 as denominator. Sampling is described as 'convenient', but p.4 says participants were 'taken randomly'. The authors' headline 23.28% (48 cases) is not 48/170 (28.2%), and 48.27% is not 81/170 (47.6%). It is unclear whether the screen asked about misophonia (with a definition shown) or about 'irritation with the sounds' (p.4). The number of incomplete surveys excluded is not reported. MAQ is reported …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is Mysore University students; frame was students reached via WhatsApp/Gmail social platforms, not an enrolment list — Page 3, Section 2.1 — «to university students using various social platforms, such as WhatsApp, and Gmail, using convenient sampling methods.»
2. способ отбора: **no** — Convenience, open online opt-in survey — Page 3, Section 2.1 — «using convenient sampling methods.»
3. размер выборки: **no** — n=170 < 385; authors also say sample size inadequate — Page 8, Conclusions — «The sample size of our study is not adequate.»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported — Page 2, Section 2.0; Page 4, Table 1 — «from October 2021 to December 2021. The participants were all between 18 and 30 years, with a mean age of 22 years»
5. охват (пропуски): **unclear** — Incomplete surveys were omitted but their number is not reported; all 81 screen-positives completed A-MISO-S — Page 3, Section 2.3 — «The study omitted those participants who did not complete the survey.»
6. валидность определения случая: **yes** — Rated on the L2 definition A-MISO-S >=10 (English version, validation cited, Naylor 2021); note that it was applied only after an ad hoc self-report screen — Page 3, Section 2.1; Page 4, Section 3.4 — «the score of 10 (5.88%) participants ranges from 10-14 and classified as Moderate Misophonia.»
7. единое надёжное измерение: **yes** — Same online instrument and scoring for all; Cronbach's alpha for the English version cited from source (Naylor 2021) — Page 3, Section 2.1 — «this questionnaire has been found to be reliable, with Chronbach's alpha value of 0.814 (Naylor et al., 2021).»
8. статистика (числитель и знаменатель): **no** — Headline percentages (23.28%, 48.27%) cannot be traced to the reported counts (48/170=28.2%; 81/170=47.6%); no CIs — Page 4, Section 3.4 — «even though 81 (48.27%) among 170 participants reported misophonia symptoms, only 48 (23.28%) reported clinically significant misophonia»
9. отклик: **no** — Open online survey with no denominator of invited students — Page 3, Section 2.1 — «The poll received responses from 172 Mysore university students aged 18 to 30.»

Правки:
- 

Проверено: да
---

## ST064 · Banker 2022 · iScience

Основной отчёт R0861: [текст](../../fulltext/text/R0861.txt) — «Disrupted computations of social control in individuals with obsessive-compulsive and misophonia symptoms.» — [DOI](https://doi.org/10.1016/j.isci.2022.104617)
Не выписано ИИ: No sample was excluded as recruited for misophonia. Not extracted: the high and low Miso-OC groups (n=260 each, top and bottom quartiles of a factor score) and the other quartile and median-split groups. They are subsets of the same sample defined by factor or symptom scores, not separately recruited samples or misophonia case definitions.
Расхождения в тексте: The band counts in the Figure 1 legend (530 subclinical, 463 mild, 168 moderate, 14 severe, 0 extreme) add up to 1,175 and match the cumulative counts in the text: 645 at >=5 and 182 at >=10. Percentages check: 645/1175 = 54.9%; 182/1175 = 15.5%. The reported score range of 0-19 matches the 0 extreme scores. Participant flow: 1,269 - 38 - 9 - 47 = 1,175. There are no disagreements between text and figure.
Заметка ИИ: There is one eligible sample: Prolific US adults, n=1,175, all given the A-MISO-S. Age, sex and data collection dates are not reported for the whole sample. The A-MISO-S language version and its validation status are not stated, so JBI item 6 is rated unclear. There was no funding or COI statement in the text provided.

### ST064-1 · Prolific online sample, USA, adults 18-64, n=1,175
Отчёты: R0861 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **645 / 1175** | 54.9 | Results, Misophonia characterization; Figure 1 legend | «54.9% of participants had clinically significant symptoms (n = 645, total score: 5–24)» |
| E2 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **182 / 1175** | 15.5 | Results, Misophonia characterization; Figure 1 legend | «only 15.5% of participants had at least moderate symptoms (n = 182, total score: 10–24)» |
| E3 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **14 / 1175** | 1.2 | Results, Figure 1 legend | «14 reported severe symptoms (1.2%), and 0 reported extreme symptoms (0%).» |
| E4 | all | A-MISO-S · A-MISO-S>=20 | **L2** | **0 / 1175** | 0.0 | Results, Figure 1 legend | «and 0 reported extreme symptoms (0%).» |

- E1: источник порога: developer paper; правило: A-MISO-S row; L1 >=5; G1 sum of bands; у авторов: «clinically significant symptoms»; главная у авторов: no; период: current; заметка: The authors report both >=5 and >=10 and name neither as their main estimate. Check against Figure 1: 463 + 168 + 14 + 0 = 645.
- E2: источник порога: developer paper; правило: A-MISO-S row; L2 >=10 (recommended); G1 sum of bands; у авторов: «at least moderate symptoms»; главная у авторов: no; период: current; заметка: The recommended L2 definition (G11). Check against Figure 1: 168 + 14 + 0 = 182.
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G2 above L2 cut-off; у авторов: «severe symptoms»; главная у авторов: no; период: current; **расчёт: 14 severe + 0 extreme = 14 (Figure 1 legend)**
- E4: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G2 above L2 cut-off; у авторов: «extreme symptoms»; главная у авторов: no; период: current; заметка: Consistent with the reported score range of 0-19.

**Ключевые поля выборки:**
- **n_analysed: 1175** — Results, Misophonia characterization; Figure 1 — «The histogram shows the spread of total scores from the A-MISO-S (Amsterdam Misophonia Scale; n = 1,175).»
- **population: gp_other** — STAR Methods, Experimental model and subject details — «Participants were recruited from Prolific (www.prolific.co), an online research participant recruitment site»
- **sampling: convenience** — STAR Methods, Experimental model and subject details — «Potential participants opted to take part in the study based on a brief description»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — STAR Methods, Experimental model and subject details — «with the eligibility criteria of (1) age between 18 and 64, (2) currently living in the United States, (3) >90% approval rating in Prolific.»
- setting: online panel (Prolific) — STAR Methods, Experimental model and subject details — «Participants were recruited from Prolific (www.prolific.co), an online research participant recruitment site»
- data_years: NR — NA
- design: cross-sectional — STAR Methods, Experimental model and subject details — «Participants were enrolled in the study as part of a larger online project examining social cognition and mental health.»
- topic_disclosed: yes — STAR Methods, Experimental model and subject details — «a brief description informing them that they would be completing surveys assessing mood, personality, and sensitivity to certain sounds»
- inclusion_exclusion: Age 18-64, living in the USA, >90% Prolific approval rating. Excluded: non-completion (38), exceeding the time limit (9), missed attention checks or ID errors (47). — STAR Methods, Experimental model and subject details — «In total, 1,269 individuals attempted the study, 38 were excluded for non-completion, 9 were excluded for exceeding the time limit, and 47 were excluded due to…»
- n_invited: NR — NA
- n_responded: 1269 — STAR Methods, Experimental model and subject details — «In total, 1,269 individuals attempted the study»
- response_rate: NR — NA
- age_mean: NR — NA
- age_sd: NR — NA
- age_min: NR — STAR Methods, Experimental model and subject details — «age between 18 and 64»
- age_max: NR — STAR Methods, Experimental model and subject details — «age between 18 and 64»
- age_group: adults — STAR Methods, Experimental model and subject details — «age between 18 and 64»
- pct_female: NR — Table 2 — «Sex (female) | 143 (55.0%) | 114 (43.8%)»
- informant: self — STAR Methods, Misophonic and other psychiatric measures — «the Amsterdam Misophonia Scale (A-MISO-S), a 7-item self-report measure»
- mode: online — Limitations of the study — «the online nature of the study meant reliance on self-report data for measures of psychiatric symptoms»
- instruments: A-MISO-S (self-report; language version not stated; US sample, presumably English) — STAR Methods, Misophonic and other psychiatric measures — «participants completed the Amsterdam Misophonia Scale (A-MISO-S), a 7-item self-report measure assessing the severity of misophonia symptoms»
- instrument_validated_in_language: NR — Limitations of the study — «We believe the A-MISO-S to be a robust measure of misophonia, as it has been widely used in research and shows preliminary validity (Naylor et al., 2020; Schrö…»
- pub_status: journal — Header — «Year: 2022; venue: iScience; DOI: 10.1016/j.isci.2022.104617»
- language: English — Full text — «Disrupted computations of social control in individuals with obsessive-compulsive and misophonia symptoms»
- funding_coi: NR (no funding or COI statement in the text provided) — NA
- notes: Age and sex are reported only for the high and low Miso-OC quartile groups (n=260 each, Table 2), not for the full sample of 1,175. Age 18-64 is the eligibility range only, so age_min and age_max are NR. Data collection years are not reported. 1,041 of the 1,175 also completed the social controllability task. Recruited through Prolific; no quota or representativeness is stated. Per the text, the last A-MISO-S item is free-response. The A-MISO-S language version is not stated. The authors say no psychometrically validated misophonia scale exists yet.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is Prolific users living in the US, which covers only part of the US adult population. — STAR Methods, Experimental model and subject details — «Participants were recruited from Prolific (www.prolific.co), an online research participant recruitment site»
2. способ отбора: **no** — Volunteers opted in on an online non-probability panel. — STAR Methods, Experimental model and subject details — «Potential participants opted to take part in the study based on a brief description»
3. размер выборки: **yes** — n = 1,175, which is >= 385. — Results, Figure 1 — «(Amsterdam Misophonia Scale; n = 1,175)»
4. описание выборки и условий: **no** — Setting and country are reported. Age and sex of the full sample and the dates of data collection are not (age and sex only for the quartile subgroups). — Table 2 note — «Demographic information is shown for the high (n = 260) and low (n = 260) Miso-OC groups.»
5. охват (пропуски): **yes** — 94 of the 1,269 who attempted the study were excluded (7.4%, <= 10%); 47 of them (3.7%) for non-completion or exceeding the time limit. — STAR Methods, Experimental model and subject details — «1,269 individuals attempted the study, 38 were excluded for non-completion, 9 were excluded for exceeding the time limit, and 47 were excluded due to missed at…»
6. валидность определения случая: **unclear** — The primary L2 definition, A-MISO-S >=10, is an anchored cut-off. But the language version is not stated, and the authors say no psychometrically validated scale exists, so validation of the version used is unclear. — Limitations of the study — «future work should reinvestigate the results of this study once a psychometrically validated scale for misophonia is established»
7. единое надёжное измерение: **unclear** — Everyone had the same instrument, mode and severity bands, but no internal consistency is reported for this sample or stated for the source. — STAR Methods, Misophonic and other psychiatric measures — «Total scores range from 0 to 24, with score categories of 0–4 (subclinical), 5–9 (mild), 10–14 (moderate), 15–19 (severe), and 20–24 (extreme; Schröder et al.,…»
8. статистика (числитель и знаменатель): **yes** — Band counts and the denominator are given, so the CI can be calculated. — Results, Figure 1 legend — «530 participants reported subclinical symptoms (45.1%), 463 participants reported mild symptoms (39.4%), 168 participants reported moderate symptoms (14.3%), 1…»
9. отклик: **no** — Open opt-in Prolific study with no count of people invited and no handling of non-response. — STAR Methods, Experimental model and subject details — «Potential participants opted to take part in the study based on a brief description»

Правки:
- 

Проверено: да
---

## ST065 · Guetta 2022 · PloS one

Основной отчёт R0906: [текст](../../fulltext/text/R0906.txt) — «Examining emotional functioning in misophonia: The role of affective instability and difficulties with emotion regulation.» — [DOI](https://doi.org/10.1371/journal.pone.0263230)
Расхождения в тексте: The results text gives 13.47% (n = 40) and the Discussion gives 13.5%. Both match 40/297. Table 2 says N = 265 for the correlations, so 32 participants were missing data on at least one measure. The prevalence estimate uses all 297 participants. The text calls the MQ Severity Scale the 'Impairment Subscale' and gives its range as 0-15.
Заметка ИИ: There is one eligible sample with one L2 estimate (MQ MSS>=7, 40/297). No prevalence is reported by sex or age band. The country (USA) is inferred, not stated. The data year is not reported.

### ST065-1 · MTurk online adults, USA (inferred), n=297
Отчёты: R0906 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **40 / 297** | 13.5 | Results, Descriptive statistics | «Over a tenth of the sample (13.47%, n = 40) reported clinically significant misophonia symptoms that cause impairment in their everyday lives, as indicated by a score of seven or higher on the MQ Impairment Subscale [6].» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 L2 (recommended); у авторов: «clinically significant misophonia symptoms that cause impairment»; главная у авторов: yes; период: NR; заметка: The paper calls the MSS the 'Impairment Subscale' (0-15). 40/297 = 13.47%, which confirms the denominator of 297. The Discussion rounds this to 13.5%.

**Ключевые поля выборки:**
- **n_analysed: 297** — Methods, Participants; Results, Descriptive statistics — «we utilized data from the 297 participants who responded correctly to all three attention checks»
- **population: gp_other** — Methods, Participants; Discussion — «the sampling procedure did not selectively recruit individuals self-identifying with misophonia»
- **sampling: convenience** — Methods, Participants — «recruited using the online Amazon Mechanical Turk (MTurk) platform»

**Остальные поля:**
- clinical_group: NA — Methods, Participants — «a nonclinical sample of 297 adults»
- country: USA — Discussion, limitations paragraph — «had a higher percentage of White participants (83.2%) than is representative of the United States population (76.3%»
- setting: online panel (Amazon Mechanical Turk, data collected via REDCap) — Methods, Participants; Procedures — «a nonclinical sample of 297 adults recruited using the online Amazon Mechanical Turk (MTurk) platform»
- data_years: NR (first few months of COVID-19 pandemic; year not stated) — Introduction, last paragraph — «Data were collected over the first few months of COVID-19»
- design: cross-sectional — Discussion, limitations — «our data were cross-sectional»
- topic_disclosed: NR — Methods, Procedures — «All participants completed a battery of self-report questionnaires related to emotional functioning, mental health symptoms, COVID-19-related stress, and misop…»
- inclusion_exclusion: Read/understand English; age 18-65; MTurk approval rating >=99%; excluded those failing any of 3 attention checks — Methods, Participants — «Inclusion criteria required participants to (a) be able to read and understand English, (b) be between 18–65 years old, and (c) have an MTurk participant appro…»
- n_invited: NR — Methods, Participants — «Of the 384 participants who completed the study»
- n_responded: 384 — Methods, Participants — «Of the 384 participants who completed the study, we utilized data from the 297 participants who responded correctly to all three attention checks.»
- response_rate: NR — Methods, Participants — «Of the 384 participants who completed the study»
- age_mean: 39.13 — Table 1 — «Age | 39.13 (11.52)»
- age_sd: 11.52 — Table 1 — «Age | 39.13 (11.52)»
- age_min: 18 — Methods, Participants — «be between 18–65 years old»
- age_max: 65 — Methods, Participants — «be between 18–65 years old»
- age_group: adults — Methods, Participants — «a nonclinical sample of 297 adults»
- pct_female: 47.5 — Table 1 — «Female | | 141 (47.5)»
- informant: self — Methods, Procedures — «All participants completed a battery of self-report questionnaires»
- mode: online — Methods, Procedures — «Data were collected online via REDCap and MTurk»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), English — Methods, Measures — «The MQ contains 17 items across three subscales: Symptom Subscale, Emotions and Behaviors Subscale, and Impairment Subscale.»
- instrument_validated_in_language: yes — Methods, Measures (MQ) — «Initial validation of the MQ demonstrated good internal consistency (α = .86 - .89; [6]).»
- pub_status: journal — Header — «Venue: PloS one; DOI: 10.1371/journal.pone.0263230»
- language: English — Full text — «Examining emotional functioning in misophonia: The role of affective instability and difficulties with emotion regulation»
- funding_coi: NR — Full text — «participants received $5.00 for completing the surveys»
- notes: The country is not stated explicitly; USA is inferred from the comparison with the US census and from the Duke IRB approval. Ages 18-65 are the eligibility range, not the observed range. The year of data collection is not stated (early COVID-19, likely 2020). 87 of the 384 completers were excluded for failing attention checks. The correlation and regression analyses use N=265, but the prevalence denominator is 297 (40/297 = 13.47%). The paper calls the MSS item the 'Impairment Subscale' (0-15). No prevalence by sex is reported.

**Риск смещения (JBI):**
1. рамка выборки: **no** — MTurk workers are only part of the general/community population the study describes. — Discussion — «the sample was recruited from Amazon’s MTurk ... limiting the generalizability of study results»
2. способ отбора: **no** — Volunteer opt-in online non-probability panel. — Methods, Participants — «recruited using the online Amazon Mechanical Turk (MTurk) platform»
3. размер выборки: **no** — n=297 < 385. — Methods, Participants — «we utilized data from the 297 participants»
4. описание выборки и условий: **unclear** — Age, sex and setting are reported; the country is only implied; the dates of data collection are missing. — Table 1; Introduction — «Data were collected over the first few months of COVID-19»
5. охват (пропуски): **yes** — The prevalence uses all 297 analysed participants; attention-check failures were excluded by design. — Results, Descriptive statistics — «Over a tenth of the sample (13.47%, n = 40)»
6. валидность определения случая: **yes** — MQ Severity Scale >=7 in the original English version (L2 anchored cut-off). — Methods, Measures (MQ) — «As per Wu et al. 2014, a cut score of seven on this item indicates clinically significant misophonia symptomology.»
7. единое надёжное измерение: **yes** — Everyone completed the same online self-report MQ; internal consistency is reported for this sample. — Methods, Measures (MQ) — «Cronbach’s alpha in the current sample was also good for the MQ total score (α = .89)»
8. статистика (числитель и знаменатель): **yes** — Numerator 40 and denominator 297 are clear; a CI can be calculated. — Results, Descriptive statistics — «Over a tenth of the sample (13.47%, n = 40) reported clinically significant misophonia symptoms»
9. отклик: **no** — Open MTurk survey with no denominator of invited people; non-response is not handled. — Methods, Participants — «Of the 384 participants who completed the study»

Правки:
- 

Проверено: да
---

## ST066 · Hansen 2022 · Frontiers in neuroscience

Основной отчёт R0907: [текст](../../fulltext/text/R0907.txt) — «Neural evidence for non-orofacial triggers in mild misophonia.» — [DOI](https://doi.org/10.3389/fnins.2022.880759)
Расхождения в тексте: 1) Sex: the Participants section reports 14 females and 5 males, but the group breakdown gives 4F/3M (higher) + 9F/3M (lower) = 13F/6M. The sex-subgroup estimates use the breakdown counts (13 and 6) and flag the discrepancy. 2) The lower group is said to have 'all scored below 4' on the A-MISO-S, yet its range is printed as 0-4. Neither reading affects the >=5 or >=10 counts. 3) A-MISO-S counts come from group ranges, not from a reported count. Supplementary Table 1 (not available to us) should be checked, including for MAQ-2 counts.
Заметка ИИ: An fMRI study of 19 community adults, not designed to estimate prevalence. All prevalence estimates are derived from the post hoc group split and the A-MISO-S ranges. No participant reached A-MISO-S >=10 (0/19). 7/19 scored A-MISO-S >=5, which is also the composite >=20 group.

### ST066-1 · Ohio State University community fMRI sample, USA, n=19
Отчёты: R0907 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **0 / 19** | 0.0 | Materials and methods, Misophonia questionnaires | «individuals in the "higher misophonia" group all scored above 4 on the A-MISO-S (Mean = 7.7, SD = 1.1, Range = 6–9) ... "lower misophonia" group all scored below 4 (Mean = 2.2, SD = 1.5, Range = 0–4)» |
| E2 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **7 / 19** | 36.8 | Materials and methods, Misophonia questionnaires | «individuals in the "higher misophonia" group all scored above 4 on the A-MISO-S (Mean = 7.7, SD = 1.1, Range = 6–9), corresponding with "mild" misophonia» |
| E3 | female | A-MISO-S · A-MISO-S>=5 | **L1** | **4 / 13** | 30.8 | Materials and methods, Misophonia questionnaires | «seven individuals with higher misophonia scores (... four females, three males ...) and twelve individuals with lower misophonia scores (... nine females, three males ...)» |
| E4 | male | A-MISO-S · A-MISO-S>=5 | **L1** | **3 / 6** | 50.0 | Materials and methods, Misophonia questionnaires | «seven individuals with higher misophonia scores (... four females, three males ...) and twelve individuals with lower misophonia scores (... nine females, three males ...)» |
| E5 | female | A-MISO-S · A-MISO-S>=10 | **L2** | **0 / 13** | 0.0 | Materials and methods, Misophonia questionnaires | «Range = 6–9» |
| E6 | male | A-MISO-S · A-MISO-S>=10 | **L2** | **0 / 6** | 0.0 | Materials and methods, Misophonia questionnaires | «Range = 6–9» |
| E7 | all | multiple · composite score (MAS-1, MAQ-2, A-MISO-S equally weighted, 0-100) >=20 | **L1** | **7 / 19** | 36.8 | Materials and methods, Misophonia questionnaires | «splitting our sample post hoc using a score of 20 as cutoff, resulting in seven individuals with higher misophonia scores (mean = 28.7, range = 20.5–37.3 ...) and twelve individuals with lower misophonia scores» |
| E8 | female | multiple · composite score (MAS-1, MAQ-2, A-MISO-S equally weighted, 0-100) >=20 | **L1** | **4 / 13** | 30.8 | Materials and methods, Misophonia questionnaires | «(mean = 28.7, range = 20.5–37.3; four females, three males; mean age = 24.2) ... (mean = 9.6, range = 0–17.7; nine females, three males; mean age = 26.4)» |
| E9 | male | multiple · composite score (MAS-1, MAQ-2, A-MISO-S equally weighted, 0-100) >=20 | **L1** | **3 / 6** | 50.0 | Materials and methods, Misophonia questionnaires | «(mean = 28.7, range = 20.5–37.3; four females, three males; mean age = 24.2) ... (mean = 9.6, range = 0–17.7; nine females, three males; mean age = 26.4)» |

- E1: источник порога: developer paper; правило: A-MISO-S row; >=10 L2; G1; у авторов: «NR (no participant reached 'moderate')»; главная у авторов: no; период: current; **расчёт: Higher group A-MISO-S range 6-9 and lower group range 0-4, so no participant scored >=10**; заметка: Zero cases. Check against Supplementary Table 1.
- E2: источник порога: developer paper; правило: A-MISO-S row; >=5 L1; G1 sum of bands; у авторов: «mild misophonia»; главная у авторов: no; период: current; **расчёт: Higher group (n=7) A-MISO-S range 6-9 (all >=5); lower group (n=12) range 0-4 (all <5): 7 of 19**; заметка: The lower group is described as 'below 4' but its range is 0-4. Either way all are <5.
- E3: источник порога: developer paper; правило: A-MISO-S row; >=5 L1; G1; у авторов: «mild misophonia»; главная у авторов: no; период: current; **расчёт: Higher group 4 females; lower group 9 females; n = 4 + 9 = 13**; заметка: Participants section reports 14 females in total, but the group breakdown sums to 13. Denominator uncertain (13 or 14).
- E4: источник порога: developer paper; правило: A-MISO-S row; >=5 L1; G1; у авторов: «mild misophonia»; главная у авторов: no; период: current; **расчёт: Higher group 3 males; lower group 3 males; n = 3 + 3 = 6**; заметка: Participants section reports 5 males in total, but the group breakdown sums to 6. Denominator uncertain (5 or 6).
- E5: источник порога: developer paper; правило: A-MISO-S row; >=10 L2; у авторов: «NR»; главная у авторов: no; период: current; **расчёт: Maximum A-MISO-S in sample = 9; females 4 + 9 = 13 from the group breakdown**; заметка: Female denominator 13 vs 14 discrepancy.
- E6: источник порога: developer paper; правило: A-MISO-S row; >=10 L2; у авторов: «NR»; главная у авторов: no; период: current; **расчёт: Maximum A-MISO-S in sample = 9; males 3 + 3 = 6 from the group breakdown**; заметка: Male denominator 6 vs 5 discrepancy.
- E7: источник порога: study's own; правило: G3 study-defined threshold on an unpublished composite (no published thresholds) -> L1; instrument coded multiple becau…; у авторов: «higher misophonia scores»; главная у авторов: no; период: NR; заметка: Post hoc split chosen to recreate Kumar et al. (2021) groups. Not a percentile of the sample, so not coded E3, but the reviewer may prefer NR or E3. Same 7 people as A-MISO-S >=5.
- E8: источник порога: study's own; правило: G3 study-defined composite threshold -> L1; у авторов: «higher misophonia scores»; главная у авторов: no; период: NR; **расчёт: Females 4 (higher) + 9 (lower) = 13**; заметка: Female total 13 vs 14 discrepancy.
- E9: источник порога: study's own; правило: G3 study-defined composite threshold -> L1; у авторов: «higher misophonia scores»; главная у авторов: no; период: NR; **расчёт: Males 3 (higher) + 3 (lower) = 6**; заметка: Male total 6 vs 5 discrepancy.

**Ключевые поля выборки:**
- **n_analysed: 19** — Materials and methods, Participants — «One adult was excluded for excessive motion ... resulting in nineteen adults (14 females, 5 males, mean age = 25.6) included in the present analyses.»
- **population: gp_other** — Discussion — «It is worth noting that the participants we studied were members of the general population, not specifically misophonia-sufferers.»
- **sampling: convenience** — Materials and methods, Participants — «All participants were recruited via advertisements on social media, flyers, and study websites.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — Materials and methods, Participants; Scan parameters — «All experimental methods were approved by The Ohio State University Institutional Review Board»
- setting: community (volunteers recruited through social media, flyers and study websites; neuroimaging at Ohio State University) — Materials and methods, Participants — «All participants were recruited via advertisements on social media, flyers, and study websites. Participants were part of a larger ongoing longitudinal study o…»
- data_years: NR — NR — «NR»
- design: other — Materials and methods, Participants — «Participants were part of a larger ongoing longitudinal study of brain development and were paid a total of $30 for participating in the neuroimaging protocol.»
- topic_disclosed: NR — Materials and methods, Participants; Discussion — «They were not recruited (or excluded) for having particular misophonic triggers.»
- inclusion_exclusion: Adults from a longitudinal brain-development study; excluded for excessive motion in resting-state fMRI (1 of 20) — Materials and methods, Participants; Resting state — «One participant of the original 20 had 237 censored timepoints (40.9%) and was thus removed from further analyses.»
- n_invited: NR — NR — «NR»
- n_responded: 20 — Materials and methods, Participants — «Twenty adults participated in this study.»
- response_rate: NR — NR — «NR»
- age_mean: 25.6 — Materials and methods, Participants — «nineteen adults (14 females, 5 males, mean age = 25.6)»
- age_sd: NR — NR — «NR»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- age_group: adults — Materials and methods, Participants — «Twenty adults participated in this study.»
- pct_female: 73.7 — Materials and methods, Participants — «nineteen adults (14 females, 5 males, mean age = 25.6)»
- informant: self — Materials and methods, Misophonia questionnaires — «All participants completed the Misophonia Activation Scale (MAS-1) (Fitzmaurice, 2010), the Misophonia Assessment Questionnaire (MAQ-2) (Johnson, 2014), and th…»
- mode: NR — NR — «NR»
- instruments: MAS-1 (language NR, presumably English); MAQ-2 (language NR); A-MISO-S (language NR); study composite of the three (0-100) — Materials and methods, Misophonia questionnaires — «Using a composite score that equally weighted the three misophonic assessment surveys (see Supplementary Table 1), with higher scores denoting more severe miso…»
- instrument_validated_in_language: NR — Materials and methods, Misophonia questionnaires — «the Amsterdam Misophonia Scale (A-MISO-S) (Schröder et al., 2013)»
- pub_status: journal — Header — «Frontiers in neuroscience; DOI: 10.3389/fnins.2022.880759»
- language: English — Full text — «Neural evidence for non-orofacial triggers in mild misophonia»
- funding_coi: Alfred P. Sloan Foundation (FG-2018-10994) and Ohio State University; no conflicts declared — Funding; Conflict of interest — «Funding was provided by the Alfred P. Sloan Foundation (FG-2018-10994) to ZS and the Chronic Brain Injury and College of Arts and Sciences at The Ohio State Un…»
- notes: Small fMRI study (n=19), not designed to estimate prevalence; prevalence is derived from the reported A-MISO-S ranges of the post hoc groups. Supplementary Table 1 (individual MAS-1, MAQ-2 and A-MISO-S scores) was not available to us; the reviewer should check it for MAQ-2 counts and exact A-MISO-S values. Participants came from a larger longitudinal study at Z-lab, Ohio State, so they may overlap with other reports from this lab. Sex breakdown is inconsistent (see consistency_notes).

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame was people who answered social-media and flyer advertisements for a brain-development study. This does not cover the general population the authors refer to. — Materials and methods, Participants — «All participants were recruited via advertisements on social media, flyers, and study websites.»
2. способ отбора: **no** — Volunteers who opted in through advertisements (convenience sample). — Materials and methods, Participants — «All participants were recruited via advertisements on social media, flyers, and study websites.»
3. размер выборки: **no** — n=19, below 385. — Materials and methods, Participants — «resulting in nineteen adults»
4. описание выборки и условий: **unclear** — Mean age, sex, setting and institution are reported, but the dates of data collection are not. — Materials and methods, Participants — «nineteen adults (14 females, 5 males, mean age = 25.6)»
5. охват (пропуски): **yes** — All participants completed the questionnaires. 1 of 20 (5%) was excluded for fMRI motion, not for missing misophonia data. — Materials and methods, Misophonia questionnaires; Resting s… — «All participants completed the Misophonia Activation Scale (MAS-1)»
6. валидность определения случая: **unclear** — Rated on A-MISO-S >=10 (L2), an anchored cut-off. The language version and its validation are not stated. — Materials and methods, Misophonia questionnaires — «the Amsterdam Misophonia Scale (A-MISO-S) (Schröder et al., 2013)»
7. единое надёжное измерение: **unclear** — Everyone got the same instruments, but the mode of administration and any reliability coefficients are not reported. — Materials and methods, Misophonia questionnaires — «All participants completed the Misophonia Activation Scale (MAS-1) (Fitzmaurice, 2010), the Misophonia Assessment Questionnaire (MAQ-2) (Johnson, 2014), and th…»
8. статистика (числитель и знаменатель): **yes** — Group counts (7 vs 12) and A-MISO-S ranges allow numerators and denominators to be traced; a CI can be calculated. — Materials and methods, Misophonia questionnaires — «resulting in seven individuals with higher misophonia scores ... and twelve individuals with lower misophonia scores»
9. отклик: **no** — Recruited by open advertisement with no denominator of invited people and no handling of non-response. — Materials and methods, Participants — «All participants were recruited via advertisements on social media, flyers, and study websites.»

Правки:
- 

Проверено: да
---

## ST067 · Heller 2022 · Frontiers in psychology

Основной отчёт R0910: [текст](../../fulltext/text/R0910.txt) — «Identification of Everyday Sounds Affects Their Pleasantness.» — [DOI](https://doi.org/10.3389/fpsyg.2022.894034)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R0314 (ST024), R0368 (ST027), R0385 (ST030): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap
Расхождения в тексте: The only misophonia-related count, 5 of 60 participants with a Sound Intolerance score of 4.5 or more, pools Experiment 1 (n=39) and Experiment 2 (n=21). Since 39 + 21 = 60, the denominator matches the analysed totals. Counts for each experiment appear only in Supplementary Figure S1, which was not provided. Experiment 2 reports 32 participants with 11 disqualified, giving 21 analysed, which is consistent. Experiment 1 does not report how many participants were excluded. The age range 18-22 is given once for "all participants" of both experiments. Percent female was computed from the counts: Exp 1 17/39 = 43.6%; Exp 2 10/21 = 47.6%.
Заметка ИИ: This is an experimental study of sound pleasantness, not a prevalence study. The only measure is a 2-item MisoQuest subset with a study-defined cut-off (score of 4.5 or more), coded L1 under rule G3. The pooled 5/60 estimate is listed under the Experiment 1 sample only, to avoid double counting.

### ST067-1 · Experiment 1, CMU psychology subject pool, USA, n=39
Отчёты: R0910 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MisoQuest · mean of 2 MisoQuest items >=4.5 (5-point scale) | **L1** | **NR / 39** |  | Comparison Across Experiments 1 and 2, Sound Intolerance Se… | «The distributions of Sound Intolerance scores are shown in the blue bars for Experiment 1 and in the orange bars for Experiment 2 in Supplementary Figure S1.» |
| E2 | Experiment 1 + Experiment 2 combined | MisoQuest · mean of 2 MisoQuest items >=4.5 (5-point scale) | **L1** | **5 / 60** | 8.3 | Comparison Across Experiments 1 and 2, Sound Intolerance Se… | «Only five of our 60 participants earned a score of 4.5 or greater.» |

- E1: источник порога: study's own; правило: MisoQuest row; G3 subset of items with study-defined threshold; у авторов: «Sound Intolerance score of 4.5 or greater»; главная у авторов: no; период: NR; заметка: Experiment 1-specific count not reported in main text (only in Supplementary Figure S1, not available). Authors do not present this as a prevalence estimate.
- E2: источник порога: study's own; правило: MisoQuest row; G3 subset of items with study-defined threshold; у авторов: «Sound Intolerance score of 4.5 or greater»; главная у авторов: no; период: NR; заметка: Pools two separately recruited samples (Exp 1 n=39; Exp 2 n=21); listed here only to avoid double counting. Not a prevalence estimate in the authors' framing.

**Ключевые поля выборки:**
- **n_analysed: 39** — Methods: Experiment 1, Participants — «Experiment 1 had 39 participants who passed the screening (21 male, 17 female, 1 other).»
- **population: university_students** — Methods: Experiment 1, Participants — «All participants ranged in age from 18 to 22, with the majority being undergraduate students.»
- **sampling: convenience** — Methods: Experiment 1, Participants — «Recruitment for both experiments was conducted through Carnegie Mellon University’s (CMU) Psychology Department for course credit.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — Methods: Experiment 1, Participants — «Recruitment for both experiments was conducted through Carnegie Mellon University’s (CMU) Psychology Department for course credit.»
- setting: university (psychology department participant pool, online experiment) — Methods: Experiment 1, Participants — «Recruitment for both experiments was conducted through Carnegie Mellon University’s (CMU) Psychology Department for course credit.»
- data_years: NR — NR — «NR»
- design: other — Methods: Experiment 1, Procedure — «They next completed questions about age, gender, hearing status, and sound tolerance. The sound tolerance items were taken directly from MisoQuest»
- topic_disclosed: NR — NR — «NR»
- inclusion_exclusion: Excluded: under 18, abnormal hearing; data removed if self-reported abnormal hearing, failed headphone screen, or failed oddball attention check — Methods: Experiment 1, Participants; Data Quality Criteria — «Participants under 18 years old or with abnormal hearing were excluded.»
- n_invited: NR — NR — «NR»
- n_responded: NR — NR — «NR»
- response_rate: NR — NR — «NR»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: 18 — Methods: Experiment 1, Participants — «All participants ranged in age from 18 to 22»
- age_max: 22 — Methods: Experiment 1, Participants — «All participants ranged in age from 18 to 22»
- age_group: adults — Methods: Experiment 1, Participants — «All participants ranged in age from 18 to 22»
- pct_female: 43.6 — Methods: Experiment 1, Participants — «(21 male, 17 female, 1 other)»
- informant: self — Methods: Experiment 1, Procedure — «They were asked to agree or disagree on a five-point Likert scale to the statements»
- mode: online — Methods: Experiment 1, Procedure — «The survey typically took 30–40 min to complete via a secure online survey platform (Qualtrics).»
- instruments: Two MisoQuest items (English wording), averaged as 'Sound Intolerance' score (5-point Likert); plus one hyperacusis-related item not part of the score — Methods: Experiment 1, Procedure — «“I find some sounds made by the human body unbearable,” and, “Some sounds bother me so much that I have difficulty controlling my emotions.” These two question…»
- instrument_validated_in_language: NR — Methods: Experiment 1, Procedure — «The sound tolerance items were taken directly from MisoQuest (Siepsiak et al., 2020)»
- pub_status: journal — Header — «Frontiers in psychology; DOI: 10.3389/fpsyg.2022.894034»
- language: English — Full text — «Identification of Everyday Sounds Affects Their Pleasantness»
- funding_coi: Funding NR; authors declare no conflict of interest — Conflict of Interest — «The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict…»
- notes: Possible overlap with R0314 (ST024), R0368 (ST027), R0385 (ST030): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Experimental study of sound pleasantness; misophonia measured only by a 2-item MisoQuest subset. The only count reported (5 of 60 with score >=4.5) pools Experiment 1 and Experiment 2; per-experiment counts are not reported (distributions only in Supplementary Figure S1, not provided). The combined estimate is listed here only, to avoid double counting. Number of Exp 1 participants excluded for data quality not rep…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is one university's psychology course-credit pool; the authors describe a normative/general student population — Methods: Experiment 1, Participants; Discussion — «Because this was a normative study of a student population»
2. способ отбора: **no** — Volunteer convenience sample for course credit — Methods: Experiment 1, Participants — «conducted through Carnegie Mellon University’s (CMU) Psychology Department for course credit»
3. размер выборки: **no** — n = 39 < 385 — Methods: Experiment 1, Participants — «Experiment 1 had 39 participants who passed the screening»
4. описание выборки и условий: **unclear** — Age range, sex, setting (CMU) given; data collection dates missing — Methods: Experiment 1, Participants — «All participants ranged in age from 18 to 22, with the majority being undergraduate students.»
5. охват (пропуски): **unclear** — Number excluded by data-quality criteria and missing sound-intolerance data not reported for Exp 1 — Data Quality Criteria — «Participant responses were removed from the analysis if: (1) they indicated that they did not have normal hearing; (2) they failed the headphone screening; or …»
6. валидность определения случая: **no** — Two-item MisoQuest subset with a study's own threshold (>=4.5); no validated cut-off — Comparison Across Experiments, Sound Intolerance Self-Rating — «Only five of our 60 participants earned a score of 4.5 or greater.»
7. единое надёжное измерение: **unclear** — Same items and online mode for all, but no reliability reported for the 2-item score — Methods: Experiment 1, Procedure — «These two questions’ averaged score served as a measure of general Sound Intolerance.»
8. статистика (числитель и знаменатель): **no** — Only a count pooled over two separately recruited samples is given; no per-sample numerator, no CI — Comparison Across Experiments, Sound Intolerance Self-Rating — «Only five of our 60 participants earned a score of 4.5 or greater.»
9. отклик: **unclear** — Number invited from the participant pool not reported; response rate unknown — Methods: Experiment 1, Participants — «Experiment 1 had 39 participants who passed the screening»

Правки:
- 

Проверено: да
### ST067-2 · Experiment 2, CMU psychology subject pool, USA, n=21
Отчёты: R0910 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MisoQuest · mean of 2 MisoQuest items >=4.5 (5-point scale) | **L1** | **NR / 21** |  | Comparison Across Experiments 1 and 2, Sound Intolerance Se… | «The distributions of Sound Intolerance scores are shown in the blue bars for Experiment 1 and in the orange bars for Experiment 2 in Supplementary Figure S1.» |

- E1: источник порога: study's own; правило: MisoQuest row; G3 subset of items with study-defined threshold; у авторов: «Sound Intolerance score of 4.5 or greater»; главная у авторов: no; период: NR; заметка: Experiment 2-specific count not reported in main text; combined 5/60 recorded under the Experiment 1 sample.

**Ключевые поля выборки:**
- **n_analysed: 21** — Methods: Experiment 2, Participants — «There were 21 new young adult participants (10 male, 10 female, 1 other) in Experiment 2.»
- **population: university_students** — Methods: Experiment 2, Participants — «There were 21 new young adult participants (10 male, 10 female, 1 other) in Experiment 2. Otherwise, the recruitment, consent process, and student population were the same as in Experiment 1.»
- **sampling: convenience** — Methods: Experiment 1, Participants — «Recruitment for both experiments was conducted through Carnegie Mellon University’s (CMU) Psychology Department for course credit.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — Methods: Experiment 1, Participants — «Recruitment for both experiments was conducted through Carnegie Mellon University’s (CMU) Psychology Department for course credit.»
- setting: university (psychology department participant pool, online experiment) — Methods: Experiment 2, Participants — «Otherwise, the recruitment, consent process, and student population were the same as in Experiment 1.»
- data_years: NR — NR — «NR»
- design: other — Methods: Experiment 2, Methods, Procedure, and Design — «All methods and procedures were the same as for Experiment 1 except as noted here.»
- topic_disclosed: NR — NR — «NR»
- inclusion_exclusion: As Exp 1: excluded under 18, abnormal hearing; data removed for failed headphone screen or oddball check — Methods: Experiment 2 — «Data from eleven out of 32 people were disqualified from Experiment 2 for failing any one of these criteria.»
- n_invited: NR — NR — «NR»
- n_responded: 32 — Methods: Experiment 2, Methods, Procedure, and Design — «Data from eleven out of 32 people were disqualified from Experiment 2 for failing any one of these criteria.»
- response_rate: NR — NR — «NR»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: 18 — Methods: Experiment 1, Participants — «All participants ranged in age from 18 to 22»
- age_max: 22 — Methods: Experiment 1, Participants — «All participants ranged in age from 18 to 22»
- age_group: adults — Methods: Experiment 2, Participants — «There were 21 new young adult participants»
- pct_female: 47.6 — Methods: Experiment 2, Participants — «(10 male, 10 female, 1 other)»
- informant: self — Methods: Experiment 1, Procedure — «They were asked to agree or disagree on a five-point Likert scale to the statements»
- mode: online — Methods: Experiment 1, Procedure (same in Exp 2) — «The survey typically took 30–40 min to complete via a secure online survey platform (Qualtrics).»
- instruments: Two MisoQuest items (English wording), averaged as 'Sound Intolerance' score (5-point Likert); plus one hyperacusis-related item not part of the score — Methods: Experiment 1, Procedure — «These two questions’ averaged score served as a measure of general Sound Intolerance.»
- instrument_validated_in_language: NR — Methods: Experiment 1, Procedure — «The sound tolerance items were taken directly from MisoQuest (Siepsiak et al., 2020)»
- pub_status: journal — Header — «Frontiers in psychology; DOI: 10.3389/fpsyg.2022.894034»
- language: English — Full text — «Identification of Everyday Sounds Affects Their Pleasantness»
- funding_coi: Funding NR; authors declare no conflict of interest — Conflict of Interest — «The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict…»
- notes: Possible overlap with R0314 (ST024), R0368 (ST027), R0385 (ST030): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. 'New' participants recruited separately from Exp 1, so a separate sample. Age range stated for 'all participants' of both experiments. The only count (5/60 with Sound Intolerance >=4.5) pools both experiments and is listed under the Experiment 1 sample.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is one university's psychology course-credit pool — Methods: Experiment 2, Participants — «Otherwise, the recruitment, consent process, and student population were the same as in Experiment 1.»
2. способ отбора: **no** — Volunteer convenience sample for course credit — Methods: Experiment 1, Participants — «conducted through Carnegie Mellon University’s (CMU) Psychology Department for course credit»
3. размер выборки: **no** — n = 21 < 385 — Methods: Experiment 2, Participants — «There were 21 new young adult participants»
4. описание выборки и условий: **unclear** — Age range, sex, setting given; dates missing — Methods: Experiment 2, Participants — «There were 21 new young adult participants (10 male, 10 female, 1 other) in Experiment 2.»
5. охват (пропуски): **no** — 11 of 32 (34%) excluded from analysis for data-quality criteria — Methods: Experiment 2, Methods, Procedure, and Design — «Data from eleven out of 32 people were disqualified from Experiment 2 for failing any one of these criteria.»
6. валидность определения случая: **no** — Two-item MisoQuest subset with study's own threshold — Comparison Across Experiments, Sound Intolerance Self-Rating — «Only five of our 60 participants earned a score of 4.5 or greater.»
7. единое надёжное измерение: **unclear** — Same items and mode, but no reliability reported — Methods: Experiment 1, Procedure — «These two questions’ averaged score served as a measure of general Sound Intolerance.»
8. статистика (числитель и знаменатель): **no** — No sample-specific numerator; only a count pooled with Exp 1 — Comparison Across Experiments, Sound Intolerance Self-Rating — «Only five of our 60 participants earned a score of 4.5 or greater.»
9. отклик: **unclear** — Number invited from the participant pool not reported — Methods: Experiment 2 — «Data from eleven out of 32 people were disqualified from Experiment 2»

Правки:
- 

Проверено: да
---

## ST068 · Herrera 2022 · 

Основной отчёт R0912: [текст](../../fulltext/text/R0912.txt) — «Clinical and Neuropsychological Correlates of Misophonia»
Расхождения в тексте: Education: the control mean is 15.03 (SD 1.83) on p.27 but 15.05 (1.83) in Table 1; the Table 1 value applies. Group definition: p.25 says MSS>=7 = misophonia group, then says the misophonia group is the upper quartile of the clinical group. Control MSS mean 2.25 (SD 0.80) vs total 4.53 (SD 3.52) suggests the subset was selected. Panic disorder in the misophonia group is 6.3% in Table 3 but 6.20% in the Discussion. The Table 1 race percentages for the misophonia group use n=31.
Заметка ИИ: Pages are the thesis's printed page numbers; the text has no '=== Page N ===' markers. No funding statement was found.

### ST068-1 · Texas State University students, USA, n=96 (subset drawn from a larger misophonia study)
Отчёты: R0912 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ MSS>=7, then 'upper quartile of the clinical group' (as stated; contradictory) | **NR** | **32 / 96** | 33.3 | Table 1, p.27; p.25 | «Control (n=64) Misophonia (n=32) Entire Sample (N=96)» |
| E2 | female | MQ · MQ MSS>=7, then 'upper quartile of the clinical group' (as stated; contradictory) | **NR** | **19 / 67** | 28.4 | Table 1, p.27 | «Female 75.00% (48) 59.40% (19) 69.80% (67)» |
| E3 | male | MQ · MQ MSS>=7, then 'upper quartile of the clinical group' (as stated; contradictory) | **NR** | **13 / 29** | 44.8 | Table 1, p.27 | «Male 25.00% (16) 40.60% (13) 30.20% (29)» |

- E1: источник порога: developer paper; правило: MQ row; MSS>=7 alone would be L2, but the stated upper-quartile step makes the definition undeterminable -> G6 (possibl…; у авторов: «misophonia group (clinical)»; главная у авторов: no; период: NR; заметка: Groups were formed for a case-control comparison, and the 96 may have been selected by MQ score from a larger study; this is not a prevalence estimate as reported. If MSS>=7 alone was the definition: L2, 33.3%.
- E2: источник порога: developer paper; правило: MQ row; G6 (definition not determinable); у авторов: «misophonia group (clinical)»; главная у авторов: no; период: NR; заметка: Same caveats as the whole-sample estimate.
- E3: источник порога: developer paper; правило: MQ row; G6 (definition not determinable); у авторов: «misophonia group (clinical)»; главная у авторов: no; период: NR; заметка: Same caveats as the whole-sample estimate.

**Ключевые поля выборки:**
- **n_analysed: 96** — Table 1, p.27 — «Entire Sample (N=96)»
- **population: university_students** — p.27, Demographic Variables — «All participants were college students»
- **sampling: convenience** — p.18, Participants — «Ninety-six participants were drawn from a larger study examining the cognitive function and clinical correlates of misophonia. Participants were recruited at Texas State University via ads, flyers, and emails.»

**Остальные поля:**
- clinical_group: NA — p.27 — «All participants were college students»
- country: USA — p.18, Participants — «Participants were recruited at Texas State University via ads, flyers, and emails.»
- setting: university (Texas State University; individual testing in a research lab) — p.18 Participants; p.25 Procedure — «The testing session took place individually in a quiet research lab room.»
- data_years: NR — Title page — «May 2022»
- design: other — p.25-26, Statistical Analyses — «The control and misophonia groups were created by using the MQ single item severity (Wu et al., 2014)»
- topic_disclosed: NR — p.18, Participants — «drawn from a larger study examining the cognitive function and clinical correlates of misophonia. Participants were recruited at Texas State University via ads…»
- inclusion_exclusion: Age 18-65, intact or corrected vision, fluent in English; excluded history of major neurological conditions — p.18, Participants — «Inclusion criteria included minimum age of 18, intact or corrected vision, and fluency in English. Exclusion criteria included age > 65 and any history of majo…»
- n_invited: NR — p.18 — «recruited at Texas State University via ads, flyers, and emails»
- n_responded: NR — p.18 — «Ninety-six participants were drawn from a larger study»
- response_rate: NR — p.18 — «recruited at Texas State University via ads, flyers, and emails»
- age_mean: 20.91 — p.18; Table 1 — «The average age of participants was 20.91 (SD = 2.87).»
- age_sd: 2.87 — p.18; Table 1 — «The average age of participants was 20.91 (SD = 2.87).»
- age_min: NR — p.18 — «Inclusion criteria included minimum age of 18»
- age_max: NR — p.18 — «Exclusion criteria included age > 65»
- age_group: adults — p.18 — «Inclusion criteria included minimum age of 18»
- pct_female: 69.8 — p.18; Table 1 — «The overall study sample consisted of 67 females (69.80%) and 29 males (30.20%).»
- informant: self — p.25, Procedure — «followed by the neuropsychological assessments and the self-report questionnaires, which were counterbalanced»
- mode: NR — p.25, Procedure — «The testing session took place individually in a quiet research lab room.»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), English — p.20, Measures — «Misophonia Questionnaire (MQ; Wu et al., 2014). The MQ consists of 17 items and is comprised of three sections.»
- instrument_validated_in_language: yes — p.20-21, Measures — «The test shows good psychometric properties in non-clinical samples (Wu et al., 2014).»
- pub_status: thesis — Title page — «A thesis submitted to the Graduate Council of Texas State University in partial fulfillment of the requirements for the degree of Master of Arts»
- language: English — Whole text — «CLINICAL AND NEUROPSYCHOLOGICAL CORRELATES OF MISOPHONIA»
- funding_coi: NR — Whole text — «NR»
- notes: Case-control neuropsychological thesis. The 96 were 'drawn from a larger study' with no account of how they were selected. The group definition is contradictory (p.25): MSS>=7 = clinical, then 'we used the upper quartile of the clinical group' for the misophonia group. Control MSS mean 2.25 (SD 0.80) suggests intermediate scorers may have been left out. So 32/96 (33%) may reflect the design (2:1 control:case ratio) rather than prevalence. The reviewer should decide eligibility. MQ was given on the day of testing and again 3-5 weeks later; the report does not say which administration defined t…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Volunteers who answered ads at one university, and an undescribed subset of a larger study; this does not cover all enrolled students — p.18 — «Ninety-six participants were drawn from a larger study ... recruited at Texas State University via ads, flyers, and emails.»
2. способ отбора: **no** — Volunteer opt-in recruitment through ads; the subset selection is not described — p.18 — «Participants were recruited at Texas State University via ads, flyers, and emails.»
3. размер выборки: **no** — n = 96 < 385 — Table 1 — «Entire Sample (N=96)»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; data collection dates are not — p.18; Table 1 — «The average age of participants was 20.91 (SD = 2.87).»
5. охват (пропуски): **unclear** — Missing MQ data are not reported; it is unclear how the 96 were selected from the larger study — p.18 — «Ninety-six participants were drawn from a larger study»
6. валидность определения случая: **unclear** — MQ MSS>=7 (English) would be valid, but the misophonia group is also said to be the upper quartile of the clinical group, so the threshold actually applied is unclear — p.25 — «a score of 7 or more is considered clinical (misophonia group) ... Then, for our misophonia group, we used the upper quartile of the clinical group.»
7. единое надёжное измерение: **yes** — Same MQ for everyone in an individual lab session; alpha reported in this sample — p.21 — «The present study found excellent reliability for the MQ-1 (α = 0.83) and the MQ-2 (α = 0.83).»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator are given (32/96), so a CI can be calculated; the case definition is ambiguous (see item 6) — Table 1 — «Control (n=64) Misophonia (n=32) Entire Sample (N=96)»
9. отклик: **no** — Recruitment by open ads, with no denominator of people invited and no non-response handling — p.18 — «recruited at Texas State University via ads, flyers, and emails»

Правки:
- 

Проверено: да
---

## ST069 · Jakubovski 2022 · Frontiers in psychiatry

Основной отчёт R0922: [текст](../../fulltext/text/R0922.txt) — «Prevalence and clinical correlates of misophonia symptoms in the general population of Germany.» — [DOI](https://doi.org/10.3389/fpsyt.2022.1012424)
Расхождения в тексте: 1) The text and Table 2 give the MQ Severity threshold as '>7', but the Statistical analysis section says 'using the cut-off of 7', and the authors follow Wu et al. (>=7). Which operator was used is unclear. Either way the definition is L2. 2) The Discussion says 'Since the MQ Total Score cut-off was more established we sticked with that criterion', but the primary definition is the MQ Severity Scale, not the MQ total. This looks like a wording error. 3) Age SD is 18.1 in the text and 18.06 in Table 2 (rounding). 4) The Table 2 footnote reads 'p > 0.05', which is probably meant to be p < 0.05. 5) The checks agree: the age-band counts in the misophonia group add to 126 (7+19+23+16+24+25+12), and the band denominators add to 2,519. The female count 72/126 matches the printed 57.1%. 6) The ASMR percentage for the misophonia group is 50.4% in Table 2 and 50.0% in the Results text (not an ou…
Заметка ИИ: There is one sample: a German nationwide survey using random route sampling with Kish-grid selection of one person per household, and paper self-report completed during a home visit. The primary estimate is MQ Severity >7: 126/2,519 (5.0%). Other whole-sample definitions are AMISOS-R >23, MQ Symptom Scale >14 and both cut-offs combined. Subgroup estimates by sex and age band (from Table 2) use only the primary MQ definition. No survey weights were used. The report does not cite a published validation of the German MQ or AMISOS-R; it only describes their translation. The study also used a Germ…

### ST069-1 · German general population household survey (USUMA/Leipzig), DEU, n=2519
Отчёты: R0922 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ Severity Scale >7 (described also as 'cut-off of 7') | **L2** | **126 / 2519** | 5.0 | Results, Prevalence estimate of clinical misophonia symptoms | «In our sample, 126 individuals, which corresponds to 5.0% of the total sample, had a MQ Severity of >7 and were considered as suffering from clinical misophonia symptoms.» |
| E2 | all | AMISOS-R · AMISOS-R >23 | **L2** | **148 / 2519** | 5.9 | Results, Prevalence estimate; Methods, Determining individu… | «The secondary cut-off criterion of an AMISOS-R rating of >23 was met for 148 individuals, which corresponded to 5.9% of the total sample.» |
| E3 | all | MQ · MQ Symptom Scale >14 | **L1** | **81 / 2519** | 3.2 | Results, Prevalence estimate of clinical misophonia symptoms | «As far as trigger sensitivity was concerned, 81 participants (3.2%) had an MQ Symptom scale score of >14.» |
| E4 | all | multiple · MQ Severity Scale >7 AND AMISOS-R >23 | **L2** | **55 / 2519** | 2.2 | Results, Prevalence estimate of clinical misophonia symptoms | «The agreement via kappa was at 0.37, which is considered fair (20). Fifty-five individuals (2.2%) fulfilled both cut-off criterions.» |
| E5 | female | MQ · MQ Severity Scale >7 | **L2** | **72 / 1322** | 5.4 | Table 2 | «Gender, female, n, % / 1,322 / 52.5% / 1,250 / 52.2% / 72 / 57.1%» |
| E6 | male | MQ · MQ Severity Scale >7 | **L2** | **54 / 1197** | 4.5 | Table 2; Results, Sample characteristics; Prevalence estima… | «126 individuals... had a MQ Severity of >7; Gender, female ... / 72 / 57.1%; 1,197 (47.5%) were male» |
| E7 | 16-24 | MQ · MQ Severity Scale >7 | **L2** | **7 / 229** | 3.1 | Table 2 | «16–24 / 229 / 9.1% / 222 / 9.3% / 7 / 5.6%» |
| E8 | 25-34 | MQ · MQ Severity Scale >7 | **L2** | **19 / 364** | 5.2 | Table 2 | «25–34 / 364 / 14.5% / 345 / 14.4% / 19 / 15.1%» |
| E9 | 35-44 | MQ · MQ Severity Scale >7 | **L2** | **23 / 399** | 5.8 | Table 2 | «35–44 / 399 / 15.8% / 376 / 15.7% / 23 / 18.3%» |
| E10 | 45-54 | MQ · MQ Severity Scale >7 | **L2** | **16 / 411** | 3.9 | Table 2 | «45–54 / 411 / 16.3% / 395 / 16.5% / 16 / 12.7%» |
| E11 | 55-64 | MQ · MQ Severity Scale >7 | **L2** | **24 / 488** | 4.9 | Table 2 | «55–64 / 488 / 19.4% / 464 / 19.4% / 24 / 19.0%» |
| E12 | 65-74 | MQ · MQ Severity Scale >7 | **L2** | **25 / 390** | 6.4 | Table 2 | «65–74 / 390 / 15.5% / 365 / 15.3% / 25 / 19.8%» |
| E13 | >=75 | MQ · MQ Severity Scale >7 | **L2** | **12 / 238** | 5.0 | Table 2 | «>75 / 238 / 9.4% / 226 / 9.4% / 12 / 9.5%» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 L2 (if >7 means >=8, still L2 by G2); у авторов: «clinical misophonia symptoms / clinically significant misophonia symptoms»; главная у авторов: yes; период: NR; заметка: The threshold is printed as '>7' throughout, but the Statistical analysis section says 'cut-off of 7' and cites Wu et al. (>=7). The exact operator is unclear.
- E2: источник порога: study's own; правило: AMISOS-R row; >=24 equals '>23' (L2). Cut-off from an external sample (Jager et al.), so not E3 (G5); G3 applies; у авторов: «secondary cut-off criterion for clinical misophonia symptoms»; главная у авторов: no; период: NR; заметка: The authors computed the cut-off as the mean minus 1 SD (29.78 - 6.46) of Jager et al.'s 575 patients.
- E3: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 L1; у авторов: «trigger sensitivity ('sometimes' sensitive to certain sounds on average)»; главная у авторов: no; период: NR; заметка: The authors use this as a screening definition. JBI 6 would be 'no' for it.
- E4: источник порога: study's own; правило: G4 'A and B' -> higher level; both L2; у авторов: «fulfilled both cut-off criterions»; главная у авторов: no; период: NR; заметка: Agreement between the two definitions kappa = 0.37.
- E5: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR; заметка: 72 = females in the misophonia group; 1,322 = all females (1,250 + 72).
- E6: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR; **расчёт: Cases: 126 - 72 females = 54. n: 1,197 males, from the text.**
- E7: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR; заметка: This band includes adolescents aged 16-17.
- E8: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR
- E9: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR
- E10: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR
- E11: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR
- E12: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR
- E13: источник порога: developer paper; правило: MQ row; MSS >=7 L2; у авторов: «clinical misophonia symptoms»; главная у авторов: no; период: NR; заметка: The band is printed as '>75'. It probably means 75 and over, since the previous band is 65–74.

**Ключевые поля выборки:**
- **n_analysed: 2519** — Results, Sampling and assessment procedure — «resulting in a total of 2,519 complete assessments (Figure 1)»
- **population: gp_probability** — Methods, Data sampling and procedure — «Those areas were subjected to a random allocation procedure. In the second step, for each sampling area, 23 households were selected along a random route»
- **sampling: probability** — Methods, Data sampling and procedure — «The randomized sampling procedure was carried out in three steps... 23 households were selected along a random route... one target member was selected from each household via the Kish grid method»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: DEU — Methods, Data sampling and procedure — «in the first step, Germany was divided into 53,000 areas containing from 350 to 700 households»
- setting: community (nationwide household survey, in-person home visits) — Methods, Procedure of the assessment — «All information and assessments were administered during one in-person visit by an experienced staff member at the subject's home.»
- data_years: 2020-2021 — Methods, Data sampling and procedure — «Data were collected between December 2020 and March 2021.»
- design: cross-sectional — Abstract, Methods — «We conducted a large-scale representative population survey between December 2020 and March 2021.»
- topic_disclosed: NR — Methods, Procedure of the assessment — «all selected individuals were informed about the purpose of the study»
- inclusion_exclusion: Household members aged >=16 able to read and understand German; 37 invalid assessments excluded — Methods, Data sampling and procedure; Results, Sampling — «The individual needed to be at least age 16 and able to read and understand German language.»
- n_invited: 5934 — Results, Sampling and assessment procedure — «A total of 5,934 selected households were selected, out of which, 21 were not inhabited, 1,154 were not available for an assessment or sick, and 2,203 were unw…»
- n_responded: 2556 — Results, Sampling and assessment procedure — «A total of 2,556 assessments were made, out of which 37 were not valid»
- response_rate: 43.1 — Results, Sampling and assessment procedure (computed) — «A total of 5,934 selected households were selected... A total of 2,556 assessments were made»
- age_mean: 50.3 — Results, Sample characteristics — «The average age was 50.3 years (SD: 18.1; range: 16–96 years).»
- age_sd: 18.1 — Results, Sample characteristics — «The average age was 50.3 years (SD: 18.1; range: 16–96 years).»
- age_min: 16 — Results, Sample characteristics — «range: 16–96 years»
- age_max: 96 — Results, Sample characteristics — «range: 16–96 years»
- age_group: mixed — Results, Sample characteristics — «range: 16–96 years»
- pct_female: 52.5 — Results, Sample characteristics — «Out of the total of 2,519 participants, 1,322 (52.5%) were female and 1,197 (47.5%) were male.»
- informant: self — Methods, Procedure of the assessment — «a battery of paper and pencil self-assessment questionnaires»
- mode: paper — Methods, Procedure of the assessment — «The assessment included an inquiry of sociodemographic data and a battery of paper and pencil self-assessment questionnaires.»
- instruments: Misophonia Questionnaire (MQ; Symptom, Emotions and Behaviors, Severity scales), German translation; Amsterdam Misophonia Scale-Revised (AMISOS-R), German translation — Methods, Assessment instruments — «Both questionnaires were back to back translated into German by bilingual and professional translators and approved by the original authors (15, 16).»
- instrument_validated_in_language: NR — Methods, Assessment instruments — «Both questionnaires were back to back translated into German by bilingual and professional translators and approved by the original authors (15, 16).»
- pub_status: journal — Header — «Frontiers in psychiatry; DOI: 10.3389/fpsyt.2022.1012424»
- language: English — Full text — «Prevalence and clinical correlates of misophonia symptoms in the general population of Germany»
- funding_coi: Funding source not reported; authors declare no conflict of interest — Conflict of interest — «The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict…»
- notes: The sample includes 16-17-year-olds (age range 16-96). The MQ Severity threshold is printed as '>7' but also described as a 'cut-off of 7' (Wu et al., >=7). The level is L2 under either reading. The AMISOS-R >23 cut-off was set by the authors from Jager et al.'s patient sample (mean - 1 SD). No survey weights were used. The report cites no German validation of the MQ or AMISOS-R, only a translation approved by the original authors. The authors made the data public (doi 10.17632/zjrt56tcnx.1). Check for overlap with other reports by the Hamburg/Leipzig groups (e.g., Moellmann et al. 2023).

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Nationwide area frame covering German private households; target is the general population of Germany aged >=16 (German-speaking). — Methods, Data sampling and procedure — «Germany was divided into 53,000 areas containing from 350 to 700 households. Those areas were subjected to a random allocation procedure.»
2. способ отбора: **yes** — Random area selection, random-route households, then Kish grid within the household. Random route is quasi-probability; reviewer to confirm. — Methods, Data sampling and procedure — «one target member was selected from each household via the Kish grid method (12) – a procedure that allows each family member to be randomly selected with the …»
3. размер выборки: **yes** — n = 2,519 >= 385. — Results, Sampling and assessment procedure — «resulting in a total of 2,519 complete assessments»
4. описание выборки и условий: **yes** — Age, sex, setting (household survey), country and dates reported. — Results, Sample characteristics; Methods — «1,322 (52.5%) were female... The average age was 50.3 years (SD: 18.1; range: 16–96 years).»
5. охват (пропуски): **yes** — Only 37 of 2,556 assessments (1.4%) invalid; analysis on complete assessments. — Results, Sampling and assessment procedure — «A total of 2,556 assessments were made, out of which 37 were not valid, resulting in a total of 2,519 complete assessments»
6. валидность определения случая: **unclear** — The primary MQ Severity cut-off is L2, but the report cites no published validation of the German MQ (translation only). The threshold is printed as '>7' yet described as a 'cut-off of 7'. — Methods, Determining individuals with clinical misophonia s… — «we used a cut-off score of >7 on the MQ Severity Scale to diagnose clinically significant misophonia symptoms»
7. единое надёжное измерение: **yes** — Same paper self-report instruments and thresholds for all; Cronbach's alpha reported in sample. — Results, Sampling and assessment procedure — «Cronbach's alpha was 0.90 for MQ total and 0.89 for AMISOS-R.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are clear (126/2,519) and a CI can be calculated. No survey weights were applied, although Kish selection gives unequal selection probabilities by household size (reviewer to check). — Results, Prevalence estimate — «In our sample, 126 individuals, which corresponds to 5.0% of the total sample, had a MQ Severity of >7»
9. отклик: **no** — Response was about 43% (2,556/5,934). There was no comparison with non-responders and no non-response weighting; the only check is sample vs census (Table 1). — Results, Sampling and assessment procedure; Table 1 — «1,154 were not available for an assessment or sick, and 2,203 were unwilling to participate. A total of 2,556 assessments were made»

Правки:
- 

Проверено: да
---

## ST070 · Kenar 2022 · Turkish Journal Of Neurology

Основной отчёт R0925: [текст](../../fulltext/text/R0925.txt) · [PDF](../../fulltext/pdf/R0925.pdf) — «The Effect of Misophonia on the Severity of Depression and Anxiety in Multiple Sclerosis» — [DOI](https://doi.org/10.4274/tnd.2022.93892)
Расхождения в тексте: (1) Controls: Table 2 header says n=63 but absent 50 + present 12 = 62. The printed percentages (80.6%, and 19.4% in the text) match n=62, and the Total column 87 (71.9) matches n=121. Denominator 62 used. (2) Table 1 sex counts appear swapped between columns: the MS column shows 44/19 (sum 63) and the control column 41/18 (sum 59). Table 3 gives MS female 13+28=41 and male 9+9=18 (=59), so MS 41/59=69.5% and controls 44/63=69.8%. (3) The power-analysis text says 119 participants were studied, but 59+63=122 (121 classified). (4) The design is called a 'prospective case-control study' in Methods and a 'cross-sectional study' in the Discussion. (5) Mean misophonia scores (A-MISO-S 11.1 in MS, 10.0 in controls) look like scores among positives only ('A-miso-S test in the presence of misophonia'). No A-MISO-S cut-off prevalence is reported.
Заметка ИИ: Main uncertainty: the level of the case definition. The Schröder 2013 criteria are listed in full, but the report does not say whether a clinician or interviewer applied them or whether participants judged themselves. L3 and JBI 6 = yes are tentative; if the criteria were self-applied, recode to adhoc, 'self-completed', L2. The A-MISO-S Turkish version was translated by the authors and has no validation.

### ST070-1 · MS outpatients, Ankara City Hospital, Turkey, n=59
Отчёты: R0925 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | interview · interview: Schröder 2013 criteria | **L3** | **22 / 59** | 37.3 | Page 3, Table 2; Results | «MS (n=59) ... Misophonia Absent 37 (62.7) Present 22; the frequency of misophonia was significantly higher in the MS group (37.3%)» |
| E2 | female | interview · interview: Schröder 2013 criteria | **L3** | **13 / 41** | 31.7 | Page 3, Table 3 | «Female 13 (59.1%) 28 (75.7%)» |
| E3 | male | interview · interview: Schröder 2013 criteria | **L3** | **9 / 18** | 50.0 | Page 3, Table 3 | «Male 9 (40.9%) 9(24.3%)» |
| E4 | RRMS | interview · interview: Schröder 2013 criteria | **L3** | **19 / 52** | 36.5 | Page 3, Table 3 | «RRMS ... 19 (86.4%) ... 33 (89.2%)» |
| E5 | SPMS | interview · interview: Schröder 2013 criteria | **L3** | **2 / 4** | 50.0 | Page 3, Table 3 | «SPMS ... 2 (9.1%) ... 2 (5.4%)» |
| E6 | PPMS | interview · interview: Schröder 2013 criteria | **L3** | **0 / 2** | 0.0 | Page 3, Table 3 | «PPMS ... - ... 2 (5.4%)» |
| E7 | PRMS | interview · interview: Schröder 2013 criteria | **L3** | **1 / 1** | 100.0 | Page 3, Table 3 | «PRMS ... 1 (4.5%) ... -» |

- E1: источник порога: developer paper; правило: interview row; explicit cited criteria (Schröder 2013) -> L3 (tentative, application method unclear); у авторов: «misophonia positive / frequency of misophonia»; главная у авторов: yes; период: current; заметка: Who applied the criteria and in what format is not stated
- E2: источник порога: developer paper; правило: interview row; explicit cited criteria -> L3 (tentative); у авторов: «MSwM»; главная у авторов: no; период: current; **расчёт: n = 13 (MSwM) + 28 (MSwoM) females from Table 3**
- E3: источник порога: developer paper; правило: interview row; explicit cited criteria -> L3 (tentative); у авторов: «MSwM»; главная у авторов: no; период: current; **расчёт: n = 9 (MSwM) + 9 (MSwoM) males from Table 3**
- E4: источник порога: developer paper; правило: interview row; explicit cited criteria -> L3 (tentative); у авторов: «MSwM»; главная у авторов: no; период: current; **расчёт: n = 19 (MSwM) + 33 (MSwoM) RRMS from Table 3**
- E5: источник порога: developer paper; правило: interview row; explicit cited criteria -> L3 (tentative); у авторов: «MSwM»; главная у авторов: no; период: current; **расчёт: n = 2 (MSwM) + 2 (MSwoM) SPMS from Table 3**
- E6: источник порога: developer paper; правило: interview row; explicit cited criteria -> L3 (tentative); у авторов: «MSwM»; главная у авторов: no; период: current; **расчёт: MSwM '-' (0) + MSwoM 2 PPMS from Table 3**
- E7: источник порога: developer paper; правило: interview row; explicit cited criteria -> L3 (tentative); у авторов: «MSwM»; главная у авторов: no; период: current; **расчёт: MSwM 1 + MSwoM '-' (0) PRMS from Table 3**

**Ключевые поля выборки:**
- **n_analysed: 59** — Page 3, Table 2 — «MS (n=59) ... Absent 37 (62.7) ... Present 22»
- **population: clinical** — Page 2, Study Population — «All patients met the 2017 McDonald criteria.»
- **sampling: convenience** — Page 2, Study Design and Procedures — «MS patients who presented to MS outpatient clinic and volunteered to answer the questionnaires were included in the study.»

**Остальные поля:**
- clinical_group: other: multiple sclerosis — Page 2, Study Population — «All patients met the 2017 McDonald criteria.»
- country: TUR — Page 1, affiliation — «Ankara City Hospital, Clinic of Neurology, Ankara, Turkey»
- setting: clinic (MS outpatient clinic, neurology, Ankara City Hospital) — Page 2, Study Design and Procedures — «Fifty-nine MS patients who presented to MS outpatient clinic and volunteered to answer the questionnaires were included in the study.»
- data_years: NR — Page 1 — «Re­cei­ved/Ge­liﬂ Ta­ri­hi: 29.09.2021»
- design: cross-sectional — Page 2, Study Design; Page 4, Discussion — «This study was a prospective case-control study. ... In this cross-sectional study, misophonia (37.3%) was more common in patients with MS»
- topic_disclosed: yes — Page 2, Study Design and Procedures — «After the patients were informed about misophonia, those with misophonic complaints that met Schröder's et al. (9) diagnostic criteria were considered as misop…»
- inclusion_exclusion: MS by 2017 McDonald criteria, presenting to MS outpatient clinic, volunteered; excluded severe cognitive impairment and aphasia; none had hearing loss or tinnitus complaints — Page 2, Study Population — «All patients met the 2017 McDonald criteria. Patients with severe cognitive impairment and aphasia were not included to the study. None of the patients had hea…»
- n_invited: NR — NA
- n_responded: 59 — Page 2, Study Design and Procedures — «Fifty-nine MS patients who presented to MS outpatient clinic and volunteered to answer the questionnaires were included in the study.»
- response_rate: NR — NA
- age_mean: 32.4 — Page 3, Table 1 — «Age (year) 32.4±9.8»
- age_sd: 9.8 — Page 3, Table 1 — «Age (year) 32.4±9.8»
- age_min: NR — NA
- age_max: NR — NA
- age_group: NR — Page 3, Table 1 — «Age (year) 32.4±9.8»
- pct_female: 69.5 — Page 3, Table 1; Table 3 — «Female 44 (69.5); Table 3: Female 13 (59.1%) 28 (75.7%)»
- informant: mixed — Page 2, Study Design and Procedures — «After the patients were informed about misophonia, those with misophonic complaints that met Schröder's et al. (9) diagnostic criteria were considered as misop…»
- mode: NR — Page 2 — «volunteered to answer the questionnaires»
- instruments: Schröder et al. 2013 diagnostic criteria (applied in Turkish; assessor and format not described); A-MISO-S, Turkish translation by the authors (not validated) — Page 2, Study Design and Procedures — «The scale was translated into Turkish by the authors but was not validated in the Turkish language.»
- instrument_validated_in_language: NR — Page 2; Page 6, limitations — «the A-miso-S scale was used to investigate the severity of misophonia; since it was not validated in the Turkish population»
- pub_status: journal — Page 1, header — «Turk J Neurol 2022;28:24-30»
- language: English (abstract also in Turkish) — Page 1 — «The Effect of Misophonia on the Severity of Depression and Anxiety in Multiple Sclerosis»
- funding_coi: No financial support; no conflict of interest declared — Page 6, Ethics — «Conflict of Interest: No conflict of interest was declared by the authors. Financial Disclosure: The authors declared that this study received no financial sup…»
- notes: Case definition: Schröder 2013 criteria, listed in full. The report does not say who applied them or whether a formal interview was used. L3 is tentative; reviewer should check (L2 if self-judged). A-MISO-S seems to have been given only to misophonia-positive people (mean 11.1±4); no A-MISO-S cut-off prevalence is reported. Table 1 sex counts for MS (44/19) sum to 63 and look swapped with the control column. Table 3 gives 41 female/18 male = 59, so pct_female = 41/59 = 69.5%. Age range not reported. Data years NR (ethics protocol E1-20-1315; received 09/2021). Table 6 gives misophonia by BDI/…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is patients attending one MS outpatient clinic, while the claims are about the MS population — Page 2; Page 6, Conclusion — «Misophonia is frequent in the MS population»
2. способ отбора: **no** — Volunteers among clinic attendees (convenience) — Page 2, Study Design and Procedures — «MS patients who presented to MS outpatient clinic and volunteered to answer the questionnaires were included in the study.»
3. размер выборки: **no** — n=59, below 139 for a clinical sample — Page 3, Table 2 — «MS (n=59)»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection missing — Page 3, Table 1; Page 2 — «Age (year) 32.4±9.8»
5. охват (пропуски): **yes** — All 59 patients classified for misophonia — Page 3, Table 2 — «Absent ... 37 (62.7) ... Present ... 22»
6. валидность определения случая: **yes** — Explicit Schröder 2013 criteria listed; tentatively yes as L3, but who applied them and how is not reported (flag) — Page 2, Study Design and Procedures — «those with misophonic complaints that met Schröder's et al. (9) diagnostic criteria were considered as misophonia positive.»
7. единое надёжное измерение: **unclear** — Same criteria for everyone, but no inter-rater reliability and no description of how they were applied — Page 2 — «After the patients were informed about misophonia, those with misophonic complaints that met Schröder's et al. (9) diagnostic criteria were considered as misop…»
8. статистика (числитель и знаменатель): **yes** — 22/59 = 37.3% traceable; CI calculable — Page 3, Table 2 — «MS (n=59) ... Present 22; frequency of misophonia was significantly higher in the MS group (37.3%)»
9. отклик: **unclear** — Number of patients approached not reported — Page 2 — «volunteered to answer the questionnaires»

Правки:
- 

Проверено: да
### ST070-2 · Healthy controls, Ankara (Turkey), n=63 (62 classified)
Отчёты: R0925 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | interview · interview: Schröder 2013 criteria | **L3** | **12 / 62** | 19.4 | Page 3, Table 2; Results | «Control (n=63) ... Absent 50 (80.6) ... Present 12; compared to controls (19.4%)» |

- E1: источник порога: developer paper; правило: interview row; explicit cited criteria -> L3 (tentative, application method unclear); у авторов: «misophonia present»; главная у авторов: yes; период: current; заметка: Table header n=63 but 50+12=62; 19.4% = 12/62. Denominator 62 used.

**Ключевые поля выборки:**
- **n_analysed: 62** — Page 3, Table 2 — «Control (n=63) ... Absent 50 (80.6) ... Present 12»
- **population: other_nonclinical** — Page 2, Study Population — «63 age- and sex-matched healthy individuals who had no diagnosed neurological disorder»
- **sampling: NR** — Page 2, Study Population — «Control group consisted of 63 age- and sex-matched healthy individuals who had no diagnosed neurological disorder.»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Page 2, Study Population — «Ankara City Hospital Institutional Review Board/Ethics Committee approved the study protocol»
- setting: NR (healthy controls; recruitment setting not described) — Page 2, Study Population — «Control group consisted of 63 age- and sex-matched healthy individuals who had no diagnosed neurological disorder.»
- data_years: NR — NA
- design: cross-sectional — Page 2, Study Design — «This study was a prospective case-control study.»
- topic_disclosed: NR — Page 2 — «BDI, BAI, and A-miso-S test in the presence of misophonia were performed on control group.»
- inclusion_exclusion: Healthy, age- and sex-matched to MS patients, no diagnosed neurological disorder — Page 2, Study Population — «Control group consisted of 63 age- and sex-matched healthy individuals who had no diagnosed neurological disorder.»
- n_invited: NR — NA
- n_responded: 63 — Page 2, Study Population; Table 1 — «Control n=63»
- response_rate: NR — NA
- age_mean: 33.3 — Page 3, Table 1 — «Age (year) 32.4±9.8 33.3±9.7»
- age_sd: 9.7 — Page 3, Table 1 — «Age (year) 32.4±9.8 33.3±9.7»
- age_min: NR — NA
- age_max: NR — NA
- age_group: NR — Page 3, Table 1 — «33.3±9.7»
- pct_female: 69.8 — Page 3, Table 1 — «Female ... 41 (69.8)»
- informant: mixed — Page 2 — «those with misophonic complaints that met Schröder's et al. (9) diagnostic criteria were considered as misophonia positive.»
- mode: NR — NA
- instruments: Schröder et al. 2013 diagnostic criteria (assessor/format not described); A-MISO-S, Turkish translation by the authors (not validated) — Page 2 — «BDI, BAI, and A-miso-S test in the presence of misophonia were performed on control group.»
- instrument_validated_in_language: NR — Page 2 — «The scale was translated into Turkish by the authors but was not validated in the Turkish language.»
- pub_status: journal — Page 1, header — «Turk J Neurol 2022;28:24-30»
- language: English (abstract also in Turkish) — Page 1 — «The Effect of Misophonia on the Severity of Depression and Anxiety in Multiple Sclerosis»
- funding_coi: No financial support; no conflict of interest declared — Page 6, Ethics — «The authors declared that this study received no financial support.»
- notes: Healthy matched controls, recruited separately from the MS patients; recruitment source not described. The procedure text describes the criteria for 'patients'; Table 2 implies the same case definition was used for controls. Table 2: 50 absent + 12 present = 62, not 63; 80.6% and 19.4% correspond to n=62 (one control not classified). Table 1 sex counts (41/18) sum to 59 and look swapped with the MS column; 69.8% = 44/63. L3 is tentative, as for the MS sample.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Frame for controls not described — Page 2, Study Population — «Control group consisted of 63 age- and sex-matched healthy individuals»
2. способ отбора: **unclear** — Sampling method for controls not described (matched, non-random) — Page 2, Study Population — «63 age- and sex-matched healthy individuals who had no diagnosed neurological disorder»
3. размер выборки: **no** — n=62/63, below 385 — Page 3, Table 2 — «Control (n=63)»
4. описание выборки и условий: **no** — Age and sex reported; setting and dates not reported (country only implied) — Page 3, Table 1 — «Age (year) ... 33.3±9.7»
5. охват (пропуски): **yes** — 62 of 63 classified (1.6% missing) — Page 3, Table 2 — «Absent 50 (80.6) ... Present 12»
6. валидность определения случая: **yes** — Explicit Schröder 2013 criteria; tentatively yes as L3, but how they were applied is not reported (flag) — Page 2 — «met Schröder's et al. (9) diagnostic criteria were considered as misophonia positive»
7. единое надёжное измерение: **unclear** — No reliability reported; procedure in controls not described — Page 2 — «BDI, BAI, and A-miso-S test in the presence of misophonia were performed on control group.»
8. статистика (числитель и знаменатель): **yes** — 12/62 = 19.4% traceable despite stated n=63; CI calculable — Page 3, Table 2; Results — «compared to controls (19.4%)»
9. отклик: **unclear** — Number approached not reported — Page 2 — «Control group consisted of 63 age- and sex-matched healthy individuals»

Правки:
- 

Проверено: да