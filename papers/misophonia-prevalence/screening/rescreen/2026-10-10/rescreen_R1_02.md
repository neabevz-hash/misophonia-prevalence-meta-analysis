# Повторный отбор вслепую, часть 2

Записи 151–300 из 790: всё, что ИИ исключил, кроме калибровочной выборки. Повторный отбор вслепую по правилу защиты (протокол, §11b). **Меток и причин ИИ в этом файле нет** — решайте с нуля по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261011).

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

### 151 · R0092

**Subcortical encoding of harmonicity and frequency in autism: Insights from frequency-following responses**

2026 · The Journal of the Acoustical Society of America · article · en · https://doi.org/10.1121/10.0042534

Autistic individuals often exhibit atypical sound perception, yet the specific acoustic properties involved-beyond sound intensity-remain unclear. This study examined whether subcortical processing of harmonicity and frequency differs in autistic children, potentially contributing to altered auditory experiences. Frequency-following responses (FFRs) were recorded from 15 autistic boys (ages 7-14) and nine age-matched neurotypical (NT) boys. In Experiment 1, participants heard three complex tones varying in their degree of harmonicity. No group differences emerged in FFRs to either the envelope or fine structure, suggesting comparable subcortical encoding of harmonicity. In Experiment 2, participants were presented with complex tones differing in the frequency of partials and/or fundamental frequency. Autistic children showed significantly weaker envelope responses across all stimuli and reduced fine structure responses around 500 Hz, while responses at lower and higher frequencies matched NT peers. These findings suggest that atypical subcortical encoding of frequency-specific information may contribute to altered sound perception in autism. Larger-scale studies are needed to confirm these results and connect them to behavioral measures.

**Решение:** -6 не про мизофонию

---

### 152 · R0995

**Characterizing Interoceptive Differences in Autism: A Systematic Review and Meta-analysis of Case–control Studies**

2022 · Journal of Autism and Developmental Disorders · article · eng · https://doi.org/10.1007/s10803-022-05656-2

Interoception, the body's perception of its own internal states, is thought to be altered in autism, though results of empirical studies have been inconsistent. The current study systematically reviewed and meta-analyzed the extant literature comparing interoceptive outcomes between autistic (AUT) and neurotypical (NT) individuals, determining which domains of interoception demonstrate robust between-group differences. A three-level Bayesian meta-analysis compared heartbeat counting performance, heartbeat discrimination performance, heartbeat counting confidence ratings, and self-reported interoceptive attention between AUT and NT groups (15 studies; nAUT = 467, nNT = 478). Autistic participants showed significantly reduced heartbeat counting performance [g = - 0.333, CrI95% (- 0.535, - 0.138)] and higher confidence in their heartbeat counting abilities [g = 0.430, CrI95% (0.123, 0.750)], but groups were equivalent on other meta-analyzed outcomes. Implications for future interoception research in autism are discussed.

**Решение:** -6 не про мизофонию

---

### 153 · R0073

**A genomic study of trichotillomania and excoriation disorder in families.**

2026 · Translational psychiatry · journal article · eng · https://doi.org/10.1038/s41398-026-04164-6

Trichotillomania and excoriation disorder are obsessive-compulsive related disorders that are often subclassified together as body-focused repetitive behavior (BFRB) disorders. While previous research suggests shared genetic factors, the genetic architecture of these BFRBs remains incompletely understood. Probands with trichotillomania and/or excoriation disorder and both of their biological parents were recruited for an ongoing genetic study of parent-offspring trios with BFRBs. Genome-wide array data were generated in 110 families (334 individuals total) to investigate the role of both common single-nucleotide polymorphisms and rare copy-number variants (CNVs). Polygenic scores were calculated using summary statistics from genome-wide association studies of related psychiatric conditions, including obsessive-compulsive disorder (OCD), depression, anxiety, and attention-deficit/hyperactivity disorder. Using the polygenic transmission disequilibrium test (pTDT), we observed a significant over-transmission of the OCD polygenic score in probands of European ancestry from their parents (mean pTDT = 0.36, p = 0.01, n = 92), and a non-significant enrichment for the other conditions. Our results suggest that common variants associated with OCD may contribute to risk for BFRBs, consistent with their current classification as obsessive-compulsive related disorders. We also identified several rare CNVs in probands that overlapped genes intolerant to loss-of-function (LoF) mutations and those previously associated with neurodevelopmental disorders. The LoF-intolerant genes were enriched in biological processes relevant to synapse organization and neurodevelopment. This work provides new insight into the genetic underpinnings of these BFRB disorders, paving the way for larger genomic studies of these understudied conditions.

**Решение:** -6 не про мизофонию

---

### 154 · R1378

**A Possibility of Pupil Diameter as Reliable Index for Lie Detection**

2016 · International Journal of Psychophysiology · article · en · https://doi.org/10.1016/j.ijpsycho.2016.07.435

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 155 · R1513

**[Mechanisms and management of hyperacusis (decreased sound tolerance)].**

2006 · Acta otorrinolaringologica espanola · article, english abstract, journal article · spa · https://doi.org/10.1016/s0001-6519(06)78731-3

Hyperacusis is a decreased sound tolerance. Prevalence of the disease is described in 9-15% of the population, but this percentage increases among the tinnitus patients. Pathophysiological mechanisms involve some disruptions in the amplification and regulation processes of the external hair cells or affect the central sound processing at the subcortical level. The role of the serotonin, also involved in other diseases related with hyperacusis (migraine, depression), can be crucial in this disorder. Other theories confirm the effect of the endorphins that activate the excitatory function of the glutamate, the auditory neurotransmitter, increasing its toxicity. The activation of the limbic and autonomic nervous systems produces the emotional reaction of the hyperacusis (anxiety, fear and depression). Proposed treatments are based on acoustic stimulation by a progressive introduction of sound (tinnitus retraining therapy TRT). Noise generators and hearing aids can be fitted in severe cases. The role of some drugs involved in the metabolism of the serotonin open new approaches for the management of hyperacusis.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 156 · R1272

**Diplacusis**

2018 · Digital Commons @ East Tennessee State University · text

Book Summary: Hyperacusis and Disorders of Sound Intolerance: Clinical and Research Perspectives is a professional resource for audiology practitioners involved in the clinical management of patients who suffer from sound tolerance concerns. The text covers emerging assessment and intervention strategies associated with hyperacusis, disorders of pitch perception, and other unusual processing deficits of the auditory system. In order to illustrate the patients perspectives and experiences with disorders of auditory processing, cases are included throughout. This collection of diagnostic strategies and tools, evidence-based clinical research, and case reports provides practitioners with avenues for supporting patient management and coping. It combines new developments in the understanding of auditory mechanisms with the clinical tools developed to manage the effects such disorders exert in daily life. Topics addressed include unusual clinical findings and features that influence a patient s auditory processing such as their perceptual accuracy, recognition abilities, and satisfaction with the perception of sound. Hyperacusis is covered with respect to its effects, its relation to psychological disorders, and its management. Hyperacusis is often linked to trauma or closed head injury and the text also considers the management of patients with traumatic brain injury as an opportunity to illustrate the effectiveness of interprofessional care in such cases. Interventions such as cognitive behavioral therapy, self-efficacy training, and hearing aid use are reported in a way that enhances clinicians\u27 ability to weave such strategies into their own work, or into their referral system. Hyperacusis and Disorders of Sound Intolerance illuminates increasingly observed auditory-related disorders that challenge students, clinicians, physicians, and patients. The text elucidates and reinforces audiologists contributions to polytrauma and interprofessional care teams and provides clear definitions, delineation of mechanisms, and intervention options for auditory disorders

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 157 · R0262

**MISOPHONIA AND THE QUALITY OF SEXUAL LIFE IN COUPLES**

2025 · Journal of Hearing Science · article, journalarticle, google scholar result · und · https://doi.org/10.17430/jhs/214371

Introduction Misophonia or selective ‘hatred of sound’ is a newly recognized mental disorder characterised by negative emotional reactions, feelings, and thoughts with or without impulsive behavior to specific irritating triggering sounds. The term &lt;i&gt;misophonics&lt;/i&gt; has been used to refer to misophonia sufferers. A major effect reported by misophonics is a negative, or even ruinous, impact on close romantic relationships. The aim of our study was to evaluate the quality of sexual life (QoSL) in misophonics of both sexes and their close partners. Material and methods We enrolled 91 misophonics aged 25.1 ± 5.4 years old (24 males and 67 females) and 91 opposite-sex partners aged 27.3 ± 4.9 years old. Their misophonia was confirmed by use of the Amsterdam Misophonia Scale (A-Miso-S) questionnaire. For evaluation of the QoSL in male misophonics, we used the International Index of Erectile Function (IIEF) and the Sexual Quality of Life–Male (SQoL-M) self-report questionnaires. For female misophonics we used the self-report questionnaire Sexual Quality of Life–Female (SQoL-F) and the Female Sexual Function Index (FSFI). For comparison, the total scores from the misophonics were compared with scores from controls, who were healthy peers (91 males and 91 females who were loving couples) without misophonia. Results We found that the total SQoL-F scores in female misophonics were statistically lower than in controls (62.7 ± 3.5 vs 89.4 ± 4.7 in controls, &lt;i&gt;p&lt;/i&gt; = 0.004). In males with misophonia, the SQoL-M total score was 38.3 ± 4.2 vs 60.7 ± 4.6 in controls (&lt;i&gt;p&lt;/i&gt; = 0.002), while IIEF total scores were correspondingly 40.6 ± 5.8 and 68.1 ± 6.3 (&lt;i&gt;p&lt;/i&gt; = 0.001). Erectile function score in males with misophonia was 16.3 ± 2.4 vs 27.2 ± 2.8 in controls (&lt;i&gt;p&lt;/i&gt; = 0.003). Partners of misophonics of both sexes also demonstrated decreased scores in total IIEF, SQoL-M, SQoL-F, and FSFI. In female partners of misophonic males, SQoL-F total score was 71.4 ± 4.6 vs 89.4 ± 4.7 in controls (&lt;i&gt;p&lt;/i&gt; = 0.007). Erectile function score in male partners of misophonic females was 20.1 ± 3.2 vs 27.2 ± 2.8 in controls (&lt;i&gt;p&lt;/i&gt; = 0.015). In misophonics of both sexes who had comorbid mental disorders, the scores that characterized QoSL were even lower. Conclusions Misophonia decreases the quality of sexual life in sufferers of both sexes as well as their partners.

**Решение:** ? случай-контроль (91 пара), проверить скрининг пула

---

### 158 · R1450

**Help for Hyperacusis**

2014 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0000453391.20357.f7

