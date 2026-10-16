# Проверка с метками ИИ, часть 1

Записи 1–150 из 600, с меткой ИИ над строкой решения. Согласны с ИИ — поставьте `=`; не согласны — свой код (`+`, `?` или `-`, причина и заметка не нужны). Решаете вы.

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

### 1 · R0001

**Let misophonia be heard:Advancing recognition, diagnostics and treatment of misophonia in youth**

2027 · other · en · https://core.ac.uk/download/689077029.pdf

Misophonia is a recently identified disorder of decreased tolerance to specific sounds or associated stimuli (so-called “triggers”). Triggers primarily include human-made sounds such as eating or breathing. Confrontation with triggers elicits intense emotional, behavioral and physiological responses that are difficult to control. Misophonia typically develops during childhood and has considerable consequences for the daily lives of children and families. Often, children can no longer eat, sleep or travel by car together with their family, and they experience problems at school and with friends. There is a great need for adequate diagnostics and evidence-based treatment. The main aim of this thesis is to improve care for children, adolescents and families suffering from misophonia. We present the first controlled study worldwide investigating misophonia in 95 children and adolescents (aged 8-18). We: 1) assessed clinical characteristics, psychiatric comorbidity and quality of life; 2) designed and validated two child-specific questionnaires for screening and severity assessment of misophonia in children and adolescents; 3) performed a randomized controlled trial (RCT) investigating combined cognitive behavioral and psychomotor group therapy (CBT+PMT); 4) performed a cost-of-illness study investigating the financial burden of misophonia on families and society. This thesis underlines the importance of classifying misophonia as a discrete disorder. By providing two validated questionnaires and the first evidence-based treatment, this thesis paves the way for improved recognition, diagnostics and treatment of misophonia in youth

**ИИ:** ? · другое · Thesis mainly on youth with misophonia, but its controlled design and screening-questionnaire validation may include unselected controls or community samples.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 2 · R0002

**Correction to: Resolving competition in auditory cortex: effects of emotional content and misophonia sensitivity.**

2026 · Cerebral cortex (New York, N.Y. : 1991) · published erratum, erratum · eng · https://doi.org/10.1093/cercor/bhag129

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Erratum without data. The parent article measured misophonia sensitivity in an auditory cortex study, and its sample may be unselected, so check it.

**Решение:** -7 erratum / correction

---

### 3 · R0008

**Resolving competition in auditory cortex: effects of emotional content and misophonia sensitivity.**

2026 · Cerebral cortex (New York, N.Y. : 1991) · article, journal article, journalarticle · eng · https://doi.org/10.1093/cercor/bhag021

Abstract How the human auditory cortex prioritizes relevant information amid concurrent sounds has been a long-standing question in auditory cognitive neuroscience. The present study used auditory steady-state responses to tag the electrocortical response to a tone embedded in concurrent naturalistic sounds, addressing methodological challenges with overlapping auditory streams. Participants endorsing low (high misophonia symptoms) or high misophonia symptoms—a condition with decreased tolerance to specific, typically orofacial, sounds—were recruited. Sounds varied in emotional valence (pleasant, neutral, unpleasant) to investigate how emotional content modulates attentional competition. Orofacial sounds were also included to evaluate how attentional biases are affected by inter-individual sensitivity toward a specific sound category. Affective ratings, alpha-band changes, and pupil dilation were also assessed. Hypothetical models of competition were tested, revealing a facilitation trend in the auditory steady-state responses amplitude when accompanied by pleasant and unpleasant, compared to neutral sounds, regardless of misophonia symptoms. However, auditory steady-state responses was selectively reduced in the high misophonia symptoms but not the high misophonia symptoms group when accompanied by orofacial sounds. Analyses of alpha-band, pupil, and rating data showed that the groups differed primarily in their response to pleasant sounds and orofacial sounds, with the high misophonia symptoms group exhibiting a stronger response to orofacial sounds than the high misophonia symptoms group.

**ИИ:** ? · скрининг пула · EEG study of low vs high misophonia symptom groups; groups were likely picked by screening an unselected (e.g., student) pool, but the abstract doesn't say.

**Решение:** =

---

### 4 · R0010

**An investigation into the relationship between misophonia awareness and perceived stress levels among occupational therapy and audiology students**

2026 · The Egyptian Journal of Otolaryngology · article, google scholar result · en · https://doi.org/10.1186/s43163-026-01163-8

Abstract Background and aims Misophonia is a sound intolerance disorder characterised by an excessive negative reaction to specific sounds. A key feature of misophonia is the strong emotional reactions an individual develops towards specific triggering sounds. These reactions typically manifest as sudden anger, irritation, anxiety, or intense discomfort. This study aims to determine the level of misophonia awareness among occupational therapy and audiology students and establish the relationship between misophonia symptom severity and perceived stress levels. The study also aims to determine the correlation between misophonia symptoms and awareness of the condition. Methods A total of 196 adult university students completed a demographic information form designed to assess their knowledge of misophonia, as well as the Misophonia Questionnaire (MQ) and the Perceived Stress Scale (PSS). Analysis of the internal consistency (Cronbach’s alpha) coefficients and descriptive statistics of the scales and their sub-dimensions revealed that the internal consistency coefficients of the MQ subscales (0.752–0.829) and the PSS Cronbach’s alpha value (0.709) were acceptable, indicating good internal consistency. Results Examining the responses to the scales according to stress status and the module studied revealed statistically significant differences across all parameters ( p &lt; 0.05). The reason why occupational therapy students scored higher on the MQ and PSS may be due to their heightened sensory sensitivity, stress levels or awareness. This study revealed a relationship between the severity of misophonia symptoms, perceived stress levels, and demographic factors, psychological support status, and sensory awareness in university students. The findings suggest that misophonia is a multidimensional condition interacting with emotional regulation, stress response and adaptation to environmental stimuli, rather than merely an auditory sensitivity. While no significant differences were observed in terms of age, factors such as gender, department, and family history produced distinct differences in some sub-scales. The high stress scores of participants not receiving psychological support highlight the need for awareness of, and strategies to manage, misophonia. Conclusions Furthermore, the findings support the existing literature which suggests that misophonia symptoms become established at an early age and may become chronic in adulthood. These results emphasise the importance of considering not only the neurophysiological basis of misophonia, but also its psychosocial dimensions. They also suggest that a multidisciplinary approach could improve treatment outcomes.

**ИИ:** + · ненабранная выборка · 196 occupational therapy and audiology students, not recruited for misophonia, completed the Misophonia Questionnaire; full text may report how many met a case cutoff.

**Решение:** =

---

### 5 · R0011

**Family history of misophonia and co-occurring neuropsychiatric conditions**

2026 · medRxiv · article, preprint, review · und · https://doi.org/10.64898/2026.03.13.26347988

Abstract Objective To characterize the familial patterns of misophonia and other commonly co-occurring neuropsychiatric conditions. Methods We examined cross-sectional survey responses from 101 probands with misophonia and their biological parents enrolled in a genetics study. Results Probands had a mean age of 24.6 ± 11.6 years (8-64 years), were predominantly female (88%), and had high rates of co-occurring neuropsychiatric conditions, including anxiety (70%), depression (38%), ADHD (31%), and OCD (25%). Among probands, 39% had a first-degree relative with misophonia, and 48% had at least one any-degree relative with misophonia. In addition, many probands had at least one first-degree relative with anxiety (65%), depression (57%), ADHD (40%), OCD (20%), and autism (13%). Comparing rates of neuropsychiatric conditions reported by parents, mothers had significantly higher rates of misophonia (29% maternal vs. 9% paternal, p = 0.001) and anxiety (44% maternal vs. 26% paternal, p = 0.02) than fathers. Conclusion These findings provide new insight into the familial patterns of misophonia and co-occurring neuropsychiatric conditions. Future research on underlying genetic and environmental factors is needed to shed light on the observed shared predispositions for misophonia and other neuropsychiatric conditions in families.

**ИИ:** ? · другое · Probands were selected for misophonia, but the study reports misophonia rates in their biological parents, a family-risk sample. Eligibility is borderline.

**Решение:** + ненабранный опрос со шкалой мизофонии

---

### 6 · R0015

**SAVi-M: A Standardised Auditory-Visual Database to Investigate Affective Response to Trigger Events**

2026 · PsyArXiv · article, preprint · und · https://doi.org/10.31234/osf.io/kmv2e_v1

Objectives: This study presents a publicly available standardised set of auditory-visual stimuli specifically designed for misophonia research. This was done with the purpose of addressing some of the main limitations of current databases available, namely the lack of standardised, lab-curated, and ecologically valid auditory-visual databases.Method: The database is comprised of 250 videos categorised into six categories, according to the Sussex Misophonia Scale (SMS; Simner et al., 2024): 1) eating, 2) repetitive tapping, 3) rustling, 4) mouth/nose, 5) throat, and 6) neutral (non-triggers). Four non-professional actors (2 males and 2 females) were filmed preforming scripted main events (e.g., eating an apple). To gather further information regarding the emotional responses our database videos elicited, we conducted an online study where 96 participants (32 with misophonia, 31 with misophonia-misokinesia (combined), and 33 control participants) rated each database video on their arousal (emotional intensity), valence (pleasantness), and dominance (sense of control). Results: Participants with misophonia and those with both misophonia and misokinesia exhibited significantly higher arousal, lower valence, and reduced dominance compared to controls when attending to the database videos. These differences were most profound in the eating category. Examining pairwise correlations between the affective dimensions revealed across all groups that arousal was negatively correlated with both valence and dominance, while valence and dominance were positively correlated. Conclusion: The SAVi-M database provides researchers with a standardised, ecologically valid, and behaviourally rated set of auditory-visual stimuli. Using affective response ratings based on the Pleasure-Arousal-Dominance (PAD) model, the database offers a new approach of quantifying the behavioural/emotional response in misophonia. The SAVi-M database can be utilised to enhance exploration of misophonia from a multisensory approach.</p

**ИИ:** ? · выборка неясна · Online study with balanced misophonia, misokinesia and control groups. Unclear whether participants were recruited for misophonia or classified from a screened pool using the SMS.

**Решение:** =

---

### 7 · R0016

**Standardised Auditory-Visual Misophonia (SAVi-M) Database**

2026 · OSF Preprints (OSF Preprints) · preprint, project · en

The Standardised Auditory-Visual Misophonia (SAVi-M) Database contains 250 lab-curated standardised auditory-visual stimuli designed specifically for Misophonia research, all of which have been rated on arousal, valence (pleasure), and dominance. Further to the videos themselves this OSF project contains the ratings from the Online Rating Study and Participant Screening details.

**ИИ:** ? · выборка неясна · Stimulus database with an online rating study and participant screening details; the screening may report misophonia rates in an unselected sample.

**Решение:** =

---

### 8 · R0019

**Hyperacusis impact questionnaire: translation and psychometric evaluation of the Persian version.**

2026 · International journal of audiology · journal article · eng · https://doi.org/10.1080/14992027.2025.2549463

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Hyperacusis questionnaire validation with no abstract; it may have used a misophonia measure for comparison, so the full text is needed.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 9 · R0022

**Navigating Misophonia at University: A mixed-methods exploration of how Misophonia impacts university experiences.**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/ztnx2

Misophonia is characterised by extreme distress responses to specific everyday sounds (e.g. chewing, sniffing), which can have a detrimental impact on daily functioning and mental health (Dibb &amp; Golding, 2022; Swedo et al., 2022). Recent studies have linked Misophonia to suicidal ideation and attempts, highlighting the urgency of Misophonia research and clinical recognition (Alekri &amp; Al Saif, 2019; Siepsiak et al., 2022; Simner &amp; Rinaldi, 2023). Despite a growing consensusthat Misophonia has an overall negative impact in individuals’ lives, existing research has largely provided a generalised understanding of the condition, lacking in-depth investigation into specific life domains (Guzick et al., 2023). Educational settings provide relevant contexts in which to study Misophonia, as they are prone to frequent trigger sounds (Robinson &amp; Zdravkova, 2023). Education is also an influential development period, where academic engagement, concentration and social integration are imperative to overall success and wellbeing (Hunter, 2006; Morgan, 2012). However, existing literature indicates that Misophonia is associated with increased avoidance behaviours, as well as difficulties in concentration and socialisation (Guzick et al., 2025; Hansen et al., 2024). These findings align with theoretical formulations of the condition, which position Misophonia responses as heightened neurophysiological reactivity to triggers, often referred to as a “fight-or-flight” response (Jastreboff &amp; Jastreboff, 2023). This response is associated with disrupted cognitive and emotional functioning, which could impair an individual’s ability to engage effectively in learning environments (Babmiri et al., 2018). Therefore, this research will conceptualise Misophonia within the neurophysiological framework. The study proposes that overall university experience is negatively impacted by consequences of Misophonia distress responses, specifically as these responses may cause a reduced ability to concentrate and engage within academic and social contexts. To the researcher’s knowledge, the present study will be the first to isolate and explore the impact of Misophonia on university experiences.

**ИИ:** ? · выборка неясна · Mixed-methods preregistration on university students; unclear whether the sample was unselected students screened for misophonia or people with misophonia.

**Решение:** -7 preregistration without data

---

### 10 · R0023

**OP-25 Misophonia, ObsessiveCompulsive Personality Traits, and Emotion Regulation in Individuals with Bipolar Disorder in Remission: A CaseControl Study**

2026 · Turkish Journal of Psychiatry · article, journalarticle, conference-abstract · en · https://doi.org/10.5080/61upk.ozt444

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · клиническая группа · Conference abstract, no abstract text; title shows misophonia measured in remitted bipolar patients and controls, neither recruited for misophonia.

**Решение:** =

---

### 11 · R0025

**Neural Tracking of Social Navigation in Autism Spectrum Disorder.**

2026 · Biological psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.biopsych.2025.08.018

BACKGROUND: As we navigate changing social landscapes, maintaining maps of interpersonal dynamics can help guide our choices. Autism spectrum disorder (ASD) is associated with social challenges that may affect the accumulation or application of social information. However, little is known about social cognitive mapping in autistic adults. METHODS: Herein, we investigated differences in social navigation among 122 adults with ASD, typical development (TD), and misophonia (MIS) (included as a clinical comparison group) using a social interaction task during functional magnetic resonance imaging. RESULTS: Compared with other groups, adults with ASD behaved socially distant from task characters. Nevertheless, the groups displayed comparable neural tracking of social distances in regions previously identified in nonclinical samples, including the posterior cingulate cortex (PCC), as well as the parahippocampal place area, where tracking uniquely related to cross-diagnostic social avoidance symptoms. In contrast, the ASD group showed distinctive hypoactivity in the temporal pole (TP) during social decisions, associated with smaller real-world social networks and reduced insight into their external symptoms. Additionally, while the TD and MIS groups showed functional decoupling between the TP and PCC during social decisions, this was not detected in ASD. CONCLUSIONS: Adults with ASD showed distinct behaviors and neural activity during deliberation in social interactions. However, brain systems supporting social mapping appear preserved across groups, consistent with previous findings, which have now been extended to a clinically diverse sample. These results highlight both shared and ASD-specific neural mechanisms of social navigation, thereby offering insight into potential neural differences in how social evidence guides choices in ASD.

**ИИ:** ? · другое · The misophonia group was recruited for misophonia, but the ASD and TD groups may have completed misophonia measures. Worth checking the full text.

**Решение:** =

---

### 12 · R0027

**Psychometric and Sound-Response Profiles in Decreased Sound Tolerance Conditions.**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/pwgzb

Hyperacusis and misophonia are Decreased Sound Tolerance (DST) conditions. Emerging research suggests that some people may experience misophonia and hyperacusis concurrently. However, previous studies have excluded hyperacusis from misophonia research, because the overlap between these conditions is unclear. This study aims to account for this gap, by replicating previous misophonia research (Andermane et al., 2023; Smees et al., 2025) and extending those methods to hyperacusis samples. This will ultimately improve understanding of how DST conditions differ, allowing researchers to use validated psychometrics confidently to assess misophonia and hyperacusis separately in research. The research is separated into two sections, the former assessing psychometrics of hyperacusis and misophonia, and the latter exploring sound-response profiles and acoustic properties to explore ways in which hyperacusis and misophonia manifest, both together and separately. This pre-registration will detail both sections of the project. As part of this study, questionnaires assessing hyperacusis and misophonia are administered, alongside demographic information including self-reported hyperacusis, misophonia, experience of hearing loss and tinnitus. A sound-response task is also presented, in which participants are asked to rate 16 descriptor words according to their experience to the sound (using a 0-100 slider bar). This will allow us to have a detailed analysis into psychometrics and sound-response profiles of Decreased Sound Tolerance, testing whether previous misophonia results are replicated, as well as attempts to assess hyperacusis samples using these methods.

**ИИ:** ? · выборка неясна · Pre-registration that measures misophonia in hyperacusis and possibly general samples; how participants are recruited is unclear, and it may report misophonia rates.

**Решение:** -7 preregistration without data

---

### 13 · R0031

**Misophonia symptom severity is linked to impaired flexibility and heightened rumination.**

2026 · British journal of psychology (London, England : 1953) · article, journal article, journalarticle · eng · https://doi.org/10.1111/bjop.70025

Abstract Misophonia is a disorder involving sensitivity to certain sounds and related stimuli. Here, we explore the relationship between misophonia and affective flexibility, which describes cognitive shifting abilities in the face of emotion‐evoking stimuli. The secondary aim of this study is to test the potential association between misophonia and cognitive flexibility, building upon findings from previous research. The third objective is to examine the relationship between misophonia and rumination. One hundred and forty participants completed the Memory and Affective Flexibility Task (MAFT), designed to assess affective flexibility, as well as a battery of self‐report measures to evaluate misophonia severity, cognitive flexibility, and rumination. Results suggested an inverse relationship between affective flexibility as measured by switch accuracy, but not reaction time, and misophonia severity. Cognitive flexibility was also inversely associated with misophonia severity, but was not attributed to task‐based affective flexibility, suggesting two independent constructs both involved in misophonia manifestation. Rumination associated positively with misophonia severity and inversely with cognitive flexibility, but not affective flexibility. Taken together, these findings highlight a unique cognitive profile of misophonia, characterized by rigidity at the psychological level through cognitive inflexibility and rumination, as well as at the executive function level in terms of affective switching difficulties.

**ИИ:** ? · выборка неясна · Misophonia severity was measured in 140 participants, but the abstract doesn't say how they were recruited; they may be an unselected sample.

**Решение:** =

---

### 14 · R0035

**Decreased Sound Tolerance in Older Adults: The Relationship Between Depression and Auditory Sensitivities**

2026 · kulak burun boğaz ve baş boyun cerrahisi dergisi · article, journalarticle, google scholar result · en · https://doi.org/10.24179/kbbbbc.2025-113232

ABS TRACT Objective:The aim of this study is to determine the prevalence of subtypes of decreased sound tolerance (DST) in older adults and examine their associations with depressive symptoms and auditory variables.Material and Methods: Following the audiological evaluations of the participants, symptoms of DST were assessed using the Decreased Sound Tolerance Scale-Screening (DSTS-S), depressive symptoms were evaluated using the Geriatric Depression Scale (GDS), and tinnitus complaints were measured using the Tinnitus Handicap Inventory.Results: Hyperacusis was the most commonly reported subtype of DST (62.7%), followed by phonophobia (46.3%) and misophonia (43.3%).No significant overall relationship was found between the GDS and DSTS-S scores.However, weak yet statistically significant positive correlations were identified between GDS scores and the pure tone average (r=0.257;p=0.036) as well as the speech recognition threshold (r=0.287;p=0.020) in the left ear.Participants reporting tinnitus complaints exhibited higher scores across all DSTS-S subscales.Conclusion: This study observed a notable prevalence of DSTS-S subtypes among older adults.The findings suggest significant associations between depressive symptoms and hearing thresholds, and individuals with a history of tinnitus may exhibit higher DSTS-S scores.Further advanced studies with larger sample sizes are needed to clarify the causality of these relationships.

**ИИ:** + · исследование распространённости · Reports misophonia prevalence (43.3%) in older adults, measured with the DSTS-S misophonia subscale; the sample wasn't recruited for misophonia.

**Решение:** =

---

### 15 · R0040

**Advances in assessing and addressing Decreased Sound Tolerance in Autism**

2026 · Unpublished · text/poster, article · https://doi.org/10.13140/rg.2.2.15523.41762

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Poster on decreased sound tolerance in autism with no abstract; it may have measured misophonia in an autism clinical group.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 16 · R0041

**More than Covering Ears: A Clinical Inventory for Characterizing Decreased Sound Tolerance (I-DST) in Autism**

2026 · The Open Journal of Occupational Therapy · article, journalarticle · en · https://doi.org/10.15453/2168-6408.2393

Background: Decreased sound tolerance (DST) is among the most common and distressing forms of sensory over-responsivity experienced by children with autism spectrum disorders. DST includes hyperacusis and misophonia, among others, and can limit participation in daily activities. Recently, a new screening tool, the Pediatric Hyperacusis and Misophonia Questionnaire (PMHQ-4) has been developed to allow health professionals to better identify and differentiate these conditions using a single assessment. Additional clinical tools are needed to further characterize DST symptoms to facilitate treatment planning after diagnosis. Methods: In this mixed-methods study n = 15 parents of autistic children 6 to 17 years of age completed an online survey and interviews regarding DST in autism and PMHQ item content. Participants were asked to identify sounds that bother their children and described how their children respond to these sounds. Results: Content analysis revealed two themes for bothersome sounds: (a) the context of sounds and (b) the qualities of sounds, each with their own subthemes; and four themes for responses to bothersome sounds: (a) avoidance, (b) distress/anger, (c) physical and (d) communication. Conclusion: Study findings were compiled into a clinical Inventory to Characterize DST (I-DST) that can be used to develop a detailed clinical profile for client-centered treatment.

**ИИ:** ? · другое · Mixed-methods, mostly qualitative study of 15 parents of autistic children. The survey may report PMHQ misophonia counts, but the children were possibly recruited for sound intolerance.

**Решение:** =

---

### 17 · R0042

**Pediatric Misophonia and Hyperacusis Questionnaire**

2026 · Unpublished · conference object, text/poster, article · und · https://doi.org/10.13140/rg.2.2.35937.26722

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Poster on a pediatric misophonia questionnaire with no abstract; it could be a validation study in an unselected or clinical sample.

**Решение:** =

---

### 18 · R0044

**Prevalence of misophonia in a tertiary healthcare hospital in Mumbai with Marathi translated Amsterdam misophonia scale A-MISO-S**

2026 · The Egyptian Journal of Otolaryngology · article, journalarticle, review · en · https://doi.org/10.1186/s43163-026-01108-1

Abstract Purpose Misophonia is a condition characterized by strong emotional reactions to specific sounds, often leading to distress. This study aims to translate and validate the Amsterdam Misophonia Questionnaire (A-MISO-S) into Marathi, a widely spoken Indian language, to facilitate better diagnosis and understanding of misophonia among Marathi-speaking populations. Method The translation process followed the American Association of Orthopedic Surgeons (AAOS) guidelines, involving forward and backward translations by proficient Marathi and English speakers, followed by a review by audiologists for face validity. Data were collected through face-to-face interviews with 227 individuals, excluding those with hearing or psychological issues. Randomly selected thirty participants with equal competence in English and Marathi were asked to retake the evaluation after 2 weeks in both languages. Descriptive statistics and Chi-square tests were used for analysis. The factor analysis, test-retest reliability and concurrent validity were assessed. Results The translated questionnaire showed good internal consistency (Cronbach’s alpha = 0.82). It also demonstrated good test-retest reliability and internal structure. Among participants, 11% exhibited moderate to severe misophonic symptoms. A significant gender difference was found, with females more likely to experience misophonia ( p = 0.03), but no significant association with age was observed. Conclusion The Marathi version of the A-MISO-S can be used in clinical settings for diagnosing misophonia, with 11% of the population showing moderate to severe symptoms. The findings highlight the need for increased awareness and treatment options for misophonia, particularly in India, where there is limited epidemiological data. Future research should explore factors contributing to misophonia, including its complex relationship with gender and other psychological factors.

**ИИ:** + · исследование распространённости · Marathi A-MISO-S validation in 227 hospital attendees not selected for misophonia; reports 11% with moderate-to-severe symptoms.

**Решение:** =

---

### 19 · R0047

**The subtypes of sensory hypersensitivity and their cross-modal relationships: a platform for transdiagnostic understanding**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-10490912/v1

Abstract Sensory hypersensitivity is common in the population and across many clinical conditions and areas of neurodivergence, yet its underlying mechanisms remain poorly understood. One challenge is the lack of coherent characterisation of the different types of hypersensitivity. Here, we developed a systematic framework across five senses, extending previous work on vision to hearing, touch, taste and smell. Using a large qualitative dataset and existing questionnaires, we generated and refined a comprehensive set of questions covering reported sensory triggers through several cohorts (N = 774, 335, 227). Bifactor analysis (N = 665) identified three subfactors of auditory hypersensitivity ( Loud/Multiple , Misophonia , Background ), four in touch sensitivity ( Human Touch , Food Texture , Clothing , Hands/Feet ), two for smell ( Fragrances, Natural Odours ), while taste was unimodal. We selected representative items to create the Cardiff Hypersensitivity Scale (CHYPS) and a brief version (CHYPS-Mini) which showed good reliability, validity and confirmatory bifactors (Ns = 191, 118, 561). Cross-modality analysis revealed that, rather than factoring by sense, three novel factors of hypersensitivity emerge: Social Auditory (Human Touch and auditory subfactors), Body and Chemosensory (T aste , Food Texture , Natural Odours and Hands/Feet) , and Vision (visual subtypes only). This framework can guide new research into mechanisms and the associations of sensory hypersensitivity with other traits and symptoms, as well as personalised approaches to clinical management.

**ИИ:** ? · другое · Hypersensitivity scale developed in large general cohorts includes a misophonia subfactor; unclear whether misophonia cases or prevalence are reported.

**Решение:** =

---

### 20 · R0048

**Digital treatment for tinnitus combining tinnitus retraining therapy and cognitive behavioral therapy: a Norwegian naturalistic study.**

2026 · Frontiers in psychiatry · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyt.2026.1868527

Introduction Ten to fifteen percent of the population experience tinnitus. It is necessary to develop effective treatments for patients suffering from tinnitus. This study aimed to explore the effectiveness of an internet-based treatment consisting of tinnitus retraining therapy and cognitive behavioral therapy for patients with primarily tinnitus. The secondary aims were to investigate changes in hyperacusis (hypersensitivity to sounds), misophonia (strong emotional reaction to a sound), depression, and anxiety. Methods A total of 144 patients diagnosed with tinnitus were included and assessed before treatment, and after 90 and 180 days. The results were differentiated for patients with mild, moderate, and severe+ tinnitus according to their scores on the Tinnitus Handicap Inventory (THI). Results A significant change in scores on the THI ( d = 0.41) was found from pre-treatment to the 180-day assessment for the total sample. A large effect size ( d = 0.95) was found for the group with severe+ tinnitus and a small effect size for the group with mild tinnitus ( d = 0.22). Further, there were small improvements in anxiety, depression, and hyperacusis, but no change in misophonia. Discussion In conclusion, this study indicate that the treatment can be helpful for people with tinnitus.

**ИИ:** + · клиническая группа · Tinnitus patients (n=144) recruited for tinnitus; misophonia measured at baseline, so the full text may report how many met a misophonia case definition.

**Решение:** =

---

### 21 · R0050

**Electrophysiological Correlates of Misokinesia: ERP Evidence for Rapid Aversive Processing of Triggering Movements**

2026 · JoCN Forum · article, journalarticle · en · https://doi.org/10.21428/8e6ba8ef.5df566c5

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract. ERP study of misokinesia might have screened an unselected pool and also measured misophonia; needs the full text to check.

**Решение:** =

---

### 22 · R0052

**Sound-evoked pupil dilation quantifies misophonic symptoms.**

2026 · PloS one · dataset/, journal article, journalarticle · eng · https://doi.org/10.1371/journal.pone.0348278

Misophonia is a debilitating disorder where seemingly innocuous sounds (often human made, such as chewing or throat clearing) evoke intense negative cognitive, emotional and physical “fight-or-flight” responses. Recent studies reported alarmingly high prevalence across different countries and population characteristics, revealing an urgent need for a better understanding of this condition as well as improved measurement and diagnostic tools. Firstly, current misophonia symptom measurements rely on (subjective) self-reports, and different studies employ various diagnostic approaches and cut-off scores. There is an urgent need for a complementary (objective) psychophysiological measurement tool. Secondly, the role of “mild” or “moderate” symptoms are currently topic of debate: are they still manifestations of the misophonic disorder? Here, we employ pupillometry to map out arousal responses to misophonia trigger sounds. We show that (i) pupil dilation can reliably differentiate misophonic responses from responses to generally unpleasant sounds (such as nails on chalk board), (ii) the “milder cases” of misophonia still show arousal responses characteristic of misophonia, and (iii) pupillometry can even be used to aid diagnosis in an individual; based on only pupil dilation, misophonic symptom severity could be reliably predicted at the level of a single individual. We conclude that even mild misophonic responses can reliably, objectively and cost-effectively be indexed by pupil-linked arousal

**ИИ:** ? · выборка неясна · Pupillometry experiment covering a range of misophonia severity; the abstract doesn't say how participants were recruited, so an unselected pool may have been screened.

**Решение:** =

---

### 23 · R0056

**Objective measures of sensory gating capacity do not predict the severity of misophonia symptoms.**

2026 · Hearing research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.heares.2026.109595

