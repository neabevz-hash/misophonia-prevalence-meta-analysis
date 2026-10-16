# Повторный отбор вслепую, часть 6

Записи 751–790 из 790: всё, что ИИ исключил, кроме калибровочной выборки. Повторный отбор вслепую по правилу защиты (протокол, §11b). **Меток и причин ИИ в этом файле нет** — решайте с нуля по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261011).

**Быстрый режим:** достаточно одного символа — `+`, `?` или просто `-` (исключить, причина не нужна). Заметки не нужны. Если по названию всё ясно, аннотацию можно не читать.

**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: исследование может дать долю людей с мизофонией в выборке, набранной **не** из-за мизофонии |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
| `-1` | исключить: обзор, редакционная статья, комментарий, письмо без данных |
| `-2` | исключить: клинический случай или серия случаев |
| `-3` | исключить: выборка набрана из-за мизофонии или чувствительности к звукам |
| `-4` | исключить: нет инструмента именно для мизофонии (гиперакузия, шумочувствительность…) |
| `-5` | исключить: качественное, теоретическое, на животных, не эмпирическое |
| `-6` | исключить: не про мизофонию |
| `-7` | исключить: другое — напишите почему |

Пример: `**Решение:** -4 только гиперакузия`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Что включаем:** опросы распространённости; опросы студентов, школьников, работников, общих выборок со шкалой мизофонии (A-MISO-S, AMISOS-R, MQ, MisoQuest, S-Five, DMQ, DVMSQ, BMQ-R, SMS, MAQ, NYMS, свои вопросы) или интервью; валидации шкал на неклинических выборках; клинические группы, набранные по другому поводу (ОКР, тревога, депрессия, СДВГ, аутизм, тики, тиннитус, гиперакузия…), если мизофонию измеряли; эксперименты, где сначала просеяли ненабранный пул; диссертации, препринты, постеры и тезисы любого из этого. Подробно — протокол, §8.

---

### 751 · R0491

**Perceived Negative Effects of Tic Management Strategies in Adults With Tic Disorders.**

2024 · Behavior modification · journal article, randomized controlled trial, research support, n.i.h., extramural · eng · https://doi.org/10.1177/01454455241236446

Behavior therapy is a well-established and empirically supported treatment for tic disorders (TDs). However, concerns have been expressed about the negative effects of behavioral interventions, such as tic worsening, tic substitution, and excessive effort. This study explored perceived negative effects of tic management strategies in adults with TDs and predictors of these experiences. Participants (N = 72) completed semi-structured interviews 11 years after receiving behavior therapy or supportive therapy in a randomized clinical trial. We examined responses to interview questions about managing tics and predictors of reported negative effects. Most participants did not experience tic worsening (84%) or tic substitution (75%) from tic management strategies. The majority felt they could manage tics while participating in their environment (87%) and did not report life interference from tic management (77%). About half (45%) felt less present when managing tics. Treatment non-responders in the original trial were more likely to report negative effects of tic management strategies. No differences in reported negative consequences were found between those who received behavior therapy versus supportive therapy, suggesting that behavior therapy specifically does not lead to such adverse effects. These findings could reduce misconceptions about behavior therapy for TDs and enhance its acceptability and utilization.

**Решение:** -6 не про мизофонию

---

### 752 · R1511

**TRT: efficacité après un an de traitement.**

2007 · review

INTRODUCTION: Tinnitus Retraining Therapy (TRT) (which aims to induce changes in the mechanisms responsible for transferring signals from the auditory system to the limbic and autonomic systems) is a method for treating Tinnitus and decreased sound tolerance. An individualised explanation of Jastreboff's neurophysiological model allows greater insight and motivation on the part of the patient. Previous studies have demonstrated that daytime TRT is effective. As sleep forms a significant component of the distress associated with Tinnitus however, we hypothesised that night-time TRT could represent a useful tool in the treatment of this disabling condition. MATERIAL AND METHODS: 46 patients were studied (30 male, 16 female). Patients were selected from an ENT outpatient clinic. Patients with significant psychological disability were excluded. Patients were reviewed twice by their doctor and 5 times by a therapist over 12 months. Treatment consisted of 8 hours nighttime white noise stimulation, at progressively increasing intensity. Although several objective assessments of response were undertaken, patients' subjective testimonies were considered a more accurate signal of success. RESULTS: In total, 80% of patients had a satisfactory response after 1 year of treatment. 20% had no response. Patients were subcategorised according to Jastreboff's categories as follows: 1. Tinnitus (n = 6), 100% improved; 2. Tinnitus with hearing loss (n = 16); 62% improved; 3. Hyperacusis (with or without Tinnitus) (n = 16), 88.5% improved; 4. Hyperacusis (with or without Tinnitus, exacerbated by noise) (n = 8), 75% improved. CONCLUSION: Tinnitus is a symptom rather than an illness, and TRT gives patients greater control, allowing re-integration of normal perception. Night-time TRT is an effective treatment for Tinnitus and decreased sound tolerance. It has the potential advantage over day-time TRT of rapidly improving sleep and decreasing use of sedative hypnotics, a secondary effect noted in the personal testimonies of our cohort of patients. Further studies are needed to confirm this advantage, in view of the significant risks associated with long-term use of benzodiazepines. When investigating therapies for Tinnitus, it is necessary to measure success in terms of quality of life, as it is to this that the patient attaches the most importance

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 753 · R0790

**Psychiatric Comorbidities in Hyperacusis and Misophonia: A Systematic Review Protocol**

2023 · European psychiatry : the journal of the Association of European Psychiatrists · abstract, article, review · eng · https://doi.org/10.1192/j.eurpsy.2023.2196

INTRODUCTION: Decreased sound tolerance amongst individuals can be divided into two conditions: Hyperacusis and Misophonia. Hyperacusis is the perception of certain everyday sounds as too loud or painful. Misophonia is characterized by heightened emotional reaction to a sound with a specific pattern and/or meaning to an individual, with the context in which occurs being relevant. Scattered evidence from clinical research suggests that Hyperacusis and Misophonia can co-occur with a wide range of psychiatric disorders. These factors can have an impact on the severity of the symptoms and subsequently, in the clinical management of these patients. A better understanding these comorbid conditions is important as it could help to clarify its underlying mechanisms and ultimately, to improve the care of these patients. Despite this, no attempt has been made to synthesize the spectrum of such co-occurring disorders. OBJECTIVES: To conduct a systematic review of the available evidence on the prevalence of psychiatric disorders in patients with Hyperacusis and Misophonia, and to explore which factors may influence prevalence estimates. METHODS: Preferred Reporting Items for systematic Reviews and Meta-Analyses (PRISMA) and Meta-analyses of Observational Studies in Epidemiology (MOOSE) recommendations will be followed. The CoCoPop (Condition, Context and Population) framework was used to develop the review question. Pubmed, PsycINFO, Scopus and Web of Science electronic databases will be searched, as well as grey literature, using key-terms in accordance with the pre-established research question. Additional manual searches will also be conducted. Searches will be limited to human studies and no date, language or country origin restrictions will be applied. Outcomes of interest will be the occurrence of comorbid psychiatric disorders in patients with Hyperacusis and Misophonia that are reported according to validated assessment methods. Retrieved records will be screened for eligibility by two independent reviewers using a two-phase approach (title and abstracts screening and full-text review). The methodological quality of primary studies will be assessed using the Joanna Briggs Institute (JBI) – Critical Appraisal Tools, depending on study design, and data will be extracted independently using a standardized extraction form. RESULTS: Quantitative data will be synthetized and presented in text and tabular format. Studies heterogeneity will be verified and if feasible, a meta-analysis will be conducted. CONCLUSIONS: It is expected that this systematic review will provide evidence of a significant prevalence of a wide range of psychiatric comorbidities in patients with Hyperacusis and Misophonia, supporting the importance of screening these patients for psychiatric disorders. DISCLOSURE OF INTEREST: None Declared

**Решение:** -7 protocol / preregistration without data

---

### 754 · R1454

**Selecting and optimising hearing aids for tinnitus benefit: a rough guide**

2014 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 755 · R0966

**Neuroticism Drives Associations Between Repetitive Behaviors and Depression in Autistic Adults**

2022 · Frontiers in Psychiatry · article · und · https://doi.org/10.3389/fpsyt.2022.803361

