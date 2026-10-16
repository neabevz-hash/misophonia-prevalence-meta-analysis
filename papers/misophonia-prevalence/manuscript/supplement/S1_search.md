# Supplementary File S1. Search strategies (PRISMA-S)

No date, language or publication-type limits. Condition terms only, no prevalence filter. Searches ran after the OSF registration (10.17605/OSF.IO/39MQ2). Code: `search/search.py`; logs: `search/runs/2026-10-10/`.

| Source | Interface | Searched (UTC) | Query | Records |
| --- | --- | --- | --- | --- |
| PubMed | NCBI E-utilities | 2026-10-10T15:56:24+00:00 | `misophonia[All Fields] OR misophon*[tw] OR "selective sound sensitivity"[tw] OR misokinesia[tw] OR "decreased sound tolerance"[tw] OR "sound intolerance"[tw] OR "sound tolerance disorder*"[tw] OR "misophonia"[Supplementary Concept]` | 480 |
| Europe PMC | REST API | 2026-10-10T15:56:32+00:00 | `(TITLE_ABS:misophon* OR KW:misophon* OR TITLE_ABS:"selective sound sensitivity" OR TITLE_ABS:misokinesia OR TITLE_ABS:"decreased sound tolerance" OR TITLE_ABS:"sound intolerance" OR TITLE_ABS:"sound tolerance disorder" OR TITLE_ABS:"sound tolerance disorders" OR TITLE_ABS:misofonia OR TITLE_ABS:mizofoni OR TITLE_ABS:misophonie)` | 527 |
| OpenAlex | API, title and abstract | 2026-10-10T15:56:45+00:00 | `title_and_abstract.search:misophonia¦misophonic¦misophonics¦"selective sound sensitivity"¦misokinesia¦"decreased sound tolerance"¦"sound intolerance"¦"sound tolerance disorder"¦"sound tolerance disorders"¦misofonia¦misofonía¦mizofoni¦misophonie¦мизофония¦ミソフォニア¦미소포니아` | 1,136 |
| Semantic Scholar | Graph API, bulk search | 2026-10-10T15:56:55+00:00 | `misophonia ¦ misophonic ¦ "selective sound sensitivity" ¦ misokinesia ¦ "decreased sound tolerance" ¦ "sound intolerance" ¦ misofonia ¦ mizofoni ¦ misophonie` | 791 |
| DataCite | REST API | 2026-10-10T15:56:58+00:00 | `titles.title:(misophon* OR misofon* OR mizofon* OR "selective sound sensitivity" OR misokinesia OR "decreased sound tolerance" OR "sound intolerance" OR "sound tolerance disorder" OR "sound tolerance disorders") OR descriptions.description:(misophon* OR misofon* OR mizofon* OR "selective sound sensitivity" OR misokinesia OR "decreased sound tolerance" OR "sound intolerance" OR "sound tolerance disorder" OR "sound tolerance disorders") OR subjects.subject:(misophon* OR misofon* OR mizofon* OR "selective sound sensitivity" OR misokinesia OR "decreased sound tolerance" OR "sound intolerance" OR "sound tolerance disorder" OR "sound tolerance disorders")` | 331 |
| OpenAIRE Graph | API v1, research products, type publication; three queries (at most four OR operators each) | 2026-10-10T15:57:37+00:00 | `misophonia OR misophonic OR misofonia OR misofonía OR mizofoni ¦ misophonie OR misokinesia OR "selective sound sensitivity" OR "decreased sound tolerance" OR "sound intolerance" ¦ "sound tolerance disorder" OR "sound tolerance disorders"` | 1,098 |
| CORE | API v3, title or abstract, one query per term; records kept only if the term occurs in the title or abstract | 2026-10-10T16:25:08+00:00 | `title:misophonia OR abstract:misophonia ¦ title:misophonic OR abstract:misophonic ¦ title:misofonia OR abstract:misofonia ¦ title:misofonía OR abstract:misofonía ¦ title:mizofoni OR abstract:mizofoni ¦ title:misophonie OR abstract:misophonie ¦ title:misokinesia OR abstract:misokinesia ¦ title:"selective sound sensitivity" OR abstract:"selective sound sensitivity" ¦ title:"decreased sound tolerance" OR abstract:"decreased sound tolerance" ¦ title:"sound intolerance" OR abstract:"sound intolerance" ¦ title:"sound tolerance disorder" OR abstract:"sound tolerance disorder" ¦ title:"sound tolerance disorders" OR abstract:"sound tolerance disorders"` | 1,615 |
| Instrument citations | OpenAlex, works citing the development papers of ten instruments | 2026-10-10T15:58:15+00:00 | `A-MISO-S (Schröder et al., 2013) (10.1371/journal.pone.0054706): 415; MQ (Wu et al., 2014) (10.1002/jclp.22098): 365; AMISOS-R (Jager et al., 2020) (10.1371/journal.pone.0231390): 272; MisoQuest (Siepsiak et al., 2020) (10.3390/ijerph17051797): 106; S-Five (Vitoratou et al., 2021) (10.3390/psych3040041): 61; DMQ (Rosenthal et al., 2021) (10.3389/fpsyg.2021.709928): 118; BMQ-R (Remmert et al., 2022) (10.1371/journal.pone.0269428): 17; DVMSQ (Williams et al., 2022) (10.3389/fpsyg.2022.897901): 60; SMS-Adolescent (Rinaldi et al., 2022) (10.3389/fpsyg.2022.808379): 57; SMS-Adult (Simner et al., 2024) (10.1177/10731911241234104): 29` | 1,500 |
| SciELO | SciELO Search in a browser, all indexes | 2026-10-10 | `misofonia OR misophonia OR misofonía` | 7 |
| Google Scholar | browser, first 200 results per query, pages saved by the reviewer | 2026-10-10 | `misophonia prevalence ¦ misophonia "cut-off" OR "clinically significant"` | 400 |

## De-duplication

- Records retrieved: 7,885; unique records: 1,570; duplicates removed: 6,315 (of which 1,284 pointer or component records attached to their database record).
- Removed automatically as non-study records (every source types them as datasets, peer-review reports, paratext, book reviews, software, registrations or figures): 62.
- Records screened: 1,508; found only through instrument citations: 75; only through DataCite, OpenAIRE, CORE or Google Scholar: 310.
- Recall on the seed set (the 12 studies of Gowda & Prabhu, 2024): 12 of 12.

LILACS (BVS) could not be searched: its search servers refused connections from our network (deviations.md).

## Citation searching of the included studies

Run on 2026-10-14T19:12:50+00:00 through OpenAlex (`search/citation_chase.py`). Seeds: the 119 included reports and four systematic reviews; 119 found in OpenAlex; not found: R0555, R0717, R0912, R0986 (reference lists checked by hand).
- Backward: 2,081 cited works, 323 already in the record set. Forward: 1,561 citing links, 1,392 already in the set.
- New records: 1,915; with a condition term in the title or abstract: 0.
- OpenAlex full-text search for misophonia, misophonic, selective sound sensitivity, misokinesia: 674 of the new records have a full text in OpenAlex, 140 mention a term and went to full-text assessment (deviations.md).