Misophonia is characterized by intense negative emotional responses to specific trigger sounds. Given that repetitive sounds are frequently endorsed as triggers, we investigated whether impaired preattentive sensory gating contributes to misophonia pathophysiology. Forty-eight participants (36 female; aged 18-64) completed self-report measures of misophonia severity (MisoQuest) and sensory gating ability (Sensory Gating Inventory-Brief), alongside an objective measure of sensory gating capacity (suppression of the P50 component in a paired-pulse paradigm). Resting-state beta and gamma power were also examined as potential markers of inhibitory capacity. A dimensional approach was employed, examining relationships across the spectrum of symptom severity rather than discrete diagnostic groups. Participants showed normal P50 suppression overall (mean S2/S1 ratio = 0.40 ± 0.34). Despite significant correlation between self-reported misophonia severity and sensory gating difficulties (τ = 0.51, p &amp;lt; .001), no significant associations emerged between P50 suppression ratios and either misophonia severity (τ = -0.05, p = .652) or self-reported gating difficulties (τ = 0.14, p = .198). Similarly, resting-state beta and gamma power showed, at best, weak evidence of a relationship with misophonia symptoms. These findings suggest that misophonia may not arise from deficits in early, automatic sensory filtering mechanisms. Rather, the characteristic hypersensitivity to trigger sounds likely emerges from alterations in higher-order auditory processing networks, consistent with neuroimaging evidence of altered salience network activity. These results help constrain theoretical models that seek to understand the patterns of atypical neural activity that underlie the experience of misophonia.

**ИИ:** ? · выборка неясна · EEG study of 48 adults measured with MisoQuest dimensionally; recruitment unclear, may include unselected participants with case counts.

**Решение:** =

---

### 24 · R0058

**Development and Validation of the Japanese Version of the Amsterdam Misophonia Scale (A-MISO-S-J)**

2026 · PsyArXiv · article, preprint · und · https://doi.org/10.31234/osf.io/er4f3_v1

Background: Misophonia is characterized by heightened emotional and physiological responses to specific sounds made by others, such as chewing or sniffing. Although several scales have been developed to assess misophonia severity, few Japanese versions are currently available. This study developed a Japanese version of the Amsterdam Misophonia Scale (A-MISO-S-J), one of the most widely used instruments for assessing misophonia severity, and examined its reliability and validity for both research and clinical use in Japan. Methods: In Study 1, we surveyed 265 Japanese adults and evaluated factorial and criterion-related validity using confirmatory factor analysis (CFA) and correlations. In Study 2, 120 participants completed the A-MISO-S-J at two time points to assess test–retest reliability. Results: The CFA supported a one-factor structure for the A-MISO-S-J, demonstrating acceptable model fit and good internal consistency. Evidence of criterion-related validity was found, with moderate-to-strong positive correlations between A-MISO-S-J scores and scales measuring hyperacusis, obsessive-compulsive symptoms, disgust, and negative affect. Furthermore, approximately 76% of the participants reported at least mild symptoms, which is significantly higher than the prevalence rates reported in other countries. Study 2 demonstrated acceptable test–retest reliability of the A-MISO-S-J. Discussion: The A-MISO-S-J demonstrated good psychometric properties. It may serve as a useful tool for advancing understanding of misophonia symptoms in East Asian populations.

**ИИ:** + · валидация шкалы · Validation study of the Japanese A-MISO-S in 265 adults from the general population; reports about 76% with at least mild symptoms.

**Решение:** =

---

### 25 · R0059

**Misophonia: when everyday sounds become unbearable**

2026 · other · https://doi.org/10.64628/aak.4mfjq6kuh

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract; title suggests an overview or commentary, but original prevalence data can't be ruled out.

**Решение:** =

---

### 26 · R0061

**Social-Cognitive Dysregulation Model of Misophonia: Perspective from a Behavioural Study**

2026 · bioRxiv · preprint, google scholar result, project · https://doi.org/10.64898/2026.09.03.749152

Misophonia is characterised by intense emotional, physiological, and behavioural reactions to specific everyday sounds, particularly sounds produced by other people. Although previous research has mainly focused on sensory reactivity and negative emotional responses to trigger sounds, less is known about the broader social-cognitive processes associated with misophonia. This online study will examine whether misophonia symptoms and severity are associated with individual differences in theory of mind, empathy, alexithymia, and facial mimicry. Participants will complete the Yoni Task to assess cognitive and affective theory of mind and the Multifaceted Empathy Test to assess cognitive and affective empathy. They will also complete validated self-report measures of misophonia symptoms, alexithymia, anxiety, depression, and general sound sensitivity. Facial mimicry will be assessed as an additional indicator of automatic social-emotional processing. The primary analyses will test whether greater misophonia severity is associated with differences in the ability to infer other people’s thoughts and emotions, recognise emotional states, experience empathic concern, identify and describe one’s own emotions, and show facial mimicry. The study will also examine whether alexithymia helps explain associations between misophonia and social-cognitive functioning. Anxiety, depression, and general sound sensitivity will be included as control variables to determine whether any observed associations are specific to misophonia rather than being explained by broader emotional distress or sensitivity to sound. Participants aged 18–60 will be recruited through Prolific, and the study will be administered online using Gorilla Experiment Builder. The findings are expected to contribute to a broader understanding of misophonia as a condition involving not only sound intolerance and emotional reactivity, but also potentially important social, emotional, and interpersonal processes.

**ИИ:** ? · другое · Study protocol with no data yet; Prolific sample appears unselected and misophonia will be measured; the completed study could report case counts.

**Решение:** =

---

### 27 · R0062

**Misophonia in Adolescents: The Interplay of Parental Emotional Expression, Family Functioning, and Childhood Trauma-A Cross-Sectional Control Study.**

2026 · Journal of clinical psychology · article, journal article, journalarticle · eng · https://doi.org/10.1002/jclp.70128

ABSTRACT Objective Misophonia is an underrecognized condition characterized by intense emotional responses to specific auditory stimuli. Beyond its sensory basis, growing evidence suggests that relational experiences and difficulties in emotional processes may play a critical role in its development and severity. This study aimed to explore the roles of family functioning, adolescent‐reported parental emotional expression, and childhood trauma in adolescents with misophonia, using a clinical comparison group with anxiety disorders. Methods A total of 128 adolescents aged 12–18 were assessed in a child and adolescent psychiatry outpatient clinic. The misophonia group ( n = 78) was identified using the Misophonia Questionnaire (cutoff ≥ 7) and structured clinical interviews. The control group ( n = 50) included adolescents with primary anxiety disorders but no clinically significant misophonia symptoms. Validated self‐report measures were used to assess family dynamics, perceptions of parental emotional expression, trauma history, and functional impact, along with parent‐reported behavioral difficulties that provide indirect information about adolescents' emotion regulation–related challenges. Results Adolescents with misophonia reported significantly higher levels of emotional and physical neglect and abuse, along with more dysfunctional family dynamics and heightened emotional intrusiveness and irritability. These youth also showed greater difficulties in emotion regulation–related domains, as reflected in parental emotional expression patterns and parent‐reported behavioral difficulties, as well as higher levels of functional impairment in home and social settings. Misophonia severity was associated with trauma exposure and maladaptive familial emotional climates. Conclusion Findings suggest that misophonia in adolescence may be shaped by early adverse experiences and relational patterns that contribute to difficulties in emotional functioning. Family‐based and trauma‐informed approaches should be considered when assessing and treating adolescents presenting with misophonia symptoms.

**ИИ:** ? · выборка неясна · Psychiatric outpatient adolescents with misophonia identified by MQ cutoff; unclear whether an unselected clinic pool was screened.

**Решение:** =

---

### 28 · R0063

**The multidimensional effects of sleep quality in young adults: the relationship between auditory performance, sound tolerance, and anxiety.**

2026 · European archives of oto-rhino-laryngology : official journal of the European Federation of Oto-Rhino-Laryngological Societies (EUFOS) : affiliated with the German Society for Oto-Rhino-Laryngology - Head and Neck Surgery · article, journal article, journalarticle · eng · https://doi.org/10.1007/s00405-025-09979-5

Abstract Purpose This study aimed to comprehensively evaluate the effects of sleep quality on auditory performance, sound tolerance, and anxiety levels in young adults and to examine the possible relationships between these variables. Materials and methods The study included 607 young adults aged 18-30 years (mean 21.48 ± 2.88 years). Participants completed a participant information form created for this study, the Pittsburgh Sleep Quality Index (PSQI), the Decreased Sound Tolerance Scale-Screening (DSTS-S), the Speech, Spatial, and Hearing Qualities Scale (SSQ), and the Beck Anxiety Scale. Data analysis was performed using IBM SPSS Statistics (Version 23.0) software. Results The participants’ PSQI mean was 7.62±3.76, and 65.53% of the participants (&gt;5) showed poor sleep quality. PSQI scores showed a negative correlation with SSQ total scores (rₛ=-0.242, p &lt;0.001) and a moderate positive correlation with Beck Anxiety scores (rₛ=0.420, p &lt;0.001). Furthermore, PSQI showed significant positive correlations with hyperacusis (rₛ=0.294, p &lt;0.001), phonophobia (rₛ=0.159, p =0.001), and misophonia (rₛ=0.312, p &lt;0.001). Conclusion This study revealed statistically significant relationships between poor sleep quality in young adults and auditory performance in daily life, reduced sound tolerance, and anxiety levels. The findings of the present study indicate that poor sleep quality is significantly associated with lower auditory performance and sound tolerance. Furthermore, poor sleep quality was found to be associated with higher anxiety levels. These findings demonstrate the effects of sleep on various systems and emphasize its physiological necessity for healthy functioning.

**ИИ:** + · ненабранная выборка · 607 unselected young adults completed the DSTS-S, which has a misophonia subscale; the full text might report how many met a misophonia cutoff.

**Решение:** =

---

### 29 · R0066

**Early maladaptive schemas and misophonia: Incremental contributions beyond personality traits and general psychopathology.**

2026 · Hearing research · article, dataset/dataset, journal article · eng · https://doi.org/10.1016/j.heares.2026.109756

Misophonia is a sound sensitivity disorder characterized by heightened emotional, physiological, and behavioral reactions to specific auditory stimuli. Although prior research has linked misophonia to maladaptive personality traits and internalizing symptoms, the role of early maladaptive schemas (EMSs) remains underexplored. The present study examined the associations between misophonia severity, EMSs, personality trait domains, and psychological symptoms, and tested whether EMSs accounted for incremental variance beyond these factors. A total of 144 adults (72 with misophonia and 72 matched controls) completed self-report measures of misophonia, EMSs, personality traits, depression, and anxiety. Misophonia severity was positively associated with most EMSs, as well as with negative affectivity, detachment, psychoticism, and symptoms of depression and anxiety. Individuals with misophonia reported significantly higher levels across all EMSs, personality domains, and psychological symptoms compared to controls. Regression analyses indicated that several EMSs predicted misophonia severity, with Entitlement and Emotional Inhibition emerging as the strongest independent predictors. In a hierarchical regression model, EMSs accounted for additional variance beyond personality traits and psychological symptoms. In the final model, Entitlement and Negative Affectivity remained significant predictors. These findings support a hierarchical framework in which personality trait domains reflect a broad dispositional vulnerability, whereas EMSs represent more specific cognitive-emotional processes that may shape the appraisal and perceived meaning of trigger sounds. Targeting EMSs may enhance psychological interventions by addressing maladaptive appraisals and emotional regulation difficulties underlying misophonic responses.

**ИИ:** ? · выборка неясна · Case-control design (72 misophonia, 72 matched controls); cases may come from screening a larger unselected pool, but recruitment isn't described.

**Решение:** =

---

### 30 · R0068

**Validating and refining a psychoacoustic test to diagnose hyperacusis.**

2026 · Hearing research · article, journal article, validation study · eng · https://doi.org/10.1016/j.heares.2025.109482

International audienceDecreased sound tolerance refers to conditions like hyperacusis and misophonia, in which everyday sounds may provoke discomfort or distress. Hyperacusis is characterized by exaggerated loudness perception and aversive reactions to moderate to loud sounds, often leading to significant impairment. Despite its estimated prevalence of 10–15 %, no objective clinical test exists. Current assessment relies on interviews, questionnaires, and loudness discomfort levels (LDLs), which lack reliability and ecological validity. Recent work has shown that pleasantness ratings of natural sounds can differentiate individuals with hyperacusis from controls. A subset of seven natural sounds, termed Core Discriminant Sounds (CDShyper), was identified post-hoc as particularly effective, yielding 81 % sensitivity and 88 % specificity in prior lab-based testing. A similar approach for misophonia identified ten distinct trigger sounds (CDSmiso). This study aimed to validate a tablet-based version of the CDS test to diagnose hyperacusis prospectively. Forty-nine participants (20 with hyperacusis, 29 controls) completed the test that presented randomly CDShyper and CDSmiso sounds at 60, 70, and 80 dBA. Participants rated each sound presentation on visual analog scales for pleasantness and loudness. Hyperacusis was defined by clinical complaints, Hyperacusis Questionnaire scores (≥22), and LDLs (≤77 dB HL). Results showed that individuals with hyperacusis rated CDShyper sounds as significantly less pleasant (means score of 39 vs 25 for hyperacusis vs controls, p = .002, η² = 0.185) and louder (means score of 71 vs 63 for hyperacusis vs controls, p = .024, η² = 0.104) than controls. No group differences emerged for misophonia trigger sounds (CDSmiso sounds). The sensitivity and specificity for the combined CDShyper scores of pleasantness and loudness at detecting hyperacusis were 90 % and 69 %, respectively. These findings validate the tablet-based test as an efficient, ecologically valid tool for diagnosing hyperacusis

**ИИ:** ? · другое · Hyperacusis patients and controls rated misophonia trigger sounds; no misophonia case measure reported, but the full text might include one.

**Решение:** =

---

### 31 · R0069

**Clinical correlates of individuals with and without misophonia in the U.S.: Results from a population-based study.**

2026 · Psychiatry research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.psychres.2026.116941

• Self-reported clinical correlates of misophonia were examined in a representative U.S. sample. • High rates of sensory, auditory, and psychiatric disorders were found in the misophonia group. • Two-thirds of the misophonia sample had at least one psychological disorder. • Anxiety and depression were the most common mental health comorbidities. • Adjusted models showed misophonia was associated with greater odds of most disorders studied. Misophonia is a disorder characterized by strong negative affective, physiological, cognitive, and behavioral reactions to specific sounds (e.g., chewing, swallowing). Studies have begun to investigate co-occurring psychological and audiological disorders with misophonia, but are limited by methodology and generalizability. This study investigated the rate of comorbid disorders in a sample of individuals with and without misophonia using a nationally representative sample in the United States. Data were collected through Ipsos KnowledgePanel—a large, probability-based web panel that is representative of the United States. Participants were invited to complete a brief self-report survey of previous and current psychological and auditory-sensory symptoms and diagnoses. Over half (62.5%) of the misophonia sample reported they had received at least one psychological disorder diagnosis, wherein depression (48.9%) and anxiety disorders (46.7%) were the most commonly reported. Separate hierarchical multivariate binary logistic regression results demonstrate individuals with misophonia ( n = 185) are more likely to report current mental health and auditory-sensory symptoms compared to individuals without misophonia ( n = 1,644) regardless of demographic factors. Further, hierarchical multivariate binary logistic results show individuals with misophonia are more likely to report lifetime diagnoses of all psychological, auditory-sensory, and communication disorders except hyperacusis, autism spectrum disorders, and certain behavior disorders compared to individuals without misophonia. Comorbidity rates were higher in the misophonia sample, and misophonia status was significantly associated with the presence of other clinical syndromes. Findings advance characterization of misophonia by highlighting the elevated co-occurrence rates of psychological and auditory-sensory disorders compared to individuals without misophonia.

**ИИ:** + · исследование распространённости · Nationally representative US Ipsos KnowledgePanel sample; 185 of 1,829 met misophonia criteria, so prevalence can be derived.

**Решение:** =

---

### 32 · R0071

**Quantifying insula neurotransmitter concentrations in misophonia and non-misophonic clinical emotion dysregulation: an in-vivo spectroscopy study**

2026 · Open Science Framework · other · https://doi.org/10.17605/osf.io/h9g2k

Misophonia is a disorder of decreased tolerance to sounds and associated stimuli that often causes significant emotional distress. This study will examine whether in-vivo concentrations of the main excitatory (glutamate) and inhibitory (GABA) neurotransmitters as measured by proton magnetic resonance spectroscopy (1H-MRS) within the left and right insula are associated with misophonia symptoms in adults, as well as the therapeutic response to non-invasive neurostimulation (repetitive transcranial magnetic stimulation [rTMS]).

**ИИ:** ? · другое · OSF protocol; misophonia group is selected, but the emotion-dysregulation clinical group may have been screened for misophonia.

**Решение:** =

---

### 33 · R0072

**A-192: Misophonia Severity and Cognitive Performance in Young Adults: Evidence for Context-Dependent and Domain-Specific Effects**

2026 · Archives of Clinical Neuropsychology · journalarticle, conference-abstract · en · https://doi.org/10.1093/arclin/acag065.208

Abstract Objective: Misophonia is characterized by strong negative emotional and physiological reactions to specific auditory stimuli, often accompanied by heightened attentional capture. Emerging research suggests it may interfere with cognitive processes, particularly attention and executive functioning, though findings remain limited. Most prior work has focused on responses to trigger stimuli, leaving its relationship with baseline cognitive functioning under neutral conditions unclear. This study examined whether misophonia severity is associated with performance across cognitive domains during standard neuropsychological testing. Method/Data Selection: Undergraduate participants (N = 25; mean age = 19.6 years, SD = 2.1), comprising a predominantly female (96%) nonclinical sample, completed the Duke-Vanderbilt Misophonia Questionnaire (DVMQ) and the Repeatable Battery for the Assessment of Neuropsychological Status (RBANS). Pearson correlations assessed associations between misophonia severity and RBANS index scores (attention, immediate memory, delayed memory, visuospatial functioning, language). Results/Data Synthesis: All participants were prescreened for elevated misophonia symptoms. Misophonia severity was not significantly associated with attention (r = .03, p = .889), immediate memory (r = −.04, p = .866), delayed memory (r = .22, p = .292), visuospatial functioning (r = −.25, p = .227), or language (r = .24, p = .238). Effect sizes suggested a differentiated pattern, with positive associations for delayed memory and language and a negative association for visuospatial functioning. Conclusions: Misophonia does not appear to be associated with global cognitive deficits under neutral conditions but may involve context-dependent, domain-specific effects. These findings align with models emphasizing attentional capture and emotional interference. Future research incorporating trigger exposure and cognitive load will clarify when misophonia-related cognitive differences emerge.

**ИИ:** + · скрининг пула · Undergraduates were prescreened for elevated misophonia symptoms using the DVMQ, so the full text may report screening-pool counts.

**Решение:** =

---

### 34 · R0074

**Decreased Sound Tolerance: School Functioning in Children and Findings from Otoacoustic Emissions**

2026 · Diva portal (Dalarna University Library) · master thesis, dissertation, thesis · en · http://urn.kb.se/resolve?urn=urn:nbn:se:ltu:diva-117072

Decreased Sound Tolerance (DST) is a condition in which everyday sounds are perceived as disturbing, painful, excessively loud, or frightening. It is an overarching term including hyperacusis, misophonia, phonophobia, and noise sensitivity. Among 11-year-old children, prevalence is approximately 3.7% and is higher in individuals with autism spectrum disorder (ASD), attention deficit hyperactivity disorder (ADHD), anxiety, depression, migraine, stress-related conditions, and traumatic brain injury. DST can be debilitating and lead to withdrawal and activity limitations. Given the challenging sound environments in schools, it is reasonable to expect negative effects on academic performance and participation. However, knowledge of its consequences for school children remains limited, and there is a lack of tools to assess DST. This work comprises a systematic review of otoacoustic emissions (OAE) in individuals with hyperacusis and a study of school outcomes in children with DST. The review followed a pre-registered PROSPERO protocol and PRISMA guidelines. Searches in Embase, Scopus, and MEDLINE yielded 2,072 articles, of which 19 were included. Most studies had some concerns or high risk of bias. The narrative synthesis produced inconclusive results, likely due to differences in OAE methodology, hyperacusis identification, populations, and study quality. Implications for further research are discussed. The second study included children aged 9–11 years, recruited from mainstream schools in Sweden. Out of 773 contacted, 240 agreed to participate, of whom 44 had DST. Groups were defined by the presence or absence of DST and additional neurodevelopmental disorders (e.g. ASD, ADHD) or other health conditions. Outcomes included absenteeism (Grades 3–4), national test scores (Grade 3), and caregiver reports. The groups were comparable for gender, caregiver education level, immigration background or course curriculum (native or non-native speaker). Children with DST combined with additional conditions demonstrated greater school difficulties, including higher absenteeism, lower test scores, and more caregiver-reported problems. Findings are discussed together with possible implications and directions for further research. Ljudöverkänslighet är ett tillstånd där vardagliga ljud upplevs som störande, smärtsamma, alltför högljudda eller skrämmande. Det är ett samlingsbegrepp som inkluderar hyperakusi, misofoni, fonofobi och bullerkänslighet. Hos 11-åriga barn är förekomsten cirka 3.7 % och högre hos individer med autismspektrumtillstånd (ASD), ADHD, ångest, depression, migrän, stresstillstånd och traumatisk hjärnskada. Ljudöverkänslighet kan vara ett begränsande tillstånd som påverkar individen socialt samt i skolan och arbetslivet. Mot bakgrund av de utmanande ljudmiljöerna i skolan kan tillståndet förväntas påverka skolprestation och delaktighet negativt. Kunskapen om konsekvenserna för skolbarn är dock begränsad, och diagnostiska verktyg för att bedöma ljudöverkänslighet saknas. Detta arbete omfattar en systematisk litteraturöversikt av otoakustiska emissioner (OAE) hos individer med hyperakusi samt en studie av skolrelaterade utfall hos barn med ljudöverkänslighet. Översikten följde ett förregistrerat PROSPERO-protokoll och PRISMA-riktlinjer. Sökningar i Embase, Scopus och MEDLINE gav 2 072 artiklar, varav 19 inkluderades. De flesta studier hade viss eller hög risk för bias. Den narrativa syntesen gav inga entydiga slutsatser, sannolikt på grund av variation i OAE-mätmetodik, diagnostik av hyperakusi, populationer och studiekvalitet. Implikationer för framtida forskning diskuteras. Den andra studien inkluderade barn i åldern 9–11 år som rekryterades från grundskolor i en svensk kommun. Av 773 kontaktade valde 240 att ingå i studien, varav 44 hade ljudöverkänslighet. Grupper bildades utifrån närvaro eller frånvaro av ljudöverkänslighet och neuropsykiatriska tillstånd (t.ex. ASD eller ADHD) eller andra hälsotillstånd. Utfallsvariabler var frånvaro (årskurs 3–4), resultat på nationella prov (årskurs 3) samt vårdnadshavares rapporter. Grupperna var jämförbara avseende kön, vårdnadshavares utbildningsnivå, invandrarbakgrund, och kursplan (svenska som första eller andra språk). Barn med ljudöverkänslighet i kombination med ytterligare tillstånd uppvisade mer uttalade skolsvårigheter. Fynden diskuteras tillsammans med implikationer för framtida forskning. PRECISE

**ИИ:** ? · другое · Unselected Swedish school sample (44/240 with DST); DST is an umbrella term including misophonia, but whether misophonia was measured separately is unclear.

**Решение:** -4 нет инструмента именно для мизофонии (только гиперакузия/шумочувствительность)

---

### 35 · R0075

**Misophonia severity in university students: associations with negative emotionality, motor impulsivity, and checking.**

2026 · BMC psychology · article, collection/collection, journal article · eng · https://doi.org/10.1186/s40359-026-04390-z

Background Misophonia is characterized by strong negative emotional and behavioral reactions to specific everyday sounds and is associated with significant functional impairment. Previous studies have primarily focused on associations between misophonia and negative affect (e.g., depression, anxiety, and stress), whereas less is known about how misophonia severity relates to impulsivity and specific obsessive–compulsive symptom dimensions in non-clinical populations. Objective The present study aimed to estimate the prevalence of Misophonia Questionnaire (MQ) cut-off–defined elevated misophonia symptoms among university students, describe emotional and behavioral responses to trigger sounds, and examine whether motor impulsivity and checking are involved in the associations between depression, anxiety, stress symptoms, and misophonia severity. Methods A total of 562 university students aged 18–30 years participated in this cross-sectional study. Participants completed the MQ, Depression Anxiety Stress Scales (DASS-21), Barratt Impulsiveness Scale–Short Form (BIS-11-SF), and Maudsley Obsessional–Compulsive Inventory (MOCI). Model-based path analyses were conducted to examine direct and indirect associations between negative affect symptoms and misophonia severity through motor impulsivity and checking. Results Sixteen point 4% of participants met the MQ cut-off for elevated misophonia symptoms. Misophonia severity showed positive associations with depression, anxiety, stress symptoms, motor impulsivity, and checking. Path analyses indicated that anxiety and stress symptoms were directly associated with misophonia severity, while depressive symptoms were associated only indirectly. Significant indirect associations were observed through motor impulsivity and checking, although the indirect pathway via checking was not significant for anxiety. Conclusions Misophonia severity is associated not only with negative affect but also with impulsivity- and compulsivity-related dimensions. These findings highlight the relevance of motor impulsivity and checking as behavioral dimensions linked to misophonia severity and underscore the importance of considering multidimensional psychopathological features when assessing misophonia in non-clinical populations. Supplementary Information The online version contains supplementary material available at 10.1186/s40359-026-04390-z.

**ИИ:** + · исследование распространённости · Unselected sample of 562 university students; 16.4% met the MQ cut-off for elevated misophonia symptoms.

**Решение:** =

---

### 36 · R0077

**Misophonia Levels and Care Behaviours in Intensive Care Nurses: A Descriptive, Cross-Sectional and Relational Study.**

2026 · Nursing open · article, journal article, journalarticle · eng · https://doi.org/10.1002/nop2.70504

ABSTRACT Background and Objectives Misophonia is a condition that causes abnormal emotional reactions to certain environmental sounds. The aim of this study was to investigate whether there is a relationship between the responses of nurses working in intensive care units to these sounds and the care provided to the patient. Methods Personal Information Form, Misophonia Scale and Caring Behaviours Scale‐24 were used to collect data. Mann Whitney U test and Kruskall Wallis test were used to analyse the data, and pearson correlation coefficient was used to examine the relationship between variables. The significance level was taken as p &lt; 0.05. Results It was determined that the mean scores of the participants on the Caring Behaviours Scale‐24 and the Misophonia Scale were moderate. A moderate negative correlation was found between the Caring Behaviours Scale‐24 and the Misophonia Scale. Conclusions In the light of the data we obtained from the study, it is possible to say that nurses exhibiting misophonic behaviours may be adversely affected by the sounds in the intensive care environment and this situation may negatively affect their care behaviours. Relevance to Clinical Practice Nurses with misophonic symptoms should be identified and their personal coping strategies should be strengthened. In this way, the quality of patient care and patient safety can be improved. Patient or Public Contribution Descriptive and cross‐sectional study. After obtaining the necessary permissions for the study, the researcher met with the intensive care nurses in the nurses' work environment, provided information about the study, and obtained written consent forms from those who volunteered to participate in the study. The relevant forms were delivered to the intensive care nurses in envelopes to be filled in and were returned in a sealed envelope at the end of the 2‐day filling period. The study adhered to the STROBE checklist.

**ИИ:** + · ненабранная выборка · Cross-sectional survey of ICU nurses (workers) not recruited for misophonia, measured with Misophonia Scale.

**Решение:** =

---

### 37 · R0078

**Smartphone-based tinnitus retraining therapy in Ménière's disease patients following vestibular ablation: a feasibility study**

2026 · European Archives of Oto-Rhino-Laryngology · journalarticle, article · en · https://doi.org/10.1007/s00405-026-10255-3

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract; tinnitus retraining therapy trial in Ménière's patients. TRT sometimes assesses misophonia, so a misophonia measure is unlikely but possible.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 38 · R0082

**Selective Disruption of Salience-Network Anterior Insula Connectivity in Misophonia: A Disorder-Specific Neural Signature.**

2026 · Human brain mapping · article, journal article, journalarticle · eng · https://doi.org/10.1002/hbm.70468

ABSTRACT Misophonia, a disorder characterized by extreme aversion to certain sounds, affects 5%–20% of the general population, yet mechanisms are still largely unknown. Recent neuroimaging studies have reported abnormal functional connectivity of the anterior insula to various limbic, salience, and motor regions in smaller samples of misophonic individuals versus controls, suggesting potential differences in underlying attentional or emotional processes. These findings prompt questions about the insular connectivity profile in larger samples of adults, what patterns emerge when the samples span a wider range of misophonia severity, and how these patterns may or may not overlap with other co‐occurring disorders. To address these questions, we analyzed resting‐state functional magnetic resonance imaging data from the open Welsh Advanced Neuroimaging Database ( N = 162) comprising participants recruited from the general adult population and assessed for sensory sensitivity, anxiety, depression, and autistic traits. A misophonia severity score was derived from the sensory sensitivity data using a model trained on a second adult self‐report sample from Oklahoma ( N = 777). Using anterior insula as a seed for a whole‐brain seed‐to‐voxel connectivity analysis, the derived misophonia severity scores were found to be significantly related to connectivity from the insula to clusters overlapping the planum temporale, operculum, precentral gyrus, and supplementary motor area. Notably, this insular connectivity profile was unique to the anterior insula of the salience network and was not observed when dividing the sample into misophonia (patient) versus control groups, or when grouping participants as a function of anxiety, depression, or autistic traits. These results underline the importance of the salience‐network anterior insula in understanding misophonic aversion and provide tentative evidence of neurological differences between misophonia and anxiety, depression, and autism. This work aids in our understanding of neural mechanisms of misophonia and emphasizes the benefit of treating misophonia as a continuous spectrum disorder to better reflect the variability of symptoms in the real world.

**ИИ:** + · ненабранная выборка · General-population imaging sample (N=162) plus Oklahoma adult sample (N=777); misophonia vs control grouping likely reports case counts.

**Решение:** =

---

### 39 · R0090

**Exploring the Relationship Between Decreased Sound Tolerance and Neural Attention Processing: An ERP Study**

2026 · F1000Res · article, journalarticle, preprint · en · https://doi.org/10.12688/f1000research.175631.1

