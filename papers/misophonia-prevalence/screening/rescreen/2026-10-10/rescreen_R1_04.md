# Повторный отбор вслепую, часть 4

Записи 451–600 из 790: всё, что ИИ исключил, кроме калибровочной выборки. Повторный отбор вслепую по правилу защиты (протокол, §11b). **Меток и причин ИИ в этом файле нет** — решайте с нуля по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261011).

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

### 451 · R1303

**Cognitive-Behavioral Therapy for an Adolescent Female Presenting With Misophonia: A Case Example**

2018 · Clinical Case Studies · article, journalarticle · en · https://doi.org/10.1177/1534650118782650

The case illustrates the effective assessment and treatment of misophonia in a 14-year-old adolescent female in which short-term cognitive-behavioral therapy (CBT) and exposure and response prevention (ERP) principles were utilized. Misophonia-related symptomology declined significantly during treatment, and partial gains were consolidated over time with the use of ongoing sporadic booster sessions to maintain reported improvements and to address the variable nature of the patient’s symptom expression. Significant tolerance of noise triggers occurred, both within and in between sessions, and the patient achieved concurrent behavioral changes and tolerated a marked reduction in relevant avoidance behaviors. Self-reported and observed psychological and physiological distress diminished when confronted with identified trigger noises, both during conducted in vivo exposures and, more broadly, in the patient’s home and school environments. The case serves as a contribution to the growing body of psychiatric literature recognizing misophonia as a distinct phenomenon, and offers anecdotal evidence regarding assessment treatment implications.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 452 · R1503

**Tinnitus- Latest Thinking**

2008 · NSUWorks · presentation

The most common form of tinnitus is a mildly annoying perception of a ‘ringing in the ears’, but it can take many other forms. It typically co-exists with hearing loss and decreased sound tolerance. Its severity can range from very slight to completely debilitating, leading to suicidal ideation. Until recently its origins were obscure and patients were typically told ‘there’s nothing that can be done for it so you’ll just have to learn to live with it’. In the past decade or so, science’s understanding of this disorder has improved enormously, so these findings will be briefly outlined. Treatment options have also increased dramatically, so these too will be summarized. Some useful clinical tips will be given to help Health Professionals assist patients suffering from this condition

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 453 · R1494

**Моделирование природоохранных технологий в теплоэнергетике с учетом макрокинетических процессов**

2011 · Вестник Саратовского государственного технического университета · article · en

Presented an analytical model for evaluating the environmental impact of power equipment on the environment. The basis of the model of the law laid macrokinetic flow gross reaction of nitrogen oxides in the zone of high temperatures, reflecting the regularities of formation of nitrogen oxides on the thermal mechanism. Received oxygen and nitrogen in the reaction zone, depending on the modes of operation of burners and furnaces of the boiler, as well as their possible changes due to entry of additional moisture. Defined analytical reaction rate, concentration of nitrogen oxides and exit rates of nitrogen oxides from fuel combustion, taking into account the input of moisture.

**Решение:** -6 не про мизофонию

---

### 454 · R0087

**Sona: Towards Context-Aware, Real-Time Personalization of Acoustic Environments for Noise Sensitivity**

2026 · Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA) · conference-paper · https://doi.org/10.1145/3772363.3799034

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 455 · R0009

**Altered intrinsic brain connectivity in misophonia, with and without hyperacusis.**

2026 · Hearing research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.heares.2025.109521

Misophonia and loudness hyperacusis are debilitating sound intolerance conditions marked by extreme emotional and physiological responses to everyday sounds. Although frequently co-occurring, their distinct neural correlates remain poorly delineated. In an exploratory data-driven analysis, we identified neural-connectivity based markers of misophonia among cortical and subcortical networks in the brain using resting-state fMRI data. We leveraged an optimized and cross-validated machine learning framework to sift through >85 thousand functional connections and to evaluate detectability of misophonia, in isolation and when comorbid with hyperacusis. Participants were rigorously categorized using structured interviews into misophonia-only (MI), misophonia with hyperacusis (MH), and control (CTR) groups. Classifier models trained on individual functional connectivity distinguished both MI and MH from CTR, with 63 % and 67 % test prediction accuracy respectively. Core misophonia-related alterations consistently emerged across both groups, particularly in salience, somatomotor, and frontoparietal control networks, implying disruptions in emotion regulation, motor inhibition, and attentional control, respectively. Specific to misophonia-only were connectivity abnormalities in the basal ganglia and subcortex, suggesting a neural dissociation between MI and MH conditions. In contrast, connectivity trends unique to MH revealed networks implicated in higher-order visual processing, likely reflecting hyperacusis-linked processes. These findings offer a refined neurobiological dissociation between misophonia and hyperacusis and underscore the importance of careful diagnostic separation in both research and clinical contexts. By isolating misophonia-relevant brain networks, our results provide actionable insight into the development of precise neuroscience-informed interventions. In particular, they support psychology-based therapy to target dysfunctional connectivity in salience and control circuits for treating misophonia.

**Решение:** ? фМРТ покоя (случай-контроль), проверить скрининг пула

---

### 456 · R0628

**An Exploration of Misophonia in the Literature**

2024 · ScholarWorks@GVSU · en · https://core.ac.uk/download/613737079.pdf

Misophonia is a disorder that elicits an extreme negative reaction to specific auditory and visual stimuli. Triggering stimuli, which are often human produced, provoke an array of symptoms including heightened negative emotions along with autonomic nervous system responses. Despite being a relatively common disorder, misophonia is still inadequately recognized and is often classified under conditions such as obsessive-compulsive disorder and anxiety. No cure for misophonia currently exists, but there are many treatments and coping mechanisms used by people with misophonia to ease their symptoms. This comprehensive review synthesizes current research on misophonia, exploring underlying mechanisms, comorbidities, diagnostic methodologies, and treatment efficacy. By combining valuable insights, this review aims to enhance awareness and understanding of this often-overlooked disorder

**Решение:** -1 обзор литературы / концептуальная статья

---

### 457 · R0848

**Video_2_Synopsis and Qualitative Evaluation of a Treatment Protocol to Guide Systemic Group-Cognitive Behavioral Therapy for Misophonia.WMV**

2022 · https://doi.org/10.3389/fpsyt.2022.794343.s002

Misophonia is a disorder in which patients suffer from anger or disgust when confronted with specific sounds such as those associated with eating or breathing, causing avoidance of cue related situations resulting in significant functional impairment. Functional magnetic resonance imaging studies suggest misophonia is associated with increased activity in the auditory cortex and salience network, which might reflect increased vigilance toward specific misophonia triggers. New treatments have been developed and investigated in the last years in which this vigilance plays an important role. This is a synopsis of the first group protocol for systemic Cognitive Behavioral Therapy (G-CBT) for misophonia. We discuss the model of CBT for misophonia, provide a detailed guide to the treatment illustrated with a case study, discuss advantages, limitations, and possible pitfalls by a qualitative evaluation of the protocol, and review evidence for the protocol.</p

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 458 · R1506

**SELECTIVE SOUND INTOLERANCE AND EMOTIONAL DISTRESS: WHAT EVERY CLINICIAN SHOULD HEAR**

2008 · Psychosomatic Medicine · article, case reports, letter · eng · https://doi.org/10.1097/psy.0b013e318180edc2

We report two cases of selective sound intolerance associated with intense emotional distress and functional impairment. To our knowledge, there have not been any previous cases of this nature documented in the psychiatric literature.Case 1 – Over the course of 4 to 5 months, a 13-year-old girl beca

**Решение:** -2 клинический случай / серия случаев

---

### 459 · R0876

**Implications of the COVID-19 Pandemic for Tinnitus**

2022 · Plural Publishing · part of book or chapter of book · eng · https://arro.anglia.ac.uk/id/eprint/707432/10/Beukes_Manchaiah_2022.pdf

The term ‘tinnitus’ is searched over 110,000+ times every month. Unfortunately, much of the information readily available through internet searches is inaccurate, whereas most evidence-based information is only available through peer-reviewed journal articles often containing dense scientific jargon. Tinnitus: Advances in Prevention, Assessment, and Management aims to bridge this gap by providing up-to-date and evidence-based information on tinnitus prevention, assessment, and management. Presented in a quick, easy-to-read format, this text offers a practical and handy resource for busy practitioners and health profession students, as well as individuals with bothersome tinnitus.\ud Each section contains short chapters providing accessible overviews of research related to tinnitus and hyperacusis. Section I delves into various approaches for prevention of hearing loss and tinnitus. Section II covers tinnitus assessment, while Section III introduces readers to a range of tinnitus management solutions. Section IV focuses solely on recent advances in assessment and management of hyperacusis and other disorders of decreased sound tolerance. Authors of Section V review recent tinnitus-related developments, including social media use and COVID-19. The final section consists of interesting real-life case studies involving patients with bothersome tinnitus.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 460 · R1354

**Why some hate chewing noises**

2017 · The New Scientist · article · en · https://doi.org/10.1016/s0262-4079(17)30255-5

Now Sukhbinder Kumar and his team at Newcastle University, UK, have carried out a series of tests on 20 volunteers with severe misophonia, as well as 22 people who don't have it. Both groups listened to neutral noises, like the sound of rain; unpleasant sounds, such as a baby crying; and sounds that were triggers for the misophonics, such as chewing or breathing noises. While both groups reacted to the neutral and unpleasant sounds in a similar way, the misophonic group experienced increased heart rates and skin conductance--both signs of the body's fight-or-flight response--when they heard trigger sounds. Brain scans revealed that, when the trigger sounds were played, the misophonics had heightened activity in the anterior insular cortex, an area that helps determine which things they should pay attention to.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 461 · R0656

**Psychological Intervention for Misophonia**

2024 · OSF Preprints (OSF Preprints) · preprint, project

Acceptance and commitment therapy (ACT) is a promising psychotherapy for supporting traditional behavioral methods for treating misophonia, but has not been previously tested. ACT teaches skills to develop acceptance, mindfulness, and defusion from difficult internal experiences while increasing connections with personal values and encouraging meaningful behavioral changes. We are proposing to test ACT+ traditional audiological behavioral intervention as an integrated, multi-disciplinary approach for the assessment and treatment of misophonia. Participants will be 40 adults with misophonia and will be randomly assigned to receive 12 sessions of ACT+behavioral intervention or receive 12 weeks of progressive relaxation training+psychoeducation (PRT; a commonly used active control condition) after undergoing a comprehensive psychological and audiological evaluation. This study will help determine if ACT+behavioral intervention is a feasible and acceptable treatment for misophonia, help clarify active psychological mechanisms of misophonia, and determine whether or not this combination of services can effectively help individuals diagnosed with misophonia.

**Решение:** -7 protocol / preregistration without data

---

### 462 · R0277

**Misophonia**

2025 · Springer eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1007/978-3-031-94841-1_108

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глава книги / справочник

---

### 463 · R1000

**Psychological Intervention for Misophonia**

2022 · OSF Registries · studyregistration/pre-registration · https://doi.org/10.17605/osf.io/rq7ag

Acceptance and commitment therapy (ACT) is a promising psychotherapy for supporting traditional behavioral methods for treating misophonia, but has not been previously tested. ACT teaches skills to develop acceptance, mindfulness, and defusion from difficult internal experiences while increasing connections with personal values and encouraging meaningful behavioral changes. We are proposing to test ACT+ traditional audiological behavioral intervention as an integrated, multi-disciplinary approach for the assessment and treatment of misophonia. Participants will be 40 adults with misophonia and will be randomly assigned to receive 12 sessions of ACT+behavioral intervention or receive 12 weeks of progressive relaxation training+psychoeducation (PRT; a commonly used active control condition) after undergoing a comprehensive psychological and audiological evaluation. This study will help determine if ACT+behavioral intervention is a feasible and acceptable treatment for misophonia, help clarify active psychological mechanisms of misophonia, and determine whether or not this combination of services can effectively help individuals diagnosed with misophonia.

**Решение:** -7 protocol / preregistration without data

---

### 464 · R1471

**When selective audiovisual stimuli become unbearable: a case series on pediatric misophonia**

2013 · Neuropsychiatry · article, other literature type · en · https://doi.org/10.2217/npy.13.70

Background: Those with misophonia experience distress in response to specific sounds (e.g., sounds of eating) and often to repetitive movements (e.g., seeing leg shaking). The literature on misophonia is sparse but it is gaining increased clinical attention. Methods: We report on four cases to highlight clinical characteristics associated with misophonia seen in a pediatric treatment setting. Results: Patients typically responded to triggers with avoidant behavior or made attempts to stop the production of the trigger. Misophonia caused varying levels of impairment and was often seen as the patient’s primary complaint. Onset began in childhood and demonstrated increasing severity until the point at which evaluation and treatment was sought. Family accommodation was consistently present and reinforced the patient’s difficulties. Conclusion: Misophonia is distinguished from existing psychological and auditory disorders that have known etiologies and treatments. Further research is required to understand the neurological and psychological underpinnings of the disorder, and identify appropriate treatments.

**Решение:** -2 клинический случай / серия случаев

---

### 465 · R1295

**DSM-5'e Giremeyen Tanılar (Kompulsif Satın Alma, Misophonia, Facebook Kıskançlığı, Pagofaji, Siberkondria, İnternet Bağımlılığı)**

2018 · Turkiye Klinikleri Psychiatry - Special Topics · article · tr

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 обзор литературы / концептуальная статья

---

### 466 · R1479

**Modèles cognitifs de la conscience**

2013 · Revue Neurologique · article · fr · https://doi.org/10.1016/j.neurol.2013.01.532

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 467 · R0424

**Misophonia: An Underrecognized Disease in Pediatric Patients.**

2025 · Ear, nose, & throat journal · article, journal article, case reports · eng · https://doi.org/10.1177/01455613221095606

Misophonia is a chronic condition in which patients experience a strong negative, emotional, or psychologic reaction to specific sounds. These sounds cause the individual to have a sudden, uncontrolled, and disproportionate negative reaction affecting their daily activities. The literature describes several cases of misophonia in the adult population; however, only 2 pediatric case studies are reported. Herein, we present 2 additional cases. An exaggerated response to an auditory stimulus is observed in other disorders such as tinnitus, hyperacusis, migraines, and many psychiatric disorders. Sound aversion has a broad differential diagnosis and may require visits to numerous specialists, placing strain on the patient and the healthcare system. Furthermore, misophonia is underdiagnosed in the pediatric population as it requires self-reporting of symptoms. The pathophysiology, prevalence, and treatment of misophonia continue to be relatively unknown. We attempt to highlight this rarely reported pediatric diagnosis and elaborate on its clinical presentation to increase awareness among otolaryngologists.

**Решение:** -2 клинический случай / серия случаев

---

### 468 · R1375

**Problemas otológicos (II): acúfenos y vértigo**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 469 · R1054

**EMDR therapy for misophonia: a pilot study of case series.**

2021 · European journal of psychotraumatology · article, journal article, journalarticle · eng · https://doi.org/10.1080/20008198.2021.1968613

ABSTRACT Background: Misophonia is a disorder in which patients suffer from anger or disgust when confronted with specific sounds such as loud chewing or breathing, causing avoidance of cue-related situations resulting in significant functional impairment. Though the first treatment studies with cognitive behavioural therapy (CBT) showed promising results, an average of 50% of the patients has not improved much clinically. Objective: The aim of this pilot study was to assess the effectiveness of eye movement desensitization and reprocessing (EMDR) therapy as a trauma-focused approach in treating misophonia symptoms. Method: A sample of 10 adult participants with misophonia was studied at the outpatient clinic of the Academic Medical Center in Amsterdam. Participants were either on the waiting list for CBT or non-responders to CBT. EMDR was focused on misophonia-related emotionally disturbing memories and delivered in a mean of 2.6 sessions of 60–90 minutes. Pre- and post-treatment self-assessed ratings of misophonia symptoms (AMISOS-R, primary outcome), of general psychopathology (SCL-90-R) and of quality of life (SDS) were administered. The co-primary outcome was the Clinical Global Impression Improvement scale (CGI-I). Results: A paired t-test (n = 8) showed improvement on the primary outcome (−6.14 [MD], 5.34 [SD]) on the AMISOS-R (P = .023). Three of the eight patients showed clinically significant improvement measured with the CGI-I. No significant effect on secondary outcomes was found. Conclusions: These preliminary results suggest that EMDR therapy focused on emotionally disturbing misophonia-related memories can reduce misophonia symptoms. RCTs with sufficient sample sizes are required to firmly establish the value of EMDR therapy for misophonia. HIGHLIGHTS This pilot study investigated the potential benefits of EMDR for 10 patients with misophonia. Three of the seven completers showed clinical improvement in misophonia symptoms within a mean of 2.6 sessions. The exploratory nature of this study makes further research necessary.

**Решение:** -2 клинический случай / серия случаев

---

### 470 · R0847

**Video_1_Synopsis and Qualitative Evaluation of a Treatment Protocol to Guide Systemic Group-Cognitive Behavioral Therapy for Misophonia.MOV**

2022 · https://doi.org/10.3389/fpsyt.2022.794343.s001

Misophonia is a disorder in which patients suffer from anger or disgust when confronted with specific sounds such as those associated with eating or breathing, causing avoidance of cue related situations resulting in significant functional impairment. Functional magnetic resonance imaging studies suggest misophonia is associated with increased activity in the auditory cortex and salience network, which might reflect increased vigilance toward specific misophonia triggers. New treatments have been developed and investigated in the last years in which this vigilance plays an important role. This is a synopsis of the first group protocol for systemic Cognitive Behavioral Therapy (G-CBT) for misophonia. We discuss the model of CBT for misophonia, provide a detailed guide to the treatment illustrated with a case study, discuss advantages, limitations, and possible pitfalls by a qualitative evaluation of the protocol, and review evidence for the protocol.</p

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 471 · R1310

**Misophonia in Children with Tic Disorders: A Case Series.**

2018 · Journal of developmental and behavioral pediatrics : JDBP · article, case reports, journal article · eng · https://doi.org/10.1097/dbp.0000000000000563

ABSTRACT: Objective: Misophonia is a condition characterized by the dislike or hatred (miso) of specific sounds (phonia) that results in an extreme emotional response. There has been growing interest in misophonia, with emerging evidence from neurodevelopmental populations and ongoing debate regarding the psychiatric classification and the mechanisms underlying this phenomenon. This is the first article to report on misophonic experiences and associated clinical characteristics in young people with tic disorders. Method: In this article, we present the cases of 12 children and young people with tic disorders who have attended clinics in the United Kingdom and Italy who report misophonia. Misophonia was classified as a selective aversive response in accordance with the criteria proposed by Schröder. Results: These cases support the view that a range of auditory stimuli may lead to negative/aversive emotional responses of varying degrees, with misophonia seeming to contribute to behavioral reactions. Among these, the most frequent was anger outbursts, followed by an increase in tics, trigger avoidance, repetition of the sound, and self-injurious behavior. No single treatment approach was effective, with some patients responding to cognitive behavioral therapies and others to pharmacological support. Conclusion: We postulate that misophonia could be an underestimated causative phenomenon for abrupt emotional dysregulation in individuals with tic disorders and should be considered as part of a comprehensive clinical assessment. This article presents findings of relevance to general discussions regarding the classification of misophonia, as well as the potential relationship between sensory abnormalities and the broader phenotype of tic disorders during development.

**Решение:** -2 клинический случай / серия случаев

---

### 472 · R1492

**Hyperacusis and misophonia: the lesser-known siblings of tinnitus.**

2011 · Minnesota medicine · article, case reports, journal article · eng · https://pubmed.ncbi.nlm.nih.gov/22413649/

Hyperacusis (decreased sound tolerance) and misophonia (fear of sound) are two conditions about which little is known. Consequently, physicians often struggle when they encounter patients who are affected by them. This article attempts to educate the medical community about hyperacusis and misophonia, both of which can have devastating effects on the lives of patients, and ways to manage them.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 473 · R0770

**Identifying Optimal Parameters for Neuroscience-Informed Interventions for Misophonia**

2023 · medRxiv · article, preprint · en · https://doi.org/10.1101/2023.06.25.23291872

Abstract Background Misophonia is the inability to tolerate certain aversive, repetitive common sounds. Methods Using a within-subjects experimental design, twenty-nine participants with misophonia and thirty clinical controls with high emotion dysregulation received inhibitory neurostimulation (1Hz) over a personalized medial prefrontal cortex (mPFC) target functionally connected to the left insula; excitatory neurostimulation (10Hz) over a personalized dorsolateral PFC (dlPFC) target; and sham stimulation over either target. Stimulations were applied while participants were either listening or cognitively downregulating emotions associated with personalized aversive, misophonic, or neutral sounds. Subjective units of distress (SUDS) and psychophysiological measurements (skin conductance response[SCR] and level [SCL], and high-frequency heart rate variability [HF-HRV]) were collected. Results Compared to controls, participants with misophonia reported higher distress (Δ SUDS = 1.91-1.93, p s&lt;.001) when listening to and when downregulating misophonic distress, although no psychophysiological differences were found. Both types of neurostimulation reduced distress significantly more than sham, with excitatory rTMS providing the most benefit (Cohen’s d SUDS = 0.53; d SCL = 0.14). Excitatory rTMS also enhanced the regulation of emotions associated with misophonic sounds in both groups when measured by SUDS ( d control = 1.28; d Misophonia = 0.94), and in the misophonia group alone when measured with SCL ( d = 0.20). Both types of neurostimulation were well tolerated and feasible to administer. Discussion Clinical controls and misophonic participants were different in their self-report but not in psychophysiological measures of distress and regulations. Participants reported the lowest misophonic distress when engaging in cognitive restructuring enhanced with high-frequency neurostimulation, a finding that offers insight into the best path forward for misophonia interventions.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 474 · R0583

**Positive Attributable Visual Sources Attenuate the Impact of Trigger Sounds in Misophonia.**

2024 · Multisensory research · article, journal article, journalarticle · eng · https://doi.org/10.1163/22134808-bja10137

Abstract Misophonia is characterized by strong negative reactions to everyday sounds, such as chewing, slurping or breathing, that can have negative consequences for daily life. Here, we investigated the role of visual stimuli in modulating misophonic reactions. We recruited 26 misophonics and 31 healthy controls and presented them with 26 sound-swapped videos: 13 trigger sounds paired with the 13 Original Video Sources (OVS) and with 13 Positive Attributable Visual Sources (PAVS). Our results show that PAVS stimuli significantly increase the pleasantness and reduce the intensity of bodily sensations associated with trigger sounds in both the misophonia and control groups. Importantly, people with misophonia experienced a larger reduction of bodily sensations compared to the control participants. An analysis of self-reported bodily sensation descriptions revealed that PAVS-paired sounds led participants to use significantly fewer words pertaining to body parts compared to the OVS-paired sounds. We also found that participants who scored higher on the Duke Misophonia Questionnaire (DMQ) symptom severity scale had higher auditory imagery scores, yet visual imagery was not associated with the DMQ. Overall, our results show that the negative impact of misophonic trigger sounds can be attenuated by presenting them alongside PAVSs.

**Решение:** ? эксперимент (26 мизофоников vs 31 контроль), проверить скрининг пула

---

### 475 · R0166

**Remote delivery of a mindfulness-based intervention for adults with tics: Protocol of a randomized controlled trial.**

2026 · Contemporary clinical trials · journal article, clinical trial protocol · eng · https://doi.org/10.1016/j.cct.2026.108224

Tourette Syndrome and persistent tic disorders (collectively, TS) are characterized by involuntary motor and/or vocal tics that onset in childhood. Existing evidence-based treatments-including behavior therapy and pharmacotherapy-are often only partially effective, associated with burdensome side effects, and/or inaccessible. The current paper describes a randomized controlled trial designed to compare a novel, remotely delivered mindfulness-based group intervention for tics (MBIT) to psychoeducation with relaxation and supportive therapy (PRST) in 150 adults with TS. All interventions and assessments will be delivered remotely using secure telehealth platforms and online electronic data capture systems. An independent evaluator masked to treatment condition will administer all tic assessments. The primary aims of the study are to: 1) examine the efficacy of MBIT relative to PRST for tic severity and 2) investigate the mechanism by which MBIT reduces tic severity. Additional aims include: 1) examination of secondary outcomes (e.g., comorbid conditions, quality of life), and 2) exploration of the durability of any observed improvements over a 6-month follow-up. Findings have the potential to meaningfully expand the range of evidence-based treatment options available to adults with TS.

**Решение:** -6 не про мизофонию

---

### 476 · R1328

**Self-Assessment Questions**

2017 · Seminars in Hearing · article · en · https://doi.org/10.1055/s-0037-1598117

