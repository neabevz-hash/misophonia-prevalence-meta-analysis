# Проверка выписывания — файл 10 из 10

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

## ST091 · SAKARYA 2020 · DergiPark (Istanbul University)

Основной отчёт R1182: [текст](../../fulltext/text/R1182.txt) · [PDF](../../fulltext/pdf/R1182.pdf) — «Validity and Reliability Testing Study of the Turkish Version of the Misophonia Scale» — [DOI](https://doi.org/10.26650/sp2020-845239)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R0794 (ST056): Both Baskent University students, same first author (119 vs 638); R0794 cites R1182 as a separate study
Расхождения в тексте: Text (p.15) and Table 4 agree: 83 with MSS>=7 and 135 without in n=218 (38%). The counts in Table 4 (135/83) exactly match the female/male counts of the CFA subsample (p.9: 135 female, 83 male), which may be a coincidence or a reporting error; this needs checking. CFA fit statistics differ between the text (chi2 285.34, chi2/df 2.46 before modification) and Table 2 (three-factor chi2 255.94); this is not relevant to prevalence. Explained variance is given as 55.2% (results) and 55.52% (discussion). The article is dated 2022 (Vol 42(1)), but the DOI and job metadata say 2020 (submitted 22.12.2020).
Заметка ИИ: Single sample, single L2 estimate (MQ MSS>=7, 83/218). Sample-level demographics refer to the n=218 subsample that supplies the estimate. Possible overlap with R0794 (ST056) is recorded in the sample notes.

### ST091-1 · Baskent University undergraduates, Ankara, TUR (n=638; MSS estimate on CFA subsample n=218)
Отчёты: R1182 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **83 / 218** | 38.1 | Page 15, text above Tablo 4; Tablo 4; Page 18 Discussion | «218 kişilik örneklemde 7 ve üzeri işaretleme yapanların oranı %38 (N =83) olarak bulunmuştur. [In the sample of 218, the proportion marking 7 or above was 38% (N = 83).]» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 = L2 (recommended); у авторов: «klinik olarak anlamlı mizofoni [clinically significant misophonia]»; главная у авторов: yes; период: NR; заметка: Only for the CFA subsample (n=218) of the 638 students. Table 4 group sizes (135 non-misophonic, 83 misophonic) are identical to the CFA sex counts (135 female, 83 male); possible reporting error, so verify. Authors compare it with Wu 2014 (19.9%) and Zhou 2017 (16.6%).

**Ключевые поля выборки:**
- **n_analysed: 218** — Page 15, text above Tablo 4 — «218 kişilik örneklemde 7 ve üzeri işaretleme yapanların oranı %38 (N =83) olarak bulunmuştur. [In the sample of 218, the proportion marking 7 or above was 38% (N = 83).]»
- **population: university_students** — Page 9, Katılımcılar — «Mizofoni Ölçeği, Başkent Üniversitesinde 18-26 yaş aralığında lisans düzeyinde öğrenim gören 638 öğrenciye uygulanmıştır. [The scale was administered to 638 undergraduate students aged 18-26 at Başkent University.]»
- **sampling: quota** — Page 9, Katılımcılar — «Fakültelerdeki öğrenci sayıları eşit olmadığı için ağırlıklandırma yapılmış ve her fakülteden belirlenen sayı doğrultusunda öğrenci çalışmaya katılmıştır. [Because faculty sizes were unequal, weighting was applied and students took part according to a number …»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Page 2, Abstract — «The research was carried out on 638 undergraduate students at Baskent University, from 18 to 26 years of age.»
- setting: university (Baskent University, Ankara; questionnaires administered in classrooms in five faculties) — Page 10, İşlem — «Sınıflara gidilerek ölçek kağıt kalem formunda uygulanmıştır. [The scale was administered in paper-and-pencil form by visiting classrooms.]»
- data_years: NR — Page 6; Page 10, İşlem — «Bu çalışmanın planlandığı 2018 yılında [In 2018, when this study was planned]»
- design: validation study — Page 2, Abstract — «This study aims to meet the need for a measurement tool ... by adapting the Misophonia Questionnaire (Wu et al., 2014) to Turkish.»
- topic_disclosed: NR — Page 10, İşlem; Page 23, Ek 1 — «EK 1 MİZOFONİ ÖLÇEĞİ [Appendix 1 MISOPHONIA SCALE]»
- inclusion_exclusion: Undergraduates aged 18-26 at Baskent University in five selected faculties (Law, Dentistry, Education, Engineering, Health Sciences); no other criteria reported — Page 9, Katılımcılar — «Katılımcıların %15'i (N = 99) Hukuk Fakültesi, %6'sı (N = 39) Diş Hekimliği Fakültesi, %22'si (N = 138) Eğitim Fakültesi, %30'u (N = 189) Mühendislik Fakültesi…»
- n_invited: NR — NR
- n_responded: 638 — Page 9, Katılımcılar — «638 öğrenciye uygulanmıştır [administered to 638 students]»
- response_rate: NR — NR
- age_mean: 20.6 — Page 9, Katılımcılar (CFA subsample n=218) — «Öğrencilerin yaşlarının ortalaması 20.6 ve standart sapması 2.4 olarak elde edilmiştir. [Mean age 20.6, SD 2.4.]»
- age_sd: 2.4 — Page 9, Katılımcılar (CFA subsample n=218) — «Öğrencilerin yaşlarının ortalaması 20.6 ve standart sapması 2.4 olarak elde edilmiştir.»
- age_min: 18 — Page 9, Katılımcılar — «18-26 yaş aralığında [aged 18-26]»
- age_max: 26 — Page 9, Katılımcılar — «18-26 yaş aralığında [aged 18-26]»
- age_group: adults — Page 9, Katılımcılar — «18-26 yaş aralığında lisans düzeyinde öğrenim gören 638 öğrenci»
- pct_female: 62 — Page 9, Katılımcılar (CFA subsample n=218) — «Çalışmanın bu kısmına katılanların %62'si (N =135) kadın ve %38'i (N =83) erkek öğrencidir. [62% (N=135) female, 38% (N=83) male.]»
- informant: self — Page 23-25, Ek 1 — «Lütfen ses hassasiyetinizin derecesini aşağıda 1 (en az) ile 15 (çok şiddetli) arasında verilen skaladan yalnızca birini işaretleyerek belirleyiniz.»
- mode: paper — Page 10, İşlem — «Sınıflara gidilerek ölçek kağıt kalem formunda uygulanmıştır. [administered in paper-and-pencil form in classrooms]»
- instruments: MQ (Misophonia Questionnaire, Turkish version 'Mizofoni Ölçeği', incl. Misophonia Severity Scale 1-15) — Page 9-10, Veri Toplama Aracı — «Bu bölümde 7 ve üzerindeki işaretlemeler klinik olarak anlamlı mizofoniyi ifade etmektedir (Wu ve ark., 2014). [In this section, marks of 7 and above indicate …»
- instrument_validated_in_language: yes — Page 2, Abstract — «With this study, the Misophonia Questionnaire, which can be used to evaluate misophonia in the general population, was adapted into Turkish.»
- pub_status: journal — Page 1, header — «Psikoloji Çalışmaları - Studies in Psychology Cilt/Volume: 42, Sayı/Issue: 1, 2022 ... Araştırma Makalesi/Research Article»
- language: Turkish (with English abstract and extended abstract) — Page 1-4 — «Mizofoni Ölçeği'nin Türkçe Formunun Geçerlik ve Güvenirlik Sınama Çalışması [Validity and Reliability Testing Study of the Turkish Version of the Misophonia Sc…»
- funding_coi: Baskent University Research Fund; authors declare no conflict of interest — Page 20 — «Grant Support: ... supported by Baskent University Research Fund. Conflict of Interest: The authors have no conflict of interest to declare.»
- notes: Possible overlap with R0794 (ST056): both Baskent University students, same first author (119 vs 638); R0794 cites R1182 as a separate study. This report is the Turkish MQ validation. The MSS prevalence (83/218) is reported only for the CFA subsample (n=218), not for all 638 or the EFA subsample (n=420); the split method is not described. Age/sex fields refer to the n=218 subsample; whole-sample female % derivable as (307+135)/638 = 69.3%. EFA subsample: 73% female, mean age 20.9 (SD 1.6). Data years NR (planned and permission obtained 2018; ethics KA18/412; submitted Dec 2020). MSS was not p…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was only the students in five selected faculties of one university, reached by visiting classes; it does not cover all enrolled students — Page 10, İşlem — «Çalışma için belirlenen fakültelerdeki öğrenci sayısı Öğrenci İşleri Daire Başkanlığından yazılı olarak istenmiştir. [Student numbers in the faculties selected…»
2. способ отбора: **no** — Non-random allocation by faculty (quota-like) with classroom recruitment; no random selection described — Page 9, Katılımcılar — «her fakülteden belirlenen sayı doğrultusunda öğrenci çalışmaya katılmıştır [students took part according to a number set for each faculty]»
3. размер выборки: **no** — Prevalence estimate is based on n=218 (<385); full sample was 638, but no estimate is given for it — Page 15 — «218 kişilik örneklemde 7 ve üzeri işaretleme yapanların oranı %38 (N =83)»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection not reported — Page 9, Katılımcılar — «Öğrencilerin yaşlarının ortalaması 20.6 ve standart sapması 2.4 ... %62'si (N =135) kadın»
5. охват (пропуски): **unclear** — Missing data not reported; MSS estimate only for 218 of 638 respondents, and the split method is not described — Page 9; Page 15 — «Doğrulayıcı faktör analizi için ise 218 öğrenciden oluşan ikinci bir veri kullanılmıştır.»
6. валидность определения случая: **yes** — MQ Severity Scale >=7 (L2) in the Turkish MQ version, which this report validates — Page 10; Page 15 — «Bu bölümde 7 ve üzerindeki işaretlemeler klinik olarak anlamlı mizofoniyi ifade etmektedir (Wu ve ark., 2014).»
7. единое надёжное измерение: **yes** — Same paper instrument and threshold for everyone in classrooms; Cronbach alpha .89 reported in the sample — Page 16, Güvenirlik Analizleri — «Cronbach Alfa katsayısı tüm ölçek için .89»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are given (83/218), so a CI can be calculated; no design weights are needed — Page 15, Tablo 4 — «Mizofonisi Olmayan / Mizofonisi Olan 135 / 83»
9. отклик: **unclear** — Number of students approached in classes and response rate not reported — Page 10, İşlem — «Sınıflara gidilerek ölçek kağıt kalem formunda uygulanmıştır.»

Правки:
- 

Проверено: да
---

## ST092 · Siepsiak 2020 · International journal of environmental research and public health

Основной отчёт R1188: [текст](../../fulltext/text/R1188.txt) — «Prevalence of Misophonia and Correlates of Its Symptoms among Inpatients with Depression.» — [DOI](https://doi.org/10.3390/ijerph17155464)
Приложен R0810: [текст](../../fulltext/text/R0810.txt) — «Psychophysiological and psychological correlates of misophonia»
Связь отчётов: Siepsiak et al. 2020, depression inpatients (n = 94): the doctoral thesis R0810 reproduces the article
Расхождения в тексте: The authors report 12.76% for the interview-inclusive definition; 12/94 = 12.77% (rounding/truncation). The thesis R0810 rounds prevalence to 9-12% (Polish summary and abstract) and 9-13% (review section). The interview-positive count of 12 is consistent with sensitivity 66.67% (8/12); specificity 96.34% = 79/82 implies 3 MisoQuest false positives, matching the text (2 not meeting criteria + 1 PTSD). The sex share of 45.7% female is of all participants, with 19.1% missing. The PTSD figure '6 participants (7.4%)' implies a denominator of about 81, not 94.
Заметка ИИ: There is one eligible sample: 94 inpatients with depression. The primary estimate is L3 (interview AND MisoQuest >=61, 8/94). Other estimates are the interview including mild cases (L3, 12/94), MisoQuest >=61 alone (L2, 11/94), and a PTSD subgroup (0/6). topic_disclosed was set to NR because the text does not describe what participants were told.

### ST092-1 · Psychiatric inpatients with depression, Kraków and Warsaw hospitals, POL, n=94
Отчёты: R1188 (main); R0810

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · interview positive (Schröder 2013 criteria, semi-structured face-to-face) AND MisoQuest>=61 | **L3** | **8 / 94** | 8.5 | 3.1. Prevalence of Misophonia among Inpatients with Depress… | «Eight out of 94 subjects were diagnosed with misophonia (8.5%), meeting criteria for misophonia in both face-to-face interview and MisoQuest.» |
| E2 | all | interview · interview: Schröder 2013 criteria, including mild misophonia (regardless of MisoQuest) | **L3** | **12 / 94** | 12.8 | 3.1; 4. Discussion | «There were also 4 patients (52, 59, 59, and 60 points) who met criteria for mild misophonia [6] in face-to-face interviews ... If we included the 4 cases with mild misophonia, with very limited impact on one's life, thi…» |
| E3 | all | MisoQuest · MisoQuest>=61 | **L2** | **11 / 94** | 11.7 | 3.1 | «According to the assumed cutoff in MisoQuest (61 out of 70 points), 11 patients should be classified as having misophonia (11.7%).» |
| E4 | PTSD (self-reported psychiatrist diagnosis) | interview · interview: Schröder 2013 criteria | **L3** | **0 / 6** | 0.0 | 4. Discussion | «There were 6 participants (7.4%) who reported that they had been diagnosed by their psychiatrist with PTSD... no patients with PTSD were diagnosed with misophonia in the face-to-face interviews.» |

- E1: источник порога: study's own; правило: interview row + MisoQuest row; G4 'A and B' takes the higher level (interview L3); у авторов: «diagnosed with misophonia, meeting criteria in both face-to-face interview and …»; главная у авторов: yes; период: current; заметка: Lower bound of the authors' 8.5-12.76% range; Discussion: 'A total of 8.5% of patients met the criteria for misophonia.'
- E2: источник порога: developer paper; правило: interview row; L3 explicit criteria applied by trained interviewer; у авторов: «misophonia including 4 cases with mild misophonia»; главная у авторов: no; период: current; **расчёт: 8 (interview + MisoQuest positive) + 4 (interview-positive mild, MisoQuest <61) = 12; consistent with sensitivity 66.67% = 8/12**; заметка: Authors print 12.76%; 12/94 = 12.77%. Mild cases described as having 'very limited impact on one's life'.
- E3: источник порога: study's own; правило: MisoQuest row; L2 >=61; у авторов: «should be classified as having misophonia (assumed cutoff)»; главная у авторов: no; период: current; заметка: Cut-off proposed in this report (mean 65.72 minus SD 4.3 of misophonia group in external 2018 validation sample), so not E3; this report is the Table 1 source for >=61 -> flag. Of the 11, 2 did not meet interview criteria and 1 was explained by PTSD.
- E4: источник порога: developer paper; правило: interview row; L3; у авторов: «no patients with PTSD were diagnosed with misophonia»; главная у авторов: no; период: current; заметка: Not stated whether mild cases were included; 0 under either interview definition. 6 = 7.4% implies a PTSD-item denominator of about 81, not 94. One MisoQuest-positive patient (62 points) had symptoms explained by PTSD.

**Ключевые поля выборки:**
- **n_analysed: 94** — 2.1. Participants — «Data was missing for six participants, so 94 participants were analyzed.»
- **population: clinical** — 2.1. Participants — «A total of 100 patients with a current diagnosis of depression were enrolled in the study.»
- **sampling: convenience** — 2.1. Participants — «we recruited them with the help of their psychiatric doctors, who recommended patients who fulfilled the criteria of participation for this study»

**Остальные поля:**
- clinical_group: depression — 2.1. Participants — «The reason the participants were in a patient unit was depression»
- country: POL — 2.1. Participants — «recruited from psychiatric care wards in Kraków (Dr Jozef Babinski Clinical Hospital) and Warsaw (Institute of Psychiatry and Neurology)»
- setting: clinic: psychiatric inpatient wards of two hospitals (Kraków, Warsaw) — 2.1. Participants — «Both male and female participants were recruited from psychiatric care wards in Kraków (Dr Jozef Babinski Clinical Hospital) and Warsaw (Institute of Psychiatr…»
- data_years: NR — 2. Materials and Methods — «approved by The Ethics Committee at the Faculty of Psychology at the University of Warsaw (Psychologiczne korelaty mizofonii u osób z depresją, 21/05/2019)»
- design: cross-sectional — 1. Introduction (last paragraph) — «the main goal of this study was to assess the prevalence of misophonia among the patients with the diagnosis of depression»
- topic_disclosed: NR — 2. Materials and Methods — «Psychologiczne korelaty mizofonii u osób z depresją [Psychological correlates of misophonia in people with depression]»
- inclusion_exclusion: Inpatients with current ICD-10 diagnosis of depression (hospitalised 2 weeks-2 months), recommended by their psychiatrists; excluded cognitive impairment, psychosis/psychotic depression, OCD, drug/alcohol addiction, bipolar depressive episode — 2.1. Participants — «Exclusion criteria were as follows: (a) cognitive impairment, (b) psychosis, (c) obsessive-compulsive disorder, (d) drug and/or alcohol addiction, and (e) expe…»
- n_invited: NR — 2.1. Participants — «A total of 100 patients with a current diagnosis of depression were enrolled in the study.»
- n_responded: 100 — 2.1. Participants — «A total of 100 patients with a current diagnosis of depression were enrolled in the study.»
- response_rate: NR — 2.1. Participants — «A total of 100 patients with a current diagnosis of depression were enrolled in the study.»
- age_mean: 39.95 — 2.1. Participants — «Participants' ages ranged from 18 to 79 years old (M = 39.95, SD = 14.9).»
- age_sd: 14.9 — 2.1. Participants — «(M = 39.95, SD = 14.9)»
- age_min: 18 — 2.1. Participants — «Participants' ages ranged from 18 to 79 years old»
- age_max: 79 — 2.1. Participants — «Participants' ages ranged from 18 to 79 years old»
- age_group: adults — 2.1. Participants — «Participants' ages ranged from 18 to 79 years old»
- pct_female: 45.7 — 2.1. Participants — «There were slightly more women than men in this study (45.7%; missing data for 19.1% of participants).»
- informant: mixed — 2.2. Assessments — «Misophonia was identified using both the MisoQuest questionnaire [30] and a semi-structured interview based on Schröder et al.'s diagnostic criteria for misoph…»
- mode: mixed — 2.2. Assessments — «The participants were individually evaluated by researchers trained in the diagnosis of misophonia using the measures described below.»
- instruments: MisoQuest (original Polish version, 14 items); semi-structured interview based on Schröder et al. 2013 diagnostic criteria (Polish; Supplementary File S1) — 2.2. Assessments — «MisoQuest, a 14-item self-report questionnaire for assessing misophonia, was developed and validated on a Polish population.»
- instrument_validated_in_language: yes — 2.2. Assessments — «MisoQuest, a 14-item self-report questionnaire for assessing misophonia, was developed and validated on a Polish population.»
- pub_status: journal — Title block — «International journal of environmental research and public health; DOI: 10.3390/ijerph17155464»
- language: English — Full text — «Prevalence of Misophonia and Correlates of Its Symptoms among Inpatients with Depression»
- funding_coi: Faculty of Psychology, University of Warsaw (ministry subsidy), Polish National Science Center grant 2018/29/N/HS6/01108, Foundation for Polish Science project; authors declare no conflict of interest — Funding; Conflicts of Interest — «the Polish National Science Center grant number 2018/29/N/HS6/01108 ... The authors declare no conflict of interest.»
- notes: R0810 (Siepsiak doctoral thesis, 2023) reproduces this article in full (Article no. 2) and summarises prevalence as 9-12% / 9-13% (rounded). The MisoQuest >=61 cut-off was proposed in this report (mean minus SD of the misophonia group in the external 2018 MisoQuest validation sample) and checked against the interview in this same sample; it is the Table 1 source of MisoQuest >=61 -> flag (cf. G8). Not E3 because it comes from another sample (G5). Much age and sex data missing (19.1% missing sex). pct_female 45.7 is of all participants; among those with known sex about 56.6% (implied 43/76, t(…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is inpatients with depression, but the frame was only patients recommended by psychiatrists on wards in two hospitals — 2.1. Participants — «we recruited them with the help of their psychiatric doctors, who recommended patients who fulfilled the criteria of participation for this study»
2. способ отбора: **no** — Convenience selection: patients were recommended by their doctors, not a probability sample or consecutive census — 2.1. Participants — «psychiatric doctors, who recommended patients who fulfilled the criteria of participation»
3. размер выборки: **no** — n = 94 is below 139 for a clinical sample — 2.1. Participants — «so 94 participants were analyzed»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not — 2.1. Participants — «Participants' ages ranged from 18 to 79 years old (M = 39.95, SD = 14.9)... (45.7%; missing data for 19.1% of participants)»
5. охват (пропуски): **yes** — 6 of 100 enrolled (6%) excluded for missing data, which is 10% or less. Age/sex data missing, but not misophonia data — 2.1. Participants — «Data was missing for six participants, so 94 participants were analyzed.»
6. валидность определения случая: **yes** — Primary estimate (L3) comes from a face-to-face semi-structured interview with explicit Schröder 2013 criteria by trained researchers, combined with the Polish MisoQuest >=61 — 2.2. Assessments — «a semi-structured interview based on Schröder et al.'s diagnostic criteria for misophonia [6]. During the interview, the diagnostician asked whether the patien…»
7. единое надёжное измерение: **yes** — Same interview and questionnaire for all participants; the source validation reports MisoQuest internal consistency (alpha 0.955) — 2.2. Assessments; R0810, MisoQuest article 3.3 — «The reliability of MisoQuest was excellent in both samples (α = 0.961, α = 0.955, respectively).»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are explicit (8/94); a CI can be calculated — 3.1 — «Eight out of 94 subjects were diagnosed with misophonia (8.5%)»
9. отклик: **unclear** — Number of eligible or invited patients not reported; no response rate — 2.1. Participants — «A total of 100 patients with a current diagnosis of depression were enrolled in the study.»

Правки:
- 

Проверено: да
---

## ST093 · Wallace 2020 · VCU Scholars Compass (Virginia Commonwealth University)

Основной отчёт R1198: [текст](../../fulltext/text/R1198.txt) — «Differential Identification of Hyperacusis and Misophonia: Implications of Discrete Decreased Sound Tolerance (DST) Condition Subtypes» — [DOI](https://doi.org/10.25772/yeq1-3915)
Расхождения в тексте: 1) The text (p. 38) says 13.1% have MSS>=7. That is the sum of the rounded band percentages (11.3 + 1.7 + 0.1). The Table 1 counts give 207/1572 = 13.17%, which rounds to 13.2%. 2) The text on p. 44 says 'Overall, 61.6% of the sample is female', but Table 1 gives 1154/1572 = 73.4%. The 61.6% figure is the female share of the Low DST cluster in Table 4. 3) In Table 4, the female percentage for the Misophonia cluster is printed as 81.1%, but 175/215 = 81.4%. 4) Table 4 gender counts sum to 448 for Low DST (cluster n = 449) and 371 for High DST (cluster n = 376). These gaps are consistent with the 6 'other' gender participants, who are not shown. 5) The Procedure says the survey stayed open until about 1000 students had completed it, but N = 1572 were analysed. 6) Of the clusters that report both conditions, Attentional + Social = 373/1572 = 23.7%; the text says 23.8%.
Заметка ИИ: There are no '=== Page N ===' markers in the text, so locations use the dissertation's printed page numbers and table labels. The authors' main analysis is a latent class analysis, so the cluster estimates are E3. The recommended review estimate is MQ Severity >=7 (L2), 207/1572; I summed the bands upward from Table 1 myself. Time frame is NR because the MQ states no recall period.

### ST093-1 · VCU undergraduate participant pool, USA, n=1572
Отчёты: R1198 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **207 / 1572** | 13.2 | p. 38 text; p. 39, Table 1 | «13.1% of our sample endorsed clinically significant misophonia symptoms a score of 7 or higher. / 7, Moderate sound sensitivity 178 (11.3%) 11, Severe sound sensitivity 27 (1.7%) 15, Very severe sound sensitivity 2 (0.1…» |
| E2 | all | MQ · MSS>=4 | **L1** | **781 / 1572** | 49.7 | p. 39, Table 1 | «4, Mild sound sensitivity 574 (36.5%) 7, Moderate sound sensitivity 178 (11.3%) 11, Severe sound sensitivity 27 (1.7%) 15, Very severe sound sensitivity 2 (0.1%)» |
| E3 | all | MQ · MSS>=11 | **L2** | **29 / 1572** | 1.8 | p. 39, Table 1 | «11, Severe sound sensitivity 27 (1.7%) 15, Very severe sound sensitivity 2 (0.1%)» |
| E4 | all | MQ · MSS>=15 | **L2** | **2 / 1572** | 0.1 | p. 39, Table 1 | «15, Very severe sound sensitivity 2 (0.1%)» |
| E5 | all | MQ · MSS>=1 | **L0** | **1373 / 1572** | 87.3 | p. 39, Table 1 | «0, No sound sensitivity 199 (12.7%) 1, Minimal sound sensitivity 592 (37.7%)» |
| E6 | all | multiple · Latent class 'Misophonia' cluster (6-class LCA on MQ Total, MQ Severity, HQ Loudness and HQ subscales; indicators cut at sample SDs/means) | **E3** | **215 / 1572** | 13.7 | p. 42 text; p. 43, Table 3; Abstract | «The "Misophonia" cluster included 13.7% of (N = 215) had a high probability of experiencing mild to moderate sound sensitivities, a high probability of experiencing misophonia symptoms» |
| E7 | all | multiple · Latent class 'High DST' cluster (comorbid hyperacusis/misophonia) | **E3** | **376 / 1572** | 23.9 | p. 42 text; Table 3 | «The "High DST" cluster included 23.9% (N = 376) of participants and was characterized by ... high misophonia and hyperacusis symptoms» |
| E8 | all | multiple · Latent classes with both misophonia and hyperacusis symptoms (High DST + DST Attentional + DST Social) | **E3** | **749 / 1572** | 47.6 | p. 75, Discussion; Table 3 | «a large proportion (47.6%) of the sample reported both misophonia and hyperacusis symptoms» |
| E9 | female | multiple · Latent class 'Misophonia' cluster | **E3** | **175 / 1154** | 15.2 | p. 44, Table 4 | «Female 276 (61.6%) 301 (81.1%) 175 (81.1%) 169 (81.6%) 107 (64.5%) 126 (79.2%)» |
| E10 | male | multiple · Latent class 'Misophonia' cluster | **E3** | **40 / 412** | 9.7 | p. 44, Table 4 | «Male 172 (38.4%) 70 (18.9%) 40 (18.6%) 38 (18.4%) 59 (35.5%) 33 (20.8%)» |
| E11 | female | multiple · Latent class 'High DST' cluster | **E3** | **301 / 1154** | 26.1 | p. 44, Table 4 | «Female 276 (61.6%) 301 (81.1%) 175 (81.1%) 169 (81.6%) 107 (64.5%) 126 (79.2%)» |
| E12 | male | multiple · Latent class 'High DST' cluster | **E3** | **70 / 412** | 17.0 | p. 44, Table 4 | «Male 172 (38.4%) 70 (18.9%) 40 (18.6%) 38 (18.4%) 59 (35.5%) 33 (20.8%)» |

- E1: источник порога: developer paper; правило: MQ row; L2 MSS>=7; G1 sum of bands; у авторов: «clinically significant misophonia symptoms»; главная у авторов: no; период: NR; **расчёт: 178 + 27 + 2 from Table 1 (bands 7, 11, 15)**; заметка: The text gives 13.1% (the sum of rounded band percentages); 207/1572 = 13.17%. This is the recommended L2 estimate for the review; the authors' focus is the LCA.
- E2: источник порога: developer paper; правило: MQ row; L1 MSS>=4; G1 sum of bands; у авторов: «mild sensitivity or more (not labelled by the authors as a case definition)»; главная у авторов: no; период: NR; **расчёт: 574 + 178 + 27 + 2 from Table 1**; заметка: 49.7%
- E3: источник порога: developer paper; правило: MQ row; G2 above L2 cut-off; G1 sum of bands; у авторов: «severe sound sensitivity or more»; главная у авторов: no; период: NR; **расчёт: 27 + 2 from Table 1**; заметка: Stricter than the recommended threshold.
- E4: источник порога: developer paper; правило: MQ row; G2 above L2 cut-off; G1 top band; у авторов: «very severe sound sensitivity»; главная у авторов: no; период: NR; заметка: Top band only, so the cumulative count equals the band count.
- E5: источник порога: developer paper; правило: MQ row; G2 below L1 cut-off (minimal 1-3) -> L0; у авторов: «any sound sensitivity (minimal or more)»; главная у авторов: no; период: NR; **расчёт: 592 + 574 + 178 + 27 + 2 (= 1572 - 199) from Table 1**; заметка: Listed, not pooled.
- E6: источник порога: percentile of this sample; правило: G5 latent class -> E3; у авторов: «Misophonia (misophonia only)»; главная у авторов: yes; период: NR; заметка: The authors' headline misophonia figure (abstract and discussion). Distribution-based; not pooled.
- E7: источник порога: percentile of this sample; правило: G5 latent class -> E3; у авторов: «High DST; comorbid hyperacusis/misophonia»; главная у авторов: no; период: NR; заметка: Not misophonia-specific; listed only.
- E8: источник порога: percentile of this sample; правило: G5 latent class -> E3; у авторов: «reported both misophonia and hyperacusis symptoms»; главная у авторов: no; период: NR; **расчёт: 376 + 207 + 166 from Table 3**; заметка: 749/1572 = 47.6%.
- E9: источник порога: percentile of this sample; правило: G5 latent class -> E3; у авторов: «Misophonia»; главная у авторов: no; период: NR; **расчёт: n = sum of female counts across clusters in Table 4 (276+301+175+169+107+126 = 1154)**; заметка: Table 4 percentages are within-cluster; 175/215 = 81.4%, but 81.1% is printed.
- E10: источник порога: percentile of this sample; правило: G5 latent class -> E3; у авторов: «Misophonia»; главная у авторов: no; период: NR; **расчёт: n = sum of male counts across clusters in Table 4 (172+70+40+38+59+33 = 412)**
- E11: источник порога: percentile of this sample; правило: G5 latent class -> E3; у авторов: «High DST»; главная у авторов: no; период: NR; **расчёт: n = sum of female counts in Table 4**; заметка: High DST has 376 members, but 301 female + 70 male = 371; the remaining 5 are presumably 'other' gender.
- E12: источник порога: percentile of this sample; правило: G5 latent class -> E3; у авторов: «High DST»; главная у авторов: no; период: NR; **расчёт: n = sum of male counts in Table 4**

**Ключевые поля выборки:**
- **n_analysed: 1572** — p. 39, Table 1; p. 45, Table 5 — «MQ Sound Severity 2.84 (2.47) 0 - 15 1572»
- **population: university_students** — p. 26, Participants — «A sample comprising of 1572 university students (1154 females, 412 males, and 6 identifying as other)»
- **sampling: convenience** — p. 26, Participants; Procedure — «The survey was administered through SONA ... The survey was made available until approximately 1000 students completed it.»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — p. 26, Method: Participants; title page — «Participants were drawn from the Virginia Commonwealth University undergraduate participant pool»
- setting: university (psychology undergraduate research participant pool, online) — p. 26, Method: Participants — «using an online system that allows students to participate in research for extra credit in psychology courses»
- data_years: 2018-2019 — pp. 26-27, Procedure — «Data collection occurred between January 2018 and December 2019.»
- design: cross-sectional — p. 26, Design — «This is a cross-sectional survey study in which participants provided responses to a variety of questions through a secure online survey.»
- topic_disclosed: NR — pp. 26-27, Procedure — «The survey was administered through SONA with a link to take the survey at an external, secure electronic data storage system, RedCAP.»
- inclusion_exclusion: VCU undergraduates in psychology courses who took part for extra credit; no explicit exclusion criteria reported (control items to detect random responding were included, but no exclusions are reported) — p. 26 Participants; p. 27 Measures — «A demographics questionnaire and a set of control items buried within the survey to detect random responding were also included.»
- n_invited: NR — NA
- n_responded: 1572 — p. 26, Participants — «A sample comprising of 1572 university students»
- response_rate: NR — NA
- age_mean: 19.49 — p. 26, Participants; Table 1 — «aged between 18 and 66 years, with a mean age of 19.49 ± 3.50 years»
- age_sd: 3.50 — p. 26, Participants — «with a mean age of 19.49 ± 3.50 years»
- age_min: 18 — p. 26, Participants — «aged between 18 and 66 years»
- age_max: 66 — p. 26, Participants — «aged between 18 and 66 years»
- age_group: adults — p. 26, Participants — «aged between 18 and 66 years»
- pct_female: 73.4 — p. 39, Table 1 — «Female 1154 (73.4%)»
- informant: self — Abstract — «Undergraduate students (N = 1572) completed self-report measures assessing DST symptoms»
- mode: online — p. 26, Design — «responses to a variety of questions through a secure online survey»
- instruments: Misophonia Questionnaire (MQ: Symptom, Emotions and Behaviors, and Severity scales), English; Decreased Sound Tolerance Differential Diagnostic Scale (Cash 2015; discomfort ratings for sounds, including misophonia sounds), English; ad hoc DST/misophonia screening items (used only for routing; no pr… — pp. 28-29, Measures — «The Misophonia Questionnaire (MQ) is a three-part, 20-item, self-report questionnaire that assesses for the presence of misophonia ... (Wu et al., 2014).»
- instrument_validated_in_language: yes — p. 28, Measures — «Convergent and discriminant validity were demonstrated in a large college student sample (Wu et al., 2014).»
- pub_status: thesis — Title page — «A dissertation submitted in partial fulfillment of the requirements for the degree of Doctor of Philosophy at Virginia Commonwealth University»
- language: English — Whole report — «Differential Identification of Hyperacusis and Misophonia: Implications of Discrete Decreased Sound Tolerance (DST) Condition Subtypes»
- funding_coi: NR — NA
- notes: Doctoral dissertation (Wallace, VCU 2020; director S. Vrana). This sample may overlap with other studies from the VCU participant pool or the Vrana lab (e.g., Cash 2015 and Cusack et al. 2018 used VCU samples, though from different years); check later VCU reports covering 2018-2019. MQ Severity responses take only the values 0, 1, 4, 7, 11 and 15 (the category anchors). The questionnaire order changed in October 2019 (n=1160 before, n=412 after); the authors report no differences. The authors' main analysis is a latent class analysis (E3). Only 1350 participants answered the MQ Emotions & Beh…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is the psychology-course participant pool, which covers only part of VCU's undergraduates. — p. 26, Participants — «online system that allows students to participate in research for extra credit in psychology courses»
2. способ отбора: **no** — Volunteers opted in through SONA for course credit; no probability sampling. — pp. 26-27, Procedure — «The survey was made available until approximately 1000 students completed it.»
3. размер выборки: **yes** — n = 1572 >= 385. — p. 39, Table 1 — «Total N = 1572»
4. описание выборки и условий: **yes** — Age, sex, setting, country (VCU, Richmond, Virginia) and dates are all reported. — pp. 26-27; Table 1 — «Data collection occurred between January 2018 and December 2019.»
5. охват (пропуски): **yes** — MQ Severity data are available for all 1572 analysed respondents. — p. 45, Table 5 — «MQ Sound Severity 2.84 (2.47) 0 - 15 1572»
6. валидность определения случая: **yes** — The primary L2 definition is MQ Severity Scale >=7, and the English MQ has a published validation (Wu et al. 2014). — p. 38, Total Sample Descriptives — «According to the criteria proposed by authors who developed the MQ (Wu et al., 2014), 13.1% of our sample endorsed clinically significant misophonia symptoms a…»
7. единое надёжное измерение: **unclear** — Everyone completed the same online MQ, but no internal consistency or reliability is reported for the MQ, either in this sample or quoted from the source (alphas are given only for other measures). — pp. 28, 31-34, Measures — «Cronbach's alpha calculated for this sample was 0.923, suggesting excellent internal consistency.»
8. статистика (числитель и знаменатель): **yes** — Band counts and the denominator (1572) are given, so a CI can be calculated. — p. 39, Table 1 — «7, Moderate sound sensitivity 178 (11.3%) 11, Severe sound sensitivity 27 (1.7%) 15, Very severe sound sensitivity 2 (0.1%)»
9. отклик: **no** — Open participant-pool survey with no denominator of invited students and no handling of non-response. — pp. 26-27, Procedure — «The survey was made available until approximately 1000 students completed it.»

Правки:
- 

Проверено: да
---

## ST094 · Janik McErlean 2018 · PeerJ

Основной отчёт R1298: [текст](../../fulltext/text/R1298.txt) — «Increased misophonia in self-reported Autonomous Sensory Meridian Response.» — [DOI](https://doi.org/10.7717/peerj.5351)
Не выписано ИИ: No group in this study was recruited for misophonia. The ASMR-positive students and acquaintances ('ASMR Non-Social Media', about 47% of that recruitment) were left out of the primary analysis. Their data are only in Supplemental Information 2, which was not available, so they are not a separate sample; one reported percentage (70.8% among females) is listed as a subgroup estimate of the control sample. The ASMR Facebook sample is extracted but flagged for a possible E1 decision, since ASMR is described as sound-related.
Расхождения в тексте: The paper gives only percentages, so all counts are derived. Controls, female, Symptom Scale >=14: the reported 26% matches no integer out of 52 (13/52 = 25.0%, 14/52 = 26.9%); the rounding rule gives 14. As a result, the male controls' Symptom Scale count (1 or 2) is not derived. All other percentages map exactly to integers: 15/68, 4/68, 2/52, 23/64, 8/64, 14/40, 5/40. The paper labels the Symptom Scale 'MSS' and calls the Symptom Scale >=14 'clinically significant'; by Table 1 that threshold is L1. The Severity Scale >=7 is L2.
Заметка ИИ: Two separately recruited samples: the ASMR Facebook group and students/acquaintances (ASMR-negative controls). The controls are a selected subset of their recruitment, because ASMR-positive people (about 47%) were removed. The authors nonetheless describe the 22% as a general-population prevalence. Funding and country are not in the supplied text.

### ST094-1 · Students and acquaintances, ASMR-negative controls, online (country NR), n=68
Отчёты: R1298 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all (ASMR-negative controls) | MQ · MQ Misophonia Severity Scale >=7 | **L2** | **4 / 68** | 5.9 | Results | «12.5% of ASMR-responders compared to 6% of the control sample reported 7 or above on the Misophonia Severity Scale which is treated as clinically significant misophonia level» |
| E2 | all (ASMR-negative controls) | MQ · MQ Symptom Scale >=14 | **L1** | **15 / 68** | 22.1 | Results; Discussion | «36% of ASMR-responders compared to 22% non-responders scored 14 and above on the Misophonia Symptom Scale, which is treated as clinically significant misophonia symptoms.» |
| E3 | female (ASMR-negative controls) | MQ · MQ Misophonia Severity Scale >=7 | **L2** | **2 / 52** | 3.8 | Analysis based on female participants only | «only 3.8% of the control sample scored 7 or above on this scale» |
| E4 | female (ASMR-negative controls) | MQ · MQ Symptom Scale >=14 | **L1** | **14 / 52** | 26.9 | Analysis based on female participants only | «Specifically, 35% of ASMR-responders compared to 26% non-responders scored 14 and above on this scale.» |
| E5 | male (ASMR-negative controls) | MQ · MQ Misophonia Severity Scale >=7 | **L2** | **2 / 16** | 12.5 | Results; Analysis based on female participants only | «6% of the control sample reported 7 or above ... only 3.8% of the control sample scored 7 or above» |
| E6 | female, ASMR-positive students/acquaintances (ASMR Non-Social Media) | MQ · MQ Symptom Scale >=14 | **L1** | **NR / NR** |  | Discussion (Supplemental Information 2 not available) | «They do, however, have a much higher prevalence rate (70.8%) of clinically relevant symptoms based on MSS scores compared to ASMR Social-Media (35%) and controls (26%)» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2, recommended); у авторов: «clinically significant misophonia level»; главная у авторов: no; период: NR; **расчёт: 6% x 68 = 4.08 -> 4 (4/68 = 5.9%)**; заметка: Applies to the ASMR-negative subset only.
- E2: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 (L1); у авторов: «clinically significant misophonia symptoms; presence of misophonia»; главная у авторов: yes; период: NR; **расчёт: 22% x 68 = 14.96 -> 15 (15/68 = 22.1%)**; заметка: The Discussion calls this the 'prevalence rate of misophonia in the general population reported in this study'. The paper abbreviates the Symptom Scale as 'MSS'.
- E3: источник порога: developer paper; правило: MQ row; MSS >=7 (L2); у авторов: «clinically significant misophonia level»; главная у авторов: no; период: NR; **расчёт: 3.8% x 52 = 1.98 -> 2 (2/52 = 3.85%)**
- E4: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 (L1); у авторов: «clinically relevant range»; главная у авторов: no; период: NR; **расчёт: 26% x 52 = 13.52 -> 14**; заметка: 26% does not match any integer out of 52 (13/52 = 25.0%, 14/52 = 26.9%), so the count is uncertain.
- E5: источник порога: developer paper; правило: MQ row; MSS >=7 (L2); у авторов: «clinically significant misophonia level»; главная у авторов: no; период: NR; **расчёт: whole-group 4 (6% x 68) minus female 2 (3.8% x 52) = 2; n = 68 - 52 = 16**; заметка: The authors do not report this; it is derived by subtraction. The male Symptom Scale count cannot be derived reliably (15 - 13 or 14 = 1 or 2).
- E6: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 (L1); у авторов: «clinically relevant symptoms»; главная у авторов: no; период: NR; заметка: Reported percentage is 70.8%. This is the ASMR-positive part of the same student/acquaintance recruitment; n is given only in the unavailable supplement.

**Ключевые поля выборки:**
- **n_analysed: 68** — Participants — «sixty eight controls (52 female, 16 male»
- **population: gp_other** — Participants — «sixty eight controls (52 female, 16 male; age M = 26.75, SD = 11.20, range: 18–66)»
- **sampling: convenience** — Participants — «Control participants were recruited among acquaintances and student population»

**Остальные поля:**
- clinical_group: NA — NA
- country: NR — Materials & Methods — «This study was conducted online and was approved by the ethical committee of Goldsmiths University of London.»
- setting: university (students) and community (acquaintances); online survey — Participants — «Control participants were recruited among acquaintances and student population and were either given credit points, cash vouchers, or were entered into a prize…»
- data_years: NR — Materials & Methods — «This study was conducted online»
- design: cross-sectional — Abstract — «The Misophonia Questionnaire (MQ) was administered to individuals reporting to experience ASMR and to age and gender matched controls.»
- topic_disclosed: NR — Materials & Methods — «Participants were first presented with information about the study.»
- inclusion_exclusion: Students/acquaintances; included only if they answered no to experiencing ASMR (ASMR-positive ones, about 47%, excluded from the primary analysis) — Participants; Discussion — «Participants were included in the control group based on a negative answer to a question whether they experience ASMR»
- n_invited: NR — NA
- n_responded: NR — Discussion — «A large proportion of participants recruited outside of the ASMR Facebook site (47%) also indicated to experience ASMR»
- response_rate: NR — NA
- age_mean: 26.75 — Participants — «age M = 26.75, SD = 11.20, range: 18–66»
- age_sd: 11.20 — Participants — «age M = 26.75, SD = 11.20, range: 18–66»
- age_min: 18 — Participants — «range: 18–66»
- age_max: 66 — Participants — «range: 18–66»
- age_group: adults — Participants — «range: 18–66»
- pct_female: 76.5 — Participants — «sixty eight controls (52 female, 16 male»
- informant: self — Measures — «Participants are asked to rate the severity of their sound sensitivity»
- mode: online — Materials & Methods — «This study was conducted online»
- instruments: Misophonia Questionnaire (Wu et al. 2014), English: Symptom Scale, Emotions and Behaviors Scale, Misophonia Severity Scale — Measures — «The Misphonia Questionnaire (Wu et al., 2014) consists of three parts: the Misophonia Symptom Scale, the Misophonia Emotions and Behaviors Scale and the Misoph…»
- instrument_validated_in_language: yes — Measures — «The Misphonia Questionnaire (Wu et al., 2014)»
- pub_status: journal — Header — «Year: 2018; venue: PeerJ; DOI: 10.7717/peerj.5351»
- language: English — Full text — «Increased misophonia in self-reported Autonomous Sensory Meridian Response»
- funding_coi: NR — NA
- notes: The recruited sample was students plus acquaintances. About 47% said they experienced ASMR; this 'ASMR Non-Social Media' group was left out of the primary analysis and is reported only in Supplemental Information 2, which was not available. So the 68 analysed are the ASMR-negative subset, not the whole recruited sample, and estimates are biased by that selection. Only percentages are reported; counts are derived. pct_female computed as 52/68. Country is not stated (ethics approval from Goldsmiths, London). The authors call 22% the 'prevalence rate of misophonia in the general population'. Fun…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The authors treat the controls as the general population, but the frame was acquaintances and students, filtered to ASMR-negative people. — Participants — «Control participants were recruited among acquaintances and student population»
2. способ отбора: **no** — Convenience recruitment with incentives. — Participants — «were either given credit points, cash vouchers, or were entered into a prize draw»
3. размер выборки: **no** — n=68, below 385. — Participants — «sixty eight controls»
4. описание выборки и условий: **no** — Age, sex and setting are reported; country and dates of data collection are not. — Participants — «sixty eight controls (52 female, 16 male; age M = 26.75, SD = 11.20, range: 18–66)»
5. охват (пропуски): **unclear** — Missing data not reported; the chi-square tests use N=132, which suggests none were missing. — Results — «[χ2(1,N=132) = 3.09, p = .078)»
6. валидность определения случая: **yes** — Primary L2 definition: MQ Misophonia Severity Scale >=7 in the original English version. — Measures — «A score greater than or equal to 7 indicates ‘moderate sound sensitivity’ which interferes with daily life and thus is treated as a cut-off for clinically sign…»
7. единое надёжное измерение: **yes** — Same online MQ for all participants; Cronbach's alpha reported for the study sample. — Results — «MQ Total, Cronbach’s alpha = .872»
8. статистика (числитель и знаменатель): **yes** — Percentages with known n, so counts and CIs can be computed for the whole group. The female 26% does not match an integer of 52 exactly. — Results — «22% non-responders scored 14 and above»
9. отклик: **no** — No denominator of invited people and no handling of non-response. — Participants — «Control participants were recruited among acquaintances and student population»

Правки:
- 

Проверено: да
### ST094-2 · ASMR Facebook group members (ASMR Social-Media), online, n=64
Отчёты: R1298 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MQ Misophonia Severity Scale >=7 | **L2** | **8 / 64** | 12.5 | Results | «12.5% of ASMR-responders compared to 6% of the control sample reported 7 or above on the Misophonia Severity Scale» |
| E2 | all | MQ · MQ Symptom Scale >=14 | **L1** | **23 / 64** | 35.9 | Results | «36% of ASMR-responders compared to 22% non-responders scored 14 and above on the Misophonia Symptom Scale» |
| E3 | female | MQ · MQ Misophonia Severity Scale >=7 | **L2** | **5 / 40** | 12.5 | Analysis based on female participants only | «the percentage of participants who reported 7 or above on the Misophonia Severity Scale was exactly the same as for the entire ASMR group (12.5%)» |
| E4 | female | MQ · MQ Symptom Scale >=14 | **L1** | **14 / 40** | 35.0 | Analysis based on female participants only | «Specifically, 35% of ASMR-responders compared to 26% non-responders scored 14 and above on this scale.» |
| E5 | male | MQ · MQ Misophonia Severity Scale >=7 | **L2** | **3 / 24** | 12.5 | Results; Analysis based on female participants only | «12.5% of ASMR-responders ... exactly the same as for the entire ASMR group (12.5%)» |
| E6 | male | MQ · MQ Symptom Scale >=14 | **L1** | **9 / 24** | 37.5 | Results; Analysis based on female participants only | «36% of ASMR-responders ... 35% of ASMR-responders compared to 26% non-responders» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2, recommended); у авторов: «clinically significant misophonia level»; главная у авторов: no; период: NR; **расчёт: 12.5% x 64 = 8**
- E2: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 (L1); у авторов: «clinically significant misophonia symptoms»; главная у авторов: no; период: NR; **расчёт: 36% x 64 = 23.04 -> 23**
- E3: источник порога: developer paper; правило: MQ row; MSS >=7 (L2); у авторов: «clinically significant misophonia level»; главная у авторов: no; период: NR; **расчёт: 12.5% x 40 = 5**
- E4: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 (L1); у авторов: «clinically relevant range»; главная у авторов: no; период: NR; **расчёт: 35% x 40 = 14**
- E5: источник порога: developer paper; правило: MQ row; MSS >=7 (L2); у авторов: «clinically significant misophonia level»; главная у авторов: no; период: NR; **расчёт: 8 (12.5% x 64) - 5 (12.5% x 40) = 3; n = 64 - 40 = 24**; заметка: Derived by subtraction; the authors do not report it.
- E6: источник порога: developer paper; правило: MQ row; Symptom Scale >=14 (L1); у авторов: «clinically significant misophonia symptoms»; главная у авторов: no; период: NR; **расчёт: 23 (36% x 64) - 14 (35% x 40) = 9; n = 24**; заметка: Derived by subtraction; the authors do not report it.

**Ключевые поля выборки:**
- **n_analysed: 64** — Participants — «sixty four ASMR—responders (40 female, 24 male»
- **population: other_nonclinical** — Participants — «All ASMR-responders confirmed they experience ASMR based on this description.»
- **sampling: convenience** — Participants — «The ASMR sample was recruited via a Facebook site dedicated to ASMR»

**Остальные поля:**
- clinical_group: NA — NA
- country: NR — Participants — «The ASMR sample was recruited via a Facebook site dedicated to ASMR»
- setting: online community (Facebook ASMR group) — Participants — «The ASMR sample was recruited via a Facebook site dedicated to ASMR (https://www.facebook.com/groups/ASMRGroup/).»
- data_years: NR — NA
- design: cross-sectional — Abstract — «The Misophonia Questionnaire (MQ) was administered to individuals reporting to experience ASMR and to age and gender matched controls.»
- topic_disclosed: NR — Materials & Methods — «Participants were first presented with information about the study.»
- inclusion_exclusion: Recruited from an ASMR Facebook group; included if they confirmed experiencing ASMR from the description given — Participants — «Participants recruited from the ASMR Facebook site who indicated they did not experience ASMR were excluded from the analysis.»
- n_invited: NR — NA
- n_responded: NR — NA
- response_rate: NR — NA
- age_mean: 28.81 — Participants — «age M = 28.81, SD = 6.05, range: 18–38»
- age_sd: 6.05 — Participants — «age M = 28.81, SD = 6.05, range: 18–38»
- age_min: 18 — Participants — «range: 18–38»
- age_max: 38 — Participants — «range: 18–38»
- age_group: adults — Participants — «range: 18–38»
- pct_female: 62.5 — Participants — «sixty four ASMR—responders (40 female, 24 male»
- informant: self — Measures — «Participants are asked to rate the severity of their sound sensitivity»
- mode: online — Materials & Methods — «This study was conducted online»
- instruments: Misophonia Questionnaire (Wu et al. 2014), English: Symptom Scale, Emotions and Behaviors Scale, Misophonia Severity Scale — Measures — «The Misphonia Questionnaire (Wu et al., 2014) consists of three parts»
- instrument_validated_in_language: yes — Measures — «The Misphonia Questionnaire (Wu et al., 2014)»
- pub_status: journal — Header — «Year: 2018; venue: PeerJ; DOI: 10.7717/peerj.5351»
- language: English — Full text — «Increased misophonia in self-reported Autonomous Sensory Meridian Response»
- funding_coi: NR — NA
- notes: Eligibility needs a reviewer decision. These people were recruited because of ASMR (a sound-triggered experience), not misophonia. The authors frame ASMR and misophonia as 'two ends of the same sound sensitivity spectrum', so this group may count as E1 (sound sensitivity or special interest). If kept, it is a special-interest group, not the general population. Counts are derived from percentages. pct_female computed as 40/64.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is people who experience ASMR; the frame was a single Facebook group. — Participants — «recruited via a Facebook site dedicated to ASMR»
2. способ отбора: **no** — Volunteer opt-in from social media. — Participants — «recruited via a Facebook site dedicated to ASMR»
3. размер выборки: **no** — n=64, below 385. — Participants — «sixty four ASMR—responders»
4. описание выборки и условий: **no** — Country and dates of data collection not reported. — Participants — «sixty four ASMR—responders (40 female, 24 male; age M = 28.81, SD = 6.05, range: 18–38)»
5. охват (пропуски): **unclear** — Missing data not reported. — Results — «[χ2(1,N=132) = 3.09, p = .078)»
6. валидность определения случая: **yes** — MQ Severity Scale >=7 in the original English version. — Measures — «treated as a cut-off for clinically significant symptoms»
7. единое надёжное измерение: **yes** — Same online MQ for everyone; alpha reported. — Results — «MQ Total, Cronbach’s alpha = .872»
8. статистика (числитель и знаменатель): **yes** — Percentages with known n map exactly to integer counts. — Results — «12.5% of ASMR-responders»
9. отклик: **no** — Open social-media recruitment with no denominator. — Participants — «recruited via a Facebook site dedicated to ASMR»

Правки:
- 

Проверено: да
---

## ST095 · Cash 2015 · VCU Scholars Compass (Virginia Commonwealth University)

Основной отчёт R1402: [текст](../../fulltext/text/R1402.txt) — «DECREASED SOUND TOLERANCE (DST): PREVALENCE, CLINICAL CORRELATES, AND DEVELOPMENT OF A DST ASSESSMENT INSTRUMENT» — [DOI](https://doi.org/10.25772/je67-v432)
Расхождения в тексте: MQ threshold: Method and Table 4a/4b give '7 or higher', but p. 61 and the Table 16 header say 'greater than 7'/'>7'. The count of 129 (Table 9 and Table 16, TP+FN) fits 129/826 = 15.6%, the combined percentage, so the full-sample denominators (451, 375) appear to have been used, not the 817 who completed the Severity item. Table 16, however, uses N=817. Misophonia screening item: Table 4b percentages (student 18.4% yes, 44.8% sometimes; community 13.5% yes) differ slightly from Table 5b counts (83/448 = 18.5%, 200/448 = 44.6%; 49/368 = 13.3%) because Table 5b's denominators are 448 and 368; Table 5b counts were used. Text p. 53 says males were more likely to screen positive, but there are no sex-specific prevalence counts. Data cleaning: 41 is reported as 8.30% of submitted responses, which does not exactly fit 653-161 = 492 (8.33%). Age minimum 17 (Table 3) conflicts with the 18+ incl…
Заметка ИИ: The sex comparison is reported only as means, so there are no subgroup estimates. A-MISO-S estimates are coded NR under G10: the scale was given only to screen-positives, and the screen-positive counts appear larger than the 314 and 228 completers. Per-sample MQ counts are derived from percentages.

### ST095-1 · VCU undergraduate participant pool, USA, n=451
Отчёты: R1402 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **73 / 451** | 16.2 | Table 4b; Discussion p. 87 | «Misophonia Questionnaire Severity Score= 7 or higher ... 16.2%» |
| E2 | all | A-MISO-S · A-MISO-S>=5 (among screen-positives completing the scale) | **NR** | **202 / 314** | 64.3 | Table 4b; Table 6b (n=314) | «#Amsterdam Misophonia Scale Total Score Mild (5 to 9) Moderate (10 to 14) Severe (15 to 19) Extreme (20 to 24) 42.4% 19.7% 2.2% 0.0%» |
| E3 | all | A-MISO-S · A-MISO-S>=10 (among screen-positives completing the scale) | **NR** | **69 / 314** | 22.0 | Table 4b; Table 6b | «Moderate (10 to 14) Severe (15 to 19) Extreme (20 to 24) 19.7% 2.2% 0.0%» |
| E4 | all | A-MISO-S · A-MISO-S>=15 (among screen-positives completing the scale) | **NR** | **7 / 314** | 2.2 | Table 4b | «Severe (15 to 19) Extreme (20 to 24) 2.2% 0.0%» |
| E5 | all | adhoc · screening item 'Compared to other people, are you sensitive to certain sounds made by other people?' = Yes | **L0** | **83 / 448** | 18.5 | Table 5b | «Positive misophonia screen ... Total 28 (6.25%) 55 (12.28%) 83 (18.53%)» |
| E6 | all | adhoc · screening item = Yes or Sometimes | **L0** | **283 / 448** | 63.2 | Table 5b; Table 4b | «'Sometimes' misophonia screen ... Total 35 (7.81%) 165 (36.83%) 200 (44.64%)» |

- E1: источник порога: developer paper; правило: MQ row; MSS>=7 L2; у авторов: «clinically significant misophonia symptoms»; главная у авторов: yes; период: NR; **расчёт: 16.2% x 451 = 73.06 -> 73 (with community 56 gives 129 = Table 9 N)**; заметка: Denominator unclear: 444 completed the Severity item (Table 6b); 72/444 would also round to 16.2%. 451 used because the sum across samples matches 129/826 = 15.6%. Text p. 61 says 'greater than 7'.
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G10 two-stage with incomplete stage 2 -> G6 NR; у авторов: «mild or more»; главная у авторов: no; период: current; **расчёт: (42.4% + 19.7% + 2.2% + 0.0%) = 64.3% x 314 = 201.9 -> 202**; заметка: Only screen-positives were given the scale. The screen-positive count (misophonia yes/sometimes 283 + tinnitus positives + DST positives) appears to exceed 314, so not all screen-positives completed it. Over all 451 screened this would be 202/451 (44.8%) if there were no other cases.
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G10 -> G6 NR; у авторов: «moderate or more»; главная у авторов: no; период: current; **расчёт: (19.7% + 2.2% + 0.0%) = 21.9% x 314 = 68.8 -> 69**; заметка: Two-stage design with incomplete stage 2; 69/451 = 15.3% over all screened if all cases were captured.
- E4: источник порога: developer paper; правило: A-MISO-S row; G1/G2; G10 -> G6 NR; у авторов: «severe or more»; главная у авторов: no; период: current; **расчёт: (2.2% + 0.0%) x 314 = 6.9 -> 7**; заметка: Two-stage design with incomplete stage 2.
- E5: источник порога: study's own; правило: adhoc row; 'sensitive to' sound item -> L0; у авторов: «definite affirmative / positive misophonia screen»; главная у авторов: no; период: current; заметка: Table 4b gives 18.4% (consistent with 83/451); Table 5b denominator is 448.
- E6: источник порога: study's own; правило: adhoc row; 'sensitive to' sound item -> L0; у авторов: «at least occasional misophonia symptoms»; главная у авторов: no; период: current; **расчёт: 83 (Yes) + 200 (Sometimes) from Table 5b**; заметка: Table 4b gives 44.8% sometimes + 18.4% yes = 63.2%.

**⚠ Проверка скриптом (обратите внимание):**
- E2, E3, E4, E5, E6: n оценки не равно n_analysed выборки (451): проверьте знаменатель

**Ключевые поля выборки:**
- **n_analysed: 451** — Table 2 — «Total number of participants included in final analyses 451»
- **population: university_students** — Method, Participants, p. 34 — «Virginia Commonwealth University undergraduate participant pool»
- **sampling: convenience** — Method, Participants, p. 34 — «an online system that allows students to participate in research for extra credit in psychology courses»

**Остальные поля:**
- clinical_group: NA — Method, Participants, p. 35 — «The selection of two different, non-clinical samples was appropriate»
- country: USA — Method, Participants, p. 34 — «The first sample was recruited through the Virginia Commonwealth University undergraduate participant pool»
- setting: university (VCU undergraduate psychology participant pool; online survey via REDCap) — Method, Participants and Procedure, pp. 34-35 — «recruited through the Virginia Commonwealth University undergraduate participant pool using an online system that allows students to participate in research fo…»
- data_years: 2014 — Method, Procedure, p. 35 — «The student sample was collected continuously between July and December 2014.»
- design: cross-sectional — Method, Design, p. 35 — «This was a cross-sectional survey study in which participants provided responses to a variety of questions through a secure online survey.»
- topic_disclosed: NR — Method, Procedure, p. 36 — «At the beginning of the survey, all participants answered a series of screening questions about tinnitus, sound intolerance, and hearing problems.»
- inclusion_exclusion: Age 18+ and able to consent; no other exclusion criteria; excluded if 3+ errors on embedded control questions or incomplete/not submitted survey — Method, Participants, pp. 34-35; Effort measure, p. 45 — «Participants were required to be 18 years of age and older and capable of providing informed consent. There were no other exclusion criteria»
- n_invited: NR — Table 2 — «Total number of participants who initiated survey 653»
- n_responded: 492 — Table 2 — «Total number of participants who initiated survey 653 ... Number of incomplete/not submitted survey responses in REDCap 161»
- response_rate: NR — Table 2 — «Total number of participants who initiated survey 653»
- age_mean: 19.58 — Table 3 — «Age, Mean (SD) (Range) 19.58 (3.60) (17-67)»
- age_sd: 3.60 — Table 3 — «Age, Mean (SD) (Range) 19.58 (3.60) (17-67)»
- age_min: 17 — Table 3 — «19.58 (3.60) (17-67)»
- age_max: 67 — Table 3 — «19.58 (3.60) (17-67)»
- age_group: adults — Method p. 34; Table 3 — «Participants were required to be 18 years of age and older»
- pct_female: 71.2 — Table 3 — «Gender* Female Male No response 71.2% 28.4% .4%»
- informant: self — Method, Measures, p. 36 — «Measures were selected... either valid and reliable self-report questionnaires or experimental questions created by the research team»
- mode: online — Method, Design, p. 35 — «participants provided responses to a variety of questions through a secure online survey»
- instruments: Misophonia Questionnaire (MQ; English, Wu et al. 2014) incl. Severity Scale; Amsterdam Misophonia Scale (A-MISO-S; English, self-completed online, only for screen-positives); ad hoc misophonia screening item (English); DST Scale / Human Sounds Subscale (study-developed, English) — Method, Measures, pp. 36-38; Appendix A — «Only participants who responded affirmatively to questions about tinnitus, DST in general, or misophonia specifically were asked to complete the A-MISO-S»
- instrument_validated_in_language: yes — Method, Measures, p. 38 — «Convergent and discriminant validity were demonstrated in a large college student sample (Wu et al., 2014).»
- pub_status: thesis — Title page — «A dissertation submitted in partial fulfillment of the requirements for the degree of Doctor of Philosophy at Virginia Commonwealth University»
- language: English — Full text — «DECREASED SOUND TOLERANCE (DST): PREVALENCE, CLINICAL CORRELATES, AND DEVELOPMENT OF A DST ASSESSMENT INSTRUMENT»
- funding_coi: NR — Acknowledgement, p. ii — «I am grateful to many people for their support and guidance throughout this challenging but ultimately rewarding process.»
- notes: Doctoral dissertation. Two separately recruited samples (students, MTurk); the authors pool them as a 'combined sample' (n=826; MQ Severity>=7 15.6%, 129 cases per Table 9). Reported age minimum 17 (Table 3) contradicts the 18+ inclusion criterion. A-MISO-S (a clinician scale) was self-completed online only by screen-positives (n=314). Some measures were given only to a subset (n=103/94). Per-sample MQ case counts are reconstructed (73/451); they sum with the community sample's 56 to the 129 of Table 9.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is the psychology-course participant pool of one university, while the authors claim the general adult/undergraduate population — Method, p. 34; Discussion p. 87 — «participate in research for extra credit in psychology courses»
2. способ отбора: **no** — Volunteer opt-in from participant pool, no probability sampling — Method, Procedure, p. 35 — «The survey was made available until approximately 400 students and 400 community adults completed it.»
3. размер выборки: **yes** — n=451 >= 385 — Table 2 — «Total number of participants included in final analyses 451»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates reported — Table 3; Procedure p. 35 — «The student sample was collected continuously between July and December 2014.»
5. охват (пропуски): **yes** — MQ Severity available for 444 of 451 (1.6% missing) — Table 6b — «Severity scale 444 2.99 (2.45)»
6. валидность определения случая: **yes** — Primary estimate MQ Severity Scale >=7, English version validated (Wu et al. 2014) — Method, Measures, p. 38 — «individuals that reported a 7 or higher on the MQ Misophonia Severity Scale were considered to have clinically significant misophonia symptoms (Wu et al., 2014)»
7. единое надёжное измерение: **yes** — Same online MQ and threshold for all; internal consistency reported in the source (Wu et al. 2014) — Review of literature, p. 25; Procedure p. 36 — «In its initial validation within a large college student sample, adequate internal consistency, and convergent and discriminant validity were demonstrated»
8. статистика (числитель и знаменатель): **yes** — Percentage per sample with margin of error; counts reconstructable (73/451; sums to combined 129) — Discussion, p. 87; Table 9 — «students' (16.2%) and community members' (14.9%) ... (95% margin of error is +/- 3.41%)»
9. отклик: **no** — Open participant-pool survey with no invited denominator; 161 of 653 initiators incomplete; not handled — Table 2 — «Number of incomplete/not submitted survey responses in REDCap 161»

Правки:
- 

Проверено: да
### ST095-2 · Amazon MTurk community adults, USA, n=375
Отчёты: R1402 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **56 / 375** | 14.9 | Table 4b; Discussion p. 87 | «Misophonia Questionnaire Severity Score= 7 or higher ... 14.9%» |
| E2 | all | A-MISO-S · A-MISO-S>=5 (among screen-positives completing the scale) | **NR** | **154 / 228** | 67.5 | Table 4b; Table 6b (n=228) | «#Amsterdam Misophonia Scale Total Score ... 43.9% 18.9% 4.8% 0.0%» |
| E3 | all | A-MISO-S · A-MISO-S>=10 (among screen-positives completing the scale) | **NR** | **54 / 228** | 23.7 | Table 4b | «Moderate (10 to 14) Severe (15 to 19) Extreme (20 to 24) ... 18.9% 4.8% 0.0%» |
| E4 | all | A-MISO-S · A-MISO-S>=15 (among screen-positives completing the scale) | **NR** | **11 / 228** | 4.8 | Table 4b | «Severe (15 to 19) ... 4.8%» |
| E5 | all | adhoc · self-reported earlier diagnosis of misophonia (yes/no item) | **L1** | **3 / 375** | 0.8 | Table 4a; Table 4b | «Percentage of participants reporting having received sound-related diagnoses (community sample only) Misophonia .7%» |
| E6 | all | adhoc · screening item 'sensitive to certain sounds made by other people' = Yes | **L0** | **49 / 368** | 13.3 | Table 5b | «Total 18 (4.89%) 31 (8.42%) 49 (13.32%)» |
| E7 | all | adhoc · screening item = Yes or Sometimes | **L0** | **213 / 368** | 57.9 | Table 5b | «Total 35 (9.51%) 129 (35.05%) 164 (44.57%)» |

- E1: источник порога: developer paper; правило: MQ row; MSS>=7 L2; у авторов: «clinically significant misophonia symptoms»; главная у авторов: yes; период: NR; **расчёт: 14.9% x 375 = 55.9 -> 56 (73 + 56 = 129 = Table 9 N)**; заметка: Denominator unclear: 373 completed the Severity item; 56/373 = 15.0%, so 375 fits the 14.9% better.
- E2: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G10 -> G6 NR; у авторов: «mild or more»; главная у авторов: no; период: current; **расчёт: (43.9% + 18.9% + 4.8% + 0.0%) = 67.6% x 228 = 154.1 -> 154**; заметка: Only screen-positives were given the scale; completeness of stage 2 cannot be determined; 154/375 = 41.1% over all screened if there were no other cases.
- E3: источник порога: developer paper; правило: A-MISO-S row; G1 sum of bands; G10 -> G6 NR; у авторов: «moderate or more»; главная у авторов: no; период: current; **расчёт: (18.9% + 4.8% + 0.0%) = 23.7% x 228 = 54.0 -> 54**; заметка: Two-stage design; 54/375 = 14.4% over all screened if all cases were captured.
- E4: источник порога: developer paper; правило: A-MISO-S row; G1/G2; G10 -> G6 NR; у авторов: «severe or more»; главная у авторов: no; период: current; **расчёт: (4.8% + 0.0%) x 228 = 10.9 -> 11**; заметка: Two-stage design with incomplete stage 2.
- E5: источник порога: study's own; правило: adhoc row; self-reported professional diagnosis -> L1; у авторов: «reported having received misophonia diagnosis»; главная у авторов: no; период: lifetime; **расчёт: 0.7% x 375 = 2.6 -> 3**; заметка: Rounding uncertain (2/375 = 0.5%, 3/375 = 0.8%); denominator not stated.
- E6: источник порога: study's own; правило: adhoc row; 'sensitive to' sound item -> L0; у авторов: «positive misophonia screen (definitive)»; главная у авторов: no; период: current; заметка: Table 4b gives 13.5%.
- E7: источник порога: study's own; правило: adhoc row; 'sensitive to' sound item -> L0; у авторов: «at least occasional misophonia symptoms»; главная у авторов: no; период: current; **расчёт: 49 (Yes) + 164 (Sometimes) from Table 5b**; заметка: Table 4b: 44.6% sometimes + 13.5% yes.

**⚠ Проверка скриптом (обратите внимание):**
- E2, E3, E4, E6, E7: n оценки не равно n_analysed выборки (375): проверьте знаменатель

**Ключевые поля выборки:**
- **n_analysed: 375** — Table 2 — «Total number of participants included in final analyses 451 375»
- **population: gp_other** — Method, Participants, p. 34 — «community-dwelling English speaking adults located in the United States»
- **sampling: convenience** — Method, Participants, p. 34 — «"workers" (in this case, research participants) choose jobs to complete for pay»

**Остальные поля:**
- clinical_group: NA — Method, p. 35 — «The selection of two different, non-clinical samples was appropriate»
- country: USA — Method, Participants, p. 34 — «drawn from community-dwelling English speaking adults located in the United States participating in research for compensation through Amazon's Mechanical Turk …»
- setting: online panel (Amazon Mechanical Turk; REDCap survey) — Method, Procedure, p. 35 — «The community sample was collected using Amazon's MTurk within approximately ten hours on a single day in April 2015.»
- data_years: 2015 — Method, Procedure, p. 35 — «on a single day in April 2015»
- design: cross-sectional — Method, Design, p. 35 — «This was a cross-sectional survey study»
- topic_disclosed: NR — Method, Procedure, p. 36 — «At the beginning of the survey, all participants answered a series of screening questions about tinnitus, sound intolerance, and hearing problems.»
- inclusion_exclusion: US English-speaking MTurk workers aged 18+; no other exclusion; excluded if 3+ errors on control questions or incomplete survey — Method, pp. 34-35, 45 — «Participants were required to be 18 years of age and older and capable of providing informed consent. There were no other exclusion criteria»
- n_invited: NR — Table 2 — «Total number of participants who initiated survey ... 612»
- n_responded: 400 — Table 2 — «612 ... Number of incomplete/not submitted survey responses in REDCap ... 212»
- response_rate: NR — Table 2 — «Total number of participants who initiated survey 653 612»
- age_mean: 37.04 — Table 3 — «37.04 (12.54)* (17-77)»
- age_sd: 12.54 — Table 3 — «37.04 (12.54)* (17-77)»
- age_min: 17 — Table 3 — «37.04 (12.54)* (17-77)»
- age_max: 77 — Table 3 — «37.04 (12.54)* (17-77)»
- age_group: adults — Method p. 34; Table 3 — «Participants were required to be 18 years of age and older»
- pct_female: 54.6 — Table 3 — «Female Male No response ... 54.6% 44.6% .8%»
- informant: self — Method, Measures, p. 36 — «either valid and reliable self-report questionnaires or experimental questions created by the research team»
- mode: online — Method, Procedure, p. 35 — «with a link to take the survey at an external, secure electronic data storage system, Research Electronic Data Capture (REDCap)»
- instruments: Misophonia Questionnaire (MQ; English, Wu et al. 2014) incl. Severity Scale; A-MISO-S (English, self-completed online, only for screen-positives); ad hoc misophonia screening item; ad hoc item on received sound-related diagnoses (community only); DST Scale / Human Sounds Subscale (study-developed) — Method, Measures, pp. 36-38; Table 4b — «Screening for sound-related diagnoses Misophonia ... Not administered ... .7%»
- instrument_validated_in_language: yes — Method, Measures, p. 38 — «Convergent and discriminant validity were demonstrated in a large college student sample (Wu et al., 2014).»
- pub_status: thesis — Title page — «A dissertation submitted in partial fulfillment of the requirements for the degree of Doctor of Philosophy at Virginia Commonwealth University»
- language: English — Full text — «DECREASED SOUND TOLERANCE (DST): PREVALENCE, CLINICAL CORRELATES, AND DEVELOPMENT OF A DST ASSESSMENT INSTRUMENT»
- funding_coi: NR — Acknowledgement; Procedure p. 35 — «Community sample participants spent an average of 46 minutes completing the survey and received $1 upon completion.»
- notes: Doctoral dissertation; the authors pool this sample with the student sample as a 'combined sample'. The sample was randomly split into two subsamples (188/187) for factor analysis only. Reported age minimum 17 contradicts the 18+ criterion. A-MISO-S was self-completed only by screen-positives (n=228). Per-sample MQ cases are reconstructed (56/375), consistent with the combined 129.

**Риск смещения (JBI):**
1. рамка выборки: **no** — MTurk workers only; the authors claim the general (US) adult population — Method p. 34; Discussion p. 99 — «This study is the first to investigate two emerging behavioral medicine conditions... in two large, representative general population samples.»
2. способ отбора: **no** — Online non-probability opt-in panel, first-come until target reached — Procedure p. 35 — «The survey was made available until approximately 400 students and 400 community adults completed it.»
3. размер выборки: **no** — n=375 < 385 — Table 2 — «Total number of participants included in final analyses 451 375»
4. описание выборки и условий: **yes** — Age, sex, setting, country, date reported — Table 3; Procedure p. 35 — «collected using Amazon's MTurk within approximately ten hours on a single day in April 2015»
5. охват (пропуски): **yes** — MQ Severity available for 373 of 375 — Table 6b — «Severity scale ... 373 ... 2.89 (2.81)»
6. валидность определения случая: **yes** — MQ Severity Scale >=7, English validated version — Method, Measures, p. 38 — «individuals that reported a 7 or higher on the MQ Misophonia Severity Scale were considered to have clinically significant misophonia symptoms (Wu et al., 2014)»
7. единое надёжное измерение: **yes** — Same online instrument and threshold for all; internal consistency reported in the source — p. 25 — «adequate internal consistency, and convergent and discriminant validity were demonstrated (Wu et al., 2014)»
8. статистика (числитель и знаменатель): **yes** — Percentage reported; counts reconstructable (56/375; sums to combined 129); margin of error given — Discussion p. 87; Table 9 — «community members' (14.9%) report of misophonia symptoms»
9. отклик: **no** — Open MTurk task, no invited denominator; 212 of 612 initiators incomplete; not handled — Table 2 — «Number of incomplete/not submitted survey responses in REDCap 161 212»

Правки:
- 

Проверено: да