Figure: © Kiki Tikiriki/Stock Illustration SourceIt took visits to five doctors over several months for Rob, a musician from Georgia who requested that his last name not be published, to be diagnosed with hyperacusis. At times, the process was scary and frustrating, he said. As a musician, Rob was always careful to use hearing protection around loud music, including in clubs and at concerts, he said. “In the work I do in a recording studio, I never set the volume loud.” He acquired hyperacusis shortly after exposure to the noise of a pressure washer. “I wasn't wearing hearing protection and didn't experience anything that was an immediate cause for concern,” Rob said. However, when he put on a CD in his car 30 to 40 minutes later, the music sounded louder and exceptionally sharper than normal in both ears. A couple of days later, he started to experience constant pain deep in his left ear. Rob then saw a neurologist, who suggested he undergo an MRI. “The doctor didn't tell me anything about the importance of wearing hearing protection during the MRI, and what was moderate hyperacusis, at best, became severe hyperacusis,” he said. A better understanding of hyperacusis is needed so that hearing healthcare professionals can more effectively diagnose and manage cases like Rob's, which have a great impact on a patient's quality of life. More research investigating the mechanisms of the disorder is crucial to improving treatment approaches and reimbursement policy. Several therapies for hyperacusis do exist, and they have shown some success in relieving patients’ discomfort. DEFINITION SOMETIMES UNCLEAR The definition of hyperacusis varies and is sometimes unclear, said Jennifer R. Melcher, PhD, associate professor of otology and laryngology at Harvard Medical School. In her research, she describes the condition as intolerance to a level of sound. People with hyperacusis reach a point at which sounds are too loud, even at lower physical levels, she said. Other terms used to describe decreased sound tolerance include phonophobia, the fear of a particular sound, and misophonia, a “negative reaction to a sound with a specific pattern and meaning,” according to Pawel J. Jastreboff, PhD, ScD, MBA, and Margaret M. Jastreboff, PhD, of Emory University School of Medicine. They describe hyperacusis as a negative reaction to a sound that depends only on the sound's physical characteristics, such as spectrum and intensity (Decreased Sound Tolerance (DST): Hyperacusis/Misophonia/Phonophobiahttp://www.hyperacusis.net/hyperacusis/misophoniaphonophobia/default.asp).Figure: Jennifer R. Melcher, PhDRichard S. Tyler, PhD, professor of communication sciences and disorders and of otolaryngology at the University of Iowa, describes four categories of hyperacusis: loudness, annoyance, fear, and pain. While he sees all of these subtypes intersecting in the clinic, epidemiological data on hyperacusis are lacking, “so it's hard to know how much overlap actually occurs,” he said. In loudness hyperacusis, moderately intense sounds are perceived as too loud, while annoyance hyperacusis is “a negative emotional reaction to sounds,” Dr. Tyler said. Fear hyperacusis is a negative response to sounds that may cause patients to avoid social situations or feel anxiety in anticipation of hearing these sounds. Pain is also associated with hyperacusis and may include a stabbing sensation at much lower sound levels than would typically prompt pain. One type of hyperacusis may lead to another, Dr. Tyler said. “If you experience loudness hyperacusis, emotional consequences may follow, leading to stress and annoyance, which eventually lead to fear of going to events and socializing,” he said. “Pain is a little more complicated because it consists of both a fundamental attribute and an emotional consequence.” People with hyperacusis have increased activity in the tensor tympani muscle in response to some sounds, which can tighten the eardrum and lead to pain, said Dr. Melcher, citing research published in Noise & Health (2013;15[63]:117-128http://www.noiseandhealth.org/article.asp?issn=1463-1741;year=2013;volume=15;issue=63;spage=117;epage=128;aulast=Westcott). “We often see pain in our patients,” said Fan-Gang Zeng, PhD, professor of otolaryngology in the School of Medicine and director of the Center for Hearing Research at the University of California, Irvine, and chair of The Hearing Journal’s Editorial Advisory Board. “When the sound reaches a certain level, patients will say, ‘It's not just the loudness that's bothering me; it's the pinging sensation or tingling.’” ONE IN 50,000 Hyperacusis is rare, affecting one in 50,000 people, according to the American Academy of Otolaryngology–Head and Neck Surgery (AAO-HNShttp://www.entnet.org/content/hyperacusis-increased-sensitivity-everyday-sounds). Prevalence rates were between eight and nine percent in a 2002 mail and Internet survey ( Int J Audiol 2002;41[8]:545-554http://informahealthcare.com/doi/abs/10.3109/14992020209056075), while other researchers have estimated a prevalence of two percent in the adult population. (Baguley DM, McFerran DJ. Hyperacusis and disorders of loudness perception. In: Møller A, Langguth B, De Ridder D, Kleinjung T, eds. Textbook of Tinnitus. New York, NY: Springer; 2011:13-24.) Hyperacusis appears to result from reduced nerve input and response to sound, Dr. Zeng said. As a result, the brain has no choice but to increase gain, causing over-amplification in its attempt to compensate. “The brain is dynamically changing in response to the environment and the pathological conditions in the ear,” he said. With the loudness form of the condition, “there is likely greater activity on individual hearing nerve fibers and across more hearing nerve fibers than would occur in the normal ear without hyperacusis,” Dr. Tyler said. If patients experience annoyance or fear, then the many corresponding emotional centers of the brain must also be activated. These networks are active for different types of stressors, not just hyperacusis, he noted. Hyperacusis is frequently associated with noise exposure and tinnitus (see box), but many patients have apparently normal hearing thresholds, Dr. Tyler said. Some patients with hyperacusis have high-frequency hearing loss, but the loss is not always reflected by the audiogram, Dr. Zeng said. Patients with hyperacusis are often bothered by sounds at all frequencies, provided they reach a certain decibel level, he added.Figure: Fan-Gang Zeng, PhDConditions that are associated with hyperacusis include Bell's palsy, Lyme disease, depression, and autism, among others, according to the American Speech–Language–Hearing Association (ASHA)http://www.asha.org/uploadedFiles/AIS-Hyperacusis.pdf. In addition to noise exposure, causes may include physical trauma to the head or viral infection of the inner ear. Audiologists can assess loudness hyperacusis by measuring loudness growth or loudness discomfort levels with pure tones, said Dr. Tyler, although some studies from the hearing healthcare literature use actual recordings of environmental sounds. Dr. Zeng finds that exposing patients to a conversational sound level of 60 to 70 dB and asking them to indicate if this level is too loud helps determine if they have hyperacusis, he said. Questionnaires are valuable for determining annoyance and fear components of the disorder, Dr. Tyler said. Generally, such assessments consist of subjective responses. “If patients say they're afraid to go to work or the cafeteria because it's too noisy, then, clinically speaking, you know they have fear hyperacusis,” he said. Audiologists also need to ask patients if they are experiencing any associated ear pain, he added. LOWERING THE VOLUME Counseling and sound therapy are two common approaches to managing hyperacusis. They can help retrain the brain and reduce the physiological activity that leads to the condition, Dr. Melcher said. Many counseling techniques are now available, Dr. Tyler said. For example, hyperacusis activities treatment includes components of cognitive behavior therapy, helping patients adjust their perceptions and providing techniques to improve concentration. “And, of course, when people change their feelings and impressions about a condition, something in the brain changes as well,” Dr. Tyler said. Sound therapy can be very effective for hyperacusis, he said. Data indicate that exposure to continuous low-level broadband noise can improve objective measures of loudness hyperacusis ( Semin Hear 2002;23[1]:21-34https://www.thieme-connect.com/products/ejournals/html/10.1055/s-2002-32944; Acta Otolaryngol 2005;125[5]:503-509http://www.ncbi.nlm.nih.gov/pubmed/16092541). While continuous broadband noise has been used to treat tinnitus and is now advocated for hyperacusis therapy, “white noise is not very effective compared with modulated dynamic sounds,” Dr. Zeng said. Another approach, successive approximation using high-level broadband noise, may be effective, said Dr. Tyler, adding that the therapy was recommended by the late Jack A. Vernon, PhD, cofounder of the American Tinnitus Association (ATA). This form of sound therapy involves noise exposure that increases in loudness and duration over time. (Tyler RS, Noble W, Coelho C, Haskell G, Bardia A. Tinnitus and hyperacusis. In: Katz J, Medwetsky L, Burkard R, Hood L, eds. Handbook of Clinical Audiology. 6th ed. Philadelphia, PA: Lippincott Williams & Wilkins; 2009:726-742.)Figure: Richard S. Tyler, PhD“We have also used successive approximation to the specific environmental sounds that bother a patient,” Dr. Tyler said, noting that this technique can be very helpful for children with hyperacusis. If patients complain of hyperacusis at 50 dB, audiologists can expose them to a lower sound level and then gradually increase exposure over time in 5-dB steps until 50 dB is tolerable, according to an idea developed by Craig Formby, PhD, Dr. Zeng said ( J Acoust Soc Am 2003;114[1]:55-58http://scitation.aip.org/content/asa/journal/jasa/114/1/10.1121/1.1582860). Once 50 dB is acceptable, audiologists can continue increasing the sound level exposure in 5-dB steps. Dr. Zeng and his colleagues have had some success with this adaptation process. However, the technique of “increasing tolerance has not been widely adopted,” he said. “There are also questions about what is the most effective type of sound. Is it white noise, such as the ocean, or dynamic sounds, such as speech or music?” Another approach to sound therapy includes partial masking with continuous background noise, which can help reduce the loudness of sounds that patients might find bothersome, Dr. Tyler said. If the patient wears a hearing aid, the amplified sound levels may need to be lowered and then gradually increased to contend with hyperacusis. UNCOVERING THE CAUSE While therapies for hyperacusis are available, treatment codes are not, so reimbursement for audiologists is challenging, Dr. Tyler said. Once more effective treatments are established, the healthcare system will likely provide better reimbursement, Dr. Zeng said. The effectiveness of hyperacusis therapy needs to be comparable to that of other reimbursable audiological treatments, such as cochlear implants, he said. “First, you have to have the research, with good quality-of-life outcomes.” Additional clinical trials are essential, Dr. Tyler said. Investigators need a better understanding of how to measure loudness hyperacusis while taking emotional influences into account. Studies also must evaluate the use of sound therapy and more specific counseling procedures for hyperacusis treatment. In addition, further research needs to investigate the causes of hyperacusis, the physiological changes that occur in the inner ear and nerves, and the brain's response, in addition to how sound can affect pain receptors, Dr. Zeng said. “We really need some kind of biomarker to objectively measure the condition,” he said. “It's almost impossible to create effective treatments until we know what causes the condition.” In the case of Rob, the musician from Georgia, an audiologist at Emory University recommended Tinnitus Retraining Therapy (TRT) as a treatment for hyperacusis. However, Rob found the presentation of sound in TRT too difficult to tolerate, so he opted for customized pink noise. His pink noise program used open-air headphones and started with a high-end frequency presentation of 3,000 Hz. He listened to this for eight hours a day at a low volume for three months, gradually increasing the volume during the second and third months. Rob also gradually increased the high-end frequency of the presentation, as well as the amplitude of selected frequency points. He can now listen to 22,050 Hz. His loudness discomfort levels were originally in the 30- and 40-dB range, and now they're in the 90- and 100-dB range. Overall, his therapy has taken about three years, and Rob said he believes his sound tolerance can further improve. “It took me a long time to get there, but it's been very successful,” he said. Hyperacusis and Tinnitus: Two Related, but Very Different, Conditions When patients with tinnitus are tested for loudness discomfort levels, they often cannot tolerate louder sounds, as demonstrated in research by Jennifer R. Melcher, PhD, associate professor of otology and laryngology at Harvard Medical School, and colleagues ( J Neurophysiol 2010;104 [6]:3361-3370http://jn.physiology.org/content/104/6/3361.long). “There's more hyperacusis in people with tinnitus,” Dr. Melcher said. In MRI neuroimaging studies of patients, she found increased responses to sound in the inferior colliculus in people with hyperacusis, regardless of whether they had tinnitus. This finding demonstrates amplification in brain activity, which leads to a perception of loudness, she said. When evaluating patients, practitioners should ask those who have tinnitus about loudness discomfort, Dr. Melcher said. Conversely, patients who present with hyperacusis should be evaluated for tinnitus, she said. While a lot of patients with tinnitus have hyperacusis, some people with tinnitus say that loud noises make their tinnitus worse, and this symptom should not be classified as hyperacusis, Dr. Tyler said. Even though hyperacusis treatment is rooted in tinnitus management, the two conditions are very different, Dr. Zeng said. Tinnitus is the perception of sound when there is no external stimulus to the ear, he noted. Hyperacusis is over-reaction to external sound. “You have to have an external stimulus that is perceived as loud,” he said.

**Решение:** -1 колонка / обзор (The Hearing Journal)

---

### 159 · R0149

**Who benefits most? Exploring demographic and psychological predictors of misophonia psychotherapy outcomes.**

2026 · Cognitive behaviour therapy · article, journal article, journalarticle · eng · https://doi.org/10.1080/16506073.2026.2655348

Misophonia is characterized by intense emotional and physiological responses to specific auditory triggers, typically repetitive, human-generated sounds. Treatment research in misophonia is nascent, with several studies showing promising outcomes across a range of treatments. While these findings suggest that misophonia symptoms are responsive to psychological interventions, more research is needed to identify which treatments are most effective, and for whom. This study examined baseline prognostic factors of treatment outcome from a randomized controlled trial for adults with misophonia, comparing acceptance and commitment therapy to progressive relaxation training for misophonia. Using multilevel modeling, the following baseline variables were tested as prognostic factors of clinician- and self-reported misophonia symptoms over time: age, age of misophonia onset, number of comorbid psychological diagnoses, psychological flexibility, and baseline misophonia severity. While exploratory, the findings suggest that older age, earlier age of onset and greater comorbidity, psychological inflexibility, and baseline symptom severity have small-to-moderate clinical and statistical effects on the longitudinal maintenance of treatment gains. Together, these findings highlight the complexity of treating misophonia and identifying potential treatment responders early on.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 160 · R0813

**TRANSTORNO DO PROCESSAMENTO AUDITIVO CENTRAL E MISOFONIA: ESTUDO DE CASO**

2023 · Atena Editora · part of book or chapter of book, book-chapter · pt · https://doi.org/10.22533/at.ed.2672322035

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 161 · R1387

**Characteristics of hyperacusis in the general population**

2016 · Noise and Health · article · en · https://doi.org/10.4103/1463-1741.189244

There is a need for better understanding of various characteristics in hyperacusis in the general population. The objectives of the present study were to investigate individuals in the general population with hyperacusis regarding demographics, lifestyle, perceived general health and hearing ability, hyperacusis-specific characteristics and behavior, and comorbidity. Using data from a large-scale population-based questionnaire study, we investigated individuals with physician-diagnosed (n = 66) and self-reported (n = 313) hyperacusis in comparison to individuals without hyperacusis (n = 2995). High age, female sex, and high education were associated with hyperacusis, and that trying to avoid sound sources, being able to affect the sound environment, and having sough medical attention were common reactions and behaviors. Posttraumatic stress disorder, chronic fatigue syndrome, generalized anxiety disorder, depression, exhaustion, fibromyalgia, irritable bowel syndrome, migraine, hearing impairment, tinnitus, and back/joint/muscle disorders were comorbid with hyperacusis. The results provide ground for future study of these characteristic features being risk factors for development of hyperacusis and/or consequences of hyperacusis.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 162 · R0263

**A case of a child with misophonia and hyperacusis: assessment and management of auditory hypersensitivity**

2025 · conference paper

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 163 · R0312

**The overlooked reality of Misophonia: Urging scientific and clinical inquiry.**

2025 · General hospital psychiatry · article, letter, lettersandcomments · eng · https://doi.org/10.1016/j.genhosppsych.2025.04.013

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 редакционная статья / письмо

---

### 164 · R0866

**Misofonía: evaluación, diagnóstico y tratamiento; una revisión sistemática.**

2022 · DOAJ (DOAJ: Directory of Open Access Journals) · article, text/article · es · https://doi.org/10.34810/psicosompsiquiatrnum200405

RESUMEN Introducción. La misofonía es una condición caracterizada por una reacción psicofisiológica y emocional desproporcionada en respuesta a estímulos auditivos y/o visuales específicos, pudiendo causar un deterioro funcional en diversas áreas vitales. Objetivo. Realizar una búsqueda actualizada en la literatura científica publicada recientemente acerca de la misofonía, en concreto, su conceptualización, epidemiología, comorbilidad, neurobiología y neuropsicología, evaluación, diagnóstico, y tratamiento. Método. Revisión sistemática de artículos científicos desde el año 2017 hasta el 2021 en la base de datos Pubmed en inglés y español. Se ha incluído en la búsqueda el término misophonia en el título, así como los términos treatment, therapy, psychotherapy, intervention, psychology o mental health. Se han seleccionado 41 de los 45 artículos encontrados, siguiendo los criterios de inclusión y exclusión determinados. Resultados. Los síntomas de misofonía suelen producirse por desencadenantes, siendo los orales y nasales los más frecuentes, y la respuesta emocional puede ir de la incomodidad a la ira severa. Existen instrumentos de evaluación diseñados recientemente con buenas propiedades psicométricas, superando las limitaciones presentes en medidas anteriores. Se han propuesto criterios diagnósticos para la misofonia, aunque éstos no están incluidos en los sistemas de clasificación y manuales de referencia. Existe elevada comorbilidad entre la misofonía y los trastornos de ansiedad, depresivos, estrés postraumático y obsesivo compulsivo, entre otros, por lo que no existe consenso sobre si se trata o no de una entidad independiente. La terapia cognitivo-conductual muestra buenos resultados, así como la terapia por desensibilización y movimientos oculares y la terapia dialéctico conductual, con resultados prometedores en estudios de caso o muestra pequeña. Discusión. La misofonía es una condición de creciente interés. Existe una conceptualización de la misma, sin embargo, pese a que se han propuesto criterios diagnósticos, estos no han sido validados y no se incluye todavía en los sistemas de clasificación internacionales. Psicosomàtica y Psiquiatría, Núm. 20 (2022): enero-febrero-marzo

**Решение:** -1 обзор / комментарий / письмо

---

### 165 · R0759

**Sound sensitivity among people with autism spectrum disorder. A literature study on causes, strategies and treatments**

2023 · Gothenburg University Publications Electronic Archive (Gothenburg University) · article, text

Introduction: Sound sensitivity has been described as a common phenomenon among people with Autistic spectrum disorder (ASD). Sound sensitivity is an umbrella term that includes several different conditions. In this study the conditions hyperacusis, misophonia and phonophobia are addressed, as the conditions often occur together and have some similarities. Aim: Based on current research this study aims to investigate which hypotheses and theories exist about what causes sound sensitivity in people with ASD. The aim is also to summarize the treatments and strategies available for people with ASD who suffer from sound sensitivity and to some extent relate this to audiologist clinical practice. Material &amp; method: Descriptive literature study examining 12 scientific articles published between 1996 and 2022 from the Pubmed database. Results: Sound sensitivity in people with ASD may be caused by abnormality/dysfunction at the neural level. It could also be caused by dysfunction in the cochlea. Abnormalities in the brain anatomy/structure in people with AST have been hypothesized. Psychological factors such as lack of attentiveness have also been hypothesized. Regarding treatments and strategies, the articles have covered coping strategies, auditory training and technical equipment. The coping strategies studied had variable results, while auditory training and technical equipment showed positive results. However, the options are limited and not sufficiently researched. Conclusions: Research has shown a clear connection between sound hypersensitivity and ASD, but so far, no clear cause has been determined. Effective treatments and strategies are today limited. Audiologists with their expertise in hearing do not seem to be contributing much in the way of interventions in the clinical setting for this target group today, which is remarkable and can be seen as a major area of development.Bakgrund: Ljudöverkänslighet har visat sig vara ett utbrett fenomen hos personer med autismspektrumtillstånd (AST). Ljudöverkänslighet är ett paraplybegrepp som innefattar flera olika tillstånd. I denna studie behandlas tillstånden Hyperacusis, Misofoni samt Fonofobi, då tillstånden ofta förekommer tillsammans och har en del likheter. Syfte: Utifrån befintlig forskning syftar denna studie till att undersöka vilka hypoteser och teorier det finns om vad som orsakar ljudöverkänslighet hos personer med AST. Syftet är även att sammanfatta de behandlingar och strategier som finns för personer med AST som lider av ljudöverkänslighet och i möjlig mån relatera detta till audionomyrket. Material och metod: Beskrivande litteraturstudie baserat på 12 originalartiklar publicerade mellan 1996 och 2022. Sökningen av vetenskapliga artiklar har gjorts via databasen Pubmed. Resultat: Ljudöverkänslighet hos personer med AST kan bero på abnormalitet/dysfunktion på neural nivå. Det kan även bero på funktionsrubbning i cochlea. Avvikelser när det kommer till hjärnans anatomi/struktur hos personer med AST har framförts som hypotes. Även psykologiska faktorer, så som bristande uppmärksamhet har lagts fram som hypotes. Angående behandlingar och strategier har artiklarna tagit upp copingstrategier, auditiv träning och teknisk utrustning. Copingstrategierna som studerats hade varierande resultat, medan auditiv träning och teknisk utrustning visade goda resultat. Alternativen är dock begränsade och inte tillräckligt beforskade. Slutsatser: Forskning har visat på ett tydligt samband mellan ljudöverkänslighet och AST, men har hittills inte kunnat fastslå någon entydlig orsak. Effektiva behandlingar och strategier är begränsade idag. Audionomer med sin expertis inom hörsel verkar inte bidra med särskilt mycket åtgärder i klinisk verksamhet för denna målgrupp idag, vilket är anmärkningsvärt och kan ses som ett stort utvecklingsområde

**Решение:** -1 обзор литературы / концептуальная статья

---

### 166 · R1002

**Anger, fear and disgust in response to sounds**

2022 · OSF Registries · studyregistration/pre-registration · https://doi.org/10.17605/osf.io/jzmyb

Bothersome tinnitus, misophonia and hyperacusis share important characteristics and cause substantial distress to their sufferers, yet are still poorly understood. Research investigating underlying mechanisms is very limited. Both associative and non-associative learning accounts have been introduced in the past as possible explanations for severe aversive reactions to sounds. We expect to find support for the theory that the strong emotional reactions may stem from acquired meanings of the trigger sounds rather than from an (un)expected aversive event. The current literature remains inconclusive in terms of generating overarching theories and experimental paradigms. Therefore, the present project will consider and explore a referential learning account as a potential mechanism underlying aversive reactions to sounds. We aim to use qualitative research to explore possible unconditioned stimulus (US) – unconditioned response (UR) themes. The study involves conducting focus group discussions with three groups of people suffering from misophonia, hyperacusis or bothersome tinnitus. Thematic analysis and content analysis will be conducted to identify common themes to discover the underlying meaning attached to the sound that underlies the emotional reaction.

**Решение:** -7 protocol / preregistration without data

---

### 167 · R1545

**Auditory Deprivation , Inhibitory Circuits and Plasticity : Implications for the Comprehension of Tinnitus and Hyperacusis Keila**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 168 · R1371

**Plateware and slurping influence regular consumers׳ sensory discriminative and hedonic responses to a hot soup**

2017 · International Journal of Gastronomy and Food Science · article · en · https://doi.org/10.1016/j.ijgfs.2017.06.005

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 169 · R0588

**The effectiveness of cognitive-behavioral therapy on social isolation and anxiety sensitivity of adolescent girls with misophonia**

2024 · Clinical Psychology … · google scholar result · https://www.sid.ir/fileserver/je/832-466344-x-1894271.pdf

… A total of 30 participants with clinically significant misophonia symptoms were selected through purposive sampling and randomly assigned to experimental and control groups (15 …

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 170 · R0540

**MY EXPERIENCE Self And Else Living On The Receiving Ends Of Misophonia**

2024 · Unpublished · preprint, text/preprint · und · https://doi.org/10.13140/rg.2.2.15221.79847

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 171 · R1231

**Misofonía**

2019 · Facultad de Artes · es · https://core.ac.uk/download/323368339.pdf

La contaminación acústica es un fenómeno que afecta las grandes urbes en el mundo y que con el tiempo ha ido aumentando. Puede llegar a ser un problema para las personas, puesto que su impacto puede dañar físicamente el oído y ocasionar problemas de audición en un momento de la vida en que todavía se es joven. Según un informe en el 2015 de la Organización Mundial de la Salud, la contaminación acústica es el segundo problema ambiental después de la polución y las personas sufren no solo daños en su oído, sino problemas con relación a otras partes del cuerpo y la mente. Una reacción al sonido es la “misofonía”, que corresponde a la fobia que sienten algunas personas hacia algunos sonidos que, para el resto de la gente, pueden pasar desapercibidos. A partir de estos dos temas se creó una historia mediante el cómic como contribución a conocimiento y toma de consciencia del ruido como factor de riesgo de enfermedades acústicas.Noise pollution is a phenomenon that affects the big cities in the world and also has increased over time. It can be a problem for people, since its impact can physically damage the ear and cause hearing problems at a time in life when you are still young. According to a 2015 report by the World Health Organization, noise pollution is the second environmental problem after pollution and people suffer not only damage to their ear, but problems in relation to other parts of the body and mind. A reaction to sound is "misophony," which corresponds to the phobia that some people feel towards some sounds that, for the rest of the people, may go unnoticed. From these two themes, a story was created through a comic book, as a contribution to knowledge and awareness of noise as a risk factor for acoustic diseases.Maestro (a) en Artes VisualesPregrad

**Решение:** -1 обзорная публикация / словарный очерк

---

### 172 · R1089

**Misophonia Successfully Treated of With Fluoxetine: A Case Report.**

2021 · Clinical neuropharmacology · article, case reports, journal article · eng · https://doi.org/10.1097/wnf.0000000000000465

OBJECTIVE: A large number of people experience misophonia. In 2013, the Amsterdam Study Group recommended diagnostic criteria for misophonia. However, misophonia is not yet included in the Diagnostic and Statistical Manual of Mental Disorders. This report is the first report on drug use that directly affects misophonia and demonstrates a 14-year-old adolescent girl with misophonia successfully treated with fluoxetine. METHODS: The patient's misophonia symptoms had been continuing for approximately 2 years, and her quality of life was significantly reduced. Psychotherapy conditions could not be applied, and fluoxetine 10 mg/d was started and increased to 20 mg/d after a week. At the second-month follow-up, because of partial improvement, fluoxetine dose was increased to 30 mg/d. RESULTS: At the fourth-month follow-up, there was a 40% decrease in Amsterdam Misophonia Scale score with a 70% decrease in the children's global assessment scale scores. By the 16th week, the overall functionality level was good at the end. CONCLUSIONS: Fluoxetine may be used as an effective drug in the treatment of misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 173 · R0983

**“The Wind Cries Mary”: The Effect of Soundscape on the Prairie-Madness Phenomenon**

2022 · Historical Archaeology · article · en · https://doi.org/10.1007/s41636-022-00335-6

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 174 · R1373

**Association between tinnitus and hyperacusis in school staff in Stockholm - A quantitative study**

2016

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 175 · R1141

**Increased orbitofrontal connectivity in misophonia**

2020 · bioRxiv · article, other literature type, preprint · en · https://doi.org/10.1101/2020.10.29.346650

Abstract For individuals with misophonia, specific innocuous sensory stimuli - such as hearing another person chewing or breathing - evoke strong negative emotional and physiological responses, such as extreme anger, disgust, stress and anxiety. Instead people with misophonia do not experience or display atypical reactions to generic aversive sounds such as screams or nails scratching on a blackboard. Misophonia appears to be unrelated to neurological trauma or hearing deficit, and features a characteristic developmental pattern. Its aetiology is currently unknown. The few previous fMRI studies on misophonia showed that sufferers feature increased dorsal anterior insula activity during trigger vs. generic aversive sounds. While this effect likely reflects the saliency associated with the perception of trigger sounds in people with misophonia, in the present fMRI study we investigate the neural mechanisms underlying the emotional reaction to trigger stimuli. To this aim, we probe the task-dependent connectivity of mid-cingulate, medial premotor and ventrolateral premotor cortex. We observe that only in participants with misophonia the presentation of trigger audio-visuals prompts an increased interaction of these three brain regions with the lateral orbitofrontal cortex. This brain region is crucial for behavioural inhibition mediated by cognitive and emotional content (such as in reward-reversal learning) and is part of the temporo-amygdala-orbitofrontal network, which integrates visceral and emotional states with cognition and behaviour. We also observe that in people with misophonia trigger sounds prompt a significant increase in the interaction between mid-cingulate and the primary auditory cortex. Our study replicates previous results and expands the network of brain regions involved in misophonia. The involvement of the orbitofrontal cortex suggests a defective functioning of high-order integrative processes allowing the reappraisal of experience-dependent negative emotional association with harmless sensory stimuli, and sheds light on the mechanisms underlying the compulsive nature of the misophonic reaction. The increased interaction, rather than the overall activity, of the primary auditory cortex with the mid-cingulate supports the hypothesis that the emotional response in misophonia is subserved by an indirect auditory-limbic pathway processing the subjective valence of specific sounds, rather than their physical properties alone.

**Решение:** ? нейровизуализация fMRI (случай-контроль), проверить скрининг пула

---

### 176 · R1409

**Misophonia: A Conditioned Aversive Reflex Disorder**

2015 · Unpublished · other/ · https://doi.org/10.13140/rg.2.1.2843.6563

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 177 · R1148

**Misophonia: A Neurologic, Psychologic, and Audiologic Complex**

2020 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0000657984.74790.d5

iStock/nicoletaionescu, misophonia, pain, health.Figure 1: CBT-based case formulation model in distress caused by misophonia.36 Misophonia, pain, health.Box: Resources on Misphonia.Misophonia1 is a newly described condition that is still not thoroughly understood. To her credit, Marsha Johnson, AuD, was the first to informally discuss sensitivity to specific sounds in online support groups for patients with hyperacusis, and documented about 500 cases of similar sound sensitivity problems in the late 1990s (personal communication, Dec. 3, 2019). She designed the term selective sound sensitivity syndrome (S4), which is still used today to describe misophonia. Later, Margaret Jasterboff, PhD, and Pawel Jastreboff, PhD, coined the term misophonia (which conservatively means dislike of sound),1,2 and other scientists such as Tyler, et al., refer to essentially the same condition as annoyance hyperacusis.3 Misophonia is considered sound intolerance and oversensitivity to certain sounds, which can result in distraction and annoyance that may limit a person's ability to concentrate, think, and learn.4 Some of the trigger sounds include gum popping, lip-smacking, food chewing or crunching, throat clearing, nose sniffing, breathing, tapping, and clicking.3, 5-8 Misophonia has yet to be classified in the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition (DSM-V); and unfortunately, the scientific community has not reached a consensus to categorize this condition as an auditory, psychiatric/psychologic, or neurologic ailment. This lack of recognition not only prevents health care providers from officially classifying the disorder but also hinders affected individuals from seeking help. COEXISTING CONDITIONS Misophonia can be associated with high levels of anxiety9 and comorbid factors, including post-traumatic stress disorder (PTSD), obsessive-compulsive disorder (OCD), and anorexia.10,11 Autonomous sensory meridian response (ASMR), usually triggered by auditory and visual stimuli, has been associated with heightened levels of misophonia. ASMR is described as a relaxing tingling sensation that starts from the head and neck and spreads through the body.12 Although sound sensitivity and hyperacusis have been investigated in autism spectrum disorder (ASD),13,14 misophonia has not been explored in children and adults with ASD. Misophonia can also cause academic difficulties. Connie Porcaro, PhD, a university professor, was concerned about misophonia awareness among her peers in the academic community. In 2019, she designed a study to see how much the university instructors knew about misophonia and what they would do to accommodate students with this condition in their classrooms. Of the 686 survey participants, only 18.4 percent self-reported having knowledge of misophonia. Instructors who knew about this condition indicated that they would be willing to provide classroom accommodations for those who suffer from misophonia.4 UNDERLYING CAUSES & NEURAL CORRELATES The neural correlates of misophonia have been explored, with areas of interest that include the non-classical auditory pathway, limbic system, and auditory cortices.7, 15-18 Kumar and colleagues employed fMRI in individuals with misophonia while they were exposed to unpleasant trigger sounds.16 The researchers found increased neuronal activities in an area referred to as the anterior insular cortex (AIC). Although the findings of this study have been questioned by some researchers,19 it still is considered as one of the strongest pieces of evidence for a neurological origin of misophonia. It is believed that AIC, in general, is a major player in emotional awareness,20 and one can simply expect the increased responses in this area in individuals with misophonia when they are exposed to trigger sounds. Schröder and colleagues provided additional evidence for a neurobiological basis for misophonia. They studied the response of the N1 component of late auditory evoked potentials to oddball stimuli in a group of subjects with misophonia. Their findings indicated a reduced amplitude in N1 to oddball stimuli. They concluded that a neurobiological deficit in those with misophonia could potentially impair auditory processing of incoming stimuli.18 Another fMRI study has shown some correlations between misophonia and OCD. fMRI data have indicated that those with misophonia have perfectionist and compulsive behaviors.21 These findings may support the clinical observation of annoyance at chewing sounds in those with misophonia. Additionally, genetics may play a role in misophonia. Although no strong research supports a genetic basis of misophonia, Sanchez and Silva from Brazil have reported a family with 15 members with misophonia and a possible autosomal dominant inheritance.22 Anecdotally, some of our patients have reported a mutation in chromosome 5 when they checked their genetic makeup using commercially available kits. Interestingly, a gene by the name of TENM2, which is involved in brain development, has a cytogenic location at 5q34 (in chromosome 5, longarm region 3 band 4).23 MISOPHONIA EVALUATION No standard questionnaire has been developed for misophonia. During the evaluation, patients are usually asked to complete a set of surveys, such as the Misophonia Questionnaire,24 which has three subscales: the Misophonia Symptom Scale, Misophonia Emotions and Behaviors Scale, and Misophonia Severity Scale. Another useful tool is the Amsterdam Misophonia Scale (A-MISO-S),25 which is widely used in many clinics. There are no universally accepted protocols for misophonia evaluation. Dozier, et al., have proposed a set of diagnostic criteria for misophonia that employs a variety of misophonic stimuli, including both auditory and visual modalities.26 Some clinics may measure loudness discomfort levels, particularly if misophonia is associated with hyperacusis. Aazh and colleagues described the loudness level measures in a group of children and adolescents with tinnitus and hyperacusis, and noticed that the uncomfortable loudness levels (ULLs) were at least 20 dB lower at 8 kHz than at 250 Hz.27 These findings also provide important information on the assessment of misophonic triggers, such as high-pitched screeching, that are reported by some patients. MANAGEMENT PROTOCOLS & METHODS Misophonia can be managed through tinnitus retraining therapy (TRT), cognitive behavioral therapy (CBT), compassion training, distress tolerance, mindfulness, and acceptance-based treatment, among others.28 Comorbid conditions such as depression and anxiety could be treated with antidepressants and anxiolytics. Brout and colleagues recommended a multidisciplinary care pathway to develop coping skills through CBT, mindfulness, and behavioral change.29 In general, it is understood that mental health and comorbid factors such as anxiety and depression can exacerbate misophonic responses. Parental mental health has also been explored, and the effectiveness of treatment for sound sensitivity disorders has been shown to influence the treatment of people with a history of parental mental health illness.30, 31 TRT. TRT employs extensive counseling and sound therapy. In a study by Margaret and Pawel Jastreboff, on a relatively large number of patients with decreased sound tolerance disorders, 152 out of 184 patients with both misophonia and hyperacusis and 139 out of 167 patients with misophonia alone experienced improvements after TRT.32 In the clinical practice of Ali Danesh, PhD, the use of ear-level sound generators with pleasant signals such as Zen fractal music or other sounds streamed via a smartphone to a Bluetooth hearing device, combined with extensive counseling, were shown to be helpful in managing those with misophonia. However, no solid evidence-based data are available for this observation. CBT. Since the models describing hyperacusis and tinnitus have significant commonalities with misophonia, it can be presumed that the methods used to treat tinnitus and hyperacusis can also be effective for misophonia. The evidence-based and research-proven protocols for hyperacusis and tinnitus management support CBT.33-35 The CBT protocol for misophonia is designed to identify negative automatic thoughts (NATs) and examine the validity and truth behind those negative thoughts. After a few sessions, patients realize that most NATs such as anger, isolation, fear, or poor relationships are false perceptions. Aazh and colleagues provide a case formulation model for a CBT plan to manage misophonia.36 This model starts with the exploration of misophonia patients’ initial emotional responses, such as anger and irritation, and their physical complaints, such as tightening of the stomach, static-like tingling sensations on the skin, or pain, when exposed to trigger sounds. These physical sensations and initial emotional reactions to trigger sounds generate a series of negative thoughts that lead to further emotional and physical responses, which in turn result in evaluative thoughts, hence generating a vicious circle of thoughts (Fig. 1).36 The CBT-based interventional model for misophonia aims to break this cycle by assisting the patients in examining and exploring their negative thoughts so they can process and modify them. Although there is no quick fix or magic pill for misophonia, the use of sound therapies, behavioral modifications, and CBT seems to be promising. Further research will be able to show the effectiveness of other treatment methods, such as electrical and magnetic stimulations, in the search for misophonia management.

**Решение:** -1 колонка / обзор (The Hearing Journal)

---

### 178 · R1185

**Clinical and Health Affairs Hyperacusis and Misophonia The Lesser-Known Siblings of Tinnitus**

2020 · https://core.ac.uk/download/357525307.pdf

■ Hyperacusis (decreased sound tolerance) and misophonia (fear of sound) are two conditions about which little is known. Consequently, physicians often struggle when they encounter patients who are affected by them. This article attempts to educate the medical community about hyperacusis and misophonia, both of which can have devastating effects on the lives of patients, and ways to manage them. Hearing loss and tinnitus are the primary hearing-related reasons people seek help from physicians. There are, however, several lesser-known maladies that result in suffering and affect a person&apos;s quality of life. Among these are hyperacusis (decreased sound tolerance) and misophonia (dislike or fear of sound). The prevalence of these conditions is not welldocumented; however, it is believed that between 10% and 17% of the population experiences tinnitus and of that population, 37% requires specific treatment for hyperacusis and misophonia

**Решение:** -1 обзор литературы / концептуальная статья

---

### 179 · R1419

**Executive Control and Emotional Information Processing in Dissociation: A Task-Switching Study Reneé San Giorgi Hyperactivity in amygdala and auditory cortex in misophonia: preliminary results of a functional magnetic resonance imaging study**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (fMRI амигдалы и слуховой коры при мизофонии)

---

### 180 · R0421

**Symptom Dimensions of Pediatric Obsessive-Compulsive Disorder: Exploratory Examination of Associations with Clinical Features and Response to Cognitive-Behavioral Therapy.**

2025 · Journal of obsessive-compulsive and related disorders · journal article · eng · https://doi.org/10.1016/j.jocrd.2025.100969

Several overarching symptom dimensions have been identified within pediatric obsessive-compulsive disorder (OCD), including doubting, obsessing, washing, ordering, neutralizing, and hoarding. These unique symptom presentations may have important clinical implications, especially in terms of potentially distinct associations with age, functional impairment, insight, family accommodation, and symptoms of anxiety and depression. Such symptom dimensions may also differ in their responsiveness to cognitive-behavioral therapy (CBT). Existing literature on the features associated with and the clinical impact of OCD dimensions has primarily focused on adults and has often employed measures that make standardized categorization of OCD dimensions across studies more challenging. In the present exploratory study, we examined the clinical features and treatment outcomes associated with different OCD symptom dimensions measured by the Obsessive-Compulsive Inventory-Children's Version (OCI-CV) using data from a previously completed clinical trial. A secondary analysis of data collected from 161 primarily White/non-Hispanic youth (M age = 12.19) enrolled in a randomized control trial of d-cycloserine-augmented CBT with exposure and response prevention revealed differential relations between clinical features and OCD symptom dimensions at baseline, particularly related to doubting symptoms which were associated with all measured clinical features except insight. However, the rate of improvement in OCD symptom severity during CBT did not differ as a function of OCD symptom dimension. The present study provides evidence that youth can benefit from CBT despite differences in clinical features associated with OCD symptom dimensions. Findings suggest that mental health providers can deliver idiographically tailored gold standard CBT flexibly to youth regardless of OCD symptom dimensionality.

**Решение:** -6 не про мизофонию

---

### 181 · R1317

**Soundbites : Diagnosis, neural mechanisms and treatment of misophonia**

2018 · Data Archiving and Networked Services (DANS) · dissertation, other · en · https://core.ac.uk/download/555923834.pdf

Misophonia (meaning hatred of sound) is a novel condition in which patients experience irritation, anger and disgust, triggered by sounds produced by other human beings. These intense emotions lead to severe suffering and social disfunctioning. The aim of this thesis was to lay a first foundation for understanding misophonia by addressing three core issues: 1. What is misophonia? 2. What happens in the brain of someone with misophonia during the misophonic reaction? 3. How can we treat misophonia? Our findings suggest that misophonia can be considered a separate psychiatric disorder. This is further underlined by our two neurobiological studies, using EEG and fMRI paradigms. Automatic processing of ordinary sounds is aberrant in misophonia patients. Subsequently, when they are confronted with misophonic triggers in a fMRI scanner, patients indeed feel anger and disgust and experience physiological arousal which is also visible in brain activation patterns. Importantly, misophonia symptoms can be reduced by a combination of four cognitive behavioral therapy techniques.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 182 · R0568

**Evaluation and Treatment of Central Auditory Processing and Sound Tolerance Disorders**

2024 · ISU ReD: Research and eData · text · en · https://core.ac.uk/download/599426297.pdf

Abstract 1 Introduction: Central auditory processing disorder (CAPD) affects how a listener understands speech even though their peripheral auditory system is intact. Case Presentation: An adult female was seen for a CAPD evaluation after experiencing recent listening difficulties following an automobile accident while 20 weeks pregnant. Results from a comprehensive audiological evaluation revealed audiometrically normal hearing in both ears. Results from the CAPD evaluation suggested a prosodic deficit. Discussion: Although results from testing were consistent with a prosodic deficit, the patient’s case history, original complaints, and recommendations were more consistent with an integration deficit. Conclusion: This case demonstrates that clinicians should thoroughly examine a patient’s clinical history. For this case, recommendations aligned with an integration deficit, as opposed to a prosodic processing disorder. Abstract 2 Introduction: A sound tolerance disorder is when individuals have adverse (either physical or emotional) responses to everyday sounds. A sound tolerance disorder is a broad term that encompasses tinnitus, hyperacusis, misophonia, and phonophobia. Case Presentation: A young adult female was seen for a sound tolerance evaluation. Results from an audiological evaluation revealed normal hearing thresholds and results from a sound tolerance evaluation indicated that a majority of responses to uncomfortable listening levels were in the normal range, which is consistent with hyperacusis. Discussion: Due to reduced uncomfortable listening levels, the patient was diagnosed with hyperacusis and misophonia, and extensive counseling was conducted. The counselor explained what hyperacusis was and presented the various treatment options available to the patient, including sound therapy and cognitive behavioral therapy. Conclusion: This case demonstrates that there may be multiple options available to aid in successful treatment for the patient, while some options may require collaboration with mental health professionals

**Решение:** -1 обзор литературы / концептуальная статья

---

### 183 · R0251

**Effects of Auditory Training on Sound Tolerance, Acceptance of Noise and Perceived Noise Sensitivity in Individuals with Hyperacusis**

2025 · ResearchSpace (University of Auckland) · dissertation

Aim: The objective of this study was to assess the effectiveness of a phone-based auditory training program in improving tolerance to sound, acceptance of background noise and perceived noise sensitivity in individuals with hyperacusis. Background: Hyperacusis is a disorder of decreased sound tolerance where ordinary sound is perceived as painful or uncomfortably loud. Increased central auditory gain and other central processes including attention and auditory scene analysis are thought to be involved in the manifestation of the disorder. An Auditory Object Identification and Localisation (AOIL) training program developed to target attention and auditory scene analysis processes has previously demonstrated effectiveness in improving acceptance of background noise while listening to speech in individuals without sound tolerance disorders (Bees, 2016; Searchfield et al., 2007). The current study assessed if the AOIL training adapted into a phone-based version will have a similar effect on improving acceptance of noise in individuals with hyperacusis. The study also explored the effectiveness of the AOIL in improving sound tolerance and perceived noise sensitivity, and whether individuals with hyperacusis would engage with the phone-based auditory training. Methods: Loudness Discomfort Levels (LDLs), Acceptable Noise Levels (ANLs) and perceived noise sensitivity scores (NoiSeQ) were measured in a group of 16 participants with hyperacusis before and after completing two weeks of AOIL auditory training. Findings: Results showed improvement in tolerance to sound, acceptance of background noise and perceptions of noise sensitivity. This was indicated by a statistically significant increase in LDLs, reduction in ANLs and increase in NoiSeQ scores after completion of the AOIL training. Conclusions: The phone-based AOIL training showed overall positive outcomes on sound tolerance, acceptance of background noise and perceptions of noise sensitivity in individuals with hyperacusis. The AOIL offers a new interactive approach to hyperacusis management. The training is thought to produce this effect through mechanisms of auditory scene analysis and attention however this requires further investigation. Understanding the underlying mechanisms that contributed to the improvements can help inform hyperacusis research and the understandings of mechanisms associated with the disorder, as well as the development of new treatment options.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 184 · R0769

**Towards a neurocomputational account of social controllability: From models to mental health**

2023 · Neuroscience & Biobehavioral Reviews · article · en · https://doi.org/10.1016/j.neubiorev.2023.105139

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 185 · R1269

**The effectiveness of Cognitive Behavioral Psychotherapy in Misophonia: A Case Report**

2018 · Journal of Clinical Psychiatry · article, research article · en · https://doi.org/10.5505/kpd.2018.18480

Misophonia is a condition that is triggered by certain sounds, which leads to unpleasant feelings such as anger, disgust, fear. Misophonia can severely affect patients' daily activities, social life, and interpersonal relationships. For these reasons, lately, misophonia is being recommended to be defined as a psychiatric disorder lately. Here we represent a case with misophonia and discuss the application of the cognitive behavioral psychotherapy as a treatment in an individual with misophonia. Although not being defined as a psychiatric diagnosis, many individuals are suffering from misophonia, and for these individuals, cognitive behavioral psychotherapy seems to be beneficial as a treatment option.

**Решение:** -2 клинический случай / серия случаев

---

### 186 · R0175

**Why Certain Sounds Trigger Rage: The Science of Misophonia**

2026 · Zenodo (CERN European Organization for Nuclear Research) · audiovisual/, other · en · https://doi.org/10.5281/zenodo.19049522

Episode summary: Ever felt an irrational surge of rage at the sound of someone chewing or clicking a pen? This episode dives deep into misophonia, a genuine neurological condition where the brain's "smoke detector" misidentifies neutral sounds as personal threats. We explore the latest research on the anterior insular cortex, the link between sound and motor control, and why this condition frequently overlaps with ADHD and autism. Learn about the "executive function tax" of sensory sensitivity and the modern clinical treatments—from specialized CBT to acoustic filters—that are helping people reclaim their lives from a world that's often just too loud. Show Notes For many, the sound of a ticking clock or someone chewing gum is a minor background annoyance. But for a significant portion of the population, these sounds trigger a physical response akin to a "fight or flight" emergency. This phenomenon is known as misophonia, or Selective Sound Sensitivity Syndrome (4S). Recent neurological research has moved the conversation away from viewing this as a behavioral quirk or a "short temper," revealing instead a complex breakdown in how the brain assigns meaning to sensory input. ### The Neurological "Smoke Detector" At the heart of misophonia is a malfunction in the brain's salience network, specifically within the anterior insular cortex (AIC). In a typical brain, the AIC acts as a filter, deciding which environmental sounds deserve attention and which should be ignored. In a misophonic brain, however, the AIC is hyper-connected to the amygdala—the brain's emotional center—and the hippocampus. When a trigger sound occurs, the brain skips logical processing and goes straight into a high-alert threat response. It is as if the brain's smoke detector is screaming "fire" because of a scented candle. This results in an instantaneous autonomic nervous system spike, causing increased heart rate, sweating, and intense emotional distress. ### The Mirror Neuron Hypothesis One of the most striking discoveries in recent years is the link between sound and movement. Functional MRI scans show that people with misophonia have higher connectivity between the AIC and the sensory-motor cortex. This suggests that when a sufferer hears a repetitive sound, like tapping or chewing, their brain's mirror neurons involuntarily simulate that action. The person isn't just hearing the sound; they are "feeling" the action in their own motor system. This creates a sense of physical intrusion or violation, explaining why the emotional response is often one of intense rage or a desperate need to escape the environment. ### A Common Neurodivergent Thread Misophonia is more common than previously thought, with studies suggesting up to 20% of the population experiences some symptoms. For about 2% to 5%, the condition is life-altering, impacting career choices and personal relationships. There is also a significant overlap with other neurodivergent conditions, such as ADHD and autism. In ADHD, a weakened "sensory gate" in the prefrontal cortex makes it difficult to filter out background noise. When misophonia is added to this, the brain becomes weaponized against itself—unable to ignore a sound that it simultaneously perceives as a threat. This creates an "executive function tax," where the brain spends so much energy trying to manage sensory input that it has little processing power left for other tasks. ### Moving Toward Management While there is no "cure" for the hard-wired connectivity of misophonia, clinical approaches are evolving. Specialized Cognitive Behavioral Therapy (CBT) aims to decouple the sound from the emotional threat response through counter-conditioning. Other treatments focus on Tinnitus Retraining Therapy (TRT), which uses sound generators to raise the "floor" of background noise. By reducing the contrast between the silence and the trigger sound, the brain is less likely to experience a sharp neurological spike. From acoustic filters to environmental management, the goal is to provide "shock absorbers" for the nervous system, allowing those with the condition to navigate a noisy world with less distress. Listen online: https://myweirdprompts.com/episode/science-of-misophonia-triggers

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 187 · R1176

**Methylphenidate Ameliorates Worsening Distractibility Symptoms of Misophonia in an Adolescent Male.**

2020 · The primary care companion for CNS disorders · article, journal article, journalarticle · eng · https://doi.org/10.4088/pcc.19l02553

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 188 · R0919

**Misophonia revised**

2022 · book, doctoral thesis · eng · https://hdl.handle.net/11245.1/829ead1a-2142-414c-aa0a-5f770bcd5f94

The objectives of this thesis are first, to increase knowledge concerning the phenomenology of misophonia and second, to investigate the effectiveness of different treatments for misophonia. In this thesis the phenomenology of misophonia is studied in a highly qualitative and quantitative sample (N=575). This leads to new insights and an important revision of the diagnostic criteria. Misophonia is considered a psychiatric disorder, which is characterized by anger and disgust provoked by human sounds in particular. The effectiveness of group cognitive behavioral therapy (G-CBT) on misophonia symptoms compared to a waiting list control group is investigated in the first randomized controlled trial of G-CBT for misophonia worldwide. Three months of G-CBT reduces misophonia symptoms compared to the waiting list condition. Clinical improvement is found in 56% of all completers (37% intention-to-treat) compared to 0% in the waiting list control group. One year after the end of treatment, the reduction in misophonia symptoms sustains. This thesis also consists the treatment manual for G-CBT, illustrated by single clinical case study. Moreover, a pilot study of case series shows that alternative treatment options, notably eye movement desensitization and reprocessing (EMDR) therapy, can be considered. EMDR therapy, focused on emotionally disturbing misophonia-related memories, significantly reduces misophonia symptoms in three of eight participating patients. The new insights gained from the studies in this thesis contribute to a further development of scientific research into misophonia.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 189 · R0162

**Decreased Sound Tolerance in Autism Spectrum Disorder: A Narrative Review of the Prevalence, Mechanisms, Assessment Tools, and Interventions for Hyperacusis and Misophonia**

2026 · Scientific Journal of Rehabilitation Medicine · article, journalarticle, review · und · https://doi.org/10.32598/sjrm.15.1.3432

Background and Aims Decreased sound tolerance (DST), including hyperacusis and misophonia, is one of the most prominent and disabling sensory features in autism spectrum disorder (ASD) and has significant consequences on the social, emotional, and cognitive functioning of these individuals. This phenomenon occurs due to the overlap of multilayered mechanisms in neural pathways and has been reported with high prevalence in individuals with ASD. This study aimed to review the literature on the prevalence, neural mechanisms, assessments, and interventions related to DST in individuals with ASD. Methods This narrative review was conducted by searching for articles between 2000 and 2025 in PubMed, Scopus, Web of Science, and Google Scholar. The search was performed by combining keywords related to autism, sound sensitivity, DST, hyperacusis, misophonia, prevalence, neural mechanisms, assessment, and interventions. After the initial screening, 91 studies were included. Results DST is significantly more prevalent in the autism population than in the general population, with hyperacusis (affecting approximately 27%-40%) and misophonia (affecting 12%–35% of individuals on the spectrum). Investigation of mechanisms suggests increased central gain, an imbalance in excitation/inhibition ratio, increased auditory cortex sensitivity, pattern changes in subcortical areas, and involvement of the anterior insula and amygdala. Assessments also included questionnaires, measurements of loudness discomfort levels, otoacoustic emissions, electrophysiological indices, and imaging. Interventions included modified cognitive-behavioral therapy, sound therapy, environmental modifications, and virtual/augmented reality technologies. Conclusion DST in ASD is a multifactorial phenomenon that requires multidimensional assessment and integrated interventions. Given its high prevalence and significant impact on functioning, future research should focus on standardizing assessment tools, developing autism-specific treatment protocols, and directly evaluating the effectiveness of interventions with enough samples.

**Решение:** -1 обзор / комментарий / письмо

---

### 190 · R1529

**Still too loud? It may be hyperacusis**

2002 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0000292894.50693.5c

Congratulations. Thanks to your careful testing and the fitting of a new hearing aid, your patient can hear better. So, why has the patient just called to complain about painfully loud sounds? One reason could be hyperacusis, an abnormal, strong reaction to sound occurring in the auditory pathways. On Friday morning from 8 to 9:30, Natan Bauman, EdD, and Janice Howard, MA, will discuss this condition and techniques for recognizing and treating it. “Specifically, the concept of recruitment vs. hyperacusis will be explained,” says Bauman. Measurements for differentiating the two, such as LDL, ABLB and MLB testing, will be discussed. Attendees will also learn about: the neurophysiologic model of hyperacusis as described by Pawel J. Jastreboff, PhD; new concepts related to loudness tolerance, such as misophonia and phonophobia, and treatment techniques with the use of noise generators and hearing aids.

**Решение:** -1 колонка / обзор (The Hearing Journal)

---

### 191 · R0170

**Sensory Sensitivity: Implications From the Fields of Medicine and Psychology for a Gifted Population**

2026 · Gifted Child Quarterly · article · en · https://doi.org/10.1177/00169862261453385

Most individuals have similar responses to everyday stimuli from the environment. But some individuals have responses that are stronger or weaker than others, and different ways of processing sensory information from the environment. Some individuals are so bothered by or negatively affected by sensory input and stimulation, or the lack of response to it, for example, that significant complications can arise with school, employment, and personal and family life. This article explores the literature on sensory sensitivity from the fields of medicine and psychology to enhance understanding of gifted and twice-exceptional individuals with sensory sensitivity. Within each field of study, theoretical, conceptual, and measurement approaches are discussed. Literature from the field of autism is explored, which is rich with research, as is research in the area of specific sound sensitivities. The very limited research from the field of gifted education is also explored. Implications for both research and practice are numerous.

**Решение:** -6 не про мизофонию

---

### 192 · R0878

**A Brief Commentary on the Consensus Definition of Misophonia**

2022 · Frontiers in Neuroscience · article, journal article, journalarticle · eng · https://doi.org/10.3389/fnins.2022.879070

A small body of academic literature on misophonia has developed over the last decade. This research includes case studies, experimental studies with small convenience samples, and those with more stringent study designs. For a list of studies see Brout et al. (2018). New hypotheses use prior papers as their basis and therefore some early misconceptions about misophonia and its definition are carried throughout some present-day research across the disciplines of audiology, otolaryngology, psychology, and psychiatry. The result is confusion amongst misophonia sufferers, as well as disagreement across clinicians and researchers. Based on these studies, numerous individuals with misophonia have received treatments that ranged from ineffective to highly uncomfortable. Thus, the need for a consensus definition is clear. The Misophonia Research Foundation, in partnership with the Center for Strategic Philanthropy, responded to this need by using a modified Delphi method, which structures group communication to deal with a complex problem (Stone Fish and Busby, 2005). It is a lengthy process that begins with the grouping of 15 experts. Experts were comprised of psychologists/psychiatrists, audiologists/ear, nose and throat (ENT) physicians/hearing scientists, a small number of neuroscientists, and one pediatrician. The result of the modified Delphi process yielded a consensus definition that was descriptive in nature, but missed some issues crucial to the misophonia sufferer, omitted some important related literature, and included some contradictory statements.

**Решение:** -1 обзор / комментарий / письмо

---

### 193 · R1069

**Misophonia: Is Disorder Not Mannerisms**

2021 · Unpublished · text/other, article · en · https://doi.org/10.13140/rg.2.2.13612.18563

(sound sensitivity) is a disorder in which people abnormally have strong and negative reactions to the sounds humans make which are ordinary, such as breathing or, chewing become enraged at people when we listen to them eating or breathing etc. The word Misophonia was given by audiologists Pawel and Margaret Jastreboff. means “hatred of was suggested in the year 2000 which explains the condition in which emotions, negative thoughts, and physical reactions are set off by specific sounds. It is not unexpected for people to occasionally be annoyed by some normal routine daily sounds. But for individuals with Misophonia, the sound of someone chewing, drinking water sound, making any other little sound can make them want to scream, get annoyed, angry. These reactions which are physical and emotional, which are ordinary sounds, are alike to the fight or flight response which may lead to panic, anxiety, and rage.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 194 · R0152

**Withdrawn**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.20411748

We apply the Displacement Framework to misophonia, formalizing it as an auditory-trigger wrong attractor in which specific sounds generate catastrophic D(ξ) through an aberrant salience-assignment mechanism. The acoustic ground state S°_acoustic is defined as the capacity to inhabit environments with ordinary ambient sound without involuntary threat activation. The wrong attractor W_miso has three components: trigger pattern recognition (not all sounds but specific patterns, often oral/nasal/repetitive rhythmic), interpersonal specificity (triggers frequently source-specific — the same sound from different people generates different responses), and the anger-disgust cascade (rage directed at the sound source, unusual among sensory sensitivity conditions which typically produce anxiety/withdrawal). The neurobiological substrate involves anomalous myelination in the anterior insular cortex connecting auditory and salience networks (Kumar et al., 2017), and the mirror neuron hypothesis: trigger sounds activate motor circuit simulations generating embodied disgust. A secondary anticipatory avoidance wrong attractor progressively narrows the accessible acoustic landscape — avoiding meals, open-plan offices, restaurants, relationships with trigger-producing people. The anger-disgust paradox generates a shame-suppression-secondary-Φ loop: the disproportionate rage is ego-alien, shame drives suppression, suppression increases internal D(ξ), eventual expression damages relationships, and guilt deepens the wrong attractor. Nine formal propositions are derived covering trigger specificity, the interpersonal dimension, progressive avoidance deepening, and the anger-disgust-shame triple accumulation. Return paths include CBT, mindfulness as response flexibility (not desensitization), and acceptance work on the shame dimension.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 195 · R1157

**Searching for an anchor in an unpredictable world: A computational model of obsessive compulsive disorder.**

2020 · Psychological Review · article · en · https://doi.org/10.1037/rev0000188

In this article, we develop a computational model of obsessive-compulsive disorder (OCD). We propose that OCD is characterized by a difficulty in relying on past events to predict the consequences of patients' own actions and the unfolding of possible events. Clinically, this corresponds both to patients' difficulty in trusting their own actions (and therefore repeating them), and to their common preoccupation with unlikely chains of events. Critically, we develop this idea on the basis of the well-developed framework of the Bayesian brain, where this impairment is formalized as excessive uncertainty regarding state transitions. We illustrate the validity of this idea using quantitative simulations and use these to form specific empirical predictions. These predictions are evaluated in relation to existing evidence, and are used to delineate directions for future research. We show how seemingly unrelated findings and phenomena in OCD can be explained by the model, including a persistent experience that actions were not adequately performed and a tendency to repeat actions; excessive information gathering (i.e., checking); indecisiveness and pathological doubt; overreliance on habits at the expense of goal-directed behavior; and overresponsiveness to sensory stimuli, thoughts, and feedback. We discuss the relationship and interaction between our model and other prominent models of OCD, including models focusing on harm-avoidance, not-just-right experiences, or impairments in goal-directed behavior. Finally, we outline potential clinical implications and suggest lines for future research. (PsycInfo Database Record (c) 2020 APA, all rights reserved).

**Решение:** -6 не про мизофонию

---

### 196 · R0730

**Depressive Symptoms in Autistic Youth with Anxiety Disorders.**

2023 · Journal of developmental and behavioral pediatrics : JDBP · randomized controlled trial, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1097/dbp.0000000000001223

Anxiety and depression often coexist in youth and share overlapping symptomatology; however, little is known about the comorbidity of anxiety and depression in autistic youth. This study explores (1) the frequency of depressive symptoms among autistic children with clinically significant anxiety, (2) clinical variables that may be associated with elevated depressive symptoms, and (3) whether pretreatment depressive symptoms predict cognitive behavioral therapy (CBT) outcomes for anxiety. Children aged 7 to 13 years (N = 87) and their parents participated in a randomized controlled trial comparing 2 versions of a parent-led, telehealth-delivered CBT program. Parents and children completed a variety of clinical assessments and self-report questionnaires before and after treatment. Fifty-seven percent of the child sample reported experiencing elevated depressive symptoms while roughly 20% of parents reported elevated depressive symptoms in their child. A strong association between anxiety and depression was found. Heightened feelings of loneliness, per child report, and functional impairment, per parent report, were found to be uniquely associated with elevated depressive symptoms. Finally, depressive symptoms were not a significant predictor of CBT outcomes for anxiety. Findings suggest high degrees of comorbidity between anxiety and depression among autistic children and that feelings of loneliness, anxiety, and functional impairment may be early indicators of mood-related concerns. Further research is needed to determine the full extent of the association between anxiety and depression and additional options for treating depression in autistic children.

**Решение:** -6 не про мизофонию

---

### 197 · R0762

**Mind the NIH-Funding Gap: Structural Discrimination in Physical Health–Related Research for Cognitively Able Autistic Adults**

2023 · Journal of Autism and Developmental Disorders · article · eng · https://doi.org/10.1007/s10803-022-05856-w

Autistic adults experience disparities in physical health and health care access. A major barrier to addressing these disparities is a lack of federal funding for research on this topic. In seeking funding from the National Institutes of Health (NIH), we discovered nodes that contribute to structural discrimination in physical health-related research for autistic adults. To examine this structural discrimination, we systematically searched funded research on all physical health-disparity conditions in autistic adults using NIH RePORTER. Among 61 unique studies, none focused on improving the relevant physical health condition through intervention, programs, or services for autistic adults. Thus, we need updated policies and procedures that support research on physical health disparities in populations with developmental or mental health conditions.

**Решение:** -6 не про мизофонию

---

### 198 · R0538

**Misophonia is related to stress but not directly with traumatic stress.**

2024 · PloS one · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1371/journal.pone.0296218

The relationship between misophonia, stress, and traumatic stress has not been well characterized scientifically. This study aimed to explore the relationships among misophonia, stress, lifetime traumatic events, and traumatic stress. A community sample of adults with self-reported misophonia ( N = 143) completed structured diagnostic interviews and psychometrically validated self-report measures. Significant positive correlations were observed among perceived stress, traumatic stress, and misophonia severity. However, multivariate analyses revealed that perceived stress significantly predicted misophonia severity, over and above traumatic stress symptoms. The number of adverse life events was not associated with misophonia severity. Among symptom clusters of post-traumatic stress disorder, only hyperarousal was associated with misophonia severity. These findings suggest that transdiagnostic processes related to stress, such as perceived stress and hyperarousal, may be important phenotypic features and possible treatment targets for adults with misophonia.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 199 · R0946

**Audiological and psychological assessment of tinnitus patients with normal hearing.**

2022 · Frontiers in neurology · journal article · eng · https://doi.org/10.3389/fneur.2022.1102294

This study was performed to assess identifiable abnormalities in tinnitus patients with normal hearing. The medical records of subjective non-pulsatile tinnitus patients with normal hearing confirmed by conventional pure-tone audiometry who visited our tinnitus clinic between March 2020 and May 2022 were reviewed. The loudness discomfort level (LDL), extended high-frequency hearing loss (EHFHL), summating potential (SP)/action potential (AP) ratio, distortion product otoacoustic emission (DPOAE), thresholds of auditory brainstem response (ABR) wave V, somatic modulation, and psychiatric symptoms, such as anxiety, depression, and stress were evaluated by questionnaires. Decreased LDL (n = 48, 59.8%) was the most frequent finding, followed by EHFHL (n = 29, 35.4%), increased SP/AP ratio (n = 27, 32.9%), psychiatric symptoms (n = 24, 29.3%), decreased DPOAE (n = 17, 20.7%), somatic modulation (n = 8, 9.8%), and increased ABR threshold (n = 3, 3.7%); 75.6% of patients had one or more of these findings. The presence of psychiatric symptoms was independently associated with the Tinnitus Handicap Inventory (THI) score. Tinnitus in patients with normal hearing may be accompanied by a combination of various subclinical abnormal audiological findings. However, the presence of psychiatric symptoms alone was independently associated with tinnitus distress.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 200 · R1274

**Misophonia – when certain sounds drive you crazy**

2018 · The Conversation · article, other · en · https://doi.org/10.64628/ab.dyyedqmrc

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 научно-популярная статья (The Conversation)

---

### 201 · R0376

**A randomized controlled trial evaluating an mHealth intervention for anger-related cognitions in misophonia.**

2025 · Journal of affective disorders · article, journal article, randomized controlled trial · eng · https://doi.org/10.1016/j.jad.2025.03.060

Misophonia is a condition characterized by strong, aversive reactions to specific sounds produced by others, often manifesting as intense negative emotions like anger or rage in response to nearby noises. The present study aimed to evaluate the effectiveness of an mHealth app in reducing misophonia symptoms and related cognitions. In this study, 85 participants were randomly assigned to an immediate app use (iApp) or delayed app use (dApp) group and completed measures at baseline (T0), after 15 days of app use (T1 for iApp, T2 for dApp), and at 1-month follow-up (T3). Intention-to-treat analyses at T1 revealed significant interaction effects; compared with the dApp group, the iApp group exhibited lower misophonia symptoms on select measures (interaction effect sizes ranging from d = 0.06 to 0.52) as well as reductions in anger ruminations and anger-related metacognitions (interaction effect sizes of d = 0.47). Within-group analyses demonstrated substantial reductions in misophonia symptoms from baseline to follow-up (iApp: d = 0.62–1.51; dApp: d = 0.89–1.75) with similar decreases in anger-related outcomes (iApp: d = 0.89–0.92; dApp: d = 0.85–0.90). Mediation analyses, however, did not support an indirect effect of the intervention on misophonia symptoms via changes in rumination or anger-related metacognitions. mHealth applications show promise in alleviating misophonia symptoms and related cognitive processes. Further research is needed to elucidate the roles of anger rumination and metacognitions in misophonia. • Negative emotions like anger are common reactions to human noises in misophonia. • Daily training with a mobile app may reduce anger rumination and misophonia symptoms. • Improvements in anger rumination were maintained at a 1-month follow-up. • Results highlight the potential of cost-effective, accessible mHealth interventions.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 202 · R1233

**Sound intolerance [Elektronisk resurs] : characteristics, psychosocial work factors and reactions to exposure**

2019 · Umeå

Sound intolerance refers to an adverse reaction to sounds at sound pressure levels most people do not find bothersome. It is sometimes associated with hearing loss and tinnitus, but neither conditions are a prerequisite for being intolerant to sounds. The processes underlying the heightened reactions to sound, or how sound intolerance is related to other afflictions is not fully known, and research in this area can still be described as being in an early stage. This thesis aims to broaden the knowledge about sound intolerance and the sub-category of hyperacusis by using cross-sectional epidemiological and quasi-experimental methods of inquiry.The thesis consists of three studies, each approaching the subject from a different perspective with the aim to better understand various characteristics of sound intolerance in general, its relation to psychosocial factors in the work environment, and its effects during noise exposure. Studies I &amp; II are cross-sectional studies using two different data sets with similar design. Study I was based on data from a stratified sample in the Västerbotten Environmental Health Study. It examined the characteristics, background descriptions and comorbidities of self-reported and physician diagnosed individuals with hyperacusis, and compared them to a healthy referent group. Analyses revealed that a majority of both hyperacusis groups actively tried to avoid sound sources, and experienced that they for the most part could affect the environment to make it less noisy. There were significantly increased risks for other diagnosed illnesses in the hyperacusis groups compared to the healthy referent group, with large odds ratios (ORs) for the psychiatric illnesses anxiety, depression, post-traumatic stress disorder and exhaustion syndrome. Other common illnesses were tinnitus, hearing impairment and musculoskeletal disorders. Study II used data from the Österbotten Environmental Health Study and focused on the psychosocial work environment for people with hyperacusis. Working participants with hyperacusis who were employed/on leave of absence/paternal leave/long-term sick listed were compared to a working sample without hyperacusis on measures of effort-reward imbalance, work over commitment, emotional and social support and worry at work. The hyperacusis group scored significantly higher on worry, social support, and reward, whereas the groups did not differ significantly with respect to emotional support, over commitment or effort. In the final study, a quasi-experimental design was employed to investigate how individuals with sound intolerance react to noise exposure over time, in terms of perceived sound intensity, unpleasantness, rated distractibility, symptoms, heart rate variability and cognitive performance. Participants were divided into three groups of equal size based on their self-rated sound intolerance, which resulted in low, medium, and high sound intolerance groups. Results revealed large variations across individuals in several outcome variables. Compared to the other two groups, the high sound intolerance group perceived the noise as more unpleasant, stronger, and more distracting. They further rated the symptoms as higher in intensity, showed deviations in heart rate variability, and performed poorer on a cognitive task selected to measure inhibition.In conclusion, the results suggest that persons with sound intolerance have relatively poor general health and hearing as well as high odds of comorbidity with various symptoms, including psychiatric diagnoses and functional somatic syndromes. In a working population, the sound intolerant show high odds for worrying about things at work, perceiving low social support at work and not feeling rewarded at work. Finally, the results suggest that persons with high sound intolerance have increased distractibility, sound unpleasantness, symptoms over time as well as lowered heart rate variability and cognitive performance when exposed to sounds.Ljudintolerans syftar på en negativ reaktion på ljud vid ljudtrycksnivåer som de flesta människor inte finner obehagligt. Vilka processer som ligger bakom de förhöjda reaktionerna eller relationerna till andra åkommor är ännu oklart. Syftet med den här avhandlingen är att bredda kunskapen om ljudintolerans och dess underkategori hyperakusi, genom bruket av tvärsektionella och kvasi-experimentella metoder. Avhandlingen består av tre studier som angriper ämnet från olika perspektiv, med syfte att bättre förstå generella egenskaper hos ljudintolerans; relationen till psykosociala arbetsmiljöfaktorer; samt effekterna av en ljudexponering i kontrollerad laboratoriemiljö. Studie I bestod av tvärsnittsdata från Miljöhälsostudien i Västerbotten och avhandlade egenskaper, bakgrundsdata och komorbiditeter för självrapporterade och läkardiagnostiserade individer med hyperakusi, jämfört med en referensgrupp utan dessa besvär. Resultaten visade att en majoritet av båda hyperakusi-grup

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 203 · R0245

**What’s next for misophonia? Child and parent priorities for misophonia advocacy, treatment, and research**

2025 · Personalized Medicine in Psychiatry · article, journalarticle, google scholar result · en · https://doi.org/10.1016/j.pmip.2025.100160

Background Misophonia is characterized by sensitivity to specific common sounds and associated visual stimuli. Despite a high estimated prevalence in the general population, "misophonia" as a term remains largely unknown by the general population, with research on misophonia treatment still in a nascent stage. This is especially the case in children and adolescents, despite misophonia most often beginning in this time. To guide the growing foundation of misophonia literature, this study seeks to inquire about advocacy, research, and treatment priorities from the perspective of youth with misophonia and their parents. Methods In this study, twenty youth with clinically significant misophonia (ages 10–17) and their parents engaged in semi-structured focused interviews. Interviews were transcribed and thematically analyzed using an inductive approach. Results Eight themes were identified, including Advancing Awareness for Advocacy, Misophonia is Outside a Child's Control, Practical and Misophonia-Specific Therapies Needed , Understanding the Neurobiology of Misophonia, Defining Misophonia Beyond Sound Triggers , Understanding the Daily Impact of Misophonia, Uncovering the Misophonia-Mental Health Connection , and Long-Term Prognosis. Discussion While some participants' ideas were distinctive to their experience, several themes, described above, emerged across interviews. These findings propose paths forward for future advocacy, research, and treatment development.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 204 · R1174

**Misophonie**

2020 · Sprache · Stimme · Gehör · article · de · https://doi.org/10.1055/a-1197-9751

Marsha Johnson war die erste, die die Empfindlichkeit gegenüber bestimmten Geräuschen in Online-Selbsthilfegruppen für Patienten mit Hyperakusis diskutierte und Ende der neunziger Jahre des vergangenen Jahrhunderts ca. 500 Fälle mit verminderter Geräuschsensitivität dokumentiert hat. Sie bezeichnete das Phänomen als „Selective Sound Sensitivity Syndrome“ (selektives Geräuschempfindlichkeitssyndrom gegenüber jeder Art von Schall) – ein Begriff, der bis heute verwendet wird. Hiervon abzugrenzen ist der später geprägte Terminus „Misophonie“, der deutlich eine Hypersensitivität gegenüber Geräuschpegeln übersteigt und auf die amerikanischen Neurowissenschaftler Pawel J. und Magret M. Jastreboff [1, 2] zurückgeht. Er beschreibt eine Intoleranz gegenüber unschädlichen Geräuschen wie etwa Kauen von Möhren, Äpfeln, Chips; Schmatz- oder Schlürfgeräusche; Zerplatzen von Kaugummiblasen an den Lippen; Räuspern; Schniefen; Schnarchen; mit Fingern auf einer Oberfläche trommeln; Fingerknacken; Papier rascheln; Kugelschreiber Klicken; Trittgeräusche von Schuhen; Quietschen von Kreide beim Schreiben an der Wandtafel; Reibegeräusche auf Stoff (Tischdecke glatt Streichen) o. ä., die von anderen verursacht werden. Solche Geräusche lösen bei manchen Personen unangemessene, aversive Reaktionen aus (Wut, Ekel, Hass, Aggression) und können bei ihnen zu Abgelenktheit, Irritation, Konzentrations-, Denk- und Lernproblemen führen. Der Störungsbeginn liegt meistens bereits in Kindheit und Adoleszenz. Im Diagnostischen und Statistischen Manual Psychischer Störungen (DSM-V) der APA und in der ICD-10 der WHO ist „Misophonie“ nicht verschlüsselt, da ihr pathologischer Status bislang unklar ist (physiologische Reaktion? Symptom? eigenständige [neurologische, psychische] Störung?). Fazit Aazh et al. [11] präsentieren ein Fallformulierungsmodell für ein kognitiv-VT Vorgehen. Es startet mit der Untersuchung der anfänglichen emotionalen Reaktionen (Ärger, Irritation) und körperlichen Beschwerden (wie beschleunigter Herzschlag, flache Atmung, Schweißausbruch, Schwindel, Kribbeln auf der Haut, Übelkeit), wenn Betroffene mit individuell aversiven akustischen Reizen konfrontiert werden. Es folgt die Protokollierung der hieraus resultierenden negativen Gedanken und der weiteren emotionalen sowie physischen Reaktionen, die wiederum bewertende Überlegungen, etwa Selbstzweifel, bei Betroffenen zur Folge haben und somit einen Teufelskreis von Gedanken erzeugen. Der Interventionsansatz zielt darauf ab, genau diesen Kreislauf zu durchbrechen, indem Betroffene in der Exploration und Analyse ihrer negativen Gedanken unterstützt werden, um diese besser verarbeiten und modifizieren zu können. Publication History Article published online: 21 September 2020 © Georg Thieme Verlag KG Stuttgart · New York

**Решение:** -1 обзорная публикация / словарный очерк

---

### 205 · R1121

**Rapid and Sustained Resolution of Misophonia-Type Hyperacusis With the Selective Serotonin Reuptake Inhibitor Sertraline.**

2021 · The primary care companion for CNS disorders · article, journal article, journalarticle · eng · https://doi.org/10.4088/pcc.20l02731

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 206 · R1230

**Tics and stereotypies: A comparative clinical review.**

2019 · Parkinsonism & related disorders · article, comparative study, journal article · eng · https://doi.org/10.1016/j.parkreldis.2019.02.005

Tics and stereotypies are the most common pathological repetitive complex motor behaviors occurring during the neurodevelopmental period. Although they may appear transiently during development without acquiring a pathological status, when they become chronic they may be distressing, socially impairing, or even, in the case of malignant tics, potentially physically harmful. Despite a certain similarity in their phenomenology, physicians should be able to distinguish them for their different variability over time, topographical distribution, association with sensory manifestations, and relationship with environmental triggers. The complex phenomenology of tics and stereotypies is constantly enriched by the characterization of novel variants, e.g. tics triggered by auditory stimuli in association with misophonia and stereotypies associated with intense imagery activity. Their pathophysiology remains partially elusive, but both animal model and brain imaging studies confirm the involvement of all the three major loops (sensorimotor, associative and limbic) within the cortico-basal ganglia circuitry. From a management perspective, the greatest advances witnessed in the last decade involve the diffusion of behavioral strategies (e.g. habit reversal training or response interruption and redirection), including the development of protocols for telehealth on online training in order to optimise access. In the context of severe tics, e.g. in refractory Tourette syndrome, there is increasing experience with deep brain stimulation of the intralaminar thalamic nuclei or the globus pallidus internus, although more research is needed to fine tune target choice and stimulation setting definition.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 207 · R1527

**Clinical Management of Tinnitus and Hyperacusis**

2003 · ASHA Leader · article · en · https://doi.org/10.1044/leader.ftr1.08202003.4

You have accessThe ASHA LeaderFeature1 Nov 2003Clinical Management of Tinnitus and Hyperacusis Susan L. Gold Susan L. Gold Google Scholar More articles by this author https://doi.org/10.1044/leader.FTR1.08202003.4 SectionsAbout ToolsAdd to favorites ShareFacebookTwitterLinked In The understanding and treatment of intrusive tinnitus have changed over the past 15 years. The disorder used to be viewed simply as a problem of the ear. Now any discussion of intrusive tinnitus must consider how the brain processes input from the auditory system. Evaluation and treatment have developed into a neurophysiologically based protocol that has as its goal habituation to the tinnitus. A crucial feature of this model is that a number of systems in the brain are involved in the emergence of tinnitus. The cochlea and auditory periphery play only a secondary role. These concepts were first proposed in the 1980s by Pawel Jastreboff, and the clinical protocol for evaluation and treatment based on the neurophysiological model was implemented at The University of Maryland Medical Center in 1990. As this treatment was refined, it became known internationally as Tinnitus Retraining Therapy (TRT). TRT offers an individualized, noninvasive treatment that is effective for patients with intrusive tinnitus. The protocol is targeted to work above the source of the tinnitus; therefore, the etiology of the tinnitus is irrelevant. Whether a patient associates the onset of the tinnitus with noise trauma, medication, surgery, medical problem, motor vehicle accident, or does not associate onset with any known incident has little predictive value for success in a habituation-based protocol. In addition, factors such as maskability, whether tinnitus is bilateral or unilateral, constant or intermittent, pitch or other psychoacoustic characterizations, or level of hearing ability do not preclude treatment with TRT. Habituation and Sound Sensitivity Habituation to the tinnitus signal is most effectively achieved by the combined application of two components: directive counseling, which attempts to neutralize the negative emotional associations with the tinnitus (habituation of reaction or annoyance) sound therapy, which interferes with the detection of the tinnitus signal (habituation of perception or awareness) Both elements of the treatment must be incorporated to result in the “chicken/egg” effect necessary to achieve complete habituation. When this occurs, the tinnitus, although still present, is no longer an issue in the patient’s life. Patients can go for long periods of time without thinking about it as the tinnitus becomes more like the refrigerator noise that you tune out, unless you stop to listen for it. The introduction of the concept of habituation to the tinnitus signal was a turning point in tinnitus treatment. A second important clinical contribution by Jastreboff was the assessment of sound sensitivity. When the program was first established, the primary emphasis was on tinnitus. However, measurements of loudness discomfort levels (LDLs) for live voice and pure tones always were performed as part of the evaluation. As reported by Jastreboff and Hazell in 1993, patients treated with sound therapy using low-level, broadband sound exhibited improved LDLs. Patients with initially reduced LDLs generally reported discomfort when exposed to moderate or even soft sounds in their environment. When LDLs improved and dynamic range increased, they reported subjective improvements in their ability to tolerate normal sounds in their environment. As these response patterns emerged, patients with reduced tolerance levels and complaints of discomfort were evaluated and treated in a more specific way, implementing a variant of the basic TRT protocol. Approximately 40% of the tinnitus patients evaluated in our center have at least some degree of hyperacusis (decreased sound tolerance). This category also includes patients exhibiting phonophobia (fear or emotional reaction to certain sounds) and misophonia (dislike of certain sounds). The aspect of decreased sound tolerance has become an increasingly important part of our evaluation and treatment protocol. Implementation TRT, as it is implemented at the University of Maryland Tinnitus & Hyperacusis Center, usually lasts about 1-2 years. Initial treatment begins with four main components: audiological/tinnitus/hyperacusis evaluation otolaryngology evaluation directive counseling sound therapy instruction Audiological/tinnitus/hyperacusis evaluation is performed to separate the status of tinnitus, hearing, hyperacusis, phonophobia, and misophonia. A detailed history includes specific questions to determine the effect of noise on tinnitus, whether tinnitus and/or ear discomfort is exacerbated in noise and, if so, for how long. During testing, in addition to establishing audiometric thresholds, pitch and loudness of tinnitus are matched. It also is imperative to establish LDLs for live voice and pure-tone frequencies of, minimally, 500, 1k, 2k, 4k, 8k, and 12k Hz. Spontaneous otoacoustic emissions tests are performed to rule out objective tinnitus. Distortion product otoacoustic emissions tests assess the function of outer hair cells. No test is performed that will exceed the levels of the LDLs. Tests such as tympanometry, acoustic reflex thresholds, reflex decay, or auditory brainstem response may have to wait until LDLs improve. Two hours are scheduled for this evaluation. The second component is an otolaryngology or neurotology evaluation to rule out any medical problem or disease process such as acoustic neuroma, glomus tumor, superior canal dehiscence, vascular bruit, Eustachian tube dysfunction, cochlear malformation, Lyme disease, autoimmune disorders, syphilis, and others. Past medical records and current test results are reviewed by the physician. Referrals may be made by the otolaryngologists to other medical specialties. MRI/CT scans or other tests may be requested. If any medical treatment is indicated, further tinnitus treatment is suspended until the results are determined. After consultation with the otolaryngologist, the audiologist places the patient in one of the five general categories described by Jastreboff (1998): Category 1 patients are significantly affected by tinnitus, but do not have hyperacusis or subjective hearing loss. Category 2 patients are affected by tinnitus and have significant hearing loss, but no hyperacusis. Category 3 patients have hyperacusis, but no prolonged ear discomfort or exacerbation of tinnitus when exposed to noise. Exacerbation of ear discomfort and/or tinnitus is usually brief, and, if present, resets itself by the next morning. Hearing loss, if present, is irrelevant because hyperacusis must be addressed first. Amplification may be considered after the hyperacusis problem is resolved. Category 4 patients have tinnitus and hyperacusis, but have prolonged (day or weeks) worsening of ear discomfort and/or exacerbation of tinnitus after being exposed to noise. This category must be treated very cautiously and requires careful monitoring. Category 0 patients have tinnitus, but are not seriously distressed by it. They are generally seeking information and reassurance, and typically do not require sound therapy. This category of patient is more frequently seen in an otolaryngology or audiology practice. It should be noted that negative (and often incorrect) information at this point, such as “there is nothing you can do about it, just learn to live with it,” or “perhaps you are going to lose your hearing,” can push a patient into Category 1. The categorization determines the emphasis for directive counseling and the course of sound therapy. Patients can change categories as they progress through treatment. During the third component, which consists of at least two hours of directive counseling, family members or friends are encouraged to participate. This session is designed to demystify the tinnitus and neutralize the negative emotional association. The audiologist reviews test results with the patient so there is a clear understanding of the status of hearing, tinnitus, hyperacusis and phonophobia, or misophonia. The anatomy and physiology of the auditory system is explained in detail, with special emphasis on the cochlear structures. Dialogue includes how the brain handles the input from the auditory system, as well as how this relates to the patient’s individual case. If hyperacusis is present, discussion also includes how the brain increases the gain or sensitivity in the auditory structures and subsequent limbic and autonomic nervous system response. Tinnitus and hyperacusis are thought to be two separate but related issues. An important contribution of TRT counseling is that intrusive tinnitus is the result of a dynamic relationship between the ear, brain, emotions, biochemistry, neurophysiology, what you eat, what you drink, the stresses you are under, how much sleep you get, and more. It is frequently the inability to control the tinnitus that results in issues such as significant intrusiveness and subsequent anxiety, muscle tension, and sleeplessness. Further discussion relates to an in-depth explanation of the neurophysiological model developed by Jastreboff. Factors such as the role of the limbic and autonomic nervous system, relationship to hearing ability, pitch and loudness of the tinnitus, and assessment of outer hair cell activity are discussed. Sound Therapy Options for sound therapy are introduced, and the patient and clinician make decisions together. Most importantly, patients need to understand why a specific course of sound therapy is necessary. Sound therapy is designed to both interfere with the brain’s ability to detect the tinnitus signal and to reset the neuronal networks. TRT does not employ traditional masking techniques, which are felt to be short-term and counterproductive to the habituation process. For patients in Category 1 with tinnitus but no significant hearing loss or hyperacusis, sound-generating instruments are the most direct and convenient way to proceed. These instruments emit a broadband sound and allow an open ear canal so the patients can hear easily. They must have a zero noise floor because the volume setting tends to be just slightly above the threshold of hearing. Both ears are fit with instruments even if tinnitus is unilateral, and patients are given specific instructions regarding volume settings and schedule of use. Patients in Category 2, who have tinnitus and significant hearing loss but no hyperacusis, are fit with amplification to amplify sounds in their environment. Patients are taught that, to use amplification as sound therapy for tinnitus, they must wear the hearing aids all their waking moments, avoid silence, and keep neutral sound on in their environment at all times. This amplified sound does not have to mask the tinnitus. As with other forms of sound therapy, habituation of the tinnitus is a slow, gradual process. Category 3 patients, those with hyperacusis, may include patients with normal hearing or those with significant hearing loss. In all cases, if hyperacusis is present, it must be addressed first. These patients are fit with sound generators and enter into a variant of the basic tinnitus protocol, which is slightly more conservative. Although appropriate protection from noise is important, patients who overprotect are taught to wean themselves off. Gold, Frederick, and Formby (1999) reported that improvements in sound sensitivity for Category 3 patients typically occur quickly, and patients report subjective improvement in their ability to tolerate sounds that were previously uncomfortable. For example, they become comfortable riding in a car, hearing dishes clatter, and going to church, movies, the mall, or sports events. Sound therapy continues for about one year until improvements are stabilized. Patients with hyperacusis and significant hearing loss who were previously unable to benefit from amplification frequently make a comfortable transition to appropriate amplification in about eight months to a year. Almost all patients with hyperacusis will exhibit an element of phonophobia, which is discussed in the directive counseling session and at follow-up appointments. For those patients with misophonia and/or phonophobia only, a different approach is indicated. Category 4 patients exhibit an exacerbation of tinnitus and/or hyperacusis for extended periods of time (days or weeks) as the result of sound exposure. Sound therapy is implemented with extreme caution and close follow-up. These patients are the most difficult to treat successfully. For all categories, it is essential to monitor progress and systematically reinforce and clarify the concepts introduced during directive counseling. Ideally, periodic follow-up visits occur for 1–2 years until the goals are met. These visits are typically more frequent during the first six months. Change is generally slow, incremental, and subtle with expected rough patches. Outcome measures for TRT are limited by the inability to measure tinnitus or assess severity objectively. Past inability to perform double-blind studies and low rate of follow-up also have contributed to this limitation. Historically, the success rate has been measured by patient responses on questionnaires related to percentage of time they are aware of tinnitus, number of activities interfered with, and effect on their life. Improvement in at least two of these areas by at least 20% was required to indicate significant improvement. Early retrospective studies by Jastreboff (1998) indicated significant improvement in about 80% of patients who received full treatment. Data replicating these results were reported in 1999 by Sheldrake, Hazell, and Graham; Bartnick, Fabijanska, and Rogowski; and Heitzman, et al. Berry et al. (2002) reported significant improvement in self-perceived disability following TRT as measured by the Tinnitus Handicap Inventory, a validated, patient-based outcome measure. Efficacy Clinically, TRT has not been as effective for patients with short-term memory loss, traumatic brain injury, untreatable psychological or psychiatric problems, or those undergoing litigation related to the tinnitus and/or hyperacusis problem. Controlled studies are necessary to evaluate the efficacy of the individual components, such as directive counseling, sound therapy, and clinician effect. Currently, Henry and Schecter are conducting randomized clinical trials comparing TRT and masking sponsored by Veterans Affairs Rehabilitation, Research and Development Service in Portland, OR. The University of Maryland Tinnitus & Hyperacusis Center has been awarded a planning grant for a multi-center, double-blind, randomized clinical trial testing the efficacy of TRT and its components. Study participants will include active and retired military personnel at six major medical centers of the U.S. Armed Forces and two civilian centers. Participating clinical centers will include audiology and otolaryngology staff in the U.S. Army, Navy, and Air Force and two universities. In addition, research in adaptive chronic auditory gain and its relationship to sound tolerance is ongoing at the University of Maryland Tinnitus & Hyperacusis Center as a direct outgrowth of our clinical experience with hyperacusis. We are currently recruiting subjects who have hearing loss and are unable to benefit from amplification due to sound sensitivity problems. This article is presented as an introduction to Tinnitus Retraining Therapy. TRT continues to be adapted and refined by Jastreboff and others all over the world. The concepts of the neurophysiologically based model and habituation-based protocol have opened new areas for both scientific research and clinical applications. The role of audiologists in TRT involves more than performing a battery of tests. They are actively involved in the individual directive counseling process, not as psychologists or psychiatrists, but to educate and empower this group of patients who were previously difficult to manage. For More Information Visit the Web site of the American Tinnitus Association at http://www.ata.org/, call 503-248-9985 or 800-634-8978, or e-mail [email protected]. References Bartnick G., Fabijanska A., & Rogowski M. (1999). Our experience in treatment of patients with tinnitus and/or hyperacusis using the habituation method.Proceedings of the VIth International Tinnitus Seminar (pp. 415–417). London: The Tinnitus and Hyperacusis Centre. Google Scholar Berry J. A., Gold S. L., Frederick E. A., Gray W. C., & Staecker H. (2002). Patient-based outcomes in patients with primary tinnitus undergoing tinnitus retraining therapy.Archives of Otolaryngology Head and Neck Surgery, 128, 1153–1157. CrossrefGoogle Scholar Formby C., & Gold S. L. (2002). Modification of loudness discomfort levels: Evidence for adaptive chronic auditory gain and its clinical relevance.Seminars in Hearing, 23(1), 21–34. CrossrefGoogle Scholar Gold S. L., Formby C., & Gray W. C. (2000). Celebrating a decade of evaluation and treatment: The University of Maryland Tinnitus & Hyperacusis Center.American Journal of Audiology, 9, 69–74. LinkGoogle Scholar Gold S. L., Frederick E. A., & Formby C. (1999). Shifts in dynamic range for hyperacusis patients receiving tinnitus retraining therapy (TRT).Proceedings of the VIth International Tinnitus Seminar (pp. 297–301). London: The Tinnitus and Hyperacusis Centre. Google Scholar Heitzman T., Rubio L., Cardenas M. R., & Zofio E. (1999). The importance of continuity in TRT patients: Results at 18 months.Proceedings of the VIth International Tinnitus Seminar (pp. 509–511). London: The Tinnitus and Hyperacusis Centre. Google Scholar Jastreboff P. J. (1998). Tinnitus; the method of.In Gates G. A. (Ed.), Current therapy in otolaryngology head and neck surgery (pp. 90–95). St Louis, MO: Mosby. Google Scholar Jastreboff P. J., Gray W. C., & Gold S. L. (1996). Neurophysiological approach to tinnitus patients.American Journal of Otolaryngology, 17, 236–240. Google Scholar Jastreboff P. J., & Hazell J. W. P. (1993). A neurophysiological approach to tinnitus: Clinical implications.British Journal of Audiology, 27, 7–17. CrossrefGoogle Scholar Jastreboff P. J., & Jastreboff M. M. (2000). Tinnitus Retraining Therapy as a method for treatment of tinnitus and hyperacusis patients.Journal of the American Academy of Audiology, 11, 162–177. Google Scholar Jastreboff P. J., & Jastreboff M. M. (2001). Tinnitus Retraining Therapy.Seminars in Hearing, 22, 51–63. CrossrefGoogle Scholar Sheldrake J. B., Hazell J. W. P., & Graham R. L. (1999). Results of tinnitus retraining therapy.In Hazell J.W.P. (Ed.), Proceedings of the Sixth International Tinnitus Seminar (pp. 292–296). Cambridge, UK: The Tinnitus and Hyperacusis Centre. Google Scholar Author Notes Susan L. Gold, joined the Tinnitus Center in 1990 when it was established at the University of Maryland Medical Center by Pawel Jastreboff. Currently, as senior audiologist and clinical coordinator, she lectures and teaches audiologists and otolaryngologists clinical management of tinnitus and hyperacusis patients, and is involved in clinical research in these areas. Contact her by e-mail at [email protected]. Advertising Disclaimer | Advertise With Us Advertising Disclaimer | Advertise With Us Additional Resources FiguresSourcesRelatedDetails Volume 8Issue 20November 2003 Get Permissions Add to your Mendeley library History Published in print: Nov 1, 2003 Metrics Downloaded 1,460 times Topicsasha-topicsleader_do_tagleader-topicsasha-article-typesCopyright & Permissions© 2003 American Speech-Language-Hearing AssociationLoading ...

**Решение:** -1 профессиональное издание (ASHA Leader)

---

### 208 · R0721

**Multidimensional Characterization of Misophonia: Toward The Emerging Psychometric Perspective**

2023 · OSF Registries · journalarticle/pre-registration, journalarticle/project · en · https://doi.org/10.17605/osf.io/9s7gb

Misophonia, characterized by heightened reactions to specific sounds, may extend beyond an affective sound sensitivity disorder. Recent validation studies confirm its impact on daily life in diverse populations. This study employs the S-Five questionnaire to quantify emotional and behavioral aspects and assesses the factor structure and psychometric properties of the S-Five-T scales within the Iranian population. Participants self-identified as experiencing misophonia. This study uses the Penn State Worry Questionnaire (PSWQ), Interpersonal Reactivity Index (IRI), Cognitive Emotion Regulation Questionnaire (CERQ), and Multidimensional Assessment of Interoceptive Awareness (MAIA) to characterize the emotional and cognitive attributes, contributing to a more comprehensive understanding of the multidimensional nature of misophonia.

**Решение:** -7 protocol / preregistration without data

---

### 209 · R1549

**Aversive sound classification and filtration using deep neural networks**

Summit (Simon Fraser University) · article · en

Decreased sound tolerance (DST) is common among many children with Autism Spectrum Disorder (ASD).When children are exposed to specific aversive sounds at school, they may be very distressed and can react with behaviours such as covering their ears, yelling, screaming, or running out of the room to avoid the aversive sound.Schools' approaches for accommodating DST include letting students wear earplugs or earmuffs or allowing them to leave to take breaks in a quiet area.Most wearable devices (e.g., earmuffs, ear plugs, noise canceling headphones) tend to block or attenuate all sounds indiscriminately, including speech, and if the child leaves the classroom to escape the noise, this will disrupt learning and social interaction.Therefore, existing strategies tend to interfere with the child's full participation in class and other activities.This thesis aims to develop an intervention tool to selectively filter out aversive sounds for children with ASD.Ideally, this tool will attenuate unwanted sounds (e.g., dog barking, sirens, jackhammers) while letting other sounds (e.g., the teacher's voice) to be heard.In this thesis, Deep Neural Network (DNN) methods and signal processing techniques are employed to intelligently identify the aversive sounds in the environment, attenuate them from the ambient sound and pass the rest of the sound to users.To identify aversive sounds, a combination of a Recurrent Neural Network (RNN) and a Convolutional Neural Network (CNN) is used.After the aversive sound is identified, another part of this thesis is dedicated to filter the aversive sound.A DNN-based learning framework is proposed to address the audio denoising problem for real-time applications.The proposed method has the ability to suppress stationary noises such as engine and air conditioner, and also non-stationary, and dynamic noises such as dog barking, siren, and jackhammer.Further, a Graphical User Interface (GUI) is designed to combine the identification and filtration components of the intervention.The user-friendly GUI enables the users to initiate specific tasks in order to hear their surrounding sounds without any disturbances.In order to evaluate the performance of the proposed intervention technique, several testing sessions are conducted with autistic individuals.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 210 · R1227

**Misophonia: Neural mechanisms, symptoms and diagnostic classification**

2019 · Työväentutkimus Vuosikirja · article · fi

Tavoitteet. Misofonia on vähän tunnettu neurofysiologinen ja behavioraalinen oireyhtymä, jossa keskeistä on yliherkkyys valikoidulle joukolle ääniä. Sitä ei ole määritelty kansainvälisissä diagnoosiluokituksissa, mutta lisääntyvä empiirinen tutkimus on alkanut määrittää sen ominaisuuksia. Tutkielman tavoitteena on määritellä ja esitellä lyhyesti misofonian keskeisimpiä piirteitä sekä sitä, miten ilmiötä on tutkittu. Misofonian oirekuvan ja seurauksien lisäksi tutkielmassa perehdytään häiriön neuraalisiin ja fysiologisiin mekanismeihin sekä otetaan kantaa siihen, tulisiko se määritellä erilliseksi psykiatriseksi oireyhtymäksi. Menetelmät. Tietoa etsittiin PubMed, Scopus, Helka ja Google Scholar –tietokannoista ensisijaisesti hakusanoilla ”misophonia” ja ”misofonia” sekä taustoitusta varten hakusanoilla ”sound sensitivity”, ”hyperacusis” ja ”tinnitus”. Tarkasteluun valittiin erityisesti viimeaikaisia katsausartikkeleita, kokeellisia tutkimuksia ja kyselytutkimuksia. Tulokset ja johtopäätökset. Misofoniaa luonnehtii yliherkkyys joukolle ”kuvioltaan” tai merkitykseltään tietynlaisia ääniä. Näitä ovat erityisesti ihmisten aiheuttamat, varsinkin syömiseen liittyvät äänet. Äänen kuuleminen laukaisee voimakkaan emotionaalisen reaktion, jossa hallitsevana tunteena on tyypillisesti viha, ärtymys tai ahdistus. Seurauksena on yleensä välttämiskäyttäytymistä, mutta myös verbaalisesti tai fyysisesti aggressiiviset reaktiot ovat mahdollisia. Lisäksi misofonialla on todettu olevan negatiivisia vaikutuksia sekä päivittäiseen toimintaan sosiaalisissa ympäristöissä että yksilön psyykkiseen hyvinvointiin. Yliherkkyys ei perustu audiologisiin syihin. Sen sijaan tutkimuksissa on saatu viitteitä siitä, että misofoniaan liittyy poikkeavia yhteyksiä kuulo- ja emotionaalista tietoa käsittelevien aivoalueiden välillä, epätavallisia varhaisen tarkkaavuuden ja kuulotiedon käsittelyn prosesseja sekä autonomisen hermoston aktivaatiota reaktiona ääniin. Näiden neurofysiologisten tekijöiden lisäksi misofonisen reaktion syntyyn näyttävät vaikuttavan yksilölliset merkityksenannot ja sosiaaliseen kontekstiin liittyvät tekijät. Myös ehdollistumista on ehdotettu häiriön aiheuttavaksi mekanismiksi. Misofonia täyttää tietyt mielenterveyden häiriön kriteerit, mutta sen luonne on toistaiseksi liian tuntematon, jotta sitä tulisi määrittää omaksi diagnostiseksi luokakseen. Lisää tutkimusta vaatii esimerkiksi se, onko kyseessä erillinen häiriö vai jonkin laajemman oireyhtymän ominaisuus, sekä toisaalta se, onko kyseessä psykiatrinen vai neurologinen häiriö.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 211 · R1369

**Noise sensitivity and hyperacusis in patients affected by multiple chemical sensitivity.**

2017 · International archives of occupational and environmental health · article, journal article, journalarticle · eng · https://doi.org/10.1007/s00420-016-1185-8

Purpose The aim of this study was to investigate the presence of noise sensitivity and hyperacusis in patients suffering from multiple chemical sensitivity (MCS), a chronic condition characterized by several symptoms following low-level chemical exposure. Moreover, distortion product otoacoustic emissions (DPOAE) were performed to further study cochlear function. Methods A questionnaire-based survey was performed. Eighteen MCS patients, selected with strict diagnostic criteria, and 20 healthy age- and gender-matched subjects filled Weinstein's Noise Sensitivity Questionnaire (WNS) and Khalfa's Hyperacusis Questionnaire (HQ). Results were compared with scores from the quick Environmental Exposure Sensitivity Index (qEESI), a routinarily used questionnaire to screen MCS symptoms, and with DPOAE values. An analysis of variance (ANOVA) was performed between MCS and control subjects scores; moreover, Spearman's rank correlation test was performed between questionnaire results. Results ANOVA testing on DPOAE values showed any significant difference between groups, while WNS, HQ and qEESI scores were significantly higher in MCS group compared to controls. Correlation analysis showed strong positive correlation between WNS, HQ and qEESI in MCS subjects. Conclusions For the first time, auditory-related perceptual disorders were studied in MCS. A strong association between WNS, HQ results and MCS symptoms severity has been highlighted. These findings suggest that decreased sound tolerance and noise sensitivity could be considered as possible new aspects of this syndrome, contributing to its peculiar phenotype. Furthermore, as DPOAE values did not differ from healthy subjects, present findings might suggest a 'central' source for such disorders in this group of patients.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 212 · R1219

**The Suitability of an Inhibitory Learning Approach in Exposure When Habituation Fails: A Clinical Application to Misophonia**

2019 · Cognitive and Behavioral Practice · article · en · https://doi.org/10.1016/j.cbpra.2018.04.003

Abstract Recent findings have led to a reconceptualization of the mechanisms that account for the efficacy of exposure-based treatments. Termed the “inhibitory learning model,” this approach emphasizes new learning when confronted with previously avoided stimuli rather than merely the cessation of fear or aversive emotional responding. In this paper, we propose the applicability of the inhibitory learning model for conditions and contexts in which simple exposure does not produce habituation. We illustrate this application from an in-progress randomized controlled treatment trial for adults with misophonia. Misophonia is a condition marked by strong aversive reactions to specific sounds. It is a difficult to treat and understudied syndrome. All participants in the trial received exposure, either before or after a stress management module of treatment. Exposure treatment emphasized altered expectancies for the target sounds as well as deliberate practice in hearing sounds on the individually developed hierarchy. Inhibitory learning strategies were employed to increase treatment adherence and commitment, shape patient behavior during exposures, manufacture negative prediction errors, increase perceived control over reactions, and promote learning that generalized to functional improvements. The findings are discussed in the context of future applications of the inhibitory learning model for psychopathology associated with avoidance.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 213 · R1216

**Neural Basis of Response Bias on the Stop Signal Task in Misophonia.**

2019 · Frontiers in psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.3389/fpsyt.2019.00765

Objective: Misophonia is a newly described condition in which specific ordinary sounds provoke disproportionately strong negative affect. Since evidence for psychobiological dysfunction underlying misophonia is scarce, we tested whether misophonia patients, like many patients with impulse control or obsessive-compulsive spectrum disorders, show impaired ability to inhibit an ongoing motor response. Methods: We collected functional magnetic resonance imaging data during a stop signal task in 22 misophonia patients and 21 matched healthy controls. Results: Compared to controls, patients tended to show longer stop signal delays, which is the time between stimuli signaling response initiation and inhibition. Additionally, patients tended to activate left dorsolateral prefrontal cortex more during responding rather than successful inhibition, as was seen in controls. Furthermore, patients lacked inhibition success-related activity in posterior cingulate cortices and activated the superior medial frontal gyri less during inhibition success compared to failure, a feature correlated with stop signal delays over the sample. Conclusions: Misophonia patients did not show impaired response inhibition. However, they tended to show a response bias on the stop signal task, favoring accuracy over speed. This implies perfectionism and compulsive, rather than impulsive, behavior. Moreover, brain activations were in line with patients, compared to controls, engaging more cognitive control for slowing responses, while employing more attentional resources for successful inhibition.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 214 · R1399

**[Misophonia is a neglected disorder].**

2015 · Ugeskrift for laeger · article, case reports, journal article · dan · https://pubmed.ncbi.nlm.nih.gov/26617171/

A 14-year-old girl, who was diagnosed with OCD when she was 11-year-old, experienced emotional reactions and autonomic arousal in response to specific human-made sounds. At first she thought that these symptoms were part of her OCD, but it became clear to her that she suffered from misophonia - a disorder not yet classified.

**Решение:** -2 клинический случай / серия случаев

---

### 215 · R0608

**Misophonia matters: A case study of the role of brain imaging in debates over new diagnoses.**

2024 · Sociology of health & illness · article, journal article, journalarticle · eng · https://doi.org/10.1111/1467-9566.13679

Abstract Misophonia has gained attention in scientific circles that utilise brain imaging to validate diagnoses. The condition is promoted as not merely a symptom of other psychiatric diagnoses but as a discrete clinical entity. We illustrate the social construction of the diagnostic category of misophonia through examining prominent claims in research studies that use brain imaging to substantiate the diagnosis. We show that brain images are insufficient to establish the ‘brain basis for misophonia’ due to both technical and logical limitations of imaging data. Often misunderstood as providing direct access to the matter of the body, brain images are mediated and manipulated numerical data (Joyce, 2005, Social Studies of Science 35(3), p. 437). Interpretations of brain scans are further shaped by social expectations and attributes considered salient to the data. Causal inferences drawn from these studies are problematic because ‘misophonics’ are clinically pre‐diagnosed before participating. We argue that imaging cannot replace the social process of diagnosis in the case of misophonia, nor validate diagnostic measures or otherwise substantiate the condition. More broadly, we highlight both the cultural authority and inherent limitations of brain imaging in the social construction of contested diagnoses while also illustrating its role in the disaggregation of symptoms into new diagnoses.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 216 · R1465

**Modern Pharmacotherapies Revivify Patulous Eustachian Tube as Di Bartolomeo's Syndrome of Misophonic Autophony**

2013 · Otolaryngology · article · en · https://doi.org/10.1177/0194599813495815a215

Objectives: 1) Analyze the contemporary etiologic factors for the increasing incidence of rare patulous Eustachian Tube (PET) disorders within this century. 2) Enable physicians to recognize this elusive syndrome in the clinical otologic history and physical examination. 3) Identify the specific etiologies causing the PET in Di Bartolomeo's Syndrome of pathognomic autophony and the complex factors that enable the disturbing autogenic tubular sounds. Methods: Double blind, random clinical trial, employing the preferred topical nasal medication. A collateral PET study (2002‐2006) to formulate a drug‐free remedy which supports healing and tissue strength, within the generally regarded as safe (GRAS) Food and Drug Administration standards. The National Institutes of Health, and collateral PET support group social media forum, informed new PET inquirers of The Ear Foundation's former research website.160 subjects completed the study. In the online forum, 3,500 PET patients (4,000 ears) were treated. The results of the investigational new drug clinical trials and separate drug‐free study are presented. Results: Recent scientific and cultural advances in this century are identified which facilitate the evolution and increase in patients with disabling PET symptoms. Each has an individual multi‐factorial and enigmatic etiology and mechanism of action. Conclusions: None provided by author.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 217 · R1368

