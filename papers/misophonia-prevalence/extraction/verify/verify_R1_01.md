# Проверка выписывания — файл 1 из 10

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

## ST001 · Black 2026 · British journal of psychology (London, England : 1953)

Основной отчёт R0031: [текст](../../fulltext/text/R0031.txt) — «Misophonia symptom severity is linked to impaired flexibility and heightened rumination.» — [DOI](https://doi.org/10.1111/bjop.70025)
Приложен R0267: [текст](../../fulltext/text/R0267.txt) · [PDF](../../fulltext/pdf/R0267.pdf) — «Misophonia Symptoms Severity is Attributed to Impaired Flexibility and Heightened Rumination»
Связь отчётов: bioRxiv preprint (R0267) and article (R0031): same 140 adults, 128 from Prolific (Black et al.)
Не выписано ИИ: 12 volunteers recruited through misophonia newsletters (soQuiet Misophonia Research Pool, Misophonia International): E1, recruited because of interest in misophonia; 11/12 (91.67%) scored S-Five >=87. The whole-sample estimate (35/140 = 25%) and the Table 1 sex split (female 18/49, male 17/91) are not extracted because they mix in this E1 group.
Расхождения в тексте: The counts agree: 24 Prolific + 11 volunteers = 35 of 140; Table 1 gives 18+17 = 35 significant and 31+74 = 105 non-significant; 49 female + 91 male = 140. Prolific: 142 attempted MAFT − 128 analysed = 14 excluded; volunteers: 21 − 12 = 9; 14 + 9 = 23 = 20 + 1 + 2 exclusions. The main report says 163 'completed' the MAFT, while the R0267 Figure 3 legend says 'attempted' (157 Prolific and 42 volunteers recruited). The cut-off citation is inconsistent: Materials attributes the ROC cut-off to Vitoratou et al. 2021, other sections to Vitoratou et al. 2023. The R0267 text says '>87' for the higher group, but its Figure 6 and the main report say >=87. The Table 1 note says 'p ≤ .05' in the article and 'p ≥ 0.05' in the preprint.
Заметка ИИ: Only the Prolific subsample was extracted. Funding comes from the preprint (R0267) because the article text supplied has no funding section. The main report has no page markers, so locations are given by section.

### ST001-1 · Prolific online panel adults, country NR, n=128 (Black et al.)
Отчёты: R0031 (main); R0267

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | S-Five · S-Five total >=87 | **L2** | **24 / 128** | 18.8 | Participants section (after Table 1); R0267 p.7 | «Specifically, 18.75% of Prolific participants (N = 24) endorsed significant misophonia.» |

- E1: источник порога: validation paper; правило: S-Five row; L2 >=87; у авторов: «significant misophonia»; главная у авторов: no; период: NR; заметка: 24/128 = 18.75%, which matches the reported percentage. Primary analyses were continuous; the dichotomy was used for comparison. No sex or age breakdown for the Prolific subsample (Table 1 sex split includes the volunteers).

**Ключевые поля выборки:**
- **n_analysed: 128** — Participants — «Of those, 128 participants were recruited from Prolific»
- **population: gp_other** — Participants — «128 participants were recruited from Prolific (www.prolific.com), an online study participant pool»
- **sampling: convenience** — Procedure — «We first recruited participants through Prolific (www.prolific.com), an academic research‐focused crowdsourcing platform.»

**Остальные поля:**
- clinical_group: NA — NA
- country: NR — Procedure — «Eligibility criteria as screened using the demographic pre‐screen feature on Prolific included age of 18–45 ... fluency in English»
- setting: online panel (Prolific) — Participants — «128 participants were recruited from Prolific (www.prolific.com), an online study participant pool»
- data_years: NR — Method — «Committee for Protection of Human Subjects at the University of California, Berkeley (CPHS protocol ID 2024‐01‐17038)»
- design: cross-sectional — Procedure — «participants were redirected from Qualtrics to complete the Memory and Affective Flexibility Task ... and then completed a battery of questionnaires (e.g. S‐Fi…»
- topic_disclosed: NR — Procedure — «Eligible participants based on the Prolific pre‐screen filter were shown a study advert briefly describing the procedures»
- inclusion_exclusion: Age 18-45; no hearing loss/difficulties; no cognitive impairment/dementia; normal or corrected vision; English fluency; willing to see distressing images; no current psychiatric diagnosis (stated in advert, not screened). Excluded: incomplete MAFT, multiple MAFT attempts, incomplete questionnaires. — Procedure — «included age of 18–45 ... no hearing loss or hearing difficulties; absence of cognitive impairment or dementia, normal or corrected‐to‐normal vision; fluency i…»
- n_invited: NR — Procedure — «Eligible participants based on the Prolific pre‐screen filter were shown a study advert»
- n_responded: 157 — R0267, p.13, Figure 3 legend — «199 subjects were initially recruited for the study. Of 157 Prolific participants, 142 attempted the MAFT»
- response_rate: NR — Procedure — «A total of 199 participants were recruited for the study, of whom 163 completed the MAFT: 142 from Prolific and 21 from outreach to newsletters.»
- age_mean: NR — Participants — «The sample comprised 140 participants (mean age = 29.98 ± 6.72 years; 49 females, 91 males)»
- age_sd: NR — Participants — «mean age = 29.98 ± 6.72 years»
- age_min: NR — Procedure — «Eligibility criteria ... included age of 18–45»
- age_max: NR — Procedure — «Eligibility criteria ... included age of 18–45»
- age_group: adults — Procedure — «Eligibility criteria ... included age of 18–45»
- pct_female: NR — Participants — «The sample comprised 140 participants (mean age = 29.98 ± 6.72 years; 49 females, 91 males)»
- informant: self — Procedure — «reported their age and gender, and then completed a battery of questionnaires (e.g. S‐Five ...)»
- mode: online — Procedure — «All participants were directed via URL to Qualtrics (www.qualtrics.com) to provide informed consent.»
- instruments: S-Five, 25 items (English); SSSQ 6-item version including item 4 (misophonia item) (English; no misophonia prevalence reported from it) — Materials: S-Five; SSSQ — «Misophonia symptom severity was assessed using the 25‐item S‐Five ... the 6‐item version showed acceptable internal consistency (α = .77) as well as when remov…»
- instrument_validated_in_language: yes — Materials: S-Five — «A score of 87 or above indicates significant misophonia as suggested by ROC analysis (Vitoratou et al., 2021). The S‐Five has previously exhibited good interna…»
- pub_status: journal — Header: venue — «British journal of psychology (London, England : 1953); DOI: 10.1111/bjop.70025»
- language: English — Full text — «Misophonia symptom severity is linked to impaired flexibility and heightened rumination»
- funding_coi: UC Berkeley Undergraduate Research Apprentice Program; SoQuiet Misophonia Student Research Grant; ME and HA supported by R&D fund of Hashir International Specialist Clinics (misophonia/tinnitus/hyperacusis clinic). Authors declare no conflict of interest. — R0267, p.26-27, Acknowledgement; Declaration of Conflicting… — «funded by the University of California, Berkeley Undergraduate Research Apprentice Program (URAP) and the SoQuiet Misophonia Student Research Grant ... The aut…»
- notes: Age, sex, country and dates of data collection are not reported for the Prolific subsample. Whole-sample values (n = 140, including 12 E1 volunteers): age 29.98 ± 6.72, 49 female / 91 male. Age eligibility 18-45. Same 140 participants as the bioRxiv preprint R0267. Payment in USD, with 2 pilot participants paid in GBP; country not stated. The 18.75% estimate is for Prolific only and is not affected by the volunteers. The S-Five cut-off was derived in the Vitoratou 2023 UK sample.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is Prolific users meeting pre-screen filters (18-45, no hearing/psychiatric problems), while the comparison is with the general population; country not stated. — Procedure — «Eligibility criteria as screened using the demographic pre‐screen feature on Prolific included age of 18–45»
2. способ отбора: **no** — Opt-in online non-probability panel. — Procedure — «We first recruited participants through Prolific (www.prolific.com), an academic research‐focused crowdsourcing platform.»
3. размер выборки: **no** — n = 128 < 385. — Participants — «128 participants were recruited from Prolific»
4. описание выборки и условий: **no** — Age and sex reported only for the combined 140; country and dates of data collection not reported. — Participants — «The sample comprised 140 participants (mean age = 29.98 ± 6.72 years; 49 females, 91 males)»
5. охват (пропуски): **unclear** — 157 Prolific recruited, 142 attempted MAFT, 128 analysed; 14/142 (9.9%) or 29/157 (18.5%) lost, depending on how respondents are counted; exclusions mostly before S-Five was given; not handled. — R0267, p.13, Figure 3 legend — «Of 157 Prolific participants, 142 attempted the MAFT ... exclusions included incomplete MAFT (N = 20), multiple attempts (N = 1), and incomplete questionnaires…»
6. валидность определения случая: **yes** — S-Five >= 87, the interview-anchored ROC cut-off, in the original English version. — Results/Participants — «Based on the recommended cut‐off score of 87 or above on the S‐Five (Vitoratou et al., 2023)»
7. единое надёжное измерение: **yes** — Same online S-Five and threshold for everyone; alpha reported in the study sample. — Materials: S-Five — «In the current study, the S‐Five showed excellent internal consistency (α = .96).»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (24/128), so a CI can be calculated; no weighting needed. — Participants — «Specifically, 18.75% of Prolific participants (N = 24) endorsed significant misophonia.»
9. отклик: **no** — Open online panel with no denominator of invited people; no non-response handling. — Procedure — «Eligible participants based on the Prolific pre‐screen filter were shown a study advert»

Правки:
- 

Проверено: да
---

## ST002 · Bozkurt 2026 · kulak burun boğaz ve baş boyun cerrahisi dergisi

Основной отчёт R0035: [текст](../../fulltext/text/R0035.txt) · [PDF](../../fulltext/pdf/R0035.pdf) — «Decreased Sound Tolerance in Older Adults: The Relationship Between Depression and Auditory Sensitivities» — [DOI](https://doi.org/10.24179/kbbbbc.2025-113232)
Расхождения в тексте: The prevalence matches between text (page 4) and Table 2: 29/67 (43.3%). Absent 38 + present 29 = 67. The abstract says participants with tinnitus "exhibited higher scores across all DSTS-S subscales", but Table 5 shows a lower misophonia mean with tinnitus (4.97 vs 5.76) and only a higher median (2 vs 1, p=0.894). Table 5's footnote lists a Kruskal-Wallis test, but only Mann-Whitney results are flagged. The Methods call DSTS-S misophonia >=4 'clinically significant', but this is the developers' sensitivity-oriented screening cut-off (Table 1 DSTS-S row).
Заметка ИИ: One eligible sample: older adults (65-84) in Türkiye, n=67. There is one misophonia estimate, DSTS-S misophonia >=4, 29/67 (L1). The recruitment source and sampling method are not reported, so the population and setting codes need reviewer checking.

### ST002-1 · Older adults aged 65-84 with audiological assessment, Türkiye, n=67
Отчёты: R0035 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSTS-S · DSTS-S misophonia subscale >=4 | **L1** | **29 / 67** | 43.3 | Page 4, Table 2 and Results text | «Hyperacusis symptoms were observed in 42 (62.7%) participants, phonophobia in 31 (46.3%) participants, and misophonia in 29 (43.3%) participants.» |

- E1: источник порога: developer paper; правило: DSTS-S row; L1 >=4 (developers' screening cut-off); у авторов: «clinically significant; misophonia present»; главная у авторов: yes; период: NR; заметка: The cut-off comes from Allusoglu & Aksoy 2022 (ref 11), the DSTS-S developers' reliability/validity paper. The authors call it 'clinically significant', but by Table 1 it is a screening cut-off (L1).

**Ключевые поля выборки:**
- **n_analysed: 67** — Page 4, Table 2 — «Misophonia 5.37±7.46 2 (0-33) Absent 38 56.7 Present 29 43.3»
- **population: other_nonclinical** — Page 2, Participants — «the age of 65 was used as the threshold for older adulthood»
- **sampling: NR** — Page 2, Participants — «An a priori power analysis indicated that a minimum of 59 participants was required to achieve sufficient statistical power, and 67 individuals were included in the study.»

**Остальные поля:**
- clinical_group: NA — Page 2, Participants — «Exclusion criteria included middle ear dysfunction; any physical condition that could hinder participation in questionnaire administration or medical evaluatio…»
- country: TUR — Page 1, affiliations; Page 2, Material and Methods — «approved by the Ethics Committee of KTO Karatay University (date: November 28, 2024; no: 2024/011)»
- setting: Not stated. Older adults had audiological testing in a soundproof room; authors are affiliated with Gülhane Training and Research Hospital (Ankara) and KTO Karatay University (Konya). The recruitment site is not reported. — Page 3, Audiological Assessment; Page 1, affiliations — «Pure-tone audiometry measurements were conducted in a soundproof room»
- data_years: 2024-2025 — Page 2, Material and Methods — «Data were gathered between December 2024 and June 2025.»
- design: cross-sectional — Page 2, Material and Methods — «This study followed a descriptive cross-sectional design»
- topic_disclosed: NR — Page 2, Participants — «67 participants aged between 65 and 84 years (X̄=72.27; SD=5.4) were included.»
- inclusion_exclusion: Inclusion: age 65 or older. Exclusion: middle ear dysfunction; a physical condition that would hinder completing the questionnaires or evaluations; a neurological or psychiatric diagnosis. — Page 2, Participants — «Exclusion criteria included middle ear dysfunction; any physical condition that could hinder participation in questionnaire administration or medical evaluatio…»
- n_invited: NR — Page 2, Participants — «67 individuals were included in the study»
- n_responded: NR — Page 2, Participants — «67 individuals were included in the study»
- response_rate: NR — Page 2, Participants — «67 individuals were included in the study»
- age_mean: 72.27 — Page 3, Results — «The mean age of the participants was 72.27±5.4 years, with ages ranging from 65 to 84.»
- age_sd: 5.4 — Page 3, Results — «The mean age of the participants was 72.27±5.4 years»
- age_min: 65 — Page 3, Results — «with ages ranging from 65 to 84»
- age_max: 84 — Page 3, Results — «with ages ranging from 65 to 84»
- age_group: adults — Page 3, Results — «with ages ranging from 65 to 84»
- pct_female: 50.7 — Page 3, Results; Page 4, Table 1 — «The sample consisted of 67 individuals, including 34 (50.7%) women and 33 (49.3%) men.»
- informant: self — Page 3, Procedure — «the Decreased Sound Tolerance Scale-Screening (DSTS-S) and the Geriatric Depression Scale (GDS) were administered to participants through face-to-face intervie…»
- mode: face-to-face interview — Page 3, Procedure — «were administered to participants through face-to-face interviews»
- instruments: DSTS-S misophonia subscale (14 items, 0-3 each). The language version is not stated; it is presumably the Turkish original of Allusoglu & Aksoy 2022. — Page 3, Decreased Sound Tolerance Assessment — «The DSTS-S consists of 31 items structured under three subscales: hyperacusis (12 items), phonophobia (5 items), and misophonia (14 items).»
- instrument_validated_in_language: yes — Page 3, Decreased Sound Tolerance Assessment; Page 8, ref 11 — «Allusoglu S, Aksoy S. The reliability and validity of decreased sound tolerance scale-screening. Braz J Otorhinolaryngol. 2022»
- pub_status: journal — Page 1, header — «Kulak Burun Boğaz ve Baş Boyun Cerrahisi Dergisi Journal of Ear Nose Throat and Head Neck Surgery ORIGINAL RESEARCH»
- language: English (abstract also in Turkish) — Page 1 — «ABS TRACT Objective: The aim of this study is to determine the prevalence of subtypes of decreased sound tolerance (DST) in older adults»
- funding_coi: No financial support reported. No conflicts of interest declared. — Page 7, Source of Finance; Conflict of Interest — «No conflicts of interest between the authors and / or family members»
- notes: How participants were recruited and where they came from is not described. The sample has high rates of hearing loss (77.6%) and tinnitus (49.3%), which suggests an audiology/clinic-based sample, but this is not stated. Population was coded other_nonclinical because no recruitment for a condition is reported; the reviewer may prefer gp_other. The DSTS-S was given by face-to-face interview but is a self-report scale, so informant = self (rule G7: the scale keeps its level). The authors call DSTS-S misophonia >=4 'clinically significant', but it is the developers' screening cut-off (L1). Tinnit…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — The target population is older adults, but the sampling frame and recruitment source are not described. — Page 2, Participants — «67 participants aged between 65 and 84 years (X̄=72.27; SD=5.4) were included.»
2. способ отбора: **unclear** — The sampling method is not described; only a power analysis is reported. — Page 2, Participants — «An a priori power analysis indicated that a minimum of 59 participants was required to achieve sufficient statistical power, and 67 individuals were included i…»
3. размер выборки: **no** — n = 67, below 385. — Page 3, Results — «The sample consisted of 67 individuals»
4. описание выборки и условий: **unclear** — Age, sex, country and dates are reported, but the setting/recruitment site is not. — Page 2-3 — «Data were gathered between December 2024 and June 2025.»
5. охват (пропуски): **yes** — All 67 participants are classified on the misophonia subscale (38 absent + 29 present = 67). — Page 4, Table 2 — «Misophonia ... Absent 38 56.7 Present 29 43.3»
6. валидность определения случая: **no** — DSTS-S misophonia >=4 is a screening cut-off chosen for sensitivity, not a clinical-significance cut-off. — Page 3, Decreased Sound Tolerance Assessment — «scores of 7 or higher for hyperacusis, 1 or higher for phonophobia, and 4 or higher for misophonia were considered clinically significant.»
7. единое надёжное измерение: **yes** — Everyone had the same instrument, mode (face-to-face) and threshold. The cited source is a reliability/validity study, but no reliability values are reported for this sample. — Page 3, Procedure; Page 8, ref 11 — «were administered to participants through face-to-face interviews»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are clear (29/67), so a CI can be calculated, although none is reported. — Page 4, Table 2 — «Present 29 43.3»
9. отклик: **unclear** — The number of people invited and the response rate are not reported. — Page 2, Participants — «67 individuals were included in the study»

Правки:
- 

Проверено: да
---

## ST003 · Chalotra 2026 · The Egyptian Journal of Otolaryngology

Основной отчёт R0044: [текст](../../fulltext/text/R0044.txt) · [PDF](../../fulltext/pdf/R0044.pdf) — «Prevalence of misophonia in a tertiary healthcare hospital in Mumbai with Marathi translated Amsterdam misophonia scale A-MISO-S» — [DOI](https://doi.org/10.1186/s43163-026-01108-1)
Расхождения в тексте: (1) Primary estimate: Table 2 gives 21 moderate + 4 severe = 25/227 = 11.01%. The Table 2 note says 10.96%, the Results say 10.9% and the Abstract/Discussion say 11%. The table counts are used. (2) Table 4 (age groups) conflicts with Table 2. Group totals 141+73+12 = 226, not 227. The Group 2 bands add up to 72 (37+24+10+1), not the printed 73. Band totals across groups do not match Table 2: subclinical 125 vs 137, mild 79 vs 65, moderate 19 vs 21, severe 2 vs 4. Age-group estimates are taken from Table 4 as printed, with the printed n. (3) The age bands are 18-40/40-60/>60 in the Methods but 18-40/41-60/>60 in Tables 3-4. (4) The sex-specific counts are derived from rounded female-to-male ratios (1.2, 0.9, 1.0). These give a unique split only for the moderate and severe bands. The overall ratio of 1.11 cannot be reproduced with any integer mild split. (5) The chi-square for sex (df=17)…
Заметка ИИ: One sample was extracted. The primary L2 estimate is A-MISO-S>=10: 25/227. The Marathi validation is in this same report, so the 'validated in language' = yes and JBI 6 = yes ratings rest on internal validation only; reviewer should confirm. The sex-specific estimates rest on rounded ratios and should be checked against Fig. 1 or dropped.

### ST003-1 · Hospital students, relatives and friends (snowball), Mumbai, India, n=227
Отчёты: R0044 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **25 / 227** | 11.0 | Page 3, Table 2; Results | «10–14 21(9.25%) Moderate 15–19 4(1.76%) Severe 20–24 0 Extreme Total 227 (100%) Note: The clinically significant misophonia is 10.96%» |
| E2 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **90 / 227** | 39.6 | Page 3, Results; Table 2 | «Among the 227 participants, 65(28.63%) exhibited mild, 21(9.25%) moderate, and 4(1.76%) severe misophonic symptoms.» |
| E3 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **4 / 227** | 1.8 | Page 3, Table 2 | «15–19 4(1.76%) Severe 20–24 0 Extreme» |
| E4 | 18-40 | A-MISO-S · A-MISO-S>=10 | **L2** | **10 / 141** | 7.1 | Page 4, Table 4 (Group 1) | «10–14 9(6.38%) Moderate 15–19 1(0.70%) Severe 20–24 0 Extreme Total 141 (100%)» |
| E5 | 18-40 | A-MISO-S · A-MISO-S>=5 | **L1** | **59 / 141** | 41.8 | Page 4, Table 4 (Group 1) | «5–9 49(34.75%) Mild 10–14 9(6.38%) Moderate 15–19 1(0.70%) Severe» |
| E6 | 18-40 | A-MISO-S · A-MISO-S>=15 | **L2** | **1 / 141** | 0.7 | Page 4, Table 4 (Group 1) | «15–19 1(0.70%) Severe 20–24 0 Extreme Total 141 (100%)» |
| E7 | 41-60 | A-MISO-S · A-MISO-S>=10 | **L2** | **11 / 73** | 15.1 | Page 4, Table 4 (Group 2) | «10–14 10(13.69%) Moderate 15–19 1(1.36%) Severe 20–24 0 Extreme Total 73 (100%)» |
| E8 | 41-60 | A-MISO-S · A-MISO-S>=5 | **L1** | **35 / 73** | 47.9 | Page 4, Table 4 (Group 2) | «5–9 24(32.87%) Mild 10–14 10(13.69%) Moderate 15–19 1(1.36%) Severe» |
| E9 | 41-60 | A-MISO-S · A-MISO-S>=15 | **L2** | **1 / 73** | 1.4 | Page 4, Table 4 (Group 2) | «15–19 1(1.36%) Severe 20–24 0 Extreme Total 73 (100%)» |
| E10 | >60 | A-MISO-S · A-MISO-S>=10 | **L2** | **0 / 12** | 0.0 | Page 4, Table 4 (Group 3) | «10–14 0 Moderate 15–19 0 Severe 20–24 0 Extreme Total 12 (100%)» |
| E11 | >60 | A-MISO-S · A-MISO-S>=5 | **L1** | **6 / 12** | 50.0 | Page 4, Table 4 (Group 3) | «0–4 6 (50%) Subclinical Group 3 5–9 6(50%) Mild» |
| E12 | >60 | A-MISO-S · A-MISO-S>=15 | **L2** | **0 / 12** | 0.0 | Page 4, Table 4 (Group 3) | «15–19 0 Severe 20–24 0 Extreme Total 12 (100%)» |
| E13 | female | A-MISO-S · A-MISO-S>=10 | **L2** | **12 / 131** | 9.2 | Page 3, Results; Table 2; Fig. 1 | «The gender ratio in the mild, moderate, and severe categories was 1.2, 0.9, and 1.0 respectively, resulting in an overall female-to-male ratio of 1.11.» |
| E14 | male | A-MISO-S · A-MISO-S>=10 | **L2** | **13 / 96** | 13.5 | Page 3, Results; Fig. 1 | «The gender ratio in the mild, moderate, and severe categories was 1.2, 0.9, and 1.0 respectively» |
| E15 | female | A-MISO-S · A-MISO-S>=15 | **L2** | **2 / 131** | 1.5 | Page 3, Results; Fig. 1 | «The gender ratio in the mild, moderate, and severe categories was 1.2, 0.9, and 1.0 respectively» |
| E16 | male | A-MISO-S · A-MISO-S>=15 | **L2** | **2 / 96** | 2.1 | Page 3, Results; Fig. 1 | «The gender ratio in the mild, moderate, and severe categories was 1.2, 0.9, and 1.0 respectively» |

- E1: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (moderate + severe + extreme); у авторов: «clinically significant misophonic symptoms (moderate or higher severity)»; главная у авторов: yes; период: NR; **расчёт: 21 (10-14) + 4 (15-19) + 0 (20-24) from Table 2 = 25**; заметка: 25/227 = 11.01%. The authors state 10.96% (Table 2 note), 10.9% (Results) and 11% (Abstract, Discussion). Scale administered by an audiologist in a face-to-face interview (rule G7: keeps scale level).
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (mild and above); у авторов: «mild or more misophonic symptoms (cumulative of mild, moderate, severe)»; главная у авторов: no; период: NR; **расчёт: 65 (5-9) + 21 (10-14) + 4 (15-19) + 0 (20-24) from Table 2 = 90**; заметка: 90/227 = 39.6%. The authors do not report this cumulative figure.
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (severe + extreme); G2 above L2 cut-off; у авторов: «severe misophonic symptoms»; главная у авторов: no; период: NR; **расчёт: 4 (15-19) + 0 (20-24) from Table 2**
- E4: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: NR; **расчёт: 9 (10-14) + 1 (15-19) + 0 (20-24) from Table 4, Group 1**; заметка: Table 4 age-group bands do not add up to the Table 2 overall bands (see consistency_notes). The Methods give the age bands as 18-40 / 40-60 / >60; the table gives 18-40 / 41-60 / >60.
- E5: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «mild or more»; главная у авторов: no; период: NR; **расчёт: 49 + 9 + 1 + 0 from Table 4, Group 1**; заметка: Table 4 is inconsistent with Table 2.
- E6: источник порога: developer paper; правило: A-MISO-S row; G1; G2; у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: 1 (15-19) + 0 (20-24) from Table 4, Group 1**
- E7: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: NR; **расчёт: 10 (10-14) + 1 (15-19) + 0 (20-24) from Table 4, Group 2**; заметка: The Group 2 bands add up to 72 (37+24+10+1), but the printed total is 73 and the percentages use 73. The printed total is used as n.
- E8: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «mild or more»; главная у авторов: no; период: NR; **расчёт: 24 + 10 + 1 + 0 from Table 4, Group 2**; заметка: The Group 2 bands add up to 72, but the printed total is 73.
- E9: источник порога: developer paper; правило: A-MISO-S row; G1; G2; у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: 1 (15-19) + 0 (20-24) from Table 4, Group 2**; заметка: The Group 2 bands add up to 72, but the printed total is 73.
- E10: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: NR; **расчёт: 0 + 0 + 0 from Table 4, Group 3**
- E11: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «mild or more»; главная у авторов: no; период: NR; **расчёт: 6 + 0 + 0 + 0 from Table 4, Group 3**
- E12: источник порога: developer paper; правило: A-MISO-S row; G1; G2; у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: 0 + 0 from Table 4, Group 3**
- E13: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: NR; **расчёт: Moderate 21, female-to-male ratio 0.9 -> only split is 10F/11M (10/11=0.91); severe 4, ratio 1.0 -> 2F/2M; female >=10 = 10+2 = 12**; заметка: Uncertain derivation from rounded ratios; the counts behind Fig. 1 are not in the text. This assumes the ratios are count ratios. The overall ratio of 1.11 cannot be reproduced exactly. Reviewer should check Fig. 1.
- E14: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: NR; **расчёт: Moderate 21, ratio 0.9 -> 11M; severe 4, ratio 1.0 -> 2M; male >=10 = 11+2 = 13**; заметка: Uncertain derivation from rounded ratios (see the female estimate); check Fig. 1. Mild-band split is ambiguous (29 or 30 males), so the >=5 estimates by sex cannot be derived.
- E15: источник порога: developer paper; правило: A-MISO-S row; G1; G2; у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: Severe 4, female-to-male ratio 1.0 -> 2F/2M; extreme 0**; заметка: Derived from a rounded ratio; check Fig. 1.
- E16: источник порога: developer paper; правило: A-MISO-S row; G1; G2; у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: Severe 4, female-to-male ratio 1.0 -> 2F/2M; extreme 0**; заметка: Derived from a rounded ratio; check Fig. 1.

**Ключевые поля выборки:**
- **n_analysed: 227** — Page 3, Table 2 — «Categorization of misophonia severity using the Amsterdam Misophonia Scale (n = 227)»
- **population: gp_other** — Page 2, Materials and methods — «A total of 227 individuals from the general population were recruited using non-parametric snowball sampling»
- **sampling: snowball** — Page 2, Materials and methods — «A total of 227 individuals from the general population were recruited using non-parametric snowball sampling to meet this requirement.»

**Остальные поля:**
- clinical_group: NA — NA
- country: IND — Title; Page 1, affiliations — «Prevalence of misophonia in a tertiary healthcare hospital in Mumbai»
- setting: community: students affiliated with a tertiary healthcare teaching hospital in Mumbai, plus their relatives and friends — Page 2-3, Materials and methods — «Participants were recruited from among students affiliated with the tertiary healthcare teaching hospital, as well as their relatives and friends.»
- data_years: NR — Page 5, Declarations — «Received: 19 May 2025 / Accepted: 24 April 2026»
- design: validation study — Page 2, Materials and methods — «The present study was conducted in two phases: translation and validation of the Amsterdam Misophonia Scale – Revised (A-MISO-S) through empirical data collect…»
- topic_disclosed: NR — Page 3, Materials and methods — «Recruitment was conducted through direct approach, their family members, the relative and individuals known to the family member and voluntary participation.»
- inclusion_exclusion: Adults 18+ with self-reported normal hearing; excluded: self-reported psychiatric history, people on medication for any medical condition, people at risk of severe emotional distress from the questionnaire content — Page 3, Materials and methods — «All participants reported normal hearing status. Individuals with a self-reported history of psychiatric illness, those on medication for any medical condition…»
- n_invited: NR — NR
- n_responded: NR — Page 2, Materials and methods — «A total of 227 individuals from the general population were recruited»
- response_rate: NR — NR
- age_mean: 34.29 — Page 3, Materials and methods — «with a mean age of 34.29 years (SD ± 15.01), and an age range of 18 to 77 years»
- age_sd: 15.01 — Page 3, Materials and methods — «with a mean age of 34.29 years (SD ± 15.01)»
- age_min: 18 — Page 3, Materials and methods — «an age range of 18 to 77 years»
- age_max: 77 — Page 3, Materials and methods — «an age range of 18 to 77 years»
- age_group: adults — Page 3, Materials and methods — «an age range of 18 to 77 years»
- pct_female: 57.7 — Page 3, Materials and methods — «The final sample included 96 males and 131 females»
- informant: clinician — Page 2-3, Materials and methods — «It comprises six clinician-rated items, each scored on a scale of 0 to 4.»
- mode: face-to-face interview — Page 3, Materials and methods — «Data were collected through face-to-face structured interviews conducted by the Audiologist.»
- instruments: A-MISO-S (6 items, 0-24), Marathi translation (main data); A-MISO-S English version (only in the 30-person cross-language equivalence subsample) — Page 2-3, Materials and methods — «The participants were asked to fill the form in English and after 2 weeks fill the Marathi version of the questionnaire.»
- instrument_validated_in_language: yes — Page 3, Results — «The internal consistency of the translated questionnaire was found to be satisfactory, with a Cronbach's alpha coefficient of 0.82»
- pub_status: journal — Page 1, header — «The Egyptian Journal of Otolaryngology (2026) 42:149»
- language: English — Full text — «Prevalence of misophonia in a tertiary healthcare hospital in Mumbai with Marathi translated Amsterdam misophonia scale A-MISO-S»
- funding_coi: No external funding; authors declare no competing interests — Page 5, Funding; Competing interests — «The study was conducted without any external funding. ... The authors declare no competing interests.»
- notes: pct_female is derived: 131/227 = 57.7%. The Marathi A-MISO-S is validated in this same report (alpha 0.82, ICC 0.98, EFA, r=0.979 against English); there is no external validation. The authors call the scale 'Amsterdam Misophonia Scale - Revised (A-MISO-S)', but they describe the original 6-item, 0-24 A-MISO-S with Schroder 2013 bands, so it is coded A-MISO-S, not AMISOS-R. Recruitment is a snowball sample from people around the hospital (students, relatives, friends), described as 'general population'. Data collection years are not reported. Table 4 (age groups) does not match Table 2 (see c…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The study claims to describe the general (Marathi-speaking) population, but the frame was hospital-affiliated students and their relatives and friends. — Page 2-3, Materials and methods — «Participants were recruited from among students affiliated with the tertiary healthcare teaching hospital, as well as their relatives and friends.»
2. способ отбора: **no** — Snowball, non-probability sampling. — Page 2, Materials and methods — «recruited using non-parametric snowball sampling»
3. размер выборки: **no** — n = 227 < 385. — Page 2, Materials and methods — «A total of 227 individuals from the general population were recruited»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — Page 3, Materials and methods — «The final sample included 96 males and 131 females, with a mean age of 34.29 years (SD ± 15.01), and an age range of 18 to 77 years.»
5. охват (пропуски): **yes** — All 227 recruited participants have A-MISO-S scores in Table 2; no missing data reported. — Page 3, Table 2 — «Total 227 (100%)»
6. валидность определения случая: **yes** — A-MISO-S >=10 is the anchored cut-off, and the Marathi version has a published validation, though only in this same report (flag). — Page 3, Results; Table 2 — «approximately 10.9% of the population exhibited clinically significant misophonic symptoms (moderate or higher severity)»
7. единое надёжное измерение: **yes** — Same instrument, mode (face-to-face interview by an audiologist) and threshold for everyone; Cronbach's alpha reported in the sample. — Page 3, Materials and methods; Results — «Data were collected through face-to-face structured interviews conducted by the Audiologist. ... Cronbach's alpha coefficient of 0.82»
8. статистика (числитель и знаменатель): **yes** — Primary numerator and denominator traceable from Table 2 (21+4 of 227); CI calculable. Small inconsistencies: 10.96% stated vs 11.01% calculated, and Table 4 age-group totals. — Page 3, Table 2 — «10–14 21(9.25%) Moderate 15–19 4(1.76%) Severe ... Total 227 (100%)»
9. отклик: **no** — Snowball recruitment with no denominator of invited people; response rate not reported and not handled. — Page 3, Materials and methods — «Recruitment was conducted through direct approach, their family members, the relative and individuals known to the family member and voluntary participation.»

Правки:
- 

Проверено: да
---

## ST004 · Dalseng 2026 · Frontiers in psychiatry

Основной отчёт R0048: [текст](../../fulltext/text/R0048.txt) · [PDF](../../fulltext/pdf/R0048.pdf) — «Digital treatment for tinnitus combining tinnitus retraining therapy and cognitive behavioral therapy: a Norwegian naturalistic study.» — [DOI](https://doi.org/10.3389/fpsyt.2026.1868527)
Расхождения в тексте: The MQ range is stated as 0-68 in Measures (p.4) but as "15 to 68" in the Table 1 footnote. The MQ cut-off of 14 is cited from Jakubovski 2022, which applied it to the MQ Symptom Scale, but this paper describes only the total score. The discussion says the cut-off was set to detect people who are "sometimes sensitive". Table 1 counts (26+40+24=90) match the text's 62.50% of 144. The subgroup percentages (55.32, 67.80, 63.16) match the counts. The 121 exclusions mix patients missing baseline with patients missing 90-day questionnaires; the split is not given. THI exclusion is "scores below 16", while the mild band starts at 18.
Заметка ИИ: Tinnitus treatment study; the misophonia rate is an incidental baseline figure on an unanchored, low MQ cut-off. I coded it L0, assuming total >=14, and the reviewer should check this. If the reviewer reads it as the Symptom Scale, it becomes L1. JBI 3 uses the >=139 clinical threshold; under the general >=385 threshold it is no.

### ST004-1 · Tinnitus patients referred to hospital ENT clinic, Norway (n=144)
Отчёты: R0048 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ score >=14 (apparently MQ total 0-68; cut-off borrowed from Jakubovski et al. 2022) | **L0** | **90 / 144** | 62.5 | Table 1; Page 5, Results; Page 7 | «Indications of hyperacusis was present in 16.67% of the sample, and 62.50% for misophonia.» |
| E2 | mild tinnitus (THI 18-36) | MQ · MQ score >=14 (apparently MQ total 0-68) | **L0** | **26 / 47** | 55.3 | Table 1 | «Misophonia Yes 26 (55.32)» |
| E3 | moderate tinnitus (THI 38-56) | MQ · MQ score >=14 (apparently MQ total 0-68) | **L0** | **40 / 59** | 67.8 | Table 1 | «Misophonia Yes 26 (55.32) 40 (67.80) 24 (63.16)» |
| E4 | severe+ tinnitus (THI 58-100) | MQ · MQ score >=14 (apparently MQ total 0-68) | **L0** | **24 / 38** | 63.2 | Table 1 | «Misophonia Yes 26 (55.32) 40 (67.80) 24 (63.16)» |

- E1: источник порога: study's own; правило: MQ row; G2/G3: total >=14 = mean item 0.82 (14/17), below the L1 Symptom Scale >=14 (mean item 2) -> L0; у авторов: «Indications of ... misophonia; scored above cutoff on the MQ»; главная у авторов: no; период: NR; **расчёт: 26 + 40 + 24 from Table 1 = 90; 90/144 = 62.50%, matching the text**; заметка: Which MQ score the 14 was applied to is not stated. If it was the Symptom Scale (as in Jakubovski 2022), the level would be L1. A sample mean total of 19.51 (SD 12.43) fits a total-score cut-off. Denominator: patients who completed baseline and 90-day questionnaires.
- E2: источник порога: study's own; правило: MQ row; G2/G3 as for whole sample; у авторов: «Misophonia Yes»; главная у авторов: no; период: NR; заметка: Clinical subgroup defined by THI severity
- E3: источник порога: study's own; правило: MQ row; G2/G3 as for whole sample; у авторов: «Misophonia Yes»; главная у авторов: no; период: NR; заметка: Clinical subgroup defined by THI severity
- E4: источник порога: study's own; правило: MQ row; G2/G3 as for whole sample; у авторов: «Misophonia Yes»; главная у авторов: no; период: NR; заметка: Clinical subgroup defined by THI severity

**Ключевые поля выборки:**
- **n_analysed: 144** — Page 3, Participants and procedure; Table 1 — «The final sample therefore consisted of 144 patients.»
- **population: clinical** — Page 3, Participants and procedure — «To be included in the study the patients had to: a) be diagnosed with tinnitus»
- **sampling: census** — Page 3, Methods — «Before initiating the treatment used in this study, patients were invited to participate ... Out of 424 referred patients, a total of 294 (69%) gave their consent to be included in the study.»

**Остальные поля:**
- clinical_group: tinnitus — Page 3, Participants and procedure — «a) be diagnosed with tinnitus, b) be between 18 and 90 years of age, and c) give their consent to the study.»
- country: NOR — Page 1, title and affiliations — «a Norwegian naturalistic study ... Møre og Romsdal Hospital Trust, Molde, Norway»
- setting: clinic: hospital ENT (ear, nose and throat) department; patients referred by their GP for tinnitus (probably Møre og Romsdal Hospital Trust, from the author affiliation) — Page 3, Methods — «The patients were referred because of tinnitus complaints by their general practitioner and then examined and assessed by an ear, nose, and throat (ENT) specia…»
- data_years: NR — Methods — «NR»
- design: cohort baseline — Page 3, Methods — «This study is a single arm, prospective observational study without a control group.»
- topic_disclosed: NR — Page 3, Methods — «patients were invited to participate, and only those who provided informed consent were included in the study.»
- inclusion_exclusion: Inclusion: tinnitus diagnosis, age 18-90, consent. Exclusion: vestibular schwannoma or other vestibular disorders; THI <16 (n=29); no questionnaires at baseline or at 90 days (n=121) — Page 3, Participants and procedure — «29 with slight to no tinnitus handicap according to Tinnitus Handicap Inventory (THI; scores below 16) were excluded ... Another 121 patients were excluded bec…»
- n_invited: 424 — Page 3, Methods — «Out of 424 referred patients, a total of 294 (69%) gave their consent»
- n_responded: 294 — Page 3, Methods — «a total of 294 (69%) gave their consent to be included in the study.»
- response_rate: 69 — Page 3, Methods — «Out of 424 referred patients, a total of 294 (69%) gave their consent»
- age_mean: NR — Table 1 — «Age ... 18-30 ... 71+ (bands only)»
- age_sd: NR — Table 1 — «NR»
- age_min: NR — Page 3, inclusion criteria; Table 1 — «b) be between 18 and 90 years of age»
- age_max: NR — Page 3, inclusion criteria; Table 1 — «b) be between 18 and 90 years of age»
- age_group: adults — Page 3, inclusion criteria — «b) be between 18 and 90 years of age»
- pct_female: 49.31 — Page 5, Results; Table 1 — «The sample comprised 144 patients (50.69% male)»
- informant: self — Page 4, Measures — «Answers to the questionnaires were collected using the same digital platform used for treatment delivery.»
- mode: online — Page 4, Measures — «Answers to the questionnaires were collected using the same digital platform used for treatment delivery.»
- instruments: Misophonia Questionnaire (MQ), Norwegian version (MQ-NOR; Larsen et al. 2023) — Page 4, Measures; ref 34 — «The Misophonia Questionnaire (MQ; 34, 35) ... 34. Larsen EA ... Preliminary validation of the Norwegian version of misophonia questionnaire (MQ-NOR).»
- instrument_validated_in_language: yes — Page 4, Measures; ref 34 — «Preliminary validation of the Norwegian version of misophonia questionnaire (MQ-NOR). Int J Audiol. (2023)»
- pub_status: journal — Page 1, header — «Front. Psychiatry 17:1868527. doi: 10.3389/fpsyt.2026.1868527»
- language: English — Full text — «Digital treatment for tinnitus combining tinnitus retraining therapy and cognitive behavioral therapy: a Norwegian naturalistic study»
- funding_coi: Funded by the liaison committee between Helse Midt-Norge and NTNU (grant to the third author for developing the treatment); the authors declare no conflicts — Page 8, Funding; Conflict of interest — «The third author was awarded funding from the liaison committee between the regional health authority (Helse Midt-Norge) and the Norwegian University of Scienc…»
- notes: Treatment study; the prevalence figure is a baseline by-product. The analysed sample (144) is 49% of the 294 who consented and 34% of the 424 referred. Selection required THI >=16 and completed questionnaires at baseline AND 90 days, so patients with only baseline data are excluded. Only male % is reported (50.69%; 73 = 24+27+22); female % = 100 - 50.69 = 49.31, assuming the other 71 are female. Age is given only in bands (18-30 to 71+); inclusion was 18-90. The MQ cut-off of 14 is cited from Jakubovski 2022 (which used it on the Symptom Scale) but seems to be applied to the MQ total (0-68). …

