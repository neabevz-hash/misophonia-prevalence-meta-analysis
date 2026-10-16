# Проверка выписывания — файл 6 из 10

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

## ST051 · Dwyer 2023 · eScholarship, University of California

Основной отчёт R0717: [текст](../../fulltext/text/R0717.txt) — «Attention, Monotropism, and Sensory Experiences in Autistic Adolescents: Characterization via Multiple Measurement Methods»
Расхождения в тексте: Chapter 1 reports 13 autistic participants (Tables 1.1-1.2). Chapter 2 reports 14 (Tables 2.1-2.2), with different age and sex figures for the autistic group. Chapter 1 values were used because the DVMSQ was available for 13 autistic participants. The comparison group was the same in both chapters (n=17). Section 1.2.e.iii says the CDS reference group was 'non-autistic participants not meeting the DVMSQ misophonia criteria; n=15', but DVMSQ data were available for only 16 comparison participants. Whether 1 or 2 comparison participants met the criteria cannot be settled from the text. Table 1.3 says 16 comparison participants contributed CDS data, while the text says CDS data were available from all 17.
Заметка ИИ: This is a lab-based thesis comparing autistic and typically-developing adolescents, not a prevalence study. No prevalence is reported. The only categorical misophonia information is an indirect count (comparison group: about 1 of 16 meeting the DVMSQ criteria), extracted at level NR and flagged. The autistic sample is eligible but has no extractable estimate.

### ST051-1 · Typically-developing comparison adolescents, UC Davis lab study, USA, n=17 (DVMSQ n=16)
Отчёты: R0717 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DVMSQ · meets DVMSQ misophonia criteria per Williams et al. 2022 Table 2 (clinical vs subclinical not specified) | **NR** | **1 / 16** | 6.2 | Section 1.2.e.iii, p. 20; Section 1.2.c.iii, p. 14 | «75% quantiles ... were extracted in non-autistic participants not meeting the DVMSQ misophonia criteria as described in Table 2 of Williams et al. (2022); n=15» |

- E1: источник порога: developer paper; правило: DVMSQ row; G6 (unclear whether clinical or subclinical algorithm); у авторов: «meeting the DVMSQ misophonia criteria»; главная у авторов: no; период: NR; **расчёт: 16 comparison participants with DVMSQ data minus 15 'not meeting the DVMSQ misophonia criteria' = 1**; заметка: Indirect derivation, not reported by the authors. If the 15 included the one comparison participant without DVMSQ data, cases could be 2 of 16. The authors do not present this as a prevalence estimate.

**Ключевые поля выборки:**
- **n_analysed: 16** — Section 1.2.c.iii, p. 14 — «DVMSQ scores were available from 13 autistic and 16 comparison participants.»
- **population: other_nonclinical** — Section 1.2.a, p. 10 — «Comparison participants had no known or suspected neurodivergence and no first- or second-degree autistic relatives.»
- **sampling: convenience** — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups, personal contacts, and from institutional research registries»