**Misophonia: Case Report**

2017 · European Psychiatry · article, review, conference-abstract · en · https://doi.org/10.1016/j.eurpsy.2017.01.2259

Introduction Misophonia refers to a condition in which there is a strong aversion to certain sounds, in response to it the person reports unpleasant emotional experiences and autonomic arousal. Objectives To present the case of misophonia carrier and discuss diagnostic features. Methodology Case report and literature review. Results Female, 32 years old, married, two children. In anamnesis reported obsessional symptoms (Check doors and windows, concerned with order and symmetry of objects; read all that lies ahead, pull the hand two or three times on mobile) since adolescence. Also reported triggering situations of anger: intolerance to some noises and sounds, like chewing third, mobile keyboard, click the “mouse” computer, printer and rub hands. In the presence of these noises, she tries to move away, and already tried to attack physically relatives and insulting co-workers. She was treated with escitalopram and re-evaluation after thirty days, reported partial relief misophonia and reduction of obsessional symptoms. Conclusion The condition was first described in the early 2000s by two audiologists, and has become the focus of interest in the field of psychiatry. Some reports suggest that misophonic symptoms may be part of other conditions such as Tourette's syndrome, obsessive compulsive disorder and generalized anxiety disorder. Specifically, the characteristics shared between misophonia and OCD, as the relief of discomfort associated with avoidance behaviour suggest that the condition is part of the obsessive-compulsive spectrum, which seems to happen with the case described above. Disclosure of interest The authors have not supplied their declaration of competing interest.

