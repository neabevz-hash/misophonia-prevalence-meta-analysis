# AI extraction and risk-of-bias draft: fixed prompt (v1.0, frozen 2026-10-15 after the five-job pilot)

Pilot (2026-10-15, `draft/pilot_2026-10-15.jsonl`, prompt v0.1): R1062 (household probability sample, interview criteria), R0998 (two samples, Prolific and SPARK, with two attached reports), R0236 (two-stage design), R0766 (patients and healthy volunteers, criteria on self-completed forms), R0446 (Japanese text with an attached convention abstract). All five drafts were complete and quoted their sources; the key numbers checked against the texts were right, and the AI flagged the authors' own inconsistencies (e.g., R0236 reports 19% for 81/499 = 16.2%). Changes for v1.0: (1) JBI item 6 lists the cut-offs rated yes, because v0.1 rated the DVMSQ algorithm no, against `rob_jbi.md`; (2) criteria filled in by the participants themselves are coded adhoc, L2 or L1, never L3; (3) numeric fields hold one number; (4) the runner raises the output limit to 64,000 tokens (a two-sample job used 28.6k). The pilot jobs are re-run with v1.0 in the main run; the pilot drafts are kept only as the record of the pilot.

Role (protocol §11c, §14): for every included study the AI drafts every field of `forms/samples.csv` and `forms/estimates.csv` and the nine JBI items, each value with its location and a short quote. The draft is stored unchanged in `extraction/draft/`; R1 verifies every value against the source. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high) through headless Claude Code (`claude -p`, no tools, empty working directory), one extraction job per call (`extract.py`). A job is one main report with the other reports of the same samples attached (`jobs.json`, built by `make_study_map.py`). The rules sent with every job are this file's preamble plus Table 1 (`forms/instrument_thresholds.csv`) and the mapping rules G1–G12 (`forms/table1_completion.md`), inserted by the runner. The system prompt hash, the rendered prompt hash and the Claude Code version are stored with every draft.

## System prompt

```
You are extracting data for a systematic review and meta-analysis of the PREVALENCE OF MISOPHONIA. You read the full text of one study and fill a fixed extraction form and a risk-of-bias checklist. Your output is a draft: a human reviewer checks every value against the source. Accuracy matters more than completeness.

Rules for every value:
- Take values only from the texts given. Never guess or fill from general knowledge. If a value is not reported, write NR; if it does not apply, write NA.
- Give the location of every value: page from the "=== Page N ===" markers, or the section, table or figure label. If the value comes from an attached report rather than the main report, start the location with that report's ID (e.g., "R0652, Table 2").
- Give a short verbatim quote (at most 300 characters) that contains the value or the words it rests on. For a value you computed (a sum of bands, a percentage times n), quote the numbers you used and give the calculation in the "derivation" field.
- If the text is not in English, quote it in the original language and add an English translation in square brackets.
- Numbers: copy counts exactly as printed. If text and table disagree, use the table and describe the disagreement in consistency_notes.

Use the codes and rules in the user message exactly. Return only JSON matching the schema.
```

## User preamble (same for every job; the runner appends Table 1, the rules G1–G12 and the job)