This section provides a review. Mark each statement on the Answer Sheet according to the factual materials contained in this issue and the opinions of the authors. Article One (pp. 3–25) Why is knowledge of typical intra- and intersubject variability in clinical audiometric measures, including threshold measures and loudness judgments, over an extended time period of 1 year important information? It instills clinician confidence in the stability of the patient's performance (relative to his or her previous performance as well as with respect to that of others on comparable audiometric tests) independent of changes due to age or pathology. It allows the clinician to gauge changes in relevant audiometric outcome measures used in assessing the efficacy or effectiveness of an experimental therapeutic intervention against inherent variability expected in these measures over an extended time in a control group of normalhearing individuals. It may encourage the patient to return for annual hearing tests. It is essential for powering and estimating sample size in evidence-based audiological research using these measures to assess treatment validity and efficacy. A, B, and D are correct. Repeated measures of pure tone thresholds yield the lowest intrasubject variability when measured over a prolonged period of days in close succession within the same test session with the headphones removed between the repeated measurements in close succession within the same test session without the headphones removed between the repeated measurements just after the end of an upper respiratory condition none of the above Repeated measures of loudness discomfort levels typically yield larger values for intersubject variability than for intrasubject variability smaller values for intersubject variability than for intrasubject variability larger within-subject variability than typical test–retest reliability no differences between inter- and intrasubject variability none of the above In this study, changes in level required for a categorical loudness change across the continuum for the Contour Test of Loudness were similar for warble tones and spondee speech stimuli were greatest for categorical judgments for warble tones between the “very soft” and “soft” categories were greatest for categorical judgments for warble tones between the “loud, but OK” and “uncomfortably loud” categories were more uniform across categories for warble tones than for the spondee speech stimuli none of the above In this study, repeated measures of categorical judgments for warble tones increased in level over time for all categories increased in level over time for 500 Hz, but not for either 2,000 or 4,000 Hz decreased in level over time more for 4,000 Hz than for either 500 or 2,000 Hz were independent of frequency none of the above Article Two (pp. 26–52) As defined and measured in this study, how were absolute judgments of loudness similar, but different from relative judgments of loudness? Absolute judgments were greater in level (decibels) than corresponding relative judgments measured within group. Absolute judgments were slightly less in level (decibels) than corresponding relative judgments measured within group. Relative loudness judgments were made in virtual isolation from other judgments, whereas absolute loudness judgments were made in the context of a continuum of categorical judgments. Absolute loudness judgments were clinically synonymous with relative loudness judgments for “soft” and for “loud, but OK” sound levels measured within group. Both B and D are correct. In this study, there was no clinically significant effect on loudness judgments within session and within group for task order trial order left ear right ear all of the above “Comfortable” judgments of loudness annot be estimated from the measured levels judged to be “soft” and “loud, but OK” can be estimated from measured “soft” and “loud, but OK” judgments by bisecting the levels for the respective judgments predicted from measured “soft” and “loud, but OK” judgments underestimated measured “comfortable” judgments by ~2 dB predicted from measured “soft” and “loud, but OK” judgments overestimated measured “comfortable” judgments by ~2 dB B and C Why might prescriptive fitting protocols based on average loudness data for groups of listeners fail? An individual listener's loudness judgments may not be typical of average group loudness judgments. An individual listener's loudness judgments may underestimate average loudness judgments by 20 dB or more. An individual listener's loudness judgments may overestimate average loudness judgments by 20 dB or more. The hearing-impaired listener cannot reliably perform loudness judgments. A, B, and C are correct. Average loudness judgments measured monthly across six test sessions in this study were unchanged between sessions 1 and 6 increased by ~2 to 3 dB between sessions 1 and 6 decreased by ~2 to 3 dB between sessions 1 and 6 are consistent with changes in loudness discomfort level judgments measured after chronic exposure to amplified sound from bilateral hearing aids are inconsistent with changes in loudness discomfort level judgments measured after chronic exposure to amplified sound from bilateral hearing aids Article Three (pp. 53–70) People who are sensitive to sound should wear hearing protection devices under which of the following circumstances? Any time they will be around sounds that are uncomfortable for them, including soft sounds All the time To protect their hearing from noiseinduced hearing loss Never Activity avoidance due to sound tolerance problems were most frequently reported by respondents for which of the following activities? Driving the car and going to concerts Going to concerts and movies Going to church and movies Taking care of children and doing housework Nearly all questionnaires that could be used to identify the impact of reduced sound tolerance on hearing aid use evaluate other hypersensitivities (e.g., light, touch) True False People fitted with hearing aids who complain about the hearing aids being too loud when they are having dinner with their family, but not when they are in a restaurant, may be experiencing this type of reduced sound tolerance Misophonia Recruitment Hyperacusis None of the above The majority of the respondents indicated that tinnitus was their primary problem True False Article Four (pp. 71–93) Auditory brainstem and middle latency responses were recorded in this study bilaterally unilaterally simultaneously to click stimuli B and C Auditory brainstem responses were evaluated for wave I, III, and V latency wave V latency wave V-V peak-to-peak amplitude wave I and wave V amplitudes to click stimuli B and C Middle latency responses were evaluated for wave Pa latency wave Na-Pa amplitude wave Na amplitude wave Na latency A and B The auditory brainstem response (ABR) wave V latency values were inconsistent with pretreatment predictions (i.e., shorter than normal latency values) only at 500 Hz inconsistent with posttreatment predictions (i.e., similar to normal latency values) only at 2,000 Hz consistent with all pretreatment predictions consistent with all posttreatment predictions inconsistent with pre- and posttreatment predictions at 500 and 2,000 Hz The only ABR or middle latency response (MLR) measure consistent with both pre- and posttreatment study predictions for all cases was ABR amplitude for wave V-V' at 2000 Hz ABR amplitude for wave V-V' at 500 Hz MLR latency for wave Pa at 2,000 Hz MLR latency for wave Pa at 500 Hz MLR amplitude for wave Na-Pa at 500 and 2,000 Hz Article Five (pp. 94–114) When normal-hearing adults judge the loudness of brief tonal stimuli on a behavioral loudness scaling technique, such as the Contour Test of Loudness, their individual responses are homogeneous and show little intersubject variability vary considerably (30 to 40 dB) when judging the loudness of these stimuli within a specific loudness category display greater variability for the lowest loudness categories, such as “very soft” and “soft,” and little or no variability for the higher loudness categories, such as “loud, but OK” and “uncomfortably loud” display a systematic increase of 10 dB for each loudness category clearly identify a consistent anchor level across subjects for their loudness judgment of a “very soft” tone burst signal When the participants' behavioral loudness judgments of the brief tone burst signals increased from “comfortable, but slightly soft” to “loud, but OK” categories, the response measures of the auditory brainstem response (ABR) and middle latency response (MLR) showed which of the following patterns? Both the response latencies for ABR wave V and MLR wave Pa and their corresponding response amplitudes decreased. The response latencies for ABR wave V and MLR wave Pa increased and their corresponding response amplitudes decreased. There was an inverse relation, such that the response latencies for ABR wave V and MLR wave Pa decreased and the response amplitudes for these two waves increased as the loudness category increased. There was no significant change in either the ABR/MLR response latencies or response amplitudes as a function of loudness categories. The response measures for the ABR changed significantly as a function of loudness category; however, there were no corresponding changes in the response measures of the MLR. Which response measures of tone-evoked ABRs/MLRs are the most sensitive indicator of the listener's perception of loudness? Response latencies Response amplitudes Overall morphology of the response Response latencies and amplitudes Replicability of the response To date, the literature has suggested that which of the following objective auditory measure(s) might provide insight into the behavioral processing of loudness that occurs in the peripheral and central auditory nervous systems? Click-evoked ABRs Late evoked wave P1-N1-P2 complex, the auditory steady state response, and tone-evoked ABRs/MLRs Acoustic reflexes Otoacoustic emissions Real ear measurements What clinical populations might benefit from having an objective audiologic tool to assess the growth of loudness to assist in prescriptive protocols for fitting nonlinear hearing aids? Young children with a sensorineural hearing loss Cognitively challenged adults with a sensorineural hearing loss Individuals with reduced sound tolerance issues Elderly individuals with a sensorineural hearing loss All of the above Article Six (pp. 115–129) Positive treatment outcome for hearing impaired persons with auditory reduced dynamic range includes improvements in loudness discomfort levels a comfortable transition into appropriate amplification reduced complaints of discomfort to sound all of the above Sound therapy for auditory dynamic range expansion is best delivered by a sound generator used in one ear set at soft level sound generators used in both ears set at soft levels sound machine or radio played all night sound generators in both ears used with increased volume weekly Reduced sound tolerance is always accompanied by tinnitus only seen in persons with bilateral hearing loss a predictor of future changes in hearing sensitivity controlled by the cortical and subcortical areas of the brain Treatment of reduced sound tolerance should include use of earplugs or earmuffs whenever a person is worried about the sounds in the environment counseling, which includes correct use of sound therapy and appropriate use of noise protection avoidance of social activities while under treatment immediate use of hearing aids for predetermined periods of time daily The counseling implemented in this study was adapted from counseling used in Tinnitus Retraining Therapy sets the stage for demystifying the subject's problem and neutralizing the negative emotional associations is effective alone in decreasing auditory gain both A and B Article Eight (pp. 130–150) Low-level broadband sound therapy for dynamic range expansion was shown in this study to be most effective when offered with a hearing aid specialized structured counseling placebo sound generators no counseling subthreshold noise The sound therapy intervention is shown to be efficacious for hearing-impaired persons with loudness adaptation profound hearing loss conductive hearing loss hyperacusis loudness recruitment The sound therapy intervention described in this study is based on the idea that the therapeutic noise increases the gain of an underlying central auditory neuronal process reduces the gain of this process has no effect on the gain setting of this process operates by adaptive plasticity B and D After successfully completing the sound therapy intervention to expand the auditory dynamic range, aided listeners were able to tolerate sound at higher levels were unable to listen to sound at levels greater than at pretreatment achieved improved word recognition scores (if not limited by ceiling performance) demonstrated no aided benefit reported reduced aided satisfaction Hearing aid use subsequent to successful intervention to expand the auditory dynamic range was shown in this report to differ among participants. For some, amplification sustained the intervention effects in full fully eliminated the intervention effects partially sustained the intervention effects enhanced the intervention A and C

**Решение:** -7 ceu / self-assessment questions

---

### 477 · R1516

**[Primary Human Immunodeficiency Virus infection revealed by psychiatric symptoms].**

2006 · L'Encephale · article, case reports, english abstract · fre · https://doi.org/10.1016/s0013-7006(06)76189-9

Introduction Any atypical psychiatric disorder, especially if associated with somatic manifestations and when any psychiatric antecedents are missing, should lead to search for an organic pathology, and notably a Human Immunodeficiency Virus (HIV) infection. In the case of Primary Human Immunodeficiency Virus Infection (PHI), which is often symptomatic, the diagnosis is seldom made, probably because of atypical or non specific manifestations. Therefore, it is essential to consider such a diagnosis, because it may have important clinical and public health consequences (stopping the contamination chain). Case-report We present the case of a 38 year-old homosexual man from West Indies, in whom the diagnosis of PHI had been made on the basis of psychiatric symptoms evoking a Major Depressive Episode with a doubt on the presence of psychotic symptoms. To our knowledge, this is the first report of psychiatric PHI found in scientific literature. Clinical presentation was atypical: the patient had no psychiatric history (except probably a schizotypical personality, according to his family), symptoms were atypical (sudden onset and fast improvement) associated with somatic symptoms (fever, headache, sound intolerance), the latter possibly due to a meningo-encephalitis, which had been underestimated and attributed to dehydration in a period when France was faced with an important and unexpected heatwave. Blood samples were performed on admission and revealed a thrombopenia and presence of HIV P24 antigen, testifying a contamination by HIV 2 to 4 weeks earlier, this possibility having been confirmed by the patient. Further analyses found a Western-Blot partially positive test and an HIV viral load of 315 711 Eq copies/mL. Discussion The main question about this report is the primary or secondary nature of psychiatric symptoms towards HIV infection, given that in this patient mood alteration could have possibly occurred, before HIV contamination, due to particularities of his personal and professional life. We can also question whether the neurological manifestations of PHI might be changed by a schizotypical personality. Further reports are required to answer these questions.

**Решение:** -2 клинический случай / серия случаев

---

### 478 · R0330

**La misofonia en l'entorn hospitalari: identificació dels sons desencadenants i propostes de millora. Projecte de recerca**

2025 · Universitat de Girona Digital Repository (Universitat de Girona) · bachelor thesis, dissertation, thesis · ca · http://hdl.handle.net/10256/27107

Introduction: Misophonia is a condition characterized by disproportionate emotional and physiological reactions, termed “misophonic responses,” to both organic and inorganic everyday sounds, known as triggers. Misophonic responses may include anxiety, stress or tachycardia. Despite having an estimated prevalence of 20%, it is not recognized in the DSM-V or ICD-11, underdiagnosed and little known. The lack of knowledge in the healthcare setting could be aggravating the situation of hospitalized people because they are unable to use their personal coping mechanisms. Objective: To identify the factors in the hospital enviroment that contribute to agrravate the symptoms of misophonia and to propose effective measures to reduce the triggers, thus improving hospital stay. Methodology: This is a qualitative phenomenological study carried out at the General Hospital of Granollers. The sample will be formed by people with diagnosis or symptoms of misophonia who star at least three days in hospital. Data collection will be carried out by means of semi-structured interviews and will be analyzed with the ATLAS.ti program, in which codes and subcodes will be applied to classify triggers, emotional and physiological reactions, coping mechanisms and proposals for improvement provided by the participants. Practical implications: The results of this work could contrubute to reducing the emotional and physical impact generated by the hospital enviroment, creating more inclusive hospitals and making the affected population more visible. The study promotes research, detection and recognition of the disease within the healthcare system and steeks to ensure that nursing care adopts a holistic vision. In the long term, the implementation of the proposed mesures could improve the recovery and quality of hospital stay of those affected 10 3

**Решение:** -1 обзор литературы / концептуальная статья

---

### 479 · R0648

**Misophonia assessment tools: a systematic review**

2024 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint, project · https://doi.org/10.17605/osf.io/tgmrv

A systematic review of misophonia assessment tools

**Решение:** -7 protocol / preregistration without data

---

### 480 · R0711

**Novel five-phase model for understanding the nature of misophonia, a conditioned aversive reflex disorder**

2023 · F1000Research · article · en · https://doi.org/10.12688/f1000research.133506.2

Background: Misophonia is a recently identified condition in which a person perceives a subtle stimulus (e.g., eating sounds, hair twirling) and has an intense, negative emotional response. Misophonia cannot be classified with established nosological systems. Methods: We present a novel five-phase model of misophonia from a cognitive-behavioral framework. This model identifies a learned reflex of the autonomic nervous system as the primary etiology and maintenance of misophonia. Phase one is anticipatory anxiety and avoidance. Phase two is a conditioned physical reflex (for example, the tensing of calf muscles) that develops through stimulus-response Pavlovian conditioning. Phase three includes intense negative emotional responses and accompanying physiological distress, thoughts, urges, and emotion-driven behavior. Phase four is the individual’s coping responses to emotional distress, and phase five is the environmental response and resulting internal and external consequences of the coping behaviors. Each phase helps explain the maintenance of the response and the individual’s impairment. Results: Anticipatory anxiety and avoidance of phase one contributes to an increased arousal and awareness of triggers, resulting in increased severity of the trigger experience. Both the Pavlovian-conditioned physical reflex of phase two and the emotion-driven behavior caused by the conditioned emotional response of phase three increase with in vivo exposure to triggers. Phase four includes internal and external coping behaviors to the intense emotions and distress, and phase 5 includes the consequences of those behaviors. Internal consequences include beliefs and new emotions based on environmental responses to anger and panic. For example, the development of emotions such as shame and guilt, and beliefs regarding how ‘intolerable’ the trigger is. Conclusions: We assert misophonia is a multi-sensory condition and includes anticipatory anxiety, conditioned physical reflexes, intense emotional and physical distress, subsequent internal and external responses, and environmental consequences.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 481 · R1105

**Assessment and Intervention for Individuals With Misophonia**

2021 · Journal of Health Service Psychology · article, other literature type · en · https://doi.org/10.1007/s42843-021-00025-6

Misophonia is a condition characterized by marked distress following the perception of innocuous sounds and is often accompanied by behavioral avoidance. This presentation is currently absent from the Diagnostic and Statistical Manual of Mental Disorders, as it remains poorly understood and understudied. Despite these limitations, there have been recent efforts to develop empirically supported assessment tools and intervention. Interventions for misophonia predominantly incorporate principles of cognitive-behavioral interventions. This article describes in detail the assessment and intervention process of working with an individual with misophonia.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 482 · R0172

**Ep. 2565: Why Background Conversation Hijacks Your Focus**

2026 · Zenodo (CERN European Organization for Nuclear Research) · audiovisual/, other · en · https://doi.org/10.5281/zenodo.20181308

Episode summary: Ever feel like background conversation hijacks your brain the moment you try to focus? This episode explores sensory gating deficit—the neurological mechanism behind auditory distraction in ADHD. We break down the P50 suppression ratio, why white noise can paradoxically help, and the difference between sensory gating issues, misophonia, and hyperacusis. We also cover practical interventions: high-fidelity earplugs, stochastic resonance with noise, neurofeedback targeting the sensory motor rhythm, and how stimulant medications affect filtering. Plus, why "just ignore it" is neurologically naive advice. Show Notes Why Some Brains Can't Filter Out Background Noise** For many people, background conversation is just that—background. For others, it's a cognitive wrecking ball. This episode unpacked the neuroscience behind that difference, focusing on a phenomenon called sensory gating deficit. **What Is Sensory Gating?** Sensory gating is the brain's ability to filter out irrelevant stimuli before they reach conscious awareness. It happens automatically in most people—about 50 milliseconds after a sound hits the ear, the brain decides whether to pass it along for processing or shunt it to the background. In people with ADHD, that gating mechanism is measurably weaker. The technical marker is called P50 suppression. If you hear two identical clicks in quick succession, a healthy brain shows a substantially reduced response to the second click—it's learned the sound is irrelevant. In ADHD brains, that suppression is weaker. The brain treats every instance as novel, which means background conversation—already a high-priority signal for human brains—keeps fragmenting working memory. **This Is Not Misophonia or Hyperacusis** The episode drew important distinctions between three conditions that are often confused. Misophonia involves an emotional reaction—rage or disgust—triggered by specific sounds like chewing or breathing. Hyperacusis is physical discomfort or pain from sounds at normal volumes. Sensory gating deficit is neither. The person isn't angry at the sound, and it isn't too loud. Their brain simply fails to shunt it to the background. **The White Noise Paradox** One of the most counterintuitive findings discussed is that white noise can actually help. This is the stochastic resonance phenomenon: a moderate level of random noise can boost signal detection in certain neural systems by raising baseline activation closer to firing threshold. For ADHD brains with lower tonic dopamine levels in prefrontal regions, that extra noise may partially compensate for underactivation. Studies have shown that white noise around 70-80 decibels during cognitive tasks improved performance on memory and attention measures—though the optimal level varies dramatically between individuals. **Interventions That Might Help** The episode covered several approaches, each with different evidence levels: - **High-fidelity earplugs** (Loop, Flare, Vibes) reduce overall volume while preserving frequency balance, unlike foam earplugs that muffle everything. - **Active noise control earbuds** with adaptive transparency (like AirPods Pro) let you selectively filter sound. - **Bone conduction headphones** playing white or brown noise leave ear canals open while providing stochastic resonance benefits. - **Neurofeedback** targeting the sensory motor rhythm (SMR) has shown promise in strengthening thalamic gating, with a 2016 RCT finding improved P50 suppression correlated with reduced distractibility. - **Stimulant medications** normalize P50 suppression by increasing dopamine and norepinephrine in prefrontal cortex, strengthening top-down attentional control. - **Auditory training programs** exist but show limited generalization to real-world situations. **The Invisibility of Impaired Accommodation** The episode emphasized a deeper frustration: sensory gating deficits are invisible from the outside. Two people can have identical hearing and radically different experiences of the same sound environment. Telling someone with a sensory gating deficit to "just ignore it" is neurologically naive—the mechanism that does the ignoring is the thing that's impaired. The episode left open the question of whether reduced sensory gating might actually be adaptive in certain evolutionary contexts, but for daily life in a noisy world, it remains a genuine cognitive challenge with no single silver bullet. Listen online: https://myweirdprompts.com/episode/sensory-gating-deficit-adhd

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 483 · R1504

**Intervention for restricted dynamic range and reduced sound tolerance**

2008 · The Journal of the Acoustical Society of America · conference-abstract · en · https://doi.org/10.1121/1.2935164

Hyperacusis is an abnormal condition of sound intolerance that may cause some persons to reject amplified sound from their hearing aids. A significant secondary benefit reported for many patients receiving Tinnitus Retraining Therapy (TRT) is increased Loudness Discomfort Levels (LDLs). TRT involves both counseling and sound therapy (i.e., daily exposure to soft sound from bilateral noise generators (NGs)). We implemented a randomized, double-blind, placebo-controlled clinical trial to assess the efficacy of TRT as an intervention to improve sound tolerance in hearing-aid eligible persons with hyperacusis and/or restricted dynamic ranges. Subjects were assigned to one of four treatment groups: 1) full treatment, both counseling and NGs, 2) counseling and placebo NGs, 3) NGs without counseling, and 4) placebo NGs without counseling. They were evaluated at least monthly, typically for five months or more, on a variety of audiometric tests, including LDLs, the Contour Test for Loudness, and word recognition measured at comfortable and loud levels. Over 80% of the subjects assigned to full treatment achieved significant benefit (defined as shifts of greater than 10 dB in LDLs or the Contour Test uncomfortable level); whereas, most subjects assigned to a partial treatment group did not benefit from their treatment. [Supported by NIH].

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 484 · R1012

**Mental health literacy program: misophonia**

2021 · RACS · journal article · pt · https://core.ac.uk/download/543997001.pdf

Os níveis de literacia são um fator determinante na existência de conhecimentos e de crenças adequadas, associados à prevenção e tratamento das perturbações mentais. Assim, o programa de promoção de literacia em misofonia reveste-se como ponto chave na educação e sensibilização face à condição. A prevalência estimada desta perturbação, conjugada com os baixos níveis de literacia, exacerbam a necessidade de uma nova abordagem sustentável e escalável nos programas de literacia. O objetivo é o empoderamento dos participantes para o reconhecimento e autogestão da misofonia e a melhoria de atitudes em relação à condição. O programa e-learning de promoção de literacia de misofonia que propomos implementar, recorre a uma abordagem inovadora, positiva e interativa, potenciando a assimilação e implementação da informação disponibilizada. Espera-se um aumento da literacia e consciencialização sobre misofonia, redução do estigma e aumento da eficácia na procura de ajuda. A capacitação da população permitirá diminuir o impacto da misofonia e permitir o acesso a cuidados de saúde especializado como a intervenção da terapia ocupacional.info:eu-repo/semantics/publishedVersio

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 485 · R0183

**Transdiagnostic mechanisms of decreased sound tolerance**

2026 · Nature Reviews Psychology · article, journalarticle, review · en · https://doi.org/10.1038/s44159-026-00565-y

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 486 · R1390

**Exploring perceptions of sexual assault in African American collegiate women with membership in Greek-letter sororities at a predominantly white institution**

2016 · dissertation · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 487 · R1445

**Theory and Treatment of Tinnitus and Decreased Sound Tolerance**

2014 · Thieme eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1055/b-0034-102419

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 488 · R1189

**Extraordinary emotional responses elicited by auditory stimuli linked to the consumption of food and drink**

2020 · Nippon Onkyo Gakkaishi/Acoustical science and technology/Nihon Onkyo Gakkaishi · article · en · https://doi.org/10.1250/ast.41.28

