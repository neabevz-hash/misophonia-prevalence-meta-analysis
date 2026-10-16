# Check run, 2026-10-10 (before registration; not a search for screening)

Purpose: test the changes made after the pilot, before freezing protocol v1.0.
- PubMed parser now keeps book records (pilot: 480 hits, 478 records; now 480).
- DataCite added as a source (330 records).
- OpenAIRE Graph added as a source (1,096 records), replacing BASE and OATD, which block automated access.
- De-duplication v1.0 rules (version DOIs, supplementary files, pointer sources, more non-study types).

Sources: PubMed, DataCite and OpenAIRE were searched on 2026-10-10 (`search_log.json`). Europe PMC, OpenAlex, Semantic Scholar and the instrument citations are copies of the pilot exports of 2026-10-09 (`../2026-10-09-pilot/search_log.json`). CORE, the other replacement for BASE, was tested with single queries only (969 hits for "misophonia" in titles or abstracts): without an API key it serves about ten requests per ten minutes, so its full retrieval runs only in the final search.

Result (`dedup_report.json`): 5,857 records, 1,434 unique, 99 removed automatically, 1,335 to screen; 132 records reached the set only through DataCite or OpenAIRE (18 only through DataCite, 70 only through OpenAIRE). Recall on the seed set: 12 of 12 (`recall_seed_set.json`).