Background: Decreased sound tolerance (DST) is common in individuals with autism spectrum disorder (ASD). This study examined how attentional control resources influence DST. Previous studies have shown that increasing cognitive load enhances the brain activity component (N100) to task-irrelevant noise. We hypothesized that individuals with DST would be more sensitive to cognitive load, showing a greater increase in their neural responses to noise as cognitive load increases. Because DST comprises multiple subjective symptoms, we analyzed the associations with specific symptoms. Methods Thirteen adults with ASD and twenty-two adults without ASD participated in the study. Participants who self-reported auditory hypersensitivity were classified as the DST group. All participants completed a DST questionnaire with six subscales: excessive loudness, ear pain, fear, annoyance, attention control, and attention to detail. Event-related potentials (ERPs) elicited by task-irrelevant noise were analyzed during an auditory n-back task. The n-back task included a low (1-back) and a high (2-back) cognitive load condition. Results The prevalence of self-reported DST was significantly higher in the ASD group than in controls. Individuals who reported DST also tended to experience other types of sensory hypersensitivity. Attentional functions were associated with fear, annoyance, and loudness perception of sounds, and ear pain appeared to function independently of other DST symptoms. Scores for attentional control difficulties related to DST did not correlate with performance on the n-back task, which reflects susceptibility to noise interference. Contrary to previous findings, N100 amplitude did not differ between task-load conditions and did not vary according to the presence of DST. P200 amplitude was larger in the 1-back than in the 2-back condition but did not differ by ASD diagnosis or DST status. Conclusions The presence of DST or ASD was not associated with cognitive capacity or with the auditory processing of task-irrelevant noise.

**ИИ:** ? · другое · ASD and control adults completed a DST questionnaire; its annoyance/fear subscales might capture misophonia, but misophonia is never named.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 40 · R0094

**Hyperacusis, misophonia, and mental health in young adults in Canada: Estimated prevalence and associated factors**

2026 · Journal of Affective Disorders Reports · journalarticle, article, google scholar result · en · https://doi.org/10.1016/j.jadr.2026.101170

Introduction Despite growing recognition of hyperacusis and misophonia, evidence regarding their prevalence in young adults remains limited. This study aimed to address this gap by estimating the prevalence of hyperacusis, misophonia, and tinnitus, identifying sociodemographic and health-related factors associated with these conditions, and examining their associations with current anxiety and depressive symptoms. Methods A total of 606 young adults completed validated self-report questionnaires, including the Hyperacusis Questionnaire, Hyperacusis Assessment Questionnaire, Misophonia Assessment Questionnaire, Generalized Anxiety Disorder-7, and Patient Health Questionnaire-9. Results Of the total sample, 8.60% met criteria for significant hyperacusis; 24.50% reported at least mild misophonia, including 8.60% with moderate or greater severity; and 12.70% reported constant tinnitus. More than 70% of participants with hyperacusis or tinnitus also reported misophonia. Moderate or greater current anxiety and depressive symptoms were reported by 53.10% and 42.10% of participants, respectively. Multiple linear regression analyses showed strong associations between hyperacusis (32.80%) and misophonia (33.0%) symptom severity, while hearing issues, tinnitus, overall health status, and gender showed smaller associations. Current anxiety (44.50%) and depressive (44.60%) symptom severity were likewise strongly associated, while overall health status, ethnicity, and family history of hearing issues showed smaller associations with these symptoms. Moreover, hyperacusis was independently associated with current anxiety symptom severity ( p <0.001). Conclusions The findings indicate that hyperacusis, misophonia, and tinnitus frequently co-occur, and that anxiety and depressive symptoms are strongly interrelated in young adults. These highlight the role of sound hypersensitivity in mental health, and the importance of integrated assessment of auditory and psychological disorders.

**ИИ:** + · исследование распространённости · Prevalence survey of 606 young adults in Canada using the MAQ: 24.5% had at least mild misophonia and 8.6% moderate or worse.

**Решение:** =

---

### 41 · R0096

**Atypical brain activation and functional connectivity during affective sounds processing in misophonia: An fMRI study**

2026 · The Journal of the Acoustical Society of America · journalarticle, conference-abstract, journal article · en · https://doi.org/10.1121/10.0045101

Sound is a powerful driver of emotion, with the brain rapidly processing acoustic features and attributing emotional significance to everyday sounds. In misophonia, this sound–emotion interaction is exaggerated, provoking intense negative emotional and behavioral reactions to otherwise benign “trigger” sounds like chewing or breathing. While misophonia is typically linked to these specific triggers, growing evidence suggests that misophonia-related affective responses may extend beyond classical triggers. To explore this, we investigated brain responses to generally unpleasant and neutral sounds using task-based fMRI. Ninety-one young adults with misophonia and matched controls listened to 90 emotionally valenced sounds and provided valence ratings during scanning. Compared to controls, individuals with misophonia exhibited hyperactivation in visual association areas and reduced functional connectivity between salience and visual networks when processing unpleasant relative to neutral sounds. These findings indicate atypical cross-modal sensory engagement and suggest that altered brain activation and connectivity in misophonia extend beyond trigger sounds to a broader range of emotionally relevant auditory stimuli. Building on these fMRI results, our ongoing behavioral study explores whether similar emotional response patterns generalize across cultures. Together, these studies aim to advance understanding of misophonia’s neural and behavioral mechanisms and inform culturally sensitive clinical assessment and intervention.</jats:p

**ИИ:** ? · выборка неясна · fMRI case-control conference abstract; recruitment unclear, young adults may have come from a screened unselected student pool.

**Решение:** =

---

### 42 · R0097

**Differential brain responses to affective sounds in misophonia and hyperacusis: A task-based fMRI approach.**

2026 · Cognitive, affective & behavioral neuroscience · article, journal article, journalarticle · eng · https://doi.org/10.3758/s13415-026-01435-z

Abstract Humans are naturally attuned to emotionally salient sounds, such as screams signaling danger, which trigger survival-related responses. In sound-sensitivity disorders, such as misophonia and hyperacusis, everyday sounds provoke intense emotional and behavioral reactions. Misophonia is typically triggered by specific sounds, such as chewing, whereas hyperacusis involves hypersensitivity to sounds above certain intensity thresholds. Because these disorders share overlapping symptoms and frequently co-occur, disentangling their neural bases is essential for improving diagnosis and treatments. We recruited 91 young adults categorized into four groups: misophonia, hyperacusis, comorbid misophonia and hyperacusis, and controls. We conducted task-based fMRI, where participants listened to 90 emotionally valenced sounds from the International Affective Digitized Sounds-2 database and rated their valence during scanning. Whole-brain functional activation and seed-to-voxel functional connectivity analyses revealed both distinct and overlapping pattern of neural correlates associated with these disorders. The misophonia group, regardless of comorbid hyperacusis (relative to controls), showed hyperactivation in visual association areas and reduced connectivity between salience and visual networks during unpleasant versus neutral sound processing. This suggests atypical cross-modal sensory involvement. The hyperacusis group exhibited reduced connectivity between salience hubs and frontal control regions compared to misophonia and controls, indicating impaired top-down regulation. In contrast, this connectivity was preserved in misophonia for generally unpleasant sounds, suggesting intact regulation. The comorbid group showed neural patterns associated with both disorders. Overall, these findings reveal overlapping and disorder-specific neural patterns across sound tolerance profiles. Future research should combine neural and behavioral data to refine mechanistic models and guide targeted interventions.

**ИИ:** ? · выборка неясна · fMRI study of 91 young adults sorted into misophonia/hyperacusis/control groups; the full text may show screening of an unselected pool.

**Решение:** =

---

### 43 · R0098

**Decreased Sound Tolerance: School Functioning in Children and Findings from Otoacoustic Emissions [Elektronisk resurs]**

2026 · text

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Likely a Swedish thesis on decreased sound tolerance in school children; may include misophonia measures in unselected samples. No abstract.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 44 · R0099

**The Autonomous Sensory Meridian Response (ASMR) and Misophonia: Attention, Senses and Emotion. Part 1 of 3: Questionnaires.**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/vq45n

The Autonomous sensory meridian response (ASMR) and misophonia are two relatively understudied multisensory phenomena with small yet rapidly growing research fields. Misophonia is associated with negative affective responses such as anger, irritation, disgust, distress or rage and appears to be most commonly, but not exclusively, triggered by human-produced oral-nasal sounds (Andermane et al., 2023; Dixon et al., 2024). Individuals experiencing misophonia "lock on" to certain trigger sounds, such as chewing, breathing, sniveling or tapping, leading to discomfort and highly negative affective responses (Swedo et al., 2022). This, in turn, has consequences on daily life, from home environments to difficulty in academic and work environments. Prevalence rates of misophonia have been studied using a range of methods and using different populations. Although mild symptoms of misophonia can affect up to 50-78% of the population, more severe, clinically significant symptoms are far rarer, typically seen in 4-10% of the population. It is worth noting that although studies based on representative samples have been made, many are based on undergraduate samples across the globe. Additionally, measures used to score misophonia severity differs across studies. Misophonia is thought to most commonly start in childhood or early adolescence (Dixon et al., 2024; Jakubovski et al., 2022; Vitoratou et al., 2023). In ASMR, strong positive affective responses, such as tingling sensations, or “tingles”, decreased stress and heightened calm, are evoked by both social and non-social sounds, though not much is known about the physiology behind tingle-responses. The sounds triggering these highly pleasurable affective responses vary from person to person, from someone whispering in your ear, watching tasks be performed slowly and carefully, to object manipulation (Barratt & Davis, 2015; Barratt et al., 2017; Poerio et al., 2018). Previous research has highlighted important features in tingle-elicitation, including body-proximate information and directed attention as key factors (Jones et al., 2025). ASMR is also hypothesized to be connected to touch and somatosensation (Villena‐Gonzalez, 2023). To date, research on touch and ASMR has remained largely theoretical, and thus the evidentiary basis for the connection between touch and ASMR experience remains unknown. The involvement of human-related trigger stimuli may indicate a connection between the phenomena and interpersonal and potentially socially driven information, influencing both misophonic and ASMR responses. Although distinct in their respective affective and physical responses, there appears to be some overlap in that both ASMR and misophonia experience is related to heightened sensory sensitivity and involvement of similar triggering features (Poerio et al., 2022; Rinaldi et al., 2023). Further, a small number of articles have investigated possible connections between misophonia and ASMR (Janik McErlean & Banissy, 2018). Both ASMR and misophonia hold potentially high scientific value for the understanding of how auditory and visual sensory information is integrated in the brain and perceived in terms of affect and social cognition (such as how sensory information plays a role in social interaction and functioning). Further, both conditions also appear to primarily alter and affect emotional reactions, and could therefore have an integrated higher-level perceptual role, rather than be rooted alterations in lower-level auditory functions (Savard & Coffey, 2025). This larger project is divided into three studies, each with separate research questions and their own preregistration. The same participants will be invited to take part in all studies, which will take place in three separate waves (see sampling plan for an overview). We will in this online project aim to study misophonia and ASMR both separately and together from three standpoints, 1) through questionnaires measuring self-reported socioaffective traits, 2) through subjective experiences of sounds and 3) through attentional function and audiovisual integration via a dichotic listening task and by examining the McGurk effect. This preregistration covers part 1: “Questionnaires measuring self-reported socioaffective traits in ASMR and misophonia”. As indicated by previous research, ASMR and misophonia may share underlying traits (McGeoch & Rouw, 2020). There may also be aspects of social and affective psychological traits which are unique to each phenomenon. In this study, we aim to measure how these populations score on a battery of questionnaires measuring social-, affective- and sensory traits. This will serve as an initial step to investigate how these phenomena may fit into a broader socioaffecitve spectrum, which in turn could have effects on and ties to overall social functioning. In particular, we want to investigate the possible connection between misophonia and ASMR through a general over-responsivity to stimuli, which may be modulated through socioaffective traits. These traits may then determine whether over-responsiveness develops into aversive, pleasant or a combination of both in reaction to particular sounds. That is, while ASMR and misophonia may very well be separate in their affective response to sound, there may be converging underlying trait similarities. Outcomes: Anxiety total scores, reappraisal and suppression subscales of the ERQ, Sensory sensitivity using the GSQ Exploratory outcomes: autistic traits, social support. SMS and ASMR-15 scores, ATC scores.

**ИИ:** ? · выборка неясна · Preregistration of an online study using SMS. It is unclear whether participants are recruited for misophonia/ASMR or come from an unselected pool that gets classified.

**Решение:** -7 preregistration without data

---

### 45 · R0100

**The Autonomous Sensory Meridian Response (ASMR) and Misophonia: Attention, Senses and Emotion. Part 2 of 3 Attention and audiovisual integration**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/5a6n4

The Autonomous sensory meridian response (ASMR) and misophonia are two relatively understudied multisensory phenomena with small yet rapidly growing research fields. Misophonia is associated with negative affective responses such as anger, irritation, disgust, distress or rage and appears to be most commonly, but not exclusively, triggered by human-produced orofacial sounds (Andermane et al., 2023; Dixon et al., 2024). Individuals experiencing misophonia "lock on" to certain trigger sounds, such as chewing, breathing, sniveling or tapping, leading to discomfort and highly negative affective responses (Swedo et al., 2022). This, in turn, has consequences on daily life, from home environments to difficulty in academic and work environments. Prevalence rates of misophonia have been studied using a range of methods and using different populations. Although mild symptoms of misophonia can affect up to 50-78%, more severe, clinically significant symptoms are far rarer, typically seen in 4-10% of the population. It is worth noting that although studies based on representative samples have been made, many are based on undergraduate samples across the globe. Additionally, measures used to score misophonia severity differs across studies. Misophonia is thought to most commonly start in childhood or early adolescence (Dixon et al., 2024; Jakubovski et al., 2022; Vitoratou et al., 2023). In ASMR, strong positive affective responses, such as tingling sensations, or “tingles”, decreased stress and heightened calm, are evoked by both social and non-social sounds, though not much is known about the physiology behind tingle-responses. The sounds triggering these highly pleasurable affective responses vary from person to person, from someone whispering in your ear, watching tasks be performed slowly and carefully, to object manipulation (Barratt & Davis, 2015; Barratt et al., 2017; Poerio et al., 2018). Previous research has highlighted important features in tingle-elicitation, including body-proximate information and directed attention as key factors (Jones et al., 2025). ASMR is also hypothesized to be connected to touch and somatosensation (Villena‐Gonzalez, 2023). To date, research on touch and ASMR has remained largely theoretical, and thus the evidentiary basis for the connection between touch and ASMR experience remains unknown. The involvement of human-related trigger stimuli may indicate a connection between the phenomena and interpersonal and potentially socially driven information, influencing both misophonic and ASMR responses. Although distinct in their respective affective and physical responses, there appears to be some overlap in that both ASMR and misophonia experience is related to heightened sensory sensitivity and involvement of similar triggering features (Poerio et al., 2022; Rinaldi et al., 2023). Further, a small number of articles have investigated possible connections between misophonia and ASMR (Janik McErlean & Banissy, 2018). Both ASMR and misophonia hold potentially high scientific value for the understanding of how auditory and visual sensory information is integrated in the brain and perceived in terms of affect and social cognition (such as how sensory information plays a role in social interaction and functioning). Further, both conditions also appear to primarily alter and affect emotional reactions, and could therefore have an integrated higher-level perceptual role, rather than be rooted alterations in lower-level auditory functions (Savard & Coffey, 2025). This larger project is divided into three studies, each with separate research questions and their own preregistration. The same participants will be invited to take part in all studies, which will take place in three separate waves (see sampling plan for an overview). We will in this online project aim to study misophonia and ASMR both separately and together from three standpoints, 1) through questionnaires measuring self-reported socioaffective traits, 2) through subjective experiences of sounds and 3) through attentional function and audiovisual perception via a dichotic listening task and by examining the McGurk effect. This preregistration covers part 2: "selective attention and audiovisual integration ability in ASMR and misophonia". In this study, we want to investigate basic properties of selective attention and audiovisual integration ability in individuals with ASMR or misophonia. Previous research on attention and perception in ASMR and misophonia have been somewhat mixed. Misophonia has previously been associated with an increased accuracy on an attentional task (Simner et al., 2022) and selective attention during exposure to misophonic trigger sounds (Silva & Sanchez, 2019). There have also been reports of poorer performance on attention-related tasks (Frank et al., 2020). An increase in selective attention toward misophonic trigger stimuli has also been suspected to lead to worse attentional function surrounding other relevant events, which could impact performance across a multitude of daily tasks (Silva & Sanchez, 2019). For ASMR, scientific exploration of the role of attention is scarce, and has thus far not yielded any significant outcomes (see e.g., Engelbrekt et al., 2022). However, one important aspect of the efficacy of ASMR stimuli is the insinuation of mutual and shared attention, suggesting that one may need to attend to the stimuli in a particular way for them to be effective. Whether this carries over to more basic attentional mechanisms is unknown. In this study, we are using two tasks to measure attention in individuals with ASMR, misophonia and controls. By presenting both an auditory selective attention task (dichotic listening task) and a task aimed to measure audiovisual integration via the McGurk effect (phonemes task), we want to explore possible differences, or rule out differences in performance across the groups. McGurk task. This task consists of 138 trials. In the task, participants will view short videos in which a woman speaks a phoneme (e.g., "ba, ba") out load. The trials will either be congruent (mouth movement and sound matches) or incongruent (sound is not matched with the mouth movement). The McGurk effect emerges when a sound and a movement are presented simultaneously whilst not matching, creating the illusion that another sound is perceived which is different from the sound that is in fact presented. Dichotic listening task. This task consists of 150 trials. In this task, participants are tasked to listen to a specific cue and use that to answer a question. More specifically, they will be instructed to listen to either a female or a male voice, which will be played simultaneously in each ear (binaurally). The voices will each speak a number between 1 and 8. The task is to indicate with a button press whether the cued voice is speaking a number above or below 5. The voices will either both speak a number below or above 5 (congruent) or each voice will speak a number above or below 5 respectively (incongruent). E.g., in a congruent condition, the voices might speak the numbers "2" and "4", both being below 5. In an incongruent condition, one voice may speak the number "2" whilst the other speaks the number "7", one below and one above 5. We first seek to rule out that ASMR and misophonia can be reduced to attentional factors; by using the McGurk illusion, we will be able to compare functioning of audiovisual integration across groups. If variability within the groups is comparable to each other, this will indicate that ASMR and misophonia population do not differ from a normal population in the integration of auditory and visual stimuli. If the groups are comparable, it will indicate that whatever is causing ASMR- and misophonia populations to perceive stimuli differently is happening at another, possibly higher level. While the McGurk effect relates to speech, similar patterns have been explored for other features. For instance, a study has developed a database with stimuli using the principals relating to the McGurk effect to lower misophonic responses, (tested through manipulated audiovisual videos containing misophonic audio with misophonic video, or with innocuous videos matching the original sound e.g. a broom sweeping instead of a person sniffling) (Samermit et al., 2022). We aim to test attentional processing without misophonic, or ASMR stimuli present, to evaluate the basic attentional functioning within the groups. Looking at selective attention comes from previous findings which have used an attentional task using pattern recognition. The results there indicated that severe misophonia was connected to increased accuracy on attentional tasks (Simner et al., 2022), with accuracy increasing with severity of misophonic symptoms. Theories surrounding increased attention to detail, sustained focus, or inability to disengage from sensory inputs are used as explanations for the misophonic response. If misophonia is connected to increased attentional accuracy due to problems in disengagement and an increased attention to detail, they may also differ from a “normal population” in tasks requiring selective attention. If we believe that both an ASMR population and a misophonia population have sensory over-responsivity as a shared trait, then we might see similar patterns of increased accuracy on selective attention due to e.g., increased attention to detail. If, however, this over responsivity only pertains to specific stimuli, then basic attentional mechanisms may be intact without the presence of the stimuli. The selective attention task will be conducted once without priming and once after completing ASMR and misophonia audio rating tasks, to investigate any effect that salient stimuli may have on performance. Outcomes: accuracy and reaction time on selective attention and audiovisual integration tasks across an ASMR, misophonia and comparison

**ИИ:** ? · выборка неясна · Preregistration comparing ASMR, misophonia and control groups; unclear whether groups come from screening an unselected online pool or targeted recruitment.

**Решение:** -7 preregistration without data

---

### 46 · R0101

**The Autonomous Sensory Meridian Response (ASMR) and Misophonia: Attention, Senses and Emotion. Part 3 of 3 Sound Ratings**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/ymfq3

The Autonomous sensory meridian response (ASMR) and misophonia are two relatively understudied multisensory phenomena with small yet rapidly growing research fields. Misophonia is associated with negative affective responses such as anger, irritation, disgust, distress or rage and appears to be most commonly, but not exclusively, triggered by human-produced oral-nasal sounds (Andermane et al., 2023; Dixon et al., 2024). Individuals experiencing misophonia "lock on" to certain trigger sounds, such as chewing, breathing, sniveling or tapping, leading to discomfort and highly negative affective responses (Swedo et al., 2022). This, in turn, has consequences on daily life, from home environments to difficulty in academic and work environments. Prevalence rates of misophonia have been studied using a range of methods and using different populations. Although mild symptoms of misophonia can affect up to 50-78% of the population, more severe, clinically significant symptoms are far rarer, typically seen in 4-10% of the population. It is worth noting that although studies based on representative samples have been made, many are based on undergraduate samples across the globe. Additionally, measures used to score misophonia severity differs across studies. Misophonia is thought to most commonly start in childhood or early adolescence (Dixon et al., 2024; Jakubovski et al., 2022; Vitoratou et al., 2023). In ASMR, strong positive affective responses, such as tingling sensations, or “tingles”, decreased stress and heightened calm, are evoked by both social and non-social sounds, though not much is known about the physiology behind tingle-responses. The sounds triggering these highly pleasurable affective responses vary from person to person, from someone whispering in your ear, watching tasks be performed slowly and carefully, to object manipulation (Barratt & Davis, 2015; Barratt et al., 2017; Poerio et al., 2018). Previous research has highlighted important features in tingle-elicitation, including body-proximate information and directed attention as key factors (Jones et al., 2025). ASMR is also hypothesized to be connected to touch and somatosensation (Villena‐Gonzalez, 2023). To date, research on touch and ASMR has remained largely theoretical, and thus the evidentiary basis for the connection between touch and ASMR experience remains unknown. The involvement of human-related trigger stimuli may indicate a connection between the phenomena and interpersonal and potentially socially driven information, influencing both misophonic and ASMR responses. Although distinct in their respective affective and physical responses, there appears to be some overlap in that both ASMR and misophonia experience is related to heightened sensory sensitivity and involvement of similar triggering features (Poerio et al., 2022; Rinaldi et al., 2023). Further, a small number of articles have investigated possible connections between misophonia and ASMR (Janik McErlean & Banissy, 2018). Both ASMR and misophonia hold potentially high scientific value for the understanding of how auditory and visual sensory information is integrated in the brain and perceived in terms of affect and social cognition (such as how sensory information plays a role in social interaction and functioning). Further, both conditions also appear to primarily alter and affect emotional reactions, and could therefore have an integrated higher-level perceptual role, rather than be rooted alterations in lower-level auditory functions (Savard & Coffey, 2025). This larger project is divided into three studies, each with separate research questions and their own preregistration. The same participants will be invited to take part in all studies, which will take place in three separate waves (see sampling plan for an overview). We will in this online project aim to study misophonia and ASMR both separately and together from three standpoints, 1) through questionnaires measuring self-reported socioaffective traits, 2) through subjective experiences of sounds and 3) through attentional function and audiovisual perception via a dichotic listening task and by examining the McGurk effect. This preregistration covers part 3: "ratings of ASMR and misophonia audio stimuli in ASMR and misophonic populations". This study aims to further elucidate affective response profiles from populations experiencing unusual affective responses to specific sounds, namely ASMR and Misophonia. This study aims to disentangle controls from overresponsive populations experiencing ASMR, Misophonia or both, through an audio rating task. Sounds will consist of control, ASMR and misophonia-related trigger stimuli. Audio will be selected from audio files produced by Andermane et al., 2023, originally sourced from Freesound, for consistency as previous research efforts (see , e.g., Andermane et al., 2023; Orloff et al., 2023) have used the sound data base for research on misophonia and ASMR. Standardized sounds are used in this study as a step toward building replicability across both misophonia and ASMR research. ASMR sounds from ASMRtist 'GibiASMR', used with permission, will be added to expand the number of ASMR audio stimuli. Additional scrambling of new added stimuli and for previously used but not scrambled ASMR stimuli was created through time-domain scrambling of audio signals in Matlab, which was previously done for some of the stimuli in Andermane et al., (2023) While there are a small number of studies linking ASMR and misophonia (Janik McErlean & Banissy, 2018; McGeoch & Rouw, 2020), recent previous research has provided data to suggest that ASMR and misophonia are separate phenomena with distinct phenomenological profiles (Andermane et al., 2023) . We want to further investigate the possibility distinct profiles of the two phenomena. Outcomes: Trigger/tingle frequency ratings across an ASMR, misophonia and comparison group.

**ИИ:** ? · выборка неясна · Pre-registration with ASMR, misophonia and comparison groups; unclear whether groups come from screening an unselected online pool or targeted recruitment.

**Решение:** -7 preregistration without data

---

### 47 · R0102

**Adaptation and Validation of the Amsterdam Misophonia Scale (A-MISO-S) in Nepali**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-10123589/v1