A growing number of food and beverage brands have recently started to become interested in trying to link extraordinary emotional experiences to their product offerings. Oftentimes, such extraordinary responses are triggered by product-extrinsic auditory and, to a lesser extent, visual stimuli, such as music or videos having particular sensory qualities or semantic meaning. While much of the interest in this area recently has been linked to the Autonomous Sensory Meridian Response (ASMR), it is worth noting that there are also a number of other responses, such as chills, thrills, and so-called `skin orgasms' that have been documented previously, if not always in a food-related context. Elsewhere, both multisensory dining experiences and experiential events have also been reported to bring people to tears. There are, in other words, a number of extraordinary emotional responses that can or, in some cases, already have been linked to the consumption of food and drink. While such responses to auditory stimuli (increasingly mediated by technology) in the context of food are by no means widespread, they nevertheless hold the potential of delivering dramatic food and beverage experiences that offer the promise of being more stimulating, more memorable, and more emotionally-engaging than anything that has gone before.

**Решение:** -6 не про мизофонию

---

### 489 · R0215

**On Noises and People**

2026 · Antología Concurso Literario USAL en Lengua Inglesa · article · es

Misophonia is a disorder of decreased tolerance to specific sounds or their associated stimuli.Unfortunately, I am one of the seemingly few people who suffer from it.And, trust me, I do not exaggerate when I say it feels like a psychological torture method.Unlike other invisible ailments, you cannot medicate or meditate it away.You just have to sit there, trying to be normal as if your sanity was not being slowly chipped away with every pen click, sniff, or chewing mouth you are trapped with.Having to deal with misophonia is like being shoved onto a knife throwing wheel every single day of your life, the knives being the noise that will always catch you off guard, and the knife thrower being the cruel universe which seems to be constantly conspiring against you.The worst part is that, no matter how much you try, you will never break free from these triggering sounds, unless you decide to become a monk and live in the mountains away from society for the rest of your life.Personally, I do not want to become a monk, as peaceful as my brain would finally be.I actually enjoy being with people, with most people at least.Sadly, coexisting with others also means having to coexist with the dreadful symphony of noises they are capable of emitting.Some people can make this coexistence easier, others, on the contrary, make it completely impossible, and some others do nothing about it.I will start off by referring to people who are actually normal, decent people, but make me furious the second they emit any sound which triggers my misophonia.Most commonly, the pen clickers.They are everywhere and you will never be able to escape them no matter what, especially when you are trapped in a room where pens proliferate, such as a classroom.In that context, all you can do is leave for a few minutes and pray that the haunting click, click, click, click has stopped the moment you come back.There are also the ones who do not even realize they are producing disturbing sounds, because they are asleep.People who snore, especially those whose snoring is as loud as a semitruck horn, can be a nightmare.You either have to get up, shake them, and tell them they are snoring (which they will utterly resent), suffer in silence while the snores penetrate your skull, or put some loud music on, using earphones, of course.The last choice seems to be, and usually is, the best option, though it is pretty difficult to sleep while your eardrums are being blasted by music and, if you are a side sleeper, one of your earbuds is stabbing your ear.There is another kind, which is most frequent during the winter: the sniffers, those who have a cold and have either forgotten or did not think they would need to bring tissues, making the entire room aware of that by sniffing all day long.I must confess that I have been guilty of this, forgetting to bring tissues and only remembering when I had already left home, having to endure not being able to blow my noise for hours and also having to put others through the pain of hearing me sniff every other minute.There are also the best, and nicest people alive, those who understand your plight and avoid making noises out of pure empathy.They may start making some noises unheedingly, such as the pen clicking, but once they become aware of it, they stop in order not to trigger your misophonia.Obviously, not that their thoughtfulness would cure misophonia or delete triggering noises altogether, but the intention is what matters the most.In their case, I do not get angry and try my best to ignore any noises they might make, since I know they are doing their best to be quiet.It is rare to find people like these because most fail to understand what you are talking about and do not pay attention or act annoyed as though it were a huge inconvenience.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 490 · R0945

**Treatment of Misophonia with Risperidone in a Patient with Autism Spectrum Disorder.**

2022 · Case reports in psychiatry · article, case reports, journal article · eng · https://doi.org/10.1155/2022/3169834

We report the case of a 32-year-old male with autism spectrum disorder (ASD) suffering from severe misophonia. After titrating risperidone to 2 mg twice a day, the patient reported a significant reduction in his symptoms and his Amsterdam misophonia scale-revised (AMISOS-R) score dropped by from 31 to 5. Upon discharge, the patient was noted to have decreased irritability and overall improved behavior and effect. This significant symptomatic improvement was likely not explained by inpatient admission alone or other simultaneous pharmacologic treatments, as the effect was seen during an isolated titration of risperidone with other treatments remaining constant. Although, unfortunately, follow-up findings indicated that the treatment was not curative for the patient, risperidone's potential for treating misophonia may warrant systematic investigation.

**Решение:** -2 клинический случай / серия случаев

---

### 491 · R1537

**[Treatment of postoperative pain with non-narcotic drugs; evaluation of lysine acetylsalicylate in high doses. Double-blind controlled study].**

1981 · Minerva anestesiologica · article, clinical trial, comparative study · ita · https://pubmed.ncbi.nlm.nih.gov/6793921/

Further work on the treatment of postoperative pain with non-narcotic analgesics involving an investigation of the effect of twice the customary dose of lysine acetylsalicylate in a double-blind trial versus meperidine is reported. In addition to subjective and objective pain, the parameters included blood pressure, pulse rate, breathing rate, sweating, pupil diameter, nausea, vomiting, somnolence, hiccuping feeling of cold, erythema, dizziness, and nasograstric sound intolerance. Application of Wilcoxon's non-parametric tests and the chi-square test showed that the drug was as good as or better than meperidine with regard to pain, and performed very well overall with respect to the other parameters. The conclusion is drawn that its administration in high doses is justified in many patients subjected to general surgery.

**Решение:** -6 не про мизофонию

---

### 492 · R1108

**Additional file 1 of Improving the measurement of alexithymia in autistic adults: a psychometric investigation and refinement of the twenty-item Toronto Alexithymia Scale**

2021 · figshare · article · und · https://doi.org/10.6084/m9.figshare.14150932.v1

Additional file 1. Supplementary Materials and TAS-8 Questionnaire.

**Решение:** -6 не про мизофонию

---

### 493 · R0445

**Cochlear neural contributions to triple network changes in tinnitus, hyperacusis & misophonia? A perspective review.**

2025 · Hearing research · article, journal article, review · eng · https://doi.org/10.1016/j.heares.2025.109305

What do tinnitus, the perception of sounds without an internal or external source of noise, hyperacusis, the pathological hypersensitivity to noise, or misophonia, an intolerance to certain everyday noises, have in common, and what differentiates them? A large number of excellent studies focused in the last few decades on identifying the neural correlates of tinnitus, hyperacusis, or misophonia on the basis of central triple-network changes. In this perspective review we explicitly examine, possible differential and causal involvement of peripheral components as a presumptive trigger that may drive observed triple-network changes. Based on our results, we venture to hypothesize that: (i) tinnitus, hyperacusis, and misophonia can occur despite clinically normal hearing thresholds, and are likely causally independent of sex and age, (ii) tinnitus and hyperacusis, but possibly also misophonia are related to altered auditory processing that through desynchronized (tinnitus) or hyperactive (hyperacusis, misophonia) bottom-up ascending processing potentially explains the activity changes in, e.g., default or salient brain networks, as suggested in various studies of these different diseases. (iii) In misophonia a stress-induced top-down influence, as deep as the auditory nerve fibers, may be discussed as a contributor to generating misophonia-trigger sounds, a hypothesis that can be tested in future studies. We hope that the selective consideration of a possible interaction between peripheral and central components will help to minimize the greatest handicap of these pathologies to date towards successful therapy: the lack of clarification of the underlying causative mechanism of the diseases.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 494 · R1534

**Components of Decreased Sound Tolerance : Hyperacusis, Misophonia, Phonophobia**

2001 · ITHS News Lett · google scholar result · http://www.hazell.plus.com/iths/papers1/DST_NL2_PJMJ.pdf

… In particular, as we recently proposed a new term “misophonia” and we would like to provide some explanation and justification for it (Jastreboff, PJ and Jastreboff, MM, Tinnitus and …

**Решение:** -1 обзор литературы / концептуальная статья

---

### 495 · R0055

**Collaboration and Assistive Technology: Facilitating Joint Awareness for Noise Sensitivity**

2026 · CHI Conference on Human Factors in Computing Systems · conference-paper · https://doi.org/10.1145/3772318.3793203

Existing research has explored various methods to support people with noise sensitivity (PWNS), from desensitization therapies to technological solutions. However, there is a gap in systems that identify and monitor characteristics of noise sensitivity experiences to help PWNS and their companions better understand their condition and make informed management decisions. To fill this gap, we developed AudioBuddy, an app with sensing and tracking features designed to promote awareness between PWNS and their companions. We tested AudioBuddy as a technological probe over a two-week field deployment. Our results show that AudioBuddy can support awareness of how sounds and environments influence the psychophysiological states of PWNS, aiding in understanding noise sensitivity experiences. Nonetheless, technical limitations impacted the depth of awareness participants could attain. We discuss challenges and opportunities for future systems to facilitate awareness among PWNS and their companions.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 496 · R0888

**Novel Five-Phase Model for Understanding the Nature of Misophonia and Providing Treatment**

2022 · PsyArXiv · article, preprint · en · https://doi.org/10.31234/osf.io/6sqpr

We present a novel five-phase model of misophonia from a cognitive-behavioral framework. This model identifies a learned reflex of the autonomic nervous system as the primary etiology and maintenance of misophonia. Phase 1 is anticipatory anxiety and avoidance. Phase 2 is a conditioned physical reflex (for example, the tensing of calf muscles) that develops through stimulus-response Pavlovian conditioning. Phase 3 includes intense negative emotional responses and accompanying physiological distress, thoughts, urges, and emotion-driven behavior. Phase 4 is the individual’s coping responses to emotional distress, and phase 5 is the environmental response and resulting internal and external consequences of the coping behaviors. Each phase helps explain the maintenance of the response and the individual’s impairment. Anticipatory anxiety and avoidance of phase 1 contributes to an increased arousal and awareness of triggers, resulting in increased severity of the trigger experience. Both the Pavlovian-conditioned physical reflex of phase 2 and the emotion-driven behavior caused by the conditioned emotional response of phase 3 increase with in vivo exposure to triggers. Phase 4 includes internal and external coping behaviors to the intense emotions and distress, and phase 5 includes the consequences of those behaviors. Internal consequences include beliefs and new emotions based on environmental responses to anger and panic. For example, the development of emotions such as shame and guilt, and beliefs regarding how “intolerable” the trigger is. We assert misophonia is a multi-sensory condition and includes anticipatory anxiety, conditioned physical reflexes, intense emotional and physical distress, subsequent internal and external responses, and environmental consequences.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 497 · R0253

**Effetti del suono**

2025 · Edizioni Minerva Medica · part of book or chapter of book, book · ita · https://hdl.handle.net/2434/1210943

Il capitolo analizza il ruolo fondamentale dell’udito nello sviluppo e nella vita dell’essere umano. L’orecchio è attivo già in fase fetale e rappresenta non solo un sistema di percezione dei suoni, ma anche un elemento chiave per lo sviluppo cognitivo, linguistico ed emotivo, grazie alla sua integrazione con numerose aree cerebrali. La mancanza di stimolazione uditiva precoce, come nel caso della sordità congenita, compromette l’acquisizione del linguaggio. Il suono e la musica hanno effetti potenti sul cervello: possono favorire emozioni, socialità, apprendimento e processi terapeutici (musicoterapia), ma in alcuni casi possono anche avere effetti negativi, come crisi epilettiche musicogene o comportamenti a rischio legati all’ascolto di musica ad alto volume. Ampio spazio è dedicato ai danni da rumore: l’esposizione prolungata a suoni intensi può causare sordità permanente e acufeni, aggravati oggi dall’inquinamento acustico e dall’uso scorretto di cuffie e auricolari. Vengono descritte inoltre condizioni di ridotta tolleranza al suono, come l’iperacusia e la misofonia, legate a un’alterata interazione tra sistema uditivo, limbico e nervoso autonomo. Infine, il capitolo sottolinea l’importanza della prevenzione della sordità attraverso comportamenti corretti, educazione all’ascolto, limitazione dell’esposizione al rumore e rispetto dei limiti di sicurezza, con particolare attenzione a bambini e adolescenti.

**Решение:** -1 глава книги / справочник

---

### 498 · R1136

**Mizofoni Tedavisinde BDT ve Olgu Sunumu**

2020 · conference object, conference paper · tur · https://avesis.ogu.edu.tr/publication/details/e0caca20-bb78-4e28-af52-c8553d45319a/oai

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 499 · R0650

**Steroids for the Treatment of Misophonia and Misokinesia.**

2024 · Case reports in psychiatry · article, case reports, journal article · eng · https://doi.org/10.1155/2024/3976837

Misophonia and misokinesia are disorders characterized by intensely negative physical and emotional reactions to specific auditory and visual stimuli. The availability of effective treatments, especially pharmacological ones, is limited. This report presents a case of a 35-year-old male with severe misophonia and misokinesia who experienced nearly complete resolution of symptoms while undergoing high-dose steroid therapy for an unrelated muscular injury. Two days after starting a 20 mg oral prednisone taper pack (in which the steroid dose is reduced by 4 mg daily), his Amsterdam Misophonia Scale (A-Miso-S) score drastically reduced from a baseline of 23 (i.e., extreme symptoms) to 1, with symptom relief persisting for approximately 2 weeks after completing the taper. Months later, a daily dose of prednisone (4 mg) was reintroduced. This again resulted in a marked reduction in symptoms (A-Miso-S of 6), enabling him to resume working in an office setting despite his triggers. Symptom improvement remained stable over several months. This case raises the possibility of the steroid prednisone as a novel treatment for misophonia and misokinesia. However, further investigation is needed to determine the generalizability of this observation.

**Решение:** -2 клинический случай / серия случаев

---

### 500 · R0967

**["Ear rage": misophonia : Review and current state of knowledge].**

2022 · HNO · article, journal article, review · ger · https://doi.org/10.1007/s00106-021-01072-7

Die Misophonie ist eine Intoleranz auf bestimmte Alltagsgeräusche. Hierbei fungieren als „Trigger“ „menschliche Körpergeräusche“, z. B. Schlucken/Schmatzen/Atemgeräusche oder Geräusche, die von Menschen, aber nicht vom menschlichen Körper erzeugt werden (z. B. Klicken Kugelschreiberknopf ), ferner Tier-/Maschinengeräusche. Die Betroffenen verspüren sofort eine negativemotionale Reaktion wie Wut, Aggression, Ekel u.a. Objektivierbare Veränderungen sind Herzfrequenzerhöhung und Blutdruckveränderungen. Die emotionale Reaktion ist individuell und hängt z. B. von Geräuschart, persönlicher Vorerfahrung, sozialem Kontext oder psychologischem Profil ab. Die Misophonie ist bisher als Krankheit nicht definiert und keinem offiziellen Diagnosesystem zugeordnet, sie scheint eine eigenständige Störung zu sein: Assoziationen bestehen u. a. mit Aufmerksamkeits-/Zwangsstörungen, Tinnitus, Hyperakusis, Autismus- Spektrum-Krankheiten. Definitionskriterien wurden 2013 veröffentlicht; verschiedene, validierte Fragebögen wurden bisher zur Misophonieausprägung entwickelt. Studien mit funktionellenMRT-Untersuchungen des Kopfes zeigten eine übermäßige Aktivierung des anterioren Inselkortex (AIC) und seiner benachbarten Regionen, die für Emotionsverarbeitung/- regulation verantwortlich sind. Bisher gibt es keine randomisierten kontrollierten Studien zur Therapie. Einzelne Publikationen beschreiben kognitive Verhaltensinterventionen, Retrainingtherapien und Schallmaskierungssysteme. Zur Triggerreduktion werden Ohrstöpsel/Musikkopfhörer verwendet. Auch HNO-Ärzte können mit Misophoniepatienten konfrontiert werden, z. B. zur Klärung des Hörvermögens oder Beratung von Therapiemöglichkeiten. Der Bericht stellt eine Übersicht des aktuellen Wissensstands zur Misophonie sowie ihrer Diagnostik und Therapie dar.Projekt DEAL 202

**Решение:** -1 обзор литературы / концептуальная статья

---

### 501 · R0060

**Misophonie : quand les sons du quotidien deviennent insupportables**

2026 · The Conversation · other · https://doi.org/10.64628/aak.wkdxmnnst

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 научно-популярная статья (The Conversation)

---

### 502 · R0818

**Childhood exposure to parental threatening behaviors and anxiety in emerging adulthood: Indirect effects of perceived stress.**

2023 · Journal of clinical psychology · journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1002/jclp.23516

Although childhood exposure to parental threatening behaviors is associated with elevated anxiety in emerging adulthood, the underlying mechanisms remain unexplored. Perceived stress-a subjective experience comprised of feelings of helplessness (being unable to cope or exert control) and poor self-efficacy (confidence in one's ability to manage stressors)-is one candidate mechanism. The present investigation examined the underlying role of perceived stress in the association between childhood exposure to parental threatening behaviors and anxiety symptom severity in a sample of emerging adults. Participants (N = 855; Mage = 18.75 years, SD = 1.05, range 18-24; 70.8% female) were recruited from a large state university and administered a battery of self-report questionnaires assessing constructs of interest. Structural equation modeling (SEM) analyses indicated that only greater childhood exposure to maternal threatening behaviors was directly associated with greater feelings of helplessness and lower self-efficacy. Furthermore, only childhood exposure to maternal threatening behaviors was indirectly associated with anxiety severity through greater feelings of helplessness and lower self-efficacy. In contrast, childhood exposure to paternal threatening behaviors was neither directly nor indirectly associated with anxiety severity. Limitations include a cross-sectional design, use of self-report measures, and a nonclinical sample. Replicating these findings in a clinical sample and testing the hypothesized model in a longitudinal design is necessary. Findings underscore the need for intervention efforts that screen for and target perceived stress in emerging adults exposed to negative maternal parenting behaviors.

**Решение:** -6 не про мизофонию

---

### 503 · R1374

**Cognitive behavioural therapy in management of hyperacusis: a narrative review and clinical implementation**

2016 · DOAJ (DOAJ: Directory of Open Access Journals) · review · en

Background and Aim: The aim of this article was to critically discuss the clinical application of a cognitive behaviour therapy (CBT) protocol for the treatment of hyperacusis and its asso­ciated distress.\nMethods: Narrative review\nRecent Findings: Reviewing the research lit­erature suggests that hyperacusis, anxiety and safety seeking behaviours may be linked. Therefore, it seems reasonable to suggest that clinical management of hyperacusis should also include addressing co-existing anxiety and avoidance behaviour. Although, there is strong evidence supporting the effectiveness of CBT in treating anxiety, the studies directly assessing the effect of CBT on hyperacusis are limited. In this paper, the clinical implementation of a CBT protocol for hyperacusis rehabilitation is discussed.\nConclusion: Although a causal relationship bet­ween anxiety and hyperacusis is not clear, there is a growing body of evidence suggesting a pos­sible link between them. In the absence of a cure for hyperacusis, treatment of the anxiety component of the condition could be beneficial.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 504 · R0120

**Emotional responses to environmental sounds: associations with self‑reported well‑being in adults reporting minimal hearing difficulties, some hearing difficulties, and hearing aid use**

2026 · International Journal of Audiology · article · en · https://doi.org/10.1080/14992027.2026.2668503

OBJECTIVE: The study investigated the association between emotional responses to environmental sounds and various well-being indicators. DESIGN: Participants rated 120 environmental sounds on valence and arousal and completed questionnaires assessing affect in daily life, emotional communication in hearing, pleasantness of everyday listening, and mental well-being. STUDY SAMPLE: Forty hearing aid (HA) users and 90 individuals with self-reported normal hearing (NH) were recruited. The NH group was divided into two subgroups based on their hearing difficulties score on the Hearing-Related Lifestyle Questionnaire: 36 with no-to-minimal hearing difficulties ("NH no-difficulty" group) and 54 with some hearing difficulties ("NH some-difficulty" group). RESULTS: NH some-difficulty group reported greater challenges in emotional communication, reduced pleasantness of everyday listening, and poorer mental well-being compared to the NH no-difficulty group. HA users showed greater difficulties in emotional communication and lower listening enjoyment than both NH groups. Higher sensitivity to both positive and negative emotional sounds was linked to greater emotional communication difficulties. A more positive perception of typically negative sounds was associated with a more pleasant experience in everyday listening situations and better mental well-being. CONCLUSIONS: Targeting how individuals interpret and manage emotional reactions to sound may help improve well-being outcomes, particularly for individuals with hearing difficulties.

**Решение:** -6 не про мизофонию

---

### 505 · R1267

**Insights from the third international conference on hyperacusis: causes, evaluation, diagnosis, and treatment.**

2018 · Noise & health · article, journal article, journalarticle · eng · https://doi.org/10.4103/nah.nah_2_18

Background: Hyperacusis is intolerance of certain everyday sounds that causes significant distress and impairment in social, occupational, recreational, and other day-to-day activities. Objective: The aim of this report is to summarize the key findings and conclusions from the Third International Conference on Hyperacusis. Topics covered: The main topics discussed comprise (1) diagnosis of hyperacusis and audiological evaluations, (2) neurobiological aspect of hyperacusis, (3) misophonia, (4) hyperacusis in autism spectrum disorder, (5) noise sensitivity, (6) hyperacusis-related distress and comorbid psychiatric illness, and (7) audiologist-delivered cognitive behavioral therapy for hyperacusis. Conclusions: Implications for research and clinical practice are summarised.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 506 · R1255

**Evaluation of selective attention in patients with misophonia.**

2019 · Brazilian journal of otorhinolaryngology · article, comparative study, journal article · eng · https://doi.org/10.1016/j.bjorl.2018.02.005

INTRODUÇÃO: A misofonia é caracterizada pela aversão a sons bem seletivos, que provocam uma forte reação emocional. Foi proposto que a misofonia, assim como o zumbido, esteja associada à hiperconectividade entre os sistemas auditivo e límbico. Indivíduos com zumbido de incômodo significativo podem apresentar comprometimento da atenção seletiva, o que ainda não foi demonstrado no caso da misofonia. OBJETIVO: caracterizar uma amostra de indivíduos com misofonia e compará-la com dois grupos controle, um com zumbido (sem misofonia) e outro assintomático (sem zumbido e sem misofonia). METODOLOGIA: Foram avaliados 40 sujeitos normo-ouvintes, sendo 10 com misofonia (grupo misofonia - GM), 10 com zumbido (sem misofonia) (grupo controle zumbido - GCZ) e 20 sem zumbido e sem misofonia (grupo controle assintomático - GCA). Foi realizada anamnese geral em todos os grupos e anamnese específica apenas para o GM. Nos três grupos, foi aplicado o Teste de Identificação de Sentenças Dicóticas em três situações. Na primeira, foi realizado o exame padrão. Em seguida, foi aplicado incluindo mensagem competitiva, uma com som de mastigação (exame mastigação), e outra com white noise (exame white noise). RESULTADOS: A amostra do GM apontou que os primeiros sintomas da misofonia foram percebidos ainda na infância ou adolescência (média 11,5 anos). O grau de incômodo variou de 6 a 10 na escala visual analógica e, dentre os 10 participantes do GM, nove (90%) responderam que a misofonia atrapalha, sempre ou às vezes, a vida social e profissional. No teste de Identificação de Sentenças Dicóticas, foi observado que no exame mastigação, as médias da porcentagem de acertos diferem entre os grupos GM e GCA (valor-p = 0,027) e entre os grupos GM e GCZ (valor-p = 0,002), sendo menor em ambos os casos no GM. Para os exames padrão e white noise, não há diferença entre as médias da porcentagem de acertos nos três grupos (valores-p >= 0,452). CONCLUSÃO: os participantes do GM apresentaram menor porcentagem de acertos no Teste de Identificação de Sentenças Dicóticas na situação de apresentação de um ruído distraidor (exame mastigação) em relação ao mesmo teste aplicado em situação padrão ou white noise, sugerindo que indivíduos com misofonia podem apresentar alteração da atenção seletiva quando expostos a sons que desencadeiam esta condiçãoINTRODUCTION: Misophonia is characterized by the aversion to very selective sounds, which evoke a strong emotional reaction. It has been proposed that misophonia, as well as tinnitus, is associated with hyperconnectivity between the auditory and limbic systems. Individuals with bothersome tinnitus may have selective attention impairment, but it has not been demonstrated in case of misophonia yet. OBJECTIVE: to characterize a sample of misophonic subjects and compare it to two control groups, one with tinnitus individuals (without misophonia) and the other one with asymptomatic individuals (without misophonia and without tinnitus), regarding self-perception of the condition and selective attention. METHODOLOGY: we had evaluated 40 normal hearing participants: 10 with misophonia (GM), 10 with tinnitus (without misophonia) (GCZ) and 20 without tinnitus and without misophonia (GCA). General questionnare was applied in all of three groups and specific misophonia questionnaire was applied only in GM. In order to evaluate the selective attention, it was applied the Dichotic Sentence Identification (DSI) Test in three situations: In the first one, it was applied the original test. Then, the test was applied in two other situations including two competitive sounds, one with chewing sound (chewing test), and the other one with white noise sound (white noise test). RESULTS: The GM sample indicated that the onset of misophonia occurred in childhood or adolescence (mean 11.5 years). According to the visual analog scale, the discomfort with misophonia ranged from 5 to 10, and nine (90%) participants answered that misophonia always or sometimes limits their social and professional interactions. In the chewing test, it was observed that the average of correct responses differed between GM and GCA groups (pvalue = 0.027) and between GM and GCZ groups (p-value = 0.002), in both cases it was lower in GM. In the original and white noise tests, no difference was observed between the averages of correct responses in the three groups (p-values >= 0.452). CONCLUSION: The GM participants had a lower percentage of correct responses in the chewing test, suggesting that individuals with misophonia may have selective attention impairment when they are exposed to sounds that trigger the conditio

**Решение:** ? избирательное внимание (10 с мизофонией vs контроль), проверить скрининг пула

---

### 507 · R1266

**The mixed-methods case study of "Zara"**

2018 · No Publisher Supplied · other literature type, text/, article · en · https://doi.org/10.7282/t33j3hkh

This single-subject, mixed-method, behavioral analytic case-study dissertation presents a systematic, 12-session cognitive behavior therapy (CBT) treatment of “Zara,” an undergraduate student with severe misophonia. Misophonia is a rare condition characterized by an aversive response of sympathetic nervous system (SNS) activation and negative emotions (e.g. anger, disgust, and/or anxiety) elicited by the presence of specific and commonly encountered sounds (e.g. lip-smacking, chewing). Distress caused by trigger sounds and efforts to avoid and escape from these sounds often result in impairment in functioning. The goals of this case study are to (1) detail the assessment process used; (2) document and analyze the successful implementation of the CBT intervention; and (3) evaluate hypotheses regarding the mechanisms of change. The intervention utilized an A-B research design with a six-month follow-up. The independent variable consisted of a multi-component treatment that included skills training in cognitive restructuring, mindfulness and exposure procedures. The treatment was designed to reinforce adaptive and appropriate coping responses and extinguish the aversive respondent conditioned responses and the negatively reinforced inappropriate coping responses. The dependent variables included both behavioral outcomes (e.g. inappropriate coping behaviors, avoidance, and social interference) and subjective report outcomes (e.g. sensitivity to sounds, distress, and reported SNS response). The Amsterdam Misophonia Scale and the Misophonia Questionnaire were collected to evaluate changes in misophonia symptoms. At the end of treatment, the intervention was associated with a substantial improvement in all dependent variable measures. The largest reduction in symptoms occurred following session five, the first session with prolonged exposure exercises. At the six-month follow-up, which was completed by an independent evaluator, Zara reported an increase in her subjective “sensitivity” to trigger sounds; however, she remained at post-treatment levels in terms of her subjective SNS distress, use of inappropriate coping behaviors, avoidance, social interference, and overall misophonia symptoms. These findings support the role of two mechanisms of change as being responsible for Zara’s long-term relief: (a) skills training in cognitive restructuring; and (b) the expectancy violation and behavioral experimentation components of exposure therapy. The case concludes with a discussion of the intervention’s limitation and recommendations for future research.Psy.D.Includes bibliographical referencesby David A. Singe

**Решение:** -2 клинический случай / серия случаев

---

### 508 · R0981

**Composing ‘Weird' Music**

2022 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9781003183624-27

Anya Ustaszewski discusses how hyperacusis and misophonia have affected both her day-to-day experiences of the world and her music-making. The diagnosis of autism and Attention Deficit Hyperactivity Disorder led to differences in hearing and fixations on certain sounds resulting in the composition of ‘weird’ music. The chapter celebrates hearing difference and argues for greater acceptance of aural diversity in society.

**Решение:** -1 глава книги / справочник

---

### 509 · R1075

**O dilema da prometeutica cardíaca**

2021 · Revista Brasileira de Fisiologia do Exercício · article, other literature type · pt · https://doi.org/10.33233/rbfex.v20i1.4597

Como Prometeu sou castigado por levar a chama aos humanos (1). Paradoxo que em mim carrego desde o meu despertar. Entrelaço de mito e realidade de quem emana o bem e o mal, de quem decide entre a vida e a morte. Hoje vivo esse paradoxo de forma mais intensa, pois palpito como um contador regressivo que insiste em prorrogar. O som dos instrumentos que me cercam já soa familiar e reconheço as notas agudas e prolongadas que precedem uma agitação nos corredores. Ciclo de misofonia que se tornou constante neste último mês...

**Решение:** -1 обзор литературы / концептуальная статья

---

### 510 · R0948

**Acceptance and Commitment Therapy for a Child With Misophonia: A Case Study**

2022 · Clinical Case Studies · article, journalarticle, google scholar result · en · https://doi.org/10.1177/15346501221126136

Misophonia, a condition involving hypersensitivity, anger, and/or disgust in response to specific noises (e.g., chewing, tapping), is highly underresearched in children. Several case studies point towards the utility of cognitive behavioral therapy and related treatments (e.g., acceptance and commitment therapy [ACT]). ACT presents a particularly promising option, as it focuses on building psychological flexibility in response to difficult internal experiences, rather than trying to remove or change them (e.g., responding effectively to irritation provoked by chewing). The present case study describes “Kelly” (pseudonym), a 12-year-old girl with moderately severe misophonia symptoms, who received a 16-session course of ACT for misophonia. At post-treatment, Kelly reported a decline to the mild range of misophonia, as well as re-engagement in activities that were important to her and clinically significant reductions in depressive symptoms. These results suggest that ACT may be an appropriate treatment for children with misophonia; however, much more research is warranted.

**Решение:** -2 клинический случай / серия случаев

---

### 511 · R1415

**[Misophonia or aversion to human sound: a clinical illustration].**

2015 · Revue medicale suisse · article, case reports, english abstract · fre · https://pubmed.ncbi.nlm.nih.gov/25915989/

Misophonia, meaning hatred of sound, is a cluster of symptoms which is not completely included in anxiety disorders category as obsessive compulsive or as an impulsivity disorder. It is described as a chronic condition characterized by reactions, aversion to specific sounds that result in subsequent emotional. Indeed, this condition is relatively unknown and few psychiatrists have already faced this disorder causing in some individuals severe impairment. The investigation of a patient suffering of misophonia with severe impairment that we took into care in an outpatient psychiatric clinic in Geneva contributes to a better understanding of this condition and indicates potential factors that may co-occur and influence the clinical presentation. The good response in psychotherapy, has led us to carry out a brief review of the literature in order to better define and identify this disorder.

**Решение:** -2 клинический случай / серия случаев

---

### 512 · R1111

**Current and Lifetime Somatic Symptom Burden Among Transition-aged Autistic Young Adults**

2021 · Autism Research · article · und · https://doi.org/10.1002/aur.2671

Abstract Background and Objectives Somatic symptoms are the most common cause of outpatient medical visits in the general population, yet their presence and severity in individuals on the autism spectrum has rarely been studied. We sought to assess the prevalence, impact, and clinical correlates of fourteen commonly-reported somatic symptoms in a sample of transition-aged autistic young adults. Methods A sample of 290 independent and cognitively able autistic young adults (aged 18–26 years; mean [ SD ]: 23.10 [2.38] years) was recruited from the Simons Foundation SPARK participant pool. A modified version of the Patient Health Questionnaire–15 was used to assess somatic symptom prevalence/impact, along with measures of depression, anxiety, autistic traits, and quality of life. Results Somatic symptom burden was much higher in autistic young adults than previously reported in the general population. The most commonly reported current symptoms were fatigue (72.8%), sleep problems (69.0%), and menstrual problems (61.4% of females). Moderate or severe symptom levels were reported by 53.9% of females and 18.75% of males in our cohort, with the odds of females of endorsing any given symptom being 2–4 times greater than males. Both individual symptoms and total symptom burden were related to higher levels of depression, anxiety, and autistic traits, along with lower quality of life. Conclusion Despite little research on this topic previously, somatic symptoms are highly prevalent in autistic young adults, particularly women. Future research is needed to investigate links between somatic symptoms, medical and psychiatric morbidity, and health care utilization in the autistic population. What’s Known on This Subject Somatic symptoms are highly prevalent in the general population and account for a large proportion of health care costs. However, few studies have investigated the prevalence, impact, or correlates of these symptoms in individuals on the autism spectrum. What This Study Adds To our knowledge, this is the first study to specifically assess current and lifetime somatic symptom burden, symptom onset patterns, and the clinical correlates of multisystem symptom distress in transition-aged young adults on the autism spectrum.

**Решение:** -6 не про мизофонию

---

### 513 · R1385

**Misophonia and phonophobia**

2016 · Tinnitus Clin Res Perspect · google scholar result · https://books.google.com/books?hl=en&lr=&id=xH9FDAAAQBAJ&oi=fnd&pg=PA245&dq=misophonia+prevalence&ots=wSkCyWTQVY&sig=c8KECElR_r8n1Ve81Wnmy2yMIF8

… There are no robust figures defining the prevalence, incidence, or natural history of misophonia in the general population. Studies examining the prevalence of all forms of decreased …

**Решение:** -1 обзор литературы / концептуальная статья

---

### 514 · R0579

**Clinical characteristics of treatment-seeking youth with misophonia.**

2024 · Journal of clinical psychology · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1002/jclp.23672

Abstract Objective Misophonia is a psychiatric condition characterized by strong emotional and/or behavioral responses to auditory stimuli, leading to distress and functional impairment. Despite previous attempts to define and categorize this condition, misophonia is not currently included in the Diagnostic and Statistical Manual of Mental Disorders or International Classification of Diseases. The lack of formal diagnostic consensus presents challenges for research aimed at assessing and treating this clinical presentation. Methods The current study presents clinical characteristics of youth ( N = 47) with misophonia in the largest treatment‐seeking sample to date. We examined demographic characteristics of the sample, frequency of comorbid disorders, frequency of specific misophonia symptoms (i.e., triggers, emotional and behavioral responses, and impairments), and caregiver‐child symptom agreement. Misophonia symptoms were evaluated using a multimodal assessment including clinician, youth, and caregiver reports on empirically established misophonia measures, and concordance among measures was assessed. Results Youth seeking treatment for misophonia presented with marked misophonia symptoms and an array of comorbid conditions. Youth and caregivers identified various triggers of misophonia symptoms (e.g., chewing sounds, breathing sounds), as well as a wide range of emotional (e.g., anger, annoyance, disgust) and behavioral (e.g., aggression, avoidance) responses to triggers. Youth and caregivers exhibited high agreement on misophonia triggers but lower agreement on symptom severity and associated impairment. Compared to younger children (aged 8−13), older children (aged 14+) appeared to report symptom severity and associated impairment more reliably. Conclusion Misophonia is a heterogenous and impairing clinical condition that warrants future investigation and evidence‐based treatment development.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 515 · R1357

**A ansiedade dos pacientes que sofrem de claustrofobia e misofonia na realização de exames de ressonância magnética**

2017 · article · pt

O exame de RM e um dos mais importantes metodos de diagnosticos por imagem existente na atualidade. Considerando que e um metodo diagnostico de fantastico, mesmo assim as pessoas que realizam esse exame podem apresentar resistencia ao procedimento devido a Claustrofobia e a Misofonia. A claustrofobia e um quadro em que a pessoa apresenta mal estar em lugares apertados e Misofonia e a agitacao/irritacao constante na presenca de um determinado som. Assim, e comum que esses pacientes passem mal quando realizam o exame de RM em aparelhos de tunel fechado, devido o barulho intenso e a sensacao de sufocamento. Este estudo abordou os diferentes tipos de equipamentos de RM, Bobinas e metodos, como tambem classificou a fobia, suas caracteristicas e sintomas relacionando em especial a Claustrofobia e a misofonia. Assim, o objetivo geral e analisar a forma adequada de abordagem aos pacientes com pânico as caracteristicas dos aparelhos de Ressonância Magnetica de tunel fechado na execucao de certos exames; e os objetivos especificos foram de Relatar a importância do exame de Ressonância magnetica e sua contribuicao para os avancos na medicina, Caracterizar os equipamentos de RM, em especial o de tunel fechado, Apontar as possiveis reacoes emocionais apresentada pelos pacientes durante o pre exame e o exame, Descrever o procedimento que deve ser adotado em casos de reacoes emocionais apresentadas pelos pacientes durante o pre e o exame de RM, sendo alcancados atraves de uma revisao bibliografica baseada em trabalhos de natureza semelhante. Concluiu-se que a opcao de fazer o exame de RM num equipamento de campo aberto e uma fator imprescindivel, pois foi constatado que 82,3% admitem que a configuracao do equipamento RM e a principal dificuldade encontrada ao realizar este exame, acompanhado pela imobilidade corporal com 62,9%, e como terceiro ponto esta o ruido com 14,5%, com isso foi confeccionado um quadro de procedimentos para facilitar a realizacao dos exames.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 516 · R1319

**Intolerance to environmental chemicals and sounds in irritable bowel syndrome: Explained by central sensitization?**

2018 · Journal of health psychology · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1177/1359105316656242

This study tested the hypotheses of irritable bowel syndrome showing (1) comorbidity with chemical and sound intolerance, other types of functionally somatic syndromes, and psychiatric disorders and (2) stronger than normal affective reactions to and behavioral disruptions from odorous/pungent chemicals and sounds in daily life. These hypotheses were tested by means of data from a large-scale population-based questionnaire study. The results showed comorbidity in irritable bowel syndrome with chemical and sound intolerance, fibromyalgia, migraine, post-traumatic stress disorder, generalized anxiety disorder, panic syndrome, and depression as well as strong reactions/disruptions from odorous/pungent chemicals and sounds in irritable bowel syndrome.</p

**Решение:** -6 не про мизофонию

---

### 517 · R0425

**Unraveling the pivotal role of autistic traits in misophonia: A preliminary investigation of the interrelationship between misophonia and sensory sensitivity**

2025 · Journal of Clinical Psychiatry · article, journalarticle, google scholar result · en · https://doi.org/10.5505/kpd.2025.79907

Objective: A burgeoning body of evidence suggests a higher prevalence of autistic traits among individuals with misophonia.This study aimed to examine the comorbid psychiatric diagnoses and autistic traits along with associations between sensory profiles and internalizing symptoms in a clinical sample of adolescents with misophonia, while also comparing them to a control group.Method: Female adolescents with misophonia (n = 22) and controls (n = 22) aged 14-18 years participated in this study.Psychiatric evaluations were conducted with semi-structured interviews.The diagnosis of misophonia was established both clinically and through the use of the Amsterdam Misophonia Scale Revised.Autistic traits were assessed by the Youth Self Report.The Revised Children's Anxiety and Depression Scale-Child Version and the Adolescent/Adult Sensory Profile were administered.Results: The misophonia group exhibited a high prevalence of psychiatric diagnoses, particularly obsessive-compulsive disorder (OCD) and anxiety disorders.Adolescents with misophonia had a significantly higher level of internalizing symptoms, autistic traits, and sensory sensitivities (p<0.001,r=0.58; p<0.01, d=1.02; and p<0.001, r=0.58, respectively).Autistic traits had a mediating role in the relationship between misophonia and sensory sensitivity.Discussion: These findings suggest that evaluating autistic traits may offer valuable insights into understanding and managing misophonia in female adolescents, opening up avenues for the development of targeted interventions aimed at mitigating the impact of misophonia-related sensory sensitivity outcomes.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 518 · R1437

**Self-Assessment Questions**

2014 · Seminars in Hearing · article · en · https://doi.org/10.1055/s-0034-1373742

This section provides a review. Mark each statement on the Answer Sheet according to the factual materials contained in this issue and the opinions of the authors. Article One (pp. 65–73) Which of the following best approximates prevalence of tinnitus in the general population? 15% 30% 40% 0.5% 10 to 17 million in the United States Which of the following is not a common comorbid condition in tinnitus? Insomnia Anxiety Depression Attention deficit hyperactivity disorder Cognitive dysfunction Which of the following is not likely involved in the pathophysiology of tinnitus? Decreased inhibition along the auditory pathway Increased spontaneous activity along the auditory pathway Enhanced lateral inhibition (correct answer) Neuroplasticity Enhanced rhythmic activity All of the following are legitimate means that may be used in tinnitus management except masking tinnitus retraining therapy cognitive behavioral therapy anxiolytics labyrinthectomy Which of the following is likely not among areas of current tinnitus research? Improving tinnitus evaluation tools Identifying medications effective in treating tinnitus Developing electromagnetic stimulation protocols for tinnitus treatment Cochlear transplant for tinnitus (correct answer) Increasing knowledge on brain activities correlated to tinnitus Article Two (pp. 74–83) Hyperacusis refers to extraordinarily good hearing like Superman reduced tolerance to environmental sound a cochlear hearing loss recruitment hearing your own voice too loudly The prevalence of hyperacusis in adults is 90% 70% 50% 30% less than 10% In a patient with hyperacusis, loudness tolerance testing is indicated never always only in children in some patients, but caution is advised in patients with acoustic shock The physiological mechanism suspected as underpinning hyperacusis is increased central auditory gain cochlear dead regions ossicular chain abnormalities vestibular dysfunction auditory neuropathy The first mention of hyperacusis in the clinical literature was in 1971 1881 2002 1906 1984 Article Three (pp. 84–91) Which of the following is/are questionnaire(s) available to use with misophonia patients? Misophonia and Tinnitus Assessment (MTA) Amsterdam Misophonia Scale (A-MISO-S) Misophonia Reaction Questionnaire (MRQ) Sound Sensitivity Index (SSI) All of the above Which of the following trigger sounds listed in this article are associated with misophonia? The dog's nails on the floor Other's chewing Other's lip smacking Other's yawning All of the above Based on this article, which of the following describes misophonia? An abnormally strong reaction to certain sounds Hearing one's own voice louder than normal Sensitivity to loud sounds associated with hearing loss A hatred of musical sounds None of the above According to Schröder, the misophonia trigger sounds are primarily auditory and then may be associated with which other sensory modality(ies)? Visual Tactile Olfactory Tactile and visual None of the above Based on this article, misophonia research has concluded that imaging studies suggest the auditory cortex is responsible for the initiation of the misophonia trigger sounds that misophonia is associated with tinnitus and hearing loss as reported by subjective questionnaires that misophonia initiates with the patients noting bothersome reactions from their own voice and progresses to include reactions to family members' vocal sounds, as reported by subjective questionnaires and history forms that misophonia has been associated with bipolar disorder none of the above Article Four (pp. 92–104) The tinnitus intervention with the strongest evidence base for clinical use employs repetitive transcranial magnetic stimulation cognitive-behavioral therapy tinnitus retraining therapy ginkgo biloba zinc For a patient who is not a cochlear implant candidate, surgery for subjective tinnitus is indicated in a few specific situations, and should be used primarily to improve hearing insert an electrode into the brainstem section the VIIIth nerve both A and C both B and C Which of the following should be considered a tinnitus treatment? Hearing aids Cognitive-behavioral therapy Intradural electrode implant Tinnitus retraining therapy Mindfulness meditation Which strategy was used by Norena and Eggermont when they demonstrated cortical reorganization may be minimized following damaging exposures to noise employed? Neuromodulation Repetitive transcranial magnetic stimulation Enriched acoustic environment Deep-brain implant Cochlear implant Searchfield described hearing aid programming that improved outcomes among patients with tinnitus; which of the following characteristics should not be included in a “tinnitus setting”? Omnidirectional microphone High outputs to facilitate masking Open fit whenever possible Noise suppression disengaged High compression ratios for inputs above 60-dB SPL Article Five (pp. 105–120) In cases of hyperacusis, sensitivity to sound is determined by the physical characteristics of sound patients always have normal hearing patients should protect their ears with both earplugs and earmuffs patients are very afraid of sounds patients are typically oversensitive to specific sounds only Loudness discomfort levels in tinnitus retraining therapy should not be measured in patients with decreased sound tolerance generally exceed 120-dB hearing level are a direct measure of loudness recruitment should be measured only in patients reporting hyperacusis none of the above Hyperacusis is only present when a person is exposed to very loud sounds an abnormal emotional reaction to sound, typically involving fear closely associated with recruitment a condition that occurs only in patients with normal hearing none of the above Treatment for misophonia always involves the use of ear-level instruments should be performed by the use of sound only can be effectively treated by counseling and specific protocols of sound usage requires the use of pink noise cannot be performed for patients who also have hyperacusis Misophonia is a psychiatric problem and as such should be treated exclusively by psychiatrists a condition that always creates a strong uncontrollable reaction in patients a condition that occurs only to soft sounds a condition that occurs only to patterns of sound that are specific for a given patient observed when physical features of sound determine the reactions to a sound Article six (pp. 121–130) Misophonia is a reaction to specific sounds usually visual response a reaction to the loudness of the sound sensitivity to the sounds of ambulances, blenders, and so on responsive to aversive techniques in therapy The severity of tinnitus is related to the loudness of tinnitus the duration tinnitus has been present the frequency of the tinnitus level of disturbance of the tinnitus A and C only Hyperacusis is best treated with suitable noise-reducing earplugs reimaging, reimagining, refocusing ear-level sound generators isolation from competitive sounds A and B Hyperacusis, misophonia, and tinnitus are all caused by damage to the cochlea heightened reaction of the limbic system reduced reaction of the autonomic nervous system all of the above none of the above Tinnitus retraining therapy incorporates collaborative counseling directive counseling patient centered counseling mindfulness-based counseling cognitive behavioral therapy Article Seven (pp. 131–144) Which of the following affirmations is correct? Electroencephalography and magnetoencephalography provide high temporal resolution. Functional magnetic resonance imaging and positron emission tomography provide high temporal resolution. Electroencephalography and magnetoencephalography provide poor spatial resolution. Functional magnetic resonance imaging provides poor spatial resolution. Both A and C are true. Regarding the brain resting-state activity, which of the following statements is true? The resting state is the least metabolically demanding component of neural activity. Resting-state studies focused on the observation of modification of brain activity in response to a task or stimuli. Resting-state brain networks look like networks activated during tasks. Resting-state paradigms are difficult to apply in clinical setting. Resting-state paradigms have never been applied to the study of tinnitus. According to neuroimaging findings, which of the following statements is true? Changes of brain activity in auditory cortices accompany tinnitus. Tinnitus is associated to modification of brain activity in nonauditory brain areas. Alteration of functional interactions between key neural circuits of the brain seems to be crucial for the emergence of tinnitus. None of the above is true. All of the above are true. When doing tinnitus studies, one has to carefully control for hearing loss hyperacusis age anxiety/depression all of the above Which of the following affirmations is correct? Tinnitus affects brain activity only in auditory regions. Tinnitus is easily treated. Tinnitus characteristics cannot be correlated to the activity of particular brain regions. Tinnitus neuroimaging findings have helped to design tinnitus theoretical models. Tinnitus studies have always had proper control groups as well as good control of confounding factors. Article Eight (pp. 145–156) The air—bone gap in patients with superior semicircular canal dehiscence is due to improved bone-conduction transmission dissipation of air-conducted sound through the dehiscence fixation of the ossicular chain a hole in the tympanic membrane A and B The audiometric configuration in superior semicircular canal dehiscence is most similar to test results found in patients with otosclerosis Meniere disease ototoxicity presbycusis cholesteatoma Vestibular evoked myogenic potential responses in patients with superior semicircular canal dehiscence are typically absent prolonged difficult to interpret due to excessive noise present with reduced thresholds present with elevated thresholds A positive malleolus sign means a tuning fork placed on the forehead localized to the dehiscent ear the patient was able to hear a 128-or 256-Hz tuning fork placed on his or her ankle the patient became symptomatic when exposed to high-intensity sound the patient became symptomatic when pressure was presented in the external auditory canal C and D Diagnosis of superior semicircular canal dehiscence is based on computed tomography findings vestibular evoked myogenic potential thresholds audiometric findings case history all of the above

**Решение:** -7 ceu / self-assessment questions

---

### 519 · R1306

**Hipersensibilidade e Intolerância aos Sons**

2018 · Canal Saúde Fiocruz

dubladoA hipersensibilidade e a intolerância aos sons são problemas reais para muita gente e que ainda são pouco conhecidos pela maioria. Existe a misofonia, que torna barulhos comuns, como o tique taque de um relógio, insuportáveis para quem sofre do transtorno; e a hiperacusia, que faz os sons parecerem mais altos para quem sofre dela. O programa vai explicar cada um desses transtornos e abordar os tratamentos. Para saber mais sobre o assunto, a apresentadora Marcela Morato conversa com a otorrinolaringologista Patrícia Ciminelli do Hospital Federal da Lagoa do Ministério da Saúde. Participantes: Patrícia Coutinho, 35 anos; Patrick Coutinho Ferraz, 10 anos, filho da Patrícia; Sheila de Fátima Coutinho, mãe da Patrícia

**Решение:** -1 обзор литературы / концептуальная статья

---

### 520 · R0353

**Tourette Syndrome.**

2025 · The Psychiatric clinics of North America · editorial · eng · https://doi.org/10.1016/j.psc.2024.08.001

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 521 · R0053

**Cognitive-Behavioural Therapy applied to Misophonia, a scoping review.**

2026 · Hearing research · article, journal article, scoping review · eng · https://doi.org/10.1016/j.heares.2026.109661

Misophonia is characterized by negative emotional, cognitive, and sometimes physical reactions to specific sounds, with impact that depends on context and meaning. Cognitive- behavioural therapy (CBT) is the most commonly described psychological approach for misophonia, but implementations vary and the clinical literature is heterogeneous. We conducted a focused scoping review of CBT applications to misophonia in clinical settings. Searches of PubMed, PsycINFO, and Google Scholar (2013-2025) identified 30 publications that delivered CBT-family procedures with pre- to post-treatment measurement. Fourteen reports that introduced novel protocols or provided the greatest procedural detail were synthesized in depth; the remainder were summarized. We extracted setting, format, session dose, main procedures, trigger selection and progression, homework structure, outcome measures, and follow-up where available. Across single-case exposure and response-prevention applications, counterconditioning programs, inhibitory-learning-informed procedures, standardized group packages, service-based CBT repertoires, and early adaptations of a transdiagnostic protocol, CBT-family interventions were generally feasible to deliver and often associated with reductions on misophonia-specific measures. However, designs were mostly uncontrolled and samples small. Interpretation is constrained by heterogeneous designs, inconsistent reporting of procedures, and variability in measurement (e.g., MQ, A-MISO-S/AMISOS-R, MAQ, S-Five, DMQ). We did not pool effects. The available evidence supports CBT-family procedures as deliverable and potentially helpful for misophonia, while falling short of firm efficacy claims. Future studies should adopt core outcome batteries, specify procedures at a granular level, and test whether particular ingredients (e.g., graded exposure with response prevention, counterconditioning, expectancy-violation strategies, attentional training, cognitive restructuring formats) contribute uniquely, or in combination, to clinically meaningful change.

**Решение:** -1 обзор / комментарий / письмо

---

### 522 · R1021

**Treating Adolescent Misophonia With Cognitive Behavioral Therapy: Considerations for Including Exposure**

2021 · Clinical Case Studies · article, journalarticle, google scholar result · en · https://doi.org/10.1177/15346501211045707

Although misophonia is not yet included in the primary diagnostic manuals used by psychologists or psychiatrists, proposed criteria suggest that this condition is characterized by a strong negative reaction to and avoidance of certain trigger sounds. Misophonic trigger sounds are largely human-made (e.g., chewing and slurping) and evoke responses such as disgust, irritation, and/or anger that are out of proportion to the situation and cause distress and/or impairment. Currently, there is no gold standard evidence-based treatment for misophonia. As the misophonia treatment literature grows, several important questions are arising: (1) should exposure to aversive sound triggers be included in treatment for misophonia and (2) how can clinicians best assess misophonia symptoms. This case offers one example of misophonia being successfully treated with a cognitive-behavioral approach to treatment (including exposures) in an adolescent girl. This case also offers an example of how clinicians may conduct a comprehensive assessment of misophonia symptoms. Theoretically and empirically derived recommendations for including exposure in misophonia treatment are presented. Information from this case may be helpful in informing future research, as there is a paucity of evidence-based assessment and treatment protocols for misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 523 · R1115

**Prevalence of Decreased Sound Tolerance (Hyperacusis) in Individuals With Autism Spectrum Disorder: A Meta-Analysis.**

2021 · Ear and hearing · article, journal article, meta-analysis · eng · https://doi.org/10.1097/aud.0000000000001005

Supplemental Digital Content is available in the text. Objectives: Hyperacusis, defined as decreased tolerance to sound at levels that would not trouble most individuals, is frequently observed in individuals with autism spectrum disorder (ASD). Despite the functional impairment attributable to hyperacusis, little is known about its prevalence or natural history in the ASD population. The objective of this study was to conduct a systematic review and meta-analysis estimating the current and lifetime prevalence of hyperacusis in children, adolescents, and adults with ASD. By precisely estimating the burden of hyperacusis in the ASD population, the present study aims to enhance recognition of this particular symptom of ASD and highlight the need for additional research into the causes, prevention, and treatment of hyperacusis in persons on the spectrum. Design: We searched PubMed and ProQuest to identify peer-reviewed articles published in English after January 1993. We additionally performed targeted searches of Google Scholar and the gray literature, including studies published through May 2020. Eligible studies included at least 20 individuals with diagnosed ASD of any age and reported data from which the proportion of ASD individuals with current and/or lifetime hyperacusis could be derived. To account for multiple prevalence estimates derived from the same samples, we utilized three-level Bayesian random-effects meta-analyses to estimate the current and lifetime prevalence of hyperacusis. Bayesian meta-regression was used to assess potential moderators of current hyperacusis prevalence. To reduce heterogeneity due to varying definitions of hyperacusis, we performed a sensitivity analysis on the subset of studies that ascertained hyperacusis status using the Autism Diagnostic Interview-Revised (ADI-R), a structured parent interview. Results: A total of 7783 nonduplicate articles were screened, of which 67 were included in the review and synthesis. Hyperacusis status was ascertained in multiple ways across studies, with 60 articles employing interviews or questionnaires and seven using behavioral observations or objective measures. The mean (range) age of samples in the included studies was 7.88 years (1.00 to 34.89 years). The meta-analysis of interview/questionnaire measures (k(3) = 103, nASD = 13,093) estimated the current and lifetime prevalence of hyperacusis in ASD to be 41.42% (95% CrI, 37.23 to 45.84%) and 60.58% (50.37 to 69.76%), respectively. A sensitivity analysis restricted to prevalence estimates derived from the ADI-R (k(3) = 25, nASD = 5028) produced similar values. The estimate of current hyperacusis prevalence using objective/observational measures (k(3) = 8, nASD = 488) was 27.30% (14.92 to 46.31%). Heterogeneity in the full sample of interview/questionnaire measures was substantial but not significantly explained by any tested moderator. However, prevalence increased sharply with increasing age in studies using the ADI-R (BF10 = 93.10, R2Het = 0.692). Conclusions: In this meta-analysis, we found a high prevalence of current and lifetime hyperacusis in individuals with ASD, with a majority of individuals on the autism spectrum experiencing hyperacusis at some point in their lives. The high prevalence of hyperacusis in individuals with ASD across the lifespan highlights the need for further research on sound tolerance in this population and the development of services and/or interventions to reduce the burden of this common symptom.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 524 · R0051

**Les Sens Oubliés de la médecine**

2026 · book · fra/fre · https://hal.science/hal-05671219v1

Cet ouvrage interroge un angle mort de la formation médicale francophone contemporaine : la faible intégration, dans les cursus et dans la pratique clinique courante, des modalités sensorielles dites « oubliées » — intéroception, proprioception, système vestibulaire, chronoception, thermoception, nociception, prurit, tact C-affectif. Alors que la sémiologie classique reste organisée autour des cinq sens aristotéliciens, plus d'un siècle de neurosciences, depuis les travaux fondateurs de Sherrington jusqu'aux avancées contemporaines sur le cerveau prédictif, a profondément renouvelé la cartographie sensorielle humaine. L'ouvrage défend la thèse selon laquelle cette désynchronisation entre savoirs neurobiologiques et formation médicale contribue à une errance diagnostique substantielle pour plusieurs entités cliniques en expansion : vertige perceptuel postural persistant (PPPD), syndrome d'Ehlers-Danlos hypermobile (SEDh), misophonie, autisme adulte récemment reconnu, troubles des conduites alimentaires (TCA) et dépressions à composante chronoceptive. La position défendue est délibérément modérée. Il ne s'agit pas de disqualifier la psychiatrie ou la médecine fonctionnelle, dont la légitimité demeure entière, mais de plaider pour un dialogue renforcé avec une sémiologie sensorielle étendue, capable d'identifier en amont des dysfonctionnements perceptifs aujourd'hui interprétés comme purement psychogènes ou idiopathiques. Le livre se déploie en seize chapitres répartis en cinq parties. La première partie (chapitres 1-3) reconstitue l'état de l'art historique et épistémologique. La deuxième partie (chapitres 4-6) déploie la sémiologie sensorielle étendue. La troisième partie (chapitres 7-12) propose six études de cas cliniques contemporaines (PPPD, SEDh, misophonie, autisme, TCA, dépression chronoceptive). La quatrième partie (chapitres 13-14) audite les programmes francophones de formation médicale. La cinquième partie (chapitres 15-16) explore les implications cliniques, pédagogiques et prospectives. L'ouvrage valorise particulièrement la tradition scientifique francophone : Alain Berthoz, Jean Massion, Michel Lacour, Jean-Pierre Roll, Catherine Tallon-Baudry, Laurent Mottron, Claude Hamonet, Philip Gorwood, Sylvie Droit-Volet. Ces apports francophones sont mis en dialogue avec la littérature anglophone dominante (Craig, Damasio, Critchley, Seth). L'ouvrage s'achève sur une orientation prospective ouverte vers magnétoréception humaine, sensorialité spatiale chez les astronautes, sensorialités animales et biomimétisme.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 525 · R0539

**Misofonía.**

2024 · https://core.ac.uk/download/672975245.pdf

Este trabajo de grado es una colección de cuentos que aborda la precarización, la marginalidad y las tensiones internas de personajes masculinos que habitan en espacios urbanos violentos y opresivos

**Решение:** -7 dataset / audio repository

---

### 526 · R0780

**[Misophonia in Childhood and Adolescence: A Narrative Review].**

2023 · Zeitschrift fur Kinder- und Jugendpsychiatrie und Psychotherapie · article, english abstract, journal article · ger · https://doi.org/10.1024/1422-4917/a000885

Zusammenfassung. Die Misophonie beschreibt ein Phänomen, bei welchem betroffene Kinder und Jugendliche eine starke negative physiologische und emotionale Reaktion bei Konfrontation mit speziellen auditiven (misophonischen) Reizen zeigen (am häufigsten Ess- oder Atemgeräusche). Einzelne Studien mit Erwachsenen liefern bereits Prävalenzen zwischen 6 und 20 % in verschiedenen (klinischen) Stichproben, wobei eine Repräsentativität der Stichproben in den meisten Studien nur sehr eingeschränkt gegeben war. Die Erstmanifestation der Symptomatik liegt jedoch bei über 80 % der Fälle im Kindes- und Jugendalter, weshalb diese Altersgruppe besonders betrachtet werden sollte. Hinsichtlich komorbider Störungen zeigt sich auch eine große Heterogenität mit Schätzungen zwischen 28 bis 76 % an komorbiden psychischen Störungen und etwa 25 % mit komorbiden körperlichen Erkrankungen. Die genaue Ätiologie ist derzeit noch nicht ausreichend untersucht. Erste neurophysiologische Erklärungsansätze und Bildgebungsstudien weisen auf eine spezifische physiologische Reaktion bei Misophoniepatient_innen hin. Obwohl mittlerweile eine Vielzahl von Fallberichten vorliegt, Diagnosekriterien und Messinstrumente entwickelt und erste kognitiv-behaviorale Behandlungsansätze evaluiert wurden, stellt die Misophonie weiterhin keine eigenständige neurologische, audiologische oder psychiatrische Störung im DSM-5 oder der ICD-11 dar. </jats:p

**Решение:** -1 обзор / комментарий / письмо

---

### 527 · R1438

**Insights from the First International Conference on Hyperacusis: causes, evaluation, diagnosis and treatment.**

2014 · Noise & health · article, conference object, conference proceedings · eng · https://doi.org/10.4103/1463-1741.132100

The First International Conference on Hyperacusis gathered over 100 scientists and health care professionals in London, UK. Key conclusions from the conference included: (1) Hyperacusis is characterized by reduced tolerance of sound that has perceptual, psychological and social dimensions; (2) there is a growing awareness that children as well as adults experience symptoms of hyperacusis or misophonia; (3) the exact mechanisms that give rise to hyperacusis are not clear, but the available evidence suggests that functional changes within the central nervous system are important and in particular, hyperacusis may be related to increased gain in the central auditory pathways and to increased anxiety or emotional response to sound; (4) various counseling and sound therapy approaches seem beneficial in the management of hyperacusis, but the evidence base for these remains poor.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 528 · R0093

**Çocukluk çağı travması ile mizofoni arasındaki ilişkide duygu düzenleme güçlüğünün aracılık rolünün incelenmesi**

2026 · Biruni Üniversitesi · master thesis · tur · https://hdl.handle.net/20.500.12445/3983

The aim of this study is to examine the mediating role of emotion regulation difficulties on the relationship between childhood trauma and misophonia. The participants of this study consists of 486 individuals aged 18 and over who are disturbed by specific sounds. This descriptive study is designed in accordance with the relational screening model to reveal the impact of childhood trauma on misophonia and the effect of emotion regulation difficulties on this relationship. The model used in the study is the structural equation model, which is employed to test theoretical constructs. Participants are selected using purposive sampling, a type of non-probability sampling. Data collection tools include the Demographic Information Form, Childhood Trauma Questionnaire, Misophonia Questionnaire, and Difficulties in Emotion Regulation Scale. Data were collected via Google Forms through social media and obtained data is analyzed subsequently. The analysis revealed a significant relationship between Childhood Trauma Questionnaire scores and Misophonia Questionnaire scores. From a gender perspective, there was a higher rate in the Childhood Trauma Questionnaire scores of women participants in comparison to men, indicating that women are more affected by childhood traumas. Similarly, comparisons in terms of misophonia also showed a significant difference in women. In terms of professional psychological support, those who received such support showed significant differences in childhood trauma and misophonia compared to those who did not. The analysis using the Structural Equation Model found that emotion regulation difficulties play a partial mediating role in the relationship between childhood trauma and misophonia. Bu çalışmanın amacı, çocukluk çağı travmaları ve mizofoni arasındaki ilişkide duygu düzenleme güçlüğünün aracılık rolünün incelenmesidir. Araştırmanın çalışma grubunu, ortaya çıkan seslerden rahatsız olan 18 yaş ve üstü 486 birey oluşturmaktadır. Betimleyici bir çalışma olan bu araştırmada çocukluk çağı travması ile mizofoni ve duygu düzenleme güçlüğünün bu ilişkideki etkisini ortaya koymak adına ilişkisel tarama yöntemine uygun şekilde düzenleme yapılmıştır. Çalışmanın modeli ise teorik yapıları test etmek için kullanılan yapısal eşitlik modelidir. Araştırmaya katılan bireylerin seçimi, olasılıksız örnekleme yönteminden olan amaçlı örnekleme yöntemiyle gerçekleştirilmiştir. Çalışmada veri toplama araçları olarak; Demografik Bilgi Formu, Çocukluk Çağı Travmaları Ölçeği, Mizofoni Ölçeği, Duygu Düzenleme Güçlüğü Ölçeği kullanılmıştır. Veriler sosyal medya aracılığıyla Google Forms üzerinden toplanmış, elde edilen veriler değerlendirilmiştir. Yapılan analizlerde cinsiyet değişkeni açısından bakıldığında; katılımcıların Çocukluk Çağı Travması Ölçeğinden almış oldukları puanlar açısından, kadınlar lehine anlamlı bir farklılık bulunmuştur. Benzer şekilde mizofoni açısından yapılan karşılaştırmada da kadınlar lehine anlamlı farklılık bulunmuştur. Profesyonel ruhsal yardım alma açısından bakıldığında; çocukluk çağı travması ve mizofoni açısından profesyonel ruhsal yardım alanlar lehine anlamlı fark bulunmuştur. Yapılan yapısal Eşitlik Modelin analizde, duygu düzenleme güçlüklerinin çocukluk çağı travması ile mizofoni arasındaki ilişkide kısmi aracılık rolü oynadığını bulunmuştur.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 529 · R1498

**Misophonia, Phonophobia, and “Exploding Head” Syndrome**

2010 · Springer eBooks · other literature type, part of book or chapter of book, book-chapter · en · https://doi.org/10.1007/978-1-60761-145-5_4

1. Misophonia, phonophobia, and “exploding head” syndrome have symptoms that may occur together with some forms of tinnitus or they can occur alone. 2. These sensations are different from hyperacusis which is a lowered tolerance to most kinds of sounds. 3. Misophonia is a dislike of specific kinds of sounds. 4. Attempts have been made to treat misophonia using the same methods as used for treating tinnitus. 5. Phonophobia is a fear of specific sounds related to the implication of the sounds. 6. The non-classical auditory pathways providing a subcortical route to the amygdala may be involved in phonophobia. 7. The “exploding head” syndrome is the experience of a very loud and sudden noise that seems to originate from within the head. It often occurs during sleep and wakes up the individual. 8. The “exploding head” syndrome may have similarities with REM sleep behavior disorder (RBD).

**Решение:** -1 глава книги / справочник

---

### 530 · R1485

**Pop-rock musicians: auditory and non-auditory effects due to electronically amplified music exposure**

2012 · Programa de Estudos Pós-Graduados em Fonoaudiologia

Introdução: Os músicos representam uma categoria profissional sob risco de problemas auditivos e queixas de saúde, em decorrência da exposição à música eletronicamente amplificada. Objetivo: Medir os níveis sonoros e identificar queixas auditivas e não auditivas em músicos de bandas de pop-rock. Método: Foram avaliados 34 músicos de pop-rock, do sexo masculino, com idades entre 26 e 60 anos. Os sujeitos responderam um questionário com dados sobre histórico de saúde, queixas relacionadas à audição e informações sobre exposição à música. Foi realizada a dosimetria de ruído no músico durante uma apresentação da banda em uma casa noturna de São Paulo. Para tanto foi utilizado um dosímetro do tipo 1, devidamente calibrado, cujo microfone foi posicionado próximo à orelha do músico, cinco minutos antes do início da apresentação. Resultados: A prevalência das queixas auditivas intolerância a som intenso e sente os ouvidos tampados foi de 20,6%. Do total, 50% da amostra relataram achar que o som ao qual está exposto afeta sua saúde. A maioria (27, 79,4%) dos músicos trabalha na profissão há mais de 10 anos. Os maiores níveis sonoros obtidos nas variáveis Lmax nível médio máximo, Lavg nível médio e Lmin nível médio mínimo em dB (A) foram de 129,6; 119,1 e 94,5 (respectivamente). E os menores foram de 105,9; 94,5 e 62,2 (respectivamente). Os valores estavam muito acima dos níveis máximos diários permitidos, segundo a Legislação Trabalhista. Conclusões: A dosimetria pode ser útil na investigação dos níveis. Entretanto, medidas de proteção aos músicos devem ser imediatamente adotadas com o objetivo de evitar os efeitos deletérios à saúde dessa populaçãoIntroduction: The musicians are part of a professional category under the risk of auditory issues and health complaints, due to electronically amplified music exposure. Objective: Measuring sound levels and identifying auditory and non-auditory complaints on pop-rock musicians groups. Method: 34 male pop-rock musicians, ages between 26 and 60 years old were evaluated. The subjects answered a questionnaire composed of health history, complaints related to hearing and information about music exposure. The noise dosimeter was applied on the musicians during a band concert on a nightclub in São Paulo. It was used a dosimeter type 1, properly calibrated, in which the microphone was positioned behind the musician s ear, 5 minutes before the beginning of the presentation. Results: The prevalence of auditory complaints, loud sound intolerance and the felling of occluded ears was 20,6%. From all, 50% of the sample reported the thought of being exposure to that sound can damage their hearing. The majority (27, 79,4%) of the musicians work in this area for further than 10 years. The highest sound level obtained on Lmax variation medium maximum levels, Lavg - average levels and Lmin - medium minimum levels in dB (A) were of 129,6; 119,1 and 94,5 (respectively). The values were further above the maximum level daily allowed, according to the occupational legislation. Conclusions: Dosimeter can be useful on levels investigation. Although, measures for musicians protection must be immediately taken, so that it can avoid deleterious effects on this population healthCoordenação de Aperfeiçoamento de Pessoal de Nível Superio

**Решение:** -6 не про мизофонию

---

### 531 · R0680

**Factors associated with internalizing and externalizing symptoms in a clinical sample of youth with misophonia.**

2023 · Journal of obsessive-compulsive and related disorders · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jocrd.2023.100831

Misophonia is an often chronic condition characterized by strong, unpleasant emotional reactions when exposed to specific auditory or visual triggers. While not currently defined within existing classification systems, and not clearly fitting within the framework of extant psychiatric conditions, misophonia has historically been studied most frequently within the context of obsessive-compulsive and related disorders. Internalizing and externalizing psychiatric symptoms are common in misophonia, but specific factors that confer risk for these symptoms remain unknown. The present cross-sectional study examined whether sensory sensitivity and cognitive emotion regulation facets are associated with co-occurring internalizing and externalizing symptoms in 102 youth with misophonia aged 8-17 years ( N females = 69). Participants completed self-report assessments of misophonia severity, sensory sensitivity, cognitive emotion regulation, and emotional-behavioral functioning. In the final model, controlling for all variables, multiple linear regression analyses revealed that sensory sensitivity and age were significant predictors of internalizing symptoms, while sensory sensitivity and the other-blame cognitive emotion regulation facet were significant predictors of externalizing symptoms. Further, findings demonstrated that the positive reappraisal cognitive emotion regulation facet moderated the effect of misophonia severity on internalizing symptoms. Results highlight a strong, consistent relation between sensory sensitivities (beyond sound sensitivity) and psychiatric symptoms in misophonic youth. Further research is necessary to determine mechanisms and clinical variables impacting internalizing and externalizing symptoms within youth with misophonia.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 532 · R0688

**Behavioral and pharmacological interference with the reconsolidation of a cue-elicited misophonia memory**

2023 · OSF Registries · studyregistration/pre-registration · https://doi.org/10.17605/osf.io/hq3r6

One of the core processes presumably underlying misophonia – a condition characterized by decreased tolerance for specific sounds – is associative learning. The goal of this project is to evaluate whether interference with the reconsolidation of a reactivated misophonia memory with propranolol or counterconditioning can alleviate aversive reaction to misophonia-related cues.

**Решение:** -7 protocol / preregistration without data

---

### 533 · R0887

**Using brief cognitive training on a mobile application to reduce anger and misophonic symptoms: A randomized control trial**

2022 · OSF Registries · studyregistration/pre-registration · https://doi.org/10.17605/osf.io/xdeyn

People with misophonia suffer from aversive reactions provoked by the presence or anticipation of a specific sound produced by other people (e.g., eating or breathing sounds). Such aversive reactions typically start with irritation or disgust that immediately becomes anger that initiates a profound sense of loss of self-control with rare but potentially aggressive outbursts. These impulsive aversive reactions drive the sufferer to avoid situations in which the triggers may be produced. The aim of the current study is to evaluate whether challenging anger-related maladaptive beliefs using a specialized mHealth app will reduce misophonic symptoms, cognitions and associated distress. Specifically, a randomized controlled trial with a crossover design was conducted with individuals reporting misophonic symptoms to evaluate the pre- to post- changes in the levels of misophonia-related distress and maladaptive beliefs following 15 days of app use. Our primary hypothesis is that the immediate use (iApp) group who used the Anger module of the GGtude platform from baseline measurement (T0) to completion of the anger module 15 days later (T1) would show decreased misophonic symptoms, anger and associated cognitions compared to the delayed app use (dApp) group at T1. It is also expected that the dApp group would exhibit a significant decline in all measurements after crossover (from T1 to T2b). The reductions in symptoms and cognitions found in the iApp group were expected to be maintained at 1 month follow up (T2a for iApp, T3 for dApp).

**Решение:** -7 protocol / preregistration without data

---

### 534 · R0979

**Beyond tingles: An exploratory qualitative study of the Autonomous Sensory Meridian Response (ASMR)**

2022 · PLoS ONE · article · en · https://doi.org/10.1371/journal.pone.0277962

This qualitative exploratory study investigated the embodied experiences and the meanings of Autonomous Sensory Meridian Response (ASMR) from the viewer's perspective. ASMR research has been sparse and largely quantitative, assuming it to be a predominantly fixed physiological response of "tingles", despite the acronym being rooted in pseudoscience. A qualitative research design was adopted to facilitate the exploratory nature of the study in this under-researched area. In contrast to the mostly survey-based research on ASMR, this study employed semi-structured interviews as a means to understand the lived experience of ASMR and to promote participant agency. Six self-identifying ASMR consumers were recruited using a mixture of snowball and opportunity sampling. Semi-structured interviews were conducted both in person and using Skype to facilitate transnational data collection. Interview transcripts were analysed using an inductive, data-driven approach to thematic analysis. The analysis suggests that ASMR is felt to provide a social environment of comfort rather than a solely physiological-based experience. Three key themes emerged: who and what defines ASMR? (reflecting the variety of what was classed as ASMR and what content was consumed to produce the response); "real" intimacy tailored to me (reflecting the idiosyncratic perception of intimacy made possible through ASMR); and emotional relief on my terms (reflecting the role of ASMR in self-soothing). The present data reflect a rich, complex experience of the ASMR consumer, pointing to potential wider applications and informing further research.

**Решение:** -6 не про мизофонию

---

### 535 · R1470

**Hatred of sounds: misophonic disorder or just an underreported psychiatric symptom?**

2013 · Annals of clinical psychiatry : official journal of the American Academy of Clinical Psychiatrists · article, case reports, journal article · eng · https://doi.org/10.1177/104012371302500406

BACKGROUND: Misophonia, or selective sound sensitivity syndrome, is a preoccupation with or aversion to certain types of sounds that evokes feelings of irritability, disgust, or anger. Recently, it has been suggested that misophonia is a discrete clinical entity deserving of its own place in psychiatric diagnostic manuals. In this paper, we describe 3 patients whose misophonia could be attributed to different underlying primary psychiatric disorders. METHODS: Case series report. RESULTS: In these patients, we argue that misophonia is better described as a symptom of a) obsessive-compulsive disorder, b) generalized anxiety disorder, and c) schizotypal personality disorder. CONCLUSIONS: The nosological status of misophonia remains a matter of debate. Patients who exhibit misophonia as a major complaint should be assessed for other conditions. Further studies on the prevalence, natural history, and additional features of misophonia are needed.

**Решение:** -2 клинический случай / серия случаев

---

### 536 · R1351

**Assessing Individual Variation in Personality and Empathy Traits in Self-Reported Autonomous Sensory Meridian Response**

2017 · Multisensory Research · article · en · https://doi.org/10.1163/22134808-00002571

Autonomous Sensory Meridian Response (ASMR) is a self-reported multi-sensory phenomenon described as a pleasant tingling sensation, triggered by certain auditory and visual stimuli, which typically originates at the back of the head and tends to spread throughout the whole body resulting in a relaxed and sedated state. Despite growing reports of ASMR there is a lack of scientific investigation of this intriguing phenomenon. This study is the first to examine whether self-reported ASMR is associated with individual differences in personality characteristics compared to general population. To do so we administered the Big Five Inventory (BFI) and the Inter-Personal Reactivity Index (IRI) to a group of individuals reporting to experience ASMR and a matched control group. Our findings showed that ASMR self-reporters scored higher on Openness to Experience and lower on Conscientiousness measures of BFI. They also showed greater scores on Empathic Concern and Fantasizing subscale of IRI. These findings are discussed in the context of the personality profile found in synaesthesia, which has been recently suggested to be more prevalent among people reporting ASMR experiences.

**Решение:** -6 не про мизофонию

---

### 537 · R0137

**719. A New Treatment for a New Disorder: Neurostimulation Enhanced Behavioral Therapy for Misophonia**

2026 · Biological Psychiatry · article, journalarticle · en · https://doi.org/10.1016/j.biopsych.2026.03.953

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 538 · R1265

**Misophonia Is a Legitimate Affliction**

2018 · ASHA Leader · article · en · https://doi.org/10.1044/leader.in1.23102018.4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 профессиональное издание (ASHA Leader)

---

### 539 · R1407

**Counterconditioning Treatment for Misophonia**

2015 · Clinical Case Studies · article, journalarticle · en · https://doi.org/10.1177/1534650114566924

Misophonia is a recently identified discrete and independent condition that cannot be classified using DSM-V criteria. With misophonia, a trigger stimulus elicits a reaction starting with irritation or disgust that immediately escalates. The trigger stimulus can be any typically occurring sound. The reaction is both extreme and irrational, and can include feelings of hate, anger, rage, and disgust. This response is perceived as involuntary, and individuals report feeling a loss of self-control. Misophonia can be conceptualized as a conditioned response to the trigger stimulus. This article describes a counterconditioning treatment of a middle-aged woman for misophonia that involved pairing a positive stimulus with a reduced trigger stimulus. Under these conditions, the misophonic response to the stimulus progressively weakened. Four distinct trigger stimuli were addressed in a multiple baseline treatment format. The overall severity of misophonia and the strength of the misophonic responses to triggers reduced over the course of the treatment, based on client self-assessments. These indicated large reductions in severity of misophonia and response to individual triggers, both at the end of treatment and at 10 months posttreatment. During treatment, responses to low intensity trigger stimuli were purely physical and independent of any emotional response. This demonstrated that, in this case, misophonia included a conditioned physical reflex to the trigger stimulus. It is proposed that misophonia consists of an aversive physical reflex elicited by the trigger stimulus and an emotional response elicited by the aversive physical reflex.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 540 · R0916

**Hyperacusis: demographic, audiological, and clinical characteristics of patients at the ENT department.**

2022 · European archives of oto-rhino-laryngology : official journal of the European Federation of Oto-Rhino-Laryngological Societies (EUFOS) : affiliated with the German Society for Oto-Rhino-Laryngology - Head and Neck Surgery · journal article · eng · https://doi.org/10.1007/s00405-022-07336-4

To document whether patients with and without hyperacusis differ from each other on demographic, audiological, and clinical characteristics. Based on the Hyperacusis Questionnaire's (HQ) cut-off (HQ > 28), a total of 2301 participants were divided into patients with and without hyperacusis. Demographic data, scores on self-reported questionnaires [Tinnitus Functional Index (TFI), Visual Analogue Scale of tinnitus loudness (VASloudness), Hospital Anxiety Depression Scale (HADS)], and audiological parameters were retrospectively analysed to determine differential factors between the two groups. In total, 10.9% of the patients was classified as hyperacusis patients (n = 251). They reported a significant, higher tinnitus severity (mean difference of 19 points on TFI) and mental distress (mean difference of 4 points on the HADS subscales) (p < 0.001) than patients without hyperacusis. Moreover, this group consisted of more women (45% % in hyperacusis group vs. 35% in non-hyperacusis group) and women scored significantly higher on the HQ (p < 0.001) and TFI (p < 0.01). Patients with hyperacusis have distinctive characteristics. The presence of hyperacusis in combination with tinnitus can indicate a higher need for psychoeducation. Patients that present themselves with hyperacusis without tinnitus complaints remain a minority, yet might be underdiagnosed. Hence, future studies should disentangle tinnitus from hyperacusis. In clinical practice, greater efforts are required to increase knowledge about hyperacusis as a primary or secondary complaint and to provide individualized treatment for these patients.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 541 · R1068

**Case Reports on Disorders of Sound Tolerance: Misophonia and Hyperacusis**

2021 · ISU ReD: Research and eData · text · https://core.ac.uk/download/481230579.pdf

Introduction: Misophonia is a rare disorder affecting approximately one in 1,500 people, of which, a small percentage are pediatric patients. Misophonia is characterized by the dislike of an explicit sound in a specific context. Treatment for misophonia includes a four-step program that can be modified for pediatrics. Case Presentation: A young female presented to the clinic with a significant distressed reaction when in the presence of specific sounds that included chewing, clicking pens, and loud music bass tones. Discussion: Treatment of misophonia is comparable to a care-plan for both tinnitus and hyperacusis. For this case, a four-step approach was used for treatment that entailed listening to something enjoyable, allowing a trusted adult to control the volume of an enjoyable sound, participating in enjoyable activities, and gradually becoming desensitized to bothersome sounds. Conclusion: Additional misophonia research in young populations is needed in order to develop treatment programs that may be individualized. Introduction: Hyperacusis affects approximately 1 in 50,000 individuals, so it is classified as a rare disorder. Hyperacusis is clinically indicated by a sensitivity to moderate sounds that can lead to physical pain or discomfort, and it co-occurs commonly with tinnitus. Case Presentation: An older adult presented to the clinic with intolerance to loud sound that included music played in her church, the voices of children, and booming laughter. She frequently donned circumaural headphones in noisy listening environments to self-prevent falling into a pattern of avoidance behavior. Discussion: Treatment of hyperacusis has a strong foundation in counseling and may be accompanied by a four-step approach that is comparable to treatment for tinnitus and misophonia. The goal of this four-step approach is to target sounds that are perceived as too loud and train the affected individual to become more tolerant. Conclusion: Testing and treatment for hyperacusis is comparable to that of individuals affected by tinnitus, as it has been hypothesized that cochlear cell damage may be responsible for these disorders. Nevertheless, there is a need for a test battery specific to hyperacusis in order to differentiate other disorders of sound tolerance

**Решение:** -2 клинический случай / серия случаев

---

### 542 · R1421

**Tools to Offer TLC for Hatred of Sound**

2015 · review, article · en

There is no approved screening tool for misophonia, but a case review can lead to a diagnosis. Several treatment options may aid in symptom management.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 543 · R0116

**Response: Commentary: The Brain Basis for Misophonia**

2026 · Newcastle University · journalarticle/journal contribution · https://doi.org/10.25405/ncl.34321866

No description provided

**Решение:** -1 обзор литературы / концептуальная статья

---

### 544 · R1425

**PSICOTERAPIA NARRATIVA EN UN CASO DE ANSIEDAD INFANTIL**

2015 · Ajayu Órgano de Difusión Científica del Departamento de Psicología UCBSP · article · es

El objetivo del presente analisis de caso es identificar la eficacia de las intervenciones basadas en la terapia narrativa, en un caso de ansiedad infantil de una nina de 11 anos por medio del analisis minucioso del proceso individual. El proceso de analisis es fundamental teniendo en cuenta que la ansiedad es una de las psicopatologias mas comunes en la poblacion tanto de ninos y adolescentes como de adultos, aumentando el riesgo de trastornos de otra indole como la depresion y otros. El proceso terapeutico se realizo con una nina de 11 anos a la cual se hace referencia con el nombre ficticio de Ana quien forma parte de dos sistemas familiares de clase social media alta. La nina mencionada llega a consulta con su padre con la demanda de controlar el malestar que le causaban los ruidos al momento de comer con su familia; malestar entendido por la familia como consecuencia del Sindrome de sensibilidad sonora selectiva o Misofonia y que conforma la historia dominante la cual sera reconstruida a partir de estrategias de externalizacion, la enorme capacidad de imaginacion de la nina y la construccion de una historia alternativa mas favorable para su desarrollo personal.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 545 · R0604

**Misophonia – symptom or disorder and susceptibility to psychotherapeutic treatment**

2024 · Zenodo · conference object, conferenceproceeding/ · en · https://doi.org/10.5281/zenodo.13911272

Summery: Misophonia, or “hatred of sound,” is defined as a complex neurophysiological and behavioral syndrome that involves intense physiological and emotional reactions to specific auditory stimuli. Specific triggers include everyday environmental sounds that may or may not be repetitive – chewing, coughing, slurping, typing, clicking pens… Common emotional responses include anger and rage, anxiety and panic, disgust. Physiological reactions often include muscle tension and elevated heart rate. The phenomenon was first described in 2001. Bibliometric analysis shows a growth in publications within neuroscience, psychiatry, psychology and related disciplines. Despite the increase in research, the etiology and mechanisms of the disorder are still unknown, and research is aimed at discovering both genetic and environmental factors. The initial line of research focused on distinguishing misophonia from related auditory disorders. Potential underlying mechanisms include connections to attention problems, anxiety, obsessive-compulsive tendencies, and emotional regulation problems. Misophonia is not included in the latest diagnostic categories and we lack systematic studies and standardized instruments to aid in the diagnostic process. Additionally, there are no guidelines or empirically supported treatments. Case Study – A client in late adolescence started therapy primarily due to issues with impulsivity and difficulties in emotional regulation. As a secondary concern, not the primary reason for seeking help, she reports extremely aversive reactions to certain sounds – chewing, loud breathing, coughing. As part of the treatment focused on recognizing emotions and strengthening emotional control, a portion of the process also targeted misophonia symptoms. The paper will present techniques that have been successful in reducing aversive reactions to misophonia triggers – techniques aimed at enhancing emotional literacy, with an emphasis on the emotion of anger and socially acceptable forms of expression, behavior control, and delayed response. The effects could be understood as supporting the hypothesis of emotional regulation as a factor of the disorder.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 546 · R0515

**The Johnson Boy, Age 11, and: Misophonia**

2024 · The North Dakota quarterly · article, journalarticle · en · https://doi.org/10.1353/ndq.2024.a928288

The Johnson Boy, Age 11, and: Misophonia Caitlin Johnson Castelaz (bio) The Johnson Boy, Age 11 And so, at a Nebraska construction site,one day while skipping school,he came across a sheet of plywoodtaller than his father or motherand managed to take it home.Past the house, the sagging fence,he dragged it into the woods,propped it against a treeand wedged himself between. He'd been stealing his parents' booze again, dizzywith the thrill of villainy and justice.His hands, finally as large as his father's,clutched a shock of grass and tore itfrom the scalp of the earth. The wound smelledfresh as Christmas. He had decidedto become an orphan. He borrowed a shovel without askingfrom the neighbor's shed and dug.The shaft was cheap wood that splintered.The blade rebelled, dull sheet of steel.For six feet's dig, his palms blistered,the juice in his limbs burned muscle and vein.He laid the plywood over the ground like a blanket.After this he could rest. It doesn't matter if my hands are muddy,or if my hair stinkslike rank forest bark.Somewhere a dog smells out its meal andhere, in the rot of autumn,in the gap between the trees, thereis sustenance, still. [End Page 145] Misophonia My father's work necessitated the useof a decibel meter, a gadget that helpslawyers prove the existence of noise. It's comforting, if not unlikely, to thinkall sound can be charted and graphedbut I've often wondered why, when ill oranxious, I hear the lamp hum accusations; an innocent songacquires a sinister timbre; and even anexhale sounds like a threat. And once, in my ex-boyfriend's father'shunting gear, I found something perverse: aheadset that could amplify a sighor discrete fart in the next room over: Unlike a decibel meter, this whatever-it-israises the question, who would want it, but also,in the name of all that is holy, why? As if this realm weren't already slitheringwith sounds too strange, too many anddragon-tailed to call down and catalog.Are bullet and blood not nightmare enough? Must we also magnify the sound ofa doe's final breath leaking out of herlike venom, a curse for anyone who hears? [End Page 146] Caitlin Johnson Castelaz caitlin johnson castelaz lives in New York City, where she works in media and tech. She holds a bachelor's degree in English from Northwestern University. Her poems have been published in Chiron Review, Coal City Review, and elsewhere. Copyright © 2024 University of North Dakota

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 547 · R1070

**Autonomous Sensory Meridian Response self-reporters showed higher scores for cognitive reappraisal as an emotion regulation strategy.**

2021 · PeerJ · article, other literature type, journal article · eng · https://doi.org/10.7717/peerj.11474

Background: Autonomous Sensory Meridian Response (ASMR) describes the experience of a pleasant tingling sensation along the back of the head, accompanied with a feeling of well-being and relaxation, in response to specific audio-visual stimuli, such as whispers, soft sounds, and personal attention. Previous works have assessed individual variations in personality traits associated with ASMR, but no research to date has explored differences in emotion regulation associated with ASMR. This omission occurred even when ASMR, a sensory-emotional experience, has been proposed to be located in a sound sensitivity spectrum as the opposite end of misophonia, a phenomenon associated with difficulties regulating emotions. The present work aimed to assess group differences between ASMR self-reporters and non-ASMR controls associated with emotion regulation strategies.Methods: We used the validated Spanish version of the Emotion Regulation Questionnaire to assess individual differences in the use of cognitive reappraisal and expressive suppression.Results: Our results showed that participants who experience ASMR had higher scores in the cognitive reappraisal subscale of the emotion regulation questionnaire than the non-ASMR group.Conclusions: Individuals who experience ASMR reported higher use of cognitive reevaluation of emotionally arousing situations, suggesting more effectiveness in regulating emotions. Our finding further elucidates individual differences related to this experience, supporting that ASMR is a real psychophysiological phenomenon associated with other psychological constructs and has remarkable consequences in affective/emotional dimensions and general well-being.Fondecyt Postdoctorad

**Решение:** -1 обзор литературы / концептуальная статья

---

### 548 · R0736

**The Persian Version of the Inventory of Hyperacusis Symptoms: The Translation Process, Psychometric Properties, and Diagnostic Criteria in Compared with Hyperacusis Questionnaire**

2023 · شنوایی شناسی - دانشگاه علوم پزشکی تهران · article, journalarticle · en · https://doi.org/10.18502/avr.v33i1.14272

Background and Aim: One of the important loudness perception problems is hyperacusis. It is generally defined as sensitivity to average-intensity sounds, which are perceived as excessively loud or uncomfortable. Assessing symptoms of sound intolerance and their impact on patients’ lives is crucial. The study aims to determine the validity and reliability of the Persian version of the Inventory of Hyperacusis Symptoms (IHS), assess its validity in differentiating normal-hearing and hyperacusis adults, and measure its cutoff point. Methods: The questionnaire was translated according to the international quality of life assessment protocol. After determining both qualitative and quantitative face validity and content validity, it was completed by 120 adults (60 with normal hearing and 60 with hyperacusis) to evaluate the differential validity and reliability. The reliability assessment was conducted using the test-retest method for all participants. For assessing the convergent validity, the correlation of the Persian IHS score with the score of the Hyperacusis Questionnaire (HQ) was evaluated. Results: The questionnaire had good face validity and content validity. The Cronbach coefficient α was 0.93 for the overall scale. The Interclass Correlation Coefficient (ICC=0.97) confirmed reliability. The cutoff point of the Persian IHS score was 48, with 91% sensitivity and 96% specificity. Additionally, a strong significant correlation was found between the scores of IHS and HQ (r=0.82). Conclusion: The Persian version of the IHS has high validity and reliability for use in hyperacusis clinics and research. Keywords: Hyperacusis; inventory of hyperacusis symptoms; validity; reliability

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 549 · R1480

**S.06.02 Quantitative electroencephalographic assessment of ADHD**

2013 · European Neuropsychopharmacology · article · en · https://doi.org/10.1016/s0924-977x(13)70142-1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 550 · R0997

**Measuring subjective quality of life in autistic adults with the PROMIS global–10: Psychometric study and development of an autism-specific scoring method**

2022 · Autism · article, other literature type · und · https://doi.org/10.1177/13623613221085364

Quality of life is widely acknowledged as one of the most important outcomes in autism research, but few measures of this construct have been validated for use in autistic people. The goal of the current study was to examine the psychometric properties of the Patient-Reported Outcomes Measurement Information System Global–10, an established self-report measure of health-related quality of life, in a sample of 901 autistic adults (predominantly female and adult-diagnosed) recruited from the Simons Foundation Powering Autism Research for Knowledge cohort. Using an item response theory framework, we performed a comprehensive psychometric evaluation of the Patient-Reported Outcomes Measurement Information System Global–10 in this sample, examining its latent structure, differential item functioning, reliability, and construct validity. After developing an autism-specific measurement model, the Patient-Reported Outcomes Measurement Information System Global–10 demonstrated excellent psychometric properties in the current sample, including excellent model-data fit, high reliability, minimal differential item functioning across subgroups of autistic adults, and an expected pattern of correlations with external variables. Exploratory analyses indicated that lower quality of life was associated with female sex and identified as a sexual/gender minority. A free online score calculator has been created to facilitate the use and interpretation of normed Patient-Reported Outcomes Measurement Information System Global–10 general quality of life latent trait scores for clinical and research applications (available at https://asdmeasures.shinyapps.io/promis_qol ). Lay Abstract Quality of Life an outcome that both researchers and autistic advocates agree is extremely important to consider when implementing services, interventions, and supports for autistic people. However, there has been little research on the topic of how quality of life can best be measured in autistic people or whether existing quality of life questionnaires are appropriate for use in the autistic population. This study aimed to validate an established quality of life measure, the Patient-Reported Outcomes Measurement Information System Global–10, in a large sample of autistic adults recruited online. We created a new way to score the Patient-Reported Outcomes Measurement Information System Global–10 scale and generate a “General quality of life” score specific to autistic adults. This new score performed very well in this sample, showing very little measurement error and relating in expected ways to similar constructs, such as physical health and emotional distress. Exploratory analyses found that lower quality of life was associated with female sex and self-identification as a sexual or gender minority (i.e. LGBTQ + identity). These findings suggest that the new Patient-Reported Outcomes Measurement Information System Global–10 quality of life score is a reliable and valid measure of quality of life in autistic adults, although additional studies are necessary to further explore its measurement properties in other subsets of the autistic population, such as individuals with intellectual disabilities. This measure is freely available for use as an outcome in both research and clinical practice, and an online score calculator is available to support the use of this measure in real-world applications.

**Решение:** -6 не про мизофонию

---

### 551 · R0635

**Family Accommodation in Children and Adolescents With Misophonia.**

2024 · Behavior therapy · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1016/j.beth.2023.09.001

Family accommodation (e.g., reassurance, modifying routines, assisting avoidance) has not been explored among youth with misophonia but may have important clinical and intervention implications. We examined family accommodation in 102 children and adolescents with interview-confirmed misophonia and compared its frequency and content to family accommodation in 95 children and adolescents with anxiety disorders. Findings showed that family accommodation was ubiquitous in pediatric misophonia and may be even more frequent than in youth with anxiety disorders. Assisting the child, participating in misophonia-related behaviors, and modifying family routines were endorsed by more than 70% of parents of children with misophonia. Further, compared to parents of children with anxiety disorders, parents of children with misophonia more frequently reported child distress and anger when they did not accommodate. Family accommodation was moderately to strongly associated with misophonia severity even when accounting for co-occurring internalizing and externalizing symptoms and sociodemographic factors. This first study of family accommodation in pediatric misophonia suggests accommodation may be an important clinical feature. A notable study limitation is that the measure of misophonia did not delineate between adaptive versus maladaptive accommodations. Excessive and maladaptive accommodation may be one potential candidate to target in interventions when considered within a broader treatment plan. Importantly, adaptive accommodations should also be considered in day-to-day management if they improve functioning and quality of life.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 552 · R1205

**Suicidal misophonia: a case report**

2019 · Psychiatry and Clinical Psychopharmacology · article, other literature type · en · https://doi.org/10.1080/24750573.2019.1597585

ABSTRACT Misophonia is still an unclassified disorder and means literally “strong dislike (hate) of sounds”. In this paper, we present a case report of an adolescent female who had misophonia that was complicated with two non-fatal suicide attempts. She presented with anxiety features and started to follow up for three years. Assessment of the level of misophonia for a year using Amsterdam Misophonia Scale (A-MISO-S) showed an extreme degree soon after the second suicide attempt. Initially, psychotherapy was noticed to be ineffective due to her poor motivation. Escitalopram was added to the management plan and improvement was reported in the depressive symptoms and obsessional thoughts of misophonia but were intolerable eventually because of the weight gain. Therefore, it was switched into Fluoxetine and Bupropion but six weeks later she attempted her second suicide by Bupropion overdose. At that point, the psychiatrist, the patient and her parents agreed to continue therapy with non-psychopharmacological treatment. Gradually she became more engaged in psychotherapy sessions after noticing its effectiveness. It was concluded that significant improvement of misophonia was reported when she was treated by Selective Serotonin Reuptake Inhibitors (SSRI) namely Escitalopram or Fluoxetine, motivated in psychotherapy sessions, adapted good coping strategies, decreased her dysfunctional challenging behaviour, rejoined social interaction and activity in her life, was more insightful and aware about her illness and developed self-acceptance.

**Решение:** -2 клинический случай / серия случаев

---

### 553 · R1455

**The misunderstood Misophonia**

2014 · Audiology Today · article, google scholar result · en · https://www.audiology.org/wp-content/uploads/legacy/resources/misophonia.pdf

In misophonia, or hatred of sound, the extreme reaction to sound is quite often limited to specific sounds, referred to as “trigger sounds.” Reported trigger sounds include chewing, breathing, and repetitive sounds like a pen clicking. The most common reaction is irritation followed by disgust or an

**Решение:** -1 обзор литературы / концептуальная статья

---

### 554 · R0970

**Does context matter in misophonia? A multi-method experimental investigation.**

2022 · Frontiers in neuroscience · article, journal article, journalarticle · eng · https://doi.org/10.3389/fnins.2022.880853

Introduction: Misophonia is a recently defined disorder in which certain aversive repetitive sounds and associated stimuli elicit distressing and impairing affective, behavioral, and physiological responses. The responses in misophonia may be stronger when the sound is produced by close friends and family, suggesting that the context in which a triggering cue occurs may have an important role in misophonia. As such, the goal of this study was to test experimentally whether the context of the sound source influences affective and psychophysiological responses to triggering stimuli in misophonia. Methods: Sixty one adults with misophonia and 45 controls listened to audio recordings (8 s) of human eating, animals eating, and human mouth smacking sounds (without eating). After a break, the same audio recordings were presented embedded within videos of human eating (congruent stimuli), animals eating (congruent stimuli), and, in the mouth smacking condition, with visually incongruent stimuli (hands playing in mud or in a bowl with a watery dough). Psychophysiological responses - skin conductance response (SCR) and heart rate (HR), and self-reported affective responses (valence, arousal, dominance) were gathered during the experiment in a laboratory. Results: Participants with misophonia assessed all the stimuli as more negative and arousing than the controls, and reported feeling less dominant with respect to the sounds. Animal and mouth smacking sounds were assessed by all the participants as less negative and arousing than human eating sounds, but only in the audio-video conditions. SCR data partially confirmed increased psychophysiological arousal in misophonia participants during an exposure to mouth sounds, but did not reflect the self-report changes in response to different contexts. Misophonia participants had deeper deceleration of HR than controls during human eating sound with congruent video stimuli, while there was no group difference during human mouth smacking with incongruent video stimuli. Conclusion: Results suggest that the context of mouth sounds influences affective experiences in adults with misophonia, but also in participants without misophonia. Presentation of animal eating sounds with congruent visual stimuli, or human mouth smacking sounds with incongruent stimuli, decreased self-report reaction to common misophonic triggers

**Решение:** -1 обзор литературы / концептуальная статья

---

### 555 · R0569

**Current Recommendations for the Use of Sound Therapy in Adults with Hyperacusis: A Scoping Review.**

2024 · Brain sciences · journal article, scoping review · eng · https://doi.org/10.3390/brainsci14080797

Hyperacusis is a condition that is characterized by hypersensitivity to normal everyday sounds or reduced sound tolerance and can affect patients in distressing ways. Sound therapy is a treatment intervention that is used to desensitize patients. However, as yet, there is a lack of understanding on how it is used in clinical practice, the different types of devices, or how to use them. The aim of this scoping review was to establish the current use of sound therapy in adults with hyperacusis and identify any factors that may influence treatment. Methodology: An established methodological framework was used to formulate the research question and guide the search strategy and reporting. The inclusion criteria were studies reporting adult (>18 years) populations with hyperacusis and sound therapy treatments which were published in any language. Searches of electronic databases (CINAHL, Cochrane Library, Medline (EBSCO), Scopus, PsycINFO) identified 31 studies that met the inclusion criteria (completed in April 2024). Data from included records were collated and summarized descriptively.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 556 · R1508

**36 Theory and Treatment of Tinnitus and Decreased Sound Tolerance**

2007 · Thieme eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1055/b-0034-89187

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 557 · R1344

**The Sound and the Fury: Characterizing Misophonia**

2017 · Fordham Research Commons (Fordham University) · dissertation, text · en

Misophonia, a recently coined term, describes a sound-sensitivity disorder in which individuals react to trigger sounds (e.g. chewing, swallowing, breathing) with marked distress, anxiety, irritability, and physiological arousal. To date, clinical and research literature has been limited – and an ongoing debate has emerged – regarding whether or not misophonia should be classed as a unique disorder, linked with other psychiatric conditions, particularly obsessive compulsive disorders, or considered a subclinical phenomenon. The present study addressed these questions by collecting diagnostic and self-report data from individuals enrolled in an ongoing randomized controlled treatment trial of misophonia. Specifically, this is the first known examination of misophonia in the context of DSM-5 psychopathology. Results demonstrate support for considering misophonia its own distinct disorder; no significant evidence was found to support the assertion that misophonia is a subtype of OCD. The present data suggest that anger is a core component of misophonia, in line with diagnostic considerations to date.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 558 · R0209

**Acceptance and commitment therapy versus progressive relaxation training for misophonia: A randomized controlled trial.**

2026 · Journal of affective disorders · article, comparative study, randomized controlled trial · eng · https://doi.org/10.1016/j.jad.2025.120366

Objective: To date, no in-person-delivered psychotherapies for adults with misophonia have been tested against active control conditions. The purpose of this study was to test the preliminary efficacy of acceptance and commitment therapy (ACT), supplemented with audiologically informed behavioral strategies (e.g., functional adaptations to manage exposure to misophonic sounds), versus education and progressive relaxation training (PRT) for adults with misophonia. Method: In a well-controlled randomized trial, 60 adults were randomized to ACT or PRT and each received 12, one-hour sessions of individualized psychotherapy for misophonia. Audiological and psychological assessments were conducted at baseline to assess for eligibility and severity of misophonia. Posttreatment, and three- and sixmonth follow-ups were collected. Assessments of assessor- and client-rated misophonia, clinical severity, wellbeing, psychological flexibility, and treatment credibility and acceptability were collected. Results: Both treatments were rated as credible and acceptable. Response rates for participant-rated misophonia (MQ scores) were small to modest in this sample (ACT 6.67–26.67 %, PRT 3.33–20 %), depending on the subscale. On an assessor-rated measure of misophonia, there were generally large within-condition effect sizes but no between-condition differences. Response rates for assessor-rated misophonia ranged from 20 % to 70 % for ACT and 6 % to 50 % for PRT, depending on the subscale. No between-condition differences were observed on clinician and participant-rated global severity, well-being, or psychological flexibility. Conclusions: This study showed medium to strong within condition effect sizes for ACT and PRT for misophonia. Additional research is needed, but it suggests psychosocial interventions can be beneficial for adults with misophonia

**Решение:** -3 выборка набрана из-за мизофонии

---

### 559 · R1316

**Sound bites**

2018 · book, doctoral thesis · eng · https://handle.uba.uva.nl/personal/pure/en/publications/soundbites(227f18c2-f02e-4d72-acd6-37f0289726d1).html

Misophonia (meaning hatred of sound) is a novel condition in which patients experience irritation, anger and disgust, triggered by sounds produced by other human beings. These intense emotions lead to severe suffering and social disfunctioning. The aim of this thesis was to lay a first foundation for understanding misophonia by addressing three core issues: 1. What is misophonia? 2. What happens in the brain of someone with misophonia during the misophonic reaction? 3. How can we treat misophonia? Our findings suggest that misophonia can be considered a separate psychiatric disorder. This is further underlined by our two neurobiological studies, using EEG and fMRI paradigms. Automatic processing of ordinary sounds is aberrant in misophonia patients. Subsequently, when they are confronted with misophonic triggers in a fMRI scanner, patients indeed feel anger and disgust and experience physiological arousal which is also visible in brain activation patterns. Importantly, misophonia symptoms can be reduced by a combination of four cognitive behavioral therapy techniques.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 560 · R1211

**MISOPHONIA: A NARRATIVE REVIEW ABOUT AN ELUSIVE NEUROPSYCHIATRIC CONDITION**

2019 · Morressier · article, review · en · https://doi.org/10.26226/morressier.5d1a037457558b317a1404bb

Objectives: to review recent literature concerning the clinical picture, therapeutic approach and future research goals concerning misophoniaBackground and aims: misophonia is a neurobehavioural syndrome defined by a heightened autonomic nervous system arousal and negative emotional reactivity towards specific sounds. There is scarce information about this condition, as it was described recently.Materials and methods: bibliographic search in Medline, with the keywords u201cmisophoniau201d and u201cSelective sound sensitivity syndromeu201dResults: Misophonia is a chronic condition, in which someone reports unpleasant emotional experiences and autonomic arousal in response to specific sounds. It is still uncertain if presents as a feature of co-occurring psychiatric disorders or if it is a specific disorder. Considering its therapeutic approach, most of the available data is based on case-reports of cognitive and behavioural interventions, such as exposure and response prevention, dialetic behavior therapy and acceptance and commitment therapy. There is no available data concerning the efficacy of specific pharmacological interventions, although if misophonia appears in the context of neurodevelopmental or anxiety disorders it could respond to agents modulating serotoninergic or antidopaminergic pathways.Conclusions: There is currently little information concerning misophonia, both related to its clinical characteristics, neurobiological basis and therapeutic approach. In the future, it will be importante to have a better charaterization of the symptoms among those who report impairment form misophonia and clarify whether it occurs as a specific symdrome or as part of other psychiatric disorders. Also, studies concerning psychotherapeutic and pharmacologic approaches with large samples will be necessary to define its preferencial approach.

**Решение:** -1 обзор / комментарий / письмо

---

### 561 · R1349

**The Brain Basis for Misophonia.**

2017 · Current biology : CB · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.cub.2016.12.048

Summary Misophonia is an affective sound-processing disorder characterized by the experience of strong negative emotions (anger and anxiety) in response to everyday sounds, such as those generated by other people eating, drinking, chewing, and breathing [1, 2, 3, 4, 5, 6, 7, 8]. The commonplace nature of these sounds (often referred to as “trigger sounds”) makes misophonia a devastating disorder for sufferers and their families, and yet nothing is known about the underlying mechanism. Using functional and structural MRI coupled with physiological measurements, we demonstrate that misophonic subjects show specific trigger-sound-related responses in brain and body. Specifically, fMRI showed that in misophonic subjects, trigger sounds elicit greatly exaggerated blood-oxygen-level-dependent (BOLD) responses in the anterior insular cortex (AIC), a core hub of the “salience network” that is critical for perception of interoceptive signals and emotion processing. Trigger sounds in misophonics were associated with abnormal functional connectivity between AIC and a network of regions responsible for the processing and regulation of emotions, including ventromedial prefrontal cortex (vmPFC), posteromedial cortex (PMC), hippocampus, and amygdala. Trigger sounds elicited heightened heart rate (HR) and galvanic skin response (GSR) in misophonic subjects, which were mediated by AIC activity. Questionnaire analysis showed that misophonic subjects perceived their bodies differently: they scored higher on interoceptive sensibility than controls, consistent with abnormal functioning of AIC. Finally, brain structural measurements implied greater myelination within vmPFC in misophonic individuals. Overall, our results show that misophonia is a disorder in which abnormal salience is attributed to particular sounds based on the abnormal activation and functional connectivity of AIC.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 562 · R1067

**'Misophonia in pregnancy - a case report'.**

2021 · Australasian psychiatry : bulletin of Royal Australian and New Zealand College of Psychiatrists · article, case reports, journal article · eng · https://doi.org/10.1177/1039856220986719

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 563 · R1029

**Case study of Relaxation and Counterconditioning Therapy for Misophonia: A Conditioned Aversive Reflex Disorder**

2021 · PsyArXiv · article, preprint · en · https://doi.org/10.31234/osf.io/nf8gw

Misophonia is an under-studied condition in which a person has intense emotional and physiological reactions to subtle stimuli (e.g., chewing sounds or hair twirling) which cannot be classified using DSM-5 criteria. This case illustrates the conceptualization of misophonia as a conditioned aversive reflex disorder consisting of a physical (e.g., muscle) reflex elicited by the misophonic trigger stimulus and subsequent emotional, physiological, and behavioral responses. This case describes a successful behavioral treatment of a middle-aged woman who was disabled by severe misophonia. The treatment included identifying the initial physical reflex, progressive muscle relaxation, and counterconditioning the initial physical reflex. Counterconditioning was accomplished by relaxing the initial physical reflex muscle during exposure to in vivo trigger stimuli, while using ambient sound as needed to reduce the severity of the misophonic response. The overall severity of misophonia reduced over the course of the 13-week treatment, based on client self-report. Data were analyzed using recovery percentage formula. The recovery percentage average of 3 scales was 82.1% at end of treatment and 93.1% at 1-year follow-up. In this case, when the initial physical reflex’s muscle was held relaxed by the patient when exposed to trigger stimuli, the initial physical reflex and the emotional reflex diminished and extinguished. This theory of misophonia, as a conditioned physical reflex to subtle stimuli, should be an essential consideration for research of the etiology, expansion, maintenance, and treatment of misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 564 · R0757

**Impact of a Virtual Reality-Based Simulation on Empathy and Knowledge Toward Misophonia**

2023 · Experiment@International Conference · article, conference object, journalarticle · en · https://doi.org/10.1109/exp.at2358782.2023.10546205

Virtual Reality (VR) is considered a powerful resource for developing empathy and pro-social behaviors since it allows individuals to experience a situation that is close to reality from another person's perspective. This quasi-experimental study was designed to measure the impact that a VR simulation which mimics the experience of misophonic symptoms, while performing a cognitive task, has on empathy and knowledge for this condition, compared to simply reading the descriptive vignette of the same simulation. The sample consisted of 98 higher education health students, randomly assigned to the experimental and control groups. The impact of the program was measured by filling out questionnaires on levels of empathy and knowledge about misophonia. Both methods (VR and vignette) were effective. However, the vignette proved to be more effective in some domains. These results suggest that not only VR, but also vignette texts may be interesting strategies for increasing empathy and knowledge towards people with misophonia in this population.info:eu-repo/semantics/publishedVersio

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 565 · R0695

**Right Prefrontal Cortical Thickness Is Associated With Response to Cognitive-Behavioral Therapy in Children With Obsessive-Compulsive Disorder.**

2023 · Journal of the American Academy of Child and Adolescent Psychiatry · journal article, research support, non-u.s. gov't, research support, n.i.h., extramural · eng · https://doi.org/10.1016/j.jaac.2022.07.865

Cognitive-behavioral therapy (CBT) is considered a first-line treatment for obsessive-compulsive disorder (OCD) in pediatric and adult populations. Nevertheless, some patients show partial or null response. The identification of predictors of CBT response may improve clinical management of patients with OCD. Here, we aimed to identify structural magnetic resonance imaging (MRI) predictors of CBT response in 2 large series of children and adults with OCD from the worldwide ENIGMA-OCD consortium. Data from 16 datasets from 13 international sites were included in the study. We assessed which variations in baseline cortical thickness, cortical surface area, and subcortical volume predicted response to CBT (percentage of baseline to post-treatment symptom reduction) in 2 samples totaling 168 children and adolescents (age range 5-17.5 years) and 318 adult patients (age range 18-63 years) with OCD. Mixed linear models with random intercept were used to account for potential cross-site differences in imaging values. Significant results were observed exclusively in the pediatric sample. Right prefrontal cortex thickness was positively associated with the percentage of CBT response. In a post hoc analysis, we observed that the specific changes accounting for this relationship were a higher thickness of the frontal pole and the rostral middle frontal gyrus. We observed no significant effects of age, sex, or medication on our findings. Higher cortical thickness in specific right prefrontal cortex regions may be important for CBT response in children with OCD. Our findings suggest that the right prefrontal cortex plays a relevant role in the mechanisms of action of CBT in children.

**Решение:** -6 не про мизофонию

---

### 566 · R1519

**Tinnitus and Hyperacusis Diagnosis**

2005 · conference object · eng · https://hdl.handle.net/11386/3862098

There is a great demand for robust measurements of tinnitus. Although such testing is performed routinely, response reliability has not been demonstrated. The diagnostic approach to tinnitus presents some general problems that must be considered. First of all the different professional consistency between managing other hearing difficulties and assessing tinnitus. Moreover the training programs do not focus on tinnitus management with the consequence of lack of adequate professional standards. A real problem is then to develope clinical management procedures for tinnitus that can be used in a standardized fashion: the multi-dimensional character of tinnitus create many difficulties in its management and objective measurements are hard to find. Finally the frequent association of hyperacusis in tinnitus patients (the prevalence is about 40%) must be take in account early because conditions testing order and treatment. This paper will explain our approach to tinnitus patient assessment that include three main point: aetiological diagnosis, psychometric and psychoacoustic evaluation. The evaluation of tinnitus patients includes three inseparable aspect: the attempt of an aetiological diagnosis, the psychometric evaluation by questionnaires or interviews and the psychoacoustic assessment that is the most problematic point given the lack of objective tinnitus measurements. Finally, a special section will be dedicated to decreased sound tolerance as important aspect able to condition testing ongoing and treatment settings.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 567 · R0550

**Tinnitus Stepped-Care: A Model for Standardizing Clinical Services for Tinnitus**

2024 · Seminars in Hearing · article · en · https://doi.org/10.1055/s-0045-1804509

Clinical services for tinnitus have expanded greatly since the "masking" method was introduced by Jack Vernon in the 1970s. According to PubMed, the number of peer-reviewed publications has increased dramatically since that time (seven with "tinnitus" in the title in 1975; 477 in 2023). With so much research and overall interest, it might be expected that tinnitus services have improved accordingly. In reality, there are many variations of treatment, but no one method has been shown to be more effective than any other. This diversity of methods is evident when researching "tinnitus" on the internet and considering the many different ways clinicians offer tinnitus services. Some offer an evidence-based method but may not have the competency to ensure fidelity. Further is the proliferation of commercial methods that can cost thousands of dollars. In this article, I propose a framework for providing tinnitus clinical services called Tinnitus Stepped-Care. This framework does not promote specific procedures for tinnitus assessment and treatment, but rather suggests guiding principles that are essential in each of six progressive steps of tinnitus clinical care. It is further proposed to test the stepped-care model in the (currently under development) Tinnitus Learning Health Network (TLHN). The TLHN would consist of a network of clinicians, patients, and researchers from around the world who collaborate in establishing "best tinnitus practices." Collaboration would involve using and sharing data for the ongoing monitoring of a large, diverse, well-described patient population, and using quality improvement science to test and monitor outcomes over time, to determine the most effective treatments for different subgroups of tinnitus patients.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 568 · R1337

**Misophonia and affective disorders: The relationship and clinical perspective**

2017 · European Psychiatry · article, other · en · https://doi.org/10.1016/j.eurpsy.2017.01.539

Misophonia is characterized by aversive reactivity to repetitive and pattern based auditory stimuli [1]. Misophonic sufferers demonstrate autonomic nervous system arousal, accompanied by heightened emotional distress. Sufferers describe extreme irritation, anger, and aggressive urge with physiological reactions including hypertonia, diaphoresis and tachycardia [2]. Some studies have found comorbidity with psychiatric disorders. However, most of these studies used small samples and few experimental methodologies [3]. This study identifies the possible relationship between misophonia and affective disorders, and any difference between the severity of misophonia in male and female patients. Fifty misophonic patients (female = 25, mean age = 46.28) were evaluated with Amsterdam Misophonia Scale (A-MISO-S) for the diagnosis of misophonia and with the M.I.N.I International Neuropsychiatric Interview for the diagnosis of affective disorders. Among n = 50 misophonic patients, we found major depression (MDD) = 11, melancholic depression = 5, dysthymia = 11, suicidality = 10, manic = 3, panic disorder = 8, agoraphobia = , social phobia = , obsessive compulsive disorder (OCD) = 14, post-traumatic stress disorder (PTSD) = 15. Misophonia was associated with MDD (U = 76, P = .001), suicidality (U = 67, P = .001), OCD (U = 115, P = .002) and PTSD (U = 142.5, P = .008). There was an indication of a significant difference between men and women in severity of misophonia (U = 160.5, P = .002). The presence of these varying affective disorders suggests that the sufferers are at high risk for affective disorders. Investigation of the co-morbidity will assist researchers to better understand the nature of the symptoms and how they may be interacting.Disclosure of interestThe authors have not supplied their declaration of competing interest.</jats:sec

**Решение:** -1 обзор литературы / концептуальная статья

---

### 569 · R1363

**Good Stress Gone Bad: Transition Conditions in Transforming Stress from Negative to Positive**

2017 · https://doi.org/10.26690/sri20170702

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 570 · R0444

**Recognizing individual variability in misophonia: Identifying symptom-based subgroups with Gaussian mixture modeling.**

2025 · Journal of psychiatric research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.jpsychires.2025.02.054

Misophonia is characterized by intense emotional and physiological reactions to everyday sounds such as chewing and tapping. While previous researchers have focused on defining and characterizing the disorder, limited attention has been given to the variability in symptom presentations across individuals. In this study, we sought to identify distinct subgroups of individuals with misophonia by applying a Gaussian finite mixture model to explore the heterogeneity of symptom profiles. Sixty treatment-seeking participants completed the Duke Misophonia Interview, which assessed the presence and severity of various behavioral, affective, and cognitive symptoms. Items from this measure served as model indicators. Two clusters were found: anticipatory and reactive. The anticipatory group reported heightened awareness of potential triggers, preemptive anticipatory distress, and increased avoidance behaviors, while the reactive group primarily displayed emotional and physiological responses during the occurrence of sounds. Notably, both groups reported similar frequencies of misophonic triggers, but the anticipatory group demonstrated greater internalizing symptoms, such as intrusive thoughts or rumination about misophonic sounds and social isolation. Our findings support the need for tailored interventions that address subgroup-specific symptom patterns. Future researchers should aim to include larger sample sizes and develop more comprehensive models to capture the full spectrum of misophonia symptoms, including externalizing behaviors.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 571 · R0512

**Loud and unwanted: Individual differences in the tolerance for exposure to music**

2024 · The Journal of the Acoustical Society of America · article, journalarticle · en · https://doi.org/10.1121/10.0025924

Music is generally considered a pleasant and positive stimulus. However, constant exposure to loud music, especially in acoustic environments where individuals have limited control, can transform music listening into a potentially distressing and detrimental experience. In certain contexts, music can therefore be classified as noise, with implications for mental well-being and cognitive functioning. In our paper, we delve into the complexities of this paradoxical phenomenon, discussing the implications of commonly experienced situations in which music becomes a source of discomfort due to its intensity or forced exposure. Our exploration of the effects of music exposure focuses on individual differences, encompassing clinical sensitivity (hyperacusis, misophonia), non-clinical sensitivity (noise sensitivity, sensory-processing sensitivity), and music-related individual factors (sensitivity to music pleasure). We argue that only by recognizing these aspects, significant progress can be made in prevention strategies and interventions. Our aim is to identify regulatory gaps and propose strategies to mitigate potential music-related discomfort in order to promote the creation of auditory environments that align with individual preferences and sensitivities. This approach is particularly relevant when considering clinical and non-clinical populations, for whom sensory sensitivities may substantially influence the quality of life.</p

**Решение:** -1 обзор литературы / концептуальная статья

---

### 572 · R0642

**Misophonia in relation to sensory sensitivity**

2024 · Työväentutkimus Vuosikirja · article · fi

Tavoite: Misofonia on vielä vähän tutkittu ilmiö, mutta se voidaan määritellä häiriöksi, jossa tietyt äänet aiheuttavat kohtuuttoman voimakkaita negatiivisia tunnereaktioita. Sen voidaan ajatella olevan yksi aistiherkkyyden muoto, millä yleisesti tarkoitetaan tavallista herkempää tai voimakkaampaa reagointia ympäristön ärsykkeisiin. Aistiherkkyydelle ei ole olemassa vakiintunutta määritelmää ja se voidaan jaotella kolmeen eri näkökulmaan: subjektiiviseen (itse koettu aistiherkkyys), neuraaliseen (aistiärsykkeen aiheuttama hermostollinen vaste) ja behavioraaliseen (kyky havaita tai erottaa aistimuksia). Katsauksen tavoitteena on selvittää misofonian suhdetta aistiherkkyyteen hyödyntäen edellä mainittua jaottelua. Menetelmät: Kirjallisuushaku toteutettiin syys-lokakuussa 2023 käyttäen pääasiassa PubMed- tietokantaa. Hakusanoina käytettiin termejä kuten “misophonia”, "selective sound sensitivity", "sensory over-responsivity", "sensory hypersensitivity" ja "sensory sensitivity". Tulokset: Misofoniasta kärsivät raportoivat johdonmukaisesti kontrolliryhmiä enemmän, mutta ei äärimmäistä subjektiivista aistiyliherkkyyttä eri aistien osalta. Heillä esiintyi myös subjektiivista aliherkkyyttä, joskin tuloksissa oli enemmän vaihtelua ja voi selittyä kysymyksien monitulkinnallisuudella. Behavioraalista aistiherkkyyttä tutkittiin vain vähän ja tulokset olivat vaihtelevia, mutta niiden perusteella misofoniasta kärsivien moniaistinen aistiherkkyys sai jonkin verran tukea. Neuraalista aistiherkkyyttä ei käsitelty tutkimuksissa lainkaan. Aihetta ei ole tutkittu paljon ja misofonian määrittelyssä käytetyt kriteerit vaihtelivat. Tulokset antoivat kuitenkin viitteitä siitä, että misofoniasta kärsivät ovat moniaistisesti aistiherkkiä, erityisesti subjektiivisesta ja osin behavioraalisesta näkökulmasta.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 573 · R0103

**Normative Ranges for Auditory Brainstem Response Wave I Amplitude: A Potential Diagnostic Indicator of Cochlear Deafferentation.**

2026 · American journal of audiology · article, journal article, journalarticle · eng · https://doi.org/10.1044/2026_aja-25-00296

Purpose: While cochlear synaptopathy has limited impact on auditory thresholds, there is increasing evidence that cochlear deafferentation is associated with auditory perceptual deficits. However, there is currently no means for diagnosing synaptopathy or deafferentation in individual patients. The objectives of this study were to establish normative ranges for auditory brainstem response (ABR) Wave I amplitude, a measure sensitive to synaptopathy in animals, in a population at low risk for cochlear deafferentation and then compare a population at high risk for deafferentation to the normative ranges. Method: The low-risk sample consisted of 169 non-Veteran young adults with normal audiograms, minimal self-reported noise exposure history, and no auditory complaints (tinnitus, decreased sound tolerance, or speech perception in noise difficulty). ABR Wave I amplitude normative ranges were generated for 2, 4, and 8 kHz tonebursts and were statistically adjusted for sex and average distortion product otoacoustic emission (DPOAE) levels. Ninety-one military Veterans with normal audiograms and at least one auditory complaint were included in the high-risk comparison sample. Results: While the DPOAE-adjusted ABR normative ranges were effective at distinguishing between the low- and high-risk samples, the results also indicated that adjusting the ABR normative ranges for outer hair cell dysfunction may not be necessary and could be problematic. ABR normative ranges that were adjusted only for sex were able to differentiate between the low- and high-risk samples, with 51% of the high-risk sample falling below the normative ranges for a 105 dB peak equivalent sound pressure level 8-kHz toneburst. Conclusion: In patients with normal audiograms, sex-specific ABR Wave I amplitude normative ranges can be used by clinicians to identify patients with high degrees of cochlear deafferentation. </jats:sec

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 574 · R0192

**Hyperacusis surgery: The lifechanging effects of round and oval window reinforcement using a patient reported outcome analysis.**

2026 · American journal of otolaryngology · journal article · eng · https://doi.org/10.1016/j.amjoto.2026.104944

To evaluate patient-reported outcomes following round and oval window reinforcement (RWR/OWR) surgery for hyperacusis using a concise disease-specific outcome instrument incorporating sound tolerance, pain hyperacusis, psychological well-being, and global quality-of-life measures. Retrospective cohort study. Tertiary referral neurotology practice. Eighty-nine patients with debilitating hyperacusis who underwent round and oval window reinforcement surgery from 2014 to 2026. Round and oval window reinforcement surgery. A novel hyperacusis surgery outcome survey incorporating hyperacusis severity, pain hyperacusis, functional sound tolerance, psychological distress, and global improvement. 71.8% of patients reported that their hyperacusis was better or much better following surgery. Respondents reported a significant improvement in hyperacusis severity, pain tolerance, sound tolerance, psychologic distress, and global parameters. Overall, 68% (26/38) of respondents would recommend the surgery to someone who has failed conservative therapy for hyperacusis. Round and oval window reinforcement surgery demonstrated meaningful improvements in sound tolerance, pain perception, and quality of life among appropriately selected patients with hyperacusis.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 575 · R0518

**Study 2: What are the appraisals, perceptions, and coping strategies in response to adverse sound experience among autistic adults?**

2024 · University College Cork · thesis

Chapter One: Introduction This chapter introduces autism as a heterogenic condition and discusses the different types of Decreased Sound Tolerance (DST). Further information related to influential models of autism are also provided. Chapter Two: Scoping Review This chapter presents ‘A Scoping Review of Noise-Attenuating Device Use and its Consequences in Autistic People’. The review is written in the format of a journal article for ‘Research in Autism Spectrum Disorders’. Chapter Three: Scoping Review: Extended Methodology Supplementary information pertinent to the process of completing the scoping review is presented in this chapter. This information pertains to the development of the review question, eligibility criteria, and search strategy. Further information related to the synthesis, data extraction and the rationale for selecting a scoping review as a methodological framework is included. Chapter Four: Major Research Project In this chapter, the empirical paper explores the experience of sound intolerance among autistic people, as well as the coping strategies used to address this. The paper is written in the format of a journal article for ‘Autism’. Chapter Five: Supplementary Information for Major Research Project This chapter provides further information on the methodology of the major research project. This included an in-depth description of Interpretative Phenomenological Analysis (IPA) and its use in autism research information on sampling and recruitment, further information on the data collection and analysis process, and reflexivity. Chapter Six: Discussion and Conclusion The findings of the scoping review and the major research project are summarized in this chapter, as well as the limitations, clinical implications, and original contributions. Appendices Appendices pertaining to the scoping review and major research project are presented in this section

**Решение:** -7 ceu / self-assessment questions

---

### 576 · R0754

**Misofonifeltet i fremvekst: Oversettelse og kvalitetssikring av et spørreskjema**

2023 · master thesis · nor · http://hdl.handle.net/10852/104837

Formål: Gjennomføre en kvalitetssikring av en norsk versjon av Berlin Misophonia Questionnaire Revised (BMQR-NOR) ved å undersøke de psykometriske egenskapene til spørreskjemaet og sammenligne det med et annet misofoni-spørreskjema, MQ-NOR. Metode: BMQ-R ble oversatt til norsk (BMQR-NOR) med utgangspunkt i retningslinjene angitt i «Process of translation and adaptation of instruments» av WHO (u.å.). Deretter ble BMQR-NOR opprettet som et nettbasert spørreskjema i tjenesten Nettskjema, som var koblet til Tjenester for Sensitive Data (TSD). Ved første måletidspunkt (T1) svarte 82 deltakere med selvrapportert misofoni på BMQR-NOR og MQ-NOR, og ved andre måletidspunkt (T2) svarte 41 av disse på BMQR-NOR en annen gang. Intern konsistens ble evaluert med McDonalds omega og Cronbachs alfa. Konvergent validitet ble vurdert ved Spearmans korrelasjonskoeffisient mellom BMQR-NOR og MQ-NOR. Test-retest reliabiliteten ble evaluert ved bruk av Cohens vektet kappa og Intraklassekorrelasjonskoeffisienter. Resultater: BMQR-NOR viste generelt god intern konsistens. Utvalgte delskalaer fra BMQR-NOR korrelerte signifikant og positivt med MQ Emosjoner og Atferds Skala fra MQ-NOR, og viste dermed konvergent validitet. Test-retest reliabiliteten til BMQR-NOR var akseptabel. Konklusjon: BMQR-NOR viser akseptable psykometriske egenskaper. Ved bruk av spørreskjemaet anbefales det imidlertid å utvise forsiktighet inntil det har gjennomgått ytterligere validering.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 577 · R1226

**Guidelines for Writing an Audiology Case Study**

2019 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0000582440.17021.cb

Case studies provide accurate and complete accounts of patient symptoms, history, care, potential complications, treatment alternatives, and preventive medicine and disease avoidance. Some highlight the clinical findings in a patient with a rare disease or disorder. A published case study may be used to reinforce best practices, report alarming observations in a patient encounter, and convey important clinical knowledge. Case studies may also contribute to improving the safety of our patients. In preparation for a new section in The Hearing Journal that will feature audiology case studies, we outline the structure and necessary components of an audiology case study.iStock/tumsasedgars, audiology, case study, medical educationTable 1: The Hearing Journal’s Case Study Writing GuidelinesWHAT'S A CASE STUDY? As far back as the 1800s, case studies (also called case reports) became established as a popular tool for medical training. At that time, a case study was intended to accumulate knowledge of clinical issues, diagnostic methods, and treatments. They were primarily written to provide an educational message about the etiology and pathogenesis of diseases and disorders, as well as improvement of patient care. Today, case studies serve the same educational functions. Any component of a written clinical note about a patient can form the basis of a case study, such as an unusual patient complaint, atypical test findings, a rarely encountered diagnosis, or even a novel treatment plan. Fundamentally, a case study should tell a succinct story about the patient that may be readily consumed by clinicians, students, researchers, therapists, allied health personnel, and, on occasion, manufacturer representatives. Although a bell curve is commonly used to represent patient outcomes on a distribution, we accept that, for various reasons, some patients lie somewhere on the tails of the curve. These outliers often become the subjects of case studies. Audiologists frequently say, “Two patients with the same audiogram do not always have the same complaints.” The opposite is also true. Two patients with similar chief complaints and histories may, in fact, have very different diagnoses. These nuances may be captured in a well-presented case study. Clearly, not every patient experiences the same progression of hearing loss, vestibular disease, or tinnitus, or the same degree, type, and pattern of hearing loss or related disorder. Large clinical research studies are not practical for diagnosis and treatment of every clinical condition, particularly ones with multiple factors at play.1 Controlled experimental trials usually report group-level data that may not be applied to or clinically relevant for all patients. Indeed, statistically significant findings in a large research study of people with a particular disorder may have absolutely no clinical significance to the assessment and management of individual patients with the same disorder. In contrast, published case studies are invariably clinically relevant and instructive. HOW TO GET PUBLISHED A major advantage of a published case study is the modest manuscript length, especially when the subject is a single patient. In most medical specialties, published case studies are brief and about issues related to one patient. Audiology case studies tend to be more extensive with substantial literature review. Some even include multiple patients, or are included as part of a research report. The challenge in preparing a case study is to concisely and briefly tell an adequately detailed clinical story about a patient. Overall, a case study must be no less than 750 words and no more than 1,400 words. Table 1 summarizes guidelines for submission of case studies for publication in The Hearing Journal. This should make the task of writing the manuscript more tolerable for audiologists. Clinicians will enjoy an article that is organized, succinct, and contains a compelling educational message. To reach this goal, a case study manuscript should include some or all the components described below.2,3 Published case studies are a practical and clinically useful venue for disseminating important information about the assessment and management of people with hearing loss and related disorders, including auditory processing disorders, tinnitus, disorders of decreased sound tolerance, and vestibular problems. Case studies allow us to highlight those unique differences and findings that we observe in our patients and our patient populations. A case study may serve as a training tool for students and junior clinicians. Used this way, they can enhance clinical learning, and serve as a catalogue of our experiences. Published case studies may be used to advance an audiologist's career. In some instances, a case study may stimulate research, such as large experimental studies. Finally, case studies may focus on actions taken in the clinic that demonstrate safer examinations and treatments of audiology patients.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 578 · R0242

**Comorbid Anxiety and Depression in Hyperacusis and Misophonia. Reply to Jastreboff, P.J. Comment on "Rodrigues, A.L.M.; Aazh, H. Psychiatric Comorbidities in Hyperacusis and Misophonia: A Systematic Review. Audiol. Res. 2025, 15, 101".**

2025 · Audiology research · article, comment, journal article · eng · https://doi.org/10.3390/audiolres15060147

This systematic review found that depression was reported in 8-80% of patients with hyperacusis and 1 [...].

**Решение:** -1 обзор / комментарий / письмо

---

### 579 · R1143

**SELF-IDENTIFIED MISOPHONIA PHENOMENOLOGY, IMPACT, AND CLINICAL CORRELATES**

2020 · Psychological Thought · article, review, google scholar result · en · https://doi.org/10.37708/psyct.v13i2.454

Misophonia is a newly recognized condition involving adverse emotional reactions to environmental sounds, most often produced by other people. This study reports results of a survey describing the phenomenology of misophonia based on a large sample. Survey data were collected from individuals self-identified as having misophonia. A total of 1,061 individuals reported specific distressing reactions to sounds, and responses indicating severity of misophonia and perceived comorbidity. Over 82% of respondents were female. The average age of the study participants was 37.49 years ( SD = 12.24; range from 18 to 72). Most respondents reported multiple triggers and adverse emotional reactions, as well as multiple coping responses. The majority of respondents reported comorbid diagnoses. Misophonia severity is described, as well as impact on quality of life. A minority of respondents had some experience with treatment and most reported no change in symptoms. Treatments reported for misophonia were typically ineffective, and once developed, misophonia symptoms persist. The results of the study showed that misophonia is a newly recognized condition that appears to have important impact on people’s lives. It typically develops in early life, and is associated with a reduced quality of life, substantial comorbidity, negative emotional experiences, and behaviors that are likely to impact interpersonal relationships.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 580 · R0043

**Impacts of Distress Intolerance and Anxiety Sensitivity on the Maintenance and Treatment of Youth Misophonia.**

2026 · Journal of clinical psychology · article, journal article, randomized controlled trial · eng · https://doi.org/10.1002/jclp.70095

ABSTRACT Objective Misophonia often co‐occurs with emotional disorders in youth, indicating that these conditions may share underlying risk factors, such as distress intolerance and anxiety sensitivity. However, the specific relationships between misophonia severity, distress intolerance, and anxiety sensitivity have not been formally explored. Understanding how these transdiagnostic risk factors impact misophonia severity and related impairment could offer valuable insights into misophonia phenomenology and identify key therapeutic targets for affected youth. Methods This study examined the impacts of distress intolerance and anxiety sensitivity on misophonia severity during treatment in youth ( N = 43) randomized to either a 10‐week course of the Unified Protocols for Transdiagnostic Treatment of Emotional Disorders in Children and Adolescents (UP‐C/A; N = 29) or psychoeducation/relaxation training (PRT; N = 14). Youth completed self‐report measures at 0‐, 5‐, and 10‐weeks post‐enrollment. Results Greater distress intolerance and anxiety sensitivity were both associated with greater misophonia symptom severity at pre‐treatment. Distress intolerance, but not anxiety sensitivity, improved significantly across treatment course. Compared to youth receiving PRT, youth receiving UP‐C/A exhibited greater improvements in distress intolerance across treatment, and indirect effect estimates indicated that improvement in distress intolerance was a mechanism through which the UP‐C/A elicited change in misophonia symptom severity. Conclusion Preliminary findings support distress intolerance as a mechanism of symptom change in transdiagnostic cognitive‐behavioral treatment for youth misophonia. Future large‐scale trials are warranted to further investigate distress intolerance and other transdiagnostic factors as treatment targets for misophonia.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 581 · R0417

**A Pilot Clinical Trial Examining Exposure and Stress Management Therapy for Adults With Misophonia.**

2025 · Journal of psychiatric practice · article, journal article, journalarticle · eng · https://doi.org/10.1097/pra.0000000000000874

Misophonia is a recently recognized condition characterized by extreme intolerance of idiosyncratic and repetitive sounds (often human-generated gustatory or breathing-based noises), coupled with intense affective-based reactions, that results in significant impairment and distress. Cognitive-behavioral therapy approaches, including exposure principles and stress management/distress tolerance skills, have demonstrated promise for the treatment of misophonia. However, efforts to develop interventions remain ongoing and further empirical examination of candidate treatment models is needed. In the pilot study described in this article, we preliminarily examined the efficacy of exposure and stress management therapy (ESMT) individually delivered via synchronous telehealth modality for adults with misophonia. Data from 26 participants (mean age=34.4 y) enrolled between April 2016 and September 2020 provided initial support for ESMT on the basis of pretreatment to post-treatment reductions in misophonia symptomology and increases in distress tolerance. Gains were generally maintained at 3- and 6-month follow-ups. The results did not appear to differ based on the order in which the exposure and stress management modules were delivered, which was randomized across participants. Participant perceptions of ESMT homework regarding adherence, comprehension, and usefulness were generally acceptable. This study provides preliminary support for ESMT as a potentially viable psychosocial intervention for misophonia and highlights the promising roles of exposure (with appropriate adaptations) and stress management for alleviating misophonia-related distress and impairment. Findings are discussed in the context of continuing to develop, refine, and test ESMT using more rigorous methodologies and diverse samples.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 582 · R0621

**For Whom the Bell Tolls: Misophonia as a complex experience of hope and dread in self-with-other regulation**

2024 · Psychoanalysis Self and Context · article, journalarticle · en · https://doi.org/10.1080/24720038.2024.2332240

ABSTRACT Misophonia is a condition in which everyday sounds evoke pain and reactive aversion. The etiology of misophonia is largely unknown, with discordant conceptualizations of its roots, ranging from psychiatric, to neurological, to a combination of auditory processing and neurobiological dysfunction. Common protocols are focused on symptom reduction and management, though have not been proven to be clinically effective. For these reasons, it is generally considered to be difficult to treat. In this paper, I re-consider misophonia as a complex interweaving of auditory, neurobiological and relational experience. Reflecting upon a clinical case, I present misophonia in the context of self-with-other regulation from a developmental lens, traverse the landscape of misophonic self states, explore the complex toll of dissociation and intergenerational trauma in relational space, and consider ways in which the painful somatic-auditory bell of misophonia concretizes self and relational “hope” and “dread”. Finally, I will offer some thoughts on how psychoanalytic psychotherapy can create new relational-neurobiological pathways out of the misophonic experience.

**Решение:** -7 ceu / self-assessment questions

---

### 583 · R0404

**Kasuistik einer traumatisch bedingten Phonophobie**

2025 · Laryngo-Rhino-Otologie · article · de · https://doi.org/10.1055/a-2699-8615

Einleitung Eine Phonophobie als „sonstige abnorme Hörabweichung“ (ICD H93.2) kann diagnostiziert werden, wenn Patienten auf spezielle Geräusche – weitestgehend unabhängig von deren Lautstärke – mit hohem subjektivem Leiden und Erschrecken reagieren. Anders als beim Recruitment bei Innenohrerkrankungen ist dies unabhängig von einer Höreinschränkung [ 1 ]. Anders als bei einer allgemeinen Hyperakusis mit einer Überempfindlichkeit über das gesamte Frequenzspektrum des Hörvermögens steht bei der Phonophobie die individuelle Bedeutung der akustischen Signale im Vordergrund [ 1 ]. Diese können – von außen offensichtlich – etwa für Lehrer oder Erzieherinnen Kinderstimmen sein, bei Büroangestellten kann es das Telefonklingeln oder das Rauschen des Computerlüfters sein. Eindringlich hat F. Kafka seine Phonophobie für Geräusche von bestimmten Personen in der Erzählung „Großer Lärm“ [ 2 ] beschrieben. Speziell bei der Misophonie imponiert die starke Reaktion mit Hass, Wut und Ekel gegenüber Geräuschen, die mit Essen, z.B. Kauen und Schlucken, Schlürfen, Schlucken) oder Atmen verbunden sind [ 3 ]. Schwieriger kann die Zuordnung bei einer posttraumatischen Belastungsstörung (PTBS) sein. Diese kann sich entwickeln, nachdem eine Person einem extrem bedrohlichen oder schrecklichen Ereignis oder einer Folge solcher Ereignisse ausgesetzt war [ 4 ]. Eine PTBS geht mit einer Dysregulation in stressverarbeitenden Hirnregionen wie der Amygdala, dem Hippocampus und dem präfrontalen Kortex einher. Ein Wiedererleben kann über eine oder mehrere Sinnesmodalitäten erfolgen und wird typischerweise von starken Emotionen, insbesondere Angst oder Entsetzen, und starken körperlichen Empfindungen begleitet [ 4 ]. Trigger im Rahmen einer PTBS können folgende Symptome auslösen: Somatische Reaktionen: Herzrasen, Zittern, Schweißausbrüche, Atemnot Psychische Reaktionen: Angst, Panikattacken, Wut, Dissoziation, emotionale Taubheit Vermeidungsverhalten: Rückzug aus Situationen mit potenziellen Triggern (z.B. Menschenansammlungen, öffentliche Verkehrsmittel) Hypervigilanz: Dauerhafte Übererregung und „Lauschen auf Gefahr“ Zudem berichten Betroffene häufig über eine unerklärliche Reizbarkeit, Schlafprobleme sowie Konzentrationsstörungen. Als Trigger wird in der wissenschaftlichen Literatur zumeist über visuelle Wahrnehmungen berichtet, hier sollen in das Fachgebiet der HNO fallende akustische Trigger als mögliche Auslöser für eine, den Betroffenen meist nicht zuordnungsfähige Symptomatik, dargestellt werden. Akustische Trigger können bei einer PTBS eine schnelle, unbewusste Stressantwort initiieren – häufig ohne bewusste Erinnerungsassoziation. Besonders Reize, die dem Ursprungsereignis ähneln, wirken dabei potenziell retraumatisierend. Die Bedeutung akustischer Trigger liegt oft in ihrer assoziativen Verknüpfung mit dem ursprünglichen Trauma. Eine Flashback-Reaktion oder eine Dissoziation auslösen können in diesem Kontext laute, plötzliche Geräusche (Explosionen, Türknallen), menschliche Stimmen (Tonlage, Akzent, Stimmlautstärke), bestimmte Musikstücke oder Sprachfetzen. Publication History Received: 01 July 2025 Accepted after revision: 10 September 2025 Article published online: 19 September 2025 © 2025. Thieme. All rights reserved. Georg Thieme Verlag KG Oswald-Hesse-Straße 50, 70469 Stuttgart, Germany

**Решение:** -2 клинический случай / серия случаев

---

### 584 · R0707

**Corrigendum: A longitudinal investigation of quality of life and negative emotions in misophonia.**

2023 · Frontiers in neuroscience · article, other literature type, published erratum · eng · https://doi.org/10.3389/fnins.2023.1266908

In the published article, there was an error. In the discussion the word 'greater' appears when it should read 'less'. This sentence previously stated: "[Greater role limitations due to emotional problems were predicted by greater avoidance of triggers, a stronger emotional response to the trigger, and perceptions of more impact on participation in life.]"The corrected sentence appears below: "[Greater role limitations due to emotional problems were predicted by less avoidance of triggers, a stronger emotional response to the trigger, and perceptions of more impact on participation in life.]"The authors apologize for this error and state that this does not change the scientific conclusions of the article in any way. The original article has been updated.

**Решение:** -7 erratum / correction

---

### 585 · R0193

**Interdisciplinary Management of Misophonia in Adolescents and Young Adults: A Systematic Review**

2026 · International Journal of Allied Medical Sciences and Clinical Research · article, journalarticle, review · en · https://doi.org/10.61096/ijamscr.v14.iss2.2026.1093-1111

Misophonia is a condition defined by intense, disproportionate emotional and physiological reactivity to specific auditory triggers and remains one of the most undercharacterized sensory-based conditions affecting youth and young adults globally. This systematic review synthesises evidence from 21 studies (15 case reports, three case series, one single-case experimental design, one non-randomized controlled trial, and one randomized controlled trial) published between 2013 and 2025 to evaluate the efficacy, feasibility, and safety of interventions targeting misophonia in individuals aged 10-35 years. Four databases were searched, namely, PubMed, ScienceDirect, ResearchGate and, Google Scholar for studies published between 2010 and 2025 using a structured Boolean strategy. Study quality was appraised using Joanna Briggs Institute (JBI) tools appropriate for each design. The reviewed literature showed a gradual yet clear trend that shifts from mostly anecdotal, single-case reports towards organised, replicable intervention methods. Cognitive Behavioral Therapy (CBT), especially family-adapted variants, became the most widely used form of treatment, whereas pharmacological and audiological approaches were primarily used as supplementary rather than main treatments. The available body of evidence is still limited. This review maps the existing intervention landscape for misophonia in adolescents and young adults, identifies key developmental and methodological considerations, and highlights directions for future research.

**Решение:** -1 обзор / комментарий / письмо

---

### 586 · R1417

**Decreased sound tolerance: hyperacusis, misophonia, diplacousis, and polyacousis.**

2015 · Handbook of clinical neurology · article, journal article, review · eng · https://doi.org/10.1016/b978-0-444-62630-1.00021-4

Definitions, potential mechanisms, and treatments for decreased sound tolerance, hyperacusis, misophonia, and diplacousis are presented with an emphasis on the associated physiologic and neurophysiological processes and principles. A distinction is made between subjects who experience these conditions versus patients who suffer from them. The role of the limbic and autonomic nervous systems and other brain systems involved in cases of bothersome decreased sound tolerance is stressed. The neurophysiological model of tinnitus is outlined with respect to how it may contribute to our understanding of these phenomena and their treatment.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 587 · R1242

**Misophonia: A scoping review of research.**

2019 · Journal of clinical psychology · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1002/jclp.22771

Abstract Objective To scope the literature describing misophonia populations, management, and research opportunities. Method Literature searches for research studies describing patients diagnosed with misophonia, defining a patient profile, or outlining development or testing of an intervention for misophonia. A data extraction form was developed and piloted before data from each article were independently charted by two researchers. Researchers then agreed on a final data set for each article. Results Thirty‐one records were included. The misophonia population was described in terms of onset age, triggers, reaction, coping strategies, and comorbid conditions. We identified nine outcome measures. Case studies on treatments included cognitive behavioral therapy, counterconditioning, mindfulness and acceptance, dialectical behavioral therapy, and pharmaceuticals. Future research priorities identified included clarifying the phenomenology and prevalence of misophonia, and randomized controlled trials of treatments. Conclusion Misophonia is under‐researched but there are strong foundations for future research to finalize diagnostic criteria, validate outcome measures, and trial treatments.

**Решение:** -1 обзор / комментарий / письмо

---

### 588 · R0598

**Anti-suicidal effects of IV ketamine in a real-world setting.**

2024 · Psychiatry research · journal article · eng · https://doi.org/10.1016/j.psychres.2023.115604

The current study evaluated the effectiveness of intravenous ketamine treatment for suicidality in a community-based clinical sample of 295 outpatients (mean age= 40.37; 58.6 % male). We conducted growth mixture modeling to estimate latent classes of changes in symptoms of suicidality measured by the Concise Health Risk Tracking - Self-Report (CHRT-SR) across five infusions in a two-week course of treatment. Best-fit indices indicated three trajectory groups demonstrating non-linear, quadratic changes in CHRT-SR scores during ketamine treatment. The largest group of patients (n= 170, 57.6 %) had moderate CHRT-SR scores at baseline and showed gradual improvement during treatment. The other two groups of patients had severe CHRT-SR scores at baseline and diverged into one group with no improvement throughout treatment (n = 63, 21 %) and one group with rapid improvement (n = 62, 21 %). Of the clinical and demographic variables available and tested, only higher scores pertaining to active thoughts of death and/or plan were found to predict which of the patients with severe CHRT-SR scores at baseline would not benefit from treatment. The present study provides an important contribution to the knowledge of ketamine's effects on symptoms related to suicide over time. providing support for the possible effectiveness of ketamine in a proportion of patients.

**Решение:** -6 не про мизофонию

---

### 589 · R0401

**Compreensão e empatia fazem diferença na vida de quem vive com misofonia: como lidar?**

2025

A misofonia é uma condição ainda pouco conhecida, mas que pode afetar de forma significativa a vida das crianças, interferindo em seu bem-estar emocional, social e escolar. Caracteriza-se por uma reação intensa e desproporcional a determinados sons cotidianos, como mastigar, respirar, digitar ou bater de caneta. Essas situações podem gerar sentimentos de irritação, ansiedade ou até mesmo sofrimento, prejudicando a convivência familiar e a interação com colegas.Este folder tem como objetivo informar, orientar e sensibilizar pais, professores, profissionais de saúde e cuidadores sobre a misofonia em crianças. Aqui, você encontrará explicações claras sobre o que é a condição, seus sinais de alerta, impactos no desenvolvimento infantil, além de estratégias de acolhimento e manejo.Com informação de qualidade e cuidado humanizado, é possível oferecer apoio e promover uma melhor qualidade de vida para a criança, fortalecendo vínculos e favorecendo seu crescimento saudável

**Решение:** -1 обзор литературы / концептуальная статья

---

### 590 · R0216

**Trigger Sound Suppression for Misophonia**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.36351

Misophonia, a disorder of decreased tolerance to specific sounds, affects 5-20% of the population, yet sufferers have no good options: therapy helps a minority, and earplugs or noise cancellation silence everything. We present a study for neural trigger sound suppression for misophonia, selectively removing trigger sounds. We curate a dataset covering the 10 most common trigger classes. Using streaming dual-path networks operating on 6 ms audio chunks, we explore both one-hot and multi-hot-conditioned models that suppress 1-3 triggers from the acoustic scene. We validate our model outputs in a listening study with 30 adults with clinically elevated misophonia impairment. Participants reported significantly lower distress and arousal, and improved valence, for suppressed audio.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 591 · R0396

**From Misophonia Through Puberphonia: Window Toward Gender Dysphoria in Autism?**

2025 · Autism research : official journal of the International Society for Autism Research · article, journal article, review · eng · https://doi.org/10.1002/aur.70092

ABSTRACT Autism is characterized by distinct patterns of social communication, interests, and behaviors. Gender incongruence involves a mismatch between one's experienced and assigned gender, often accompanied by significant distress (i.e., gender dysphoria). Recent studies revealed that autistic individuals report gender dysphoria more frequently than the general population and are overrepresented in gender clinic settings. Autistic individuals also report hypersensitivity to certain sensory stimuli, which can elicit distress. When this distress is triggered by certain auditory stimuli (e.g., one's or others' biological sounds such as chewing or swallowing) it is categorized as misophonia. Misophonia appears to be highly prevalent in autism. We propose that a lesser‐studied phenomenon, puberphonia, could exemplify an attempt to reduce the distress elicited by misophonia in a certain category of individuals. Puberphonia is characterized by an unusually high‐pitched voice, predominantly in teenage boys and men, that can occur in the absence of identifiable physical causes. The psychogenic aspects of puberphonia are just beginning to be explored. We hereby propose an exploratory direction, suggesting that puberphonia may be an individual's attempt at diminishing a distressing auditory stimulus (misophonia) due to their deepening voice. This, in turn, may be an indicator of unrecognized gender dysphoria. Given that voice pitch has also been reported to be higher in autistic males compared to controls, we further ask whether autism is more prevalent among cases of psychogenic puberphonia. Finally, we wish to draw attention to the need for research on the epidemiology and overlap of puberphonia, gender dysphoria, misophonia, and autism.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 592 · R0020

**Association Between Hyperacusis and Tinnitus: Analysis of Prevalence and Impact on Daily Functioning.**

2026 · Audiology research · journal article, journalarticle, article · eng · https://doi.org/10.3390/audiolres16050126

Background: Hyperacusis is a common, but often underrecognized comorbidity in patients with chronic subjective tinnitus. Reduced sound tolerance is associated with a greater tinnitus-related burden, impaired communication, reduced social participation, and poorer daily functioning. However, published data regarding its prevalence and clinical impact remain limited and inconsistent. Objectives: To determine the prevalence of hyperacusis in patients with chronic subjective tinnitus and to assess its association with tinnitus-related handicap, uncomfortable loudness levels, and degree of hearing loss and daily functioning. Methods: This cross-sectional study included 194 patients aged 21–85 years with chronic subjective tinnitus. Hyperacusis was assessed using a structured clinical interview that included questions on decreased sound tolerance and sound-induced ear pain and uncomfortable loudness level measurements (ULLs). Patients were categorized into two groups: tinnitus with hyperacusis (T + H; n = 32) and tinnitus without hyperacusis (T; n = 162). The impact of tinnitus on daily functioning was evaluated using a standardized and clinically validated questionnaire—the Tinnitus Handicap Inventory (THI). Data were analyzed using appropriate parametric and nonparametric statistical tests. Results: Hyperacusis was identified in 32 of 194 patients with chronic tinnitus (16.5%). Patients with tinnitus and hyperacusis (T + H) had significantly higher THI scores than those with isolated tinnitus, indicating greater tinnitus-related handicap (76.3 vs. 41.9; p &lt; 0.001). Patients with hyperacusis also demonstrated significantly lower ULL values than those without hyperacusis (p &lt; 0.001). Conclusions: Although the reported prevalence of hyperacusis among patients with tinnitus varies across the literature, our findings indicate that hyperacusis is a common comorbidity associated with significantly greater tinnitus-related handicap. Routine assessment of hyperacusis, including ULL measurements, should be incorporated into the clinical evaluation of patients with tinnitus to facilitate comprehensive diagnosis and optimize management. These findings highlight the importance of systematic assessment of hyperacusis in patients with tinnitus in routine audiological practice.</jats:p

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 593 · R1110

**Commentary: The construct validity of ‘camouflaging’ in autism: psychometric considerations and recommendations for future research ‐ reflection on Lai et al. (2020)**

2021 · Journal of Child Psychology and Psychiatry · article · eng · https://doi.org/10.1111/jcpp.13468

Research on the construct of ‘camouflaging’ in autism and its sociodemographic/clinical correlates has far outpaced the work being done to establish the construct validity of camouflaging and its distinction from other similar constructs. The imprecision with which camouflaging is defined and measured has serious implications for future research on this topic, and unless additional effort is made to produce reliable and valid measurements of this construct, researchers will not be able to meaningfully assess important questions such as whether the effort of camouflaging one's behavior contributes to increased mental health difficulties. By reviewing the psychometric strengths and weaknesses of various operationalizations of camouflaging, this commentary highlights a pressing need for further measure validation in this area. Specific methodological guidance is provided for researchers interested in rigorously testing the validity of putative camouflaging measures.

**Решение:** -6 не про мизофонию

---

### 594 · R1193

**Concussion Management Guidelines Neglect Auditory Symptoms**

2020 · Clinical Journal of Sport Medicine · editorial · en · https://doi.org/10.1097/jsm.0000000000000874

BACKGROUND Evidence-based guidelines are essential to promote and provide best practices. They present a logical framework for clinicians to find established criteria for diagnostic purposes and treatment recommendations. Unfortunately, many published guidelines for the assessment and management of patients with traumatic brain injury (TBI) or concussion fail to synthesize current knowledge pertaining to the occurrence of auditory symptoms at the time of injury or the recovery timeline for these symptoms.1–6 The underlying mechanisms for many auditory symptoms after head injury are poorly understood, which complicates classifying these symptoms as either “post-TBI related” or in the case of mild TBI (mTBI), “postconcussive related.” Identifying auditory symptoms that manifest secondary to head injury will aid in the assessment and treatment of these conditions. Most importantly, and the main issue addressed in this editorial, is that there are a number of auditory deficits besides vestibular injury that occur secondary to head injury, and, yet, often go unnoticed by health care professionals. AUDITORY SYMPTOMS The primary auditory symptoms associated with head injury are tinnitus, noise sensitivity, and difficulty understanding speech in complex listening environments (ie, auditory processing deficits.7 There is a growing body of literature reporting these auditory symptoms following sports-related head injuries, blast injuries, falls, and motor vehicle accidents.7–14 Despite many attempts to create symptom profiles and subtypes to assist in the management of concussion patients, a clinical consensus on this subject does not currently exist.15 Although many concussion subtypes include a vestibular category, rarely do they include an auditory category. Often, meta-analytic approaches are used to identify subtypes, but this effort is hindered by poor documentation of auditory symptoms in most studies. Emphasizing this point Lumba-Brown,16 acknowledge an auditory subtype of concussion exists but is not commonly assessed. Because of the heterogeneity of concussion symptom profiles, persistence of auditory symptoms post-head injury beyond expected physiologic recovery thresholds (ie, 3 months) could refine classification processes of TBI and concussion subtypes. Taking this into consideration, screening for common auditory symptoms as part of the clinical interview might greatly assist with the clinical management of TBI and concussion patients (Table 1). TABLE 1. - Common Auditory Symptoms Associated With Concussion Defined and Suggested Screening Questions Auditory Symptoms Definition Screening Question Tinnitus Perception of sound in the absence of an external [acoustic] source. Do you experience ringing in the ears (tinnitus) that lasts for at least 5 min? Noise sensitivity General intolerance to everyday sounds that encompasses a range of psychological attributes that contribute to the degree an individual is reactive to noise. Do you have a problem tolerating sounds because they often seem too loud or bother you for other reasons? Hearing difficulty Trouble understanding speech or other sounds in quiet or noisy environments. Do you have any difficulties understanding speech or other sounds? Do you feel like you have more difficulties hearing in noise compared with others? TREATMENT CONSIDERATIONS Screening patients for tinnitus, noise sensitivity, and hearing difficulty after head injury will aid the clinician in providing targeted rehabilitation to best meet the patient's needs. When patients screen positive for one or more of these issues, it is important to determine if the auditory symptom(s) occurred pre-head or post-head injury, and for any symptoms that were preoccurring, to ask if they became exacerbated. Referral to an audiologist or otologist is recommended for these patients as these healthcare professionals are uniquely trained to diagnose and treat auditory conditions. For example, hearing loss is not uncommon after closed head injury17,18 and both structural and functional changes that occur in the peripheral and central auditory system post-head injury contribute to many of the auditory symptoms reported by patients. In these instances, provision of hearing aids may improve patients' symptoms and ability to communicate. However, many patients will experience symptoms in the absence of hearing loss.8,19 For these patients, additional testing may be recommended to aid with a differential diagnosis, such as tests of speech-in-noise comprehension or other tests of auditory processing.20 Many of the auditory symptoms reported after head injury have subtypes and identifying these features can help to guide treatment protocols. For example, when tinnitus occurs secondary to head injury, the perceptional attributes (ie, loudness, pitch, and timbre) may change after head and neck maneuvers, forceful muscle contractions, or jaw movements. This clinical phenotype is classified as somatosensory tinnitus.21,22 Patients with somatosensory tinnitus often have an underlying biomechanical deficit, such as temporomandibular joint dysfunction, or injury to their cervical spine, that may trigger or exacerbate the tinnitus. In these instances, patients may benefit from individualized physiotherapy to address both the tinnitus and underlying musculoskeletal issue simultaneously.23–25 Among patients describing decreased sound tolerance, which includes noise sensitivity and hyperacusis, it is important to differentiate if the primary complaint is related to the “loudness” of everyday sounds, suggestive of hyperacusis, or a broader issue involving multiple factors that contribute to being overwhelmed by all the “noise.” Hyperacusis is an intolerance of sounds at low-to-moderate intensity levels that would be considered tolerable by most people and may also include physical discomfort, stress, and anxiety.26 Noise sensitivity addresses an individual's reactivity to noise, theorized to be a manifestation of a state of hyperarousal resulting in negative attitudes to sound, including annoyance and feelings of being overwhelmed.27 However, because distinguishing auditory signals such as speech from background noise is a particularly challenging task for the central auditory system, patients may also endorse symptoms of noise sensitivity stemming from poorer auditory functioning in environments with competing noise sources after head injury.20 Thus, asking the patient to give examples is necessary to distinguish hyperacusis from noise sensitivity and hearing difficulties related to background noise. There are multiple types of decreased sound tolerance conditions, and they are not mutually exclusive.28 Patients with noise sensitivity should consistently use hearing protection when exposed to loud sounds (eg, band practice and concerts), but using hearing protection in quiet environments (eg, classrooms) can result in the auditory system becoming more sensitive, not less.29 In some instances, it may be appropriate for patients to initially use hearing protection sparingly in quiet environments and slowly reintroduce listening to sounds at tolerable levels. When patients reacclimate to environmental sounds in this fashion, it is essential to monitor that using hearing protection in this way does not exacerbate their auditory symptoms. SUMMARY Because of the complex clinical presentation of patients with head injuries, auditory symptoms may not receive equivalent attention as other clinical signs and symptoms. This fact, along with the lack of familiarity regarding these auditory symptoms, results in many missed opportunities to delineate the type and nature of auditory symptoms relevant for treatment triage. In addition, because patients may find it difficult to articulate their complaints and experiences, many symptoms and their negative consequences often go unaddressed.30 Furthermore, a lack of consistent terminology used to describe auditory symptoms associated with head injury (eg, hearing difficulty, auditory processing deficits, noise sensitivity, phonophobia, and hyperacusis) contributes to this problem. Because of various terms being used in different disciplines and the lack of a gold standard to diagnose many of these conditions, it is challenging to estimate the prevalence of auditory symptoms in this patient population. In contrast to the sports medicine literature, there are many accounts of auditory symptoms documented for military service–related head injuries, most likely because of the inherent co-occurring noise exposure with those events.31 This is also evident in the joint Department of Veterans Affairs and Department of Defense32 clinical practice guidelines for the management of mTBI, which uses an algorithm-based stepped-care approach to derive appropriate assessment and management plans for each patient. Auditory symptoms are listed in the category of physical symptoms post-head injury, but specific management recommendations are not made because of a lack of published scientific findings. Therefore, to provide the necessary evidence to inform clinical care decision making, research is critically needed to address the auditory symptoms and deficits that are caused or exacerbated by head injury. Although the mechanism of injury might vary for mTBI associated with blasts compared with sport-related injuries, both types of exposures result in auditory symptom reporting.33–35 It is noteworthy that 92% of a cohort with nonblast mTBI (eg, motor vehicle accident, falls, sports related, etc.) endorsed auditory symptoms.33 In comparison, an ongoing chart review of over 1000 patients seen at the Oregon Health & Science University Concussion Clinic has similarly revealed that over 50% of those diagnosed with concussion endorsed one or more auditory complaint at their intake appointment. These data suggest auditory symptoms occur secondary to a variety of head injuries and are not particular to a specific mechanism of injury. This work highlights the need to develop an auditory subtype to complement the other more established subtypes mentioned in clinical practice guidelines to date. It is essential to increase the research and clinical efforts to address the taxonomy of auditory symptoms associated with head injury, as well as the temporal recovery gradient of specific symptoms or clusters of symptoms, and how auditory symptoms may or may not relate to other injury/individual characteristics. Research is needed to better isolate the mechanism of injury that gives rise to auditory symptoms associated with head injuries. Identifying the separate peripheral versus central auditory deficits that result in these symptoms will also help to explain patient-specific characteristics and risk factors for these conditions. In addition, it is likely a combination of peripheral, subcortical, and cortical maladaptive changes that result in the persistence of these auditory symptoms months after the head injury. Addressing these unanswered questions will help fill the gaps in our knowledge of the etiology, clinical manifestation, and associated risk factors for post-head injury auditory symptoms. In addition to our goal of highlighting and characterizing the auditory consequences associated with head injury, immediate next steps are to (1) further develop a model-based auditory subtype of concussion and (2) involve the scientific and clinical community to gain consensus on how this information will assist with patient assessment and recovery from injury. These efforts are necessary to inform best practices and update clinical practice guidelines for the management of patients with TBI and concussion.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 595 · R0564

**Tinnitus Retraining Therapy**

2024 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-3-031-35647-6_47

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 596 · R1178

**A review of human reactions to environmental sounds**

2020 · Srpski medicinski casopis Lekarske komore · article, other literature type, review · en · https://doi.org/10.5937/smclk2001067p

Soundscape is defined as the entire acoustic environment and the human responses to it. This review summarizes different human reactions to sound exposure, their development, prevalence, symptoms, comorbidities, methods for their assessment, and possible origins. The interpretation of sounds from the environment depends, not only on the characteristics of the sound itself, but also on the characteristics of the listener, their judgments, preferences, motivations, and emotional reactions to the sound or its source. Typical sound-related reactions are presented from two standpoints: population reactions, from the community perspective, and individual reactions, from the clinical perspective. Noise annoyance is a specific, unique, and typical psychological and physiological reaction to noise, which is assessed from the community perspective. Noise sensitivity, a stable personality trait, is at the basis of noise annoyance. Both noise annoyance and noise sensitivity play important roles in the development of other noise-related health disturbances. From the clinical perspective, hyperacusis and misophonia are the most distinctive individual responses to specific sounds. They may become so pronounced that they disturb one's physical and mental health, behavior, and functioning. Human reactions to sounds in the environment are widespread and well-investigated. This review goes beyond merely defining terminology in the domain of psychoacoustics; it may help health professionals understand human reactions to sound better. Further studies need to be directed towards developing methods for alleviating or treating the described reactions, but also towards creating a more pleasant acoustic environment for the purpose of protecting public health.

**Решение:** -1 обзор / комментарий / письмо

---

### 597 · R1264

**Misophonia Awareness**

2018 · ASHA Leader · article · en · https://doi.org/10.1044/leader.in2.23092018.4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 профессиональное издание (ASHA Leader)

---

### 598 · R1225

**Mizofoni tedavisinde yeni bir tedavi seçeneği olarak EMDR'nin etkinliği: Olgu sunumu**

2019 · Unpublished · conference object, text/poster · eo · https://doi.org/10.13140/rg.2.2.11857.68965

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 599 · R0300

**Hyperacusis and Misophonia Treatment**

2025 · WORLD SCIENTIFIC eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1142/9789819807345_0012

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глава книги / справочник

---

### 600 · R0937

**Tech companies liable for illegal wildlife trade**

2022 · Science · article · en · https://doi.org/10.1126/science.ade0843

1. The aim of this report is to review whether A-Weighting accurately represents the hearing of the whole UK population, to explore the consequences if it does not, and to make recommendations for future research to address the problems identified. 2. The approach taken was to first research the construction of A-Weighting from its root in early research on loudness perception and the development of the equal loudness contours. We then identified three groups of interest, who may not be well represented by A-Weighting. These are people with age-related hearing loss, neurodivergent people, and noise-sensitive people. These groups were chosen because they each represent a different kind of hearing difference, and they are all a substantial size. 3. A detailed literature review was conducted to examine the available evidence of hearing differences in the three groups and to discuss how these relate to A-Weighting and its uses. We reviewed 540 papers and cite 182 in this report. This dataset was then analysed to identify significant research gaps and suggest future research to fill them. 4. A-Weighting was found to be a significant way in which the assumption of normal hearing is embedded in a very wide range of acoustic assessment and legislation. This is because A-Weighting was developed from the equal loudness contours, and the contours are produced from measurements on a relatively small sample of otologically normal people – 18-25-year-olds with no hearing impairment. This is important because A-Weighting extends far beyond its original use to convert sound levels into loudness estimates and is now found in most assessments and control of noise worldwide, from product design to environmental noise. 5. People with age-related hearing loss represent 7.9% of the UK population. Age-related hearing loss is caused by degradation of the hair cells’ transducer mechanism in the inner ear. Among other effects, this typically causes problems with masking, where it becomes harder to pick a target speech sound out of a noisy background. Because background noise is usually quantified using A-Weighting, and A-Weighting models normal hearing, this may mean that the enhanced need for reduced background interference is often not met for this group. 6. Neurodivergent people (who include autistic people, those with attention deficit hyperactivity disorder (ADHD), dyslexia, dyspraxia, dysgraphia, dyscalculia, and Tourette’s) make up about 10% of the UK population. Evidence was found of auditory processing differences for autistic people, and for people with ADHD and dyslexia. The auditory processing differences occur at a low level in the brain and can result in difficulty separating out sound signals, especially when trying to listen to someone speak against a background of competing speech. It is likely that enhanced background noise targets would improve the experience of this group, but it is currently difficult to translate the laboratory findings on auditory processing into new noise assessment methods. There is too little evidence for people with dyspraxia, dyscalculia, dysgraphia and Tourette’s to base a conclusion on. 7. People who are noise-sensitive represent 17-50% of the population. In this report, this group included people who are more sensitive to general noise, people with misophonia and people with hyperacusis. For this group, the widespread use of A-Weighted sound level to predict noise annoyance is likely to significantly underpredict their heightened response. Hyperacusis is very common in autistic people, and it is particularly likely that A-Weighted levels do not represent the experience of this group. 8. It is not possible to simply adapt the A-Weighting curve to better fit any of the groups at this time. Partly this is because of lack of data on how to adjust, but mostly it is because most of the differences in sound perception are not equivalent to a simple transformation in loudness. The exception is for people with hyperacusis, where more detailed data on their loudness responses might enable a new weighting to be derived. 9. The overarching research gap identified is a lack of translational research. There is a need for research that builds on existing laboratory studies of hearing differences and translates them into guidelines for practitioners to assess sound and design spaces suitable for people with atypical hearing. 10. We also identify nine specific research gaps and projects to address them: a. Acoustic guidelines for spaces for people with a hearing impairment b. Acoustic design guidelines for people with auditory processing problems c. Accurate estimate of the numbers of noise sensitive people in the UK d. Loudness for people with age-related hearing impairment e. Loudness functions for autistic people with hyperacusis f. Equal loudness contours for autistic people with hyperacusis g. Demographic factors as a modulating effect on neurodivergent hearing h. Loudness functions for people with hyperacusis i. Psychoacoustic factors in misophonia Of these, we suggest that the first three are the most important. 11. This report represents an initial exercise in a much larger project for acoustics to respond to the aural diversity movement – the idea that a wide range of different kinds of hearing differences exist, in contrast to the assumed binary division of normal hearing and impaired hearing. This project could be repeated with other groups of people, such as those with noise-induced hearing loss, Meniere’s disease, or many other conditions.

**Решение:** -1 обзор литературы / концептуальная статья