Depression is more prevalent among autistic adults than neurotypical adults, yet risk factors are incompletely understood in this population. Some research groups have focused on relationships between negative repetitive thinking and depression in the autistic population, which may explain elevated prevalence rates in line with general population findings on rumination and internalizing disorders. Little is known about associations between depression and more prototypical repetitive cognitions and/or behaviors characteristic of autism (i.e., insistence on sameness [IS] and repetitive sensorimotor [RSM] behaviors). Therefore, the present study aimed to examine associations between IS, RSM behaviors, and depressive symptoms in 762 autistic adults, and whether observed effects are confounded by additional factors (e.g., demographic factors, trait neuroticism). To test if greater IS scores were associated with greater depressive symptoms on the BDI-II, a Bayesian linear regression was conducted with BDI-II scores (dependent variable) regressed on age, gender, educational level, RSM scores, and IS scores (independent variables). To test the effects of neuroticism on observed relationships, a second regression was conducted that included all predictors from the baseline model and neuroticism. Standardized regression coefficients were tested against an interval null hypothesis of [−0.1, 0.1] to assess for practical significance. Results indicated that IS exhibited a moderate positive relationship with depressive symptoms, while RSM behaviors provided only a slight increase in predictive ability. However in the second model, neuroticism exhibited a strong positive relationship with depressive symptoms, completely attenuating the effect of IS. Associations between RSM behaviors and depressive symptoms did not meet our criteria for practical significance, particularly when neuroticism was added to the model. Neither RSM nor IS moderated the effect of neuroticism on depression. The findings from this study add to the literature on risk factors in the pathway to depression in autism, and suggest opportunities for clinical translation to screening and intervention efforts. Screening for IS in autistic individuals is a common diagnostic practice in clinical and research settings that may be leveraged to also identify those at higher risk for depression, and increasing flexibility in daily life may promote emotional regulation and distress tolerance.

**Решение:** -6 не про мизофонию

---

### 756 · R0595

**Did Kant suffer from misophonia?**

2024 · Frontiers in psychology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyg.2024.1242516