Abstract Aim and Objective This study aimed to translate and validate the Amsterdam Misophonia Scale (A-MISO-S) into Nepali. Methods The A-MISO-S was translated to Nepali following ISPOR guidelines, including forward and back translation, cognitive debriefing, and an expert review. A cross-sectional study was conducted among individuals with self-reported misophonia symptoms visiting a tertiary care hospital in Nepal. A total of 64 participants completed the Nepali version. Content validity was assessed using the Content Validity Index (CVI). Construct validity was evaluated using Principal Component Analysis (PCA), with Kaiser–Meyer–Olkin (KMO) and Bartlett’s Test of Sphericity assessing data suitability. Internal consistency was measured using Cronbach’s alpha. Results The mean total score was 4.83 (SD = 4.04), with 60.9% of participants demonstrating subclinical symptoms. Content validity was excellent (S-CVI = 0.92; I-CVI = 0.80–1.00). The KMO value (0.821) and significant Bartlett’s test (p

**ИИ:** ? · выборка неясна · Nepali A-MISO-S validation; sample had self-reported symptoms, but the low mean score suggests hospital visitors may have been screened.

**Решение:** =

---

### 48 · R0104

**Obsesif Kompulsif Bozukluk Tanılı Hastalarda Anksiyete Duyarlılığı, Mizofoni Ve Bilinçli Farkındalık Arasındaki İlişki - Ön Çalışma**

2026 · Turkish Journal of Psychiatry · article, journalarticle · en · https://doi.org/10.5080/61upk.ozt158

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · клиническая группа · OCD patients assessed for misophonia, anxiety sensitivity and mindfulness; clinical group recruited for another condition; no abstract.

**Решение:** =

---

### 49 · R0105

**Assessment of misophonia, hyperacusis, and tinnitus using questionnaires in patients with low- and high-frequency hearing loss who will use hearing devices**

2026 · Praxis of Otorhinolaryngology · article, journalarticle, review · und · https://doi.org/10.5606/kbbu.2026.16023

Objectives: This study aims to evaluate the frequency and severity of misophonia, hyperacusis, and tinnitus in patients with low- and high-frequency hearing loss using standardized questionnaires. Patients and Methods: This cross-sectional study, conducted between 01.05.2025 and 31.08.2025, included 100 patients (52 males, 48 females; mean age 62.5±13.8 year; range, 14 to 95 year) classified into low-, high-, or mixed-frequency hearing loss groups. Misophonia was assessed using the Misophonia Questionnaire (MISO), hyperacusis using the Hyperacusis Scale, and tinnitus using a standardized tinnitus survey. Associations between hearing loss type and symptom severity were analyzed using Chi-square tests, Monte Carlo simulations, Cramér’s V statistics, and logistic regression analyses. Effect sizes were estimated using bootstrap methods. Results: Among auditory sensitivity disorders, tinnitus showed a significant association with frequency-specific hearing loss (p&lt;0.05). In contrast, no statistically significant associations were found for misophonia or hyperacusis. Frequency loss was significantly associated with misophonia, hyperacusis, and tinnitus (Cramér’s V=0.61-0.73, permuted p&lt;0.001). Gender was independently associated with hyperacusis (OR≈3, p=0.046). A moderate positive correlation was observed between misophonia and hyperacusis severity (Spearman ρ=0.29, p=0.01). Subgroup analyses by age and gender revealed similar trends. Conclusion: Tinnitus is more prevalent in individuals with frequency-specific hearing loss, highlighting the need for individualized assessment prior to hearing aid fitting. Although misophonia and hyperacusis are commonly observed, no significant associations with audiometric patterns were identified.

**ИИ:** + · клиническая группа · Hearing-loss patients, not recruited for misophonia, assessed with the Misophonia Questionnaire; reports how often misophonia occurs.

**Решение:** =

---

### 50 · R0106

**Misophonia in Individuals with Obsessive-Compulsive Disorder: Its Relationship with Anxiety Sensitivity and Mindfulness.**

2026 · Medicina (Kaunas, Lithuania) · article, journal article, journalarticle · eng · https://doi.org/10.3390/medicina62010216

Background and Objectives: This study aimed to examine the severity of misophonia symptoms in individuals diagnosed with obsessive&ndash;compulsive disorder (OCD) and to evaluate the pattern of the relationship between misophonia and OCD symptom severity in relation to anxiety sensitivity and mindfulness. Materials and Methods: This comparative and cross-sectional study included 108 patients diagnosed with OCD according to DSM-5 criteria and 81 healthy control subjects without any psychiatric diagnosis. Participants completed the Misophonia Symptom List (MSL), Anxiety Sensitivity Index-3 (ASI-3), Mindful Attention Awareness Scale (MAAS), Yale&ndash;Brown Obsessive Compulsive Scale (Y-BOCS), and Beck Anxiety Inventory (BAI). Statistical analyses included group comparisons, Pearson correlations, multiple linear regression, and mediation analyses using the PROCESS macro. Results: MSL scores were significantly higher in the OCD group compared to the control group (104.10 &plusmn; 33.00 vs. 87.56 &plusmn; 20.07, p &lt; 0.001). ASI-3 (33.53 &plusmn; 18.72 vs. 18.12 &plusmn; 11.55, p &lt; 0.001) and BAI scores (20.74 &plusmn; 13.14 vs. 11.04 &plusmn; 8.47, p &lt; 0.001) were higher; MAAS scores were lower (53.23 &plusmn; 14.92 vs. 60.72 &plusmn; 12.70, p &lt; 0.001). In the OCD group, MSL scores were positively correlated with anxiety sensitivity (r = 0.626, p &lt; 0.001) and Beck anxiety (r = 0.515, p &lt; 0.001) and negatively correlated with MAAS (r = &minus;0.357, p &lt; 0.001). In multiple regression analysis, anxiety sensitivity was identified as the only variable significantly predicting misophonia severity (&beta; = 0.523, p &lt; 0.001). Mediation analyses showed that anxiety sensitivity emerged as the dominant indirect pathway between OCD symptom severity and misophonia, whereas the contribution of mindfulness was not independent of anxiety sensitivity in the serial mediation model. Conclusions: The findings indicate that misophonia symptoms are significantly elevated in individuals diagnosed with OCD and that these symptoms are particularly associated with cognitive-emotional variables such as anxiety sensitivity and mindfulness. Given the cross-sectional design, the mediation findings should be interpreted as indirect associations rather than evidence of causal pathways. Considering these variables may be useful in assessing misophonia symptoms accompanying OCD and planning clinical approaches

**ИИ:** + · клиническая группа · OCD patients and healthy controls assessed with the Misophonia Symptom List; the full text may report how many meet a cutoff.

**Решение:** =

---

### 51 · R0107

**Factors associated with misophonia in children.**

2026 · International journal of pediatric otorhinolaryngology · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.ijporl.2025.112681

… ., which reported that the prevalence of hyperacusis in children and adolescents ranges from 3 % to 17 % [7]. The prevalence of misophonia in the general pediatric population remains …

**ИИ:** ? · выборка неясна · Empirical study of factors linked to misophonia in children. The abstract is only a snippet, so it's unclear how the sample was recruited; full text needed.

**Решение:** =

---

### 52 · R0108

**Misophonia as a Psychological Correlate of Anxiety and Depression: The Mediating Role of Obsessive-Compulsive Symptoms**

2026 · google scholar result · https://www.sid.ir/paper/1928721/en

… Approximately 28% of individuals with misophonia present with clinically significant symptoms of co-occurring psychiatric conditions, with major depressive disorder, attention-deficit/…

**ИИ:** ? · выборка неясна · Correlational study measuring misophonia with anxiety/depression/OCD; the snippet doesn't describe the sample, which may be unselected.

**Решение:** =

---

### 53 · R0114

**Sensory Processing, Dissociation, and Affective Symptoms in Misophonia: A Cross-Sectional Study of 35 Adults.**

2026 · Medical science monitor : international medical journal of experimental and clinical research · article, journal article, journalarticle · eng · https://doi.org/10.12659/msm.950938

BACKGROUND Misophonia provokes intense reactions to everyday sounds and is linked to sensory and psychiatric symptoms; the role of dissociation remains unclear, so we compared these features in adults with misophonia and controls. MATERIAL AND METHODS In a cross-sectional online survey, adults aged 18-65 years (n=86) were classified into a misophonia group (n=35) and controls (n=51) using the Misophonia Questionnaire (MisoQuest; cut-off ≥7). Sensory processing was assessed with the Adolescent/Adult Sensory Profile (A/ASP), dissociation with the Dissociative Experiences Scale (DES), and depression, anxiety, and stress with the Depression Anxiety Stress Scale-21 (DASS-21). Between-group comparisons used independent t tests or Mann-Whitney U and χ² (Monte Carlo when needed); associations used Spearman correlations; predictors were examined via hierarchical multiple regression (two-tailed alpha=.05). RESULTS The misophonia group scored higher than controls on misophonia symptoms, sensory sensitivity, avoidance, dissociative experiences, depression, anxiety, and stress (all P<.001). Misophonia symptoms correlated with sensory sensitivity (r=.717, P<.001), dissociation (r=.348, P<.001), and psychological distress (r=.440, P<.001). In regression, sensory sensitivity (ß=.308, P=.025), avoidance (ß=.319, P=.010), and seeking (ß=.239, P=.004) independently predicted MisoQuest scores; demographic and psychiatric covariates were non-significant (all P≥.05). CONCLUSIONS Misophonia is characterized by heightened sensory sensitivity and avoidance, with moderate links to dissociation, supporting routine assessment of these sensory and psychiatric domains.

**ИИ:** ? · выборка неясна · An online survey of 86 adults was split into groups by MisoQuest cut-off; unclear if sample was unselected (35/86) or recruited for misophonia.

**Решение:** =

---

### 54 · R0115

**Misophonia: A Disorder of Emotion Processing of Sounds**

2026 · Newcastle University · conferenceproceeding/conference contribution · https://doi.org/10.25405/ncl.34236561

No description provided

**ИИ:** ? · нет аннотации · Conference contribution with no abstract. It is likely Kumar-group work on selected misophonia participants, but the sample can't be confirmed.

**Решение:** =

---

### 55 · R0117

**The brain basis for misophonia**

2026 · Newcastle University · journalarticle/journal contribution · https://doi.org/10.25405/ncl.34298076.v1

No description provided

**ИИ:** ? · нет аннотации · No abstract; likely a data deposit linked to Kumar et al. 2017 neuroimaging study, which probably recruited misophonia cases. Check the sample.

**Решение:** =

---

### 56 · R0118

**Prevalence of Misophonia in High School Students: A Cross Sectional Study.**

2026 · The Psychiatric quarterly · article, journal article, journalarticle · eng · https://doi.org/10.1007/s11126-026-10264-9

Abstract Misophonia is a disorder characterized by decreased tolerance to specific sounds or stimuli associated with these sounds, such as oral, nasal, or instrument-generated noises. Reported prevalence rates vary widely, ranging from 5% to 49%, with limited studies among children. Therefore, this study aimed to investigate the prevalence of misophonia among children presenting to a public hospital for any reason. 1,006 high school students attending six high schools in Kahta district of Adıyaman province, voluntarily participated in the study. Each completed a sociodemographic data form and the Misophonia Questionnaire. Clinically significant misophonia was found in 49.7% (n = 500) of students. Higher misophonia scores were observed among female students, those reporting high stress during exam periods, those with poor parental relationships, and those with poor general health (p &lt; 0.05). Students who described themselves as introverted, emotional, indecisive, rule-oriented, ambitious, or detail-oriented had significantly higher misophonia scores than their peers (p &lt; 0.05). This study demonstrates a high prevalence of clinically significant misophonia among high school students in Türkiye and highlights its association with various stress factors and certain personality traits. Future research should focus on individuals with elevated misophonia symptoms to determine, through standardized clinical evaluations, the proportion that meets the criteria for a clinical disorder and to investigate the related sociodemographic and clinical features and the course of the condition.

**ИИ:** + · исследование распространённости · Cross-sectional prevalence survey of 1,006 Turkish high school students using the Misophonia Questionnaire; reports 49.7% clinically significant misophonia.

**Решение:** =

---

### 57 · R0119

**The Mediating Role of Emotion Regulation Difficulties in the Relationship Between Childhood Trauma and Misophonia: A Cross-Sectional Study of University Students**

2026 · Behavioral Psychology/Psicología Conductual · journalarticle, article, journal article · en · https://doi.org/10.31083/bp45905

Background:Misophonia is a sound intolerance characterized by intense emotional and physiological responses to specific repetitive sounds, often impairing functioning. Childhood trauma (CT) may elevate the risk of misophonia through its impact on emotion regulation difficulties (ERDs).Methods:We conducted a cross-sectional study of university students (N = 294; mean age = 23.4 ± 5.0; 71.4% female). Participants completed the Childhood Trauma Questionnaire (CTQ), the Difficulties in Emotion Regulation Scale (DERS), and a misophonia Scale. Pearson correlations were calculated, and mediation analysis was performed to test DERS as a mediator between CTQ scores and misophonia.Results:CTQ, DERS, and misophonia were all positively correlated. CTQ showed a significant total effect on misophonia (b = 0.31, 95% confidence interval [CI]: 0.15, 0.46). When DERS was included in the model, the direct effect of CTQ on misophonia was not significant (b = 0.08, 95% CI: –0.06, 0.23), while the indirect effect via DERS was significant (b = 0.22, 95% CI: 0.13, 0.34).Conclusions:Findings are consistent with a full mediation model, with DERS statistically accounting for the association between CTQ and misophonia. Trauma-related impairments in emotion regulation may represent key factors contributing to misophonia. Longitudinal studies are needed to establish temporal and causal pathways.</jats:p

**ИИ:** + · ненабранная выборка · Cross-sectional survey of 294 university students that measured misophonia with a questionnaire; the full text may report how many met a case definition.

**Решение:** =

---

### 58 · R0122

**Introducing the ASMR-sens: a reliable and valid questionnaire specifically assessing ASMR sensation**

2026 · Current Psychology · article · en · https://doi.org/10.1007/s12144-026-09547-y

Abstract The ASMR-Sens is a newly developed questionnaire for reliably assessing the core phenomenon of Autonomous Sensory Meridian Response (ASMR): a tingling sensation, typically occurring on the skin of the neck and back of the head. Existing tools are too lengthy or lack focus on the core sensory ASMR experience. This study aimed to create a concise, valid instrument for evaluating ASMR sensations. A total of 345 participants viewed one of four video types (ASMR, walking tour, relaxation or screensaver) and completed 60 ASMR-related items and other established questionnaires. From the set of 60 items, 10 items were selected to form the ASMR-Sens, which showed a unidimensional factor structure and high internal consistency (Cronbach’s Alpha = 0.976). The ASMR-Sens demonstrated strong criterion-related validity, moderate convergent validity with the ASMR-15, and discriminant validity regarding constructs like sensory processing sensitivity and mindfulness. This robust tool offers a reliable method for advancing ASMR research.

**ИИ:** ? · другое · ASMR questionnaire validation in an unselected sample. The abstract lists unnamed "other established questionnaires", which might include a misophonia measure.

**Решение:** -6 не про мизофонию

---

### 59 · R0126

**The Relationships Among Tinnitus Intensity, Complexity, Sound Intolerance, and Psychiatric Symptoms.**

2026 · Journal of clinical medicine · journal article, journalarticle, article · eng · https://doi.org/10.3390/jcm15166382

Objective: This study investigated the associations between tinnitus-related features, psychological symptoms, and everyday functioning. Material and Methods: In this study, 293 patients with primary subjective tinnitus participated. Participants received otorhinolaryngological and audiological evaluations and completed the Tinnitus Handicap Inventory (THI), Beck Depression Inventory (BDI), and Generalised Anxiety Disorder-7 (GAD-7) questionnaires. Results: Significant positive correlations were observed between total THI scores and several tinnitus characteristics, including subjective loudness, pitch, complexity, and sound intolerance. Higher THI scores were also associated with higher depression and anxiety scores. Psychoacoustically matched tinnitus intensity was positively correlated with perceived tinnitus loudness; however, no significant association was found between overall THI scores and psychoacoustic tinnitus intensity. Longer tinnitus duration was positively correlated with both tinnitus loudness and participant age, while age was also positively associated with tinnitus loudness. Subjective tinnitus loudness, pitch, complexity, and sound intolerance were positively correlated with both BDI and GAD-7 scores. After applying the Bonferroni correction for multiple comparisons, the following correlations were no longer statistically significant: psychoacoustic tinnitus intensity with subjective tinnitus loudness and the THI Functional (F) subscale; tinnitus duration with subjective tinnitus loudness; subjective tinnitus loudness with BDI and GAD-7 scores; and age with subjective tinnitus loudness and tinnitus pitch. However, all remaining significant correlations were retained. In linear regression analyses, THI scores were independently associated with sound intolerance, tinnitus pitch, and BDI scores, while THI scores were also independently associated with BDI scores and sound intolerance in reciprocal models. Conclusions: In this single-centre, cross-sectional study of patients with tinnitus and without a control group, greater tinnitus handicap was associated with subjective tinnitus pitch, sound intolerance, and depressive symptoms. Subjective tinnitus loudness was positively associated with psychoacoustically matched tinnitus intensity before correction for multiple testing but was not retained after Bonferroni adjustment. Several subjective tinnitus characteristics remained associated with symptoms of depression and anxiety after adjustment for multiple comparisons. These findings describe associations within the studied population and should not be interpreted as evidence of causal relationships or generalised beyond similar clinical populations without further multicentre, longitudinal, controlled studies.</jats:p

**ИИ:** ? · другое · Tinnitus clinical sample assessed for 'sound intolerance'; the full text may break this down into misophonia, but the abstract never mentions misophonia.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 60 · R0130

**Perceived Social Support as a Moderator of the Relationship Between Misophonia Symptoms and Depression.**

2026 · ReIn UW (University of Warsaw) · review · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract. The title suggests an empirical study of misophonia symptoms in a possibly unselected sample, likely a thesis; the "review" label may be wrong.

**Решение:** =

---

### 61 · R0131

**Pediatric Misophonia & Hyperacusis**

2026 · Unpublished · conference object, text/poster, article · und · https://doi.org/10.13140/rg.2.2.18321.19047

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Conference poster on pediatric misophonia and hyperacusis with no abstract; it might report prevalence or a clinical sample.

**Решение:** =

---

### 62 · R0134

**Beyond the Auditory System: Sensory Processing in Decreased Sound Tolerance Disorders.**

2026 · Multisensory research · article, journal article, journalarticle · eng · https://doi.org/10.1163/22134808-bja10185

This study aims to investigate the correlation between decreased sound tolerance disorders and sensory processing disorder, as well as the sensory systems that are affected when decreased sound tolerance disorders exist. The study included 315 individuals aged 18-35 with normal hearing and no neurological disorders. Participants completed the Decreased Sound Tolerance Disorder Scale (DSTS) and the Adult Sensory Processing Scale (ASPS). According to the DSTS, 278 individuals with decreased sound tolerance disorders were included as the study group, and 37 individuals without decreased sound tolerance were included as a control group. The DSTS includes 33 items assessing symptoms of hyperacusis, phonophobia, and misophonia. The ASPS consists of 48 items across 11 factors that assess the sensitivity of different sensory domains. The distribution of decreased sound tolerance disorders among the participants indicated that 113 participants (35.9%) had all three types of DSTs (triple DST), 85 participants (27.0%) had two types of DSTs (dual DST), 16 participants (5.1%) had hyperacusis only, 14 participants (4.4%) had phonophobia only, 50 participants (15.9%) had misophonia only, and 37 participants (11.7%) had no DSTs (non-DST). A moderately positive correlation was found between the total scores of the ASPS and hyperacusis ( r = 0.260, p < 0.001), and misophonia ( r = 0.348, p < 0.001) scores. Total ASPS scores were higher in those with misophonia compared to those without ( p < 0.05). The results of this study indicate that individuals with decreased sound tolerance may have difficulty in processing not only auditory but also visual, vestibular, proprioceptive, and tactile stimuli.

**ИИ:** + · ненабранная выборка · 315 adults with normal hearing were screened with the DSTS, which includes misophonia items. The abstract reports misophonia proportions, so the sample appears unselected.

**Решение:** =

---

### 63 · R0138

**Patterns of shared and differential neural activity in misophonia and non-misophonic clinical emotional dysregulation.**

2026 · BMC psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.1186/s12888-026-08331-3

Misophonia is a poorly understood clinical condition characterized by reduced tolerance to select trigger sounds. Whether misophonic distress and its regulation involve unique neural mechanisms compared to other forms of emotion dysregulation remains unclear. We used functional magnetic resonance imaging (fMRI) to identify putative neural signatures of misophonic reactivity and regulation compared to a transdiagnostic clinical control group. Twenty-nine adults with misophonia and 30 with high emotional dysregulation and a DSM-5 psychiatric disorder underwent an fMRI session. After the presentation of misophonic, aversive, or neutral sound cues, they either experienced emotions naturally or reduced negative affect through cognitive reappraisal. Compared to controls, participants with misophonia showed greater distress after listening to or downregulating misophonic sounds and lower distress when listening to non-misophonic aversive sounds. Listening to misophonic sounds elicited lower functional connectivity between the right insula and the left dorsomedial prefrontal cortex (dmPFC), and between the left insula and the right superior temporal sulcus, in the misophonia group compared with controls. During the regulation of misophonic sounds, the misophonia group showed increased left insula connectivity with the anterior cingulate cortex and increased right insula connectivity with the bilateral dmPFC and other sensorimotor regions compared to controls. In the misophonia group only, higher emotion dysregulation and lower habitual use of reappraisal were respectively associated with increased insula-dmPFC connectivity and with increased insula connectivity with the dorsolateral prefrontal cortex. Prefrontal cortex activation during regulation of misophonic distress was not significantly different between the two groups. Insula activity and connectivity may be key features that distinguish misophonia from other forms of emotional dysregulation. These novel findings identify candidate neural processes that may be selectively associated with misophonia, as well as processes that may be shared between misophonia and other forms of emotion dysregulation.

**ИИ:** ? · другое · Misophonia group recruited for misophonia, but the full text may report misophonia screening of the transdiagnostic emotion-dysregulation clinical controls.

**Решение:** =

---

### 64 · R0140

**Auditory attention and speech perception in misophonia**

2026 · The Journal of the Acoustical Society of America · journalarticle, conference-abstract, journal article · en · https://doi.org/10.1121/10.0045872

Misophonia is a disorder of decreased tolerance to specific sounds, called triggers. Previous research suggests that misophonia is grounded in fundamental differences in auditory attention that may also be implicated in speech perception. Speech perception in misophonia is extremely understudied and conveys mixed results. One hypothesis is that misophones maintain a state of hypervigilance or hyperarousal in conditions in which triggers are likely. Such heightened arousal could affect performance on complex, attention-dependent listening tasks like understanding speech in noise. However, it is not clear whether observed group-level differences are due to trait-level differences in auditory attention or context-dependent differences in arousal, or some combination. Here, we present preliminary results from an ongoing study of auditory attention and speech perception with misophones and controls. We evaluate listeners’ auditory attention using the Auditory Attention Test (AAT) and perception of speech in multi-talker babble under conditions of typical versus heightened arousal (trigger threat). Self-reported and physiological measures of arousal and stress, including heart rate and electrodermal activity, are collected and analyzed alongside behavioral test scores. Findings will clarify whether misophonic “hypervigilance” reflects a clinical-level attentional alteration, how attentional differences affect speech perception, and could inform interventions targeting attentional control.</jats:p

**ИИ:** ? · выборка неясна · Conference abstract comparing misophones with controls; unclear whether groups came from screening an unselected pool or targeted recruitment.

**Решение:** =

---

### 65 · R0143

**Meaning transfer and conditioned anger to orofacial sounds: A referential learning model of misophonia.**

2026 · Behaviour research and therapy · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.brat.2026.105097

When confronted with orofacial sounds such as chewing or breathing, persons with misophonia react with intense anger and disgust, accompanied by perceived meanings of intrusion, violation of personal boundaries, offence, or diminished autonomy. To build a laboratory model of how such responses can be acquired, a first study (N = 92) tested an anger provocation emotional imagery scenario, hypothesized to evoke misophonic meanings in student population. Using a differential conditioning procedure, a second study with non-misophonic participants (N = 64) tested whether these misophonic responses could be experimentally conditioned to an orofacial sound. In the acquisition phase, one sound (eating/sniffling) (CS+) was paired 3 times with the provocative scenario (US), whereas a control sound (sniffling/eating) (CS-) with a control relaxation scenario. Both sounds were presented without imagery in a subsequent test and extinction phase. To test whether conditioned responses would generalise, orofacial sounds similar to the CSs were presented before acquisition and after the test phase. Participants rated experienced emotions and meanings after each trial, while heart rate, respiration, and corrugator muscle activity were recorded during stimulus presentation. Test phase results showed that relative to the CS- sound, the CS + sound was associated with higher self-reported anger, violation, offence, and with a higher heart rate. These conditioned responses failed to extinguish, and did not generalise to sounds that were similar to the CSs. These findings demonstrate that misophonic responses can be conditioned to orofacial sounds, supporting the role of referential learning as a potentially etiological process underlying misophonia.

**ИИ:** ? · скрининг пула · Conditioning experiment in students; the "non-misophonic participants" suggest a misophonia screen, so the full text may report how many screened positive.

**Решение:** =

---

### 66 · R0144

**Misophonia and Internet Addiction Among Nursing, Midwifery, and Emergency Medical Services Students: A Cross-sectional Study**

2026 · Research Square · article, preprint · und · https://doi.org/10.21203/rs.3.rs-8748692/v1

Abstract Background Misophonia is a sensory sensitivity condition characterized by intense emotional reactions (such as anger, anxiety, and avoidance) to everyday sounds, often impairing psychological well-being and social functioning. Internet addiction, a growing behavioral health concern among university students, has been linked to emotional dysregulation and various mental health problems. However, limited research has examined the association between misophonia and internet addiction, particularly in non-Western student populations. Objective This study aimed to examine the association between misophonia and internet addiction among nursing, midwifery, and emergency medical services students in Iran. Methods This cross-sectional study was conducted in 2024 among 277 students at the Faculty of Nursing and Midwifery, Hamadan University of Medical Sciences, using stratified random sampling. Data were collected using the Misophonia Questionnaire (Wu et al., 2014) and the Internet Addiction Test (Young, 1998). Descriptive statistics, Pearson’s correlation coefficients, independent t-tests, and ANOVA were performed using SPSS. Results The mean internet addiction score was 41.45 ± 12.13, with 25.6% of participants classified as at risk of internet addiction. The mean misophonia score was 26.00 ± 12.59. Internet addiction showed a significant positive correlation with total misophonia scores (r = 0.377, p &lt; 0.001), with a stronger association observed for the emotions/behaviors subscale (r = 0.410, p &lt; 0.001) than for misophonia symptoms (r = 0.259, p &lt; 0.001). Higher internet addiction scores were reported among male students, nursing students, and those in higher academic years. Conclusions These findings suggest that problematic internet use may be associated with heightened emotional reactivity to sensory stimuli among university students. The results highlight the importance of psychological screening and preventive interventions targeting both behavioral addictions and sensory sensitivities to support student mental health. Longitudinal studies are recommended to clarify causal pathways and underlying psychological mechanisms.

**ИИ:** + · ненабранная выборка · Stratified random sample of 277 nursing, midwifery and emergency medical services students measured with the Misophonia Questionnaire; the full text may give a case count.

**Решение:** =

---

### 67 · R0145

**SENSORY PROCESSING SENSITIVITY AND ADULT ATTACHMENT IN PRONENCY TO MISOPHONIA**

2026 · Repository of Wyższa Szkoła Biznesu – National-Louis University (Wyższa Szkoła Biznesu – National-Louis University) · dissertation · pl

Przedstawiona praca badawcza jest ukierunkowana na analizę zależności zachodzących między wysoką wrażliwością sensoryczną oraz wykształconego stylu przywiązania u badanych osób dorosłych a ich skłonnością do mizofonii. Mizofonia jest obniżoną tolerancją na bodźce akustyczne o charakterze selektywnym i bardzo często dotyczącym dźwięków generowanych przez inne osoby np. mlaskanie, przeżuwanie, połykanie itp. W projekcie badawczym wzięło udział 160 respondentów, z których poprzez wypełnienie Kwestionariusza MisoQuest autorstwa M. Siepsiak, A. Śliwerski, W. Ł. Dragan, wyłoniono osoby o nasilonej oraz obniżonej nadwrażliwości dźwiękowej. Kwestionariusz Stylów Przywiązaniowych (KSP) M. Plopa oraz Polska adaptacja narzędzia Highly Sensitive Person Scale E. N. Aron i A. Aron - Kwestionariusz HSPS-10 umożliwiły uzyskanie wyników na temat poziomu wysokiej wrażliwości na bodźce z otoczenia oraz charakter stylu przywiązania badanych osób. Najsilniejsze potwierdzenie uzyskały hipotezy odnoszące się do związku wysokiej wrażliwości sensorycznej ze skłonnością do mizofonii. Słabsze i mniej jednoznaczne wyniki dotyczyły powiązań między mizofonią a stylami przywiązania. W szczególności jedynie lękowo-ambiwalentny styl przywiązania wykazał istotny związek z nasileniem mizofonii, i to tylko w grupie badawczej. Styl unikowy nie wykazał istotnej zależności z mizofonią, mimo dodatniego kierunku współczynników korelacji, natomiast styl bezpieczny nie pozostawał w istotnym statystycznie związku z nasileniem objawów mizofonicznych. Wyniki te wskazują, że w badanej próbie kluczową rolę odgrywała przede wszystkim wysoka wrażliwość przetwarzania sensorycznego, podczas gdy style przywiązania pozostawały z mizofonią w relacjach słabszych i mniej jednoznacznych.

**ИИ:** + · скрининг пула · Polish thesis: 160 adults screened with MisoQuest to identify high- vs low-misophonia groups; recruitment appears not misophonia-based.

**Решение:** =

---

### 68 · R0147

**MERGE: Misophonia and emotion regulation in a guided experience sampling study.**

2026 · Hearing research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.heares.2026.109709

BACKGROUND: Increased sensitivity and reactivity to contextualized sound triggers is the defining feature of misophonia. Emotion regulation (ER) fluctuates at a momentary level, is a malleable misophonia risk factor, and characterizes maladaptive cognitive, affective, and behavioral responses to aversive stimuli in individuals with misophonia. As misophonia symptom expression varies due to context (e.g., sound exposure), it is likely that misophonia also fluctuates momentarily. Understanding real-time associations between momentary ER and misophonia symptoms would help 1) better characterize misophonia and 2) inform an understanding of misophonia symptoms, symptom trajectories, and tailored interventions; yet, experience sampling studies of misophonia are limited. METHOD: Interval- and event-contingent ecological momentary assessment methods measured misophonia, ER strategies (techniques to manage emotions), and ER abilities (capacity to manage emotions) over a 30-day period three times per day to capture ER and misophonia during and outside of triggers. Sixty individuals screening positive for misophonia were recruited, and participants completed ∼3000 momentary surveys. RESULTS: Intraclass correlation coefficients suggested between 23-52% of individual variability in momentary misophonia, ER abilities, and ER strategies was due to momentary-level changes. In multilevel models, within- and between-individual domains of ER strategies and abilities were related to misophonia both during and not during triggers, controlling for: 1) time since most recent trigger and 2) trigger anticipation for individuals not endorsing a current trigger. DISCUSSION: Results suggest meaningful individual variability in misophonia, ER strategies, and ER abilities. Findings will inform follow-on just-in-time adaptive interventions targeting momentary misophonia variability.

**ИИ:** ? · выборка неясна · EMA study of 60 people screening positive for misophonia; the screening pool may have been unselected and could yield prevalence data.

**Решение:** =

---

### 69 · R0150

**Misophonia in a large treatment-seeking child and adolescent sample in mental health care in Germany and Austria.**

2026 · BMC psychiatry · article, collection/collection, journal article · eng · https://doi.org/10.1186/s12888-026-07979-1

Background Misophonia is a newly conceptualized disorder. Although its onset is usually in childhood and early adolescence, the current knowledge about etiology or treatment options for children and adolescents is still limited. This is the first study investigating treatment-seeking children and adolescents in routine mental health care with regard to misophonia symptomatology and co-occurring symptoms. Methods In this multi-center cross-sectional study, conducted in Germany and Austria, N = 214 participants completed measures on misophonia, anxiety, depression, posttraumatic stress disorder, obsessive-compulsive symptoms, chronic irritability, quality of life and functional impairment. The probable misophonia subsample also reported on current coping strategies and situations in which the misophonia related problems were most evident. Results In the overall sample, 90.19% of the participants reported being bothered by at least one (misophonia-relevant) repetitive sound and 31.28% scored above the clinical cut-off for probable misophonia. In the probable misophonia subsample, 96.97% showed clinically significant co-occurring symptoms such as anxiety. The probable misophonia subsample reported significantly higher scores on all co-occurring symptom scales as well as higher functional impairment and lower quality of life, compared with the non-misophonia subsample. Most misophonia-related problems occurred in the company of other people (mostly classmates (68.18%)). The most frequent coping strategies were listening to music (57.81%) and leaving the room (25.00%). Discussion The high rates of reported salient repetitive sounds and misophonia symptoms in routine mental health care, particularly in comparison to non–treatment-seeking populations, highlight the need for an awareness of the disorder in mental health services, and further research on feasible diagnostic and treatment approaches for misophonia and co-occurring symptoms in children and adolescents. Clinical trial number Not applicable. Supplementary Information The online version contains supplementary material available at 10.1186/s12888-026-07979-1.

**ИИ:** + · клиническая группа · Treatment-seeking youth recruited from general mental health care (not for misophonia); 31.28% scored above the probable misophonia cut-off.

**Решение:** =

---

### 70 · R0155

**Characterizing symptom presentations in children and adolescents with obsessive-compulsive disorder.**

2026 · Journal of psychiatric research · journal article · eng · https://doi.org/10.1016/j.jpsychires.2026.02.024

Pediatric obsessive-compulsive disorder (OCD) is characterized by significant heterogeneity in symptom presentation, complicating assessment and treatment planning. This study presents item-level data on the frequency of specific OCD symptoms using the updated Children's Yale-Brown Obsessive Compulsive Scale-II (CY-BOCS-II), which includes expanded content and greater emphasis on avoidance behaviors. Participants included 101 children and adolescents (54% male; M = 12.81 years, SD = 2.81, range = 7-17) with a primary OCD diagnosis recruited from two specialty clinics. Analyses examined the current presence or absence of 58 individual symptoms, and item-level frequency comparisons were conducted between children (≤12 years) and adolescents (≥13 years). Youth endorsed an average of 17 total symptoms, with reassurance seeking, "just right" behaviors, and need for symmetry/exactness among the most common. Most youth (77.2%) reported experiencing symptoms in at least three dimensions. Adolescents endorsed significantly more symptoms than children, and ritualized avoidance behaviors were reported by 31.7% of the sample. Findings highlight the value of item-level assessment for characterizing the full range of pediatric OCD symptoms, guiding personalized treatment, and improving diagnostic accuracy.

**ИИ:** ? · другое · Pediatric OCD clinical sample with item-level symptom frequencies; abstract doesn't mention misophonia, but the checklist might include sound-sensitivity items.

**Решение:** -6 не про мизофонию

---

### 71 · R0157

**Behavioral Avoidance Measurement Framework**

2026 · OSF · project

