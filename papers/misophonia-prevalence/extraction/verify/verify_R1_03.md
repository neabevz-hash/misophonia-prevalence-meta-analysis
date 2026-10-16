# Проверка выписывания — файл 3 из 10

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

## ST021 · Valente 2026 · Audiology - Communication Research

Основной отчёт R0210: [текст](../../fulltext/text/R0210.txt) · [PDF](../../fulltext/pdf/R0210.pdf) — «Fatores associados à misofonia em estudantes, professores, técnicos de uma universidade pública brasileira» — [DOI](https://doi.org/10.1590/2317-6431-2025-3080pt)
Расхождения в тексте: Response: 25% of 809 = 202, but the final sample is 206 (206/809 = 25.5%). The number who responded before exclusions is not given in the text (Figure 1 is not available). The percentages for female (51.3%) and occupation (54.2/31.0/6.2, sum 91.4%) are given for 'participants with misophonia' but match neither n=47 nor n=206. Table 1 percentages do not always match the counts: otalgia 98/159 = 61.6% (printed 61.3); self-reported hearing loss 44/159 = 27.7% (printed 27.6). Table 2: depression 'improvável' 30/47 = 63.8% (printed 63.2); 'possível' 58/159 = 36.5% (printed 34.4); 'provável' 2/47 = 4.3% (printed 4.9) and 1/159 = 0.6% (printed 0.7); anxiety 'possível' 19/47 = 40.4% (printed 40.5). In the Discussion, anxiety signs are given as 61.7%, but by Table 2 (19+12)/47 = 66.0%. The prevalence numerator and denominator (47/206) are consistent: 47+159 = 206.
Заметка ИИ: One sample, one estimate: 47/206 (22.8%) on a 5-item misophonia screening list attributed to Schröder et al. 2013, cut-off >=3/5. The Portuguese translation has not been validated, so the instrument is coded adhoc and the estimate L1. Age is not reported, and the sex distribution is reported only for the misophonia group.

### ST021-1 · UFBA Institute of Health Sciences students, faculty and staff, Salvador, Brazil, n=206
Отчёты: R0210 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · positive response to >=3 of 5 items of the Lista de Triagem para Misofonia (self-completed, Portuguese unvalidated translation) | **L1** | **47 / 206** | 22.8 | Page 4, Tabela 1; Page 2, Procedimentos | «Misofonia Sim (%) N= 47 Não (%) N= 159» |

- E1: источник порога: study's own; правило: adhoc row (unvalidated short screener; symptom count on item set); G3; у авторов: «presença de misofonia [presence of misophonia]»; главная у авторов: yes; период: NR; заметка: Prevalence 47/206 = 22.8% (not stated as a percentage by the authors). Item content is not reported, so we cannot tell whether a positive screen requires distress or impairment; coded L1.

**Ключевые поля выборки:**
- **n_analysed: 206** — Page 4, Tabela 1 — «Misofonia Sim (%) N= 47 Não (%) N= 159»
- **population: other_nonclinical** — Page 2, Métodos; Page 3, Resultados — «A ocupação mais frequente foi a de estudante universitário (54,2%), seguida por técnico administrativo (31,0%) e docente (6,2%). [Most frequent occupation: university student (54.2%), then administrative staff (31.0%) and faculty (6.2%)]»
- **sampling: convenience** — Page 2, Métodos — «com uma amostra de conveniência composta por estudantes, professores e técnicos do instituto de saúde [with a convenience sample of students, faculty and staff of the health institute]»

**Остальные поля:**
- clinical_group: NA — NA
- country: BRA — Page 1, footnote — «Trabalho realizado na Universidade Federal da Bahia – UFBA – Salvador (BA), Brasil.»
- setting: university (Instituto de Ciências da Saúde, UFBA, Salvador: 2 undergraduate courses, 2 postgraduate programmes, institute staff) — Page 2, Métodos — «contato com as coordenações de dois cursos de graduação (Fonoaudiologia e Fisioterapia) e dois de pós-graduação vinculados ao Instituto de Ciências da Saúde [c…»
- data_years: 2022 — Page 2, Métodos — «disponibilizado via e-mail, entre junho e dezembro de 2022 [made available by e-mail between June and December 2022]»
- design: cross-sectional — Page 2, Métodos — «Trata-se de um estudo seccional, quantitativo, analítico, exploratório [This is a cross-sectional, quantitative, analytical, exploratory study]»
- topic_disclosed: yes — Page 2, Procedimentos — «Essa pesquisa integra o projeto intitulado “Misofonia em estudantes, professores e técnicos em uma universidade pública brasileira”. [This research is part of …»
- inclusion_exclusion: Included: students, faculty, staff of ICS/UFBA who consented and answered; excluded: those who withdrew or answered outside the collection period — Page 2, Métodos — «Foram excluídos aqueles que desistiram em qualquer momento da pesquisa ou que responderam ao questionário fora do período determinado para a coleta de dados.»
- n_invited: 809 — Page 3, Resultados — «Do total dos 809 e-mails enviados, obteve-se taxa de resposta de 25%. [Of 809 e-mails sent, response rate 25%]»
- n_responded: 206 — Page 3, Resultados — «A amostra final foi composta por 206 indivíduos. [The final sample comprised 206 individuals]»
- response_rate: 25 — Page 3, Resultados — «Do total dos 809 e-mails enviados, obteve-se taxa de resposta de 25%.»
- age_mean: NR — NR
- age_sd: NR — NR
- age_min: NR — NR
- age_max: NR — NR
- age_group: NR — NR
- pct_female: NR — Page 3, Resultados — «Entre os participantes com misofonia, observou-se predominância do sexo feminino (51,3%). [Among participants with misophonia, female predominance (51.3%)]»
- informant: self — Page 2, Métodos — «As respostas foram fornecidas pelos próprios participantes após leitura independente dos itens. [Responses were given by participants themselves after reading …»
- mode: online — Page 2, Procedimentos — «por meio de um formulário elaborado na plataforma Google Forms e disponibilizado via e-mail»
- instruments: Lista de Triagem para Misofonia (Misophonia Screening List, 5 items, citing Schröder et al. 2013), Portuguese translation, not validated — Page 2, Procedimentos — «A terceira seção incluiu a Lista de Triagem para Misofonia(7) ... traduzida para o português ... o instrumento ainda não dispõe de validação formal para o idio…»
- instrument_validated_in_language: no — Page 2, Procedimentos; Page 5, Discussão — «o instrumento ainda não dispõe de validação formal para o idioma, sendo utilizado nesta pesquisa apenas como medida de triagem [the instrument has no formal va…»
- pub_status: journal — Page 1, header — «Audiol Commun Res. 2026;31:e3080 ... Artigo Original»
- language: Portuguese (English abstract) — Page 1 — «Fatores associados à misofonia em estudantes, professores, técnicos de uma universidade pública brasileira»
- funding_coi: No funding declared; no conflict of interest — Page 1, footnotes — «Conflito de interesses: Não. ... Financiamento: Nada a declarar.»
- notes: Misophonia measured with a 5-item 'Lista de Triagem para Misofonia' attributed to Schröder et al. 2013 (not the MSL-CY); item content not reported; Portuguese translation not validated. Population mixes students (~54%), administrative staff (~31%) and faculty (~6%), coded other_nonclinical; occupation percentages are ambiguous (stated in the misophonia-group sentence, and they sum to 91.4%). The only sex figure (51.3% female) is given for participants with misophonia and cannot be traced to 47 or 206, so pct_female = NR. Age not reported. The flowchart (Figure 1) is not available as text. Top…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The target population is 'a Brazilian public university', but the frame was e-mail lists of only 2 undergraduate courses, 2 postgraduate programmes and the staff of one institute — Page 2, Métodos — «contato com as coordenações de dois cursos de graduação (Fonoaudiologia e Fisioterapia) e dois de pós-graduação vinculados ao Instituto de Ciências da Saúde»
2. способ отбора: **no** — Convenience sample with voluntary opt-in to an e-mailed online form — Page 2, Métodos — «com uma amostra de conveniência composta por estudantes, professores e técnicos»
3. размер выборки: **no** — n=206 < 385 — Page 3, Resultados — «A amostra final foi composta por 206 indivíduos.»
4. описание выборки и условий: **no** — Setting, country and dates are reported; age is not reported, and sex is given only for the misophonia group — Page 3, Resultados — «Entre os participantes com misofonia, observou-se predominância do sexo feminino (51,3%).»
5. охват (пропуски): **unclear** — Only the consent item was mandatory; missing misophonia data not reported — Page 2, Procedimentos — «o seu aceite foi a única pergunta obrigatória a ser respondida no questionário»
6. валидность определения случая: **no** — Unvalidated Portuguese translation of a 5-item screening list; ad hoc count threshold (>=3/5) — Page 2, Procedimentos — «o instrumento ainda não dispõe de validação formal para o idioma, sendo utilizado nesta pesquisa apenas como medida de triagem»
7. единое надёжное измерение: **unclear** — Same online instrument and threshold for everyone, but no reliability reported — Page 2, Procedimentos — «A presença de misofonia foi definida pela resposta positiva a pelo menos três dos cinco itens»
8. статистика (числитель и знаменатель): **yes** — Numerator 47 and denominator 206 clear in Table 1; CI calculable — Page 4, Tabela 1 — «Misofonia Sim (%) N= 47 Não (%) N= 159»
9. отклик: **no** — 25% response with no non-response handling — Page 3, Resultados — «Do total dos 809 e-mails enviados, obteve-se taxa de resposta de 25%.»

Правки:
- 

Проверено: да
---

## ST022 · Şahin Kamişli 2026 · The Journal of laryngology and otology

Основной отчёт R0236: [текст](../../fulltext/text/R0236.txt) — «Incidence of misophonia, associated auditory symptoms and sensory processing profiles in university students in Turkey: a comparative study of clinical, subcli…» — [DOI](https://doi.org/10.1017/s0022215126104526)
Расхождения в тексте: The clinical misophonia prevalence is given as 19% (abstract, Conclusions) and 19.2% (Discussion), but 81/499 = 16.2%. In Results, 26.6% (clinical) and 53.6% (subclinical) are 81/304 and 163/304, using the stage-2 total (60 controls + 244) as denominator. Discussion says 21 participants (7.9%) with misophonia symptoms had a psychiatric diagnosis; Table 1 gives 13 + 8 = 21 but 9.9% overall of 304. Discussion says 52 (21.3%) of the misophonia participants reported tinnitus and 74 (30.3%) hyperacusis; Table 1 gives 33 + 19 = 52 tinnitus and 43 + 31 = 74 hyperacusis, consistent. Results text attributes all 58 tinnitus and 76 hyperacusis cases to 'those with misophonia', but Table 1 includes controls. Table 5 counts do not match the text (e.g., 37 vs 30 in 'much less' sensation seeking).
Заметка ИИ: One eligible sample. Primary L2 estimate is 81/499 under the G10 two-stage rule; it differs from the authors' 19%. Sex-specific denominators for all 499 are not reported.

### ST022-1 · University students, multiple universities, Turkey, n=499
Отчёты: R0236 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · screening question 'yes' AND MQ Misophonia Severity Scale >=7 | **L2** | **81 / 499** | 16.2 | Results; Conclusions | «Of these participants, 163 were categorised as having subclinical misophonia and 81 as having clinical misophonia. ... In our sample of 499 individuals, 19 per cent met the criteria for clinical misophonia.» |
| E2 | all | adhoc · 'yes' to screening question on being disturbed/triggered by specific sounds (self-completed) | **L0** | **244 / 499** | 48.9 | Results | «A total of 244 students (48.8%) reported being sensitive to at least one specific sound, indicating subjective misophonia.» |
| E3 | female | multiple · screening question 'yes' AND MQ Misophonia Severity Scale >=7 | **L2** | **45 / NR** |  | Table 1 | «Female / 35 (11.5%) / 96 (31.6%) / 45 (14.8%) / 176 (57.9%)» |
| E4 | male | multiple · screening question 'yes' AND MQ Misophonia Severity Scale >=7 | **L2** | **36 / NR** |  | Table 1 | «Gender / Male / 25 (8.2%) / 67 (22%) / 36 (11.8%) / 128 (42.1%)» |

- E1: источник порога: developer paper; правило: MQ row (MSS>=7); G4 combined 'A and B'; G10 two-stage denominator; у авторов: «clinical misophonia»; главная у авторов: yes; период: NR; **расчёт: Denominator = all 499 screened at stage 1 (G10); screen-negatives count as non-cases; 81/499 = 16.2%**; заметка: The authors report 19% / 19.2%, which does not equal 81/499 (16.2%). MQ Severity was given only to the 244 screen-positives.
- E2: источник порога: study's own; правило: adhoc row; item asks only about being disturbed/triggered by sounds -> L0; у авторов: «subjective misophonia»; главная у авторов: no; период: current; заметка: Listed, not pooled.
- E3: источник порога: developer paper; правило: MQ row (MSS>=7); G4; G10; у авторов: «clinical misophonia»; главная у авторов: no; период: NR; заметка: Number of females among the 499 screened is not reported, so there is no denominator; 45 females in the clinical group.
- E4: источник порога: developer paper; правило: MQ row (MSS>=7); G4; G10; у авторов: «clinical misophonia»; главная у авторов: no; период: NR; заметка: Number of males among the 499 screened is not reported, so there is no denominator; 36 males in the clinical group.

**Ключевые поля выборки:**
- **n_analysed: 499** — Results — «In the first phase of the study, 499 university students were included to subjectively determine the incidence of misophonia.»
- **population: university_students** — Results — «In the first phase of the study, 499 university students were included to subjectively determine the incidence of misophonia.»
- **sampling: NR** — Materials and methods — «A total of 499 participants aged between 18 and 26 years (mean = 20.2, SD = 1.6) were included in the first phase of the study.»

**Остальные поля:**
- clinical_group: NA — NA
- country: TUR — Materials and methods — «The study was conducted among university students from various universities across Turkey, regardless of their field of study.»
- setting: university (students from various universities across Turkey) — Materials and methods — «The study was conducted among university students from various universities across Turkey, regardless of their field of study.»
- data_years: NR — Materials and methods — «Ethical approval was obtained from the University Ethics Committee (research code: 2022 – 750»
- design: cross-sectional — Study design and procedure — «In the first stage of data collection, participants were asked a screening question»
- topic_disclosed: NR — Materials and methods — «Written informed consent was obtained from all participants before data collection.»
- inclusion_exclusion: Students aged ≥18, educated in Turkish, Turkish native language; excluded if unable to complete scales, additional disabilities or conditions preventing completion — Materials and methods — «Participants included students who were 18 years of age or older, received their education in Turkish and whose native language was Turkish. Individuals who we…»
- n_invited: NR — NR
- n_responded: 499 — Materials and methods — «A total of 499 participants aged between 18 and 26 years (mean = 20.2, SD = 1.6) were included in the first phase of the study.»
- response_rate: NR — NR
- age_mean: 20.2 — Materials and methods — «499 participants aged between 18 and 26 years (mean = 20.2, SD = 1.6)»
- age_sd: 1.6 — Materials and methods — «499 participants aged between 18 and 26 years (mean = 20.2, SD = 1.6)»
- age_min: 18 — Materials and methods — «499 participants aged between 18 and 26 years»
- age_max: 26 — Materials and methods — «499 participants aged between 18 and 26 years»
- age_group: adults — Materials and methods — «499 participants aged between 18 and 26 years»
- pct_female: NR — Table 1 — «Female | 35 (11.5%) | 96 (31.6%) | 45 (14.8%) | 176 (57.9%)»
- informant: self — Limitations — «the assessment of misophonia and related auditory and sensory features was based entirely on self-report measures.»
- mode: mixed — Materials and methods — «Data were collected using both online and paper-and-pencil versions of the questionnaires.»
- instruments: Ad hoc screening question (structured interview form, self-completed); MQ (Misophonia Questionnaire incl. Misophonia Severity Scale; language version not stated, participants Turkish native speakers) — Study design and procedure; Data collection tools — «Misophonia was assessed using the MQ,10,25 which measures misophonia symptoms as well as emotional and behavioural responses to trigger sounds.»
- instrument_validated_in_language: NR — Data collection tools — «Misophonia was assessed using the MQ,10,25 ... A score of 7 or higher in this section is considered clinically significant for misophonia.»
- pub_status: journal — Header — «venue: The Journal of laryngology and otology; DOI: 10.1017/s0022215126104526»
- language: English — Full text — «Incidence of misophonia, associated auditory symptoms and sensory processing profiles in university students in Turkey»
- funding_coi: TÜBİTAK 2209-A undergraduate research support (project 1919B012206530); no conflict of interest declared — Acknowledgments; Conflict of interest — «This study was supported by TÜBİTAK ... with the project number 1919B012206530. ... There is no conflict of interest in the study.»
- notes: Two-stage design: everyone (n=499) answered an ad hoc screening question; only the 244 screen-positives were classified by MQ Severity (>=7 clinical = 81; <7 subclinical = 163). 60 controls were drawn at random from the screen-negatives of the same sample (not a separate sample). Sex and the Table 1 characteristics are reported only for the 304 people in stage 2 (57.9% female), not for all 499. The authors' 19%/19.2% clinical prevalence cannot be reproduced (81/499 = 16.2%). Partly presented earlier as a preliminary study at Ulusal Otoloji Norotoloji Kongresi: possible overlap with a conferen…

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Target is university students in Turkey; the sampling frame (which universities, how students were reached) is not described. — Materials and methods — «The study was conducted among university students from various universities across Turkey, regardless of their field of study.»
2. способ отбора: **unclear** — Recruitment and sampling method for the 499 students are not described. — Materials and methods — «A total of 499 participants aged between 18 and 26 years (mean = 20.2, SD = 1.6) were included in the first phase of the study.»
3. размер выборки: **yes** — n = 499 >= 385. — Results — «In the first phase of the study, 499 university students were included»
4. описание выборки и условий: **unclear** — Age, setting and country are reported; dates are missing; sex is reported only for the 304 stage-2 participants, not all 499. — Materials and methods; Table 1 — «499 participants aged between 18 and 26 years (mean = 20.2, SD = 1.6)»
5. охват (пропуски): **yes** — All 244 screen-positives were classified by MQ Severity (163 + 81 = 244); no missing misophonia data apparent. — Results — «Of these participants, 163 were categorised as having subclinical misophonia and 81 as having clinical misophonia.»
6. валидность определения случая: **unclear** — Primary definition is screening question plus MQ Severity >=7 (L2). The MQ language version and its validation are not stated. — Data collection tools — «Misophonia was assessed using the MQ,10,25 ... A score of 7 or higher in this section is considered clinically significant for misophonia.»
7. единое надёжное измерение: **no** — Online and paper modes were mixed with no mode check; no reliability reported in the sample. — Materials and methods — «Data were collected using both online and paper-and-pencil versions of the questionnaires.»
8. статистика (числитель и знаменатель): **no** — The reported 19%/19.2% prevalence cannot be traced to 81/499 (16.2%); 26.6% uses a denominator of 304; no CI. — Results; Discussion — «In our study, 19.2 per cent of participants were classified within the clinical misophonia group.»
9. отклик: **unclear** — Number invited and response rate are not reported. — Materials and methods — «A total of 499 participants aged between 18 and 26 years (mean = 20.2, SD = 1.6) were included in the first phase of the study.»

Правки:
- 

Проверено: да
---

## ST023 · Chalotra 2025 · The Egyptian Journal of Otolaryngology

Основной отчёт R0274: [текст](../../fulltext/text/R0274.txt) · [PDF](../../fulltext/pdf/R0274.pdf) — «Evaluation of extended high frequency thresholds in individuals with misophonia» — [DOI](https://doi.org/10.1186/s43163-025-00912-5)
Не выписано ИИ: Experiment Group 2 (n=15, people with misophonia who agreed to take part) and Group 1 controls (n=15, people with no misophonia complaints). Both are subsets of, or selected in relation to, misophonia status for the case-control audiometry comparison; they give no prevalence estimate. Group 2 was selected because of misophonia (E1). How the controls were recruited is not stated.
Расхождения в тексте: The abstract gives an age SD of 11.3 for all 30 participants; the Method gives 11.37 for Group 1 only, and the abstract's mean of 32.01 matches Group 1's mean. The A-MISO-S is described as 7 items with a range of 0-28 and bands up to 'extreme (20–28)', yet the case rule is '1–24'. The text says paired t-tests are in 'Tables 2 and 3' and effect sizes in 'Table 2', but these are actually Tables 3/4 and 5. None of this changes the prevalence numbers (36/283).
Заметка ИИ: There is one eligible sample: the screening of 283 adults. Its only estimate (36/283) uses A-MISO-S >=1, which is L0 (listed, not pooled). Country (IND) is inferred from the author affiliations.

### ST023-1 · Preliminary misophonia screening of adults, India (probably Vadodara), n=283
Отчёты: R0274 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | A-MISO-S · A-MISO-S score 1-24 (>=1) | **L0** | **36 / 283** | 12.7 | Page 3, Method | «If participants score anything between 1–24 they were moved to the group-2 ... A preliminary screening was done on 283 adults out of which 36 were identified to have misophonia.» |

- E1: источник порога: study's own; правило: A-MISO-S row; G2 threshold below the L1 cut-off (score 1-24 = misophonia) -> L0; у авторов: «identified to have misophonia»; главная у авторов: yes; период: NR; заметка: 12.7%. The text does not say explicitly that the 1-24 rule was applied at screening (it is stated for group allocation). L0: listed, not pooled.

**Ключевые поля выборки:**
- **n_analysed: 283** — Page 3, Method — «A preliminary screening was done on 283 adults out of which 36 were identified to have misophonia.»
- **population: gp_other** — Page 3, Method — «A preliminary screening was done on 283 adults»
- **sampling: NR** — Page 3, Method — «A preliminary screening was done on 283 adults»

**Остальные поля:**
- clinical_group: NA — NA
- country: IND — Page 1, affiliations — «1 Sumandeep Vidyapeeth deemed to be University, Vadodara, India»
- setting: NR (adults screened before an audiology case-control study; the place of recruitment is not stated. The authors are at a university and the work is part of a doctoral thesis) — Page 3, Method; Page 6, Ethics — «A preliminary screening was done on 283 adults out of which 36 were identified to have misophonia.»
- data_years: NR — Page 6, Ethics — «approved by Ethics Committee for Academic Research projects with ref no. ECARP/2024/67»
- design: screening phase of experiment — Page 3, Method — «A preliminary screening was done on 283 adults out of which 36 were identified to have misophonia. However, 15 participants with Misophonia agreed to participa…»
- topic_disclosed: NR — Page 3, Method — «All the participants were screened for Misophonia using the revised Amsterdam Misophonia Scale (A-MISO-S) [8].»
- inclusion_exclusion: Adults. Stated exclusions (known neurological or psychological conditions, recent anxiety or stress, abnormal hearing) apply to the 30 experiment participants. Criteria for the 283 screened are not reported. — Page 2, Method — «All the participants with known neurological and psychological conditions were excluded from the study. Additionally, participants who reported recent anxiety …»
- n_invited: NR — Page 3, Method — «A preliminary screening was done on 283 adults»
- n_responded: 283 — Page 3, Method — «A preliminary screening was done on 283 adults»
- response_rate: NR — NA
- age_mean: NR — Page 1, Abstract — «Thirty participants aged 18–54 years (mean age 32.01, SD = 11.3)»
- age_sd: NR — Page 1, Abstract — «Thirty participants aged 18–54 years (mean age 32.01, SD = 11.3)»
- age_min: NR — Page 3, Method — «A preliminary screening was done on 283 adults»
- age_max: NR — NA
- age_group: adults — Page 3, Method — «A preliminary screening was done on 283 adults»
- pct_female: NR — Page 2, Method — «There were 8 and 9 females in Group1 and Group2, respectively.»
- informant: clinician — Page 3, Method — «The Amsterdam Misophonia Scale – Structured (A-MISO-S) is a clinician-administered tool developed to assess the severity of misophonia symptoms.»
- mode: face-to-face interview — Page 3, Method — «is a clinician-administered tool ... The questionnaire was administered in English language only»
- instruments: A-MISO-S (described as 'revised Amsterdam Misophonia Scale', 7 items, 0-28), English — Page 3, Method — «includes seven items ... total score ranging from 0 to 28 ... The questionnaire was administered in English language only»
- instrument_validated_in_language: NR — Page 3, Method — «All the participants were screened for Misophonia using the revised Amsterdam Misophonia Scale (A-MISO-S) [8].»
- pub_status: journal — Page 1, header — «The Egyptian Journal of Otolaryngology (2025) 41:171»
- language: English — Page 1 — «Evaluation of extended high frequency thresholds in individuals with misophonia»
- funding_coi: No external funding. The authors declare no competing interests. The study is part of a doctoral thesis. — Page 6, Funding; Page 7, Competing interests — «This research did not receive any grant from any funding agencies. ... The authors declare no competing interests.»
- notes: The main study is a case-control audiology study (15 misophonia vs 15 controls); prevalence comes only from the preliminary screening (36/283). Demographics, setting, recruitment and dates of the 283 screened adults are not reported; country is inferred from author affiliations. Informant and mode are taken from the authors' general description of the A-MISO-S as clinician-administered; how it was actually given at screening is not stated. The A-MISO-S is described with 7 items and a range of 0-28 (the published A-MISO-S has 6 items, 0-24), and the case rule is 'anything between 1-24'. It is …

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — The sampling frame of the 283 screened adults is not described. — Page 3, Method — «A preliminary screening was done on 283 adults»
2. способ отбора: **unclear** — The sampling method for the screening is not described. — Page 3, Method — «A preliminary screening was done on 283 adults»
3. размер выборки: **no** — n = 283, below 385. — Page 3, Method — «A preliminary screening was done on 283 adults»
4. описание выборки и условий: **no** — For the screened sample, age, sex, setting and dates are not reported; only the country can be inferred. — Page 3, Method — «A preliminary screening was done on 283 adults out of which 36 were identified to have misophonia.»
5. охват (пропуски): **unclear** — Missing data in the screening are not reported. — Page 3, Method — «A preliminary screening was done on 283 adults»
6. валидность определения случая: **no** — Cases are defined by an A-MISO-S score of 1 or more, which is inside the subclinical range (L0). The scale version (7 items, 0-28) is nonstandard and has no stated English validation. — Page 3, Method — «If participants score anything between 1–24 they were moved to the group-2 (individuals with misophonia).»
7. единое надёжное измерение: **unclear** — Everyone received the same instrument, but no reliability is reported and the mode of administration is unclear. — Page 3, Method — «All the participants were screened for Misophonia using the revised Amsterdam Misophonia Scale (A-MISO-S) [8].»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are given (36/283), so a CI can be calculated. The case rule is only implied. — Page 3, Method — «283 adults out of which 36 were identified to have misophonia»
9. отклик: **unclear** — The number invited and the response rate are not reported. — Page 3, Method — «A preliminary screening was done on 283 adults»

Правки:
- 

Проверено: да
---

## ST024 · Heller 2025 · PloS one

Основной отчёт R0314: [текст](../../fulltext/text/R0314.txt) — «Reassigning sources of misophonic trigger sounds to change their unpleasantness: Testing alternative mechanisms with a new set of movies, paintings, and words.» — [DOI](https://doi.org/10.1371/journal.pone.0321594)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R0368 (ST027), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap
Не выписано ИИ: Expt 1 (n=82; 20 misophonic) and Expt 2 (n=81; 26 misophonic): E1. These groups were screened, and extra misophonic participants were recruited on purpose ('additional recruitment for misophonic participants ... through Prolific, flyers ..., soQuiet.org, and social media'). The general-pool and targeted recruits cannot be told apart, so the counts do not give a prevalence. Expt 5C is not a separate sample: it used the same 32 participants as Expt 3C.
Расхождения в тексте: The authors' pooled figure does not match the per-experiment counts. Pooled statement (General methods): 'Across all unscreened groups (i.e., Experiments 3A, 4 and 5A-B; N = 154), the percentage of individuals who received a clinical or subclinical misophonia score was 11.69%, or 9.09%, respectively.' The N matches the parts: 68+32+20+34 = 154. The cases do not. The per-experiment misophonia counts are 6+11+4+5 = 26/154 = 16.9%. 11.69% of 154 = 18 and 9.09% of 154 = 14; together that is 32 (20.8%). It is also unclear whether 11.69% means clinical and 9.09% subclinical, or the other way round. Because of these problems the pooled values were not extracted as estimates; per-experiment counts are used. The misophonic subgroup in Expt 3C (Mage 21.83, range 19–28, 4 F, 2 M) is described exactly as in Expt 3A, which may be a copy error. Date format is dd/mm/yyyy (01/07/2022 to 23/04/2024). n_…
Заметка ИИ: This is an experimental paper, not a prevalence study. Misophonia status was screened only to classify participants. The case definition is the 'umbrella' criterion: a subclinical or clinical score on any of MisoQuest, MQ, DVMSQ or S-Five, which is L1 under rule G4. Each participant completed 'one or more' of these questionnaires, and which ones is not reported. Funding statement not present in the supplied text. The language of the questionnaire versions is not stated. Expt 3B and 3C are not part of the authors' pooled N=154.

### ST024-1 · Expt 3A unscreened, CMU pool/Prolific, n=68
Отчёты: R0314 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five (each questionnaire's scoring guidelines) | **L1** | **6 / 68** | 8.8 | Expt 3A, Participants | «In this unscreened group that was recruited irrespective of misophonic status, six individuals (Mage = 21.83 years; range = 19–28 years; 4 females, 2 males) met our criteria for misophonia.» |
| E2 | female | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **4 / 35** | 11.4 | Expt 3A, Participants | «35 females, 31 males, two non-binary ... six individuals (... 4 females, 2 males) met our criteria for misophonia» |
| E3 | male | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **2 / 31** | 6.5 | Expt 3A, Participants | «35 females, 31 males, two non-binary ... six individuals (... 4 females, 2 males) met our criteria for misophonia» |

- E1: источник порога: developer paper; правило: G4 'A or B' (subclinical or clinical on any) -> L1; у авторов: «met our criteria for misophonia»; главная у авторов: no; период: NR; заметка: Criterion defined in General methods for Expts 1-2 ('umbrella criterion'); questionnaires completed vary across participants. Not a prevalence aim.
- E2: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met our criteria for misophonia»; главная у авторов: no; период: NR
- E3: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met our criteria for misophonia»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 68** — Expt 3A, Participants — «Sixty-eight participants (Mage = 22.42 years; range = 18–30 years; 35 females, 31 males, two non-binary) were tested»
- **population: other_nonclinical** — Common procedures — «Participants were compensated for their time with money or credit to fulfill a course requirement at CMU.»
- **sampling: convenience** — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- setting: university participant pool (Carnegie Mellon University) and online panel (Prolific); online experiment — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- data_years: 2022-2024 — General methods, Participant populations — «Participant recruitment began on 01/07/2022 and ended on 23/04/2024.»
- design: screening phase of experiment — General methods, Participant populations — «For the remaining experiments (i.e., Experiments 3, 4, 5), the participants were recruited irrespective of their misophonic severity. We refer to these partici…»
- topic_disclosed: no — General methods, Participant populations — «participant recruitment for all unscreened groups (Expts. 3–5) described the study as being about “judging properties of sounds and/or videos” and did not ment…»
- inclusion_exclusion: Normal hearing and corrected-to-normal vision required; recruited irrespective of misophonia status; excluded if failed headphone (Huggins pitch) screening or catch trial — Common procedures; Expt 3A Participants — «Normal hearing and corrected-to-normal vision were required.»
- n_invited: NR — NA — «NA»
- n_responded: 112 — Expt 3A, Participants — «Sixty-eight participants ... were tested (after excluding 44 participants for failing the headphone screening).»
- response_rate: NR — NA — «NA»
- age_mean: 22.42 — Expt 3A, Participants — «Mage = 22.42 years; range = 18–30 years»
- age_sd: NR — NA — «NA»
- age_min: 18 — Expt 3A, Participants — «range = 18–30 years»
- age_max: 30 — Expt 3A, Participants — «range = 18–30 years»
- age_group: adults — Expt 3A, Participants — «range = 18–30 years»
- pct_female: 51.5 — Expt 3A, Participants — «35 females, 31 males, two non-binary»
- informant: self — General methods, Participant populations — «all participants completed one or more of the following questionnaires that assessed misophonia severity»
- mode: online — Common procedures — «Prior to completing the experimental trials online using Qualtrics [37]»
- instruments: MisoQuest; MQ; DVMSQ; S-Five (one or more per participant; language version not stated, presumably English) — General methods, Participant populations — «all participants completed one or more of the following questionnaires that assessed misophonia severity: MisoQuest [31], Misophonia Questionnaire (MQ) [32], D…»
- instrument_validated_in_language: NR — General methods, Participant populations — «We followed the scoring guidelines for each questionnaire to determine misophonic severity for each individual.»
- pub_status: journal — Citation — «PloS one; DOI: 10.1371/journal.pone.0321594»
- language: English — Full text — «Reassigning sources of misophonic trigger sounds to change their unpleasantness»
- funding_coi: NR in text provided (IRB approval only) — Common procedures — «approved by Carnegie Mellon’s Institutional Review Board (IRB#2015_00000409)»
- notes: Possible overlap with R0368 (ST027), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. This is an experimental paper; misophonia screening was used only to classify participants. Which questionnaire(s) each participant completed is not reported. The authors' pooled statement over the unscreened Expts 3A, 4, 5A and 5B (N=154) is '11.69%, or 9.09%' clinical or subclinical; it is ambiguous (see consistency_notes). Population is coded other_nonclinical because the pool mixes CMU students (paid in course …

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is a university participant pool plus Prolific; covers only part of any general population — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
2. способ отбора: **no** — Convenience/volunteer opt-in recruitment — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
3. размер выборки: **no** — n=68 < 385 — Expt 3A, Participants — «Sixty-eight participants»
4. описание выборки и условий: **unclear** — Age, sex, setting and dates reported; country not explicitly stated — Expt 3A, Participants; General methods — «Participant recruitment began on 01/07/2022 and ended on 23/04/2024.»
5. охват (пропуски): **unclear** — 44 excluded before questionnaires for failing headphone screening; missing questionnaire data among analysed not reported — Expt 3A, Participants — «after excluding 44 participants for failing the headphone screening»
6. валидность определения случая: **no** — Primary definition is subclinical or clinical on any of four questionnaires (L1), not an anchored clinical cut-off — General methods, Participant populations — «The misophonic group included all participants who received a subclinical or clinical misophonia score on any of the questionnaires.»
7. единое надёжное измерение: **no** — Participants completed one or more of different questionnaires; no reliability reported — General methods, Participant populations — «all participants completed one or more of the following questionnaires»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator given (6/68); CI calculable — Expt 3A, Participants — «six individuals ... met our criteria for misophonia»
9. отклик: **no** — No denominator of invited people; participant pool/online panel opt-in — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

Правки:
- 

Проверено: да
### ST024-2 · Expt 3B unscreened, CMU pool/Prolific, n=17
Отчёты: R0314 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **1 / 17** | 5.9 | Expt 3B, Participants | «Only one individual met our criteria for misophonia in this unscreened group.» |

- E1: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met our criteria for misophonia»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 17** — Expt 3B, Participants — «A new set of seventeen participants were tested»
- **population: other_nonclinical** — Common procedures — «Participants were compensated for their time with money or credit to fulfill a course requirement at CMU.»
- **sampling: convenience** — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- setting: university participant pool (CMU) and online panel (Prolific); online experiment — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- data_years: 2022-2024 — General methods, Participant populations — «Participant recruitment began on 01/07/2022 and ended on 23/04/2024.»
- design: screening phase of experiment — Expt 3B, Participants — «A new set of seventeen participants were tested to replicate Experiment 3A»
- topic_disclosed: no — General methods, Participant populations — «participant recruitment for all unscreened groups (Expts. 3–5) described the study as being about “judging properties of sounds and/or videos” and did not ment…»
- inclusion_exclusion: Normal hearing and corrected-to-normal vision; recruited irrespective of misophonia status; excluded if failed headphone screening — Common procedures; Expt 3B Participants — «after excluding seven participants who did not pass the headphone screening»
- n_invited: NR — NA — «NA»
- n_responded: 24 — Expt 3B, Participants — «seventeen participants ... after excluding seven participants who did not pass the headphone screening»
- response_rate: NR — NA — «NA»
- age_mean: 19 — Expt 3B, Participants — «Mage = 19 years; range = 18–20 years»
- age_sd: NR — NA — «NA»
- age_min: 18 — Expt 3B, Participants — «range = 18–20 years»
- age_max: 20 — Expt 3B, Participants — «range = 18–20 years»
- age_group: adults — Expt 3B, Participants — «range = 18–20 years»
- pct_female: 58.8 — Expt 3B, Participants — «10 females, seven males»
- informant: self — General methods, Participant populations — «all participants completed one or more of the following questionnaires that assessed misophonia severity»
- mode: online — Common procedures — «Prior to completing the experimental trials online using Qualtrics [37]»
- instruments: MisoQuest; MQ; DVMSQ; S-Five (one or more per participant; language version not stated) — General methods, Participant populations — «MisoQuest [31], Misophonia Questionnaire (MQ) [32], Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) [33] and the S-Five [34].»
- instrument_validated_in_language: NR — General methods, Participant populations — «We followed the scoring guidelines for each questionnaire to determine misophonic severity for each individual.»
- pub_status: journal — Citation — «PloS one; DOI: 10.1371/journal.pone.0321594»
- language: English — Full text — «Experiment 3B: Alternative meaning of auditory-visual match»
- funding_coi: NR in text provided — Common procedures — «approved by Carnegie Mellon’s Institutional Review Board (IRB#2015_00000409)»
- notes: Possible overlap with R0368 (ST027), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Not included in the authors' pooled unscreened N=154. The sex of the one misophonic participant is not reported, so there are no sex subgroups.

**Риск смещения (JBI):**
1. рамка выборки: **no** — University participant pool plus Prolific — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
2. способ отбора: **no** — Convenience opt-in — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
3. размер выборки: **no** — n=17 — Expt 3B, Participants — «A new set of seventeen participants»
4. описание выборки и условий: **unclear** — Country not explicitly stated — Expt 3B, Participants — «Mage = 19 years; range = 18–20 years; 10 females, seven males»
5. охват (пропуски): **unclear** — Missing questionnaire data not reported — Expt 3B, Participants — «after excluding seven participants who did not pass the headphone screening»
6. валидность определения случая: **no** — L1 umbrella definition (subclinical or clinical on any questionnaire) — General methods, Participant populations — «The misophonic group included all participants who received a subclinical or clinical misophonia score on any of the questionnaires.»
7. единое надёжное измерение: **no** — Different questionnaires across participants; no reliability reported — General methods, Participant populations — «all participants completed one or more of the following questionnaires»
8. статистика (числитель и знаменатель): **yes** — 1/17 traceable — Expt 3B, Participants — «Only one individual met our criteria for misophonia»
9. отклик: **no** — No invited denominator — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

Правки:
- 

Проверено: да
### ST024-3 · Expt 3C unscreened (also Expt 5C), CMU pool/Prolific, n=32
Отчёты: R0314 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **6 / 32** | 18.8 | Expt 3C, Participants | «In this unscreened group that was recruited irrespective of misophonic status, there were six misophonic individuals (Mage = 21.83 years; range = 19–28 years; 4 females, 2 males).» |
| E2 | female | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **4 / 15** | 26.7 | Expt 3C, Participants | «15 females, 13 males, four non-binary ... six misophonic individuals (... 4 females, 2 males)» |
| E3 | male | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **2 / 13** | 15.4 | Expt 3C, Participants | «15 females, 13 males, four non-binary ... six misophonic individuals (... 4 females, 2 males)» |

- E1: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «misophonic individuals»; главная у авторов: no; период: NR; заметка: Subgroup demographics identical to Expt 3A; possible copy error.
- E2: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «misophonic individuals»; главная у авторов: no; период: NR
- E3: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «misophonic individuals»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 32** — Expt 3C, Participants — «A total of 32 participants (Mage = 21.88 years; range = 18–29 years; 15 females, 13 males, four non-binary) were tested.»
- **population: other_nonclinical** — Common procedures — «Participants were compensated for their time with money or credit to fulfill a course requirement at CMU.»
- **sampling: convenience** — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- setting: university participant pool (CMU) and online panel (Prolific); online experiment on Gorilla.sc — Expt 3C, Procedure — «The experimental platform was Gorilla.sc [40].»
- data_years: 2022-2024 — General methods, Participant populations — «Participant recruitment began on 01/07/2022 and ended on 23/04/2024.»
- design: screening phase of experiment — Expt 3C, Participants — «In this unscreened group that was recruited irrespective of misophonic status»
- topic_disclosed: no — General methods, Participant populations — «participant recruitment for all unscreened groups (Expts. 3–5) described the study as being about “judging properties of sounds and/or videos” and did not ment…»
- inclusion_exclusion: Recruited irrespective of misophonia status; normal hearing/vision required; exclusions for this experiment not reported — Expt 3C, Participants — «A total of 32 participants ... were tested.»
- n_invited: NR — NA — «NA»
- n_responded: NR — NA — «NA»
- response_rate: NR — NA — «NA»
- age_mean: 21.88 — Expt 3C, Participants — «Mage = 21.88 years; range = 18–29 years»
- age_sd: NR — NA — «NA»
- age_min: 18 — Expt 3C, Participants — «range = 18–29 years»
- age_max: 29 — Expt 3C, Participants — «range = 18–29 years»
- age_group: adults — Expt 3C, Participants — «range = 18–29 years»
- pct_female: 46.9 — Expt 3C, Participants — «15 females, 13 males, four non-binary»
- informant: self — General methods, Participant populations — «all participants completed one or more of the following questionnaires that assessed misophonia severity»
- mode: online — Expt 3C, Procedure — «The experimental platform was Gorilla.sc [40].»
- instruments: MisoQuest; MQ; DVMSQ; S-Five (one or more per participant; language version not stated) — General methods, Participant populations — «MisoQuest [31], Misophonia Questionnaire (MQ) [32], Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) [33] and the S-Five [34].»
- instrument_validated_in_language: NR — General methods, Participant populations — «We followed the scoring guidelines for each questionnaire to determine misophonic severity for each individual.»
- pub_status: journal — Citation — «PloS one; DOI: 10.1371/journal.pone.0321594»
- language: English — Full text — «Experiment 3C: Cross-modal agreement in Experiment 3A»
- funding_coi: NR in text provided — Common procedures — «approved by Carnegie Mellon’s Institutional Review Board (IRB#2015_00000409)»
- notes: Possible overlap with R0368 (ST027), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Expt 5C used the same 32 participants, so it is not a separate sample. Not included in the authors' pooled N=154. The misophonic subgroup is described exactly as in Expt 3A (Mage 21.83, range 19-28, 4 F, 2 M), which may be a copy error; please check.

**Риск смещения (JBI):**
1. рамка выборки: **no** — University participant pool plus Prolific — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
2. способ отбора: **no** — Convenience opt-in — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
3. размер выборки: **no** — n=32 — Expt 3C, Participants — «A total of 32 participants»
4. описание выборки и условий: **unclear** — Country not explicitly stated — Expt 3C, Participants — «Mage = 21.88 years; range = 18–29 years; 15 females, 13 males, four non-binary»
5. охват (пропуски): **unclear** — Missing data/exclusions not reported — Expt 3C, Participants — «A total of 32 participants ... were tested.»
6. валидность определения случая: **no** — L1 umbrella definition — General methods, Participant populations — «The misophonic group included all participants who received a subclinical or clinical misophonia score on any of the questionnaires.»
7. единое надёжное измерение: **no** — Different questionnaires across participants; no reliability reported — General methods, Participant populations — «all participants completed one or more of the following questionnaires»
8. статистика (числитель и знаменатель): **yes** — 6/32 traceable — Expt 3C, Participants — «there were six misophonic individuals»
9. отклик: **no** — No invited denominator — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

Правки:
- 

Проверено: да
### ST024-4 · Expt 4 unscreened, CMU pool/Prolific, n=32
Отчёты: R0314 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **11 / 32** | 34.4 | Expt 4, Participants | «In this unscreened group, 11 participants (Mage = 25.18 years; range = 18–29 years; five females, six males) met the criteria for misophonia.» |
| E2 | female | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **5 / 12** | 41.7 | Expt 4, Participants | «12 females, 20 males ... 11 participants (... five females, six males) met the criteria for misophonia» |
| E3 | male | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **6 / 20** | 30.0 | Expt 4, Participants | «12 females, 20 males ... 11 participants (... five females, six males) met the criteria for misophonia» |

- E1: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met the criteria for misophonia»; главная у авторов: no; период: NR
- E2: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met the criteria for misophonia»; главная у авторов: no; период: NR
- E3: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met the criteria for misophonia»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 32** — Expt 4, Participants — «Thirty-two participants (Mage = 24.40 years; range = 18–30 years; 12 females, 20 males) were tested»
- **population: other_nonclinical** — Common procedures — «Participants were compensated for their time with money or credit to fulfill a course requirement at CMU.»
- **sampling: convenience** — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- setting: university participant pool (CMU) and online panel (Prolific); online experiment — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- data_years: 2022-2024 — General methods, Participant populations — «Participant recruitment began on 01/07/2022 and ended on 23/04/2024.»
- design: screening phase of experiment — Expt 4, Participants — «In this unscreened group, 11 participants ... met the criteria for misophonia.»
- topic_disclosed: no — General methods, Participant populations — «participant recruitment for all unscreened groups (Expts. 3–5) described the study as being about “judging properties of sounds and/or videos” and did not ment…»
- inclusion_exclusion: Normal hearing/vision; recruited irrespective of misophonia; excluded if failed headphone screening — Expt 4, Participants — «after excluding 13 participants for failing headphone screening»
- n_invited: NR — NA — «NA»
- n_responded: 45 — Expt 4, Participants — «Thirty-two participants ... were tested (after excluding 13 participants for failing headphone screening).»
- response_rate: NR — NA — «NA»
- age_mean: 24.40 — Expt 4, Participants — «Mage = 24.40 years; range = 18–30 years»
- age_sd: NR — NA — «NA»
- age_min: 18 — Expt 4, Participants — «range = 18–30 years»
- age_max: 30 — Expt 4, Participants — «range = 18–30 years»
- age_group: adults — Expt 4, Participants — «range = 18–30 years»
- pct_female: 37.5 — Expt 4, Participants — «12 females, 20 males»
- informant: self — General methods, Participant populations — «all participants completed one or more of the following questionnaires that assessed misophonia severity»
- mode: online — Common procedures — «Prior to completing the experimental trials online using Qualtrics [37]»
- instruments: MisoQuest; MQ; DVMSQ; S-Five (one or more per participant; language version not stated) — General methods, Participant populations — «MisoQuest [31], Misophonia Questionnaire (MQ) [32], Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) [33] and the S-Five [34].»
- instrument_validated_in_language: NR — General methods, Participant populations — «We followed the scoring guidelines for each questionnaire to determine misophonic severity for each individual.»
- pub_status: journal — Citation — «PloS one; DOI: 10.1371/journal.pone.0321594»
- language: English — Full text — «Experiment 4: The role of sound misidentification in the effectiveness of neutral visual sources»
- funding_coi: NR in text provided — Common procedures — «approved by Carnegie Mellon’s Institutional Review Board (IRB#2015_00000409)»
- notes: Possible overlap with R0368 (ST027), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Part of the authors' pooled unscreened N=154 (Expts 3A, 4, 5A, 5B), for which they report 11.69% and 9.09% clinical or subclinical; the meaning is ambiguous (see consistency_notes).

**Риск смещения (JBI):**
1. рамка выборки: **no** — University participant pool plus Prolific — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
2. способ отбора: **no** — Convenience opt-in — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
3. размер выборки: **no** — n=32 — Expt 4, Participants — «Thirty-two participants»
4. описание выборки и условий: **unclear** — Country not explicitly stated — Expt 4, Participants — «Mage = 24.40 years; range = 18–30 years; 12 females, 20 males»
5. охват (пропуски): **unclear** — Missing questionnaire data not reported — Expt 4, Participants — «after excluding 13 participants for failing headphone screening»
6. валидность определения случая: **no** — L1 umbrella definition — General methods, Participant populations — «The misophonic group included all participants who received a subclinical or clinical misophonia score on any of the questionnaires.»
7. единое надёжное измерение: **no** — Different questionnaires across participants; no reliability reported — General methods, Participant populations — «all participants completed one or more of the following questionnaires»
8. статистика (числитель и знаменатель): **yes** — 11/32 traceable — Expt 4, Participants — «11 participants ... met the criteria for misophonia»
9. отклик: **no** — No invited denominator — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

Правки:
- 

Проверено: да
### ST024-5 · Expt 5A unscreened, CMU pool/Prolific, n=20
Отчёты: R0314 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **4 / 20** | 20.0 | Expt 5A, Participants | «In this unscreened group, four participants (Mage = 20 years; range = 18–22 years; 3 females, 1 male) met the criteria for misophonia.» |
| E2 | female | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **3 / 17** | 17.6 | Expt 5A, Participants | «17 females, two males, one non-binary ... four participants (... 3 females, 1 male) met the criteria for misophonia» |
| E3 | male | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **1 / 2** | 50.0 | Expt 5A, Participants | «17 females, two males, one non-binary ... four participants (... 3 females, 1 male) met the criteria for misophonia» |

- E1: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met the criteria for misophonia»; главная у авторов: no; период: NR
- E2: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met the criteria for misophonia»; главная у авторов: no; период: NR
- E3: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «met the criteria for misophonia»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 20** — Expt 5A, Participants — «Twenty participants (Mage = 19.76 years; range = 18–22 years; 17 females, two males, one non-binary)»
- **population: other_nonclinical** — Common procedures — «Participants were compensated for their time with money or credit to fulfill a course requirement at CMU.»
- **sampling: convenience** — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- setting: university participant pool (CMU) and online panel (Prolific); online experiment — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- data_years: 2022-2024 — General methods, Participant populations — «Participant recruitment began on 01/07/2022 and ended on 23/04/2024.»
- design: screening phase of experiment — Expt 5A, Participants — «were tested irrespective of misophonic status»
- topic_disclosed: no — General methods, Participant populations — «participant recruitment for all unscreened groups (Expts. 3–5) described the study as being about “judging properties of sounds and/or videos” and did not ment…»
- inclusion_exclusion: Normal hearing/vision; irrespective of misophonia; excluded if failed headphone screening — Expt 5A, Participants — «after excluding five participants for failing the headphone screening»
- n_invited: NR — NA — «NA»
- n_responded: 25 — Expt 5A, Participants — «Twenty participants ... were tested irrespective of misophonic status (after excluding five participants for failing the headphone screening).»
- response_rate: NR — NA — «NA»
- age_mean: 19.76 — Expt 5A, Participants — «Mage = 19.76 years; range = 18–22 years»
- age_sd: NR — NA — «NA»
- age_min: 18 — Expt 5A, Participants — «range = 18–22 years»
- age_max: 22 — Expt 5A, Participants — «range = 18–22 years»
- age_group: adults — Expt 5A, Participants — «range = 18–22 years»
- pct_female: 85 — Expt 5A, Participants — «17 females, two males, one non-binary»
- informant: self — General methods, Participant populations — «all participants completed one or more of the following questionnaires that assessed misophonia severity»
- mode: online — Expt 5A, Procedure — «survey via Qualtrics, volume calibration, headphone screening, and catch trials»
- instruments: MisoQuest; MQ; DVMSQ; S-Five (one or more per participant; language version not stated) — General methods, Participant populations — «MisoQuest [31], Misophonia Questionnaire (MQ) [32], Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) [33] and the S-Five [34].»
- instrument_validated_in_language: NR — General methods, Participant populations — «We followed the scoring guidelines for each questionnaire to determine misophonic severity for each individual.»
- pub_status: journal — Citation — «PloS one; DOI: 10.1371/journal.pone.0321594»
- language: English — Full text — «Experiment 5A: Altering the pleasantness ratings of sounds with meaningless visual stimuli»
- funding_coi: NR in text provided — Common procedures — «approved by Carnegie Mellon’s Institutional Review Board (IRB#2015_00000409)»
- notes: Possible overlap with R0368 (ST027), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Part of the authors' pooled unscreened N=154 (see consistency_notes).

**Риск смещения (JBI):**
1. рамка выборки: **no** — University participant pool plus Prolific — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
2. способ отбора: **no** — Convenience opt-in — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
3. размер выборки: **no** — n=20 — Expt 5A, Participants — «Twenty participants»
4. описание выборки и условий: **unclear** — Country not explicitly stated — Expt 5A, Participants — «Mage = 19.76 years; range = 18–22 years; 17 females, two males, one non-binary»
5. охват (пропуски): **unclear** — Missing questionnaire data not reported — Expt 5A, Participants — «after excluding five participants for failing the headphone screening»
6. валидность определения случая: **no** — L1 umbrella definition — General methods, Participant populations — «The misophonic group included all participants who received a subclinical or clinical misophonia score on any of the questionnaires.»
7. единое надёжное измерение: **no** — Different questionnaires across participants; no reliability reported — General methods, Participant populations — «all participants completed one or more of the following questionnaires»
8. статистика (числитель и знаменатель): **yes** — 4/20 traceable — Expt 5A, Participants — «four participants ... met the criteria for misophonia»
9. отклик: **no** — No invited denominator — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

Правки:
- 

Проверено: да
### ST024-6 · Expt 5B unscreened, CMU pool/Prolific, n=34
Отчёты: R0314 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **5 / 34** | 14.7 | Expt 5B, Participants | «In this unscreened group, there were five misophonics (Mage = 19.40 years; range = 18–20 years; 4 females, 1 male).» |
| E2 | female | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **4 / 23** | 17.4 | Expt 5B, Participants | «23 females, 11 males ... five misophonics (... 4 females, 1 male)» |
| E3 | male | multiple · subclinical or clinical score on any of MisoQuest, MQ, DVMSQ, S-Five | **L1** | **1 / 11** | 9.1 | Expt 5B, Participants | «23 females, 11 males ... five misophonics (... 4 females, 1 male)» |

- E1: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «misophonics»; главная у авторов: no; период: NR
- E2: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «misophonics»; главная у авторов: no; период: NR
- E3: источник порога: developer paper; правило: G4 'A or B' -> L1; у авторов: «misophonics»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 34** — Expt 5B, Participants — «Thirty-four participants (Mage = 19.70 years; range = 18–31 years; 23 females, 11 males)»
- **population: other_nonclinical** — Common procedures — «Participants were compensated for their time with money or credit to fulfill a course requirement at CMU.»
- **sampling: convenience** — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- setting: university participant pool (CMU) and online panel (Prolific); online experiment — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
- data_years: 2022-2024 — General methods, Participant populations — «Participant recruitment began on 01/07/2022 and ended on 23/04/2024.»
- design: screening phase of experiment — Expt 5B, Participants — «participated irrespective of misophonia status»
- topic_disclosed: no — General methods, Participant populations — «participant recruitment for all unscreened groups (Expts. 3–5) described the study as being about “judging properties of sounds and/or videos” and did not ment…»
- inclusion_exclusion: Normal hearing/vision; irrespective of misophonia; excluded if failed headphone screening — Expt 5B, Participants — «after excluding 9 participants for failing the headphone screening»
- n_invited: NR — NA — «NA»
- n_responded: 43 — Expt 5B, Participants — «Thirty-four participants ... participated irrespective of misophonia status (after excluding 9 participants for failing the headphone screening).»
- response_rate: NR — NA — «NA»
- age_mean: 19.70 — Expt 5B, Participants — «Mage = 19.70 years; range = 18–31 years»
- age_sd: NR — NA — «NA»
- age_min: 18 — Expt 5B, Participants — «range = 18–31 years»
- age_max: 31 — Expt 5B, Participants — «range = 18–31 years»
- age_group: adults — Expt 5B, Participants — «range = 18–31 years»
- pct_female: 67.6 — Expt 5B, Participants — «23 females, 11 males»
- informant: self — General methods, Participant populations — «all participants completed one or more of the following questionnaires that assessed misophonia severity»
- mode: online — Expt 5B, Procedure — «The procedure was identical to Part Two of Experiment 5A»
- instruments: MisoQuest; MQ; DVMSQ; S-Five (one or more per participant; language version not stated) — General methods, Participant populations — «MisoQuest [31], Misophonia Questionnaire (MQ) [32], Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) [33] and the S-Five [34].»
- instrument_validated_in_language: NR — General methods, Participant populations — «We followed the scoring guidelines for each questionnaire to determine misophonic severity for each individual.»
- pub_status: journal — Citation — «PloS one; DOI: 10.1371/journal.pone.0321594»
- language: English — Full text — «Experiment 5B: Altering the pleasantness of an unpleasant sound with concurrent presentation of a neutral visual source»
- funding_coi: NR in text provided — Common procedures — «approved by Carnegie Mellon’s Institutional Review Board (IRB#2015_00000409)»
- notes: Possible overlap with R0368 (ST027), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Part of the authors' pooled unscreened N=154 (see consistency_notes).

**Риск смещения (JBI):**
1. рамка выборки: **no** — University participant pool plus Prolific — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
2. способ отбора: **no** — Convenience opt-in — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»
3. размер выборки: **no** — n=34 — Expt 5B, Participants — «Thirty-four participants»
4. описание выборки и условий: **unclear** — Country not explicitly stated — Expt 5B, Participants — «Mage = 19.70 years; range = 18–31 years; 23 females, 11 males»
5. охват (пропуски): **unclear** — Missing questionnaire data not reported — Expt 5B, Participants — «after excluding 9 participants for failing the headphone screening»
6. валидность определения случая: **no** — L1 umbrella definition — General methods, Participant populations — «The misophonic group included all participants who received a subclinical or clinical misophonia score on any of the questionnaires.»
7. единое надёжное измерение: **no** — Different questionnaires across participants; no reliability reported — General methods, Participant populations — «all participants completed one or more of the following questionnaires»
8. статистика (числитель и знаменатель): **yes** — 5/34 traceable — Expt 5B, Participants — «there were five misophonics»
9. отклик: **no** — No invited denominator — General methods, Participant populations — «We recruited participants online through Carnegie Mellon University system and through Prolific [30].»

Правки:
- 

Проверено: да
---

## ST025 · Itoi 2025 · Journal of psychiatric research

Основной отчёт R0323: [текст](../../fulltext/text/R0323.txt) · [PDF](../../fulltext/pdf/R0323.pdf) — «Reliability and validity of the Japanese version of the Misophonia Questionnaire (MQ).» — [DOI](https://doi.org/10.1016/j.jpsychires.2025.05.040)
Не выписано ИИ: Misophonia group (n=64 recruited, 63 analysed): self-identified people with misophonic symptoms, recruited from the community by snowball sampling with help from the Japan Misophonia Association. Excluded because they were recruited for misophonia (E1). Their MSS>=7 rate (58/63, 92%) is not extracted.
Расхождения в тексте: The reported control prevalence (103, 23%) does not match the analysed control n of 387 (103/387 = 26.6%). It matches 103/448, where 448 is the Table 1 N for all analysed participants: Table 4 rows sum to 386 controls + 62 misophonia = 448, while the text says 63 + 387 = 450. I used n = 387 as printed for the analysed controls and flagged the discrepancy. The introduction gives the MSS threshold as '>7', but Methods and Results use '≥7'; I used ≥7. Age, SD and sex are given for the 500 recruited controls, not the 387 analysed. Excluded ill subgroup: 25/63 = 39.7% vs 39.6% printed.
Заметка ИИ: There is one eligible sample: the online-panel control group. The main estimate is MQ-J Severity ≥7 (L2). It needs reviewer checking because the denominator is ambiguous (387 vs 386 vs 448). The sex-matched panel (90% female) limits representativeness.

### ST025-1 · Control group, iBRIDGE online research panel, Japan, n=387 analysed
Отчёты: R0323 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | MQ · MSS>=7 | **L2** | **103 / 387** | 26.6 | Page 5, Results 3.5 (end); Discussion 4.1 | «Based on this criterion, 58 (92 %) misophonic and 103 (23 %) control participants were classified as having significant misophonia symptoms.» |
| E2 | physical or mental illness (excluded from main analysis) | MQ · MSS>=7 | **L2** | **25 / 63** | 39.7 | Page 5, Results 3.5 (end) | «Incidentally, of the 63 control group participants with physical or mental illnesses who were excluded, 25 (39.6 %) scored 7 or higher.» |

- E1: источник порога: developer paper; правило: MQ row; MSS >=7 (L2 recommended); у авторов: «clinically significant misophonia symptoms»; главная у авторов: yes; период: NR; заметка: Denominator unclear. 103/387 = 26.6%, but the reported 23% matches 103/448 (all analysed, including the misophonia group; Table 1 N = 448). Table 4 control item rows sum to 386. The authors report 23% as the Japanese prevalence.
- E2: источник порога: developer paper; правило: MQ row; MSS >=7; у авторов: «scored 7 or higher»; главная у авторов: no; период: NR; заметка: Recruited panel members with self-reported physical or mental illness who were excluded from the main analysis; the type of illness is not specified. 25/63 = 39.7% (reported as 39.6%).

**Ключевые поля выборки:**
- **n_analysed: 387** — Page 2, 2.1 Participants — «Data from 63 misophonia and 387 control participants were analyzed.»
- **population: gp_other** — Page 2, 2.1 Participants — «500 control participants via an Internet research service (iBRIDGE Co., Tokyo, Japan)»
- **sampling: quota** — Page 2, 2.1 Participants — «We matched the gender ratio between participants with misophonia and control participants.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: JPN — Page 2, 2.1 Participants — «500 control participants via an Internet research service (iBRIDGE Co., Tokyo, Japan)»
- setting: online panel (Internet research service iBRIDGE) — Page 2, 2.1 Participants — «500 control participants via an Internet research service (iBRIDGE Co., Tokyo, Japan)»
- data_years: NR — NR — «NR»
- design: validation study — Abstract, Page 1 — «This study aimed to develop a Japanese version of the Misophonia Questionnaire (MQ-J) and examine its psychometric properties.»
- topic_disclosed: NR — Page 3, 2.10 Procedure — «Participants were informed that (1) the survey would take about 30 min, and (2) participation was completely voluntary»
- inclusion_exclusion: Excluded: mental or physical disease; non-response to multiple items or multiple responses to same item; failed attention check (colour-name check). 113 of 500 excluded. — Page 2, 2.1 Participants — «Exclusion criteria were those who had a mental or physical disease, did not respond to multiple items or provided multiple responses for the same item, or were…»
- n_invited: NR — NR — «NR»
- n_responded: 500 — Page 2, 2.1 Participants — «The control group comprised 500 participants (n = 500)»
- response_rate: NR — NR — «NR»
- age_mean: 28.2 — Page 2, 2.1 Participants — «The mean age in the control group was 28.2 years (SD = 0.30).»
- age_sd: 0.30 — Page 2, 2.1 Participants — «The mean age in the control group was 28.2 years (SD = 0.30).»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- age_group: adults — Page 5, 4. Discussion — «we compared the MQ-J scores between adults with and without misophonia symptoms»
- pct_female: 90 — Page 2, 2.1 Participants — «with 10 % (n = 50) identifying as male and 90 % (n = 450) as female»
- informant: self — Abstract, Page 1 — «The Misophonia Questionnaire (MQ) is a self-report measure designed to assess misophonia symptoms.»
- mode: online — Page 3, 2.10 Procedure — «All questionnaire data were obtained online from participants with misophonia and control participants.»
- instruments: Misophonia Questionnaire, Japanese version (MQ-J; Symptom Scale, Emotions and Behaviors Scale, Misophonia Severity Scale) — Page 2, 2.2 Measures — «We translated the MQ into Japanese with approval from the corresponding author in the original study (Wu et al., 2014).»
- instrument_validated_in_language: yes — Abstract, Page 1 — «These findings supported the validity and reliability of the MQ-J.»
- pub_status: journal — Page 1, header — «Journal of Psychiatric Research 188 (2025) 133–139»
- language: English — Page 1 — «Reliability and validity of the Japanese version of the Misophonia Questionnaire (MQ)»
- funding_coi: JSPS KAKENHI JP24K16882 and JP25K00887; no competing interests declared — Page 6, Funding; Declaration of competing interest — «This work was supported by JSPS KAKENHI Grant Numbers JP24K16882 and JP25K00887. ... We have no competing interests to declare.»
- notes: This report is itself the MQ-J validation study (the only Japanese validation; Tada et al. 2022 used the MQ in Japan without validating it). Age mean, SD and % female refer to all 500 recruited controls, not the 387 analysed; the 'SD' of 0.30 looks like an SE. The 113 exclusions include 63 participants with physical or mental illness, so the remaining ~50 were data-quality exclusions (inferred). The panel was sex-matched to the misophonia group (90% female), so it is far from representative. The authors interpret 23% as the 'prevalence rate of misophonia in the Japanese population'. Data-coll…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The authors describe the result as Japanese population prevalence, but the frame is a commercial internet research panel matched to a 90% female sex ratio. — Page 2, 2.1; Page 5, 4.2 — «500 control participants via an Internet research service (iBRIDGE Co., Tokyo, Japan)»
2. способ отбора: **no** — Non-probability online panel, with sex matched to the misophonia group. — Page 2, 2.1 Participants — «We matched the gender ratio between participants with misophonia and control participants.»
3. размер выборки: **yes** — 387 analysed, which is at least 385. — Page 2, 2.1 Participants — «Data from 63 misophonia and 387 control participants were analyzed.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; data-collection dates are not. — Page 2, 2.1 Participants — «The mean age in the control group was 28.2 years (SD = 0.30).»
5. охват (пропуски): **unclear** — 113 of 500 (22.6%) excluded, including 63 for illness. The split of the remaining data-quality exclusions is not given, and Table 4 control rows sum to 386, not 387. — Page 2, 2.1; Page 5; Table 4 — «Therefore, of the 500 control participants, 113 were excluded.»
6. валидность определения случая: **yes** — MQ Severity Scale >=7 in the Japanese version, validated in this report. — Page 2, 2.3 MQ — «A score of ≥7 points indicated clinically significant symptoms, according to Wu et al.’s criteria (2014).»
7. единое надёжное измерение: **yes** — Same online MQ-J and threshold for all participants; Cronbach's alpha reported in the sample. — Page 3, 3.2 Internal consistency — «Cronbach’s alpha for the Total Scale score was .93»
8. статистика (числитель и знаменатель): **no** — The reported 23% does not match 103/387 (26.6%); it matches 103/448 (the combined sample). No CI is given. — Page 5 — «58 (92 %) misophonic and 103 (23 %) control participants were classified as having significant misophonia symptoms.»
9. отклик: **no** — Online panel with no number of people invited and no non-response handling. — Page 2, 2.1 Participants — «500 control participants via an Internet research service»

Правки:
- 

Проверено: да
---

## ST026 · Manning 2025 · PloS one

Основной отчёт R0350: [текст](../../fulltext/text/R0350.txt) — «Decreased sound tolerance in a Canadian University Context: Associations with autistic traits, social competence, and gender in an undergraduate sample.» — [DOI](https://doi.org/10.1371/journal.pone.0334689)
Приложен R0349: [текст](../../fulltext/text/R0349.txt) · [PDF](../../fulltext/pdf/R0349.pdf) — «Decreased sound tolerance in a Canadian University Context: Associations with autistic traits, social competence, and g…»
Приложен R0197: [текст](../../fulltext/text/R0197.txt) · [PDF](../../fulltext/pdf/R0197.pdf) — «Anxiety and depression among Canadian undergraduates with decreased sound tolerance.»
Приложен R0437: [текст](../../fulltext/text/R0437.txt) — «Social success in a noisy world: exploring the relationship between decreased sound tolerance and social profiles.»
Связь отчётов: Wilfrid Laurier University undergraduate survey 2023-24 (N about 2,080-2,095): PsyArXiv preprint R0349 and PLoS ONE article R0350; R0197 and R0437 analyse the same survey and cite it
Расхождения в тексте: Inside the main report: (1) MQ denominator. Table 2 gives MQ Severity n=1025, but the text says 1033, and the gender ns in Table 2 add up to 1033. I used 1025 under the table rule. The MQ gender cases (114+20+6=140) are more than the 128 overall. (2) Non-cisgender percentages: 61% for DMQ, 58% for DVMSQ, 47% for IHS and 42% for AQ all imply a denominator of 38, not the 45 in Table 1. (3) The 'at least one of MQ, DMQ, DVMSQ' union (310) is smaller than the DMQ count alone (374), which is impossible. (4) Table 2 gives DMQ F statistics (95.38, 112.82) that differ from the text (78.2, 88.9). (5) The DMQ threshold is given only as '39 or greater', with no subscale named. Attached reports: R0349 (preprint) gives data collection as October 2023-April 2024; the main report says November 2023 and R0197 says September 2023. All counts in R0349 are the same as in the main report. R0197 gives final…
Заметка ИИ: There is one sample. I chose DVMSQ clinical (272/2080) as the primary estimate because the authors call the DVMSQ the measure that reflects the consensus definition. A reviewer should check three things: the DMQ case definition and its level, the MQ denominator (1025 vs 1033), and the impossible union count (310).

### ST026-1 · Wilfrid Laurier University undergraduates, Canada, n=2080
Отчёты: R0350 (main); R0349 (preprint of same paper); R0197; R0437

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DVMSQ · DVMSQ algorithm: clinical misophonia | **L2** | **272 / 2080** | 13.1 | Results, Misophonia; Discussion | «The DVMSQ detected clinical misophonia in 13% (n = 272) of the sample.» |
| E2 | all | DVMSQ · DVMSQ algorithm: subclinical or clinical misophonia | **L1** | **559 / 2080** | 26.9 | Results, Misophonia; Discussion | «14% of the sample (n = 287) were suggested to have sub-clinical misophonia. ... 13% (n = 272) of the sample» |
| E3 | female | DVMSQ · DVMSQ algorithm: clinical misophonia | **L2** | **230 / 1600** | 14.4 | Results, Misophonia | «14% of women (n = 230), 4% of men (n = 18), and 58% (n = 22) of non-cisgendered participants met criteria for clinical misophonia.» |
| E4 | male | DVMSQ · DVMSQ algorithm: clinical misophonia | **L2** | **18 / 435** | 4.1 | Results, Misophonia | «14% of women (n = 230), 4% of men (n = 18), and 58% (n = 22) of non-cisgendered participants met criteria for clinical misophonia.» |
| E5 | non-cisgender | DVMSQ · DVMSQ algorithm: clinical misophonia | **L2** | **22 / 45** | 48.9 | Results, Misophonia; Table 1 | «58% (n = 22) of non-cisgendered participants met criteria for clinical misophonia.» |
| E6 | all | MQ · MSS>=7 and Emotions-and-Behaviors mean>=2 | **L2** | **128 / 1025** | 12.5 | Results, Misophonia; Table 2; Data integrity check | «For the MQ, 12% (n = 128) of the sample met the clinical cut-off for misophonia.» |
| E7 | female | MQ · MSS>=7 and Emotions-and-Behaviors mean>=2 | **L2** | **114 / 805** | 14.2 | Results, Misophonia; Table 2 | «with 14% (n = 114) of women meeting cut-off» |
| E8 | male | MQ · MSS>=7 and Emotions-and-Behaviors mean>=2 | **L2** | **20 / 200** | 10.0 | Results, Misophonia; Table 2 | «while 10% (n = 20) of men» |
| E9 | non-cisgender | MQ · MSS>=7 and Emotions-and-Behaviors mean>=2 | **L2** | **6 / 28** | 21.4 | Results, Misophonia; Table 2 | «and 25% (n = 6) of those with non-cisgender expression met the cut-off» |
| E10 | all | DMQ · DMQ score >=39 as stated by authors (subscale not named; companion reports R0197/R0437 state Symptom Severity mean >=1.8 / total >=41.4) | **L2** | **374 / 2080** | 18.0 | Results, Misophonia; Methods, DMQ | «For the DMQ, misophonia was reported in 18% (n = 374) of the sample.» |
| E11 | female | DMQ · DMQ score >=39 as stated by authors | **L2** | **328 / 1600** | 20.5 | Results, Misophonia | «Prevalence according to DMQ was 21% (n = 328) among women, 6% (n = 24) among men, and 61% (n = 23) among non-cisgendered participants.» |
| E12 | male | DMQ · DMQ score >=39 as stated by authors | **L2** | **24 / 435** | 5.5 | Results, Misophonia | «Prevalence according to DMQ was 21% (n = 328) among women, 6% (n = 24) among men» |
| E13 | non-cisgender | DMQ · DMQ score >=39 as stated by authors | **L2** | **23 / 45** | 51.1 | Results, Misophonia; Table 1 | «and 61% (n = 23) among non-cisgendered participants» |
| E14 | all | multiple · clinical on at least one of MQ (MSS>=7 and E&B mean>=2), DMQ (>=39) or DVMSQ (clinical algorithm) | **L2** | **310 / 2080** | 14.9 | Results, Comorbid misophonia and hyperacusis | «we found that 15% (n = 310) of the participants had clinically significant misophonia according to at least one of the MQ, DMQ, or DVMSQ.» |
| E15 | all | multiple · clinical misophonia (any measure) or hyperacusis (IHS) | **E2** | **374 / 2080** | 18.0 | Results, Comorbid misophonia and hyperacusis | «Participants who met criteria for either misophonia or hyperacusis made up 18% (n = 374)» |

- E1: источник порога: developer paper; правило: DVMSQ row; L2 clinical (algorithm); у авторов: «clinical misophonia»; главная у авторов: yes; период: NR; заметка: Authors present the DVMSQ as reflecting the consensus definition ('highly advantageous'). R0197 (n=2095) reports DVMSQ clinical n=165 (8%) for the same survey.
- E2: источник порога: developer paper; правило: DVMSQ row; L1 subclinical or clinical; G1 sum of bands; у авторов: «sub-clinical + clinical misophonia ('approximately 27%')»; главная у авторов: no; период: NR; **расчёт: 272 clinical + 287 subclinical = 559; 559/2080 = 26.9%**; заметка: Authors state 'approximately 27% of post-secondary students are experiencing distress'.
- E3: источник порога: developer paper; правило: DVMSQ row; L2 clinical (algorithm); у авторов: «clinical misophonia»; главная у авторов: no; период: NR; заметка: Denominator from Table 1/Table 2 (1600 female); 230/1600 = 14.4%.
- E4: источник порога: developer paper; правило: DVMSQ row; L2 clinical (algorithm); у авторов: «clinical misophonia»; главная у авторов: no; период: NR; заметка: Denominator from Table 1 (435 male); 18/435 = 4.1%.
- E5: источник порога: developer paper; правило: DVMSQ row; L2 clinical (algorithm); у авторов: «clinical misophonia»; главная у авторов: no; период: NR; заметка: Table 1 gives 45 non-cisgendered; 22/45 = 49%, while reported 58% implies a denominator of 38. Subgroup sum 230+18+22 = 270 vs 272 overall.
- E6: источник порога: validation paper; правило: MQ row; L2 MSS>=7 and E&B mean>=2 (Rosenthal 2021); у авторов: «clinical cut-off for misophonia»; главная у авторов: no; период: NR; заметка: Denominator unclear: Table 2 gives MQ Severity n = 1025 (used per table rule); text says severity data collected from 1033 (Table 2 gender ns 805+200+28 = 1033; r(1031)). 128/1025 = 12.5%; 128/1033 = 12.4%. MQ severity missing for ~half the sample due to a Qualtrics error.
- E7: источник порога: validation paper; правило: MQ row; L2 MSS>=7 and E&B mean>=2; у авторов: «met cut-off»; главная у авторов: no; период: NR; заметка: Denominator = Table 2 MQ Severity female n (805); 114/805 = 14.2%.
- E8: источник порога: validation paper; правило: MQ row; L2 MSS>=7 and E&B mean>=2; у авторов: «met cut-off»; главная у авторов: no; период: NR; заметка: Denominator = Table 2 MQ Severity male n (200).
- E9: источник порога: validation paper; правило: MQ row; L2 MSS>=7 and E&B mean>=2; у авторов: «met cut-off»; главная у авторов: no; период: NR; заметка: Table 2 n = 28 (6/28 = 21%); reported 25% implies 24. Subgroup cases 114+20+6 = 140 exceed overall 128.
- E10: источник порога: developer paper; правило: DMQ row; L2 (Impairment >=39 severe or Symptom Severity >=1.8); reviewer to verify; у авторов: «misophonia ('severe symptomology')»; главная у авторов: no; период: NR; заметка: Methods: 'Scores on each subscale are summed for a total score, and a cut-off of 39 or greater indicates severe symptomology'. Exact scale ambiguous; level L2 under either Impairment>=39 or SS>=1.8 reading, but if SS total>=39 (mean 1.70) it would be below the L2 cut-off. R0437 reports 378/2095 wit…
- E11: источник порога: developer paper; правило: DMQ row; L2; reviewer to verify; у авторов: «misophonia»; главная у авторов: no; период: NR; заметка: 328/1600 = 20.5%.
- E12: источник порога: developer paper; правило: DMQ row; L2; reviewer to verify; у авторов: «misophonia»; главная у авторов: no; период: NR; заметка: 24/435 = 5.5%.
- E13: источник порога: developer paper; правило: DMQ row; L2; reviewer to verify; у авторов: «misophonia»; главная у авторов: no; период: NR; заметка: 23/45 = 51%; reported 61% implies denominator 38. Subgroup sum 328+24+23 = 375 vs 374 overall.
- E14: источник порога: study's own; правило: G4 'A or B' takes lower level; all components L2; у авторов: «clinically significant misophonia according to at least one of the MQ, DMQ, or …»; главная у авторов: no; период: NR; заметка: Internally inconsistent: union (310) is smaller than DMQ alone (374); MQ available for only ~half the sample. Reviewer to check.
- E15: источник порога: study's own; правило: G9 not misophonia-specific (merges misophonia with hyperacusis); у авторов: «met criteria for either misophonia or hyperacusis»; главная у авторов: no; период: NR; заметка: Listed, not pooled. IHS cut-off for hyperacusis not specified for this combination (56 or 69). Comorbid 'both conditions' 13% (n = 280) not extracted as an estimate.

**⚠ Проверка скриптом (обратите внимание):**
- E6: n оценки не равно n_analysed выборки (2080): проверьте знаменатель

**Ключевые поля выборки:**
- **n_analysed: 2080** — Data integrity check; Table 1 — «After removing low-quality data (n = 1016), a final sample of 2080 participants were included in the analyses»
- **population: university_students** — Materials and methods, Participants — «A sample of 3096 undergraduate students»
- **sampling: convenience** — Materials and methods, Participants — «using the research participant portal at Wilfrid Laurier University ... Participants received course credit for their participation.»

**Остальные поля:**
- clinical_group: NA — NA
- country: CAN — Materials and methods, Participants — «using the research participant portal at Wilfrid Laurier University in Ontario, Canada»
- setting: university (research participant portal, Wilfrid Laurier University, Ontario; course credit) — Materials and methods, Participants — «participated in an online survey administered through Qualtrics (Qualtrics, Provo, UT) using the research participant portal at Wilfrid Laurier University in O…»
- data_years: 2023-2024 — Materials and methods, Procedure — «Data collection ran from November 2023 to April 2024.»
- design: cross-sectional — Discussion — «The most significant limitations are the use of self-report measures and the cross-sectional nature of the study.»
- topic_disclosed: no — Materials and methods, Participants — «The study was advertised as investigating the quality of life of university students, with no mention of DST or related concepts»
- inclusion_exclusion: Undergraduates in the WLU research participant pool (R0197: enrolled in a psychology course, device access); excluded: failed any of 4 attention checks or answered 'yes' to honesty check (n=1016 removed) — Data integrity check; R0197, 2.1 — «Participants who answered “yes” to this question, or incorrectly responded to any of the attention check questions were removed from the dataset and analyses.»
- n_invited: NR — NA
- n_responded: 3096 — Materials and methods, Participants; Table 1 note — «Initial sample prior to data integrity check was N = 3096.»
- response_rate: NR — NA
- age_mean: 20.47 — Table 1; Data integrity check — «(M age = 20.47, SD = 3.35; 435 male, 1600 female, 45 non-cisgendered)»
- age_sd: 3.35 — Table 1; Data integrity check — «(M age = 20.47, SD = 3.35; 435 male, 1600 female, 45 non-cisgendered)»
- age_min: 18 — R0437, Methods, Participants / Table 1 — «A sample of 2095 undergraduate students from Wilfrid Laurier University ranging in age from 18 to 60 years»
- age_max: 60 — R0437, Methods, Participants / Table 1 — «A sample of 2095 undergraduate students from Wilfrid Laurier University ranging in age from 18 to 60 years»
- age_group: adults — R0437, Table 1 — «Age | 2059 | 20.34 | 2.76 | 18–60»
- pct_female: 76.9 — Table 1 — «Gender | 435 male, 1600 female, 45 non-cisgendered»
- informant: self — Abstract — «2080 students completed an online survey using multiple established self-report measures of decreased sound tolerance»
- mode: online — Materials and methods, Participants — «participated in an online survey administered through Qualtrics»
- instruments: MQ (English); DMQ (English); DVMSQ (English) — Current study — «using the Misophonia Questionnaire (MQ), the Duke Misophonia Questionnaire (DMQ), and the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ)»
- instrument_validated_in_language: yes — R0349, References [32] — «Williams ZJ, Cascio CJ, Woynaroski TG. Psychometric validation of a brief self-report measure of misophonia symptoms and functional impairment: The duke-vander…»
- pub_status: journal — Header — «Year: 2025; venue: PloS one; DOI: 10.1371/journal.pone.0334689»
- language: English — Full text — «Decreased sound tolerance in a Canadian University Context»
- funding_coi: NR in main report; companion report on same survey: WLU Research Support Fund; no conflicts declared (R0197) — R0197, Acknowledgements / Declaration of competing interest — «This research was funded by the Wilfrid Laurier University Research Support Fund.»
- notes: The same survey is analysed in R0197 (n=2095) and R0437 (n=2095), which use different exclusion counts (1001 vs 1016) and report different case counts. R0349 is the preprint of this paper. MQ Severity was collected for only about half the sample because of a Qualtrics error, so MQ estimates use a reduced denominator. The DMQ threshold is stated ambiguously ('cut-off of 39 or greater', with no subscale named); the companion reports state Symptom Severity mean >=1.8. Non-cisgender subgroup percentages imply a denominator of 38, not 45. The age range comes from R0437 (the n=2095 version of the s…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is Canadian post-secondary students; frame is one university's psychology research participant pool. — Materials and methods, Participants — «using the research participant portal at Wilfrid Laurier University in Ontario, Canada»
2. способ отбора: **no** — Volunteer opt-in for course credit from participant pool (convenience). — Materials and methods, Participants — «Participants received course credit for their participation.»
3. размер выборки: **yes** — n = 2080 >= 385. — Data integrity check — «a final sample of 2080 participants were included in the analyses»
4. описание выборки и условий: **yes** — Age, sex/gender, setting, country and data collection dates reported. — Table 1; Procedure — «Data collection ran from November 2023 to April 2024.»
5. охват (пропуски): **unclear** — 1016/3096 (33%) removed for failed quality checks; item-level missingness on DVMSQ not reported in main report (companion report R0197 shows incomplete measures were dropped). — Data integrity check — «After removing low-quality data (n = 1016), a final sample of 2080 participants were included»
6. валидность определения случая: **yes** — Primary estimate uses the DVMSQ diagnostic algorithm (clinical), English original version with published validation. — Methods, DVMSQ — «The questionnaire’s diagnostic algorithm, which compiles scores across all items, is then used to determine if a respondent has no misophonia, subclinical miso…»
7. единое надёжное измерение: **yes** — Same online self-report instruments for all; reliability reported in sample (MQ alpha .90, DMQ .98) and DVMSQ reliability in source (Williams 2022); DVMSQ alpha not given in this sample. — Table 2; R0197, 2.3.1 — «For reliability, the omega-total score (ωT) for the DVMSQ total score has been reported as high as 0.98 (Williams et al., 2022).»
8. статистика (числитель и знаменатель): **yes** — Primary numerator and denominator clear (272/2080), CI calculable; but subgroup and MQ denominators inconsistent (see consistency notes). — Results, Misophonia — «The DVMSQ detected clinical misophonia in 13% (n = 272) of the sample.»
9. отклик: **no** — Participant-pool opt-in survey with no denominator of invited students; no non-response handling. — Materials and methods, Participants — «participated in an online survey administered through Qualtrics ... using the research participant portal»

Правки:
- 

Проверено: да
---

## ST027 · Oszczapinska 2025 · Psychophysiology

Основной отчёт R0368: [текст](../../fulltext/text/R0368.txt) — «The Impact of Disgusting Sounds on Pupil Diameter of Misophonic and Non-Misophonic Listeners.» — [DOI](https://doi.org/10.1111/psyp.70014)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R0314 (ST024), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap
Не выписано ИИ: Online pilot (preliminary testing) sample used to select the sounds: no misophonia measure and no size reported, so not extractable. 'Other preliminary lab data' on pleasantness ratings of misophonic vs non-misophonic listeners: not described, not extractable. No group in R0368 was explicitly recruited for misophonia, so no E1 exclusion was applied. However, recruitment aims are not described.
Расхождения в тексте: The participants paragraph reports 59 recruited with 36 female, 20 male and 1 non-binary (= 57), and a final sample of 57. The sex breakdown therefore seems to refer to the 57 analysed, and the age mean (23.54) may refer to either 59 or 57. pct_female was computed as 36/57 = 63.2%. Group sizes 14 + 43 = 57 agree with the final sample. The escape-scale subsample (37: 13 misophonic, 24 non-misophonic) is not a prevalence denominator.
Заметка ИИ: One eligible sample (laboratory experiment at CMU, n=57). The only case definition is the experimental 'misophonic' grouping (14/57) based on the scoring guidelines of DVMSQ, MQ and S-Five. Its thresholds and combination rule are not stated; it was coded L2 under G4 and flagged for reviewer check. Possible overlap with R0314, R0385 and R0910 (same lab) is noted.

### ST027-1 · Carnegie Mellon University and surrounding area pupillometry experiment, USA, n=57
Отчёты: R0368 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · Clinical presentation of misophonia according to the scoring guidelines of DVMSQ, MQ and S-Five (combination rule and exact thresholds not stated) | **L2** | **14 / 57** | 24.6 | Method, Participants | «Participants (N = 14) in the "misophonic" category reported symptoms that corresponded to clinical presentations of misophonia. Participants (N = 43) in the "non-misophonic" category reported symptoms that corresponded …» |

- E1: источник порога: developer paper; правило: DVMSQ/MQ/S-Five rows; G4 combined definition (clinical on any or all of the L2 cut-offs -> L2); у авторов: «misophonic: symptoms that corresponded to clinical presentations of misophonia»; главная у авторов: no; период: NR; заметка: 14/57 = 24.6%. Grouping for an experiment, not a prevalence estimate. It is not stated whether 'clinical' required clinical status on all three scales or on any one, or which MQ threshold was used. Every component cut-off is at L2, so the level is L2 either way under G4; the reviewer should check t…

**Ключевые поля выборки:**
- **n_analysed: 57** — Method, Participants — «Our final sample size was 57 participants.»
- **population: gp_other** — Method, Participants — «from Carnegie Mellon University and the surrounding area in Pittsburgh, PA ... compensated with course credit or payment»
- **sampling: convenience** — Method, Participants — «Fifty-nine individuals were recruited ... from Carnegie Mellon University and the surrounding area ... compensated with course credit or payment.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: USA — Method, Participants — «from Carnegie Mellon University and the surrounding area in Pittsburgh, PA»
- setting: university and community (laboratory experiment at Carnegie Mellon University; participants from the university and the surrounding area) — Method, Participants — «Fifty-nine individuals were recruited ... from Carnegie Mellon University and the surrounding area in Pittsburgh, PA.»
- data_years: NR — Method — «NR»
- design: screening phase of experiment — Method, Participants — «We followed the scoring guidelines provided for each of the scales to categorize participants into "misophonic" and "non-misophonic" participant groups.»
- topic_disclosed: NR — Method, Participants — «NR»
- inclusion_exclusion: Age 18-45 years (because of age-related pupillary differences); all reported normal hearing. Reasons for 2 of 59 not in final sample not given. — Method, Participants — «we set an age criterion between 18 and 45 years old ... Our final sample size was 57 participants.»
- n_invited: NR — Method, Participants — «NR»
- n_responded: 59 — Method, Participants — «Fifty-nine individuals were recruited»
- response_rate: NR — Method, Participants — «NR»
- age_mean: 23.54 — Method, Participants — «M AGE = 23.54; range = 18-45 years old»
- age_sd: NR — Method, Participants — «NR»
- age_min: 18 — Method, Participants — «range = 18-45 years old»
- age_max: 45 — Method, Participants — «range = 18-45 years old»
- age_group: adults — Method, Participants — «range = 18-45 years old»
- pct_female: 63.2 — Method, Participants — «36 females, 20 males, and one non-binary»
- informant: self — Method, Participants — «All participants completed the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) ..., the Misophonia Questionnaire (MQ) ..., and the S-Five»
- mode: NR — Method, Participants / Procedure — «Participants signed in-person consent forms»
- instruments: DVMSQ (English); MQ (English); S-Five (English) — Method, Participants — «All participants completed the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) (Williams, Cascio and Woynaroski 2022), the Misophonia Questionnaire …»
- instrument_validated_in_language: yes — Method, Participants — «(DVMSQ) (Williams, Cascio and Woynaroski 2022), the Misophonia Questionnaire (MQ) (Wu et al. 2014), and the S-Five (Vitoratou et al. 2023)»
- pub_status: journal — Header (Psychophysiology 2025) — «Psychophysiology; DOI: 10.1111/psyp.70014»
- language: English — Full text — «The Impact of Disgusting Sounds on Pupil Diameter of Misophonic and Non-Misophonic Listeners»
- funding_coi: Funding source not stated in the text (authors listed for 'funding acquisition'); authors declare no conflicts of interest. — Author Contributions; Conflicts of Interest — «The authors declare no conflicts of interest.»
- notes: Possible overlap with R0314 (ST024), R0385 (ST030), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Experimental study comparing misophonic vs non-misophonic listeners; not designed for prevalence. The recruitment text does not say whether people with misophonia were targeted; if they were, 14/57 would be enriched. Sex counts (36+20+1=57) are given next to N=59 recruited; pct_female = 36/57 (61.0% if /59). 11 of the 14 misophonic participants had sound level intolerance on LDL testing (not a misophonia estimate).…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Laboratory volunteers from one university and the surrounding area; the frame does not cover any defined population. — Method, Participants — «recruited ... from Carnegie Mellon University and the surrounding area in Pittsburgh, PA»
2. способ отбора: **no** — Volunteer convenience recruitment for an experiment, paid or rewarded with course credit. — Method, Participants — «Participants signed in-person consent forms and were compensated with course credit or payment.»
3. размер выборки: **no** — n = 57 < 385. — Method, Participants — «Our final sample size was 57 participants.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — Method, Participants — «M AGE = 23.54; range = 18-45 years old, 36 females, 20 males, and one non-binary»
5. охват (пропуски): **yes** — 57 of 59 recruited were analysed (3.4% not included); all analysed participants completed the misophonia scales. — Method, Participants — «Our final sample size was 57 participants. All participants completed the Duke-Vanderbilt Misophonia Screening Questionnaire»
6. валидность определения случая: **unclear** — Classification used the 'scoring guidelines' of DVMSQ, MQ and S-Five. The thresholds and the rule for combining them (any vs all) are not stated. — Method, Participants — «We followed the scoring guidelines provided for each of the scales to categorize participants into "misophonic" and "non-misophonic" participant groups.»
7. единое надёжное измерение: **unclear** — All participants completed the same instruments, but the mode is not stated and no reliability is reported in this report. — Method, Participants — «All participants completed the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) ..., the Misophonia Questionnaire (MQ) ..., and the S-Five»
8. статистика (числитель и знаменатель): **yes** — Numerator (14) and denominator (57) are clear; a CI can be calculated. — Method, Participants — «Participants (N = 14) in the "misophonic" category ... Participants (N = 43) in the "non-misophonic" category»
9. отклик: **unclear** — The number of people approached or invited is not reported. — Method, Participants — «Fifty-nine individuals were recruited»

Правки:
- 

Проверено: да
---

## ST028 · Pfeiffer 2025 · Social psychiatry and psychiatric epidemiology

Основной отчёт R0375: [текст](../../fulltext/text/R0375.txt) — «The prevalence of misophonia in a representative population-based survey in Germany.» — [DOI](https://doi.org/10.1007/s00127-024-02707-0)
Расхождения в тексте: 1) Share with at least one trigger sound: the abstract says 33.3%, Results say 33.5% (n = 844) and the Discussion says 34%. 844/2522 = 33.5%. 2) No sensitivity: 1670 (66.2%); 1670 + 844 = 2514, so 8 participants are unaccounted for. 3) Moderate to extreme: 2.1% + 0.1% = 2.2% (56/2522 = 2.22%), but the Discussion gives 2.3%. 4) The Discussion says 37.3% of the trigger subsample had at least mild symptoms. The bands give 307/844 = 36.4% (29.7 + 6.2 + 0.4 = 36.3%). 5) The response is reported as 41.2%, but 2522/6192 = 40.7%. 6) Exposure-time item: 495 + 267 + 52 + 6 + 1 + 22 = 843, not 844. 7) Table 1 male percentages for the subthreshold group sum to 100.1% (rounding). 8) Sex-subgroup counts are derived from Table 1 column percentages; the derived counts add back to the band totals (female + male + diverse = 844; 186 + 121 = 307; 30 + 26 = 56). 9) The Table 1 note mentions 'GAD-7', but th…
Заметка ИИ: Single probability sample (random route with Kish grid), German population aged 16-96. The primary estimate is AMISOS-R >=21 (L2 by Table 1, but JBI 6 = no because the band has no anchoring and the German version is not validated). The recommended cut-off (>=24) cannot be computed from the report. No survey weights were reported.

### ST028-1 · German general population random-route household survey (USUMA), DEU, n=2522
Отчёты: R0375 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | AMISOS-R · AMISOS-R >=21 (moderate to severe or more) | **L2** | **56 / 2522** | 2.2 | Results, Misophonia symptoms and severity; Table 1; Discuss… | «moderate to severe symptoms were reported by 2.1% (n = 53) and severe to extreme symptoms were reported in 0.1% (n = 3) of participants» |
| E2 | all | AMISOS-R · AMISOS-R >=11 (mild or more) | **L1** | **307 / 2522** | 12.2 | Results, Misophonia symptoms and severity | «mild symptoms were reported by 9.9% (n = 251), moderate to severe symptoms were reported by 2.1% (n = 53) and severe to extreme symptoms were reported in 0.1% (n = 3)» |
| E3 | all | AMISOS-R · AMISOS-R >=31 (severe to extreme) | **L2** | **3 / 2522** | 0.1 | Results, Misophonia symptoms and severity | «severe to extreme symptoms were reported in 0.1% (n = 3) of participants» |
| E4 | all | AMISOS-R · at least one misophonic trigger sound endorsed on the AMISOS-R trigger checklist | **L0** | **844 / 2522** | 33.5 | Results, Misophonic reactions; Table 1 | «Among those participants who reported at least one specific misophonic sound (33.5%, n = 844)» |
| E5 | female | AMISOS-R · AMISOS-R >=21 (moderate to severe or more) | **L2** | **30 / 1296** | 2.3 | Table 1 | «Female / 51.4 / 59.8 / 62.0 / 53.6» |
| E6 | female | AMISOS-R · AMISOS-R >=11 (mild or more) | **L1** | **186 / 1296** | 14.4 | Table 1 | «Female / 51.4 / 59.8 / 62.0 / 53.6» |
| E7 | female | AMISOS-R · at least one misophonic trigger sound endorsed on the AMISOS-R trigger checklist | **L0** | **507 / 1296** | 39.1 | Table 1 | «Female / 51.4 / 59.8 / 62.0 / 53.6» |
| E8 | male | AMISOS-R · AMISOS-R >=21 (moderate to severe or more) | **L2** | **26 / 1221** | 2.1 | Table 1 | «Male / 48.4 / 39.9 / 38.0 / 46.4» |
| E9 | male | AMISOS-R · AMISOS-R >=11 (mild or more) | **L1** | **121 / 1221** | 9.9 | Table 1 | «Male / 48.4 / 39.9 / 38.0 / 46.4» |
| E10 | male | AMISOS-R · at least one misophonic trigger sound endorsed on the AMISOS-R trigger checklist | **L0** | **335 / 1221** | 27.4 | Table 1 | «Male / 48.4 / 39.9 / 38.0 / 46.4» |

- E1: источник порога: validation paper; правило: AMISOS-R row (L2: >=21 moderate to severe or more); G1 sum of bands; G10 denominator all screened; у авторов: «moderate to extreme symptoms; clinically relevant symptoms»; главная у авторов: yes; период: current; **расчёт: 53 (moderate to severe) + 3 (severe to extreme) = 56; matches Table 1 n = 56**; заметка: In the Discussion the authors give 2.3% as 'clinically relevant symptoms'; 56/2522 = 2.2%. The study gives the bands without a citation. The time frame is printed as 'assessment period: 3 last 3 days' (garbled). Not the recommended >=24 cut-off; JBI 6 = no.
- E2: источник порога: validation paper; правило: AMISOS-R row (L1: >=11); G1 sum of bands; G10; у авторов: «at least mild symptoms of misophonia»; главная у авторов: no; период: current; **расчёт: 251 (mild) + 53 (moderate to severe) + 3 (severe to extreme) = 307**
- E3: источник порога: validation paper; правило: AMISOS-R row; G2 threshold above the L2 cut-off; у авторов: «severe to extreme symptoms»; главная у авторов: no; период: current; заметка: Top band, so already cumulative.
- E4: источник порога: study's own; правило: adhoc row L0 (any trigger only), applied to the AMISOS-R checklist; у авторов: «sensitive to at least one specific misophonic sound»; главная у авторов: no; период: current; заметка: The abstract says 33.3% and the Discussion 34%; 844/2522 = 33.5%.
- E5: источник порога: validation paper; правило: AMISOS-R row (L2 >=21); G1; G10; у авторов: «moderate to extreme misophonia»; главная у авторов: no; период: current; **расчёт: 53.6% female x 56 = 30.0 -> 30; n = 51.4% x 2522 = 1296.3 -> 1296**; заметка: Derived from column percentages in Table 1.
- E6: источник порога: validation paper; правило: AMISOS-R row (L1 >=11); G1; G10; у авторов: «mild misophonia or more»; главная у авторов: no; период: current; **расчёт: 62.0% x 251 = 155.6 -> 156; 53.6% x 56 = 30.0 -> 30; 156+30 = 186; n = 51.4% x 2522 = 1296**; заметка: Derived from column percentages in Table 1.
- E7: источник порога: study's own; правило: adhoc row L0 (any trigger); у авторов: «misophonia subsample (reported misophonic sounds)»; главная у авторов: no; период: current; **расчёт: 59.8% x 537 = 321.1 -> 321; 62.0% x 251 -> 156; 53.6% x 56 -> 30; 321+156+30 = 507; n = 51.4% x 2522 = 1296**; заметка: Derived from column percentages in Table 1.
- E8: источник порога: validation paper; правило: AMISOS-R row (L2 >=21); G1; G10; у авторов: «moderate to extreme misophonia»; главная у авторов: no; период: current; **расчёт: 46.4% x 56 = 26.0 -> 26; n = 48.4% x 2522 = 1220.6 -> 1221**; заметка: Derived from column percentages in Table 1.
- E9: источник порога: validation paper; правило: AMISOS-R row (L1 >=11); G1; G10; у авторов: «mild misophonia or more»; главная у авторов: no; период: current; **расчёт: 38.0% x 251 = 95.4 -> 95; 46.4% x 56 = 26.0 -> 26; 95+26 = 121; n = 48.4% x 2522 = 1221**; заметка: Derived from column percentages in Table 1.
- E10: источник порога: study's own; правило: adhoc row L0 (any trigger); у авторов: «misophonia subsample (reported misophonic sounds)»; главная у авторов: no; период: current; **расчёт: 39.9% x 537 = 214.3 -> 214; 38.0% x 251 -> 95; 46.4% x 56 -> 26; 214+95+26 = 335; n = 48.4% x 2522 = 1221**; заметка: Derived from column percentages in Table 1.

**Ключевые поля выборки:**
- **n_analysed: 2522** — Results, Misophonia symptoms and severity — «In the total sample of N = 2522 participants, subthreshold symptoms were reported by 21.3% (n = 537)»
- **population: gp_probability** — Methods, Procedure and sample — «a representative sample of the German population (age 16–96) was collected employing a random route approach»
- **sampling: probability** — Methods, Procedure and sample — «the target households within these regional areas were selected according to a random route procedure. For multi-person households, one person was randomly selected using the Kish selection grid technique.»

**Остальные поля:**
- clinical_group: NA — NA — «NA»
- country: DEU — Methods, Procedure and sample — «a representative sample of the German population (age 16–96) was collected employing a random route approach»
- setting: community (household survey, face-to-face visits by trained assessors of USUMA) — Methods, Procedure and sample — «possible participants were not recruited from specific platforms, but were unexpectedly contacted directly by trained assessors of the research institute USUMA»
- data_years: 2022 — Methods, Procedure and sample — «The population-based survey was conducted in the period from 3th March to 26th May 2022.»
- design: cross-sectional — Abstract, Methods — «a cross-sectional population representative survey in Germany has been conducted»
- topic_disclosed: no — Methods, Procedure and sample — «Prospective subjects were informed that the study was about psychological health and well-being.»
- inclusion_exclusion: Age >=16 years and sufficient German language skills — Methods, Procedure and sample — «To qualify for inclusion in the survey, participants had to be at least 16 years of age and have sufficient German language skills.»
- n_invited: 6192 — Methods, Procedure and sample — «Out of the 6192 addresses used, 2522 responded indicating a utilization rate of 41.2%.»
- n_responded: 2522 — Methods, Procedure and sample — «Out of the 6192 addresses used, 2522 responded»
- response_rate: 41.2 — Methods, Procedure and sample — «Out of the 6192 addresses used, 2522 responded indicating a utilization rate of 41.2%.»
- age_mean: 49.42 — Methods, Procedure and sample — «with an average age of M = 49.42 years (SD = 18.89; range 16–96)»
- age_sd: 18.89 — Methods, Procedure and sample — «(SD = 18.89; range 16–96)»
- age_min: 16 — Methods, Procedure and sample — «(SD = 18.89; range 16–96)»
- age_max: 96 — Methods, Procedure and sample — «(SD = 18.89; range 16–96)»
- age_group: mixed — Methods, Procedure and sample — «range 16–96»
- pct_female: 51.4 — Methods, Procedure and sample; Table 1 — «The final sample consisted of N = 2522 respondents (51.4% female)»
- informant: self — Methods, Procedure and sample — «the participants alone filled out other instruments like the AMISOS-R or PHQ-4, while the interviewer was waiting in the room»
- mode: mixed — Methods, Procedure and sample — «Demographic data was assessed face-to-face by a trained interviewer and the participants alone filled out other instruments like the AMISOS-R or PHQ-4, while t…»
- instruments: AMISOS-R (German version; trigger and emotion checklists plus 10-item severity scale) — Methods, AMISOS-R; Limitations — «Misophonia symptoms were measured using the Amsterdam Misophonia Scale-Revised (AMISOS‐R: [4]).»
- instrument_validated_in_language: no — Limitations and future research — «it’s important to note that this measure (in both Dutch and German versions) has not undergone sufficient validation.»
- pub_status: journal — Header — «Social psychiatry and psychiatric epidemiology»
- language: English — Full text — «The prevalence of misophonia in a representative population-based survey in Germany»
- funding_coi: No relevant financial interests; Open Access funding by Projekt DEAL; no competing interests declared — Funding; Competing interests — «The authors have no relevant financial or non-financial interests to disclose. Open Access funding enabled and organized by Projekt DEAL.»
- notes: Two-stage AMISOS-R structure: only the 844 who endorsed at least one trigger sound were placed in severity bands (537+251+56=844); others counted as non-cases, denominator 2522 (G10). No survey weights reported. Mode of the AMISOS-R itself (paper/tablet) not stated: self-completed during the interviewer's home visit; demographics collected face-to-face. A different sample from Jakubovski et al. 2022 (German population survey, data Dec 2020-Mar 2021). The Leipzig/USUMA 2022 survey may be described in other reports; check for overlap. Severity bands are given in the text without a citation (AMI…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — ADM sampling system of regional areas covers the German population aged 16+, which is the target population. — Methods, Procedure and sample — «258 German regional areas were predefined using the reference system for representative studies in Germany provided by the “ADM-Sampling- System”.»
2. способ отбора: **yes** — Multistage probability sampling: random route household selection, Kish grid selection within households. — Methods, Procedure and sample — «the target households within these regional areas were selected according to a random route procedure. For multi-person households, one person was randomly sel…»
3. размер выборки: **yes** — n = 2522 >= 385. — Methods, Procedure and sample — «The final sample consisted of N = 2522 respondents»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates all reported. — Methods, Procedure and sample — «N = 2522 respondents (51.4% female) with an average age of M = 49.42 years ... conducted in the period from 3th March to 26th May 2022»
5. охват (пропуски): **yes** — Severity bands sum to the 844 trigger-positive respondents; only 8 of 2522 (0.3%) are unaccounted for in the trigger item (1670+844=2514). — Results, Misophonic sounds; Table 1 — «Overall 66.2% (n = 1670) reported to have no particular sensitivity towards misophonic sounds»
6. валидность определения случая: **no** — Primary estimate uses AMISOS-R >=21 (moderate to severe band), which has no anchoring; the German AMISOS-R version is not validated. — Limitations and future research — «this measure (in both Dutch and German versions) has not undergone sufficient validation»
7. единое надёжное измерение: **yes** — Same instrument and procedure for all participants; Cronbach alpha reported in this sample. — Methods, AMISOS-R — «The reliability of the AMISOS-R in the current sample was good (α = 0.89»
8. статистика (числитель и знаменатель): **unclear** — Band counts and the denominator are given, so CIs can be calculated. No design weights are reported despite Kish selection within households. Summary percentages are inconsistent (2.3% vs 2.2%; 33.3% vs 33.5%). — Results; Discussion — «moderate to severe symptoms were reported by 2.1% (n = 53) and severe to extreme symptoms were reported in 0.1% (n = 3)»
9. отклик: **no** — Response 41.2% (<60%); no comparison with non-responders and no non-response weighting reported. — Methods, Procedure and sample — «Out of the 6192 addresses used, 2522 responded indicating a utilization rate of 41.2%.»

Правки:
- 

Проверено: да
---

## ST029 · Prabhu 2025 · Research Square

Основной отчёт R0381: [текст](../../fulltext/text/R0381.txt) · [PDF](../../fulltext/pdf/R0381.pdf) — «Prevalence of misophonia in the general population and those with complaints of tinnitus: An epidemiological study» — [DOI](https://doi.org/10.21203/rs.3.rs-8333185/v1)
Расхождения в тексте: (1) Age: the normal-hearing group is given as mean 39.3 ± 4.7 (range 18-50), but the misophonia subgroup has mean 24.8 ± 7.1 and 56.3% of the sound-sensitive subgroup is 18-25. These are hard to reconcile. The A-MISO-S subsample range of 17-50 conflicts with the 18-50 eligibility rule. In the tinnitus group (mean 42.6 ± 6.9), the subgroups have means of 37.6 and 39.1. (2) In Table 1, the tinnitus group shows 74 without and 85 with misophonia (total 159), but the stated n is 500 (500 - 85 = 415 expected without). (3) In the normal-hearing group, 66/24/10% are said to be mild/moderate/severe, but the 200 A-MISO-S completers scored only 1-4 (subclinical on the A-MISO-S bands), and Table 1 calls them 'Mild-Moderate'. The instrument behind the severity bands cannot be identified. (4) Table 1 gives the tinnitus-with-misophonia A-MISO-S mean as 6.4 ± 2.3, i.e., mild (5-9), while the text calls…
Заметка ИИ: Preprint (Research Square, 2025). The misophonia case definition is not stated. The design looks two-stage: a screen on the general questionnaire, then A-MISO-S and S-Five for screen-positives. But A-MISO-S data exist only for subsamples (200 and 7), and there are no S-Five results. All estimates are therefore level NR (G6). Instrument is coded 'adhoc' on the assumption that cases came from the screening items; please verify against Appendix.docx (not available). This report has the same first author as Aryal & Prabhu 2022, Patel et al. 2023, Sujeeth et al. 2024 and Valsa et al. 2025 (all AII…

### ST029-1 · Normal-hearing adults, nationwide India (community outreach, social media, audiology centres), n=10,000
Отчёты: R0381 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · not stated: 'met the criteria for misophonia' (screening on the study's general questionnaire; criteria not reported) | **NR** | **2615 / 10000** | 26.1 | Page 6, Prevalence of Misophonia; Table 1 | «Among individuals with normal hearing, 26% (2,615 of 10,000) met the criteria for misophonia.» |
| E2 | all | adhoc · severity moderate or severe among misophonia cases (instrument and band cut-offs not stated) | **NR** | **889 / 10000** | 8.9 | Page 7, Prevalence of Misophonia | «in the normal-hearing group, 66% of affected individuals reported mild symptoms, 24% moderate, and 10% severe.» |
| E3 | all | adhoc · severity severe among misophonia cases (instrument and band cut-offs not stated) | **NR** | **262 / 10000** | 2.6 | Page 7, Prevalence of Misophonia | «66% of affected individuals reported mild symptoms, 24% moderate, and 10% severe.» |
| E4 | all | adhoc · any reported sound sensitivity/intolerance or misophonia (437 subclinical + 2,615 misophonia) | **L0** | **3052 / 10000** | 30.5 | Page 7, Normal-Hearing Individuals with Sound Sensitivity; … | «A subset of 437 individuals from the normal-hearing sample reported sound sensitivity or intolerance without fulfilling the diagnostic criteria for misophonia.» |
| E5 | female | adhoc · not stated: 'met the criteria for misophonia' | **NR** | **1780 / 3927** | 45.3 | Page 7; Page 4 | «Among the 2,615 normal-hearing participants diagnosed with misophonia, 1,780 (68.1%) were female» |
| E6 | male | adhoc · not stated: 'met the criteria for misophonia' | **NR** | **835 / 6073** | 13.7 | Page 7; Page 4 | «1,780 (68.1%) were female and 835 (31.9%) were male.» |

- E1: источник порога: study's own; правило: G6 case definition not determinable; у авторов: «met the criteria for misophonia / diagnosed with misophonia»; главная у авторов: yes; период: NR; заметка: Instrument coded adhoc on the assumption that cases came from the screening items; the report does not say. The A-MISO-S subsample (n=200) scored 1-4, which is subclinical by A-MISO-S bands.
- E2: источник порога: study's own; правило: G1 sum of bands (24% + 10%); G6 instrument not determinable; у авторов: «moderate + severe»; главная у авторов: no; период: NR; **расчёт: (24% + 10%) x 2,615 = 889.1 -> 889**; заметка: The severity bands do not match the A-MISO-S subsample data (range 1-4).
- E3: источник порога: study's own; правило: G1 top band; G6 instrument not determinable; у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: 10% x 2,615 = 261.5 -> 262**
- E4: источник порога: study's own; правило: adhoc row; L0 any sound sensitivity; у авторов: «sound sensitivity or intolerance (incl. misophonia)»; главная у авторов: no; период: NR; **расчёт: 437 + 2,615 from Table 1 / text**; заметка: Reviewer-derived union; the authors do not report it as an estimate.
- E5: источник порога: study's own; правило: G6 case definition not determinable; у авторов: «diagnosed with misophonia»; главная у авторов: no; период: NR; заметка: Denominator = 3,927 females in the normal-hearing group (Page 4).
- E6: источник порога: study's own; правило: G6 case definition not determinable; у авторов: «diagnosed with misophonia»; главная у авторов: no; период: NR; заметка: Denominator = 6,073 males in the normal-hearing group (Page 4).

**Ключевые поля выборки:**
- **n_analysed: 10000** — Page 6, Prevalence of Misophonia — «Among individuals with normal hearing, 26% (2,615 of 10,000) met the criteria for misophonia.»
- **population: gp_other** — Page 4, Participant and Recruitment — «10,000 with normal hearing (6,073 males, 3,927 females; mean age = 39.3 ± 4.7 years)»
- **sampling: convenience** — Page 4, Participant and Recruitment — «identified through nationwide recruitment channels, including community outreach programs, social media advertisements, and tertiary care audiology centers.»

**Остальные поля:**
- clinical_group: NA — NA
- country: IND — Page 2, Abstract — «A descriptive cross-sectional survey was conducted among 10,500 participants recruited across India»
- setting: community / online (social media) / clinic (tertiary care audiology centres); mixed recruitment channels — Page 4, Participant and Recruitment — «identified through nationwide recruitment channels, including community outreach programs, social media advertisements, and tertiary care audiology centers.»
- data_years: NR — Page 6, Ethical Considerations — «approved the study (AIISH/IRB/2024/35)»
- design: cross-sectional — Page 4, Study Design — «A large-scale, descriptive cross-sectional survey was conducted to determine the prevalence and severity of misophonia in adults with normal hearing and in ind…»
- topic_disclosed: NR — Page 5, Procedure — «All participants received detailed information about the study objectives and procedures prior to participation.»
- inclusion_exclusion: Age 18-50, informed consent, normal hearing; excluded chronic otitis media/ear surgery/canal abnormalities, active ear infection, documented psychiatric illness (e.g., psychosis), ototoxic medication, ongoing sound therapy — Page 4, Eligibility Criteria — «Participants were eligible if they were between 18 and 50 years of age, provided informed consent, and demonstrated normal hearing sensitivity»
- n_invited: NR — Page 4, Participant and Recruitment — «A total of 10,980 individuals were identified through nationwide recruitment channels»
- n_responded: NR — Page 4, Participant and Recruitment — «Following screening, 480 respondents were excluded due to incomplete responses, ineligibility, or missing demographic data.»
- response_rate: NR — Page 4, Participant and Recruitment — «A total of 10,980 individuals were identified ... 480 respondents were excluded»
- age_mean: 39.3 — Page 4, Participant and Recruitment — «10,000 with normal hearing (6,073 males, 3,927 females; mean age = 39.3 ± 4.7 years)»
- age_sd: 4.7 — Page 4, Participant and Recruitment — «mean age = 39.3 ± 4.7 years»
- age_min: 18 — Page 4, Eligibility Criteria — «Participants were eligible if they were between 18 and 50 years of age»
- age_max: 50 — Page 4, Eligibility Criteria — «Participants were eligible if they were between 18 and 50 years of age»
- age_group: adults — Page 4, Eligibility Criteria — «between 18 and 50 years of age»
- pct_female: 39.27 — Page 4, Participant and Recruitment — «10,000 with normal hearing (6,073 males, 3,927 females»
- informant: self — Page 10, Limitations — «self-report measures may be influenced by recall bias or underreporting.»
- mode: mixed — Page 5, Assessment Tools / Procedure — «Participants completed a series of validated instruments administered either in paper or digital format, depending on accessibility.»
- instruments: Study-developed General Questionnaire with misophonia symptom/screening items (language NR); A-MISO-S (language NR, 'minor linguistic modifications'; screen-positives only, detailed data for subsample of 200); S-Five (language NR; screen-positives only) — Page 4-5, Development of the Questionnaire; Assessment Tool… — «Participants who screened positive for misophonia completed the A-MISO-S and S-Five»
- instrument_validated_in_language: NR — Page 5, Assessment Tools — «minor linguistic modifications were made to ensure clarity and contextual relevance for the Indian population without altering the conceptual framework.»
- pub_status: preprint — Page 1 — «Research Article ... Posted Date: December 17th, 2025 DOI: https://doi.org/10.21203/rs.3.rs-8333185/v1»
- language: English — Full text — «Prevalence of misophonia in the general population and those with complaints of tinnitus: An epidemiological study»
- funding_coi: No specific grant; authors declare no conflicts of interest — Page 11, Funding; Disclosure Statement — «This study did not receive any specific grant from public, commercial, or not-for-profit funding agencies. ... The authors declare that there are no conflicts …»
- notes: The 10,980 identified and 480 excluded are given for both groups combined. The misophonia criteria are not stated. Two-stage: screen-positives completed A-MISO-S and S-Five, but A-MISO-S data are reported only for a subsample of 200 (scores 1-4, all subclinical on A-MISO-S bands), and no S-Five results are reported. The study cites STROBE and PRISMA. Several internal inconsistencies (see consistency_notes). Same first author and institute (AIISH Mysore) as earlier Indian prevalence studies (Aryal & Prabhu 2022; Patel 2023; Sujeeth 2024; Valsa 2025): check for overlap.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is adults in India; frame is community outreach, social media and audiology centres, which cover only part of that population — Page 4, Participant and Recruitment — «community outreach programs, social media advertisements, and tertiary care audiology centers.»
2. способ отбора: **no** — Convenience/volunteer recruitment, not probability sampling — Page 4, Participant and Recruitment — «identified through nationwide recruitment channels, including community outreach programs, social media advertisements»
3. размер выборки: **yes** — n = 10,000 (≥385) — Page 6, Prevalence of Misophonia — «26% (2,615 of 10,000) met the criteria for misophonia.»
4. описание выборки и условий: **unclear** — Age, sex, country and setting reported; dates of data collection not reported — Page 4, Participant and Recruitment — «6,073 males, 3,927 females; mean age = 39.3 ± 4.7 years»
5. охват (пропуски): **unclear** — 480/10,980 excluded overall (4.4%, both groups) for incomplete data/ineligibility, split not given; only 200 of the 2,615 screen-positives have detailed A-MISO-S data, and how cases were defined is unclear — Page 4; Page 7 — «480 respondents were excluded due to incomplete responses, ineligibility, or missing demographic data. ... A subsample of 200 participants completed detailed p…»
6. валидность определения случая: **unclear** — The criteria behind 'met the criteria for misophonia' are not stated (screen items not reported; A-MISO-S scores of the 200-person subsample were all 1-4, below any threshold) — Page 6-7 — «met the criteria for misophonia. ... Scores ranged from 1–4 (Mean = 1.61 ± 0.66)»
7. единое надёжное измерение: **no** — Paper and online modes mixed with no check of equivalence; no reliability reported in this sample — Page 5, Assessment Tools — «administered either in paper or digital format, depending on accessibility.»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator stated (2,615/10,000), so a CI can be calculated; but the severity percentages cannot be traced to an instrument — Page 6 — «26% (2,615 of 10,000) met the criteria for misophonia.»
9. отклик: **no** — Open recruitment (incl. social media) with no denominator of invited people; no non-response handling — Page 4 — «A total of 10,980 individuals were identified through nationwide recruitment channels»

Правки:
- 

Проверено: да
### ST029-2 · Adults with self-reported tinnitus, India (recruitment incl. tertiary audiology centres), n=500
Отчёты: R0381 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | adhoc · not stated: 'showed comorbid misophonia' / 'met criteria for misophonia' | **NR** | **85 / 500** | 17.0 | Page 6, Prevalence of Misophonia; Table 1 | «Within the tinnitus group, 17% (85 of 500) showed comorbid misophonia.» |
| E2 | all | adhoc · severity moderate or severe among misophonia cases (instrument and band cut-offs not stated) | **NR** | **65 / 500** | 13.0 | Page 7 | «among tinnitus patients with misophonia, 33% had severe, 44% moderate, and 23% mild symptoms.» |
| E3 | all | adhoc · severity severe among misophonia cases (instrument not stated) | **NR** | **28 / 500** | 5.6 | Page 7 | «among tinnitus patients with misophonia, 33% had severe, 44% moderate, and 23% mild symptoms.» |
| E4 | female | adhoc · not stated | **NR** | **61 / 135** | 45.2 | Page 8; Page 4 | «Eighty-five participants exhibited both tinnitus and misophonia. Of these, 61 (71.8%) were female and 24 (28.2%) male.» |
| E5 | male | adhoc · not stated | **NR** | **24 / 365** | 6.6 | Page 8; Page 4 | «61 (71.8%) were female and 24 (28.2%) male.» |

- E1: источник порога: study's own; правило: G6 case definition not determinable; у авторов: «comorbid misophonia»; главная у авторов: yes; период: NR; заметка: Instrument coded adhoc by assumption (screen items); the criteria are not reported. Table 1 lists only 74 tinnitus participants without misophonia.
- E2: источник порога: study's own; правило: G1 sum of bands (44% + 33%); G6; у авторов: «moderate + severe»; главная у авторов: no; период: NR; **расчёт: (44% + 33%) x 85 = 65.45 -> 65**; заметка: Only 7 cases had A-MISO-S data (mean 6.4, range 3-10), so the basis of the bands is unclear.
- E3: источник порога: study's own; правило: G1 top band; G6; у авторов: «severe»; главная у авторов: no; период: NR; **расчёт: 33% x 85 = 28.05 -> 28**
- E4: источник порога: study's own; правило: G6; у авторов: «tinnitus and misophonia»; главная у авторов: no; период: NR; заметка: Denominator = 135 females in the tinnitus group (Page 4).
- E5: источник порога: study's own; правило: G6; у авторов: «tinnitus and misophonia»; главная у авторов: no; период: NR; заметка: Denominator = 365 males in the tinnitus group (Page 4).

**Ключевые поля выборки:**
- **n_analysed: 500** — Page 6, Prevalence of Misophonia — «Within the tinnitus group, 17% (85 of 500) showed comorbid misophonia.»
- **population: clinical** — Page 4, Participant and Recruitment — «500 with self-reported tinnitus (365 males, 135 females; mean age = 42.6 ± 6.9 years)»
- **sampling: convenience** — Page 4, Participant and Recruitment — «identified through nationwide recruitment channels»

**Остальные поля:**
- clinical_group: tinnitus — Page 6, Results — «those in the tinnitus group reported chronic subjective tinnitus with predominantly mild sensorineural hearing loss.»
- country: IND — Page 2, Abstract — «10,500 participants recruited across India»
- setting: clinic (tertiary care audiology centres) / community / social media; channels for this group not separated — Page 4, Participant and Recruitment — «community outreach programs, social media advertisements, and tertiary care audiology centers.»
- data_years: NR — Page 6, Ethical Considerations — «approved the study (AIISH/IRB/2024/35)»
- design: cross-sectional — Page 4, Study Design — «descriptive cross-sectional survey ... in adults with normal hearing and in individuals with tinnitus.»
- topic_disclosed: NR — Page 5, Procedure — «All participants received detailed information about the study objectives and procedures prior to participation.»
- inclusion_exclusion: Age 18-50, consent, self-reported tinnitus with normal hearing or audiologically confirmed mild SNHL; same exclusions (ear disease/surgery, reversible tinnitus causes, psychiatric illness, ototoxic drugs, ongoing sound therapy) — Page 4, Eligibility Criteria — «or, in the tinnitus group, mild sensorineural hearing loss confirmed through audiological evaluation.»
- n_invited: NR — Page 4 — «A total of 10,980 individuals were identified»
- n_responded: NR — Page 4 — «480 respondents were excluded»
- response_rate: NR — Page 4 — «A total of 10,980 individuals were identified»
- age_mean: 42.6 — Page 4 — «500 with self-reported tinnitus (365 males, 135 females; mean age = 42.6 ± 6.9 years)»
- age_sd: 6.9 — Page 4 — «mean age = 42.6 ± 6.9 years»
- age_min: 18 — Page 4, Eligibility Criteria — «between 18 and 50 years of age»
- age_max: 50 — Page 4, Eligibility Criteria — «between 18 and 50 years of age»
- age_group: adults — Page 4, Eligibility Criteria — «between 18 and 50 years of age»
- pct_female: 27.0 — Page 4 — «500 with self-reported tinnitus (365 males, 135 females»
- informant: self — Page 10, Limitations — «self-report measures may be influenced by recall bias or underreporting.»
- mode: mixed — Page 5, Assessment Tools — «administered either in paper or digital format, depending on accessibility.»
- instruments: Study-developed General Questionnaire with misophonia screening items (language NR); A-MISO-S (language NR; complete data n=7); S-Five (language NR); plus THI and TCHSQ (tinnitus) — Page 5, Assessment Tools; Page 8 — «Among a subset of participants with complete psychometric data (n = 7), ... the mean Amsterdam Misophonia Scale (A-MISO-S) score was 6.4 ± 2.3 (range = 3–10)»
- instrument_validated_in_language: NR — Page 5, Assessment Tools — «minor linguistic modifications were made to ensure clarity and contextual relevance for the Indian population»
- pub_status: preprint — Page 1 — «Research Article ... DOI: https://doi.org/10.21203/rs.3.rs-8333185/v1»
- language: English — Full text — «Prevalence of misophonia in the general population and those with complaints of tinnitus»
- funding_coi: No specific grant; no conflicts of interest — Page 11 — «This study did not receive any specific grant ... The authors declare that there are no conflicts of interest»
- notes: Treated as a separate sample from the normal-hearing group because eligibility differs (tinnitus with audiological confirmation) and the group size (500) looks fixed in advance. The report gives one combined recruitment pool, though, so the reviewer should confirm whether recruitment was separate. Table 1 accounts for only 159 tinnitus participants (74 without, 85 with misophonia). A-MISO-S data exist for only 7 cases. Possible overlap with other AIISH studies.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is people with tinnitus in India; the frame mixes audiology centres, community outreach and social media, with no defined patient frame — Page 4 — «community outreach programs, social media advertisements, and tertiary care audiology centers.»
2. способ отбора: **no** — Convenience recruitment; not consecutive or random — Page 4 — «identified through nationwide recruitment channels»
3. размер выборки: **yes** — n = 500 (≥139 clinical; ≥385) — Page 6 — «17% (85 of 500)»
4. описание выборки и условий: **unclear** — Age, sex, country and setting reported; dates not reported — Page 4 — «365 males, 135 females; mean age = 42.6 ± 6.9 years»
5. охват (пропуски): **unclear** — Table 1 accounts for only 159 (74 + 85) of the 500 tinnitus participants; A-MISO-S data complete for only 7 of 85 cases — Page 6, Table 1; Page 8 — «Among 74 tinnitus participants who did not meet criteria for misophonia ... a subset of participants with complete psychometric data (n = 7)»
6. валидность определения случая: **unclear** — Misophonia criteria not stated — Page 6 — «Within the tinnitus group, 17% (85 of 500) showed comorbid misophonia.»
7. единое надёжное измерение: **no** — Paper and online modes mixed with no check; no reliability in this sample — Page 5 — «administered either in paper or digital format, depending on accessibility.»
8. статистика (числитель и знаменатель): **unclear** — 85/500 is stated, but the non-case count (74) does not add up to 500, so the denominator is uncertain — Page 6-8 — «17% (85 of 500) ... Among 74 tinnitus participants who did not meet criteria for misophonia»
9. отклик: **no** — No denominator of invited people; no non-response handling — Page 4 — «A total of 10,980 individuals were identified through nationwide recruitment channels»

Правки:
- 

Проверено: да
---

## ST030 · Qiu 2025 · Frontiers in psychology

Основной отчёт R0385: [текст](../../fulltext/text/R0385.txt) — «Visual disgust constricts pupils in response to misophonic movies.» — [DOI](https://doi.org/10.3389/fpsyg.2025.1569598)
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R0314 (ST024), R0368 (ST027), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap
Расхождения в тексте: Exp 1 counts are internally consistent: 38+24+2+1=65 for sex; 41+24=65 for order; 13+13=26 misophonic; 28+11=39 controls. Exp 1 component counts (DVMSQ 22, MQ 19, S-Five 8) overlap and together give 26 positive on any criterion. Hearing tests were done on 21 of the 26 misophonic participants (26 minus 5 not tested). No table/text disagreements for the prevalence counts.
Заметка ИИ: Three separately recruited experiment samples from one report. Exp 2 and Exp 3 report DVMSQ 'misophonic' status without restating the threshold; L2 was assumed from Exp 1's DVMSQ definition (criteria A-E) and is flagged for review. The country (USA) is inferred from Carnegie Mellon University; it is not stated in the text. Instrument language is not stated. No funding statement in the supplied text.

### ST030-1 · Exp 1: Carnegie Mellon University and surrounding area, pupillometry experiment, n=65
Отчёты: R0385 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | multiple · clinical on any of DVMSQ (criteria A-E), MQ MSS>=7, S-Five>=87 | **L2** | **26 / 65** | 40.0 | 2.1.1 Participants | «A subset of 26 participants scored at the clinically significant level on the DVMSQ, MQ, and/or S-Five ... we classified participants as misophonic if they met the threshold on any of the three criteria.» |
| E2 | all | DVMSQ · DVMSQ algorithm: criteria A-E met (clinical) | **L2** | **22 / 65** | 33.8 | 2.1.1 Participants | «22 participants met the misophonia threshold on the DVMSQ, 19 on the MQ, and 8 on the S-Five» |
| E3 | all | MQ · MSS>=7 | **L2** | **19 / 65** | 29.2 | 2.1.1 Participants | «22 participants met the misophonia threshold on the DVMSQ, 19 on the MQ, and 8 on the S-Five» |
| E4 | all | S-Five · S-Five>=87 | **L2** | **8 / 65** | 12.3 | 2.1.1 Participants | «22 participants met the misophonia threshold on the DVMSQ, 19 on the MQ, and 8 on the S-Five» |

- E1: источник порога: developer paper; правило: G4 'A or B', all components L2 -> L2 (DVMSQ, MQ, S-Five rows); у авторов: «clinically significant level; classified as misophonic»; главная у авторов: yes; период: NR; заметка: Cut-off sources: DVMSQ Williams 2022 (developer), S-Five Vitoratou 2023, MQ MSS via Wu 2014.
- E2: источник порога: developer paper; правило: DVMSQ row; clinical algorithm; у авторов: «met the misophonia threshold on the DVMSQ»; главная у авторов: no; период: NR
- E3: источник порога: developer paper; правило: MQ row; MSS>=7; у авторов: «met the misophonia threshold on the MQ»; главная у авторов: no; период: NR
- E4: источник порога: validation paper; правило: S-Five row; >=87; у авторов: «met the misophonia threshold on the S-Five»; главная у авторов: no; период: NR

**Ключевые поля выборки:**
- **n_analysed: 65** — 2.1.1 Participants — «We recruited 65 participants ... A subset of 26 participants scored at the clinically significant level»
- **population: gp_other** — 2.1.1 Participants — «from Carnegie Mellon University and its surrounding area»
- **sampling: convenience** — 2.1.1 Participants — «We recruited 65 participants ... from Carnegie Mellon University and its surrounding area.»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — 2.1.1 Participants — «from Carnegie Mellon University and its surrounding area»
- setting: university/community (lab experiment at Carnegie Mellon University) — 2.1.1 Participants — «We recruited 65 participants ... from Carnegie Mellon University and its surrounding area.»
- data_years: NR — 2.1.1 Participants — «the sample likely reflects Carnegie Mellon University's 2024 student population»
- design: screening phase of experiment — 2.1.1 Participants — «Prior to participating in the study, participants completed a set of scales that evaluated sound sensitivity»
- topic_disclosed: NR — 2.1.1 Participants — «We recruited 65 participants ... from Carnegie Mellon University and its surrounding area.»
- inclusion_exclusion: Age 18-41 (pupillary reactivity); self-reported normal hearing and normal-to-corrected vision — 2.1.1 Participants — «Participants were between the ages of 18 and 41 due to known differences in pupillary reactivity... All participants reported having normal hearing and normal-…»
- n_invited: NR — NA
- n_responded: 65 — 2.1.1 Participants — «We recruited 65 participants»
- response_rate: NR — NA
- age_mean: 24.6 — 2.1.1 Participants — «MAGE = 24.6, SD = 5.9»
- age_sd: 5.9 — 2.1.1 Participants — «MAGE = 24.6, SD = 5.9»
- age_min: 18 — 2.1.1 Participants — «Participants were between the ages of 18 and 41»
- age_max: 41 — 2.1.1 Participants — «Participants were between the ages of 18 and 41»
- age_group: adults — 2.1.1 Participants — «Participants were between the ages of 18 and 41»
- pct_female: 58.5 — 2.1.1 Participants — «38 females, 24 males, 2 non-binary, 1 undisclosed»
- informant: self — 2.1.1 Participants — «participants completed a set of scales that evaluated sound sensitivity»
- mode: NR — 2.1.1 Participants — «Prior to participating in the study, participants completed a set of scales»
- instruments: DVMSQ (English, presumed); MQ incl. Misophonia Severity Scale (English, presumed); S-Five (English, presumed) — 2.1.1 Participants — «the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) Williams et al. (2022), the Misophonia Questionnaire (MQ) (Wu et al., 2014), and the S-Five (Vit…»
- instrument_validated_in_language: yes — 2.1.1 Participants — «using the established clinical cutoffs for each scale, following prior research»
- pub_status: journal — Header — «Frontiers in psychology; DOI: 10.3389/fpsyg.2025.1569598»
- language: English — Full text — «Visual disgust constricts pupils in response to misophonic movies»
- funding_coi: NR — NA
- notes: Possible overlap with R0314 (ST024), R0368 (ST027), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Recruitment method not described. The high misophonia proportion (26/65) and the group-comparison design suggest possible enrichment for misophonic participants; reviewer to check eligibility (E1). Country inferred from CMU (not stated). Language of instruments not stated. pct_female computed as 38/65. Age 18-41 is the eligibility range, not the observed range.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Recruitment frame (CMU and surrounding area) not described; no prevalence target stated. — 2.1.1 Participants — «We recruited 65 participants ... from Carnegie Mellon University and its surrounding area.»
2. способ отбора: **no** — Non-probability recruitment of paid volunteers for a lab experiment. — 2.1.1 Participants — «compensated in cash according to an approved protocol»
3. размер выборки: **no** — n = 65 < 385. — 2.1.1 Participants — «We recruited 65 participants»
4. описание выборки и условий: **unclear** — Age, sex and setting given; country implicit; dates of data collection not reported. — 2.1.1 Participants — «MAGE = 24.6, SD = 5.9; 38 females, 24 males»
5. охват (пропуски): **yes** — All 65 classified (26 misophonic + 39 control across orders). — 2.1.3 Procedure — «order USNV-first (N= 41, 13 misophonic, 28 control) or order USUV-first (N = 24, 13 misophonic, 11 control)»
6. валидность определения случая: **yes** — Primary definition = clinical on any of DVMSQ algorithm, MQ MSS>=7, S-Five>=87; all are listed anchored cut-offs in original-language versions. — 2.1.1 Participants — «meeting criteria A-E on the DVMSQ, a score of ≥7 on the Misophonia Severity Scale from the MQ, and ≥87 out of 250 on the S-Five»
7. единое надёжное измерение: **unclear** — Same instruments for all, but mode and reliability not reported. — 2.1.1 Participants — «participants completed a set of scales that evaluated sound sensitivity»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator clear (26/65); CI calculable. — 2.1.1 Participants — «A subset of 26 participants scored at the clinically significant level»
9. отклик: **unclear** — No information on number invited or response. — 2.1.1 Participants — «We recruited 65 participants»

Правки:
- 

Проверено: да
### ST030-2 · Exp 2: Carnegie Mellon University students, online silent-movie ratings, n=22
Отчёты: R0385 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DVMSQ · DVMSQ 'misophonic' (presumably algorithm criteria A-E as in Exp 1; not restated) | **L2** | **1 / 22** | 4.5 | 3.1.3 Procedure | «One of the 22 participants was misophonic.» |

- E1: источник порога: developer paper; правило: DVMSQ row; clinical algorithm (assumed from Exp 1); у авторов: «misophonic»; главная у авторов: yes; период: NR; заметка: Threshold not stated in Exp 2; reviewer to confirm L2 vs NR (G6).

**Ключевые поля выборки:**
- **n_analysed: 22** — 3.1.3 Procedure — «One of the 22 participants was misophonic.»
- **population: university_students** — 3.1.1 Participants — «We recruited a new group of 22 participants ... from the student population of Carnegie Mellon University.»
- **sampling: convenience** — 3.1.1 Participants — «compensated with course credit»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — 3.1.1 Participants — «from the student population of Carnegie Mellon University»
- setting: university (student pool, online via Qualtrics) — 3.1.1; 3.1.3 — «Participants completed the experiment using their personal computers through the Qualtrics platform.»
- data_years: NR — NA
- design: screening phase of experiment — 3.1.3 Procedure — «Next, they completed the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ)»
- topic_disclosed: NR — NA
- inclusion_exclusion: Screening for normal hearing; all included regardless of DVMSQ; failed catch trial excluded — 3.1.3 Procedure — «As we recruited from a general population, all participants were included regardless of their DVMSQ score.»
- n_invited: NR — NA
- n_responded: 22 — 3.1.1 Participants — «a new group of 22 participants»
- response_rate: NR — NA
- age_mean: 19.2 — 3.1.1 Participants — «MAGE = 19.2; Range = 18 to 22 years old»
- age_sd: NR — NA
- age_min: 18 — 3.1.1 Participants — «Range = 18 to 22 years old»
- age_max: 22 — 3.1.1 Participants — «Range = 18 to 22 years old»
- age_group: adults — 3.1.1 Participants — «Range = 18 to 22 years old»
- pct_female: 54.5 — 3.1.1 Participants — «12 females, 9 males, 1 undisclosed»
- informant: self — 3.1.3 Procedure — «they completed the Duke-Vanderbilt Misophonia Screening Questionnaire»
- mode: online — 3.1.3 Procedure — «using their personal computers through the Qualtrics platform»
- instruments: DVMSQ (English, presumed) — 3.1.3 Procedure — «Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) Williams et al. (2022)»
- instrument_validated_in_language: yes — 3.1.3 Procedure — «Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) Williams et al. (2022)»
- pub_status: journal — Header — «Frontiers in psychology»
- language: English — Full text — «Visual disgust constricts pupils in response to misophonic movies»
- funding_coi: NR — NA
- notes: Possible overlap with R0314 (ST024), R0368 (ST027), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Recruited separately from Exp 1 ('new group'). Catch-trial exclusions not counted; unclear whether 22 is before or after exclusion. DVMSQ case definition not restated for Exp 2 (Exp 1 used criteria A-E). pct_female computed as 12/22.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — CMU student pool; frame not described. — 3.1.1 Participants — «from the student population of Carnegie Mellon University»
2. способ отбора: **no** — Course-credit volunteers, non-probability. — 3.1.1 Participants — «compensated with course credit»
3. размер выборки: **no** — n = 22 < 385. — 3.1.1 Participants — «a new group of 22 participants»
4. описание выборки и условий: **unclear** — Age, sex and setting given; dates not reported. — 3.1.1 Participants — «MAGE = 19.2; Range = 18 to 22 years old, 12 females, 9 males, 1 undisclosed»
5. охват (пропуски): **unclear** — Catch-trial exclusions not quantified. — 3.1.3 Procedure — «The data of participants who failed to correctly answer the catch trials were excluded.»
6. валидность определения случая: **unclear** — DVMSQ used, but threshold for 'misophonic' not stated for this experiment. — 3.1.3 Procedure — «One of the 22 participants was misophonic.»
7. единое надёжное измерение: **unclear** — Same online instrument for all; reliability not reported. — 3.1.3 Procedure — «they completed the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ)»
8. статистика (числитель и знаменатель): **yes** — 1/22 traceable. — 3.1.3 Procedure — «One of the 22 participants was misophonic.»
9. отклик: **unclear** — No invited denominator. — 3.1.1 Participants — «We recruited a new group of 22 participants»

Правки:
- 

Проверено: да
### ST030-3 · Exp 3: Carnegie Mellon University students and faculty, online sound ratings, n=21
Отчёты: R0385 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DVMSQ · DVMSQ 'misophonic' (presumably algorithm criteria A-E as in Exp 1; not restated) | **L2** | **0 / 21** | 0.0 | 4.1.3 Procedure | «None of the participants were misophonic.» |

- E1: источник порога: developer paper; правило: DVMSQ row; clinical algorithm (assumed from Exp 1); у авторов: «misophonic»; главная у авторов: yes; период: NR; заметка: Threshold not stated in Exp 3; reviewer to confirm L2 vs NR (G6).

**Ключевые поля выборки:**
- **n_analysed: 21** — 4.1.3 Procedure — «None of the participants were misophonic.»
- **population: other_nonclinical** — 4.1.1 Participants — «recruited from the student and faculty populations of Carnegie Mellon University»
- **sampling: convenience** — 4.1.1 Participants — «compensated in cash»

**Остальные поля:**
- clinical_group: NA — NA
- country: USA — 4.1.1 Participants — «from the student and faculty populations of Carnegie Mellon University»
- setting: university (students and faculty, online via Qualtrics) — 4.1.1; 4.1.3 — «Participants completed the experiment using their personal computers through the Qualtrics platform.»
- data_years: NR — NA
- design: screening phase of experiment — 4.1.3 Procedure — «Next, they completed the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ)»
- topic_disclosed: NR — NA
- inclusion_exclusion: Screening for normal hearing; all included regardless of DVMSQ; failed catch trial excluded — 4.1.3 Procedure — «all participants were included regardless of DVMSQ score»
- n_invited: NR — NA
- n_responded: 21 — 4.1.1 Participants — «A new group of 21 participants»
- response_rate: NR — NA
- age_mean: 21.21 — 4.1.1 Participants — «MAGE = 21.21, SD = 4.47»
- age_sd: 4.47 — 4.1.1 Participants — «MAGE = 21.21, SD = 4.47»
- age_min: NR — NA
- age_max: NR — NA
- age_group: NR — 4.1.1 Participants — «MAGE = 21.21, SD = 4.47»
- pct_female: 57.1 — 4.1.1 Participants — «12 females, 9 males»
- informant: self — 4.1.3 Procedure — «they completed the Duke-Vanderbilt Misophonia Screening Questionnaire»
- mode: online — 4.1.3 Procedure — «using their personal computers through the Qualtrics platform»
- instruments: DVMSQ (English, presumed) — 4.1.3 Procedure — «Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) Williams et al. (2022)»
- instrument_validated_in_language: yes — 4.1.3 Procedure — «Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) Williams et al. (2022)»
- pub_status: journal — Header — «Frontiers in psychology»
- language: English — Full text — «Visual disgust constricts pupils in response to misophonic movies»
- funding_coi: NR — NA
- notes: Possible overlap with R0314 (ST024), R0368 (ST027), R0910 (ST067): Carnegie Mellon University experiments of one lab; separate experiments and years, participant pools may overlap. Includes faculty as well as students (population coded other_nonclinical). Age range not reported (adult status not stated). Catch-trial exclusions not counted. DVMSQ threshold not restated. pct_female computed as 12/21.

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — Frame (CMU students and faculty) not described. — 4.1.1 Participants — «recruited from the student and faculty populations of Carnegie Mellon University»
2. способ отбора: **no** — Paid volunteers, non-probability. — 4.1.1 Participants — «compensated in cash»
3. размер выборки: **no** — n = 21 < 385. — 4.1.1 Participants — «A new group of 21 participants»
4. описание выборки и условий: **unclear** — Age, sex and setting given; dates not reported. — 4.1.1 Participants — «MAGE = 21.21, SD = 4.47; 12 females, 9 males»
5. охват (пропуски): **unclear** — Catch-trial exclusions not quantified. — 4.1.3 Procedure — «The data of participants who failed to correctly answer the catch trials were excluded.»
6. валидность определения случая: **unclear** — DVMSQ used; threshold for 'misophonic' not stated in this experiment. — 4.1.3 Procedure — «None of the participants were misophonic.»
7. единое надёжное измерение: **unclear** — Same instrument for all; reliability not reported. — 4.1.3 Procedure — «they completed the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ)»
8. статистика (числитель и знаменатель): **yes** — 0/21 traceable. — 4.1.3 Procedure — «None of the participants were misophonic.»
9. отклик: **unclear** — No invited denominator. — 4.1.1 Participants — «A new group of 21 participants»

Правки:
- 

Проверено: да