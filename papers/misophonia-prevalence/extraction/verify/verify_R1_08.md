# Проверка выписывания — файл 8 из 10

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

## ST071 · Norris 2022 · Frontiers in neuroscience

Основной отчёт R0941: [текст](../../fulltext/text/R0941.txt) — «Toward a Multidimensional Understanding of Misophonia Using Cluster-Based Phenotyping.» — [DOI](https://doi.org/10.3389/fnins.2022.832516)
Приложен R0260: [текст](../../fulltext/text/R0260.txt) · [PDF](../../fulltext/pdf/R0260.pdf) — «A Tutorial on Supervised Machine Learning Variable Selection Methods in Classification for the Social and Health Scienc…»
Приложен R0488: [текст](../../fulltext/text/R0488.txt) · [PDF](../../fulltext/pdf/R0488.pdf) — «A Tutorial on Supervised Machine Learning Variable Selection Methods for the Social and Health Sciences in R»
Связь отчётов: University of Oklahoma 343 undergraduates (Norris et al. 2022); the two tutorials R0260 and R0488 reuse a listwise-deleted subset of this dataset and cite it
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R0082 (ST012): Both University of Oklahoma students with the MQ (777 vs 343); R0082 calls its data 'collected for other purposes' and does not say it reuses Norris et al. 2022
Расхождения в тексте: 1) 54/343 = 15.74%, but the text gives 15.6%. Cluster counts (22+31+1 = 54) and Table 6 (21 = 38.9% of 54; 92 = 31.8% of 289) support 54/343. 2) The text describes the MSS threshold as '7 out of 10', but the MQ Severity Scale ranges 1-15; the threshold of 7 matches Wu 2014. 3) Table 5 gives MQ severity ANOVA df = 2, 240 (about 243 with MSS), while the other MQ variables have df around 330. Missing MSS may have been counted as non-cases in the 343 denominator. 4) The Discussion says '~20%' of misophonia cases reported PTSD; Table 10 gives 11.1%. 5) The text says tinnitus co-occurrence 'χ2(1, 516)', an implausible N. 6) R0260 reports 16.5% diagnosed in a listwise-deleted subset (n not given), which differs from 15.6% in the main report. 7) Subgroup estimates by self-reported diagnosis are back-calculated from the within-group percentages in Table 10 and are approximate.
Заметка ИИ: Primary estimate: MQ MSS>=7 (L2), 54/343. JBI 6 = yes (English MQ, validated). Flags for the reviewer: possible overlap with R0082 (ST012), and a possible missing-MSS denominator issue.

### ST071-1 · University of Oklahoma undergraduates, USA, n=343
Отчёты: R0941 (main); R0260; R0488

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **54 / 343** | 15.7 | Results; Discussion | «Of 343 participants, 54 (15.6%) reported clinically relevant levels of misophonia symptoms indicated by self-reported scores of 7 or greater on the MQ Misophonia Severity Scale.» |
| E2 | tinnitus screener positive | MQ · MSS>=7 | **L2** | **40 / 173** | 23.1 | Results, Tinnitus | «A total of 50.4% (N = 173) of participants reported experiencing ringing in the ears or tinnitus ... Forty participants who qualified for misophonia reported experiencing tinnitus ... was 23.1%» |
| E3 | tinnitus screener negative | MQ · MSS>=7 | **L2** | **14 / 170** | 8.2 | Results; Results, Tinnitus | «A total of 50.4% (N = 173) of participants reported experiencing ringing in the ears ... Forty participants who qualified for misophonia reported experiencing tinnitus» |
| E4 | self-reported GAD | MQ · MSS>=7 | **L2** | **13 / 49** | 26.5 | Table 10 | «General anxiety disorder (GAD) / 12.4 / 24 / 4.77*» |
| E5 | self-reported OCD | MQ · MSS>=7 | **L2** | **6 / 10** | 60.0 | Table 10 | «Obsessive compulsive disorder (OCD) / 1.3 / 11.1 / 14.16***» |
| E6 | self-reported PTSD | MQ · MSS>=7 | **L2** | **6 / 12** | 50.0 | Table 10 | «Post-traumatic stress disorder (PTSD) / 2 / 11.1 / 10.36**» |
| E7 | self-reported panic disorder | MQ · MSS>=7 | **L2** | **1 / 3** | 33.3 | Table 10 | «Panic disorder / 0.6 / 1.8 / 0.78» |
| E8 | self-reported social anxiety disorder | MQ · MSS>=7 | **L2** | **0 / 9** | 0.0 | Table 10 | «Social anxiety disorder / 3.1 / 0 / 1.71» |
| E9 | self-reported any anxiety disorder | MQ · MSS>=7 | **L2** | **15 / 37** | 40.5 | Table 10 | «Anxiety disorders (total) / 7.6 / 27.7 / 17.81***» |
| E10 | self-reported depression | MQ · MSS>=7 | **L2** | **12 / 51** | 23.5 | Table 10 | «Depression / 13.4 / 22.2 / 2.67» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2, recommended); у авторов: «clinically relevant levels of misophonia symptoms»; главная у авторов: yes; период: NR; заметка: 54/343 = 15.74%, but reported as 15.6%. Consistent with cluster counts 22+31+1 = 54 and Table 6 (21 = 38.9% of 54). Denominator may include participants with missing MSS (see sample notes).
- E2: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «co-occurrence of misophonia and tinnitus»; главная у авторов: no; период: NR; заметка: Self-reported tinnitus/ear ringing via a screening question, which the authors say includes many false positives.
- E3: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «clinically relevant levels of misophonia symptoms»; главная у авторов: no; период: NR; **расчёт: cases 54 - 40 = 14; n 343 - 173 = 170**; заметка: Check: 133/289 (46%) of non-misophonia participants were screen-positive, matching the text.
- E4: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «misophonia group»; главная у авторов: no; период: NR; **расчёт: 24% x 54 = 12.96 -> 13; 12.4% x 289 = 35.8 -> 36; n = 13 + 36 = 49**; заметка: Approximate: group denominators of 54 and 289 assumed; missing diagnosis data unknown. Self-reported diagnoses.
- E5: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «misophonia group»; главная у авторов: no; период: NR; **расчёт: 11.1% x 54 = 5.99 -> 6; 1.3% x 289 = 3.76 -> 4; n = 6 + 4 = 10**; заметка: Approximate derivation (denominators of 54/289 assumed). Self-reported diagnosis.
- E6: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «misophonia group»; главная у авторов: no; период: NR; **расчёт: 11.1% x 54 = 5.99 -> 6; 2% x 289 = 5.78 -> 6; n = 12**; заметка: Approximate derivation. Self-reported diagnosis. The Discussion gives '~20%' PTSD among misophonia cases, which conflicts with Table 10 (11.1%).
- E7: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «misophonia group»; главная у авторов: no; период: NR; **расчёт: 1.8% x 54 = 0.97 -> 1; 0.6% x 289 = 1.73 -> 2; n = 3**; заметка: Approximate derivation; very small n. Self-reported diagnosis.
- E8: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «misophonia group»; главная у авторов: no; период: NR; **расчёт: 0% x 54 = 0; 3.1% x 289 = 8.96 -> 9; n = 9**; заметка: Approximate derivation. Self-reported diagnosis.
- E9: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «misophonia group»; главная у авторов: no; период: NR; **расчёт: 27.7% x 54 = 14.96 -> 15; 7.6% x 289 = 21.96 -> 22; n = 37**; заметка: Approximate. The 'total' row (combining GAD, OCD and PTSD per the text) is smaller than the sum of its components; its construction is unclear.
- E10: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «misophonia group»; главная у авторов: no; период: NR; **расчёт: 22.2% x 54 = 11.99 -> 12; 13.4% x 289 = 38.7 -> 39; n = 51**; заметка: Approximate derivation. Self-reported diagnosis.

**Ключевые поля выборки:**
- **n_analysed: 343** — Results — «Of 343 participants, 54 (15.6%) reported clinically relevant levels of misophonia symptoms»
- **population: university_students** — Abstract — «in a non-clinical sample of young adult undergraduate students (N = 343)»
- **sampling: convenience** — Materials and Methods, Participants — «recruited using a secure online research participation system through the university's undergraduate psychology research participation pool ... Those who completed the survey received 1 h worth of class credit.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — Materials and Methods, Participants — «Participants were undergraduate students (N = 343) at the University of Oklahoma (OU) in Norman, Oklahoma.»
- setting: university (undergraduate psychology research participation pool) — Materials and Methods, Participants — «Participants were recruited using a secure online research participation system through the university's undergraduate psychology research participation pool»
- data_years: NR — NA — «NR»
- design: cross-sectional — Materials and Methods, Measures — «The final survey was designed to address an array of symptoms characteristic of or that may overlap with misophonia, referred to as the Spectrum Characteristic…»
- topic_disclosed: NR — Materials and Methods — «The SCS was comprised of a demographics section and six clinical measures designed to address various aspects of misophonia»
- inclusion_exclusion: Undergraduates in the OU psychology participant pool; no other criteria reported — Materials and Methods, Participants — «Participants were undergraduate students (N = 343) at the University of Oklahoma (OU)»
- n_invited: NR — NA — «NR»
- n_responded: 343 — Materials and Methods, Participants — «Participants were undergraduate students (N = 343)»
- response_rate: NR — NA — «NR»
- age_mean: 18.96 — Participants; Table 1 — «ranged from ages 18 to 36 (M = 18.96, SD = 1.7)»
- age_sd: 1.7 — Participants; Table 1 — «ranged from ages 18 to 36 (M = 18.96, SD = 1.7)»
- age_min: 18 — Participants — «ranged from ages 18 to 36»
- age_max: 36 — Participants — «ranged from ages 18 to 36»
- age_group: adults — Participants — «ranged from ages 18 to 36»
- pct_female: 69.7 — Table 1 — «Female | 239 Female (69.7%)»
- informant: self — Results — «indicated by self-reported scores of 7 or greater on the MQ Misophonia Severity Scale»
- mode: online — Participants — «all data were collected anonymously via Qualtrics»
- instruments: Misophonia Questionnaire (MQ, Wu et al. 2014), English; S-Five 2018 preprint version (Vitoratou 2018), English, not the validated version — Measures — «The version used in the current study was the 2018 version of the S-Five ... but was not the validated version available after completion of data collection»
- instrument_validated_in_language: yes — Measures, Misophonia Questionnaire — «The Misophonia Questionnaire (MQ) is a validated, three-part, 20-item self-report measure designed to index misophonia symptoms (Wu et al., 2014).»
- pub_status: journal — Header — «Frontiers in neuroscience; DOI: 10.3389/fnins.2022.832516»
- language: English — Full text — «Toward a Multidimensional Understanding of Misophonia Using Cluster-Based Phenotyping»
- funding_coi: Funding NR in main report (R0488 says no funding for the tutorial); COI: none declared — Conflict of Interest; R0488, Declarations — «The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict…»
- notes: Possible overlap with R0082 (ST012): both University of Oklahoma students with the MQ (777 vs 343); R0082 calls its data 'collected for other purposes' and does not say it reuses Norris et al. 2022. R0260/R0488 reanalyse a listwise-deleted subset of this dataset (binary 'MQDX'). R0260 gives 16.5% diagnosed, n not reported; R0488's training-set confusion matrix shows 24 of 148. Not extracted separately to avoid double counting. K-means clusters are not case definitions and are not extracted. The MQ Severity ANOVA df (2, 240) suggests only ~243 had an MSS score; the denominator of 343 may count…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is the psychology research participant pool, only part of the university's undergraduates or 'college students'. — Participants — «through the university's undergraduate psychology research participation pool»
2. способ отбора: **no** — Volunteer opt-in for course credit; no probability sampling. — Participants — «Those who completed the survey received 1 h worth of class credit.»
3. размер выборки: **no** — n = 343 < 385. — Participants — «Participants were undergraduate students (N = 343)»
4. описание выборки и условий: **unclear** — Age, sex, setting, and country reported; dates of data collection not reported. — Participants; Table 1 — «Participants were predominately female [69.7% ...] and ranged from ages 18 to 36 (M = 18.96, SD = 1.7)»
5. охват (пропуски): **unclear** — Missing data not reported. The MQ Severity ANOVA df (2, 240) suggests missing MSS for ~100 participants, but all 343 are used as the denominator; R0260 used listwise deletion. — Table 5; R0260, p.110 — «MQ severity | 48.12*** | 2, 240»
6. валидность определения случая: **yes** — MQ Severity Scale >=7 in the English version, validated by Wu et al. 2014. — Measures, Misophonia Questionnaire — «MQ severity was utilized to split participants into groups reflecting clinically or non-clinically relevant levels of misophonia symptoms based on threshold sc…»
7. единое надёжное измерение: **yes** — Same online self-report MQ for everyone; reliability cited from the source (Wu 2014). — Measures, Misophonia Questionnaire — «Wu et al. (2014) reported high internal consistencies for total scores (α = 0.89)»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given (54/343); CI calculable. Minor discrepancy: 54/343 = 15.7%, reported as 15.6%. — Results — «Of 343 participants, 54 (15.6%) reported clinically relevant levels of misophonia symptoms»
9. отклик: **no** — Opt-in participant pool; number invited not known, response rate not reported, no handling of non-response. — Participants — «recruited using a secure online research participation system through the university's undergraduate psychology research participation pool»

Правки:
- 

Проверено: да
---

## ST072 · Paunovic 2022 · Noise & health