**Решение:** -2 клинический случай / серия случаев

---

### 218 · R0032

**Les Sens Oubliés de la médecine (préprint allégé)**

2026 · HAL (Le Centre pour la Communication Scientifique Directe) · book, book/ · fr · https://doi.org/10.5281/zenodo.20933021

Cet ouvrage interroge un angle mort de la formation médicale francophone contemporaine : la faible intégration, dans les cursus et la pratique clinique, des modalités sensorielles « oubliées » — intéroception, proprioception, système vestibulaire, chronoception, thermoception, nociception, prurit, tact C-affectif. Alors que la sémiologie classique reste organisée autour des cinq sens aristotéliciens, plus d'un siècle de neurosciences a profondément renouvelé la cartographie sensorielle humaine. L'ouvrage défend la thèse selon laquelle cette désynchronisation contribue à une errance diagnostique substantielle pour PPPD, SEDh, misophonie, autisme adulte, TCA et dépressions chronoceptives. Position délibérément modérée : plaidoyer pour un dialogue renforcé entre sémiologie sensorielle étendue, psychiatrie et médecine fonctionnelle. 16 chapitres en 5 parties (histoire, sémiologie, 6 cas cliniques, audit formation FR, implications). Préprint allégé — manuscrit complet via Amazon KDP.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 219 · R0406

**The Misophonia Audiovisual Trigger Archive (MATA)**

2025 · OSF · dataset/project · https://doi.org/10.17605/osf.io/e7qbm

The Misophonia Audiovisual Trigger Archive contains 1,300 five-second audiovisual clips spanning 12 empirically validated categories of misophonic triggers. Stimuli are organized into 12 folders, each representing a broad category: body-part sounds, mouth sounds (eating), mouth sounds (not eating), nasal–throat sounds, repetitive and continuous sounds (animal), repetitive and continuous sounds (human), repetitive and continuous sounds (non-human), rubbing sounds, rustling and tearing sounds, speech and vocalization sounds, talking sounds, and walking sounds. All clips are provided in .mp4 format.

**Решение:** -7 dataset / audio repository

---

### 220 · R1495

**Моделирование природоохранных технологий в теплоэнергетике с учетом макрокинетических процессов**

2011 · Вестник Саратовского государственного технического университета · article · en

Presented an analytical model for evaluating the environmental impact of power equipment on the environment. The basis of the model of the law laid macrokinetic flow gross reaction of nitrogen oxides in the zone of high temperatures, reflecting the regularities of formation of nitrogen oxides on the thermal mechanism. Received oxygen and nitrogen in the reaction zone, depending on the modes of operation of burners and furnaces of the boiler, as well as their possible changes due to entry of additional moisture. Defined analytical reaction rate, concentration of nitrogen oxides and exit rates of nitrogen oxides from fuel combustion, taking into account the input of moisture.

**Решение:** -6 не про мизофонию

---

### 221 · R0900

**Effectiveness of Online Group-mindfulness and Acceptance‐based Therapy and Cognitive-behavioral Therapy on Misophonia**

2022 · Iranian Journal of Psychiatry and Behavioral Sciences · article, google scholar result · en · https://doi.org/10.5812/ijpbs-120159

Background: Misophonia is a disorder in which people show negative emotions such as anger, disgust, and anxiety about certain sounds, such as mouth and nose sounds, as well as some repetitive sounds. This disorder has a high prevalence and causes many problems for patients. Objectives: This study aimed to examine and compare the effectiveness of two therapies, including online group-mindfulness and acceptance‐based therapy (OG-MACT) and online group-cognitive-behavioral therapy (OG-CBT) in patients with misophonia. Methods: This study was a two-group random assignment pretest-posttest design. Thirty-eight participants were recruited using convenience sampling and randomly assigned to OG-CBT (n = 19) and OG-MACT (n = 19) groups. The statistical population included patients with misophonia (a score higher than seven on the Misophonia Questionnaire) referred to the Tehran Institute of Psychiatry from October to December 2019. They were asked to respond to online self-report questionnaires evaluating misophonia, distress tolerance, quality of life, depression, anxiety, and stress scale in three stages, including before treatment sessions, one week after the end of sessions, and during a three-month follow-up. Results: The difference in the mean scores of the scales at different times did not differ according to the type of treatment group (OG-CBT versus OG-MACT). The results showed that the effect of time was significant on misophonia scores. Over time, this finding also applies to depression, anxiety, and stress subscales in the distress tolerance questionnaire. However, there was no significant difference in the quality of life over time. The changes in misophonia were clinically significant in 53% of OG-MACT members and 69% of OG-CBT members. Discussion: According to the findings, the two online group therapies of CBT and MACT effectively reduced the symptoms of misophonia.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 222 · R1489

**Tinnitus and Hyperacusis/Phonophobia**

2011 · Springer New York · other literature type, part of book or chapter of book · eng · https://doi.org/10.1007/978-1-60761-145-5_57

1. Hyperacusis is a decreased sound tolerance. 2. Prevalence of the disease is described in 9–15% of the population, but increases among tinnitus patients. 3. Pathophysiological mechanisms involve some disruptions in the amplification and regulation processes of the external hair cells, disorders of the efferent system (medial and lateral olivocochlear pathways), or effects to the central sound ­processing at the subcortical level. 4. The role of some neurotransmitters (serotonin, GABA), which are also involved in other hyperacusis-related diseases (migraine, depression), can be relevant in this disorder. 5. Other theories confirm the effect of the endorphins that activates the excitatory function of the glutamate, the main auditory neurotransmitter, increasing its toxicity. 6. The activation of the limbic and autonomic nervous systems produces the emotional reaction of the hyperacusis (anxiety, fear, and depression). 7. Proposed treatments are based on acoustic stimulation: progressive introduction of white sound (tinnitus retraining therapy TRT) and customized sounds based on the damaged hearing frequencies. 8. Noise generators and hearing aids can be fitted in severe cases. 9. The role of some drugs involved in the metabolism of serotonin and GABA opens new approaches for the management of hyperacusis.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 223 · R0580

**Brain circuits in autonomous sensory meridian response and related phenomena.**

2024 · Philosophical transactions of the Royal Society of London. Series B, Biological sciences · article, journal article, review · eng · https://doi.org/10.1098/rstb.2023.0252

Autonomous sensory meridian response (ASMR) is characterized by a tingling sensation with a feeling of relaxation and a state of flow. We explore the neural underpinnings and comorbidities of ASMR and related phenomena with altered sensory processing. These phenomena include sensory processing sensitivity (SPS), synaesthesia, Alice in Wonderland syndrome and misophonia. The objective of this article is to uncover the shared neural substrates and distinctive features of ASMR and its counterparts. ASMR, SPS and misophonia exhibit common activations in the brain regions associated with social cognition, emotion regulation and empathy. Nevertheless, ASMR responders display reduced connectivity in the salience network (SN), while individuals with SPS exhibit increased connectivity in the SN. Furthermore, ASMR induces relaxation and temporarily reduces symptoms of depression, in contrast to SPS and misophonia, which are linked to depression. These observations lead us to propose that ASMR is a distinct phenomenon owing to its attention dispatch mechanism and its connection with emotion regulation. We suggest that increased activations in the insula, along with reduction in connectivity within the salience and default mode networks in ASMR responders, may account for their experiences of relaxation and flow states. This article is part of the theme issue 'Sensing and feeling: an integrative approach to sensory processing and emotional experience'.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 224 · R1428

**Letter to the editor: potential treatment targets for misophonia.**

2015 · General hospital psychiatry · article, letter, lettersandcomments · eng · https://doi.org/10.1016/j.genhosppsych.2015.03.020

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 редакционная статья / письмо

---

### 225 · R1179

**Autonomous Sensory Meridian Response**

2020 · The International Encyclopedia of Media Psychology · reference-entry · en · https://doi.org/10.1002/9781119011071.iemp0304

This entry provides an overview of extant research on the phenomenon of autonomous sensory meridian response (ASMR). ASMR is a pleasant tingling sensation (often described as “brain tingles”) that some people experience in response to a set of triggers including whispering, tapping, and soft speaking. Now, nearly 10 years since the term ASMR was coined, it has become increasingly mainstream and prevalent in popular culture. Large online communities on sites such as YouTube allow people to watch videos created to trigger ASMR which they use to combat insomnia and improve mood. This entry covers the small but growing body of research on ASMR, its historical context, descriptive characteristics, and neurological and physiological basis. The association between ASMR and other perceptual phenomena (synesthesia, misophonia, and frisson) as well as its link to individual difference variables (personality, empathy, flow/absorption, and mindfulness), is also discussed.

**Решение:** -7 dictionary / reference entry

---

### 226 · R0278

**Quieting the Triggers: Exploring Therapeutic Avenues for Misophonia**

2025 · Annals of Indian Psychiatry · article, journalarticle, review · en · https://doi.org/10.4103/aip.aip_185_25

