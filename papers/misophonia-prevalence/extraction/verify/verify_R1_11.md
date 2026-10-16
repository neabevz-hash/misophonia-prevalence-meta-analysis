# Проверка выписывания — файл 11 из 11

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

## ST096 · Jahn 2024 · Journal of Pain

Основной отчёт R2119: [текст](../../fulltext/text/R2119.txt) — «Clinical phenotype and management of sound-induced pain: Insights from adults with pain hyperacusis» — [DOI](https://doi.org/10.1016/j.jpain.2024.104741)
Расхождения в тексте: Table 1: 5/31 = 16.13%, which matches. The text gives n=32 participants; the comorbidity denominator is 31 (Table 1 title). The concept-mapping stages had different n (26 in the focus group, 26 in rating, 15 in sorting, 24 in the follow-up survey). These do not affect the misophonia estimate. pct_female = 11/32 = 34.4%, calculated from the text.
Заметка ИИ: Single-sample concept-mapping study of pain hyperacusis. The only misophonia data is one self-reported comorbidity item (5/31). The reviewer should confirm eligibility under E1 (sound-sensitivity recruitment) and the country (USA is likely but not stated).

### ST096-1 · Adults with self-reported pain hyperacusis, online/snowball recruitment (University of Texas at Dallas), n=32 (31 for comorbidity items)
Отчёты: R2119 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · self-reported co-morbid misophonia (condition checklist) | **L1** | **5 / 31** | 16.1 | Table 1 | «Thirty-one participants responded to the audiovestibular, neurological, and mental health questions. ... Misophonia / 16.13% (n = 5)» |

- E1: источник порога: study's own; правило: adhoc row; self-reported diagnosis/self-identification -> L1 (no scale-based L1 estimate in sample); у авторов: «self-reported co-morbid conditions: Misophonia»; главная у авторов: no; период: NR; заметка: Item wording not reported; unclear whether it means a professional diagnosis or self-identification. Sample recruited for pain hyperacusis.

**Ключевые поля выборки:**
- **n_analysed: 31** — Table 1 title — «Thirty-one participants responded to the audiovestibular, neurological, and mental health questions.»
- **population: clinical** — Methods, Participants — «who self-reported that they experience physical pain when they hear sounds participated. All participants had experienced pain hyperacusis for at least one year»
- **sampling: snowball** — Methods, Participants — «A snowball sampling technique was used to recruit prospective participants»

**Остальные поля:**
- clinical_group: hyperacusis (pain hyperacusis/noxacusis, self-reported) — Methods, Participants — «All participants had experienced pain hyperacusis for at least one year (range 1 to 27 years)»
- country: NR — Methods, Participants — «approved by the Institutional Review Board of The University of Texas at Dallas (IRB-23–200)... recruitment flyers were posted online on our laboratory website…»
- setting: online (social media, lab website, ResearchMatch registry); people with self-reported pain hyperacusis; virtual focus group plus online surveys — Methods, Participants — «recruitment flyers were posted online on our laboratory website, social media (Facebook, Instagram, and Twitter/X), and a research recruitment registry (Resear…»
- data_years: NR — Methods — «This study was approved by the Institutional Review Board of The University of Texas at Dallas (IRB-23–200)»
- design: other — Methods, Procedures — «We first used a modified concept mapping approach to identify the key symptoms and experiences associated with sound-induced pain»
- topic_disclosed: yes — Methods, Participants — «32 fluent English-speaking adults ... who self-reported that they experience physical pain when they hear sounds participated»
- inclusion_exclusion: Fluent English-speaking adults who self-report physical pain from sounds, pain hyperacusis for at least 1 year — Methods, Participants — «fluent English-speaking adults ... who self-reported that they experience physical pain when they hear sounds participated. All participants had experienced pa…»
- n_invited: NR — Methods, Participants — «A snowball sampling technique was used to recruit prospective participants»
- n_responded: 32 — Methods, Participants — «A total of 32 fluent English-speaking adults»
- response_rate: NR — Methods, Participants — «A snowball sampling technique was used to recruit prospective participants»
- age_mean: 37 — Methods, Participants — «age 19–65 years, mean age = 37 years, 11 female»
- age_sd: NR — Methods, Participants — «age 19–65 years, mean age = 37 years»
- age_min: 19 — Methods, Participants — «age 19–65 years»
- age_max: 65 — Methods, Participants — «age 19–65 years»
- age_group: adults — Methods, Participants — «32 fluent English-speaking adults (age 19–65 years»
- pct_female: 34.4 — Methods, Participants — «A total of 32 ... adults (age 19–65 years, mean age = 37 years, 11 female)»
- informant: self — Table 1 title; Methods — «Prevalence of self-reported co-morbid conditions.»
- mode: online — Concept Mapping Stage 2 — «They received a private link to a Qualtrics survey»
- instruments: Self-reported co-morbid condition checklist item 'Misophonia' (ad hoc, English) — Table 1 — «Misophonia | 16.13% (n = 5)»
- instrument_validated_in_language: no — Table 1 — «Prevalence of self-reported co-morbid conditions.»
- pub_status: journal — Header — «Journal of Pain; DOI: 10.1016/j.jpain.2024.104741»
- language: English — Full text — «Clinical phenotype and management of sound-induced pain: Insights from adults with pain hyperacusis»
- funding_coi: NIH NIDCD K01 DC019647 and others; KNJ on Scientific Advisory Board for Hyperacusis Research Ltd. and scientific advisor for Hyperacusis Central; no other conflicts declared — Acknowledgments — «This work was supported by the National Institutes of Health National Institute on Deafness and Other Communication Disorders (NIH NIDCD) K01 DC019647 ... KNJ …»
- notes: Eligibility to check: the sample was recruited for pain hyperacusis (a sound-intolerance condition). Extracted as clinical group 'hyperacusis' because Table 1 coding lists hyperacusis, but the reviewer should decide whether E1 ('recruited because of sound sensitivity') applies. Misophonia is only a self-reported co-morbid condition (wording and time frame not described). Country not stated: the IRB is at UT Dallas (USA), but recruitment was online and open, so participants may be international. Data collection years not reported. Small concept-mapping study; pct_female = 11/32.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was online/social-media and registry volunteers, not a frame covering adults with pain hyperacusis — Methods, Participants — «recruitment flyers were posted online on our laboratory website, social media (Facebook, Instagram, and Twitter/X), and a research recruitment registry (Resear…»
2. способ отбора: **no** — Snowball / volunteer opt-in sampling — Methods, Participants — «A snowball sampling technique was used to recruit prospective participants»
3. размер выборки: **no** — n=31 for the misophonia item, below 139 for a clinical sample — Table 1 title — «Thirty-one participants responded to the audiovestibular, neurological, and mental health questions.»
4. описание выборки и условий: **no** — Age, sex and setting reported; country and dates of data collection not reported — Methods, Participants — «age 19–65 years, mean age = 37 years, 11 female»
5. охват (пропуски): **yes** — 31 of 32 participants (97%) answered the comorbidity items — Table 1 title — «Thirty-one participants responded to the audiovestibular, neurological, and mental health questions.»
6. валидность определения случая: **no** — Misophonia defined by an ad hoc self-reported comorbidity item — Table 1 — «Prevalence of self-reported co-morbid conditions. ... Misophonia | 16.13% (n = 5)»
7. единое надёжное измерение: **unclear** — Same online survey for all, but item wording not given and no reliability reported — Table 1 — «Prevalence of self-reported co-morbid conditions.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (5/31); CI calculable — Table 1 — «Misophonia | 16.13% (n = 5)»
9. отклик: **no** — Open online/snowball recruitment with no denominator of invited people — Methods, Participants — «A snowball sampling technique was used to recruit prospective participants»

Правки:
- 

Проверено: да