**Риск смещения (JBI):**
1. рамка выборки: **yes** — The frame is patients referred to the ENT clinic for tinnitus, which matches the target population (tinnitus patients at the clinic). — Page 3, Methods — «The patients were referred because of tinnitus complaints by their general practitioner and then examined and assessed by an ear, nose, and throat (ENT) specia…»
2. способ отбора: **yes** — All referred patients were invited, which is effectively consecutive or census. Losses from consent and follow-up are dealt with under items 5 and 9. — Page 3, Methods — «Before initiating the treatment used in this study, patients were invited to participate ... Out of 424 referred patients»
3. размер выборки: **yes** — n=144 is at least 139, the threshold for a clinical sample. It is below 385 if the general threshold is applied. — Page 3 — «The final sample therefore consisted of 144 patients.»
4. описание выборки и условий: **unclear** — Age (bands), sex, setting and country are reported, but data collection dates are not. — Table 1; Methods — «TABLE 1 Participant demographics and clinical profile at pre-treatment (N = 144).»
5. охват (пропуски): **no** — 121 of the 265 consenting eligible patients were excluded for missing questionnaires at baseline or 90 days (>10%). Baseline exclusions were not handled; EM imputation was used only for 180-day data. — Page 3; Page 5, Statistical analysis — «Another 121 patients were excluded because they did not answer questionnaires before starting the digital treatment or after 90 days.»
6. валидность определения случая: **no** — The MQ score of 14 (apparently the total, 0-68) has no clinical anchoring and is far below the anchored cut-offs. The authors say it was likely set too low. — Page 4, Measures; Page 8 — «there is no official cut-off for the MQ, but some studies have used a score of 14 as a cut-off (36). ... This could suggest that the cutoff value was set too l…»
7. единое надёжное измерение: **unclear** — Everyone completed the same online MQ, but internal consistency is not reported in this text. The Norwegian validation is cited, but its reliability values are not given here. — Page 4, Measures — «Answers to the questionnaires were collected using the same digital platform used for treatment delivery.»
8. статистика (числитель и знаменатель): **yes** — Counts by subgroup and the overall % are given (90/144), so a CI can be calculated. Which MQ score was used is unclear. — Table 1; Page 5 — «Misophonia Yes 26 (55.32) 40 (67.80) 24 (63.16)»
9. отклик: **no** — 69% consented, but only 144/424 (34%) were analysed. Included and excluded patients were not compared. — Page 3; Page 5 — «Of the 294 individuals who provided informed consent, 144 (49%) met the inclusion criteria and were retained for analysis.»