Misophonia is a disabling condition where specific sounds, such as chewing, breathing, or tapping, trigger intense emotional and physiological responses disproportionate to their acoustic properties. These reactions are shaped by associative learning rather than volume levels, and prevalence estimates vary widely across populations. Misophonia can severely impair concentration, interpersonal relationships, academic performance, and workplace productivity. Management remains experimental, with cognitive behavioral therapy showing the strongest and the most consistent evidence of effectiveness. Tinnitus retraining therapy also shows promise, particularly in habituating individuals to trigger sounds, whereas pharmacological options (such as selective serotonin reuptake inhibitors and beta-blockers) and neuromodulatory techniques (including transcranial magnetic stimulation (TMS), eye movement desensitization and reprocessing (EMDR), vagus nerve stimulation, and auditory training) are emerging adjuncts with encouraging but preliminary results. Despite these developments, there is no established, standardized treatment protocol for misophonia. The current review emphasizes the urgent need for well-designed, mechanism-based clinical trials and the development of integrated, multimodal care approaches.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 227 · R1550

**Misophonia: a case report**



_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 228 · R1191

**Subjektif tinnituslu bireylerin çok yönlü değerlendirilerek tinnitus yönetim protokolünün hazırlanması**

2020 · Sağlık Bilimleri Enstitüsü · doctoral thesis · tur · https://acikbilim.yok.gov.tr/handle/20.500.12812/488329

The aim of this study was to form a `tinnitus management protocol` according to the tinnitus levels by evaluating the subjects with subjective tinnitus by evaluating the multifactorial approach principle based on emotion, cognition, quality of life, sleep and decreased sound tolerance criteria. 145 subjects aged between 18-64 (45 ± 11, 78 M, 67 F) were included in the study. Tinnitus Assessment Form, Short Form-36, Beck Depression Inventory (BDI), STAI-D, STAI-S, Montreal Cognitive Assessment Scale (MoCA), Tinnitus Handicap Inventory (THI), Hearing Handicap Inventory (HHI), Pitsburgh Sleep Quality Index (PSQI) and Khalfa Hyperacusis Questionnaire were applied after audiological evaluation. In the evaluation of tinnitus, psychoacoustic measurements (loudness, picth matching, minimal masking level and residual inhibition) were performed. As a result of statistical analysis, PSQI, STAI-S and STAI-D scores were higher than normal limit values independent of tinnitus level. When the relationship between severity of tinnitus and BDI was examined, it was found that there was an increase in depression scores at severe / catastrophic levels. As the severity of tinnitus increased, the quality of life subscales decreased. As a result of the comparison of the tinnitus levels and PSQI sub-dimensions, it was determined that severe / catastrophic levels had worse scores in sleep disturbances, general sleep quality and sleep latency than the other three level (Kruskal-Wallis p &lt;0.05). When the scores of 75 individuals with hearing loss and tinnitus complaints were compared, there was a moderate significant correlation between the HHI and THI scores (r=0.598, p=0.00). A significant relationship was found between asymmetric high frequency hearing loss and localization of tinnitus. This study demonstrated the presence of level-related factors for subjective tinnitus assessment. As a result, according to the severity (level) of tinnitus; three different protocols were prepared: very mild / mild, moderate and severe / catastrophic.Key words: Tinnitus, quality of life, hyperacusis, sleep, anxiety. Bu çalışmanın amaçı; Subjektif tinnituslu bireylerin çok faktörlü yaklaşım prensibi ile değerlendirilerek duygudurum, biliş, yaşam kalitesi, uyku ve azalmış ses toleransı kriter alınarak tinnitus düzeylerine göre `tinnitus yönetim protokolu` oluşturmaktı. Çalışmaya yaşları 18-64 (45±11, 78 E, 67 K) arasında değişen 145 birey dahil edildi. Odyolojik değerlendirmeler ile birlikte Tinnitus Değerlendirme Formu, Short Form-36, Beck Depresyon Envanteri (BDE), STAI-D, STAI-S, Montreal Bilişsel Değerlendirme Ölçeği (MoCA), Tinnitus Engel Ölçeği (TEÖ), İşitme Engel Ölçeği (İEÖ), Pitsburgh Uyku Kalite İndeksi (PUKİ), Khalfa Hiperakuzi Ölçeği (KHÖ) uygulandı. Tinnitus değerlendirmesinde, psikoakustik ölçümler (loudness, picth eşleştirme, minimal maskeleme seviyesi ve rezidüel inhibisyon) yapıldı. İstatistiksel analiz sonucunda PUKİ, STAI-S ve STAI-D ölçek puanlarının tinnitus düzeyinden bağımsız normal sınır değerlerinin üzerinde olduğu belirlendi. Tinnitus şiddeti ile BDE arasındaki ilişki incelendiğinde şiddetli/çok şiddetli düzeylerde depresyon puanlarında artış olduğu belirlendi. Tinnitus şiddeti artıkça yaşam kalitesi alt alanlarının hepsinde düşüş elde edildi. Tinnitus şiddeti ve PUKİ alt boyutların karşılaştırması sonucunda uyku düzensizliği, genel uyku kalitesi ve uyku gecikmesinde şiddetli/çok şiddetli grupların diğer üç gruptan daha kötü puanlar aldığı bu farkın anlamlı olduğu belirlendi (Kruskal-Wallis p &lt;0,05). İşitme kaybı ve tinnitus yakınması olan 75 bireyin İEÖ ve TEÖ puanları karşılaştırıldığında orta düzeyde anlamlı korelasyon elde edildi (r=0.598, p= 0.00). Asimetrik yüksek frekans işitme kaybı ile tinnitus lokalizasyonu arasında anlamlı ilişki bulundu. Bu çalışmada subjektif tinnitus değerlendirmesi için düzey ile ilişkili etkenlerin varlığı gösterildi. Sonuç olarak tinnitus şiddetine göre; çok hafif/hafif, orta ve şiddetli/çok şiddetli olmak üzere üç farklı protokol oluşturuldu.Anahtar kelimeler: Tinnitus, yaşam kalitesi, hiperakuzi, uyku, anksiyete. 170

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 229 · R1273

**Diplacusis**

2018 · Digital Commons @ East Tennessee State University

Book Summary: Hyperacusis and Disorders of Sound Intolerance: Clinical and Research Perspectives is a professional resource for audiology practitioners involved in the clinical management of patients who suffer from sound tolerance concerns. The text covers emerging assessment and intervention strategies associated with hyperacusis, disorders of pitch perception, and other unusual processing deficits of the auditory system. In order to illustrate the patients perspectives and experiences with disorders of auditory processing, cases are included throughout. This collection of diagnostic strategies and tools, evidence-based clinical research, and case reports provides practitioners with avenues for supporting patient management and coping. It combines new developments in the understanding of auditory mechanisms with the clinical tools developed to manage the effects such disorders exert in daily life. Topics addressed include unusual clinical findings and features that influence a patient s auditory processing such as their perceptual accuracy, recognition abilities, and satisfaction with the perception of sound. Hyperacusis is covered with respect to its effects, its relation to psychological disorders, and its management. Hyperacusis is often linked to trauma or closed head injury and the text also considers the management of patients with traumatic brain injury as an opportunity to illustrate the effectiveness of interprofessional care in such cases. Interventions such as cognitive behavioral therapy, self-efficacy training, and hearing aid use are reported in a way that enhances clinicians\u27 ability to weave such strategies into their own work, or into their referral system. Hyperacusis and Disorders of Sound Intolerance illuminates increasingly observed auditory-related disorders that challenge students, clinicians, physicians, and patients. The text elucidates and reinforces audiologists contributions to polytrauma and interprofessional care teams and provides clear definitions, delineation of mechanisms, and intervention options for auditory disorders

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 230 · R0202

**Tinnitus and decreased sound tolerance in military Veterans: Relationship with cochlear deafferentation.**

2026 · Hearing research · dataset/dataset, journal article, journalarticle · eng · https://doi.org/10.1016/j.heares.2026.109789

Purpose Military Veterans are at high risk for noise-induced cochlear synaptopathy, a type of cochlear deafferentation. Predicted perceptual consequences of deafferentation include tinnitus and hyperacusis. The objective of this study was to determine if compared to young non-Veteran controls with minimal noise exposure, Veterans with normal audiograms who report constant tinnitus and/or decreased sound tolerance (DST) show reductions in three physiological indicators of deafferentation: (1) auditory brainstem response [ABR] wave I amplitude, (2) envelope following response [EFR] magnitude, and (3) wideband middle ear muscle reflex [MEMR] magnitude. Outer hair cell (OHC) function was also evaluated using distortion product otoacoustic emissions [DPOAEs]. Results Mean ABR wave I amplitudes, EFR magnitudes, and high frequency DPOAEs were reduced in a sample of 22 Veterans with tinnitus and 19 Veterans with DST relative to 165 controls. On average, MEMR magnitudes were also smaller for Veterans with DST than for controls. While many Veterans with tinnitus had smaller MEMRs than controls, a small number had large MEMRs. ABR wave V/I amplitude ratios tended to be elevated for Veterans compared to controls. Conclusions ABR, EFR, and DPOAE measurements were suggestive of both cochlear deafferentation and subclinical high frequency OHC dysfunction in Veterans with constant tinnitus or DST. Reductions in MEMR magnitude were not consistently observed in Veterans with tinnitus who had reduced ABR and EFR measurements, indicating that the MEMR may not be a reliable indicator of cochlear deafferentation. Increased central gain in the auditory brainstem may have contributed to the perception of tinnitus and DST.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 231 · R1514

**Tinnitus retraining therapy : A different view on tinnitus. Commentary**

2006

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 232 · R0442

**Assessing cognitive performance and comfort under simulated MRI noise and its association with autistic like traits**

2025 · The Plymouth student scientist · article · en · https://doi.org/10.70156/1754-2383.1535

Magnetic Resonance Imaging (MRI) scanners produce noise levels between 65 and 130 decibels. This noise, alongside the broader sensory environment of the MRI, poses challenges for individuals with autism spectrum disorder (ASD). Noise exposure has been shown to impair task performance, increase errors, and affect brain activity. ASD traits are associated with decreased sound tolerance, including hyperacusis, misophonia, and phonophobia. In ASD, noisy environments disrupt inferior frontal gyrus function, impairing task response and brain connectivity. Given this, it’s crucial to understand how these sensory challenges specifically affect ASD experience and performance during MRI procedures. This study assesses cognitive performance and comfort under simulated MRI noise and its association with autistic-like traits. Participants completed the AQ questionnaire before performing a computerised 3-back task under three noise conditions of MRI noise in a within-subjects design. Accuracy, hit rates, false alarm rates and comfort ratings were collected after each condition. A univariate ANOVA was conducted to analyse the effects of noise across different levels on task performance, correlated against AQ scores. The results suggest that individuals with more autistic traits may be less negatively affected by auditory distractions. While this study did not find statistical significance for the hypothesis, it does emphasise the differences in those with high ASD-like traits. These findings challenge assumptions about sensory sensitivity in ASD traits and suggest that cognitive adaptation mechanisms may influence noise tolerance, highlighting the need for individualised accommodations in MRI settings

**Решение:** -1 обзор литературы / концептуальная статья

---

### 233 · R0915

**More than a little sound**

2022 · The Lancet Psychiatry · article · en · https://doi.org/10.1016/s2215-0366(22)00306-6

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 234 · R1239

**Clinical Advancements for Managing Hyperacusis with Pain**

2019 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0000602900.16223.0e

Like many who suffer from a rare disorder, hyperacusis sufferers frequently face clinicians who have an insufficient understanding of the most impacting characteristics of the condition. Expanding disorder definitions to include new markers takes significant time and evidence. Subtyping can help provide a path to distinguishing important features. Hyperacusis is categorized into four subtypes: loudness, pain, annoyance, and fear.1 This differentiates two physically and two emotionally based components of the condition. This distinction represented an important step forward for clinicians to assess these subtypes—especially to determine whether it's the loudness of everyday sounds or the pain induced by those sounds that has the most impact on the patient. A small but growing body of hyperacusis publications now include pain in the discussion (with 39 articles found in a recent PubMed search).Shutterstock/aleks333, Hyperacusis, tinnitus, hearing loss.Figure 1: Percentage of respondents with asymmetrical hyperacusis. Difference in surveys not statistically significant (p = 0.40). Hyperacusis, tinnitus, hearing loss.Figure 2: Actions to prevent setbacks. Hyperacusis, tinnitus, hearing loss.The wide array of definitions has made establishing prevalence of hyperacusis challenging. In the 2014 National Health Interview Survey,2 5.9 percent of respondents had sensitivity to everyday sounds as determined by the question, “Do everyday sounds, such as from a hair dryer, vacuum cleaner, lawnmower, or siren, seem too loud or annoying to you?” This question applied to all who are more broadly described as having decreased sound tolerance. In a recent paper on decreased sound tolerance associated with blast exposure, Theodoroff, et al.,3 found that irrespective of blast exposure, 29 percent (53 of 181) of military service members and 40 percent (99 of 245) of U.S. military veterans reported some degree of decreased sound tolerance. These findings highlighted the need for better methods to screen for hyperacusis, and identify complaints of decreased sound tolerance as part of audiological evaluations. One of our aims at Hyperacusis Research Limited, Inc., is to identify key characteristics of hyperacusis to support basic scientific and clinical research. In 2015, a comprehensive registry of people with hyperacusis was initiated with the Coordination of Rare Diseases at Sanford (CoRDS) Registry. Over 200 patients have registered for the 98-question survey. While the anonymized data is available to any interested research institution, we have performed a preliminary analysis that has shown critical insights. Our findings highlight important areas for audiologists to assess when evaluating patients for hyperacusis. SURVEYS ON HYPERACUSIS COMPLAINTS Several factors must be considered about the applicability of the Sanford dataset to the hyperacusis population at large due to the extensive nature of the registration process and length of the survey. The effort required to complete the survey could bias the results toward worse case sufferers. Over the past few years, we have determined several characteristics that need closer investigation. We also wanted to hear more from the patients using open-ended questions. Therefore, we initiated a new survey to get insights beyond the Sanford registry and potentially shed light on whether the Sanford findings can be broadly applied. To ensure a wide range of patients, we recruited participants on six social media platforms, including those oriented toward tinnitus, considering the fact that about 30 to 40 percent of tinnitus sufferers have hyperacusis.4 We streamlined the survey design, limited it to 30 questions (which took an average of 11 minutes to complete), and included some questions from the Sanford registry to allow crossover analysis. Since June 2019, over 350 participants have completed the new survey. A leading question in the new survey asked participants to select up to three primary complaints related to hyperacusis. While the complaint list included 14 items, three complaints stood out: ear pain caused by sound, loudness sensation, and increased tinnitus from sound. With this rank order, we suspected that pain from sound is likely more prevalent in the hyperacusis population than previously assumed. Aural fullness and a thumping or fluttering sensation in the ear were also highly ranked. A question related to hyperacusis symmetry was: “Would you say that you experience your hyperacusis symptoms equally in each ear?” A similar question was also asked in the Sanford survey. The results of both surveys (see Fig.1) were statistically matched, which revealed that about half indicated having symptom differences between ears. Following this question, participants were asked: “On a scale of 0 to 10, how would you rate your level of symptom severity in each ear?” (with 0 for no symptoms and 10 for severe pain or major life impact), and 41 percent rated each ear differently for symptom level. The delta between ears averaged a dramatic 4.6 difference. An open question also asked participants to describe the differences in sensation that they experience between ears. A word analysis demonstrated that ear pain differences were the most common, followed by loudness sensation, tinnitus, and ear fullness. Additionally, most participants had an explanation for symptom differences between the ears. Most frequently, the initial injury was known to be one-sided, such as with a gun shot or a loud noise on one side. These findings are extremely important since hyperacusis has been considered as typically bilateral. But with many sufferers experiencing symptom differences between ears, the exact role of the central gain model and the hypothesis that various auditory pathways within the brain are primarily responsible for patients’ symptoms need to be examined more thoroughly. FOCUS ON PAIN AND SETBACKS On the topic of pain, 92 percent of the 2019 survey respondents said that sounds caused pain or physical discomfort. This number was well matched to the Sanford survey at 91 percent. Additional details from the Sanford survey showed that 62 percent of respondents experienced ear pain at least daily, and 75 percent indicated the ear pain was a result of being exposed to new loud noises. Once initiated, the pain cycle lasted weeks or longer for 28 percent of the respondents, and several days for 18 percent. Responses about the type of pain patients experienced (e.g., dull ache, burning, sharp, stabbing pain, and throbbing pain) were evenly distributed. A key focus of the 2019 survey (also briefly covered in the Sanford survey) was what patients refer to as a setback. Both surveys asked participants how often they experienced setbacks that made their condition worse. About 37 percent of Sanford survey respondents and 50 percent of the 2019 survey respondents reported having setbacks at least weekly. In the 2019 survey, a critical question related to setbacks was: “Think about your worst setback—what impact did it have?” Fifty-four percent indicated their setback made their condition worse than ever, and 43 percent said they usually needed a few weeks to a few months to recover from these setbacks. These results were like those of the Sanford survey. Notably, 14 percent of the 2019 survey respondents said they never fully recovered. This population represents the most challenging and most overlooked group of hyperacusis sufferers. SETBACK PREVENTION Setback prevention is a key focus for many hyperacusis sufferers. In the new survey, we asked: “Describe the actions you take to prevent setbacks.” A word cloud, shown in Figure 2, was generated from the responses. Avoiding loud sounds was the most common response, followed by wearing earplugs. The responses were logical, given that loud sounds were the main cause of setbacks. A clinically focused question asked: “If you have had a clinical evaluation for your hyperacusis, did the clinician ask you any question related to setbacks?” Only 29 percent reported that the topic of setbacks was covered by their clinician. These results represent critical components that need to be comprehended in clinical evaluations. A patient's history of setbacks should be considered when determining the best treatment approach and expected outcome. Many patients will likely rank setback prevention and reduction of pain symptoms as their top priorities. For some, perceiving sounds as excessively loud may be a low priority. In summary, the new 2019 brief hyperacusis survey reinforces the primary findings of the extensive Sanford registry. Both surveys suggest that hyperacusis with pain is common among hyperacusis sufferers. Also, many sufferers experience setbacks that temporarily or permanently make their symptoms worse. Therefore, setback prevention should be a top priority of clinical treatment programs. Opportunities also exist for researchers to study the physiological mechanism for setbacks and determine what inhibits or enables a quicker recovery. With a better understanding of these key characteristics of hyperacusis patients, a path will emerge to create a better future for them.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 235 · R0920

**Misophonia revised:New insights in phenomenology and psychotherapy**

2022 · other · en · https://core.ac.uk/download/555950115.pdf

The objectives of this thesis are first, to increase knowledge concerning the phenomenology of misophonia and second, to investigate the effectiveness of different treatments for misophonia.In this thesis the phenomenology of misophonia is studied in a highly qualitative and quantitative sample (N=575). This leads to new insights and an important revision of the diagnostic criteria. Misophonia is considered a psychiatric disorder, which is characterized by anger and disgust provoked by human sounds in particular.The effectiveness of group cognitive behavioral therapy (G-CBT) on misophonia symptoms compared to a waiting list control group is investigated in the first randomized controlled trial of G-CBT for misophonia worldwide. Three months of G-CBT reduces misophonia symptoms compared to the waiting list condition. Clinical improvement is found in 56% of all completers (37% intention-to-treat) compared to 0% in the waiting list control group. One year after the end of treatment, the reduction in misophonia symptoms sustains. This thesis also consists the treatment manual for G-CBT, illustrated by single clinical case study.Moreover, a pilot study of case series shows that alternative treatment options, notably eye movement desensitization and reprocessing (EMDR) therapy, can be considered. EMDR therapy, focused on emotionally disturbing misophonia-related memories, significantly reduces misophonia symptoms in three of eight participating patients.The new insights gained from the studies in this thesis contribute to a further development of scientific research into misophonia

**Решение:** -1 обзор литературы / концептуальная статья

---

### 236 · R0561

**Hypersensitivity to Sounds**

2024 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-3-031-35647-6_3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 237 · R0634

**A meta-analysis of transcranial magnetic stimulation in Tourette syndrome.**

2024 · Journal of psychiatric research · meta-analysis, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.jpsychires.2024.02.057

There is growing enthusiasm for the treatment of neuropsychiatric disorders using neuromodulation. While some reports claim that transcranial magnetic stimulation (TMS) can be used to treat Tourette Syndrome (TS), little research exists to support this assertion. This meta-analysis examined the efficacy of TMS to reduce tic severity in patients with TS. Additionally, it explored the effect of TMS to reduce premonitory urge severity-the primary mechanism implicated in the frontline evidence-based treatment of TS. Five treatment comparisons were selected using PRISMA guidelines. All studies included were required to be (1) a randomized controlled trial, (2) compare TMS to a sham condition, and (3) have all participants meet diagnostic criteria for a persistent tic disorder and/or TS. A random effects model meta-analysis examined the efficacy of using TMS to reduce tic severity and explored the effect of TMS to reduce premonitory urge severity. TMS did not significantly reduce tic severity (g = 0.44; 95% CI = -0.17, 1.05; z = 1.40; p = 0.16), but a moderate reduction in premonitory urge severity was found (g = 0.63; 95% CI = 0.9, 1.17; z = 2.27; p < 0.02). Trials with larger sample sizes and a preponderance of women were found to have greater therapeutic effects of TMS for tic severity. There is limited support for the use of TMS to reduce tic severity, though reductions in premonitory urge severity were observed. Major limitations of the existing literature are examined, with a call for research investigating newer TMS protocols and their use as a treatment augmentation strategy.

**Решение:** -6 не про мизофонию

---

### 238 · R1435

**Misophonia**

2015 · İstanbul Beykent Üniversitesi

Ayla alkolik babası ve sevgi dolu annesi ile birlikte yaşayan, seslere karşı uç noktalarda hassasiyetleri olan küçük bir kızdır. Babasının kavgacı karakteri Ayla'nın seslere karşı duyarlılığını arttırıp sosyal hayatını yaşanması zor bir hale sokmaktadır. Yıllar sonra evlendiğinde dahi bu rahatsızlıktan kurtulamamış, ancak bir takım önlemlerle gündelik hayata adapte olmaya çalışmıştır. Lakin yaşam koşullarının zorluğu ve yaşamındaki insanların tutumu onu her şeyi bırakıp sessiz bir ortamda doğada yaşamaya itecektir. Anahtar Kelimeler : Aile içi şiddet, ses, doğaAyla is a little girl who lives together with her alcoholic father and loving mother. She has a strong sensibility towards sounds which exceeds to extreme levels. The agressive character of her father increases her sensitiveness towards sounds and makes it hard for her to live her social life. Even years later, after getting married she still struggles with this disease. However by taking some precautions, she tries to adapt to daily life. However the difficulty of her life conditions and the attitude of the people in her life will push her to leave everything behind and go live in a quiet setting in nature. Key Words : Domestic violence, noise, natur

**Решение:** -1 обзорная публикация / словарный очерк

---

### 239 · R0256

**Transdiagnostic Cognitive Behavioral Therapy and Acceptance-Based Therapy on Emotional Dysregulation and Aggression in Adolescents with High Misophonia (Preprint)**

2025 · JMIR Publications Inc. · article, preprint · en · https://doi.org/10.2196/preprints.81562

UNSTRUCTURED This study examined the efficacy of transdiagnostic cognitive-behavioral therapy (T-CBT) and acceptance-based therapy (ABT) in reducing emotional dysregulation and aggression in adolescents with elevated misophonia symptoms. Employing a quasi-experimental pre-test/post-test design with a control group, the research targeted 45 adolescents from Etrat Public Model High School in Khalkhal, Iran, diagnosed with high misophonia via psychiatrist evaluation and clinical interview. Participants were purposively sampled and randomly assigned to T-CBT (n = 15), ABT (n = 15), or a no-treatment control group (n = 15). Interventions followed protocols adapted from Barlow et al. (2011) for T-CBT and Hayes et al. (2013) for ABT. Outcomes were measured using the Noise Sensitivity Screening Questionnaire (DSTS-S) , Buss and Perry Aggression Questionnaire (1992) , and Difficulties in Emotion Regulation Scale (DERS) . Data were analyzed via ANCOVA, controlling for baseline scores. Results indicated significant reductions in emotional dysregulation and aggression in both treatment groups compared to the control (p &lt; 0.05). No significant differences emerged between T-CBT and ABT, suggesting both interventions are viable for addressing misophonia-related symptoms. Findings underscore the comorbidity of emotional dysregulation and aggression in adolescents with misophonia and highlight the clinical utility of transdiagnostic and acceptance-based approaches. Future research should explore long-term outcomes and comparative effectiveness of these therapies.

**Решение:** ? школьная выборка (N=45 старшеклассниц), проверить скрининг пула

---

### 240 · R1028

**Family-Based Cognitive Behavioral Therapy for Youth With Misophonia: A Case Report**

2021 · Cognitive and Behavioral Practice · article · en · https://doi.org/10.1016/j.cbpra.2021.05.005

Abstract Misophonia is a common condition that causes significant distress and impairment for patients and families. Despite the growing body of literature, most treatment descriptions do not incorporate objective assessment measures or detail techniques to involve family members in addressing misophonia. This case report provides a step-by-step family-based cognitive-behavioral approach to treat youth with misophonia, uses objective rating scales to monitor therapeutic improvement, and elicits feedback on the therapeutic skills used between therapy sessions. It also provides guidance on implementing inhibitory learning exposures for youth with misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 241 · R0304

**Case Report: Potential of pharmacological treatment for auditory abnormal sensations with aripiprazole: a report of two cases.**

2025 · Frontiers in psychiatry · article, case reports, journal article · eng · https://doi.org/10.3389/fpsyt.2025.1614500

Auditory abnormal sensations encompass various subjective auditory symptoms such as tinnitus, hyperacusis, aural fullness, autophony, dysacusis, pseudo-hallucinations, and misophonia. Although tinnitus management typically includes lifestyle counseling and sound therapy, there remains no established treatment for symptoms like aural fullness or pseudo-hallucinations with unknown etiology. In cases where central sensory processing abnormalities or emotional instability are suspected, psychotropic medications may offer benefit. We report two cases in which aripiprazole, an atypical antipsychotic, was effective in treating such symptoms. In both cases, traditional approaches such as antidepressants and supportive therapy were insufficient, but aripiprazole led to marked improvement in subjective auditory symptoms. These cases suggest a potential role for pharmacological modulation of central sensory and emotional regulation in patients with auditory abnormal sensations. One involved a man with phonophobia and aural fullness, and the other a woman with tinnitus and pseudo-hallucinations.

**Решение:** -2 клинический случай / серия случаев

---

### 242 · R1500

**The Biological Mechanisms of Hyperacusis**

2009 · ASHA Leader · article · en · https://doi.org/10.1044/leader.ftr2.14112009.5

You have accessThe ASHA LeaderFeature1 Sep 2009The Biological Mechanisms of HyperacusisAnimal Models Help Uncover Brain Basis for Disorder Wei SunPhD, CCC-A Wei Sun Google Scholar More articles by this author , PhD, CCC-A https://doi.org/10.1044/leader.FTR2.14112009.5 SectionsAbout ToolsAdd to favorites ShareFacebookTwitterLinked In Hyperacusis, or recruitment, is characterized by an abnormally strong reaction or reduced tolerance to ordinary environmental sound. Hyperacusis can reduce the quality of life. Patients with severe hyperacusis avoid going to parties, restaurants, and even meetings, since the environment is just “too loud” for them. Some people with this condition will leave their homes only if wearing ear plugs. The prevalence of hyperacusis in the general population is about 9%–15% (Herraiz et al., 2006). Hyperacusis can occur along with a variety of disorders including acoustic trauma, stapedectomy, Williams syndrome in children, migraine attacks, facial paralysis, and tinnitus. The mechanism underlying hyperacusis is unclear and as yet there is no treatment. Physiological Mechanisms It has been hypothesized that hyperacusis is induced by hyperactivity of the auditory nerve, which will increase the sensitivity to a loud sound (Moore, 1995). Supporting this hypothesis is the fact that noise exposure, a common cause of hyperacusis, can broaden the tuning curve of the auditory nerve, i.e., the auditory nerve acquires poor frequency selectivity. This poor frequency selectivity was assumed to cause the faster recruitment of activated auditory fibers with increasing sound intensity. However, recent animal studies contradict this assumption because excitation of auditory nerve fibers decreases following acoustic trauma, suggesting that hyperacusis may not be induced by hyperactivity of the auditory nerve (Heinz et al., 2004). A growing body of evidence from animal studies shows that cochlear damage can induce an abnormally rapid growth in the amplitude of sound-evoked potentials as well as other neuronal response properties within the central auditory system (Salvi et al., 2000; Syka et al., 2000). Exposure to noise or ototoxic drugs can enhance the response in the central auditory system despite a reduced output from the cochlea. For example, when rats received a high dose of sodium salicylate (the major component of aspirin), known to temporarily induce high-frequency hearing loss and tinnitus, the amplitude of the compound action potential was reduced (Sun et al., 2009; see Figure 1A [PDF, 2.67 MB]). Paradoxically, the sodium salicylate dose significantly enhanced the sound-evoked auditory cortical response (Figure 1B [PDF, 2.67 MB]). Because the enhanced cortical response was not caused by a reduction in peripheral input, salicylate may increase the cortical response by adjusting the “volume” of neural input. Most activities in the brain are strongly regulated by inhibitory neurons, known as GABAergic neurons. A reduction of inhibitory influences in the brain may cause an increased state of excitation in the brain. Recent studies detected salicylate’s ability to reduce inhibitory neuronal activity in the auditory cortex, which presumably would result in an overall enhancement of the cortical response to sound (Wang et al., 2008). Because the auditory cortex is essential for sound perception, the enhanced cortical response to acoustic stimuli is to increase the perception of loudness and may underlie hyperacusis. Animal Model for Hyperacusis Because hyperacusis involves the perception of sound, a behavioral test is critical in an animal model of hyperacusis to corroborate the relationship of hyperacusis perception to changes in neurological activity. Several laboratories recently reported using the acoustic startle reflex, a contraction of the skeletal and facial muscles to sudden, intense sounds, to measure the behavioral response to loud sounds (Ison et al., 2007; Sun et al., 2009; Turner et al., 2008). As shown in Figure 2A [PDF], the startle reflex can be quantified by measuring the power of the animal’s response using the voltage output of a piezoelectric transducer mounted under the animal’s testing chamber. In normal animals, the acoustic reflex is proportional to the sound intensity. Interestingly, when animals develop aging-related high-frequency hearing loss, they show an exaggerated startle response to low-frequency sound stimuli. This exaggerated response suggests that the animal developed an increased sensitivity to low-frequency stimuli as it developed a high-frequency hearing loss. This observation is consistent with the frequent co-occurrence of hyperacusis with presbycusis in humans. We found that salicylate can induce an enhanced acoustic startle reflex response as well as mild hearing loss, as shown in Figure 2B [PDF]. The increased startle reflex is consistent with the salicylate-induced enhancement of the sound-evoked auditory cortex response described above and implies that hyperacusis may be related to the enhanced response in the central auditory system, such as in the auditory cortex. These results also suggest that the response in the central auditory system can be altered by ototoxic drugs or by another mechanism regardless of the level of peripheral input. The incidence of hyperacusis is very high among people who have tinnitus; 40%–86% of those who have tinnitus also have hyperacusis (Moller, 2007). Determining the biological mechanism of hyperacusis and whether there is a relationship between hyperacusis and tinnitus may provide insight for clinical treatment of both of these disorders. References Heinz M.G., & Young E.D. (2004). Response growth with sound level in auditory-nerve fibers after noise-induced hearing loss.Journal of Neurophysiology, 91, 784–95. CrossrefGoogle Scholar Herraiz C., Plaza G., & Aparicio J.M. (2006). Mechanisms and management of hyperacusis (decreased sound tolerance).Acta Otorrinolaringol Espanola, 57, 373–7. Google Scholar Ison J.R., Allen P.D., & O’Neill W.E. (2007). Age-Related Hearing Loss in C57BL/6J Mice has both Frequency-Specific and Non-Frequency-Specific Components that Produce a Hyperacusis-Like Exaggeration of the Acoustic Startle Reflex.Journal of the Association for Research in Otolaryngology, 8, 539–50. CrossrefGoogle Scholar Moller A.R. (2007). Tinnitus: presence and future.Progress in Brain Research, 166, 3–16. Google Scholar Moore B.C. (1995). Perceptual Consequences of Cochlear Damage. New York: Oxford University Press. CrossrefGoogle Scholar Salvi R.J., Wang J., & Ding D. (2000). Auditory plasticity and hyperactivity following cochlear damage.Journal of Hearing Research, 147, 261–74. Google Scholar Sun W., Lu J., Stolzberg D., Gray L., Deng A., Lobarinas E., & Salvi R.J. (2009). Salicylate increases the gain of the central auditory system.Neuroscience, 159, 325–334. CrossrefGoogle Scholar Syka J., & Rybalko N. (2000). Threshold shifts and enhancement of cortical evoked responses after noise exposure in rats.Journal of Hearing Research, 139, 59–68. Google Scholar Turner J.G., & Parrish J. (2008). Gap detection methods for assessing salicylate-induced tinnitus and hyperacusis in rats.Am J Audiol, 17, S185–92. LinkGoogle Scholar Wang H.T., Luo B., Huang Y.N., Zhou K.Q., & Chen L. (2008). Sodium salicylate suppresses serotonin-induced enhancement of GABAergic spontaneous inhibitory postsynaptic currents in rat inferior colliculus in vitro.Journal of Hearing Research, 236, 42–51. Google Scholar Author Notes Wei Sun, PhD, CCC-A, assistant professor in the Department of Communicative Disorders and Sciences at State University of New York at Buffalo, researches the physiological mechanisms of the central auditory system reorganization related to tinnitus and hyperacusis in animal models. His research is funded by The Royal National Institute for Deaf People and the American Federation for Aging Research. Contact him at [email protected]. Advertising Disclaimer | Advertise With Us Advertising Disclaimer | Advertise With Us Additional Resources FiguresSourcesRelatedDetails Volume 14Issue 11September 2009 Get Permissions Add to your Mendeley library History Published in print: Sep 1, 2009 Metrics Downloaded 402 times Topicsasha-topicsleader_do_tagleader-topicsasha-article-typesCopyright & Permissions© 2009 American Speech-Language-Hearing AssociationLoading ...

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 243 · R0244