Misophonia is a disorder of decreased tolerance to specific sounds, often produced by humans but not always, which can trigger intense emotional reactions (anger, disgust etc.). This relatively prevalent disorder can cause a reduction in the quality of life. The causes of misophonia are still unclear. In this article, we develop a hypothesis suggesting that misophonia can be caused by a failure in the organization of the perceived world. The perceived world is the result of both the structure of human thought and the many conditioning factors that punctuate human life, particularly social conditioning. It is made up of abstract symbols that map the world and help humans to orient himself in a potentially dangerous environment. In this context, the role of social rules acquired throughout life is considerable. Table manners, for example, are a set of deeply regulated and controlled behaviors (it's considered impolite to eat with the mouth open and to make noise while eating), which contribute to shape the way the perceived world is organized. So it's not surprising to find sounds from the mouth (chewing etc.) among the most common misophonic sound triggers. Politeness can be seen as an act of obedience to moral rules or courtesy, which is a prerequisite for peaceful social relations. Beyond this example, we also argue that any sound can become a misophonic trigger as long as it is not integrated into the perceived ordered and harmonious world, because it is considered an "anomaly," i.e., a disorder, an immorality or a vulgarity.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 757 · R0319

**More relaxing than nature? The impact of ASMR content on psychological and physiological measures of parasympathetic activity**

2025 · Neuroscience of Consciousness · article · en · https://doi.org/10.1093/nc/niaf012

Autonomous sensory meridian response (ASMR) is a sensory-emotional phenomenon characterized by distinct tingling sensations and a sense of relaxation induced by specific auditory and visual stimuli. Although ASMR is recognized as a cross-modal experience, psychological and physiological mechanisms behind ASMR remain only partially understood. Across two experiments, we investigated these mechanisms. Experiment 1 showed that ASMR videos with combined audiovisual content elicited stronger tingling sensations than those with auditory-only content, suggesting an additive effect through sensory processing. In Experiment 2, we measured responses to ASMR and nature videos using finger photoplethysmography (PPG) and found that both types of videos reduced pulse rates compared to rest. Notably, ASMR videos caused a greater reduction in pulse rate than nature videos. These findings are discussed in relation to autonomic nervous system activation, cross-modal interactions, and the social grooming hypothesis, which posits that ASMR may replicate comforting effects of social bonding behaviors, such as grooming.

**Решение:** -6 не про мизофонию

---

### 758 · R0038

**Normative Ranges for Wideband Middle Ear Muscle Reflex Magnitude: Limited Potential for Diagnosing Cochlear Deafferentation.**

2026 · American journal of audiology · article, dataset/dataset, journal article · eng · https://doi.org/10.1044/2025_aja-25-00241

Abstract Purpose Cochlear synaptopathy, the loss of the synapses between the inner hair cells and their auditory nerve fiber targets, is expected to be a common type of auditory deficit resulting from noise exposure or aging. Unfortunately, there is currently no means for diagnosing cochlear synaptopathy or other forms of cochlear deafferentation. Wideband middle ear muscle reflexes (MEMRs) have been proposed as a potential diagnostic indictor of cochlear deafferentation, but we lack normative ranges for MEMR magnitude. The objective of this study was to develop normative ranges for wideband MEMR magnitude that can be used to identify patients with abnormally weak MEMRs. Method Normative ranges were generated for ipsilateral and contralateral wideband MEMR magnitude in a population at low risk for cochlear synaptopathy due to young age, normal hearing thresholds, and minimal noise exposure history. The normative ranges were statistically adjusted for average distortion product otoacoustic emission (DPOAE) levels to account for possible impacts of outer hair cell dysfunction. To evaluate the ability of the normative ranges to differentiate between populations at low versus high risk of synaptopathy, measurements were also collected from military Veterans with normal hearing thresholds who reported at least one of the auditory complaints predicted to result from synaptopathy – tinnitus, speech perception in noise difficulty, or decreased sound tolerance. Results For individuals with poorer DPOAEs, it is not possible to fall below the lower bounds of the wideband MEMR normative ranges. For individuals with more robust DPOAEs, the lower bounds are very close to an MEMR magnitude indicating an absent reflex. Few individuals from the high-risk sample fell below the normative ranges, suggesting that these normative ranges do not identify significant cochlear deafferentation as expected. Conclusions Wideband MEMR magnitude normative ranges will not be effective as a stand-alone indicator of cochlear deafferentation.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 759 · R0687

**Misophonia Sound Recognition Using Vision Transformer.**

2023 · Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Annual International Conference · article, conference object, journal article · eng · https://doi.org/10.1109/embc40787.2023.10340283

Misophonia is a condition characterized by an abnormal emotional response to specific sounds, such as eating, breathing, and clock ticking noises. Sound classification for misophonia is an important area of research since it can benefit in the development of interventions and therapies for individuals affected by the condition. In the area of sound classification, deep learning algorithms such as Convolutional Neural Networks (CNNs) have achieved a high accuracy performance and proved their ability in feature extraction and modeling. Recently, transformer models have surpassed CNNs as the dominant technology in the field of audio classification. In this paper, a transformer-based deep learning algorithm is proposed to automatically identify trigger sounds and the characterization of these sounds using acoustic features. The experimental results demonstrate that the proposed algorithm can classify trigger sounds with high accuracy and specificity. These findings provide a foundation for future research on the development of interventions and therapies for misophonia.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 760 · R1341

**Therapist-rated Engagement and Compliance as Proxies for Treatment Success: A Bayesian Mediation Analysis of Exposure and Stress Management for Adults with Misophonia**

2017 · Fordham Research Commons (Fordham University) · dissertation, text · en

Previous research has found that treatment engagement and compliance predict better outcomes for a number of mental health symptoms. These common factors may contribute over and above the particular effects of specific psychotherapeutic interventions. This study assessed whether therapist-rated engagement and treatment compliance mediated outcome in a randomized controlled trial (RCT) of exposure and stress management for adults with misophonia (selective sound aversion). A theoretical pathway was proposed in which engagement and treatment compliance would increase inhibitory learning, foster distress tolerance and reduce anxiety sensitivity, and mediate clinical outcome. Participants (n = 18) received six sessions of exposure and six session of stress management over six weeks. Study therapists rated engagement and treatment compliance after sessions 2, 4, 6, 8, 10 and 12. Bayesian mediation analysis was conducted on misophonia symptoms, behaviors, and severity ratings, as well as secondary outcome measures. None of the initial models converged. However, employing a sample simulated from the models’ correlation matrix (n = 100), posterior probabilities were computed for path alpha, beta, tau, and full mediation. Bayesian credible intervals suggested that engagement and treatment compliance were not significant mediators. Further, Bayes factors (\u3c 0.33) supported the null hypothesis for primary outcomes. This could suggest that technical aspects of cognitive-behavioral therapy were sufficient to produce change in our sample. However, there were several limitations including sample size, a lack of psychometric evidence, and the potential for rater error. In addition, there was some evidence for a nonlinear mediational pathway. Future studies should be conducted on this topic with larger samples

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 761 · R1042

**Tinnitus, Hyperacusis, Otalgia, and Hearing Loss.**

2021 · Continuum (Minneapolis, Minn.) · article, other literature type, journal article · eng · https://doi.org/10.1212/con.0000000000000961

ABSTRACT PURPOSE OF REVIEW This article reviews the causes of tinnitus, hyperacusis, and otalgia, as well as hearing loss relevant for clinicians in the field of neurology. RECENT FINDINGS Important causes of unilateral and bilateral tinnitus are discussed, including those that are treatable or caused by serious structural or vascular causes. Concepts of hyperacusis and misophonia are covered, along with various types of neurologic disorders that can lead to pain in the ear. Hearing loss is common but not always purely otologic. SUMMARY Tinnitus and hearing loss are common symptoms that are sometimes related to a primary neurologic disorder. This review, tailored to neurologists who care for patients who may be referred to or encountered in neurology practice, provides information on hearing disorders, how to recognize when a neurologic process may be involved, and when to refer to otolaryngology or other specialists.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 762 · R1486

**[Decreased sound tolerance and tinnitus].**

2012 · Lin chuang er bi yan hou tou jing wai ke za zhi = Journal of clinical otorhinolaryngology head and neck surgery · article, english abstract, journal article · chi · https://pubmed.ncbi.nlm.nih.gov/23285963/

Decreased sound tolerance includes hyperacusis and/or misphobia (phonophobia). As a commonly subjective symptom, tinnitus is defined to be a sound perceived in the ear or head without corresponding sound or electrical stimulus in the surrounding environment. It is usually occurred with or without hearing loss or harmful psychic reaction, which includes dyssomnia, annoy, rage, anxiety, depress, hard to concentrate, etc. Frequently, tinnitus is accompanied by decreased sound tolerance, while this text is aimed to review the correlated concepts of decreased sound tolerance,and focus on the hyperacusis which is a more common symptom.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 763 · R0867

**The Ethics of Translational Audiology.**

2022 · Audiology research · article, conference object, journal article · eng · https://doi.org/10.3390/audiolres12030028

Translational research moves promising primary research results from the laboratory to practical application. The transition from basic science to clinical research and from clinical research to routine healthcare applications presents many challenges, including ethical. This paper addresses issues in the ethics of translational audiology and discusses the ethical principles that should guide research involving people with hearing loss. Four major ethical principles are defined and explained, which are as follows: beneficence, nonmaleficence, autonomy, and justice. In addition, the authors discuss issues of discrimination and equal access to medical services among people with hearing loss. Despite audiology's broad field of interest, which includes evaluation and treatment of auditory disorders (e.g., deafness, tinnitus, misophonia, or hyperacusis) and balance disorders, this study focuses primarily on deafness and its therapies.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 764 · R0451

**When Everyday Sounds Become Barriers: The Effect of Misophonia on Speech Perception.**

2025 · Brain and behavior · article, journal article, journalarticle · eng · https://doi.org/10.1002/brb3.70924

ABSTRACT Introduction Misophonia is a condition characterized by intense emotional reactions, such as anger, anxiety, or disgust, in response to specific sounds. This study aims to investigate the speech perception performance in noise of individuals with misophonia. Recent perspectives suggest that these emotional reactions may interfere with auditory attention, particularly in socially relevant listening situations. However, little is known about how misophonia affects speech perception in noisy environments. Methods The study included 40 individuals with misophonia and 40 healthy controls, matched for age and gender. Both groups were administered the Hearing in Noise Test (HINT) under two different scenarios: one with speech noise only and another with speech noise combined with the triggering sound of a buzzing fly. The fly sound was identified as aversive by all participants with misophonia. Speech perception performances in noise of the groups across the two scenarios were compared. Results The findings revealed that the presence of a triggering sound significantly impaired the speech perception ability in noise in individuals with misophonia. The misophonia group demonstrated lower performance in the presence of the triggering sound compared to the control group. Additionally, increased severity of misophonia and a greater number of triggering sounds were associated with further declines in HINT performance. Conclusion This study highlights that misophonia is a condition that adversely affects speech perception in noise. Understanding the communication challenges faced by individuals with misophonia in noisy environments provides a crucial foundation for the assessment of this disorder and the development of therapeutic interventions.

**Решение:** ? речевое восприятие (40 с мизофонией vs 40 контроль), проверить скрининг пула

---

### 765 · R0342

**Severe tinnitus: how can we approach it?**

2025 · Singapore Medical Journal · article · en · https://doi.org/10.4103/singaporemedj.smj-2025-073

INTRODUCTION Tinnitus, the perception of sound without an external source, is a prevalent condition affecting approximately 20% of people worldwide, with 2%–4% experiencing significant distress.[1] Commonly described as ringing, buzzing, hissing, whistling or whooshing sounds, tinnitus is also notable in Singapore, where a community screening programme reported a prevalence of 17% among seniors aged 60 and above.[2] Despite its widespread occurrence, the experience of tinnitus varies greatly. While most individuals can cope with the condition, a small percentage find tinnitus highly distressing. This raises an important question: why do some individuals adapt effortlessly, while others struggle with significant psychological and emotional distress? Tinnitus is associated with a variety of conditions affecting both the peripheral and central auditory systems. It often coexists with hearing loss. However, many individuals with hearing loss do not experience tinnitus, and some patients with tinnitus exhibit no measurable hearing loss. Interestingly, the severity of tinnitus distress is not strongly correlated with its audiological characteristics, such as pitch, loudness or minimum masking levels. These traditional measures fail to capture the subjective aspects of tinnitus, which are more reflective of the level of distress and need for intervention. This suggests that the psychological response to tinnitus, rather than its sensory features, plays a key role in determining the individual impact. METHODS A retrospective study was carried out in a public hospital in Singapore to determine the key factors associated with patients distressed by tinnitus. The data of tinnitus patients who were referred to the audiology department for tinnitus management from 2016 to 2019 were analysed. This study was approved by the Ethics Committee of the National Healthcare Group Domain Specific Review Board (DSRB Ref No.: 2020/00745). All patients filled out the Tinnitus Handicap Inventory (THI) and tinnitus questionnaire as a part of their first tinnitus management session. The THI is a self-reported measure to evaluate the perceived severity of tinnitus and quantify its impact on a patient’s quality of life. It contains 25 items grouped into catastrophic, emotional and functional subscales. The overall score ranges from 0 to 100 and is categorised into five grades of tinnitus severity. A score of 0–16 indicates slight/no handicap, 18–36 indicates mild handicap, 38–56 indicates moderate handicap, 58–76 indicates severe handicap, and 78–100 indicates catastrophic handicap.[3] The tinnitus questionnaire contains questions on the characteristics of the tinnitus. Information on ear symptoms such as ear pain, ear fullness or muffed hearing were solicited. Patients were also asked if they experienced hyperacusis or sound intolerance, recent personal stressors or sleep disturbances. Age, gender, ethnic group and audiometric data were recorded as baseline information. Data from the questionnaires were extracted and tabulated. During data extraction, no patient identifiers were extracted. Anonymisation involves using a random serial number for each patient and de-linking the anonymised data from the collated data. RESULTS From January 2016 to September 2019, 4356 patients attended the Ear, Nose and Throat (ENT) Clinic at Ng Teng Fong General Hospital with otological complaints as the primary concern. Of these, 760 reported tinnitus, and 208 (27.4%) were referred to the tinnitus clinic for management. Prior to their referral, patients would have been examined by an ENT specialist. Patients with medically treatable tinnitus or underlying psychiatric conditions were not referred to the tinnitus clinic and therefore excluded from this study. The median age of the referred patients was 52 ± 16 years (range 18–88), and 52% of patients were male. Audiometric data revealed that 42% had normal hearing, while 58% had hearing loss of varying degrees. Among those with hearing loss, 74% exhibited bilateral sensorineural high-frequency loss, and eight patients had conductive hearing loss. Tinnitus was bilateral in 50% of cases and unilateral in the rest. Tinnitus characteristics were described by patients as high-pitched ringing (54%), cricket-like sound (24%), and other sounds such as buzzing, hissing or roaring (23%). Aural symptoms such as aural fullness and otalgia were reported by 13% of patients, and 8% experienced sound intolerance or hyperacusis, with sounds such as traffic sounds or children crying being triggers. Additionally, 48% and 42% of patients reported personal stressors and sleep disturbances, respectively. Of the 208 patients, 201 completed the THI questionnaire (seven patients could not understand the questions). Among these, 54% had a slight or mild tinnitus handicap, 27% had a moderate handicap, 10% had a severe handicap, and 9% had a catastrophic handicap. Analysis of THI responses revealed that feelings of frustration (30.7%) and feeling upset (28.8%) were the most common emotion reactions. On the catastrophic subscale, 55% felt a loss of control, and 42% felt trapped by the condition. Severe tinnitus-related distress, as indicated by THI scores of 58 and above, was found to be associated with specific factors. Patients presenting with difficulty coping with life stressors and having sleep disturbances had significantly higher THI scores. No significant associations were observed between severe tinnitus distress and gender, hearing status, nature of tinnitus sounds, presence of hyperacusis or other aural symptoms. Multivariate logistic regression showed that patients experiencing life stressors were 3.4 times more likely to report severe tinnitus distress (adjusted odds ratio [AOR] 3.4, 95% confidence interval [CI] 1.54–7.46), while those with sleep disturbances had a 2.8 times higher likelihood of reporting severe distress (AOR 2.79. 95% CI 1.28–6.06) [Table 1]. Among patients with severe distress, 73% experienced life stressors and 71% insomnia. Comparatively, only 15% of patients with severe tinnitus distress reported hyperacusis, or intolerance to everyday sounds. This underscores the importance of emotional factors in tinnitus distress.Table 1: Factors associated with severe tinnitus distress.DISCUSSION Notwithstanding its retrospective design, which precludes establishing causality between factors and severe tinnitus distress, and its reliance on self-reported measures such as the THI, this study provides important insights into the factors driving severe tinnitus distress. Our findings reveal that psychological and emotional factors, rather than audiological characteristics, predominantly influence the severity of tinnitus-related distress. Notably, 42% of patients with tinnitus had normal hearing and the severity of distress was not correlated with hearing loss, challenging the assumption that tinnitus severity is primarily tied to auditory deficits. Similarly, there appears to be no significant association between the nature of tinnitus sound and the level of distress, reinforcing that sensory characteristics are less critical than subjective responses. In this study, severe tinnitus distress, as indicated by THI scores above 58, was associated with the presence of life stressors and sleep disturbances. Several theories have been proposed to explain how individuals adapt to tinnitus, with three prominent ones being the neurophysiological, habituation and stress-coping models. The neurophysiological model[4] posits that tinnitus is a physiological condition rooted in abnormalities within the auditory system. It emphasises the role of auditory pathways and non-auditory systems, such as the limbic system, in tinnitus perception. Those with distressing tinnitus are thought to have an abnormal ‘gain’ or amplification in these pathways, leading to heightened sensitivity. This model suggests that the inability to habituate to this overactive sensory input contributes to the distress associated with tinnitus. The habituation model[5] compares tinnitus adaptation to how animals adapt to repetitive stimuli through habituation. In humans, this process is influenced by the emotional and physiological states. The level of arousal at the time of exposure to tinnitus plays a significant role in how the brain processes the sound. Lower stress levels and a more relaxed state can facilitate habituation, making the sound less intrusive over time. The stress-coping model[6] frames tinnitus adaptation as a cognitive process tied to stress management. Tinnitus is viewed as a chronic stressor that causes emotional strain when coping resources are insufficient. Individuals who struggle with tinnitus may lack effective coping strategies or use approaches that inadvertently prolong distress. Successful adaptation involves developing better coping mechanisms and reframing the perception of tinnitus-related stress. Our findings support these models that collectively highlight the interplay of cognitive and emotional factors in shaping individual responses to tinnitus. Patients with severe distress often reported maladaptive beliefs, such as a perceived lack of control over tinnitus (55% endorsed THI item 19: “Do you feel that you have no control over your tinnitus?”) or feeling trapped by the condition (42%). These catastrophic cognitions amplify emotional distress and hinder adaptation. Clinically, healthcare professionals should address these beliefs through targeted counselling, challenging notions like “tinnitus will ruin my life” or “I can never cope with this sound.” Providing accurate information about tinnitus and its manageability can reframe these perceptions and reduce distress. For healthcare professionals, managing severe tinnitus requires a multifaceted approach. Beyond ruling out red flags, clinicians should assess for significant life stressors and sleep disturbances, referring patients to tinnitus management programmes when these are present. Given the emotional toll of severe tinnitus, clinicians must also screen for suicidal ideation, particularly in patients with catastrophic THI scores (9% in this study). Urgent referral to psychiatry is warranted if suicidal thoughts or significant distress are identified, ensuring timely intervention. Tinnitus management programmes should integrate cognitive-behavioural strategies to weaken the link between tinnitus and distress, alongside therapeutic sound interventions to promote habituation. The ultimate goal of therapy is learned inhibition, where the link between tinnitus and distress is weakened, even if the perception of tinnitus persists. By targeting cognitive and emotional factors, therapy empowers individuals, minimising tinnitus reaction and its impact on their lives. Financial support and sponsorship Nil. Conflicts of interest There are no conflicts of interest.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 766 · R0570

**Triggering Misophonia: The Importance of Spectral Information, Temporal Information, and Action Identification**

2024 · Auditory Perception & Cognition · article, journalarticle · en · https://doi.org/10.1080/25742442.2024.2302295

Misophonia is characterized by severe negative emotional responses to specific environmental sounds. In this experiment, we investigated the importance of spectral and temporal acoustic information, as well as the role of action identification (e.g., chewing) in triggering misophonia. Eighteen participants with severe misophonia completed the experiment. In total, three stimulus sets were used: the first set consisted of recorded sounds that were either common misophonic triggers or neutral sounds that are not expected to trigger misophonia; the other two sets were each generated by applying temporal and spectral modifications to the unmodified (recorded) stimulus set. Participants rated how triggered they were by each sound (i.e., aversiveness) and were asked to identify the action category of each sound. The unmodified trigger sounds were rated to be more aversive than neutral sounds (p < 0.0001). The main effects of modification type and identification on aversiveness of trigger sounds were significant (p = 0.0001 and p = 0.006, respectively), but their interaction was marginally significant (p = 0.053). Although the unmodified and temporally modified sounds were not significantly different from each other (p = 0.4), spectrally modified sounds were rated significantly less aversive than both the temporally modified (p = 0.003) and unmodified sounds (p = 0.001). Regarding identification, the sounds that were incorrectly identified were on average rated as less aversive than the correctly identified sounds (p = 0.006). Furthermore, the interaction shows that the identification effect was largest for the spectrally modified sounds. This shows that both identification and spectral information play an important role in triggering misophonia.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 767 · R0543

**Psychometric properties of the GAD-7 and PROMIS-Anxiety-4a among youth with depression and suicidality: Results from the Texas youth depression and suicide research network.**

2024 · Journal of psychiatric research · journal article · eng · https://doi.org/10.1016/j.jpsychires.2023.12.033

There is a tremendous need for brief, valid, and free assessments of anxiety in child mental healthcare. The goal of this study was to determine the psychometric properties of two such measures, the GAD-7 and PROMIS-Anxiety-4a, in 1000 children, adolescents, and young adults (8-20 years-old) with depression and/or suicidality. The GAD-7, the PROMIS-Anxiety-4a, and other validated assessments of anxiety, physical functioning, and psychiatric diagnoses were completed. Confirmatory factor analyses showed an acceptable fit for a single factor in both measures via all indices but the RMSEA. They demonstrated measurement invariance across pre-adolescents (8-12 years-old) and adolescents and emerging adults (13-20 years-old), though scalar invariance was not observed for the GAD-7. Both measures showed strong convergent validity, GAD-7: r = 0.68; PROMIS-Anxiety-4a: r = 0.75, divergent validity with a measure of physical function, GAD-7: r = -0.24; PROMIS-Anxiety-4a: r = -0.28, good internal consistency, ω = 0.89 for both, and high test-retest reliability, GAD-7: r = 0.69; PROMIS-Anxiety-4a: r = 0.71. Both measures also showed acceptable sensitivity and specificity in detecting the presence of any anxiety disorder, GAD-7 cut-off score of 10: AUC = 0.75; PROMIS-Anxiety-4a cutoff score of 12: AUC = 0.79. The GAD-7 correlated similarly with the Screen for Child Anxiety Related Disorders total score and generalized anxiety subscale, and also showed similar diagnostic sensitivity and specificity when used to detect the presence of any anxiety disorder vs. generalized anxiety disorder specifically. Results suggest that both of these brief, publicly available instruments are valid and reliable assessments of anxiety among youth in treatment for depression and/or suicidality.

**Решение:** -6 не про мизофонию

---

### 768 · R0012

**Remote Triggers: Misophonia, Technology Non-Use, and Design for Inclusive Digital Spaces**

2026 · arXiv (Cornell University) · article, preprint, journalarticle · und · https://doi.org/10.48550/arxiv.2601.13355

Misophonia, characterized by intense negative reactions to specific sounds or related visual cues, remains poorly recognized in clinical settings yet profoundly affects daily life. This study examines how individuals with misophonia experience and sometimes avoid technology that amplifies their triggers. Drawing on 16 semi-structured interviews with U.S. adults recruited from online communities, we explore how social media platforms such as TikTok and Instagram, along with remote communication tools like Zoom and Discord, shape coping strategies and patterns of non-use. Participants described frequent distress from uncontrollable audiovisual content and food-related behaviors during virtual gatherings. We propose design interventions -- including channel-specific audio-visual controls, real-time trigger detection, and shared preference tools -- to better support misophonic users and reduce exclusion in increasingly mediated social and professional contexts.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 769 · R0070

**A qualitative study exploring early experiences of misophonia through firsthand perspectives.**

2026 · Frontiers in psychiatry · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpsyt.2026.1852664

Introduction Misophonia is characterized by highly aversive affective, physiological, and behavioral responses to specific auditory and related cues. Although research on misophonia has increased in recent years, relatively little is known about onset, course, and maintenance of this disorder. The present study explores early experiences of misophonia through firsthand perspectives with the goal of constructing themes to reflect patterns related to symptom onset, progression, coping, and perceived causal or contextual factors. Methods Adults residing in the United States who identified as having misophonia completed an online survey that included demographic questions, the Duke Misophonia Questionnaire (DMQ), and a series of open-ended questions about early experiences with misophonia. Responses from 50 participants who completed the survey were analyzed using reflexive thematic analysis to generate patterns of meaning across narratives. Results A total of seven themes were developed: 1) Concealment, 2) Psychological Distress, 3) Course Variability, 4) Heterogeneity of Misophonic Cues, 5) Coping Mechanisms and Management Strategies, 6) Barriers to Coping, and 7) Theories of Causality. Discussion Findings highlight the complex and heterogeneous nature of early experiences and are consistent with a biopsychosocial understanding of misophonia in which contextual and individual factors may shape its development and course. </jats:sec

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 770 · R1080