Основной отчёт R0947: [текст](../../fulltext/text/R0947.txt) — «The proposed criteria for high perceived misophonia in young healthy adults and the association between Misophonia symptoms and noise sensitivity.» — [DOI](https://doi.org/10.4103/nah.nah_40_20)
Расхождения в тексте: 1) Table 4, criterion 6 by sex: the table prints men 162 (39.6) and women 313 (43.3), with p = 0.228. These are the symptom 1 figures from Table 2. They do not add up to the printed total of 575 (50.8%). The total of 575 is confirmed three ways: by the band sum (187+140+146+71+31), by 1132 - 557 with no symptoms, and by the 51% in the Discussion. The sex-specific criterion 6 counts were therefore derived from the bands: men 207, women 368. 2) Table 1 percentages: the table prints 409 (35.3) and 723 (63.7), which sum to 99.0. The correct values are 36.1% and 63.9%, so pct_female = 723/1132 = 63.9. 3) Criteria 1-4 are exact (non-cumulative) symptom-count bands and are not extracted as estimates (G1). Criterion 5 (all five) is the top band and is therefore cumulative. 4) Single-symptom prevalences (Table 2: e.g., symptom 1 475/1132, symptom 5 187/1132) were not extracted as case definition…
Заметка ИИ: Country is inferred as Serbia (SRB) from the funding statement. The 5 items are a yes/no adaptation of A-MISO-S content, not the scored A-MISO-S, so instrument = adhoc and JBI 6 = no. Criterion 5 (all five symptoms) was coded L2 because it requires both the reaction and social impairment. The authors' primary criterion 9 (at least 4) is L1.

### ST072-1 · Medical students, Faculty of Medicine, Serbia (inferred), 2013, n=1132
Отчёты: R0947 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · at least 4 of 5 yes/no symptoms (criterion 9) | **L1** | **102 / 1132** | 9.0 | Table 4; Discussion | «Criterion 9 / At least four or more symptoms reported / 40 (9.8) / 62 (8.6) / 102 (9.0)» |
| E2 | all | adhoc · at least 1 of 5 yes/no symptoms (criterion 6) | **L1** | **575 / 1132** | 50.8 | Table 4; Results | «Criterion 6 / At least one or more symptoms reported / 162 (39.6) / 313 (43.3) / 575 (50.8)» |
| E3 | all | adhoc · at least 2 of 5 yes/no symptoms (criterion 7) | **L1** | **388 / 1132** | 34.3 | Table 4 | «Criterion 7 / At least two or more symptoms reported / 140 (34.2) / 248 (34.3) / 388 (34.3)» |
| E4 | all | adhoc · at least 3 of 5 yes/no symptoms (criterion 8) | **L1** | **248 / 1132** | 21.9 | Table 4 | «Criterion 8 / At least three or more symptoms reported / 92 (22.5) / 156 (21.6) / 248 (21.9)» |
| E5 | all | adhoc · all 5 of 5 yes/no symptoms (criterion 5), including aversive reaction (symptom 1) and impaired social functioning (symptom 5) | **L2** | **31 / 1132** | 2.7 | Table 4 | «Criterion 5 / All five misophonia symptoms reported / 12 (2.9) / 19 (2.6) / 31 (2.7)» |
| E6 | female | adhoc · at least 4 of 5 yes/no symptoms (criterion 9) | **L1** | **62 / 723** | 8.6 | Table 4 | «Criterion 9 / At least four or more symptoms reported / 40 (9.8) / 62 (8.6) / 102 (9.0)» |
| E7 | male | adhoc · at least 4 of 5 yes/no symptoms (criterion 9) | **L1** | **40 / 409** | 9.8 | Table 4 | «Criterion 9 / At least four or more symptoms reported / 40 (9.8) / 62 (8.6) / 102 (9.0)» |
| E8 | female | adhoc · at least 1 of 5 yes/no symptoms (criterion 6) | **L1** | **368 / 723** | 50.9 | Table 4 | «Criterion 1 ... 120 (16.6); Criterion 2 ... 92 (12.7); Criterion 3 ... 94 (13.0); Criterion 4 ... 43 (5.9); Criterion 5 ... 19 (2.6)» |
| E9 | male | adhoc · at least 1 of 5 yes/no symptoms (criterion 6) | **L1** | **207 / 409** | 50.6 | Table 4 | «Criterion 1 ... 67 (16.4); Criterion 2 ... 48 (11.7); Criterion 3 ... 52 (12.7); Criterion 4 ... 28 (6.8); Criterion 5 ... 12 (2.9)» |
| E10 | female | adhoc · at least 2 of 5 yes/no symptoms (criterion 7) | **L1** | **248 / 723** | 34.3 | Table 4 | «Criterion 7 / At least two or more symptoms reported / 140 (34.2) / 248 (34.3) / 388 (34.3)» |
| E11 | male | adhoc · at least 2 of 5 yes/no symptoms (criterion 7) | **L1** | **140 / 409** | 34.2 | Table 4 | «Criterion 7 / At least two or more symptoms reported / 140 (34.2) / 248 (34.3) / 388 (34.3)» |
| E12 | female | adhoc · at least 3 of 5 yes/no symptoms (criterion 8) | **L1** | **156 / 723** | 21.6 | Table 4 | «Criterion 8 / At least three or more symptoms reported / 92 (22.5) / 156 (21.6) / 248 (21.9)» |
| E13 | male | adhoc · at least 3 of 5 yes/no symptoms (criterion 8) | **L1** | **92 / 409** | 22.5 | Table 4 | «Criterion 8 / At least three or more symptoms reported / 92 (22.5) / 156 (21.6) / 248 (21.9)» |
| E14 | female | adhoc · all 5 of 5 yes/no symptoms (criterion 5) | **L2** | **19 / 723** | 2.6 | Table 4 | «Criterion 5 / All five misophonia symptoms reported / 12 (2.9) / 19 (2.6) / 31 (2.7)» |
| E15 | male | adhoc · all 5 of 5 yes/no symptoms (criterion 5) | **L2** | **12 / 409** | 2.9 | Table 4 | «Criterion 5 / All five misophonia symptoms reported / 12 (2.9) / 19 (2.6) / 31 (2.7)» |

- E1: источник порога: study's own; правило: adhoc row; symptom count on ad hoc item set (L1); G3; у авторов: «high perceived misophonia (criterion 9; proposed)»; главная у авторов: yes; период: NR; заметка: The authors propose criterion 9 as the decisive measure. It does not require symptom 5 (impairment), so L1, not L2.
- E2: источник порога: study's own; правило: adhoc row; symptom count on ad hoc item set (L1); G3; у авторов: «high perceived misophonia (criterion 6)»; главная у авторов: no; период: NR; заметка: Matches 1132 - 557 with no symptoms = 575, and the sum of criteria 1-5. A single symptom (e.g., irritation at specific sounds) is enough, so L0 is arguable; coded L1 as a symptom count.
- E3: источник порога: study's own; правило: adhoc row; symptom count on ad hoc item set (L1); G3; у авторов: «high perceived misophonia (criterion 7)»; главная у авторов: no; период: NR
- E4: источник порога: study's own; правило: adhoc row; symptom count on ad hoc item set (L1); G3; у авторов: «high perceived misophonia (criterion 8)»; главная у авторов: no; период: NR
- E5: источник порога: study's own; правило: adhoc row; L2: item set requires misophonic reaction and impairment; G1 (top band = cumulative >=5); у авторов: «high perceived misophonia (criterion 5; 'most strict')»; главная у авторов: no; период: NR; заметка: Coded L2 because it requires symptom 1 (reaction) and symptom 5 (social impairment). The authors say it may be more applicable in clinical settings.
- E6: источник порога: study's own; правило: adhoc row; symptom count (L1); G3; у авторов: «high perceived misophonia (criterion 9)»; главная у авторов: no; период: NR
- E7: источник порога: study's own; правило: adhoc row; symptom count (L1); G3; у авторов: «high perceived misophonia (criterion 9)»; главная у авторов: no; период: NR
- E8: источник порога: study's own; правило: adhoc row; symptom count (L1); G1 sum of bands; у авторов: «high perceived misophonia (criterion 6)»; главная у авторов: no; период: NR; **расчёт: Women, criteria 1-5 bands: 120 + 92 + 94 + 43 + 19 = 368 (Table 4)**; заметка: Table 4 prints 313 (43.3) for women under criterion 6. That is the symptom 1 count from Table 2 and is inconsistent with the bands and the total of 575; the band sum is used instead.
- E9: источник порога: study's own; правило: adhoc row; symptom count (L1); G1 sum of bands; у авторов: «high perceived misophonia (criterion 6)»; главная у авторов: no; период: NR; **расчёт: Men, criteria 1-5 bands: 67 + 48 + 52 + 28 + 12 = 207 (Table 4)**; заметка: Table 4 prints 162 (39.6) for men under criterion 6. That is the symptom 1 count from Table 2 and is inconsistent with the bands; the band sum is used instead.
- E10: источник порога: study's own; правило: adhoc row; symptom count (L1); G3; у авторов: «high perceived misophonia (criterion 7)»; главная у авторов: no; период: NR
- E11: источник порога: study's own; правило: adhoc row; symptom count (L1); G3; у авторов: «high perceived misophonia (criterion 7)»; главная у авторов: no; период: NR
- E12: источник порога: study's own; правило: adhoc row; symptom count (L1); G3; у авторов: «high perceived misophonia (criterion 8)»; главная у авторов: no; период: NR
- E13: источник порога: study's own; правило: adhoc row; symptom count (L1); G3; у авторов: «high perceived misophonia (criterion 8)»; главная у авторов: no; период: NR
- E14: источник порога: study's own; правило: adhoc row; L2: reaction + impairment required; G1; у авторов: «high perceived misophonia (criterion 5)»; главная у авторов: no; период: NR
- E15: источник порога: study's own; правило: adhoc row; L2: reaction + impairment required; G1; у авторов: «high perceived misophonia (criterion 5)»; главная у авторов: no; период: NR

**⚠ Проверка скриптом (обратите внимание):**
- E5, E14, E15: самодельные вопросы на L2: верно, только если требуются и реакция, и нарушения

**Ключевые поля выборки:**
- **n_analysed: 1132** — Table 4 — «Criterion 9 | At least four or more symptoms reported | 40 (9.8) | 62 (8.6) | 102 (9.0)»
- **population: medical_students** — Subjects and Methods — «first and second-year medical students of the Faculty of Medicine»
- **sampling: census** — Subjects and Methods — «about 1200 medical students were approached during classes to join a survey»

**Остальные поля:**
- clinical_group: NA — NA
- country: SRB — Financial support and sponsorship — «The study was financially supported by the Ministry of Education, Science and Technological Development of the Republic of Serbia, projects no. 175078 and no. …»
- setting: university (Faculty of Medicine; questionnaires distributed during classes) — Subjects and Methods — «performed in 2013 among first and second-year medical students of the Faculty of Medicine. As described previously in detail,[15] about 1200 medical students w…»
- data_years: 2013 — Subjects and Methods — «This cross-sectional study was performed in 2013 among first and second-year medical students»
- design: cross-sectional — Subjects and Methods — «This cross-sectional study was performed in 2013»
- topic_disclosed: yes — Subjects and Methods — «to join a survey aiming to estimate the prevalence of noise sensitivity, noise annoyance, left-handedness, self-reported anxiety and depression, and misophonia…»
- inclusion_exclusion: First- and second-year medical students approached in class; only completely filled-out questionnaires analysed. No other criteria stated. — Subjects and Methods — «Out of 1200 distributed questionnaires, 1132 were completely filled out and returned (response rate 94%).»
- n_invited: 1200 — Subjects and Methods — «Out of 1200 distributed questionnaires, 1132 were completely filled out and returned»
- n_responded: 1132 — Subjects and Methods — «Out of 1200 distributed questionnaires, 1132 were completely filled out and returned (response rate 94%).»
- response_rate: 94 — Subjects and Methods — «1132 were completely filled out and returned (response rate 94%)»
- age_mean: 21.4 — Table 1 — «Age (years) | Mean ± SD | 21.5 ± 2.0 | 21.4 ± 2.1 | 21.4 ± 2.1»
- age_sd: 2.1 — Table 1 — «Age (years) | Mean ± SD | 21.5 ± 2.0 | 21.4 ± 2.1 | 21.4 ± 2.1»
- age_min: NR — NR
- age_max: NR — NR
- age_group: adults — Abstract; Table 1 — «A cross-sectional study on 1132 medical students, aged 21.4 ± 2.1 years.»
- pct_female: 63.9 — Table 1 — «Number of students (%) | | 409 (35.3) | 723 (63.7) | 1132 (100.0)»
- informant: self — Abstract — «Misophonia symptoms were self-reported using the Amsterdam Misophonia Scale.»
- mode: paper — Subjects and Methods — «Out of 1200 distributed questionnaires, 1132 were completely filled out and returned»
- instruments: Ad hoc 5-item yes/no symptom checklist adapted from the A-MISO-S (Schröder et al. 2013), translated into the local language (presumably Serbian; language not named); severity not rated — Subjects and Methods — «Each item was responded with yes or no. Unlike the original A-MISO-S,[5] the intensity of each symptom was not measured»
- instrument_validated_in_language: no — Subjects and Methods; Discussion — «We agree that the proposed cutoff is not validated, and it should be understood as a pioneer attempt to measure the problem in the general population.»
- pub_status: journal — Header — «Noise & health; DOI: 10.4103/nah.nah_40_20»
- language: English — Full text — «The Proposed Criteria for High Perceived Misophonia in Young Healthy Adults and the Association Between Misophonia Symptoms and Noise Sensitivity»
- funding_coi: Ministry of Education, Science and Technological Development of the Republic of Serbia (projects 175078, 41020); no conflicts of interest — Financial support; Conflicts of interest — «financially supported by the Ministry of Education, Science and Technological Development of the Republic of Serbia, projects no. 175078 and no. 41020. ... The…»
- notes: Country inferred as Serbia from the funding statement; the text only says 'our country' and 'translated into our language'. Data collected in 2013, published in 2022. The same survey was 'described previously in detail' in ref [15] (noise sensitivity paper): check for overlap with other reports of this cohort. The 5 yes/no items adapt A-MISO-S content but are not the scored A-MISO-S, so instrument = adhoc. n_responded = complete returned questionnaires; the number of incomplete returns is not reported. Sampling was coded census (class-based approach to all first- and second-year students); co…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The study claims to describe young healthy adults, but the frame is first- and second-year students of one medical faculty. — Introduction; Subjects and Methods — «we decided to undertake an observational study among young healthy adults in order to estimate the prevalence of the problem»
2. способ отбора: **unclear** — Students were approached in class (close to a class census), but the report does not say whether every enrolled first- and second-year student was reached ('about 1200'). — Subjects and Methods — «about 1200 medical students were approached during classes to join a survey»
3. размер выборки: **yes** — n = 1132, which is at least 385. — Subjects and Methods — «1132 were completely filled out and returned»
4. описание выборки и условий: **unclear** — Age, sex, setting and year are reported. The country is not named in the text and can only be inferred from the funding statement (Serbia). — Subjects and Methods; Funding — «The sample included 409 male and 723 female students, aged 21.4 ± 2.1 years.»
5. охват (пропуски): **yes** — Only complete questionnaires were analysed: 1132 of 1200 distributed (94%). Incomplete returns were at most 5.7% of those distributed. — Subjects and Methods — «Out of 1200 distributed questionnaires, 1132 were completely filled out and returned (response rate 94%).»
6. валидность определения случая: **no** — Ad hoc yes/no items adapted from the A-MISO-S, with study-defined symptom-count criteria. The authors state the criteria are not validated. — Discussion — «We agree that the proposed cutoff is not validated»
7. единое надёжное измерение: **yes** — Everyone got the same paper questionnaire and the same criteria. Reliability was reported (alpha 0.753, test-retest in 30 students). — Subjects and Methods — «tested and retested within a 2-week period. The Cronbach's coefficient alpha equaled 0.753»
8. статистика (числитель и знаменатель): **yes** — Counts and denominators are given in Table 4, so CIs can be calculated. One error: the sex-specific counts for criterion 6 are wrong (see consistency notes). — Table 4 — «Criterion 9 | At least four or more symptoms reported | 40 (9.8) | 62 (8.6) | 102 (9.0)»
9. отклик: **yes** — Response rate 94%. — Subjects and Methods — «(response rate 94%)»