**Designing for Special Neurological Conditions: Architecture Design Criteria for Anti-Misophonia and Anti-ADHD Spaces for Enhanced User Experience**

2025 · Architecture · article, journalarticle, text · en · https://doi.org/10.3390/architecture5040085

ADHD and misophonia are developmental neurological disorders that are currently increasing in prevalence due to excessive acoustic and visual pollution. ADHD, which is characterized by a lack of attention and excessive impulsive hyperactivity, and misophonia, which is hypersensitivity to sounds accompanied by a severe emotional and psychological reaction, are both affected by the user&rsquo;s spatial environment to a great extent. Spatial design can contribute to increasing or decreasing these unfavorable sensory triggers that affect individuals with ADHD and/or Misophonia. However, the role of architectural spatial design as a therapeutic approach to alleviate the symptoms of Misophonia and ADHD has never been proposed before in the literature, despite its accumulative and chronic effects on the user&rsquo;s experience in everyday life in terms of well-being and productivity. Therefore, the current work discusses this problem of neglecting the potential effect of architectural spatial design on alleviating Misophonia and ADHD. Thus, the objective of the current work is to propose customized architectural spatial design as a therapeutic approach to alleviate Misophonia and ADHD through adopting the compatible architectural trends of minimal and metaphysical architecture. The methodology of the current work includes a theoretical proposal of this customized architectural spatial design for alleviating these two special neurological conditions. This includes introducing and analyzing these two neurological conditions and their relation to and interaction with architectural spatial design, analyzing minimal and metaphysical architectural trends employed in the proposed therapeutic architectural design, and then proposing augmented and virtual reality as auxiliary add-ons to the architectural spatial design to boost its therapeutic effect. Minimal architecture achieves the &ldquo;no emotion&rdquo; criteria through reduced forms, patterns, and colors and adopts simple geometry and natural materials to reduce sensory stressors or stimuli, in order to alleviate the loss of attention and distraction prevalent in those with ADHD, as well as allowing the employment of acoustic materials to achieve acoustic comfort and noise blockage for Misophonia relief. Metaphysical architecture leads the hierarchy of sensory experience through the symbolistic, dynamic, and enigmatic composition of forms and colors, which enhance the spatial analysis and cognitive capacities of the inhabitants. Meanwhile, the use of customized virtual and augmented reality environments is an effective add-on to minimal and metaphysical architectural spaces thanks to its proven therapeutic effect in alleviating various neurological disorders and injuries. At this level of intervention, VR/AR can be used as an add-on to minimal-architecture design, to simulate varied scenarios, as minimal design offers a clean canvas for simulating these varied virtual environments. The other option is to build these customized VR/AR scenarios around a specific architectural element as an add-on metaphysical architecture design to lead the sensory experience and enable the user to detach from the physical constraints of the space. AI-generated designs were used as a proof of concept for the proposed customized architectural spatial design following minimal and metaphysical architecture, as well as to provide AR and VR scenarios as add-on architecture to enhance the therapeutic effect of these architectural spaces for Misophonia and ADHD patients. Furthermore, the validity of VR/AR as a therapeutic approach, alongside the customized architectural design, was discussed, and it was concluded that this study proves the need for extended clinical studies on its efficiency in the long run, which will be conducted in the future

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 244 · R0527

**Attributes of Provider Referrals for Digital Mental Health Applications in an Integrated Health System, 2019-2021.**

2024 · Psychiatric services (Washington, D.C.) · journal article · eng · https://doi.org/10.1176/appi.ps.20220401

This article describes trends and attributes associated with digital mental health application (DMHA) referrals from December 2019 through December 2021. In total, 43,842 DMHA referrals for 25,213 unique patients were extracted from the electronic health record of a large, diverse, integrated health system. DMHAs were aggregated by type (cognitive-behavioral therapy [CBT] or mindfulness and meditation [MM]). Monthly referral patterns were described and categorized into mutually exclusive clusters (MM, CBT, or MM and CBT). Multinomial logistic regression and post hoc predicted probabilities were used to profile patient, clinical, and encounter attributes among referral clusters. DMHA referrals increased, reached equilibrium, and then began to decline over the 25-month observation period. Compared with the referral cluster average, MM-alone referrals were more likely to occur for patients who were ages ≥65, who were Hispanic or Asian, whose reason for visit concerned mental health, and who had a primary diagnosis of other anxiety disorders. CBT-alone referrals were more likely to occur for patients with a primary diagnosis of depression and less likely to occur for Hispanic patients. Combined MM and CBT referrals were more likely to occur for patients who were ages 18-30, whose reason for visit was "other," and who had a primary diagnosis of depression and were less likely to occur for Hispanic patients and those ages ≥65. Although this study demonstrates readiness to integrate DMHA referral into clinical workflows, observed variations in attributes of referral clusters support the need to further investigate provider decision making and whether referral patterns are optimal and sustainable.

**Решение:** -6 не про мизофонию

---

### 245 · R1410

**Treating the Initial Physical Reflex of Misophonia With the Neural Repatterning Technique: A Counterconditioning Procedure**

2015 · Psychological Thought · article, journalarticle/article · en · https://doi.org/10.5964/psyct.v8i2.138

Misophonia is a condition in which a person has an acute emotional response of anger or disgust to a commonly occurring innocuous auditory or visual stimulus referred to as a trigger. This case details the effective treatment of misophonia in a young woman that included a counterconditioning treatment called the Neural Repatterning Technique (NRT), which combines a continuous positive stimulus and a reduced intensity, intermittent trigger. The treatment was delivered via the Misophonia Trigger Tamer smartphone app and all treatments were conducted independently by the patient. In this patient, the trigger elicited a physical reflex of contraction of the flexor digitorum profundus, which caused her to clench her fist. To enhance the effect of the NRT treatment, Progressive Muscle Relaxation was incorporated to increase her ability to deliberately relax the affected muscle during treatment. During NRT treatment sessions, the patient experienced a weak physical reflex to the reduced trigger stimulus but no emotional response. Her emotional response of misophonia was not treated, but when the physical reflex extinguished, the emotional response also extinguished. This case indicates that the misophonic response includes a Pavlovian-conditioned physical reflex. It is proposed that the trigger elicited the physical reflex and the physical reflex then elicited the conditioned emotional response that is characteristic of misophonia. Because of the conditioned reflex nature of misophonia, it is proposed that a more appropriate name for this disorder would be Conditioned Aversive Reflex Disorder.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 246 · R0574

**Current Trends in the Treatment of Misophonia**

2024 · Psikiyatride Guncel Yaklasimlar - Current Approaches in Psychiatry · article, journalarticle, review · en · https://doi.org/10.18863/pgy.1302983

Misophonia is a disorder characterized by emotional and physiological responses that occur in response to certain auditory stimuli. Visual, tactile, and olfactory stimuli, primarily oral and nasal sounds such as eating, nose, and respiratory sounds, reveal misophonic responses. People with misophonia may have difficulty in social interactions, and work or school performance may be adversely affected. Misophonia symptoms can also cause anxiety, depression, and other mental health problems. Physiological reactions in the body, such as pain, sweating, tachycardia, hot flashes, and breathing difficulties, negatively affect people's physical health. For this reason, people's physical and mental health and quality of life are significantly affected. The absence of agreed diagnostic criteria for the diagnosis of misophonia and the lack of sufficient data to classify it as a psychiatric disorder has led to the lack of validated treatment guidelines. However, there are treatment recommendations discussed in the literature for misophonia, which has a prevalence of 20% in a limited number of studies and negatively affects the functionality of the individual. In the management of misophonia, tinnitus re-education therapy (TRT) was used as audiological treatment, antidepressants, and anxiolytics were used as pharmacological treatment and cognitive behavioral therapies were used as therapy. Other suggested treatment recommendations are neural remodeling technique, sequential remodeling hypnotherapy, trauma prevention technique, and trauma and tension reduction exercises. This review aims to present the treatment approaches available in the literature together and to understand the need for experimental evidence for treatment methods.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 247 · R1382

**Tinnitus, Hyperacusis, Misophonia☆**

2016 · Elsevier eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1016/b978-0-12-809324-5.02028-9

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 глава книги / справочник

---

### 248 · R0999

**Race and Sex Bias in the Autism Diagnostic Observation Schedule (ADOS-2) and Disparities in Autism Diagnoses**

2022 · JAMA Network Open · article · eng · https://doi.org/10.1001/jamanetworkopen.2022.9503

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 249 · R1235

**MisophoniAPP: Person-Centric Gamified Therapy for Smarter Treatment of Misophonia**

2019 · IEEE Global Conference on Signal and Information Processing · article, conference object, journalarticle · en · https://doi.org/10.1109/globalsip45357.2019.8969513

Misophonia is a newly-classified chronic psychiatric condition in which an individual experiences highly-negative reactions to "trigger" sounds that do not affect others. In this work, a website has been developed, entitled "MisophoniAPP", as a person-centric serious game which provides a relaxing environment for the treatment of misophonia through exposure therapy. Using highly customizable gameplay and an interface that allows users and administrators to set individualized goals and rewards, as well as data monitoring to track an individual's progress, MisophoniAPP addresses the challenge posed by conventional Cognitive Behavioral Therapy and Neural Repatterning Technique approaches, which often only assist a limited subset of the misophonia population.

**Решение:** -3 выборка набрана из-за мизофонии (испытание терапии)

---

### 250 · R0874

**An evolutionary account of impairment of self in cognitive disorders**

2022 · Cognitive Processing · article · en · https://doi.org/10.1007/s10339-022-01110-4

Recent research has proposed that certain aspects of psychosis, as experienced in, e.g., schizophrenia (SCZ), but also aspects of other cognitive conditions, such as autism spectrum disorders (ASD) and synesthesia, can be related to a shattered sense of the notion of self. In this paper, our goal is to show that altered processing of self can be attributed to an abnormal functioning of cortico-striatal brain networks supporting, among other, one key human distinctive cognitive ability, namely cross-modality, which plays multiple roles in human cognition and language. Specifically, our hypothesis is that this cognitive mechanism sheds light both on some basic aspects of the minimal self and on some aspects related to higher forms of self, such as the narrative self. We further link the atypical functioning in these conditions to some recent evolutionary changes in our species, specifically, an atypical presentation of human self-domestication (HSD) features. In doing so, we also lean on previous work concerning the link between cognitive disorders and language evolution under the effects of HSD. We further show that this approach can unify both linguistic and non-linguistic symptoms of these conditions through deficits in the notion of self. Our considerations provide further support for the hypothesis that SCZ and ASD are diametrically opposed cognitive conditions, as well for the hypothesis that their etiology is associated with recent human evolution, leading to a deeper understanding of the causes and symptoms of these disorders, and providing new cues, which can be used for an earlier and more accurate diagnostics.

**Решение:** -6 не про мизофонию

---

### 251 · R1290

**Diplacusis**

2018 · Digital Commons - East Tennessee State University (East Tennessee State University) · article

Book Summary: Hyperacusis and Disorders of Sound Intolerance: Clinical and Research Perspectives is a professional resource for audiology practitioners involved in the clinical management of patients who suffer from sound tolerance concerns. The text covers emerging assessment and intervention strategies associated with hyperacusis, disorders of pitch perception, and other unusual processing deficits of the auditory system. In order to illustrate the patients perspectives and experiences with disorders of auditory processing, cases are included throughout. This collection of diagnostic strategies and tools, evidence-based clinical research, and case reports provides practitioners with avenues for supporting patient management and coping. It combines new developments in the understanding of auditory mechanisms with the clinical tools developed to manage the effects such disorders exert in daily life. Topics addressed include unusual clinical findings and features that influence a patient s auditory processing such as their perceptual accuracy, recognition abilities, and satisfaction with the perception of sound. Hyperacusis is covered with respect to its effects, its relation to psychological disorders, and its management. Hyperacusis is often linked to trauma or closed head injury and the text also considers the management of patients with traumatic brain injury as an opportunity to illustrate the effectiveness of interprofessional care in such cases. Interventions such as cognitive behavioral therapy, self-efficacy training, and hearing aid use are reported in a way that enhances clinicians' ability to weave such strategies into their own work, or into their referral system. Hyperacusis and Disorders of Sound Intolerance illuminates increasingly observed auditory-related disorders that challenge students, clinicians, physicians, and patients. The text elucidates and reinforces audiologists contributions to polytrauma and interprofessional care teams and provides clear definitions, delineation of mechanisms, and intervention options for auditory disorders.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 252 · R1422

**A striking reduction of simple loudness adaptation in autism.**

2015 · Scientific reports · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1038/srep16157

Abstract Reports of sensory disturbance, such as loudness sensitivity or sound intolerance, are ubiquitous in Autism Spectrum Disorder (ASD) but a mechanistic explanation for these perceptual differences is lacking. Here we tested adaptation to loudness, a process that regulates incoming sensory input, in adults with ASD and matched controls. Simple loudness adaptation (SLA) is a fundamental adaptive process that reduces the subjective loudness of quiet steady-state sounds in the environment over time, whereas induced loudness adaptation (ILA) is a means of generating a reduction in the perceived volume of louder sounds. ASD participants showed a striking reduction in magnitude and rate of SLA relative to age and ability-matched typical adults, but in contrast ILA remained intact. Furthermore, rate of SLA predicted sensory sensitivity coping strategies in the ASD group. These results provide the first evidence that compromised neural mechanisms governing fundamental adaptive processes might account for sound sensitivity in ASD.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 253 · R0850

**Clinical management of sound tolerance conditions (Henry et al., 2022)**

2022 · ASHA journals · other/online resource · https://doi.org/10.23641/asha.20164130

Purpose: For some people, exposure to everyday sounds presents a significant problem. The purpose of this tutorial was to define and differentiate between the various sound tolerance conditions and to review some options for their clinical management. Method: We informally reviewed the literature regarding sound tolerance conditions. The terminology and definitions provided are mostly consistent with how these terms are defined. However, many inconsistencies are noted. Methods of assessment and treatment also differ, and different methodologies are briefly described. Results: Hyperacusis describes physical discomfort or pain when any sound reaches a certain level of loudness that would be tolerable for most people. Misophonia refers to intense emotional reactions to certain sounds (often body sounds such as chewing and sniffing) that are not influenced by the perceived loudness of those sounds. Noise sensitivity refers to increased reactivity to sounds that may include general discomfort (annoyance or feeling overwhelmed) due to a perceived noisy environment, regardless of its loudness. Phonophobia , as addressed in the audiology profession, describes anticipatory fear of sound. Phonophobia is an emotional response such as anxiety and avoidance of sound due to the “fear” that sound(s) may occur that will cause a comorbid condition to get worse (e.g., tinnitus) or the sound itself will result in discomfort or pain. (Note that phonophobia is a term used by neurologists to describe “migraineur phonophobia”—a different condition not addressed herein.) Conclusions: The literature addresses sound tolerance conditions but reveals many inconsistencies, indicating lack of consensus in the field. When doing an assessment for decreased sound tolerance, it is important to define any terms used so that the patient and all health care professionals involved in the care of the patient are aligned with the goals of the treatment plan. Treatment generally involves gradual and systematic sound desensitization and counseling. Supplemental Material S1. Tinnitus and Hearing Survey. Supplemental Material S2. Sound Tolerance Interview. Henry, J. A., Theodoroff, S. M., Edmonds, C., Martinez, I., Myers, P. J., Zaugg, T. L., &amp; Goodworth, M.-C. (2022). Sound tolerance conditions (hyperacusis, misophonia, noise sensitivity, and phonophobia): Definitions and clinical management. American Journal of Audiology . Advance online publication. https://doi.org/10.1044/2022_AJA-22-00035

**Решение:** -1 обзор литературы / концептуальная статья

---

### 254 · R1268

**Uncomfortable loudness levels among children and adolescents seeking help for tinnitus and/or hyperacusis.**

2018 · International journal of audiology · journal article, journalarticle/article · eng · https://doi.org/10.1080/14992027.2018.1453617

OBJECTIVE: To assess the prevalence of hyperacusis and severe hyperacusis among children and adolescents seen at an audiology outpatient tinnitus and hyperacusis service. DESIGN: This was a retrospective study. Hyperacusis was considered as present if the average uncomfortable loudness level (ULL) at 0.25, 0.5, 1, 2, 4 and 8 kHz for the ear with the lower average ULL, which is denoted as ULLmin, was ≤77 dB HL. Severe hyperacusis was considered as present if the ULL was 30 dB HL or less for at least one of the measured frequencies for at least one ear. STUDY SAMPLE: There were 62 young patients with an average age of 12 years (SD = 4.1 years, range 4-18 years). RESULTS: Eighty-five percent of patients had hyperacusis and 17% had severe hyperacusis. On average, ULLs at 8 kHz were 9.3 dB lower than ULLs at 0.25 kHz. For 33% of patients, ULLs were at least 20 dB lower at 8 than at 0.25 kHz. CONCLUSIONS: Among children and adolescents seen at an audiology outpatient clinic for tinnitus and hyperacusis, hyperacusis diagnosed on the basis of ULLs is very prevalent and it is often characterised by lower ULLs at 8 than at 0.25 kHz.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 255 · R1538

**Journal of the Acoustical Society of America**

1972 · Ultrasonics · article · en · https://doi.org/10.1016/0041-624x(72)90262-4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 не про мизофонию

---

### 256 · R1256

**Decreased sound tolerance associated with blast exposure.**

2019 · Scientific reports · article, journal article, research support, u.s. gov't, non-p.h.s. · eng · https://doi.org/10.1038/s41598-019-46626-6

Abstract Current research on blast and other injuries sustained by United States Service members and Veterans of the Iraq and Afghanistan Wars reveals a multitude of auditory complaints linked to exposures experienced during these conflicts. Among these complaints is decreased sound tolerance, which refers to a class of auditory-related problems including physical and/or psychological reactions to aspects of everyday sounds. Limited attention has been given to the possible relationship between blast exposure and decreased sound tolerance in Service members and Veterans, which is the purpose of this report. Baseline data were gathered and analyzed from 426 Service members (n = 181) and Veterans (n = 245) who participated in the Noise Outcomes in Servicemembers Epidemiology (NOISE) Study. Logistic regression analyses were performed to generate odds ratios (ORs) with 95% confidence intervals (CIs) for each group, adjusted for age and sex. Of those who reported blast exposure, 33% of Service members (adjusted OR = 1.4; CI = 0.7–2.8) and 48% of Veterans (adjusted OR = 1.9; CI = 1.1–3.3) reported decreased sound tolerance. Among Service members and Veterans who did not report blast exposure, 28% and 34% respectively, also reported decreased sound tolerance. Overall, blast exposure increased the likelihood of participants reporting decreased sound tolerance. The strength of this association was significant in Veterans.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 257 · R0911

**Sound Tolerance Conditions (Hyperacusis, Misophonia, Noise Sensitivity, and Phonophobia): Definitions and Clinical Management.**

2022 · American journal of audiology · article, journal article, review · eng · https://doi.org/10.1044/2022_aja-22-00035

Purpose: For some people, exposure to everyday sounds presents a significant problem. The purpose of this tutorial was to define and differentiate between the various sound tolerance conditions and to review some options for their clinical management. Method: We informally reviewed the literature regarding sound tolerance conditions. The terminology and definitions provided are mostly consistent with how these terms are defined. However, many inconsistencies are noted. Methods of assessment and treatment also differ, and different methodologies are briefly described. Results: Hyperacusis describes physical discomfort or pain when any sound reaches a certain level of loudness that would be tolerable for most people. Misophonia refers to intense emotional reactions to certain sounds (often body sounds such as chewing and sniffing) that are not influenced by the perceived loudness of those sounds. Noise sensitivity refers to increased reactivity to sounds that may include general discomfort (annoyance or feeling overwhelmed) due to a perceived noisy environment, regardless of its loudness. Phonophobia, as addressed in the audiology profession, describes anticipatory fear of sound. Phonophobia is an emotional response such as anxiety and avoidance of sound due to the “fear” that sound(s) may occur that will cause a comorbid condition to get worse (e.g., tinnitus) or the sound itself will result in discomfort or pain. (Note that phonophobia is a term used by neurologists to describe “migraineur phonophobia”—a different condition not addressed herein.) Conclusions: The literature addresses sound tolerance conditions but reveals many inconsistencies, indicating lack of consensus in the field. When doing an assessment for decreased sound tolerance, it is important to define any terms used so that the patient and all health care professionals involved in the care of the patient are aligned with the goals of the treatment plan. Treatment generally involves gradual and systematic sound desensitization and counseling. Supplemental Material: https://doi.org/10.23641/asha.20164130

**Решение:** -1 обзор литературы / концептуальная статья

---

### 258 · R1542

**Fundamentals of Biochemistry.**

1941 · Annals of Internal Medicine · article · en · https://doi.org/10.7326/0003-4819-14-8-1452_1

1. The aim of this report is to review whether A-Weighting accurately represents the hearing of the whole UK population, to explore the consequences if it does not, and to make recommendations for future research to address the problems identified. 2. The approach taken was to first research the construction of A-Weighting from its root in early research on loudness perception and the development of the equal loudness contours. We then identified three groups of interest, who may not be well represented by A-Weighting. These are people with age-related hearing loss, neurodivergent people, and noise-sensitive people. These groups were chosen because they each represent a different kind of hearing difference, and they are all a substantial size. 3. A detailed literature review was conducted to examine the available evidence of hearing differences in the three groups and to discuss how these relate to A-Weighting and its uses. We reviewed 540 papers and cite 182 in this report. This dataset was then analysed to identify significant research gaps and suggest future research to fill them. 4. A-Weighting was found to be a significant way in which the assumption of normal hearing is embedded in a very wide range of acoustic assessment and legislation. This is because A-Weighting was developed from the equal loudness contours, and the contours are produced from measurements on a relatively small sample of otologically normal people – 18-25-year-olds with no hearing impairment. This is important because A-Weighting extends far beyond its original use to convert sound levels into loudness estimates and is now found in most assessments and control of noise worldwide, from product design to environmental noise. 5. People with age-related hearing loss represent 7.9% of the UK population. Age-related hearing loss is caused by degradation of the hair cells’ transducer mechanism in the inner ear. Among other effects, this typically causes problems with masking, where it becomes harder to pick a target speech sound out of a noisy background. Because background noise is usually quantified using A-Weighting, and A-Weighting models normal hearing, this may mean that the enhanced need for reduced background interference is often not met for this group. 6. Neurodivergent people (who include autistic people, those with attention deficit hyperactivity disorder (ADHD), dyslexia, dyspraxia, dysgraphia, dyscalculia, and Tourette’s) make up about 10% of the UK population. Evidence was found of auditory processing differences for autistic people, and for people with ADHD and dyslexia. The auditory processing differences occur at a low level in the brain and can result in difficulty separating out sound signals, especially when trying to listen to someone speak against a background of competing speech. It is likely that enhanced background noise targets would improve the experience of this group, but it is currently difficult to translate the laboratory findings on auditory processing into new noise assessment methods. There is too little evidence for people with dyspraxia, dyscalculia, dysgraphia and Tourette’s to base a conclusion on. 7. People who are noise-sensitive represent 17-50% of the population. In this report, this group included people who are more sensitive to general noise, people with misophonia and people with hyperacusis. For this group, the widespread use of A-Weighted sound level to predict noise annoyance is likely to significantly underpredict their heightened response. Hyperacusis is very common in autistic people, and it is particularly likely that A-Weighted levels do not represent the experience of this group. 8. It is not possible to simply adapt the A-Weighting curve to better fit any of the groups at this time. Partly this is because of lack of data on how to adjust, but mostly it is because most of the differences in sound perception are not equivalent to a simple transformation in loudness. The exception is for people with hyperacusis, where more detailed data on their loudness responses might enable a new weighting to be derived. 9. The overarching research gap identified is a lack of translational research. There is a need for research that builds on existing laboratory studies of hearing differences and translates them into guidelines for practitioners to assess sound and design spaces suitable for people with atypical hearing. 10. We also identify nine specific research gaps and projects to address them: a. Acoustic guidelines for spaces for people with a hearing impairment b. Acoustic design guidelines for people with auditory processing problems c. Accurate estimate of the numbers of noise sensitive people in the UK d. Loudness for people with age-related hearing impairment e. Loudness functions for autistic people with hyperacusis f. Equal loudness contours for autistic people with hyperacusis g. Demographic factors as a modulating effect on neurodivergent hearing h. Loudness functions for people with hyperacusis i. Psychoacoustic factors in misophonia Of these, we suggest that the first three are the most important. 11. This report represents an initial exercise in a much larger project for acoustics to respond to the aural diversity movement – the idea that a wide range of different kinds of hearing differences exist, in contrast to the assumed binary division of normal hearing and impaired hearing. This project could be repeated with other groups of people, such as those with noise-induced hearing loss, Meniere’s disease, or many other conditions.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 259 · R0718

**Habituation of auditory responses in young autistic and neurotypical children.**

2023 · Autism research : official journal of the International Society for Autism Research · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1002/aur.3022

Abstract Prior studies suggest that habituation of sensory responses is reduced in autism and that diminished habituation could be related to atypical autistic sensory experiences, for example, by causing brain responses to aversive stimuli to remain strong over time instead of being suppressed. While many prior studies exploring habituation in autism have repeatedly presented identical stimuli, other studies suggest group differences can still be observed in habituation to intermittent stimuli. The present study explored habituation of electrophysiological responses to auditory complex tones of varying intensities (50–80 dB SPL), presented passively in an interleaved manner, in a well‐characterized sample of 127 autistic ( M DQ = 65.41, SD = 20.54) and 79 typically developing ( M DQ = 106.02, SD = 11.50) children between 2 and 5 years old. Habituation was quantified as changes in the amplitudes of single‐trial responses to tones of each intensity over the course of the experiment. Habituation of the auditory N2 response was substantially reduced in autistic participants as compared to typically developing controls, although diagnostic groups did not clearly differ in habituation of the P1 response. Interestingly, the P1 habituated less to loud 80 dB sounds than softer sounds, whereas the N2 habituated less to soft 50 dB sounds than louder sounds. No associations were found between electrophysiological habituation and cognitive ability or participants' caregiver‐reported sound tolerance (Sensory Profile Hyperacusis Index). The results present study results extend prior research suggesting habituation of certain sensory responses is reduced in autism; however, they also suggest that habituation differences observed using this study's paradigm might not be a primary driver of autistic participants' real‐world sound intolerance.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 260 · R0187

**Developmental plasticity and network-level mechanisms in misophonia: A theory-building review.**

2026 · Behavioural brain research · article, journal article, review · eng · https://doi.org/10.1016/j.bbr.2026.116248

Introduction: Misophonia is a decreased sound tolerance (DST) condition characterized by disproportionate emotional, autonomic, and behavioral responses to specific, typically low-intensity sounds. Despite increasing recognition, its neurobiological basis remains incompletely understood, particularly with respect to its typical onset during late childhood and adolescence. Existing models emphasize auditory–limbic conditioning but may not fully account for developmental vulnerability or stimulus specificity. This theory-building review proposes a developmental neurobiological framework in which misophonia is conceptualized as a disorder of perception–emotion coupling, potentially shaped by maladaptive plasticity across interacting auditory, salience, limbic, and prefrontal networks during sensitive periods of maturation. Methods: A theory-driven narrative review was conducted, integrating evidence from neuroimaging, electrophysiological, autonomic, and clinical studies. Relevant literature was identified through PubMed, Scopus, and Web of Science databases, covering the period up to early 2026. Search terms included “misophonia,” “auditory processing,” “salience network,” and “development.” Jastreboff's conditioned reflex model was considered alongside contemporary frameworks from network neuroscience. This review is selective and hypothesis-generating rather than systematic. Results: Available evidence suggests that exaggerated, stimulus-specific salience attribution to auditory stimuli—potentially mediated by anterior insula–centered networks—may interact with relatively immature prefrontal regulatory mechanisms during development. This interaction may contribute to the strengthening of auditory–limbic associations and the emergence of persistent, context-dependent misophonic responses. Conclusions: Reframing misophonia within a developmental network framework may help situate the condition within disorders involving altered sensory appraisal and emotional regulation, while preserving its stimulus-specific profile. This perspective generates testable hypotheses and may provide a basis for future empirical research and the development of mechanism-informed intervention strategies.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 261 · R0734

**Auditory discomfort in visually sensitive individuals**

2023 · Frontiers in Psychology · article · en · https://doi.org/10.3389/fpsyg.2023.1126481

Introduction: Sensory discomfort occurs in clinical and non-clinical populations. While some of the parameters that evoke visual discomfort have been identified, the parameters of sounds that evoke auditory discomfort are largely unknown. Methods: We presented various sounds and asked participants to rate the discomfort they experienced. In Experiments 1 and 2 tones were presented at frequencies between 0.25-8 kHz and modulated sinusoidally in amplitude at frequencies between 0-32 Hz. In Experiment 3 tones were swept in frequency from 500 Hz-2 kHz at sweep rates of 5-50 per second. In Experiment 4, sweeps varied in frequency range and central frequency. Results: Discomfort increased with frequency. The effects of the amplitude modulation and sweep rate on discomfort were relatively small and were experienced mainly at low modulation frequencies and high sweep rates. Individuals who experienced visuo-perceptual distortions in the Pattern Glare (PG) Test reported greater auditory discomfort. Discussion: This suggests that sensory sensitivity in one modality may occur in another.

**Решение:** -6 не про мизофонию

---

### 262 · R1521

**Relations of the Working Conditions, Quality of Life and Voice Perception in Municipal High School Teachers of the City of Belo Horizonte.**

2005 · Programa de Estudos Pós-Graduados em Fonoaudiologia