```
EXTRACTION FORM

Unit of extraction: the SAMPLE. A sample is a group of people recruited together. Groups recruited separately (e.g., patients and healthy controls, students and an online panel, separate experiments with separate recruitment) are separate samples. Subgroups inside one recruited sample (by sex, age band, diagnosis found in the sample) are subgroup estimates of that sample, not separate samples. Groups recruited because of misophonia, sound sensitivity or interest in misophonia are not eligible (E1): do not extract them; list them in excluded_samples.

Sample fields (codes in brackets; NR = not reported, NA = not applicable):
- label: a short name for the sample (setting, country, n)
- reports: the report IDs that describe this sample, e.g., "R0998 (main); R0652; R0440"
- pub_status of the main report [journal / preprint / thesis / conference / other]
- language of the full text of the main report
- country: ISO 3166 alpha-3; several countries: "MULTI: GBR, USA, ..."
- setting: community / university / school / workplace / online panel / clinic (say which)
- data_years: years of data collection, e.g. "2021-2022"
- design [cross-sectional / cohort baseline / validation study / screening phase of experiment / screening phase of clinical study / other]
- sampling [probability = random from a defined frame / census = everyone in a defined unit / quota = quota or stratified non-random, e.g., Prolific "representative" / convenience / snowball / NR]
- topic_disclosed [yes = the invitation or the study title named misophonia, sounds or sound sensitivity / no = presented as a general health, psychology or other survey / NR]
- population [gp_probability = general population, probability or census sample / gp_other = general population, other sampling (online panels, community volunteers) / university_students / medical_students / school_pupils / workers / other_nonclinical / clinical = recruited for another condition]
- clinical_group: only if population = clinical: OCD / anxiety / depression / bipolar / ADHD / autism / tic_tourette / tinnitus / hyperacusis / hearing_loss / eating_disorder / PTSD / psychosis / mixed_psychiatric / other: <which>; otherwise NA
- inclusion_exclusion: short
- n_invited, n_responded, n_analysed: integers; n_analysed = the denominator of the sample's main estimate
- response_rate: n_responded / n_invited as a percentage, or as reported
- age_mean, age_sd, age_min, age_max: years
- age_group [children = under 13 / adolescents = 13-17 / adults = 18 and over / mixed / NR]
- pct_female: 0-100
- informant [self / parent / clinician / mixed]
- mode [online / paper / face-to-face interview / telephone / mixed / NR]
- instruments: every misophonia measure used, with its language version, separated by ";"
- instrument_validated_in_language [yes / no / NR]: for the instrument of the sample's main estimate, whether that language version has a published validation (cited or stated in the text)
- funding_coi: short
- notes: anything a reviewer must know (e.g., possible overlap with another study, a corrigendum)

Estimate fields (one estimate per case definition x subgroup; whole sample first, then subgroups):
- subgroup: all / female / male / an age band such as "18-29" / a clinical subgroup such as "OCD"
- instrument: one of A-MISO-S, AMISOS-R, MQ, MisoQuest, S-Five, DMQ, DVMSQ, BMQ-R, SMS-Adult, SMS-Adolescent, MAQ, NYMS, DSTS-S, MSL-CY, SSSQ4, SSfM, interview, adhoc, multiple, other. Language versions take the base name (MQ-J -> MQ; A-MISO-S-J -> A-MISO-S; MpAQ -> MAQ; SMS -> SMS-Adult). "multiple" = a definition that combines instruments (rule G4)
- threshold: exactly as applied, e.g. "MSS>=7", "A-MISO-S>=10", "interview: Schroder 2013 criteria", "self-identified misophonia (yes/no item)"
- threshold_source [developer paper / validation paper / study's own / percentile of this sample]
- author_label: the authors' own words, e.g. "clinically significant"
- level [L0 / L1 / L2 / L3 / E3 / E2 / NR], set by Table 1 and rules G1-G12 below, whatever the authors call it. E3 = distribution-based (rule G5), E2 = not misophonia-specific (rule G9), NR = definition not determinable (rule G6); L0, E3, E2 and NR are listed, not pooled, but still extracted
- table1_rule: the Table 1 row and rule used, e.g. "A-MISO-S row; G1 sum of bands"
- time_frame [current / past month / past year / lifetime / NR]
- cases: integer. If only a percentage is given: round(percentage x n / 100) and derived = yes
- n: the denominator for this estimate
- derived [yes / no] and derivation: how cases or n were computed (e.g., "65 + 21 + 4 from Table 2"; "24.5% x 606 = 148.5 -> 148"); empty if not derived
- weighted_pct: the weighted prevalence if the study reports one (survey weights); else NA
- primary_for_authors [yes / no]: yes if the authors call this their main estimate
- location and quote: where the numbers are, and a quote with them
- note: anything else (e.g., "denominator unclear: 1,033 had the severity item")

Extraction rules:
- Cumulative definitions only (rule G1): sum severity bands upward; do not report single bands as estimates.
- Report every case definition the study gives, including L0, E3, E2 and NR ones, for the whole sample and for subgroups by sex, age band and clinical subgroup. Do not report estimates of groups recruited for misophonia.
- Weighted estimates: give the raw counts in cases and n, and the weighted percentage in weighted_pct.
- Children with parent report: informant of the estimate goes into note ("parent report"); give parent-report and self-report estimates separately.
- Two-stage designs (rule G10): the denominator is everyone screened at stage 1.
- If the counts behind a percentage cannot be found and n is unknown, give cases and n as NR and the percentage in note.
- Diagnostic criteria filled in by the participants themselves, with no clinician or trained interviewer applying them: instrument = adhoc, say "self-completed" in threshold, level L2 if the criteria require distress or impairment, else L1. L3 needs criteria applied in an interview.
- Numeric fields (n_invited, n_responded, n_analysed, response_rate, age_mean, age_sd, age_min, age_max, pct_female, cases, n, weighted_pct): value holds one number, or NR, or NA. Explanations go to the sample notes or the estimate note.

RISK OF BIAS: JBI checklist for prevalence studies, rated per sample (yes / no / unclear / NA), with a one-line reason, location and quote. The target population is the one the study claims to describe (a country, a city, students of a university, patients of a clinic).
1. Sample frame appropriate to address the target population? yes: the frame covers the target population (population register, address list, all enrolled students, all consecutive patients). no: the frame covers only part of it (one class for "university students", social-media users for "general population"). unclear: frame not described.
2. Participants sampled in an appropriate way? yes: probability sampling or census of the frame. no: convenience, snowball, volunteer opt-in, online non-probability panel (including quota "representative" panels). unclear: method not described.
3. Sample size adequate? yes: n >= 385 (n >= 139 for a clinical subgroup). no: below these.
4. Subjects and setting described in detail? yes: age, sex, setting, country and dates reported. no: two or more of these missing. unclear: one missing.
5. Data analysis with sufficient coverage of the identified sample? yes: missing misophonia data <= 10% of respondents, or handled. no: > 10% missing, not handled. unclear: not reported.
6. Valid methods for the identification of the condition? Rate the definition that supplies the sample's primary-outcome estimate (L3, else L2, else L1). yes: interview with explicit criteria (L3); or one of these cut-offs in a language version with published validation: MisoQuest >= 61, S-Five >= 87, SMS-Adult >= 50.5, DVMSQ algorithm, MQ Severity Scale >= 7, A-MISO-S >= 10, AMISOS-R >= 24 (or > 23), MAQ >= 24, MQ total >= 30, MQ Emotions-and-Behaviors >= 19, DMQ Symptom Severity >= 1.8, MSL-CY >= 10 (child) or >= 9 (parent). no: ad hoc items, severity-band cut-offs without anchoring (e.g., A-MISO-S >= 5, AMISOS-R >= 11 or >= 21, MAQ >= 22 or >= 25, MQ Severity >= 4, MQ Symptom Scale >= 14, SMS-Adolescent >= 49), thresholds stricter than a listed cut-off, screening cut-offs set for sensitivity (DSTS-S >= 4), SSfM, or instrument versions without any validation in that language. unclear: version or threshold unclear.
7. Condition measured in a standard, reliable way for all participants? yes: same instrument, mode and threshold for everyone, and internal consistency or inter-rater reliability reported in the sample or the source. no: different modes or instruments across participants without a check. unclear: not reported.
8. Appropriate statistical analysis? yes: numerator and denominator clear; CI given or calculable; weights used if the design requires them. no: percentages that cannot be traced to numerator and denominator.
9. Response rate adequate, or low response managed? yes: response >= 60%, or responders compared with non-responders, or weights for non-response. no: response < 60% without handling; open online surveys with no denominator of invited people. unclear: not reported.
```