Правки:
- 

Проверено: да
---

## ST005 · Dwyer 2026 · Journal of attention disorders

Основной отчёт R0057: [текст](../../fulltext/text/R0057.txt) — «A Trans-Diagnostic Investigation of Attention and Diverse Phenotypes of "Auditory Hyperreactivity" in Autism, ADHD, and the General Population.» — [DOI](https://doi.org/10.1177/10870547251361226)
Приложен R0441: [текст](../../fulltext/text/R0441.txt) · [PDF](../../fulltext/pdf/R0441.pdf) — «The Multidimensional Inventory of Sound Tolerance in Adults (MIST-A): Psychometric Evaluation of a Dimensional Self-rep…»
Связь отчётов: NDD study (Dwyer et al. 2024): R0057 says the sample is described in Dwyer et al. 2024; R0441 reports it as the 'NDD' sample (n = 478 there, 492 in R0057)
Расхождения в тексте: Sample size: R0057 reports 492 participants. R0441 reports the same NDD sample as n=478 because 14 participants had no MIST-A data. Misophonia definitions differ: R0057 Table 1 counts current self-identified or diagnosed misophonia after a definition was shown: 17+49+76+98 = 240/492 (48.8%). R0441 Suppl. Table 4.10 gives 115/478 (24.1%) for the whole NDD sample, using prior professional diagnosis OR (current self-identification AND at least 'mildly disabling'). That is L1 under rule G4, but it is not split by diagnostic group, so it is noted, not extracted. R0441 also regrouped autism and ADHD by professional diagnosis, so its groups differ from R0057's. JBI 3: the 139 threshold for clinical groups was applied to the three neurodivergent groups. Only autistic+ADHD (141) passes, and only narrowly; under the 385 threshold all four groups fail. MIST-A Misophonia T>60 ('clinically elevated'…
Заметка ИИ: MIST-A is not in Table 1; no counts were reported for it anyway. Data-collection years and funding are not in the provided texts. Dwyer et al. 2024 (Neurodiversity) is the primary description of this sample but was not attached.

Основной отчёт R0441: [текст](../../fulltext/text/R0441.txt) · [PDF](../../fulltext/pdf/R0441.pdf) — «The Multidimensional Inventory of Sound Tolerance in Adults (MIST-A): Psychometric Evaluation of a Dimensional Self-report Measure of Hyperacusis, Misophonia, …» — [DOI](https://doi.org/10.31234/osf.io/4qryg_v1)
Связь отчётов: Williams dissertation chapter: only the AUT sample (n = 295) is reported nowhere else; PROA is extracted from R0998 and NDD from R0057; ClinDST and LAB were recruited partly for sound intolerance (E1)
Не выписано ИИ: PROA (Prolific US general population, n=1403): extracted from R0998. NDD (autism/ADHD and controls, SPARK/CloudResearch/Prolific, n=478): extracted from R0057. ClinDST (n=516): recruited for clinically significant hyperacusis or misophonia via DST support groups (E1). LAB (Vanderbilt laboratory study, n=115): recruited partly for clinically significant DST complaints (E1).
Расхождения в тексте: 1) Text (p.5) says 1459 clinical and 1348 general population participants, but Table 4.1 shows Clinical n=1397 and General Population n=1410. This does not affect the AUT values. 2) AUT misophonia shows '16 (100.0%)' in Suppl. Table 4.10 because non-diagnosed participants were treated as missing (p.52). Hyperacusis shows the same pattern: 13 (100.0%). 3) AUT sex counts are 56 + 228 = 284 of 295 (11 missing); 80.3% female is of non-missing values. 4) Text p.5 says the entire AUT sample completed the development version of the MIST-A. The Discussion (p.33-34) says 'primarily in the AUT sample' and 'approximately half of the autistic participants'. 5) Tinnitus in AUT is given as 27% prevalence in the text (p.54) but as 57 (19.3%) in Suppl. Table 4.10.
Заметка ИИ: Extracted one sample (AUT). Its only misophonia case count is self-reported professional diagnoses (16). I set the denominator to 295, the whole sample, myself; the authors gave no prevalence for this sample. The MIST-A Misophonia screening cut-off was not applied to AUT counts in the report.