**Остальные поля:**
- clinical_group: NA — Section 1.2.a, p. 10 — «Comparison participants had no known or suspected neurodivergence»
- country: USA — Section 1.2.a, p. 10 — «institutional research registries (the UC Davis MIND Institute Research Participant Registry and the UC Davis Center for Mind and Brain's participant pool)»
- setting: university laboratory study; participants recruited from the community (social media, community groups, personal contacts) and university research registries — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups, personal contacts, and from institutional research registries»
- data_years: NR — Section 1.2.a, p. 10 — «data collection remains ongoing»
- design: other — Section 1.1.d, p. 7 — «well-characterized samples of autistic and comparison adolescents completed a mixture of self-report questionnaire and lab-based sensory measures»
- topic_disclosed: NR — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups»
- inclusion_exclusion: Age 11-16; no known/suspected neurodivergence; no 1st/2nd-degree autistic relatives; trichromatic vision, >=20/40 vision; intellectual disability and hearing loss (PTA >=25 dB HL) excluded — Section 1.2.a, p. 10 — «In both groups, intellectual disability and hearing loss (monaural pure tone average ≥ 25 dB HL) were exclusionary.»
- n_invited: NR — Section 1.2.a, p. 10 — «A total of 64 participants' caregivers filled out screening questionnaires to determine eligibility; 17 were ineligible.»
- n_responded: 17 — Section 1.2.a, p. 10 — «a total of 13 autistic and 17 control participants completed laboratory visits»
- response_rate: NR — Section 1.2.a, p. 10 — «Of the remaining 42 prospective participants, a total of 13 autistic and 17 control participants completed laboratory visits»
- age_mean: 13.02 — Table 1.1, p. 11 — «Age (years) ... 13.02 (1.46) 11.16 to 15.67 17»
- age_sd: 1.46 — Table 1.1, p. 11 — «13.02 (1.46) 11.16 to 15.67 17»
- age_min: 11.16 — Table 1.1, p. 11 — «13.02 (1.46) 11.16 to 15.67 17»
- age_max: 15.67 — Table 1.1, p. 11 — «13.02 (1.46) 11.16 to 15.67 17»
- age_group: mixed — Section 1.2.a, p. 10 — «Participants aged 11–16 years old»
- pct_female: 29.41 — Table 1.2, p. 12 — «5 female (29.41%) 12 male (70.59%)»
- informant: self — Section 1.2.c.iii, p. 14 — «is a brief self-report measure of core misophonic characteristics»
- mode: NR — Section 1.4.b, p. 37 — «participants generally filled out the DVMSQ during or soon after the lab visit in which they completed the psychoacoustic tasks»
- instruments: DVMSQ (English, items slightly revised to remove work/employment references); MIST-A misophonia (anger/aggression) subscale (English); Core Discriminant Sounds psychoacoustic misophonia score (CDSMiso) — Sections 1.2.c.i, 1.2.c.iii, 1.2.e.iii, pp. 13-19 — «In this study, items were slightly revised to remove references to work/employment.»
- instrument_validated_in_language: yes — Section 1.2.c.iii, p. 14 — «It has been validated in general-population and autistic adult samples (Williams et al., 2022).»
- pub_status: thesis — Title page — «UC Davis Electronic Theses and Dissertations ... DOCTOR OF PHILOSOPHY in Psychology»
- language: English — Full text — «Attention, Monotropism, and Sensory Experiences in Autistic Adolescents»
- funding_coi: Autism Speaks and Royal Arch Masons; Tsakopoulos Foundation; HRSA AIR-P; UC Davis MIND Institute IDDRC (NICHD P50 HD103526). COI NR. — Acknowledgements, p. vi — «Funding for this project was provided by Autism Speaks and the Royal Arch Masons, by the Tsakopoulos Foundation, by HRSA's Autism Intervention Research Network…»
- notes: Not a prevalence study; preliminary data from an ongoing lab study. No misophonia prevalence is reported directly. The only categorical information is indirect: the CDS reference group comprised 'non-autistic participants not meeting the DVMSQ misophonia criteria ... n=15'. DVMSQ data were available for 16 comparison participants (17 with CDS data). The DVMSQ was validated in adults and was modified here (work items removed). Chapter 2 reports the same comparison sample (n=17). Language of administration was not stated; English was assumed from the US setting.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Volunteer comparison group from registries and community advertising, screened for absence of neurodivergence; does not cover a defined target population — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups, personal contacts, and from institutional research registries»
2. способ отбора: **no** — Convenience/volunteer recruitment — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups, personal contacts»
3. размер выборки: **no** — n=16 with DVMSQ, below 385 — Section 1.2.c.iii, p. 14 — «DVMSQ scores were available from 13 autistic and 16 comparison participants.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection not reported — Tables 1.1-1.2, pp. 11-12 — «data collection remains ongoing»
5. охват (пропуски): **yes** — 1 of 17 comparison participants lacked DVMSQ data (5.9%) — Section 1.2.c.iii, p. 14 — «DVMSQ scores were available from 13 autistic and 16 comparison participants.»
6. валидность определения случая: **unclear** — DVMSQ criteria referenced (Williams 2022, Table 2), but not clear whether clinical or subclinical criteria were applied; the instrument was modified and is validated only in adults — Section 1.2.e.iii, p. 20 — «non-autistic participants not meeting the DVMSQ misophonia criteria as described in Table 2 of Williams et al. (2022); n=15»
7. единое надёжное измерение: **unclear** — Same self-report instrument for all, but no reliability reported in the sample — Section 1.2.c.iii, p. 14 — «If participants report being bothered by specific sounds, even if they are not loud, participants complete the measure; otherwise, their scores are assumed to …»
8. статистика (числитель и знаменатель): **no** — No prevalence reported; numerator only inferable indirectly from the CDS reference-group size — Section 1.2.e.iii, p. 20 — «non-autistic participants not meeting the DVMSQ misophonia criteria ... n=15»
9. отклик: **unclear** — Per-group response not reported; 30 of 42 eligible prospective participants (both groups) completed visits, and data collection was ongoing — Section 1.2.a, p. 10 — «Of the remaining 42 prospective participants, a total of 13 autistic and 17 control participants completed laboratory visits»

Правки:
- 

Проверено: да
### ST051-2 · Autistic adolescents, UC Davis lab study, USA, n=13 (Ch. 1; 14 in Ch. 2)
Отчёты: R0717 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |


**Ключевые поля выборки:**
- **n_analysed: 13** — Section 1.2.c.iii, p. 14 — «DVMSQ scores were available from 13 autistic and 16 comparison participants.»
- **population: clinical** — Section 1.2.a, p. 10 — «Autistic participants had prior diagnoses of "autism spectrum disorder" or equivalent "pervasive developmental disorders."»
- **sampling: convenience** — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups, personal contacts»

**Остальные поля:**
- clinical_group: autism — Section 1.2.a, p. 10 — «Autistic participants had prior diagnoses of "autism spectrum disorder"»
- country: USA — Section 1.2.a, p. 10 — «the UC Davis MIND Institute Research Participant Registry»
- setting: university laboratory study; recruited from community advertising, personal contacts and university research registries — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups, personal contacts, and from institutional research registries»
- data_years: NR — Section 1.2.a, p. 10 — «data collection remains ongoing»
- design: other — Section 1.1.d, p. 7 — «well-characterized samples of autistic and comparison adolescents completed a mixture of self-report questionnaire and lab-based sensory measures»
- topic_disclosed: NR — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups»
- inclusion_exclusion: Age 11-16; prior autism diagnosis (confirmed by ADOS-2/clinician or SCQ); trichromatic vision, >=20/40 vision; intellectual disability and hearing loss excluded — Section 1.2.a, pp. 10-11 — «11 autistic participants' diagnoses were confirmed by clinician judgement in a visit including administration of a masked Autism Diagnostic Observation Schedul…»
- n_invited: NR — Section 1.2.a, p. 10 — «A total of 64 participants' caregivers filled out screening questionnaires»
- n_responded: 13 — Section 1.2.a, p. 10 — «a total of 13 autistic and 17 control participants completed laboratory visits»
- response_rate: NR — Section 1.2.a, p. 10 — «Of the remaining 42 prospective participants, a total of 13 autistic and 17 control participants completed laboratory visits»
- age_mean: 13.09 — Table 1.1, p. 11 — «Age (years) 13.09 (1.47) 11.24 to 15.72 13»
- age_sd: 1.47 — Table 1.1, p. 11 — «13.09 (1.47) 11.24 to 15.72 13»
- age_min: 11.24 — Table 1.1, p. 11 — «13.09 (1.47) 11.24 to 15.72 13»
- age_max: 15.72 — Table 1.1, p. 11 — «13.09 (1.47) 11.24 to 15.72 13»
- age_group: mixed — Section 1.2.a, p. 10 — «Participants aged 11–16 years old»
- pct_female: 15.38 — Table 1.2, p. 12 — «2 female (15.38%) 11 male (84.62%)»
- informant: self — Section 1.2.c.iii, p. 14 — «is a brief self-report measure of core misophonic characteristics»
- mode: NR — Section 1.4.b, p. 37 — «participants generally filled out the DVMSQ during or soon after the lab visit»
- instruments: DVMSQ (English, slightly revised to remove work references); MIST-A misophonia subscale (English); CDSMiso psychoacoustic score — Sections 1.2.c.i-iii, 1.2.e.iii, pp. 13-19 — «In this study, items were slightly revised to remove references to work/employment.»
- instrument_validated_in_language: yes — Section 1.2.c.iii, p. 14 — «It has been validated in general-population and autistic adult samples (Williams et al., 2022).»
- pub_status: thesis — Title page — «UC Davis Electronic Theses and Dissertations»
- language: English — Full text — «Attention, Monotropism, and Sensory Experiences in Autistic Adolescents»
- funding_coi: Autism Speaks and Royal Arch Masons; Tsakopoulos Foundation; HRSA AIR-P; NICHD P50 HD103526. COI NR. — Acknowledgements, p. vi — «Funding for this project was provided by Autism Speaks and the Royal Arch Masons, by the Tsakopoulos Foundation»
- notes: Eligible clinical sample (autism), but no misophonia prevalence or case count is reported. Only continuous DVMSQ, MIST-A and CDS scores are given, so there are no estimates. Chapter 2 reports 14 autistic participants (one additional participant who completed visual tasks only; age 13.26 ± 1.54, 21.43% female).

**Риск смещения (JBI):**
1. рамка выборки: **no** — Volunteer autistic adolescents from registries and the community; not a defined frame of patients — Section 1.2.a, p. 10 — «recruited from community advertising via social media and community groups, personal contacts, and from institutional research registries»
2. способ отбора: **no** — Convenience recruitment — Section 1.2.a, p. 10 — «recruited from community advertising via social media»
3. размер выборки: **no** — n=13, below 139 for a clinical group — Section 1.2.c.iii, p. 14 — «DVMSQ scores were available from 13 autistic and 16 comparison participants.»
4. описание выборки и условий: **unclear** — Data collection dates not reported — Section 1.2.a, p. 10 — «data collection remains ongoing»
5. охват (пропуски): **yes** — DVMSQ data available for all 13 autistic participants — Section 1.2.c.iii, p. 14 — «DVMSQ scores were available from 13 autistic and 16 comparison participants.»
6. валидность определения случая: **unclear** — No case definition applied to this group; the DVMSQ was modified and is validated only in adults — Section 1.2.c.iii, p. 14 — «items were slightly revised to remove references to work/employment»
7. единое надёжное измерение: **unclear** — Same instrument for all; no reliability reported in the sample — Section 1.2.c.iii, p. 14 — «If participants report being bothered by specific sounds ... participants complete the measure; otherwise, their scores are assumed to be zero.»
8. статистика (числитель и знаменатель): **no** — No prevalence numerator reported — Table 1.6, p. 32 — «Misophonia Composite 0.19 (1.01) -0.69 to 2.33 13»
9. отклик: **unclear** — Per-group response not reported — Section 1.2.a, p. 10 — «Of the remaining 42 prospective participants, a total of 13 autistic and 17 control participants completed laboratory visits»

Правки:
- 

Проверено: да
---

## ST052 · Guzick 2023 · Journal of affective disorders

Основной отчёт R0733: [текст](../../fulltext/text/R0733.txt) · [PDF](../../fulltext/pdf/R0733.pdf) — «Clinical characteristics, impairment, and psychiatric morbidity in 102 youth with misophonia.» — [DOI](https://doi.org/10.1016/j.jad.2022.12.083)
Не выписано ИИ: Misophonia group (112 youth recruited for suspected misophonia, 102 analysed; A-MISO-S >=10 required): E1, recruited because of misophonia. Not extracted (its screening count, 5/112 with A-MISO-S <10, is not eligible either).
Расхождения в тексте: Anxiety group exclusions add up: 26+9+9+2=46 = 140-94. The printed percentages are rounded from /140: 26/140=18.6% (printed 19%), 9/140=6.4% (6%), 2/140=1.4% (1%). Anxiety group gender in Table 1: 32+54+8=94. Misophonia sample (not extracted): 'any diagnosis' is 81 (79%) on p7 and 80% on p9. Depression is 47% on p7 and 46% in the Highlights. The text puts elevated SRS-RRB at 11% (p8) and 10% (p10).
Заметка ИИ: There is one eligible sample: the anxiety comparison group, which is clinical (anxiety). Its estimate is weak. It comes from a screening-exclusion count, the true denominator is uncertain, and the analysed subset was selected to have A-MISO-S <=4. The reviewer may prefer to recode the level as NR (G6/G10) or to exclude the estimate. A corrigendum (10.1016/j.jad.2023.11.045) exists but was not available.

### ST052-1 · Youth with suspected anxiety disorders (comparison group), recruited online, USA, n=140 screened (94 analysed)
Отчёты: R0733 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S >=5 (score above the anxiety-group inclusion limit of <=4; 'too high') | **L1** | **9 / 140** | 6.4 | Page 4, Participants | «of the 140 in the anxiety group, 94 were included. Reasons for exclusion in the anxiety group included: MASC score below the clinical cutoff, n = 26 (19%), A-MISO-S score too high, 9 (6%)» |

- E1: источник порога: developer paper; правило: A-MISO-S row; >=5 = L1 (mild or more); G2; у авторов: «A-MISO-S score too high»; главная у авторов: no; период: current; заметка: Screening exclusion count, not reported as a prevalence by the authors. Exclusion categories appear mutually exclusive (26+9+9+2=46=140-94); people excluded for other reasons may also have had A-MISO-S >4, so 9 is likely a lower bound and the denominator uncertain. Population includes 9 later found…

**Ключевые поля выборки:**
- **n_analysed: 140** — Page 4, Participants — «of the 140 in the anxiety group, 94 were included. Reasons for exclusion in the anxiety group included: MASC score below the clinical cutoff, n = 26 (19%), A-MISO-S score too high, 9 (6%)»
- **population: clinical** — Page 3-4, Procedures — «Youth with suspected anxiety disorders were also recruited to serve as a non-misophonia clinical comparison group»
- **sampling: convenience** — Page 3, Procedures — «Youth with suspected misophonia were recruited via online advertisements, misophonia/anxiety-focused social media pages, as well as clinical and professional networks.»

**Остальные поля:**
- clinical_group: anxiety — Page 4, Procedures — «For the anxiety group, additional inclusion criteria were: 1) a Parent-report Multidimensional Anxiety Scale for Children (MASC) T-Score of at least 60, 2) an …»
- country: USA — Page 1 (affiliation, correspondence); Page 4 (IRB) — «The Institutional Review Board at Baylor College of Medicine approved the study. All portions of the study were completed virtually.»
- setting: clinic (academic medical centre research study, Baylor College of Medicine), conducted fully online/virtually; participants recruited mainly via online advertisements — Page 3-4, Procedures — «Youth with suspected anxiety disorders were also recruited to serve as a non-misophonia clinical comparison group... The majority of participants were recruite…»
- data_years: NR — NR — «NR»
- design: screening phase of clinical study — Page 4, Procedures/Participants — «For the anxiety group, additional inclusion criteria were: ... 3) a score of ≤4 on the A-MISO-S, corresponding with subclinical misophonia symptoms.»
- topic_disclosed: NR — Page 3, Procedures — «Youth with suspected anxiety disorders were also recruited to serve as a non-misophonia clinical comparison group»
- inclusion_exclusion: Age 8-17, parent willingness, English fluency; for analysis additionally MASC parent T>=60, MINI-KID anxiety disorder diagnosis, A-MISO-S <=4 — Page 4, Procedures — «Inclusion criteria for both samples were: 1) being 8–17 years, 2) parent willingness to participate, 3) English fluency.»
- n_invited: NR — NR — «NR»
- n_responded: 140 — Page 4, Participants — «One-hundred and twelve youth with suspected misophonia and 140 youth with suspected anxiety disorders were recruited.»
- response_rate: NR — NR — «NR»
- age_mean: 12.4 — Table 1 (Page 20) — «Age M (SD) 13.7 (2.5) 12.4 (2.6)»
- age_sd: 2.6 — Table 1 (Page 20) — «Age M (SD) 13.7 (2.5) 12.4 (2.6)»
- age_min: 8 — Page 4, Procedures (inclusion criterion) — «Inclusion criteria for both samples were: 1) being 8–17 years»
- age_max: 17 — Page 4, Procedures (inclusion criterion) — «Inclusion criteria for both samples were: 1) being 8–17 years»
- age_group: mixed — Page 4, Procedures — «Inclusion criteria for both samples were: 1) being 8–17 years»
- pct_female: 57 — Table 1 (Page 20) — «Female 69 (68%) 54 (57%)»
- informant: self — Page 5, Measures — «It was administered as a child-report measure in this study»
- mode: online — Page 4, Procedures — «Participants and their parents assented/consented to participate in the study during an initial video call... All portions of the study were completed virtuall…»
- instruments: A-MISO-S (English, child-report, with trained assessor present; 5-item total used in analyses); MAQ child-report (C-MAQ) and parent-report (P-MAQ) (English; use in anxiety group not stated); Misophonia Assessment Interview (misophonia group only) — Page 4-5, Measures — «the measure was presented to youth with a trained assessor present to provide additional clarifications on items when youth had questions. Item 4 was not inclu…»
- instrument_validated_in_language: yes — Page 5, Measures — «has shown strong psychometric properties as a self-report measure in college students, including good internal consistency and a single-factor structure... (Na…»
- pub_status: journal — Page 1 — «Published in final edited form as: J Affect Disord. 2023 March 01; 324: 395–402. doi:10.1016/j.jad.2022.12.083.»
- language: English — Page 1 — «Clinical characteristics, impairment, and psychiatric morbidity in 102 youth with misophonia»
- funding_coi: Ream Foundation/Milken Institute/Misophonia Research Fund grant; NICHD P50HD103555 (core facilities). COI not reported. — Page 12, Role of the Funding Source — «supported by a grant from the Ream Foundation/Milken Institute/Misophonia Research Fund, as well as support from the Eunice Kennedy Shriver National Institute …»
- notes: A corrigendum to this article exists (10.1016/j.jad.2023.11.045, 2024; found through Crossref); its text was not available. The only prevalence information for this eligible sample is the screening exclusion count: 9/140 had an 'A-MISO-S score too high', i.e., above 4. The exclusion reasons look mutually exclusive and the screening order is not stated, so 9 is likely a lower bound and the denominator is uncertain. It is not stated whether the cut-off used the 6- or 5-item total. Age and sex describe the 94 analysed, not the 140 screened. The analysed 94 have 0% misophonia by design. Possible …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is youth responding to online adverts/social media/networks, not all youth with anxiety disorders or a defined clinic population. — Page 3-4, Procedures — «The majority of participants were recruited via online advertisements.»
2. способ отбора: **no** — Volunteer opt-in recruitment (convenience). — Page 3, Procedures — «recruited via online advertisements, misophonia/anxiety-focused social media pages, as well as clinical and professional networks»
3. размер выборки: **yes** — Clinical group screened n=140 (>=139); analysed comparison group only 94. — Page 4, Participants — «140 youth with suspected anxiety disorders were recruited»
4. описание выборки и условий: **unclear** — Age, sex, setting reported (for the 94 analysed); country only implied by Baylor IRB; dates of data collection not reported. — Table 1; Page 4 — «Age M (SD) 13.7 (2.5) 12.4 (2.6)»
5. охват (пропуски): **unclear** — Not stated whether all 140 completed the A-MISO-S at screening; exclusion reasons listed as single categories. — Page 4, Participants — «MASC score below the clinical cutoff, n = 26 (19%), A-MISO-S score too high, 9 (6%), no anxiety disorder as assessed on the MINI-KID, n = 9 (6%)»
6. валидность определения случая: **no** — Case definition is A-MISO-S >=5 (above the <=4 inclusion limit), an unanchored severity-band cut-off. — Page 4, Procedures — «a score of ≤4 on the A-MISO-S, corresponding with subclinical misophonia symptoms»
7. единое надёжное измерение: **yes** — Same child-report A-MISO-S administered virtually with assessor present; internal consistency reported (in misophonia sample and source). — Page 5, Measures — «in this sample, internal consistency was α = .68 with all 6 items and α = .76 with 5 items»
8. статистика (числитель и знаменатель): **unclear** — 9/140 traceable, but it is an exclusion count; overlapping exclusion reasons make the true numerator/denominator uncertain; no CI. — Page 4, Participants — «A-MISO-S score too high, 9 (6%)»
9. отклик: **no** — Open online recruitment with no denominator of invited people. — Page 4, Procedures — «The majority of participants were recruited via online advertisements.»

Правки:
- 

Проверено: да
---

## ST053 · MUTLU 2023 · Medical Records

Основной отчёт R0766: [текст](../../fulltext/text/R0766.txt) · [PDF](../../fulltext/pdf/R0766.pdf) — «Misophonia and its Relationship with Other Psychiatric Disorders» — [DOI](https://doi.org/10.37990/medr.1208093)
Расхождения в тексте: Counts agree across text, Table 2 and Table 4. Disorder-level: 8 healthy + 31 anxiety + 4 depressive + 8 OCD = 51; with 5 others (ADHD, somatic, tic, PTSD) this gives the total of 56. Symptom-level: 1 + 25 + 13 + 4 = 43; with 6 others this gives 49. The Table 2 misophonia(+) rows sum to 105 and the misophonia(-) rows to 158. Table 4 percentages are column percentages over the four diagnoses shown. The healthy group is 9 + 41 = 50, so patients are 263 - 50 = 213. The authors' headline 21.3% (56/263) and 18.6% (49/263) combine both samples. These pooled figures are not extracted as sample estimates. By sex, only the pooled 263 are reported (female 72/166 misophonia+; male 33/97), so they cannot be split by sample. Discussion says 2.4% (n=6) of all participants had OCPD; Table 2 gives 5 + 1 = 6, which is consistent.
Заметка ИИ: Key judgement for the reviewer is the level of 'disorder-level misophonia'. The tool is called the 'Misophonia Interview Scale' (Öz et al.; used face-to-face in Kılıç 2021). Here, though, the participants 'fill out' the impairment form, and the first author only helped those who had difficulty. So I coded it as self-completed criteria (adhoc, L2). If you judge it interviewer-applied, it becomes interview L3 and JBI 6 would be yes. 'Any misophonia' (disorder + symptom level) rests on the participant choosing misophonia on the Sound Disturbance Problems Form (which shows explanations and exampl…

### ST053-1 · Psychiatric outpatients (first admission), Çukurova University, Adana, Türkiye, n=213
Отчёты: R0766 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · Self-completed Öz criteria: misophonia type on Sound Disturbance Problems Form + >=1 MSL sound moderate/very + >=1 emotional/physical reaction moderate/very + life affected moderate/very + functional item (yes or >1 h/day) | **L2** | **48 / 213** | 22.5 | Page 4, Results; Table 4 | «21.3% (n=56) of the participants had disorder-level misophonia ... 16% (n=8) of healthy individuals were diagnosed with disorder-level misophonia» |
| E2 | all | adhoc · Self-identified misophonia type on Sound Disturbance Problems Form (with explanations/examples) + >=1 MSL sound rated moderate/very (disorder- or symptom-level) | **L1** | **96 / 213** | 45.1 | Table 2, Page 5 | «Healthy 9 8.6 41 25.9» |
| E3 | anxiety disorders | adhoc · Self-completed Öz criteria (disorder-level), as above | **L2** | **31 / 121** | 25.6 | Page 4, Results; Table 4 | «Among the participants with anxiety disorder, 25.6% (n=31) had disorder-level misophonia, and 20.7% (n=25) had symptom-level misophonia.» |
| E4 | anxiety disorders | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **56 / 121** | 46.3 | Table 2, Page 5 | «Anxiety Disorders 56 53.3 65 41.1» |
| E5 | depressive disorder | adhoc · Self-completed Öz criteria (disorder-level) | **L2** | **4 / 41** | 9.8 | Page 4, Results | «9.8% (n=4) of the individuals diagnosed with major depressive disorder had disorder-level misophonia, and 31.7% (n=13) had symptom-level misophonia.» |
| E6 | depressive disorder | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **17 / 41** | 41.5 | Table 2, Page 5 | «Depressive Disorder 17 16.2 24 15.2» |
| E7 | OCD | adhoc · Self-completed Öz criteria (disorder-level) | **L2** | **8 / 29** | 27.6 | Page 4, Results | «27.6% (n=8) of individuals diagnosed with OCD had disorder-level misophonia, and 13.8% (n=4) had symptom-level misophonia.» |
| E8 | OCD | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **12 / 29** | 41.4 | Table 2, Page 5 | «OCD 12 11.4 17 10.8» |
| E9 | ADHD | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **6 / 10** | 60.0 | Table 2, Page 5 | «ADHD 6 5.7 4 2.5» |
| E10 | PTSD | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **1 / 3** | 33.3 | Table 2, Page 5 | «PTSD 1 1 2 1.3» |
| E11 | tic disorders | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **2 / 2** | 100.0 | Table 2, Page 5 | «Tic Disorders 2 1.9 0 0» |
| E12 | somatic symptom disorders | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **2 / 3** | 66.7 | Table 2, Page 5 | «Somatic Symptom Disorders 2 1.9 1 0.6» |
| E13 | eating disorders | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **0 / 2** | 0.0 | Table 2, Page 5 | «Eating Disorders 0 0 2 1.3» |
| E14 | sleep disorders | adhoc · Self-identified misophonia on form + >=1 MSL sound moderate/very | **L1** | **0 / 2** | 0.0 | Table 2, Page 5 | «Sleep Disorders 0 0 2 1.3» |

- E1: источник порога: developer paper; правило: adhoc row: self-completed criteria requiring impairment -> L2 (interview row L3 if judged interviewer-applied); у авторов: «disorder-level misophonia»; главная у авторов: no; период: NR; **расчёт: 56 disorder-level (all) - 8 healthy = 48; n = 263 - 50 = 213**; заметка: Authors' headline 21.3% pools patients and healthy controls.
- E2: источник порога: developer paper; правило: adhoc row: self-identification with definition shown -> L1; G1 sum of disorder- and symptom-level; у авторов: «misophonia (disorder-level + symptom-level)»; главная у авторов: no; период: NR; **расчёт: 105 misophonia(+) - 9 healthy = 96; n = 213**; заметка: If the reviewer regards the form only as a trigger item, this would be L0.
- E3: источник порога: developer paper; правило: adhoc row; L2 (impairment required); у авторов: «disorder-level misophonia»; главная у авторов: no; период: NR; **расчёт: n = 56 + 65 from Table 2**; заметка: Clinical subgroup within the patient sample
- E4: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: 31 + 25 (Table 4) = 56; n = 56 + 65**
- E5: источник порога: developer paper; правило: adhoc row; L2; у авторов: «disorder-level misophonia»; главная у авторов: no; период: NR; **расчёт: n = 17 + 24 from Table 2**
- E6: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 17 + 24 from Table 2**
- E7: источник порога: developer paper; правило: adhoc row; L2; у авторов: «disorder-level misophonia»; главная у авторов: no; период: NR; **расчёт: n = 12 + 17 from Table 2**
- E8: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 12 + 17 from Table 2**
- E9: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 6 + 4 from Table 2**; заметка: Disorder-level split not reported for ADHD
- E10: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 1 + 2 from Table 2**
- E11: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 2 + 0 from Table 2**
- E12: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 2 + 1 from Table 2**
- E13: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 0 + 2 from Table 2**
- E14: источник порога: developer paper; правило: adhoc row; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: n = 0 + 2 from Table 2**

**⚠ Проверка скриптом (обратите внимание):**
- E1, E3, E5, E7: самодельные вопросы на L2: верно, только если требуются и реакция, и нарушения

**Ключевые поля выборки:**
- **n_analysed: 213** — Page 2, Sample; Table 2 — «The study included 213 literate patients»
- **population: clinical** — Page 2, Sample — «213 literate patients ... admitted to Çukurova University Faculty of Medicine, Department of Mental Health and Disorders for the first time»
- **sampling: convenience** — Page 2, Sample — «The study included 213 literate patients ... who were admitted ... for the first time between 15.10.2020 and 15.04.2021»

**Остальные поля:**
- clinical_group: mixed_psychiatric — Table 2, Page 5 — «Anxiety Disorders 56 53.3 65 41.1 Depressive Disorder 17 16.2 24 15.2 OCD 12 11.4 17 10.8»
- country: TUR — Page 1, affiliations; Page 2, Sample — «admitted to Çukurova University Faculty of Medicine, Department of Mental Health and Disorders for the first time»
- setting: clinic (university hospital psychiatry outpatient clinic, first admissions) — Page 2, Sample — «213 literate patients between the ages of 18 and 65 years, who were admitted to Çukurova University Faculty of Medicine, Department of Mental Health and Disord…»
- data_years: 2020-2021 — Page 2, Sample — «for the first time between 15.10.2020 and 15.04.2021»
- design: cross-sectional — Page 2, Material and Method — «Our study aims to explore the relationship between misophonia and other mental disorders»
- topic_disclosed: NR — Page 2, Procedure — «all participants signed an informed consent form»
- inclusion_exclusion: Literate first-time outpatients aged 18-65; excluded: external auditory canal defect, reported hearing defects, hearing aids, schizophrenia, bipolar, schizoaffective, psychotic depression, schizotypal PD, neurocognitive disorders, mental retardation — Page 2, Sample — «patients with schizophrenia, bipolar disorder, schizoaffective disorder, major depressive disorder with psychotic features, and schizotypal personality disorde…»
- n_invited: NR — NA
- n_responded: 213 — Page 2, Sample — «The study included 213 literate patients»
- response_rate: NR — NA
- age_mean: NR — Table 1, Page 4 — «Age, years 35.66 11.48 36.05 11.29»
- age_sd: NR — Table 1, Page 4 — «Age, years 35.66 11.48 36.05 11.29»
- age_min: 18 — Page 2, Sample — «patients between the ages of 18 and 65 years»
- age_max: 65 — Page 2, Sample — «patients between the ages of 18 and 65 years»
- age_group: adults — Page 2, Sample — «patients between the ages of 18 and 65 years»
- pct_female: NR — Table 1, Page 4 — «Female 72 68.6 94 59.5»
- informant: self — Page 3, Misophonia Interview Scale — «participants who answered 'moderate or very' on the MSL were asked to fill out a form that included questions about their physical/emotional reactions and func…»
- mode: NR — Page 2, Procedure and measures — «The first author accompanied the participants who had difficulty completing the forms and scales and explained the points where they had difficulty.»
- instruments: Misophonia Interview Scale (Öz et al.; Turkish) with Öz diagnostic criteria, incl. Sound Disturbance Problems Form and Misophonia Symptom List (MSL, 50 sounds) — Page 2-3, Misophonia Interview Scale — «the diagnostic criteria recommended by Öz et al. were used, and the form of "Sound Disturbance Problems" was added to the misophonia interview scale.»
- instrument_validated_in_language: NR — Page 2, Misophonia Interview Scale — «Öz et al. developed the misophonia interview scale (8,20).»
- pub_status: journal — Page 1, header — «MEDICAL RECORDS-International Medical Journal»
- language: English — Page 1 — «Misophonia and its Relationship with Other Psychiatric Disorders»
- funding_coi: No financial support; authors declare no competing interests — Page 7 — «Financial disclosures: This study has no financial support. Conflict of Interest: The author declare that they have no competing interest.»
- notes: Recruited separately from the 50 healthy controls, so treated as a separate sample. Results are reported only pooled (n=263) or by diagnosis; patient-sample counts were derived by subtracting the healthy-group counts (Tables 2 and 4). Age and sex are reported only for the pooled misophonia(+)/(-) groups (pooled female 166/263 = 63.1%); age 18-65 is an inclusion criterion. Mode of the misophonia assessment is ambiguous. The tool is called an 'interview scale' (Öz/Kılıç 2021), but participants 'fill out' the impairment form, so I coded it as self-completed criteria (adhoc L2). If a reviewer jud…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Frame = first-time outpatients of one university psychiatry clinic in the period, but psychotic/bipolar patients excluded and consecutive enrolment not stated — Page 2, Sample — «admitted to Çukurova University Faculty of Medicine, Department of Mental Health and Disorders for the first time between 15.10.2020 and 15.04.2021»
2. способ отбора: **unclear** — Not stated whether all consecutive first admissions were approached — Page 2, Sample — «The study included 213 literate patients»
3. размер выборки: **yes** — n=213 clinical sample >= 139 (clinical threshold); below 385 if the general threshold were applied — Page 2, Sample — «The study included 213 literate patients»
4. описание выборки и условий: **no** — Setting, country and dates reported, but age and sex not reported separately for the patient sample (only pooled with controls) — Table 1, Page 4 — «Misophonia (+) (n=105) Misophonia (-) (n=158)»
5. охват (пропуски): **yes** — All participants classified (105 + 158 = 263); no missing misophonia data apparent — Table 2, Page 5 — «Misophonia (+) (n=105) Misophonia (-) (n=158)»
6. валидность определения случая: **no** — Primary definition is self-completed Öz criteria (ad hoc, no published validation stated) — Page 3 — «were defined as having "disorder-level misophonia."»
7. единое надёжное измерение: **unclear** — Same forms for all, but some participants were helped by the first author; no reliability reported for the misophonia measure — Page 2, Procedure — «The first author accompanied the participants who had difficulty completing the forms and scales»
8. статистика (числитель и знаменатель): **yes** — Counts per diagnosis in Tables 2 and 4, so numerator and denominator are traceable; CI calculable — Table 4, Page 6 — «Healthy 41(27.9) 8(15.7) 1(2.3)»
9. отклик: **unclear** — Number approached and response rate not reported — Page 2, Sample — «The study included 213 literate patients»

Правки:
- 

Проверено: да
### ST053-2 · Healthy volunteers (hospital staff and relatives), Çukurova University, Adana, Türkiye, n=50
Отчёты: R0766 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · Self-completed Öz criteria: misophonia type on Sound Disturbance Problems Form + >=1 MSL sound moderate/very + reaction moderate/very + life affected moderate/very + functional item | **L2** | **8 / 50** | 16.0 | Page 4, Results; Table 4 | «16% (n=8) of healthy individuals were diagnosed with disorder-level misophonia» |
| E2 | all | adhoc · Self-identified misophonia type on form + >=1 MSL sound moderate/very (disorder- or symptom-level) | **L1** | **9 / 50** | 18.0 | Table 2, Page 5 | «Healthy 9 8.6 41 25.9» |

- E1: источник порога: developer paper; правило: adhoc row: self-completed criteria requiring impairment -> L2 (L3 if judged interviewer-applied); у авторов: «disorder-level misophonia»; главная у авторов: no; период: NR
- E2: источник порога: developer paper; правило: adhoc row: self-identification with definition -> L1; G1 sum; у авторов: «misophonia (+)»; главная у авторов: no; период: NR; **расчёт: 8 disorder-level + 1 symptom-level = 9 (= Table 2 healthy misophonia+); n = 9 + 41**

**⚠ Проверка скриптом (обратите внимание):**
- E1: самодельные вопросы на L2: верно, только если требуются и реакция, и нарушения

**Ключевые поля выборки:**
- **n_analysed: 50** — Table 2, Page 5 — «Healthy 9 8.6 41 25.9»
- **population: other_nonclinical** — Page 2, Sample — «had no history of psychiatric disorders and were not receiving treatment»
- **sampling: convenience** — Page 2, Sample — «50 healthy volunteers from hospital staff and their relatives who agreed to participate in the study»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Page 1, affiliations — «Çukurova University, Faculty of Medicine, Department of Psychiatry, Adana, Türkiye»
- setting: workplace/community (hospital staff and their relatives, university hospital) — Page 2, Sample — «50 healthy volunteers from hospital staff and their relatives who agreed to participate in the study»
- data_years: NR — Page 2, Sample — «between 15.10.2020 and 15.04.2021, and 50 healthy volunteers»
- design: cross-sectional — Page 2, Sample — «50 healthy volunteers from hospital staff and their relatives»
- topic_disclosed: NR — Page 2, Procedure — «all participants signed an informed consent form»
- inclusion_exclusion: Hospital staff and their relatives with no psychiatric history and no current treatment — Page 2, Sample — «had no history of psychiatric disorders and were not receiving treatment»
- n_invited: NR — NA
- n_responded: 50 — Page 2, Sample — «50 healthy volunteers»
- response_rate: NR — NA
- age_mean: NR — Table 1 — «Age, years 35.66 11.48 36.05 11.29»
- age_sd: NR — Table 1 — «Age, years 35.66 11.48 36.05 11.29»
- age_min: NR — NA
- age_max: NR — NA
- age_group: adults — Page 2, Sample — «healthy volunteers from hospital staff and their relatives»
- pct_female: NR — Table 1 — «Female 72 68.6 94 59.5»
- informant: self — Page 3 — «were asked to fill out a form that included questions about their physical/emotional reactions and functionality»
- mode: NR — Page 2, Procedure — «The first author accompanied the participants who had difficulty completing the forms and scales»
- instruments: Misophonia Interview Scale (Öz et al.; Turkish) with Öz diagnostic criteria, incl. Sound Disturbance Problems Form and Misophonia Symptom List (MSL) — Page 2-3 — «the diagnostic criteria recommended by Öz et al. were used, and the form of "Sound Disturbance Problems" was added to the misophonia interview scale.»
- instrument_validated_in_language: NR — Page 2 — «Öz et al. developed the misophonia interview scale (8,20).»
- pub_status: journal — Page 1, header — «MEDICAL RECORDS-International Medical Journal»
- language: English — Page 1 — «Misophonia and its Relationship with Other Psychiatric Disorders»
- funding_coi: No financial support; no competing interests — Page 7 — «This study has no financial support.»
- notes: Control group recruited separately from the patients and selected for having no psychiatric history. The age range (18-65) and collection dates are stated for the patients only. Age and sex are not reported by sample. Same question as for the patient sample over whether the misophonia criteria were self-completed or applied in an interview.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Hospital staff and relatives do not form a frame for a healthy/general population — Page 2, Sample — «50 healthy volunteers from hospital staff and their relatives»
2. способ отбора: **no** — Volunteer convenience sample — Page 2, Sample — «healthy volunteers ... who agreed to participate in the study»
3. размер выборки: **no** — n=50 < 385 — Table 2 — «Healthy 9 8.6 41 25.9»
4. описание выборки и условий: **no** — Age, sex and dates not reported for this sample — Page 2, Sample — «50 healthy volunteers from hospital staff and their relatives»
5. охват (пропуски): **yes** — All 50 classified (9 + 41) — Table 2 — «Healthy 9 8.6 41 25.9»
6. валидность определения случая: **no** — Self-completed ad hoc Öz criteria, no published validation stated — Page 3 — «were defined as having "disorder-level misophonia."»
7. единое надёжное измерение: **unclear** — No reliability reported; some participants assisted — Page 2 — «The first author accompanied the participants who had difficulty completing the forms and scales»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator given — Page 4, Results — «16% (n=8) of healthy individuals were diagnosed with disorder-level misophonia, and 2% (n=1) with symptom-level misophonia.»
9. отклик: **unclear** — Number approached not reported — Page 2 — «who agreed to participate in the study»

Правки:
- 

Проверено: да
---

## ST054 · Orloff 2023 · Journal of open psychology data

Основной отчёт R0777: [текст](../../fulltext/text/R0777.txt) — «Curation of FOAMS: a Free Open-Access Misophonia Stimuli Database.» — [DOI](https://doi.org/10.5334/jopd.94)
Расхождения в тексте: Sex is given for only 19 of 21 participants (11 female + 8 male), so 2 are unaccounted for. The S5 is cited as Vitoratou et al. 2021, and its prevalence comparison as Vitoratou et al. 2023. The Background says 5-20% and the Reuse section says about 20%; these figures are from other studies, not from this one.
Заметка ИИ: This paper is mainly a description of a stimulus database. The only prevalence figure is a by-the-way pilot count: 4 of 21 scored above 87 on the S-Five. The DMQ was given but no case count is reported.

### ST054-1 · Ohio State University undergraduate pilot sample (Intro Psychology), USA, n=21
Отчёты: R0777 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | S-Five · S-Five >87 ("scored above the 87 criterion") | **L2** | **4 / 21** | 19.0 | 2.2 Sample | «Our 21 participants had a mean S5 score of 44.8 (range: 0-134); four participants scored above the 87 criterion» |

- E1: источник порога: validation paper; правило: S-Five row; L2 >=87; у авторов: «misophonia is suggested to be present above scores of 87»; главная у авторов: yes; период: current; заметка: Authors say 'above' 87; unclear whether a score of exactly 87 counted as a case. Cut-off cited from Vitoratou et al. 2021/2023.

**Ключевые поля выборки:**
- **n_analysed: 21** — 2.2 Sample — «Our 21 participants had a mean S5 score of 44.8 (range: 0-134); four participants scored above the 87 criterion»
- **population: university_students** — 2.2 Sample — «Participants were undergraduate students who were enrolled in an Introduction to Psychology course»
- **sampling: convenience** — 2.2 Sample — «Participants were undergraduate students who were enrolled in an Introduction to Psychology course at The Ohio State University and received course credit for their participation.»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — 2.2 Sample — «enrolled in an Introduction to Psychology course at The Ohio State University»
- setting: university (laboratory experiment, The Ohio State University) — 2.2 Sample; 2.3 Study design — «The experiment was run in a dimly lit, sound-attenuated testing room»
- data_years: NR — 3.7 Publication Date — «September 25, 2022»
- design: screening phase of experiment — 2.1.2 Pilot stimuli — «Pilot discomfort ratings were derived from a larger experiment studying the cognitive and social effects of misophonia via a face memory task»
- topic_disclosed: NR — 2.3 Study design — «Participants were made aware that sounds would play concurrently with the faces, and that some sounds may feel unpleasant to them.»
- inclusion_exclusion: Undergraduates in Intro Psychology course at Ohio State receiving course credit; no other criteria reported — 2.2 Sample — «Participants were undergraduate students who were enrolled in an Introduction to Psychology course at The Ohio State University and received course credit»
- n_invited: NR — 2.2 Sample — «21 participants ... were recruited for the pilot.»
- n_responded: 21 — 2.2 Sample — «21 participants (Mean Age = 18.5; 11 female, 8 male) were recruited for the pilot.»
- response_rate: NR — 2.2 Sample — «21 participants ... were recruited for the pilot.»
- age_mean: 18.5 — 2.2 Sample — «Mean Age = 18.5»
- age_sd: NR — 2.2 Sample — «Mean Age = 18.5»
- age_min: NR — 2.2 Sample — «Mean Age = 18.5»
- age_max: NR — 2.2 Sample — «Mean Age = 18.5»
- age_group: NR — 2.2 Sample — «Mean Age = 18.5; ... undergraduate students»
- pct_female: 52.4 — 2.2 Sample — «11 female, 8 male»
- informant: self — 2.2 Sample — «Participants were assessed for misophonia using the Duke Misophonia Questionnaire (DMQ; Rosenthal et al., 2021) and Selective Sound Sensitivity Syndrome Scale …»
- mode: NR — 2.2 Sample — «Participants were assessed for misophonia using the Duke Misophonia Questionnaire (DMQ...) and Selective Sound Sensitivity Syndrome Scale (S5...)»
- instruments: DMQ (English); S-Five (English) — 2.2 Sample; 3.5 Language — «Duke Misophonia Questionnaire (DMQ; Rosenthal et al., 2021) and Selective Sound Sensitivity Syndrome Scale (S5; Vitoratou et al., 2021)»
- instrument_validated_in_language: yes — 2.2 Sample — «Selective Sound Sensitivity Syndrome Scale (S5; Vitoratou et al., 2021), of which misophonia is suggested to be present above scores of 87 out of 250»
- pub_status: journal — Header — «Journal of open psychology data; DOI: 10.5334/jopd.94»
- language: English — Full text — «Curation of FOAMS: a Free Open-Access Misophonia Stimuli Database»
- funding_coi: NR — Full text — «All research was approved by the Institutional Review Board at The Ohio State University.»
- notes: Mainly a stimulus-database paper; the prevalence figure is a by-the-way result from a pilot of a larger dissertation experiment (Hansen et al., n.d.), which may overlap with that later report. Sex given for 19 of 21 (11 F, 8 M); pct_female computed as 11/21. Age range not reported (mean 18.5), so age_group = NR, though participants are probably adults. DMQ was given but no DMQ case count is reported. Individual S5/DMQ scores are in MisoAssessments.csv on Zenodo (10.5281/zenodo.8170180); that file was not read. Years of data collection not reported.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is one introductory psychology course, only part of a university student population — 2.2 Sample — «undergraduate students who were enrolled in an Introduction to Psychology course at The Ohio State University»
2. способ отбора: **no** — Volunteer participation for course credit (convenience) — 2.2 Sample — «received course credit for their participation»
3. размер выборки: **no** — n = 21 < 385 — 2.2 Sample — «21 participants ... were recruited for the pilot.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection missing — 2.2 Sample — «21 participants (Mean Age = 18.5; 11 female, 8 male)»
5. охват (пропуски): **yes** — Misophonia scores available for all 21 participants — 3.2.2 Pilot — «MisoAssessments.csv: DMQ and S5 assessment scores for all 21 participants»
6. валидность определения случая: **yes** — S-Five cut-off 87, English version validated — 2.2 Sample — «misophonia is suggested to be present above scores of 87 out of 250»
7. единое надёжное измерение: **unclear** — Same instrument for everyone, but mode and reliability not reported — 2.2 Sample — «Participants were assessed for misophonia using the Duke Misophonia Questionnaire (DMQ...) and Selective Sound Sensitivity Syndrome Scale (S5...)»
8. статистика (числитель и знаменатель): **yes** — Numerator 4 and denominator 21 clear; CI calculable — 2.2 Sample — «Our 21 participants ... four participants scored above the 87 criterion»
9. отклик: **unclear** — Number invited/eligible not reported — 2.2 Sample — «21 participants ... were recruited for the pilot.»

Правки:
- 

Проверено: да
---

## ST055 · Patel 2023 · Indian journal of otolaryngology and head and neck surgery : official publicati…

Основной отчёт R0779: [текст](../../fulltext/text/R0779.txt) · [PDF](../../fulltext/pdf/R0779.pdf) — «Prevalence of Misophonia in College Going Students of India: A Preliminary Survey.» — [DOI](https://doi.org/10.1007/s12070-022-03266-z)
Расхождения в тексте: 1) The sex-specific prevalences (8.84% males, 7.01% females) use the total sample of 328 as denominator (29/328, 23/328), not the sex totals; within-sex rates are 29/148 = 19.6% and 23/180 = 12.8%. 2) The sex paragraph repeats the whole-sample percentages for mild (33.84%) and subclinical (50.3%), which do not apply to the sex subgroups. 3) Methods give females as 54.87%; 180/328 = 54.88%. 4) A-MISO-S reference [8] is Jamir et al. 2014, a paper on noise pollution, so the citation is wrong. 5) The Introduction reports Zhou et al. as 20%, while the Discussion says 6% of Chinese students. 6) Chi-square is printed as 'p > 005' (typo). 7) Table 1 has no extreme band; the band counts (165+111+47+5 = 328; male 148; female 180) match the sample totals. 8) The MQ (Symptom + Emotions-and-Behaviors sections only) was given to all participants, but only means by A-MISO-S band are reported, so there…
Заметка ИИ: There is one eligible sample. The primary estimate is A-MISO-S >=10: 52/328 (15.85%). Age is reported only by sex, so overall age mean and SD are NR. The language of the instruments, the recruitment method, the number invited and the data-collection dates are not reported.