**Obsessive-Compulsive Spectrum Disorders in Children and Adolescents**

2021 · Comprehensive Clinical Psychology · book-chapter · en · https://doi.org/10.1016/b978-0-12-818697-8.00082-0

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 771 · R0285

**OUTLOOK ON HYPERACUSIS AND MISOPHONIA IN AUTISM SPECTRUM DISORDERS (ASD)**

2025 · Journal of Hearing Science · article, journalarticle · und · https://doi.org/10.17430/jhs/211236

Individuals with autism spectrum disorder (ASD) frequently experience decreased sound tolerance (DST), which reduces their social interaction and engagement. The purpose of this perspective piece is to look at the gap in the literature concerning the possible genetic and functional bases for the comorbidity of ASD and two distinct types of DST, hyperacusis and misophonia.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 772 · R1199

**WITHDRAWN: Improving the Measurement of Alexithymia in Autistic Adults: A Psychometric Investigation and Refinement of the Twenty-item Toronto Alexithymia Scale**

2020 · Springer Science and Business Media LLC · article · und · https://doi.org/10.21203/rs.3.rs-96364/v2

Abstract Background: Alexithymia, a personality trait characterized by difficulties interpreting emotional states, is commonly elevated in autistic adults, and a growing body of literature suggests that this trait underlies a number of cognitive and emotional differences previously attributed to autism. Although questionnaires such as the twenty-item Toronto Alexithymia Scale (TAS-20) are frequently used to measure alexithymia in the autistic population, there have been few studies attempting to determine the psychometric properties of these questionnaires in autistic adults, including whether differential item functioning (I-DIF) exists between autistic and general population adults. Methods: We conducted an in-depth psychometric analysis of the TAS-20 in a large sample of 743 cognitively able autistic adults recruited from the Simons Foundation SPARK participant pool and 721 general population controls enrolled in a large international psychological study. The factor structure of the TAS-20 was examined using confirmatory factor analysis, and item response theory was used to further refine the scale based on local model misfit and I-DIF between the groups. Correlations between alexithymia and other clinical outcomes were used to assess the nomological validity of the revised alexithymia scale in the SPARK sample. Results: The TAS-20 did not exhibit adequate model fit in either the autistic or general population samples. Empirically driven item reduction was undertaken, resulting in an eight-item unidimensional scale (TAS-8) with sound psychometric properties and practically ignorable I-DIF between diagnostic groups. Correlational analyses indicated that TAS-8 scores meaningfully predict autistic trait levels, anxiety and depression symptoms, and quality of life, even after controlling for trait neuroticism. Limitations: Limitations of the current study include a sample of autistic adults that was overwhelmingly female, later-diagnosed, and well-educated; clinical and control groups drawn from different studies with variable measures; and an inability to test several other important psychometric characteristics of the TAS-8, including sensitivity to change and I-DIF across multiple administrations. Conclusions: These results indicate the potential of the TAS-8 as a psychometrically robust tool to measure alexithymia in both autistic and non-autistic adults. A free online score calculator has been created to facilitate the use of norm-referenced TAS-8 latent trait scores in research applications (available at http://asdmeasures.shinyapps.io/TAS8_Score).

**Решение:** -6 не про мизофонию

---

### 773 · R1332

**Sensory determinants of the autonomous sensory meridian response (ASMR): understanding the triggers.**

2017 · PeerJ · journal article, article, research-article · eng · https://doi.org/10.7717/peerj.3846

The autonomous sensory meridian response (ASMR) is an atypical sensory phenomenon involving electrostatic-like tingling sensations in response to certain sensory, primarily audio-visual, stimuli. The current study used an online questionnaire, completed by 130 people who self-reported experiencing ASMR. We aimed to extend preliminary investigations into the experience, and establish key multisensory factors contributing to the successful induction of ASMR through online media. Aspects such as timing and trigger load, atmosphere, and characteristics of ASMR content, ideal spatial distance from various types of stimuli, visual characteristics, context and use of ASMR triggers, and audio preferences are explored. Lower-pitched, complex sounds were found to be especially effective triggers, as were slow-paced, detail-focused videos. Conversely, background music inhibited the sensation for many respondents. These results will help in designing media for ASMR induction.

**Решение:** -6 не про мизофонию

---

### 774 · R1405

**La [b]misophonie[/b] ou l’aversion pour le bruit : à propos d’un cas clinique**

2015 · JMIG · article, journalarticle · fr · https://doi.org/10.53738/revmed.2015.11.462.0466

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 775 · R0523

**Professionals in psychiatry need reflective competence**

2024 · World Psychiatry · article · en · https://doi.org/10.1002/wps.21196

The paper by Stein et al1 provides a comprehensive and timely overview of key theoretical advances in work on philosophy and psychiatry. The authors respond to the grand epistemological questions of psychiatry – the classification debate, the nature of psychiatry, and the mind-body problem – with soft naturalism, pluralism, and 4E cognition, respectively. Though I empathically comply with their considerations, I was surprised by the self-centered view of psychiatry. The authors see psychiatry as a scientific and clinical island in splendid isolation without relationship to society in which it is embedded. Here I address a perspective that takes in account: a) how psychiatry is shaped by forces of society; b) how the above-mentioned topics are influenced by philosophical assumptions held by the global community; and c) why the concept of conceptual competence, in agreement with Stein et al, is indispensable for professionals in psychiatry. Psychiatry is not a stand-alone discipline. It dialogues continuously with other sciences such as pharmacology, neuroscience and psychology. In fact, except for descriptive clinical phenomenology, which has been largely neglected lately, innovation often takes place outside psychiatry, through development of new drugs, new techniques in imaging and genetics, or psychotherapeutic restyling. Artificial intelligence predicts that in the near future substantial innovations in psychiatry may be expected in psychedelic-assisted therapy, neuromodulation (repetitive transcranial magnetic stimulation and deep brain stimulation), and digital personalized psychiatry. On closer inspection, we should even recognize that psychiatry, more than any other medical discipline, is being determined not by science but by society. All psychiatric symptoms are ultimately defined on the background of what is commonly agreed upon as normality. Normality is established not by science but by society. Normal is individual behavior that conforms to the most common behavior. Fluctuations in prevalence of mental disorder across culture and time are not caused by sophisticated adaptations of scientific criteria by experts, but pushed by societal waves. Autism and attention-deficit/hyperactivity disorder have become 100-fold more common due to changing perspectives on education and productivity. Long before misophonia became known in psychiatry and sporadically entered scientific articles, the disease term circulated globally on the Internet between interest groups. Often psychiatry is lagging behind social developments. Only in 1974 did homosexuality disappear as a disorder from the DSM-II, and only in 2019 did conditions related to sexual identity disappear as mental disorders from the ICD-11. We should accept that psychiatry no longer shapes itself. The course and faith of psychiatry is not determined by psychiatrists or philosophers, but by socio-economic variations fueled by influencers on social media. The current and ongoing identity crisis in psychiatry is due to the yet-to-be-embedded realization that psychiatry as a scientific discipline has lost control of itself, sadly popularized by the universal theme of mental well-being. Normality has profoundly changed. Whereas for a long time "mental health" was the norm, now "mental well-being" is paramount. Every self-respecting institution, from companies to universities, appoints "well-being officers". Mental health refers to the absence of mental illness. Mental well-being refers to the presence of favorable conditions, including experiencing positive emotions, maintaining relationships, and feeling meaningful in life. Mental well-being includes feeling good in your own skin, being resilient and able to enjoy life. In view of the "norm" of mental well-being, every person has become a potential patient. Mental disorders are reported to be highly prevalent. Around 1-in-7 people have one or more mental disorders. In 2020, rates of depression and anxiety have climbed globally by more than 25%. This increased rate of mental disorders is not due to changes of perspectives in psychiatry, but of social processes reflecting philosophical values. Once you are born in this world, you are expected to actualize yourself as an individual autonomous person, i.e. an absolute authentic and perfectly self-determining subject. We are all brought up with the assumption that individual freedom is the highest attainable thing in life. The Western ideal of human being is the autonomous person who thrives best in the greatest freedom, surrounded by the greatest convenience, and striving for absolute self-determination and maximum self-actualization. Each step towards greater individual autonomy takes us higher up the evolutionary ladder, further away from the animal instinct. The Western ideal of unlimited autonomy has been globalized in line with consumerism and technologism. Unfortunately, most people fail to comply with that ideal. First, the ideal is either unattainable or untenable. Second, the constant bombardment with social commands to self-maximize, to become ourselves, and to prove that we are worth it, makes people feel stressed, exhausted, traumatized, burn-out, lonely, useless and meaningless. Third, though people suffer because they cannot meet the high demands of a society that values the absolute ideal of individual autonomy, this society does not allow mental suffering. Failure is no option. Individual autonomy dictates that we need to be successful; that we are always in control and feel happy. Since mental suffering is unacceptable, mental distress is allowed only as a psychiatric disorder for which we carry no individual responsibility and are not to blame. Mental disorders are not spiking because more patients are developing psychiatric diseases, but because the ideal of individual autonomy has become the standard of normality across the globe. It is no coincidence that anxiety and depression are the most common mental disorders. They express our failure in attempting to fulfil the impossible demand of individual autonomy. We are more anxious not because our world has become more dangerous – on the contrary it has become safer – but because our desire for control is out of proportion. We are more depressed not because our lives are hopeless and meaningless – the opposite is actually true – but because we are confronted with too many choices, we are set up for unrealistically high expectations, and blame ourselves for any and all failures. I was delighted to read about "conceptual competence" in Stein et al's paper. I want to go one step further. The competence of a psychiatrist should include three different skills: professional competence, or the theoretical knowledge and training to practice your profession; experiential competence, or the clinical expertise through years of contact with patients or clients; and reflective competence, or the ability to reflect on your profession, the specific role you hold in it, and how they are affected by society. Reflective competence is the transformative awareness of how conceptual assumptions in society shape clinical care. The philosophical presuppositions of health and illness, mind and body, normal and abnormal are constantly changing in a globalized and digital world. Imperceptibly, they determine the validity of diagnosis and treatment. That is why thinking about our profession is part of the basic skills of every professional. Just as a jeweler not only designs jewelry but also calculates gold prices, a psychiatrist takes into account society's view of mental suffering in addition to what emerges from his/her contact with patients. Following the crisis in psychiatry, colleagues called for "a fundamental rethinking of the creation and training of psychiatric knowledge"2. A survey found that 65.2% of mental health professionals struggle with conceptual and philosophical questions related to their profession, and only 4.3% feel that training adequately prepared them to face this intellectual challenge3. Is it the task of psychiatry to reflect, beyond psychopathology of individuals, about philosophical values of modern societies? But, then again, do we have a choice?

