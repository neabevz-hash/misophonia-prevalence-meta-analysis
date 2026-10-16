# Повторный отбор вслепую, часть 1

Записи 1–150 из 790: всё, что ИИ исключил, кроме калибровочной выборки. Повторный отбор вслепую по правилу защиты (протокол, §11b). **Меток и причин ИИ в этом файле нет** — решайте с нуля по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261011).

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

### 1 · R0891

**Loudness recruitment and hyperacusis**

2022 · Elsevier eBooks · book-chapter · en · https://doi.org/10.1016/b978-0-323-91912-8.00003-7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 2 · R0530

**Structural Variants and Implicated Processes Associated with Familial Tourette Syndrome.**

2024 · International journal of molecular sciences · journal article, research-article · eng · https://doi.org/10.3390/ijms25115758

Gilles de la Tourette syndrome (GTS) is a neurodevelopmental psychiatric disorder with complex and elusive etiology with a significant role of genetic factors. The aim of this study was to identify structural variants that could be associated with familial GTS. The study group comprised 17 multiplex families with 80 patients. Structural variants were identified from whole-genome sequencing data and followed by co-segregation and bioinformatic analyses. The localization of these variants was used to select candidate genes and create gene sets, which were subsequently processed in gene ontology and pathway enrichment analysis. Seventy putative pathogenic variants shared among affected individuals within one family but not present in the control group were identified. Only four private or rare deletions were exonic in LDLRAD4 , B2M , USH2A , and ZNF765 genes. Notably, the USH2A gene is involved in cochlear development and sensory perception of sound, a process that was associated previously with familial GTS. In addition, two rare variants and three not present in the control group were co-segregating with the disease in two families, and uncommon insertions in GOLM1 and DISC1 were co-segregating in three families each. Enrichment analysis showed that identified structural variants affected synaptic vesicle endocytosis, cell leading-edge organization, and signaling for neurite outgrowth. The results further support the involvement of the regulation of neurotransmission, neuronal migration, and sound-sensing in GTS.

**Решение:** -6 не про мизофонию

---

### 3 · R0400

**Sound Tolerance Disorders (part I)**

2025 · Zenodo · other literature type, text/technical note · und · https://doi.org/10.5281/zenodo.14974724

This bulletin addresses a topic of great clinical relevance, Sound Tolerance Disorders (STDs). Although there are many questions and several points surrounding STD that still need to be clarified, we nevertheless invite you to join us on a journey into this challenging and perplexing field.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 4 · R0013

**When Sounds Hurt and Voices Aren't Heard: An Experience Report on Misophonia, Sensory Trauma, and Trauma-Informed Design**

2026 · arXiv (Cornell University) · article, preprint, journalarticle · und · https://doi.org/10.48550/arxiv.2605.09796

This experience report reflects on researching misophonia as someone who lives with it. Misophonia is an aversive response to everyday sounds (chewing, sniffling, pen clicking) and, for many of us, to associated visual cues (misokinesia). It is poorly recognized clinically and socially. People with misophonia are routinely disbelieved, and they live inside platform surfaces (auto-playing audio, algorithmic ASMR, normalized eating on camera) that turn the sensory environment itself into recurring distress. This report is a re-reading of a prior qualitative study of 16 semi-structured interviews with misophones, conducted in dialogue with my lived experience and my role in the soQuiet Misophonia Research Network. I extend the trauma-informed design (TID) conversation in two ways. First, TID must treat embodied, contested conditions as sources of both sensory and epistemic harm: ongoing trauma produced by the audiovisual surface and by repeated dismissal of users' accounts of their bodies. Second, the closed groups and moderated subreddits participants relied on can reproduce that dismissal when a few moderators decide whose experiences count. I close with implications for ASSETS.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 5 · R0934

**Diagnosis and Management of Functional Tic-Like Phenomena.**

2022 · Journal of clinical medicine · journal article, review · eng · https://doi.org/10.3390/jcm11216470

Over the past 3 years, a global phenomenon has emerged characterized by the sudden onset and frequently rapid escalation of tics and tic-like movements and phonations. These symptoms have occurred not only in youth known to have tics or Tourette syndrome (TS), but also, and more notably, in youth with no prior history of tics. The Tourette Association of America (TAA) convened an international, multidisciplinary working group to better understand this apparent presentation of functional neurological disorder (FND) and its relationship to TS. Here, we review and summarize the literature relevant to distinguish the two, with recommendations to clinicians for diagnosis and management. Finally, we highlight areas for future emphasis and research.

**Решение:** -6 не про мизофонию

---

### 6 · R0189

**Misophonia among young adults: A narrative review**

2026 · Stephens Journal of Healthcare Research · google scholar result · http://journal.sjhr.in/index.php/SJHR/article/view/15

… recognition of misophonia and its … prevalence, clinical characteristics, neurobiological mechanisms, psychosocial consequences, and treatment approaches related to misophonia …

**Решение:** -1 обзор / комментарий / письмо

---

### 7 · R1441

**The Dilemma of Central Presbycusis**

2014 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0000446438.42386.a8