### ST055-1 · Undergraduate students, India, online survey, n=328
Отчёты: R0779 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>=10 | **L2** | **52 / 328** | 15.9 | Page 2, Results; Page 3, Table 1 | «the prevalence of misophonia was approximately 15.85% with moderate (N = 47) to severe degree (N = 5) of misophonia according to A-MISO scale.» |
| E2 | male | A-MISO-S · A-MISO-S>=10 | **L2** | **29 / 148** | 19.6 | Page 2, Results; Page 3, Table 1 | «a total of 8.84% males and 7.01% females with moderate (Males N = 26, Females N = 21) to a severe degree (Males N = 3, Females N = 2)» |
| E3 | female | A-MISO-S · A-MISO-S>=10 | **L2** | **23 / 180** | 12.8 | Page 2, Results; Page 3, Table 1 | «a total of 8.84% males and 7.01% females with moderate (Males N = 26, Females N = 21) to a severe degree (Males N = 3, Females N = 2)» |
| E4 | all | A-MISO-S · A-MISO-S>=5 | **L1** | **163 / 328** | 49.7 | Page 2, Results; Page 3, Table 1 | «moderate (N = 47) to severe degree (N = 5) ... it was also found that most of them (N = 111) also exhibited mild misophonia (33.84%) symptoms that are a risk for developing misophonia.» |
| E5 | male | A-MISO-S · A-MISO-S>=5 | **L1** | **74 / 148** | 50.0 | Page 2, Results; Page 3, Table 1 | «moderate (Males N = 26, Females N = 21) to a severe degree (Males N = 3, Females N = 2) ... most of them (Males N = 45, Females N = 66) also exhibited mild misophonia» |
| E6 | female | A-MISO-S · A-MISO-S>=5 | **L1** | **89 / 180** | 49.4 | Page 2, Results; Page 3, Table 1 | «moderate (Males N = 26, Females N = 21) to a severe degree (Males N = 3, Females N = 2) ... most of them (Males N = 45, Females N = 66) also exhibited mild misophonia» |
| E7 | all | A-MISO-S · A-MISO-S>=15 | **L2** | **5 / 328** | 1.5 | Page 2, Results; Page 3, Table 1 | «moderate (N = 47) to severe degree (N = 5) of misophonia according to A-MISO scale.» |
| E8 | male | A-MISO-S · A-MISO-S>=15 | **L2** | **3 / 148** | 2.0 | Page 2, Results; Page 3, Table 1 | «to a severe degree (Males N = 3, Females N = 2)» |
| E9 | female | A-MISO-S · A-MISO-S>=15 | **L2** | **2 / 180** | 1.1 | Page 2, Results; Page 3, Table 1 | «to a severe degree (Males N = 3, Females N = 2)» |