**Решение:** -1 обзор литературы / концептуальная статья

---

### 776 · R0781

**Touching you, touching me: Higher incidence of mirror-touch synaesthesia and positive (but not negative) reactions to social touch in Autonomous Sensory Meridian Response**

2023 · OSF Preprints (OSF Preprints) · article, preprint · en · https://doi.org/10.1016/j.concog.2022.103380

Study abstract: The characterisation of autonomous sensory meridian response (ASMR) as an audio-visual phenomenon overlooks how tactile experiences are not just perceptual concurrents of ASMR (i.e., tingling) but also commonly strong ASMR inducers. Here we systematically investigated whether ASMR-responders show altered tactile processing compared to controls. Using a screening measure of vicarious touch with a predefined cut-off for mirror-touch synaesthesia (MTS; a condition where tactile sensations are experienced when viewing, but not receiving, touch), we found that ASMR-responders had more frequent and intense vicarious touch experiences, as well as a strikingly higher incidence of MTS, than non-responders. ASMR-responders also reported greater reactivity to positive, but not negative, interpersonal touch. Correlations further showed these patterns to be more prevalent in those responders with stronger ASMR. We discuss the implications of our findings in terms of heightened sensory sensitivity, bodily awareness, and the underlying neuro-cognitive mechanisms driving vicarious tactile perception in ASMR and MTS.