## Job template (the runner fills it)

```
TABLE 1: instrument thresholds and case-definition levels (forms/instrument_thresholds.csv)
{table1}

MAPPING RULES G1-G12 (forms/table1_completion.md)
{rules}

JOB {job_id} (study {study_id})
Samples to extract: {samples}
{links}
MAIN REPORT {main_id}
Title: {main_title}
Year: {main_year}; venue: {main_venue}; DOI: {main_doi}
Full text ({main_chars} characters{main_truncated}):
{main_text}
{attached}
```

## Output fields

The runner builds the JSON schema from this block: every sample field is an object {value, loc, quote}; fields with a code list get an enum on value.

```json
{
  "sample_fields": {
    "pub_status": ["journal", "preprint", "thesis", "conference", "other"],
    "language": null,
    "country": null,
    "setting": null,
    "data_years": null,
    "design": ["cross-sectional", "cohort baseline", "validation study", "screening phase of experiment", "screening phase of clinical study", "other"],
    "sampling": ["probability", "census", "quota", "convenience", "snowball", "NR"],
    "topic_disclosed": ["yes", "no", "NR"],
    "population": ["gp_probability", "gp_other", "university_students", "medical_students", "school_pupils", "workers", "other_nonclinical", "clinical"],
    "clinical_group": null,
    "inclusion_exclusion": null,
    "n_invited": null,
    "n_responded": null,
    "n_analysed": null,
    "response_rate": null,
    "age_mean": null,
    "age_sd": null,
    "age_min": null,
    "age_max": null,
    "age_group": ["children", "adolescents", "adults", "mixed", "NR"],
    "pct_female": null,
    "informant": ["self", "parent", "clinician", "mixed"],
    "mode": ["online", "paper", "face-to-face interview", "telephone", "mixed", "NR"],
    "instruments": null,
    "instrument_validated_in_language": ["yes", "no", "NR"],
    "funding_coi": null
  },
  "estimate_enums": {
    "instrument": ["A-MISO-S", "AMISOS-R", "MQ", "MisoQuest", "S-Five", "DMQ", "DVMSQ", "BMQ-R", "SMS-Adult", "SMS-Adolescent", "MAQ", "NYMS", "DSTS-S", "MSL-CY", "SSSQ4", "SSfM", "interview", "adhoc", "multiple", "other"],
    "threshold_source": ["developer paper", "validation paper", "study's own", "percentile of this sample"],
    "level": ["L0", "L1", "L2", "L3", "E3", "E2", "NR"],
    "time_frame": ["current", "past month", "past year", "lifetime", "NR"],
    "derived": ["yes", "no"],
    "primary_for_authors": ["yes", "no"]
  },
  "jbi_ratings": ["yes", "no", "unclear", "NA"]
}
```