The project is part of my PhD in Psychology at Freie Universität Berlin. Goals: Develop a computerized behavioral testing framework for anticipating and reactive avoidance strategies utilizing missing responses and reaction times as behavioral indicators. Validating two new measures: a) endurance and b) anticipating avoidance tendency. Application of the framework to misophonia (i.e., developing the Misophonic Behavioral Avoidance Test

**ИИ:** ? · выборка неясна · OSF PhD project building a misophonia behavioral avoidance test; the abstract is cut off and doesn't say how the sample was recruited or screened.

**Решение:** =

---

### 72 · R0158

**Prevalence and Demographic Influences of Misokinesia and Misophonia in Adults in India**

2026 · Research Square · article, preprint, google scholar result · und · https://doi.org/10.21203/rs.3.rs-5659312/v1

Abstract Purpose:: This study aimed to assess the prevalence and characteristics of misophonia and misokinesia among adults in India, focusing on demographic influences such as age and gender. Misophonia, characterized by aversive reactions to specific sounds, and misokinesia, involving similar reactions to repetitive visual stimuli, are sensory processing disorders with profound impacts on affected individuals. Methods: : The study used a cross-sectional survey design and included 450 adults (240 females and 210 males) aged 18-50 years, recruited from various regions across India. Data were collected through an online survey that included demographic information and standardized questionnaires: the Misophonia Assessment Questionnaire (MAQ) and the Misokinesia Assessment Questionnaire (MkAQ). Participants who indicated symptoms rated the severity of their experiences. Results: : The prevalence of misophonia was found to be 16.89%, and misokinesia was 5.34%. Co-occurrence of both conditions was observed in 8.89% of participants. Prevalence rates were higher among females across both conditions. A moderate negative correlation was identified between symptom severity and age, indicating that younger adults experience greater sensitivity to both misophonia and misokinesia. Conclusions: : The findings reveal a notable prevalence of misophonia and misokinesia among Indian adults, with higher rates observed in younger individuals and females. The co-occurrence of these conditions suggests shared mechanisms and emphasizes the need for targeted, culturally relevant assessment and intervention approaches. These results underscore the importance of understanding sensory processing disorders within diverse cultural contexts, providing foundational insights for clinical practice and future research in India.

**ИИ:** + · исследование распространённости · Cross-sectional online survey of 450 Indian adults using MAQ; reports misophonia prevalence of 16.89%.

**Решение:** =

---

### 73 · R0161

**Demographic Determinants of Misophonia Severity: The Role of Age, Gender, Education, and Socioeconomic Status**

2026 · Pakistan Journal of Social Science Review · other literature type, text/, article · en · https://doi.org/10.5281/zenodo.21774385

The present study examined the demographic determinants of misophonia severity among Pakistani university students, with a particular focus on the roles of age, gender, education, and socioeconomic status. A total of 2,021 students were recruited using a random sampling technique. The Psychotic Symptom Rating Scale (PSYRATS) was administered to screen for psychotic symptoms, and participants exhibiting psychotic symptoms were excluded. The remaining participants completed the Urdu version of the Misophonia Scale. For the predictive analysis, participants reporting misophonia symptoms 4–7 times per week, 2–5 times per day, or six or more times per day were retained, whereas those reporting symptoms 2–3 times per month or 1–3 times per week were excluded because these frequencies reflected infrequent and less stable symptom occurrence. This screening process reduced heterogeneity in symptom severity and ensured a more behaviorally comparable sample. Following the application of the inclusion and exclusion criteria, the final analytical sample consisted of 196 participants. Multiple linear regression analysis revealed that age, gender, and educational level were significant predictors of misophonia severity, whereas socioeconomic status was not. Specifically, misophonia severity decreased with increasing age and educational attainment, while significant gender differences were observed in symptom severity. These findings suggest that demographic characteristics, particularly age, gender, and education, play an important role in understanding individual differences in misophonia severity and should be considered in future research, assessment, and intervention efforts.

**ИИ:** + · скрининг пула · 2,021 randomly sampled university students screened with Urdu Misophonia Scale; 196 met frequency criterion, so a prevalence figure can be derived.

**Решение:** =

---

### 74 · R0164

**Psychometric Validation of the New Misophonia Screening List-Child and Youth and AMISOS-Y (Dutch Child- and Parent-Report Versions) for Assessing Misophonia in Youth.**

2026 · Child psychiatry and human development · article, journal article, validation study · eng · https://doi.org/10.1007/s10578-024-01781-4

Misophonia is a recently identified disorder of decreased sound tolerance that often originates in childhood. Currently, there is a lack of validated questionnaires for screening and assessing misophonia severity in children/adolescents. This paper presents an iterative validation process of two innovative (parallel child-/parent-reported) questionnaires: the Misophonia Screening List-Child and Youth for screening, and the Amsterdam Misophonia Scale-Youth (AMISOS-Y) for assessing misophonia severity in youth. After instrument refinement, we performed ROC curve, reliability, and principal component analyses, and assessed concurrent, convergent and divergent validity, on a combined sample (aged 8-18; clinical sample N = 94 youth, 95 parents; control group screening N = 197 youth, 56 parents; control group AMISOS-Y N = 192 youth, 55 parents). Both questionnaires were unidimensional and displayed excellent psychometric properties (α = 0.95-0.96). Future replication studies are needed in community and clinical samples to contribute to a unified diagnostic framework. Trial registered 09/2021: NL-OMON20775.

**ИИ:** + · валидация шкалы · Validation of youth misophonia questionnaires that includes a non-clinical control group (N=197) screened, which could give a count of positive screens.

**Решение:** =

---

### 75 · R0165

**A comparison of misophonia proportion and patterns of uncomfortable loudness levels between individuals with and without hyperacusis reporting sensitivity to environmental sounds.**

2026 · International journal of audiology · article, journal article, journalarticle · eng · https://doi.org/10.1080/14992027.2026.2642751

Objective To compare audiological characteristics and misophonia symptoms proportion in young adults with normal hearing and self-reported sound sensitivity (without tinnitus), classified as having hyperacusis status. Design Cross-sectional study. Participants classified as having hyperacusis (ULLmin ≤77 dB HL) or non-hyperacusis (>77 dB HL). Misophonia symptoms were identified using screening thresholds: Sound Sensitivity Symptoms Questionnaire item 4 (SSSQ4 ≥ 2) or Misophonia Questionnaire-Misophonia Severity Scale (MQ-MSS ≥7). Audiological variables included ULLmin (uncomfortable loudness level minimum), slopes, asymmetry, and repetition differences. Study sample 153 participants (19-31 years), recruited via social media. Results 31.4% met the hyperacusis criterion. The hyperacusis group showed lower ULLmin, steeper ULL slopes, and higher HQ, SSSQ, and MQ scores ( p ≤ 0.002). Misophonia was more prevalent in the hyperacusis group (52.1% vs. 32.4%, p = 0.020). Multivariable analysis showed that hyperacusis was the strongest predictor of misophonia, with ULLmin and slope contributing. Conclusions Many individuals reporting sound sensitivity did not meet objective criteria for hyperacusis, underscoring the value of measures such as ULLmin. The higher prevalence of misophonia symptoms in hyperacusis and their shared audiological correlates suggest substantial overlap between decreased sound tolerance subtypes. These findings support integrated audiological-psychometric assessment and highlight the need for longitudinal and neuroimaging studies.

**ИИ:** ? · другое · Reports misophonia proportion in a hyperacusis group, but everyone was recruited for self-reported sound sensitivity, which may exclude it.

**Решение:** =

---

### 76 · R0168

**Attention and physiological responses to task-irrelevant sounds in misophonia.**

2026 · Journal of clinical and experimental neuropsychology · article, journal article, journalarticle · eng · https://doi.org/10.1080/13803395.2026.2633236

ABSTRACT Introduction Misophonia is a disorder in which certain sounds (known as triggers) cause a negative and often overwhelming emotional response. Common triggers include human-produced and repetative sounds such as chewing and tapping. The extent to which this response is modulated by task focus – such as whether a sound is attended or not – is largely unknown. Similarly, the extent to which these responses are specific to triggers or found, to some degree, for a wider range of stimuli is unclear. Methods In this study, two groups (misophonics, controls) engage in a visuo-motor task during the presence of irrelevant sounds (misophonic triggers, unpleasant sounds, neutral sounds) whilst the effects of distraction (poorer performance in the visuo-motor task) and psychophysiological responsiveness (heart and skin conductance) are measured. Results The results show that misophonic triggers elicit more distraction than other sounds (for people with misophonia), but this is set against a backdrop of an overall tendency for people with misophonia to be more distracted by all sounds. We found no differences in skin conductance, but significant group differences in heart rate and heart rate variability across both sounds and silence. Conclusions These findings suggest that misophonia is linked to trait-like differences in attentional style and emotional regulation.

**ИИ:** ? · выборка неясна · Experimental study comparing misophonia and control groups; the abstract doesn't say whether groups came from screening an unselected pool.

**Решение:** =

---

### 77 · R0177

**Does Misophonia Affect Spatial Hearing? A Study Using Closed-Field Assessment Tools.**

2026 · American journal of audiology · article, journal article, journalarticle · eng · https://doi.org/10.1044/2025_aja-25-00058

PURPOSE: The study compared spatial hearing in individuals with misophonia, by examining interaural time difference (ITD) and interaural level difference (ILD) thresholds, Virtual Acoustic Spatial Identification (VASI) scores, and potential correlations between these thresholds and the Amsterdam Misophonia Questionnaire (A-MISO-S). METHOD: Standard group comparison consisting of 40 individuals with normal hearing was conducted. Participants were divided into two groups: 20 individuals with misophonia and 20 without misophonia (controls). Misophonia was diagnosed based on A-MISO-S scores. Behavioral assessments included ITD and ILD, and VASI tests (identification of eight virtual locations), which were carried out in a closed field environment (under headphones). RESULTS: Multivariate analysis of variance results showed that the misophonic group demonstrated significantly higher ITD thresholds and significantly lower overall VASI accuracy scores. This effect was also reflected in location-specific performance on VASI test, with markedly poorer scores at the R45 and L45 positions, compared to the nonmisophonic group. Correlational analysis showed significant negative correlation between A-MISO-S scores and VASI accuracy scores, in a misophonic group. Furthermore, Fisher discriminant analysis revealed that ITD and VASI are effective predictors of group segregation based on spatial hearing performance, with an overall classification accuracy of 95%. CONCLUSIONS: The findings suggest that misophonia may be associated with reduced performance on binaural hearing tasks involving temporal cues (ITD) and spatial identification tasks (VASI). This may be secondary to limited cognitive resources in complex spatial tasks and altered binaural temporal processing in misophonics.

**ИИ:** ? · выборка неясна · Case-control study (20 vs 20) using A-MISO-S. Unclear how people were recruited; groups may have come from screening a larger unselected pool.

**Решение:** =

---

### 78 · R0184

**Does aberrant connectivity underlie the experience of Does aberrant connectivity underlie the experience of misophonia? misophonia?**

2026 · Unpublished · text/thesis, article · en · https://doi.org/10.13140/rg.2.2.10047.88486

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Thesis on connectivity in misophonia, no abstract; it may have screened an unselected pool before the neuroimaging.

**Решение:** =

---

### 79 · R0185

**Conceptualizing the substrates and sequelae of decreased sound tolerance as a developmental cascade: A pilot study.**

2026 · Hearing research · article, journal article, research support, u.s. gov't, non-p.h.s. · eng · https://doi.org/10.1016/j.heares.2025.109472

• High likelihood infants, especially those with autism, display DST by 3 years old. • Early sensory hyperresponsiveness predicts later DST symptomatology. • DST symptomatology predicts later anxiety, at least in high likelihood infants. • Gamma power was not a significant predictor of sensory hyperresponsiveness or DST. A growing body of research has shown that decreased sound tolerance (DST) is highly prevalent and impacts the mental health of affected individuals. Recent work has shown this is especially true for autistic individuals. The extant literature has been limited, however, by a focus on DST relatively late in life. Consequently, at present we know little about when and how DST emerges and produces cascading effects on mental health. In this pilot study, we prospectively followed infants at high likelihood for autism, and thus hypothetically for DST, based on their status as younger siblings of autistic children (Sibs-Autism) and infants at lower, general population-level likelihood for these conditions (Sibs-NA) to determine whether (a) DST symptomatology differs based on autism likelihood status and/or diagnostic outcome; (b) indices of early resting brain states, specifically gamma power, predict sensory hyperresponsiveness and DST; (c) sensory hyperresponsiveness predicts DST symptomatology; (d) DST symptomatology predicts anxiety; and (e) if the aforementioned associations vary by familial likelihood for autism or later autism status. Preliminary results indicate that DST symptoms are elevated in Sibs-Autism, particularly those who go on to receive a diagnosis of autism, relative to Sibs-NA. Gamma power is not significantly associated with later sensory hyperresponsiveness or DST, but hyperresponsiveness is associated with later DST, which is associated with later anxiety in Sibs-Autism.

**ИИ:** ? · другое · Infants at high or low autism likelihood assessed for decreased sound tolerance; the full text may separate misophonia symptoms from the overall DST measure.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 80 · R0186

**Developing a Coding System to Record Orofacial Movements for Misophonia with Verification from Physiology Data**

2026 · Scholar Commons (University of South Carolina) · dissertation, text

My thesis aims to develop and evaluate a facial coding system that can quantify facial movements in the context of misophonia. The system uses binary coding to individually quantify and identify each orofacial movement that occurs independent of other movements or artifacts that could interfere with coding data. The system can be used across multiple coders with statistically significant reliability into how orofacial movements are interpreted. The psychophysiological verification study used electromyography to examine the muscle potentiation of the corrugator supercilii and zygomaticus major muscles to map observable facial movement to underlying muscle potentiation. This facial coding system can be used to identify specific expressions linked to misophonia and contribute to a better understanding of the underlying mechanisms of the condition. Data derived from the facial coding system can also be used as a benchmark coding system to verify and develop other facial coding systems such as OpenFace and Py-Feat.

**ИИ:** ? · выборка неясна · Methodological facial-coding thesis on misophonia; how participants were recruited and whether misophonia was measured in an unselected pool is not stated.

**Решение:** =

---

### 81 · R0188

**RELATIONSHIP BETWEEN MISOPHONIA AND OBSESSIVE COMPULSIVE DISORDER MODERATED BY ANXIETY SENSITIVITY**

2026 · Pakistan Journal of Social Science Review · article · en

Misophonia is characterized by intense emotional, physiological, ad cognitive reaction to the auditory triggers and associated with obsessive- compulsive symptoms. Present study evaluated the relationship between misophonia and obsessive-compulsive disorder moderated by anxiety severity. Internal constancy of the scale was assessed by using Cronbach Alpha. Moderated multiple regression was conducted to investigate the independent and interactive effects of misophonia and anxiety severity on obsessive-compulsive disorder. Misophonia and anxiety severity jointly explained 9% of the variance in obsessive compulsive symptoms, F(2, 423) = 21.93, p < .001. Adding the interaction term increased the explained variance to 13%, F(3, 425) = 21.04, p < .001. The interaction between misophonia and anxiety sensitivity was significant (β = .29, p < .001), indicating that the association between misophonia and obsessive –compulsive symptoms became stronger as anxiety sensitivity increased. Results indicated that individuals with elevated anxiety sensitivity may be particularly vulnerable to intense emotional and physiological reactions to misophonic trigger may contribute to obsessive thoughts and compulsive behaviour. Assessment and intervention strategies targeting anxiety sensitivityand emotional regulation may therefore help reduce the psychological consequences of misophonia, particularly within South Asian populations.

**ИИ:** ? · выборка неясна · Misophonia was measured in about 426 participants, but the abstract doesn't say how they were recruited. It is likely a non-clinical Pakistani sample.

**Решение:** =

---

### 82 · R0196

**Misophonia Symptoms in Autistic Adults.**

2026 · Journal of autism and developmental disorders · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10803-025-07184-1

PURPOSE: Misophonia is the adverse emotional reaction to everyday sounds (e.g., chewing or pen clicking). Since atypical sensory experiences are a key feature of autism, we investigated whether autistic individuals are more liable for experiencing misophonia symptoms. In addition, we explore the contribution of sensory sensitivity to misophonia symptoms in autism.METHODS: Autistic adults (N = 1050) filled out the Amsterdam Misophonia Scale-Revised (AMISOS-R), the Autism Spectrum Quotient (AQ-28), and the Sensory Processing Questionnaire (SPQ). Chi-square tests were applied to compare proportion of moderate or higher AMISOS-R scores over 20 to previously reported values in the extant literature. Next we modelled the quantitative level of AMISOS-R scores as function of AQ-28 with age, sex, and co-occurring disorders. Finally, we ran a mediation model adding SPQ as a mediator.RESULTS: Autistic people reported moderate to extreme levels of AMISOS-R in higher proportion than the general population. In particular autistic females and those with co-occurring disorders scored higher. In quantitative models, we found that autistic traits strongly predicted misophonia symptoms after correcting for multiple covariates. Both the hearing and vision subscales of the SPQ significantly mediated the effect.CONCLUSION: The increased level of misophonia symptoms in autism and the mediation analyses suggest that autistic traits and sensory sensitivity are factors to consider for a subset of misophonia sufferers, with possible consequences for their clinical interventions.</p

**ИИ:** + · клиническая группа · 1050 autistic adults (recruited for autism) completed the AMISOS-R; reports proportion scoring moderate or higher (over 20).

**Решение:** =

---

### 83 · R0197

**Anxiety and depression among Canadian undergraduates with decreased sound tolerance.**

2026 · Hearing research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.heares.2025.109522

Decreased sound tolerance (DST) is an encompassing term for conditions marked by a reduced tolerance to everyday sounds. Misophonia, sensitivity to specific trigger sounds which cue aversive responses, is one DST subtype. Hyperacusis, another DST subtype, occurs when people are irritated by general sounds that are unbothersome to others. Research suggests that those with DST face heightened mental health challenges. Psychometrically validated measures aligned with the recent misophonia consensus definition have not assessed the relationship between DST and mental health. There is also a complete dearth of DST-mental health research in Canadian universities. Here, 2,095 Canadian undergraduate students completed DST and mental health questionnaires. We explored the relationship between anxiety and depression and DST. We found strong, positive, and significant correlations between DST symptoms and mental health difficulties. These findings highlight DST’s detrimental effects and the need for future research on strategies for managing and treating DST in post-secondary institutions.

**ИИ:** + · ненабранная выборка · 2,095 Canadian undergraduates completed DST measures, likely including a misophonia measure aligned with the consensus definition; the full text could report how many meet a case definition.

**Решение:** =

---

### 84 · R0203

**MEG Signatures of Differences in Auditory Cortex Responses to Trigger versus Non-Trigger Sounds in Misophonia**

2026 · bioRxiv · preprint · https://doi.org/10.64898/2026.09.14.751161

Abstract Misophonia is characterized by intense emotional and physiological reactions to specific “trigger” sounds that may vary across individuals. Despite greater recognition and increased research, the neural mechanisms underlying misophonia are still poorly understood. Using magnetoencephalography (MEG) with millisecond temporal resolution, we examined auditory cortex responses to trigger versus non-trigger sounds in 23 individuals (ages 14 – 32 years) that met criteria for misophonia on a screening assessment. We found that in the right hemisphere, trigger sounds elicited significantly smaller evoked responses, lower power of induced alpha-band oscillations, and stronger alpha-gamma cross-frequency phase-amplitude coupling, compared to non-trigger sounds. We also found that evoked responses correlated with behaviorally assessed extent of misophonia symptoms. These findings support the idea that misophonia is characterized at least in part by altered neurophysiological processing of auditory trigger stimuli early in the auditory cortex hierarchy. Our results provide novel insight into the neural basis of misophonia and underscore the importance of examining brain activity even at the earliest levels of the cortical hierarchy with high spatio-temporal resolution.

**ИИ:** ? · выборка неясна · MEG study of 23 people who met misophonia criteria on a screening assessment; unclear whether an unselected pool was screened or misophonia cases were recruited.

**Решение:** =

---

### 85 · R0204

**Misophonia in adolescents: clinical correlates and associations with autism-related behavioral characteristics within a clinical context**

2026 · BMC Pediatrics · article, journalarticle, google scholar result · en · https://doi.org/10.1186/s12887-026-07387-0

Misophonia is characterized by intense emotional and behavioral reactions to specific sounds and has been associated with psychiatric symptoms and sensory sensitivity. This study investigated the prevalence of misophonia in a clinical adolescent outpatient sample and examined its associations with psychiatric symptoms and autism-related behavioral characteristics. The study included 200 adolescents aged 12–18 years who were referred to a child and adolescent psychiatry outpatient clinic. Psychiatric diagnoses were assessed using the Kiddie Schedule for Affective Disorders and Schizophrenia for School-Age Children—Present and Lifetime Version for DSM-5. Misophonia severity was evaluated with the Amsterdam Misophonia Scale–Revised, while emotional-behavioral problems and autism-related behavioral characteristics were assessed using the Youth Self-Report/11–18. Group comparisons were performed using the chi-squared test, Fisher’s exact test, and the Mann–Whitney U test. Spearman’s correlation analyses and hierarchical logistic regression analyses were conducted. Adolescents with misophonia had higher rates of major depressive disorder. They also had significantly higher internalizing and externalizing symptoms and elevated autism-related behavioral characteristics than those without misophonia (all p < 0.001; Z = -5.62, -4.59, and − 5.70, respectively). Hierarchical logistic regression analysis revealed that higher internalizing problem scores independently predicted the presence of misophonia (Nagelkerke R² = 0.226, p < 0.001; OR = 1.07). Misophonia in adolescents appears to be closely associated with broader internalizing psychopathology and emotional-behavioral difficulties within psychiatric outpatient settings. Elevated autism-related behavioral characteristics in adolescents with misophonia support further research into the relationship between misophonia and neurodevelopmental characteristics. Such research may contribute to improving clinical assessment and understanding of behavioral patterns associated with misophonia. However, study limitations and inconsistencies in the literature highlight the need for further research in this area.

**ИИ:** + · клиническая группа · Prevalence of misophonia (AMISOS-R) in 200 adolescent psychiatric outpatients not recruited for misophonia.

**Решение:** =

---

### 86 · R0205

**Neural Indicators of Misophonia Related Cognitive Load**

2026 · K-State Research Exchange (Kansas State University) · dataset/eeg, dissertation, project · en · https://doi.org/10.18112/openneuro.ds008003.v1.0.0

Doctor of PhilosophyDepartment of Psychological SciencesMatthew WisniewskiMisophonia is characterized by disproportionate emotional and physiological responses to specific “trigger” sounds, often accompanied by self-reported difficulty maintaining focus during exposure. This dissertation sought to provide objective evidence of such cognitive disruptions by combining behavioral measures of auditory working memory (WM) with electroencephalographic (EEG) indices of neural processing. Fifty-seven participants (27 misophonic, 30 control) completed a pitch-matching WM task under three distractor conditions: silence, neutral sounds, and individualized trigger sounds. EEG was analyzed using a time– frequency approach to assess changes in alpha (8–12 Hz) and theta (4–7 Hz) oscillatory activity during the retention interval. Behaviorally, misophonic participants exhibited reduced overall WM performance compared to controls and a selective decrease in response precision, without loss of accuracy, when exposed to trigger sounds, suggesting degraded memory fidelity under emotionally salient distraction. From the EEG analysis, misophonic participants showed lower frontal alpha and theta power across conditions, consistent with diminished inhibitory control and reduced cognitive control engagement, rather than trigger-specific effects. These results indicate that misophonia may involve a generalized attentional control vulnerability that amplifies the disruptive impact of emotionally salient auditory stimuli. Implications and directions for future research are discussed

**ИИ:** ? · выборка неясна · EEG dissertation, 27 misophonic vs 30 controls; recruitment unclear, possibly screened from a university participant pool.

**Решение:** =

---

### 87 · R0206

**Working Memory Disruption and Altered Alpha Dynamics in Misophonics**

2026 · Preprints.org · dataset/eeg, preprint · https://doi.org/10.20944/preprints202609.1892.v1

Background: /Objectives: Misophonia is characterized by disproportionate emotional and physiological responses to specific "trigger" sounds, often accompanied by self-reported difficulty maintaining focus. Here, we sought to provide objective evidence of such cognitive disruptions by combining behavioral measures of auditory working memory with electroencephalographic (EEG) indices of neural processing. Methods: Fifty-five participants (23 Misophonic, 32 control) completed a pitch-matching WM task under three distractor conditions: individualized trigger sounds, neutral sounds, and silence. EEG was analyzed using a time-frequency approach to assess alpha (8-12 Hz) oscillatory activity during working memory retention at the source level with Independent Component Analyses (ICA). Results: Behaviorally, Misophonic participants exhibited reduced overall working memory performance compared to controls, with no difference between neutral and trigger conditions, suggesting a general deficit in distractor inhibition. EEG results showed lower alpha power across all conditions in the misophonia group, consistent with diminished inhibitory control rather than trigger-specific effects. This lower Alpha appeared to occur for sources in parietal and somatomotor areas. Group differences were apparent in alpha suppression around trigger onset times and alpha enhancements occurring later in retention intervals. Conclusions: Results are consistent with claims made in the literature that Misophonics show impaired attentional control and motor regulation. Implications for Misophonia theoretical models and directions for future research are discussed.

**ИИ:** ? · выборка неясна · EEG case-control study (23 misophonic, 32 controls); unclear whether groups came from screening an unselected pool or targeted recruitment.

**Решение:** =

---

### 88 · R0207

**A Comparison of Misophonia and Autistic Traits in Parents of Children with and without Autism Spectrum Disorder.**

2026 · Turk psikiyatri dergisi = Turkish journal of psychiatry · article, comparative study, research-article · eng;tur · https://doi.org/10.5080/u27720

Objective This study aims to compare misophonia levels and autistic traits between parents of children diagnosed with autism spectrum disorder (ASD) and parents of typically developing children. Methods Parents of children diagnosed with ASD who presented to the Child and Adolescent Psychiatry outpatient clinic (n=56) and parents of typically developing children (n=56) were included in the study. The Childhood Autism Rating Scale (CARS) was administered to the children with ASD. All participating parents completed the Autism Spectrum Quotient (AQ) and the Amsterdam Misophonia Scale&ndash; Revised (AMISOS-R). Results The rate of reporting throat sounds as a misophonic trigger was higher among parents of children with ASD (p=0.004). Weak but significant positive correlations were found across all participants between the AMISOS-R total score and the AQ total score, the attention switching subscale score, and the communication subscale score (r=0.275, p=0.003; r=0.266, p=0.005; r=0.35, p&lt;0.001, respectively). Among parents of children with ASD, the AMISOS-R total score was positively correlated with items 3, 5, and 9 of the CARS (p&lt;0.05). Conclusion Our findings support potential associations between misophonia and ASD, and suggest that misophonia in parents may be related to certain characteristics in the child, such as sensory processing and emotional regulation.

**ИИ:** + · ненабранная выборка · Parents recruited because of their child's ASD status, not misophonia; all completed the AMISOS-R, so misophonia rates may be reported.

**Решение:** =

---

### 89 · R0208

**Misophonia, Autistic Traits, and Obsessive-Compulsive Symptoms in Migraine: A Controlled Comparative Study.**

2026 · Pediatrics international : official journal of the Japan Pediatric Society · article, comparative study, journal article · eng · https://doi.org/10.1111/ped.70462

ABSTRACT Objective This study examined misophonia severity and triggers in adolescents with migraine versus controls and their associations with autistic traits and obsessive‐compulsive symptoms. Methods This cross‐sectional case–control study included 80 adolescents aged 15–18 years (40 with migraine; 40 age‐ and sex‐matched controls). Participants completed the Amsterdam Misophonia Scale–Revised (AMISOS‐R) and the Obsessive‐Compulsive Inventory–Child Version (OCI‐CV); parents completed the Autism Spectrum Screening Questionnaire (ASSQ‐TR). Results Adolescents with migraine had higher AMISOS‐R scores than controls (20.70 ± 8.59 vs. 13.65 ± 8.69, p &lt; 0.001) and a higher prevalence of misophonia (85.0% vs. 62.5%, p = 0.022). Repetitive clicking and ambient background sounds were more frequently reported as triggers in the migraine group ( p = 0.003 and p = 0.001, respectively). ASSQ total scores were higher in migraine ( p = 0.022), whereas OCI‐CV total scores did not differ, despite higher doubting/checking scores ( p = 0.024). Within the migraine group, headache intensity correlated with misophonia severity ( r = 0.329, p = 0.038). In regression analysis, migraine status, female sex, and ASSQ scores independently predicted misophonia severity (adjusted R 2 = 0.362). Conclusion Misophonia was more prevalent and severe in adolescents with migraine and was associated with headache severity and autistic traits. These findings suggest that misophonia may be a sensory feature of adolescent migraine and highlight the need for longitudinal studies to elucidate the common sensory processing pathways linking migraine and misophonia.

**ИИ:** + · клиническая группа · Adolescents with migraine and matched controls; reports misophonia prevalence measured with AMISOS-R (85.0% vs 62.5%).

**Решение:** =

---

### 90 · R0210

**Fatores associados à misofonia em estudantes, professores, técnicos de uma universidade pública brasileira**

2026 · Audiology - Communication Research · article, journalarticle · pt · https://doi.org/10.1590/2317-6431-2025-3080pt

RESUMO Objetivo investigar a associação da misofonia às queixas auditivas e aos sintomas de ansiedade e depressão. Métodos estudo de caráter quantitativo, observacional, descritivo e analítico, de delineamento seccional, realizado com alunos, professores e técnicos de uma universidade pública brasileira A coleta de dados foi realizada de forma virtual, utilizando formulário confeccionado na plataforma Google Forms, disponibilizado aos participantes via e-mail no período de junho a dezembro de 2022. O formulário apresentou perguntas referentes à misofonia (a partir da Lista de Triagem para Misofonia), queixas auditivas, comorbidades, ansiedade e depressão (por meio da Escala Hospitalar de Ansiedade e Depressão). Resultados a misofonia foi associada à queixa de perda auditiva (p=0,020), ao zumbido (p=0,004), ao incômodo a sons intensos (p=0,010) e à ansiedade (p=0,011). Conclusão a misofonia apresenta associação à hipoacusia, ao zumbido, ao incômodo a sons intensos e à ansiedade.

**ИИ:** + · ненабранная выборка · University-wide survey of students, teachers and staff that screened for misophonia with a screening list; likely reports how many screened positive.

**Решение:** =

---

### 91 · R0214

**Étude préliminaire sur les caractéristiques psychologiques reliées à l’ASMR et des phénomènes apparentés (misophonie, synesthésie) dans une population d’étudiants âgés entre 18 et 25 ans**

2026 · Psychologie Française · article, journalarticle · fr · https://doi.org/10.1016/j.psfr.2026.02.001

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · ненабранная выборка · Student sample aged 18-25 assessed for ASMR and related phenomena including misophonia; no abstract, but the title suggests misophonia was measured.

**Решение:** =

---

### 92 · R0217

**Examining Sleep-Related Problems in Youth With Misophonia.**

2026 · Journal of clinical psychology · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1002/jclp.70075

ABSTRACT The relationship between misophonia and sleep‐related problems (SRPs) in youth is underexplored. This paucity of research is concerning because SRPs might be elevated among youth with misophonia. If left untreated, SRPs can contribute to long‐term health consequences. Thus, in this study we examined the link between misophonia and SRPs in youth aged 8 to 17. In this study, we compared SRPs in 102 children and adolescents with clinically significant misophonia to SRPs in a normative youth sample and a sample of 94 youth with anxiety disorders. We also examined the extent to which SRPs were associated with misophonia severity. Approximately 30% of youth with misophonia endorsed clinical levels of SRPs. SRPs were more prevalent in youth with misophonia compared to normative data from the general youth population ( d = 1.22) and similar to SRPs in youth with anxiety disorders ( d = 0.13). Youth with more severe misophonia symptoms had greater difficulties with SRPs and this association was attenuated but still significant when adjusting for gender, age, and internalizing and externalizing symptoms. In this study, we provided the first evidence of substantial issues with SRPs in youth with misophonia. Importantly, there was a moderate association between misophonia severity and SRPs, indicating that SRPs should be carefully assessed and potentially addressed in treatment for youth with misophonia. We discussed suggestions for clinical practice and future research.

**ИИ:** ? · выборка неясна · Main sample recruited for misophonia, but an anxiety-disorder comparison group (n=94) may have had misophonia measured; check full text.

**Решение:** =

---

### 93 · R0218

**Psychometric Validation of the Mandarin Version of the Duke Misophonia Questionnaire**

2026 · OSF Preprints (OSF Preprints) · preprint, project

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · Mandarin DMQ validation preprint, likely a general sample, but there is no abstract to confirm how participants were recruited.

**Решение:** =

---

### 94 · R0221

**Distinguishing Misophonia From Nonclinical Sound Aversion: Emotional Response Profiles for Auditory Triggers.**

2026 · American journal of audiology · journal article, journalarticle, review · eng · https://doi.org/10.1044/2026_aja-25-00333

PURPOSE: This study examined how individuals with and without clinically significant misophonia differ in trigger sounds, emotional response types, and reaction intensities to determine whether specific sound-emotion pairings distinguish misophonia from typical sound aversion. METHOD: A total of 168 participants (84 misophonia, 84 control) completed online surveys including the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ) for group classification and the Selective Sound Sensitivity Syndrome Scale Trigger Checklist, which assessed emotional responses and intensity ratings for 37 sounds. Demographic variables and comorbidities were examined as potential confounds. Heat map visualizations displayed sound-emotion relationships by group. RESULTS: The misophonia group reported significantly more trigger sounds, higher DVMSQ scores, and higher emotional intensity across emotions than controls. While both groups frequently reported irritation, individuals with misophonia exhibited significantly higher frequencies of anger, disgust, distress, and panic, with large effect sizes for anger. Heat maps revealed that misophonia participants reported anger at significantly higher rates for 18 sounds, particularly eating and oral sounds, whereas controls predominantly experienced irritation. Demographic variables and mental health diagnoses showed minimal associations with primary outcomes and did not account for group differences in emotional response patterns. CONCLUSIONS: Misophonia was distinguished by experiencing anger and disgust rather than irritation, at substantially higher intensities, particularly to human-produced sounds. These findings suggest that emotional response type and intensity, assessed alongside trigger identification, may help audiologists as part of multidisciplinary teams differentiate clinical misophonia requiring intervention from typical sound aversion. SUPPLEMENTAL MATERIAL: https://doi.org/10.23641/asha.33334227.