Правки:
- 

Проверено: да
---

## ST073 · Rinaldi 2022 · Frontiers in psychology

Основной отчёт R0956: [текст](../../fulltext/text/R0956.txt) — «Poorer Well-Being in Children With Misophonia: Evidence From the Sussex Misophonia Scale for Adolescents.» — [DOI](https://doi.org/10.3389/fpsyg.2022.808379)
Приложен R0787: [текст](../../fulltext/text/R0787.txt) — «Autistic traits, emotion regulation, and sensory sensitivities in children and adults with Misophonia.»
Связь отчётов: Multisense cohort, 142 children aged 10-14 tested Nov 2020-Mar 2021: R0787 Experiment 2 is the same sample as R0956
Не выписано ИИ: Parents of the children (n=133 in R0956; 138 in R0787): informants for other measures, not assessed for their own misophonia. R0787 Experiment 1 (adults: self-declared misophonics recruited via online misophonia forums plus University of Sussex controls): a different sample, not part of this job; the misophonia-recruited stream is E1.
Расхождения в тексте: R0956 and R0787 report the same classification (15 misophonic: 9 girls, 6 boys; 127 controls: 56 girls, 71 boys). The parent counts differ: R0956 has 133 parents (113 F, 19 M, 1 NS) and R0787 has 138 (116 F, 21 M, 1 NS). R0787 calls the >=49 threshold one "taken from" Rinaldi et al. 2022, but R0956 shows it is the 90th percentile of this same sample, so it is E3 in both reports. Sex subgroups add up: 65 = 9 + 56 and 77 = 6 + 71.
Заметка ИИ: There is one eligible sample. Every estimate is E3, a percentile-based threshold, so none is pooled. R0956 has no page markers, so locations are given by section.

### ST073-1 · MULTISENSE cohort follow-up, Sussex schools, GBR, children 10-14 y, n=142
Отчёты: R0956 (main); R0787 (Experiment 2)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SMS-Adolescent · SMS-Adolescent >=49 (90th percentile of sample) | **E3** | **15 / 142** | 10.6 | Results, Identifying Children With Misophonia | «to set the child threshold at the 90th percentile of total SMS-Adolescent scores. This threshold captured all children with a test-score of 49 or higher... we classified 15 children with misophonia.» |
| E2 | female | SMS-Adolescent · SMS-Adolescent >=49 (90th percentile of sample) | **E3** | **9 / 65** | 13.8 | Results, Identifying Children With Misophonia | «This group comprised nine girls ... and six boys ... The remaining 127 children were designated controls, and comprised 56 girls ... and 71 boys» |
| E3 | male | SMS-Adolescent · SMS-Adolescent >=49 (90th percentile of sample) | **E3** | **6 / 77** | 7.8 | Results, Identifying Children With Misophonia | «This group comprised nine girls ... and six boys ... The remaining 127 children were designated controls, and comprised 56 girls ... and 71 boys» |

- E1: источник порога: percentile of this sample; правило: SMS-Adolescent row; G5 percentile of Multisense sample; у авторов: «children with misophonia»; главная у авторов: yes; период: NR; заметка: Prevalence ~10% fixed by the percentile threshold; listed, not pooled.
- E2: источник порога: percentile of this sample; правило: SMS-Adolescent row; G5 percentile of Multisense sample; у авторов: «children with misophonia»; главная у авторов: no; период: NR; **расчёт: n = 9 misophonic girls + 56 control girls = 65**
- E3: источник порога: percentile of this sample; правило: SMS-Adolescent row; G5 percentile of Multisense sample; у авторов: «children with misophonia»; главная у авторов: no; период: NR; **расчёт: n = 6 misophonic boys + 71 control boys = 77**

**Ключевые поля выборки:**
- **n_analysed: 142** — Results, Identifying Children With Misophonia — «we classified 15 children with misophonia... The remaining 127 children were designated controls»
- **population: school_pupils** — Participants — «The inclusion criteria for the MULTISENSE project was to be in Years 2–5 within 22 Infant and Primary schools across Sussex»
- **sampling: convenience** — Discussion — «were a sub-set from a much larger randomly-sampled cohort (MULTISENSE) but were not strictly randomly-sampled themselves (They were children whose parents had signed on for further study, comprising around 5% of the initial wave.)»

**Остальные поля:**
- clinical_group: NA — NA
- country: GBR — Participants — «22 Infant and Primary schools across Sussex in the south of England in 2016»
- setting: school-recruited community cohort (MULTISENSE); tested online from home — Participants; Materials and Procedure — «Participants completed our study from home, using our in-house web application, which houses tests and advice on misophonia.»
- data_years: 2020-2021 — Materials and Procedure — «Testing took place between November 2020 and March 2021.»
- design: validation study — Introduction — «A final aim of our manuscript is to validate a novel diagnostic measure for adolescent misophonia (our SMS-Adolescent).»
- topic_disclosed: NR — Materials and Procedure — «Parent participants were sent a URL via email to take part, and this led them directly into our testing page without any access to the broader framework.»
- inclusion_exclusion: MULTISENSE cohort children (Years 2-5 in 22 Sussex schools in 2016) whose parents agreed to further contact; aged 10-14 at testing — Participants — «The 142 children in our current study were those whose parents had agreed to stay in touch for future screening»
- n_invited: NR — Participants — «the sample comprised over 3,000 children in the initial recruitment wave»
- n_responded: 142 — Participants — «We tested 275 participants, comprising 142 children and adolescents aged 10–14 years»
- response_rate: NR — Discussion — «comprising around 5% of the initial wave»
- age_mean: 11.72 — Participants — «142 children and adolescents aged 10–14 years (Mean 11.72 SD 1.12; 65 female, 77 male)»
- age_sd: 1.12 — Participants — «(Mean 11.72 SD 1.12; 65 female, 77 male)»
- age_min: 10 — Participants — «aged 10–14 years»
- age_max: 14 — Participants — «aged 10–14 years»
- age_group: mixed — Participants — «aged 10–14 years»
- pct_female: 45.8 — Participants — «65 female, 77 male»
- informant: self — Discussion — «our screening for misophonia was child-completed»
- mode: online — Materials and Procedure — «Participants completed our study from home, using our in-house web application»
- instruments: Sussex Misophonia Scale for Adolescents (SMS-Adolescent), English — Sussex Misophonia Scale for Adolescents — «This novel self-report questionnaire presents 48 known misophonia triggers in Part 1 (see Table 1), and then 39 Likert-type statements in Part 2.»
- instrument_validated_in_language: yes — Introduction; R0787, Experiment 2 Materials — «has been validated in adolescents with convergent validity against measures of life-satisfaction, quality of life, anxiety, and obsessive compulsive traits (Ri…»
- pub_status: journal — Header — «Year: 2022; venue: Frontiers in psychology»
- language: English — Full text — «Poorer Well-Being in Children With Misophonia: Evidence From the Sussex Misophonia Scale for Adolescents»
- funding_coi: No funding statement in R0956 text; R0787 (same sample): REAM foundation Misophonia Research Fund. No COI declared. — Conflict of Interest; R0787, Acknowledgements — «Authors received funding from the REAM foundation, Misophonia Research Fund initiative awarded to JS and JW.»
- notes: Same sample as R0787 Experiment 2 (same 15/142 classification). Threshold SMS-A>=49 is the 90th percentile of this sample (E3 by Table 1/G5), so prevalence is fixed by design at about 10%. R0956 is itself the validation paper of SMS-Adolescent (convergent/discriminant validity only, no ROC). Parent numbers differ: 133 in R0956 vs 138 in R0787. The cohort subset (~5% of initial wave) was compared with the remainder on well-being (no differences) but scored higher in spelling/maths (R0787 footnote). Design could alternatively be coded as cohort follow-up (tested 4 years after recruitment).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is a ~5% volunteer subset of a cohort from 22 Sussex schools, while authors claim to describe children in the population at large. — Discussion — «They were children whose parents had signed on for further study, comprising around 5% of the initial wave.»
2. способ отбора: **no** — Participants were families that opted in to further contact, not randomly sampled. — Discussion — «but were not strictly randomly-sampled themselves»
3. размер выборки: **no** — n = 142 < 385. — Participants — «comprising 142 children and adolescents aged 10–14 years»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported. — Participants; Materials and Procedure — «(Mean 11.72 SD 1.12; 65 female, 77 male)... Testing took place between November 2020 and March 2021.»
5. охват (пропуски): **yes** — All 142 tested children were classified (15 + 127); no missing misophonia data apparent. — Results, Identifying Children With Misophonia — «we classified 15 children with misophonia... The remaining 127 children were designated controls»
6. валидность определения случая: **no** — SMS-Adolescent >=49 is a sample percentile (90th) without interview/ROC anchoring; listed as 'no' in rule G12. — Results, Identifying Children With Misophonia — «In children however, the threshold for misophonia is unknown.»
7. единое надёжное измерение: **yes** — Same child-completed online instrument and threshold for all; alpha reported in sample. — Sussex Misophonia Scale for Adolescents — «In part 2, our measure showed an excellent overall internal consistency of α = 0.97.»
8. статистика (числитель и знаменатель): **yes** — Numerator 15 and denominator 142 clear; CI calculable (though proportion is fixed by percentile threshold). — Results, Identifying Children With Misophonia — «Using this threshold score, we classified 15 children with misophonia.»
9. отклик: **yes** — Low uptake (~5%) but responders were compared with the rest of the original wave on well-being indicators (differences only in spelling/maths). — R0956 Discussion; R0787, Footnotes — «there were no well-being differences between our subset and the larger wave (using seven different well-being indicators, see footnote 1)»

Правки:
- 

Проверено: да
---

## ST074 · Samermit 2022 · Frontiers in psychology

Основной отчёт R0963: [текст](../../fulltext/text/R0963.txt) — «Development and Evaluation of a Sound-Swapped Video Database for Misophonia.» — [DOI](https://doi.org/10.3389/fpsyg.2022.890829)
Приложен R0940: [текст](../../fulltext/text/R0940.txt) · [PDF](../../fulltext/pdf/R0940.pdf) — «Sound-Swapped Video Database»
Связь отчётов: UC Santa Cruz Study 3 (n = 102): OSF record R0940 and Frontiers article R0963
Не выписано ИИ: Study 1 interview sample (n=80, Bay Area/Santa Cruz; recruited as people with misophonia after a phone pre-screen): E1, recruited because of misophonia; only MQ means were reported. Study 1 Stage 1 naive participants (n=16): no misophonia measure, so no estimate. Study 2 (n=34, UCSC participant pool): no misophonia measure reported, so no estimate.
Расхождения в тексте: (1) The prevalence count is printed as '14 participants out of 101 (13.7%)', but 14/101 = 13.86% and 14/102 = 13.73%. Elsewhere, n=102 is used (paired t101), and the two-sample test is reported as t101. Cases=14 and n=101 were extracted as printed. (2) The Methods (Study 1) say 'A score above 7 ... indicates clinically significant', while the Study 3 Results and the Discussion use '7 or above'. The estimate follows the applied rule (>=7). (3) The MSS range is given as 0-15 in the Methods and 1-15 in the Results. (4) R0940 is the published PDF of the same article; its text matches R0963 and also has the Funding section, which is missing from the R0963 text.
Заметка ИИ: I extracted one eligible sample: Study 3, the UCSC participant pool, n=102. The other three groups were left out (see excluded_samples). Prevalence was a secondary analysis in an experimental study. Funding is taken from R0940.

### ST074-1 · UC Santa Cruz psychology participant pool, Study 3, USA, n=102
Отчёты: R0963 (main); R0940

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **14 / 101** | 13.9 | R0963 Results, Study 3; Discussion (R0940 p.9, p.11) | «There are 14 participants out of 101 (13.7% of the sample) that had misophonia severity scores of 7 or above.» |
| E2 | all | MQ · MSS>=10 (inferred: participants scoring 10 or 11) | **L2** | **4 / 101** | 4.0 | R0963 Results, Study 3 (R0940 p.9) | «we found that the correlation is driven by four participants with very high scores (10 and 11 on the scale).» |

- E1: источник порога: developer paper; правило: MQ row; L2 MSS >=7; у авторов: «clinically significant misophonic reactions»; главная у авторов: yes; период: NR; заметка: Denominator unclear: 14/101 = 13.9%, but 13.7% = 14/102. Methods say 'A score above 7' while Results use '7 or above'.
- E2: источник порога: study's own; правило: MQ row; G2 (above MSS >=7 cut-off), G3; у авторов: «very high scores»; главная у авторов: no; период: NR; заметка: Not presented as a prevalence. Cumulative MSS >=10 assumes that nobody scored above 11, which the text implies but does not state (see Figure 8). The reviewer should check this against Figure 8.

**⚠ Проверка скриптом (обратите внимание):**
- E2: пары «случаи / n» нет в независимом предложении ИИ по полному тексту (там: 14/101) — сверьте числа

**Ключевые поля выборки:**
- **n_analysed: 101** — R0963 Results, Study 3 — «There are 14 participants out of 101 (13.7% of the sample) that had misophonia severity scores of 7 or above.»
- **population: university_students** — R0963 Study 3, Participants — «University of California, Santa Cruz Psychology participant pool who received course credit»
- **sampling: convenience** — R0963 Study 3, Participants — «We recruited 102 naïve participants ... from the University of California, Santa Cruz Psychology participant pool who received course credit»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — R0963 Study 3, Participants — «from the University of California, Santa Cruz Psychology participant pool»
- setting: university (psychology participant pool; remote online study) — R0963 Study 3, Participants; Discussion — «from the University of California, Santa Cruz Psychology participant pool who received course credit for their participation»
- data_years: NR — R0940, p.1 — «Received: 06 March 2022»
- design: other — R0963 Study 3, Procedure — «After viewing and rating all 40 stimuli, participants then completed the Misophonia Questionnaire (MQ) and answered several demographic questions.»
- topic_disclosed: NR — R0963 Study 3, Participants — «We recruited 102 naïve participants»
- inclusion_exclusion: Naive participants from UCSC psychology participant pool; not screened for misophonia — R0963 Discussion (limitations) — «we did not screen for participants with misophonia»
- n_invited: NR — NA
- n_responded: 102 — R0963 Study 3, Participants — «We recruited 102 naïve participants (65 women, 33 men, and 4 non-binary; ages 18–29)»
- response_rate: NR — NA
- age_mean: NR — NA
- age_sd: NR — NA
- age_min: 18 — R0963 Study 3, Participants — «ages 18–29»
- age_max: 29 — R0963 Study 3, Participants — «ages 18–29»
- age_group: adults — R0963 Study 3, Participants — «ages 18–29»
- pct_female: 63.7 — R0963 Study 3, Participants — «102 naïve participants (65 women, 33 men, and 4 non-binary»
- informant: self — R0963 Study 3, Procedure — «participants then completed the Misophonia Questionnaire (MQ)»
- mode: online — R0963 Study 3, Participants; Discussion — «Participants completed a questionnaire via Qualtrics ... the study was conducted remotely»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), English: Symptom Scale, Emotions and Behaviors Scale, Misophonia Severity Scale — R0963 Study 3, Procedure; Results — «participants then completed the Misophonia Questionnaire (MQ)»
- instrument_validated_in_language: yes — R0963 Introduction; R0940 References — «Misophonia Questionnaire (MQ; Wu et al., 2014)»
- pub_status: journal — R0963 header — «Year: 2022; venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2022.890829»
- language: English — R0963 full text — «Development and Evaluation of a Sound-Swapped Video Database for Misophonia»
- funding_coi: Funded by the Misophonia Research Fund (UCSC OSP #A20-0510); authors declare no conflict of interest — R0940, p.11 Funding; R0963 Conflict of Interest — «The Misophonia Research Fund (UCSC OSP #A20-0510) funded this project in its entirety, including open access publication fees.»
- notes: Experimental stimulus-rating study (sound-swapped videos); MQ completed after the task; prevalence not a study aim. pct_female derived: 65/102 = 63.7% (4 non-binary). n_analysed 101 as printed, but 13.7% equals 14/102 (14/101 = 13.9%); one participant possibly missing the severity item. Funding stated only in R0940 (OSF PDF of the same article). MQ Severity Scale described as 0-15 in Methods but 1-15 in Results. Mean MQ total 27.5 (SD 11.0), mean MSS 4.0 (SD 2.6). Interview sample (Study 1, n=80) recruited separately for misophonia; not part of this sample.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is the psychology participant pool, only part of UCSC students — R0963 Study 3, Participants — «from the University of California, Santa Cruz Psychology participant pool who received course credit»
2. способ отбора: **no** — Volunteer sign-up for course credit (convenience) — R0963 Study 3, Participants — «We recruited 102 naïve participants ... who received course credit for their participation»
3. размер выборки: **no** — n=101-102 < 385 — R0963 Results, Study 3 — «There are 14 participants out of 101»
4. описание выборки и условий: **unclear** — Age range, sex, setting and country reported; data collection dates not reported — R0963 Study 3, Participants — «65 women, 33 men, and 4 non-binary; ages 18–29»
5. охват (пропуски): **yes** — 101 of 102 with severity data (about 1% missing) — R0963 Results, Study 3 — «There are 14 participants out of 101 (13.7% of the sample)»
6. валидность определения случая: **yes** — MQ Severity Scale >=7, English original version (Wu et al. 2014) — R0963 Results, Study 3 — «For this scale, a score of 7 or above would constitute clinically significant misophonic reactions.»
7. единое надёжное измерение: **yes** — Same online MQ for all; Cronbach alpha reported in this sample — R0963 Results, Study 3 — «the internal consistency (Cronbach’s alpha) was 0.792 for the Misophonia Symptom Scale, 0.834 for the Misophonia Emotions and Behaviors Scale, and 0.863 for th…»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given (minor 101/102 discrepancy); CI calculable — R0963 Results, Study 3 — «There are 14 participants out of 101 (13.7% of the sample)»
9. отклик: **no** — Opt-in participant pool; no denominator of invited people, no handling of non-response — R0963 Study 3, Participants — «We recruited 102 naïve participants ... from the University of California, Santa Cruz Psychology participant pool»

Правки:
- 

Проверено: да
---

## ST075 · Savard 2022 · Frontiers in neuroscience

Основной отчёт R0964: [текст](../../fulltext/text/R0964.txt) — «Specificity of Affective Responses in Misophonia Depends on Trigger Identification.» — [DOI](https://doi.org/10.3389/fnins.2022.879583)
Расхождения в тексте: The >61 count (4/300) is given twice: once as 'scored above 61' (4.1) and once as 'scoring above 61' (5. Conclusion). The paper also says the cut-off is 61 ('a general cut-off of 61 out of 70 points'), so it is unclear whether >61 or >=61 was applied. The MM group was meant to be the top 20% but holds 66/300 = 22%, probably because of ties at the cut score. The LM group (bottom 20%, <31, n=68) is not a case definition and was not extracted.
Заметка ИИ: An experimental online study whose prevalence-relevant information is limited to the MisoQuest distribution. The authors give no main prevalence estimate. The Supplementary Material, which has a data-driven cut-off, was not available.

### ST075-1 · Prolific online community sample, English-speaking countries (CAN/USA, IRL/GBR, AUS/NZL), n=300
Отчёты: R0964 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MisoQuest · MisoQuest >61 (reported as 'scored above 61'; developer cut-off 61) | **L2** | **4 / 300** | 1.3 | 4.1 Discussion; 5. Conclusion | «only 4 out of 300 participants (less than 2%) scored above 61 on the MisoQuest» |
| E2 | all | MisoQuest · MisoQuest >45 (top 20% of this sample) | **E3** | **66 / 300** | 22.0 | 3.1 MisoQuest Scores | «The resulting MM group (N = 66, 33 females, mean age: 24.0 SD = 5.9) included participants with a total score above 45 on the MisoQuest» |
| E3 | female | MisoQuest · MisoQuest >45 (top 20% of this sample) | **E3** | **33 / 151** | 21.9 | 3.1 MisoQuest Scores; 2.1 Participants | «MM group (N = 66, 33 females ... 151 females» |
| E4 | male | MisoQuest · MisoQuest >45 (top 20% of this sample) | **E3** | **33 / 149** | 22.1 | 3.1 MisoQuest Scores; 2.1 Participants | «MM group (N = 66, 33 females ... (149 males, 151 females» |

- E1: источник порога: developer paper; правило: MisoQuest row; L2 >=61; G2 (>61 is at or above the L2 cut-off); у авторов: «recommended screening score for severe misophonia»; главная у авторов: no; период: NR; заметка: It is unclear whether >61 or >=61 was applied. The English MisoQuest is unvalidated. No breakdown by sex or age.
- E2: источник порога: percentile of this sample; правило: MisoQuest row; G5 percentile of the same sample; у авторов: «Most-Misophonic (MM) group»; главная у авторов: no; период: NR; заметка: Top 20% chosen to match a 20% prevalence from the literature. 66/300 = 22%. Listed, not pooled.
- E3: источник порога: percentile of this sample; правило: MisoQuest row; G5 percentile of the same sample; у авторов: «Most-Misophonic (MM) group»; главная у авторов: no; период: NR; заметка: Denominator = 151 females in the whole sample (Section 2.1).
- E4: источник порога: percentile of this sample; правило: MisoQuest row; G5 percentile of the same sample; у авторов: «Most-Misophonic (MM) group»; главная у авторов: no; период: NR; **расчёт: 66 MM total - 33 females = 33 males; n = 149 males (Section 2.1)**; заметка: Assumes sex was binary (149+151=300).

**Ключевые поля выборки:**
- **n_analysed: 300** — 4.1 Discussion — «only 4 out of 300 participants (less than 2%) scored above 61 on the MisoQuest»
- **population: gp_other** — 1.3 Goal — «we collected responses from an online community sample on a scale assessing misophonia»
- **sampling: convenience** — 2.1 Participants; 4.1 — «there are differences between the general population and online convenience samples»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: MULTI: CAN, USA, IRL, GBR, AUS, NZL — 2.1 Participants — «recruitment was only open to residents of predominantly English-speaking countries (65% from Canada/USA, 32% from the Ireland/UK, 3% from Australia/New-Zealand)»
- setting: online panel (Prolific), with the experiment run on Pavlovia — 2.1 Participants; 2.2 Protocol — «were recruited online through Prolific (https://www.prolific.co/)»
- data_years: NR — NA — «NR»
- design: screening phase of experiment — 2.2 Protocol — «Before proceeding with the task, participants were asked to complete a questionnaire designed to screen for misophonia (see Section 2.4).»
- topic_disclosed: NR — NA — «NR»
- inclusion_exclusion: Adults resident in predominantly English-speaking countries; self-reported good neurological health, normal hearing, no diagnosed language disorder. Excluded: people taking medication for depression, anxiety or low mood, and people with self-reported ASD diagnosis. Prolific approval rate >92%. — 2.1 Participants — «we used the Prolific pre-screeners to exclude all individuals who were taking medication to treat symptoms of depression, anxiety, or low mood... The exclusion…»
- n_invited: NR — NA — «NR»
- n_responded: 300 — 2.1 Participants — «A total of 300 adults participated in this study (149 males, 151 females»
- response_rate: NR — NA — «NR»
- age_mean: 24.6 — 2.1 Participants — «age range: 18–50 years, mean age: 24.6 SD = 6.7»
- age_sd: 6.7 — 2.1 Participants — «mean age: 24.6 SD = 6.7»
- age_min: 18 — 2.1 Participants — «age range: 18–50 years»
- age_max: 50 — 2.1 Participants — «age range: 18–50 years»
- age_group: adults — 2.1 Participants — «A total of 300 adults participated in this study»
- pct_female: 50.3 — 2.1 Participants — «149 males, 151 females»
- informant: self — 4.2 Discussion — «two sub-groups of participants were formed on the basis of their self reports in a questionnaire designed for misophonia symptom assessment»
- mode: online — 2.2 Protocol — «redirected to an online behavioral platform (Pavlovia, https://pavlovia.org/) running the experiment designed on PsychoPy»
- instruments: MisoQuest (English translation provided by the developers) — 2.4 Questionnaires — «The English translation was provided by the team who developed the questionnaire, and (to the best of our knowledge) has yet to be validated in an English-spea…»
- instrument_validated_in_language: no — 5. Conclusion — «it has not yet been validated in an English-speaking population. To our knowledge, this is the first study that is using the English translation of the questio…»
- pub_status: journal — Header — «Frontiers in neuroscience; DOI: 10.3389/fnins.2022.879583»
- language: English — Full text — «Specificity of Affective Responses in Misophonia Depends on Trigger Identification»
- funding_coi: Misophonia Research Fund, REAM foundation, NSERC award to M-AS; authors declare no conflict of interest — Funding; Conflict of Interest — «This research was supported by the Misophonia Research Fund and REAM foundation, and the Natural Sciences and Engineering Research Council of Canada (NSERC) aw…»
- notes: Experimental study (sound identification in babble); MisoQuest given to all 300 before the task. Excluding people on medication for depression, anxiety or low mood may have removed severe cases (the authors say so). The wording 'scored above 61' leaves open whether >61 or >=61 was applied. The Supplementary Material has a data-driven grouping (not available). Data on OSF (https://osf.io/39dzb/). 80% were aged 18-29; 60% were students.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The target is the 'general population', but the frame is Prolific users in English-speaking countries, with medication and ASD exclusions. — 4.1 Discussion — «our sample may not be representative of all populations... there are differences between the general population and online convenience samples»
2. способ отбора: **no** — Volunteer opt-in online panel (convenience). — 2.1 Participants — «were recruited online through Prolific»
3. размер выборки: **no** — n=300, below 385. — 2.1 Participants — «A total of 300 adults participated in this study»
4. описание выборки и условий: **unclear** — Age, sex, setting and countries are reported; data-collection dates are not. — 2.1 Participants — «149 males, 151 females; age range: 18–50 years, mean age: 24.6 SD = 6.7»
5. охват (пропуски): **yes** — All 300 participants were included in the MisoQuest distribution; no missing questionnaire data reported. — 2.4 Questionnaires — «The internal consistency (Cronbach's alpha) of the MisoQuest in our sample of 300 participants was of 0.890.»
6. валидность определения случая: **no** — The primary L2 definition (MisoQuest above 61) uses an English version with no published validation, and 'above 61' may be stricter than the >=61 cut-off. — 2.4 Questionnaires — «has yet to be validated in an English-speaking sample»
7. единое надёжное измерение: **yes** — Same instrument and online mode for everyone; alpha reported in this sample. — 2.4 Questionnaires — «The internal consistency (Cronbach's alpha) of the MisoQuest in our sample of 300 participants was of 0.890.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (4/300); CI calculable; no weighting needed. — 4.1 Discussion — «only 4 out of 300 participants (less than 2%) scored above 61 on the MisoQuest»
9. отклик: **no** — Open online panel recruitment with no denominator of invited people. — 2.1 Participants — «were recruited online through Prolific»

Правки:
- 

Проверено: да
---

## ST076 · Smit 2022 · Frontiers in neuroscience

Основной отчёт R0972: [текст](../../fulltext/text/R0972.txt) — «A genome-wide association study of a rage-related misophonia symptom and the genetic link with audiological traits, psychiatric disorders, and personality.» — [DOI](https://doi.org/10.3389/fnins.2022.971752)
Приложен R0973: [текст](../../fulltext/text/R0973.txt) · [PDF](../../fulltext/pdf/R0973.pdf) — «Genetic evidence for the link of misophonia with psychiatric disorders and personality»
Связь отчётов: 23andMe chewing-rage item (n = 80,607): medRxiv preprint R0973 and article R0972
Расхождения в тексте: Main report R0972 gives 22% positive among 80,607; R0973 Figure 1 gives yes 17,606 and no 63,001 (sum 80,607; 21.8%), which matches the rounded 22%. R0973 calls 22% 'likely to be an overestimation' and says no population prevalence numbers are available. R0972 compares it with published prevalences (5-5.9% Germany, 12.8% Turkey, 18% UK).
Заметка ИИ: One sample: the 23andMe chewing-rage item, analysed secondarily from the Fayzullina et al. 2015 white paper. Single ad hoc intensity item, so L1 and JBI 6 = no. Check for overlap with any other included report of the 23andMe item.

### ST076-1 · 23andMe research participants, European ancestry, chewing-rage item (n = 80,607)
Отчёты: R0972 (main); R0973

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · 'yes' to 'Does the sound of other people chewing fill you with rage?' (yes/no item) | **L1** | **17606 / 80607** | 21.8 | R0972 Materials and methods (22%); R0973, Page 5, Figure 1 … | «N=80607 participants who reported either yes (N=17606) or no (N=63001) to the question: "Does the sound of other people chewing fill you with rage?"» |

- E1: источник порога: study's own; правило: adhoc row; L1 intensity item ('does the sound of chewing fill you with rage?'); у авторов: «prevalence of a positive answer; rage-related misophonia symptom»; главная у авторов: yes; период: NR; заметка: Main report gives only 22%; the counts come from R0973. 17,606/80,607 = 21.8%. Authors call it an overestimation of clinical prevalence. Non-yes/no answerers excluded from the denominator.

**Ключевые поля выборки:**
- **n_analysed: 80607** — Materials and methods, GWAS summary statistics — «in 80,607 subjects from the general population, including only subjects who answered yes or no to the question.»
- **population: gp_other** — Materials and methods, GWAS summary statistics — «in 80,607 subjects from the general population, including only subjects who answered yes or no to the question.»
- **sampling: convenience** — Discussion (limitations) — «participation in the UK Biobank and 23andMe participation may come with a participation bias, likely selecting on higher educational attainment.»

**Остальные поля:**
- clinical_group: NA — NA
- country: NR — Materials and methods, GWAS summary statistics — «published a GWAS on the self-reported item of "Does the sound of other people chewing fill you with rage?" in 80,607 subjects from the general population»
- setting: online panel: customers of the genetic service provider 23andMe, Inc. taking part in its research (secondary analysis of the GWAS white paper by Fayzullina et al. 2015) — Introduction; Discussion — «we used a proxy in the form of a GWAS of a common misophonia symptom assessed in a general population-based sample (23andMe)»
- data_years: NR — Materials and methods — «Fayzullina et al. (2015) published a GWAS on the self-reported item»
- design: other — Ethics statement; Materials and methods — «This study was secondary analysis of published GWAS results that were approved by their respective ethics committees.»
- topic_disclosed: NR — Materials and methods — «a GWAS on the self-reported item of "Does the sound of other people chewing fill you with rage?"»
- inclusion_exclusion: 23andMe participants who answered yes or no to the chewing-rage item; >97% European ancestry required — Materials and methods, GWAS summary statistics — «including only subjects who answered yes or no to the question... All study participants were required to have over 97% European ancestry»
- n_invited: NR — NA
- n_responded: NR — NA
- response_rate: NR — NA
- age_mean: NR — NA
- age_sd: NR — NA
- age_min: NR — NA
- age_max: NR — NA
- age_group: NR — NA
- pct_female: NR — Materials and methods — «There was no selection on gender.»
- informant: self — Abstract — «on a self-report item probing a single common misophonic symptom: the occurrence of rage when others produce eating sounds.»
- mode: NR — NA
- instruments: Ad hoc single yes/no item 'Does the sound of other people chewing fill you with rage?' (23andMe; English wording as quoted, language of administration NR) — Materials and methods, GWAS summary statistics — «the self-reported item of "Does the sound of other people chewing fill you with rage?"»
- instrument_validated_in_language: no — Discussion (limitations) — «the GWAS of misophonia was based on a self-reported symptom of misophonia rather than a case-control study of misophonia.»
- pub_status: journal — Header: Frontiers in neuroscience 2022 — «Year: 2022; venue: Frontiers in neuroscience; DOI: 10.3389/fnins.2022.971752»
- language: English — Full text — «A genome-wide association study of a rage-related misophonia symptom and the genetic link with audiological traits, psychiatric disorders, and personality»
- funding_coi: Funding NR in text; authors declare no conflict of interest; 23andMe provided the white-paper results — Conflict of interest; Acknowledgments — «The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict…»
- notes: Secondary analysis: the prevalence figure comes from the unpublished, non-peer-reviewed 23andMe white paper (Fayzullina et al. 2015). Any other report of the 23andMe chewing-rage item (the white paper, preprint R0973) is the same sample, so do not count it twice. Main report gives only 22%; R0973 Figure 1 gives the counts (yes 17,606; no 63,001). People who did not answer yes/no were excluded, and their number is not reported. Age, sex, country and data years not reported.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Claimed general population; frame is 23andMe customers of European ancestry only — Materials and methods; Discussion — «All study participants were required to have over 97% European ancestry»
2. способ отбора: **no** — Volunteer customers of a commercial genetic service; participation bias acknowledged — Discussion (limitations) — «23andMe participation may come with a participation bias, likely selecting on higher educational attainment.»
3. размер выборки: **yes** — n = 80,607 >= 385 — Materials and methods — «in 80,607 subjects from the general population»
4. описание выборки и условий: **no** — Age, sex, country and dates of data collection not reported — Materials and methods — «There was no selection on gender.»
5. охват (пропуски): **unclear** — Only yes/no answerers were included; the number of other or missing answers is not reported — Materials and methods — «including only subjects who answered yes or no to the question.»
6. валидность определения случая: **no** — Ad hoc single intensity item (L1) — Materials and methods — «"Does the sound of other people chewing fill you with rage?"»
7. единое надёжное измерение: **unclear** — Same item for everyone, but mode not reported and no reliability data — Materials and methods — «a GWAS on the self-reported item of "Does the sound of other people chewing fill you with rage?"»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator traceable (17,606/80,607 in R0973); CI calculable; no weighting needed for this design — R0973, Page 5, Figure 1 caption — «N=80607 participants who reported either yes (N=17606) or no (N=63001)»
9. отклик: **unclear** — No number of invited people or response rate reported — NA

Правки:
- 

Проверено: да
---

## ST077 · Tada 2022 · The Japanese journal of psychology

Основной отчёт R0977: [текст](../../fulltext/text/R0977.txt) · [PDF](../../fulltext/pdf/R0977.pdf) — «Sensitivity to everyday sounds:» — [DOI](https://doi.org/10.4992/jjpsy.93.21319)
Расхождения в тексте: The abstract gives the prevalence as 54%; the Results only say 'over 50%' (50 % を超えていた). No counts are printed anywhere, so every count is derived. Table 1 gives MQ descriptives for n=180 (the ASMR subsample), but the analysis section says the MQ distribution was tested on n=552. The 4 straight-line responders were excluded from analysis, but they seem to belong to the 184 ASMR respondents. It is unclear whether they were also removed from the n=552 MQ prevalence; this was assumed not. Figure 1 shows 36.4% male / 63.6% female, but this appears to describe the ASMR-aware group (n=184), not N=552, where 303/552 = 54.9% are female. The Page 1 header carries a template artefact ('2020年 第91巻'); the article was published online on 30 June 2022 (vol. 93).
Заметка ИИ: I split the study into two samples because the students (class enrollees) and the working adults (survey-company panel) were recruited separately. The authors report prevalence only for the combined N=552 and for students. The panel-only figure is derived by subtraction and is approximate. All estimates use MQ Symptom Scale >=14 → L1, and JBI 6 = no. The MQ Severity Scale was not reported.

### ST077-1 · University students, Japan, n=152 (Tada et al. 2022)
Отчёты: R0977 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ Symptom Scale >=14 (mean item >=2) | **L1** | **63 / 152** | 41.4 | Page 4, Results and discussion | «本研究で分析対象を大学生に限定した場合，音嫌悪症の割合は41.4 % であった。[Restricted to university students, the misophonia proportion was 41.4%.]» |

- E1: источник порога: developer paper; правило: MQ row; L1 Symptom Scale >=14; у авторов: «音嫌悪症の割合 [proportion with misophonia]»; главная у авторов: no; период: NR; **расчёт: 41.4% x 152 = 62.9 -> 63 (63/152 = 41.4%)**; заметка: Cut-off attributed to Wu et al. 2014 and Zhou et al. 2017. Japanese MQ translated by the authors, not validated.

**Ключевые поля выборки:**
- **n_analysed: 152** — Page 4, Results and discussion — «本研究で分析対象を大学生に限定した場合，音嫌悪症の割合は41.4 % であった。[When analysis was restricted to university students, the misophonia proportion was 41.4%.]»
- **population: university_students** — Page 2, Methods, Participants — «大学生152 名 [152 university students]»
- **sampling: convenience** — Page 2, Methods, Participants — «大学生については授業の履修者に回答を依頼した。[University students: those taking a class were asked to respond.]»

**Остальные поля:**
- clinical_group: NA — Abstract — «in a non-clinical population (N = 552; 18-60 years)»
- country: JPN — Page 2, Introduction end — «本邦におけるASMR の認知度および音嫌悪症の実態を明らかにした [clarified ... the actual state of misophonia in Japan]»
- setting: university (students enrolled in a course; university not named) — Page 2, Methods, Participants — «大学生については授業の履修者に回答を依頼した。[University students: those taking a class were asked to respond.]»
- data_years: 2020 — Page 2, Methods, Survey and procedure — «オンライン調査は2020 年7 月下旬に実施された。[The online survey was conducted in late July 2020.]»
- design: cross-sectional — Page 2, Methods — «大学生152 名と社会人400 名をあわせた合計552 名...がオンライン調査に参加した。[A total of 552 (152 university students and 400 working adults) took part in an online survey.]»
- topic_disclosed: NR — Page 2, Methods — «Google フォームにて，MQ，AQ，およびASMR 質問票の順に質問項目を提示した。[Items were presented in Google Forms in the order MQ, AQ, ASMR questionnaire.]»
- inclusion_exclusion: Students taking a class; no other criteria stated. 4 participants who gave identical answers to all items were excluded from analyses (apparently from the ASMR subsample of 184) — Page 2, Methods — «4 名の参加者がすべての質問項目で同じ回答をしていたため，データ分析から除外した。[4 participants who gave the same answer to all items were excluded from analysis.]»
- n_invited: NR — Page 2, Methods — «授業の履修者に回答を依頼した [those taking a class were asked to respond]»
- n_responded: 152 — Page 2, Methods, Participants — «大学生152 名 [152 university students]»
- response_rate: NR — Page 2, Methods — «授業の履修者に回答を依頼した [those taking a class were asked to respond]»
- age_mean: NR — Page 2, Methods, Participants — «平均年齢35.5 歳，標準偏差14.2 歳，範囲：18─60 歳 [mean age 35.5, SD 14.2, range 18-60] (whole N=552 only)»
- age_sd: NR — Page 2, Methods, Participants — «平均年齢35.5 歳，標準偏差14.2 歳 (whole N=552 only)»
- age_min: NR — Page 2, Methods, Participants — «範囲：18─60 歳 [range 18-60] (whole N=552 only)»
- age_max: NR — Page 2, Methods, Participants — «範囲：18─60 歳 [range 18-60] (whole N=552 only)»
- age_group: adults — Page 2, Methods, Participants — «範囲：18─60 歳 [range: 18-60 years] (whole sample)»
- pct_female: NR — Page 2, Methods, Participants — «男性248 名，女性303 名，その他1 名 [248 men, 303 women, 1 other] (whole N=552 only)»
- informant: self — Abstract — «through self-reporting measures»
- mode: online — Page 2, Methods — «Google フォームにて，MQ，AQ，およびASMR 質問票の順に質問項目を提示した。[presented via Google Forms]»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), Japanese translation made by the authors (Symptom Scale and Emotions and Behaviors Scale; Severity Scale not mentioned) — Page 2-3, Methods — «ASMR 質問票とMQ の訳出にあたって，著者を含む複数名が個別に担当し，合議のうえで質問項目の日本語訳を決定した。[Several people incl. the authors translated the ASMR questionnaire and MQ independently and decided …»
- instrument_validated_in_language: no — Page 2, Methods, Survey and procedure — «著者を含む複数名が個別に担当し，合議のうえで質問項目の日本語訳を決定した。[Japanese translation decided by consensus among the authors; no validation cited.]»
- pub_status: journal — Page 1, header — «The Japanese Journal of Psychology / J-STAGE Advanced published date: June 30, 2022»
- language: Japanese (English abstract) — Page 1-6 — «日常の音に対する感受性─ASMR，音嫌悪症，および自閉症傾向─ [Sensitivity to everyday sounds: ASMR, misophonia, and autistic traits]»
- funding_coi: JSPS KAKENHI Grant-in-Aid (B) 20H01789; authors declare no conflicts of interest — Page 1 footnote 1; Page 6, COI statement — «本研究は，日本学術振興会 科学研究費補助金（基盤研究B, 20H01789）の助成を受けた。... 開示すべき利益相反に関する事項はない。»
- notes: Recruited separately from the 400 working adults (survey company), so extracted as a separate sample. The combined N=552 estimate (54%) is recorded under the panel sample entry with a 'combined' subgroup label. Age and sex reported only for combined N=552. Part of the results presented at the Acoustical Society of Japan hearing research meeting (2020) (Page 1 footnote 2): possible overlapping report. Page 1 header shows a template artefact ('心理学研究2020年 第91巻 第3号'); published online 30 June 2022.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was students taking one course, not all students — Page 2, Methods, Participants — «大学生については授業の履修者に回答を依頼した。»
2. способ отбора: **no** — Convenience sample of students in a class — Page 2, Methods, Participants — «大学生については授業の履修者に回答を依頼した。»
3. размер выборки: **no** — n=152 < 385 — Page 2, Methods, Participants — «大学生152 名»
4. описание выборки и условий: **no** — Setting, country and dates reported, but age and sex reported only for the combined N=552, not for students — Page 2, Methods — «合計552 名（男性248 名，女性303 名，その他1 名，平均年齢35.5 歳...）»
5. охват (пропуски): **yes** — MQ analysed for all participants (n=552); 41.4% matches 63/152 — Page 3, Methods, Analysis — «MQ 得点（n = 552）»
6. валидность определения случая: **no** — MQ Symptom Scale >=14 has no clinical anchoring (L1); Japanese translation not validated — Page 3, Methods — «音嫌悪症状尺度が14 点以上の場合，すべての質問に対する平均値が2 以上であることを意味し，音嫌悪症状を示唆するカットオフ得点として扱われる»
7. единое надёжное измерение: **yes** — Same online questionnaire and cut-off for all; Cronbach's alpha reported (Symptom .84, in n=180) — Page 3, Table 1 — «Symptom 13.5 5.3 0 28 .84 ... Reliability was calculated using Cronbach's alpha.»
8. статистика (числитель и знаменатель): **yes** — Percentage with known denominator (152); numerator derivable (63); CI calculable — Page 4, Results and discussion — «本研究で分析対象を大学生に限定した場合，音嫌悪症の割合は41.4 % であった。»
9. отклик: **unclear** — Number of students invited and response rate not reported — Page 2, Methods — «授業の履修者に回答を依頼した»

Правки:
- 

Проверено: да
### ST077-2 · Survey-company online panel of adults (社会人), Japan, n=400 (Tada et al. 2022)
Отчёты: R0977 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ Symptom Scale >=14 (mean item >=2) | **L1** | **235 / 400** | 58.8 | Abstract; Page 4, Results and discussion | «The prevalence of misophonia... was estimated at 54 %. / 分析対象を大学生に限定した場合，音嫌悪症の割合は41.4 % であった。» |
| E2 | combined: students + panel (N=552) | MQ · MQ Symptom Scale >=14 (mean item >=2) | **L1** | **298 / 552** | 54.0 | Abstract; Page 4, Results and discussion | «The prevalence of misophonia, previously unknown in Japan, was estimated at 54 %. / MQ 得点に基づく音嫌悪症を呈する割合は，驚くべきことに50 % を超えていた。» |

- E1: источник порога: developer paper; правило: MQ row; L1 Symptom Scale >=14; у авторов: «NR (not reported separately by the authors)»; главная у авторов: no; период: NR; **расчёт: Combined 54% x 552 = 298.1 -> 298; students 41.4% x 152 = 62.9 -> 63; 298 - 63 = 235 (58.8%). Rounding of 54% allows 296-300 combined, so 233-237**; заметка: Approximate; derived by subtraction from rounded percentages. The reviewer should decide whether to use it.
- E2: источник порога: developer paper; правило: MQ row; L1 Symptom Scale >=14; у авторов: «prevalence of misophonia / 音嫌悪症を呈する割合»; главная у авторов: yes; период: NR; **расчёт: 54% x 552 = 298.1 -> 298**; заметка: Spans two separately recruited samples (152 students + 400 panel); do not pool with the subsample estimates. 54% is rounded (296-300 cases possible).

**Ключевые поля выборки:**
- **n_analysed: 400** — Page 2, Methods; Page 3, Analysis — «社会人400 名 ... MQ 得点（n = 552）»
- **population: gp_other** — Page 2, Methods, Participants — «社会人400 名 [400 working adults / members of the public]»
- **sampling: convenience** — Page 2, Methods, Participants — «民間の調査会社に参加者の募集を委託し，成人の男女を無作為抽出して回答を依頼した。[random selection of adult men and women by a private survey company]»

**Остальные поля:**
- clinical_group: NA — Abstract — «in a non-clinical population (N = 552; 18-60 years)»
- country: JPN — Page 2, Introduction end — «本邦におけるASMR の認知度および音嫌悪症の実態を明らかにした [in Japan]»
- setting: online panel (private survey company) — Page 2, Methods, Participants — «社会人については，民間の調査会社に参加者の募集を委託し，成人の男女を無作為抽出して回答を依頼した。[Working adults: recruitment was outsourced to a private survey company, which randomly selected adult men and…»
- data_years: 2020 — Page 2, Methods, Survey and procedure — «オンライン調査は2020 年7 月下旬に実施された。[conducted in late July 2020]»
- design: cross-sectional — Page 2, Methods — «合計552 名...がオンライン調査に参加した。»
- topic_disclosed: NR — Page 2, Methods — «Google フォームにて，MQ，AQ，およびASMR 質問票の順に質問項目を提示した。»
- inclusion_exclusion: Adults (men and women) selected by the survey company; no other criteria stated — Page 2, Methods, Participants — «成人の男女を無作為抽出して回答を依頼した。»
- n_invited: NR — Page 2, Methods, Participants — «成人の男女を無作為抽出して回答を依頼した。»
- n_responded: 400 — Page 2, Methods, Participants — «社会人400 名»
- response_rate: NR — Page 2, Methods — «民間の調査会社に参加者の募集を委託し»
- age_mean: NR — Page 2, Methods, Participants — «平均年齢35.5 歳 (whole N=552 only)»
- age_sd: NR — Page 2, Methods, Participants — «標準偏差14.2 歳 (whole N=552 only)»
- age_min: NR — Page 2, Methods, Participants — «範囲：18─60 歳 (whole N=552 only)»
- age_max: NR — Page 2, Methods, Participants — «範囲：18─60 歳 (whole N=552 only)»
- age_group: adults — Page 2, Methods, Participants — «成人の男女 [adult men and women]»
- pct_female: NR — Page 2, Methods, Participants — «男性248 名，女性303 名，その他1 名 (whole N=552 only)»
- informant: self — Abstract — «through self-reporting measures»
- mode: online — Page 2, Methods — «Google フォームにて...質問項目を提示した。»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), Japanese translation made by the authors (Symptom Scale and Emotions and Behaviors Scale) — Page 2-3, Methods — «ASMR 質問票とMQ の訳出にあたって，著者を含む複数名が個別に担当し，合議のうえで質問項目の日本語訳を決定した。»
- instrument_validated_in_language: no — Page 2, Methods — «合議のうえで質問項目の日本語訳を決定した。[Japanese translation decided by consensus; no validation cited.]»
- pub_status: journal — Page 1, header — «The Japanese Journal of Psychology / J-STAGE Advanced published date: June 30, 2022»
- language: Japanese (English abstract) — Page 1-6 — «日常の音に対する感受性─ASMR，音嫌悪症，および自閉症傾向─»
- funding_coi: JSPS KAKENHI 20H01789; no conflicts of interest declared — Page 1 footnote 1; Page 6 — «日本学術振興会 科学研究費補助金（基盤研究B, 20H01789）... 開示すべき利益相反に関する事項はない。»
- notes: The authors give a prevalence only for the combined N=552 (54%) and for students (41.4%). The panel-only estimate here is derived by subtraction from rounded percentages and is approximate (range 233-237/400). The combined N=552 estimate (both separately recruited samples) is listed under this sample as subgroup 'combined' because it is the authors' headline figure; do not pool it with the subsample estimates. Sampling coded convenience: the authors say 'random selection' (無作為抽出), but it was done within a commercial panel (non-probability frame). Part of the results presented at an ASJ meetin…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is a commercial survey panel, not the Japanese adult population — Page 2, Methods, Participants — «民間の調査会社に参加者の募集を委託し»
2. способ отбора: **no** — Online non-probability panel (random selection within the panel only) — Page 2, Methods, Participants — «成人の男女を無作為抽出して回答を依頼した。»
3. размер выборки: **yes** — n=400 >= 385 — Page 2, Methods, Participants — «社会人400 名»
4. описание выборки и условий: **no** — Age and sex not reported for this sample separately (only combined N=552) — Page 2, Methods — «合計552 名（男性248 名，女性303 名，その他1 名，平均年齢35.5 歳...）»
5. охват (пропуски): **yes** — MQ analysed for all 552 participants — Page 3, Methods, Analysis — «MQ 得点（n = 552）»
6. валидность определения случая: **no** — MQ Symptom Scale >=14 (L1, no clinical anchoring); Japanese translation not validated — Page 3, Methods — «音嫌悪症状尺度が14 点以上の場合...音嫌悪症状を示唆するカットオフ得点として扱われる»
7. единое надёжное измерение: **yes** — Same online instrument and cut-off for all; alpha reported — Page 3, Table 1 — «Symptom 13.5 5.3 0 28 .84»
8. статистика (числитель и знаменатель): **no** — No prevalence reported for this sample; only an approximate figure can be derived from rounded combined and student percentages — Page 4; Abstract — «estimated at 54 % ... 音嫌悪症の割合は41.4 % であった。»
9. отклик: **unclear** — Number invited by the survey company not reported — Page 2, Methods — «民間の調査会社に参加者の募集を委託し»

Правки:
- 

Проверено: да
---

## ST078 · Vitoratou 2022 · Frontiers in psychology

Основной отчёт R0985: [текст](../../fulltext/text/R0985.txt) — «Evidence of Cross-Cultural Consistency of the S-Five Model for Misophonia: Psychometric Conclusions Emerging From the Mandarin Version.» — [DOI](https://doi.org/10.3389/fpsyg.2022.879881)
Приложен R0984: [текст](../../fulltext/text/R0984.txt) · [PDF](../../fulltext/pdf/R0984.pdf) — «Evidence of cross-cultural consistency in a multidimensional model for the severity of misophonia and trigger burden: p…»
Связь отчётов: Mandarin S-Five sample (n = 256): PsyArXiv preprint R0984 and article R0985
Расхождения в тексте: Sex: 186 of 256 females is 72.7%, but the text prints 71%; males 66/256 = 25.8%, printed 25%. The study reports one self-identification count: 41 (16%) in Descriptive Indices. The validity analysis instead compares n=33 self-identified with n=159 not self-identified. Mean S-Five total is 98.1 (SD 50.9), above the later S-Five cut-off of 87, but no count at that cut-off is reported. No cases are reported for the A-MISO-S or MQ (including MSS >=7); these measures were completed by subsamples only (A-MISO-S n=125; MQ n=118). The preprint R0984 matches the main report on n, demographics and the self-identification figure. It does not mention the removal of 60 responses or the n=251 for age. Ethics references differ inside R0985: RESCM-19/20-11,826 in Recruitment and HR-19/20-17173 in the Ethics Statement.
Заметка ИИ: There is one eligible sample. Its only prevalence-type estimate is the ad hoc self-identification (41/256, L1). The psychometric scales (S-Five, A-MISO-S, MQ) are not used to report any case counts.

### ST078-1 · Online snowball sample of Mandarin-speaking adults, China, n=256 (S-Five Mandarin validation)
Отчёты: R0985 (main); R0984

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-identified misophonia (yes/no item) | **L1** | **41 / 256** | 16.0 | Results, Descriptive Indices | «In terms of misophonia, 85 participants (33%) stated they were aware of the term misophonia and 41 (16%) identified as having misophonia.» |

- E1: источник порога: study's own; правило: adhoc row; L1 self-identified misophonia (only definition available; no scale-based count reported); у авторов: «identified as having misophonia»; главная у авторов: no; период: NR; заметка: Denominator assumed to be the full sample of 256 (41/256 = 16.0%). The validity analysis compares n=33 self-identified with n=159 not self-identified (192 in total), so the item denominator or count may differ. No definition of misophonia shown to participants was reported. The study is a psychomet…

**Ключевые поля выборки:**
- **n_analysed: 256** — Results, Descriptive Indices — «The sample (n = 256) consisted of 186 females (71%) and 66 males (25%)»
- **population: gp_other** — Discussion (limitations) — «the sample collected cannot be considered a representative sample of the Chinese population ... our data come from the general population»
- **sampling: snowball** — Materials and Methods, Recruitment — «Recruitment was done using a snowball sampling technique via social media in China»

**Остальные поля:**
- clinical_group: NA — NA
- country: CHN — Results, Descriptive Indices — «All participants were born in China and lived there at the time of completing the survey.»
- setting: online (social media snowball: WeChat Moment, Weibo, Douban, Twitter, Reddit, King's College London recruitment circular) — Materials and Methods, Recruitment — «Recruitment was done using a snowball sampling technique via social media in China (Wechat Moment, Weibo & Douban), as well as via Twitter, Reddit, and the For…»
- data_years: 2021 — Materials and Methods, Recruitment — «Data collection took part between January and September 2021, including the retest study.»
- design: validation study — Discussion — «The purpose of this study was to evaluate the psychometric properties of the Mandarin version of the S-Five questionnaire.»
- topic_disclosed: NR — Materials and Methods, Recruitment — «A participants' information sheet was available at the beginning of the survey and consent was granted before completing the questionnaires online»
- inclusion_exclusion: Aged 18+ and fluent in Mandarin; excluded self-disclosed severe learning or intellectual disability; responses failing attention checks or missing >3 of 25 S-Five items removed (n=60) — Materials and Methods, Recruitment; Measures — «Inclusion criteria followed being aged 18 years and over and fluent in Mandarin. Exclusion criteria were the presence of a severe learning or intellectual disa…»
- n_invited: NR — NA
- n_responded: 316 — Materials and Methods, Measures; Results, Descriptive Indic… — «Responses which did not meet the requirement of the attention check questions or failed to respond to more than 3 of the 25 S-Five items were removed to ensure…»
- response_rate: NR — NA
- age_mean: 25 — Results, Descriptive Indices — «with a mean age of 25 years (sd = 6.5; n = 251)»
- age_sd: 6.5 — Results, Descriptive Indices — «with a mean age of 25 years (sd = 6.5; n = 251)»
- age_min: NR — Materials and Methods, Recruitment — «Inclusion criteria followed being aged 18 years and over»
- age_max: NR — NA
- age_group: adults — Materials and Methods, Recruitment — «Inclusion criteria followed being aged 18 years and over and fluent in Mandarin.»
- pct_female: 72.7 — Results, Descriptive Indices — «The sample (n = 256) consisted of 186 females (71%) and 66 males (25%)»
- informant: self — Materials and Methods, Measures — «The following self-report questionnaires were also included.»
- mode: online — Materials and Methods, Recruitment — «consent was granted before completing the questionnaires online»
- instruments: S-Five (Mandarin, translated by research team; validated in this study); S-Five-T trigger checklist (Mandarin); A-MISO-S (Mandarin, translated by research team, self-report); MQ (Mandarin, translated by research team); self-identification item (identifies as having misophonia) — Materials and Methods, Measures; Translation — «Participants were asked whether they were aware of the term misophonia and whether they identified as having misophonia. ... Using the same method, the A-MISO-…»
- instrument_validated_in_language: no — Materials and Methods, Measures — «Participants were asked whether they were aware of the term misophonia and whether they identified as having misophonia.»
- pub_status: journal — Header — «Year: 2022; venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2022.879881»
- language: English — Full text — «Evidence of Cross-Cultural Consistency of the S-Five Model for Misophonia: Psychometric Conclusions Emerging From the Mandarin Version»
- funding_coi: NIHR Maudsley Biomedical Research Centre (SV, CH); Wellcome Trust grant 102176/B/13/Z (JG); authors declare no conflict of interest — Funding; Conflict of Interest — «This research was funded in whole, or in part, by the Wellcome Trust (JG; grant number 102176/B/13/Z). ... The authors declare that the research was conducted …»
- notes: n_responded 316 is derived: 256 analysed + 60 removed (attention check / >3 S-Five items missing); the number who started the survey may be higher. pct_female derived as 186/256 = 72.7%; paper prints 71%. Age n = 251. 63% were students. Recruitment partly through King's College London circular, Twitter and Reddit, but all participants born and living in China. Only prevalence-type figure: self-identified misophonia 41 (16%). No count at S-Five >=87, A-MISO-S or MQ cut-offs is reported (A-MISO-S n=125, MQ n=118 completers). Preprint R0984 reports the same sample and does not mention the 60 rem…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is the Chinese population; the frame was social-media users reached by snowball, not a frame covering that population. — Materials and Methods, Recruitment — «Recruitment was done using a snowball sampling technique via social media in China (Wechat Moment, Weibo & Douban)»
2. способ отбора: **no** — Snowball, volunteer opt-in sampling. — Materials and Methods, Recruitment — «Recruitment was done using a snowball sampling technique via social media»
3. размер выборки: **no** — n = 256 < 385. — Results, Descriptive Indices — «The sample (n = 256)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are all reported. — Results, Descriptive Indices; Recruitment — «186 females (71%) and 66 males (25%), with a mean age of 25 years ... All participants were born in China ... between January and September 2021»
5. охват (пропуски): **unclear** — Missingness of the self-identification item not reported; the t-test uses only 33 + 159 = 192 participants, against 41 self-identified out of 256. — Results, S-Five Scores: Reliability and Validity — «S-Five total (n = 33) mean = 146.12, sd = 41.0 versus S-Five total (n = 159) mean = 88.65»
6. валидность определения случая: **no** — The only prevalence estimate rests on an ad hoc self-identification item (L1). — Materials and Methods, Measures — «Participants were asked whether they were aware of the term misophonia and whether they identified as having misophonia.»
7. единое надёжное измерение: **unclear** — Same online item for everyone, but no reliability is reported for the self-identification item. — Materials and Methods, Measures — «whether they identified as having misophonia»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are given (41 of 256, 16%), so a CI can be calculated; no CI is reported. There is a discrepancy with the n=33 group in the t-test. — Results, Descriptive Indices — «41 (16%) identified as having misophonia»
9. отклик: **no** — Open online snowball survey with no denominator of invited people and no handling of non-response. — Materials and Methods, Recruitment — «Recruitment was done using a snowball sampling technique via social media»

Правки:
- 

Проверено: да
---

## ST079 · Yektatalab 2022 · International journal of community based nursing and midwifery

Основной отчёт R1001: [текст](../../fulltext/text/R1001.txt) — «The Prevalence of Misophonia and Its Relationship with Obsessive-compulsive Disorder, Anxiety, and Depression in Undergraduate Students of Shiraz University of…» — [DOI](https://doi.org/10.30476/ijcbnm.2022.92902.1888)
Расхождения в тексте: The prevalence figures agree across Abstract, Results and Table 2: 93/390 (23.8%). In Table 3 the p-values are printed as 0.05, 0.05 and 0.008, but the Abstract reports P<0.001 for all three associations. The Table 3 p-values come from chi-square tests and the Abstract's P<0.001 may come from Spearman correlations (Table 4). Either way, the p-values are inconsistent across the paper. This does not affect the prevalence estimate. The Abstract says 'A score of 7 or higher is considered as misophonia' without naming the scale. Methods tie it to the 1-15 severity item. Field counts in Table 1 match the planned allocation (Nursing 102, Lab 74, etc.).
Заметка ИИ: Draft for reviewer check. topic_disclosed is coded yes because participants were told the study objectives, and those objectives name misophonia. The invitation wording itself is not quoted in the paper. Sampling is coded probability (stratified, then systematic within classes), but the paper does not report the number of students contacted or refusals.

### ST079-1 · Undergraduate students, Shiraz University of Medical Sciences (nursing-midwifery, paramedical, health faculties), IRN, n=390
Отчёты: R1001 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **93 / 390** | 23.8 | Table 2; Abstract | «Of the 390 participants in the study, 93 (23.8%) had experienced misophonia.» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2, recommended); у авторов: «misophonia (significant clinical signs)»; главная у авторов: yes; период: current; заметка: Threshold applied to the final MQ severity item (1-15). No estimates by sex or age band are reported.

**Ключевые поля выборки:**
- **n_analysed: 390** — Table 2 — «No | 297 (76.2) Yes | 93 (23.8)»
- **population: university_students** — Methods — «Nursing, operating room, Anesthesia, Midwifery, Emergency Medical Technician (EMT), paramedical sciences (Laboratory sciences, Radiology) and Health (Health, Nutrition)»
- **sampling: probability** — Methods — «the required number of students in each field and each class was determined using relative stratified sampling, and in the next step in each class, the students were selected using a systematic method.»

**Остальные поля:**
- clinical_group: NA — NA
- country: IRN — Title; Methods — «undergraduate students of Shiraz University of Medical Sciences»
- setting: university (Nursing-Midwifery, Paramedical Sciences and Health faculties, Shiraz University of Medical Sciences) — Methods — «undergraduate students of Nursing-Midwifery ... paramedical sciences ... and Health ... at Shiraz University of Medical Sciences in October 2020»
- data_years: 2020 — Abstract; Methods — «an analytical descriptive study conducted in October 2020»
- design: cross-sectional — Methods — «This is a cross-sectional descriptive study with correlational design.»
- topic_disclosed: yes — Methods — «After contacting them, we explained the objectives of the study and after accepting the participation in the study, they signed the consent forms.»
- inclusion_exclusion: Undergraduates of nursing-midwifery, paramedical and health faculties who were willing, gave consent, and had a smartphone, internet and WhatsApp; excluded: self-reported hearing-related disease — Methods — «The exclusion criterion was suffering from diseases related to hearing based on the person's statement in the questionnaire.»
- n_invited: NR — Methods — «the total number of students of Nursing-Midwifery, Paramedical Sciences and Health Faculties at the undergraduate level was 1190»
- n_responded: 390 — Results; Table 1 — «This study was performed on 390 students»
- response_rate: NR — Methods — «given a 10% drop, 390 students were finally considered as the sample in this study.»
- age_mean: NR — Table 1 — «itincluded data on age, gender, marital status»
- age_sd: NR — Table 1
- age_min: NR — Table 1
- age_max: NR — Table 1
- age_group: adults — Methods — «undergraduate students»
- pct_female: 58.2 — Table 1 — «Female | 227 (58.2)»
- informant: self — Methods — «The misophonia questionnaire is a self-report tool developed by Monica Wu.»
- mode: online — Methods — «the link of the online questionnaire was sent to the student through WhatsApp.»
- instruments: Misophonia Questionnaire (MQ; Wu et al. 2014), Persian version — Methods — «In Iran, for the first time, the psychometric properties of the sound instrument questionnaire were studied by Mehrabizade Honarmand and Roshani (2020) on 350 …»
- instrument_validated_in_language: yes — Methods (ref 20) — «psychometric properties ... were studied by Mehrabizade Honarmand and Roshani (2020) on 350 students. Reliability of this instrument was measured using Cronbac…»
- pub_status: journal — Header — «International journal of community based nursing and midwifery»
- language: English — Full text — «The Prevalence of Misophonia and Its Relationship with Obsessive-compulsive Disorder, Anxiety, and Depression»
- funding_coi: Shiraz University of Medical Sciences grant 20828 (thesis of A. Mohammadi); no conflict of interest declared — Acknowledgement; Conflict of Interest — «supported by Shiraz University of Medical Sciences under grant (20828) ... None declared.»
- notes: Age not reported. Allocation was proportional by field and year, with systematic selection within classes. Participation was consent-based, and the number of students contacted or declining is not reported. The planned sample of 390 equals the achieved sample. The frame was limited to three faculties; the Faculty of Rehabilitation (and other faculties) refused to cooperate. Participants studied nursing and allied health, not medicine, so population is coded university_students. The Abstract's 'score of 7 or higher' refers to the MQ Severity Scale item (1-15), per Methods.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The target is SUMS undergraduates, but the frame covered only three faculties, and some faculties refused to cooperate. — Methods — «However, some disciplines and faculties, such as the Faculty of Rehabilitation, were not willing to cooperate.»
2. способ отбора: **yes** — Proportional stratified sampling with systematic selection within classes from faculty lists. — Methods — «relative stratified sampling, and in the next step in each class, the students were selected using a systematic method.»
3. размер выборки: **yes** — n=390 >= 385. — Results — «This study was performed on 390 students»
4. описание выборки и условий: **unclear** — Sex, setting, country and dates are reported; age is not. — Table 1; Methods — «Male | 163 (41.8) Female | 227 (58.2)»
5. охват (пропуски): **yes** — Table 2 classifies all 390 participants for misophonia; no missing data reported. — Table 2 — «No | 297 (76.2) Yes | 93 (23.8)»
6. валидность определения случая: **yes** — MQ Severity Scale >=7, in a Persian version with published validation. — Methods — «A score of 7 or higher indicates significant clinical signs.»
7. единое надёжное измерение: **yes** — Same online MQ and threshold for everyone; reliability is reported from the Persian validation source. — Methods — «The reliability coefficient was 0.79 for the subspecies of misophonia symptoms, 0.66 for the subscale of excitement due to misophonia, and 0.73 for the total s…»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (93/390); CI calculable. — Table 2 — «Yes | 93 (23.8)»
9. отклик: **unclear** — Number contacted and refusals not reported, so the response rate is unknown. — Methods — «Then, all the samples were contacted by phone or SMS.»

Правки:
- 

Проверено: да
---

## ST080 · Beukes 2021 · International journal of clinical practice

Основной отчёт R1018: [текст](../../fulltext/text/R1018.txt) — «Investigating tinnitus subgroups based on hearing-related difficulties.» — [DOI](https://doi.org/10.1111/ijcp.14684)
Расхождения в тексте: The female percentage differs between sources: the abstract says 50% (n=1,457), the Results text says 49% and Table 1 says 48.9%. Table 1 (48.9) is used. In Table 1 the row 'hearing loss, hyperacusis and misophonia' prints 54 (6.7), but 54/795 = 6.8%. The Cluster 2 combination rows add up exactly to 795 (298+26+353+18+46+54). Hearing aid figures do not agree: Table 1 gives 1,230 overall, but the clusters give 0 + 345 + 600 = 945. The text says 364 hearing aid wearers reported no hearing loss, yet Cluster 1 (tinnitus only) shows 0 wearers, and 'hearing aid wearer' is still a significant predictor for Cluster 1 in Table 2. This makes Table 1's cluster columns less reliable, although the misophonia rows add up consistently. The introduction gives 1-2% misophonia among people with tinnitus, from Jager 2020. That is a background citation, not this study's data.
Заметка ИИ: The authors give no misophonia prevalence. The estimates are worked out from the Table 1 rows that combine misophonia with hearing loss and/or hyperacusis. The wording of the misophonia question is not reported. Population is coded clinical (tinnitus) because the eligibility criterion was having tinnitus and recruitment went through tinnitus patient organizations and clinics. topic_disclosed = no because the survey was presented as being about tinnitus during COVID-19 and did not name misophonia. A reviewer may want to reconsider this, since tinnitus is a hearing condition. This survey datase…

### ST080-1 · International online tinnitus survey (COVID-19), adults with tinnitus, n=2,980
Отчёты: R1018 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-reported presence of misophonia (yes/no item) | **L1** | **144 / 2980** | 4.8 | Table 1 | «Presence of misophonia only 0 (0) 26 (3.3) 0 (0) ... hearing loss and misophonia 0 (0) 18 (2.3) ... hyperacusis and misophonia 0 (0) 46 (5.8) ... hearing loss, hyperacusis and misophonia 0 (0) 54 (6.7)» |
| E2 | self-reported hearing loss | adhoc · self-reported presence of misophonia (yes/no item) | **L1** | **72 / 1304** | 5.5 | Table 1 | «Presence of hearing loss only 0 (0) 0 (0) 879 (100) ... hearing loss and hyperacusis 0 (0) 353 (44.4) ... hearing loss and misophonia 0 (0) 18 (2.3) ... hearing loss, hyperacusis and misophonia 0 (0) 54 (6.7)» |
| E3 | self-reported hyperacusis | adhoc · self-reported presence of misophonia (yes/no item) | **L1** | **100 / 751** | 13.3 | Table 1 | «Presence of hyperacusis only 0 (0) 298 (37.5) 0 (0) ... hearing loss and hyperacusis 0 (0) 353 (44.4) ... hyperacusis and misophonia 0 (0) 46 (5.8) ... hearing loss, hyperacusis and misophonia 0 (0) 54 (6.7)» |

- E1: источник порога: study's own; правило: adhoc row; self-identified misophonia (L1); G1 sum of combination categories; у авторов: «Presence of misophonia»; главная у авторов: no; период: NR; **расчёт: 26 + 18 + 46 + 54 = 144 (Cluster 2 misophonia rows, Table 1; Clusters 1 and 3 = 0); denominator overall N = 2,980; 4.8%**; заметка: Item wording not reported. Denominator assumes non-endorsement = absence; missing data on the item not reported.
- E2: источник порога: study's own; правило: adhoc row; self-identified misophonia (L1); G1 sum of combination categories; у авторов: «Presence of misophonia»; главная у авторов: no; период: NR; **расчёт: Cases 18 + 54 = 72; n with hearing loss = 879 (Cluster 3) + 353 + 18 + 54 (Cluster 2) = 1,304**; заметка: Subgroup defined by self-reported hearing loss within the tinnitus sample; derived from mutually exclusive combination rows.
- E3: источник порога: study's own; правило: adhoc row; self-identified misophonia (L1); G1 sum of combination categories; у авторов: «Presence of misophonia»; главная у авторов: no; период: NR; **расчёт: Cases 46 + 54 = 100; n with hyperacusis = 298 + 353 + 46 + 54 = 751 (Cluster 2; none in Clusters 1 and 3)**; заметка: Subgroup defined by self-reported hyperacusis within the tinnitus sample; derived from mutually exclusive combination rows.

**Ключевые поля выборки:**
- **n_analysed: 2980** — Page 10, Results; Table 1 — «Overall N= 2,980»
- **population: clinical** — Page 8, Data Collection — «Eligibility criteria included adults aged 18 years and older reporting the presence of tinnitus.»
- **sampling: convenience** — Page 8, Data Collection — «distributed via patient organizations' social media outlets (i.e., Twitter, LinkedIn, and Facebook) and tinnitus clinics»

**Остальные поля:**
- clinical_group: tinnitus — Page 8, Data Collection — «adults aged 18 years and older reporting the presence of tinnitus»
- country: MULTI: USA, GBR, SWE, BEL, NLD, others (by region: North America 50.2%, mainland Europe 23.7%, UK 23.0%; individual countries NR) — Page 10, Results; Table 1; Acknowledgments p.21 — «Respondents were predominantly from North America (n= 1,497; 50%), mainland Europe (n= 707; 24%) or the United Kingdom (n= 684; 23%).»
- setting: online survey distributed via patient organizations' social media and tinnitus clinics (worldwide) — Page 8, Data Collection — «recruitment targeted both clinical and non-clinical tinnitus populations and was distributed via patient organizations' social media outlets (i.e., Twitter, Li…»
- data_years: 2020 — Page 8, Study Design — «survey distributed world-wide to investigate tinnitus experiences during the COVID-19 pandemic in May-June 2020»
- design: cross-sectional — Page 8, Study Design — «An exploratory cross-sectional survey study design was used.»
- topic_disclosed: no — Page 8, Study Design — «a survey distributed world-wide to investigate tinnitus experiences during the COVID-19 pandemic»
- inclusion_exclusion: Adults >=18 reporting tinnitus; excluded if no tinnitus or tinnitus questions not completed — Page 8 Data Collection; Page 9 Data Analysis — «Cases were initially removed if they did not meet study eligibility due to not having tinnitus or not completing the questions related to tinnitus on the quest…»
- n_invited: NR — NA — «NR»
- n_responded: 3400 — Page 10, Results — «There were 3,400 respondents of which 2,980 were eligible for inclusion for this analysis.»
- response_rate: NR — NA — «NR»
- age_mean: 58 — Page 10, Results; Table 1 — «The mean age of all respondents was 58 years (SD= 14.7)»
- age_sd: 14.7 — Page 10, Results — «The mean age of all respondents was 58 years (SD= 14.7)»
- age_min: 18 — Page 8, Data Collection (eligibility criterion, not observe… — «adults aged 18 years and older»
- age_max: NR — NA — «NR»
- age_group: adults — Page 8, Data Collection — «adults aged 18 years and older reporting the presence of tinnitus»
- pct_female: 48.9 — Table 1 — «Female 1,457 (48.9)»
- informant: self — Page 9, Data Collection — «the following self-reported information was gathered»
- mode: online — Page 8, Data Collection — «The survey was distributed online via Qualtrics.»
- instruments: Ad hoc self-report item on presence/absence of misophonia (wording not given); survey in English, Dutch, Portuguese, Swedish, German, Brazilian-Portuguese — Page 8-9, Data Collection — «The presence or absence of other hearing-related difficulties (e.g., hearing loss, hyperacusis, and/or misophonia).»
- instrument_validated_in_language: no — Page 9, Data Collection — «The presence or absence of other hearing-related difficulties (e.g., hearing loss, hyperacusis, and/or misophonia).»
- pub_status: journal — Header — «International journal of clinical practice; DOI: 10.1111/ijcp.14684»
- language: English — Full text — «Investigating tinnitus subgroups based on hearing-related difficulties»
- funding_coi: Partly funded by NIDCD/NIH R21DC017214 (VM) and EU Horizon 2020 Marie Sklodowska-Curie 722046 (ML); no conflicts declared — Page 22, Funding; Conflicts of interest — «This work is partly funded by the National Institute on Deafness and Other Communication Disorders (NIDCD) ... The authors declare that the research was conduc…»
- notes: Misophonia is a side variable in a tinnitus cluster-analysis study. The authors give no misophonia prevalence; it is worked out from the Table 1 combination rows (all misophonia cases are in Cluster 2; Clusters 1 and 3 have 0). The wording of the misophonia question and any definition are not reported. Same survey dataset as Beukes et al. 2020, Front Public Health 8:592878 (ref 27): check overlap with any other included report of this survey. The denominator assumes that not endorsing the item means absence; missing data on the item are not reported. The estimates also include about 23% UK re…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is adults with tinnitus (globally); frame was patient-organization social media and tinnitus clinics, covering only part of it — Page 8, Data Collection; Page 19-20, Limitations — «distributed via patient organizations' social media outlets (i.e., Twitter, LinkedIn, and Facebook) and tinnitus clinics»
2. способ отбора: **no** — Volunteer opt-in online survey (convenience) — Page 8, Data Collection — «The survey was distributed online via Qualtrics.»
3. размер выборки: **yes** — n = 2,980 >= 139 for a clinical sample — Page 10, Results — «2,980 were eligible for inclusion for this analysis»
4. описание выборки и условий: **yes** — Age, sex, setting, regions/countries and dates reported — Page 8; Page 10; Table 1 — «in May-June 2020 ... The mean age of all respondents was 58 years (SD= 14.7), and 49% (n= 1,457) were females»
5. охват (пропуски): **unclear** — Missing data on the misophonia item not reported; only exclusion for missing tinnitus questions described — Page 9, Data Analysis — «not completing the questions related to tinnitus on the questionnaire»
6. валидность определения случая: **no** — Ad hoc self-reported presence of misophonia (yes/no), no validated instrument — Page 9; Page 20, Limitations — «Findings are based only on self-reported survey data without any clinical data»
7. единое надёжное измерение: **unclear** — Same online item for all but in six language versions; no reliability reported — Page 8, Data Collection — «The survey was available in English, Dutch, Portuguese, Swedish, German, and Brazilian-Portuguese»
8. статистика (числитель и знаменатель): **yes** — Numerator (sum of Table 1 misophonia rows) and denominator (2,980) traceable; CI calculable, though authors give no misophonia prevalence — Table 1 — «Presence of misophonia only 26 (3.3) ... hearing loss and misophonia 18 (2.3) ... hyperacusis and misophonia 46 (5.8) ... hearing loss, hyperacusis and misopho…»
9. отклик: **no** — Open online survey with no denominator of invited people; non-response not handled — Page 10, Results — «There were 3,400 respondents of which 2,980 were eligible»

Правки:
- 

Проверено: да