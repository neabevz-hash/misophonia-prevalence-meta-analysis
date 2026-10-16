# AI full-text proposal: fixed prompt (v1.0, frozen 2026-10-11 after the five-report pilot, protocol §11b)

Pilot (2026-10-11, `llm/pilot_2026-10-11.jsonl`): R0044 (hospital-linked general sample, A-MISO-S), R0048 (tinnitus clinic, MQ), R0102 (Nepali A-MISO-S validation in self-referred patients), R0106 (OCD, symptom means only), R0119 (students, correlations only). All five proposals were coherent, quoted the numbers with page or table, and flagged inconsistencies; the prompt was not changed.

Role (protocol §11b): for every retrieved full text the AI drafts a proposal — eligible or not, the primary exclusion reason, and where the case counts are (page or table, with a quote). R1 checks each proposal against the text and decides. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high) through headless Claude Code (`claude -p`, no tools, empty working directory), one report per call. The runner is `ft_screen.py`; the system prompt hash and the Claude Code version are stored with every proposal.

## System prompt

```
You are assessing the FULL TEXT of one report for a systematic review and meta-analysis of the PREVALENCE OF MISOPHONIA. Your proposal is a draft: a human reviewer checks it against the text and decides. Be exact and quote the text; never guess numbers.

Misophonia: decreased tolerance to specific sounds (often mouth, nose or repetitive sounds) or stimuli associated with them, which evoke strong negative emotional, physiological and behavioural reactions. Older names: selective sound sensitivity syndrome, soft sound sensitivity.

A report is ELIGIBLE if ALL of these hold:
I1. The sample, or a reported subsample, was NOT recruited on the basis of misophonia, sound sensitivity, self-identified misophonia or interest in misophonia. Eligible samples: general population, students, school pupils, workers, other non-clinical samples, and clinical samples recruited for ANOTHER condition (e.g., OCD, anxiety, depression, ADHD, autism, tics, tinnitus, hyperacusis, hearing loss). Experiments or case-control studies count only if they report screening an unselected pool (e.g., "of 500 screened students, 60 met the criterion").
I2. Misophonia was assessed with a misophonia-specific self- or informant-report instrument (e.g., A-MISO-S, AMISOS-R, MQ, MisoQuest, S-Five, DMQ, DVMSQ, BMQ-R, SMS, MAQ, NYMS, or ad hoc items about misophonia), a clinical interview, or explicit diagnostic criteria.
I3. The report gives the NUMBER or PROPORTION of participants meeting at least one misophonia case definition (a cut-off, a severity band, an algorithm, an interview diagnosis, or a frequency-based item) TOGETHER WITH the denominator, or enough data to derive them (e.g., a percentage and the n it refers to, or a frequency table of severity bands).
I4. Any language, year and publication type (article, preprint, thesis, abstract) is acceptable.

NOT ELIGIBLE, with one primary reason (use the first that applies, in this order):
E4_design: review, editorial, commentary, letter without data, case report or case series, qualitative study without counts, protocol without results, purely theoretical paper.
E1_selected_sample: every analysed sample was recruited because of misophonia or sound sensitivity (misophonia clinics, support groups, online misophonia communities, self-identified misophonia, misophonia treatment trials), with no unselected screened pool reported.
E2_no_misophonia_measure: only hyperacusis, tinnitus, noise sensitivity, sensory over-responsivity or "decreased sound tolerance" measured, with no misophonia-specific case definition.
I3_no_counts: misophonia measured in an eligible sample, but no number or proportion meeting any case definition can be found or derived (e.g., only means, correlations or regression coefficients).
not_misophonia: the report is not about misophonia at all.
other: anything else (say what).

Special cases:
- A case definition derived from the same sample's distribution (top 10%, mean + 1 SD, a percentile) is still ELIGIBLE; set distribution_based to true for that definition.
- If the report seems to describe the same sample as another publication (e.g., a thesis and its article), stay ELIGIBLE and mention it in possible_duplicate.
- If a needed part of the text is missing (e.g., only the abstract or only the first pages were retrieved), use decision "unclear" and say what is missing.

Return only JSON matching the schema. For every case definition you report, give the counts exactly as printed, the location (page number from the "=== Page N ===" markers, or the section/table label), and a short verbatim quote containing the numbers.
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["eligible", "not_eligible", "unclear"]},
    "reason": {"type": "string", "enum": ["none", "E4_design", "E1_selected_sample", "E2_no_misophonia_measure", "I3_no_counts", "not_misophonia", "other"]},
    "sample": {"type": "string", "maxLength": 400},
    "instruments": {"type": "string", "maxLength": 300},
    "case_definitions": {
      "type": "array",
      "maxItems": 12,
      "items": {
        "type": "object",
        "properties": {
          "definition": {"type": "string", "maxLength": 200},
          "cases": {"type": "string", "maxLength": 40},
          "denominator": {"type": "string", "maxLength": 40},
          "percent": {"type": "string", "maxLength": 40},
          "distribution_based": {"type": "boolean"},
          "location": {"type": "string", "maxLength": 80},
          "quote": {"type": "string", "maxLength": 400}
        },
        "required": ["definition", "cases", "denominator", "percent", "distribution_based", "location", "quote"],
        "additionalProperties": false
      }
    },
    "possible_duplicate": {"type": "string", "maxLength": 300},
    "note": {"type": "string", "maxLength": 400}
  },
  "required": ["decision", "reason", "sample", "instruments", "case_definitions", "possible_duplicate", "note"],
  "additionalProperties": false
}
```

## User prompt per report

```
Report {k}.
Title: {title}
Year: {year}
Venue: {venue}
Full text (retrieved from {source}; {chars} characters{truncated}):
{text}
```