**Решение:** -6 не про мизофонию

---

### 777 · R1424

**Misophonia: Towards a Taxonomy of Annoyance**

2015 · Front Matter · other · https://doi.org/10.59350/hdr2s-p3p16

This is the second post in Sounding Out!'s 4th annual July forum on listening in observation of World Listening Day on July 18th, 2015.</jats:p

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 778 · R1478

**P.1.b.005 A diminished mismatch negativity response in misophonia, a potential marker for aggressive impulsivity**

2013 · European Neuropsychopharmacology · article · en · https://doi.org/10.1016/s0924-977x(13)70269-4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (ERP исследование MMN при мизофонии)

---

### 779 · R0033

**Les Sens Oubliés de la médecine — édition savante (préprint allégé)**

2026 · OSF Preprints (OSF Preprints) · book, preprint, project · und · https://doi.org/10.6084/m9.figshare.32814179

Synthèse académique et vulgarisée de 16 chapitres explorant la sensorialité humaine au-delà des cinq sens classiques : intéroception, proprioception, vestibulaire, chronoception, thermoception, nociception, magnétoréception. Implications cliniques pour PPPD, SEDh, misophonie, autisme adulte, TCA. Préprint allégé — manuscrit complet via Amazon KDP (ASIN 9798199405577).

**Решение:** -1 обзор литературы / концептуальная статья

---

### 780 · R1448

**MISOPHONIA: A DISORDER OF EMOTION PROCESSING OF SOUNDS**

2014 · Journal of Neurology Neurosurgery & Psychiatry · article, conference paper · en · https://doi.org/10.1136/jnnp-2014-308883.38

