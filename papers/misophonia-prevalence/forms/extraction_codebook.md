# Data extraction codebook (v1.0, frozen with protocol v1.0 on 2026-10-10)

Two linked tables. `samples.csv` has one row per independent sample. `estimates.csv` has one row per case definition × sample × subgroup (all, female, male, age band, clinical subgroup). Unknown = `NR` (not reported); not applicable = `NA`.

**Procedure (protocol §11c).**
- The AI assistant pre-fills every field of both tables from the full text. For every value it gives the source location: page, table or figure, and a short quote. The draft is stored unchanged in `extraction/draft/<sample_id>.json`.
- R1 verifies every field against the source and accepts or corrects it. The verified values go to `samples.csv` and `estimates.csv`.
- Fields marked **[K]** are key fields. R1 always checks them against the source table or text, never accepts them from the draft unseen.
- The proportion of AI-drafted values that R1 corrected is computed by comparing the stored draft with the verified tables, overall and for the [K] fields.
- The form is piloted on five studies before use. Any rule added in the pilot goes to `deviations.md` with a date.

## samples.csv

| Field | Rule |
| --- | --- |
| `sample_id` | `S###`; one per independent sample. A study with two separate samples (e.g., students and patients) gets two IDs |
| `study_id` | `ST###`; links multiple samples and reports |
| `report_ids` | `rec_id`s of all reports of this sample (article, preprint, thesis), `;`-separated; the first one supplies data |
| `first_author`, `year`, `doi` | of the main report |
| `pub_status` | journal / preprint / thesis / conference / other |
| `language` | language of the full text |
| `country` | ISO 3166 alpha-3; multi-country samples: `MULTI` + list in `notes` |
| `continent` | Asia / Europe / Americas / Africa / Oceania by the UN M49 geoscheme (Türkiye, Iran, Saudi Arabia = Asia; Russia = Europe); filled automatically from country |
| `who_region` | AFR / AMR / SEAR / EUR / EMR / WPR (filled automatically from country) |
| `income_group` | World Bank group of the country in the year of data collection: high / upper-middle / lower-middle / low (filled automatically) |
| `setting` | community / university / school / workplace / online panel / clinic (state which) |
| `data_years` | years of data collection, e.g. `2021-2022`; `NR` if not stated |
| `design` | cross-sectional / cohort baseline / validation study / screening phase of experiment / screening phase of clinical study / other |
| `sampling` **[K]** | probability (random from a defined frame) / census (everyone in a defined unit) / quota or stratified non-random (e.g., Prolific representative) / convenience / snowball / NR |
| `topic_disclosed` | yes = invitation or title named misophonia or sounds; no = disclosed as a general health or psychology survey; NR |
| `population` **[K]** | gp_probability / gp_other / university_students / medical_students / school_pupils / workers / other_nonclinical / clinical |
| `clinical_group` | only if population = clinical: OCD / anxiety / depression / bipolar / ADHD / autism / tic_tourette / tinnitus / hyperacusis / hearing_loss / eating_disorder / PTSD / psychosis / mixed_psychiatric / other (state which) |
| `inclusion_exclusion` | free text, short |
| `n_invited`, `n_responded`, `n_analysed` **[K: n_analysed]** | integers; `n_analysed` = denominator of the main estimate |
| `response_rate` | n_responded / n_invited, or as reported |
| `age_mean`, `age_sd`, `age_min`, `age_max` | years |
| `age_group` | children (<13) / adolescents (13–17) / adults (18+) / mixed |
| `pct_female` | 0–100 |
| `informant` | self / parent / clinician / mixed |
| `mode` | online / paper / face-to-face interview / telephone / mixed |
| `instruments` | all misophonia measures used, `;`-separated, with language version |
| `instrument_validated_in_language` | yes / no / NR, for the instrument of the main estimate |
| `funding_coi` | short text |
| `jbi_1` … `jbi_9` | yes / no / unclear / NA (see `rob_jbi.md`) |
| `jbi_notes` | one line per item rated no or unclear |
| `contact_author` | needed / sent YYYY-MM-DD / reply YYYY-MM-DD / no reply |
| `notes` | anything else |

## estimates.csv

| Field | Rule |
| --- | --- |
| `estimate_id` | `E####` |
| `sample_id` | link |
| `subgroup` | all / female / male / age band (e.g., `18-29`) / clinical subgroup |
| `instrument` **[K]** | short name as in `instrument_thresholds.csv` (A-MISO-S, AMISOS-R, MQ, MisoQuest, S-Five, DMQ, DVMSQ, BMQ-R, SMS-Adult, SMS-Adolescent, MAQ, NYMS, interview, adhoc, other) |
| `threshold` **[K]** | exactly as applied, e.g. `MSS>=7`, `A-MISO-S>=10`, `interview: Schröder 2013 criteria` |
| `threshold_source` | developer paper / validation paper / study's own / percentile of this sample (→ E3, not pooled) |
| `author_label` | authors' own wording, e.g. "clinically significant", "mild or above" |
| `level` **[K]** | L0 / L1 / L2 / L3 by Table 1 of the protocol (`instrument_thresholds.csv`), whatever the authors' label |
| `time_frame` | current / past month / past year / lifetime / NR |
| `cases` **[K]** | integer; if only a % is given: round(% × n / 100), and `derived = yes` |
| `n` **[K]** | denominator for this estimate |
| `derived` | yes / no |
| `weighted_pct` | weighted prevalence if the study reports one (survey weights) |
| `primary_for_authors` | yes, if the authors call this their main estimate |
| `location` | page, table or figure where the numbers are |
| `notes` | |

## Extraction rules

- If the counts in the text and a table disagree, take the table and note it.
- Weighted estimates: pool the raw counts; record the weighted % separately for a sensitivity check.
- If a study reports only "≥ moderate" and "≥ severe" bands, extract each band as its own estimate.
- Children with parent report: `informant = parent`; extract parent-report and self-report estimates separately.
- Clinical subsamples inside a community survey (e.g., people with tinnitus in a general-population sample) are extracted as a subgroup estimate, not a separate sample.
- Any rule added during the five-study pilot goes to `deviations.md` with a date.