- E1: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (moderate+severe+extreme); у авторов: «misophonia (moderate to severe)»; главная у авторов: yes; период: NR; **расчёт: 47 (moderate) + 5 (severe) + 0 (no extreme band) from Table 1; 52/328 = 15.85%, matching the reported figure**; заметка: Discussion rounds this to 15.9%.
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate to severe misophonia»; главная у авторов: no; период: NR; **расчёт: 26 (moderate) + 3 (severe) from Table 1; n = 148 males**; заметка: The authors' 8.84% is 29/328, using the total sample as denominator. The within-sex rate is 29/148 = 19.6%.
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «moderate to severe misophonia»; главная у авторов: no; период: NR; **расчёт: 21 (moderate) + 2 (severe) from Table 1; n = 180 females**; заметка: The authors' 7.01% is 23/328, using the total sample as denominator. The within-sex rate is 23/180 = 12.8%.
- E4: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands (mild+moderate+severe+extreme); у авторов: «mild or more (mild = 'at risk for developing misophonic symptoms')»; главная у авторов: no; период: NR; **расчёт: 111 (mild) + 47 (moderate) + 5 (severe) from Table 1 = 163; 163/328 = 49.7%**; заметка: Equivalently 328 - 165 subclinical = 163.
- E5: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «mild or more»; главная у авторов: no; период: NR; **расчёт: 45 (mild) + 26 (moderate) + 3 (severe) from Table 1 = 74**
- E6: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; у авторов: «mild or more»; главная у авторов: no; период: NR; **расчёт: 66 (mild) + 21 (moderate) + 2 (severe) from Table 1 = 89**
- E7: источник порога: developer paper; правило: A-MISO-S row; G2 (above L2 cut-off); G1 sum of bands (severe+extreme); у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: 5 (severe) + 0 (no extreme band; band counts sum to 328) from Table 1**
- E8: источник порога: developer paper; правило: A-MISO-S row; G2; G1; у авторов: «severe»; главная у авторов: no; период: NR; заметка: No extreme band was reported.
- E9: источник порога: developer paper; правило: A-MISO-S row; G2; G1; у авторов: «severe»; главная у авторов: no; период: NR; заметка: No extreme band was reported.

**Ключевые поля выборки:**
- **n_analysed: 328** — Page 2, Methods; Page 3, Table 1 — «The total participants were 328 undergraduate students all over India»
- **population: university_students** — Page 2, Methods — «The total participants were 328 undergraduate students all over India»
- **sampling: NR** — Page 2, Methods — «An online survey was conducted through Google forms»