Objective Sounds of chewing, breathing, keyboard typing are considered by most people as 9normal9 sounds and are ignored as background sounds in everyday listening. However, for a group of people these sounds are not only distracting but also evoke a strong feeling of anger accompanied by an urge to escape from the situation producing these sounds. This condition, marked by sensitivity to a selective group of sounds, was given the name “misophonia” (hatred of sounds) almost a decade ago. Since the sounds that act as “triggers” in this condition are quite common at home, work place and in social gatherings, misophonia has devastating effects on social, family and personal life of the sufferer. Presently misophonia is not featured in any official medical/psychiatric classifications. People with misophonia suffer in silence because they do not share their problem with others for the fear of being called “crazy”. The objective of the current work was to check the consistency of profile of symptoms and trigger sounds in a population of subjects with misophonia. Method A group of subjects were assessed by a group of neurologists in a neurology clinic. To further assess the symptoms/triggers in a bigger population, a questionnaire was designed asking questions about symptoms/triggers etc which was then posted on a website dedicated to disseminate information about misophonia. People were requested to fill-in the questionnaire and send back by email. Results The assessment in the neurology clinic confirmed a striking similar profile of symptoms and triggers in the individuals. A group of 195 subjects filled-in the questionnaire posted on the website. Analysis of 157 questionnaire showed: Mean Age of Onset =12.08 years [5–50] 146/157 (93.0%) describe eating sounds as triggers 135/157 (86.0%) describe anger as the dominant emotion (other emotions include panic/anxiety) 132/157 (84.0%) describe leaving the situation which produce trigger sounds. Conclusion Our data indicate that misophonia is a disorder of emotion processing of sounds which need to be investigated further.

**Решение:** ? тезисы fMRI конференции, проверить выборку

---

### 781 · R0109

**Visual Secondhand Scrolling in Shared Environments: A Conceptual Framework and Experimental Protocol for Involuntary Exposure to Short-Form Video**

2026 · Zenodo (CERN European Organization for Nuclear Research) · research, text/working paper, article · en · https://doi.org/10.5281/zenodo.22983541

Concept paper / proposed experimental protocol. Not peer reviewed. No completed experiment is reported. Short-form video research has focused primarily on people who intentionally use the platforms. Less is known about bystanders who can see another person's rapidly changing feed without selecting, controlling, or intending to consume it. This concept paper defines visual secondhand scrolling (VSS) as incidental or involuntary visual exposure to rapidly changing digital content displayed on another person's device while the observer is engaged in another activity. The phrase &ldquo;secondhand scrolling&rdquo; is not presented as novel: it appeared in public writing by 2021 and 2023, and a 2026 human-computer interaction preprint used it for ambient technology exposure in the context of misophonia. The narrower contribution proposed here is an operational visual-attention framework for silent, neighboring short-form feeds. Existing studies show that task-irrelevant visual events and motion can capture attention under some conditions, and experimental studies of active short-form-video use report acute prospective-memory effects. Those findings do not establish an equivalent effect in passive observers. This paper therefore specifies testable hypotheses, a candidate exposure construct&mdash;visual secondhand scroll exposure (VSSE)&mdash;and a controlled eye-tracking protocol comparing screen-off, static, long-form, and short-form neighboring-screen conditions. The primary proposed outcome is neighboring-screen gaze time; task performance and subjective distraction are secondary outcomes. No medical injury, diagnosis, or long-term cognitive effect is claimed. The manuscript includes an AI-assistance disclosure.

**Решение:** -7 protocol / preregistration without data

---

### 782 · R1104

**Perceptions of Deep Brain Stimulation for Adolescents with Obsessive-Compulsive Disorder.**

2021 · Journal of child and adolescent psychopharmacology · journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1089/cap.2020.0166

Objective: The present study aims to understand perceptions of deep brain stimulation (DBS) for severe obsessive-compulsive disorder (OCD) in adolescents among two groups: parents of children with a history of OCD and adults with a history of OCD. Methods: Two hundred sixty participants completed a questionnaire exploring their treatment history, relevant symptom severity, DBS knowledge, and DBS attitudes using an acceptability scale and a series of statements indicating levels of willingness or reluctance to consider DBS for adolescents with severe OCD or severe epilepsy. Results: Overall, participants found DBS to be fairly acceptable for adolescents with severe OCD, with 63% reporting at least 7/10 on a 0-10 acceptability Likert scale. Respondents were more willing to consider DBS for epilepsy than for OCD. Several factors were associated with greater willingness to consider DBS for OCD, including familiarity with DBS, the presence of suicidal thoughts, assurances of daily functioning improvements, and assurances of substantial symptom reduction. Concerns about safety, personality changes, and long-term effects on the body were associated with greatest reluctance to consider DBS for OCD. Conclusions: Our findings support the importance of increasing parents' familiarity with DBS, monitoring factors participants identified as most important to their DBS perceptions in future DBS research, and communicating benefits and risks clearly. We also highlight the need for further research on perceptions of DBS for severe and refractory OCD in adolescents.

**Решение:** -6 не про мизофонию

---

### 783 · R0814

**Mindfulness and cognitive emotion regulation in pediatric misophonia.**

2023 · Journal of contextual behavioral science · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jcbs.2023.07.005

Misophonia is characterized by decreased tolerance of ordinary human-generated trigger sounds and associated visual stimuli (e.g., chewing, sniffing, lip smacking), coupled with intense affective reactions. The disorder often begins during childhood or adolescence and is associated with impairment and distress in numerous life domains. Research has begun to examine the underlying psychological mechanisms of misophonia in adults, but studies in youth are limited. Trait mindfulness (i.e., nonjudgmental and nonavoidant present-moment awareness) and cognitive emotion regulation (i.e., cognitive processing, or responding to, emotionally arousing situations) are two proposed mechanisms that may underpin pediatric misophonia and associated functional impairment. In the present exploratory cross-sectional study, we examined trait mindfulness and cognitive emotion regulation and their relations with misophonia features and adaptive functioning in 102 youth with misophonia ( M age = 13.7; SD = 2.5; range = 8-17). More severe misophonia was significantly associated with decreased levels of both trait mindfulness and adaptive functioning across domains, in addition to deficits in certain facets of cognitive emotion regulation, particularly self-blame. Neither trait mindfulness nor facets of cognitive emotion regulation moderated the association between misophonia severity and adaptive functioning across domains, with the notable exception that difficulties with adaptive functioning in peer relationships was attenuated in those high in mindfulness. Findings suggest that trait mindfulness- and to a lesser extent cognitive emotion regulation- may be potentially relevant processes in pediatric misophonia. However, more research is needed to uncover the precise nature of these processes to aid future characterization and intervention efforts, especially in light of equivocal findings in the present study.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 784 · R0112

**The effect of lavender herbal tea on the mental health of individuals with misophonia: A randomized controlled trial.**

2026 · Journal of psychiatric research · article, journal article, randomized controlled trial · eng · https://doi.org/10.1016/j.jpsychires.2026.01.028

Misophonia is a disorder characterized by heightened sensitivity to certain sounds, triggering symptoms such as sympathetic nervous system activation, anger, anxiety, and depression. This study aimed to evaluate the potential role of lavender tea in alleviating these symptoms due to its anxiolytic and antidepressant properties. A single-center, single-blind, randomized clinical trial was conducted with 60 participants aged 18 and over, diagnosed with misophonia. Participants were divided equally into experimental and control groups using block randomization. The experimental group consumed 2 g of lavender tea twice daily for 14 days, while the control group received no intervention. Data were collected using the Misophonia Scale, Beck Depression Inventory II, Anxiety Rating Scale, and Trait Anger Scale and analyzed with SPSS 25.0. Baseline characteristics, including age, gender, marital status, education level, income level, and scores for misophonia, anxiety, depression, and anger, were comparable between groups. The mixed ANOVA results suggested that positive changes were observed in misophonia and related psychological symptoms in the lavender tea group, and that these changes may have been more pronounced compared to the control group. The results suggest that the intervention may correlate with enhancements in misophonia, quality of life, and coping strategies. Lavender tea consumption may have helped alleviate symptoms of misophonia, anxiety, depression, and anger. However, due to the lack of participant blinding and the use of self-report measures, the findings should be interpreted cautiously in terms of placebo effects and expectancy bias. REGISTRATION: ClinicalTrials.gov Number (NCT06785649).

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 785 · R0148

**Transdiagnostic and clinical predictors of longitudinal misophonia symptoms**

2026 · Frontiers in Cognition · journalarticle, review, article · en · https://doi.org/10.3389/fcogn.2026.1945899