**ИИ:** ? · выборка неясна · Online survey used the DVMSQ to sort people into equal case and control groups; the full text may show a screened pool's prevalence.

**Решение:** =

---

### 95 · R0223

**Sound Tolerance Conditions After Mild Traumatic Brain Injury**

2026 · Archives of Physical Medicine and Rehabilitation · article · en · https://doi.org/10.1016/j.apmr.2026.02.470

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract. Sound tolerance conditions in an mTBI clinical group may include misophonia; worth checking the full text.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 96 · R0224

**Schwierigkeiten in der Emotionsregulation, Ungewissheitsintoleranz und Misophonie: Eine Mediationsanalyse**

2026 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint, project · https://doi.org/10.17605/osf.io/kj7bs

Für das Forschungsvorhaben wurde die Annahme aufgestellt, dass Emotionskontrolle als vermittelnder Mechanismus fungiert, durch den Ungewissheitsintoleranz zur Intensität von misophonen Reaktionen beiträgt. Die misophone negative Reaktion basiert üblicherweise darauf, dass das Geräusch entweder als bedrohlich, schädlich oder unangenehm („unerträglich“) eingeschätzt wird (Jastreboff &amp; Jastreboff, 2014). Ungewissheitsintoleranz beschreibt dabei eine dispositionelle Neigung, aversive Emotionen zu ertragen in Situationen, in denen wichtige oder ausreichende Informationen in der Wahrnehmung fehlen und somit Unsicherheit/Ungewissheit aufrechterhalten wird (Carleton, 2016). Konkret könnten die reaktionsauslösenden Geräusche bei Misophonie, welche aufgrund der sozialen Einbettung nicht immer vorhersehbar sind, bei Personen mit hoher Ungewissheitsintoleranz zu höheren emotionalen Belastungen und somit auch Anforderungen an die Emotionskontrolle führen. Es ist anzunehmen, dass Personen mit einer hohen Ungewissheitsintoleranz stärkere negative emotionale Zustände erleben, wenn sie mit Bedrohungen konfrontiert werden (Morriss et al., 2023). Wenn es nicht gelingt, diese emotionalen Reaktionen wirksam zu regulieren, könnte dies zu einer schwerwiegenderen misophonen Reaktion wie intensiverer Wut oder Vermeidung führen. Es zeigte sich bereits, dass Personen mit Misophonie Schwierigkeiten bei der Regulierung ihrer Emotionen aufweisen (Dixon et al., 2024; Guetta et al., 2022). Somit ist das übergeordnete Ziel des Forschungsvorhabens, Schwierigkeiten in der Emotionskontrolle als Mediator im Zusammenhang von Ungewissheitsintoleranz auf Misophonie zu untersuchen. Carleton, R. N. (2016). Into the unknown: A review and synthesis of contemporary models involving uncertainty. Journal of Anxiety Disorders, 39, 30–43. https://doi.org/10.1016/j.janxdis.2016.02.007 Dixon, L. J., Sevier, C. J., &amp; Freshley, A. M. (2024). Emotion dysregulation in misophonia: Findings from a nationally representative sample. Journal of Psychiatric Research, 180, 266–272. https://doi.org/10.1016/j.jpsychires.2024.10.022 Guetta, R. E., Cassiello-Robbins, C., Trumbull, J., Anand, D., &amp; Rosenthal, M. Z. (2022). Examining emotional functioning in misophonia: The role of affective instability and difficulties with emotion regulation. PLoS ONE, 17(2), e0263230. https://doi.org/10.1371/journal.pone.0263230 Jastreboff, M., &amp; Jastreboff, P. (2014). Treatments for decreased sound tolerance (Hyperacusis and misophonia). Seminars in Hearing, 35(02), 105–120. https://doi.org/10.1055/s-0034-1372527 Morriss, J., Goh, K., Hirsch, C. R., &amp; Dodd, H. F. (2023). Intolerance of uncertainty heightens negative emotional states and dampens positive emotional states. Frontiers in Psychiatry, 14, 1147970. https://doi.org/10.3389/fpsyt.2023.1147970

**ИИ:** ? · выборка неясна · Pre-registered mediation study measuring misophonia severity; sample and recruitment not described, possibly a general-population survey.

**Решение:** -7 preregistration without data

---

### 97 · R0228

**Sensory processing differences in misophonia: Assessing sensory sensitivities beyond auditory triggers.**

2026 · Journal of psychiatric research · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jpsychires.2025.11.026

Misophonia is characterized by decreased tolerance to specific sounds, often evoking intense emotional responses. While typically conceptualized as a sensitivity to auditory triggers, emerging evidence suggests that individuals with misophonia may also experience broader sensory processing differences. This study examined sensory profiles in adults with clinically significant misophonia (n = 60) compared to age and gender matched controls, who did not possess measurable misophonia traits (n = 60). Participants completed standardized measures of sensory processing and misophonia severity. Compared to controls, individuals with misophonia reported significantly greater sensory sensitivity and avoidance, and lower sensory seeking. No group difference was observed for low sensory registration, a pattern of sensory processing characterized by reduced awareness or response to sensory input. Within the misophonia group, 80 % endorsed sensitivity in at least one non-auditory sensory domain-most commonly tactile and olfactory. However, impairment related to these sensitivities was generally low. Misophonia severity was positively associated with sensory sensitivity, avoidance, and impairment related to olfactory and gustatory input. Similar patterns were observed in non-clinical individuals with subthreshold symptoms. These findings suggest that while misophonia may involve broader sensory sensitivity, it is the misophonia-specific auditory sensitivity that remains central to the disorder's functional impact.

**ИИ:** ? · выборка неясна · Case-control study, misophonia vs controls; the mention of subthreshold non-clinical individuals suggests a larger pool may have been screened. Recruitment is unclear.

**Решение:** =

---

### 98 · R0230

**Relationships among hyperacusis, misophonia, and autistic traits in a non-clinical population**

2026 · International Journal of Developmental Disabilities · article, journalarticle, google scholar result · en · https://doi.org/10.1080/20473869.2026.2626434

Objectives Autistic traits are associated with sensory hyper-reactivity; however, the extent to which this association applies to non-clinical populations remains unclear. This study aimed to examine whether autistic traits in the general population are linked to levels of sensory hyper-reactivity comparable to those observed in autistic people, and whether this association varies according to the severity of autistic traits. Additionally, the study sought to determine the specificity of auditory hyper-reactivity and to elucidate the relationship between two aspects of auditory hyper-reactivity: hyperacusis and misophonia, in the context of autistic traits.Methods In total, 439 university students completed four self-report questionnaires assessing autistic traits, sensory traits, hyperacusis, and misophonia.Results Correlation analyses revealed significant associations between autistic traits and increased sensory hyper-reactivity across all sensory modalities. Auditory hyper-reactivity was the most frequent sensory complaint, consistent with findings from studies involving clinical autistic people. Theoretical model comparisons indicated that hyperacusis serves as a foundational abnormality that precedes the development of misophonia.Conclusions These findings demonstrated that, even in non-clinical populations, autistic traits are associated with elevated sensory sensitivity, particularly in the auditory domain. The results further supported the hypothesis of a developmental progression in which hyperacusis may act as a precursor to misophonia.

**ИИ:** + · ненабранная выборка · 439 university students, a sample not recruited for misophonia, filled in a misophonia questionnaire, so the full text may give case counts.

**Решение:** =

---

### 99 · R0233

**Characterizing Misophonia-Related Brain Activity Using Functional Near-infrared Spectroscopy (fNIRS)**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/exdjt

Misophonia is characterized by decreased tolerance to specific sounds (“triggers”) that evoke negative emotional, physiological, and behavioral responses. To understand the neural mechanisms underlying misophonia, functional neuroimaging has been proposed such as functional magnetic resonance imaging (fMRI). However, the fMRI environment introduces substantial noise that increases anxiety, which is one of the comorbidities of misophonia, confounds auditory stimuli, and is costly. We therefore propose an alternative, functional near-infrared spectroscopy (fNIRS) to detect misophonia-related responses. This project will establish the feasibility of using fNIRS to study misophonia and generate preliminary data for subsequent investigations. We aim to (1) Characterize misophonia-triggered brain activation using fNIRS. (2) Examine the relationship between brain activation, subjective distress ratings, and physiological responses, including electrodermal activity (EDA) and photoplethysmography (PPG).

**ИИ:** ? · выборка неясна · fNIRS pre-registration; abstract doesn't say how participants are recruited or whether an unselected pool is screened for misophonia.

**Решение:** -7 preregistration without data

---

### 100 · R0234

**Feasibility of Using Functional Near-Infrared Spectroscopy for Characterizing Misophonia-Related Brain Activity**

2026 · bioRxiv · preprint, google scholar result · https://doi.org/10.64898/2026.08.30.748122

Abstract Significance Misophonia is characterized by decreased tolerance to specific sounds (“triggers”) that evoke negative emotional, physiological, and behavioral responses. To understand the neural mechanisms underlying misophonia, functional neuroimaging has been proposed such as functional magnetic resonance imaging (fMRI). However, the fMRI environment introduces substantial noise that increases anxiety, which is one of the comorbidities of misophonia, confounds auditory stimuli, and is costly. We therefore propose an alternative, functional near-infrared spectroscopy (fNIRS) to detect misophonia-related responses. Aim We evaluated the feasibility of fNIRS to detect misophonia-related sound-evoked responses. Approach We measured fNIRS, electrodermal activity (EDA), and photoplethysmography (PPG) data from ten adults with minimal to mild misophonia symptoms while they listened to trigger, unpleasant, and neutral sounds. Participants rated their annoyance and antisociality after each sound. Results Compared with neutral sounds, trigger and unpleasant sounds received higher subjective ratings and evoked greater neural response in the orofacial area. Neural responses tended to increase with annoyance ratings. Significantly lower heart rate (HR) was observed during unpleasant sounds than during neutral and trigger sounds, with no significant difference in EDA features. Conclusions fNIRS can measure misophonia responses in a quiet setting. Both brain and physiological responses have the same trend observed in prior fMRI studies, verifying its feasibility.

**ИИ:** ? · выборка неясна · fNIRS study of 10 adults with minimal-to-mild misophonia symptoms; recruitment and screening unclear, but misophonia severity may be reported.

**Решение:** =

---

### 101 · R0236

**Incidence of misophonia, associated auditory symptoms and sensory processing profiles in university students in Turkey: a comparative study of clinical, subclinical and control groups.**

2026 · The Journal of laryngology and otology · article, comparative study, research-article · eng · https://doi.org/10.1017/s0022215126104526

Abstract Objective This study aimed to investigate the prevalence of misophonia among university students, examine its relationship with hyperacusis and tinnitus and explore the sensory processing patterns of individuals with misophonia in comparison to the control group. Methods Based on the Misophonia Questionnaire severity scores, 81 clinical misophonia and 163 subclinical misophonia patients and 60 matched healthy-controls participated the study and evaluated with the Tinnitus Handicap Inventory, Khalfa Hyperacusis Questionnaire and the Dunn Adult/Adolescent Sensory Profile questionnaire. Results The incidence of clinical misophonia was 19 per cent. The clinical misophonia group had significantly higher sensory-sensitivity and sensation-avoiding scores and lower low-registration scores (Mann–Whitney U-test with Bonferroni correction; p &lt; 0.017). Sensory processing scores across all sensory domains were significantly correlated with Misophonia Questionnaire scores. The strongest associations were moderate positive correlations in the touch (r = 0.444; p = 0.00) and visual (r = 0.420; p = 0.00) processing domains. Conclusions Findings indicate that misophonia involves heightened sensitivity and avoidance not only in auditory but also in movement, visual, touch and activity-related sensory areas, suggesting it is a complex atypical multisensory condition rather than purely audiological or psychiatric.

**ИИ:** + · исследование распространённости · Reports a 19% prevalence of clinical misophonia among university students in Turkey, screened with the Misophonia Questionnaire.

**Решение:** =

---

### 102 · R0243

**Misophonia impact questionnaire (MIQ), tinnitus impact questionnaire (TIQ), and hyperacusis impact questionnaire (HIQ): Factor analysis, test-retest reliability, and minimum detectable change using a non-clinical population.**

2025 · PloS one · article, data paper, other literature type · eng · https://doi.org/10.1371/journal.pone.0324726

The objectives of this study were to (1) assess if previously reported unidimensional factor structure of the Misophonia Impact Questionnaire (MIQ), Tinnitus Impact Questionnaire (TIQ), and Hyperacusis Impact Questionnaire (HIQ) can be confirmed in a nonclinical population, and (2) examine test-retest reliability and establish the minimum detectable change (MDC) for MIQ, TIQ and HIQ. 451 people completed the MIQ and HIQ sections of an online survey. A sub-sample of 173/451 who had tinnitus completed the TIQ too. 130/451 participants completed the second survey with 2 weeks interval for the MIQ and HIQ and 32/173 participants with tinnitus completed the TIQ in the second survey. All questionnaires showed excellent internal consistency, with Cronbach's α of 0.93 for both the MIQ and TIQ and 0.91 for the HIQ. Confirmatory factor analysis (CFA) showed that the MIQ, TIQ and HIQ were all one-factor questionnaires. Based on the intra-class correlation coefficients (ICC) values, the test-retest reliability was good for MIQ and HIQ and it was excellent for TIQ. Based on the MDC values, when these questionnaires are used for repeated measurements, the minimum amount of change that constitutes a true change is ≥ 8 for the total score of MIQ, ≥ 4 for the TIQ, and ≥ 7 for the total score of HIQ. In conclusion, the MIQ, TIQ and HIQ can be used in clinical practice or research setting to measure the impact of misophonia, tinnitus and hyperacusis on the individual's life, respectively, as one-factor questionnaires with excellent internal consistency and good to excellent test-retest reliability.

**ИИ:** + · валидация шкалы · Psychometric validation of the Misophonia Impact Questionnaire in a non-clinical online sample (n=451); the full text may report misophonia rates.

**Решение:** =

---

### 103 · R0246

**Assessment of working memory abilities in normal hearing individuals with and without misophonia.**

2025 · Quarterly journal of experimental psychology (2006) · article, journal article, journalarticle · eng · https://doi.org/10.1177/17470218251322718

PURPOSE The study aimed to evaluate working memory (WM) abilities in normal hearing individuals with and without misophonia using simple and complex working memory tasks and to correlate WM abilities with severity of misophonia. METHOD The data was collected employing a standard group comparison and a non-probability purposive sampling method. The current study comprised of 40 participants aged 18-30 years, who were classified into two groups (with and without misophonia) based on the scores obtained in Misophonia Assessment Questionnaire (MAQ). Simple tasks including forward digit span and backward digit span and complex tasks including operation span and reading span were used to assess WM abilities. RESULTS WM abilities, measured using simple WM tasks, were comparable between the two groups. Among the complex tasks, although the operation span scores revealed no statistically significant difference, there was a statistically significant difference in the reading span scores. CONCLUSIONS The performance of individuals with misophonia remained similar to those without misophonia in simple WM tasks. However, their WM performance becomes poorer as tasks become more demanding.

**ИИ:** ? · выборка неясна · 40 adults put into groups by MAQ scores using purposive sampling; unclear whether an unselected pool was screened first.

**Решение:** =

---

### 104 · R0248

**Alçak Frekans ve Yüksek Frekans İşitme Kaybı Olan Cihaz Kullanacak HastalardaMizofoni, Hiperakuzi ve Tinnitus Anketi ile Değerlendirme**

2025

&nbsp;Alçak Frekans ve Yüksek Frekans İşitme Kaybı Olan Cihaz Kullanacak HastalardaMizofoni, Hiperakuzi ve Tinnitus Anketi ile DeğerlendirmeTuba Doğan Karataş1, Merve Çiftçi2, Marwan K.s Al Hazzar1, Ahmet Aksoy1, Mansur Doğan11Cumhuriyet Üniversitesi, Kulak Burun Boğaz Ana Bilim Dalı, Sivas.2Erbaa Devlet Hastanesi, Kulak Burun Boğaz Ana Bilim Dalı, Tokat/ Erbaa.Amaç: İşitme kaybı, etkilenen frekans aralığına göre farklı klinik tablolarla ortaya çıkabilir ve mizofoni, hiperakuzi iletinnitus gibi işitsel hassasiyet bozukluklarıyla birlikte görülebilir. Bu durumların anlaşılması, işitme cihazı seçimi verehabilitasyon stratejilerinin optimize edilmesi açısından önem taşımaktadır. Bu çalışmada, düşük ve yüksekfrekanslı işitme kaybı olan hastalarda mizofoni, hiperakuzi ve tinnitusun sıklığı ve şiddeti standart anketlerkullanılarak değerlendirildi.Gereç-Yöntem: Bu kesitsel çalışmaya, işitme kaybı türüne göre düşük, yüksek veya mikst gruba ayrılan 100 hastadahil edildi. Mizofoni, Mizofoni Anketi (MISO); hiperakuzi, Hiperakuzi Ölçeği; tinnitus ise standart bir tinnitus anketiile değerlendirildi. İşitme kaybı tipi ile semptom şiddeti arasındaki ilişkiler Ki-kare testi, Monte Carlo simülasyonları,Cramér’s V istatistiği ve lojistik regresyon analizleriyle incelendi. Etki büyüklükleri bootstrap yöntemleriylehesaplandı.Bulgular: İşitsel hassasiyet bozuklukları arasında tinnitus, frekans-spesifik işitme kaybı ile anlamlı ilişki göstermiştir(p &lt; 0.05). Buna karşılık mizofoni ve hiperakuzi açısından istatistiksel olarak anlamlı bir ilişki saptanmamıştır.Cinsiyet, bağımsız olarak hiperakuzi ile ilişkili bulunmuştur (OR ≈ 3, p = 0.046). Mizofoni ve hiperakuzi şiddetiarasında orta düzeyde pozitif korelasyon saptanmıştır. Yaş ve cinsiyete göre yapılan alt grup analizlerinde benzereğilimler gözlenmiştir.Sonuç: Bu çalışma, düşük ve yüksek frekanslı işitme kaybı olan bireylerde mizofoni, hiperakuzi ve tinnitus gibiişitsel hassasiyet bozukluklarının dikkate değer sıklıkta görüldüğünü ortaya koymuştur. Bulgular, işitme kaybınınyalnızca odyometrik eşiklerle sınırlı kalmadan, bireysel işitsel hassasiyetlerle birlikte değerlendirilmesi gerektiğinigöstermektedir. Bu durum, kişiye özel işitme rehabilitasyonunun başarısı için cihaz öncesi kapsamlı değerlendirmesürecinin önemini vurgulamakta ve gelecekte daha geniş örneklemlerle yapılacak araştırmalar için değerli bir temeloluşturmaktadır.Anahtar Kelimeler: Frekans-spesifik İşitme Kaybı, Hiperakuzi, İşitme Kaybı, Mizofoni, Tinnitus</p

**ИИ:** + · клиническая группа · Cross-sectional study of 100 hearing-loss patients; it assessed misophonia frequency with a misophonia questionnaire.

**Решение:** =

---

### 105 · R0257

**Evaluation of Attention and Verbal Memory Functions of Individuals with Misophonia**

2025 · Neuropsychiatric Investigation · article, journalarticle, thesis · en · https://doi.org/10.5152/neuropsychiatricinvest.2025.24063

Mizofoni diğer insanlar tarafından çıkarılan belirli seslere karşı olumsuz duygusal ve davranışsal tepkiler verme ile karakterize olan bir durumdur. Bu çalışmada mizofoni semptomları olan bireylerin dikkat ve sözel bellek performanslarının nöropsikolojik testlerle değerlendirilmesi amaçlanmıştır. Gereç ve Yöntem: Çalışmaya psikiyatri ve kulak burun boğaz bölümü tarafından değerlendirilen ve mizofoni semptomları olduğu belirlenen 30 kişi ile mizofoni semptomları olmayan 40 kontrol olmak üzere 70 katılımcı dahil edilmiştir. Katılımcılara Depresyon Anksiyete Stres Ölçeği (DASÖ-21), Mizofoni Ölçeği, Sayı Menzili Testi (SMT), Sözel Akıcılık Testi (SAT), Stroop Testi (ST) ve Öktem Sözel Bellek Süreçleri Testi (Öktem-SBST) uygulanmıştır. Bulgular: Mizofonisi olan grubun DASÖ-21 alt boyutları ve toplam puanları mizofonisi olmayanlara göre istatistiksel olarak anlamlı yüksek olduğu bulunmuştur (p &lt; 0.05). Sözel Akıcılık Testi-semantik akıcılık bölümünde mizofonisi olanlar kontrol grubuna göre anlamlı olarak düşük performans göstermiştir (p &lt; 0.05). Stroop Testi -yanlış sayısı mizofonisi olanlarda kontrol grubuna göre anlamlı olarak yüksek bulunmuştur (p &lt; 0.05). Stroop testinin diğer boyutlarında, SMT, SAT-fonetik akıcılık ve SBST görevlerinde ise mizofonisi olanlar kontrollerle benzer performans gösterdiler. Sonuç: Mizofonisi olan grubun depresyon, anksiyete ve stres düzeylerinin yüksek olduğu; bazı dikkat parametlerinde düşük performans gösterdikleri görülmüştür. Sözel bellek performansları ise kontrollerle benzerdir. Mizofonide dikkat ve bellek arasındaki ilişkinin daha büyük örneklem ve daha kapsamlı nöropsikolojik testlerle değerlendirilmesinin literatüre katkı sağlayacağı düşünülmektedi

**ИИ:** ? · выборка неясна · Case-control study; 30 misophonia cases identified at psychiatry/ENT clinics. Unclear whether a clinic pool was screened or cases were recruited for misophonia.

**Решение:** =

---

### 106 · R0258

**"Rejection Makes Me Suspicious": Complex Temporal Network Approach to the Dynamics of Real-Time Paranoid Thoughts and Psychological Vulnerability.**

2025 · Schizophrenia bulletin open · article, journal article, journalarticle · eng · https://doi.org/10.1093/schizbullopen/sgaf021

Abstract Background and Hypothesis Theoretical models and empirical evidence suggest that paranoid thoughts stem from a heightened sense of vulnerability, including the perception of the world as dangerous, and fears of rejection and social evaluation. However, the factors contributing to this sense of vulnerability and the complex interplay between these elements remain underexplored. Study Design A total of 175 individuals recruited from a nonclinical community sample, including 103 participants with low levels of paranoid thoughts (LP) and 72 with high levels (HP), took part in a 7-day ESM study assessing momentary levels of paranoia, social functioning, social rejection, negative affect, body image, and misophonia symptoms. Temporal, contemporaneous, and between-subject network models were estimated for the total sample and its subgroups separately. Study Results The temporal network identified paranoid thoughts as a predictor of negative affect, feelings of rejection, and negative body image, while in turn being predicted by feelings of rejection and reduced social safety. A bidirectional relationship between paranoia and social rejection emerged. These findings were supported by contemporaneous and between-subject networks, which showed that paranoid thoughts co-occurred with and were, on average, linked to feelings of rejection, negative affect, and reduced social safety. Conclusions These findings suggest that social rejection plays a central role in paranoia. While group differences in network structure were modest, the HP group exhibited more numerous and stronger connections between variables, suggesting that paranoia may develop through the gradual reinforcement of connections between symptoms rather than structural shifts, highlighting the importance of early intervention.

**ИИ:** ? · выборка неясна · Community sample chosen for paranoia level, not misophonia; momentary misophonia symptoms were measured, but a case definition or count is uncertain.

**Решение:** =

---

### 107 · R0259

**A Psychometric Analysis of the Duke Misophonia Questionnaire.**

2025 · Journal of clinical psychology · article, journal article, journalarticle · eng · https://doi.org/10.1002/jclp.70028

ABSTRACT Background The Duke Misophonia Questionnaire (DMQ) is one of few psychometrically constructed scales designed to measure misophonia, a condition characterized by heightened sensitivity to specific auditory stimuli, resulting in strong emotional, physiological, and behavioral responses. While prior research has evaluated the dimensionality of individual subscales, a comprehensive psychometric analysis of the entire DMQ has not been conducted. Objectives This study aimed to extend the psychometric evaluation of the DMQ using contemporary psychometric methodologies to enhance its consistency, stability, and applicability in future research. Methods Two samples of university students were recruited online via a research participation pool (Sample 1: N = 318; Sample 2: N = 424; both predominantly female and White, aged 18–30). A novel, empirically derived five‐factor model (beliefs, coping, impairment, aversion, and anxiety) and the theoretically defined eight‐factor model, developed from clinical and theoretical foundations, were assessed. The five‐factor model was further examined using multidimensional item response theory (MIRT) to gain insights into item‐ and test‐level functioning. Results Both models demonstrated adequate fit, though the five‐factor model was more parsimonious and fit slightly better. Neither model contained cross‐loadings. The five‐factor model was further evaluated through MIRT which found that the DMQ provides the most information at moderate to high levels of misophonia severity. This analysis provided valuable information regarding the functioning and efficiency of the DMQ at both item and test levels. Conclusion The results contribute to the refinement of the DMQ by identifying a more parsimonious psychometric structure, promoting greater consistency and stability in its use for future misophonia research.

**ИИ:** + · валидация шкалы · Psychometric validation of the DMQ in two unselected university student samples recruited from a research participation pool.

**Решение:** =

---

### 108 · R0260

**A Tutorial on Supervised Machine Learning Variable Selection Methods in Classification for the Social and Health Sciences in R**

2025 · Journal of Behavioral Data Science · article, journalarticle, review · en · https://doi.org/10.35566/jbds/bain

With the increasing availability of large datasets in the behavioral and health sciences, the need for efficient and effective variable selection techniques has grown. While traditional methods like stepwise regression remain prevalent, numerous advanced techniques are available but underutilized in these fields. This tutorial aims to increase awareness and understanding of five variable selection methods available in the popular statistical software R: LASSO, Elastic Net, a penalized SVM classifier, random forest, and the genetic algorithm. Using a recent survey-based assessment dataset on misophonia diagnosis, we provide step-by-step guidance on variables selections and implementation of each method in the context of classification. We discuss the strengths, weaknesses, and performance of each technique, emphasizing the importance of selecting appropriate performance metrics. The associated code and data implemented in this tutorial are available on Open Science Framework and provide an interactive learning experience. We encourage social and health science researchers to adopt these advanced variable selection methods, leading to more robust, interpretable, and impactful models. This paper is written with the assumption that individuals have at least a basic understanding of R.