Pensar nos distúrbios vocais como doença relacionada ao trabalho é uma tarefa de grande complexidade Requer analisar as condições ambientais de trabalho conhecer o histórico profissional e pessoal averiguar os possíveis hábitos vocais inadequados e os fatores extrínsecos à ocupação que compreende a saúde incluindo a qualidade de vida determinada por meio de fatores físicos biológicos psicossociais e do ambiente O objetivo desta pesquisa foi estudar as relações entre a qualidade de vida as condições no trabalho e a percepção da voz nos professores e assim especificamente identificar presença de queixa vocal, relacionar a queixa vocal com gênero associar queixa vocal com condições de saúde e trabalho e avaliar o impacto da voz na qualidade de vida Metodologia: participaram desta pesquisa 319 professores sendo 199 do gênero feminino e 120 no gênero masculino, em atividade laborativa no Ensino Médio da rede municipal da cidade de Belo Horizonte. Os professores preencheram 3 protocolos auto-explicativos e de auto-resposta que respectivamente contemplaram as seguintes etapas: o levantamento profissional e pessoal; levantamento dos indicadores da qualidade de vida; e avaliação da percepção da qualidade de vida e voz. Os resultados indicaram que 155 (48,9%) da amostra apresentaram queixa correspondendo a 106 (33,4%) do gênero feminino e 49 (15,4%) do gênero masculino. A variável gênero não se mostrou significativa na situação de queixa vocal. Foram identificadas associações estatisticamente significantes entre queixa vocal e distúrbios digestivo emocional intolerância a sons intensos rinite sinusite amigdalite faringite laringite bronquite alergia e exposições à poeira e ao ruído. A média dos escores nos domínios do WHOQOL-Bref foi de 63. O escore global do QVV resultou em 84,4. Conclusão: Foi significativo o número de professores em atividade profissional que apresenta queixa vocal; não existe relação entre queixa vocal e sexo; existem indicadores de condições de saúde e de ambiente desfavoráveis para trabalho; o impacto negativo da voz na qualidade de vida foi considerado baixo; a qualidade de vida dos professores foi considerada regularIt is a very complex task to see vocal disorders as an illness associated with working activities. It requires leads us to investigate working environmental conditions, be familiar with employee's professional and personal history, and analyze inappropriate vocal habits. Other factors, we must investigate include factors outside of work concerned with health, including the quality of life, which is determined by physical, biological, social, psychosocial and environmental factors. The objective of this research was to study the connections among working conditions, quality of life and voice perception in the teachers and, specifically, to identify the presence of vocal complaints, to relate vocal complaints with gender, and to associate vocal complaints with health and working conditions, as well as to evaluate the impact of voice on these teachers' quality of life. Methodology:Subjects of this study were 319 teachers, 199 female and 120 male, who are presently working in city schools of Belo Horizonte. Ali of them answered three self-explanatory and self-answered protocols according to the following stages: professional and personal history, quality of life indicators and evaluation of the perception of quality of life and voice. The results indicated that 155 (48.9%) of the sample presented complaints, 106 (33.4%) of the females and 49 (15.4%) of the males. However, in vocal complaint factors, gender was not considered to be a significant variable. Considered to be a significant statistically correlations between vocal complaint and gastric problems, psychiatric problems, emotional problems, high sound intolerance, rhinitis, sinusitis, tonsillitis, pharyngitis, laryngitis, bronchitis, allergy, exposure to dust and to noise were found. The global score of WHOQOL-Bref was 63. The global score of QVV was 82.8, which is considered a good score because it is close to 100. Conclusion: The number of working school teachers who present vocal complaints is significant; there is no relation between vocal complaint and gender; there are indicators of health conditions and environmental factors that are unfavorable for work; the negative impact of the voice on the quality of life was considered to be lo

**Решение:** -6 не про мизофонию

---

### 263 · R0591

**Metacognitive Interpersonal Therapy for Misophonia: A Single-Case Study.**

2024 · Brain sciences · article, case reports, journal article · eng · https://doi.org/10.3390/brainsci14070717

BACKGROUND: Misophonia is a chronic condition in which the exposure to specific sounds increases the arousal and recurrence of specific intense negative emotions. We hypothesized that misophonia may be strongly related to maladaptive interpersonal schemas that create difficulties in interpersonal relationships. Subjects with maladaptive interpersonal schemas think that other people try to subjugate, criticize, dominate, exploit, deceive, disregard, and humiliate them. Furthermore, these patients typically endorse a representation of self as mistreated, constricted, harmed, damaged, humiliated, impotent, inadequate, or fragile. METHODS: We describe the course of a treatment of Metacognitive Interpersonal Therapy (MIT) in a young man presenting misophonia and co-occurrent obsessive-compulsive personality disorder (OCPD) and avoidant personality disorder (AvPD), with narcissistic traits and normal hearing. We collected qualitative and quantitative data at the beginning of the intervention and at 2 years follow-up. RESULTS: The therapy aimed at increasing awareness of maladaptive interpersonal schemas and promoting a healthy self. The results reported a significant decrease in misophonia; behavioural experiments were used to increase the quality of social relationships and tolerance to the trigger sounds. CONCLUSIONS: MIT can be an effective therapy for the treatment of misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 264 · R0054

**A qualitative investigation of living with misophonia.**

2026 · Journal of health psychology · article, journal article, journalarticle · eng · https://doi.org/10.1177/13591053261464343

As a relatively new condition, little is understood about the individual’s experience of misophonia. Twenty-four semi-structured interviews were carried out with people with self-reported misophonia. Thematic analysis was used to analyse the data and develop inductive themes. Three themes were developed, ‘the experience of the response to the trigger (with three subthemes: emotional, physiological, and behavioural)’, ‘the perceived impact of misophonia (with three subthemes: the impact on self-esteem, relationships and day-to-day life)’, and ‘Influencing factors (with three subthemes: coping, feeling understood, and exacerbating factors)’. The results give an in-depth understanding of the experience of a misophonic response, the impact on the self and interactions with others, and how they coped. The results suggest targeting the avoidant coping strategies and raising awareness of available treatment and support groups may be helpful for managing misophonia and reducing the negative impact of this condition.</jats:p

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 265 · R1060

**The Role of Community Health Workers in HIV Care Engagement: A Qualitative Study of Stakeholder Perspectives in Tanzania.**

2021 · The Journal of the Association of Nurses in AIDS Care : JANAC · journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1097/jnc.0000000000000267

Suboptimal retention in HIV care is a major driver of the global epidemic, including in sub-Saharan Africa. In Tanzania, the national Community-Based HIV Services program integrates volunteer community health workers (CHWs) to support patient care engagement and reduce the burden placed on HIV clinic nurses; however, few studies have assessed the value of CHWs supporting HIV care. Qualitative interviews were conducted with 48 administrators, nurses, CHWs, and patients to explore strengths and limitations of the Community-Based HIV Services program. Stakeholders believed CHWs are uniquely positioned to establish trust and provide patient support. Patients who had frequent contact with CHWs described them as valued sources of education and encouragement, but fewer than half of the patients interviewed had ever met with a CHW. Clinic nurses described feeling disconnected from CHWs, and stakeholders highlighted the need for financial, logistical, and educational support to rejuvenate the program and effectively address care engagement challenges.

**Решение:** -6 не про мизофонию

---

### 266 · R0046

**Special issue on misophonia and hyperacusis.**

2026 · Hearing research · editorial, journalarticle, journal article · eng · https://doi.org/10.1016/j.heares.2026.109772

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 редакционная статья / письмо

---

### 267 · R0560

**Examination of the mediating role of emotion regulation difficulties on the relationship between childhood trauma and misophonia**

2024 · Biruni Üniversitesi

Bu çalışmanın amacı, çocukluk çağı travmaları ve mizofoni arasındaki ilişkide duygu düzenleme güçlüğünün aracılık rolünün incelenmesidir. Araştırmanın çalışma grubunu, ortaya çıkan seslerden rahatsız olan 18 yaş ve üstü 486 birey oluşturmaktadır. Betimleyici bir çalışma olan bu araştırmada çocukluk çağı travması ile mizofoni ve duygu düzenleme güçlüğünün bu ilişkideki etkisini ortaya koymak adına ilişkisel tarama yöntemine uygun şekilde düzenleme yapılmıştır. Çalışmanın modeli ise teorik yapıları test etmek için kullanılan yapısal eşitlik modelidir. Araştırmaya katılan bireylerin seçimi, olasılıksız örnekleme yönteminden olan amaçlı örnekleme yöntemiyle gerçekleştirilmiştir. Çalışmada veri toplama araçları olarak; Demografik Bilgi Formu, Çocukluk Çağı Travmaları Ölçeği, Mizofoni Ölçeği, Duygu Düzenleme Güçlüğü Ölçeği kullanılmıştır. Veriler sosyal medya aracılığıyla Google Forms üzerinden toplanmış, elde edilen veriler değerlendirilmiştir. Yapılan analizlerde cinsiyet değişkeni açısından bakıldığında; katılımcıların Çocukluk Çağı Travması Ölçeğinden almış oldukları puanlar açısından, kadınlar lehine anlamlı bir farklılık bulunmuştur. Benzer şekilde mizofoni açısından yapılan karşılaştırmada da kadınlar lehine anlamlı farklılık bulunmuştur. Profesyonel ruhsal yardım alma açısından bakıldığında; çocukluk çağı travması ve mizofoni açısından profesyonel ruhsal yardım alanlar lehine anlamlı fark bulunmuştur. Yapılan yapısal Eşitlik Modelin analizde, duygu düzenleme güçlüklerinin çocukluk çağı travması ile mizofoni arasındaki ilişkide kısmi aracılık rolü oynadığını bulunmuştur.The aim of this study is to examine the mediating role of emotion regulation difficulties on the relationship between childhood trauma and misophonia. The participants of this study consists of 486 individuals aged 18 and over who are disturbed by specific sounds. This descriptive study is designed in accordance with the relational screening model to reveal the impact of childhood trauma on misophonia and the effect of emotion regulation difficulties on this relationship. The model used in the study is the structural equation model, which is employed to test theoretical constructs. Participants are selected using purposive sampling, a type of non-probability sampling. Data collection tools include the Demographic Information Form, Childhood Trauma Questionnaire, Misophonia Questionnaire, and Difficulties in Emotion Regulation Scale. Data were collected via Google Forms through social media and obtained data is analyzed subsequently. The analysis revealed a significant relationship between Childhood Trauma Questionnaire scores and Misophonia Questionnaire scores. From a gender perspective, there was a higher rate in the Childhood Trauma Questionnaire scores of women participants in comparison to men, indicating that women are more affected by childhood traumas. Similarly, comparisons in terms of misophonia also showed a significant difference in women. In terms of professional psychological support, those who received such support showed significant differences in childhood trauma and misophonia compared to those who did not. The analysis using the Structural Equation Model found that emotion regulation difficulties play a partial mediating role in the relationship between childhood trauma and misophonia

**Решение:** -1 обзор литературы / концептуальная статья

---

### 268 · R0346

**Psychometric Properties of Misophonia Measurement Questionnaires: A Systematic Review.**

2025 · Journal of audiology & otology · article, conference object, journal article · eng · https://doi.org/10.7874/jao.2025.00241

BACKGROUND AND OBJECTIVES: Misophonia is a sound sensitivity disorder characterized by intense emotional and physiological responses to specific triggers. These responses are often associated with heightened reactions from the autonomic nervous system. In this study, we investigated the psychometric properties of the misophonia measurement questionnaires. MATERIALS AND METHODS: A bibliographic search without publication date or language restrictions was conducted in March 2023 and updated in October 2024. The search had no time limit for the retrieval of relevant studies, including cross-sectional and psychometric studies. Two authors screened the titles and abstracts, and irrelevant studies were excluded after reviewing the full text of the articles. Any disagreements during the selection process were resolved through discussion. Standardized critical appraisal tools from the Joanna Briggs Institute and the Consensus-based Standards for the Selection of Health Measurement Instruments (COSMIN) tool were used to assess the psychometric properties of the instruments. RESULTS: Of the 130 screened articles, 34 were selected for full-text evaluation, and 25 articles met the inclusion criteria. CONCLUSION: Evidence regarding the psychometric properties of the measures of misophonia is limited, indicating the need for further research to explore these instruments across various cultures and languages.

**Решение:** -1 обзор / комментарий / письмо

---

### 269 · R1025

**Hyperacusis in Autism Spectrum Disorders.**

2021 · Audiology research · article, conference object, journal article · eng · https://doi.org/10.3390/audiolres11040049

Hyperacusis is highly prevalent in the autism spectrum disorder (ASD) population. This auditory hypersensitivity can trigger pragmatically atypical reactions that may impact social and academic domains. Objective: The aim of this report is to describe the relationship between decreased sound tolerance disorders and the ASD population. Topics covered: The main topics discussed include (1) assessment and prevalence of hyperacusis in ASD; (2) etiology of hyperacusis in ASD; (3) treatment of hyperacusis in ASD. Conclusions: Knowledge of the assessment and treatment of decreased sound tolerance disorders within the ASD population is growing and changing.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 270 · R0333

**Auditory Processing and Neuroregulation in Misophonia: A Comparative Study of Behavioral Measures**

2025 · NeuroRegulation · article, journalarticle · en · https://doi.org/10.15540/nr.12.3.172

Misophonia is a condition of intolerance to certain sounds which act as triggers. This study investigates auditory processing abilities using behavioral measures in normal-hearing individuals with and without misophonia. Thirty participants aged between 18 and 30 years were included. They were divided into two primary groups: 15 individuals diagnosed with misophonia and 15 controls. All of the participants underwent auditory processing tests such as masking level difference (MLD), dichotic consonant-vowel (DCV), and pitch pattern tests (PPT). From the analyzed data, individuals with misophonia showed significantly reduced scores in DCV and PPT. Also, there was no significant difference in the thresholds of MLD at 500 Hz. This study highlights that the reduced scores of DCV and PPT in individuals with misophonia could be attributed to poor auditory cortical processing compared to the control group.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 271 · R1434

**Misophonia**

2015 · İstanbul Beykent Üniversitesi · thesis · tr · https://core.ac.uk/download/667390837.pdf

Ayla alkolik babası ve sevgi dolu annesi ile birlikte yaşayan, seslere karşı uç noktalarda hassasiyetleri olan küçük bir kızdır. Babasının kavgacı karakteri Ayla'nın seslere karşı duyarlılığını arttırıp sosyal hayatını yaşanması zor bir hale sokmaktadır. Yıllar sonra evlendiğinde dahi bu rahatsızlıktan kurtulamamış, ancak bir takım önlemlerle gündelik hayata adapte olmaya çalışmıştır. Lakin yaşam koşullarının zorluğu ve yaşamındaki insanların tutumu onu her şeyi bırakıp sessiz bir ortamda doğada yaşamaya itecektir. Anahtar Kelimeler : Aile içi şiddet, ses, doğaAyla is a little girl who lives together with her alcoholic father and loving mother. She has a strong sensibility towards sounds which exceeds to extreme levels. The agressive character of her father increases her sensitiveness towards sounds and makes it hard for her to live her social life. Even years later, after getting married she still struggles with this disease. However by taking some precautions, she tries to adapt to daily life. However the difficulty of her life conditions and the attitude of the people in her life will push her to leave everything behind and go live in a quiet setting in nature. Key Words : Domestic violence, noise, natur

**Решение:** -1 обзорная публикация / словарный очерк

---

### 272 · R0746

**Sounds, music & healing - Traditional therapies, psychoanalysis, music therapy and biophysical interactions of soundscape and musical sound**

2023

Ce texte constitue une tentative d'état de l'art concernant les effets ressourçants du son, dont la revue de littérature s'étend de l'influence des sons biophoniques, géophoniques et anthropophoniques sur la sphère de perception humaine, jusqu'aux effets thérapeutiques du sonore dans leur dimension à la fois culturelle et médicale, des rituels shamaniques à la musicothérapie et la sonothérapie. Nous y abordons le principe trans-modal de l'enveloppe sonore mobilisé dans le cadre des musicothérapies du spectre autistique, ainsi que d'autres soins de santé alternatifs par le sonore, comme l'ASMR utilisé pour les troubles misophoniques, pour les mettre en perspective avec les hypothèses de la génodique qui évoquent les rapports entre son musical et sciences du vivant. Enfin, nous introduirons la notion d'objet sonore transitionnel, qui, par sa double fonctionalité réminiscente et projective, permet d'ancrer le ressourcement par le sonore dans une perspective de symbolisation du monde.This text constitutes an attempt at the state of the art concerning the restoration effects of sound, whose literature review extends from the influence of biophony, geophony and anthropophony on the sphere of human perception, to the therapeutic effects sound in their cultural and medical dimension, from shamanic rituals to music and sound therapy. We discuss the trans-modal principle of the sound envelope mobilized in the context of autism spectrum music therapies, as well as other alternative sound health care, such as ASMR used for misophonic disorders, for put into perspective with the hypotheses of genodics which evoke the relationship between musical sound and life sciences. Finally, we will introduce the notion of transitional sound object, which, through its reminiscent and projective double functionality, allows to anchor the resourcing by the sound in a perspective of world symbolization

**Решение:** -6 не про мизофонию

---

### 273 · R0198

**Relationship Between Misophonia and Obsessive-Compulsive Disorder: Systematic Review and Meta-Analysis**

2026 · European Psychiatry · abstract, article, journalarticle · eng · https://doi.org/10.1192/j.eurpsy.2026.11075

Introduction Misophonia is a condition characterized by disproportionate emotional, behavioral, and physiological reactions to specific auditory and/or visual stimuli perceived as harmless by most people. Although not yet included in international diagnostic systems, misophonia has gained growing clinical and scientific interest. Its nosological ambiguity has hindered the understanding of associated psychiatric comorbidities. Among these, obsessive-compulsive disorder (OCD) is most frequently reported. The two conditions share features such as intrusive thoughts, heightened attention to specific stimuli, and avoidance behaviors. However, most individuals with misophonia do not meet full diagnostic criteria for OCD, suggesting that misophonia may represent a distinct yet partially overlapping psychopathological entity. This study systematically reviews and quantitatively analyzes the relationship between misophonia and OCD. Objectives To examine the co-occurrence and association between misophonia and OCD through a systematic review and meta-analysis, estimating both the pooled prevalence of OCD in misophonia and the correlation between the two conditions. Methods A systematic search of Web of Science and PsycINFO (January 2025) identified studies including individuals with misophonia and a comorbid psychiatric disorder diagnosed via clinical interview or validated scales. Of 464 screened records, 17 met inclusion criteria (total N = 1 193) (Image 1). Two random-effects meta-analyses were conducted: a prevalence analysis (k = 12) and a correlational analysis (k = 6). Heterogeneity (I2) and publication bias were assessed following PRISMA guidelines. Results The prevalence meta-analysis (k = 12) showed an aggregated OCD prevalence of 9.2 % (95 % CI 4.7–17.4) in misophonia samples, with substantial heterogeneity. The correlational meta-analysis (k = 6) revealed a moderate positive correlation (μ = 0.389, 95 % CI 0.290–0.487, p < .001; I2 = 64.9 %), consistent with a reliable association across studies. The 95 % prediction interval (0.184–0.594) indicates that this link is expected in future research. No publication bias was detected, supporting the robustness of results (Images 2-3). Image 1: Image 1: Long description.A P R I S M A flowchart illustrating the systematic review process from identification to inclusion for a meta-analysis on O C D. See long description. Image 2: Image 2: Long description.A forest plot showing O C D prevalence in misophonia patients across twelve studies from 2013 to 2024. See long description. Image 3: Image 3: Long description.A forest plot showing the correlation between Misophonia and O C D across six studies and a summary R E Model. See long description. Conclusions Current evidence supports a significant, though variable, association between misophonia and OCD, with an average correlation of moderate strength. These results reinforce the hypothesis of shared psychopathological mechanisms, possibly involving cognitive-perceptual rigidity and emotional hyper-reactivity. Clinically, obsessive-compulsive symptoms may worsen misophonia and its impact on daily life. Nevertheless, misophonia presents a unique symptom profile, suggesting it constitutes an independent though related disorder. Further studies with standardized diagnostic criteria and larger samples are needed to refine its classification and guide targeted interventions. Disclosure of Interest None Declared

**Решение:** -1 обзор / комментарий / письмо

---

### 274 · R1304

**Introduction to the Special Issue: Complexities and New Developments in Adolescent Obsessive-Compulsive Related Disorders**

2018 · Clinical Case Studies · editorial · en · https://doi.org/10.1177/1534650118782649

As readers of this special issue will see, the treatments provided in the Obsessive-Compulsive Related Disorder (OCRD) cases described are highly varied. The unifying feature would be better described as an age group rather than a breakdown in inhibitory control as speculated to be the primary unifying mechanism in the OCRD. It is encouraging that effective treatments are emerging for adolescents with OCRDs. Providers will do well to recognize that the appearance of the OCRD does not imply that a treatment for one disorder (i.e., exposure with response prevention [ERP] for OCD) will necessarily also provide relief for another condition in this class (i.e., for Trichotillomania [TM] or Hoarding Disorder [HD]). Instead, given the heterogeneity of these disorders, it comes as little surprise that the interventions are also varied, and providers will require training in a wide range of interventions embedded in sound clinical conceptualization (i.e., Tolin, 2016). It is hoped that these cases will spark additional research on clinical presentations of adolescents with OCRDs.

**Решение:** -6 не про мизофонию

---

### 275 · R0593

**An experimental examination of neurostimulation and cognitive restructuring as potential components for Misophonia interventions.**

2024 · Journal of affective disorders · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jad.2024.01.120