Introduction Anxiety sensitivity (AS) and distress tolerance (DT) are emotional-vulnerability factors driving emotion dysregulation. AS and DT may amplify misophonia. Research examining transdiagnostic factors predicting misophonia is largely cross-sectional. We examined relations between AS, DT, and longitudinal misophonia symptoms, adjusting for clinical variables. Methods Fifty-eight individuals recruited from soQuiet endorsing clinical misophonia symptoms completed baseline and daily surveys 3x daily for 30 days. Results Bivariate analyses suggested baseline AS was associated with elevated longitudinal misophonia symptoms during and not during triggers, while baseline DT was associated with higher misophonia symptoms during triggers. Baseline AS, momentary emotion dysregulation, and baseline misophonia were predictors of longitudinal misophonia during triggers, adjusting for momentary emotion dysregulation, baseline misophonia, and baseline obsessions and compulsions. An alpha correction suggested an attenuated AS effect. Null effects for DT may be explained by analyses supporting emotion dysregulation as a mediator of the relation between DT and misophonia. Effects of obsessive-compulsive symptoms were null. Discussion Results inform longitudinal relations between transdiagnostic factors and misophonia. A predominant limitation is sample homogeneity. Misophonia symptom fluctuations appear contextualized, likely impacted by environmental and emotional-vulnerability factors. Results inform ongoing advancements to misophonia assessment and, pending further investigation, clinical interventions targeting malleable transdiagnostic factors.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 786 · R0647

**Heart rate variability under acute stress and noise in healthy subjects: A tool to study autonomic activity in tinnitus?**

2024 · Authorea Preprints · article, preprint · en · https://doi.org/10.22541/au.172888410.04315106/v1

Introduction: Individuals with hearing disorders such as tinnitus often experience high levels of stress, anxiety, depression, and decreased sound tolerance. These factors may be related to maladaptive autonomic regulation, affecting their response to acute stress. Heart rate variability (HRV) is a reliable measure of autonomic activity, but its interaction with psychological factors is not well understood. Objectives: The aim was to develop a multimodal stress induction protocol in a non-clinical population and to determine how psychological factors influence physiological responses. Methods: Electrocardiograms were recorded from 30 healthy young adults during three stress tasks: mental arithmetic, noise exposure, and a cold pressor test. Heart rate (HR) and root mean square of successive differences (RMSSD) were used to index autonomic activity. Participants also completed questionnaires on perceived stress, noise sensitivity, anxiety, and depression to examine relationships with HRV. Results: All tasks produced significant time-dependent effects on HRV features, but to different extents. Mental arithmetic produced the largest increase in HR and decrease in RMSSD. In contrast, the noise task showed a significant decrease in HR without a change in RMSSD, suggesting that the task induced relaxation. In the CPT, females showed increased HR but a decrease in RMSSD, whereas males showed the reverse pattern. Psychological factors significantly interacted with HRV dynamic changes during mental and noise tasks, but not during CPT. Conclusions: HRV responses to acute stress are non-stationary and influenced by psychological factors. Thus, this protocol presents an original approach to study autonomic activity in stress-related conditions such as tinnitus.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 787 · R0765

**The sound of rage : the perceived impact of misophonia on daily life and relationships**

2023 · Umeå universitet, Institutionen för psykologi · bachelor thesis, thesis · eng · http://urn.kb.se/resolve?urn=urn:nbn:se:umu:diva-209592

Misophonia is a condition characterized by a strong physiological, emotional, and behaviouralresponse to specific auditory stimuli, which have a significant negative impact on the wellbeingof affected individuals. The present investigation focuses on emotional dysregulation, which arises due to the triggering of specific auditory stimuli. Individuals with misophoniastruggle to regulate their emotions when exposed to sounds, leading to emotional reactions, including anger, anxiety, disgust, avoidance behaviour, fight or flight, and feeling overwhelmed. These reactions might even lead to violent impulses directed towards the source of the sound. Despite its growing recognition, little is yet known about misophonia, and experts have not established any clear boundaries or criteria for the condition to be considered adisorder. As such, it is not yet included in any classification systems for disorders. The aim of this study is to understand how individuals with misophonia experience emotional dysregulation, how do they describe their experience, what is it like to live with misophonia ona day-to-day basis, and how do individuals understand and cope with emotional dysregulation caused by misophonia? The study utilized a qualitative approach with semi-structured interviews as the data collection method. Thematic analysis was used to identify patterns and themes within the data. Participants stated that misophonia causes significant distress and disruption impacting emotional well-being and daily functioning. Validation of this new condition can be very helpful and make a positive impact in their social circle, and that lack of awareness and effective treatment may hold back seeking professional help.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 788 · R1130

**Amsterdam UMC 2020 revised diagnostic criteria for misophonia.**

2020 · https://doi.org/10.1371/journal.pone.0231390.t005

Amsterdam UMC 2020 revised diagnostic criteria for misophonia.</p

**Решение:** -7 diagnostic criteria / deposited excerpt

---

### 789 · R0783

**Effectiveness of an innovative treatment protocol for misophonia in children and adolescents: Design of a randomized controlled trial.**

2023 · Contemporary clinical trials communications · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.conctc.2023.101105

Background: Misophonia is a recently identified disorder in which individuals experience intense, uncontrollable and disproportional irritation, anger or disgust when confronted with specific sounds or stimuli associated with these sounds. Prevalence rates in children and adolescents are currently still to be investigated. The reported average age of onset is around 13 years, in clinical practice children from 8 years old are referred.Misophonia is associated with avoidance and anticipation anxiety, possibly leading to serious educational and social consequences for children and families. Worldwide, no evidence-based treatment exists specifically for children and adolescents with misophonia.This article presents the design of a randomized controlled trial testing the effectiveness of cognitive behavioral therapy (CBT) combined with psychomotor therapy (PMT) for misophonia in children and adolescents (aged 8-18). Methods: In total, 82 patients will be randomly assigned to a treatment condition or waiting list condition of 3 months (WCG). Treatment consists of 7 weekly group therapy sessions (1.5 h CBT plus 1.5 h PMT) and a follow-up after 3 weeks. Pre and post treatment assessments will be conducted during a baseline assessment, after 3 and 6 months. The primary outcome will be assessed by the Amsterdam Misophonia Scale - Youth (AMISOS-Y) and secondary outcomes (e.g. quality of life) and putative predictors (e.g. parenting burden) will be studied. Conclusion: This trial is the first study worldwide testing the effectiveness of a combined CBT plus PMT protocol for misophonia in children and adolescents. If proven effective, this protocol provides an innovation to improve care for youth with misophonia.

**Решение:** -7 protocol / preregistration without data

---

### 790 · R1119

**Mizofoni: Bir Gözden Geçirme**

2021 · Psikiyatride Guncel Yaklasimlar - Current Approaches in Psychiatry · article, google scholar result · tr · https://doi.org/10.18863/pgy.857018

Mizofoni, diğer insanların oluşturduğu günlük seslere ve bazen hayvan seslerine orantısız şekilde duygusal tepki vermek olarak tanımlanmaktadır. Kişilerin mesleki ve sosyal işlevselliklerini bozabilecek kadar şiddetli olabilir. Hastalığın risk faktörleri ve etiyolojisi tam olarak bilinmemektedir. Bazı nörogelişimsel hastalıklar ve psikiyatrik bozukluklarla birlikte görülebilmektedir. Amsterdam Mizofoni Ölçeği ve Mizofoni Ölçeği mizofoniyi değerlendirmek için geliştirilmiş ölçeklerdir. Tanı kriteleri tam olarak belirlenmemiştir ve güncel tanı sınıflamalarında yer almamaktadır. Tedavisinde, bilişsel davranışçı terapi, farkındalık (mindfullnes), diyalektik davranış terapisi ve maruz bırakma gibi yöntemler kullanılmakta olup belirli bir farmakolojik tedavi tanımlanmamıştır.Misophonia is defined as a disproportionate emotional response to everyday sounds created by other people and sometimes to animal sounds. It can be severe enough to disrupt people’s professional and social functionality. The risk factors and etiology of the disease are not fully known. It can be seen together with some neurodevelopmental diseases and psychiatric disorders. Amsterdam Misophonia Scale and Misophonia Scale are scales developed to evaluate misophonia. Diagnostic criteria have not been fully determined and are not included in the current diagnostic classifications. In its treatment, methods such as cognitive behavioral therapy, mindfullnes, dialectical behavioral therapy and exposure are used, and no specific pharmacological treatment has been defined

**Решение:** -1 обзор / комментарий / письмо
