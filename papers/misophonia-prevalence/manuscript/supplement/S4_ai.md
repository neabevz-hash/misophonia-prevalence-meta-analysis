# Supplementary File S4. Use of an AI assistant

Claude Opus 5.5 (Anthropic; model `claude-opus-5-5`, reasoning effort high) ran through Claude Code in headless mode (`claude -p`) with a fixed system prompt, a JSON output schema, no tools and an empty working directory; one item per call. Every output is stored with the hash of the system prompt and of the rendered prompt, the model actually used and the Claude Code version. Every label, proposal, extracted value and rating was a draft that the reviewer (R1) accepted or corrected.

| Task | Prompt | Items | Run (UTC) | System prompt SHA-256 (first 16) | Claude Code | Models used |
| --- | --- | --- | --- | --- | --- | --- |
| Title and abstract screening labels | `screening/llm_screener_prompt.md` | 1,508 | 2026-10-10T16:53 to 2026-10-10T17:47 | 66cabb001a9b6845 | 2.1.289 (Claude Code) | claude-opus-5-5 |
| Full-text eligibility proposals | `fulltext/ft_prompt.md (git tag misophonia-ft-prompt-v1.0)` | 247 | 2026-10-10T19:14 to 2026-10-11T16:25 | ac1a584ac8a6fce0 | 2.1.289 (Claude Code) | claude-opus-5-5 |
| Full-text proposals, citation search | `fulltext/ft_prompt.md (same frozen prompt)` | 112 | 2026-10-14T19:21 to 2026-10-15T03:30 | ac1a584ac8a6fce0 | 2.1.289 (Claude Code) | claude-opus-5-5 |
| Extraction and risk-of-bias drafts | `extraction/extract_prompt.md (git tag misophonia-extraction-prompt-v1.0)` | 98 | 2026-10-14T18:57 to 2026-10-15T04:54 | b7801ae26da3cf2d | 2.1.289 (Claude Code) | claude-opus-5-5 |

## Agreement with the reviewer

- Title and abstract, blind calibration sample (n = 151): see `screening/decisions/calibration_stats.json` (κ, Gwet's AC1, sensitivity and specificity of the AI for sending a record to full text).
- Included reports that the AI had labeled exclude at title and abstract: 2 of 119 (R0274, R0583); 2 of them reached full text only through the reviewer's blind re-screening of the AI-excluded records (the pre-specified safeguard).
- Full text: the reviewer's decision matched the AI proposal for 229 of 247 reports from the database search and 111 of 112 from the citation search.
- Extraction: the reviewer verified 11,155 drafted values (125 samples, 565 estimates) against the sources and corrected 0, including 0 of 3,200 key values (sample size, population type and sampling of each sample; instrument, threshold, level, cases and denominator of each estimate); estimates added by the reviewer: 0 (`extraction/decisions/correction_stats.json`).
- Supporting quotes: 468 of 516 quotes for estimates and 361 of 368 for key sample fields were found verbatim in the source text after normalizing spacing and punctuation; the others joined cells of a table or paraphrased it (`extraction/quote_check.py`).
- Two independent AI passes over the same full texts: for 112 of 113 case counts read directly from a report (levels L1–L3, whole sample, not derived), the extraction draft and the earlier full-text proposal gave the same number of cases and denominator.