Misophonia is a disorder of decreased tolerance to certain aversive, repetitive common sounds, or to stimuli associated with these sounds. Two matched groups of adults (29 participants with misophonia and 30 clinical controls with high emotion dysregulation) received inhibitory neurostimulation (1 Hz) over a personalized medial prefrontal cortex (mPFC) target functionally connected to the left insula; excitatory neurostimulation (10 Hz) over a personalized dorsolateral PFC (dlPFC) target; and sham stimulation over either target. Stimulations were applied while participants were either listening or cognitively downregulating emotions associated with personalized aversive, misophonic, or neutral sounds. Subjective units of distress (SUDS) and psychophysiological measurements (e.g., skin conductance response [SCR] and level [SCL]) were collected. Compared to controls, participants with misophonia reported higher distress (∆SUDS = 1.91-1.93, ps < 0.001) when listening to and when downregulating misophonic distress. Both types of neurostimulation reduced distress significantly more than sham, with excitatory rTMS providing the most benefit (Cohen's dSUDS = 0.53; dSCL = 0.14). Excitatory rTMS also enhanced the regulation of emotions associated with misophonic sounds in both groups when measured by SUDS (dcontrol = 1.28; dMisophonia = 0.94), and in the misophonia group alone when measured with SCL (d = 0.20). Both types of neurostimulation were well tolerated. Engaging in cognitive restructuring enhanced with high-frequency neurostimulation led to the lowest misophonic distress, highlighting the best path forward for misophonia interventions.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 276 · R0510

**Facial emotion recognition and disgust tendency in patients diagnosed with misophonia: a preliminary study**

2024 · Neuroscience Applied · article, journalarticle · en · https://doi.org/10.1016/j.nsa.2024.104893

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (распознавание лицевых эмоций при мизофонии)

---

### 277 · R0713

**Peer Review Report For: Novel five-phase model for understanding the nature of misophonia, a conditioned aversive reflex disorder [version 1; peer review: 1 approved with reservations]**

2023 · F1000 Research Ltd · other literature type, review, peer-review · en · https://doi.org/10.5256/f1000research.146501.r186207

Background: Misophonia is a recently identified condition in which a person perceives a subtle stimulus (e.g., eating sounds, hair twirling) and has an intense, negative emotional response. Misophonia cannot be classified with established nosological systems. Methods: We present a novel five-phase model of misophonia from a cognitive-behavioral framework. This model identifies a learned reflex of the autonomic nervous system as the primary etiology and maintenance of misophonia. Phase one is anticipatory anxiety and avoidance. Phase two is a conditioned physical reflex (for example, the tensing of calf muscles) that develops through stimulus-response Pavlovian conditioning. Phase three includes intense negative emotional responses and accompanying physiological distress, thoughts, urges, and emotion-driven behavior. Phase four is the individual’s coping responses to emotional distress, and phase five is the environmental response and resulting internal and external consequences of the coping behaviors. Each phase helps explain the maintenance of the response and the individual’s impairment. Results: Anticipatory anxiety and avoidance of phase one contributes to an increased arousal and awareness of triggers, resulting in increased severity of the trigger experience. Both the Pavlovian-conditioned physical reflex of phase two and the emotion-driven behavior caused by the conditioned emotional response of phase three increase with in vivo exposure to triggers. Phase four includes internal and external coping behaviors to the intense emotions and distress, and phase 5 includes the consequences of those behaviors. Internal consequences include beliefs and new emotions based on environmental responses to anger and panic. For example, the development of emotions such as shame and guilt, and beliefs regarding how ‘intolerable’ the trigger is. Conclusions: We assert misophonia is a multi-sensory condition and includes anticipatory anxiety, conditioned physical reflexes, intense emotional and physical distress, subsequent internal and external responses, and environmental consequences.

**Решение:** -7 peer review report / decision letter

---

### 278 · R0373

**Investigating Neurophysiological, Perceptual, and Cognitive Mechanisms in Misophonia.**

2025 · Biology · article, journal article, journalarticle · eng · https://doi.org/10.3390/biology14030238

Misophonia is a condition characterized by intense, involuntary distress or anger in response to specific sounds, often leading to irritation or aggression. While the condition is recognized for its emotional and behavioral impacts, little is known about its physiological and perceptual effects. The current study aimed to explore the physiological correlates and perceptual consequences of misophonia through a combination of electrophysiological, perceptual, and cognitive assessments. Seventeen individuals with misophonia and sixteen control participants without the condition were compared. Participants completed a comprehensive battery of tests, including (a) cortical event-related potentials (ERPs) to assess neural responses to standard and deviant auditory stimuli, (b) the spatial release from the speech-on-speech masking (SRM) paradigm to evaluate speech segregation in background noise, and (c) the flanker task to measure selective attention and cognitive control. The results revealed that individuals with misophonia exhibited significantly smaller mean peak amplitudes of the N1 and N2 components in response to oddball tones compared to controls. This suggests a potential underlying neurobiological deficit in misophonia patients, as these components are associated with early auditory processing. However, no significant differences between each group were observed in the P1 and P2 components regarding oddball tones or in any ERP components in response to standard tones. Despite these altered neural responses, the misophonia group did not show differences in hearing thresholds, speech perception abilities, or cognitive function compared to the controls. These findings suggest that while misophonia may involve distinct neurophysiological changes, particularly in early auditory processing, it does not necessarily lead to perceptual deficits in speech perception or cognitive function.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 279 · R0683

**Understanding misophonia from an audiological perspective: a systematic review.**

2023 · European archives of oto-rhino-laryngology : official journal of the European Federation of Oto-Rhino-Laryngological Societies (EUFOS) : affiliated with the German Society for Oto-Rhino-Laryngology - Head and Neck Surgery · article, review, journalarticle · eng · https://doi.org/10.1007/s00405-022-07774-0

Purpose Misophonia is a neurophysiological disorder in which certain sounds trigger an intensely emotional or physiological response caused by an increased autonomic nervous system reaction to the triggers. Misophonia is a relatively new condition, and the neurophysiological mechanism behind this condition is not known yet. The assessment and management of misophonia need a team approach. Audiologists are vital members of the team. However, their roles in this condition are not well-understood. The study aims to review the neurophysiological mechanism of misophonia, highlighting the mechanism involved in the audiological pathway and directing the discussion toward applications of findings in the assessment and management of misophonia from the audiological perspective. Methods We reviewed 12 articles from different databases to understand the neurophysiological mechanisms of misophonia. Most of the studies selected were experimental designs involving individuals with misophonia. Results The result of the review revealed abnormal activation and connection among the different higher cortical structures in participants with misophonia. By signifying various neurophysiological and neuroradiological findings, the review confirms that misophonia is a neurophysiological disorder that may border between audiology, neurology, and psychiatry. Assessment of study quality reported an overall low risk of bias. Conclusions This review highlights the need to include an audiologist as a team member in the evaluation and management of misophonia.

**Решение:** -1 обзор / комментарий / письмо

---

### 280 · R0110

**Factors Associated With Misophonia: A Systematic Review.**

2026 · Revista Colombiana de psiquiatria · article, journal article, systematic review · eng;spa · https://doi.org/10.1016/j.rcpeng.2026.06.001

Introduction Misophonia, known as hypersensitivity to certain sounds, has a significant impact on psychological well-being. Studies in the literature focus on triggers, responses to triggers, neural mechanisms, and quality of life. Risk factors should be understood to guide the prevention, diagnosis, and treatment of misophonia. This systematic review aims to explore the available evidence identifying factors associated with misophonia in the general or clinical population. Material and methods This study was a systematic review protocol. PubMed, Scopus, Web of Science, Taylor & Francis, and Science Direct electronic databases were searched using the keywords. In the study with no year restriction, factors associated with misophonia were the primary outcomes. Joanna Briggs Institute critical analysis tools were used to assess the methodological quality of the studies. Results In electronic databases, 1206 records were identified, of which 19 were included. In studies the Misophonia Questionnaire (MQ) was frequently used to assess symptoms of misophonia. Methodological quality assessments of the studies ranged from 62.5% to 100%. Conclusions Most of the factors associated with misophonia were mental disorders and sociodemographic factors. The presence of mental disorders and female gender were frequently associated with misophonia.

**Решение:** -1 обзор / комментарий / письмо

---

### 281 · R0933

**Designing a Deep Learning Hybrid Using CNN and Inception V3 Transfer Learning to Detect the Aggression Level of Deep Obsessive Compulsive Disorder in Children**

2022 · International Journal of Biology and Biomedical Engineering · article · en · https://doi.org/10.46300/91011.2022.16.27

The usage of Artificial intelligence in medical arena has proved to be a game changer in the detection and diagnosis of several medical conditions. In the current digital era, children with stressful medical issues are suffering from Deep Obsessive-Compulsive Disorder (DOCD). This kind of mental stress occurs in children because of the continuous usage of gadgets such as mobile phone, playing games using play stations, watching videos on tablets, etc. In most of the possibilities, single children are the ones affected with several obsessions such as stubborn activities, fighting for selfish priorities and so on. In medical terms, these kinds of complex behavioral changes are identified as DOCD. Genetic behaviors sometimes in a few group of children are also noticed as a modality difference. As symptoms are psychiatric impairment, such a child remains isolated, abnormal silence, being obsessive and repeating irrelevant words, high stress or anxiety. All medical challenges could be treated as healthcare research metrics and the gradual increase in DOCD disorder among children of this generation can be considered too. Early detection of DOCD is essential as it can help in early diagnosis but techniques to do so is unavailable currently. Deep learning-an artificial intelligence method can be utilized to detect DOCD, diagnose and treat it and bring about a positive character in children. Behavior changes in children can be classified and detected using transfer learning algorithms. In COVID-19 pandemic situation, 3% of DOCD has increased to 10-15% as a disorder. This information is retrieved from children by monitoring negative activities, unusual behavior such as nail biting, removing spectacles and placing them in the wrong place, watching tablets, mobile phones and television for more hours. Using Convolutional Neural Networks (CNN), input such as MRI (Magnetic resonance Imaging) is used for experimenting the variations in behavior with the high dimension that are analyzed from the image dataset. Using Transfer Learning with Inception V3-, CNN generalization of misophonia level can be statistically analyzed to avoid overfitting problems. By employing AI techniques, the aggression level can be predicted using data augmentation method with better accuracy and a low error rate than the existing systems. In the research it is observed that using the model employing Inception-V3 transfer learning CNN a better prediction of aggression levels can be achieved in comparison to the existing CNN model used.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 282 · R0129

**Hyperacusis**

2026 · StatPearls · study guide · eng · https://pubmed.ncbi.nlm.nih.gov/32491645/

Hyperacusis is a rare disorder of loudness perception in which sounds that are typically considered harmless become intolerable. The Hyperacusis Network uses the description "decreased sound tolerance." Patients may experience innocuous sounds as painful, frightening, unpleasant, or excessively loud. Hyperacusis frequently co-occurs with tinnitus and can induce considerable distress; patients consistently report impairments in their social, occupational, and recreational activities. Avoiding sound sources and seeking medical attention are common behaviors. Hyperacusis is a distinct diagnosis from phonophobia and misophonia. A fear-based aversion to sound characterizes phonophobia, whereas misophonia involves intense negative emotions, such as anger or disgust, in response to specific trigger sounds, in contrast to the generalized loudness intolerance that defines hyperacusis. Hyperacusis is a symptom that includes an emotional and psychological component, as patients may experience apprehension about sound exposure and engage in avoidance behaviors, in addition to a physiological component involving changes in the central auditory system, such as increased gain. Hyperacusis can have a marked adverse impact on quality of life. Although a definitive cure has not yet been found, research in this area is progressing rapidly, and the number of peer-reviewed studies on the condition has increased 10-fold over the past 40 years.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 283 · R0743

**AURAL DIVERSITY NOISE CONTROL AND A SUSTAINABLE FUTURE**

2023 · International Congress and Exposition on Noise Control Engineering (INTER-NOISE) · article, conference-paper · eng · https://doi.org/10.25144/14517

The unquestioned assumption of a "normal" pair of standard healthy ears underpins most sound-related disciplines, from acoustics to engineering, from music to sound studies, from medicine to hearing science. Yet, the reality is that everybody hears differently. Our ears are uniquely shaped. We all experience temporary changes in hearing, such as during a cold. Everybody goes through presbyacusis (age-related hearing loss) at varying rates after the teenage years. More specific aural divergences are the result of an array of hearing differences or impairments which affect roughly one sixth of the world's population (Lancet, 2013). These include noise-related, genetic, ototoxic, traumatic, and disorder-based hearing loss, some of which may cause full or partial deafness. Moreover, "loss" is not the only form of difference: auditory perceptual disorders such as tinnitus, hyperacusis and misophonia involve an increased sensitivity to sound. This paper presents findings from the AHRC-funded Aural Diversity Network, which explores the consequences of these differences for noise-related engineering and many other fields. How may we ensure a sustainable future that acknowledges aural diversity?

**Решение:** -1 обзор литературы / концептуальная статья

---

### 284 · R0897

**Misophonia: A Systematic Review of Current and Future Trends in This Emerging Clinical Field.**

2022 · International journal of environmental research and public health · article, conference object, journal article · eng · https://doi.org/10.3390/ijerph19116790

Misophonia is a scarcely known disorder. This systematic review (1) offers a quantitative and qualitative analysis of the literature since 2001, (2) identifies the most relevant aspects but also controversies, (3) identifies the theoretical and methodological approaches, and (4) highlights the outstanding advances until May 2022 as well as aspects that remain unknown and deserve future research efforts. Misophonia is characterized by strong physiological, emotional, and behavioral reactions to auditory, visual, and/or kinesthetic stimuli of different nature regardless of their physical characteristics. These misophonic responses include anger, general discomfort, disgust, anxiety, and avoidance and escape behaviors, and decrease the quality of life of the people with the disorder and their relatives. There is no consensus on the diagnostic criteria yet. High comorbidity between misophonia and other psychiatric and auditory disorders is reported. Importantly, the confusion with other disorders contributes to its underdiagnosis. In recent years, assessment systems with good psychometric properties have increased considerably, as have treatment proposals. Although misophonia is not yet included in international classification systems, it is an emerging field of growing scientific and clinical interest.

**Решение:** -1 обзор / комментарий / письмо

---

### 285 · R0447

**Misophonia: A Scientific Review on Etiology, Pathophysiology, and Therapeutic Approaches**

2025 · International Journal of Pharmaceutical Sciences · article, journalarticle/ · und · https://doi.org/10.5281/zenodo.14704629

Misophonia, characterized by intense emotional and physiological responses to specific sounds, represents a complex neurophysiological and behavioral syndrome first identified in 1997. This review synthesizes current understanding of its epidemiology, etiology, pathophysiology, and clinical implications. Population studies indicate prevalence rates of 15-20% in the general population, with 2-3% reporting severe cases, and higher rates among university students (20-25%) and clinical populations (up to 60%). The condition shows female predominance (3:2 ratio) with typical onset between ages 8-12. Neuroimaging studies reveal altered activity in the anterior cingulate cortex, anterior insular cortex, and superior temporal cortex, suggesting disrupted sensory-emotional integration. Multiple factors contribute to its etiology, including neurobiological, genetic, developmental, environmental, and psychological mechanisms. Common triggers include eating sounds, breathing, and repetitive movements, leading to intense autonomic arousal, anxiety, and aggressive impulses. The condition frequently co-occurs with obsessive-compulsive disorder, post-traumatic stress disorder, depression, and anxiety disorders. While standardized diagnostic criteria are lacking, several assessment tools exist, including the Misophonia Assessment Questionnaire and Amsterdam Misophonia Scale. Treatment approaches encompass both non-pharmacological interventions (music therapy, sound management) and pharmacological options (MDMA, β-blockers). The condition significantly impacts daily functioning, often leading to social isolation, academic difficulties, and reduced quality of life. Future research priorities include establishing standardized diagnostic criteria, developing validated treatment protocols, understanding neurobiological mechanisms, and conducting long-term outcome studies.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 286 · R0341

**Auditory brainstem response and cortical auditory evoked potentials in patients with misophonia**

2025 · The Egyptian Journal of Otolaryngology · article, collection/collection, journalarticle · en · https://doi.org/10.1186/s43163-025-00947-8

Abstract Background Misophonia, also known as selective sound sensitivity syndrome, is a persistent condition characterized by adverse emotional reactions and autonomic arousal triggered by particular sounds. The purpose of this study is to investigate the auditory pathway processing in persons with misophonia using click auditory brainstem response (ABR) and cortical auditory evoked potentials (CAEPs). This study included 20 healthy controls and 20 patients with misophonia diagnosed according to the misophonia diagnostic criteria of Schroder et al. (2013). All subjects were subjected to a full audiological evaluation including pure tone audiometry (PTA) with detection of uncomfortable loudness level (UCLL) and most comfortable loudness level (MCLL), immitancemetry, cortical auditory evoked potentials (CAEPs) and auditory brainstem response (ABR). Results Both UCLL and MCLL were higher in patients with misophonia than the healthy controls and CAEPs results had earlier P1 and N1 waves and larger P1 and P2 amplitudes in frequencies 500, 1000, 2000, and 4000 Hz in the misophonia group. Conclusion Misophonia patients have significant findings in CAEPs waves’ amplitudes and latencies together with MCLL and UCLL.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 287 · R1440

**What is misophonia and how can we treat it?**

2014 · Expert review of neurotherapeutics · article, other literature type, editorial · eng · https://doi.org/10.1586/14737175.2014.892418

Selective sound sensitivity syndrome or misophonia is a chronic condition characterized by unpleasant emotional experiences and autonomic arousal in response to specific sounds. Over the last few years there have been a few reports detailing the clinical features associated with this condition. These focused reports raise interesting questions about the nosological status of this potentially disabling clinical entity. </p

**Решение:** -1 редакционная статья / письмо

---

### 288 · R1330

**Cognitive behavioral therapy for selective sound sensitivity syndrome (misophonia): A report of three cases**

2017 · article, conference object, conference paper · eng · https://avesis.gazi.edu.tr/publication/details/575a9c30-ece5-4861-ad52-583ec024696e/oai

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 клинический случай / серия случаев

---

### 289 · R0611

**How auditory processing influences the autistic profile: A review.**

2024 · Autism research : official journal of the International Society for Autism Research · article, conference object, journal article · eng · https://doi.org/10.1002/aur.3259

Abstract We need to combine sensory data from various sources to make sense of the world around us. This sensory data helps us understand our surroundings, influencing our experiences and interactions within our everyday environments. Recent interest in sensory‐focused approaches to supporting autistic people has fixed on auditory processing—the sense of hearing and the act of listening—and its crucial role in language, communications, and social domains, as well as non‐social autism‐specific attributes, to understand better how sensory processing might differ in autistic people. In this narrative review, we synthesize published research into auditory processing in autistic people and the relationship between auditory processing and autistic attributes in a contextually novel way. The purpose is to understand the relationship between these domains more fully, drawing on evidence gleaned from experiential perspectives through to neurological investigations. We also examine the relationship between auditory processing and diagnosable auditory conditions, such as hyperacusis, misophonia, phonophobia, and intolerance to loud sounds, as well as its relation to sleep, anxiety, and sensory overload. Through reviewing experiential, behavioral and neurological literature, we demonstrate that auditory processes interact with and shape the broader autistic profile—something not previously considered. Through a better understanding of the potential impact of auditory experiences, our review aims to inform future research on investigating the relationship between auditory processing and autistic traits through quantitative measures or using qualitative experiential inquiry to examine this relationship more holistically.

**Решение:** -1 обзор литературы / концептуальная статья

---

### 290 · R0320

**A Case Report on Early-Onset Misophonia in a Bangladeshi Pediatric Patient.**

2025 · Cureus · article, case reports, journal article · eng · https://doi.org/10.7759/cureus.86245

This case report describes a nine-year-old Bangladeshi boy with misophonia symptoms beginning at three years old, an underreported condition in children. He exhibited strong emotional reactions to specific sounds made by his mother, such as yawning and breathing, which later extended to visual triggers, including her nose-scratching. He attempted to stop these triggers through physical actions. Autism was ruled out. A brief trial of sertraline, risperidone, and behavioral therapy showed minimal benefit and was discontinued. In the fifth year, compulsive hand-washing emerged. Family history revealed parental OCD. On reevaluation, he was diagnosed with misophonia and emerging OCD. Treatment included selective serotonin reuptake inhibitors, cognitive behavioral therapy with exposure and response prevention, relaxation techniques, and follow-up. This case underscores the potential for early-onset misophonia with auditory and visual triggers, its overlap with OCD, and the need for early diagnosis, attention to comorbidities, and individualized, ongoing care.

**Решение:** -2 клинический случай / серия случаев

---

### 291 · R1065

**From Cathartic ‘Brain Tingles’ to Scratching Chalkboard Sensations**

2021 · Reinvention an International Journal of Undergraduate Research · article · en · https://doi.org/10.31273/reinvention.v14i2.743

ASMR is a sensory-perceptual experience in which specific audio-visual or haptic stimuli reliably trigger electro-static-like ‘brain tingles’ extending peripherally from the back of the scalp. While generally an under-studied phenomenon, research is beginning to identify potential therapeutic benefits of immersing in ASMR-content, supported by anecdotal accounts from active online communities. The present mixed-methods online study aimed to explore the phenomenological aspects of ASMR and its potential therapeutic effects. A total of 224 participants watched ASMR-videos and completed scales measuring ASMR response and affect. Participants then completed four open-ended questions about their ASMR experience and use. In line with our hypotheses, quantitative results suggested that participants who experienced ASMR demonstrated significantly higher positive affect and significantly lower negative affect compared to those who did not (or were unsure about whether they did) experience ASMR. The pleasurability and intensity of ASMR also positively correlated with measures of positive affect, and negatively with measures of negative affect. Thematic analysis identified great phenomenological variability in perceived pleasurability and intensity of ASMR experience among individuals as a super-theme present across themes (Psychological, Physical and Social dimensions). Based on these findings, a multi-dimensional model for characterising ASMR is proposed, providing clear opportunities for future research.

**Решение:** -6 не про мизофонию

---

### 292 · R1406

**Putting Research into Practice for Autism Spectrum Disorder**

2015 · The Hearing Journal · article · en · https://doi.org/10.1097/01.hj.0000459743.01876.fd

Figure: © Shutterstock/PathDocAs an audiologist, what is the first thing that comes to your mind when you hear the word autism? I bet that you are imagining a child covering his or her ears in the presence of noise. Many of us have seen patients with autism spectrum disorder (ASD) in our practices.Figure: Ali A. Danesh, PhDIn addition to hypersensitivity to sound, which some may refer to as hyperacusis, auditory symptoms in the ASD population include tinnitus, inattentiveness to verbal stimuli, selective auditory attention, and atypical performance of the central auditory system.Figure: Wafaa Kaf, MD, PhDA recent epidemiological study from Gallaudet Research Institute revealed that one in 59 children with hearing loss were also receiving services for autism—a much higher prevalence than the one in 110 normal hearing children reported to have ASD (J Autism Dev Disord 2012;42[10]:2027-2037http://link.springer.com/article/10.1007/s10803-012-1452-9). Several other studies have also demonstrated commonalities between people with hearing loss or deafness and those with autism spectrum disorders (Am Ann Deaf 2009;154[1]:5-14http://muse.jhu.edu/login?auth=0&type=summary&url=/journals/american_annals_of_the_deaf/v154/154.1.vernon.html; Dev Med Child Neurol 2006;48[2]:85-89http://onlinelibrary.wiley.com/doi/10.1017/S001216220600020X/full; Child Dev 2005;76[2]:502-517http://onlinelibrary.wiley.com/doi/10.1111/j.1467-8624.2005.00859.x/abstract). For example, in a study of 199 children and adolescents with autism, 7.9 percent had mild to moderate hearing impairment, and 3.5 percent had pronounced to profound bilateral hearing loss or deafness (J Autism Dev Disord 1999;29[5]:349-357http://link.springer.com/article/10.1023/A%3A1023022709710). Recent research investigating the neuroanatomical diversity and auditory symptoms of autism spectrum disorder holds lessons for the management of patients with ASD in the hearing healthcare clinic. NEUROANATOMICAL DIVERSITY From a neuroscientific point of view, we can describe autism as a neurodevelopmental disorder with atypical neural connectivity. Rich evidence from the scientific literature and imaging studies suggests differences in brain structures in people with ASD. These differences are in a variety of areas of the brain, and auditory centers are no exceptions. As audiologists, we are familiar with the role of the superior olivary complex in the process of sound localization. Studies have shown malformation of this lower brainstem area in ASD populations (Brain Res 2011;1398:102-112http://www.sciencedirect.com/science/article/pii/S0006899311008730; Brain Res 2011;1367:360-371http://www.sciencedirect.com/science/article/pii/S0006899310022225). In a study of sound localization abilities, there were no differences in horizontal localization between adults who had ASD and a control group; however, vertical localization was significantly impaired in the ASD group ( J Psychiatry Neurosci 2013;38[6]:398-406http://jpn.ca/vol38-issue6/38-6-398/). This finding confirms that the ASD population has neuroanatomical changes in the auditory brainstem. Neuroimaging studies have revealed differences in the brain structures and neurochemistry of people with ASD. For example, voxelwise comparisons have shown increased gray matter volume in the anterior temporal and dorsolateral prefrontal regions in the ASD population ( Arch Gen Psychiatry 2012;69[2]:195-209http://archpsyc.jamanetwork.com/article.aspx?articleid=1107445). Advancements in neuroimaging technology and the employment of methods beyond MRI and fMRI, such as diffusion tensor imaging (DTI) and magnetic resonance spectroscopy (MRS), have contributed significantly to the study and analysis of neural diversity in people with ASD.Figure: © Shutterstock/LightspringNeuroimaging studies using these methods have shown differences in a range of brain structures, such as the arcuate fasciculus ( NeuroImage 2010;51[3]:1117-1125http://www.sciencedirect.com/science/article/pii/S1053811910001059), corpus callosum ( NeuroImage 2007;34[1]:61-73http://www.sciencedirect.com/science/article/pii/S1053811906008901), and other auditory- and language-related brain structures that may be behind the difficulties processing emotion in others’ voices that's experienced by people with ASD ( Proc Nat Acad Sci U S A 2013;110[29]:12060-12065http://www.pnas.org/content/110/29/12060.full). In addition, an MRI study looking at the size of the planum temporale and Heschl's gyrus in children with ASD and typical children indicated larger left planum temporale volume compared with the right in control subjects, but not in children with ASD, and no significant difference in the size of the Heschl's gyrus between the two groups ( J Autism Dev Disord 2005;35[4]:479-486http://link.springer.com/article/10.1007/s10803-005-5038-7). The brain's structural diversity has also been investigated in syndromic forms of ASD, like XYY syndrome. In that condition, increased brain matter volume has been reported, which may contribute to the higher frequency of ASD in this population ( Dev Med Child Neurol 2012;54[12]:1149-1156http://onlinelibrary.wiley.com/doi/10.1111/j.1469-8749.2012.04418.x/full). In people who have ASD and tuberous sclerosis complex, a genetic disorder resulting in the growth of nonmalignant tumors in the brain and other vital organs, the function of the arcuate fasciculus was diminished, resulting in poor language skills ( Cereb Cortex 2013;23[7]:1526-1532http://cercor.oxfordjournals.org/content/23/7/1526.full). MAJOR AUDITORY SYMPTOMS A few questionnaires are available for the monitoring and assessment of sound hypersensitivity and hyperacusis in the ASD population, such as the Hyperacusis Questionnaire ( ORL J Otorhinolaryngol Relat Spec 2002;64[6]:436-442http://www.karger.com/Article/FullText/67570) and the recently validated Auditory Behavior Questionnaire ( J Autism Dev Disord 2013;43[4]:978-984http://link.springer.com/article/10.1007/s10803-012-1626-5). Previous studies have shown an 18-percent prevalence of hyperacusis in people with autism ( J Autism Dev Disord 1999;29[5]:349-357http://link.springer.com/article/10.1023/A%3A1023022709710). In our lab, we investigated self-reported hyperacusis and tinnitus in people with Asperger syndrome. Of 55 participants in the study, 38 (69%) reported hyperacusis, and 19 (35%) reported tinnitus (manuscript in preparation). Another recent study evaluated the relationship between hypersensitivity to sound and superior semicircular canal dehiscence ( Eur Arch Otorhinolaryngol 2013;270[8]:2353-2358http://link.springer.com/article/10.1007/s00405-013-2482-4). It found that 29 percent of people with ASD who showed hypersensitivity to sound had superior semicircular canal dehiscence, as revealed by CT studies. As conductive hearing loss is a common finding in children with autism, routine tympanometry and otoacoustic emission (OAE) evaluations should be considered. Among 100 young people with autism in a recent study, abnormal tympanometric patterns (i.e., types B and C2) and absent OAEs at lower frequencies were significantly more common than in age-matched controls ( Eur J Pediatr 2013;172[8]:1007-1010http://link.springer.com/article/10.1007/s00431-013-1980-0). Behavioral evaluations are less reliable in children with autism relative to typically developing children, data have suggested. For example, in a study of 22 children with autism and 22 age-matched, typically developing children evaluated for hearing, electrophysiological and physiological measures such as auditory brainstem response (ABR) and distortion product otoacoustic emissions (DPOAEs) showed similar results across both groups; however, behavioral thresholds were worse in the autistic group ( Ear Hear 2006;27[4]:430-441http://journals.lww.com/ear-hearing/Fulltext/2006/08000/Auditory_Characteristics_of_Children_with_Autism.11.aspx). These findings emphasize the importance of including electrophysiological evaluation in the hearing test battery of this vulnerable population. DPOAEs and transient-evoked otoacoustic emissions (TEOAEs) have shown mixed results (e.g., Ear Hear 2006;27[3]:299-312http://journals.lww.com/ear-hearing/Fulltext/2006/06000/Peripheral_Audition_of_Children_on_the_Autistic.9.aspx; Autism 2007;11[1]:73-79http://aut.sagepub.com/content/11/1/73.abstract), with several researchers finding no differences between groups with and without autism, and others showing potential differences. However, all these studies concluded that such physiological measures are very important to the study of the integrity of the auditory system in autism. Research from our laboratory evaluated DPOAE amplitudes in children with autism and a control group, showing reduced DPOAEs in the former group ( Int J Audiol 2012;51[4]:345-352http://informahealthcare.com/doi/abs/10.3109/14992027.2011.626202). When contralateral suppression was employed, the effect of contralateral noise was not as strong in children with autism as it was in the control group. These findings of a possible combined effect of recruitment and lack of auditory filter—because of early cochlear dysfunction and efferent system dysfunction, respectively—may explain why children with autism have hypersensitivity to sound. Interestingly, a similar study in our laboratory detected no significant differences in DPOAE amplitudes or contralateral suppression between 18 boys with Asperger syndrome and an age-matched control group ( Int J Pediatr Otorhinolaryngol 2013;77[6]:947-954http://www.sciencedirect.com/science/article/pii/S0165587613001146). Auditory electrophysiological event-related potentials (ERPs) and their magnetic counterparts also have been extensively employed in the study of autism. A 2011 study showed significantly delayed magnetic mismatch negativity field responses in ASD participants, particularly those with language impairment, leading the authors to speculate that these findings can be used as biomarkers for language impairment and autism ( Biol Psychiatry 2011;70[3]:263-269http://www.biologicalpsychiatryjournal.com/article/S0006-3223(11)00063-1/abstract). In terms of balance abnormalities, posturographic evaluation of people with ASD has shown a larger sway on the platform compared with control subjects ( J Autism Dev Disord 2003;33[6]:643-652http://link.springer.com/article/10.1023/B%3AJADD.0000006001.00667.4c). AUDITORY MANAGEMENT Management of auditory complications in the ASD population is multidimensional, addressing hearing loss, auditory processing, hypersensitivity to sound, and tinnitus. Results from studies looking at the effects of cochlear implants on profoundly deaf children with autism are promising, demonstrating significant improvements in auditory communication following implantation ( Arch Otolaryngol Head Neck Surg 2004;130[5]:666-671http://archotol.jamanetwork.com/article.aspx?articleid=647549). FM systems have been shown to be very effective as well, particularly for the enhancement of speech perception in noise ( J Pediatr 2014;164[2]:352-357http://www.jpeds.com/article/S0022-3476(13)01212-2/abstract; J Commun Disord 2013;46[1]:30-52http://www.sciencedirect.com/science/article/pii/S0021992412001165). In ASD, differences in audiovisual integration for speech processing, such as altered neural networks ( Autism Res 2012;5[1]:39-48http://onlinelibrary.wiley.com/doi/10.1002/aur.231/full), may have implications for rehabilitation and auditory training. The effects of auditory training and rehabilitative techniques, such as Fast ForWord, have been documented through the use of pre- and post-therapy electrophysiological recordings. Children with autism spectrum disorder had training-related changes in multiple dimensions, such as brainstem and cortical response timing, and pitch-tracking ( Behav Brain Funct 2010;6:60http://www.behavioralandbrainfunctions.com/content/6/1/60). Techniques such as neurofeedback, which enables self-regulation of brain oscillations, also have led to improvements in cognitive functioning for children with autism ( Appl Psychophysiol Biofeedback 2013;38[1]:17-28http://link.springer.com/article/10.1007/s10484-012-9204-3). There is evidence that the neural network of the auditory pathways reconfigures during neurofeedback ( NeuroImage 2013;81:243-252http://www.sciencedirect.com/science/article/pii/S1053811913005132), making this approach potentially useful for people with ASD and auditory processing disorders. Hearing aid fitting protocols and verification practices are pretty similar in ASD and non-ASD populations ( Am J Audiol 2001;10[1]:32-40http://aja.pubs.asha.org/Article.aspx?articleid=1773863), and management strategies for tinnitus and hyperacusis are also comparable across the two groups. Techniques such as sound therapy with custom-made sound tracks or ear-level sound generators combined with habituation therapy and counseling have been promising for tinnitus management. The issue of sound sensitivity is critical. It is believed that sound desensitization is very useful for reducing sound sensitivity. Unfortunately, many people with autism spectrum disorder are equipped with sound-protection devices, such as earplugs. Some parents believe that this kind of protection is helpful and insist on using it. One of the important steps in sound desensitization, however, is avoiding unnecessary use of sound-protection devices, particularly in environments that are not extraordinarily loud. Acoustical enrichment of the environment with music, musical toys, and computer-generated sounds will expedite the desensitization process. Some clinicians recommend “breaking” the bond between the auditory and limbic systems that potentially is causing hypersensitivity to sound ( Focus Autism Other Dev Disabl 2011;28[3]:184-186http://foa.sagepub.com/content/26/3/184.full.pdf). The negative emotional descriptions of loud sounds, such as “scary and fearful sounds,” should be replaced by descriptions such as “unwanted sounds” ( Focus Autism Other Dev Disabl 2011;26[3]:184-186http://foa.sagepub.com/content/26/3/184.full.pdf+html). A simple method of sound desensitization is to ask patients or their parents to provide the clinician with a list of sounds that are more annoying than others. The list of annoying sounds may include a fire alarm, flushing toilet, and vacuum cleaner. Most of these sounds can be downloaded as sound files to personal music players. Patients are instructed to listen to these unwanted sounds at a low level for 15 minutes to 20 minutes a day, slightly increasing the volume every week. This is a very effective method for improving sound tolerance issues in the ASD population. If necessary, sound tolerance conditions such as misophonia, hyperacusis, recruitment, and phonophobia should be explained to patients and their parents. Furthermore, extensive directive counseling and cognitive behavioral therapy by trained practitioners will ease the process of desensitization to sound.

**Решение:** -1 колонка / обзор (The Hearing Journal)

---

### 293 · R0395

**Psychiatric Comorbidities in Hyperacusis and Misophonia: A Systematic Review.**

2025 · Audiology research · article, conference object, journal article · eng · https://doi.org/10.3390/audiolres15040101

Background : The aim of this study was to conduct a systematic review of the research literature on the prevalence of psychiatric comorbidities in patients with hyperacusis and misophonia. Method : Four databases were searched: PubMed, PsycINFO, Scopus, and Web of Science (Wis)-last search conducted on the 16th of April 2024 to identify relevant studies. The methodological quality of each study was independently assessed using the JBI Critical Appraisal Checklist. Results : Five studies were included for the prevalence of psychiatric comorbidities in hyperacusis, and seventeen studies for misophonia. Among patients with hyperacusis, between 8% and 80% had depression, and between 39% and 61% had any anxiety disorder as measured via a diagnostic interview and/or self-report questionnaires. For misophonia, nine studies provided data on various forms of mood and anxiety disorders, with prevalences ranging from 1.1% to 37.3% and 0.2% to 69%, respectively. Conclusions : Although the 22 included studies varied considerably in design and scope, some recurring patterns of comorbidity were noted. However, apparent trends-such as the higher prevalence of mood and anxiety disorders compared to other psychiatric conditions-should be interpreted with caution, as most studies did not comprehensively assess a full range of psychiatric disorders. This likely skews prevalence estimates toward the conditions that were specifically investigated.

**Решение:** -1 обзор / комментарий / письмо

---

### 294 · R0190

**Real-time emotional responses to trigger sounds in misophonia: An ecological momentary assessment study.**

2026 · Journal of affective disorders · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jad.2026.121429

Although misophonia is characterized by intense negative emotional responses, the temporal dynamics of these experiences in naturalistic settings are poorly understood. This study utilized ecological momentary assessment (EMA) to characterize the real-time emotional experiences of adults with misophonia outside of laboratory settings. Forty adults with misophonia completed EMA surveys for 10 days. Results indicated that trigger sounds elicited significant elevations in negative emotions, particularly irritability and anger, compared to non-trigger periods. Although most emotional responses subsided substantially within 1 h, recovery patterns and the intensity of reactivity (e.g., hostility, disgust) varied considerably across individuals. Greater emotional reactivity was associated with higher baseline negative affect, greater misophonia severity, and co-occurring psychopathology. To our knowledge, this is the first EMA study to detail real-time emotional patterns in misophonia. Findings provide novel insights into the moment-to-moment experience of the disorder and highlight key individual differences that may inform personalized interventions targeting emotional reactivity.

**Решение:** -3 выборка набрана из-за мизофонии

---

### 295 · R0003

**Lavendeltee gegen Misophonie**

2026 · Zeitschrift für Phytotherapie · article, journalarticle · de · https://doi.org/10.1055/a-2763-4565

Eine türkische Forschergruppe untersucht die Wirksamkeit von Lavendeltee bei Probanden mit Misophonie. Misophonie ist eine ungewöhnliche Aversion gegen bestimmte Geräusche und damit abgrenzbar von Hyperakusis. Typische Trigger sind Kauen, Atmen, Klicken usw. ([ Abb. 1 ]). Bei Exposition treten sympathische Stressreaktionen auf, die auf Dauer u. a. zu Vermeidungsverhalten, Angst, Aggression, Hilflosigkeit oder Depression führen können. Neben psychotherapeutischen Behandlungen werden selektive Serotonin-Wiederaufnahmeinhibitoren (SSRI), antipsychotische Mittel und β-Blocker eingesetzt. Lavendel könnte wegen seiner angstlösenden und antidepressiven sowie das Wohlbefinden verbessernden Wirkungen bei Misophonie nützlich sein. Abb. 1 Misophonie-Betroffene empfinden bestimmte Geräusche als außerordentlich unangenehm. Abhilfe ist schwierig. © Salome/stock.adobe.com Eingeschlossen wurden Erwachsene über 18 Jahren, die über mindestens 3 Triggergeräusche im Rahmen einer Misophonie klagten. Ausgeschlossen wurden Menschen mit Allergien gegen Kräutertee, Nahrungsmittel oder Medikamente, mit psychiatrischen oder chronischen Erkrankungen, ferner solche unter psychiatrischer Medikation sowie weiterer Medikamente, Kräutertees. Menschen mit Tinnitus oder Hyperakusis wurden ebenfalls ausgeschlossen. Publication History Article published online: 02 July 2026 © 2026. Thieme. All rights reserved. Georg Thieme Verlag KG Oswald-Hesse-Straße 50, 70469 Stuttgart, Germany

**Решение:** -1 обзор литературы / концептуальная статья

---

### 296 · R0541

**Corrigendum to "Clinical characteristics, impairment, and psychiatric morbidity in 102 youth with misophonia" [J. Affect. Disord. volume 324 (2023) 395-402].**

2024 · Journal of affective disorders · article, journalarticle, published erratum · eng · https://doi.org/10.1016/j.jad.2023.11.045

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -7 erratum / correction

---

### 297 · R1466

**A brief course of cognitive behavioural therapy for the treatment of misophonia: a case example**

2013 · The Cognitive Behaviour Therapist · article · en · https://doi.org/10.1017/s1754470x13000172

Abstract Misophonia is a condition of unknown cause characterized by atypically intense negative physiological and emotional reactions to hearing certain sounds – most often those associated with oral functions. Individuals with misophonia often report high levels of psychological distress and avoidance behaviours that seriously compromise their occupational and social functioning. As of yet, no effective treatment of misophonia has been identified, and health care providers often struggle when they encounter clients who have it. This case report describes the assessment, case formulation, and treatment of a client with misophonia using cognitive behavioural therapy (CBT), and serves as an initial contribution to the evidence base for the efficacy of CBT in the treatment of misophonia.

**Решение:** -2 клинический случай / серия случаев

---

### 298 · R0875

**Audiologist-Delivered Cognitive Behavioral Therapy for Tinnitus**

2022 · Plural Publishing · part of book or chapter of book, text · eng · https://arro.anglia.ac.uk/id/eprint/707431/10/Beukes_Manchaiah_2022.pdf

The term ‘tinnitus’ is searched over 110,000+ times every month. Unfortunately, much of the information readily available through internet searches is inaccurate, whereas most evidence-based information is only available through peer-reviewed journal articles often containing dense scientific jargon. Tinnitus: Advances in Prevention, Assessment, and Management aims to bridge this gap by providing up-to-date and evidence-based information on tinnitus prevention, assessment, and management. Presented in a quick, easy-to-read format, this text offers a practical and handy resource for busy practitioners and health profession students, as well as individuals with bothersome tinnitus.\ud Each section contains short chapters providing accessible overviews of research related to tinnitus and hyperacusis. Section I delves into various approaches for prevention of hearing loss and tinnitus. Section II covers tinnitus assessment, while Section III introduces readers to a range of tinnitus management solutions. Section IV focuses solely on recent advances in assessment and management of hyperacusis and other disorders of decreased sound tolerance. Authors of Section V review recent tinnitus-related developments, including social media use and COVID-19. The final section consists of interesting real-life case studies involving patients with bothersome tinnitus.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)

---

### 299 · R0709

**Etiology, Composition, Development and Maintenance of Misophonia: A Conditioned Aversive Reflex Disorder**

2023 · PsyArXiv · preprint · en · https://doi.org/10.31234/osf.io/j2z6n

Misophonia is a recently identified condition in which an individual has an acute reaction of hatred or disgust to a specific commonly occurring sound. We propose that misophonia is a form of conditioned behavior that develops as a physical reflex through Pavlovian conditioning. Although misophonia is generally considered to be a one-step reaction, in which the sound elicits rage or disgust, as well as typical autonomic responses associated with these emotions, we propose that misophonia is a two-step reaction, in which the sound elicits an aversive conditioned physical reflex, and the aversive conditioned physical reflex elicits hatred or disgust. We also propose that the emotional response to trigger stimuli creates a Pavlovian conditioning paradigm that maintains or strengthens the misophonic physical reflex. Finally, we propose that new misophonic trigger stimuli are developed through the pairing of a neutral stimulus with a misophonic trigger stimulus. We suggest that a better name for misophonia is Conditioned Aversive Reflex Disorder (CARD) since it focuses attention on the reflexive nature of this condition and incorporates multiple stimuli modalities. A counterconditioning treatment for misophonia is presented with brief case descriptions which demonstrate the conditioned reflex nature of this disorder.

**Решение:** -5 качественное / теоретическое / алгоритмическое исследование

---

### 300 · R0378

**Low-latency Assistive Audio Enhancement for Neurodivergent People**

2025 · arXiv (Cornell University) · article, preprint, preprint/article · en · https://doi.org/10.48550/arxiv.2509.10202

Neurodivergent people frequently experience decreased sound tolerance, with estimates suggesting it affects 50-70% of this population. This heightened sensitivity can provoke reactions ranging from mild discomfort to severe distress, highlighting the critical need for assistive audio enhancement technologies In this paper, we propose several assistive audio enhancement algorithms designed to selectively filter distressing sounds. To address this, we curated a list of potential trigger sounds by analyzing neurodivergent-focused communities on platforms such as Reddit. Using this list, a dataset of trigger sound samples was compiled from publicly available sources, including FSD50K and ESC50. These samples were then used to train and evaluate various Digital Signal Processing (DSP) and Machine Learning (ML) audio enhancement algorithms. Among the approaches explored, Dynamic Range Compression (DRC) proved the most effective, successfully attenuating trigger sounds and reducing auditory distress for neurodivergent listeners.

**Решение:** -4 нет инструмента именно для мизофонии (гиперакузия, тиннитус, слух)