Figure: © iStock/CreatistaThe brain's ability to process sound into meaningful events is notably altered by aging and, specifically, by hearing loss and cognition. The central degradation caused by peripheral hearing loss, independent of other influences, can result in memory loss, dementia, and Alzheimer's disease.Figure: Dennis A. Colucci, AuD, MAKnown determinants that delay cognitive changes include level of education, physical exercise, intellectual engagement, social networking, friendships, and a healthy diet. Remarkably, most of these factors are related to hearing acuity and auditory skills. Recent investigations have shown that hearing loss is associated with a reduction in whole brain and regional volumes ( Neuroimage 2014;90:84-92http://www.sciencedirect.com/science/article/pii/S1053811914000032). After adjustment for other conditions, including cardiovascular risk, it was estimated that the brain's aging is accelerated by 6.4 years in those with a speech-frequency pure-tone average greater than 25 dB. In terms of functional abilities, a cross-sectional analysis in a separate study demonstrated that hearing loss was associated with equivalent effects on cognitive test scores as seven years of aging (J Gerontol A Biol Sci Med Sci 2011;66[10]:1131-1136http://biomedgerontology.oxfordjournals.org/content/66A/10/1131.abstract). Even more evidence comes from research indicating that patients who perform very poorly (< 50%) on the Synthetic Sentence Identification–Ipsilateral Competing Message or Dichotic Sentence Identification test are at seven to 12 times the risk of developing Alzheimer's disease within the subsequent three to 10 years (Arch Otolaryngol Head Neck Surg 2011;137[4]:390-395http://archotol.jamanetwork.com/article.aspx?articleid=716248#ref-ooa15011-7; J Am Geriatr Soc 2002;50[3]:482–488.http://onlinelibrary.wiley.com/doi/10.1046/j.1532-5415.2002.50114.x/abstract?systemMessage=Wiley+Online+Library+will+be+disrupted+Saturday%2C+15+March+from+10%3A00-12%3A00+GMT+%2806%3A00-08%3A00+EDT%29+for+essential+maintenance) BEYOND DEFAULT PRESCRIPTIONS Without competent hearing care, patients experience declining quality of life from a treatable condition. Furthermore, audiological rehabilitation is not easy. It can't be simplified by a system that places technology as the answer to hearing loss, rather than a tool of a qualified provider and hearing therapist. Clinically, a diagnostic evaluation may include a complete hearing evaluation, loudness tolerance scaling, otoacoustic emissions, auditory brainstem response to complex sounds, immittance, speech-in-noise tests, and a Mini-Mental State Examination or Montreal Cognitive Assessment if cognition is in question. With this knowledge, the audiologist and primary care physician can proceed with amplification and specialist referrals as they start the process of developing and renewing the patient's engagement. To achieve the best outcome and maximize neuroplastic changes, hearing aid fitting must start with hard clinical findings, followed by verification and validation studies to ensure brain-friendly processing and to avoid negative neuroplasticity and misophonia. No longer is choosing a default prescription—a best-fit scenario out of the 1,430 available (AudiologyOnline; Apr. 9, 2012http://www.audiologyonline.com/articles/20q-same-or-different-comparing-769)—and getting the patient's blessing acceptable practice, especially since patients don't know what constitutes maximum benefit until it is provided and scientific measures to guarantee that outcome are made available. A number of questionnaires are available to help assess outcomes. I use the Abbreviated Profile of Hearing Aid Benefit (APHAB). Nevertheless, the most rewarding finding is when the patient tells me that I have changed his or her life forever. Creating maximal engagement requires a variety of hands-on audiological services, with the goals of social normalization and reduction in isolation. These services consist of patient profiling; developing a collaborative relationship; providing varying degrees of directive counseling with music therapy, auditory training, and situational listening skills instruction; and qualifying the benefits of amplification while removing communication stress. While not all patients are willing to use computerized instruction, auditory training can be streamlined if patients are directed to utilize their hearing aids during all waking hours, venture into acceptable social situations, and avoid long periods of quiet time by listening to music or television, or by participating in other engagements. I use activities of daily living as a benchmark for directive counseling in this area. Delaying hearing loss intervention is not only profoundly detrimental to individual quality of life, but also to the ailing healthcare system, as one in three seniors die with Alzheimer's or another dementia at a cost of $203 billion a year in the United States (Alzheimer's Facts and Figures; Alzheimer's Associationhttp://www.alz.org/alzheimers_disease_facts_and_figures.asp). With this knowledge, the new role of audiology becomes obvious as we shift gears toward treatment of central presbycusis.

**Решение:** -1 колонка / обзор (The Hearing Journal)

---

### 8 · R1359

**Fuzzy Logic Based Approach for Automation of Emotion Detection in Misophonia**

2017 · International Journal of Computer Science and Information Technology · article · en · https://doi.org/10.5121/ijcsit.2017.9104

Human being mostly categories into two types, the one who follow distress cycle and other who believe on wellness cycle.Output of distress cycle is decreased productivity, decreased enjoyment and decreased intimacy, whereas output of wellness cycle is increased productivity, increased enjoyment and increased intimacy which is essential for life.Reason of distress could be anything like emotion, disease, environment, family, pain.One of the mostly unexplored areas of cause of distress is misophonia.It is a disorder related to various senses like sound, sight, smell, taste and touch.This disorder is not in DSM-V, underscoring that it is not known by psychiatric and medical communities.We have proposed an automatic fuzzy approach system for identification of intensity of emotions related to various triggers on the basis of age group.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 9 · R0181

**The Architecture of Difference: Theoretical Perspectives on Neurodivergent Cognition**

2026 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-3-032-19636-1_2

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 10 · R1432

**Misophonie et psychiatrie contemporaine [Misophonia and contemporary psychiatry].**

2015 · IRIS · letter · fr

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 редакционная статья / письмо

---

### 11 · R0136

**Assessing and Addressing Clients’ Internal Challenges to Hearing Help**

2026 · Oxford University PressOxford · part of book or chapter of book, book-chapter · en · https://doi.org/10.1093/oso/9780198935223.003.0005

Abstract This chapter explores how clinicians can identify internal challenges experienced by individuals seeking audiological care. Clinicians can use questionnaires to uncover problems influencing client ability to cope with hearing loss, their overall well-being, distress from decreased sound tolerance related to hyperacusis or misophonia, tinnitus, and effects of listening fatigue. How to incorporate questionnaires into routine practice is discussed along with counseling considerations for having conversations with clients about their difficult thoughts and emotions impacting hearing care. We have included conversation examples to illustrate how to approach talking with clients about what they are experiencing. We also provided tips for steps one can take to integrate assessment into their clinical practice.

**Решение:** -1 глава книги / справочник

---

### 12 · R0860

**General Perspective of Autonomous Sensory Meridian Response (ASMR) For Reducing Anxiety and Stress in Integrative Medicine (IM)**

2022 · Institutional Repositories DataBase (IRDB) · article · en · https://tokushima-u.repo.nii.ac.jp/records/2011721

Recently, Autonomous Sensory Meridian Response (ASMR) has been in focus. It is a sense of thrilling feeling with pleasure or joy that appears from the nape of the neck to the head scalp region. ASMR has been often found by the triggers of sound, music and video, which can induce relaxation and smooth sleep with reducing anxiety and stress. It is often caused by the triggers of sound, music and video, and shows possible relationship with anxiety, trait, neuroticism and misophonia. Based on auditory sensation, ASMR may play a main role for Brain–computer interface (BCI) from now on.journal articl

**Решение:** -1 обзор литературы / концептуальная статья

---

### 13 · R0331

**Sluh kao dio senzorne integracije u modernom svijetu**

2025 · Sveučilište u Rijeci. Medicinski fakultet. · master thesis · hrv · https://repository.medri.uniri.hr/islandora/object/medri:9728/datastream/PDF

This master's thesis analyzes hearing as a component of sensory integration, emphasizing the complexity of neurophysiological mechanisms underlying auditory perception of the environment, the development of speech and language abilities, cognitive functions, and social interaction. The structure of the auditory system includes a peripheral component, where sound waves are transmitted and converted into electrical signals, and a central component, which importance is in the transmission and processing of these signals. Functionally, the mechanism of hearing enables recognition, localization, discrimination, and interpretation of sound, with binaural hearing playing a particularly important role. Through this process, the brain uses input from both ears to determine the direction and distance of a sound source, especially in noisy environments. Due to increased exposure to auditory stimuli in modern environments, risk of the acoustic trauma has risen, which can leave permanent consequences on an auditory function. In addition to permanent damage, auditory hyperreactivity is becoming increasingly common. That is a condition that may include subjective tinnitus, hyperacusis, loudness recruitment, phonophobia, and misophonia. Any alteration in the central nervous system's ability to transmit acoustic signals from the vestibulocochlear nerve to the auditory cortex is considered an auditory processing disorder. In the context of this kind of disorder, but also in other conditions involving dysfunction of the auditory system, the significance of neuroplasticity is particularly emphasized. This inherent capacity of the brain supports various individualized rehabilitation approaches. Timely intervention can significantly improve functional outcomes, especially when therapy is provided during developmental periods of heightened neuroplastic sensitivity. Ovaj diplomski rad analizira sluh kao dio senzorne integracije, ističući složenost neurofizioloških mehanizama koji stoje iza slušne percepcije okoline, razvoja jezično-govornih sposobnosti, kognitivnih funkcija i socijalne interakcije. Struktura auditornoga sustava obuhvaća perifernu komponentu u kojoj dolazi do prijenosa zvučnih valova i njihove pretvorbe u električne signale, te centralnu komponentu koja sudjeluje u prijenosu i obradi signala nakon što napuste unutarnje uho. Funkcionalno, mehanizam slušanja omogućuje prepoznavanje, lokalizaciju, diskriminaciju i interpretaciju zvuka, a osobito je važno svojstvo binauralnoga sluha pomoću kojega mozak koristi informacije iz oba uha za određivanje smjera i udaljenosti izvora zvuka, osobito u bučnim uvjetima. Uslijed intenzivnije izloženosti zvučnim podražajima u suvremenome okruženju, povećava se rizik od pojave akustične traume koja može ostaviti trajne posljedice na funkcionalnost sluha. Osim trajnih oštećenja, sve je češća i auditivna hiperreaktivnost - stanje koje može uključivati subjektivni tinitus, hiperakuziju, rekrutman, fonofobiju i mizofoniju. Bilo kakva promjena u sposobnosti središnjega živčanoga sustava za provođenje akustičkoga signala od vestibulokohlearnoga živca do slušnoga korteksa, smatra se poremećajem slušne obrade. U kontekstu toga poremećaja, ali i drugih stanja koja uključuju disfunkciju auditornoga sustava, naglašava se značaj neuroplastičnosti. Upravo se kroz tu sposobnost provode različiti individualni rehabilitacijski pristupi. Pravovremena intervencija može značajno poboljšati funkcionalne ishode, osobito ako se terapija provodi u razvojnim razdobljima visoke neuroplastične osjetljivosti.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 14 · R1027

**The development and validation of the Misophonia response scale.**

2021 · Journal of psychosomatic research · article, other literature type, journal article · eng · https://doi.org/10.1016/j.jpsychores.2021.110587

OBJECTIVE Most current Misophonia scales are not validated, do not include both emotional and physiological responses to triggers, and/or focus only on auditory triggers. This research aimed to develop and validate a measure of the magnitude of the Misophonic response that addressed these omissions. METHOD Three studies were carried out with individuals with self-diagnosed Misophonia. In study 1, expert opinion and participants commented on initial items to determine both face and content validity. In study 2, scale structure, reliability, and convergent and discriminant validity were determined using correlations, principal component analysis (PCA), and reliability analysis. In study 3, factor structure was confirmed in another sample of participants using confirmatory factor analysis (CFA). RESULTS The final 22-item scale assesses the magnitude of responses to triggers across any sensory modality. There are three subscales (emotional, physiological, and participation in life), with three additional items measuring frequency of triggers, avoidance of triggers, and time taken to recover from the triggers. The final scale showed suitable discriminant and convergent validity, with good internal consistency (Cronbach's alphas range 0.77 to 0.89). The three-component solution extracted using PCA explained 53.97% of variance, with all items loading between 0.45 and 0.84. The structure was confirmed with CFA (χ2 = 269.01, p < .001; CFI = 0.96; TLI = 0.96 and RMSEA = 0.045 (CI 0.037-0.053). CONCLUSION The Misophonia Response Scale, which is valid and reliable, will facilitate understanding of Misophonia as it is short and easy to use for self-report in research.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 15 · R1356

**Abnormal Brain Networks Underlie Misophonia**

2017 · Neurology Today · article · en · https://doi.org/10.1097/01.nt.0000515060.86346.28

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 обзор литературы / концептуальная статья

---

### 16 · R1484

**P3 Selective sound sensitivity syndrome (misophonia) and Tourette syndrome**

2012 · Journal of Neurology Neurosurgery & Psychiatry · article, conference object, google scholar result · en · https://doi.org/10.1136/jnnp-2012-303538.20

Objective We present the case of a 52-year-old man first diagnosed with Tourette syndrome (TS) at the age of 44 following referral to our specialist TS clinic for chronic tic symptoms. Method On neuropsychiatric examination, he presented with multiple motor tics (including facial grimacing and shoulder shrugging) and phonic tics (mainly yelping and barking) which were present since the age of 11. All tics were characteristically preceded by premonitory urges and he was able to voluntarily suppress them at the expense of mounting inner tension. Co-morbid psychiatric disorders included mild obsessive-compulsive behaviours (counting, lining up newspapers), previous episodes of depression and sleep problems as a child (somnambulism). Results This patient reported being mainly distressed by what he described as functionally impairing behaviours in response to particular sounds. As a child, 1 year before developing his tics, he began experiencing annoyance at the sound of his father chewing food. Throughout his life he was affected by a range of sounds made by either familiar people or strangers with “no distinction”. He would often challenge other people who might accidentally be producing such “trigger sounds”, resulting in either risk taking or avoidance behaviours. These symptoms currently affect his health-related quality of life in different ways: for example, he struggles to take buses without distress and avoids them if possible because of the sounds encountered; he experiences violent thoughts towards people, to “slap or kick them, on the spur of the moment”, although there is no forensic history or subjective desire to act on these impulses. Although these episodes are self-limiting on stimulus removal, functional impairment is significant given the wide range of low level, innocuous stimuli which are present in the environment. Conclusion Selective sound sensitivity syndrome (SSSS, or misophonia, from the Greek “miso”, hatred, and “phonia”, sound) is described as a “hate of sound”, possibly associated with abnormal activity within the limbic system and its functional connections with the primary auditory cortex and the autonomic nervous system. Misophonia is a relatively rare condition, which can be distinguished from hyperacusis by its sensitivity to the subjective response elicited. This is the first documented case of misophonia reported by a patient with a diagnosis of TS. The phenomenological similarity between misophonia and other subjective symptoms commonly reported by patients with TS (especially premonitory urges, obsessive-compulsive symptoms, not-just-right experiences) suggests a possible pathophysiological association.

**Решение:** -2 клинический случай / серия случаев

---

### 17 · R1232

**Misophonia, Maladaptive Schemas and Personality Disorders: A Report of Three Cases**

2019 · Journal of Contemporary Psychotherapy · article · en · https://doi.org/10.1007/s10879-019-09438-3

Misophonia is a chronic condition in which specific sounds cause intense negative emotions and autonomic arousal. Misophonia is considered a psychological disorder without any relationship with specific alterations of hearing receptors and independent from physical characteristics of the sound. Moreover if misophonia can be defined as a specific psychiatric disorder or a correlate of other conditions is still under debate. The patients were two women and one man. In this case series we first identified the presence of triggers sounds inducing misophonia as reported during the psychotherapy sessions. At a qualitative level all the three patients perceived that the others were intentionally acting with the purpose of underline their maladaptive interpersonal schemas. All the patients were evaluated with the use of questionnaires. Regarding personality disorders (PD) all three patients suffered from at least one PD. As regard depression, one had moderate depression and one had severe depression. Two patients had moderate/severe anxiety. All the three patients can be considered as highly problematic in the interpersonal domain. Our findings have clinical implications for the treatment of misophonia because it seems to be sustained by underlying PD or maladaptive interpersonal schemas. The qualitative analysis of these cases has highlighted how patients with misophonia tended to ascribe intentionality to the people who emit the sounds that trigger their negative emotional reactions. Further studies are necessary to evaluate which kind of interpersonal patterns occur in these patients.

**Решение:** -2 клинический случай / серия случаев

---

### 18 · R0266

**Caractérisation et mécanismes sous-tendant la perception normale de l’intensité des sons et de l’hypersensibilité auditive**

2025 · Université de Montréal · dissertation/thèse ou mémoire / thesis or dissertation, thesis · fr · https://doi.org/10.71781/31001

Objectif : L’objectif général de cette thèse est d’explorer les mécanismes sous-jacents à la perception normale de l’intensité sonore et à l’hypersensibilité auditive, tout en clarifiant les distinctions entre l’hyperacousie et la sensibilité au bruit. La thèse repose sur quatre études distinctes, chacune ayant des objectifs et des méthodologies spécifiques. Méthodologie : L’étude 1 visait à réaliser une revue de portée des recherches sur les potentiels évoqués auditifs afin de mieux comprendre les mécanismes de l’hyperacousie et d’explorer des pistes pour une mesure objective de cette condition. L’étude 2 avait pour but d’examiner la distribution et les corrélations entre les scores du Hyperacusis Questionnaire (HQ) et de la Noise Sensitivity Scale (NSS) dans des populations clinique et non clinique afin de fournir des données normatives et d'explorer les distinctions entre hyperacousie et sensibilité au bruit; et de comparer les scores des participants avec et sans tolérance réduite au son aux deux questionnaires. L’étude 3 avait pour objectif de vérifier s'il était possible de dissocier la sonie en deux dimensions distinctes : sensorielle et affective, en utilisant deux échelles spécifiques pour examiner leur corrélation et leur dissociation, tout en examinant les facteurs prédictifs de ces perceptions. Enfin, l’étude 4 visait à documenter l’efficacité de la thérapie sonore dans le traitement de l’hyperacousie persistante après un traumatisme craniocérébral léger (TCCL). Résultats : L’étude 1 a recensé 35 articles publiés entre 2002 et 2021 sur l’utilisation des potentiels évoqués auditifs pour évaluer l’hyperacousie. Ces études ont été classées en quatre catégories d’étiologies : troubles neurodéveloppementaux, troubles neurologiques, dommages auditifs induits et hyperacousie idiopathique. La majorité des travaux a exploré des paradigmes de filtrage sensoriel, d’habituation et de détection de déviants, suggérant que des déficits attentionnels pourraient être impliqués dans certains types d’hyperacousie. L’étude 2 a comparé les scores des questionnaires HQ et NSS complétés auprès de 103 jeunes adultes sains et 95 anciens combattants, observant une corrélation modérée à forte entre les deux échelles (r = 0,58 à 0,74), confirmant leur chevauchement conceptuel. L’étude 3, a exploré les dimensions sensorielle et affective de la sonie chez 102 jeunes adultes sains. Les résultats ont montré que ces dimensions peuvent être dissociées, bien qu’elles soient corrélées à haute intensité sonore. Des scores plus élevés au NSS ont prédit des perceptions plus intenses et déplaisantes, tandis que les scores plus élevés de dépression ont prédit des perceptions plus faibles et moins plaisantes. Enfin, l’étude 4 a documenté l’efficacité de la thérapie sonore chez huit participants souffrant d’hyperacousie persistante après un TCCL, avec des améliorations notées chez au moins cinq participants sur plusieurs mesures d’issues cliniques. Discussion : Les résultats des quatre études combinées ont permis de mieux comprendre la distinction entre l’hyperacousie et la sensibilité au bruit. Ils ont révélé que l’hyperacousie peut se manifester sous diverses formes cliniques, influencées par des facteurs sensoriels, affectifs et cognitifs. La thérapie sonore semble être un traitement prometteur pour améliorer la tolérance au son dans le cadre du TCCL, bien que des études supplémentaires soient nécessaires pour mieux comprendre ses mécanismes et optimiser ses paramètres. Objective: The overall objective of this thesis is to explore the underlying mechanisms of normal loudness perception and auditory hypersensitivity, while clarifying the distinctions between hyperacusis and noise sensitivity. The thesis is based on four distinct studies, each with specific objectives and methodologies. Methods: Study 1 aimed to conduct a scoping review of research on auditory evoked potentials to better understand the mechanisms of hyperacusis and explore potential avenues for an objective measure of this condition. Study 2 aimed to examine the distribution and correlations between Hyperacusis Questionnaire (HQ) and Noise Sensitivity Scale (NSS) scores in clinical and non-clinical populations in order to provide normative data and to explore the distinctions between hyperacusis and noise sensitivity; and to compare the scores of participants with and without decreased sound tolerance on the two questionnaires. Study 3 aimed to determine whether it is possible to dissociate loudness into two distinct dimensions: sensory and affective, using two specific scales to examine their correlation and dissociation, while examining predictive factors for these perceptions. Finally, Study 4 aimed to document the effectiveness of sound therapy in treating persistent hyperacusis after mild traumatic brain injury (mTBI). Results: Study 1 reviewed 35 articles published between 2002 and 2021 on the use of auditory evoked potentials to assess hyperacusis. These studies

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 19 · R1551

**Acceptance and Commitment Therapy Versus Progressive Acceptance and Commitment Therapy Versus Progressive Relaxation Training for Misophonia: Randomized Controlled Trial Relaxation Training for Misophonia: Randomized Controlled Trial Protocol, Interventions, and Audiological Assessments Protocol, In**



_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 protocol / preregistration without data

---

### 20 · R0994

**Primary Outcomes for Adults Receiving the Unified Protocol after Hurricane Harvey in an Integrated Healthcare Setting.**

2022 · Community mental health journal · journal article, research support, n.i.h., extramural, research support, non-u.s. gov't · eng · https://doi.org/10.1007/s10597-022-00967-1

The Unified Protocol for Transdiagnostic Treatment of Emotional Disorders (UP) has demonstrated efficacy for treating anxiety and depression. However, there are limited effectiveness data when conducted in real-world settings with diverse populations, including those with trauma. We evaluated treatment outcomes in a naturalistic, community setting among 279 adults who received UP following Hurricane Harvey. We examined change in overall clinical severity, depression and anxiety symptoms, functional impairment, and baseline outcome predictors (i.e., demographic characteristics, impact from Hurricane Harvey, co-occurrence of depression and anxiety symptoms). Global clinical severity, depression and anxiety symptoms, and functional impairment decreased by end-of-treatment. Participants experienced global symptom improvement to a lesser degree than demonstrated in efficacy trials. Participants who experienced greater storm impact reported larger reductions in anxiety symptoms than those less impacted by Harvey. Further studies evaluating the effectiveness of the UP post-disaster and with diverse samples are needed.

**Решение:** -6 не про мизофонию

---

### 21 · R1567

**The effectiveness of cathodal (tDCS) in right insulla region and cognitive-behavioral thrapy in misophonia disorder**



_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -3 выборка набрана из-за мизофонии

---

### 22 · R0362

**Misofonia: ter fortes reações negativas a determinados sons está ligado à inflexibilidade mental**

2025 · The Conversation · article, other · und · https://doi.org/10.64628/ade.7cp9t3u3y

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 научно-популярная статья (The Conversation)

---

### 23 · R0793

**Treatment of Misophonia**

2023 · Advances in Psychiatry and Behavioral Health · article, journalarticle, review · en · https://doi.org/10.1016/j.ypsc.2023.03.009

However, this literal translation is misleading, as the condition is neither uniquely associated with the affective experience of hate or dislike, nor are auditory cues the only stimuli that can function as triggers. The first pilot studies directly examining misophonia were published only 9 years ago [5,10]. Since then, over 60 published empirical studies have investigated misophonia, with roughly 25% of these published over the last year in the first special section in a peer-reviewed scientific journal dedicated to misophonia ( Frontiers in Neuroscience ). Recent reviews suggest that misophonia may be associated with awide varietyofmentalhealth problems [1 – 3]. The majority of studies have used self-report

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 24 · R1168

**Subjektif Tinnituslu Bireylerin Çok Yönlü Değerlendirilerek Yönetim Protokolünün Hazırlanması**

2020 · Sağlık Bilimleri Enstitüsü

The aim of this study was to form a "tinnitus management protocol" according to the tinnitus levels by evaluating the subjects with subjective tinnitus by evaluating the multifactorial approach principle based on emotion, cognition, quality of life, sleep and decreased sound tolerance criteria. 145 subjects aged between 18-64 (45 ± 11, 78 M, 67 F) were included in the study. Tinnitus Assessment Form, Short Form-36, Beck Depression Inventory (BDI), STAI-D, STAI-S, Montreal Cognitive Assessment Scale (MoCA), Tinnitus Handicap Inventory (THI), Hearing Handicap Inventory (HHI), Pitsburgh Sleep Quality Index (PSQI) and Khalfa Hyperacusis Questionnaire were applied after audiological evaluation. In the evaluation of tinnitus, psychoacoustic measurements (loudness, picth matching, minimal masking level and residual inhibition) were performed. As a result of statistical analysis, PSQI, STAI-S and STAI-D scores were higher than normal limit values independent of tinnitus level. When the relationship between severity of tinnitus and BDI was examined, it was found that there was an increase in depression scores at severe / catastrophic levels. As the severity of tinnitus increased, the quality of life subscales decreased. As a result of the comparison of the tinnitus levels and PSQI sub-dimensions, it was determined that severe / catastrophic levels had worse scores in sleep disturbances, general sleep quality and sleep latency than the other three level (Kruskal-Wallis p <0.05). When the scores of 75 individuals with hearing loss and tinnitus complaints were compared, there was a moderate significant correlation between the HHI and THI scores (r=0.598, p=0.00). A significant relationship was found between asymmetric high frequency hearing loss and localization of tinnitus. This study demonstrated the presence of level-related factors for subjective tinnitus assessment. As a result, according to the severity (level) of tinnitus; three different protocols were prepared: very mild / mild, moderate and severe / catastrophic.Bu çalışmanın amaçı; Subjektif tinnituslu bireylerin çok faktörlü yaklaşım prensibi ile değerlendirilerek duygudurum, biliş, yaşam kalitesi, uyku ve azalmış ses toleransı kriter alınarak tinnitus düzeylerine göre "tinnitus yönetim protokolu" oluşturmaktı. Çalışmaya yaşları 18-64 (45±11, 78 E, 67 K) arasında değişen 145 birey dahil edildi. Odyolojik değerlendirmeler ile birlikte Tinnitus Değerlendirme Formu, Short Form-36, Beck Depresyon Envanteri (BDE), STAI-D, STAI-S, Montreal Bilişsel Değerlendirme Ölçeği (MoCA), Tinnitus Engel Ölçeği (TEÖ), İşitme Engel Ölçeği (İEÖ), Pitsburgh Uyku Kalite İndeksi (PUKİ), Khalfa Hiperakuzi Ölçeği (KHÖ) uygulandı. Tinnitus değerlendirmesinde, psikoakustik ölçümler (loudness, picth eşleştirme, minimal maskeleme seviyesi ve rezidüel inhibisyon) yapıldı. İstatistiksel analiz sonucunda PUKİ, STAI-S ve STAI-D ölçek puanlarının tinnitus düzeyinden bağımsız normal sınır değerlerinin üzerinde olduğu belirlendi. Tinnitus şiddeti ile BDE arasındaki ilişki incelendiğinde şiddetli/çok şiddetli düzeylerde depresyon puanlarında artış olduğu belirlendi. Tinnitus şiddeti artıkça yaşam kalitesi alt alanlarının hepsinde düşüş elde edildi. Tinnitus şiddeti ve PUKİ alt boyutların karşılaştırması sonucunda uyku düzensizliği, genel uyku kalitesi ve uyku gecikmesinde şiddetli/çok şiddetli grupların diğer üç gruptan daha kötü puanlar aldığı bu farkın anlamlı olduğu belirlendi (Kruskal-Wallis p <0,05). İşitme kaybı ve tinnitus yakınması olan 75 bireyin İEÖ ve TEÖ puanları karşılaştırıldığında orta düzeyde anlamlı korelasyon elde edildi (r=0.598, p= 0.00). Asimetrik yüksek frekans işitme kaybı ile tinnitus lokalizasyonu arasında anlamlı ilişki bulundu. Bu çalışmada subjektif tinnitus değerlendirmesi için düzey ile ilişkili etkenlerin varlığı gösterildi. Sonuç olarak tinnitus şiddetine göre; çok hafif/hafif, orta ve şiddetli/çok şiddetli olmak üzere üç farklı protokol oluşturuldu

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 25 · R0201

**Liebe Leserinnen, liebe Leser,**

2026 · Zeitschrift für Phytotherapie · editorial · de · https://doi.org/10.1055/a-2763-4728

die heiße Welle der gegenwärtigen Bemühungen um Kostenkontrolle im Gesundheitswesen scheint vor dem Hochsommer termingerecht abgeebbt. Die sog. Komplementärmedizin wird vermutlich mit dem Ausschluss von Homöopathie und Anthroposophischer Medizin aus derzeit ausschließlich Satzungsleistungen einen Minibeitrag in Höhe von etwa einem Promille des notwendigen Sparvolumens leisten – die genauen Zahlen schien auch die Sachverständigenkommission nicht zu kennen. Erstaunlicherweise wurde die Gruppe der „Besonderen Therapierichtungen“ (der Begriff Komplementärmedizin taucht auch in neuesten Versionen des Arzneimittelgesetzes nicht auf) in toto nur in ganz wenigen randständigen Aussagen entsprechend zum Untergang verurteilt, denen mangelndes Verständnis für das Konstrukt und seine Historie anzumerken war. Es stellt sich aber die Frage an die verantwortlichen Vertreter in Phytotherapie, Aufsichtsbehörden und Gesetzgeber, ob diese Gruppierung nach knapp 40 Jahren noch zeitgemäß ist. Ich meine nein. Die Phytotherapie hat sich in der Zeit doch recht geändert und wird dies weiter tun. „Besonders“ ist sie insofern geblieben, als der Weg vom traditionellen Heilmittel bis zum nach heutigen Ansprüchen präklinisch wie klinisch gut beschriebenen und verstandenen Arzneimittel sehr anspruchsvoll bleibt. Die Forschung zu Wirksamkeiten ist qualitativ und quantitativ mit der vor 40 Jahren überhaupt nicht mehr vergleichbar. Sie wird künftig wesentlich durch Versorgungsforschung ergänzt. Damit sind wir mitten in diesem Heft, das diese zum ersten Mal als Schwerpunkt hat. Die reale Situation kann mehr als in konventioneller Pharmakotherapie von der sog. internen Validität abweichen (s.a. Beitrag Piontek S. 103). Diese wird üblicherweise aus RCT, systematischen Reviews und Metaanalysen konstruiert und kann dann in Empfehlungen aus Leitlinien münden. Darum bemühen sich viele Akteure in der Phytotherapie redlich – in letzter Zeit auch zunehmend mit Erfolg. In der realen Welt zählen aber insbesondere bei freiverkäuflichen Medikamenten weitere Faktoren – hier etwa das innere Bild des Patienten von der Tauglichkeit der Phytotherapie bzw. spezieller Pflanzen für seine Probleme, möglicherweise beeinflusst durch die nicht unerhebliche Werbung auf der einen sowie mangelnde Kostenerstattung, mangelnde Compliance bei nicht rasch oder spürbar einsetzender Wirkung und/oder ungenügende bis adverse Kommunikation mit behandelnden Ärzten auf der anderen Seite. Patienten- und Arztpräferenzen spielen bei der Frage, ob eine Phytotherapie in einer bestimmten Situation zum Zuge kommt, eine völlig andere Rolle als bei chemisch definierten Pharmaka. Das sind für sich betrachtet alles weiche Faktoren, die man nicht einmal in hochwertigen Umfragen sicher eruieren kann. Die Resultante aus allen ist aber mit Methoden der Versorgungsforschung bedingt messbar: etwa der Umfang der Nutzung einer Pflanze bei einer bestimmten Indikation, die Dauer der Nutzung, subjektive Beurteilungen von Verträglichkeit wie Wirksamkeit, Ausmaß der Ko-Medikationen für diese Erkrankung, Inzidenz typischer Komplikationen usw. Erste Ergebnisse stellen wir Ihnen vor (z.B. Beitrag Kostev S. 112). Bedenken Sie bitte bei Ihrer sich möglicherweise einstellenden Kritik, dass diese Art von Auswertungen für die klinische Bedeutung der Phytotherapie in breiter Anwendung sehr neu ist: Die erste Veröffentlichung, die primäre Phyto-Verordnungen – hier bei Atemwegsinfekten – und ihre möglichen Folgen in Form von Antibiotika-Verordnungen untersuchte, Verordnungsdaten aus einem breiten Spektrum von Praxen nutzte, datiert für mich aus 2020. Mit diesem Instrument ließ sich über einen längeren Zeitraum die enorm große Zahl von ca. 120 000 Patienten mit ihren Matches ohne Phytos vergleichen. Die Liste der Fragestellungen ist umfangreicher als derzeit an RCT gestellte, etwa bezüglich Alters- oder besonderer Risikogruppen. Es ergeben sich neue Bündnispartner wie insbesondere die Allgemeinmedizin (Beitrag Jobst S. 120). „Forschung kompakt und kritisch“ beschäftigt sich dagegen wie gewohnt noch mit „konventioneller“ Forschung – einem RCT zu Lavendeltee bei Misophonie (Beitrag Uehleke S. 127). Viel Spaß beim Lesen und wie immer der Wunsch nach Kritik und Anregungen! Ihr Rainer Stange Publication History Article published online: 02 July 2026 © 2026. Thieme. All rights reserved. Georg Thieme Verlag KG Oswald-Hesse-Straße 50, 70469 Stuttgart, Germany

**Решение:** -1 редакционная статья / письмо

---

### 26 · R0493

**REVISITING TINNITUS AUDIOLOGICAL REHABILITATION**

2024 · SciELO Preprints · article, preprint · en · https://doi.org/10.1590/scielopreprints.8142

Current research shows tinnitus as more than an auditory phenomenon, but an emotional and cognitive dimension experience. Besides issues involving tinnitus perception and reaction, there is a third dimension: cognition. Both audiological assessment and rehabilitation need to follow these principles and be more comprehensive. The use of sounds to treat tinnitus is described in several papers and has different purposes. It includes hearing aid fitting if hearing loss is detected and the use of sound generator devices. But there are some cases in that hearing loss rehabilitation is not enough and cases of tinnitus and/or sound intolerance suffering without detectable hearing loss in conventional measures. There is no exclusive way for tinnitus patients’ auditory rehabilitation. Based on theoretical proposals and literature, we suggest possibilities of intervention to be even more explored and personally adapted for tinnitus patients: cognitive auditory training and the use of mindfulness-based exercises, sound stimulation during sleep, and restoring the pleasure of listening.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 27 · R1392

**Misophonia**

2016 · Critical Quarterly · article · en · https://doi.org/10.1111/criq.12304

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (Critical Quarterly)

---

### 28 · R1473

**AWARENESS OF HYPERACUSIS MANAGEMENT AMONG HEARING HEALTH CARE PROFESSIONALS - A NATIONWIDE TELEPHONIC SURVEY**

2013 · DergiPark (Istanbul University) · article, review · en · https://dergipark.org.tr/tr/pub/ejm/issue/5368/72686

Decreased sound tolerance prevents people from entering louder environments, working and interacting socially. Hyperacusis is defined as an abnormally strong reaction to sound occurring within the auditory pathways. Among patients with a primary complaint of tinnitus the prevalence of hyperacusis is about 40% (Jastreboff, &amp;amp; Jastreboff, 2000). In patients with a primary complaint of hyperacusis the prevalence of tinnitus has been reported as 86%.In various clinics, tinnitus management often has a confusing impact on quality of life of patients who have hyperacusis but the term and concept may not be accepted as the assessment and management interest. It is found that 56.6% of the respondents report that hyperacusis is not diagnosed in their clinics, 73.4 % do not know the etiology, 33.3% manage hyperacusis and tinnitus simultaneously while others are not sure which should be managed. Decreased sound tolerance, including hyperacusis, misophonia, and phonophobia, is a challenging topic to study and treat. The etiology is not clear, neural mechanisms are speculative and treatments are not yet proven. The general recognition of decreased sound tolerance, as a problem requiring attention and proper treatment, should be considered a priority in the community of hearing professionals. Key words- Hyperacusis, Awareness, Survey.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус)

---

### 29 · R0030

**Noninvasive brain stimulation combined with evidence-based psychotherapy for psychiatric disorders: A meta-analysis of optimal implementation parameters.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint · eng · https://doi.org/10.64898/2026.02.19.26346650

Evidence-based psychotherapies are first-line treatments for psychiatric disorders, yet response rates remain suboptimal. Noninvasive brain stimulation (NIBS) may augment psychotherapy by modulating treatment-engaged circuits. We conducted a systematic review and meta-analysis of randomized controlled trials comparing active NIBS plus evidence-based psychotherapy versus sham NIBS plus psychotherapy. Following Cochrane methods, we searched six databases through February 2025, screening 1,017 records. Twenty-eight trials (31 treatment arms; 1,506 participants) met inclusion criteria. Active NIBS combined with psychotherapy produced significantly greater symptom improvement than sham NIBS with psychotherapy (standardized mean difference = -0.38, 95% confidence interval [-0.68, -0.08]), with substantial heterogeneity. Moderator analyses revealed critical implementation parameters: repetitive transcranial magnetic stimulation (rTMS) showed significant benefit while transcranial direct current stimulation did not. Non-concurrent delivery-stimulation before or after psychotherapy sessions-was significantly effective, whereas concurrent administration was not. Among psychotherapy modalities, cognitive behavioral therapy combined with NIBS produced significant benefit. Human-delivered psychotherapy, but not computerized formats, significantly enhanced outcomes. By diagnosis, significant effects were observed only for anxiety disorders. Secondary analyses revealed significant anxiety symptom reduction specific to rTMS. Treatment integrity was under-reported: only 39.3% of studies used fully manualized protocols and 10.7% documented therapist adherence. Non-concurrent rTMS paired with human-delivered, manualized cognitive behavioral therapy emerges as the most effective strategy, particularly for anxiety disorders. These findings provide an evidence-based framework for optimizing combined treatment protocols and highlight the need for standardized psychotherapy fidelity monitoring in future trials.

**Решение:** -6 не про мизофонию

---

### 30 · R0232

**Physiological Responses to Auditory, Visual, and Auditory Imagery Triggers in Misophonia.**

2026 · Psychophysiology · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1111/psyp.70390

Misophonia is characterized by decreased tolerance to specific trigger sounds, yet the underlying physiological mechanisms remain poorly understood. Misophonic responses are also often reported to be elicited not only by the auditory triggers themselves, but also by visual cues associated with those sounds. However, direct empirical evidence for visual cues associated with auditory triggers remains limited. Moreover, it is not known if misophonic responses can be elicited in the absence of any sensory input, such as during auditory mental imagery. The present study systematically examined physiological responses to misophonic trigger stimuli across auditory and visual sensory modalities, as well as auditory imagery, using multi-channel psychophysiological measures and both trial-wise and time-resolved approaches. Individuals with misophonia and matched control participants were exposed to trigger, generally aversive, and non-aversive stimuli presented in auditory, visual (silent video), and auditory imagery conditions. Physiological responses were recorded across five channels, including electromyographic activity over corrugator supercilii (EMGc) and zygomaticus major (EMGz) muscles, electrodermal activity (EDA), heart rate (HR), and fingertip skin temperature. Compared with generally aversive stimuli, auditory trigger sounds elicited significantly greater physiological responses in individuals with misophonia than in control participants, characterized by increased EMGc, EMGz, EDA, and HR, indicating heightened affective and autonomic engagement beyond general aversiveness. Silent visual trigger cues also evoked greater trigger-specific physiological responses, although these effects were observed in fewer physiological channels (primarily EMGc and HR). Auditory mental imagery produced weaker group-level physiological effects, with significant differentiation limited to EDA. Across all three modalities, greater trial-wise subjective distress was consistently associated with greater EMGc, EMGz, and EDA responses, as well as greater HR responses in the auditory and visual modalities, indicating a close correspondence between physiological activation and the subjective experience of misophonic distress. In contrast, physiological overactivation was not significantly associated with overall misophonia severity or auditory imagery ability. Together, these findings provide the most comprehensive characterization to date of peripheral physiological responses in misophonia across auditory and visual perception, as well as auditory imagery. They demonstrate that misophonia is characterized by exaggerated affective and autonomic physiological responses to trigger sounds, extend this response profile to silent visual cues associated with trigger sounds, and provide initial evidence that auditory mental imagery can engage selected components of the misophonic response.

**Решение:** ? эксперимент (мизофония vs контроль), проверить скрининг пула

---

### 31 · R1515

**Tinnitus retraining therapy: a different view on tinnitus.**

2006 · ORL; journal for oto-rhino-laryngology and its related specialties · article, journal article, review · eng · https://doi.org/10.1159/000090487

Tinnitus retraining therapy (TRT) is a method for treating tinnitus and decreased sound tolerance, based on the neurophysiological model of tinnitus. This model postulates involvement of the limbic and autonomic nervous systems in all cases of clinically significant tinnitus and points out the importance of both conscious and subconscious connections, which are governed by principles of conditioned reflexes. The treatments for tinnitus and misophonia are based on the concept of extinction of these reflexes, labeled as habituation. TRT aims at inducing changes in the mechanisms responsible for &lt;i&gt;transferring &lt;/i&gt;signal (i.e., tinnitus, or external sound in the case of misophonia) from the auditory system to the limbic and autonomic nervous systems, and through this, remove signal-induced reactions without attempting to directly attenuate the tinnitus source or tinnitus/misophonia-evoked reactions. As such, TRT is effective for any type of tinnitus regardless of its etiology. TRT consists of: (1) counseling based on the neurophysiological model of tinnitus, and (2) sound therapy (with or without instrumentation). The main role of counseling is to reclassify tinnitus into the category of neutral stimuli. The role of sound therapy is to decrease the strength of the tinnitus signal. It is crucial to assess and treat tinnitus, decreased sound tolerance, and hearing loss simultaneously. Results from various groups have shown that TRT can be an effective method of treatment.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 32 · R0590

**Audiological Characteristics of a Sample of Adults With Misophonia.**

2024 · American journal of audiology · article, journal article, journalarticle · eng · https://doi.org/10.1044/2024_aja-24-00111

PURPOSE: The aim of this study was to describe the audiological test results from a sample of 60 adults with self-reported misophonia. METHOD: Audiological testing was completed prior to participant randomization in a controlled trial for misophonia treatment. Participants completed the Inventory of Hyperacusis Symptoms Survey (IHS), the Tinnitus and Hearing Survey (THS), the Misophonia Questionnaire (MQ), and behavioral and objective audiometric measures. RESULTS: Hearing thresholds were less than 25 dBHL for 97% of the participants. Loudness discomfort levels for tonal stimuli suggested hyperacusis in 25% of the sample. Total scores on the IHS indicated that 12% met the clinical cutoff for hyperacusis, and, on the THS, 27% experienced problems with tinnitus, 77% experienced problems with hearing, and 53% experienced problems with sound tolerance. On the MQ, 37% indicated mild levels of misophonia and 58% indicated moderate levels. For speech-in-noise testing, a mild signal-to-noise ratio loss was present for 15% of participants. Most of the participants had present distortion product otoacoustic emissions (DPOAEs). CONCLUSIONS: Audiological data on individuals with misophonia are lacking. In this article, we present results from audiological testing on 60 adults with self-reported misophonia. Most had normal peripheral hearing sensitivity based on pure-tone audiometry and DPOAE measures; some had difficulties with sound sensitivities and understanding speech-in-noise, self-report indicated problems with hyperacusis, tinnitus, and hearing difficulty.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 33 · R1162

**Proximal Binaural Sound Can Induce Subjective Frisson**

2020 · Frontiers in Psychology · article · en · https://doi.org/10.3389/fpsyg.2020.00316

Auditory frisson is the experience of feeling of cold or shivering related to sound in the absence of a physical cold stimulus. Multiple examples of frisson-inducing sounds have been reported, but the mechanism of auditory frisson remains elusive. Typical frisson-inducing sounds may contain a looming effect, in which a sound appears to approach the listener's peripersonal space. Previous studies on sound in peripersonal space have provided objective measurements of sound-inducing effects, but few have investigated the subjective experience of frisson-inducing sounds. Here we explored whether it is possible to produce subjective feelings of frisson by moving a noise sound (white noise, rolling beads noise, or frictional noise produced by rubbing a plastic bag) stimulus around a listener's head. Our results demonstrated that sound-induced frisson can be experienced stronger when auditory stimuli are rotated around the head (binaural moving sounds) than the one without the rotation (monaural static sounds), regardless of the source of the noise sound. Pearson's correlation analysis showed that several acoustic features of auditory stimuli, such as variance of interaural level difference (ILD), loudness, and sharpness, were correlated with the magnitude of subjective frisson. We had also observed that the subjective feelings of frisson by moving a musical sound had increased comparing with a static musical sound.

**Решение:** -6 не про мизофонию

---

### 34 · R0482

**Hyperacusis: How You Can Help Yourself**

2024 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0001069204.18007.af

Hyperacusis is an auditory sensitivity disorder in which an individual has a markedly decreased intolerance of everyday sounds that are neither threatening nor uncomfortably loud to a typical person.1,2 A slightly distinct definition has been proposed recently, which considers hyperacusis to be present if a person experiences reduced sound tolerance, whether it causes distress or not.3 Regardless of the definition, some low-and-medium-intensity everyday sounds can become so loud for a person with hyperacusis that they cause pain or discomfort. This condition leads to significant distress and impairment on the quality of life for millions of people worldwide.1,2,4,5Hyperacusis prevalence has been observed in 8-17% of the general population.6 Studies report that up to 90% of people with hyperacusis also have tinnitus, and 40% to 55% of people who have tinnitus also have hyperacusis .5,7–10 Daily social, professional, and recreational activities are severely hindered by hyperacusis, which can result in anxiety and depression.4,5,9,11–13 There are four main subtypes associated with hyperacusis: loudness, annoyance, fear, and pain.5,10,11 With loudness hyperacusis, moderate sounds are uncomfortably loud, such as a restaurant noise, dog barking, sirens, or horns. With annoyance hyperacusis, also referred to as misophonia, patients feel abnormally bothered by certain sounds such as pen clicking, sinks dripping, or plastic bag noise, even though they are not always too loud. With fear hyperacusis, referred to as phonophobia, patients anticipate a given situation involving a significant sound exposure. With pain hyperacusis, patients report pain in their ears or head while exposed to moderately intense sounds, such as the noise of electric tools, doors slamming, sudden and loud noises, or even people talking loudly. Individuals occasionally exhibit more than one of these symptoms, such as sounds perceived as being very loud also becoming annoying.11 Therefore, individuals with hyperacusis often avoid situations that could present harmful experiences. While there are no cures for hyperacusis, there are several approaches that patients find successful to lessen the discomfort when everyday sounds are too loud.5,7,14 Hyperacusis is a symptom and not a disease. As a symptom, hyperacusis is a condition that has several causes and, therefore, affects individuals in different ways and degrees, requiring different treatments and individualized counseling.5 WHAT CAUSES HYPERACUSIS? Although the most common cause of hyperacusis is exposure to high levels of sound pressure, there are many different causes of hyperacusis, and for many people the cause of hyperacusis is unknown. It can appear spontaneously or after hearing a sudden loud noise, such as fireworks. It can also appear alongside other conditions, such as tinnitus, head injury, Ménière’s disease, Bell’s palsy, Lyme disease, migraines, Williams syndrome, and autism spectrum disorder.2,5 Children are often more sensitive to loud noise than adults, and sensitivity usually lessens as they age.15,16 But some children may become more sensitive to noise than others after having an ear infection, for example, or if they have another condition, such as autism spectrum disorder.17,18 Research indicates that hyperacusis is present in 18% of people with autism.19 Moreover, in a study of 55 patients with Asperger’s syndrome, 69% experienced hyperacusis, while 35% reported experiencing tinnitus.17 Available treatments depend on the cause and effect of hyperacusis in the patient’s life.5,20 For some individuals, receiving counseling is enough to cope with hyperacusis. For others, hyperacusis is so fearful that it is necessary to work with a psychologist to change their aversions to sound through behavioral modifications.5,21 If hyperacusis is a symptom of a specific health condition, it should be treated in parallel with the disease. Moreover, if hyperacusis is caused by another condition, treating the condition may stop hyperacusis. If there is no clear or known cause, a treatment to help make the patient less sensitive to everyday sounds may be offered. HYPERACUSIS ACTIVITIES TREATMENT Hyperacusis Activities Treatment is a counseling program that includes education about hyperacusis, counseling on reactions to hyperacusis, and personalized treatments to relieve symptoms.5 Treatment options include sound therapy, medications, and relaxation exercises. Activities to desensitize and retrain the auditory system are also used, depending on the symptoms presented by each patient and the impact of hyperacusis on the patient’s life. Hyperacusis Activities Treatment uses pictures to guide counseling, which have several advantages for patients and audiologists on the management of hyperacusis. For individuals with hyperacusis, this approach offers several benefits that assist you in comprehending your condition and coping effectively, such as: enhanced understanding of concepts related to your condition, making it easier for you to grasp critical information; ensuring crucial concepts are not overlooked by clinicians, thereby providing a comprehensive understanding of your condition and its management; structured sessions that facilitate an organized and coherent process, enabling you to navigate through your treatment journey more effectively; adaptability of the sessions to meet the unique needs and interests of each patient which ensures a more personalized and tailored approach to coping strategies, optimizing the effectiveness of the treatment. Education about Hyperacusis. Knowledge is the first step to successful management of hyperacusis.5,22 Thus, it is important for you to understand your condition, its causes, and management strategies. Individuals are encouraged to self-educate about hyperacusis by considering whether they find sounds too loud, bothersome, fear-inducing, or painful; the duration and perceived causes of the condition; the presence of tinnitus or other auditory sensations; and the possible involvement of other sensory symptoms such as sensitivity to smell, touch, or vision. Reflecting on these queries concerning your hyperacusis experiences and your auditory capabilities might reveal the differential impact on various areas. Over time, you may notice changes in your responses to these questions, especially as you undergo counseling or other treatments for hyperacusis. Hyperacusis symptoms can improve with time, so it is essential to regularly re-assess personal reactions and experiences. Communication Strategies. Hyperacusis and tinnitus are auditory disorders that can significantly impact an individual’s ability to communicate and engage in social interactions. Individuals with these conditions often experience heightened sensitivity to sound and may have difficulty hearing clearly. To facilitate effective communication and convey your needs to others, individuals with hyperacusis and tinnitus can use various strategies, such as: Disclosing your condition. Individuals with tinnitus and hyperacusis should inform their friends, partners, and colleagues about their auditory challenges. A simple and direct statement, such as “I have hyperacusis” can set the foundation for effective communication and foster understanding. Requesting slow speech. Encourage partners to speak slowly and enunciate words clearly. Rapid speech can be challenging to follow for individuals with auditory sensitivity. By requesting slower speech, you can better process and comprehend the spoken information. Choosing an optimal environment. Selecting a quiet and controlled environment for conversations is crucial. Background noise can exacerbate the challenges faced by those with hyperacusis and tinnitus. Moving to a quiet place minimizes discomfort to sounds and allows for better focus on the conversation. Let your friends and partner know in which environments you feel most comfortable and can easily control the presence of any unpleasant sounds. Educational initiatives. Encourage close friends, family, and colleagues to learn about hyperacusis and tinnitus. Educating others about these conditions can lead to increased empathy and better communication strategies. Counseling on Reactions to Hyperacusis. There are many different approaches to hyperacusis counseling, such as cognitive behavioral therapy, tinnitus retraining therapy, and the Hyperacusis Activities Treatment.5,21,23 Research indicates that counseling is preferred by patients in managing symptoms of hyperacusis.4 Counseling is typically provided by an audiologist who will examine the reactions of a patient when everyday sounds are too loud, and discuss strategies to learn to respond to hyperacusis in a more positive way. Hyperacusis Activities Treatment focuses on individuals’ reactions to their concerns and addresses how they might modify their responses to distressing sounds.5 The process involves guiding individuals under the supervision of an audiologist. The primary aim of this counseling is not to eliminate hyperacusis but to decrease the apparency of hyperacusis for the patient; change the perception of hyperacusis so that it becomes less distressing; and equip individuals with strategies to alleviate the impacts when hyperacusis becomes problematic. Additional Treatments to Relieve Symptoms. Beyond counseling, sound therapy, medication, and relaxation exercises can relieve hyperacusis symptoms. Specific treatment approach may vary depending on individual needs and the severity of symptoms. You should consult an audiologist for a comprehensive evaluation and personalized treatment plan. Sound Therapy. Sound therapy consists of introducing background sounds to reduce annoyance and/or increase sound tolerance. Studies show that combining counseling and sound therapy approaches is beneficial in managing hyperacusis symptoms.20,21,23,24 By introducing sounds gradually and gently, you may resume daily activities instead of avoiding them.5 The therapy aims to retrain the auditory system and desensitize it to sounds that would typically be perceived as uncomfortable or painful. Noise generating devices such as smartphones, white noise machines, and sound therapy apps are used to reproduce sounds that cause patients discomfort. Initially, the sounds are presented at a very low, tolerable intensity. The sound intensity is then gradually increased until the patient’s discomfort threshold increases.5 The period required to obtain favorable results depends on the duration and severity of the hyperacusis and varies between individuals. Improvement in hyperacusis symptoms through sound therapy could take months to see. Living with hyperacusis can pose unique challenges, but there are self-help techniques that you can use to alleviate the discomfort associated with sound sensitivity. Hyperacusis patients can regain a sense of control over their auditory experiences by: Resting in a controlled environment. Creating a calming and controlled environment is paramount for individuals with hyperacusis. Choosing quiet spaces where external noise is minimal allows the auditory system to recover and reduces the potential for discomfort. Designating a peaceful space for relaxation can significantly contribute to overall well-being. Embracing gentle recorded sounds. Whether it is the soft rustling of leaves, flowing water, or soothing instrumental music, these sounds can provide a therapeutic backdrop while the individual engages in activities like reading or watching a movie. The key is to select sounds that resonate positively and create a calming atmosphere. Documenting triggering sounds. This can be a collaborative effort involving friends or family. Record these sounds or have someone record them for you. This process not only helps you acknowledge your triggers but also serves as a foundation for your sound desensitization journey. Gradual exposure and desensitization.5,25 Over a period of several weeks, work on gradually exposing yourself to the recorded sounds that trigger your hyperacusis. Start at a low volume that feels manageable and gradually increase the volume over time. This controlled approach allows the auditory system to adapt to the sounds, potentially reducing sensitivity over time. Mindful progress tracking. Keep a journal to document progress as you expose yourself to triggering sounds. Note any changes in your reactions, comfort levels, and sensitivity. Tracking your journey helps you recognize improvements and adjustments you might need. Patience and self-care. Managing hyperacusis is a gradual process that requires patience and self-compassion. You should be kind to yourself on this journey of self-help. Celebrate small victories and acknowledge efforts in working towards a more comfortable relationship with sound. Self-help strategies can significantly contribute to managing hyperacusis, but you should consult an ear, nose, and throat (ENT) specialist or audiologist if symptoms persist or worsen. These self-help techniques allow you to take an active role in regaining control over your auditory experiences and enhancing your overall quality of life. The sound therapy treatment protocol used in Hyperacusis Activities Treatment and a listening diary for hyperacusis patients is available in Appendix A. Medication. There is no specific medication approved for the treatment of hyperacusis. Certain medications may be prescribed to manage associated symptoms, such as anxiety, depression, and sleeping problems, or underlying conditions that contribute to hyperacusis. The usage and selection of medications will depend on the specific symptoms, medical history, and the guidance and prescription of a qualified healthcare professional. The effectiveness of medication for hyperacusis can vary between individuals, and careful monitoring of the individual’s response and potential side effects is necessary. Relaxation Exercises. Relaxation exercises are intended to provide coping strategies and lessen fear and anxiety that occur in response to environmental sounds. Progressive Muscle Relaxation is one method of practicing relaxation that requires the patient to focus on tensing and relaxing groups of muscles until the patient can release any remaining tension in their body.5 This trains the patient to initiate muscular relaxation whenever tension arises. Another relaxation technique that is popular among patients is visual imagery. In this, the patient’s attention is focused on a sensory experience. You may choose to create a mental image or recall past places and events you have experienced. Other relaxation techniques patients can explore include deep breathing, mindfulness, or meditation.5 A resource detailing relaxation exercises utilized in Hyperacusis Activities Treatment is available in Appendix B. WHEN TO USE EAR PROTECTION In a world bustling with auditory stimuli, it becomes crucial for everyone, especially hyperacusis patients, to safeguard themselves against the detrimental impact of intense sounds. Excessive noise exposure can not only lead to hearing impairment but also trigger conditions like tinnitus and hyperacusis, both of which greatly affect one’s auditory well-being. Intense sounds come in various forms, from sudden impulsive noises like loud bangs to prolonged continuous noises like construction sites or traffic. For individuals with hyperacusis, both types of sounds can be distressing and even painful. Hearing protection serves as a shield against the potential harm caused by intense sounds. There are various options available to cater to different scenarios: Earplugs. These compact devices effectively attenuate sound by reducing its intensity across different frequency ranges. Earplugs are discrete and can be worn comfortably in various settings. Filtered earplugs are preferable as they can be custom or universal to help reduce the intensity of the sound, and yet preserve speech perception abilities. Filtered plugs have an advantage of passing more sound through the ear compared to foam plugs, and therefore help to improve tolerance to moderately-loud sounds. Earmuffs. Offering a larger physical barrier, earmuffs cover the ears entirely, providing substantial sound reduction. They are particularly useful in environments where noise levels are consistently high. Combination of earplugs and earmuffs. In exceptionally noisy situations, using both earplugs and earmuffs simultaneously can yield even greater protection. Musician earplugs can also be recommended to patients with hyperacusis. These earplugs produce a smooth, flat attenuation across frequencies, resulting that the sounds heard through the earplugs retain the same quality as the original.5 Conventional earplugs are certainly recommended for particularly noisy activities such as working in environments with high sound pressure levels or attending shows with loud music. You should discuss ways to reduce your use by talking to your audiologist if you are using earplugs or earmuffs in everyday situations. It is a common behavior of people with hyperacusis to avoid loud sounds, which can lead to an increased sensitivity to sound over time.2,5,10,20 While avoiding loud environments, or wearing earplugs or earmuffs to reduce discomfort to sounds is normal, this will not help hyperacusis symptoms in the long term. In addition, using ear plugs every day causes communication difficulties. HOW TO COPE WHEN EVERYDAY SOUNDS ARE BOTHERSOME When environmental sounds are too loud, you can try these additional activities included in the Hyperacusis Activities Treatment and other hyperacusis management programs:5,22 Surround yourself with comfortable sound. It is important that you never stay away from sound completely. This could cause the auditory system to get used to the absence of sound, making it increasingly difficult to tolerate everyday sounds. Avoiding sounds completely will only make the problem worse. Therefore, you should try to stay in environments with sounds that are comfortable for you. Listen to sounds that are pleasant to you whenever possible. This may help you tolerate the everyday sounds that you do not like. Use hearing protection, such as filtered earplugs, for noisy situations only. Whenever the sounds in an environment are at a safe and comfortable level, you should remove your hearing protection. Consistent use of hearing protection will change the neural input to the brain and cause reactions to hyperacusis to worsen over time. Earplugs are only recommended when sounds are uncomfortably loud or dangerous. BE WARY OF “NEW” TREATMENTS Claims about “new” treatments or even a “cure” for hyperacusis must be critically analyzed and carefully considered for whether they are reported in reputable scientific journals; whether the study has been cited in other scientific references; whether a controlled study was conducted on hyperacusis patients; and whether the reported benefit persisted for a long time after the treatment was administered. The search for magical pills and useless treatments can generate negative effects and efforts. Only trusted professionals can determine the best treatment for a patient’s case. CONCLUSION It is important to consult an ENT specialist and an audiologist about hyperacusis and work with them on developing an effective treatment plan. Hyperacusis is a symptom, but not a disease. It has various causes and usually requires multidisciplinary treatment. Educate yourself on the available healthcare professionals specializing in hyperacusis treatment, such as audiologists, ENT specialists, or tinnitus and hyperacusis therapists or psychologists who can provide tailored guidance and support for managing your condition. Understanding basic information on the symptom is the first step to success in hyperacusis management. Hyperacusis can be characterized as an intolerance or hypersensitivity to some low and medium intensity sounds of daily life, such as a dog barking or a baby crying, which are not considered to people hyperacusis. These common sounds can become so for the person with hyperacusis that they may cause discomfort from the loudness or annoyance of the sound, as as fear and/or There are many different causes of hyperacusis, and for many the cause of hyperacusis is unknown. While there is no there are many treatment strategies, such as Hyperacusis Activities by qualified professionals that can help to the negative of hyperacusis and improve one’s quality of life. of information and help from qualified professionals making any Although the use of hearing protection is paramount in noisy situations, it is important to the potential with earplugs or earmuffs can one’s ability to and understand speech, especially in social situations. This is a significant for hyperacusis patients who to in In addition, the use of hearing protection can potentially exacerbate their condition, making them even more sensitive to sounds. Educate yourself on effective communication strategies that can help you navigate social situations. your condition with others and how they can support you. in your needs to By these strategies, individuals with hyperacusis can take control of their auditory safeguard their and foster with those

**Решение:** -1 колонка / обзор (The Hearing Journal)

---

### 35 · R0135

**Parent and Caregiver Perspectives: The Lived Experience of Raising a Child with Misophonia.**

2026 · Child psychiatry and human development · article, journal article, journalarticle · eng · https://doi.org/10.1007/s10578-026-02013-7

Misophonia is a newly recognized disorder characterized primarily by negative multi-modal emotional responses (e.g., behavioral, attentional, somatic, interpersonal, and cognitive) to certain repetitive sounds and related stimuli, usually produced by other people. Previous research has found that adults with misophonia commonly report that it begins in childhood and can cause significant psychological distress and functional impairment at home, school, and/or work. However, little is known about the challenges and perspectives of those raising a child with misophonia. Therefore, the purpose of the current study was to investigate the impact of caring for a child with misophonia, specifically in a sample of caregivers reporting any financial strain. We surveyed adult caregivers of people with misophonia (N = 22) to collect both descriptive and qualitative information. Using guidelines for reflexive thematic analysis [5], several themes emerged: (1) Household Impacted, (2) Caregivers Impacted, (3) Financial Impact of Misophonia, and (4) Non-financial Barriers to Care. This study highlights some of the challenges parents experience and explores shortcomings in treatment, advocacy, and awareness to inform misophonia researchers and clinicians on how to best support families raising someone with misophonia.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 36 · R1282

**Investigating Misophonia: A Review of the Empirical Literature, Clinical Implications, and a Research Agenda.**

2018 · Frontiers in neuroscience · article, journal article, review · eng · https://doi.org/10.3389/fnins.2018.00036

\ua9 2018 Brout, Edelstein, Erfanian, Mannino, Miller, Rouw, Kumar and Rosenthal. Misophonia is a neurobehavioral syndrome phenotypically characterized by heightened autonomic nervous system arousal and negative emotional reactivity (e. g., irritation, anger, anxiety) in response to a decreased tolerance for specific sounds. The aims of this review are to (a) characterize the current state of the field of research on misophonia, (b) highlight what can be inferred from the small research literature to inform treatment of individuals with misophonia, and (c) outline an agenda for research on this topic. We extend previous reviews on this topic by critically reviewing the research investigating mechanisms of misophonia and differences between misophonia and other conditions. In addition, we integrate this small but growing literature with basic and applied research from other literatures in a cross-disciplinary manner

**Решение:** -1 обзор / комментарий / письмо

---

### 37 · R0271

**Utility of and preliminary psychometric reliability and validity of a measure of psychological inflexibility for misophonia**

2025 · Journal of Contextual Behavioral Science · article, journalarticle, google scholar result · en · https://doi.org/10.1016/j.jcbs.2025.100896

Misophonia is a psychological disorder that has been under researched despite the impact it can have on functioning and quality of life. Acceptance and commitment therapy (ACT) has been explored as a potential treatment option for misophonia. The process of change targeted by ACT is psychological flexibility. However, research on the association of psychological inflexibility and misophonia is nascent, as there are not misophonia-specific measures available. In this study we validated a measure of misophonia-specific psychological inflexi-bility, the misophonia acceptance and action questionnaire (miso-AAQ). Participants (N = 120) were from a randomized controlled trial of ACT for misophonia and matched control participants. All completed the miso-AAQ at pre-treatment. Preliminary results indicate the miso-AAQ has satisfactory internal reliability ( α = .84). and validity ( r s = 0.33-0.55, ps < 0.05). Results also provide preliminary support of misophonia-related psychological inflexibility as a potential mediator in the relationship between misophonia symptom severity and anger and stress. Future directions and implications are discussed.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 38 · R0884

**Le retentissement corporel du bruit dans l’existence de patients souffrant de misophonie et d’hyperacousie**

2022 · HAL (Le Centre pour la Communication Scientifique Directe) · conference object, conference paper, conference-paper · fr · https://hal.science/hal-05586607v1

International audience

**Решение:** ? нет аннотации (тезисы конференции HAL)

---

### 39 · R0775

**The Analogy between Tinnitus and Chronic Pain: A Phenomenological Approach**

2023 · Brain Sciences · article · en · https://doi.org/10.3390/brainsci13081129

Tinnitus is an auditory sensation without external acoustic stimulation or significance, which may be lived as an unpleasant experience and impact the subject's quality of life. Tinnitus loudness, which is generally low, bears no relation to distress. Factors other than psychoacoustic (such as psychological factors) are therefore implicated in the way tinnitus is experienced. The aim of this article is to attempt to understand how tinnitus can, like chronic pain, generate a 'crisis' in the process of existence, which may go as far as the collapse of the subject. The main idea put forward in the present article is that tinnitus may be compared to the phenomenon of pain from the point of view of the way it is experienced. Although the analogy between tinnitus and pain has often been made in the literature, it has been limited to a parallel concerning putative physiopathological mechanisms and has never really been explored in depth from the phenomenological point of view. Tinnitus is comparable to pain inasmuch as it is felt, not perceived: it springs up (without intention or exploration), abolishes the distance between the subject and the sensation (there is only a subject and no object), and has nothing to say about the world. Like pain, tinnitus is formless and abnormal and can alter the normal order of the world with maximum intensity. Finally, tinnitus and pain enclose the subject within the limits of the body, which then becomes in excess. Tinnitus may be a source of suffering, which affects not only the body but a person's very existence and, in particular, its deployment in time. Plans are thus abolished, so time is no longer 'secreted', it is enclosed in an eternal present. If the crisis triggered by tinnitus is not resolved, the subject may buckle and collapse (depression) when their resources for resisting are depleted. The path may be long and winding from the moment when tinnitus emerges to when it assaults existence and its eventual integration into a new existential norm where tinnitus is no longer a source of disturbance.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 40 · R0731

**Misophonia: nearly one in five UK adults have the condition causing extreme reactions to certain sounds**

2023 · The Conversation · article, other · en · https://doi.org/10.64628/ab.atysekwue

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 научно-популярная статья (The Conversation)

---

### 41 · R1004

**Misophonia: A Detailed Case Series and Literature Review.**

2022 · The primary care companion for CNS disorders · article, journal article, review · eng · https://doi.org/10.4088/pcc.21cr03124

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 42 · R0250

**Distinct neural circuits processing pleasant and unpleasant sounds: an fMRI-based approach.**

2025 · BMC neuroscience · article, journal article, journalarticle · eng · https://doi.org/10.1186/s12868-025-00975-3

Investigating how the human brain processes the emotional valance of sounds is critical for understanding sensory, emotional, and motor integration at the neurobiological level. The current study utilized functional magnetic resonance imaging (fMRI) to investigate the differential brain activation patterns elicited by pleasant, unpleasant, and neutral sounds from the International Affective Digital Sounds (IADS-2) collection. Thirty healthy volunteers listened to these sounds under fMRI, followed by post-scan ratings of valence (pleasant versus unpleasant) and arousal (calm versus exciting). Average ratings did not differ from IADS-2 norms. Pleasant sounds significantly activated brain regions implicated in reward and positive affect, including the mPFC, ventral anterior cingulate cortex, and inferior frontal gyrus, compared to neutral sounds. Alternatively, unpleasant sounds elicited stronger and more widespread activation, particularly in the amygdala, nucleus accumbens, insula, and cerebellum, regions associated with negative affect and aversive learning. These results demonstrate the pivotal contributions of the amygdala in identifying unpleasant stimuli and of the mPFC in assessing pleasant auditory inputs, expand our current understanding of affective regulation at the neural circuit level, and provide a foundation for the development of sound-based interventions to treat auditory-emotional disorders such as misophonia and anxiety. Not applicable. This study uses functional MRI to reveal that pleasant and unpleasant sounds activate distinct neural circuits involved in emotional and sensory processing. Pleasant sounds primarily engaged reward-related regions, including the medial prefrontal cortex and anterior cingulate cortex, while unpleasant sounds strongly activated the amygdala, insula, and cerebellum—areas linked to aversion and emotional arousal. These findings contribute to a better understanding of the brain’s emotional response to auditory stimuli and may inform future imaging-based approaches to diagnose or manage auditory-emotional disorders such as misophonia and anxiety.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 43 · R0286

**Perspectives on self-management of noise intrusion in daily living with hyperacusis**

2025 · Hearing Research · article · en · https://doi.org/10.1016/j.heares.2025.109452

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 44 · R1032

**An Expert Roundtable Discussion on Experiences of Autistic Autism Researchers**

2021 · Autism in Adulthood · article, other literature type · eng · https://doi.org/10.1089/aut.2021.29019.rtb

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 45 · R1327

**Hyperacusis and disorders of sound intolerance**

2018 · International Journal of Audiology · article, journal article, journalarticle · eng · https://doi.org/10.1080/14992027.2018.1514471

Patients present to audiologists with concerns regarding uncomfortable loudness perception in the face of normal hearing or in being extremely disturbed by sounds such as breathing, chewing and swallowing. These symptoms are classified as disorders of sound tolerance and are relatively new to many audiologists. These patients contact audiologists for assessment and treatment of their issues, often after they have sought help from other professions, such as general medicine or psychology, and have been dismissed or told that their symptoms “sound crazy.” Questions arise as to how the profession of audiology addresses this patient population. Sound tolerance is a novel and emerging area and, as decisions are made about how to work with this population, these patients are seeking services from audiologists. Hyperacusis and Disorders of Sound Intolerance is a more than welcome addition to the field of audiology. Marc Fagelson and David Baguley have developed the only text that addresses these areas and it is a strong contribution. They have provided a comprehensive overview of the literature available and a direction for making clinical decisions with this patient population. In addition to writing chapters, Fagelson and Baguley have amassed internationally recognised experts in hyperacusis and related disorders as contributors. Section I of the text addresses definition, measurement, and epidemiology of hyperacusis and other disorders of sound perception, such as misophonia and phonophobia. These first four chapters set the foundation for understanding the scope of the disorders and considerations in audiologic assessment and questionnaires that address patient presentation of loudness tolerance issues. The rest of the text is well balanced with this strong foundation, with some chapters that are standouts. Chapter Seven, authored by Don McFerran, is a particularly useful overview of medical diagnoses related to hyperacusis and is useful for an audiologist exploring possible aetiologies and directing case history. Chapter Nine covers Traumatic Brain Injury and Auditory Processing, authored by Drs. Papesh, Theodoroff and Gallun. It delivers an excellent review of issues related to the epidemic of concussion and acquired brain injury with symptoms that often impact the auditory system, including hyperacusis. A unique contribution is a chapter on diplacusis, disorders of pitch perception. Other particularly strong chapters address the topics of sound sensitivity issues in the paediatric population and the use of hearing aids as treatment. There are references and recommendations throughout the text that provide insight into the emotional aspects of these disorders and the impact they have on patients and their families. This book provides a robust foundation for evaluating and treating patients with hyperacusis and/or other sound tolerance issues. Drs. Fagelson and Baguley are pioneers in this area and have done an admirable job of creating a valuable resource for audiologists. This book should be considered a standard for a clinical library and will likely end up in university and public libraries. It can serve as a resource for patients seeking information, who, in turn, will drive audiologists to learn more on these topics. The authors note that they “... continue to learn what it means for people and their families to live with hyperacusis and other forms of sound intolerance.” This book certainly addresses where the profession is in this journey; hopefully by the time that the Second Edition of the text is available, there will be advances in tools to assess and treat this population and advance the understanding of sound tolerance issues. This text is a first great step in addressing those areas.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 46 · R1186

**A Case of Bipolar Disorder and Misophonia.**

2020 · The primary care companion for CNS disorders · article, case reports, journal article · eng · https://doi.org/10.4088/pcc.19l02523

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 47 · R0296

**Persian Pediatric Hyperacusis Questionnaire: Translation and Psychometric Evaluation in Children with and Without Autism.**

2025 · Journal of the American Academy of Audiology · article, journal article, journalarticle · eng · https://doi.org/10.3766/jaaa.240047

Background: Hyperacusis is an auditory perception disorder causing decreased sound tolerance to everyday sounds. Children with autism often exhibit symptoms of hyperacusis. This comorbidity can significantly impact the adaptability and social development of the children. Purpose: This study’s objectives were to translate and psychometrically evaluate the Persian Pediatric Hyperacusis Questionnaire (P-HQ-P) and the prevalence determination of hyperacusis among children with or without autism. Study Sample: The study was conducted by assigning 60 parents of children diagnosed with level 1 autism spectrum disorder (ASD) and 30 parents of typical children to the ASD group and control group, respectively. Data Collection and Analysis: In the first stage, the Pediatric Hyperacusis Questionnaire (P-HQ) was translated into Persian, and in the second stage, its reliability and validity were assessed by the classical test theory methods. The P-HQ-P results were compared with the Persian Sensory Profile 2 (SP2-P). Results: The P-HQ-P demonstrated acceptable validity and reliability, with content validity ratio &gt; 0.99, content validity index &gt; 0.92, face validity &gt; 0.90, cross-cultural validity &gt; 0.94, α = 0.8, and intraclass correlation coefficient = 0.85. Spearman’s rank correlation coefficient showed a strong correlation (r = 0.83) between the P-HQ-P score and a group of seven items from SP2-P. There was not a statistically significant difference in hyperacusis between genders. Conclusions: The psychometric properties of the P-HQ-P were found to be acceptable, which made it suitable for clinical and research usage. The prevalence of hyperacusis was reported at 27.8 percent of the total sample and 38.3 percent in the ASD group. Our findings suggest the need for further research on hyperacusis in the Iranian pediatric population.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 48 · R0572

**Sound Induced Dental Sensitivity**

2024 · Pakistan Journal of Health Sciences · article, journalarticle · en · https://doi.org/10.54393/pjhs.v5i11.2154

Tooth sensitivity is a common complaint of patients [1], which can be defined as an exaggerated response to a stimulus such as thermal, chemical, tactile, osmotic, or air-current that usually causes no response in a normal, healthy tooth [2-4] but have you ever winced when hearing the screech of nails on a chalkboard or felt sharp discomfort in your teeth at the sharp sounds, such as the sound of metal scraping against metal? These reactions are common among people, as most of us feel during our lifetime. The scientific community has yet to fully explain why certain sounds cause physical discomfort in teeth. Most of the dental and facial pain had a psychological or behavioural impact. Thus, dental and facial pain is a relevant problem that is mostly associated with tooth sensitivity [5]. Direct research on the phenomenon of sound-induced teeth sensitivity is almost nil which is a void to be filled by scientists. Deep studies on misophonia, auditory-tactile synesthesia, polyvagal theory, cross-modal sensory processing, and teeth conduction provide reasonable insights that can help us understand this phenomenon. Analyzing opinion-based clues from different studies, we can explain how sharp sounds such as metal scratching can induce sensitivity in our teeth. Misophonia means "hatred or dislike of sound." It is a neurobehavioral syndrome phenotypically characterized by heightened autonomic nervous system arousal and negative emotional reactivity (e.g. irritation, anger, anxiety) in response to a decreased tolerance for specific sounds [6-8]. It is characterized by a negative reaction to a sound with a specific pattern and meaning to a given individual. Trigger sounds include food chewing, sniffling, persistent coughing, knuckle cracking, metal scratching, and nail scratching [9, 10]. The phenomenon of tooth sensitivity can be explained by misophonia in certain ways in light of different research and theories. No direct link has been explained by the researchers to teeth sensitivity, but as professionals, we have selected the lines that reflect the concept of sound-induced teeth sensitivity. The concept we extract from the condition of misophonia is that teeth sensitivity is the negative response of the body to the triggering misophonic sounds like screeching of metal. Another study suggests that individuals with misophonia exhibit stronger activation in the orofacial motor area in response to trigger sounds, indicating a motor response to misophonia [11]. Dr. Stephen Porges devised the polyvagal hypothesis, which explains how the neurological system reacts to safety or danger by concentrating on the vagus nerve, which connects the brain to the face, neck, and internal organs. Sensations of security and calm are brought on by healthy vagus nerve activity. On the other hand, when it malfunctions, dangerous reactions might occur even in the absence of real dangers. This idea links the body's stress response to sound-induced oral sensitivity. The autonomic nervous system, in particular the vagus nerve, is responsible for inducing a "fight, flight, or freeze" reaction in response to perceived dangers, such as specific noises, according to the polyvagal theory [12-15]. Certain noises may cause an unconscious stress reaction in those who have sound-induced dental sensitivity, which makes them more sensitive to oral stimuli. This response is like how people have misophonia, and strongly react to specific noises. Essentially, the nervous system may interpret sound as a threat, causing unpleasant sensations. There could be a neural connection between hearing and touch, according to a study by Oxford University Press, which indicates that the auditory and somatosensory systems are well related. An anatomical basis for multisensory interactions is provided, explaining why some unpleasant sounds irritate. Within this framework, the correlation between metallic scraping noises and tooth sensitivity can be twigged as cross-modal perception, which can be elucidated in two ways: (1) Sensory Association: The brain interprets unpleasant sounds with high pitch as physical sensations, causing tooth pain. (2) Neural Overlap: When certain noises are heard, the activation of neural circuits linked to tooth pain may result from the overlap of auditory and somatosensory regions [16]. Auditory-Tactile Synesthesia: This condition involves sounds evoking tactile sensations due to cross-modal processing and hyper-connectivity in the brain. Different sounds can induce various tactile sensations such as vibrations, warmth, and tingling, varying among individuals [17]. In the context of this study, we can suppose that certain sounds can induce painful tactile sensations in the teeth in the form of sensitivity. This study suggests that specific sounds can trigger painful tactile sensations in teeth, manifesting as sensitivity. Both teeth and bones serve as sound conductors. High-frequency sounds, like metal scratching, are conducted through the skull's bone to the teeth or directly by the teeth, causing sensitivity. These sounds disturb dental tubular fluid, which stimulates baroreceptors and leads to teeth sensitivity according to the concept of hydrodynamic theory [18, 19]. Despite, various plausible reasons discovered by linking several studies, further study is needed to recognize the exact source of sound-induced oral sensitivity. Researchers must also determine the prevalence of this condition, whether it is general or affects only a small percentage of the population. Future studies may focus on neuroimaging studies to detect brain activity in people who experience this phenomenon, or it could look into whether there is a genetic predisposition that renders certain people more prone to this form of multimodal pain. The phenomenon known as sound-induced dental sensitivity is a fascinating nexus between the fields of neuroscience, psychology, otolaryngology, and dentistry to investigate the relationship between pain in the teeth and the other systems. The interdisciplinary approach involving neurology, otolaryngology, and psychology can help the researchers understand the idea of sound-induced tooth sensitivity, which will ultimately help those who are affected by it. Identifying the gap could help dentists improve their dental practices by enabling them to investigate sound-induced dental discomfort and provide specialized, comfortable, anxiety-free, high-quality services. The results could also help develop customized treatment plans that take into account a patient's sensitivity to particular sounds or discover and use cutting-edge technical solutions like sound-mitigating devices during dental procedures. Additionally, the introduction of innovative dental materials that reduce sound vibration transmission might be considered.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 49 · R0760

**What is autonomous sensory meridian response (ASMR)? A narrative review and comparative analysis of related phenomena.**

2023 · Consciousness and cognition · article, journal article, review · eng · https://doi.org/10.1016/j.concog.2023.103477

A narrative review of autonomous sensory meridian response (ASMR) was carried out. Definitional factors relevant to ASMR were canvassed. Related, but distinctly unique, sensorial phenomena, including frisson, synaesthesia, and misophonia were considered. Finally, the status of literature with respect to clinical outcomes, individual differences, and current research applications was evaluated. ASMR is a nascent phenomenon that has rapidly progressed in scope and depth of study throughout the past decade; a notable shift from brief-form studies to an increase in formalised trials is noted. Yet, critical questions remain unaddressed, including expectancy and placebo effects, that future research should interrogate.

**Решение:** -1 обзор / комментарий / письмо

---

### 50 · R0113

**Parent-reported auditory difficulties in children with ADHD are associated with attentional and fatigue-related vulnerability, not sound avoidance**

2026 · medRxiv · preprint · https://doi.org/10.64898/2026.09.03.26362201

Abstract Atypical sensory processing is common in attention-deficit/hyperactivity disorder (ADHD), yet decreased sound tolerance has received little attention, and it remains unclear whether it reflects actual auditory sensitivity or a vulnerability to attentional breakdown under acoustic load. The only prior study provided a single overall estimate, unable to separate sensory symptoms such as avoidance and distress from attentional and fatigue-related difficulties under noisy or demanding conditions. Here, we examined whether parent-reported auditory difficulties in children with ADHD are uniform or concentrated within specific symptom domains, and whether they vary with clinical presentation or medication. A total of 226 children (ages 6-12; 162 with ADHD, 64 typically developing controls) were assessed using the parent-report adaptation of the Khalfa Hyperacusis Questionnaire (Turkish version). The ADHD cohort was stratified by medication status and clinical presentation, and total, subscale, and item-level scores were compared across groups. Our findings show that children with ADHD scored higher than controls on the total and hyperacusis-effects subscale, but not on the coping subscale. Only four of the eleven items distinguished the groups, all reflecting concentration in noise or its decline under fatigue; no item reflecting sound avoidance, sensitivity, or distress differed between groups. This pattern was independent of clinical presentation, medication, and age; it persisted after adjustment for parental education. These results suggest that elevated auditory difficulties in ADHD are better explained by attention- and fatigue-related vulnerability than by heightened auditory sensitivity and may warrant environmental rather than audiological interventions.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 51 · R0655

**Clinical characteristics of a treatment seeking sample of adults with misophonia: Onset, course, triggers, context, and comorbidity**

2024 · Journal of Obsessive-Compulsive and Related Disorders · article, journalarticle, google scholar result · en · https://doi.org/10.1016/j.jocrd.2024.100915

Misophonia is characterized by intense emotional reactions to specific repetitive sounds. The clinical characteristics and developmental course of misophonia remain underexplored, particularly in treatment-seeking adults. In this study, we characterized the onset, symptom progression, trigger noises, and psychiatric comorbidities associated with misophonia. Additionally, we investigated the relationships between these clinical attributes and the severity of self- and clinician-rated misophonia symptoms. The sample included 60 adults with misophonia enrolled in a randomized controlled trial. Most participants (79%) reported symptom onset in childhood and early adolescence, with symptoms often worsening over time. All participants reported being bothered by human produced sounds. However, responses to trigger noises vary based on the context surrounding the sound. Those who reported equivalent distress across misophonic triggers â€“regardless of the individual producing the soundâ€”endorsed significantly higher self-reported misophonia symptoms. Approximately half of the sample met diagnostic criteria for another psychiatric condition, with attention-deficit hyperactivity disorder and generalized anxiety disorder being the most prevalent. These findings underscore the complexity of misophonia and highlight the importance of considering the individual clinical histories and contextual factors influencing reactions to misophonic sounds.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 52 · R0357

**Assessment of auditory conditions in misophonia treatment research: a scoping review.**

2025 · International journal of audiology · article, other literature type, journal article · eng · https://doi.org/10.1080/14992027.2025.2467768

Abstract Objective To identify treatment research that used a behavioural approach to treat misophonia as the primary focus of treatment, and the audiological testing included in the research. Design Scoping literature review completed in February 2023 and updated in March 2024. Study Sample Included studies that provided a behavioural or audiological intervention for misophonia, were peer-reviewed, and published in English before February 29, 2024. Studies were excluded if a pharmacological treatment was provided, if misophonia was not the primary treatment target, or if the assessment of misophonia severity was not a treatment outcome. Results Fifteen articles met the inclusion criteria. Six studies had paediatric participants and nine had adult participants. Three studies included the identification of audiological comorbidities including hearing ability, hyperacusis, and/or tinnitus in their assessment process. Nine of the studies included assessment for psychological comorbidities. For the different psychological treatment approaches, misophonia severity scores decreased from baseline from 19% to 83%. Conclusions There is a need for misophonia research to identify audiological comorbidities and to provide evidence-based guidance for addressing them within treatment. Symptoms often appear during childhood and individuals with misophonia would benefit from timely assessment and interdisciplinary coordination to address broader patient impacts in the treatment process.

**Решение:** -1 обзор / комментарий / письмо

---

### 53 · R0352

**Tinnitus and disorders of sound tolerance**

2025 · Oxford University PressOxford · part of book or chapter of book, book-chapter · en · https://doi.org/10.1093/med/9780192871633.003.0006

Abstract There is no completely satisfactory definition of tinnitus—‘the conscious perception of an auditory sensation in the absence of a corresponding external source’ is widely used but even this is not perfect as it would include the auditory hallucinations of some psychological illnesses. Most tinnitus takes the form of simple sounds such as ringing, whistling, or buzzing. However, some people report more complex sounds including musical sounds or distant voices—in such cases, there is no meaning conveyed by the voices, in contrast to psychological auditory hallucinations. Defining disorders of sound tolerance is a complicated and somewhat contentious field. The word hyperacusis is frequently employed as a blanket term for all forms of sound intolerance—in its alternative usage, hyperacusis can be defined as dislike of all sounds above a certain intensity; misophonia is a word that conveys dislike or hatred of particular sounds irrespective of their intensity; phonophobia is fear of certain sounds irrespective of intensity; and recruitment is abnormal loudness growth and is generally associated with significant sensorineural hearing loss.

**Решение:** -1 глава книги / справочник

---

### 54 · R1408

**Etiology, Composition, Development and Maintenance of Misophonia: A Conditioned Aversive Reflex Disorder**

2015 · Psychological Thought · article, preprint, journalarticle/article · en · https://doi.org/10.5964/psyct.v8i1.132

Misophonia is a recently identified condition in which an individual has an acute reaction of hatred or disgust to a specific commonly occurring sound. We propose that misophonia is a form of conditioned behavior that develops as a physical reflex through Pavlovian conditioning. Although misophonia is generally considered to be a one-step reaction, in which the sound elicits rage or disgust, as well as typical autonomic responses associated with these emotions, we propose that misophonia is a two-step reaction, in which the sound elicits an aversive conditioned physical reflex, and the aversive conditioned physical reflex elicits hatred or disgust. We also propose that the emotional response to trigger stimuli creates a Pavlovian conditioning paradigm that maintains or strengthens the misophonic physical reflex. Finally, we propose that new misophonic trigger stimuli are developed through the pairing of a neutral stimulus with a misophonic trigger stimulus. We suggest that a better name for misophonia is Conditioned Aversive Reflex Disorder (CARD) since it focuses attention on the reflexive nature of this condition and incorporates multiple stimuli modalities. A counterconditioning treatment for misophonia is presented with brief case descriptions which demonstrate the conditioned reflex nature of this disorder.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 55 · R0828

**Examining the Latent Structure and Correlates of Sensory Reactivity in Autism: A Multi-site Integrative Data Analysis by the Autism Sensory Research Consortium**

2023 · Molecular Autism · article · und · https://doi.org/10.1186/s13229-023-00563-4

Abstract Background Differences in responding to sensory stimuli, including sensory hyperreactivity (HYPER), hyporeactivity (HYPO), and sensory seeking (SEEK) have been observed in autistic individuals across sensory modalities, but few studies have examined the structure of these “supra-modal” traits in the autistic population. Methods Leveraging a combined sample of 3,868 autistic youth drawn from 12 distinct data sources (ages 3–18 years and representing the full range of cognitive ability), the current study used modern psychometric and meta-analytic techniques to interrogate the latent structure and correlates of caregiver-reported HYPER, HYPO, and SEEK within and across sensory modalities. Bifactor statistical indices were used to both evaluate the strength of a “general response pattern” factor for each supra-modal construct and determine the added value of “modality-specific response pattern” scores (e.g., Visual HYPER). Bayesian random-effects integrative data analysis models were used to examine the clinical and demographic correlates of all interpretable HYPER, HYPO and SEEK (sub)constructs. Results All modality-specific HYPER subconstructs could be reliably and validly measured, whereas certain modality-specific HYPO and SEEK subconstructs were psychometrically inadequate when measured using existing items. Bifactor analyses unambiguously supported the validity of a supra-modal HYPER construct (ω H = .800), whereas a coherent supra-modal HYPO construct was not supported (ω H = .611), and supra-modal SEEK models suggested a more limited version of the construct that excluded some sensory modalities (ω H = .799; 4/7 modalities). Within each sensory construct, modality-specific subscales demonstrated substantial added value beyond the supra-modal score. Meta-analytic correlations varied by construct, although sensory features tended to correlate most strongly with other domains of core autism features and co-occurring psychiatric symptoms. Certain subconstructs within the HYPO and SEEK domains were also associated with lower adaptive behavior scores. Limitations: Conclusions may not be generalizable beyond the specific pool of items used in the current study, which was limited to parent-report of observable behaviors and excluded multisensory items that reflect many “real-world” sensory experiences. Conclusion Psychometric issues may limit the degree to which some measures of supra-modal HYPO/SEEK can be interpreted. Depending on the research question at hand, modality-specific response pattern scores may represent a valid alternative method of characterizing sensory reactivity in autism.

**Решение:** -7 peer review report / decision letter

---

### 56 · R0329

**Standardizing an Audio-Visual Database of Misophonic Triggers**

2025 · Furman University Scholar Exchange

Misophonia is a disorder of decreased tolerance to specific sounds or their associated stimuli. These sounds (e.g., chewing or scratching), also known as misophonic triggers, cause emotional distress, such as extreme irritation, anger, disgust, or anxiety to people with this condition. To study the mechanism underlying misophonic responses, specific trigger stimuli is required to evoke responses/reactions from participants in lab environments; however, with such high diversity in trigger categories/sources and the time-consuming nature of data organization, few attempts have been made at making a trigger database. Furthermore, past literature mainly focused on studying the acoustic aspect of misophonia, disregarding the visual association component of triggers. Our lab aims to create a public audio-visual database with diverse triggers. We are developing this goal by standardizing the video files and altering their viability and physical properties. One must understand what is happening in the video, and the trigger in the video must potentially provoke someone with misophonia. Our audio-visual database of triggers will aid researchers studying misophonia and help those with misophonia looking to discover more about their triggers

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 57 · R1462

**Proposed diagnostic criteria for misophonia.**

2013 · https://doi.org/10.1371/journal.pone.0054706.t002

Proposed diagnostic criteria for misophonia.</p

**Решение:** -1 обзор литературы / концептуальная статья

---

### 58 · R0542

**Internet-based, parent-led cognitive behavioral therapy for autistic youth with anxiety-related disorders: A randomized trial comparing email vs. telehealth support.**

2024 · Behaviour research and therapy · journal article, randomized controlled trial, comparative study · eng · https://doi.org/10.1016/j.brat.2024.104639

This study tested two versions of parent-led, Internet-delivered cognitive behavioral therapy for anxiety among autistic youth; one that provided weekly email support (iCBT-Email), and one that provided alternating bi-weekly emails and video calls (iCBT-Video) across 12 weeks. It was expected that those in the iCBT-Video condition would complete more treatment content, which in turn would lead to more anxiety improvement. Fifty-seven autistic youth (7-15 years-old) with anxiety disorders were randomized to iCBT-Email or iCBT-Video. There were no significant differences in improvement in clinician-rated, child-reported, or parent-reported anxiety severity or functional impairment. Posttreatment response rates were 55% in iCBT-Email and 67% in iCBT-Video. Module completion predicted improved treatment outcome, though there was no difference in module completion across groups. Therapists spent an average of 16.29 min/family/week (SD = 7.11) in the iCBT-Email condition and 24.13 min/family/week (SD = 6.84) in the iCBT-Video condition. Email and telehealth-supported, parent-led iCBT both appear to be effective treatments for autistic youth with anxiety disorders that require reduced therapist effort. Future research should seek novel methods to enhance engagement with iCBT content. CLINICALTRIALS.GOV IDENTIFIER: NCT05284435.

**Решение:** -6 не про мизофонию

---

### 59 · R0504

**Acceptance and commitment therapy versus progressive relaxation training for misophonia: Randomized controlled trial protocol, interventions, and audiological assessments.**

2024 · Contemporary clinical trials · article, clinical trial protocol, journal article · eng · https://doi.org/10.1016/j.cct.2024.107671

Background Misophonia is a disorder characterized by an intense emotional reaction to specific sounds, often leading to significant distress and impairment in daily functioning. Acceptance and commitment therapy (ACT) is a promising psychotherapy for treating misophonia, but has only been previously tested in case studies. This paper presents a protocol for the first randomized controlled trial (RCT) assessing the efficacy and feasibility of ACT supplemented by audiological interventions for misophonia versus progressive relaxation training (PRT). Methods The outlined protocol is a RCT with 60 adults with misophonia. After undergoing a comprehensive psychological and audiological evaluation, participants were randomly assigned to ACT (n = 30) or PRT (n = 30). All participants completed clinician-administered and self-report assessments at baseline, post-intervention, 3-month follow-up, and 6-month follow-up. The primary outcome was misophonia severity and impairment measured via clinical interview. Secondary outcomes included disgust, anger, sensory sensitivities, well-being, distress, and psychological flexibility. Discussion This paper outlines the rationale of using ACT supplemented by audiological methods for misophonia with the novel therapeutic target of enhancing psychological flexibility. The results of this randomized controlled trial will help determine if ACT is an efficacious and acceptable treatment for misophonia. This trial will also help clarify active psychological mechanisms of misophonia, and assess whether this combination of psychological and audiological services can effectively help individuals with misophonia.

**Решение:** -7 protocol / preregistration without data

---

### 60 · R1057

**I Hear You: The Everyday Struggle Living with Misophonia**

2021 · TopSCHOLAR® · en · https://core.ac.uk/download/426716972.pdf

The term misophonia is derivated from the Greek words misos, (hate), and phónè, (voice); it translates as hatred of sound. It is the term used to describe people who are irregularly affected by everyday noises. The first scientific observations by Pawel J. Jastreboff regarding misophonia indicate “individuals with misophonia are sensitive to a specific set of trigger sounds, which are usually recognized since childhood.” These types of sounds tend to be trivial noises, such as chewing or crunching, sniffing, breathing, clicking, lip smacking, and tapping. The noises can trigger an onslaught of negative emotions and violent reactions. This documentary film focuses on exposing the public to a disorder with few comprehensive studies. Interviews conducted with both medical professionals and sufferers of misophonia work together to create a depiction of how the disorder affects all people and why others should be considerate of those impacted by the disorder. The documentary delves into the stressful, emotional, human aspect of misophonia in a way that a scientific journal cannot provide. The intention of this study is to form a connection between the subject and the viewer the a will invoke a stronger desire to understand why this disorder is so difficult to live with

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 61 · R0808

**Community-guided, autism-adapted group cognitive behavioral therapy for depression in autistic youth (CBT-DAY): Preliminary feasibility, acceptability, and efficacy**

2023 · Autism · article, other literature type · und · https://doi.org/10.1177/13623613231213543

This study examined the preliminary feasibility, acceptability, and efficacy of an autism-adapted cognitive behavioral therapy for depression in autistic youth, CBT-DAY. Twenty-four autistic youth (11–17 years old) participated in the pilot non-randomized trial including 5 cisgender females, 14 cisgender males, and 5 non-binary youth. Youth participated in 12 weeks of, CBT-DAY and youth depressive symptoms (i.e., primary clinical outcome) and emotional reactivity and self-esteem (i.e., intervention mechanisms) were assessed through self-report and caregiver report at four timepoints: baseline (week 0), midpoint (week 6), post-treatment (week 12), and follow-up (week 24). Results suggested that CBT-DAY may be feasible (16.67% attrition) in an outpatient setting and acceptable to adolescents and their caregivers. Bayesian linear mixed-effects models showed that CBT-DAY may be efficacious in targeting emotional reactivity [β T1-T3 = −2.53, CrI 95% (−4.62, −0.58), P d = 0.995, d = −0.35] and self-esteem [β T1-T3 = −3.57, CrI 95% (−5.17, −2.00), P d &gt; 0.999, d = −0.47], as well as youth depressive symptom severity [β = −2.72, CrI 95% (−3.85, −1.63), P d &gt; 0.999]. Treatment gains were maintained at follow-up. A cognitive behavioral group therapy designed for and with autistic people demonstrates promise in targeting emotional reactivity and self-esteem to improve depressive symptom severity in youth. Findings can be leveraged to implement larger, more controlled trials of CBT-DAY. The trial was registered at Clinicaltrials.gov (Identifier: NCT05430022; https://beta.clinicaltrials.gov/study/NCT05430022 ). Lay Abstract Depression in youth is a significant public health problem worldwide, particularly for autistic youth who are over twice as likely to experience depression than their non-autistic peers. Although pathways to depression are complex, emotional reactivity and negative self-esteem are two risk factors for depression in autistic and non-autistic youth. Although autistic youth are more likely to experience depression than their non-autistic peers, psychotherapy options for autistic youth are very limited; community guidance in the development and testing of psychotherapy programs is a promising approach in autism. Therefore, in this study, we designed an autism-adapted CBT-DAY, in collaboration with autistic community members. Specifically, CBT-DAY combined neurodiversity-affirming and cognitive behavioral approaches to target emotional reactivity and self-esteem in youth to improve depressive symptom severity in a group setting across 12 weeks. We examined the preliminary feasibility, acceptability, and efficacy of CBT-DAY in a pilot non-randomized trial. In addition, we implemented a rigorous protocol for assessing, monitoring, and addressing potential harms in this intervention. Results from 24 autistic youth (11–17 years old) suggest that CBT-DAY may be feasible to use in an outpatient clinical setting and generally acceptable to youth and their caregivers. Participation in CBT-DAY may be associated with significant improvements in youth emotional reactivity and self-esteem, as well as depressive symptom severity per self-report only. Exploratory analyses showed that participation in CBT-DAY may also be associated with significant improvements in internalizing symptoms. Findings demonstrate the potential promise of neurodiversity-affirming and cognitive behavioral approaches to treating depressive symptoms in some autistic youth.

**Решение:** -6 не про мизофонию

---

### 62 · R0732

**Session-by-session change in misophonia: a descriptive case study using intensive CBT.**

2023 · Cognitive behaviour therapist · article, journal article, journalarticle · eng · https://doi.org/10.1017/s1754470x23000107

Abstract There is preliminary evidence that CBT may be helpful for improving symptoms of misophonia, but the key mechanisms of change are not yet known for this disorder of decreased tolerance to everyday sounds. This detailed case study aimed to describe the delivery of intensive, formulation-driven CBT for an individual with misophonia and report on session-by-session outcomes using a multi-dimensional measurement tool (SFive). The patient was offered 12 hours of treatment over five sessions, using transdiagnostic and misophonia-specific interventions. Reliable and clinically significant change was found from baseline to one-month follow-up. Visual inspection of outcome graphs indicated that change occurred on the ‘outbursts’ and ‘internalising appraisals’ SFive subscales following assessment, and on the ‘emotional threat’ subscale after the first treatment session. The other two subscales started and remained below a clinically significant level. The biggest symptom change appeared to have occurred after the second session, which included interventions engaging with trigger sounds. The results demonstrated the individualised nature of misophonia, supporting the use of individually tailored treatment for misophonia and highlighting the importance of using a multi-dimensional measurement tool. Key learning aims (1) To understand misophonic distress from a CBT perspective. (2) To learn a formulation-driven approach to misophonia. (3) To apply transdiagnostic interventions to misophonia. (4) To learn about misophonia-specific interventions. (5) To consider the value of a multi-dimensional measure of misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 63 · R0913

**INSIDE OUT - a visualisation of the emotional world of Borderline Personality Disorder as inspiration for a fashion collection**

2022 · thesis

The following paper deals with the topic of borderline personality disorder and its emotional world in connection with art. The terms of Personality, Personality Disorder and Borderline Personality Disorder are defined, and the different criteria and emotional states of BPD are analysed and presented with the help of personal experience and perspective. Furthermore, this thesis deals with the question of how emotions can be visualised in art. Therefore, art therapy is introduced to examine to which extent art and therapy are interrelated and mutually supportive. A concrete example of emotional expression in art is given with the artist Jesse Draxler who expresses misophonia in his works. A second example is furthermore specified by the personal processing of emotions in art in addition to abstract, expressionistic works of art created by the author. The thesis then focuses on the personal experience of BPD and explains in detail what BPD can feel like to a person affected by it. Concrete examples are given to broaden the understanding. The aim of this thesis is to visualise the emotional states of BPD by means of a clothing collection to find out if the process of visualisation and expression can benefit a mentally ill person. The design process is based on the previously elaborated criteria and characteristics of BPD and visualisations are supported by abstract expressionist paintings made by the author. A complete collection concept including colour scheme and materials used, outfit designs in the form of sketches and technical drawings as well as any other design element will be developed within this paper

**Решение:** -1 обзор литературы / концептуальная статья

---

### 64 · R1229

**Two Studies of Autonomous Sensory Meridian Response (ASMR): The Relationship between ASMR and Music-Induced Frisson**

2019 · Empirical Musicology Review · article · en · https://doi.org/10.18061/emr.v13i1-2.6012

In recent years, a widely popular phenomenon has emerged as exemplified in thousands of videos available on the Internet. Referred to using the impressive sounding term "Autonomous Sensory Meridian Response" (abbreviated ASMR), followers claim that ASMR videos evoke a special "tingling" sensation that is regarded as highly pleasurable and relaxing. The popularity of this phenomenon is reflected in individual ASMR videos receiving more than 43 million views and a reddit ASMR forum with over 130,000 subscribers. Two exploratory studies are reported. In the first study, a content analysis was carried out on 30 popular ASMR videos, and compared with 30 videos employing two different control methods. In the second study, a content analysis was carried out on 3,600 comments on discussion forums and accompanying ASMR videos. The results indicate that ASMR videos typically employ a quiet, private scene, with a relaxed, friendly, and intimate actor ("ASMRtist"). Although ASMR is evoked by non-musical stimuli, the physiological responses to ASMR (skin-related tingling and goosebumps) strongly resemble the classic frisson experience—a phenomenon that has received considerable attention among music perception researchers. Careful consideration of ASMR stimuli and responses suggest that ASMR is consistent with Huron's (2006) theory of frisson.

**Решение:** -6 не про мизофонию

---

### 65 · R1386

**Revista de Ciências Médicas e Biológicas**

2016 · Brasil

Introdução: a misofonia é uma condição crônica caracterizada por experiências emocionais desagradáveis em resposta a sons específicos. Existem poucos estudos que podem contribuir para o desenvolvimento de um modelo teórico para entender a misofonia e os fenômenos relativos a ela, bem como o seu tratamento. Objetivo: revisar a literatura sobre a misofonia e suas implicações, diagnóstico e possíveis tratamentos, numa perspectiva atual. Metodologia: foi realizada uma busca na literatura nas principais bases de dados online, utilizando o termo misofonia. Após análise dos resumos, 13 artigos foram selecionados para análise detalhada. Resultados: pouco ainda se sabe sobre os aspectos fisiopatológicos da misofonia e acredita-se que há um envolvimento dos sistemas límbico e autonômico na severidade das respostas aos chamados sons gatilhos. Os principais sons que desencadeiam respostas de aversão no indivíduo misofônico envolvem mastigação, respiração e outros sons de padrão repetitivo. Não há um consenso no melhor método diagnóstico desta condição e o tratamento também não segue uma padronização, podendo envolver terapia de habituação ao som, terapia cognitivo comportamental e utilização de medicamentos. Conclusão: a misofonia é uma condição que se mostra cada vez mais comum e que pode afetar muito a vida do indivíduo que a possui. No entanto, o entendimento sobre o mecanismo neurobiológico, os aspectos fisiopatológicos, a caracterização clínica, o diagnóstico e tratamento desse fenômeno ainda é evasivo.Salvado

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 66 · R1401

**Pump up the volume: could excessive neural gain explain tinnitus and hyperacusis?**

2015 · Audiology & neuro-otology · article, journal article, review · eng · https://doi.org/10.1159/000430459

Naturally occurring stimuli can vary over several orders of magnitude and may exceed the dynamic range of sensory neurons. As a result, sensory systems adapt their sensitivity by changing their responsiveness or 'gain'. While many peripheral adaptation processes are rapid, slow adaptation processes have been observed in response to sensory deprivation or elevated stimulation. This adaptation process alters neural gain in order to adjust the basic operating point of sensory processing. In the auditory system, abnormally high neural gain may result in higher spontaneous and/or stimulus-evoked neural firing rates, and this may have the unintended consequence of presenting as tinnitus and/or sound intolerance, respectively. Therefore, a better understanding of neural gain, in health and disease, may lead to more effective treatments for these aberrant auditory perceptions. This review provides a concise summary of (i) evidence for changes in neural gain in the auditory system of animals, (ii) physiological and perceptual changes in adult human listeners following an acute period of enhanced acoustic stimulation and/or deprivation, (iii) physiological evidence of excessive neural gain in tinnitus and hyperacusis patients, and (iv) the relevance of neural gain in the clinical treatment of tinnitus and hyperacusis.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 67 · R0275

**Investigating the familiality of trichotillomania and excoriation disorder.**

2025 · Psychiatry research · journal article, research support, n.i.h., extramural, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.psychres.2025.116560

Trichotillomania (TTM) and excoriation disorder (ED) run in families and are thought to have shared etiological underpinnings. Only a few small studies have compared the family history of individuals with TTM, ED, and both conditions. To better understand shared predispositions, we examined self-reported family history of mental health disorders using cross-sectional survey responses from a genetics study of probands ages 4-66 years with TTM only (n = 69), ED only (n = 34), and both conditions (n = 70). Individuals with TTM only reported higher rates of having a first-degree relative with TTM (25 %, 17/69) compared to individuals with ED only (6 %, 2/34) (p = 0.03). Those with ED only reported higher rates of a first-degree relative with ED (41 %, 14/34) compared to individuals with TTM only (13 %, 9/69) (p = 0.002). Individuals with both conditions reported high rates of first-degree relatives with TTM (21 %, 15/70) and ED (39 %, 27/70). All three groups reported high rates of family history of anxiety (48 %-59 %), depression (41 %-49 %), ADHD (23 %-31 %), and OCD (17 %-18 %). Comparing mental health history in parents, there were no significant differences between the parents for TTM or ED, but mothers had higher rates than fathers of anxiety (42 % maternal vs. 18 % paternal) and depression (34 % maternal vs. 14 % paternal) (p-values < 0.001). Our results provide evidence of both shared and distinct predispositions between TTM and ED, highlighting the need for further research on genetic and environmental factors contributing to these conditions.

**Решение:** -6 не про мизофонию

---

### 68 · R1072

**Misophonia in the workplace**

2021 · Medien- und Informationszentrum, Leuphana Universität Lüneburg · master thesis, text/masterthesis · en · https://doi.org/10.48548/pubdata-887

This paper uses the UN’s Sustainable Development Goals’ inclusion of human well-being and disability rights as a base to examine the work experiences of individuals with the syndrome misophonia who have been employed in white-collar office jobs in the Global North, and how these experiences fit into the current discourse on making offices more inclusive and sustainable. It reports on common workplace triggers, coping mechanisms, and the condition’s perceived effects on misophonics, as well as the perceived barriers and carriers to making workplaces more accommodating to those with the condition. A mixed-methods approach was used to address these points. First, a survey was distributed virtually and 203 responses from misophonics who work(ed) in white-collar office jobs in the study region were collected. Next, ten of these survey takers participated in semi-structured, one-on-one interviews, which were then analyzed using qualitative text analysis. The results showed that many misophonics frequently encounter intense triggers (such as mouth sounds) at the office and that self-perceived levels of productivity, well-being, and workplace sociability can be adversely affected. Though opinions on bans of certain behaviors and items and on certain terminology were diverse, there was consensus on desiring more flexible policies, understanding from others, and quiet or private working spaces, including working from home. Lack of misophonia awareness within the general populace, human resources (HR), upper management, and to some degree, the medical community was identified as a persistent barrier to misophonic employees disclosing or asking for reasonable accommodations even when they felt their misophonia was severe, negatively affected them, and there were provisions that could support them. These experiences were similar to those of other invisible conditions and pointed to the need for workplaces striving to be more sustainable and inclusive to adapt their policies and office design decisions.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 69 · R0419

**Misophonia as a New Obsessive-compulsive Related Disorder?**

2025 · Routledge eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.4324/9781003517429-12

Misophonia is characterized by decreased tolerance and intense adverse reactions to particular ordinary and repetitive sounds. Misophonia often onsets during childhood or adolescence and is associated with substantial impairment and distress in many areas of life, including difficulty in social and familial relationships and diminished quality of life. While relatively less studied in youth compared to adults, burgeoning research within misophonia is contributing to advances in classification, assessment, and treatment. However, at present, misophonia does not exist within available diagnostic nosologies, and a consensus has not yet been reached on the formal classification status of the condition. Ascertaining the classification status of misophonia is important, however, as clarity on the essential features of the condition, its etiological nature, and relations between misophonia and other conditions (i.e., conceptual boundaries) will facilitate assessment and intervention development efforts. In the present chapter, we (a) provide an overview of psychological conceptualizations of misophonia; (b) briefly summarize the current state of the misophonia assessment and intervention literature, especially as it relates to children and adolescents; and (c) suggest that the evidence does not indicate misophonia is an OCRD, and instead postulate that a more fruitful path for classification will be to understand misophonia as it relates to transdiagnostic, etiological processes of change, rather than to categories of topographically defined disorders.

**Решение:** -1 глава книги / справочник

---

### 70 · R0675

**Commentary: Consensus definition of misophonia**

2023 · Frontiers in Neuroscience · article, journal article, comment · eng · https://doi.org/10.3389/fnins.2022.1077097

COPYRIGHT © 2023 Aazh. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms. Commentary: Consensus definition of misophonia

**Решение:** -1 обзор литературы / концептуальная статья

---

### 71 · R0139

**Toward a Treatment Algorithm for Misophonia:**

2026 · Translation The University of Toledo Journal of Medical Sciences · article, journalarticle · en · https://doi.org/10.46570/utjms-2026-1680

Translation: The University of Toledo Journal of Medical Sciences is the online journal launched by the University of Toledo. Manuscripts will be considered on the understanding that they report original work and are not under consideration for publication by any other journal. The journal publishes original articles reporting experimental results of basic or clinical research, case reports, and reviews. The journal uses a single blind peer review system and each manuscript, based on the results presented in its original submission, will be evaluated by two student reviewers and one faculty reviewer. This process will provide an opportunity for medical students, graduate students, residents, fellows and faculty to publish research observation in a timely manner.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 72 · R0231

**Physiological Processing of Everyday Aversive Mental Imagery.**

2026 · Psychophysiology · journal article · eng · https://doi.org/10.1111/psyp.70282

Everyday aversive experiences, such as a crying infant or the sound of construction, are not life-threatening, yet they can strongly shape affective experience and physiological state. While most affective imagery research has focused on fear and anxiety, the mechanisms underlying imagery of mild, everyday aversive events remain underexplored. Across five experiments, we systematically investigated behavioral and physiological responses to aversive and appetitive mental imagery. Experiment 1 revealed robust corrugator EMG potentiation but comparatively weaker autonomic responses during aversive imagery compared with audiovisual and auditory stimulation. Experiments 2 and 3 identified key methodological factors that determine imagery potency, including imagery duration, instructional focus, and prompt design. Using an optimized paradigm, Experiment 4 demonstrated coherent changes across subjective valence and arousal ratings, EMG corrugator potentiation, heart rate deceleration, and skin temperature decreases for aversive compared with appetitive imagery, with effects modulated by individual differences in imagery vividness. Experiment 5 confirmed that these effects reflected genuine affective experience rather than semantic knowledge of the prompts. Together, these findings establish baseline physiological and subjective markers of everyday aversive imagery in typical young adults and emphasize the critical role of paradigm optimization in eliciting reliable affective imagery responses. By shifting focus from extreme to everyday aversive experiences, this work provides a framework for studying heightened sensitivity to ordinary stimuli in both basic and clinical contexts.

**Решение:** -6 не про мизофонию

---

### 73 · R1531

**Modification of Loudness Discomfort Level: Evidence for Adaptive Chronic Auditory Gain and Its Clinical Relevance**

2002 · Seminars in Hearing · article · en · https://doi.org/10.1055/s-2002-24973

A vexing problem in audiology has been the modification of sound tolerance. Sound intolerance and restricted dynamic ranges are common conditions that audiologists encounter daily in the hearing-impaired population, especially in the fitting of hearing aids. To date, no clinical protocol has proven to be successful for modifying sound tolerance among the hearing- impaired population. This report describes the use of low-level, broadband sound in a habituation-based treatment protocol termed Tinnitus Retraining Therapy (TRT). Over the past decade, TRT has become increasingly popular as an intervention for severe tinnitus and hyperacusis. One of the primary treatment effects from TRT is that over the course of the intervention the patient's loudness discomfort level (LDL) thresholds routinely shift to higher levels. Ostensibly, the resulting higher LDL thresholds reflect treatment effects associated with the resetting of a plastic and adaptive auditory gain process that somehow regulates the supra-threshold sensitivity of the auditory system in response to chronic changes in the sound input from the auditory periphery to the central auditory pathways. Tinnitus patients with significant hearing losses and sound tolerance problems respond successfully to TRT and, as a consequence, their LDL thresholds are usually elevated (improved) and, concomitantly, their dynamic ranges are expanded. Many of these patients, who before the TRT intervention could not tolerate amplified sound, then have been able to make a comfortable transition into appropriate amplification after treatment. In principle, TRT would seem to offer a viable intervention strategy for modifying sound tolerance in the general hearing-impaired population. If so, then the clinical applications of TRT principles may extend well beyond the treatment of tinnitus and hyperacusis. KEYWORD Sound tolerance - hyperacusis - Tinnitus Retraining Therapy - chronic auditory gain - adaptive plasticity

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 74 · R1271

**Misophonia: a disorder for social world**

2018 · Ankara Medical Journal · article · en · https://doi.org/10.17098/amj.409046

Dear Editor, Chewing, coughing, breathing, typing are activities that produce low level sounds and these audible activities are frequently encountered in the society. These background sounds are usually ignored in public places or at home. Some people may not ignore and perceive these sounds and become disgusted. Reasons of disgust are distraction and anger. Tension might be followed by anger which may then generate urge to leave the environment or intercept the background noise. Sensitivity to the group of background noise is called misophonia. 1-3 The term consists of two words: misos (strong hate or disgust) and phonia (sound) and was introduced by Margaret and Pavel Jastreboff in 2001. 4 It was aimed to present and discuss two cases of misophonia in this letter to the editor. The first case was a young man with generalized anxiety disorder. He was also suffering from misophonia and misophonia triggered anger. He reported that particularly his family life was devastated because of his anger. The second patient was suffering from obsessive compulsive disorder and misophonia. She reported that she was counting to ten, breathing slowly or leaving the environment as soon as possible, if she cannot relax. She was frequently listening music with headphones in public places to avoid from disgusting sounds. Both patients reported that they could not express themselves during their disgust, because of inhibiting themselves due to the fear of being called crazy. Misophonia is defined as immediate negative psychological responses to certain sounds that most people do not notice. 1-3 This novel psychopathology is proposed to be involved with dysregulation of emotional processing with a neurobiological basis. 5 Current classification systems have not defined misophonia yet and it is not clear whether it is a distinct entity or a dimension or symptom domain which accompany other disorders. 3 Post-traumatic stress disorder was the most frequently accompanying disorder in a recent large-scale study. 6 Accordingly, other psychopathologies may trigger or enhance the responses and therefore misophonia might be a dimensional concept. Misophonia may deteriorate quality of life and social functioning and thus should be further investigated. 1-3,5 A Google search with the key words “misophonia treatment” retrieved 217 results in the date of January 12th. 8 of the web pages’ name was including the term “misophonia”. Increased awareness of this problem would be useful in order to develop better treatments. 7,8

**Решение:** -1 обзор литературы / концептуальная статья

---

### 75 · R1117

**RETRACTED ARTICLE: Improving the measurement of alexithymia in autistic adults: a psychometric investigation and refinement of the twenty-item Toronto Alexithymia Scale**

2021 · Molecular Autism · article · eng · https://doi.org/10.1186/s13229-021-00427-9

Abstract Background Alexithymia, a personality trait characterized by difficulties interpreting one’s own emotional states, is commonly elevated in autistic adults, and a growing body of literature suggests that this trait underlies a number of cognitive and emotional differences previously attributed to autism, such as difficulties in facial emotion recognition and reduced empathy. Although questionnaires such as the twenty-item Toronto Alexithymia Scale (TAS-20) are frequently used to measure alexithymia in the autistic population, few studies have attempted to determine the psychometric properties of these questionnaires in autistic adults, including whether differential item functioning (I-DIF) exists between autistic and general population adults. Methods We conducted an in-depth psychometric analysis of the TAS-20 in a large sample of 743 verbal autistic adults recruited from the Simons Foundation SPARK participant pool and 721 general population controls enrolled in a large international psychological study (the Human Penguin Project). The factor structure of the TAS-20 was examined using confirmatory factor analysis, and item response theory was used to further refine the scale based on local model misfit and I-DIF between the groups. Correlations between alexithymia and other clinical outcomes such as autistic traits, anxiety, and quality-of-life were used to assess the nomological validity of the revised alexithymia scale in the SPARK sample. Results The TAS-20 did not exhibit adequate global model fit in either the autistic or general population samples. Empirically driven item reduction was undertaken, resulting in an eight-item unidimensional scale (TAS-8) with sound psychometric properties and practically ignorable I-DIF between diagnostic groups. Correlational analyses indicated that TAS-8 scores meaningfully predict autistic trait levels, anxiety and depression symptoms, and quality of life, even after controlling for trait neuroticism. Limitations Limitations of the current study include a sample of autistic adults that was overwhelmingly female, later-diagnosed, and well-educated; clinical and control groups drawn from different studies with variable measures; and an inability to test several other important psychometric characteristics of the TAS-8, including sensitivity to change and I-DIF across multiple administrations. Conclusions These results indicate the potential of the TAS-8 as a psychometrically robust tool to measure alexithymia in both autistic and non-autistic adults. A free online score calculator has been created to facilitate the use of norm-referenced TAS-8 latent trait scores in research applications (available at http://asdmeasures.shinyapps.io/TAS8_Score ).

**Решение:** -6 не про мизофонию

---

### 76 · R0427

**Longitudinal and cross-sectional predictors of sleep disturbance in a treatment follow-up sample with Tourette's disorder.**

2025 · Frontiers in psychiatry · journal article · eng · https://doi.org/10.3389/fpsyt.2025.1594347

Sleep disturbance is common in individuals with Tourette's disorder (TD). Tic symptoms, medication, functional impairment, and psychiatric comorbidity frequently contribute to sleep disturbance in children and adults with TD. However, long-term predictors of sleep disturbance in TD are not known. This study examined longitudinal and cross-sectional predictors of sleep disturbance in a treatment follow-up sample with TD. Eighty subjects who completed a 10-week randomized controlled trial of behavior therapy for tics in childhood (Mage = 11.47, SD = 2.42 years) participate in follow-up evaluation on average, 11.17 (SD = 1.25) years after post-treatment assessment (Mage = 22.87, SD = 2.70 years). At post-treatment (10-week) and long-term follow-up, an independent evaluator assessed tic severity and tic-related impairment using the Yale Global Tic Severity Scale. Parents provided demographic and medical history (e.g., tic medication and stimulant medication status) and rated ADHD severity. Children rated anxiety and depression. At follow-up, participants rated anxiety, depression, and ADHD severity, and reported tic and stimulant medication status. Multiple linear regression was performed to examine longitudinal and cross-sectional predictors of sleep disturbance (Pittsburgh Sleep Quality Index) at long-term follow-up. tic-related impairment (β = .34, p = .014) at post-treatment positively predicted sleep disturbance at follow-up. Chronological age (β = .21, p = .041), anxiety severity (β = .40, p = .001), and ADHD severity (β = .31, p = .010) were positive cross-sectional predictors of sleep disturbance at follow-up. Results highlight the role of residual tic-related impairment following behavior therapy for tics delivered in childhood in addition to older age, anxiety severity, and ADHD severity in early adulthood in sleep disturbance in a treatment follow-up sample of adults with TD.

**Решение:** -6 не про мизофонию

---

### 77 · R1321

**Audiological assessment of decreased sound tolerance**

2018 · Digital Commons - East Tennessee State University (East Tennessee State University) · article, text · en

Book Summary: Hyperacusis and Disorders of Sound Intolerance: Clinical and Research Perspectives is a professional resource for audiology practitioners involved in the clinical management of patients who suffer from sound tolerance concerns. The text covers emerging assessment and intervention strategies associated with hyperacusis, disorders of pitch perception, and other unusual processing deficits of the auditory system. In order to illustrate the patients perspectives and experiences with disorders of auditory processing, cases are included throughout. This collection of diagnostic strategies and tools, evidence-based clinical research, and case reports provides practitioners with avenues for supporting patient management and coping. It combines new developments in the understanding of auditory mechanisms with the clinical tools developed to manage the effects such disorders exert in daily life. Topics addressed include unusual clinical findings and features that influence a patient s auditory processing such as their perceptual accuracy, recognition abilities, and satisfaction with the perception of sound. Hyperacusis is covered with respect to its effects, its relation to psychological disorders, and its management. Hyperacusis is often linked to trauma or closed head injury and the text also considers the management of patients with traumatic brain injury as an opportunity to illustrate the effectiveness of interprofessional care in such cases. Interventions such as cognitive behavioral therapy, self-efficacy training, and hearing aid use are reported in a way that enhances clinicians\u27 ability to weave such strategies into their own work, or into their referral system. Hyperacusis and Disorders of Sound Intolerance illuminates increasingly observed auditory-related disorders that challenge students, clinicians, physicians, and patients. The text elucidates and reinforces audiologists contributions to polytrauma and interprofessional care teams and provides clear definitions, delineation of mechanisms, and intervention options for auditory disorders

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 78 · R0276

**Misokinesia**

2025 · Springer eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1007/978-3-031-94841-1_106

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глава книги / справочник

---

### 79 · R0227

**Psychological Correlates of Audiological and Self-Report Indicators of Hyperacusis in Adults With Misophonia.**

2026 · American journal of audiology · article, journal article, journalarticle · eng · https://doi.org/10.1044/2025_aja-25-00200

Purpose: Misophonia and hyperacusis are distinct sound sensitivity conditions that can co-occur and are linked to heightened emotional distress and impaired functioning. This study investigated the convergence between audiometric-based and self-reported indicators of hyperacusis and examined how each related to misophonia severity and psychological outcomes in adults with misophonia. Method: Participants ( N = 60) completed self-report measures and underwent loudness discomfort level (LDL) testing. Results: Analyses revealed discrepancies between self-reported and LDL-defined hyperacusis, with no significant associations between LDL-based classifications and psychological or misophonia-related outcomes. In contrast, hyperacusis identified via a standardized self-report measure was significantly associated with heightened emotional and behavioral reactivity in misophonia, as well as greater severity and elevated internalizing symptoms, including depression, anxiety, and stress. Conclusions: Findings raise concerns about the clinical utility of LDLs as standalone indicators in misophonia populations. They highlight the value of subjective assessments for identifying clinically relevant variables associated with hyperacusis and misophonia comorbidity. Our results support that self-report tools may better capture the lived experience and psychological features associated with co-occurring hyperacusis and misophonia. However, until more research is established, we recommend employing audiometric and self-report metrics to assess for hyperacusis in this population. Future research should focus on identifying psychometric measures that can accurately distinguish between the two conditions and on developing standardized protocols for assessing hyperacusis in individuals with misophonia.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 80 · R1541

**[Otorhinolaryngology].**

1961 · Münchener medizinische Wochenschrift · journalarticle · https://pubmed.ncbi.nlm.nih.gov/13700180/

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 81 · R0462

**A comparison of interaural asymmetry, audiogram slope, and psychometric measures of tinnitus, hyperacusis, anxiety and depression for patients with unilateral and bilateral tinnitus.**

2024 · International journal of audiology · journal article, comparative study, research support, non-u.s. gov't · eng · https://doi.org/10.1080/14992027.2022.2160383

To evaluate differences in tinnitus impact, hyperacusis and hearing threshold level (HTL) between patients with unilateral and bilateral tinnitus. For patients with unilateral tinnitus, to compare audiological variables for the tinnitus ear and the non-tinnitus ear. To assess whether the presence of unilateral tinnitus increases the likelihood of interaural hearing asymmetry (relative to bilateral tinnitus) that warrants referral for an MRI scan. Retrospective cross-sectional. Data regarding HTLs and responses to self-report questionnaires were collected from the records of 311 patients attending a tinnitus clinic. 38.5% had unilateral tinnitus and the ears with tinnitus had higher HTLs and greater HTL slopes than the ears without tinnitus. There was no significant difference in tinnitus impact and hyperacusis between patients with unilateral and bilateral tinnitus. 40% of patients with unilateral tinnitus and 13% of patients with bilateral tinnitus had a between-ear difference in HTL ≥15 dB at two adjacent frequencies (2AF15 asymmetry). Unilateral tinnitus increased the risk of 2AF15 asymmetry by a factor of 4.4. Unilateral tinnitus increases the risk of having interaural asymmetry in HTLs that warrants referral for an MRI scan.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 82 · R0619

**Parent and Provider Differences in Ratings of Mental Health and Neurodevelopmental Concerns in Children with Neurologic Disorders**

2024 · Journal of Clinical Psychology in Medical Settings · article · eng · https://doi.org/10.1007/s10880-023-09990-0

Abstract Children with neurologic disorders face increased risks for mental health and neurodevelopmental conditions, with information often limited to parent report. To better understand mental health and neurodevelopmental needs in this population, a retrospective chart review of a convenience sample of children with neurologic disorders referred for a neuropsychological evaluation was conducted in the present study to explore interrater agreement between care team members (referring providers, parents, pediatric neuropsychologist). Qualitative and quantitative data were collected from the evaluation reports of 129 youth (9:0–17:11 years old; 51.2% of female sex) with neurologic disorders (i.e., 38.0% traumatic brain injury, 27.1% epilepsy, 14.7% premature birth, 7.8% pediatric cancer, 3.9% prenatal substance exposure, and 14.7% other) who completed an evaluation in 2019. Over half the youth were flagged for unmet neurodevelopmental and mental health concerns and analyses revealed low interrater agreement for mental health concerns (κ = .324), better agreement for neurodevelopmental concerns (κ = .511), and low sensitivity of referring providers ( Se = .326) and parents ( Se = .366). One-way analyses of variance uncovered important factors (e.g., symptom severity, adaptive skills) that may account for missed concerns. Findings guide recommendations to strengthen methods for understanding mental health and/or neurodevelopmental concerns in children with neurologic disorders.

**Решение:** -6 не про мизофонию

---

### 83 · R0226

**Investigating the Role of Stress in Misophonia: Stress as a Clinical Correlate and Its Influence on Treatment Outcomes.**

2026 · Journal of cognitive psychotherapy · journal article, journalarticle, article · eng · https://doi.org/10.1891/jcp-2026-0015

Misophonia is a sound intolerance disorder characterized by strong emotional and physiological reactions to specific everyday sounds. Emerging research suggests that stress may play an important role in misophonia, yet little work has examined whether stress uniquely contributes to misophonia severity or influences treatment response. The present study examined the role of stress in misophonia using data from a randomized clinical trial of treatment-seeking adults ( N = 60) comparing acceptance and commitment therapy and progressive relaxation training. First, we examined whether stress symptoms were uniquely associated with misophonia severity and impairment at baseline when accounting for anger, disgust propensity and sensitivity, anxiety, depression, obsessive-compulsive symptoms, and demographic variables. Second, we examined whether baseline stress influenced trajectories of change in misophonia outcomes over time and whether these differed across treatment conditions. Results suggested that, at baseline, stress symptoms were the only clinical correlate that uniquely predicted misophonia symptom severity and misophonia-related impairment. Baseline stress was also associated with differences in treatment trajectories, such that individuals reporting lower stress showed greater improvement in misophonia symptoms and impairment by the 6-month follow-up compared with those with higher stress. However, stress did not interact with treatment condition; both treatments performed equally regardless of stress levels. These findings suggest that stress may represent a broader psychological process associated with misophonia severity and the durability of treatment gains.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 84 · R0045

**Identifying the acoustic fingerprints of trigger sounds and predicting discomfort for misophonia.**

2026 · Hearing research · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1016/j.heares.2025.109478

Human hearing is critical to everyday communication and the perception of natural auditory scenes. For individuals with misophonia, sounds commonly experienced in daily life can evoke severe discomfort and distress. Aversion is often described in terms of broad sound categories, such as bodily sounds, but what acoustic features cause specific sounds to be aversive or not, within the same category or across different individuals, remains unclear. Here, we explore whether bottom-up statistical sound features processed in the auditory periphery and midbrain can explain aversion to sounds. Using the Free Open-Access Misophonia Stimuli (FOAMS) dataset and a hierarchical model of the auditory system, we find that sound summary statistics can predict discomfort ratings in participants with misophonia. For each listener, the model produces individualized transfer functions that pinpoint the specific spectrotemporal modulations that contribute towards sound aversion. Overall, the model explains 76% of the variance in discomfort ratings, and we find substantial differences across participants in which sound features drive aversion. A major advantage of the modeling approach here is that it is sound-computable - perceptual ratings can be fit from or predicted for any sound. To illustrate applications of sound-computable models, we consider 1) extrapolation of participants' ratings to a large set of untested environmental sounds and develop 2) personalized trigger detection that uses the listener's acoustic feature preferences to identify potential triggers in continuous audio. Model predictions identify many untested sound categories, not in the original FOAMS set, that may also be aversive and suggest that there may be substantial heterogeneity in how aversive specific sounds are within some sound categories. In continuous audio, we show how sound-computable models can identify the timing of potential triggers from sound mixtures. Altogether, our results suggest that acoustic features - spectrotemporal modulations, in particular - can practically be used to characterize the individualized patterns of aversion in participants with misophonia. Future perceptual studies using synthetic sounds and sound sets with more diverse acoustics will allow model predictions to be tested more broadly; however, sound-computable models may already have applications in precision diagnosis and management of misophonia.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 85 · R0632

**Acceptance and Commitment Therapy for an Emerging Adult Female With Misophonia: A Case Study.**

2024 · Journal of psychiatric practice · article, casereport, journalarticle · eng · https://doi.org/10.1097/pra.0000000000000800

Misophonia is characterized by decreased tolerance to idiosyncratic and repetitive human-generated sounds (ie, triggers), coupled with affective-based reactions that result in impairment and distress. Often having its onset in youth, misophonia can become especially prominent during key developmental periods, including emerging adulthood. While efforts to develop interventions for misophonia remain ongoing, a consensus has not yet been reached concerning recommended first-line treatments. Acceptance and commitment therapy (ACT), which has demonstrated efficacy in treating various psychiatric disorders via targeting psychological flexibility processes, represents one potentially feasible approach for addressing misophonia. This case study describes the application of an individually delivered, 12-session ACT intervention for a black female in her early 20s with misophonia. Descriptive data collected at 4 time points (pretreatment, mid-treatment, posttreatment, and at 2-month follow-up) suggested the potential promise of ACT as a treatment for misophonia, improving psychological flexibility processes and reducing secondary depression and anxiety symptoms. Findings are discussed in the context of the possible mechanisms of ACT most likely responsible for misophonia-related clinical improvement. More rigorous studies (eg, clinical trials) are needed to confirm promising findings from existing case studies.

**Решение:** -2 клинический случай / серия случаев

---

### 86 · R0921

**Synopsis and Qualitative Evaluation of a Treatment Protocol to Guide Systemic Group-Cognitive Behavioral Therapy for Misophonia.**

2022 · Frontiers in psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyt.2022.794343

Misophonia is a disorder in which patients suffer from anger or disgust when confronted with specific sounds such as those associated with eating or breathing, causing avoidance of cue related situations resulting in significant functional impairment. Functional magnetic resonance imaging studies suggest misophonia is associated with increased activity in the auditory cortex and salience network, which might reflect increased vigilance toward specific misophonia triggers. New treatments have been developed and investigated in the last years in which this vigilance plays an important role. This is a synopsis of the first group protocol for systemic Cognitive Behavioral Therapy (G-CBT) for misophonia. We discuss the model of CBT for misophonia, provide a detailed guide to the treatment illustrated with a case study, discuss advantages, limitations, and possible pitfalls by a qualitative evaluation of the protocol, and review evidence for the protocol.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 87 · R0938

**Low-Dose Risperidone for an Autistic Child with Comorbid ARFID and Misophonia.**

2022 · Psychopharmacology bulletin · article, journalarticle, letter · eng · https://doi.org/10.64719/pb.4430

Avoidant/Restrictive Food Intake Disorder and misophonia seem to be overrepresented in autism spectrum disorder. Literature is mute on psychopharmacotherapy in these complex presentations. Here, authors report on a challenging case of low-functioning ASD child with comorbid ARFID and misophonia that responded favorably to a low-dose risperidone. This is followed by a brief discussion of purported pharmacodynamic mechanisms and relevant literature.

**Решение:** -1 редакционная статья / письмо

---

### 88 · R0556

**Measurement Properties of the Patient Health Questionnaire–15 and Somatic Symptom Scale–8**

2024 · JAMA Network Open · article · en · https://doi.org/10.1001/jamanetworkopen.2024.46603

Importance: The subjective experience of somatic symptoms is a key concern throughout the health care system. Valid and clinically useful instruments are needed. Objective: To evaluate the measurement properties of 2 widespread patient-reported outcomes: the Patient Health Questionnaire-15 (PHQ-15) and Somatic Symptom Scale-8 (SSS-8). Data Sources: Medline, PsycINFO, and Web of Science were last searched February 1, 2024. Study Selection: English-language studies reporting estimates pertaining to factor analysis, taxometric analysis, internal consistency, construct validity, mean scores in relevant groups, cutoffs, areas under the receiver operating characteristic curves (AUROCs), minimal clinically important difference, test-retest reliability, or sensitivity to change. Data Extraction and Synthesis: Search hits were reviewed by independent raters. Cronbach α, Pearson r, means, and between-group effect sizes indicative of sensitivity to change were pooled in random-effects meta-analysis. Study quality was assessed using 3 instruments. Reporting followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 reporting guideline. Main Outcomes and Measures: Comprehensive overview of evidence pertaining to the measurement properties of the PHQ-15 and SSS-8. Results: A total of 305 studies with 361 243 participants were included. Most concerned routine care (178 studies) and the general population (27 studies). In factor analyses, both scales reflected a combination of domain-specific factors (cardiopulmonary, fatigue, gastrointestinal, pain) and a general symptom burden factor. The pooled PHQ-15 α was 0.81 (95% CI, 0.80-0.82), but with low item-total correlations for items concerning menstrual problems, fainting spells, and sexual problems (item-total correlations <0.40), and the SSS-8 α was 0.80 (0.77-0.83). Pooled correlations with other measures of somatic symptom burden were 0.71 (95% CI, 0.64-0.78) for the PHQ-15 and 0.82 (95% CI, 0.72-0.92) for the SSS-8. Reported AUROCs for identification of somatoform disorders ranged from 0.63 (95% CI, 0.50-0.76) to 0.79 (95% CI, 0.73-0.85) for the PHQ-15 and from 0.71 (95% CI, 0.66-0.77) to 0.73 (95% CI, 0.69-0.76) for the SSS-8. The minimal clinically important difference on both scales was 3 points. Test-retest reliability could not be pooled and was inconsistent for the PHQ-15 (PHQ-15: r = 0.65-0.93; ICC, 0.87; SSS-8: r = 0.996, ICC = 0.89). The PHQ-15 showed tentative sensitivity to change (g = 0.32; 95% CI, 0.08-0.56), but data for the SSS-8 were lacking. Conclusions and Relevance: In this systematic review and meta-analysis, findings supported use of the PHQ-15 and SSS-8 for the assessment of symptom burden, but users should be aware of the complex, multifactorial structures of these scales. More evidence is needed concerning longitudinal measurement properties.

**Решение:** -6 не про мизофонию

---

### 89 · R1196

**Misophonia: An Evidence-Based Case Report.**

2020 · American journal of audiology · article, case reports, journal article · eng · https://doi.org/10.1044/2020_aja-19-00111

Purpose Misophonia is a sound tolerance disorder condition in certain sounds that trigger intense emotional or physiological responses. While some persons may experience misophonia, a few patients suffer from misophonia. However, there is a dearth of literature on audiological assessment and management of persons with misophonia. The purpose of this report is to discuss the assessment of misophonia and highlight the management option that helped a patient with misophonia. Method A case study of a 26-year-old woman with the complaint of decreased tolerance to specific sounds affecting quality of life is reported. Audiological assessment differentiated misophonia from hyperacusis. Management included retraining counseling as well as desensitization and habituation therapy based on the principles described by P. J. Jastreboff and Jastreboff (2014). A misophonia questionnaire was administered at regular intervals to monitor the effectiveness of therapy. Results A detailed case history and audiological evaluations including pure-tone audiogram and Johnson Hyperacusis Index revealed the presence of misophonia. The patient benefitted from intervention, and the scores of the misophonia questionnaire indicated a decrease in the severity of the problem. Conclusions It is important to differentially diagnose misophonia and hyperacusis in persons with sound tolerance disorders. Retraining counseling as well as desensitization and habituation therapy can help patients who suffer from misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 90 · R0160

**Bilateral transcutaneous auricular vagus nerve stimulation for misophonia symptoms: a case report and review of the literature.**

2026 · Frontiers in psychology · article, case reports, journal article · eng · https://doi.org/10.3389/fpsyg.2026.1903444

Misophonia is characterized by a markedly decreased tolerance to specific sounds, often accompanied by intense emotional, behavioral and autonomic responses. Current treatment evidence remains limited, and neuromodulation-based approaches targeting autonomic dysregulation are largely unexplored. This case report describes a 64-year-old woman with severe misophonic symptoms, whose main trigger was the rhythmic thudding sound of a basketball being bounced nearby. Exposure to this sound elicited intense distress, palpitations, choking sensation, dyspnea, acute anxiety, terror and an overwhelming urge to escape, leading to avoidance and functional impairment. The patient was receiving stable sertraline treatment and underwent a 1-month protocol of bilateral transcutaneous auricular vagus nerve stimulation, delivered daily for 60 min at an individually adjusted, non-painful intensity. Misophonia severity, psychological distress, anxiety, depressive symptoms, sleep, circadian rhythm and mood-related symptoms were assessed at baseline, after treatment and at 1-month follow-up. The Duke Misophonia Questionnaire Symptoms Composite Scale decreased from 80 at baseline to 9 after treatment and 5 at follow-up, indicating sustained reduction in symptom severity. Overall psychological distress, somatization, anxiety, hostility and depressive symptoms also improved. Sleep quality improved after treatment but returned to baseline at follow-up. Conversely, functional impairment decreased immediately after treatment but increased at follow-up, suggesting a dissociation between symptom reduction and perceived functional recovery. This case suggests that bilateral transcutaneous auricular vagus nerve stimulation may be a feasible adjunctive intervention for misophonia characterized by prominent autonomic hyperarousal. Findings are preliminary and hypothesis-generating and controlled studies are needed to clarify its therapeutic role.</jats:p

**Решение:** -2 клинический случай / серия случаев

---

### 91 · R0914

**Misofonia: definizione, eziologia e sintomi. Una revisione sistematica della letteratura secondo il metodo prisma**

2022 · Cognitivismo clinico · article · ita · https://doi.org/10.36131/cogncl20220101

La misofonia è una condizione di ridotta tolleranza a specifici suoni o stimoli ad essi associati, caratterizzata da un’intensa attivazione neurofisiologica. I sintomi generali includono un’elevata sensibilità a rumori quotidiani come tossire, annusare e masticare, che si traduce in una forte reazione emotiva a cui seguono comportamenti di evitamento, allontanamento e, in alcuni casi, risposte aggressive. Seguono emozioni di rabbia, disgusto, ansia e depressione (Swedo et al., 2022). Nonostante il crescente interesse per questo fenomeno, attualmente non esiste una classificazione diagnostica. Lo scopo del presente lavoro consiste nel fornire un quadro aggiornato della letteratura sulla definizione e sull’eziologia della misofonia, con particolare enfasi sulla sintomatologia e sui correlati psicologici e comportamentali. I dati presenti in letteratura sono stati raccolti e analizzati secondo le linee guida del metodo PRISMA (Moher et al., 2009). La revisione è stata condotta attraverso i principali motori di ricerca su lavori scientifici pubblicati tra il 2010 e il 2022, in lingua inglese. In definitiva, è stato incluso un totale di 40 articoli. Dalla ricerca è emerso che la misofonia potrebbe essere classificata come un disturbo psicologico discreto, poiché i sintomi si presentano secondo un modello stabile e coerente, e i pazienti riferiscono percorsi di sviluppo simili (Schroder et al., 2013; Jager et al., 2020). L’intensità della reazione del paziente non è determinata tanto dalle caratteristiche fisiche del suono trigger, quanto dal suo profilo psicologico, dal contesto e dalle interpretazioni cognitive che l’individuo fa circa la fonte specifica dei suoni, che influenzano l’intensità e l’incontrollabilità delle sue reazioni (Brout et al., 2018). Una difficoltà nella regolazione delle emozioni e la presenza di labilità affettiva, aggrava la severità dei sintomi e può compromettere a lungo andare il funzionamento lavorativo, scolastico e sociale del soggetto (Guetta et al., 2022). L’eziologia della misofonia si può far risalire sia a fattori ereditari, sia a cause ambientali, come ad esempio meccanismi di apprendimento associativo. Inoltre, si pensa che la misofonia sia correlata ad alti livelli di connessione tra sistema uditivo, autonomo e limbico e che, in particolare, sarebbe l’AIC a svolgere un ruolo importante nell’eziologia del fenomeno (Edelstein et al., 2013). Sarebbe auspicabile ampliare la ricerca al fine di avere maggiore chiarezza sul fenomeno e sui possibili trattamenti utili alla riduzione del disagio e al miglioramento della qualità di vita dei soggetti. Parole chiave: misofonia, definizione, eziologia, emozioni, sintomi

**Решение:** -1 обзор / комментарий / письмо

---

### 92 · R1400

**A young woman with noise intoleranceommentary by**

2015 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 93 · R1342

**Darum machen manche Geräusche wütend**

2017 · Sprache · Stimme · Gehör · article · de · https://doi.org/10.1055/s-0043-108831

Menschen mit Misophonie reagieren sehr wütend oder aggressiv auf bestimmte Geräusche. Britische Forscher fanden jetzt heraus, warum dies so ist. Sie spielten Personen mit und ohne Misophonie diverse Geräusche vor. MRT-Gehirn-Scans ergaben, dass beide Gruppen ähnlich auf neutrale und aufreibende Geräusche (z. B. Regen bzw. das Schreien eines Kleinkindes) reagierten. Bei sogenannten Triggern (essen, atmen, trinken) jedoch zeigten Misophoniker überdurchschnittlich hohe Aktivität im vorderen Inselkortex – einer Gehirnstruktur, die in die emotionale Verarbeitung involviert ist. Zudem ging die Inselrinde unüblich viele Verbindungen mit anderen Gehirnbereichen ein. Mirka Homrich

**Решение:** -1 обзор литературы / концептуальная статья

---

### 94 · R1451

**Tinnitus, Hyperacusis, and Misophonia Toolbox**

2014 · Seminars in Hearing · article, review · en · https://doi.org/10.1055/s-0034-1372528

The management of tinnitus, hyperacusis, and misophonia can be a challenge to the audiologist, physician, and psychologist, as well as the patient and their family. Assisting the patient in identifying cognitive distortions or misperceptions can aid in the transition from one who suffers from these conditions to one who is able to manage them. Although there is no cure, it is inappropriate to tell patients that nothing can be done. The audiologist can help the patient learn techniques to lower the emotional impact of tinnitus. For those with an interest in tinnitus and sound sensitivity management, many tools are available. Most importantly, knowing when to refer is paramount. Compiling a referral list of medical and allied health providers, as well as audiologists who specialize in tinnitus, hyperacusis, and misophonia management, is in the best interest of the patient. Being familiar with the ever increasing list of available products and devices is necessary to build the tinnitus toolbox. This article will review current treatments, trends, and tools that may assist in patient education and tinnitus habituation. Some attention also will be paid to other sound sensitivities such as hyperacusis and misophonia.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 95 · R1362

**Commentary: The Brain Basis for Misophonia**

2017 · Frontiers in Behavioral Neuroscience · article, journal article, comment · eng · https://doi.org/10.3389/fnbeh.2017.00111

GENERAL COMMENTARY article Front. Behav. Neurosci., 02 June 2017Sec. Pathological Conditions Volume 11 - 2017 | https://doi.org/10.3389/fnbeh.2017.00111

**Решение:** -1 обзор литературы / концептуальная статья

---

### 96 · R1307

**Recognizing and Reacting to Risk Signs for Patient Suicide**

2018 · Seminars in Hearing · article · en · https://doi.org/10.1055/s-0037-1613708

Evidence-based suggestions for developing an effective clinician-client relationship built upon trust and honesty will be shared, as well as a review of relevant scope of practice issues for audiologists. Audiologists need to be prepared if a patient threatens self-harm. Many patients do not spontaneously report their suicidal thoughts and intentions to their care providers, so we need to be alert to warning signs. Information about the strongest predictors of suicide, how to ask about suicidal intentions, and how to assess the risk of suicide will be presented. Although it is our responsibility to recognize suicidal tendencies and have a plan for preventive intervention, it is not our responsibility to conduct a suicide evaluation. Tips for collecting critical information to be provided to qualified professionals will be shared, as well as additional information about how and to whom to disclose this information. A list of suicide warning signs will be reviewed as well as some additional suggestions for how to react when a patient discloses his or her suicidal intent. A review of available resources (for both the patient and the clinician) will be provided, along with instructions for how and when it is appropriate to access them.

**Решение:** -6 не про мизофонию

---

### 97 · R1433

**The gamma-interferon (IFN-γ) gene +874 T>A polymorphism is not associated with personality traits in healthy Japanese subjects**

2015 · Brain Behavior and Immunity · article · en · https://doi.org/10.1016/j.bbi.2015.08.018

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 98 · R0992

**MDMA for the treatment of misophonia, a proposal.**

2022 · Frontiers in psychiatry · article, review, systematic review · eng · https://doi.org/10.3389/fpsyt.2022.983285

Misophonia is a disorder characterized by negative physical and emotional reactions to certain trigger sounds, such as chewing food. Up to 50% of population samples endorse some symptoms of misophonia, with about 20% having symptoms that impair normal life functioning. Most misophonia patients exhibit intense negative emotions and autonomic arousal (the fight-flight-freeze response) in response to a trigger, similarly to how someone with post-traumatic stress disorder (PTSD) might respond to a trauma trigger. Curiously, misophonia trigger sounds are often most distressing when coming from a specific person, suggesting the disorder may be responsive to interpersonal relationship factors. Treatment of misophonia is currently limited to the use of hearing modifications (e.g., earplugs or headphones) and psychotherapy, but many patients continue to suffer despite these best efforts. Phase 3 clinical trials suggest that MDMA is efficacious at treating the symptoms of autonomic arousal, negative emotions, and interpersonal suffering found in PTSD. As such, we propose that MDMA may represent an ideal treatment for some suffering from severe misophonia. In this perspective article, we review the symptoms of misophonia, and outline how MDMA may be uniquely suited for treating it, perhaps using a protocol analogous to the MAPS Phase 3 studies for PTSD.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 99 · R1539

**The rationale and methods for combatting hypercapnia in cor pulmonale**

1965 · American Heart Journal · article · en · https://doi.org/10.1016/0002-8703(65)90280-2

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 100 · R1523

**Tinnitus Retraining Therapy**

2004 · Cambridge University Press eBooks · book · en · https://doi.org/10.1017/cbo9780511544989

Tinnitus and oversensitivity to sound are common and hitherto incurable, distressing conditions that affect a substantial number of the population. Pawel Jastreboff's discovery of the mechanisms by which tinnitus and decreased sound tolerance occur has led to a new and effective treatment called Tinnitus Retraining Therapy (TRT). Audiologists, ENT specialists, psychologists and counsellors around the world currently practise this technique, with very high success rates. TRT, the treatment developed by the authors from the model, has already proved to be the most effective and most widely practised worldwide. This book presents a definitive description and justification for the Jastreboff neurophysiological model of tinnitus, outlining the essentials of TRT, reviewing the research literature justifying their claims, and providing an expert critique of other therapeutic practices.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 101 · R0745

**Sons, musiques & ressourcement -Thérapies traditionnelles, psychanalyse, musicothérapie et interactions biophysiques du son paysager et musical**

2023 · CCSD · working paper

This text constitutes an attempt at the state of the art concerning the restoration effects of sound, whose literature review extends from the influence of biophony, geophony and anthropophony on the sphere of human perception, to the therapeutic effects sound in their cultural and medical dimension, from shamanic rituals to music and sound therapy. We discuss the trans-modal principle of the sound envelope mobilized in the context of autism spectrum music therapies, as well as other alternative sound health care, such as ASMR used for misophonic disorders, for put into perspective with the hypotheses of genodics which evoke the relationship between musical sound and life sciences. Finally, we will introduce the notion of transitional sound object, which, through its reminiscent and projective double functionality, allows to anchor the resourcing by the sound in a perspective of world symbolization.Ce texte constitue une tentative d'état de l'art concernant les effets ressourçants du son, dont la revue de littérature s'étend de l'influence des sons biophoniques, géophoniques et anthropophoniques sur la sphère de perception humaine, jusqu'aux effets thérapeutiques du sonore dans leur dimension à la fois culturelle et médicale, des rituels shamaniques à la musicothérapie et la sonothérapie. Nous y abordons le principe trans-modal de l'enveloppe sonore mobilisé dans le cadre des musicothérapies du spectre autistique, ainsi que d'autres soins de santé alternatifs par le sonore, comme l'ASMR utilisé pour les troubles misophoniques, pour les mettre en perspective avec les hypothèses de la génodique qui évoquent les rapports entre son musical et sciences du vivant. Enfin, nous introduirons la notion d'objet sonore transitionnel, qui, par sa double fonctionalité réminiscente et projective, permet d'ancrer le ressourcement par le sonore dans une perspective de symbolisation du monde

**Решение:** -1 обзор литературы / концептуальная статья

---

### 102 · R1469

**Misophonia: physiological investigations and case descriptions.**

2013 · Frontiers in human neuroscience · article, journal article, journalarticle · eng · https://doi.org/10.3389/fnhum.2013.00296

Misophonia is a relatively unexplored chronic condition in which a person experiences autonomic arousal (analogous to an involuntary "fight-or-flight" response) to certain innocuous or repetitive sounds such as chewing, pen clicking, and lip smacking. Misophonics report anxiety, panic, and rage when exposed to trigger sounds, compromising their ability to complete everyday tasks and engage in healthy and normal social interactions. Across two experiments, we measured behavioral and physiological characteristics of the condition. Interviews (Experiment 1) with misophonics showed that the most problematic sounds are generally related to other people's behavior (pen clicking, chewing sounds). Misophonics are however not bothered when they produce these "trigger" sounds themselves, and some report mimicry as a coping strategy. Next, (Experiment 2) we tested the hypothesis that misophonics' subjective experiences evoke an anomalous physiological response to certain auditory stimuli. Misophonic individuals showed heightened ratings and skin conductance responses (SCRs) to auditory, but not visual stimuli, relative to a group of typically developed controls, supporting this general viewpoint and indicating that misophonia is a disorder that produces distinct autonomic effects not seen in typically developed individuals.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 103 · R1218

**Corrigendum to ‘The Suitability of an Inhibitory Learning Approach in Exposure When Habituation Fails: A Clinical Application to Misophonia’ [Cognitive and Behavioral Practice 26(1) (2019) 130-142]**

2019 · Cognitive and Behavioral Practice · article, erratum · en · https://doi.org/10.1016/j.cbpra.2019.08.001

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 erratum / correction

---

### 104 · R0726

**Management der Misophonie**

2023 · HNO Nachrichten · article, journalarticle · de · https://doi.org/10.1007/s00060-023-8617-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 обзор литературы / концептуальная статья

---

### 105 · R0501

**Association between Chronic Misophonia-Induced Stress and Gastrointestinal Pathology in Children-A Hypothesis.**

2024 · Children (Basel, Switzerland) · article, conference object, journal article · eng · https://doi.org/10.3390/children11060699

Misophonia is a neurophysiological disorder with behavioral implications, is complex and multifactorial in origin, and is characterized by an atypical and disproportionate emotional response to specific sounds or associated visual stimuli. Triggers include human-generated sounds, mainly sounds related to feeding and breathing processes, and repetitive mechanical sounds. In response to the triggering stimulus, the patient experiences immediate, high-intensity, disproportionate physical and emotional reactions that affect their quality of life and social functioning. The symptoms of misophonia can occur at any age, but onset in childhood or adolescence is most common. Affected children live in a constant state of anxiety, suffer continuous physical and emotional discomfort, and are thus exposed to significant chronic stress. Chronic stress, especially during childhood, has consequences on the main biological systems through the dysregulation of the hypothalamic-pituitary-adrenal axis, including the gastrointestinal tract. Here, we provide arguments for a positive correlation between misophonic pathology and gastrointestinal symptoms, and this hypothesis may be the starting point for further longitudinal studies that could investigate the correlations between these childhood vulnerabilities caused by misophonia and their effect on the gastrointestinal system. Further research to study this hypothesis is essential to ensure correct and timely diagnosis and optimal psychological and pharmacological support.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 106 · R0225

**Characterizing the cognitive dimensions of misophonia using a qualitative approach: from in-the-moment appraisals to intrusive thoughts about prior sounds**

2026 · Clinical Psychologist · article, journalarticle · en · https://doi.org/10.1080/13284207.2026.2627945

Objective Misophonia involves intense affective and physiological reactions to everyday sounds, yet the accompanying negative cognitive processes are understudied. The objective of this study was to qualitatively characterize cognitions that occur during and after misophoniasounds.Method We used inductive content analysis to analyse the open ended responses from 60 treatment-seeking adults using the Duke Misophonia Interview.Results During exposure, participants reported: (1) self-critical/self-devaluing thoughts related to one’s reactions to misophonicsounds, (2) externalizing appraisals of others as rude orinconsiderate, (3) intrusive aggressive thoughts, and (4)escape-focused cognitions. After exposure, they described: (1) regret and guilt about their reactions, (2) social worries about how other sperceived them, and (3) intrusive or repetitive memories of prior sound experiences.Conclusion These themes highlight how cognition play a central role in misophonia in the moment and afterwards, with post-misophonic-event processes extending distress beyond exposure to the sound itself. Clinical implications from these themes include screening for these thought patterns, targeting maladaptive self-appraisals, addressing regret and rumination, and channelling escape-related cognitions towards functional coping strategies. Future work should utilizereal-time assessment and more diverse samples to test how these cognitive processes maintain misophonia and to inform tailoredinterventions.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 107 · R0667

**misophonia, n.**

2023 · Oxford University Press eBooks · part of book or chapter of book, reference-entry · en · https://doi.org/10.1093/oed/4541953816

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 dictionary / reference entry

---

### 108 · R0944

**Case Report Treatment of Misophonia with Risperidone in a Patient with Autism Spectrum Disorder**

2022

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 109 · R1050

**If you’re annoyed by other people’s fidgeting or finger-tapping, you’re not alone: Misokinesia affects 1 in 3**

2021 · The Conversation · article, other · en · https://doi.org/10.64628/aam.7a4jcycfr

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 научно-популярная статья (The Conversation)

---

### 110 · R0932

**Trastorno del procesamiento sensorial. Una mirada conjunta desde la terapia ocupacional y la otorrinolaringología**

2022 · Revista de otorrinolaringología y cirugía de cabeza y cuello · article · es · https://doi.org/10.4067/s0718-48162022000100114

ResumenEl trastorno del procesamiento sensorial (TPS) es una condición frecuente, pero poco conocida por muchos profesionales de la salud.El procesamiento sensorial se define como la capacidad que posee el sistema nervioso central de interpretar y organizar las sensaciones del propio cuerpo y del ambiente, para su uso efectivo en el entorno mediante respuestas adaptativas.Por lo tanto, cualquier disfunción en el procesamiento (registro, modulación y/o discriminación) de estos estímulos se expresa como una respuesta desadaptativa, siendo significativo cuando esta impacta en la vida diaria del paciente.Es deber del médico sospechar este trastorno, acogiendo al paciente y su familia, derivando oportunamente a terapia ocupacional para su correcta evaluación y eventual manejo de acuerdo con las necesidades de cada paciente.

**Решение:** -6 не про мизофонию

---

### 111 · R0383

**HART Lab**

2025 · eGrove · text

HART Lab (Health and Anxiety Research and Treatment) The primary focus of the HART lab is on the etiology, maintenance, and treatment of anxiety disorders. The lab takes a transdiagnostic approach to examining behavioral, cognitive, emotional, and psychophysiological processes that underlie a variety of anxiety and related disorders, including social anxiety disorder, panic disorder, generalized anxiety disorder, posttraumatic stress disorder, obsessive compulsive disorder, misophonia, and specific phobias. The secondary emphasis of the lab pertains to the intersection of anxiety and health, and in particular, how anxiety pathology may contribute to engagement in maladaptive health behaviors (e.g., substance use) and exacerbate medical conditions (e.g., dermatological disorders). Within these critical domains, the lab aims to: (1) enhance our understanding of anxiety pathology in at-risk populations; and (2) translate scientific knowledge into the development, evaluation, and dissemination of brief, targeted anxiety interventions to optimize treatment outcomes and increase access to care

**Решение:** -1 обзор литературы / концептуальная статья

---

### 112 · R1114

**Investigating the structure of trait rumination in autistic adults: A network analysis**

2021 · Autism · article, other literature type · eng · https://doi.org/10.1177/13623613211012855

Rumination, a form of passive, repetitive negative thinking, predicts the development of depressive disorders in non-autistic individuals, and recent work suggests higher levels of rumination may contribute to elevated rates of depression in the autistic population. Using psychological network analysis, this study sought to investigate the structure of rumination in autistic individuals and the relationships between rumination and individual depressive symptoms. Non-regularized partial correlation networks were estimated using cross-sectional data from 608 autistic adults who completed the Ruminative Responses Scale and Beck Depression Inventory–II. Node centrality indices were calculated to determine which specific symptoms may have a disproportionate influence on the network of repetitive negative thoughts. Nodes were also grouped into communities, and specific “bridge” nodes were identified that most strongly connected these different communities. Results demonstrated strong positive relationships between all facets of ruminative thinking, similar to a prior study in non-autistic adults. Self-directed negative cognitions appeared to be particularly central in this network. The depression symptoms most strongly related to rumination in autistic adults were sadness and guilt. Although these findings are preliminary, they highlight specific facets of rumination that warrant future study as depression risk factors and potential intervention targets in the autistic population. Lay abstract Autistic adults are substantially more likely to develop depression than individuals in the general population, and recent research has indicated that certain differences in thinking styles associated with autism may play a role in this association. Rumination, the act of thinking about the same thing over and over without a functional outcome, is a significant risk factor for depression in both autistic and non-autistic adults. However, little is known about how different kinds of rumination relate to each other and to depressive symptoms in the autistic population specifically. To fill this gap in knowledge, we recruited a large online sample of autistic adults, who completed questionnaire measures of both the tendency to ruminate and symptoms of depression. By examining the interacting network of rumination and depression symptoms, this study was able to identify particular aspects of rumination—such as thinking repetitively about one’s guilty feelings or criticizing oneself—that may be particularly important in maintaining these harmful thought patterns in autistic adults. Although further study is needed, it is possible that the symptoms identified as most “influential” in the network may be particularly good targets for future interventions for mood and anxiety disorders in the autistic population.

**Решение:** -6 не про мизофонию

---

### 113 · R0551

**A combination of fluoxetine and olanzapine for the treatment of an adolescent with severe misophonia.**

2024 · Dusunen adam : Bakirkoy Ruh ve Sinir Hastaliklari Hastanesi yayin organi · article, journalarticle, lettersandcomments · eng · https://doi.org/10.14744/dajpns.2024.00238

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 114 · R0026

**Contextual Triggers and Tic Severity Across Life Periods: A Retrospective Analysis in Adults with Tic Disorders.**

2026 · Child psychiatry and human development · journal article · eng · https://doi.org/10.1007/s10578-024-01733-y

In tic disorders (TD), tic expression varies across the lifespan and as a function of contextual factors. This study explored connections between tic expression and contextual triggers across life periods in 74 adults (Mage = 23.2) with TDs. The Tic History and Coping Strategies form assessed retrospective self-reports of contextual antecedents, consequences, and tic severity during four life periods (middle school; 9th/10th grade; 11th/12th grade; college/work) and past month. Tics reportedly worsened during and after school in school-aged years and worsened in the evening during college/work years. Stress and anxiety were reported to consistently trigger tics across time. The impact of activities, places, and emotions did not differ across life periods. Attention-based consequences, most prevalent during middle school, were more common than escape- or avoidance-related consequences across all periods. Findings illuminate how contextual factors may influence tics across life periods and underscore the consistent impact of tic-triggering emotions and attention-related consequences.

**Решение:** -6 не про мизофонию

---

### 115 · R1305

**Tinnitus and sound intolerance: evidence and experience of a Brazilian group.**

2018 · Brazilian journal of otorhinolaryngology · article, dataset/dataset, journal article · eng · https://doi.org/10.1016/j.bjorl.2017.12.002

Abstract Introduction Tinnitus and sound intolerance are frequent and subjective complaints that may have an impact on a patient's quality of life. Objective To present a review of the salient points including concepts, pathophysiology, diagnosis and approach of the patient with tinnitus and sensitivity to sounds. Methods Literature review with bibliographic survey in LILACS, SciELO, Pubmed and MEDLINE database. Articles and book chapters on tinnitus and sound sensitivity were selected. The several topics were discussed by a group of Brazilian professionals and the conclusions were described. Results The prevalence of tinnitus has increased over the years, often associated with hearing loss, metabolic factors and inadequate diet. Medical evaluation should be performed carefully to guide the request of subsidiary exams. Currently available treatments range from medications to the use of sounds with specific characteristics and meditation techniques, with variable results. Conclusion A review on tinnitus and auditory sensitivity was presented, allowing the reader a broad view of the approach to these patients, based on scientific evidence and national experience.</div

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 116 · R0901

**Editorial: Death and Mourning Processes in the Times of the Coronavirus Pandemic (COVID-19)**

2022 · Frontiers in Psychiatry · editorial · en · https://doi.org/10.3389/fpsyt.2022.922994

Two years after the COVID-19 outbreak (WHO), and already in the 6 th wave in some countries, we feel overwhelmed by the portrait of 'our world in data' (Figure 1, top). The devastating total numbers (504M cases and 6.2M deaths) can hardly attempt to quantify the human dimension of a world map full of spots that feel like black holes. As of today, April 17, 2022, the most recent scenario unveils the pervasive emptiness, with 44.888 new persons worldwide that confronted death in the last 14 days and the start of a bereavement period for their beloved families to grieve and mourn their loss. Yet, the non-COVID deaths associated with the secondary impact of this pandemic will be hard to record. Nevertheless, the number of recovered patients reported worldwide and the extraordinary scientific efforts to draw a vaccine map, are new seeds of hope in this COVID-19 outbreak, one of the deadliest pandemics in human history.Looking back to those dreadful early months in China, Italy, and Spain that warned what would happen worldwide, this Research Topic emerged as the scientific readout of a tend-and-befriend copying (Taylor et al. 2000) that gathered together online an international group of 12 people handling and analyzing the unprecedented and devastating pandemic scenario through the lens of psychiatry, neuroscience, geriatric, palliative care, psychology, medicine, nursery, education, sociology, pediatric and pharmacy. At that time, reports from official sources and trustful academic and social media were the only information available and primarily focused on the virus, while aspects related to its actual impact could hardly be heard (WHO, Harvard Health Publishing, BBC, 2020). Thus, from our respective countries (Argentina, Belgium, Brazil, India, Iran, Italy, Netherlands, Nigeria, Panama, and the USA), we realized the taboo of death at the individual and social levels would worsen the impact on the public health emergency under the pressure of chronosystem and the minatory shadows of a secondary impact and multiple mourning that could already be foreseen (Masiero et al., 2020;Zhai and Du, 2020). The goal of this Research Topic was to face this taboo with an international call to address death and mourning processes from different multidisciplinary perspectives and cultures. We encouraged immediate opinions, perspectives, and reviews that would open discussion about the challenges and solutions before original research reports could arrive. This e-book compilates the efforts of 174 authors from 22 countries (Argentina, Australia, Austria, Brazil, China, Iran, Ireland, Israel, Italy, Japan, Nigeria, Norway, Pakistan, Panama, Portugal, Romania, South Arabia, Spain, Sweden, Switzerland, UK, and the USA) that joined us with 46 scientific papers in this goal. Their work was reviewed by 89 peers that added 14 other countries to the international scientific discussion panels (Bangladesh, Canada, France, Germany, Greece, Indonesia, Lebanon, Poland, Shri Lanka, Singapore, South Africa, South Korea, Taiwan, and Tunisia). This effort, from five continents, deserved the attentive look of 280,507 views and 36,501 downloads worldwide and a 674 total altimetric (Figure 1, middle). The editorial follows the structure of the different proposed thematic aspects (Figure 1, bottom), and we have cited the first authors with names and surnames and their countries to emphasize their personal commitment from different parts of the world, to provide not only technical but also spiritual and educational tools to mitigate the present and future impact of COVID-19 in our multiple mourning process as individuals and/or as a society.The universality of death and mourning processes is shaped by cultural perspectives (Kagawa-Singer, 1998), whose relevance is enhanced in devastating scenarios. In the current pandemic, these processes mirror the singularity of individual and societal impacts that can be alleviated through resistance and resilience. These two natural human capacities are related to demographics, available resources, and life stress (Bonanno et al., 2007). Person-centered variables and socio-contextual factors such as previous experiences, beliefs, education, and culture can promote them. Therefore, cross-cultural biopsycho-social perspectives confronting multiple losses, death, and mourning can make dying, as Juan Carlos Bermejo (Spain) said in his Opinion, "an archipelago, which is characterized precisely of being united by what it separates." Professor Purushottama Bilimorac (Australia), in his 'Hindu response to dying and death', argued and pleaded for a paradigm shift in the discursive and practical approaches to the COVID-19 pandemic, looking through the broad lens of Hinduism. That may help therapists and care workers develop a deeper understanding of cultural and religious beliefs. Also, to improve clinical practice and therapy sessions by expanding their toolkit with interventions (yoga, mindfulness, etc.) already proven to positively affect other severe health and life-threatening conditions. The review 'Understanding grief during the first wave of COVID-19 in the United Kingdom' by Chao Fang and Alastair Comery (UK) examined the first available reports from trusted media and carefully selected academic literature. They adopted a hypothetical approach to explore the experiences of death and grief in the earliest period of the pandemic. The diverse and dynamic nature of the grief needs and responses at an individual and societal level was analyzed comprehensively. They revisited the ideas of 'good' and 'bad' deaths and bereavement support, thus providing foundational understandings for the new challenges and opportunities, also relevant for other socio-cultural contexts. In the Perspective article 'Managing Grief of Bereaved Families During the COVID-19 Pandemic in Japan', Yoko Matsuda et al. (Japan) described different cultural aspects linked to the Japanese situation and how they managed psychological distress due to the distance from a sick or dead family member. The authors suggested training methods for telepsychological interventions that could allow a face to face treatment. From an autoethnographic and ethnographic analysis, Inayat Ali (Austria) discussed the challenge that the shift of meaning of a 'normal' dead body to a 'viral' dead body represents for cultures, people, and governments. He described significant differences between customary death rituals and ceremonies of a dead body during ordinary situations in Pakistan and those performed during current times by government mandate and warned about the harmful impact on mental health. In the 'Global Financial Crisis, Smart Lockdown Strategies, and the COVID-19 Spillover Impacts: A Global Perspective Implications From Southeast Asia', Chunlei Wang et al. (China) provided a detailed analysis of the critical factors of the global health emergency and the secondary impact on mental well-being and socio-economy, with global perspective implications by examining Africa, America Asia, Australia, Europe, and the Middle East, and presenting Pakistan as a case study. Non-pharmaceutical interventions were proposed to formulate smart lockdown strategies to restart economic activities and help progress towards the next normal in society.This was the thematic content receiving the first Opinions that emerged as a claim, as highlighted in the subsequent contributions. The first paper arrived from a Spanish center for the humanization of health to translate the reflections on dignified and humanized death offered in their books into the current landscapes. In a rosary of spiritual thoughts and faith, Juan Carlos Bermejo revealed the transcendental relevance of accompaniment in grief in times of coronavirus. Similarly, the opinion by Jucier Gonçalves Junior et al. (Brazil) poetically described real scenarios hidden in the news: Silent cries intensify the pain of the life that is ending in a scenario where COVID-19 was literality robbing families of the chance to say a final goodbye. In a second opinion, this team summarized what the literature tells about the use of spirituality as a tool to face the negative symptoms of various pathologies. Its influence on mental health results from several factors, it improves therapeutic adherence, self-esteem, and self-control and strengthens family/friendship ties and intellectuals. Using other tools such as beliefs allows us to reduce the adverse effects of the pandemic, social isolation, and routine deprivation, which is necessary to establish a sense of security and normality. Religiosity as a resilience factor in stressful conditions was also addressed by Ines Testoni (Italy, Israel, USA). They investigated the mourning and management of the health emergency in a priestly community in the most affected Italian region. They depicted their psychological experiences related to the contagion and the eventual death of colleagues and the resilience strategies activated during the process. The thematic analysis unveiled how religious faith transformed fear and pain into motivation to strengthen the social bond, guide the community toward the goals of spirituality, and the ways of prayer and reflection about the finiteness of life. In a second work, Testoni's team (Italy, Israel) studied the evolution of the experience of elective abortion in nine non-practicing Catholic women. In a third assessment, coinciding with the worst period of Italy's COVID-19 crisis and the Easter declaration against abortion, the conflicts between women's religiosity and their sense of free will, aggravated their physical, relational, and psychological suffering, similar to perinatal grief.Lidia Borghi and Julia Menichetti (Italy) also developed their research study in Lombardia, where the higher percentual of deaths due to COVID-19 occurred in 2020. They described spontaneous strategies that family members adopted to cope with a relative's loss and manage stressful conditions in such severe circumstances. Also, Ilaria Coppola et al. (Italy) studied 'Spiritual Well-Being and Mental Health During the COVID-19 Pandemic in Italy' to understand the role of spirituality and religiosity in reacting to the pandemic situation, and in particular on the physical and mental health of the people involved. Spirituality and religious practices were protective factors connected with psychological, mental and physical health. Finally, Roberto Bartholo and Domício Proença Júnior (Brazil), in their brief essay entitled 'Sister Death, Cousin Grief: Modes of Presence Before Life and Death' shared a mode of thinking in contrast to contemporary happy modernity that stands for expectations of limitless prosperity and progress. They argued for philo-zoe (life) rather than philo-sophy. They disclosed about what to be born ("brother birth") and to die ("sister death") is, the enjoyment of incoming alterity ("cousin expectation") or the apologetical rite for alterities passed away ("cousin grief").The maximum exponential of these thematic aspects could be found in the research work 'Underreporting of COVID-19 cases among indigenous peoples in Brazil: A new expression of old inequalities' by Martha Fellows et al. According to COIAB's reports, the epidemiological analysis of COVID-19 in the Brazilian Amazon home of half a million Indigenous Peoples representing 170 ethnic groups drew a dramatic scenario that deserved international coverage in the news and was part of the documents used to present legal actions against the federal government. This large study desperately urged when Brazil recorded its deadliest month as the health crisis deepened. It provided the first scientific evidence of the Indigenous Peoples' higher vulnerability (136 and 110% higher incidence and mortality, respectively, than the and the dimension of of deaths by the Brazil of The analysis of to the of the the between economic activities and as those the to or dying from COVID-19 in the Indigenous health the Indigenous and and their were proposed as the two solutions to the of Indigenous Peoples in the COVID-19 pandemic. A second critical analysis by Inayat Ali entitled of and During COVID-19 in how the of pandemic scenarios were The developed the of a new that the among and to that and to responses to the pandemic and and government and the other in the of et al. Romania, interventions to to the COVID-19 challenges and The of two such as the and and the was found to be to the and the impact on health challenges and at the of this pandemic also use and the impact of The use of in the of the was they were or on the Using different of for a to the most and situations for and the of the the protective effects of different of their and ways to improve and analysis that the could the of in a and to when use was and of the most aspects of this Research Topic was that it offered extraordinary into the pandemic, as personal reflections or case The first case by et al. provided a experience of of a Spanish days after being on COVID-19 and developed with a of He with a of experiences of and of and fear of dying, which was the significant of in COVID-19 the authors that the would be on these patients and their families and warned to the of this unprecedented and situations in the current COVID-19 pandemic are factors for stress for the and have a impact on psychological at or those already with mental and Spain a in that a lockdown in (WHO, factors scenarios addressed by several original research to provide scientific to their impact and provide for and Spain, studied from these two countries the loss of They examined the role of of and and in confronting death Their results of and differences during grief Two different were for not in and sense of to the fear of about particular psychological needs during grief in persons with higher in In a second part of this et al. (Spain) the of fear of death between and in a Spanish and psychological of personal death, and variables higher on and fear of personal death, in the fear of personal death the between and symptoms during the lockdown in were investigated by and colleagues of the Italian of and They described the Italian situation during the lockdown and highlighted how was related to the of the one of the most symptoms was differences were highlighted in and pain In to be affected by the effects associated with the pandemic, presenting a resilience. In a approach old of and the devastating scenarios in and (Spain) the impact of social on and of the described in people with and in their work for the first time, was found to with isolation, of the severe impact and the to and and management of by social distance to the COVID-19 pandemic in Spain affected people from a and characterized by and responses by to Two by and (Spain) provided evidence of the and perspective of the secondary impact of the pandemic on the mental health of this clinical The first study recorded an exponential in clinical for conflicts with and of on of and was in than the of strategies and protective factors and and clinical In their second a the impact of months of on enhanced and fear of with or dying from and a significant in and the loss of in response to but also under conditions or that worsen with the of and in et al., in a perspective from a team of from different in Nigeria, the and the gathered by our depicted the secondary impact of to the pandemic and the in the number of deaths by factors such as and the They analyzed the and scenarios to a of solutions through and individuals to mitigate these secondary impact of the pandemic with of previous mental health and severe and personal and fear of also cases of COVID-19 related A and content analysis by Jucier Gonçalves Júnior et al. (Brazil) described how the COVID-19 pandemic and was linked to social and health for this dramatic situation is that may affect between family members and as They are one of the for mental health and and The review article by et al. on was to this hidden and that of and social were significant to for They highlighted factors and proposed early and the use of of and social on and its impact to opinion and by et al. offered a about deaths being and processes for patients and about the significant for in grief and added during promote they provided a of and Ines Testoni et al. (Italy, Israel) also provided evidence that grief by COVID-19 can be and in this to the effects of loss. They are related to the experiences of the of with the dying and the of the and the of contemporary death is not only a social but also an educational two that were highlighted by this pandemic. Two original research from during the first of the pandemic the relevance of death The first by Ines Testoni et al. (Italy, Israel, analyzed the of the experience in a death were the of death in contemporary the of and and and the relevance of death for future health these people to the of being to with such as those associated with The second work, by was the first original study of a educational a for about the of life and in when the devastating scenarios in its were The a in the and from and Spanish women's grief to a broad The was part of an academic or used to critical thinking on meaning and societal This at as an educational to critical and among Thus, practices make it as social workers and have confronted the psychological and physical impact of the COVID-19 pandemic, and have their in the to the pandemic. The perspective by et al. the of and the impact on their mental well-being and stress but a of on the death and mourning process or grief in workers and their They for to understand these and the of the to provide psychological to From Panama, et al. critical reflections on the role of clinical during They discussed their role in and the scientific and social of They suggested how research could be to open and in mental health devastating scenarios of this pandemic have in palliative care clinical and home et al., 2020). A critical of this research is that papers provided a critical analysis of the impact of on and by the and new were shared to help with similar they focused on scenarios where the of rituals on the process COVID-19 families of the chance to say a final psychological and the process as described by Jucier Júnior et al. The experience of a palliative care team in by also the severe impact of for the the for for patients and their and the of They warned about for patients and those with that were to the the or in families their at home as as These also affected those to the for other than et al. (Spain) the and of their of Life During which to and mitigate future in grief and grief A multidisciplinary team of health social workers and clinical with and to the on family of care and the It was activated in most situations that could and say to their beloved but also an impact on the Jucier Gonçalves Júnior et al. (Brazil) also provided into the dramatic challenges in palliative and care during the pandemic. They a detailed of their to and in news to patients and their of as a of social for their by et al., was in a during the COVID-19 lockdown in The study that shared activities with their and to as a of and The authors that when a is present in a it be an for and in public is provided by and social and the of can from a or to individual or group and the group (Italy, for Bereaved Families in the of and that the of the mourning and can be as an between bereavement and interventions in a psychological In their et al. addressed with grief symptoms after an by bereavement or in this pandemic. They a new online for grief on and of as an to new that may help mourning and the receiving mental well-being The between the use of the and grief were discussed by Ines Testoni et al. (Italy, and the of media of public on et to health have the media be on this they on In a third study on Testoni et al. as a tool to help people face the of the pandemic by a understanding of the situation and their and grief in is and severe it related to of or of In the perspective Grief in the of et al. (UK) such as due to factors and They that mental health and to the by that can provide with a sense of et al. USA) to explore how between a and various death and how the pandemic and understanding during to a the but on the by and also warned about grief during the differences between is to to the needs in a pandemic scenario that the of security and when looking at the world and and through this shared experience are only the culture of death is not A case by et al., to understanding the scenarios of mourning a loss during the COVID-19 pandemic and under They described the strategies used through and and their to that and the pandemic to mental the grief through an research these international described the of the different ways of and with the death and mourning processes during the pandemic. They highlighted the and social differences but also a which is human this the pandemic is but it to its The COVID-19 due to the different and the social situation after were developed and The the stressful of an unprecedented pandemic, and individuals and are to through the that from a clinical and social of COVID-19 have and will be investigated in future for the first in the of scientific open have a also the present in this of to with a of and with a highlighted et al., This our as one to and death and mourning processes from the five in an emergency pandemic situation, to face the of research with

**Решение:** -6 не про мизофонию

---

### 117 · R0935

**Tinnitus and Hyperacusis**

2022 · CRC Press eBooks · book-chapter · en · https://doi.org/10.1201/9781003175995-15

Tinnitus is defined as the conscious perception of an auditory sensation in the absence of a corresponding external stimulus. Pulse-asynchronous rhythmical tinnitus may have an underlying muscular origin, arising from myoclonus of palatal or intratympanic muscles. Most tinnitus is subjective in that it can only be detected by the affected person. Tinnitus is more common in people with hearing loss, but the degree of hearing loss corresponds poorly with the severity of tinnitus. Disorders of sound tolerance are subdivided: hyperacusis is dislike of all sounds above a certain intensity; misophonia is dislike of particular sounds, irrespective of the level of those sounds; and phonophobia is fear of particular sounds. Audiological management is a combination of addressing any associated hearing loss with hearing aids, assistive listening devices or, if necessary, cochlear implants, using sound therapy, explanation, education and counselling, relaxation training and, if needed, advice regarding sleep.

**Решение:** -1 глава книги / справочник

---

### 118 · R1364

**Considerations in the Development of a Sound Tolerance Interview and Questionnaire Instrument.**

2017 · Seminars in hearing · article, journal article, review · eng · https://doi.org/10.1055/s-0037-1598065

Most clinicians approach the objective fitting of hearing aids with three goals in mind: audibility, comfort, and tolerance. When these three amplification goals have been met, the hearing aid user is more likely to adapt to and perceive benefit from hearing aid use. However, problems related to the loudness of sounds and reduced sound tolerance, which may or may not be reported by the aided user, can adversely impact adaptation to amplification and the individual's quality of life. Although there are several standardized questionnaires available to evaluate hearing aid benefit and satisfaction, there is no standardized questionnaire or interview tool for evaluating reduced sound tolerance and the related impact on hearing aid use. We describe a 36-item tool, the Sound Tolerance Questionnaire (STQ), consisting of six sections, including experience with hearing aids, sound sensitivity/intolerance, medical and noise exposure histories, coexisting tinnitus problems, and a final question to differentiate the primary and secondary problems related to sound intolerance, tinnitus, and hearing loss. In its current format as a research tool, the STQ was sensitive in pinpointing vague sound tolerance complaints not reported by the study participants in eligibility screening by Formby et al. A refined version of the STQ, the Sound Tolerance Interview and Questionnaire Instrument (STIQI), structured as a two-part tool, is presented in the appendix for prospective clinical use. The STIQI has potential utility to delineate factors contributing to loudness complaints and/or reduced sound tolerance in individuals considering hearing aid use, as well as those who have been unsuccessful hearing aid users secondary to loudness complaints or sound intolerance. The STIQI, when validated and refined, also may hold promise for predicting hearing aid benefit and/or assessing treatment-related change over time of hearing aid use or interventions designed to remediate problems of loudness and/or sound intolerance among hearing aid candidates or users.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 119 · R1555

**A qualitative investigation of living with misophonia Short title: Living with misophonia**

other literature type · und · https://doi.org/10.1177/1359105326146434

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 120 · R1546

**Civilisation of manners and misophonia**

research article · https://core.ac.uk/download/573470212.pdf

Misophonia is a disorder of tolerance to specific sounds (i.e. trigger sounds), such as chewing, throat clearing or breathing sounds, produced by humans, which can trigger intense emotional reactions (anger, disgust). This relatively prevalent disorder can cause a reduction in the quality of life. The causes of misophonia are still unclear. In this article, we develop a “social” hypothesis based on the work of Norbert Elias. Misophonia would be an exaggerated reaction to behaviours (of others) that have been subject to rigorous social conditioning, which are supposed to be strictly regulated and repressed. The social rules imposed by society, accompanying the long process of pacification and increasing interdependence between individuals over the centuries, would be at the origin of this conditioning. The function of this conditioning, achieved mainly through shame and disgust, would be to preserve social cohesion, through the strict training of behaviour. It is indeed imperative to control oneself, to act in a thoughtful and balanced way, to spare others by taking into account their expectations, in short to behave in a “courteous” way. Imposed and less spontaneous behaviour creates a sense of modesty and distance between individuals. The obligation to strictly regulate behaviour and affect in public contributes to the creation of an interiority, an "inner self". The feeling of intrusion by others is a collateral effect of this process of distancing and individualisation. The rigorous integration of the social rule by the misophonic subject may account for the fact that any violation of the rule is considered unacceptable. In order to put an end to the unpleasant situation, i.e. to the intrusion generated by the “encroachment” of others, the subject has no other choice but to flee or to attack the author of the sound

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 121 · R0716

**Auraldiversity: Do You Hear Differently?**

2023 · Frontiers for Young Minds · article, journalarticle · en · https://doi.org/10.3389/frym.2023.979480

This article explores the sense that opens us to the world of sound: hearing. Textbooks often repeat the same numbers and figures on the sensitivity of human hearing, as if we all share the same set of symmetrical mechanical ears. Here, you will discover hearing as we experience it day-to-day: the different kinds and qualities of hearing you, your friends, and your family may have experienced, and how hearing may change as we grow older. We call this real-life approach to understanding hearing auraldiversity. This article will tell you about some important kinds of hearing differences such as hyperacusis, misophonia, and tinnitus, and it will explain the brief changes in hearing sensitivity that sometimes occur, such as after sudden loud sounds. Hearing can open us up to the world in a very powerful way, but we must remember that it is a vulnerable sense that needs protecting from too much loud sound.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 122 · R0156

**Therapeutic Homework and Treatment Outcomes in Youth Cognitive-Behavioral Therapy for Internalizing Disorders: A Meta-Analysis.**

2026 · Clinical child and family psychology review · journal article, review · eng · https://doi.org/10.1007/s10567-026-00579-1

Homework adherence represents a salient, modifiable target for improving cognitive behavioral therapy (CBT) outcomes for pediatric internalizing disorders. While the adult literature has found a clear connection between CBT homework adherence and treatment outcomes, the evidence among youth have been mixed regarding the extent to which between-session homework adherence predicts CBT outcomes. The present study conducted a systematic review and meta-analysis that examines the association between homework adherence and CBT outcomes in clinical trials of internalizing disorders for youth. Fourteen studies met prespecified inclusion criteria, comprising a total sample of 1179 participants (M age = 11.33 years, 53.79% female). Random-effects meta-analytic models identified a small-to-moderate association between greater homework adherence and lower post-treatment symptoms (r = -0.23, p < 0.001). Interestingly, disorder type significantly moderated this association, such that the association between homework adherence and CBT outcomes was strongest in obsessive-compulsive disorder (OCD) samples (r = -0.42), compared to anxiety (r = -0.14) and depression (r = -0.06). Findings underscore the importance of homework adherence as a mechanism of youth CBT, particularly for OCD. Enhancing homework adherence may help optimize CBT outcomes in pediatric populations.

**Решение:** -6 не про мизофонию

---

### 123 · R1061

**The Motor Basis for Misophonia.**

2021 · The Journal of neuroscience : the official journal of the Society for Neuroscience · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1523/jneurosci.0261-21.2021

Misophonia is a common disorder characterized by the experience of strong negative emotions of anger and anxiety in response to certain everyday sounds, such as those generated by other people eating, drinking, and breathing. The commonplace nature of these "trigger" sounds makes misophonia a devastating disorder for sufferers and their families. How such innocuous sounds trigger this response is unknown. Since most trigger sounds are generated by orofacial movements (e.g., chewing) in others, we hypothesized that the mirror neuron system related to orofacial movements could underlie misophonia. We analyzed resting state fMRI (rs-fMRI) connectivity ( N = 33, 16 females) and sound-evoked fMRI responses ( N = 42, 29 females) in misophonia sufferers and controls. We demonstrate that, compared with controls, the misophonia group show no difference in auditory cortex responses to trigger sounds, but do show: (1) stronger rs-fMRI connectivity between both auditory and visual cortex and the ventral premotor cortex responsible for orofacial movements; (2) stronger functional connectivity between the auditory cortex and orofacial motor area during sound perception in general; and (3) stronger activation of the orofacial motor area, specifically, in response to trigger sounds. Our results support a model of misophonia based on "hyper-mirroring" of the orofacial actions of others with sounds being the "medium" via which action of others is excessively mirrored. Misophonia is therefore not an abreaction to sounds, per se, but a manifestation of activity in parts of the motor system involved in producing those sounds. This new framework to understand misophonia can explain behavioral and emotional responses and has important consequences for devising effective therapies. SIGNIFICANCE STATEMENT Conventionally, misophonia, literally "hatred of sounds" has been considered as a disorder of sound emotion processing, in which "simple" eating and chewing sounds produced by others cause negative emotional responses. Our data provide an alternative but complementary perspective on misophonia that emphasizes the action of the trigger-person rather than the sounds which are a byproduct of that action. Sounds, in this new perspective, are only a "medium" via which action of the triggering-person is mirrored onto the listener. This change in perspective has important consequences for devising therapies and treatment methods for misophonia. It suggests that, instead of focusing on sounds, which many existing therapies do, effective therapies should target the brain representation of movement.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 124 · R0638

**Interaction between the prefrontal and visual cortices supports subjective fear.**

2024 · Philosophical transactions of the Royal Society of London. Series B, Biological sciences · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1098/rstb.2023.0245

It has been reported that threatening and non-threatening visual stimuli can be distinguished based on the multi-voxel patterns of haemodynamic activity in the human ventral visual stream. Do these findings mean that there may be evolutionarily hardwired mechanisms within early perception, for the fast and automatic detection of threat, and maybe even for the generation of the subjective experience of fear? In this human neuroimaging study, we presented participants ('fear' group: N = 30; 'no fear' group: N = 30) with 2700 images of animals that could trigger subjective fear or not as a function of the individual's idiosyncratic 'fear profiles' (i.e. fear ratings of animals reported by a given participant). We provide evidence that the ventral visual stream may represent affectively neutral visual features that are statistically associated with fear ratings of participants, without representing the subjective experience of fear itself. More specifically, we show that patterns of haemodynamic activity predictive of a specific 'fear profile' can be observed in the ventral visual stream whether a participant reports being afraid of the stimuli or not. Further, we found that the multivariate information synchronization between ventral visual areas and prefrontal regions distinguished participants who reported being subjectively afraid of the stimuli from those who did not. Together, these findings support the view that the subjective experience of fear may depend on the relevant visual information triggering implicit metacognitive mechanisms in the prefrontal cortex. This article is part of the theme issue 'Sensing and feeling: an integrative approach to sensory processing and emotional experience'.

**Решение:** -6 не про мизофонию

---

### 125 · R1167

**Influence of sound intolerance : in a perspective of Empowerment**

2020 · KTH Publication Database DiVA (KTH Royal Institute of Technology) · dissertation, thesis · sv

Sound intolerance affects a large part of the population and thus contributes to increased ill health in society. However, the extent to which and in what way sound intolerant is affected is unclear. The ​purpose​ was to contribute to a more qualitative understanding of the impact that sound intolerance can have by mapping and analyzing literature on sound intolerance in a perspective of Empowerment. The ​method​ used was a scoping study. In total, n = 24 studies were reviewed and n = 10 were included for an in-depth qualitative analysis. The results​ show that there are studies that describe that sound intolerance has an impact on Empowerment, but that none of the studies examined have such a pronounced focus. Sound intolerance seems in many respects to be a hidden or unconscious phenomenon and there is reason to work for higher knowledge and awareness to strengthen the sound intolerant's Empowerment.Ljudintolerans drabbar en stor del av befolkning och bidrar således till ökad ohälsa isamhället. I vilken utsträckning och på vilket sätt ljudintoleranta påverkas är dock oklart.Syftet var att bidra till en mer kvalitativ förståelse för den påverkan ljudintolerans kan hagenom att kartlägga- och analysera litteratur om ljudintolerans i ett perspektiv avEmpowerment. Metoden som användes var en kartläggande litteraturöversikt. Totaltgranskades n=24 studier och n=10 inkluderades för en fördjupad kvalitativ analys.Resultatet visar att det finns studier som beskriver att ljudintolerans har en påverkan påljudintolerantas Empowerment men att inga av de granskade studierna har ett sådant uttalatfokus. Ljudintolerans förefaller i många avseende vara ett dolt eller omedvetet fenomenoch det finns anledning att arbeta för högre kunskap och medvetenhet för att stärkaljudintolerantas Empowerment

**Решение:** -6 не про мизофонию

---

### 126 · R1338

**REMOVED: Investigating misophonia: A review of the literature, clinical implications and research agenda reflecting current neuroscience and emotion research perspectives.**

2017 · European psychiatry : the journal of the Association of European Psychiatrists · article, journal article, retraction notice · eng · https://doi.org/10.1016/j.eurpsy.2017.01.1180

This article has been removed: please see Elsevier Policy on Article Withdrawal (https://www.elsevier.com/about/our-business/policies/article-withdrawal). This article has been removed at the request of the authors due to errors in the author list.Copyright © 2017. Published by Elsevier Masson SAS

**Решение:** -1 обзор / комментарий / письмо

---

### 127 · R1159

**Sound Enrichment Therapy for Decreased Sound Tolerance in Individuals with Autism Spectrum Disorder: Pilot Study**

2020 · Turkiye Klinikleri Journal of Health Sciences · article · en · https://doi.org/10.5336/healthsci.2019-66601

ÖZET Amaç: Bu çalışmanın amacı, tinnitus, mizofoni ve hiperakuzi yönetiminde kullanılan Ses Zenginleştirme Terapisi (SZT)’nin, azalmış ses toleransına sahip Otizm Spektrum Bozukluğu (OSB) olan bireylerde etkinliğinin araştırılmasıdır. Gereç ve Yöntemler: Çalışmaya, yaşları 8-28 yıl (X=13,25 yıl, SS=±8,48 yıl) arasında değişen ve normal işitmeye sahip 6 (4 E-2 K) OSB’li birey dâhil edilmiştir. Ailelere terapi programı hakkında bilgiler verilerek, ailelerden ve/veya bireylerden aşırı hassas olunan sesleri belirlemeleri ve rahatsızlık şiddetlerini terapi öncesi vizüel analog skala (VAS)’ya işaretlemeleri istenmiştir. SZT, enstrümental müzik ve doğa sesleri kullanılarak uygun görülen MP3 veya bilgisayar uygulamaları ile sunulmuştur. SZT, üç aşamalı ve her aşama bir hafta sürecek şekilde programlanmıştır. Bireyde duyarlılık (ses tolerans artışı) sağlanana kadar terapiye devam edilmiş ve sonuçlar, terapi öncesi, 6 ve 12. haftalar olacak şekilde VAS ve bireysel görüşme yapılarak değerlendirilmiştir. Bulgular: En çok rahatsızlık hissi veren sesler; elektrik süpürgesi, çocuk ağlaması, kalabalık uğultusu, araç-egzoz sesi ve mikrofonik sesler olarak belirtilmiştir. Bazı aileler, bu sesleri duyduğunda çocuklarının hırçın davranışlar sergilediklerini açıklamışlardır. Bireylerin VAS puanları anlamlı şekilde rahatsızlığın azaldığı yönünde bulunmuştur (p<0,01). Bir aile, dayanılmaz rahatsızlık olarak belirttiği seslerin tamamen kaybolduğunu VAS puanları ile belirtmiş ve çocuğunun hırçın davranışlar sergilemediğini açıklamıştır. Sonuç: Amerikan Nöroloji Akademisi ve Çocuk Nörolojisi Topluluğu’nun komisyon raporunda, OSB’li bireylerin atipik işitsel karakteristiklerine ışık tutacak çalışmaların yapılması gerekliliği belirtilmiştir. Çalışmamız, bireylerde ses toleransının gelişebildiğini göstermiştir. Ses intoleransı olan OSB’li bireylere SZT’nin uygulanmasının etkili bir yöntem olduğu belirlenmiştir. Yapılan bu pilot çalışma sonucunda, ses intoleransı olan OSB’li bireylerde SZT’nin, karşılaştırmalı terapi teknikleri ile geniş vaka gruplarında çalışmaya değer olduğu sonucuna varılmıştır.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 128 · R1530

**Modification of Loudness Discomfort Level: Evidence for Adaptive Chronic Auditory Gain and Its Clinical Relevance**

2002 · Seminars in Hearing · article · en · https://doi.org/10.1055/s-2002-32944

A vexing problem in audiology has been the modification of sound tolerance. Sound intolerance and restricted dynamic ranges are common conditions that audiologists encounter daily in the hearing-impaired population, especially in the fitting of hearing aids. To date, no clinical protocol has proven to be successful for modifying sound tolerance among the hearing-impaired population. This report describes the use of low-level, broadband sound in a habituation-based treatment protocol termed Tinnitus Retraining Therapy (TRT). Over the past decade, TRT has become increasingly popular as an intervention for severe tinnitus and hyperacusis. One of the primary treatment effects from TRT is that over the course of the intervention the patient's loudness discomfort levels (LDLs) routinely shift to higher levels. Ostensibly, the resulting higher LDLs reflect treatment effects associated with the resetting of a plastic and adaptive auditory gain process that somehow regulates the supra-threshold sensitivity of the auditory system in response to chronic changes in the sound input from the auditory periphery to the central auditory pathways. Tinnitus patients with significant hearing losses and sound tolerance problems respond successfully to TRT and, as a consequence, their LDLs are usually elevated (improved) and, concomitantly, their dynamic ranges are expanded. Many of these patients, who before the TRT intervention could not tolerate amplified sound, then have been able to make a comfortable transition into appropriate amplification after treatment. In principle, TRT would seem to offer a viable intervention strategy for modifying sound tolerance in the general hearing-impaired population. If so, then clinical applications of TRT principles may extend well beyond the treatment of tinnitus and hyperacusis.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 129 · R1116

**Prevalence of Strabismus in Individuals on the Autism Spectrum: A Meta-analysis**

2021 · openRxiv · article, other literature type · und · https://doi.org/10.1101/2021.07.13.21260452

Abstract Background and Objectives Strabismus, a misalignment of the eyes, is an important risk factor for amblyopia and visual impairment in the pediatric population. Several studies have reported an increased likelihood of strabismus in persons on the autism spectrum, but prevalence estimates in this group vary greatly. Methods We searched multiple databases to identify peer-reviewed articles published in English through November 1, 2020 that provided estimates of strabismus prevalence in autistic individuals. Prevalence estimates were synthesized using Bayesian random-effects meta-analysis, and sensitivity analysis was also performed using only the subset of studies that recruited participants from non-ophthalmologic settings and identified strabismus using structured ocular exams. Bayesian meta-regression was used to assess potential moderators of prevalence across studies. Results A total of 151 nonduplicate articles were screened, of which 22 were included in the meta-analysis ( k =28 samples, n AUT=113,227). The meta-analytic point prevalence of strabismus in autistic individuals was 13.4% (95% CrI [8.3,19.4]), and sensitivity analysis produced a very similar estimate (14.0% [7.0,22.0], n AUT =581). Esotropia was the predominant subtype of strabismus reported, accounting for approximately 55% of cases. Reported prevalence rates were higher in younger samples ( BF 10 =13.43, R 2 Het =0.273) and samples recruited from optometry/ophthalmology clinics ( BF 10 =11.47, R 2 Het =0.238). Conclusion This meta-analysis found a high prevalence of strabismus in autistic individuals, with rates 3–10 times that of the general population. As untreated strabismus is a major risk factor for amblyopia in young children, these findings underscore the importance of timely screening and assessment of ocular problems in persons on the autism spectrum. What’s Known on This Subject Strabismus has been reported to be more prevalent in individuals on the autism spectrum, but estimates have been very imprecise, ranging from 3–84% across studies. What This Study Adds This study performs the first quantitative synthesis of strabismus prevalence in over 100,000 autistic individuals, generating more precise estimates of the prevalence of strabismus in the autistic population. Factors contributing to the large differences between studies are also examined using meta-regression.

**Решение:** -6 не про мизофонию

---

### 130 · R1017

**Interfacing the Tympan open-source hearing aid with an external computer for research on decreased sound tolerance**

2021 · Proceedings of meetings on acoustics · article, conference-paper · en · https://doi.org/10.1121/2.0001616

While headphones and hearing protectors are often used to relieve the distress associated with decreased sound tolerance, unnecessary attenuation of surrounding sounds may have negative consequences. With an advanced hearing device that can attenuate according to the wearer’s surroundings or mental state, it may be possible to reduce distress while still mitigating possible negative effects of over-attenuation. To investigate the utility of these features in practice, there is a need for a hearing device with which these features can be implemented. Two existing platforms, the Auditory Research Platform 3.1 and the Tympan Open-Source Hearing Aid Platform RevD, were evaluated for their suitability for decreased sound tolerance research. Due to the high latency of the Auditory Research Platform and the limited computational resources of the Tympan, an open-source software pipeline was built such that some of the processing, for which latency is not as crucial, could run on an external computer.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 131 · R1123

**An age-related investigation of audio-vestibular symptoms in individuals with Covid-19 positive**

2021 · Çukurova medical journal (Online)/Çukurova medical journal · article · en · https://doi.org/10.17826/cumj.987374

Purpose: The aim of this study was to determine the rate of audio-vestibular complaints by COVID-19 patients during the disease period and to evaluate the symptoms they encountered during the disease process in accordance with age and gender. Materials and Methods: This study was conducted with a total of 1437 patients (738 M, 699 F) with a positive PCR test, aged 18–80 years, between 15 June 2020 and 10 February 2021. The patients were divided into five groups according to age. 1437 patients were questioned about their complaints on the second day of the disease, but only 656 of 1437 patients were questioned on the fourteenth day of the disease. Finally, 1437 patients were called again for the third time in the third month of the disease, but only 340 of these patients could be reached. Results: Of the 1437 patients, 524 (36.5%) had more frequent audio-vestibular complaints than common complaints. During the 14-day disease period, dizziness or vertigo (3.4% to 19.4%), tinnitus (1.02% to 19.4%), pressure in the ears (1.1% to 5.6%), difficulty understanding speech in noise (0.13% to 26%), decreased sound tolerance (0.13% to 6.4%), speech difficulties (0.13% to 5%), and earache (1.4% to 7.8%) reportedly increased compared with the first day of the disease. Fifty-two (15.3%) of 340 patients reported that they lost their sense of taste, 90 (26.4%) lost their sense of smell, and 14 (4.11%) reported intermittent vertigo in the third month of COVID-19 infection. Conclusion: Symptoms such as dizziness, tinnitus, hoarseness, swallowing difficulty, fever, and decreased sound tolerance can often be seen in the later days of COVID-19 disease.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 132 · R0274

**Evaluation of extended high frequency thresholds in individuals with misophonia**

2025 · The Egyptian Journal of Otolaryngology · article, journalarticle, google scholar result · en · https://doi.org/10.1186/s43163-025-00912-5

Abstract Background Misophonia is a condition characterized by strong emotional and physiological responses to specific auditory or visual stimuli, often leading to distress and functional impairment. It commonly co-occurs with disorders such as OCD, ADHD, and tinnitus, yet its underlying auditory mechanisms remain poorly understood. Traditional audiometry may not fully capture the auditory sensitivities reported in misophonia, suggesting a need to explore extended high-frequency hearing thresholds. Previous studies have indicated atypical neural activation patterns in misophonic individuals, pointing toward altered auditory processing. This study aimed to compare extended high-frequency thresholds between individuals with misophonia and typical adults to better understand auditory sensitivity in this population and enhance diagnostic precision. Methods Thirty participants aged 18–54 years (mean age 32.01, SD = 11.3) were divided into two groups: 15 with misophonia and 15 controls. All the participants had normal hearing sensitivity, Type-A tympanograms with acoustic reflexes at 1000 Hz, and presence of transient-evoked otoacoustic emissions. Misophonia symptoms were assessed using the Revised Amsterdam Misophonia Scale (A-MISO-S). Extended High-Frequency Audiometry (EHFA) was performed in a sound-treated environment. Results A paired t-tests showed no significant inter-ear differences; thus, bilateral data were pooled. Independent t-tests revealed significantly better extended high-frequency thresholds in the misophonia group compared to controls, with no significant age differences between groups. Conclusion This study found significantly enhanced extended high-frequency thresholds in individuals with misophonia, indicating increased auditory sensitivity possibly due to altered auditory processing mechanisms. These findings support incorporating EHFA into clinical assessments, aiding targeted management strategies for misophonia. Additional research is needed to strengthen these observations.

**Решение:** ? случай-контроль (15 с мизофонией vs 15 контроль), проверить скрининг пула

---

### 133 · R1557

**Misophonia**

article · eng · https://ddd.uab.cat/record/259880

Misophonia is a scarcely known disorder. This systematic review (1) offers a quantitative and qualitative analysis of the literature since 2001, (2) identifies the most relevant aspects but also controversies, (3) identifies the theoretical and methodological approaches, and (4) highlights the outstanding advances until May 2022 as well as aspects that remain unknown and deserve future research efforts. Misophonia is characterized by strong physiological, emotional, and behavioral reactions to auditory, visual, and/or kinesthetic stimuli of different nature regardless of their physical characteristics. These misophonic responses include anger, general discomfort, disgust, anxiety, and avoidance and escape behaviors, and decrease the quality of life of the people with the disorder and their relatives. There is no consensus on the diagnostic criteria yet. High comorbidity between misophonia and other psychiatric and auditory disorders is reported. Importantly, the confusion with other disorders contributes to its underdiagnosis. In recent years, assessment systems with good psychometric properties have increased considerably, as have treatment proposals. Although misophonia is not yet included in international classification systems, it is an emerging field of growing scientific and clinical interest.

**Решение:** -1 обзорная публикация / словарный очерк

---

### 134 · R1488

**Fear of the yawning mother: a case study of misophonia.**

2011 · Australasian psychiatry : bulletin of Royal Australian and New Zealand College of Psychiatrists · retraction notice · eng · https://doi.org/10.3109/10398562.2011.551934

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 135 · R1482

**Does training on inhibitory tasks influence alcohol consumption and attitudes**

2012 · Research Online (University of Wollongong) · article · en

Response inhibition - the suppression of a prepotent or ongoing action - is an executive function central to the regulation of behaviour. Response inhibition can be assessed in the laboratory using the Go/No-go or Stop-Signal tasks which both assess the capacity to withhold an inappropriate response. In the Go/No-go task, participants are required to respond rapidly to Go stimuli but to withhold that response upon No-go stimuli. In the Stop-Signal task, participants are required to respond to Go stimuli but to withhold the response when an auditory stop signal occurs subsequent to the Go stimulus.

**Решение:** -6 не про мизофонию

---

### 136 · R1234

**MisophoniAPP: A Website for Treating Misophonia**

2019 · article · en

abstract: This paper introduces MisophoniAPP, a new website for managing misophonia. It will briefly discuss the nature of this chronic syndrome, which is the experience of reacting strongly to certain everyday sounds, or “triggers”. Various forms of Cognitive Behavioral Therapy and the Neural Repatterning Technique are currently used to treat misophonia, but they are not guaranteed to work for every patient. Few apps exist to help patients with their therapy, so this paper describes the design and creation of a new website that combines exposure therapy, relaxation, and gamification to help patients alleviate their misophonic reflexes

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 137 · R0686

**“I’m sure Dr Jekyll had misophonia”: A Reflexive Thematic Analysis (RTA) examining lived experience patterns in misophonia and the usefulness of Reddit as an online support network.**

2023 · PsyArXiv · article, preprint · en · https://doi.org/10.31234/osf.io/wgvju

Misophonia, commonly referred to as the ‘hatred of sounds’ disorder (despite lack of official classification in the diagnostic tools), has largely been investigated with the purpose of establishing a mechanism responsible for the disorder. Perpetuating the emergence of two main gaps within the literature; i) lack of large-scale lived experience research, and ii) lack of investigation towards the online support networks that are becoming increasingly utilised and available to misophonic individuals. To address these gaps, this project utilised the r/misophonia subreddit as a data collection source to examine the presence of lived experience patterns in people with misophonia, and to assess the usefulness of online support networks. The dataset included 26 reddit posts (10 from the year 2021, and 16 from the year 2022) which were randomly sampled using an application programming interface (API), and then analysed qualitatively using reflexive thematic analysis (RTA). Overall, the findings portrayed that misophonic individuals share a plethora of lived experiences, and regarding the use of online support networks, such as the r/misophonia subreddit, these were represented as largely positive environments (via. Providing support, freedom of expression, and a place to vent). However, there were also negative implications of using online social networks, for example they can become environments of perpetuating negativity where discussions of self-harm, and suicide may take place.

**Решение:** -5 качественное исследование

---

### 138 · R1461

**Demographic and clinical characteristics of the misophonia patients (N = 42).**

2013 · https://doi.org/10.1371/journal.pone.0054706.t001

1 (Lip) smacking, swallowing, eating chips/fruit. 2 Loud breathing, nostril sounds, coughing, sneezing. 3 Typing, pen clicking, nail clipping. 4 Footsteps, sound of high heels. 5 Repetitive leg rocking. 6 (Recurrent) depressive disorder, dysthymic disorder. 7 Attention Deficit Hyperactivity Disorder. 8 Obsessive Compulsive Disorder. 9 Obsessive Compulsive Personality Disorder. 10 Trichotillomania. a No other personality disorders were diagnosed in the sample.</p

**Решение:** -1 обзор литературы / концептуальная статья

---

### 139 · R0792

**Editorial: Advances in understanding the nature and features of misophonia**

2023 · Frontiers in Neuroscience · article, other literature type, editorial · eng · https://doi.org/10.3389/fnins.2023.1267682

COPYRIGHT © 2023 Rosenthal, Campbell and Altimus. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms. Editorial: Advances in understanding the nature and features of misophonia

**Решение:** -1 редакционная статья / письмо

---

### 140 · R1347

**Darum machen manche Geräusche wütend**

2017 · DMW - Deutsche Medizinische Wochenschrift · article · de · https://doi.org/10.1055/s-0043-101802

Menschen mit Misophonie reagieren sehr wütend oder aggressiv auf bestimmte Geräusche. Britische Forscher fanden jetzt heraus, warum dies so ist. Sie spielten Personen mit und ohne Misophonie diverse Geräusche vor. MRT-Gehirn-Scans ergaben, dass beide Gruppen ähnlich auf neutrale und aufreibende Geräusche (z. B. Regen bzw. das Schreien eines Kleinkindes) reagierten. Bei sogenannten Triggern (essen, atmen, trinken) jedoch zeigten Misophoniker überdurchschnittlich hohe Aktivität im vorderen Inselkortex – einer Gehirnstruktur, die in die emotionale Verarbeitung involviert ist. Zudem ging die Inselrinde unüblich viele Verbindungen mit anderen Gehirnbereichen ein. [hhi]

**Решение:** -1 обзор литературы / концептуальная статья

---

### 141 · R1430

**P.1.i.015 Impulsive aggression in misophonia: results from a functional magnetic resonance imaging study**

2015 · European Neuropsychopharmacology · article · en · https://doi.org/10.1016/s0924-977x(15)30374-6

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (fMRI исследование импульсивной агрессии при мизофонии)

---

### 142 · R1481

**Journal Digest**

2013 · Psychiatric News · article · fr · https://doi.org/10.1176/appi.pn.2013.3b14

Back to table of contents Previous article Next article Journal DigestFull AccessJournal DigestLeslie SinclairLeslie SinclairSearch for more papers by this authorPublished Online:15 Mar 2013https://doi.org/10.1176/appi.pn.2013.3b14Risk Factors for PTSD in Combat Soldiers IdentifiedA group of researchers based at Tel Aviv University in Israel, the University of Maryland, and the National Institute of Mental Health recently set out to define risk and resilience factors associated with development of posttraumatic stress disorder (PTSD) in combat soldiers that could be targeted by novel therapeutic treatments. They conducted a longitudinal prospective study of more than 1,000 Israeli Defense Force infantry soldiers (mean age 18.8 years) from 2008 to 2010. Repeated measurements during a one-year period included baseline and predeployment data collected in training camps and deployment data collected in the combat theater.Soldiers’ threat-related attention bias interacted with combat exposure and genetic factors to predict risk of PTSD.ChameleonsEye/ShutterstockThey found that soldiers developed threat vigilance during combat deployment, particularly when they were exposed to high-intensity combat, as indicated by faster response times to targets appearing at the location of threat relative to neutral stimuli. Threat-related attention bias also interacted with combat exposure to predict risk for PTSD. Bias toward threat at recruitment and bias away from threat just before deployment predicted postcombat PTSD symptoms. Moreover, these threat-related attention associations with PTSD were moderated by genetic and environmental factors, including serotonin transporter (5-HTTLPR) genotype. The data “show plasticity in attentional components of threat processing in soldiers trained and deployed to combat duties,” concluded the researchers. “These changes in threat processing interact with combat exposure and genetic variability in the serotonin transporter gene to predict risk for PTSD symptoms.”The work was supported by the Leo and Julia Forchheimer Foundation in collaboration with Mount Sinai School of Medicine and by the Intramural Research Program of the National Institute of Mental Health.Wald I, Degnan K, Gorodetsky E, et al. “Attention to Threats and Combat-Related Posttraumatic Stress Symptoms: Prospective Associations and Moderation by the Serotonin Transporter Gene.” 2013. JAMA Psychiatry. February 13 [Epub ahead of print]. http://archpsyc.jamanetwork.com/article.aspx?articleid=1570377.Domestic Violence, Maternal Depression Have Early Effects on KidsResearchers at Indiana University School of Medicine recently evaluated the effects of intimate-partner violence (IPV) and maternal depression on a population of children who have not been well-studied: those who have not yet reached school age. IPV is defined by the Centers for Disease Control and Prevention as “a pattern of coercive behaviors that may include repeated battering and injury, psychological abuse, sexual assault, progressive social isolation, deprivation, and intimidation.” Previous studies of IPV have focused on school-age children and children in high-risk samples.In this prospective study, researchers looked at more than 2,400 children receiving care from clinics that implemented the Child Health Improvement Through Computer Automation (CHICA) system. They linked parental IPV and depression with subsequent billing and pharmacy data during the November 1, 2004, to June 7, 2012, period. They found that 5.2 percent of parents reported IPV and 31.5 percent reported depressive symptoms at least once during routine pediatric visits within the first three years of a child’s life; 2.4 percent of the sample reported both. Exposure to both IPV and depression before age 3 was associated with preschool-aged onset of attention-deficit/hyperactivity disorder (ADHD), and early exposure to parental depression was associated with being prescribed psychotropic medications. “Pediatricians play a critical role in performing active, ongoing surveillance of families with these known social risk factors and providing early intervention to negate long-term sequelae,” concluded the researchers. Bauer N, Gilbert A, Carroll A, et al. “Associations of Early Exposure to Intimate Partner Violence and Parental Depression With Subsequent Mental Health Outcomes.” 2013. JAMA Pediatr. February 4 [Epub ahead of print]. http://archpedi.jamanetwork.com/article.aspx?articleid=1567228&utm.Diagnostic Criteria for Misophonia PresentedResearchers at the University of Amsterdam have presented a description of and criteria for diagnosis of a new and discrete psychiatric disorder they have termed misophonia. The condition is a preoccupation with a specific aversive human sound that triggers impulsive aggression. The researchers recruited through a hospital Web site 42 patients who reported misophonia. All patients were interviewed by an experienced psychiatrist and screened with a version of the Yale-Brown Obsessive-Compulsive Scale, which the researchers named the Amsterdam Misophonia Scale (A-MISO-S). On a six-item scale (range 0–24) patients were asked about the (1) time they spent on misophonia; (2) interference with social functioning; (3) level of anger; (4) resistance against the impulse; (5) control they had over their thoughts and anger; and (6) time they spent avoiding misophonic situations. “We found in all patients a similar pattern of intense anger when hearing certain human sounds, impulsive reactions, avoidance of cue-related situations, worry of losing control, and the occurrence of obsessive-compulsive personality traits,” they said, noting that the symptoms they described cannot be classified in the current DSM-IV TR or ICD-10 systems.Schroder A, Vulink N, and Denys D. “Misophonia: Diagnostic Criteria for a New Psychiatric Disorder.” 2013. PLoS ONE 8 (1): e54706. http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0054706.Depression May Diminish Response to Shingles VaccineIndividuals with untreated depression may have a higher risk of developing shingles, developing more severe cases of shingles, and being less responsive to the shingles vaccine than nondepressed individuals, said researchers at the Cousins Center for Psychoneuroimmunology at the UCLA Semel Institute for Neuroscience. Their study, part of the Shingles Prevention Study (SPS), was designed to evaluate the association between major depression and immune responses to a high-titer live attenuated varicella zoster virus (VZV) vaccine (zoster vaccine), which boosts cell-mediated immunity (CMI) to VZV and decreases incidence and severity of herpes zoster (HZ). The depression substudy was a two-year longitudinal cohort study of 92 community-dwelling adults aged 60 and over.The researchers found that depressed patients have diminished VZV-CMI responses to zoster vaccine, and treatment with antidepressant medication was associated with normalization of these responses. “Because higher levels of VZV-CMI correlate with lower risk and severity of HZ, untreated depression may increase the risk and severity of HZ and reduce the efficacy of zoster vaccine,” they concluded. ■Irwin M, Levin M, Laudenslager M, et al. “Varicella Zoster Virus-Specific Immune Responses to a Herpes Zoster Vaccine in Elderly Recipients With Major Depression and the Impact of Antidepressant Medications.” 2013. Clin Infect Dis. February 13 [Epub ahead of print]. http://cid.oxfordjournals.org/content/early/2013/02/12/cid.cis1208.abstract. ISSUES NewArchived

**Решение:** -1 обзор литературы / концептуальная статья

---

### 143 · R0499

**Noise sensitivity or hyperacusis? Comparing the Weinstein and Khalfa questionnaires in a community and a clinical samples.**

2024 · Hearing research · article, journal article, review · eng · https://doi.org/10.1016/j.heares.2024.108992

Noise sensitivity and hyperacusis are decreased sound tolerance conditions that are not well delineated or defined. This paper presents the correlations and distributions of the Noise Sensitivity Scale (NSS) and the Hyperacusis Questionnaire (HQ) scores in two distinct large samples. In Study 1, a community-based sample of young healthy adults (n = 103) exhibited a strong correlation (r = 0.74) between the two questionnaires. The mean NSS and HQ scores were 54.4 ± 16.9 and 12.5 ± 7.5, respectively. NSS scores displayed a normal distribution, whereas HQ scores showed a slight positive skew. In Study 2, a clinical sample of Veterans with or without clinical comorbidities (n = 95) showed a moderate correlation (r = 0.58) between the two questionnaires. The mean scores were 66.6 ± 15.6 and 15.3 ± 7.3 on the NSS and HQ, respectively. Both questionnaires' scores followed a normal distribution. In both samples, participants who self-identified as having decreased sound tolerance scored higher on both questionnaires. These findings provide reference data from two diverse sample groups. The moderate to strong correlations observed in both studies suggest a significant overlap between noise sensitivity and hyperacusis. The results underscore that NSS and HQ should not be used interchangeably, as they aim to measure distinct constructs, however to what extent they actually do remains to be determined. Further investigation should distinguish between these conditions through a comprehensive psychometric analysis of the questionnaires and a thorough exploration of psychoacoustic, neurological, and physiological differences that set them apart.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 144 · R1380

**Misofonia: Quando o som não embala mas abala**

2016 · Revista de Ciências Médicas e Biológicas · article, other literature type · pt · https://doi.org/10.9771/cmbio.v15i3.18198

&lt;p class="Normal1"&gt;&lt;strong&gt;Introdução&lt;/strong&gt;: a misofonia é uma condição crônica caracterizada por experiências emocionais desagradáveis em resposta a sons específicos. Existem poucos estudos que podem contribuir para o desenvolvimento de um modelo teórico para entender a misofonia e os fenômenos relativos a ela, bem como o seu tratamento.&lt;strong&gt; Objetivo:&lt;/strong&gt; revisar a literatura sobre a misofonia e suas implicações, diagnóstico e possíveis tratamentos, numa perspectiva atual. &lt;strong&gt;Metodologia:&lt;/strong&gt; foi realizada uma busca na literatura nas principais bases de dados online, utilizando o termo misofonia. Após análise dos resumos, 13 artigos foram selecionados para análise detalhada. &lt;strong&gt;Resultados:&lt;/strong&gt; pouco ainda se sabe sobre os aspectos fisiopatológicos da misofonia e acredita-se que há um envolvimento dos sistemas límbico e autonômico na severidade das respostas aos chamados sons gatilhos. Os principais sons que desencadeiam respostas de aversão no indivíduo misofônico envolvem mastigação, respiração e outros sons de padrão repetitivo. Não há um consenso no melhor método diagnóstico desta condição e o tratamento também não segue uma padronização, podendo envolver terapia de habituação ao som, terapia cognitivo comportamental e utilização de medicamentos. &lt;strong&gt;Conclusão: &lt;/strong&gt;a misofonia é uma condição que se mostra cada vez mais comum e que pode afetar muito a vida do indivíduo que a possui, no entanto, o entendimento sobre o mecanismo neurobiológico, os aspectos fisiopatológicos, a caracterização clínica, o diagnóstico e tratamento desse fenômeno ainda é evasivo.&lt;/p&gt;

**Решение:** -1 обзор литературы / концептуальная статья

---

### 145 · R1493

**Improvement in Hyperacusis with Tinnitus Retraining Therapy**

2011 · Otolaryngology · article · en · https://doi.org/10.1177/0194599811415823a269

Objective Decreased sound tolerance and hyperacusis are frequently found in patients who complain of tinnitus. This study aims to investigate the efficacy of Tinnitus Retraining Therapy (TRT) in patients with hyperacusis. Method Prospective study of patients with hyperacusis presenting to the tinnitus clinic in a tertiary referral otorhinolaryngology unit. Hyperacusis was confirmed with loudness discomfort level (LDL) measurements. Audiometry was performed in all patients. Improvement of hyperacusis following TRT was measured by structured interview with aid of questionnaires and visual analogue scores. Results A total of 197 patients were studied. Improvement was achieved in 39%. Environmental sound (70%), Viennatone broadband noise generator (18%) and Marsona sound generator (5%) were used. 18% had hearing aids (HA) fitted even though 73% had hearing loss. Patients who opted for HA complained of worse effects of hyperacusis on life. Age, gender, and presence of hearing loss were similar in patients who did and did not improve. Duration of treatment was longer in patients that improved ( P &lt;. 01). Improvement with Viennatone was significantly higher than with environmental sounds alone (49% vs 35%, P &lt;. 05), especially when used in presence of hearing loss (61%). Conclusion Modest proportion of patients with hyperacusis improved with TRT. Use of broadband noise generators and longer duration of therapy appear to give better success rates. Overall success of TRT in patients with hyperacusis may also be related to underlying medical problems such as thyroid conditions and multiple sclerosis.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 146 · R1283

**UvA-DARE ( Digital Academic Repository ) Investigating Misophonia : A Review of the Empirical Literature , Clinical Implications , and a**

2018 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 обзор / комментарий / письмо

---

### 147 · R0434

**The Neurochemistry of Decreased Sound Tolerance: A Magnetic Resonance Spectroscopy (MRS) study of Misophonia and Hyperacusis**

2025 · PsyArXiv · preprint · en · https://doi.org/10.31234/osf.io/d49uq_v1

This study examined the concentrations of excitatory and inhibitory neurotransmitters (glutamate and GABA respectively) in two regions of interest (auditory and insular cortices) and a control region (visual cortex) to test the hypothesis that decreased sound tolerance would be linked to increased cortical excitability (more glutamate and/or less GABA). Misophonia (negative emotional responses to specific sounds) and hyperacusis (finding sounds atypically loud) were separately considered and key comorbidities excluded (tinnitus, migraine, autism). A MEGA-PRESS sequence was used for auditory cortex to optimise the detection of GABA. We found no significant group differences in neurotransmitter in any region and pre-registered Bayesian analyses suggested that these are sensitive null results. By contrast, we found increased brain volumes in the auditory cortex (for both misophonia and hyperacusis) and insula (misophonia only). These findings argue against the idea that decreased sound tolerances are linked to neurochemically-driven differences in excitation/inhibition but support the conclusion that they are linked to structural brain differences.

**Решение:** ? случай-контроль (MRS спектроскопия мизофонии и гиперакузии), проверить скрининг пула

---

### 148 · R1201

**Is Misophonia a Psychiatric Condition**

2020 · Journal watch · article · en · https://doi.org/10.1056/nejm-jw.na51421

Misophonia is a condition marked by “hatred of sound.” Typically, it is characterized by sensitivity to another person's chewing, snorting, or

**Решение:** -1 обзор литературы / концептуальная статья

---

### 149 · R1497

**Correlation between hyperacusis measurements in daily ENT practice.**

2010 · International journal of audiology · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.3109/14992020903160868

Olivier M. Meeus*a, Mattias Spaepena, Dirk De Ridderb & Paul H. Van de Heyningaa *University Department of Otorhinolaryngology and Head and Neck Surgeryb University Department of Neurosurgery Brain Research Center Antwerp for Innovative & Interdisciplinary Neuromodulation (BRAI2N) Antwerp University Hospital (UZA), University of Antwerp, Edegem, BelgiumOlivier M. Meeus, University Department of Otorhinolaryngology and Head and Neck Surgery, Antwerp University Hospital (UZA), University of Antwerp, Wilrijkstraat 10, B-2650 Edegem, Belgium. E-mail: olivier.meeus@uza.be AbstractThe aim of this study was to investigate hyperacusis measurement tools and to assess the correlation between diagnostic methods for hyperacusis in daily ENT practice. We studied two hyperacusis questionnaires: the Hyperacusis Questionnaire (HQ) and the Multiple-Activity Scale for Hyperacusis (MASH), audiometric measurements (uncomfortable loudness level (ULL) and dynamic range (DR)), and the questions ‘Do you have a lower tolerance for noise… ?’ and ‘Are you afraid of noise?’ Hyperacusis was assessed in 46 patients presenting with primary complaints of tinnitus. A validated Dutch version of the HQ is provided. A correlation was found between scores on the HQ and the MASH (p=0.000, R2=0.34). Significantly higher scores for both questionnaires were found in patients reporting decreased sound tolerance (p=0.000 and 0.002, respectively) or fear of noise (p=0.002 and 0.004, respectively). Overall, no correlations were found between scores on questionnaires and audiometric values including ULL and DR. The HQ and MASH were confirmed to be valid measurement tools for hyperacusis complaints. No correlations were found between audiometric measurements and hyperacusis complaints.SumarioEl objetivo de este estudio fue investigar las herramientas para mediar la hiperacusia y evaluar la correlación entre métodos diagnósticos para hiperacusia en la práctica diaria otorrinolaringológica. Estudiamos dos cuestionarios para hiperacusia: El Cuestionario de Hiperacusia (HQ) y la Escala de Multi-actividades para Hiperacusia (MASH), mediciones audiométricas (el nivel molesto de intensidad (ULL) y el rango dinámico (DR); y las preguntas ¿Tiene usted poca tolerancia al ruido?, y ¿Le da miedo el ruido?. La hiperacusia se evaluó en 46 pacientes cuya principal molestia era el acufeno. Se presenta una versión validada de HQ en holandés. Se encontró una correlación entre las puntuaciones del HQ y del MASH (p=0.000, R2=0.34). Se encontraron puntuaciones significativamente más altas para ambos cuestionarios en pacientes que reportaban una tolerancia disminuida al ruido (p=0.000 y 0.002, respectivamente) o miedo al ruido (p=0.002 y 0.004 respectivamente). En general, no se encontraron correlaciones entre la puntuación en los cuestionarios y los valores audiométricos de ULL y DR. Se confirmó que el HQ y el MASH son herramientas válidas para la medición de las quejas de una hiperacusia. No se encontró correlación entre las mediciones audiométricas y las quejas de una hiperacusia.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 150 · R1192

**Donald Trump, Boris Johnson, and other leaders win Ig Nobel awards for teaching people about life and death**

2020 · BMJ · article · en · https://doi.org/10.1136/bmj.m3675

Politicians are better than doctors or scientists at medical education. Leaders such as Donald Trump, Vladimir Putin, Alexander Lukashenko, Boris Johnson, Jair Bolsonaro, Narendra Modi, Andres Manuel Lopez Obrador, Recep Tayyip Erdogan, and Gurbanguly Berdimuhamedow of Turkmenistan have used covid-19 to teach their citizens about life and death. For their efforts they jointly won the 2020 Ig Nobel prize for medical education, although none of them showed up to make an acceptance speech. The Ig Nobel awards are given for achievements that first make people laugh and then make them think. The 30th awards were virtually handed out on 17 September by real Nobel prize winners at …

**Решение:** -6 не про мизофонию