**ИИ:** ? · выборка неясна · Methods tutorial reusing a misophonia diagnosis survey dataset; the sample's origin is unclear, and the class proportions might give prevalence.

**Решение:** =

---

### 109 · R0261

**Misophonia in Tic Disorders and Their Neuropsychiatric Associations**

2025 · Movement Disorders Clinical Practice · article, journal article, journalarticle · eng · https://doi.org/10.1002/mdc3.70017

inform clinical and pathophysiological research to develop targeted interventions for this underexplored symptom.

**ИИ:** + · клиническая группа · Misophonia assessed in a tic disorder clinical group; abstract truncated, but the title suggests it may report frequency.

**Решение:** =

---

### 110 · R0267

**Misophonia Symptoms Severity is Attributed to Impaired Flexibility and Heightened Rumination**

2025 · bioRxiv · article, preprint, text/preprint · en · https://doi.org/10.1101/2025.01.13.632542

Abstract Misophonia is a disorder involving sensitivity to certain sounds and related stimuli. Here, we explore the relationship between misophonia and affective flexibility, which describes cognitive shifting abilities in the face of emotion-evoking stimuli. Previous evidence suggests impaired subjective cognitive flexibility in misophonia, but this relationship has not been confirmed behaviourally or in emotionally-salient contexts. The secondary aim of this study is to test the potential association between misophonia and cognitive flexibility, building upon findings from previous research. The third objective is to examine the relationship between misophonia and rumination, a maladaptive cognitive process characterized by repetitive negative thinking and linked to both cognitive and affective inflexibility. One hundred and forty participants completed the recently developed Memory and Affective Flexibility Task (MAFT), designed to assess affective flexibility, as well as a battery of self-report measures to evaluate misophonia severity, cognitive flexibility and rumination. Results suggested an inverse relationship between affective flexibility as measured by switch accuracy, but not reaction time, and misophonia severity. Cognitive flexibility was also inversely associated with misophonia severity, but notably did not attribute to task-based affective flexibility, suggesting two independent constructs both involved in misophonia manifestation. Rumination associated positively with misophonia severity and inversely with cognitive flexibility, but not affective flexibility. Taken together, these findings highlight a unique cognitive profile of misophonia, characterized by rigidity at the psychological level through cognitive inflexibility and rumination, as well as at the executive-function level in terms of affective switching difficulties.

**ИИ:** ? · выборка неясна · 140 participants completed a misophonia severity measure. Recruitment isn't described, so the sample may be unselected and could yield case counts.

**Решение:** =

---

### 111 · R0268

**Sensory Gating & Misophonia**

2025 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract; this is an empirical preprint on sensory gating and misophonia, and it may have screened an unselected sample.

**Решение:** =

---

### 112 · R0269

**Sensory Gating &amp; Misophonia**

2025 · OSF · project

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · OSF project with no abstract; a sensory gating study might screen an unselected pool for misophonia.

**Решение:** =

---

### 113 · R0272

**The pediatric misophonia and hyperacusis questionnaire (PMHQ): a screening tool inspired by the MisoQuest and hyperacusis questionnaire.**

2025 · International journal of audiology · article, dataset/dataset, journal article · eng · https://doi.org/10.1080/14992027.2025.2478519

Abstract Objective Decreased Sound Tolerance (DST) conditions often emerge in childhood, making early identification and treatment important. This paper details the development and validation of the Paediatric Misophonia and Hyperacusis Questionnaire (PMHQ), a dual DST parent-report screening tool intended to provide early identification of misophonia and hyperacusis among children with and without autism age 6-17 years. Study designs and samples Three studies were completed including (1) content development with input from audiology experts (n = 9) and parents of children with DST conditions (n = 20); (2) content revision to improve relevance to autism with input from parents of children with autism (n = 15); and (3) psychometric analysis of item characteristics of the PMHQ based on responses from parents of children age 6-17 years (n = 200). Results The PMHQ-4 demonstrates adequate psychometric properties at the item level (item discrimination, difficulty, item information function) and at the test level (test information function). A definitive version of the PMHQ with recommended cut-off scores for each subscale is provided. Conclusions The resulting PMHQ-4 is a 14-item screening tool comprised of 8 misophonia and 6 hyperacusis items. The PMHQ-4 can provide a valid measure of misophonia and hyperacusis for children age 6-17 years. Further evaluation is warranted in clinical DST samples.

**ИИ:** + · валидация шкалы · Validation of a pediatric misophonia questionnaire in 200 parents of children with and without autism; it gives cut-offs, and the sample seems not misophonia-selected.

**Решение:** =

---

### 114 · R0279

**no title**

2025 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.17825555

No abstract available.

**ИИ:** ? · нет аннотации · Zenodo preprint with no title or abstract; eligibility can't be judged, so full-text check needed.

**Решение:** -6 не про мизофонию

---

### 115 · R0280

**no title**

2025 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.17825556

No abstract available.

**ИИ:** ? · нет аннотации · 2025 Zenodo preprint with no title or abstract, so eligibility can't be judged; the full record needs checking.

**Решение:** -6 не про мизофонию

---

### 116 · R0281

**no title**

2025 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.17887214

No abstract available.

**ИИ:** ? · нет аннотации · Zenodo preprint (2025) with no title or abstract; can't judge eligibility, so it needs a manual metadata check.

**Решение:** -6 не про мизофонию

---

### 117 · R0283

**Do emotional reactions to trypophobia stimuli rely on similar mechanisms as misophonia, ASMR, and musical chills?**

2025 · Lifecycle Journal · article, studyregistration/pre-registration, preprint · und · https://doi.org/10.71240/lcyc.689209

Trypophobia and misophonia are sensory-affective phenomena that scientists only recently began studying. Trypophobia is when repeating visual-spatial patterns of holes or bumps cause negative reactions, whereas misophonia is when repeating auditory-temporal patterns of chewing or tapping sounds cause negative reactions. Both phenomena can be measured using self-report questionnaires or measurement of reactions in real-time to exposure to triggering stimuli. Research on misophonia has shown links from both self-report and real-time reactions with other auditory emotional experiences like autonomous sensory-meridian response and musical chills, with brain imaging studies showing overlapping brain networks activated during all three of these experiences. Here, we ask whether trypophobia and misophonia show correlations with each other, which could imply that they also share similar psychological and neural mechanisms. We will therefore measure self-report and real-time measures of trypophobia and misophonia in 200 participants, with the sample-size determined by a power analysis designed to detect r=0.20 (alpha=.05, power=0.80). We will also measure disgust sensitivity and neuroticism in the same participants to see if trypophobia and misophonia correlate similarly to these additional psychological constructs that have been previously linked to trypophobia and/or misophonia. These findings will be helpful in motivating future studies exploring the common psychological and neural mechanisms underlying sensory-affective processing more generally.

**ИИ:** ? · выборка неясна · Pre-registered study measuring misophonia by self-report in 200 participants, apparently unselected; recruitment unclear and results not yet reported.

**Решение:** -7 preregistration without data

---

### 118 · R0288

**Examining Changes in Behavioral, Emotional, and Tic Symptoms in a Pediatric Sample in the First Year of the Pandemic.**

2025 · Child psychiatry and human development · journal article · eng · https://doi.org/10.1007/s10578-025-01817-3

Previous studies have documented worsening behavioral and emotional symptoms in children during the COVID-19 pandemic, although much focus has been on internalizing conditions with relatively short follow-up time. We examined a range of symptoms before and during the pandemic through mid-2021 in a primary care sample. Children 4-17 (n = 181) who completed emotional and behavioral assessments prior to the pandemic and then completed a follow-up assessment during the pandemic were included in our analyses. We examined changes in broad-based and clinical scales, including the Behavior Assessment System for Children and the Diagnostic and Statistical Manual of Mental Disorders, across the total sample and among subgroups using paired t-tests. Subgroups included sex, race, and ethnicity, and baseline internalizing, externalizing, and adaptive scores. Children without clinically significant elevations in internalizing, externalizing, and adaptive scores at baseline experienced worsening of symptoms in a greater number of areas than children with clinically significant elevations at baseline. Females and Black children tended to experience greater worsening of symptoms than males and White children, respectively. Our findings suggest worsening symptoms in children persisting one year into the pandemic, particularly for those without clinically significant symptoms at baseline.

**ИИ:** ? · другое · Unselected pediatric primary care sample with a broad symptom battery; the abstract doesn't mention misophonia, but the full text may include it.

**Решение:** -6 не про мизофонию

---

### 119 · R0291

**Investigating autistic hyperfocus and monotropism: Limited convergence of event-related potentials, laboratory tasks, and questionnaire responses.**

2025 · Research in autism · article, preprint, journal article · eng · https://doi.org/10.1016/j.reia.2025.202683

Purpose: The autistic-developed monotropism account suggests autism is characterized by hyper-focus towards interests, although hyper-focus research has not explored associations among self-/caregiver-report and lab-based measures. Other findings suggest autistic attention has an enhanced capacity and/or is unusually prone to involuntary capture. This study used questionnaires and lab-based tasks to investigate autistic attention and probe its relations to inattention/distractibility, sensory experiences, and anxiety. Methods: 18 autistic and 22 comparison adolescents completed self-report measures of hyper-focus, anxiety, and sensory experiences, and laboratory psychoacoustic tasks, visual working memory and cross-modal attention capture accuracy and reaction time tasks, and a hyper-focus paradigm relying on the N2pc and Pd event-related potentials. Participants’ caregivers completed proxy hyper-focus, anxiety, sensory experiences, and inattention questionnaires. Results: Autistic participants had elevated hyper-focus per self- and caregiver-report questionnaires, and exhibited less visual working memory capacity, potentially reflecting difficulty attending to multiple targets. However, groups did not differ in event-related potentials indexing hyper-focus, or behavioural cross-modal attention capture. Different types of attention measures were generally not related to one another. Participants and their caregivers overall viewed hyper-focus’ impact as modestly positive, with individual opinions differing. Self-reported hyper-focus was related to self-reported misophonia and sensory hyperreactivity. Conclusions: Questionnaires suggest hyper-focus is elevated in autism and has mixed, nuanced real-world impacts. However, some laboratory paradigms with explicit instructions in highly controlled, often non-naturalistic environments may struggle capture real-world autistic attentional experiences; additional research is needed to align laboratory and questionnaire measures. This study also suggests autistic perceptual capacities are not globally enhanced.

**ИИ:** + · клиническая группа · Autistic and comparison adolescents, not recruited for misophonia, completed a self-report misophonia measure; full text may report case counts.

**Решение:** =

---

### 120 · R0292

**Using Psychoacoustic Tasks and Multidimensional Questionnaires to Characterize Auditory Hyperreactivity in Autistic Young People.**

2025 · Journal of autism and developmental disorders · article, data paper, preprint · eng · https://doi.org/10.1007/s10803-025-06924-7

Purpose: Prior studies of auditory hyperreactivity in autism have often not distinguished between different aspects of auditory sensory discomfort, such as hyperacusis and misophonia. The present study rigorously characterizes multiple forms of auditory sensory hyperreactivity, using a mixture of laboratory-based psychoacoustic tasks and self- and caregiver-reported questionnaires, and examines group differences and relationships among different measures. Methods: 18 autistic and 22 comparison adolescents rated the pleasantness of conventionally-pleasant, conventionally-unpleasant, and misophonic trigger sounds at intensities of 50 through 80 dB SPL. They also provided hearing thresholds, loudness discomfort levels, and filled out a number of questionnaires; their caregivers completed additional questionnaires. Results: Autistic participants rated conventionally-pleasant sounds as being more unpleasant at intensities of 60 through 80 dB, but overall loudness discomfort caused by pure tones did not significantly differ across groups, nor did ratings of common misophonic triggers appear to differ. Autistic participants nevertheless self-reported more auditory hyper-reactivity, including hyperacusis and misophonia. However, in the autism group, self-reported auditory hyper-reactivity scores were unexpectedly lower than caregiver-reported scores. Psychoacoustic task and some questionnaire-based measures of misophonia converged well, but hyperacusis measures did not converge well. Conclusions: Sound intolerance reportedly affected autistic participants’ quality of life. Autistic aversions to some conventionally-pleasant sounds did not appear to be accompanied by overall heightened loudness distress at the group level, emphasizing the complexity and seeming idiosyncrasy of sensory discomfort and distress in autism. Psychoacoustic sound rating tasks showed some convergence and some divergence with questionnaire measures, pointing to the importance of multimodal measurement.

**ИИ:** + · клиническая группа · Autistic adolescents and comparison adolescents, not recruited for misophonia, completed misophonia questionnaires, so the full text may report case counts.

**Решение:** =

---

### 121 · R0294

**Investigation of Misophonia Frequency, Disgust Sensitivity, and Anger Expression Style in Patients Diagnosed with Obsessive-Compulsive Disorder**

2025 · Psychiatry and Behavioral Sciences · article, journalarticle, google scholar result · en · https://doi.org/10.5455/pbs.20250504060857

Objective: Obsessive-compulsive disorder (OCD) is a chronic psychiatric condition characterized by recurrent obsessions and/or compulsions that cause marked distress and functional impairment. Emerging evidence suggests a potential link between OCD and misophonia, a condition defined by disproportionate emotional and physiological responses to specific auditory stimuli. This study aimed to examine the prevalence of misophonia in individuals with OCD and to explore its associations with disgust sensitivity and anger expression styles. Method: The study included 51 patients diagnosed with OCD according to DSM-5 criteria and 61 age- and gender-matched healthy controls. All participants completed the Padua Inventory–Washington State University Revision (PI-WSUR) to assess OCD symptoms, the Misophonia Scale (MS) to evaluate misophonia severity, the Disgust Sensitivity Scale–Revised (DS-R) to assess disgust sensitivity, and the Trait Anger–Anger Expression Scale (TA-AES) to evaluate anger expression patterns. Data were analyzed using appropriate statistical methods. Results: Patients with OCD exhibited significantly higher total misophonia scores compared to healthy controls (p = 0.037). Statistically significant differences were also observed between groups in DS-R total and subscale scores (p &lt; 0.001), as well as in the TA-AES subscales of trait anger (p &lt; 0.001), anger control (p &lt; 0.001), and anger out (p = 0.036). Positive and statistically significant correlations were identified between MS total score and DS-R total (r = 0.313), core disgust (r = 0.296), and contamination disgust (r = 0.422) subscales. Additionally, MS total score was positively correlated with PI-WSUR total score (r = 0.459) and all subscales except for the checking compulsion subscale. Conclusion: These findings suggest that misophonia frequently co-occurs with OCD and is significantly associated with elevated disgust sensitivity and maladaptive anger expression styles. The observed symptom overlap may reflect shared neurobiological or cognitive mechanisms. Further studies are warranted to elucidate the underlying pathways linking misophonia and OCD and to evaluate interventions targeting misophonia symptoms in this population.

**ИИ:** + · клиническая группа · An OCD clinical group and healthy controls were assessed with the Misophonia Scale. The study aimed to estimate misophonia prevalence in OCD.

**Решение:** =

---

### 122 · R0295

**Comportamiento de la migraña en estudiantes de la carrera de fisioterapia de la Pontifica Universidad Católica del Ecuador**

2025 · Revista de Ciencias Médicas de Pinar del Río · article · en · https://core.ac.uk/download/658974967.pdf

Introduction: migraine is multifactorial, influenced by genetic, hormonal and environmental factors, with a biopsychosocial impact that is not yet fully understood.Objective: to evaluate the behavior of migraine in students of the physiotherapy career.Methods: a mixed, observational, and correlational study was conducted with physical therapy students from the Pontifical Catholic University of Ecuador. A sample of 104 students was selected using simple random probability sampling, meeting the selection criteria. Surveys and observations were used to obtain the information that led to the variables analyzed. Descriptive statistical methods were used, respecting medical ethics.Results: the majority of students were female (58,5 %), who worked all week (43,2 %), and had no children (63,1 %). A high percentage (93,3 %) reported having previously suffered from headaches. Among the 97 students who experienced them, 51,6 % reported difficulties that did not prevent them from carrying out their daily activities. The most frequent clinical manifestation associated with headaches was photophobia (26,8 %), followed by misophonia, nausea, and vomiting (23,7 % each). Regarding psychosocial factors, 41,3 % presented normal stress levels, and 40,4 % normal anxiety levels.Conclusions: migraine is a common disorder that affects physical and mental functioning. Its origin is multifactorial, involving genetic, hormonal, and environmental factors. Although there is evidence of the influence of biopsychosocial factors, limitations persist that hinder a complete understanding of their relationship with migraine.Introducción: la migraña es multifactorial, influida por factores genéticos, hormonales y ambientales, con impacto biopsicosocial aún no completamente comprendido.Objetivo: evaluar el comportamiento de la migraña en estudiantes de la carrera de fisioterapia.Métodos: estudio mixto, observacional y correlacional desarrollado estudiantes de Fisioterapia de la Pontificia Universidad Católica del Ecuador. Mediante un muestreo probabilístico aleatorio simple fue seleccionada una muestra de 104 estudiantes, quienes cumplieron los criterios de selección. Se aplicaron encuestas y observación para obtener la información que dio salida a las variables analizadas. Se emplearon métodos de estadística descriptiva, respetándose la ética médica.Resultados: predominaron los estudiantes del sexo femenino (58,5 %), que trabajan durante toda la semana (43,2 %) y no tienen hijos (63,1 %). Un alto porcentaje (93,3 %) refirió haber padecido cefalea previamente. Entre los 97 estudiantes que la presentaron, el 51,6 % reportó dificultades que no les impidieron realizar sus actividades diarias. La manifestación clínica más frecuente asociada a la cefalea fue la fotofobia (26,8 %), seguida por misofonía, náuseas y vómitos (23,7 % cada uno). En cuanto a los factores psicosociales, el 41,3 % presentó niveles normales de estrés, el 40,4 % niveles normales de ansiedad.Conclusiones: la migraña es un trastorno frecuente que afecta el funcionamiento físico y mental. Su origen es multifactorial, involucrando factores genéticos, hormonales y ambientales. Aunque existen indicios sobre la influencia de factores biopsicosociales, aún persisten limitaciones que dificultan una comprensión completa de su relación con la migraña

**ИИ:** ? · другое · Random student sample reports 23.7% 'misophonia' as a headache symptom, probably phonophobia mislabelled; needs full-text check.

**Решение:** + ненабранный опрос со шкалой мизофонии

---

### 123 · R0299

**Exploring the Stability of Misophonia and Other Auditory Affective Experiences Throughout Development**

2025 · Digital Scholarship - UNLV (University of Nevada Reno) · conference-paper, text · en

Sounds can give rise to powerful affective experiences, both positive and negative. Misophonia is an intensely negative response to sounds such as chewing, whereas autonomous sensory meridian response (ASMR) and musical chills result are experiences as positive and pleasant. Anecdotally, all of these experiences occur as early as childhood, but we know relatively little about how they develop. We investigated this question longitudinally.https://oasis.library.unlv.edu/durep_posters/1275/thumbnail.jp

**ИИ:** ? · выборка неясна · Longitudinal poster measuring misophonia, ASMR and chills over development; sample probably unselected but not described.

**Решение:** =

---

### 124 · R0302

**Neural differentiation of misophonic individuals from clinical controls by left insula functional connectivity before r-TMS intervention**

2025 · Brain stimulation · article, journalarticle · en · https://doi.org/10.1016/j.brs.2024.12.593

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract. This is an rTMS study that compares misophonic people with clinical controls; a clinical pool may have been screened for misophonia.

**Решение:** =

---

### 125 · R0307

**Auditory discomfort and visual sensitivity.**

2025 · Vision research · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.visres.2025.108655

The field of visual discomfort is fast growing, identifying parameters of visual stimuli that evoke discomfort, their effect on the visual system, and their heightened impact in clinical populations. In contrast, there is little work on auditory discomfort. First, we reviewed the current findings in the field of auditory discomfort and report a preliminary study investigating the effects of uncomfortable sounds on near infrared spectroscopy (NIRS) responses from auditory cortex. Nine participants listened to pure 1 kHz tones that were modulated by a 2 Hz or a 16 Hz sinusoidal wave that made the tone sound as though it wobbled. The oxyhaemoglobin response to the uncomfortable 16 Hz sound was larger and slower compared to the relatively more comfortable 2 Hz sound. This suggests cortical excitability to uncomfortable sounds, similar to the heightened response reported in the visual modality. Second, we assessed the relationship between visual and auditory sensitivity in a large sample (N = 669) of participants who completed the Pattern Glare Test (PGT), the Amsterdam Misophonia Scale, the Hyperacusis Questionnaire, and the Functional Hearing Questionnaire (FHQ). While all measures of auditory sensitivity were significantly correlated with the number of illusions seen in the PGT (.1 > r s < 0.3), the relationship with misophonia was significantly weaker than other comparisons. This highlights that while those who are visually sensitive are more likely to exhibit increased auditory sensitivity, the measures that focus on pain (PGT, hyperacusis, FHQ) may be dissociable from those that rely on emotive discomfort (misophonia). Together, this suggests similar mechanisms underlying auditory and visual discomfort.

**ИИ:** + · ненабранная выборка · Large sample (N=669), apparently not recruited for misophonia, completed the Amsterdam Misophonia Scale; full text may report how many met a cutoff.

**Решение:** =

---

### 126 · R0310

**Individual Differences in Sensitivity to Everyday Sounds: Developmental, Environmental, and Personality Predictors of Auditory Processing**

2025 · Cureus · article · en · https://doi.org/10.7759/cureus.88141

Background Sensitivity to everyday sounds shows considerable individual variation. This study aimed to identify distinct dimensions of auditory sensitivity and examine how psychosocial and developmental factors, such as early auditory environments and personality traits, shape individual differences in non-clinical adults. In addition, we explored sensitivity to low-salience sounds that are typically perceived as non-intrusive by most people but elicit discomfort in a minority of individuals. Methods A cross-sectional web-based survey was conducted between September and November 2024 with 380 Japanese adults (aged 18-56), using a self-developed questionnaire informed by prior research and pilot testing. Participants rated their affective reactions to 39 everyday sounds. Factor analysis extracted latent auditory sensitivity components. Multiple regression analyses examined the predictive roles of childhood auditory environment and personality traits measured via standardized psychological scales. Results Based on factor analysis of participants' ratings across 39 everyday sounds, two underlying dimensions of auditory sensitivity were identified. These were labeled WLS1 and WLS2, reflecting different patterns of sensitivity: WLS1 represents sensitivity to subtle, non-salient sounds, while WLS2 reflects heightened reactivity to loud or sharp auditory stimuli. WLS1 was significantly predicted by childhood exposure to parental vocal discipline (β = 0.19, 95% confidence interval (CI) (0.07-0.31), p = 0.002), emotional reactivity (β = 0.23, 95% CI (0.09-0.36), p = 0.001), and interpersonal assertiveness (β = 0.24, 95% CI (0.10-0.37), p < 0.001). WLS2 was associated with female gender (β = 0.50, 95% CI (0.27-0.72), p < 0.001), insomnia from worry (β = 0.15, 95% CI (0.04-0.27), p = 0.006), fatigue (β = 0.30, 95% CI (0.17-0.43), p < 0.001), and impulsivity (β = 0.14, 95% CI (0.04-0.24), p = 0.008). A third factor, W1, reflecting sensitivity to ambient mechanical sounds that over 80% of participants rated as non-intrusive, was predicted by orderliness (β = 0.16, 95% CI (0.03-0.25), p = 0.012), emotional sensitivity (β = 0.21, 95% CI (0.08-0.34), p = 0.002), and a preference for uniqueness (β = 0.29, 95% CI (0.15-0.44), p < 0.001). Conclusions Auditory sensitivity is multifactorial and shaped by both developmental auditory experiences and personality dimensions. The results suggest that distinct psychological pathways underlie responsiveness to subtle versus intense auditory stimuli.

**ИИ:** ? · другое · Unselected Japanese adult survey of reactions to everyday sounds; misophonia not named, but the ad hoc items may cover misophonic triggers.

**Решение:** -6 не про мизофонию

---

### 127 · R0313

**Captions for Supplemental Tables and Figures.docx**

2025 · Carnegie Mellon University · other/online resource · https://doi.org/10.1184/r1/28828070

Supplementary Figure Captions and Table Captions, with links to figures, from this article:Heller LM, Oszczapinska U, Smith JM, Julien MM (2025) Reassigning sources of misophonic trigger sounds to change their unpleasantness: Testing alternative mechanisms with a new set of movies, paintings, and words. PLoS ONE 20(4): e0321594. https://doi.org/10.1371/journal.pone.0321594

**ИИ:** ? · выборка неясна · Supplement to an experimental misophonia study (Heller 2025). The sample may be an unselected online pool screened with misophonia measures; needs checking.

**Решение:** =

---

### 128 · R0314

**Reassigning sources of misophonic trigger sounds to change their unpleasantness: Testing alternative mechanisms with a new set of movies, paintings, and words.**

2025 · PloS one · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1371/journal.pone.0321594

We conducted nine experiments to determine why a sound’s pleasantness can be altered by movies, abstract paintings, and words. In Expt. 1, unpleasant sounds, such as the sound of a person sniffing, were paired either with their original video track or with video tracks depicting neutral events that could plausibly have produced the sound, such as pulling tissues out of a tissue box. While the unpleasant sounds were mildly unpleasant to a baseline population, these sounds were expected to be more unpleasant for people who have misophonia, a condition in which certain everyday sounds are unbearable. Consistent with past literature, neutral video tracks increased the sounds’ pleasantness for the non-misophonic and misophonic populations, by 0.98 and 1.59 points, respectively (on an 11-point scale). Movies rated as having better audio-visual matches produced greater changes in pleasantness, consistent with the hypothesis that sources reassignment caused the changes. Expt. 2 found a consistent result when the video tracks were replaced with written event descriptions, although the effect size was reduced. The next experiment inverted Expt. 1 and found that unpleasant video tracks decreased the pleasantness of neutral sounds by 2.12 points, but better-matching movies did not produce greater changes in pleasantness. We sought an alternative to the source reassignment explanation by obtaining ratings of audio-visual synchrony, cross-modal agreement in symbolism, source plausibility, and sound identifiability. No explanation was found for the effect of unpleasant videos. Furthermore, pleasant abstract paintings increased the pleasantness of unpleasant sounds by 0.37 points, correlating with cross-modal agreement but not with audio-visual match. Taken together, different types and patterns of match ratings can help discern the causal mechanisms by which visual stimuli are affecting sound pleasantness (e.g., source reassignment, cross-modal agreement). {Manuscript under revision, submitted to PLOSONE in March, 2024.}

**ИИ:** ? · выборка неясна · Experiments compare misophonic and non-misophonic participants; these may come from screening a general online pool, but the recruitment method is not stated.

**Решение:** =

---

### 129 · R0315

**Supplementary Data: Reassigning sources of misophonic trigger sounds to change their pleasantness**

2025 · Carnegie Mellon University · collection/collection · https://doi.org/10.1184/r1/c.7112221

This collection contains the video stimuli and supplementary material for the publication: "Reassigning sources of misophonic trigger sounds to change their unpleasantness: testing alternative mechanisms with a new set of movies, paintings, and words". Paper citation: Heller LM, Oszczapinska U, Smith JM, Julien MM (2025) Reassigning sources of misophonic trigger sounds to change their unpleasantness: Testing alternative mechanisms with a new set of movies, paintings, and words. PLoS ONE 20(4): e0321594. https://doi.org/10.1371/journal.pone.0321594 Database citation: Heller, Laurie M.; Oszczapinska, Urszula; Smith, Jessica; Julien, Megan (2025). Supplementary Data: Reassigning sources of misophonic trigger sounds to change their pleasantness. Carnegie Mellon University. Collection. https://doi.org/10.1184/R1/c.7112221

**ИИ:** ? · выборка неясна · Supplementary data for an experimental misophonia study; misophonia likely measured, but unclear whether the sample was unselected.

**Решение:** =

---

### 130 · R0317

**The Turkish Adaptation of Sussex Misophonia Scale and A Short Form of the Scale**

2025 · OSMANGAZİ JOURNAL OF MEDICINE · article, journalarticle · en · https://doi.org/10.20515/otd.1537885

Misophonia is a neuropsychiatric disorder characterized by emotions, thoughts, behaviours toward certain sensory stimuli. Sussex Misophonia Scale (SMS) is one of the scales intending to measure misophonia. In this study we aimed to conduct Turkish adaptation of SMS and present a short form of the scale. We conducted a translation and back-translation process. The scale was applied to a subgroup of the sample. In line with feedback final version was distributed via online platforms. Reliability and validity analyses were conducted. Due to multi-loading of items, 19 items from Part II were eliminated. We defined this 19-itemed form as short form of the scale and same reliability, and validity analyses were conducted with this short form. SMS was reliable scale with .97 The Cronbach's Alpha value for Part 2. However, in EFA analysis, Kaiser-Meyer-Olkin analysis was conducted, resulting in value of .954. The Bartlett’s Test of Sphericity yielded a value of χ2=8508.921and a p&amp;lt;.001. The short form demonstrated a Cronbach's Alpha value of .913. Both original and short form of the scale were clinically valid. The Turkish version of SMS was reliable and valid scale. We presented short form of Part II of the scale and this short form was also reliable and valid.

**ИИ:** + · валидация шкалы · Turkish validation of the Sussex Misophonia Scale using an online sample that appears to be general rather than misophonia-selected; prevalence may be reported.

**Решение:** =

---

### 131 · R0318

**Traducción y adaptación transcultural del Duke Misophonia Questionnaire (DMQ) para población mexicana**

2025 · Anales Médicos de la Asociación Médica del Centro Médico ABC · article, journalarticle · es · https://doi.org/10.24875/amh.m25000102