**Остальные поля:**
- clinical_group: NA — Page 2, Methods — «328 undergraduate students all over India»
- country: IND — Page 2, Methods — «The total participants were 328 undergraduate students all over India, with diverse cultural, linguistic, and economic backgrounds.»
- setting: university (undergraduate students from across India; online survey) — Page 2, Methods — «328 undergraduate students all over India ... An online survey was conducted through Google forms»
- data_years: NR — Page 1, header — «Received: 17 February 2021 / Accepted: 26 October 2022»
- design: cross-sectional — Page 2, Methods — «An online survey was conducted through Google forms, wherein the participants filled the self-rating Amsterdam Misophonia Scale (A-MISO-S) [8] and Misophonia Q…»
- topic_disclosed: NR — Page 4, Consent for Participation — «All the procedures were explained to the participants, and informed consent was taken from all the participants of the study.»
- inclusion_exclusion: Undergraduate students aged 18-25; excluded anyone with a history or signs of otological or psychological problems, or on medication — Page 2, Methods — «None of the participants had any history or signs and symptoms of otological problems, psychological problems, neither were under medications.»
- n_invited: NR — Page 2, Methods — «An online survey was conducted through Google forms»
- n_responded: NR — Page 2, Methods — «The total participants were 328 undergraduate students»
- response_rate: NR — Page 2, Methods — «An online survey was conducted through Google forms»
- age_mean: NR — Page 2, Methods — «males (Mean age = 20.24 years, SD = 1.96), females (Mean age- 22.79 years, SD = 1.59)»
- age_sd: NR — Page 2, Methods — «males (Mean age = 20.24 years, SD = 1.96), females (Mean age- 22.79 years, SD = 1.59)»
- age_min: 18 — Page 2, Methods — «The participant’s age ranged from 18 to 25 years»
- age_max: 25 — Page 2, Methods — «The participant’s age ranged from 18 to 25 years»
- age_group: adults — Page 2, Methods — «The participant’s age ranged from 18 to 25 years»
- pct_female: 54.87 — Page 2, Methods — «The number of female (total no = 180, percentage = 54.87%) participants were slightly higher compared to male (total no = 148, percentage = 45.12%)»
- informant: self — Page 2, Methods — «participants filled the self-rating Amsterdam Misophonia Scale (A-MISO-S)»
- mode: online — Page 2, Methods — «An online survey was conducted through Google forms»
- instruments: A-MISO-S, self-rating version (language version NR); MQ (Wu et al. 2014), Symptom Scale + Emotions-and-Behaviors Scale only, total 0-68 (language version NR) — Page 2, Methods — «self-rating Amsterdam Misophonia Scale (A-MISO-S) [8] and Misophonia Questionnaire [5] ... In this study, only the first two sections were considered.»
- instrument_validated_in_language: NR — Page 2, Methods; Page 5, References — «self-rating Amsterdam Misophonia Scale (A-MISO-S) [8]»
- pub_status: journal — Page 1, header — «Indian J Otolaryngol Head Neck Surg (2023) 75:374–378»
- language: English — Full text — «Prevalence of Misophonia in College Going Students of India: A Preliminary Survey»
- funding_coi: No funding; authors report no conflicts of interest — Page 4, Funding; Conflict of interest — «There is no funding by any agency for the manuscript. ... The authors report no conflicts of interest.»
- notes: Age is reported only by sex: males mean 20.24 (SD 1.96), females mean 22.79 (SD 1.59). The weighted overall mean is about 21.64 (computed by the extractor, not reported). The language of the questionnaires is not stated; probably English, but this is not reported. The A-MISO-S citation [8] points to a paper on noise pollution (Jamir et al. 2014), not to the scale's source, so no validation is cited. Recruitment and data-collection dates are not described; data were collected before February 2021. The MQ was given to everyone, but only means by A-MISO-S band are reported, with no MQ-based prev…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — The target population is college students in India, but the sampling frame is not described; only 'students all over India' and an online Google Form are mentioned. — Page 2, Methods — «The total participants were 328 undergraduate students all over India»
2. способ отбора: **unclear** — Recruitment method not described. An online Google Forms survey is probably volunteer opt-in, which would make this 'no'. — Page 2, Methods — «An online survey was conducted through Google forms»
3. размер выборки: **no** — n = 328, below 385 — Page 2, Methods — «The total participants were 328 undergraduate students»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported, but the dates of data collection are missing. — Page 2, Methods — «The participant’s age ranged from 18 to 25 years—males (Mean age = 20.24 years, SD = 1.96), females (Mean age- 22.79 years, SD = 1.59).»
5. охват (пропуски): **yes** — All 328 participants are classified into A-MISO-S bands (165+111+47+5 = 328), so no misophonia data are missing among the reported participants. — Page 3, Table 1 — «Sub clinical ... Total 165 ... Mild ... Total 111 ... Moderate ... Total 47 ... Severe ... Total 5»
6. валидность определения случая: **unclear** — The primary definition is A-MISO-S >=10 (an anchored cut-off), but the language version is not stated and the scale's citation points to an unrelated paper, so it is unclear whether a validated language version was used. — Page 2, Methods — «self-rating Amsterdam Misophonia Scale (A-MISO-S) [8] ... moderate (score 10–14), severe (score 15–19), extreme (score 20–24) [8].»
7. единое надёжное измерение: **unclear** — Same self-rated online instrument and threshold for everyone, but no internal consistency is reported for this sample and the cited source is wrong. — Page 2, Methods — «It’s a self-rating questionnaire, where each question has 4 descriptive options corresponding to the score»
8. статистика (числитель и знаменатель): **yes** — The numerator (47+5 = 52) and denominator (328) are clear; no CI is given but one can be calculated. The sex-specific percentages use the total sample as denominator, but the counts can be traced. — Page 2, Results — «the prevalence of misophonia was approximately 15.85% with moderate (N = 47) to severe degree (N = 5) of misophonia according to A-MISO scale.»
9. отклик: **unclear** — Response rate and number invited not reported. If this was an open online survey, the rating would be 'no'. — Page 2, Methods — «An online survey was conducted through Google forms»

Правки:
- 

Проверено: да
---

## ST056 · SAKARYA 2023 · Turkiye Klinikleri Journal of Health Sciences