Основной отчёт R0998: [текст](../../fulltext/text/R0998.txt) — «Psychometric validation of a brief self-report measure of misophonia symptoms and functional impairment: The duke-vanderbilt misophonia screening questionnaire.» — [DOI](https://doi.org/10.3389/fpsyg.2022.897901)
Приложен R0652: [текст](../../fulltext/text/R0652.txt) · [PDF](../../fulltext/pdf/R0652.pdf) — «Decreased Sound Tolerance Disorders (Hyperacusis and Misophonia) in Cognitively Able Autistic Adults I: Prevalence and …»
Приложен R0440: [текст](../../fulltext/text/R0440.txt) · [PDF](../../fulltext/pdf/R0440.pdf) — «Decreased Sound Tolerance Disorders (Hyperacusis and Misophonia) in Cognitively Able Autistic Adults II: Demographic an…»
Не приложен (длинный) R0441: [текст](../../fulltext/text/R0441.txt) · [PDF](../../fulltext/pdf/R0441.pdf) — «The Multidimensional Inventory of Sound Tolerance in Adults (MIST-A): Psychometric Evaluation of a Dimensional Self-rep…»
Связь отчётов: Williams et al.: Prolific general-population adults (n = 1,403; 'PROA' in R0441) and SPARK autistic adults (n = 936; also R0652, R0440 and the dissertation chapter R0441)
Расхождения в тексте: Prolific: 1516 − 113 = 1403 matches the text. 102/1403 = 7.27% (reported 7.3%), 144/1403 = 10.26% (reported 10.2%) and 74/102 = 72.5% are all consistent. SPARK: 332/936 = 35.47%, 97/936 = 10.36%, 261/590 = 44.2% and 71/346 = 20.5% are consistent across R0998 and R0652. Disagreements: (1) SPARK S1-positive count is 647 in Table 3 but 645 in the text ('SPARK: n = 645'). I used the table value. (2) SPARK flow differs between reports. R0998 says 1271 consented, 1121 completed the measures and 185 failed quality checks. R0440 says 1178 had sufficient DST data. R0652 lists 108 dropouts and exclusions of 134+45+34+3+23 = 239, and these figures do not reproduce 936 (exclusions may overlap). (3) Hyperacusis prevalence is 40.2% in parts of R0652 and 40.3% (377/936) elsewhere; this does not affect misophonia. (4) R0652 p.17 has a label typo, 'Misophonia: Hyperacusis: 44.2% of females vs. 20.5% of …
Заметка ИИ: Points for the reviewer to decide. Sampling for Prolific is coded as quota because of the single-sex batches of 750; it could also be coded convenience. topic_disclosed = no for both samples: they were advertised as 'sensory sensitivities' without naming sound, which is borderline. The DVMSQ was developed in this same report and its algorithm has no interview or ROC anchoring. JBI 6 is still rated yes because the DVMSQ algorithm is on the listed set. The SPARK weighted_pct of 29.1 is a sex re-weighting to an assumed 3:1 male:female ratio, not survey weights. No funding statement for the Proli…

### ST005-1 · Comparison group (no autism, no ADHD), online panels, USA, n=99
Отчёты: R0057 (main); R0441 (NDD sample, pooled with the other three groups)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-identified current misophonia after reading a definition, or current formal diagnosis (yes/no item) | **L1** | **17 / 99** | 17.2 | Table 1 (Co-occurring conditions) and note c | «Co-occurring conditions c / 17 misophonia (17.17%)» |

- E1: источник порога: study's own; правило: adhoc row; L1 self-identified misophonia (definition shown) / self-reported diagnosis; у авторов: «co-occurring condition: misophonia»; главная у авторов: no; период: current; заметка: Only categorical misophonia estimate in R0057; reported as a demographic characteristic, not called a prevalence estimate.

**Ключевые поля выборки:**
- **n_analysed: 99** — Table 1; Methods, Participants — «This left a final sample of 492 participants (Table 1): 99 comparison»
- **population: gp_other** — Methods, Participants — «comparison participants who were neither autistic nor ADHD (comparison)»
- **sampling: convenience** — Methods, Participants — «Both neurodivergent and comparison participants were recruited from CloudResearch (Litman et al., 2017) and Prolific (Palan & Schitter, 2018).»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — Methods, Participants — «We recruited four groups of participants from the United States»
- setting: online panel (Prolific 89, CloudResearch 10) — Methods, Participants — «99 comparison (10 CloudResearch and 89 Prolific)»
- data_years: NR — NR — «NR»
- design: cross-sectional — Discussion — «Although this study’s cross-sectional design cannot test causality»
- topic_disclosed: NR — R0441, p. 48 (4.7.1.3) — «derived from an online survey study examining attention, hyper-focus, and related constructs in adults with and without neurodevelopmental disabilities»
- inclusion_exclusion: US adults; not autistic or ADHD; ASRS-6 <14; RAADS-14 <14; no first- or second-degree autistic/ADHD relatives; excluded uncorrected hearing loss, failed attention checks, poor/discrepant data — Methods, Participants; ASRS; RAADS-14 — «as were comparison participants with first- or second-degree autistic or ADHD relatives (n = 53)»
- n_invited: NR — Methods, Participants — «One thousand thirty-eight unique, complete screening responses were received (63 CloudResearch, 649 Prolific, and 325 SPARK).»
- n_responded: NR — Methods, Participants — «a total of 609 unique participants provided responses to the full survey»
- response_rate: NR — NR — «NR»
- age_mean: 36.74 — Table 1 — «Age (years) | 36.74 (11.75) | 19.00–67.00»
- age_sd: 11.75 — Table 1 — «Age (years) | 36.74 (11.75) | 19.00–67.00»
- age_min: 19 — Table 1 — «Age (years) | 36.74 (11.75) | 19.00–67.00»
- age_max: 67 — Table 1 — «Age (years) | 36.74 (11.75) | 19.00–67.00»
- age_group: adults — Abstract — «Four hundred ninety-two adults»
- pct_female: 45.45 — Table 1 (Sex) — «Sex | 54 M (54.55%), 45 F (45.45%)»
- informant: self — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
- mode: online — R0441, p. 49 (4.7.1.3) — «Surveys were completed on the Qualtrics platform»
- instruments: Self-identified misophonia item with definition shown (English, ad hoc); MIST-A Misophonia subscale (English, 28-item development version, T-scores); Core Discriminant Sounds (CDS) sound-rating task — Table 1 note c; Methods, MIST-A; Sound Rating Measures — «In the case of misophonia only, participants were provided with a definition of misophonia»
- instrument_validated_in_language: no — Table 1 note c — «participants were provided with a definition of misophonia ... before being asked if they had the condition»
- pub_status: journal — Header — «venue: Journal of attention disorders; DOI: 10.1177/10870547251361226»
- language: English — Full text — «A Trans-Diagnostic Investigation of Attention and Diverse Phenotypes of “Auditory Hyperreactivity” in Autism, ADHD, and the General Population»
- funding_coi: NR — NR — «NR»
- notes: Same study as Dwyer et al. 2024 (not attached) and the 'NDD' sample of R0441 (n=478 there; 14 without MIST-A data excluded). R0441 gives a different misophonia definition only for the whole NDD sample: prior professional diagnosis, or current self-identification plus at least 'mildly disabling' = 115/478 (24.1%, R0441 Suppl. Table 4.10). It is not split by group, so it is not extracted as a group estimate. The comparison group is a screened, restricted group from online panels (no autistic/ADHD relatives, low ASRS-6/RAADS-14). No counts are given for MIST-A Misophonia T>60 ('clinically elevat…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Online panels (Prolific, CloudResearch) cover only part of the US general adult population — Methods, Participants — «comparison participants were recruited from CloudResearch (Litman et al., 2017) and Prolific»
2. способ отбора: **no** — Opt-in online panel, non-probability — Methods, Participants — «Prolific participants were able to see the study if they were potentially eligible based on their demographics.»
3. размер выборки: **no** — n=99 < 385 — Table 1 — «99 comparison (10 CloudResearch and 89 Prolific)»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection not reported — Table 1; Participants — «We recruited four groups of participants from the United States»
5. охват (пропуски): **unclear** — Percentages computed over full group n, but handling of missing responses to the misophonia item not reported — Table 1 — «17 misophonia (17.17%)»
6. валидность определения случая: **no** — Ad hoc self-identification item (definition shown) — Table 1 note c — «participants were provided with a definition of misophonia»
7. единое надёжное измерение: **unclear** — Same item and online mode for all; no reliability reported for the self-identification item — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given; CI calculable — Table 1 — «17 misophonia (17.17%)»
9. отклик: **no** — Open online panel recruitment, no denominator of invited people — Methods, Participants — «One thousand thirty-eight unique, complete screening responses were received»

Правки:
- 

Проверено: да
### ST005-2 · ADHD-only group, online panels, USA, n=122
Отчёты: R0057 (main); R0441 (NDD sample, pooled with the other three groups)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-identified current misophonia after reading a definition, or current formal diagnosis (yes/no item) | **L1** | **49 / 122** | 40.2 | Table 1 (Co-occurring conditions) and note c | «49 misophonia (40.16%)» |

- E1: источник порога: study's own; правило: adhoc row; L1 self-identified misophonia (definition shown) / self-reported diagnosis; у авторов: «co-occurring condition: misophonia»; главная у авторов: no; период: current; заметка: Reported as a demographic characteristic.

**Ключевые поля выборки:**
- **n_analysed: 122** — Table 1; Methods, Participants — «122 ADHD-only (7 CloudResearch and 115 Prolific)»
- **population: clinical** — Methods, Participants — «ADHD participants who were not autistic (ADHD-only)»
- **sampling: convenience** — Methods, Participants — «Both neurodivergent and comparison participants were recruited from CloudResearch (Litman et al., 2017) and Prolific (Palan & Schitter, 2018).»

**Остальные поля:**
- clinical_group: ADHD — Table 1 — «ADHD dx status | | 93 diagnosed (76.23%)»
- country: USA — Methods, Participants — «We recruited four groups of participants from the United States»
- setting: online panel (Prolific 115, CloudResearch 7) — Methods, Participants — «122 ADHD-only (7 CloudResearch and 115 Prolific)»
- data_years: NR — NR — «NR»
- design: cross-sectional — Discussion — «Although this study’s cross-sectional design cannot test causality»
- topic_disclosed: NR — R0441, p. 48 (4.7.1.3) — «derived from an online survey study examining attention, hyper-focus, and related constructs in adults with and without neurodevelopmental disabilities»
- inclusion_exclusion: US adults; diagnosed or self-identified ADHD, not autistic; ASRS-6 >=10 (diagnosed) or >=14 (self-identified); excluded uncorrected hearing loss, failed attention checks, poor/discrepant data — Methods, ASRS — «participants who had formal ADHD diagnoses and whose ASRS-6 scores met or exceeded the most sensitive cut-off (10)»
- n_invited: NR — Methods, Participants — «One thousand thirty-eight unique, complete screening responses were received (63 CloudResearch, 649 Prolific, and 325 SPARK).»
- n_responded: NR — Methods, Participants — «a total of 609 unique participants provided responses to the full survey»
- response_rate: NR — NR — «NR»
- age_mean: 34.43 — Table 1 — «34.43 (10.07) | 18.00–72.00»
- age_sd: 10.07 — Table 1 — «34.43 (10.07) | 18.00–72.00»
- age_min: 18 — Table 1 — «34.43 (10.07) | 18.00–72.00»
- age_max: 72 — Table 1 — «34.43 (10.07) | 18.00–72.00»
- age_group: adults — Abstract — «Four hundred ninety-two adults»
- pct_female: 55.74 — Table 1 (Sex) — «54 M (44.26%), 68 F (55.74%)»
- informant: self — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
- mode: online — R0441, p. 49 (4.7.1.3) — «Surveys were completed on the Qualtrics platform»
- instruments: Self-identified misophonia item with definition shown (English, ad hoc); MIST-A Misophonia subscale (English, 28-item development version, T-scores); Core Discriminant Sounds (CDS) sound-rating task — Table 1 note c; Methods, MIST-A; Sound Rating Measures — «In the case of misophonia only, participants were provided with a definition of misophonia»
- instrument_validated_in_language: no — Table 1 note c — «participants were provided with a definition of misophonia ... before being asked if they had the condition»
- pub_status: journal — Header — «venue: Journal of attention disorders; DOI: 10.1177/10870547251361226»
- language: English — Full text — «A Trans-Diagnostic Investigation of Attention and Diverse Phenotypes of “Auditory Hyperreactivity” in Autism, ADHD, and the General Population»
- funding_coi: NR — NR — «NR»
- notes: ADHD status is partly self-identified (93/122 diagnosed). Same study as Dwyer et al. 2024 and the R0441 'NDD' sample (n=478); R0441 regrouped ADHD by professional diagnosis. R0441 gives an NDD-wide misophonia count (diagnosis, or self-identification plus at least 'mildly disabling') of 115/478, not split by group. No counts are given for MIST-A Misophonia T>60.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Online panels cover only part of US adults with ADHD — Methods, Participants — «Both neurodivergent and comparison participants were recruited from CloudResearch (Litman et al., 2017) and Prolific»
2. способ отбора: **no** — Opt-in online panel, non-probability — Methods, Participants — «Prolific participants were able to see the study if they were potentially eligible based on their demographics.»
3. размер выборки: **no** — n=122 < 139 (clinical group) — Table 1 — «122 ADHD-only (7 CloudResearch and 115 Prolific)»
4. описание выборки и условий: **unclear** — Dates of data collection not reported — Table 1; Participants — «We recruited four groups of participants from the United States»
5. охват (пропуски): **unclear** — Percentages over full group n; missing-data handling not reported — Table 1 — «49 misophonia (40.16%)»
6. валидность определения случая: **no** — Ad hoc self-identification item — Table 1 note c — «participants were provided with a definition of misophonia»
7. единое надёжное измерение: **unclear** — Same item and mode; no reliability reported for the item — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given; CI calculable — Table 1 — «49 misophonia (40.16%)»
9. отклик: **no** — Open online panel recruitment, no denominator of invited people — Methods, Participants — «One thousand thirty-eight unique, complete screening responses were received»

Правки:
- 

Проверено: да
### ST005-3 · Autistic-only group, SPARK registry and Prolific, USA, n=130
Отчёты: R0057 (main); R0441 (NDD sample, pooled with the other three groups)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-identified current misophonia after reading a definition, or current formal diagnosis (yes/no item) | **L1** | **76 / 130** | 58.5 | Table 1 (Co-occurring conditions) and note c | «76 misophonia (58.46%)» |

- E1: источник порога: study's own; правило: adhoc row; L1 self-identified misophonia (definition shown) / self-reported diagnosis; у авторов: «co-occurring condition: misophonia»; главная у авторов: no; период: current; заметка: Reported as a demographic characteristic.

**Ключевые поля выборки:**
- **n_analysed: 130** — Table 1; Methods, Participants — «130 autistic-only (38 Prolific and 92 SPARK)»
- **population: clinical** — Methods, Participants — «autistic people who were not ADHD (autistic-only)»
- **sampling: convenience** — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study, of whom 416 agreed to share their information with the research team.»

**Остальные поля:**
- clinical_group: autism — Table 1 — «Autism dx status | | | 106 diagnosed (81.54%)»
- country: USA — Methods, Participants — «We recruited four groups of participants from the United States»
- setting: research registry (SPARK Research Match, 92) and online panel (Prolific, 38) — Methods, Participants — «130 autistic-only (38 Prolific and 92 SPARK)»
- data_years: NR — NR — «NR»
- design: cross-sectional — Discussion — «Although this study’s cross-sectional design cannot test causality»
- topic_disclosed: NR — R0441, p. 48 (4.7.1.3) — «derived from an online survey study examining attention, hyper-focus, and related constructs in adults with and without neurodevelopmental disabilities»
- inclusion_exclusion: US adults; diagnosed or self-identified autistic, not ADHD; ASRS-6 <18; RAADS-14 >=14; excluded uncorrected hearing loss, failed attention checks, poor/discrepant data — Methods, ASRS; RAADS-14 — «Autistic participants were excluded if they did not have RAADS-14 scores at or exceeding cut-off (14).»
- n_invited: NR — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study»
- n_responded: NR — Methods, Participants — «a total of 609 unique participants provided responses to the full survey»
- response_rate: NR — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study, of whom 416 agreed to share their information»
- age_mean: 37.28 — Table 1 — «37.28 (14.81) | 18.00–70.00»
- age_sd: 14.81 — Table 1 — «37.28 (14.81) | 18.00–70.00»
- age_min: 18 — Table 1 — «37.28 (14.81) | 18.00–70.00»
- age_max: 70 — Table 1 — «37.28 (14.81) | 18.00–70.00»
- age_group: adults — Abstract — «Four hundred ninety-two adults»
- pct_female: 61.54 — Table 1 (Sex) — «50 M (38.46%), 80 F (61.54%)»
- informant: self — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
- mode: online — R0441, p. 49 (4.7.1.3) — «Surveys were completed on the Qualtrics platform»
- instruments: Self-identified misophonia item with definition shown (English, ad hoc); MIST-A Misophonia subscale (English, 28-item development version, T-scores); Core Discriminant Sounds (CDS) sound-rating task — Table 1 note c; Methods, MIST-A; Sound Rating Measures — «In the case of misophonia only, participants were provided with a definition of misophonia»
- instrument_validated_in_language: no — Table 1 note c — «participants were provided with a definition of misophonia ... before being asked if they had the condition»
- pub_status: journal — Header — «venue: Journal of attention disorders; DOI: 10.1177/10870547251361226»
- language: English — Full text — «A Trans-Diagnostic Investigation of Attention and Diverse Phenotypes of “Auditory Hyperreactivity” in Autism, ADHD, and the General Population»
- funding_coi: NR — NR — «NR»
- notes: Autism is partly self-identified (106/130 diagnosed). SPARK: 416 of 2296 people informed agreed to share their information (about 18%); SPARK screening n=325 across both autistic groups. Same study as Dwyer et al. 2024 and the R0441 'NDD' sample (n=478). R0441 gives an NDD-wide misophonia count of 115/478 under a different definition, not split by group.

**Риск смещения (JBI):**
1. рамка выборки: **no** — SPARK registry and Prolific cover only part of US autistic adults — Methods, Participants — «many autistic participants were recruited from SPARK Research Match (Feliciano et al., 2018)»
2. способ отбора: **no** — Volunteer opt-in from registry and online panel — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study, of whom 416 agreed to share their information»
3. размер выборки: **no** — n=130 < 139 (clinical group) — Table 1 — «130 autistic-only (38 Prolific and 92 SPARK)»
4. описание выборки и условий: **unclear** — Dates of data collection not reported — Table 1; Participants — «We recruited four groups of participants from the United States»
5. охват (пропуски): **unclear** — Percentages over full group n; missing-data handling not reported — Table 1 — «76 misophonia (58.46%)»
6. валидность определения случая: **no** — Ad hoc self-identification item — Table 1 note c — «participants were provided with a definition of misophonia»
7. единое надёжное измерение: **unclear** — Same item and mode; no reliability reported for the item — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given; CI calculable — Table 1 — «76 misophonia (58.46%)»
9. отклик: **no** — SPARK uptake 416/2296 (18%); Prolific open recruitment without denominator; not handled — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study, of whom 416 agreed to share their information»

Правки:
- 

Проверено: да
### ST005-4 · Autistic + ADHD group, SPARK registry and online panels, USA, n=141
Отчёты: R0057 (main); R0441 (NDD sample, pooled with the other three groups)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-identified current misophonia after reading a definition, or current formal diagnosis (yes/no item) | **L1** | **98 / 141** | 69.5 | Table 1 (Co-occurring conditions) and note c | «98 misophonia (69.50%)» |

- E1: источник порога: study's own; правило: adhoc row; L1 self-identified misophonia (definition shown) / self-reported diagnosis; у авторов: «co-occurring condition: misophonia»; главная у авторов: no; период: current; заметка: Reported as a demographic characteristic.

**Ключевые поля выборки:**
- **n_analysed: 141** — Table 1; Methods, Participants — «141 autistic + ADHD (1 CloudResearch, 37 Prolific, and 103 SPARK)»
- **population: clinical** — Methods, Participants — «participants who were both autistic and ADHD (autistic + ADHD)»
- **sampling: convenience** — Methods, Participants — «Furthermore, many autistic participants were recruited from SPARK Research Match (Feliciano et al., 2018).»

**Остальные поля:**
- clinical_group: other: autism and ADHD (co-occurring) — Table 1 — «118 diagnosed (83.69%) ... 113 diagnosed (80.14%)»
- country: USA — Methods, Participants — «We recruited four groups of participants from the United States»
- setting: research registry (SPARK, 103) and online panels (Prolific 37, CloudResearch 1) — Methods, Participants — «141 autistic + ADHD (1 CloudResearch, 37 Prolific, and 103 SPARK)»
- data_years: NR — NR — «NR»
- design: cross-sectional — Discussion — «Although this study’s cross-sectional design cannot test causality»
- topic_disclosed: NR — R0441, p. 48 (4.7.1.3) — «derived from an online survey study examining attention, hyper-focus, and related constructs in adults with and without neurodevelopmental disabilities»
- inclusion_exclusion: US adults; diagnosed or self-identified autistic and ADHD; ASRS-6 >=10 (diagnosed ADHD) or >=14 (self-identified); RAADS-14 >=14; excluded uncorrected hearing loss, failed attention checks, poor/discrepant data — Methods, ASRS; RAADS-14 — «Autistic participants were excluded if they did not have RAADS-14 scores at or exceeding cut-off (14).»
- n_invited: NR — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study»
- n_responded: NR — Methods, Participants — «a total of 609 unique participants provided responses to the full survey»
- response_rate: NR — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study, of whom 416 agreed to share their information»
- age_mean: 35.46 — Table 1 — «35.46 (12.30) | 18.00–75.00»
- age_sd: 12.30 — Table 1 — «35.46 (12.30) | 18.00–75.00»
- age_min: 18 — Table 1 — «35.46 (12.30) | 18.00–75.00»
- age_max: 75 — Table 1 — «35.46 (12.30) | 18.00–75.00»
- age_group: adults — Abstract — «Four hundred ninety-two adults»
- pct_female: 56.74 — Table 1 (Sex) — «61 M (43.26%), 80 F (56.74%)»
- informant: self — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
- mode: online — R0441, p. 49 (4.7.1.3) — «Surveys were completed on the Qualtrics platform»
- instruments: Self-identified misophonia item with definition shown (English, ad hoc); MIST-A Misophonia subscale (English, 28-item development version, T-scores); Core Discriminant Sounds (CDS) sound-rating task — Table 1 note c; Methods, MIST-A; Sound Rating Measures — «In the case of misophonia only, participants were provided with a definition of misophonia»
- instrument_validated_in_language: no — Table 1 note c — «participants were provided with a definition of misophonia ... before being asked if they had the condition»
- pub_status: journal — Header — «venue: Journal of attention disorders; DOI: 10.1177/10870547251361226»
- language: English — Full text — «A Trans-Diagnostic Investigation of Attention and Diverse Phenotypes of “Auditory Hyperreactivity” in Autism, ADHD, and the General Population»
- funding_coi: NR — NR — «NR»
- notes: Autism (113/141) and ADHD (118/141) formally diagnosed; the rest self-identified. Same study as Dwyer et al. 2024 and the R0441 'NDD' sample (n=478). R0441 gives an NDD-wide misophonia count of 115/478 under a different definition, not split by group. JBI 3 passes only under the 139 threshold for clinical groups.

**Риск смещения (JBI):**
1. рамка выборки: **no** — SPARK registry and online panels cover only part of US autistic+ADHD adults — Methods, Participants — «many autistic participants were recruited from SPARK Research Match (Feliciano et al., 2018)»
2. способ отбора: **no** — Volunteer opt-in from registry and online panels — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study, of whom 416 agreed to share their information»
3. размер выборки: **yes** — n=141 >= 139 (clinical-group threshold applied; < 385 if the general threshold is used) — Table 1 — «141 autistic + ADHD (1 CloudResearch, 37 Prolific, and 103 SPARK)»
4. описание выборки и условий: **unclear** — Dates of data collection not reported — Table 1; Participants — «We recruited four groups of participants from the United States»
5. охват (пропуски): **unclear** — Percentages over full group n; missing-data handling not reported — Table 1 — «98 misophonia (69.50%)»
6. валидность определения случая: **no** — Ad hoc self-identification item — Table 1 note c — «participants were provided with a definition of misophonia»
7. единое надёжное измерение: **unclear** — Same item and mode; no reliability reported for the item — Table 1 note c — «Including self-reports of both self-identified and formally diagnosed co-occurring conditions, if current.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given; CI calculable — Table 1 — «98 misophonia (69.50%)»
9. отклик: **no** — SPARK uptake 416/2296 (18%); online panels without denominator; not handled — Methods, Participants — «Two thousand two hundred ninety-six SPARK participants were informed about the study, of whom 416 agreed to share their information»

Правки:
- 

Проверено: да
### ST005-5 · AUT: online survey of diagnosed or self-identified autistic adults, international (Australian-led), n=295
Отчёты: R0441 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-reported earlier professional diagnosis of misophonia (yes) | **L1** | **16 / 295** | 5.4 | Page 63, Suppl. Table 4.10 (AUT column); Page 52, 4.7.2 | «Misophonia ... 105 (7.48%) 336 (65.1%) 115 (24.1%) 16 (100.0%)» |

- E1: источник порога: study's own; правило: adhoc row: self-reported earlier professional diagnosis -> L1; G11 (no scale-based L1 estimate in this sample); у авторов: «Misophonia (previous diagnosis by a health professional)»; главная у авторов: no; период: lifetime; **расчёт: n = whole AUT sample (295), assuming every participant answered the diagnosis item. The authors' denominator was only the 16 diagnosed (non-diagnosed treated a…**; заметка: Denominator unclear: the authors did not compute a prevalence. Number of AUT participants who answered the diagnosis item is not reported.

**Ключевые поля выборки:**
- **n_analysed: 295** — Page 50 — «one of these individuals was additionally excluded due to reporting a severe hearing loss. Thus, a final sample of 295 individuals was included»
- **population: clinical** — Page 49, 4.7.1.4 — «a formal diagnosis of autism or self-identification as being on the autism-spectrum (even if not professionally diagnosed)»
- **sampling: snowball** — Page 49, 4.7.1.4 — «Diagnosed and self-identified autistic adults were recruited through snowball convenience sampling»

**Остальные поля:**
- clinical_group: autism — Page 49, 4.7.1.4; Page 63, Suppl. Table 4.10 — «Self-identified ... 95 (32.2%) ... Professionally diagnosed ... 200 (67.8%)»
- country: NR — Page 49, 4.7.1.4 — «respondents were not limited by country (although notably, the study was conducted by Australian researchers and therefore was more likely to recruit Australia…»
- setting: online survey; recruited through autism community networks and organizations (snowball) — Page 49, 4.7.1.4 — «recruited through snowball convenience sampling (Heckathorn, 2011), as well as leveraging existing networks and community organizations using online platforms …»
- data_years: NR — Page 49, 4.7.1.4 — «The AUT sample (n = 295) was derived from an online survey study specifically focusing on the auditory experiences of autistic adults»
- design: validation study — Page 4, 4.2.1; Page 33 — «the present study was a secondary data analysis of multiple heterogeneous studies»
- topic_disclosed: yes — Page 49, 4.7.1.4 — «an online survey study specifically focusing on the auditory experiences of autistic adults»
- inclusion_exclusion: Age >=18; formal autism diagnosis or self-identified autistic; any country; excluded if insufficient MIST-A data or severe hearing loss; no attention checks — Page 49-50, 4.7.1.4 — «Eligibility for the survey included (a) age 18 years or older and (b) a formal diagnosis of autism or self-identification as being on the autism-spectrum»
- n_invited: NR — Page 50 — «Of 484 individuals who initially attempted the survey»
- n_responded: 484 — Page 50 — «Of 484 individuals who initially attempted the survey, 296 individuals were found to have sufficient data on the MIST-A»
- response_rate: NR — Page 49-50 — «Of 484 individuals who initially attempted the survey»
- age_mean: 37.87 — Page 63, Suppl. Table 4.10 — «AUT (n=295) ... Age (Years) ... 37.87 (11.40)»
- age_sd: 11.40 — Page 63, Suppl. Table 4.10 — «37.87 (11.40)»
- age_min: NR — Page 49, 4.7.1.4 — «Eligibility for the survey included (a) age 18 years or older»
- age_max: NR — Page 49, 4.7.1.4 — «age 18 years or older»
- age_group: adults — Page 4, 4.2.1 — «all participants were adults over the age of 18, fluent in English, and able to consent for themselves»
- pct_female: 80.3 — Page 63, Suppl. Table 4.10 — «Male ... 56 (19.7%) ... Female ... 228 (80.3%)»
- informant: self — Page 49, 4.7.1.4 — «Participants in the study completed a 25–45 minute survey battery on the REDCap platform»
- mode: online — Page 49, 4.7.1.4 — «an online survey study ... completed a 25–45 minute survey battery on the REDCap platform»
- instruments: MIST-A development version (English; lacks items 15, 18, 20) Misophonia subscale, no counts reported for AUT; self-reported earlier professional diagnosis of misophonia (English, ad hoc item) — Page 5, 4.2.2.1; Page 52, 4.7.2 — «In the AUT sample, misophonia status was queried using previous diagnoses by a health professional only»
- instrument_validated_in_language: no — Page 52, 4.7.2 — «misophonia status was queried using previous diagnoses by a health professional only»
- pub_status: preprint — Job metadata; Page 1 — «CHAPTER 4 The Multidimensional Inventory of Sound Tolerance in Adults (MIST-A)»
- language: English — Full text — «The present study represents an initial attempt to fill this lacuna»
- funding_coi: NR — Page 5 — «procedures were approved by the institutional review board ... Macquarie University (AUT sample)»
- notes: Dissertation chapter (Williams) posted on PsyArXiv; pub_status could be coded thesis instead. Ethics approval from Macquarie University. The AUT sample did not complete the DMQ or DVMSQ. A MIST-A Misophonia T-score screening cut-off (>56.52, derived by ROC in the LAB sample) exists, but no counts are reported for AUT. Per the job brief, the AUT sample is reported nowhere else. It is separate from the 936-autistic-adult pilot sample of Chapters 2-3. The only misophonia case count is the number of self-reported professional diagnoses (16). Authors treated non-diagnosed participants as missing, …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target population is autistic adults; recruited through online networks and community organizations, with no defined frame — Page 49, 4.7.1.4 — «leveraging existing networks and community organizations using online platforms and word of mouth»
2. способ отбора: **no** — Snowball convenience sampling — Page 49, 4.7.1.4 — «recruited through snowball convenience sampling»
3. размер выборки: **no** — n=295 < 385. The whole sample is clinical, not a clinical subgroup, so the 385 rule was applied; the reviewer may judge otherwise — Page 50 — «a final sample of 295 individuals was included in the present study»
4. описание выборки и условий: **no** — Age, sex and setting are reported; country is not specified (any country, Australian-led) and data-collection dates are missing — Page 49, 4.7.1.4; Suppl. Table 4.10 — «respondents were not limited by country»
5. охват (пропуски): **no** — Of 484 who attempted the survey, 188 (39%) were excluded for insufficient MIST-A data; no handling. Missingness of the diagnosis item is not reported — Page 50 — «Of 484 individuals who initially attempted the survey, 296 individuals were found to have sufficient data on the MIST-A»
6. валидность определения случая: **no** — Only case definition is a self-reported earlier professional diagnosis (ad hoc) — Page 52, 4.7.2 — «In the AUT sample, misophonia status was queried using previous diagnoses by a health professional only»
7. единое надёжное измерение: **unclear** — Same online item for all, but no reliability reported for the diagnosis item — Page 52, 4.7.2 — «misophonia status was queried using previous diagnoses by a health professional only»
8. статистика (числитель и знаменатель): **no** — Numerator 16 given, but the authors treated non-diagnosed participants as missing (reported as 100.0%), so no prevalence denominator is defined and no CI is given — Page 63, Suppl. Table 4.10 — «Percentages reflect the percentage of non-missing values»
9. отклик: **no** — Open online snowball survey with no denominator of invited people; no non-response handling — Page 49-50, 4.7.1.4 — «No monetary incentives were offered for this survey, and thus, no attention check items were included»

Правки:
- 

Проверено: да
### ST005-6 · Prolific general-population adults, USA, n=1403
Отчёты: R0998 (main); R0441 (not attached; 'PROA')

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DVMSQ · DVMSQ algorithm: clinical (criteria A–D and F met) | **L2** | **102 / 1403** | 7.3 | Results, Participant characteristics; Discussion; Table 3 | «the prevalence of clinically significant misophonia was 7.3% (102/1403) in a sex-balanced crowdsourced sample from Prolific» |
| E2 | all | DVMSQ · DVMSQ algorithm: subclinical or clinical (criteria A–D met, with or without F) | **L1** | **246 / 1403** | 17.5 | Results, Participant characteristics | «Subclinical misophonia, defined as meeting all DVMSQ criteria except for the “impairment” criterion, was present in an additional 144 adults in the Prolific sample (10.2%)» |
| E3 | female | DVMSQ · DVMSQ algorithm: clinical | **L2** | **74 / 717** | 10.3 | Table 3 | «Female / 717 (51.1%) / 499 (59.9%) / 74 (72.5%)» |
| E4 | male | DVMSQ · DVMSQ algorithm: clinical | **L2** | **28 / 686** | 4.1 | Table 3 | «Male / 686 (48.9%) / 334 (40.1%) / 28 (27.5%)» |
| E5 | autism (self-reported diagnosis) | DVMSQ · DVMSQ algorithm: clinical | **L2** | **7 / 32** | 21.9 | Results, Participant characteristics | «a total of 102 individuals in the Prolific sample (7.3%, including 7 autistic adults) ... an additional 32 individuals from the Prolific sample (2.3% of total sample...) reported receiving professional diagnoses of auti…» |
| E6 | all | adhoc · self-reported previous professional diagnosis of misophonia | **L1** | **10 / 1403** | 0.7 | Results, Participant characteristics | «only 10 individuals in the Prolific sample (0.7%) and 21 individuals in the SPARK sample (2.2%) reported being previously diagnosed with misophonia by a professional» |
| E7 | all | DVMSQ · DVMSQ screening item S1 = Yes (specific sounds extremely bothersome) | **L0** | **833 / 1403** | 59.4 | Table 3; Results, Participant characteristics | «1478 of whom (Prolific: n = 833; SPARK: n = 645) affirmatively answered DVMSQ screening question S1» |

- E1: источник порога: developer paper; правило: DVMSQ row; L2 clinical algorithm; G10 denominator all screened; у авторов: «clinically significant misophonia»; главная у авторов: yes; период: current; заметка: Algorithm defined in this report; impairment items refer to past 7 days.
- E2: источник порога: developer paper; правило: DVMSQ row; L1 subclinical or clinical; G1 sum upward; у авторов: «subclinical misophonia + clinically significant misophonia»; главная у авторов: no; период: current; **расчёт: 102 clinical + 144 subclinical = 246**
- E3: источник порога: developer paper; правило: DVMSQ row; L2 clinical algorithm; у авторов: «clinical misophonia»; главная у авторов: no; период: current; заметка: Sex assigned at birth.
- E4: источник порога: developer paper; правило: DVMSQ row; L2 clinical algorithm; у авторов: «clinical misophonia»; главная у авторов: no; период: current; заметка: Sex assigned at birth.
- E5: источник порога: developer paper; правило: DVMSQ row; L2 clinical algorithm; у авторов: «clinically significant misophonia»; главная у авторов: no; период: current; заметка: Small subgroup found within the general-population sample.
- E6: источник порога: study's own; правило: adhoc row; L1 self-reported diagnosis; G11 (sample has scale-based L1); у авторов: «previously diagnosed with misophonia by a professional»; главная у авторов: no; период: lifetime; заметка: Not used for pooling because a scale-based L1 exists (G11).
- E7: источник порога: developer paper; правило: adhoc row L0 (any bothersome sound / trigger only); у авторов: «S1 positive»; главная у авторов: no; период: current; заметка: Screening item only; not a case definition.

**Ключевые поля выборки:**
- **n_analysed: 1403** — Methods, General population (Prolific) sample; Table 3 — «113 individuals (7.5%) were excluded for failing one or more data quality check, leaving a final sample of 1403 individuals»
- **population: gp_other** — Methods, Participants — «a large online general-population sample of adults in the United States (n = 1403) recruited from the Prolific crowdsourcing platform»
- **sampling: quota** — Methods, General population (Prolific) sample — «Participants were recruited in two single-sex batches of 750 (i.e., 750 males and 750 females, recruited concurrently) to ensure approximate sex parity.»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — Methods, General population (Prolific) sample — «Eligibility criteria included age 18 or older, living in the United States, speaking English fluently»
- setting: online panel (Prolific crowdsourcing platform) — Methods, Participants — «a large online general-population sample of adults in the United States (n = 1403) recruited from the Prolific crowdsourcing platform»
- data_years: 2021 — Methods, General population (Prolific) sample — «recruited from the Prolific crowdsourcing platform (Palan and Schitter, 2018; Stanton et al., 2022) in the fall of 2021»
- design: validation study — Abstract — «The purpose of the current study was to introduce and psychometrically validate the duke-vanderbilt Misophonia Screening Questionnaire (DVMSQ)»
- topic_disclosed: no — Methods, General population (Prolific) sample — «The study survey was advertised as examining “sensory sensitivities,” although participant-facing materials did not specify that the study investigated decreas…»
- inclusion_exclusion: Age >=18, US resident, fluent English, answered Prolific autism/mental-health items, no dementia/MCI, >=50 prior Prolific tasks, >=95% approval; excluded severe/profound hearing loss or cochlear implant (post hoc) and failed data-quality checks — Methods, General population (Prolific) sample — «Individuals endorsing severe/profound hearing loss or the use of cochlear implants were also excluded from the current study post hoc.»
- n_invited: NR — Methods, General population (Prolific) sample — «Of the 1610 individuals who consented for the study, 1516 individuals completed the full Prolific survey»
- n_responded: 1516 — Methods, General population (Prolific) sample — «Of the 1610 individuals who consented for the study, 1516 individuals completed the full Prolific survey and had their submissions approved.»
- response_rate: NR — Methods, General population (Prolific) sample — «Of the 1610 individuals who consented for the study, 1516 individuals completed the full Prolific survey»
- age_mean: 32.27 — Results, Participant characteristics; Table 3 — «those in the Prolific sample (mean [SD] age = 32.27 [12.55] years)»
- age_sd: 12.55 — Results, Participant characteristics; Table 3 — «those in the Prolific sample (mean [SD] age = 32.27 [12.55] years)»
- age_min: 18 — Methods (eligibility); Results, Participant characteristics — «Adults in the current study ranged from 18 to 83 years old»
- age_max: 83 — R0998 Results, Participant characteristics; R0652 p.16 — «Adults in the current study ranged from 18 to 83 years old [combined samples]; R0652: autistic adults ... age range 18–80 years»
- age_group: adults — Methods, General population (Prolific) sample — «Eligibility criteria included age 18 or older»
- pct_female: 51.1 — Table 3 — «Female | 717 (51.1%)»
- informant: self — Abstract — «a novel self-report measure of misophonia symptoms»
- mode: online — Methods, General population (Prolific) sample — «surveys were completed on the REDCap platform (Harris et al., 2009)»
- instruments: DVMSQ (original 21-item version, English); abbreviated DMQ (trigger list, frequency item, 23-item Symptom Scale, global impairment VAS; English) — Methods, Measures — «The version of the DVMSQ administered to the Prolific and SPARK cohorts contained 21 items (one Yes/No “screening” item and 20 Likert items)»
- instrument_validated_in_language: yes — Abstract; Discussion — «Employing large online samples of general population adults (n = 1403) and adults on the autism spectrum (n = 936), we rigorously evaluated the internal struct…»
- pub_status: journal — Header — «Year: 2022; venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2022.897901»
- language: English — Full text — «Psychometric validation of a brief self-report measure of misophonia symptoms and functional impairment»
- funding_coi: Funding source not named in the main text provided (TW and CC 'obtained funding'). COI: ZW consulting fees from Roche and Autism Speaks; TW parent of an autistic adult. — Author contributions; Conflict of interest — «ZW was received consulting fees from Roche and Autism Speaks.»
- notes: The English DVMSQ is validated in this same report (developer/validation paper). Its clinical algorithm is theory-based, with no interview or ROC anchoring; the authors say criterion validity was not tested. The authors note prevalence may be overestimated through self-selection (survey advertised as 'sensory sensitivities'). The same Prolific sample appears as 'PROA' in dissertation R0441 (not attached). 32 participants (2.3%) self-reported an autism diagnosis. age_max 83 is derived: the combined range is 18–83 (R0998) and the SPARK range is 18–80 (R0652), so the 83-year-old must be in Proli…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is US general adult population; frame is Prolific crowdworkers with high approval ratings. — Methods, General population (Prolific) sample — «having completed at least 50 previous Prolific tasks, and a 95% or higher approval rate on Prolific»
2. способ отбора: **no** — Opt-in online panel with sex quotas; non-probability. — Methods, General population (Prolific) sample — «Participants were recruited in two single-sex batches of 750»
3. размер выборки: **yes** — n = 1403 >= 385. — Table 3 — «Sample size | 1403»
4. описание выборки и условий: **yes** — Age, sex, setting (Prolific online), country (USA) and dates (fall 2021) reported. — Methods; Table 3 — «recruited from the Prolific crowdsourcing platform ... in the fall of 2021»
5. охват (пропуски): **yes** — Prevalence computed over all 1403 retained; 7.5% excluded for data quality (handled). — Discussion — «the prevalence of clinically significant misophonia was 7.3% (102/1403)»
6. валидность определения случая: **yes** — Primary estimate uses DVMSQ algorithm (listed as valid), English version validated in this report; note no interview anchoring. — Table 2; Results — «Based on the DVMSQ algorithm, a total of 102 individuals in the Prolific sample (7.3%...) met criteria for clinically significant misophonia.»
7. единое надёжное измерение: **yes** — Same online instrument and algorithm for all; reliability reported in sample. — Results, All DVMSQ items — «reliability of the DVMSQ total score was very high in both samples (Prolific: ωT = 0.977; SPARK: ωT = 0.957»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given; CI calculable; no weighting design. — Discussion — «7.3% (102/1403) in a sex-balanced crowdsourced sample from Prolific»
9. отклик: **no** — Open Prolific recruitment; number invited not reported; no non-response handling. — Methods, General population (Prolific) sample — «Of the 1610 individuals who consented for the study, 1516 individuals completed the full Prolific survey»

Правки:
- 

Проверено: да
### ST005-7 · SPARK independent autistic adults, USA, n=936
Отчёты: R0998 (main); R0652; R0440; R0441 (not attached)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DVMSQ · DVMSQ algorithm: clinical (criteria A–D and F met) | **L2** | **332 / 936** | 35.5 | R0998 Discussion; Table 3; R0652 p.17 | «35.5% (332/936) in a female-predominant sample of independent autistic adults recruited from the SPARK cohort» |
| E2 | all | DVMSQ · DVMSQ algorithm: subclinical or clinical (criteria A–D met, with or without F) | **L1** | **429 / 936** | 45.8 | Results, Participant characteristics | «Subclinical misophonia ... was present in an additional 144 adults in the Prolific sample (10.2%) and 97 adults in the SPARK sample (10.4%).» |
| E3 | female | DVMSQ · DVMSQ algorithm: clinical | **L2** | **261 / 590** | 44.2 | Table 3; Discussion | «Female / ... / 590 (63.0%) / 463 (71.6%) / 261 (78.6%); (44.2% of autistic females and 20.5% of autistic males)» |
| E4 | male | DVMSQ · DVMSQ algorithm: clinical | **L2** | **71 / 346** | 20.5 | Table 3; Discussion | «Male / ... / 346 (37.0%) / 184 (28.4%) / 71 (21.4%)» |
| E5 | all | adhoc · self-reported previous professional diagnosis of misophonia | **L1** | **21 / 936** | 2.2 | Results, Participant characteristics | «21 individuals in the SPARK sample (2.2%) reported being previously diagnosed with misophonia by a professional» |
| E6 | all | DVMSQ · DVMSQ screening item S1 = Yes (specific sounds extremely bothersome) | **L0** | **647 / 936** | 69.1 | Table 3 | «Sample size / 1403 / 833 / 102 / 936 / 647 / 332» |

- E1: источник порога: developer paper; правило: DVMSQ row; L2 clinical algorithm; G10 denominator all screened; у авторов: «clinically significant misophonia»; главная у авторов: yes; период: current; взвешенная доля: 29.1; заметка: weighted_pct from R0652: sex-weighted using an estimated 3:1 male:female autism ratio (not survey weights): 'sex-weighted prevalence: 29.1%'.
- E2: источник порога: developer paper; правило: DVMSQ row; L1 subclinical or clinical; G1 sum upward; у авторов: «subclinical misophonia + clinically significant misophonia»; главная у авторов: no; период: current; **расчёт: 332 clinical + 97 subclinical = 429**
- E3: источник порога: developer paper; правило: DVMSQ row; L2 clinical algorithm; у авторов: «clinical misophonia»; главная у авторов: no; период: current; заметка: Sex assigned at birth.
- E4: источник порога: developer paper; правило: DVMSQ row; L2 clinical algorithm; у авторов: «clinical misophonia»; главная у авторов: no; период: current; заметка: Sex assigned at birth.
- E5: источник порога: study's own; правило: adhoc row; L1 self-reported diagnosis; G11 (sample has scale-based L1); у авторов: «previously diagnosed with misophonia by a professional»; главная у авторов: no; период: lifetime; заметка: Not used for pooling because a scale-based L1 exists (G11).
- E6: источник порога: developer paper; правило: adhoc row L0 (any bothersome sound / trigger only); у авторов: «S1 positive»; главная у авторов: no; период: current; заметка: Table 3 gives 647; text says 645 S1-positive completed the full measure; R0652 Table 1 gives 69.1%.

**Ключевые поля выборки:**
- **n_analysed: 936** — Methods, Autistic (SPARK) sample; Table 3 — «an additional 185 (16.5%) were excluded after failing one or more data quality checks, leaving a final sample of 936 autistic adults»
- **population: clinical** — Methods, Autistic (SPARK) sample — «self-reported professional diagnoses of autism spectrum disorder or equivalent conditions»
- **sampling: convenience** — Methods, Autistic (SPARK) sample — «A sample of legally independent autistic adults was recruited from the SPARK Research Match service»

**Остальные поля:**
- clinical_group: autism — Methods, Autistic (SPARK) sample — «self-reported professional diagnoses of autism spectrum disorder or equivalent conditions (e.g., Asperger syndrome, Pervasive Developmental Disorder–Not Otherw…»
- country: USA — R0652, References 39 / Supplemental Methods — «SPARK: A US cohort of 50,000 families to accelerate autism research.»
- setting: online research registry (SPARK Research Match) — Methods, Autistic (SPARK) sample — «A sample of legally independent autistic adults was recruited from the SPARK Research Match service»
- data_years: 2021 — R0652, p.8 — «were recruited during Spring 2021 from the Simons Foundation Powering Autism Research for Knowledge (SPARK)39 cohort»
- design: validation study — Methods, Participants — «The current study comprises a secondary data analysis of two large survey studies that included the DVMSQ»
- topic_disclosed: no — R0652, Supplemental Methods p.S2 — «the study was not advertised as a specific study of hearing disorders or “sound sensitivity” and was instead given a vague title (“Investigating Relationships …»
- inclusion_exclusion: Age >=18, self-reported professional autism diagnosis, legally independent; excluded possibly invalid diagnosis, inconsistent demographics, cochlear implant, Alzheimer's/DID infrequency items, dropout before DVMSQ — Methods, Autistic (SPARK) sample — «Eligibility criteria included age 18 or older, self-reported professional diagnoses of autism spectrum disorder ... and legal independence»
- n_invited: NR — Methods, Autistic (SPARK) sample — «Of the 1271 individuals who initially consented for the study, 1121 completed the measures of interest.»
- n_responded: 1121 — Methods, Autistic (SPARK) sample — «Of the 1271 individuals who initially consented for the study, 1121 completed the measures of interest.»
- response_rate: NR — Methods, Autistic (SPARK) sample — «Of the 1271 individuals who initially consented for the study»
- age_mean: 37.49 — Results, Participant characteristics; Table 3 — «participants in the SPARK sample (mean [SD] age = 37.49 [13.28] years)»
- age_sd: 13.28 — Results, Participant characteristics; Table 3 — «participants in the SPARK sample (mean [SD] age = 37.49 [13.28] years)»
- age_min: 18 — R0652, p.16 — «autistic adults in the present study (n=936, mean age 37.49 years, age range 18–80 years)»
- age_max: 80 — R0652, p.16 — «autistic adults in the present study (n=936, mean age 37.49 years, age range 18–80 years)»
- age_group: adults — Methods, Autistic (SPARK) sample — «Eligibility criteria included age 18 or older»
- pct_female: 63.0 — Table 3 — «Female | ... | 590 (63.0%)»
- informant: self — Methods, Autistic (SPARK) sample — «These participants completed a series of online surveys»
- mode: online — Methods, Autistic (SPARK) sample — «Surveys were completed within the SPARK web platform using custom software designed by Tempus Dynamics»
- instruments: DVMSQ (original 21-item version, English); abbreviated DMQ (trigger list, frequency item, Symptom Scale, global impairment VAS, Impairment Scale; English) — Methods, Measures; R0652 p.12-13 — «SPARK participants also completed the DMQ Impairment Scale (12 items), but ... this scale was not examined in our analyses.»
- instrument_validated_in_language: yes — Abstract; Discussion — «As the DVMSQ is the first measure of misophonia symptoms and impairment validated for use in the autistic population»
- pub_status: journal — Header — «Year: 2022; venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2022.897901»
- language: English — Full text — «Psychometric validation of a brief self-report measure of misophonia symptoms and functional impairment»
- funding_coi: R0652: REAM Foundation Misophonia Research Fund, NIDCD F30-DC019510, NIGMS T32-GM007347, VICTR (UL1-TR002243); funders had no role. COI: ZW consulting fees from Roche and Autism Speaks; TW parent of an autistic adult. — R0652, Funding p.31; R0998 Conflict of interest — «This project was completed with the support of the Misophonia Research Fund of the REAM Foundation (PI Woynaroski)»
- notes: The same SPARK sample is reported in R0652 (prevalence), R0440 and dissertation R0441, and largely overlaps an earlier SPARK paper (Williams et al. 2022/2023, PROMIS). One funder is a misophonia research fund. Autism diagnoses are self-reported, not confirmed. R0652 gives a sex-weighted prevalence of 29.1%, using a 3:1 male:female autism ratio. R0652 also reports DMQ-IMP impairment bands among the 332 cases (3.0% none, 23.2% mild, 62.7% moderate, 11.1% severe); these are within the case group only, so not extracted as a prevalence. Two-stage design: DVMSQ items went only to S1-positive partic…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is (cognitively able) autistic adults; frame is SPARK Research Match registry volunteers only. — Methods, Autistic (SPARK) sample — «recruited from the SPARK Research Match service (Project No. RM0111Woynaroski_DST)»
2. способ отбора: **no** — Volunteer opt-in from registry; non-probability. — R0652, p.27 — «this study was limited in its demographics to a fairly unrepresentative group of autistic adults»
3. размер выборки: **yes** — n = 936 (>=385 and >=139). — Table 3 — «Sample size | ... | 936»
4. описание выборки и условий: **yes** — Age, sex, setting, country (US cohort) and dates (Spring 2021, R0652) reported. — Table 3; R0652 p.8 — «were recruited during Spring 2021 from the Simons Foundation Powering Autism Research for Knowledge (SPARK)»
5. охват (пропуски): **unclear** — Dropouts before the DVMSQ excluded: 150/1271 (11.8%) per main text vs 108 per R0652 (8.5%); not handled; counts inconsistent. — Methods, Autistic (SPARK) sample; R0652 Supplemental Methods — «individuals who dropped out of the study before completing the DVMSQ and other sound tolerance measures were not included in the current analyses»
6. валидность определения случая: **yes** — DVMSQ algorithm (listed as valid), English, validated in autistic adults in this report; no interview anchoring. — Results, Participant characteristics — «332 individuals in the SPARK sample (35.5%) met criteria for clinically significant misophonia»
7. единое надёжное измерение: **yes** — Same online instrument/algorithm for all; reliability reported in sample. — Results, All DVMSQ items — «reliability of the DVMSQ total score was very high in both samples (Prolific: ωT = 0.977; SPARK: ωT = 0.957»
8. статистика (числитель и знаменатель): **yes** — Numerator/denominator clear; CI calculable; sex-weighted estimate also given. — Discussion — «35.5% (332/936) in a female-predominant sample of independent autistic adults recruited from the SPARK cohort»
9. отклик: **unclear** — Invitations via Research Match, but number invited not reported; no non-responder comparison. — Methods, Autistic (SPARK) sample — «Of the 1271 individuals who initially consented for the study, 1121 completed the measures of interest.»

Правки:
- 

Проверено: да
---

## ST006 · Enomoto 2026 · PsyArXiv

Основной отчёт R0058: [текст](../../fulltext/text/R0058.txt) · [PDF](../../fulltext/pdf/R0058.pdf) — «Development and Validation of the Japanese Version of the Amsterdam Misophonia Scale (A-MISO-S-J)» — [DOI](https://doi.org/10.31234/osf.io/er4f3_v1)
Не выписано ИИ: Study 2 (R0058, Section 3, pp. 15-16): Freeasy online survey company panel, Japan, May 2024; n=142 at T1 and 120 at T2 (4 weeks later). It is not an E1 exclusion, because the sample is general adults. It is not extracted because it reports no prevalence or severity-band data, only test-retest correlations (r = .67). A reviewer may prefer to list it as an eligible sample with no estimates. No groups recruited for misophonia were sampled. The 5 people with misophonia symptoms in the cognitive debriefing were not a survey sample.
Расхождения в тексте: Table 3 band counts add up to 265 (male 34+55+32+7+0=128; female 30+50+51+4+2=137), which matches the text (128 men, 137 women). The text says 76% have score 5-24, and 201/265 = 75.8%, so the two agree. Table 3 percentages add up to 100.1% because of rounding. In the Discussion (pp. 18-19), the 76% is called the 'clinical range (mild-to-severe)', but the definition actually covers mild to extreme (5-24). Section 2.3.2 says 'we decided to exclude the item [6]' but then says 'no additional items were deleted' and keeps all six items. The six-item scale (0-24) was used for the severity classification. The Methods give an RMSEA cut-off of <0.10, but the Results compare against 0.08. Neither affects the prevalence counts.
Заметка ИИ: I extracted one sample (Study 1, n=265). The authors' main estimate uses A-MISO-S >=5, which is L1 under Table 1. I derived the L2 estimate (>=10: 96/265) from the Table 3 bands. JBI item 6 is rated on the L2 definition. The only validation of the Japanese version is this same preprint, which has not been peer reviewed, so please check instrument_validated_in_language and JBI 6.

### ST006-1 · Study 1: CrowdWorks crowdsourcing adults, Japan, n=265
Отчёты: R0058 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **201 / 265** | 75.8 | Page 32, Table 3; Page 13, 2.3.4 | «Overall, 76% of the 265 respondents had clinically significant misophonia (total score: 5–24)» |
| E2 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **96 / 265** | 36.2 | Page 32, Table 3 | «Moderate (Total Score 10–14) 83（31.3） ... Severe (Total Score 15–19) 11（4.2） ... Extreme (Total Score 20–24) 2（0.8）» |
| E3 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **13 / 265** | 4.9 | Page 32, Table 3 | «Severe (Total Score 15–19) 11（4.2） ... Extreme (Total Score 20–24) 2（0.8）» |
| E4 | all | A-MISO-S · A-MISO-S>=20 | **L2** | **2 / 265** | 0.8 | Page 32, Table 3 | «Extreme (Total Score 20–24) 2（0.8）» |
| E5 | male | A-MISO-S · A-MISO-S>=5 | **L1** | **94 / 128** | 73.4 | Page 32, Table 3 | «Mild (Total Score 5–9) 105（39.6） 55 50 Moderate (Total Score 10–14) 83（31.3） 32 51 Severe (Total Score 15–19) 11（4.2） 7 4 Extreme (Total Score 20–24) 2（0.8） 0 2» |
| E6 | male | A-MISO-S · A-MISO-S>=10 | **L2** | **39 / 128** | 30.5 | Page 32, Table 3 | «Moderate (Total Score 10–14) 83（31.3） 32 51 Severe (Total Score 15–19) 11（4.2） 7 4 Extreme (Total Score 20–24) 2（0.8） 0 2» |
| E7 | male | A-MISO-S · A-MISO-S>=15 | **L2** | **7 / 128** | 5.5 | Page 32, Table 3 | «Severe (Total Score 15–19) 11（4.2） 7 4 Extreme (Total Score 20–24) 2（0.8） 0 2» |
| E8 | male | A-MISO-S · A-MISO-S>=20 | **L2** | **0 / 128** | 0.0 | Page 32, Table 3 | «Extreme (Total Score 20–24) 2（0.8） 0 2» |
| E9 | female | A-MISO-S · A-MISO-S>=5 | **L1** | **107 / 137** | 78.1 | Page 32, Table 3 | «Mild (Total Score 5–9) 105（39.6） 55 50 Moderate (Total Score 10–14) 83（31.3） 32 51 Severe (Total Score 15–19) 11（4.2） 7 4 Extreme (Total Score 20–24) 2（0.8） 0 2» |
| E10 | female | A-MISO-S · A-MISO-S>=10 | **L2** | **57 / 137** | 41.6 | Page 32, Table 3 | «Moderate (Total Score 10–14) 83（31.3） 32 51 Severe (Total Score 15–19) 11（4.2） 7 4 Extreme (Total Score 20–24) 2（0.8） 0 2» |
| E11 | female | A-MISO-S · A-MISO-S>=15 | **L2** | **6 / 137** | 4.4 | Page 32, Table 3 | «Severe (Total Score 15–19) 11（4.2） 7 4 Extreme (Total Score 20–24) 2（0.8） 0 2» |
| E12 | female | A-MISO-S · A-MISO-S>=20 | **L2** | **2 / 137** | 1.5 | Page 32, Table 3 | «Extreme (Total Score 20–24) 2（0.8） 0 2» |

- E1: источник порога: developer paper; правило: A-MISO-S row L1 >=5; G1 sum of bands; у авторов: «clinically significant misophonia»; главная у авторов: yes; период: NR; **расчёт: 105 + 83 + 11 + 2 from Table 3 (= 75.8%; text reports 76%)**
- E2: источник порога: developer paper; правило: A-MISO-S row L2 >=10 (recommended); G1 sum of bands; у авторов: «moderate or more (Moderate + Severe + Extreme)»; главная у авторов: no; период: NR; **расчёт: 83 + 11 + 2 from Table 3**; заметка: Recommended L2 definition (G11).
- E3: источник порога: developer paper; правило: A-MISO-S row >=15; G1 sum of bands; G2; у авторов: «severe or more (Severe + Extreme)»; главная у авторов: no; период: NR; **расчёт: 11 + 2 from Table 3**
- E4: источник порога: developer paper; правило: A-MISO-S row; G1 top band; G2 above L2 cut-off; у авторов: «Extreme»; главная у авторов: no; период: NR
- E5: источник порога: developer paper; правило: A-MISO-S row L1 >=5; G1 sum of bands; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; **расчёт: 55 + 32 + 7 + 0 from Table 3 (Male column); n = 34+55+32+7+0 = 128**
- E6: источник порога: developer paper; правило: A-MISO-S row L2 >=10; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: NR; **расчёт: 32 + 7 + 0 from Table 3 (Male column)**
- E7: источник порога: developer paper; правило: A-MISO-S row >=15; G1; G2; у авторов: «severe or more»; главная у авторов: no; период: NR; **расчёт: 7 + 0 from Table 3 (Male column)**
- E8: источник порога: developer paper; правило: A-MISO-S row; G1 top band; G2; у авторов: «Extreme»; главная у авторов: no; период: NR
- E9: источник порога: developer paper; правило: A-MISO-S row L1 >=5; G1 sum of bands; у авторов: «clinically significant misophonia»; главная у авторов: no; период: NR; **расчёт: 50 + 51 + 4 + 2 from Table 3 (Female column); n = 30+50+51+4+2 = 137**
- E10: источник порога: developer paper; правило: A-MISO-S row L2 >=10; G1 sum of bands; у авторов: «moderate or more»; главная у авторов: no; период: NR; **расчёт: 51 + 4 + 2 from Table 3 (Female column)**
- E11: источник порога: developer paper; правило: A-MISO-S row >=15; G1; G2; у авторов: «severe or more»; главная у авторов: no; период: NR; **расчёт: 4 + 2 from Table 3 (Female column)**
- E12: источник порога: developer paper; правило: A-MISO-S row; G1 top band; G2; у авторов: «Extreme»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 265** — Page 6, 2.2.2; Page 32, Table 3 — «Data from 265 general adults (128 men, 137 women; mean age = 40.78 years, SD = 9.94, range = 20–68) were analyzed.»
- **population: gp_other** — Page 6, 2.2.2 Sample — «Data from 265 general adults (128 men, 137 women; mean age = 40.78 years, SD = 9.94, range = 20–68) were analyzed.»
- **sampling: convenience** — Page 6, 2.2.2 Sample — «Participants were recruited via a crowdsourcing service (CrowdWorks).»

**Остальные поля:**
- clinical_group: NA — Page 6, 2.2.2 Sample — «Data from 265 general adults»
- country: JPN — Page 6, 2.2.2 Sample; Page 18, 4.3 — «This study revealed a high prevalence of misophonia among Japanese adults.»
- setting: online panel (crowdsourcing service CrowdWorks; survey on Qualtrics) — Page 6, 2.2.2 Sample — «An online survey was conducted in November 2023. Participants were recruited via a crowdsourcing service (CrowdWorks).»
- data_years: 2023 — Page 6, 2.2.2 Sample — «An online survey was conducted in November 2023.»
- design: validation study — Page 5, 2.1 Objective — «The objectives of Study 1 were to examine the factor structure of the Japanese version of the Amsterdam Misophonia Scale (A-MISO-S-J), evaluate its reliability»
- topic_disclosed: NR — Page 6, 2.2.2 Sample — «Participants were recruited via a crowdsourcing service (CrowdWorks). The survey platform Qualtrics (https://www. qualtrics.com/ja/) was used to collect the re…»
- inclusion_exclusion: NR (general adults registered with CrowdWorks; no explicit criteria reported) — Page 6, 2.2.2 Sample — «Data from 265 general adults (128 men, 137 women; mean age = 40.78 years, SD = 9.94, range = 20–68) were analyzed.»
- n_invited: NR — Page 6, 2.2.2 Sample — «Participants were recruited via a crowdsourcing service (CrowdWorks).»
- n_responded: NR — Page 6, 2.2.2 Sample — «Data from 265 general adults ... were analyzed.»
- response_rate: NR — Page 6, 2.2.2 Sample — «Participants were recruited via a crowdsourcing service (CrowdWorks).»
- age_mean: 40.78 — Page 6, 2.2.2 Sample — «mean age = 40.78 years, SD = 9.94, range = 20–68»
- age_sd: 9.94 — Page 6, 2.2.2 Sample — «mean age = 40.78 years, SD = 9.94, range = 20–68»
- age_min: 20 — Page 6, 2.2.2 Sample — «mean age = 40.78 years, SD = 9.94, range = 20–68»
- age_max: 68 — Page 6, 2.2.2 Sample — «mean age = 40.78 years, SD = 9.94, range = 20–68»
- age_group: adults — Page 6, 2.2.2 Sample — «265 general adults ... range = 20–68»
- pct_female: 51.7 — Page 6, 2.2.2 Sample — «265 general adults (128 men, 137 women»
- informant: self — Page 6, 2.2.2 Sample; Page 7, Measures — «An online survey was conducted in November 2023.»
- mode: online — Page 6, 2.2.2 Sample — «An online survey was conducted in November 2023. ... The survey platform Qualtrics ... was used to collect the responses.»
- instruments: A-MISO-S-J (Japanese version of the Amsterdam Misophonia Scale, developed in this study) — Page 7, 2.2.3 Measures — «The A-MISO-S-J, translated by the authors using the procedure described previously, was used to measure the severity of misophonia.»
- instrument_validated_in_language: yes — Page 13, 2.3.3.2; Page 21 — «This study provides evidence that the reliability and validity of the A-MISO-S-J are adequate.»
- pub_status: preprint — Page 1, header; venue PsyArXiv — «PREPRINT WITHOUT PEER-REVIEW»
- language: English — Full text — «Development and Validation of the Japanese Version of the Amsterdam Misophonia Scale (A-MISO-S-J)»
- funding_coi: JST SPRING (grant JPMJSP2124); authors declare no conflicts of interest (co-author Schröder developed the original A-MISO-S) — Page 22, Funding; Declaration of competing interest — «The authors declare no conflicts of interest. Funding This study was supported by JST SPRING (grant number JPMJSP2124).»
- notes: pct_female computed as 137/265 = 51.7%. The Japanese-version validation is this same report, a non-peer-reviewed preprint (no external validation cited). Topic disclosure not reported. Authors' primary prevalence (76%) uses A-MISO-S >=5 ('clinically significant'), which is L1 by our rules; L2 (>=10) is derived from Table 3. Time frame of A-MISO-S-J items not stated. Number of people who started the survey/were excluded not reported. Authors themselves note possible selection bias (crowdsourced, remote workers).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is Japanese adults; frame was registrants of one crowdsourcing service, covering only part of the population. — Page 6, 2.2.2; Page 21, limitations — «the sample may have been biased because the participants were recruited through a crowdsourcing service.»
2. способ отбора: **no** — Volunteer opt-in convenience sample from a crowdsourcing platform. — Page 6, 2.2.2 Sample — «Participants were recruited via a crowdsourcing service (CrowdWorks).»
3. размер выборки: **no** — n = 265 < 385. — Page 6, 2.2.2 Sample — «Data from 265 general adults ... were analyzed.»
4. описание выборки и условий: **yes** — Age, sex, setting (online crowdsourcing), country (Japan) and date (November 2023) reported. — Page 6, 2.2.2 Sample — «An online survey was conducted in November 2023. ... 265 general adults (128 men, 137 women; mean age = 40.78 years, SD = 9.94, range = 20–68)»
5. охват (пропуски): **unclear** — Only analysed n reported; number of initial respondents and any exclusions/missing data not reported. — Page 6, 2.2.2 Sample — «Data from 265 general adults ... were analyzed.»
6. валидность определения случая: **yes** — L2 definition A-MISO-S >=10 (anchored cut-off) on a Japanese version validated in this report (preprint); authors' own primary >=5 would be 'no'. — Page 7, Measures; Page 32, Table 3 — «0–4 = subclinical, 5–9 = mild, 10–14 = moderate, 15–19 = severe, and 20–24 = extreme [1].»
7. единое надёжное измерение: **yes** — Same self-report online instrument and thresholds for all; Cronbach's alpha 0.83, omega 0.84 in sample. — Page 13, 2.3.3.2 — «Cronbach’s alpha for the A-MISO-S-J was 0.83, and the McDonald’s omega value was 0.84.»
8. статистика (числитель и знаменатель): **yes** — Band counts with total n = 265 given; numerators and denominators traceable; CI calculable. — Page 32, Table 3 — «Subclinical (Total Score 0–4) 64（24.2） ... Mild (Total Score 5–9) 105（39.6） ... Note. n = 265.»
9. отклик: **no** — Open crowdsourcing recruitment with no denominator of invited people; non-response not handled. — Page 6, 2.2.2 Sample — «Participants were recruited via a crowdsourcing service (CrowdWorks).»

Правки:
- 

Проверено: да
---

## ST007 · Erfanian 2026 · bioRxiv

Основной отчёт R0061: [текст](../../fulltext/text/R0061.txt) · [PDF](../../fulltext/pdf/R0061.pdf) — «Social-Cognitive Dysregulation Model of Misophonia: Perspective from a Behavioural Study» — [DOI](https://doi.org/10.64898/2026.09.03.749152)
Расхождения в тексте: The 717 recruited minus 376 excluded equals 341 analysed, which is consistent. The S-Five >=87 count is 195 of 341 (p.10) and 188 of 332 among those with mimicry data (p.15). These are different denominators, not a contradiction. However, p.11 says all questionnaire responses were complete ('forced-response settings'), but mimicry data were available for only 332 of 341 and S-Five alpha was computed on N = 338. Age and sex were available for 329 of 341; pct_female is based on 329.
Заметка ИИ: This is a correlational behavioural study, not a prevalence study. The prevalence of S-Five >=87 comes from the reported split of the analytic sample (146 below, 195 at or above). Country and data-collection dates are not reported.

### ST007-1 · Prolific online adults, English speakers, n=341 (Erfanian & Kumar 2026)
Отчёты: R0061 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | S-Five · S-Five total >=87 | **L2** | **195 / 341** | 57.2 | Page 10, 2.3 Procedure; Figure 1B | «yielding a final analytic sample of N = 341, including 146 below and 195 above cutoff threshold (≥87) (Vitoratou et al., 2023) (Figure 1B)» |

- E1: источник порога: validation paper; правило: S-Five row; L2 >=87; у авторов: «above cutoff threshold (≥87); clinically elevated misophonia»; главная у авторов: no; период: NR; заметка: 57.2%. Primary analyses were dimensional. In the subset with mimicry data (N = 332), 188 had S-Five >=87 (p.15). Possible enrichment for misophonia (see sample notes).

**Ключевые поля выборки:**
- **n_analysed: 341** — Page 10, 2.3 Procedure — «(N = 376), yielding a final analytic sample of N = 341»
- **population: gp_other** — Page 5, 2.1 Participants — «Participants were recruited through Prolific (www.prolific.com), an online research-participant platform»
- **sampling: convenience** — Page 9, 2.3 Procedure — «Eligible participants viewed a study advertisement outlining the procedures and compensation of approximately £4»

**Остальные поля:**
- clinical_group: NA — Page 9, 2.3 Procedure — «Prespecified eligibility criteria were age 18–60 years, no self-reported hearing loss»
- country: NR — Page 9, 2.3 Procedure — «Prespecified eligibility criteria were age 18–60 years, ... and being native or bilingual English speaker.»
- setting: online panel (Prolific; tasks on Gorilla Experiment Builder) — Page 5, 2.1 Participants — «Participants were recruited through Prolific (www.prolific.com), an online research-participant platform»
- data_years: NR — Page 5, 2. Method — «The study was preregistered on Open Science Framework (OSF) [https://osf.io/vjkfx] before the data collection.»
- design: cross-sectional — Page 20, 4.5 Limitations — «First, the cross-sectional design precludes causal inference»
- topic_disclosed: NR — Page 9, 2.3 Procedure — «Eligible participants viewed a study advertisement outlining the procedures and compensation of approximately £4»
- inclusion_exclusion: Age 18-60; no self-reported hearing loss/difficulties; no cognitive impairment/dementia; normal or corrected vision; native/bilingual English. Excluded: incomplete task or questionnaire data, multiple attempts. — Page 9, 2.3; Page 10 — «Prespecified eligibility criteria were age 18–60 years, no self-reported hearing loss or hearing difficulties, no cognitive impairment or dementia, normal or c…»
- n_invited: NR — Page 9, 2.3 Procedure — «Eligible participants viewed a study advertisement»
- n_responded: 717 — Page 10, 2.3 Procedure — «A total of 717 participants were recruited.»
- response_rate: NR — Page 10, 2.3 Procedure — «A total of 717 participants were recruited. Participants were excluded for incomplete behavioural-task data, multiple participation attempts, or incomplete que…»
- age_mean: 34.68 — Page 5, 2.1 Participants — «The sample comprised 341 participants (Meanage = 34.68 years, SD = 10.02).»
- age_sd: 10.02 — Page 5, 2.1 Participants — «(Meanage = 34.68 years, SD = 10.02)»
- age_min: NR — Page 9, 2.3 Procedure — «Prespecified eligibility criteria were age 18–60 years»
- age_max: NR — Page 9, 2.3 Procedure — «Prespecified eligibility criteria were age 18–60 years»
- age_group: adults — Page 9, 2.3 Procedure — «Prespecified eligibility criteria were age 18–60 years»
- pct_female: 49.24 — Page 5, 2.1 Participants — «Age and sex data were available for 329 participants, of whom 167 identified as male (50.76%) and 162 as female (49.24%).»
- informant: self — Page 9, 2.3 Procedure — «Participants subsequently completed the S-Five, RFQ-8, QCAE, TAS-20, IMQ, SSSQ, and SAD-T»
- mode: online — Page 9, 2.3 Procedure — «All participants accessed the study through Gorilla Experiment Builder (www.gorilla.sc).»
- instruments: S-Five (25 items, English); SSSQ six-item version (English; covers tinnitus, hyperacusis and misophonia features); entry question on self-identified/diagnosed misophonia (ad hoc, English) — Page 6, 2.2.2.1; Page 8, 2.2.2.6; Page 9, 2.3 — «We used 25-item S-Five (Vitoratou et al., 2021)... At entry, they indicated whether they identified as having misophonia, had received a diagnosis, were unfami…»
- instrument_validated_in_language: yes — Page 6-7, 2.2.2.1 — «A total score of 87 or above has been proposed as indicative of clinically significant misophonia on the basis of receiver operating characteristic (ROC) analy…»
- pub_status: preprint — Page 1, footer — «bioRxiv preprint»
- language: English — Whole text — «Social-Cognitive Dysregulation Model of Misophonia: Perspective from a Behavioural Study»
- funding_coi: Funded by ESSCA School of Management; acknowledges SoQuiet and Duke Centre for Misophonia and Emotion Regulation; COI statement NR — Page 1, Acknowledgement — «We would like to thank SoQuiet and Duke Centre for Misophonia and Emotion Regulation (CMER). This study has been funded by ESSCA School of Management.»
- notes: POSSIBLE E1 – REVIEWER TO CHECK: 195/341 (57%) scored S-Five >=87, much higher than general-population rates. The authors mention 'the specificity of the target population' and thank SoQuiet (a misophonia charity) and the Duke misophonia centre. The advert content and any Prolific prescreening on misophonia are not reported, so the sample may have been enriched for misophonia. Check the OSF preregistration (osf.io/vjkfx). The age range 18-60 is the eligibility range; observed min/max NR. Prevalence was not the aim of the study: severity was analysed dimensionally. Counts for the self-identifi…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is Prolific users (English speakers) only, not a defined general population. — Page 5, 2.1 — «Participants were recruited through Prolific (www.prolific.com), an online research-participant platform»
2. способ отбора: **no** — Volunteers who opted in on an online non-probability panel. — Page 9, 2.3 — «Eligible participants viewed a study advertisement outlining the procedures and compensation»
3. размер выборки: **no** — n = 341 < 385. — Page 10, 2.3 — «yielding a final analytic sample of N = 341»
4. описание выборки и условий: **no** — Age, sex and setting reported; country and dates of data collection not reported. — Page 5, 2.1 — «The sample comprised 341 participants (Meanage = 34.68 years, SD = 10.02).»
5. охват (пропуски): **no** — 376 of 717 recruited (52%) excluded for incomplete data with no handling or comparison. — Page 10, 2.3 — «Participants were excluded for incomplete behavioural-task data, multiple participation attempts, or incomplete questionnaire data (N = 376)»
6. валидность определения случая: **yes** — S-Five >=87 (validated English version, ROC-anchored, Vitoratou 2023). — Page 6-7, 2.2.2.1 — «A total score of 87 or above has been proposed as indicative of clinically significant misophonia on the basis of receiver operating characteristic (ROC) analy…»
7. единое надёжное измерение: **yes** — Same online S-Five for all; internal consistency reported in this sample. — Page 7, 2.2.2.1 — «In the present sample, the total scale showed excellent internal consistency (α = .972, ω = .972; N = 338).»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given (195/341); CI calculable. — Page 10, 2.3 — «final analytic sample of N = 341, including 146 below and 195 above cutoff threshold (≥87)»
9. отклик: **no** — Open Prolific recruitment with no denominator of invited people; no non-response handling. — Page 10, 2.3 — «A total of 717 participants were recruited.»

Правки:
- 

Проверено: да
---

## ST008 · Fournier 2026 · Hearing research

Основной отчёт R0068: [текст](../../fulltext/text/R0068.txt) · [PDF](../../fulltext/pdf/R0068.pdf) — «Validating and refining a psychoacoustic test to diagnose hyperacusis.» — [DOI](https://doi.org/10.1016/j.heares.2025.109482)
Расхождения в тексте: Table 2 gives misophonia Y/N as 10/8 (hyperacusis) and 10/15 (controls), with 2 and 4 missing; these add up to 20 and 29, which matches the group sizes. The Table 2 label ('Misophonia trigger sounds self-reported as annoying') differs in wording from the Methods ('potential misophonia'), but it is the same item. The overall age and sex figures were computed from the group values in Table 2.
Заметка ИИ: There is one eligible sample. It is a small hyperacusis validation study, and misophonia was measured only by an ad hoc trigger-annoyance item, so all estimates are L0 (listed, not pooled). The reviewer should check: (1) the choice to treat the 3 clinic-recruited hyperacusis participants as part of the single sample; (2) the population code gp_other (a university research mailing list).

### ST008-1 · Laboratory hyperacusis-test validation sample, Québec City, Canada (n=49; 20 hyperacusis, 29 controls)
Отчёты: R0068 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-reported being bothered/disgusted by specific sounds AND named sounds are known misophonia triggers (open answer judged by researchers) | **L0** | **20 / 43** | 46.5 | Page 5, Table 2; Page 4, 2.2 | «Misophonia trigger sounds self- reported as annoying # (Y/ N) 10/8 10/15» |
| E2 | hyperacusis | adhoc · self-reported being bothered/disgusted by specific sounds AND named sounds are known misophonia triggers | **L0** | **10 / 18** | 55.6 | Page 5, Table 2 | «Misophonia trigger sounds self- reported as annoying # (Y/ N) 10/8» |
| E3 | controls (no hyperacusis) | adhoc · self-reported being bothered/disgusted by specific sounds AND named sounds are known misophonia triggers | **L0** | **10 / 25** | 40.0 | Page 5, Table 2 | «Misophonia trigger sounds self- reported as annoying # (Y/ N) ... 10/15» |

- E1: источник порога: study's own; правило: adhoc row; L0: item asks only about bothersome/disturbing sounds or any trigger; у авторов: «potential misophonia»; главная у авторов: no; период: NR; **расчёт: cases 10 + 10; n (10+8) + (10+15) = 43 from Table 2 (6 missing)**; заметка: No distress/impairment or misophonia self-identification required. The authors did not report a prevalence; the item was used to compare groups and as an exploratory ROC criterion.
- E2: источник порога: study's own; правило: adhoc row; L0: item asks only about bothersome sounds or any trigger; у авторов: «potential misophonia»; главная у авторов: no; период: NR; **расчёт: n = 10 + 8 from Table 2 (2 missing of 20)**; заметка: The hyperacusis subgroup was labelled within the sample (>=2 of: self-reported hypersensitivity, HQ>=22, LDLmin<=77 dB HL); n<139.
- E3: источник порога: study's own; правило: adhoc row; L0: item asks only about bothersome sounds or any trigger; у авторов: «potential misophonia»; главная у авторов: no; период: NR; **расчёт: n = 10 + 15 from Table 2 (4 missing of 29)**

**Ключевые поля выборки:**
- **n_analysed: 43** — Page 5, Table 2 footnote — «Misophonia trigger sounds self- reported as annoying # (Y/ N) 10/8 10/15 ... # Missing values for the hyperacusis (n = 2) and control group (n = 4)»
- **population: gp_other** — Page 3, 2.1 Participants — «recruitment ads distributed to subscribers of a research participant mailing list created by Université Laval (listesULrecherche)»
- **sampling: convenience** — Page 3, 2.1 Participants — «Participants were recruited through word of mouth and recruitment ads distributed to subscribers of a research participant mailing list»

**Остальные поля:**
- clinical_group: NA — Page 4, 2.3 Labelling subjects — «Participants were considered ″hyperacusis″ participants when at least two out of the three criteria were met»
- country: CAN — Page 5, 2.5 Procedure — «The participants were tested at the laboratory located in Québec City.»
- setting: university laboratory (Université Laval research mailing list, word of mouth; 3 participants from a rehabilitation clinic audiology program, IRDPQ) — Page 3, 2.1 Participants — «Participants were recruited through word of mouth and recruitment ads distributed to subscribers of a research participant mailing list created by Université L…»
- data_years: 2023 — Page 3, 2.1 Participants — «All participants were recruited and tested between June 14, 2023, and December 28, 2023.»
- design: validation study — Page 3, Introduction (objectives) — «The primary objective of the present study was to validate the discriminative power of the CDS score using this tablet-based format»
- topic_disclosed: NR — Page 3, 2.1 Participants — «Some hyperacusis participants (n = 3) were recruited by ads sent to active hyperacusis patients»
- inclusion_exclusion: Excluded: external/middle ear pathology, severe hearing loss, hearing aid use. Hyperacusis vs control labelled after testing (>=2 of 3 criteria). — Page 3, 2.1 Participants — «Exclusion criteria included pathology of the external ear and/or the middle ear. Participants with severe hearing loss or using hearing aids were also excluded.»
- n_invited: NR — Page 3, 2.1 Participants — «A total of 49 participants were recruited.»
- n_responded: 49 — Page 3, 2.1 Participants — «A total of 49 participants were recruited.»
- response_rate: NR — Page 3, 2.1 Participants — «A total of 49 participants were recruited.»
- age_mean: 28.4 — Page 5, Table 2 — «Mean age in years (SD) 32 (7) 26 (7)»
- age_sd: NR — Page 5, Table 2 — «Mean age in years (SD) 32 (7) 26 (7)»
- age_min: NR — NR
- age_max: NR — NR
- age_group: NR — Page 5, Table 2 — «Mean age in years (SD) 32 (7) 26 (7)»
- pct_female: 55.1 — Page 5, Table 2 — «Sex (Male/Female) 9/11 13/16»
- informant: self — Page 4, 2.2 Pre-experimental measures — «the presence of misophonia among participants was screened using the following question: « Generally, are you bothered/disgusted by specific sounds? »»
- mode: NR — Page 5, 2.5 Procedure — «Afterward, the participants were asked to fill out the different questionnaires.»
- instruments: Ad hoc screening question 'Generally, are you bothered/disgusted by specific sounds?' + open 'If yes, which ones' (language version NR); CDSmiso psychoacoustic pleasantness/loudness ratings of 10 trigger sounds (Enzler et al. 2021b; no case definition applied) — Page 4, 2.2; Page 5, 2.4 — «Participants were considered to have potential misophonia if the specific sounds mentioned in the precision question were known as trigger sounds of misophonia…»
- instrument_validated_in_language: no — Page 13, 4.3 — «the presence of misophonia was assessed using a single screening question»
- pub_status: journal — Page 1; Page 2 — «Hearing Research 469 (2026) 109482»
- language: English — Full text — «Validating and refining a psychoacoustic test to diagnose hyperacusis»
- funding_coi: REPAR (programme 1.1 and OOAQ-REPAR, Québec), A*Midex Aix-Marseille University, IHU reConnect; funder had no role. COI: none declared. — Page 14, Funding; Declaration of competing interest — «This work was supported by the Provincial Network for Research in Adaptation-Rehabilitation (REPAR)... Declaration of competing interest None.»
- notes: Hyperacusis case-control validation study; misophonia was only a secondary screening item. Hyperacusis vs control labels were assigned within the recruited sample, so they are treated as subgroups. However, 3 hyperacusis participants were recruited separately from the IRDPQ clinic; the reviewer should decide whether they need separate handling. The authors give no overall age or sex: age mean 28.4 = (20x32 + 29x26)/49 = 1394/49; % female = (11+16)/49 = 27/49 = 55.1%. The language of the questionnaire is not stated (it was probably French in Québec). The misophonia screening item has 6/49 miss…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame (a university research mailing list, word of mouth and 3 clinic patients) covers only part of any general population. — Page 3, 2.1 — «recruitment ads distributed to subscribers of a research participant mailing list created by Université Laval»
2. способ отбора: **no** — Volunteers recruited by ads and word of mouth (convenience sample). — Page 3, 2.1 — «Participants were recruited through word of mouth and recruitment ads»
3. размер выборки: **no** — n = 43 with misophonia data, below 385. — Page 3, 2.1; Table 2 — «A total of 49 participants were recruited.»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported. — Page 3, 2.1; Page 5, Table 2 — «All participants were recruited and tested between June 14, 2023, and December 28, 2023.»
5. охват (пропуски): **no** — 6/49 (12.2%) are missing the misophonia item, and this is not handled. — Page 5, Table 2 footnote — «# Missing values for the hyperacusis (n = 2) and control group (n = 4)»
6. валидность определения случая: **no** — An ad hoc single screening question about being bothered by specific sounds. — Page 13, 4.3 — «the presence of misophonia was assessed using a single screening question»
7. единое надёжное измерение: **unclear** — The same question was used for everyone, but no reliability is reported and the mode is not stated. — Page 4, 2.2 — «« Generally, are you bothered/disgusted by specific sounds? » and the following precision question: « If yes, which ones »»
8. статистика (числитель и знаменатель): **yes** — Counts per group are given in Table 2, so the numerator and denominator can be traced and a CI can be calculated. — Page 5, Table 2 — «Misophonia trigger sounds self- reported as annoying # (Y/ N) 10/8 10/15»
9. отклик: **no** — Open ad-based recruitment with no denominator of invited people. — Page 3, 2.1 — «recruitment ads distributed to subscribers of a research participant mailing list»

Правки:
- 

Проверено: да
---

## ST009 · Freshley 2026 · Psychiatry research

Основной отчёт R0069: [текст](../../fulltext/text/R0069.txt) · [PDF](../../fulltext/pdf/R0069.pdf) — «Clinical correlates of individuals with and without misophonia in the U.S.: Results from a population-based study.» — [DOI](https://doi.org/10.1016/j.psychres.2026.116941)
Расхождения в тексте: The abstract says 62.5% of the misophonia group reported at least one psychological diagnosis; Results text (p.3-4) and Table 3 give 65.2% (Table value preferred). The raw 185/4005 = 4.62% matches the 4.6% cited in the Introduction from Dixon et al. 2024, which is consistent with this being the same sample. Group percentages in Tables 1-4 are weighted; group ns are raw.
Заметка ИИ: This is a comorbidity analysis of the US KnowledgePanel sample described in Dixon et al. 2024; the prevalence report should be the main report for this sample. Here only the raw case count (185) and total N (4005) are given. Data years, response rate, overall age and sex distribution, and the language version of the instruments are not reported.

### ST009-1 · Ipsos KnowledgePanel, USA, adults, n=4005
Отчёты: R0069 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · A-MISO-S>=10 AND MQ Misophonia Severity Scale>=7 | **L2** | **185 / 4005** | 4.6 | Page 2, 2.1 Participants and procedure | «nationally representative sample of U.S. adults (N = 4005). In this study, the misophonia group (n = 185) included participants who met the clinical cutoff on both the Amsterdam Misophonia Scale (≥10 [A-MISO-S]...) and …» |

- E1: источник порога: validation paper; правило: G4 combined 'A and B': A-MISO-S row L2 (>=10) + MQ row L2 (MSS>=7) -> L2; у авторов: «met the clinical cutoff on both ... (clinical levels of misophonia)»; главная у авторов: yes; период: NR; заметка: No prevalence is stated in this report; 185/4005 = 4.62% raw. The 4.6% cited in the Introduction comes from Dixon et al. 2024 (same sample; possibly weighted), so it is not entered as weighted_pct. Denominator unclear: whether all 4005 completed both measures is not reported. Same sample as Dixon 2…

**Ключевые поля выборки:**
- **n_analysed: 4005** — Page 2, 2.1 — «nationally representative sample of U.S. adults (N = 4005). In this study, the misophonia group (n = 185)»
- **population: gp_probability** — Page 1, Abstract — «Ipsos KnowledgePanel—a large, probability-based web panel that is representative of the United States.»
- **sampling: probability** — Page 2, 2.1 — «KnowledgePanel uses a probability-proportional-to-size procedure to select study specific samples and study-specific post-stratification sampling weights are applied»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — Page 2, 2.1 Participants and procedure — «Participants were drawn from a large, nationally representative sample of U.S. adults (N = 4005).»
- setting: online panel (Ipsos KnowledgePanel, probability-based web panel) — Page 2, 2.1 — «KnowledgePanel maintains the largest online, probability-based panel that is designed to be representative of the U.S. population»
- data_years: NR — Page 2, 2.1 — «Data were collected by Ipsos KnowledgePanel (KnowledgePanel) as part of a project investigating misophonia in the U.S. population (see Dixon et al., 2024 for f…»
- design: cross-sectional — Page 1, Abstract — «Participants were invited to complete a brief self-report survey of previous and current psychological and auditory-sensory symptoms and diagnoses.»
- topic_disclosed: NR — Page 2, 2.1 — «Data were collected by Ipsos KnowledgePanel (KnowledgePanel) as part of a project investigating misophonia in the U.S. population»
- inclusion_exclusion: US adults in Ipsos KnowledgePanel; no further criteria reported. Analyses compare misophonia group (n=185) with control group (n=1644; A-MISO-S<=4 and MQ MSS<=3); intermediate scorers not analysed. — Page 2, 2.1 — «The control group (n = 1644) included participants who reported no misophonia symptoms as evidenced by scores in the subclinical range on both the A-MISO-S (≤4…»
- n_invited: NR — NA
- n_responded: 4005 — Page 2, 2.1 — «Participants were drawn from a large, nationally representative sample of U.S. adults (N = 4005).»
- response_rate: NR — NA
- age_mean: NR — Page 2, Table 1 — «Agea 40.57 (15.91) 50.60 (18.08)»
- age_sd: NR — Page 2, Table 1 — «Agea 40.57 (15.91) 50.60 (18.08)»
- age_min: NR — NA
- age_max: NR — NA
- age_group: adults — Page 2, 2.1 — «nationally representative sample of U.S. adults (N = 4005)»
- pct_female: NR — Page 2, Table 1 — «Female 53.4 49.2»
- informant: self — Page 1, Abstract — «Participants were invited to complete a brief self-report survey»
- mode: online — Page 1, Abstract — «Data were collected through Ipsos KnowledgePanel—a large, probability-based web panel»
- instruments: A-MISO-S (language version not stated; presumably English); MQ incl. Misophonia Severity Scale (language version not stated; presumably English) — Page 3, 2.2.1 Misophonia status — «Clinical levels of misophonia were determined using the clinical cutoffs for the A-MISO-S (Schröder et al., 2013) and the Misophonia Questionnaire Severity Sca…»
- instrument_validated_in_language: NR — Page 3, 2.2.1 — «A cutoff score of ≥10 has been used in previous research and detects misophonia-related impairment with 89 % sensitivity and 67 % specificity (Möllmann et al.,…»
- pub_status: journal — Page 1, header — «Psychiatry Research 357 (2026) 116941»
- language: English — Full text — «Clinical correlates of individuals with and without misophonia in the U.S.: Results from a population-based study»
- funding_coi: Misophonia Research Fund grant to L. Dixon; competing interests: none declared — Page 8, Funding statement; Declaration of competing interest — «This work was supported by a Misophonia Research Fund grant awarded to Laura Dixon. ... Declaration of competing interest None»
- notes: SAME SAMPLE as Dixon et al. 2024 (J Psychopathol Clin Sci, prevalence paper; 4.6% cited in the Introduction) and probably Dixon et al. 2023 (public awareness, same KnowledgePanel project). Do not double count; Dixon 2024 is likely the primary prevalence report. This report is a comorbidity paper: it gives no prevalence, only the count of the misophonia group (185) and total N (4005). Age and sex are given only as weighted values for the misophonia and control groups, not for the whole sample. Data years and response rate not given (referred to Dixon 2024). Language version of the instruments …

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Frame is a probability-based national panel designed to represent US adults (the target population). — Page 2, 2.1 — «KnowledgePanel maintains the largest online, probability-based panel that is designed to be representative of the U.S. population»
2. способ отбора: **yes** — Probability sampling: PPS selection from a probability-based panel, with post-stratification weights. — Page 2, 2.1 — «KnowledgePanel uses a probability-proportional-to-size procedure to select study specific samples»
3. размер выборки: **yes** — N = 4005 >= 385. — Page 2, 2.1 — «nationally representative sample of U.S. adults (N = 4005)»
4. описание выборки и условий: **unclear** — Setting and country are reported; age and sex are given only by group; data collection dates are missing (one item missing). — Page 2, 2.1 and Table 1 — «Data were collected by Ipsos KnowledgePanel ... (see Dixon et al., 2024 for full details).»
5. охват (пропуски): **unclear** — Missing data on the misophonia measures are not reported; missing data are given only for the correlate items (1.2-1.4%). — Page 5, Table 3 footnotes — «a 1.4 % of individuals did not respond to one or more items.»
6. валидность определения случая: **unclear** — Both component cut-offs are anchored (A-MISO-S>=10, MQ MSS>=7; Möllmann 2023), but the conjunction is stricter than either, and the language version and its validation are not stated. Reviewer to decide. — Page 2, 2.1; Page 3, 2.2.1 — «the misophonia group (n = 185) included participants who met the clinical cutoff on both the Amsterdam Misophonia Scale (≥10 [A-MISO-S]; Schröder et al., 2013)…»
7. единое надёжное измерение: **unclear** — Same online self-report instruments and thresholds for everyone, but no internal consistency is reported in this report. — Page 3, 2.2.1 — «Items are rated on a 0 (none) to 4 (extreme) scale and are summed to yield the A-MISO-S total score.»
8. статистика (числитель и знаменатель): **unclear** — Raw numerator (185) and total N (4005) are given, but no prevalence, CI or weighted prevalence is reported here, and the denominator for complete misophonia data is unclear. — Page 2, 2.1 — «(N = 4005). In this study, the misophonia group (n = 185)»
9. отклик: **unclear** — Response rate not reported (referred to Dixon 2024). Post-stratification weights are applied, but not to a prevalence estimate in this report. — Page 2, 2.1 — «study-specific post-stratification sampling weights are applied to survey data based on geodemographic benchmarks»

Правки:
- 

Проверено: да
---

## ST010 · Gumus 2026 · BMC psychology

Основной отчёт R0075: [текст](../../fulltext/text/R0075.txt) — «Misophonia severity in university students: associations with negative emotionality, motor impulsivity, and checking.» — [DOI](https://doi.org/10.1186/s40359-026-04390-z)
Расхождения в тексте: Participant flow is inconsistent. The Sample section says 23 participants were excluded for incomplete or missing data. It also says 579 volunteers were recruited and 17 excluded (age 9, ADHD 4, hearing loss 4), leaving 562. It is unclear whether the 23 are part of the 579. n_responded was set to 579. Table 1 labels the groups 'MQ >= 7' / 'MQ < 7'; the Methods make clear this is the Misophonia Severity Scale >=7. Text and Table 1 agree on 92/562 (16.4%) and on 356 female (63.3%). The text and tables disagree on the direct path from depression (Table 2 p = 0.102, Table 3 and text p = 0.079), but this does not affect the prevalence data.
Заметка ИИ: Single-sample study. The main estimate is MQ MSS >=7, 92/562 (L2). The female estimate is taken from Table 1; the male estimate was derived by subtraction. Country (TUR) is inferred and not stated in the text. The supplementary tables were not available.

### ST010-1 · University of Health Sciences students (medicine, dentistry, nursing, psychology), Turkey, n=562
Отчёты: R0075 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **92 / 562** | 16.4 | Results, Samples; Table 1; Discussion | «the prevalence of MQ cut-off–defined elevated misophonia symptoms was 16.4% (n = 92) based on the MQ severity cut-off of ≥ 7» |
| E2 | female | MQ · MSS>=7 | **L2** | **62 / 356** | 17.4 | Table 1 | «Sex, Female, n (%) / 356 (63.3) / 62 (67.4) / 294 (62.6)» |
| E3 | male | MQ · MSS>=7 | **L2** | **30 / 206** | 14.6 | Table 1; Sample | «Total Sample (n = 562) / MQ ≥ 7 (n = 92) ... Sex, Female, n (%) / 356 (63.3) / 62 (67.4); 36.7% were male (n = 206)» |

- E1: источник порога: developer paper; правило: MQ row; L2 MSS>=7 (recommended, G11); у авторов: «cut-off–defined elevated misophonia symptoms»; главная у авторов: yes; период: NR
- E2: источник порога: developer paper; правило: MQ row; L2 MSS>=7; у авторов: «cut-off–defined elevated misophonia symptoms»; главная у авторов: no; период: NR; заметка: Calculated prevalence 62/356 = 17.4%.
- E3: источник порога: developer paper; правило: MQ row; L2 MSS>=7; у авторов: «cut-off–defined elevated misophonia symptoms»; главная у авторов: no; период: NR; **расчёт: cases 92 - 62 = 30; n 562 - 356 = 206 (also stated in text) from Table 1**; заметка: Assumes binary sex coding (only female/male reported). Prevalence 30/206 = 14.6%.

**Ключевые поля выборки:**
- **n_analysed: 562** — Sample; Results, Samples; Table 1 — «Among the students who participated in the study, 92 individuals (16.4%) were identified as having elevated misophonia symptoms.»
- **population: university_students** — Sample — «36.7% were from the psychology department (n = 206), 26.7% were from dentistry (n = 150), 22.4% were from medicine (n = 126), and 14.2% were from nursing (n = 80)»
- **sampling: convenience** — Procedure — «using the convenience sampling method. Care was taken to select courses with high student participation in these faculties.»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Materials and methods: MQ; Procedure — «In the Turkish validity and reliability study conducted by Sakarya and Çakmak (2021)... Ethics Committee of the University of Health Sciences, Hamidiye Scienti…»
- setting: university (classroom administration in four health-sciences faculties of one university) — Procedure — «recruiting students from the Faculty of Medicine, Faculty of Dentistry, Faculty of Nursing, and Faculty of Psychology at University of Health Sciences, using t…»
- data_years: 2023 — Procedure — «Data were collected between 10.10.2023 and 15.12.2023.»
- design: cross-sectional — Design — «In this study, a cross-sectional and correlational design was employed.»
- topic_disclosed: NR — Procedure — «After the necessary information was provided, the Informed Consent Form and study scales were distributed to the prospective participants.»
- inclusion_exclusion: Inclusion: age 18-30 and agreeing to participate. Exclusion: outside 18-30, hearing aid or self-reported hearing impairment, diagnosis of autism spectrum disorder or ADHD; incomplete questionnaires — Sample — «Exclusion criteria for the study were: (i) being outside the 18–30 age range; (ii) using a hearing aid or reporting hearing impairment; (iii) having a diagnosi…»
- n_invited: NR — Sample; Procedure — «A total of 579 volunteers were initially recruited.»
- n_responded: 579 — Sample — «A total of 579 volunteers were initially recruited. Seventeen participants were excluded ... resulting in a final sample of 562 participants.»
- response_rate: NR — NA
- age_mean: 19.77 — Sample; Table 1 — «their average age was 19.77 ± 1.46 years»
- age_sd: 1.46 — Sample; Table 1 — «their average age was 19.77 ± 1.46 years»
- age_min: NR — Sample — «The inclusion criteria for the study were being between the ages of 18 and 30»
- age_max: NR — Sample — «The inclusion criteria for the study were being between the ages of 18 and 30»
- age_group: adults — Abstract — «A total of 562 university students aged 18–30 years participated»
- pct_female: 63.3 — Sample; Table 1 — «63.3% were female (n = 356), 36.7% were male (n = 206)»
- informant: self — Misophonia questionnaire (MQ) — «The MQ is a self-report measure developed by Wu et al. (2014)»
- mode: paper — Procedure — «the researcher would administer the survey and scales to the students in the classroom environment ... After the study forms were collected, they were numbered…»
- instruments: Misophonia Questionnaire (MQ; Symptom subscale, Emotions and Behaviors subscale, Misophonia Severity Scale), Turkish version (Sakarya & Çakmak 2021) — Misophonia questionnaire (MQ) — «In the Turkish validity and reliability study conducted by Sakarya and Çakmak (2021), the MQ demonstrated a three-factor structure»
- instrument_validated_in_language: yes — Misophonia questionnaire (MQ) — «In the Turkish validity and reliability study conducted by Sakarya and Çakmak (2021)... Cronbach's α of 0.89»
- pub_status: journal — Header — «BMC psychology; DOI: 10.1186/s40359-026-04390-z»
- language: English — Full text — «Misophonia severity in university students: associations with negative emotionality, motor impulsivity, and checking»
- funding_coi: No funding; authors declare no competing interests — Funding; Competing interests — «The author(s) received no financial support for the research, authorship, and/or publication of this article. ... The authors declare no competing interests.»
- notes: Turkey is never named outright. TUR was inferred from the use of Turkish-validated instruments and the ethics committee (University of Health Sciences, Hamidiye). Participants were health-sciences students (psychology, dentistry, medicine, nursing), not only medical students. Actual age range not reported; 18-30 is the inclusion range. The participant flow is inconsistent: 23 excluded for incomplete or missing data, and separately 579 recruited minus 17 = 562. Table 1 labels the groups 'MQ >= 7', but this refers to the Misophonia Severity Scale. Trigger and reaction tables (S1-S3) are in the …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is university students. The frame was selected high-attendance courses in four health-sciences faculties of one university, which covers only part of that population. — Procedure — «Care was taken to select courses with high student participation in these faculties.»
2. способ отбора: **no** — Convenience sampling of volunteers. — Procedure — «using the convenience sampling method»
3. размер выборки: **yes** — n = 562 >= 385. — Sample — «resulting in a final sample of 562 participants»
4. описание выборки и условий: **yes** — Age, sex, setting and dates are reported. The country is implied by the Turkish instruments and institution but never named. — Sample; Procedure — «average age was 19.77 ± 1.46 years ... Data were collected between 10.10.2023 and 15.12.2023.»
5. охват (пропуски): **yes** — 23 excluded for incomplete data, about 4% of respondents, under 10%. — Sample — «23 participants were excluded at baseline due to incomplete questionnaires or missing data»
6. валидность определения случая: **yes** — MQ Misophonia Severity Scale >=7 in a published Turkish validation. — Misophonia questionnaire (MQ) — «participants scoring ≥ 7 on the Misophonia Severity Scale were classified as having cut-off–defined elevated misophonia symptoms»
7. единое надёжное измерение: **yes** — Same paper self-report MQ and threshold for all participants; Cronbach's alpha reported in the sample. — Misophonia questionnaire (MQ) — «In the present sample, Cronbach's α was 0.783 for the total scale»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are clear (92/562), so a CI can be calculated; no weighting needed. — Results, Samples; Table 1 — «92 individuals (16.4%) were identified as having elevated misophonia symptoms»
9. отклик: **unclear** — Classroom recruitment; number of students approached not reported, so response rate cannot be computed. — Procedure; Sample — «A total of 579 volunteers were initially recruited.»

Правки:
- 

Проверено: да