Antecedentes: La misofonía es considerada un trastorno neurofisiológico y del comportamiento complejo de origen multifactorial, caracterizado por una hiperreactividad fisiológica, emocional y conductual ante sonidos específicos. Una variante que impide comparar datos de otros estudios es el tipo de instrumento utilizado para evaluar a los sujetos, pues actualmente existe una diversidad de ellos elaborados en otros países angloamericanos que requieren su adaptación transcultural, debido a que no existe este proceso para población mexicana. Objetivo: Realizar la traducción y adaptación transcultural del Duke Misophonia Questionnaire (DMQ) al español mexicano. Material y métodos: Se trata de un estudio con diseño de validación de instrumentos del cual se realizará la primera fase del proceso, denominada «traducción y adaptación cultural», de acuerdo con el método de Ramada-Rodilla sobre traducción, adaptación cultural y validación, consistente en traducción directa, síntesis, traducción inversa, consolidación por comité de expertos y pretest. Resultados: Se obtuvo una versión traducida y adaptada culturalmente para la población mexicana. El cuestionario final cuenta con una congruencia semántica, experimental, conceptual e idiomática. Conclusiones: Se obtuvo un cuestionario traducido y adaptado al español mexicano, concluyendo la primera fase del procedimiento para la traducción, la adaptación cultural y la validación de cuestionarios. En este punto se puede continuar con la segunda fase de validación.

**ИИ:** ? · выборка неясна · Translation/cultural adaptation of DMQ for Mexico; pretest sample not described, may report misophonia scores in non-selected participants.

**Решение:** =

---

### 132 · R0323

**Reliability and validity of the Japanese version of the Misophonia Questionnaire (MQ).**

2025 · Journal of psychiatric research · article, preprint, journal article · eng · https://doi.org/10.1016/j.jpsychires.2025.05.040

The Misophonia Questionnaire (MQ) is a self-report measure designed to assess misophonia symptoms. It has been validated in various languages and across different samples. However, no prior research has validated the MQ in Japanese samples. This study aimed to develop a Japanese version of the Misophonia Questionnaire (MQ-J) and examine its psychometric properties. This study confirmed the score distribution, internal consistency, and factor structure in a Japanese sample via an online survey. We also compared the MQ-J scores between individuals with misophonia symptoms and control participants. Additionally, we examined the relationships between the MQ-J and sensory processing issues, obsessive-compulsive tendencies, anxiety, depressive symptoms, and difficulties in daily life. Results demonstrated excellent internal consistency (alpha = .93) for the MQ-J, with significantly higher scores in the misophonia group compared with the control group. Furthermore, significant positive correlations were observed with sensory processing problems, obsessive-compulsive tendencies, anxiety, depressive symptoms, and difficulties in daily life. These findings supported the validity and reliability of the MQ-J. Hence, the MQ-J was a valuable tool for assessing misophonia symptoms in Japanese adults.This work was supported by JSPS KAKENHI Grant Numbers JP24K16882 and JP25K00887

**ИИ:** + · валидация шкалы · Japanese MQ validation using a general online adult sample; misophonia vs control groups suggest a case count may be reported.

**Решение:** =

---

### 133 · R0324

**Prevalence of misophonia in patients with bipolar disorder: its relationship with autism spectrum symptoms and emotion regulation skills in comparison to a control group.**

2025 · Nordic journal of psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.1080/08039488.2025.2511068

Abstract Introduction The aim of this study is to determine the prevalence of misophonia in patients diagnosed with bipolar disorder (BD), examine its relationship with autism spectrum symptoms and emotion regulation skills, and compare it with a healthy control group. Methods The study included 105 patients diagnosed with BD in remission for at least three months and 105 age-, gender-, and education-matched healthy controls. All participants completed the sociodemographic data form, Hamilton Depression Rating Scale, Young Mania Rating Scale, Revised Amsterdam Misophonia Scale, Emotion Regulation Skills Questionnaire, and Autism Spectrum Quotient. Results Misophonia symptoms were statistically significantly more prevalent in the healthy control group (63.8%) than in the BD group (48.6%) (p = 0.026). Among BD patients with misophonia symptoms, a history of suicide attempts and higher autistic traits were statistically significantly more common (p = 0.026, p = 0.003, respectively). No statistically significant relationship was found between the severity of misophonia and autism traits (r = 0.200; p = 0.159) or emotion regulation skills (r = −0.178; p = 0.210). Multivariate regression analyses identified suicide attempt history and autistic traits as significant predictors of misophonia severity. Conclusion Misophonia symptoms were more prevalent in control group, contrary to our hypothesis. BD patients exhibited pronounced emotion regulation deficits, which worsened with increased autistic traits. Misophonia symptoms were statistically significantly associated with adverse psychiatric outcomes in BD patients. These findings highlight the importance of assessing misophonia, emotion regulation, and autistic traits collectively in clinical settings, and suggest that addressing misophonia symptoms in treatment planning may enhance patient functioning.

**ИИ:** + · клиническая группа · Bipolar disorder patients and matched controls screened with AMISOS-R; reports misophonia prevalence (48.6% vs 63.8%).

**Решение:** =

---

### 134 · R0332

**Auditory Brainstem Response Patterns in Misophonia: A Comparative Study**

2025 · شنوایی شناسی - دانشگاه علوم پزشکی تهران · article, journalarticle, google scholar result · und · https://doi.org/10.18502/avr.v35i1.20576

Background and Aim: Misophonia is a condition characterized by a reduced tolerance to certain sounds or the stimuli linked to those sounds. Our study aimed to investigate the auditory brainstem functioning using electrophysiological measures in normal-hearing individuals with and without misophonia. Methods: Thirty participants aged between 18 and 30 years were recruited. They were divided into two primary groups: fifteen individuals diagnosed with misophonia and fifteen controls. The selection of participants with misophonia was based on the diagnostic criteria by Schröder et al. and the MisoQuest questionnaire; Auditory Brainstem Response (ABR) was recorded from all the individuals at lower (11.1/s) and higher stimulus rates (90.1/s). Results: On analysing the data, individuals with misophonia showed significantly shorter absolute latencies of ABR waves III and V at 11.1/s. Also, there was no significant difference in the absolute amplitude of ABR waves at 11.1/s and 90.1/s between the individuals with and without misophonia. Conclusion: This study indicates that the shorter absolute latencies of ABR waves III and V in individuals in misophonia could be attributed to hyperactivity at the sub-cortical pathway regions compared to the control group.

**ИИ:** ? · выборка неясна · Case-control ABR study; misophonia group identified with Schröder criteria and MisoQuest. The full text may show they were screened from an unselected pool.

**Решение:** =

---

### 135 · R0334

**Multichannel auditory cortical responses in misophonia: A neurophysiological investigation.**

2025 · Hearing research · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.heares.2025.109458

Misophonia is characterized by intense emotional responses to specific sounds, yet its neurophysiological basis remains unclear. This study investigated auditory cortical processing using multichannel auditory late latency responses (ALLR). ALLR recordings were obtained from 30 participants (15 with misophonia and 15 controls). Latencies and amplitudes of the P1-N1-P2 peaks were analyzed at Fz, Cz, and Pz, along with scalp topography. Results showed significantly earlier latencies and reduced N1 amplitudes in the misophonia group across all sites (Fz, Cz, and Pz), indicating heightened cortical activity. Topographical analysis revealed distinct scalp patterns: the misophonia group showed centro-parietal distributions, contrasting with the fronto-central patterns exhibited in controls. These findings suggest altered early-auditory processing and atypical cortical activation in individuals with misophonia, supporting its neurophysiological basis. The reduced N1 amplitude may represent a neurophysiological biomarker, while multichannel ALLR could serve as an objective index for diagnosis and treatment monitoring in future clinical applications.

**ИИ:** ? · выборка неясна · Case-control ALLR study (15 misophonia, 15 controls); unclear how participants were found, possibly by screening an unselected pool.

**Решение:** =

---

### 136 · R0335

**Sensory processing in Autism Spectrum Disorder: Insights into misophonia, and hyperacusis in a pediatric population.**

2025 · International journal of pediatric otorhinolaryngology · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.ijporl.2025.112241

Objective This study aims to investigate the prevalence of misophonia and hyperacusis in children with Autism Spectrum Disorder (ASD), focusing on gender differences and sensory processing challenges. The research further explores how these sensory sensitivities impact daily functioning and how they may differ across genders in a pediatric population. Methods A total of 60 children aged 2-12 years, diagnosed with ASD, intellectual disability, borderline intellectual functioning, or co-occurring ADHD, participated in the study. Parental consent was obtained, and parents completed the Misophonia Impact and Hyperacusis Impact Questionnaires, which assess the presence and severity of sound sensitivities. Data analysis included frequency distributions and Spearman's rank correlation to examine potential associations between age and the severity of sensory symptoms. Results The study found that 45 % of participants exhibited misophonia, and 38 % showed signs of hyperacusis. A slightly higher prevalence of misophonia and hyperacusis was observed in female participants (50 % and 43 %, respectively) compared to males (43 % and 37 %, respectively). No significant correlation was found between the age of participants and the severity of misophonia (r = 0.22, p > 0.05) or hyperacusis (r = 0.19, p > 0.05). Conclusions Misophonia and hyperacusis are prevalent sensory challenges among children with ASD, with a slightly higher occurrence in females. These findings suggest that sensory sensitivities persist across developmental stages and may be more pronounced in females. Early identification and gender-sensitive, sensory-focused interventions are critical for improving the quality of life and daily functioning of children with ASD. Future research should explore the underlying mechanisms of these sensory sensitivities to enhance intervention strategies across diverse populations.

**ИИ:** + · клиническая группа · Children with ASD and related conditions, not recruited for misophonia; misophonia prevalence reported (45%).

**Решение:** =

---

### 137 · R0338

**Identifying Distinct Tourette Disorder Subtypes using Clinical Data.**

2025 · medRxiv : the preprint server for health sciences · journal article, preprint · eng · https://doi.org/10.1101/2025.11.09.25339700

Tourette Disorder (TD), or Tourette Syndrome, is a highly heterogeneous childhood-onset neurodevelopmental disorder with a global prevalence of 0.5%. TD's large phenotypic heterogeneity, variable heritability patterns, and frequent but varied comorbidity with other neurodevelopmental disorders indicate that different TD patients might have different etiologies. In this study, we performed unsupervised clustering of clinical data, such as categorical diagnoses and comorbidities, from 865 subjects with TD from the Tourette International Collaborative Genetics (TIC Genetics) study to detect Tourette Disorder subtypes. We used two different clustering methods, K-Means and Bayesian Hierarchical Clustering to detect phenotypic subtypes. We identified five distinct, clinically relevant subtypes. These subtypes are characterized by both previously described TD comorbidities, such as Obsessive-Compulsive Disorder (OCD) and Attention Deficit/Hyperactivity Disorder (ADHD), as well as other characteristics, such as sex and region. Defining clinically relevant TD subtypes could enable better diagnostics, treatment, and the understanding of TD etiology. In addition, stratified analysis of genetic data based on these phenotypic subtypes may help identify genes contributing to each TD subtype and provide insights into the disease variability.

**ИИ:** ? · другое · Tourette clinical sample (n=865) with comorbidity data; abstract doesn't mention misophonia, but the full text might list it among clinical variables.

**Решение:** -6 не про мизофонию

---

### 138 · R0339

**Evaluation of the psychometric properties of the English MisoQuest and its relationship with audiological and psychological factors.**

2025 · International journal of audiology · article, other literature type, dataset/dataset · eng · https://doi.org/10.1080/14992027.2025.2456015

OBJECTIVE The aim was to establish the validity and reliability of the English version of MisoQuest, a 14-item misophonia questionnaire initially validated in the Polish language. DESIGN Reliability was examined through internal consistency, measurement error, and test-retest reliability. Validity was evaluated with confirmatory factor analysis, convergent, and discriminant validity. Participants completed the English MisoQuest at two-time points and participated in follow-up interviews. STUDY SAMPLE The study included 451 adult participants, with an average age of 36.4 years (SD = 12.8). RESULTS The English MisoQuest showed very good internal consistency (α and ω = 0.93) and high test-retest reliability (ICC = 0.89). While CFA indicated adequate overall model fit, it did not fully support a one-factor structure, as some items shared variance even when controlled for the latent variable. Convergent validity was demonstrated by moderate to strong correlations with established misophonia questionnaires. Weak correlations with non-misophonia measures supported discriminant validity. Unexpectedly, moderate correlations were found with Hyperacusis Impact Questionnaire (r = 0.34; p < 0.01) and Three-dimensional Fatigue Inventory (r = 0.31; p < 0.01). CONCLUSION The study found that the English version of MisoQuest is a reliable and valid tool for measuring misophonia within the English-speaking adult population.

**ИИ:** ? · выборка неясна · English MisoQuest validation in 451 adults; abstract doesn't say if participants were recruited from the general population or for misophonia.

**Решение:** =

---

### 139 · R0340

**Hyperacusis and Misophonia Measures: An Examination of the Psychometric Properties and the Impact on Health**

2025 · University of Surrey · doctoral thesis, other literature type, text/doctoral thesis · und · https://doi.org/10.15126/thesis.901519

to assess these conditions exhibit varying psychometric robustness, and the psychological links explored this relationship between misophonia and fatigue, identifying stress and sleep quality validity. These tools assess patients' confidence in managing symptoms, particularly within the sounds, such as chewing or tapping. Despite their significant impact, some questionnaires used one-factor structure was not fully supported due to shared variance among some items. While it misophonia involves strong emotional, behavioural and physical reactions to specific trigger as partial mediators, highlighting the potential for targeted interventions. The final study population, demonstrating a one-factor structure for the 4C Hyperacusis Management and two- questionnaires also showed strong reliability, along with good convergent and discriminant This thesis addressed these gaps through a systematic review and three empirical studies.

**ИИ:** ? · выборка неясна · Thesis with psychometric studies of misophonia measures and a misophonia–fatigue study; the abstract is garbled and the samples are unclear, possibly general population.

**Решение:** =

---

### 140 · R0344

**Multisensory Temporal Integration of Simple, Neutral, and Trigger Stimuli in Misophonia**

2025 · eScholarship, University of California · https://core.ac.uk/download/670175819.pdf

Misophonia, a condition marked by decreased tolerance to everyday sounds such as chewing or slurping, can cause severe impairment in social and private settings. The present study examined whether the temporal binding window (TBW) differs between individuals with misophonia and controls for simple flash-beep, complex trigger, and complex neutral stimuli. We measured participants’ TBWs using a simultaneity judgment task(SJ) with simple, trigger, and neutral audiovisual stimuli. Our findings showed that the overall width of TBW varied as a function of stimulus complexity in both groups, with trigger stimuli having the widest TBW, followed by neutral stimuli. Our results also showed that the right TBW was significantly narrower for the trigger PAVS stimuli in the misophonia group, suggesting more temporal precision for misophonics when the video preceded the trigger sound. We also report a novel finding that the benefit of PAVS stimuli is maximal when they are synchronized compared to when the trigger precedes the video or vice versa. An unexpected finding was that misophoics were less susceptible to the McGurk illusion. Overall, this study addressed a novel theoretical question regarding the temporal constraint of multisensory processing of simple, neutral, and trigger stimuli in misophonia

**ИИ:** ? · выборка неясна · UC thesis comparing a misophonia group with controls; recruitment not described, and groups may have come from screening a student pool.

**Решение:** =

---

### 141 · R0345

**Attentional distraction and physiological arousal in misophonia**

2025 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint, project · https://doi.org/10.17605/osf.io/9g6fs

Attention (Task 1) We will conduct a study looking into the role of attention in misophonia. Specifically, the study described follows on from existing literature showing differences in attention in misophonia (Frank et al., 2020, Simner et al., 2022, Ghorbani et al., 2023), as well as differences in physiological responses in misophonia (Edelstein et al., 2013, Kumar et al., 2017, Schroder et al., 2019, Siepsiak et al., 2023). In the current study we pull these threads together to test whether there are differences in behavioural or physiological responses to an attentional distraction task between people with misophonia, and controls without misophonia. Specifically, our attention task has sounds (including misophonic trigger sounds) only as a background element (I.e., sounds are not task relevant); sounds do not need to be attended in order to complete the task making it more naturalistic. The task can be considered in terms of two parallel components: a task-relevant visual display (from which we obtain behavioural responses) and task-irrelevant auditory presentation (from which we derive the psychophysiological responses). The experiment implemented in Psychopy (Pierce et al., 2019) will be available on github. The visual component of the task (following Forster et al., 2011) involves presentation of a 3x3 grid containing a mixture of letters and numbers where participants are asked to categorise each character on the screen as a letter or a number by key press (preceded by a fixation cross of 1s). There are minimally N=120 arrays generating at least 1080 *behavioural* responses (accuracy, RT). Overall duration is determined by the auditory presentation component which involves the presentation of 120 x 10s intervals, half of which are silent (N=60) and half of which contain a sound (20 each of misophonic, unpleasant and neutral sounds), and gives a fixed number of 120 *psychophysiological* responses recorded during the task. The onset of the sound is unpredictable but synchronised to the 2nd, 3rd, 4th or 5th (/9) response made to the visual display. Sounds were obtained from Hansen, Leber &amp; Saygin (2021) and pre-categorised via their prior ratings from misophonics and controls. Interoception (Task 2) Finally, we are additionally interested in interoception and alexithymia. Interoception has been implicated in the neuroscience of misophonia (Kumar et al., 2017) previously, but to date only self-reported interoceptive abilities have been measured (Andermane et al., 2023). Here we look at an objective measure of interoception using a heart beat tracking task (following Garfinkel et al., 2016) as well as the trait alexithymia, measured using the Toronto Alexithymia Scale-20 (TAS-20), associated with difficulties identifying and describing feelings, and impaired interoceptive abilities (Shah et al., 2016).

**ИИ:** ? · выборка неясна · Pre-registered misophonia vs control experiment; recruitment unclear, may have screened an unselected pool (Simner-group style).

**Решение:** -7 preregistration without data

---

### 142 · R0349

**Decreased sound tolerance in a Canadian University Context: Associations with autistic traits, social competence, and gender in an undergraduate sample**

2025 · PsyArXiv · preprint · en · https://doi.org/10.31234/osf.io/6vukr_v1

Disorders of decreased sound tolerance such as misophonia and hyperacusis cause significant distress through strong negative emotional and physiological reactions to everyday sounds. These conditions have been associated with poor mental and physical health as they impact day to day life. Prior to the recent development of consensus definitions of misophonia and hyperacusis, attempts to determine the prevalence of these conditions have been hindered by the ambiguity and inconsistency of their descriptions. Despite this, certain populations have been suggested to more frequently experience misophonia and hyperacusis, namely younger people and autistic people. Furthermore, there has been conflicting evidence regarding whether these conditions are more prevalent among women. Post-secondary campuses are often sensory-rich. As such, students with misophonia and hyperacusis are likely to experience distress. For this reason, we sought to investigate the prevalence of misophonia and hyperacusis in a Canadian university sample, and explore the relations between these conditions and gender, autistic traits, and overall social competence. As exposure to many everyday sounds can be highly aversive for individuals with misophonia and/or hyperacusis, these individuals often attempt to avoid environments in which distressing sounds are encountered. It is therefore possible that poorer social competence may be a secondary effect of these conditions. To investigate these relations, 2080 students completed an online survey using multiple established self-report measures of decreased sound tolerance. Clinical misophonia was detected in 12 – 18% of participants, and hyperacusis in 6-17%. Both conditions were significantly more prevalent among women than men. Both conditions were found to be weakly to moderately positively correlated with autistic traits, and weakly to moderately negatively correlated with social competence. These results highlight decreased sound tolerance as a significant issue at Canadian post-secondary institutions, calling for steps to be taken to mitigate its effects.

**ИИ:** + · исследование распространённости · Online survey of 2080 Canadian undergraduates found clinical misophonia in 12–18% of participants using established self-report measures.

**Решение:** =

---

### 143 · R0350

**Decreased sound tolerance in a Canadian University Context: Associations with autistic traits, social competence, and gender in an undergraduate sample.**

2025 · PloS one · article, preprint, journal article · eng · https://doi.org/10.1371/journal.pone.0334689

Disorders of decreased sound tolerance such as misophonia and hyperacusis cause significant distress through strong negative emotional and physiological reactions to everyday sounds. These conditions have been associated with poor mental and physical health as they impact day to day life. Prior to the recent development of consensus definitions of misophonia and hyperacusis, attempts to determine the prevalence of these conditions have been hindered by the ambiguity and inconsistency of their descriptions. Despite this, certain populations have been suggested to more frequently experience misophonia and hyperacusis, namely younger people and autistic people. Furthermore, there has been conflicting evidence regarding whether these conditions are more prevalent among women. Post-secondary campuses are often sensory-rich. As such, students with misophonia and hyperacusis are likely to experience distress. For this reason, we sought to investigate the prevalence of misophonia and hyperacusis in a Canadian university sample, and explore the relations between these conditions and gender, autistic traits, and overall social competence. As exposure to many everyday sounds can be highly aversive for individuals with misophonia and/or hyperacusis, these individuals often attempt to avoid environments in which distressing sounds are encountered. It is therefore possible that poorer social competence may be a secondary effect of these conditions. To investigate these relations, 2080 students completed an online survey using multiple established self-report measures of decreased sound tolerance. Clinical misophonia was detected in 12 – 18% of participants, and hyperacusis in 6-17%. Both conditions were significantly more prevalent among women than men. Both conditions were found to be weakly to moderately positively correlated with autistic traits, and weakly to moderately negatively correlated with social competence. These results highlight decreased sound tolerance as a significant issue at Canadian post-secondary institutions, calling for steps to be taken to mitigate its effects.

**ИИ:** + · исследование распространённости · Survey of 2080 Canadian undergraduates that reports clinical misophonia in 12–18% using established self-report measures.

**Решение:** =

---

### 144 · R0351

**Sound Tolerance Disorders (part II): prevalence and treatment possibilities**

2025 · Zenodo · other literature type, text/technical note · und · https://doi.org/10.5281/zenodo.15098832

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · нет аннотации · No abstract; the title suggests a review of sound tolerance disorders, but original prevalence data can't be ruled out.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 145 · R0354

**Reliability and validity of the Turkish version of the Duke-Vanderbilt Misophonia Screening Questionnaire: a new tool for misophonia assessment**

2025 · Speech Language and Hearing · article, journalarticle, google scholar result · en · https://doi.org/10.1080/2050571x.2025.2581435

Abstract The aim of this study was to conduct a Turkish validity and reliability study of the DVMSQ, which was developed to screen for misophonia and evaluate its symptoms. This study also aimed to determine the variables affecting the prevalence and severity of misophonia. Three hundred individuals aged between 18 and 65 years with clinically normal hearing were included in the study. The participants were asked to complete the Duke-Vanderbilt Misophonia Screening Questionnaire (DVMSQ), which includes 18 screening questions measured on a 5-point Likert scale. Psychometric indicators for the construct validity of the DVMSQ were obtained through confirmatory factor analysis. The Cronbach’s alpha internal consistency coefficient and item-total correlation were examined to assess the reliability of the questionnaire. A total of 144 (48%) of the 300 people included in the study suffered from misophonia. The factor loadings of the Turkish DVMSQ were between 0.46 and 0.87. Confirmatory factor analysis revealed that the Turkish DVMSQ was consistent with the structure of the original questionnaire, consisting of 18 items and two subdimensions. The item total score correlations of the questionnaire varied between 0.46 and 0.77. The Cronbach’s alpha internal consistency coefficient for the 18-item version of the questionnaire was 0.91. The DVMSQ, adapted into Turkish, has a high validity and reliability level and supports the screen of misophonia.

**ИИ:** + · валидация шкалы · Turkish DVMSQ validation in 300 adults with normal hearing; reports 48% with misophonia.

**Решение:** =

---

### 146 · R0356

**Examining Differences in Functional Impairment in Individuals With and Without Misophonia**

2025 · eGrove · text

Misophonia is a disorder of decreased tolerance to certain sounds (Swedo et al., 2022). Studies in adults with misophonia show that individuals experience functional impairment across domains (Jager et al., 2020). However, very few studies have investigated differences in specific areas of functional impairment between individuals with and without misophonia. Therefore, the current study was conducted to understand these differences in order to better understand potential treatment targets. We hypothesized that individual’s with misophonia would report greater functional impairment across domains of daily living than individuals without misophonia. Participants (N = 156; 71.6% female; 69.8% White; Mage = 28.2 years, SD = 11.2) were recruited from the community. Individuals who met screening criteria for the misophonia group (n = 81) or the control group (n = 75) were invited to participate in the study and completed self-report measures of demographics and functional impairment as part of a larger project focused on characterizing features of misophonia. Chi Square and t-test analyses were conducted to investigate differences between groups. The misophonia group demonstrated significantly higher functional impairment across areas of physical mobility, bodily pain, general health, social functioning, and mental health. As expected, results suggest that individuals with misophonia experience higher levels of functional impairment than those in the control group, indicating consideration for multidisciplinary treatments to improve quality of life. Future research should aim to further investigate long-term therapeutic interventions for individuals with misophonia-related functional limitations

**ИИ:** ? · выборка неясна · Community sample was screened into misophonia and control groups; the full text might report how many in the screened pool met criteria.

**Решение:** =

---

### 147 · R0358

**Beyond the Sound: The Role of the Source of Human-Made Trigger Sounds in Misophonia.**

2025 · Noro psikiyatri arsivi · article, journal article, journalarticle · eng · https://doi.org/10.29399/npa.28744

Introduction: Misophonia is a neuropsychiatric disorder characterised by abnormally extreme reactions to certain sensory stimuli. In this paper, we aimed to investigate the effect of the individual producing the human-generated trigger sound on the level of discomfort reported to the trigger sound. Our hypothesis was that when the misophonic sound is presented with the information that it is produced by a relative, it will create more subjective discomfort than the sound presented with the information that is not produced by a relative. Methods: This experimental study was conducted with 15 participants aged 18-65 years living in Antalya who volunteered to participate in the study. Results: In the first comparison, participants reported more subjective discomfort when the voice from the sound bank was presented with the information that it was produced by the relative than when the relative's voice was presented with the information that it was not produced by the relative (p<0.001). In the second comparison, participants reported more subjective discomfort when the voice of the relative was presented with the information that it was produced by the relative than when the voice of the relative was presented with the information that it was not produced by the relative (p=0.001). In the final comparison, there was no significant difference in subjective discomfort between presenting the voice of the voice bank with the information that it was produced by the relative and presenting the voice of the relative with the information that it was produced by the relative (p=0.783). Conclusion: In conclusion, it seems source of the trigger, especially for human-made sounds, is more important than the trigger sound itself.

**ИИ:** ? · выборка неясна · Experiment with 15 volunteers; abstract doesn't say whether they were recruited for misophonia or screened from an unselected pool.

**Решение:** =

---

### 148 · R0361

**Perception of speech-in-noise in misophonia: Intelligibility differences between misophones and non-misophones**

2025 · The Journal of the Acoustical Society of America · article, journalarticle, conference-abstract · en · https://doi.org/10.1121/10.0040609

Misophonia is a condition in which auditory or audiovisual stimuli, called triggers, cause extreme emotional distress [Swedo et al., 2022]. Triggers are often repetitive, oro-facial in nature, and usually are caused by a human being, animal, or object. In this study, we conducted an online speech intelligibility task to measure the listeners’ (misophone and non-misophone) ability to correctly identify linguistic items in noise, which can provide insight into the differences in speech perception between groups. To investigate potential differences in these listener groups, we used 50 sentences from the Harvard Sentences, in three different noise conditions (−2, 0, + 2 dB signal-to-noise ratio). Listeners (23 misophones and 87 non-misophones) were asked to type what they heard, to the best of their ability, and their responses were analyzed for accuracy using a Levenshtein distance metric. The misophone group identified the sentences significantly better than the control group. These findings may be explained by misophones’ reported hypervigilance [Guetta et al., 2024] and the common use of masking noise devices (e.g., white noise machines, box fans, headphones) to mitigate the identification of triggers. Our results highlight a proposed difference in the perception of speech by misophones.

**ИИ:** ? · выборка неясна · Online sample split into 23 misophones and 87 non-misophones; unclear whether an unselected pool was screened or misophones were recruited.

**Решение:** =

---

### 149 · R0364

**Examining Physiological Responses to Misophonic Triggers**

2025 · PsyArXiv · article, preprint · en · https://doi.org/10.31234/osf.io/q6gwm_v1

We collected and analyzed an array of biosignals (face electromyogram, skin electrodermal activity, peripheral temperature, and electrocardiogram) in 60 participants with and without misophonia, a condition characterized by decreased tolerance to innocuous sounds. Our goal was to objectively characterize the physiological response to misophonia triggering sounds. We found that misophonic responses can be objectively identified in some cases through atypical physiological reactions to triggering stimuli, though not all participants exhibited this response. Our analyses suggest a large interindividual variability in response to misophonic triggers and highlights the need for methodological adjustments in future experiments to increase the detectability of misophonic reactions

**ИИ:** ? · выборка неясна · Physiological experiment comparing 60 people with and without misophonia; abstract doesn't say whether groups came from screening an unselected pool.

**Решение:** =

---

### 150 · R0365

**From Chewing to Chirping: The Misophonia Audiovisual Trigger Archive (MATA)**

2025 · bioRxiv · preprint · https://doi.org/10.1101/2025.09.09.675007

Misophonia is an emerging condition in which everyday sounds, such as chewing, sniffing, or tapping, evoke disproportionately intense emotional and physiological responses. Despite growing recognition of its clinical significance, progress in understanding misophonia has been hindered by the limited availability of standardized and ecologically valid stimulus sets. Here, we present a large, open-access archive of 1,300 five-second audiovisual clips spanning 12 empirically validated categories of misophonic triggers. This resource extends beyond orofacial movement-related sounds to include a diverse array of real-world triggers, and its audiovisual format enables systematic investigation of how visual context shapes responses to misophonic sounds. The archive lowers the barrier for laboratories to study misophonia, promotes reproducibility across sites, and offers applications ranging from crowdsourced assessments of population-level sensitivities to machine learning approaches for automated trigger detection. By providing the largest and most diverse audiovisual misophonia stimulus repository to date, this resource is designed to accelerate mechanistic, clinical, and translational research on misophonia and related sensory-emotional phenomena.

**ИИ:** ? · другое · Stimulus archive resource paper; full text might include rating data from a sample measured for misophonia, but no sample is described.

**Решение:** =