Основной отчёт R0794: [текст](../../fulltext/text/R0794.txt) · [PDF](../../fulltext/pdf/R0794.pdf) — «Prevalance of Misophonia and its Relationship with State-Trait Anxiety in University Student: A Cross-Sectional Study» — [DOI](https://doi.org/10.5336/healthsci.2023-98758)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R1182 (ST091): Both Baskent University students, same first author (119 vs 638); R0794 cites R1182 as a separate study
Расхождения в тексте: The sex subgroups add up: female 14 + male 11 = 25 cases, and 66 + 53 = 119. Table 2 'number of people lived with' adds to 83 + 37 = 120, which does not match n = 119 (and the percentages 69% + 31%); this does not affect the prevalence counts. The abstract's conclusion says 'approximately a quarter', but the counts give 21% (25/119). In Table 5 the 'misophonia symptoms' correlations are swapped compared with the text: the text gives state 0.313 and trait 0.181, the table gives trait 0.313 and state 0.181. This does not affect prevalence.
Заметка ИИ: Main estimate: MQ Severity Scale >=7 (Turkish version, validated), 25 of 119 (21%), level L2. Points for the reviewer: (1) the authors state simple random sampling but give no sampling frame or number invited, and all students came from three faculties; (2) possible overlap with R1182 (Turkish MQ validation, same first author); (3) data collection years are not reported; (4) mode was coded face-to-face, but this means self-report forms handed out in person, not an interview.

### ST056-1 · Başkent University undergraduate students, Ankara, Turkey (n=119)
Отчёты: R0794 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **25 / 119** | 21.0 | Page 5, Bulgular; Page 1, Abstract | «Katılımcıların MQ kesim değerine göre klinik olarak anlamlı mizofonisi olanların oranı %21 (n=25) idi. [By the MQ cut-off, 21% (n=25) had clinically significant misophonia.]» |
| E2 | female | MQ · MSS>=7 | **L2** | **14 / 66** | 21.2 | Page 5, Bulgular | «Kadınlarda mizofonisi olmayan 52 kişi ve mizofonisi olan 14 kişi belirlenmiş [Among women, 52 without and 14 with misophonia were identified]» |
| E3 | male | MQ · MSS>=7 | **L2** | **11 / 53** | 20.8 | Page 5, Bulgular | «Erkeklerde mizofonisi olmayan 42 kişi ve mizofonisi olan 11 kişi belirlenmiş [Among men, 42 without and 11 with misophonia were identified]» |

- E1: источник порога: developer paper; правило: MQ row; L2 MSS>=7 (recommended); у авторов: «clinically significant misophonia (klinik olarak anlamlı mizofoni)»; главная у авторов: yes; период: NR; заметка: Cut-off source not cited at that point; text attributes the MSS item to the original Wu et al. scale.
- E2: источник порога: developer paper; правило: MQ row; L2 MSS>=7; у авторов: «misophonia (mizofonisi olan)»; главная у авторов: no; период: NR; заметка: n = 52 + 14 = 66, matches female n.
- E3: источник порога: developer paper; правило: MQ row; L2 MSS>=7; у авторов: «misophonia (mizofonisi olan)»; главная у авторов: no; период: NR; заметка: n = 42 + 11 = 53, matches male n.

**Ключевые поля выборки:**
- **n_analysed: 119** — Page 5, Bulgular; Page 1, Abstract — «Of 119 participants, 25 (21%) were found to have clinically significant misophonia.»
- **population: university_students** — Page 3, Örneklem — «Çalışmaya 18-25 yaş arasındaki lisans öğrencileri dâhil edilmiştir. [Undergraduate students aged 18-25 were included.]»
- **sampling: probability** — Page 3, Örneklem — «Çalışmanın örneklemi, basit rastgele örnekleme yöntemi ile seçilen Başkent Üniversitesi öğrencileridir. [The sample consists of Başkent University students selected by simple random sampling.]»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Page 1, affiliations; Page 3, Örneklem — «Başkent Üniversitesi Sağlık Bilimleri Fakültesi, Odyoloji Bölümü, Ankara, Türkiye»
- setting: university (Başkent University, Ankara; faculties of education, law and dentistry) — Page 3, Örneklem — «Öğrenciler; eğitim fakültesi (%49,6), hukuk fakültesi (%36,1) ve diş hekimliği fakültesinden (%14,3) seçilmiştir. [Students were selected from the faculty of e…»
- data_years: NR — Page 3, Prosedür — «Başkent Üniversitesi Tıp ve Sağlık Bilimleri Araştırma ve Etik Kurulu tarafından onaylanmıştır (Proje No: KA18/412, Tarih: 28.12.2018). [approved by the ethics…»
- design: cross-sectional — Page 1, title — «Prevalance of Misophonia and its Relationship with State-Trait Anxiety in University Student: A Cross-Sectional Study»
- topic_disclosed: NR — Page 3, Prosedür — «Uygulama öncesi bilgilendirme metni sunulmuş ve katılımcılardan onay alınmıştır. [An information text was presented before administration and consent was obtai…»
- inclusion_exclusion: Undergraduates aged 18-25; excluded: diagnosed psychological/neurological problem or known hearing loss — Page 3, Örneklem — «Tanılanmış psikolojik/nörolojik problemi olanlar ve bilinen işitme kaybı olanlar çalışmaya dâhil edilmemiştir. [Those with a diagnosed psychological/neurologic…»
- n_invited: NR — Page 3, Örneklem — «Yapılan güç analizinde α=0,05 yanılma düzeyi ve (1-β)=0,80 test gücü ile çalışmaya 119 kişi dâhil edilmiştir.»
- n_responded: NR — Page 3, Örneklem — «çalışmaya 119 kişi dâhil edilmiştir. [119 people were included in the study.]»
- response_rate: NR — NA
- age_mean: 20.97 — Page 3, Örneklem — «Yaş ortalamaları 20,97±1,57’dir. [Mean age 20.97±1.57.]»
- age_sd: 1.57 — Page 3, Örneklem — «Yaş ortalamaları 20,97±1,57’dir.»
- age_min: 18 — Page 3, Örneklem — «Çalışmaya 18-25 yaş arasındaki lisans öğrencileri dâhil edilmiştir. [Undergraduates aged 18-25 were included.]»
- age_max: 25 — Page 3, Örneklem — «Çalışmaya 18-25 yaş arasındaki lisans öğrencileri dâhil edilmiştir.»
- age_group: adults — Page 3, Örneklem — «18-25 yaş arasındaki lisans öğrencileri»
- pct_female: 55 — Page 3, Örneklem — «Katılımcıların %55’i kadın (n=66) ve %45’i erkek (n=53) idi. [55% female (n=66), 45% male (n=53).]»
- informant: self — Page 3, Ölçme araçları — «Katılımcılara bazı demografik sorulardan oluşan kişisel bilgi formu, “MQ” ve “Durumluk ve Sürekli Kaygı Ölçeği” verilmiştir. [Participants were given a persona…»
- mode: face-to-face interview — Page 3, Prosedür — «Tüm veri toplama araçları yüz yüze uygulanmıştır. [All data collection tools were administered face to face.]»
- instruments: MQ (Misophonia Questionnaire), Turkish version 'Mizofoni Ölçeği' (Deniz Sakarya & Cakmak 2022), incl. Misophonia Severity Scale item — Page 3, MQ — «Orijinal ölçek Wu ve ark. tarafından geliştirilmiş olup, Deniz Sakarya ve Cakmak tarafından “Mizofoni Ölçeği” olarak isimlendirilerek Türkçe geçerlik-güvenirli…»
- instrument_validated_in_language: yes — Page 3, MQ; ref 15 — «Deniz Sakarya ve Cakmak tarafından “Mizofoni Ölçeği” olarak isimlendirilerek Türkçe geçerlik-güvenirlik sınaması yapılmıştır.15 [Turkish validity-reliability t…»
- pub_status: journal — Page 1, header — «Turkiye Klinikleri J Health Sci. 2023;8(4):668-76 ... ORİJİNAL ARAŞTIRMA ORIGINAL RESEARCH»
- language: Turkish (English abstract) — Page 1 — «Üniversite Öğrencilerinde Mizofoninin Yaygınlığı ve Durumluk-Sürekli Kaygı ile İlişkisi: Kesitsel Bir Araştırma»
- funding_coi: Funded by Başkent University Research Fund; authors declare no conflict of interest — Page 8, Finansal Kaynak; Çıkar Çatışması — «Başkent Üniversitesi Araştırma Fonunca desteklenmiştir. ... çıkar çatışması potansiyeli olabilecek ... durumları yoktur. [Supported by Başkent University Resea…»
- notes: Possible overlap with R1182 (ST091): Both Baskent University students, same first author (119 vs 638); R0794 cites R1182 as a separate study (ref 15, Turkish MQ validation reporting 38% in 'the same population'). Data collection dates not reported (ethics approval 28.12.2018). 'Face-to-face' refers to in-person administration of self-report questionnaires, not an interview; reviewer may prefer paper/NR. Age 18-25 is the inclusion range, not observed min/max. Table 1 gives item-level response frequencies (e.g., eating sounds 'always' 31.1%); not extracted as case definitions.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target is Başkent University undergraduates; sampling frame not described and students came from only three faculties (education, law, dentistry). — Page 3, Örneklem — «Öğrenciler; eğitim fakültesi (%49,6), hukuk fakültesi (%36,1) ve diş hekimliği fakültesinden (%14,3) seçilmiştir.»
2. способ отбора: **yes** — Simple random sampling stated, though procedure, frame and numbers invited not described; reviewer should verify. — Page 3, Örneklem — «Çalışmanın örneklemi, basit rastgele örnekleme yöntemi ile seçilen Başkent Üniversitesi öğrencileridir.»
3. размер выборки: **no** — n=119 < 385. — Page 3, Örneklem — «çalışmaya 119 kişi dâhil edilmiştir.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection missing. — Page 3, Örneklem — «Katılımcıların %55’i kadın (n=66) ve %45’i erkek (n=53) idi. Yaş ortalamaları 20,97±1,57’dir.»
5. охват (пропуски): **unclear** — Missing data not reported; all 119 included appear analysed but non-completion not described. — Page 5, Bulgular — «Katılımcıların MQ kesim değerine göre klinik olarak anlamlı mizofonisi olanların oranı %21 (n=25) idi.»
6. валидность определения случая: **yes** — MQ Misophonia Severity Scale >=7 in Turkish version with published validation (ref 15). — Page 3, MQ — «Bu bölümün en yüksek puanı 15’tir. Yedi ve üzeri işaretlemeler “klinik olarak anlamlı” mizofoniyi işaret etmektedir.»
7. единое надёжное измерение: **yes** — Same instrument, threshold and in-person mode for all; reliability reported from Turkish adaptation source. — Page 3, MQ; Prosedür — «Ölçeğin Türkçe adaptasyonunda Cronbach alfa iç tutarlılık katsayısı 0,89 ... Tüm veri toplama araçları yüz yüze uygulanmıştır.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (25/119); CI calculable. — Page 1, Abstract — «Of 119 participants, 25 (21%) were found to have clinically significant misophonia.»
9. отклик: **unclear** — Number invited and response rate not reported. — Page 3, Örneklem — «çalışmaya 119 kişi dâhil edilmiştir.»

Правки:
- 

Проверено: да
---

## ST057 · Vanukuri 2023 · World Journal of Advanced Engineering Technology and Sciences

Основной отчёт R0821: [текст](../../fulltext/text/R0821.txt) · [PDF](../../fulltext/pdf/R0821.pdf) — «Misophonia assessment on individuals with various occupations» — [DOI](https://doi.org/10.30574/wjaets.2023.8.1.0031)
Расхождения в тексте: Table 2 counts are subclinical 14, mild 6, moderate 8, severe 2 (total 30; row totals match Table 1). The text, abstract and Figure 3 give 47% subclinical (14), 20% mild (6), 23% moderate (=7) and 10% severe (=3). Moderate and severe disagree with Table 2, so the table is used. The narrative text supports Table 2: severe = one homemaker and one musician; moderate = at least one in every occupation except homemaker and ASLP. The cumulative >=mild (16/30, 53%) and >=moderate (10/30) are the same under both versions. Table 2 percentages are printed as proportions with a % sign (0.40% means 40%). Page 5 says '14%' for subclinical, which appears to be the count of 14. Page 5 also attributes the 14%-of-students figure to ref [5]; the introduction attributes it to ref [3].
Заметка ИИ: Very small sample (n=30). The recruitment method is not described. The MAQ Telugu version rests only on unpublished data. All estimates use the MAQ version A bands, whose source is not cited in the report.

### ST057-1 · Adults of various occupations, Telangana, India (n=30)
Отчёты: R0821 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MAQ · MAQ >=12 (mild or more, band version A) | **L1** | **16 / 30** | 53.3 | Page 4, Table 2; Page 5, Conclusion | «nearly 53% of participants reported mild to severe misophonia based on the misophonia assessment questionnaire» |
| E2 | all | MAQ · MAQ >=25 (moderate or more, band version A) | **L2** | **10 / 30** | 33.3 | Page 4, Table 2 | «Moderate ... AWT 1 (0.50%) Student 2 (0.50%) Musician 1 (0.50%) ... Severe Homemaker 1 (0.20%) Musician 1 (0.50%)» |
| E3 | all | MAQ · MAQ >=38 (severe or more, band version A) | **L2** | **2 / 30** | 6.7 | Page 4, Table 2; Page 5, 3.4 | «Both the homemaker and the musician reported misophonia after dialysis in severe cases. Surprisingly, no one in the study reported extreme severe misophonia.» |

- E1: источник порога: developer paper; правило: MAQ row, L1 >=12 (version A); G1 sum of bands; у авторов: «mild to severe misophonia»; главная у авторов: yes; период: NR; **расчёт: Mild 6 (2+2+0+0+0+1+1+0+0) + moderate 8 (0+0+1+2+1+1+1+1+1) + severe 2 (1+0+0+0+1+0+0+0+0) from Table 2 = 16**; заметка: 16/30 = 53.3%, consistent with the text. Band source not cited in the report.
- E2: источник порога: developer paper; правило: MAQ row, L2 >=25 (version A); G1 sum of bands; у авторов: «moderate + severe»; главная у авторов: no; период: NR; **расчёт: Moderate 8 + severe 2 from Table 2 = 10**; заметка: Band-based, not anchored (excluded in sensitivity analysis 2). The text's 23% + 10% (=7+3) also gives 10 cumulatively.
- E3: источник порога: developer paper; правило: MAQ row; G2 threshold above L2 cut-off; G1 cumulative (no extreme cases); у авторов: «Severe»; главная у авторов: no; период: NR; **расчёт: Severe 1 (homemaker) + 1 (musician) from Table 2; extreme 0**; заметка: The text/Figure 3 gives 10% severe (=3/30), which disagrees with Table 2 (2/30); the table is used. Both severe cases were the participants on dialysis.

**Ключевые поля выборки:**
- **n_analysed: 30** — Page 4, Table 2 (sum of all cells = 30) — «Homemaker 2 (0.40%) 2 (0.40%) 0 1 (0.20%) ...»
- **population: gp_other** — Page 2, Table 1 — «Homemaker 5 ... Audiologist and Speech therapist 4 ... Students 4 ... Teacher 4 ... Total Participants 30»
- **sampling: NR** — Page 2, 2.1 Participants — «30 individuals with various occupation in the age range of 23 to 54 years was participated in the study.»

**Остальные поля:**
- clinical_group: NA — Page 2, 2.1 Participants — «All of the participants were healthy, with no neurological abnormalities and normal hearing.»
- country: IND — Page 1, affiliations; Abstract — «Hyderabad, 500096, Telangana, India. ... All participants were given a developed Misophonia Assessment Questionnaire in Telugu»
- setting: community (recruitment setting not described; individuals of various occupations; authors' institutions in Hyderabad/Secunderabad, Telangana) — Page 2, 2.1 Participants — «30 individuals with various occupation in the age range of 23 to 54 years was participated in the study.»
- data_years: NR — Page 1, publication history — «Received on 20 December 2022; revised on 31 January 2023»
- design: cross-sectional — Page 2, 2.3 Procedure — «All the participants were instructed to read the questionnaire carefully and select the appropriate option from the rating scale given.»
- topic_disclosed: NR — Page 2, 2.3 Procedure — «Researcher was explained about the study and collected consent form.»
- inclusion_exclusion: Healthy adults of various occupations with normal hearing (informal screening); neurological abnormalities excluded; two participants on dialysis included — Page 2, 2.1 Participants — «All of the participants were healthy, with no neurological abnormalities and normal hearing. Other neurological abnormalities were excluded from the study, wit…»
- n_invited: NR — Page 2, 2.1 — «30 individuals with various occupation in the age range of 23 to 54 years was participated in the study.»
- n_responded: 30 — Page 2, Table 1 — «Total Participants 30»
- response_rate: NR — Page 2, 2.1 — «30 individuals with various occupation ... was participated in the study.»
- age_mean: NR — Page 2, 2.1 — «in the age range of 23 to 54 years»
- age_sd: NR — Page 2, 2.1 — «in the age range of 23 to 54 years»
- age_min: 23 — Page 2, 2.1 — «in the age range of 23 to 54 years»
- age_max: 54 — Page 2, 2.1 — «in the age range of 23 to 54 years»
- age_group: adults — Page 2, 2.1 — «in the age range of 23 to 54 years»
- pct_female: NR — Page 5, 3.5 — «in other factors such as Gender and Condition there is no significant difference (p=1.00; P>0.05)»
- informant: self — Page 2, 2.3 — «All the participants were instructed to read the questionnaire carefully and select the appropriate option from the rating scale given.»
- mode: NR — Page 2, 2.3 — «All the participants were instructed to read the questionnaire carefully and select the appropriate option from the rating scale given.»
- instruments: MAQ, Telugu version (MAQ-T; 21 items, 4-point scale, plus 3 additional questions on trigger condition, hyperacusis, other issues) — Page 2, 2.2 Material — «[9] developed the Misophonia Assessment Questionnaire in Telugu (MAQ-T), which had an excellent Cronbach's value of 0.925 ... The questionnaire includes 21 que…»
- instrument_validated_in_language: no — Page 6, Reference [9] — «[9] Lakshmi Prasanna P (2023) Misophonia Assessment Questionnaire in Telugu, unpublished data, submitted to research department, Helenkeller's Institute, Hyder…»
- pub_status: journal — Page 1, header — «World Journal of Advanced Engineering Technology and Sciences, 2023, 08(01), 225–230»
- language: English — Full text — «Misophonia assessment on individuals with various occupations»
- funding_coi: Funding NR; authors declare no conflicts of interest — Page 5, Disclosure of conflict of interest — «The authors declared that there are no conflicts of interest.»
- notes: Telugu MAQ is described as 21 items on a four-point scale (0-63 range implied by bands). Its only source is unpublished data by the corresponding author. The band source (version A: 0-11 subclinical, 12-24 mild, 25-37 moderate, 38-50 severe, 51-63 extreme) is not cited. Recruitment method is not described. Sex distribution is not reported. Table 2 percentages are printed as proportions with a % sign (e.g., 0.40% = 40%). Occupation-level counts in Table 2 (n=2-5 per occupation) are not extracted as subgroup estimates because occupation is not a sex, age or clinical subgroup. Two participants o…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target is individuals of various occupations; the sampling frame is not described. — Page 2, 2.1 — «30 individuals with various occupation in the age range of 23 to 54 years was participated in the study.»
2. способ отбора: **unclear** — Recruitment and sampling method not described; it appears to be a small selection by occupation, not probability sampling. — Page 2, 2.1 — «30 individuals with various occupation in the age range of 23 to 54 years was participated in the study.»
3. размер выборки: **no** — n=30, below 385. — Page 2, Table 1 — «Total Participants 30»
4. описание выборки и условий: **no** — Age range and occupations reported. Sex distribution, dates and precise setting are not reported. — Page 2, 2.1; Table 1 — «30 individuals with various occupation in the age range of 23 to 54 years»
5. охват (пропуски): **yes** — All 30 participants are classified in Table 2; no missing data. — Page 4, Table 2 — «Subclinical Mild Moderate Severe ... Correspondent 2 (0.66%) 0 1 (0.33%) 0»
6. валидность определения случая: **no** — Primary L2 definition (MAQ >=25, band version A) is not anchored to an interview or ROC. The Telugu version has no published validation (unpublished data). — Page 2, 2.3; Page 6, Ref [9] — «Subclinical: 0-11; Mild: 12-24; Moderate: 25-37; Severe: 38-50; and Extreme: 51-63.»
7. единое надёжное измерение: **yes** — Same questionnaire and scoring for all participants; source reports Cronbach's alpha 0.925 (unpublished source). — Page 2, 2.2 — «Misophonia Assessment Questionnaire in Telugu (MAQ-T), which had an excellent Cronbach's value of 0.925»
8. статистика (числитель и знаменатель): **no** — Reported band percentages (23% moderate, 10% severe) do not match Table 2 counts (8 moderate, 2 severe). Table percentages are misformatted. No CI given. — Page 4, 3.3 and Table 2 — «47% are subclinical, 23% are moderate, 20% are mild, and 10% are severe.»
9. отклик: **unclear** — Number invited and response rate not reported. — Page 2, 2.1 — «30 individuals with various occupation ... was participated in the study.»

Правки:
- 

Проверено: да
---

## ST058 · Vitoratou 2023 · PloS one

Основной отчёт R0823: [текст](../../fulltext/text/R0823.txt) — «Misophonia in the UK: Prevalence and norms from the S-Five in a UK representative sample.» — [DOI](https://doi.org/10.1371/journal.pone.0282777)
Приложен R0822: [текст](../../fulltext/text/R0822.txt) · [PDF](../../fulltext/pdf/R0822.pdf) — «Misophonia in the UK: Prevalence and Norms for the S-Five in a UK Representative Sample, 2020-2022»
Приложен R0986: [текст](../../fulltext/text/R0986.txt) · [PDF](../../fulltext/pdf/R0986.pdf) — «Misophonia in the UK: Norms of the selective sound sensitivity five factor model (S-Five) for misophonia and prevalence…»
Связь отчётов: UK representative Prolific sample (n = 772, S-Five): UK Data Service record R0822, preprint R0986, PLoS ONE article R0823
Не выписано ИИ: Self-identified misophonia sample interviewed for ROC calibration: 30 invited, 26 interviewed, 21/26 (81%) classified 'significant misophonia' by the Pre-OK-SCIM. Excluded as E1 because it was recruited because of misophonia. The 29 Prolific interviewees are a subsample of the main sample (listed as a subgroup estimate), not a separate sample.
Расхождения в тексте: R0823 (main), R0822 (the PLoS ONE PDF with pages, deposited with the UK Data Service record) and preprint R0986 report the same figures: n=772, 142 cases, 18.4%, cut-off 87, age 46.4 (15.5). The preprint says data are available on request; the journal version points to the UK Data Service. Gender adds up: 396 + 372 + 4 = 772. The sex chi-square uses N=768 (non-binary excluded), and the age-by-gender t-test has df=758, which suggests about 760 with gender and age. The age comparison of cases and non-cases has df=770. The 'SD' values for those groups (1.21, 0.63) look like standard errors. Sample sizes for the secondary misophonia measures differ between tables: A-MISO-S N=396 in Table 3 vs N=319 in Table 5; MQ N=376 vs 300; S-Five-T N=752. No prevalence is reported for MQ or A-MISO-S. The text refers to 'A-MISO-R' while the tables say A-MISO-S. pct_female was computed as 396/772 = 51.3% …
Заметка ИИ: One eligible sample. The primary estimate is S-Five >=87, 142/772, L2, flagged under G8 because the cut-off was derived in the same report. A self-identification L1 estimate (derived) and an L3 interview count on a purposive subsample of 29 are listed but are not suitable as sample-level pooled prevalence. Possible overlap: other reports from the same S-Five study battery may reuse this Prolific UK sample.

### ST058-1 · UK representative Prolific online sample, GBR, n=772 (S-Five)
Отчёты: R0823 (main); R0822; R0986

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | S-Five · S-Five total >=87 (of 250) | **L2** | **142 / 772** | 18.4 | Results, Prevalence of misophonia in the UK population | «With 87 as the cut-off point on the S-Five, we found that 142 individuals out of 772 met the threshold for significant misophonia ... a percentage of 18.4% of the UK population» |
| E2 | all | adhoc · self-identified misophonia (identifies as having the disorder) | **L1** | **18 / 772** | 2.3 | Results, Descriptive indices | «Only 13.6% of the sample was aware of the term misophonia and 2.3% identify as having the disorder.» |
| E3 | interview subsample (Prolific participants selected across S-Five deciles) | interview · interview: Pre-OK-SCIM 'significant misophonia' (six criteria adapted from Amsterdam UMC revised criteria, Jager 2020), registered psychologists | **L3** | **4 / 29** | 13.8 | Methods, Statistical analysis; Results, Prevalence section | «The Pre-OK-SCIM classified 14% (4 participants) of the general population sample and 81% (21 participants) of the misophonia sample as having 'significant misophonia'.» |

- E1: источник порога: study's own; правило: S-Five row; L2 >=87; G8 (cut-off derived by ROC in this report); у авторов: «significant misophonia; misophonia to an extent that it causes significant burd…»; главная у авторов: yes; период: current; заметка: G8 flag: the cut-off was derived in this report by ROC against the Pre-OK-SCIM in 55 interviewees (29 from this sample plus 26 self-identified). This report is the source of the Table 1 S-Five cut-off. The authors say this is not disorder-level misophonia. No counts by sex: the authors report only …
- E2: источник порога: study's own; правило: adhoc row; L1 self-identified misophonia (no scale-based L1 estimate in sample, G11); у авторов: «identify as having the disorder»; главная у авторов: no; период: current; **расчёт: 2.3% x 772 = 17.76 -> 18**; заметка: Denominator assumed to be the full sample (772); it is not stated. The wording of the item is not reported. Awareness of the term (13.6%) is not a case definition and was not extracted.
- E3: источник порога: study's own; правило: interview row; L3 (criteria from cited source with stated modifications, applied by clinicians); у авторов: «significant misophonia»; главная у авторов: no; период: current; заметка: Purposive subsample: 30 invited from all deciles of the S-Five distribution, 29 interviewed, so this is not a prevalence estimate for the sample. It should not be pooled as one. The six criteria are not listed in full; only the modifications to Jager 2020 are given, so the L3 level needs reviewer c…

**Ключевые поля выборки:**
- **n_analysed: 772** — Results, Prevalence of misophonia in the UK population; Table 2 — «we found that 142 individuals out of 772 met the threshold for significant misophonia»
- **population: gp_other** — Methods, Recruitment — «Participants constituted a representative sample of the UK general population, recruited via Prolific.co»
- **sampling: quota** — Methods, Recruitment — «recruited via Prolific.co, via an allocation algorithm to stratify sample size across sex, age, and ethnicity using census data from the UK [23]»

**Остальные поля:**
- clinical_group: NA — NA
- country: GBR — Methods, Recruitment — «Participants constituted a representative sample of the UK general population, recruited via Prolific.co»
- setting: online panel (Prolific) — Methods, Recruitment — «recruited via Prolific.co, via an allocation algorithm to stratify sample size across sex, age, and ethnicity using census data from the UK»
- data_years: 2020-2022 — Data Availability (dataset title); R0822 title — «Misophonia in the UK: Prevalence and Norms for the S-Five in a UK Representative Sample, 2020-2022. [Data Collection]»
- design: validation study — Discussion — «The main purpose of this study was to evaluate the structure and psychometric properties of the scale, present the S-Five and S-Five-T norms for the general UK…»
- topic_disclosed: NR — Methods, Recruitment — «Participants read and consented to participants' information sheet (ethics approval reference RESCM-19/20-11826)»
- inclusion_exclusion: Aged 18+, fluent in English, no diagnosis of severe learning or intellectual disability — Methods, Recruitment — «eligibility criteria, which included being aged 18 years or older, English fluency, and no diagnosis of a severe learning or intellectual disability»
- n_invited: NR — NR
- n_responded: NR — NR
- response_rate: NR — NR
- age_mean: 46.4 — Results, Descriptive indices — «The mean age was 46.4 years old (standard deviation SD = 15.5, min = 19, max = 83)»
- age_sd: 15.5 — Results, Descriptive indices — «standard deviation SD = 15.5»
- age_min: 19 — Results, Descriptive indices — «min = 19, max = 83»
- age_max: 83 — Results, Descriptive indices — «min = 19, max = 83»
- age_group: adults — Methods, Recruitment — «being aged 18 years or older»
- pct_female: 51.3 — Results, Descriptive indices — «396 individuals identified as females (7 trans women), 372 as males (1 trans man), and 4 identified as non-binary or other»
- informant: self — Methods, Measures (S-Five) — «The S-Five consists of 25 items assessing the severity of misophonia. It is rated an interval scale from 0: not at all true to 10: completely true.»
- mode: online — Methods, Recruitment — «recruited via Prolific.co»
- instruments: S-Five (English) with S-Five-T trigger checklist; MQ (English); A-MISO-S (English, self-report); Pre-OK-SCIM semi-structured interview (English, subsample of 29) — Methods, Measures; Table 3 — «Selective sound sensitivity syndrome scale [S-Five; 22] ... Misophonia Questionnaire [MQ; 18] ... Amsterdam Misophonia Scale [A-MISO-S; 4] ... Pre-OK-SCIM»
- instrument_validated_in_language: yes — Introduction; Discussion — «Vitoratou [22] used the responses of individuals who identified with having misophonia in four waves of sampling to develop a robust psychometric tool ... the …»
- pub_status: journal — Header (venue: PLoS ONE 2023) — «Year: 2023; venue: PloS one; DOI: 10.1371/journal.pone.0282777»
- language: English — Full text — «Misophonia in the UK: Prevalence and norms from the S-Five in a UK representative sample»
- funding_coi: NIHR Maudsley BRC (SLaM/KCL) and Wellcome Trust (102176/B/13/Z); funders had no role; authors declare no competing interests — Funding Statement; R0822, p. 2 (Competing interests) — «funded by the NIHR Maudsley Biomedical Research Centre ... funded in whole, or in part, by the Wellcome Trust [JG; Grant number 102176/B/13/Z] ... Competing in…»
- notes: The S-Five >=87 cut-off was derived by ROC in this report (G8 flag). The ROC used 55 interviewees: 29 from this sample, chosen across S-Five deciles, plus 26 from a separately recruited self-identified misophonia sample. The S-Five development sample (Vitoratou 2021, Psych) is a different, self-identified sample. The 772 participants completed a battery of 17 scales, so other reports from the S-Five study may reuse this Prolific sample: check for overlap. MQ and A-MISO-S were given to subsets only (about 300-396), with no prevalence reported. 13.6% were aware of the term misophonia.

**Риск смещения (JBI):**
1. рамка выборки: **no** — The target is the UK general population, but the frame is Prolific panel members, which covers only part of it. — Methods, Recruitment — «Participants constituted a representative sample of the UK general population, recruited via Prolific.co»
2. способ отбора: **no** — Non-probability online panel with quota stratification by sex, age and ethnicity. — Methods, Recruitment — «via an allocation algorithm to stratify sample size across sex, age, and ethnicity using census data from the UK»
3. размер выборки: **yes** — n = 772, which is at least 385. — Results, Prevalence section — «142 individuals out of 772»
4. описание выборки и условий: **yes** — Age, sex, setting and country are reported. Dates come only from the title of the data record (2020-2022). — Results, Descriptive indices; Data Availability — «The mean age was 46.4 years ... 396 individuals identified as females ... UK Representative Sample, 2020-2022»
5. охват (пропуски): **yes** — The prevalence denominator equals the full sample (772), and S-Five norms are reported for N = 772. No missing S-Five data is apparent. — Table 2; Results, Prevalence section — «Norms and reliability of the S-Five 5 factors and total scores (N = 772)»
6. валидность определения случая: **yes** — S-Five >= 87 in the English version, which has published validation. The cut-off was ROC-derived against the Pre-OK-SCIM in this same report (G8 flag). — Results, Prevalence section — «The ROC analysis suggested a cut-off score for the S-Five total as 87 or above (out of 250) for the presence of significant misophonia ... sensitivity 84%, spe…»
7. единое надёжное измерение: **yes** — Everyone completed the same online instrument with the same threshold. Internal consistency was reported in this sample. — Table 2 — «S-Five total | ... | 0.94 / 0.94»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are given (142/772), so a CI can be calculated. The quota design does not call for weights. — Results, Prevalence section — «142 individuals out of 772 met the threshold ... 18.4%»
9. отклик: **no** — Online panel with no reported number invited or response rate, and no handling of non-response. — Methods, Recruitment — «recruited via Prolific.co»

Правки:
- 

Проверено: да
---

## ST059 · Yıldırım Budak 2023 · Turkish Journal of Child and Adolescent Mental Health

Основной отчёт R0832: [текст](../../fulltext/text/R0832.txt) · [PDF](../../fulltext/pdf/R0832.pdf) — «Investigation of Admitted Cases with Telepsychiatry Service in the COVID-19 Pandemic Process: A Child Psychiatry Clinic Experience» — [DOI](https://doi.org/10.4274/tjcamh.galenos.2023.94824)
Расхождения в тексте: Misophonia: the text (7/77, 9.1%) and Table 1 (2 COVID-positive + 5 COVID-negative = 7) agree. Any psychiatric diagnosis: the text gives 81.6% (n=62), but 62/77 = 80.5% (81.6% would be 62/76), and Table 1 'at least one mental disorder' gives 20 + 41 = 61. The abstract says 81.6% of the 77. COVID status: text 23 positive + 54 negative = 77, consistent. Female %: derived as 77 - 41 boys = 36, 36/77 = 46.8%.
Заметка ИИ: One clinical sample of children and adolescents (ages 0-18) assessed by telephone. The misophonia case definition is a clinician diagnosis without stated criteria, so it is L1 and JBI 6 = no.

### ST059-1 · KORDEP telepsychiatry referrals, child psychiatry clinic, Istanbul, TUR, n=77
Отчёты: R0832 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | interview · clinician diagnosis of misophonia in telephone psychiatric interview using unstated 'appropriate clinical questions' | **L1** | **7 / 77** | 9.1 | Page 4, Bulgular; Page 5, Tablo 1 (Mizofoni 2 + 5); Abstract | «%13’ü (n=10) ayrılık anksiyetesi bozukluğu, %9,1’i (n=7) mizofoni [13% (n=10) separation anxiety disorder, 9.1% (n=7) misophonia]» |

- E1: источник порога: study's own; правило: interview row; study-specific criteria not stated -> L1; у авторов: «mizofoni (clinical diagnosis) [misophonia]»; главная у авторов: no; период: NR; заметка: Misophonia was one of many diagnoses; the authors' main outcome is any psychiatric diagnosis. Table 1: COVID-positive 2 (2.6%), COVID-negative 5 (6.5%), summing to 7. Informant mixed (parent only for under-6s). Ages of cases NR.

**Ключевые поля выборки:**
- **n_analysed: 77** — Page 4, Bulgular — «%9,1’i (n=7) mizofoni [9.1% (n=7) misophonia]»
- **population: clinical** — Page 3, Gereç ve Yöntem — «0-18 yaş aralığında çocuk psikiyatri alanında ihtiyacı olan çocuk/ergenler ve aileleri 2. basamak hizmeti için ... yönlendirilmiştir [children/adolescents aged 0-18 needing child psychiatry care and their families were referred for 2nd-level service]»
- **sampling: census** — Page 3, Gereç ve Yöntem — «tarafımıza yönlendirilen 0-18 yaş aralığındaki tüm çocuk ve ergenler, çalışmamızın örneklemini oluşturmuştur [all children and adolescents aged 0-18 referred to us made up the sample]»

**Остальные поля:**
- clinical_group: mixed_psychiatric — Page 4, Bulgular — «Başvuru nedenlerinin %32,5’i (n=25) endişe-korku-panik atak-sınav kaygısı-okul kaygısı-utangaçlık, %24,7’si (n=19) depresyon, %19,5’i (n=15) öfke-sinirlilik-da…»
- country: TUR — Page 3, Gereç ve Yöntem — «İstanbul Medeniyet Üniversitesi Göztepe Prof. Dr. Süleyman Yalçın Şehir Hastanesi Çocuk Psikiyatri Kliniği’ne yönlendirilmiştir [were referred to the Child Psy…»
- setting: clinic: second-level telepsychiatry (telephone) service of a university hospital child psychiatry clinic, receiving referrals from the KORDEP COVID-19 psychological support line, Istanbul — Page 3, Gereç ve Yöntem — «Triaj değerlendirmesinde ruhsal belirtilerinin şiddetine göre gerek görülen hastalar 2. basamakta çocuk psikiyatri hekimlerine ... yönlendirilmiştir [After tri…»
- data_years: 2020-2021 — Page 4, Bulgular — «Çalışmamızda Mayıs-Aralık 2020 (n=73), Ocak-Şubat 2021 (n=4) tarihleri arasında olmak üzere toplam 77 başvuru değerlendirilmiştir. [In total, 77 referrals were…»
- design: cross-sectional — Page 3, Gereç ve Yöntem — «Mayıs 2020-Şubat 2021 tarihleri arasında KORDEP bilgisayar tabanlı sistem üzerinden tarafımıza yönlendirilen 0-18 yaş aralığındaki tüm çocuk ve ergenler, çalış…»
- topic_disclosed: no — Page 3, Gereç ve Yöntem — «genel psikiyatrik değerlendirme ve olası psikiyatrik tanıların saptanması için yarı-yapılandırılmış psikiyatrik görüşme yapılmıştır [a semi-structured psychiat…»
- inclusion_exclusion: All 0-18-year-olds referred via KORDEP to the clinic May 2020-Feb 2021 whose families gave verbal consent by telephone; no exclusion criteria stated — Page 3, Gereç ve Yöntem — «Tarafımıza başvuran aileler, çalışmaya katılımları için davet edilmiştir; çalışmaya katılmaya gönüllü olanlardan telefon üzerinden sözlü onam alınmıştır. [Fami…»
- n_invited: NR — Page 3, Gereç ve Yöntem — «Tarafımıza başvuran aileler, çalışmaya katılımları için davet edilmiştir [Families who applied to us were invited to participate]»
- n_responded: 77 — Page 4, Bulgular — «toplam 77 başvuru değerlendirilmiştir [a total of 77 referrals were assessed]»
- response_rate: NR — Page 3, Gereç ve Yöntem — «çalışmaya katılmaya gönüllü olanlardan telefon üzerinden sözlü onam alınmıştır [verbal consent was taken from those volunteering]»
- age_mean: 11.17 — Page 4, Bulgular — «Başvuruların yaş ortalaması 11,17±4,26 idi [Mean age of the referrals was 11.17±4.26]»
- age_sd: 4.26 — Page 4, Bulgular — «Başvuruların yaş ortalaması 11,17±4,26 idi»
- age_min: NR — Page 3, Gereç ve Yöntem — «0-18 yaş aralığındaki tüm çocuk ve ergenler [all children and adolescents aged 0-18] (eligible range only; observed minimum not reported)»
- age_max: NR — Page 3, Gereç ve Yöntem — «0-18 yaş aralığındaki tüm çocuk ve ergenler [all children and adolescents aged 0-18] (eligible range only; observed maximum not reported)»
- age_group: mixed — Page 3, Gereç ve Yöntem; Page 7, Kısıtlılıklar — «Altı yaş altı çocuklara sadece ebeveyninden alınan bilgi ile psikiyatrik tanısı konmuştur. [Children under six were diagnosed using parent information only.]»
- pct_female: 46.8 — Page 4, Bulgular — «%53,2’sini (n=41) erkekler oluşturmaktaydı [53.2% (n=41) were boys]; derived: 77-41=36 girls, 36/77=46.8%»
- informant: mixed — Page 7, Çalışmanın Kısıtlılıkları — «Altı yaş altı çocuklara sadece ebeveyninden alınan bilgi ile psikiyatrik tanısı konmuştur. [Children under six were diagnosed using parent information only.]»
- mode: telephone — Page 2, Giriş — «tarafımızca telefon üzerinden psikiyatrik görüşme yapılmıştır [we carried out the psychiatric interview by telephone]»
- instruments: Clinician telephone interview with unstated 'appropriate clinical questions' for misophonia (Turkish); K-SADS-PL-T used for other diagnoses, does not cover misophonia — Page 3, Gereç ve Yöntem — «ÇDŞG-ŞY-T ile taranmayan ... mizofoni, ... görüşmede bu tanıları sorgulamaya yönelik uygun klinik sorular yöneltilerek taranmıştır. [Diagnoses not covered by K…»
- instrument_validated_in_language: no — Page 3, Gereç ve Yöntem — «ÇDŞG-ŞY-T ile taranmayan ... mizofoni ... uygun klinik sorular yöneltilerek taranmıştır [misophonia, not covered by K-SADS-PL-T, was screened with clinical que…»
- pub_status: journal — Page 1, header — «Turk J Child Adolesc Ment Health 2023;30(2):181-8»
- language: Turkish (English abstract) — Page 1-7, full text — «Gereç ve Yöntem: Mayıs 2020-Şubat 2021 tarihleri arasında KORDEP bilgisayar tabanlı sisteminden tarafımıza yönlendirilen [Materials and Methods: ... referred t…»
- funding_coi: No financial support; no conflicts of interest declared — Page 7, Etik — «Çıkar Çatışması: Yazarlar tarafından çıkar çatışması bildirilmemiştir. Finansal Destek: Yazarlar tarafından finansal destek almadıkları bildirilmiştir.»
- notes: Telepsychiatry (telephone) service sample during COVID-19. Misophonia was one of many clinician diagnoses, made with unstated clinical questions (criteria not given) -> L1 under the interview row. Children under 6 were diagnosed from parent report only; the age of the misophonia cases is not reported. Table 1 splits misophonia by COVID status: COVID-positive/isolated 2 (n=23), COVID-negative 5 (n=54); percentages in that table use 77 as the denominator. These were not extracted as estimates because they are not sex, age or clinical subgroups. Ethics approval was dated 25.08.2021, after data c…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — Target population is children referred to this KORDEP telepsychiatry service; the frame is all such referrals. — Page 3, Gereç ve Yöntem — «KORDEP bilgisayar tabanlı sistem üzerinden tarafımıza yönlendirilen 0-18 yaş aralığındaki tüm çocuk ve ergenler [all 0-18-year-olds referred to us via the KORD…»
2. способ отбора: **yes** — All referrals in the period were included (census). Consent was voluntary and the number who declined is not reported. — Page 3, Gereç ve Yöntem — «tüm çocuk ve ergenler, çalışmamızın örneklemini oluşturmuştur [all children and adolescents made up the sample]»
3. размер выборки: **no** — n=77, below 139 for a clinical sample. — Page 4, Bulgular — «toplam 77 başvuru değerlendirilmiştir»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates are reported. — Page 4, Bulgular — «Başvuruların yaş ortalaması 11,17±4,26 idi ve %53,2’sini (n=41) erkekler oluşturmaktaydı»
5. охват (пропуски): **unclear** — Missing data not reported. The 81.6% for n=62 implies a denominator of 76, not 77, and Table 1 gives 61 with at least one disorder. — Page 4, Bulgular — «Başvuruların %81,6’sının (n=62) psikiyatrik tanısı olduğu görüldü»
6. валидность определения случая: **no** — Clinician diagnosis from unstated clinical questions, with no explicit criteria (L1). — Page 3, Gereç ve Yöntem — «uygun klinik sorular yöneltilerek taranmıştır [screened with appropriate clinical questions]»
7. единое надёжное измерение: **unclear** — All by telephone, but under-6s were assessed by parent report only. No reliability reported for the misophonia assessment. — Page 7, Çalışmanın Kısıtlılıkları — «Altı yaş altı çocuklara sadece ebeveyninden alınan bilgi ile psikiyatrik tanısı konmuştur.»
8. статистика (числитель и знаменатель): **yes** — Numerator (7) and denominator (77) are clear; a CI can be calculated. — Page 4, Bulgular — «%9,1’i (n=7) mizofoni»
9. отклик: **unclear** — Families were invited and volunteers consented; the number of non-consenting referrals is not reported. — Page 3, Gereç ve Yöntem — «çalışmaya katılmaya gönüllü olanlardan telefon üzerinden sözlü onam alınmıştır»

Правки:
- 

Проверено: да
---

## ST060 · Zumbrunn 2023 · PsyArXiv

Основной отчёт R0833: [текст](../../fulltext/text/R0833.txt) · [PDF](../../fulltext/pdf/R0833.pdf) — «Investigating Sound-Specific Attention Control in Mild to Moderate Misophonia Using a Modified Attention Network Test» — [DOI](https://doi.org/10.31234/osf.io/swpbd)
Расхождения в тексте: Page 8 says 'Overall, 30 individuals participated' and A-MISO-S 'ranged from 0 to 14', and also that 3 participants above moderate (>14) were excluded. So the 30 is the sample after exclusion, and the screened total is not reported. Table 2 lists the 'Extreme' band as 20-28, while the instrument range is 0-24. On page 14 the Results call the table of descriptives 'Table 5', and a later winsorization table also has that label.
Заметка ИИ: Experimental study with no prevalence aim. Its estimates are an E3 median split, an L2 count (A-MISO-S >=15) with no denominator, a self-report item with no count, and an L0 any-trigger count.

### ST060-1 · DCU students, laboratory ANT experiment, Ireland, n=30
Отчёты: R0833 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S>14 (>=15) | **L2** | **3 / NR** |  | Page 8; Page 11 | «The AMISOS scores ranged from 0 to 14, however, three participants who scored above moderate misophonia levels were excluded.» |
| E2 | all | A-MISO-S · A-MISO-S > sample median 5.5 | **E3** | **15 / 30** | 50.0 | Page 8 | «Group assignment was based on whether participants scored above or below the median split score of overall participants (M= 5.5).» |
| E3 | all | adhoc · self-reported misophonia (yes/no item) | **L1** | **NR / 30** |  | Page 11; Appendix 2 (Page 40) | «Participants indicated their gender, age and whether they self-reported misophonia.» |
| E4 | all | SMS-Adult · at least one trigger on SMS part 1 checklist | **L0** | **23 / 30** | 76.7 | Page 8 | «A total of 23 participants reported at least one trigger» |

- E1: источник порога: developer paper; правило: A-MISO-S row; G2 (>=15 above L2 cut-off); у авторов: «scored above moderate misophonia levels»; главная у авторов: no; период: current; заметка: Screened denominator not reported: probably 33 (30 + 3), or 34 if the participant excluded for error rate is not among the 30. This is an exclusion criterion, not a prevalence estimate.
- E2: источник порога: percentile of this sample; правило: A-MISO-S row; G5 median split; у авторов: «misophonia group (median group)»; главная у авторов: no; период: current; заметка: 15 of 30 per 'of which 15 were categorised in each group'. Denominator excludes the 3 participants with scores >14.
- E3: источник порога: study's own; правило: adhoc row; self-identification; у авторов: «self-reported misophonia»; главная у авторов: no; период: NR; заметка: Count of self-reported misophonics not reported.
- E4: источник порога: study's own; правило: adhoc row note: any trigger = L0; у авторов: «reported at least one trigger»; главная у авторов: no; период: current; заметка: Trigger checklist only (part 1), not the SMS part 2 score.

**Ключевые поля выборки:**
- **n_analysed: 30** — Page 8; Table 1 (Page 9) — «Overall, 30 individuals participated in the study, of which 15 were categorised in each group.»
- **population: university_students** — Page 9 — «All participants were students recruited via social media and posters.»
- **sampling: convenience** — Page 9 — «All participants were students recruited via social media and posters.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: IRL — Page 1; Page 13 — «School of Psychology, Dublin City University, Ireland»
- setting: university (students recruited via social media and posters; questionnaire and experiment in a research laboratory, Dublin City University) — Page 9; Page 11 — «All participants were students recruited via social media and posters.»
- data_years: NR — Page 13 — «The study received ethical approval from the DCU Psychology Ethics Committee on the 11th of October 2022 (DCUPEC_2023_101).»
- design: screening phase of experiment — Page 11, Procedure — «Participants who scored above the moderate level of misophonia (> 14) were excluded from the second part of the study.»
- topic_disclosed: NR — Page 11 — «Before participation, all participants received a plain language statement and filled out a consent form.»
- inclusion_exclusion: Students; excluded: diagnosis of a neurological or clinical disorder, visual/auditory conditions; A-MISO-S >14 excluded from experiment (3); error rate >20% excluded (1) — Page 8; Page 9; Page 11 — «Participants with a diagnosis of a neurological or clinical disorder, as well as visual and/or auditory conditions were excluded. One participant was excluded …»
- n_invited: NR — NA — «NR»
- n_responded: NR — Page 8 — «The AMISOS scores ranged from 0 to 14, however, three participants who scored above moderate misophonia levels were excluded.»
- response_rate: NR — NA — «NR»
- age_mean: 22.97 — Table 1, Page 9 — «Age (Years) 22.97 2.91»
- age_sd: 2.91 — Table 1, Page 9 — «Age (Years) 22.97 2.91»
- age_min: 19 — Page 8 — «the age ranged from 19 to 31 years»
- age_max: 31 — Page 8 — «the age ranged from 19 to 31 years»
- age_group: adults — Page 8 — «the age ranged from 19 to 31 years»
- pct_female: 63.3 — Page 8 — «Nineteen participants were female and 11 males»
- informant: self — Page 9 — «the AMISOS is a 7-item, self-report measurement assessing misophonia severity»
- mode: online — Page 11, Procedure — «The first part included filling out a questionnaire hosted on Qualtrics XM.»
- instruments: A-MISO-S (called AMISOS, 7 items, English); SMS-Adult part 1 trigger checklist (English); self-reported misophonia item (English) — Page 8; Page 9; Page 11 — «Participants indicated their gender, age and whether they self-reported misophonia. Lastly, participants completed the AMISOS and the SMS.»
- instrument_validated_in_language: yes — Page 10, Table 2; References (Page 33) — «Naylor, J., ... (2021). The prevalence and severity of misophonia in a UK undergraduate medical student population and validation of the Amsterdam Misophonia S…»
- pub_status: preprint — Header — «venue: PsyArXiv; DOI: 10.31234/osf.io/swpbd»
- language: English — Full text — «Investigating Sound-Specific Attention Control in Mild to Moderate Misophonia Using a Modified Attention Network Test»
- funding_coi: No conflict of interest or financial interest declared; funding NR — Page 13 — «Moreover, there was no conflict of interest nor financial interest for any party involved.»
- notes: Lab experiment on attention in mild/moderate misophonia; groups formed by a median split (5.5). Recruitment advert content not reported. The preprint title names misophonia, so the reviewer should check E1 (whether participants were recruited for misophonia or interest in it). n=30 is the sample after excluding 3 participants with A-MISO-S >14; the screened total (probably 33 or 34) is not stated. Count of self-reported misophonics not reported. Table 2 gives an A-MISO-S range of 0-28 ('20-28 Extreme'). Data years not reported; ethics approval 11 Oct 2022. No prevalence aim.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Students recruited via social media and posters; the frame does not cover any defined student population — Page 9 — «All participants were students recruited via social media and posters.»
2. способ отбора: **no** — Convenience volunteer recruitment — Page 9 — «All participants were students recruited via social media and posters.»
3. размер выборки: **no** — n=30, below 385 — Page 8 — «Overall, 30 individuals participated in the study»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not — Page 8; Page 13 — «Nineteen participants were female and 11 males, and the age ranged from 19 to 31 years.»
5. охват (пропуски): **no** — Participants scoring >14 were excluded from the analysed sample (3), and the screened total is not reported — Page 8 — «three participants who scored above moderate misophonia levels were excluded»
6. валидность определения случая: **no** — The only scale-based case count is A-MISO-S >14 (>=15), which is stricter than the anchored cut-off of >=10 — Page 11 — «Participants who scored above the moderate level of misophonia (> 14) were excluded»
7. единое надёжное измерение: **yes** — Same self-report A-MISO-S on Qualtrics for all participants; alpha cited from the source — Page 9 — «The scale shows good internal consistency (Cronbach's alpha = 0.88) (Schröder et al., 2013).»
8. статистика (числитель и знаменатель): **no** — No prevalence analysis; denominator of the screened sample not reported — Page 8 — «The AMISOS scores ranged from 0 to 14, however, three participants who scored above moderate misophonia levels were excluded.»
9. отклик: **no** — Open recruitment with no denominator of invited people — Page 9 — «All participants were students recruited via social media and posters.»

Правки:
- 

Проверено: да