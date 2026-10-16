"""Link the eligible reports into studies and extraction jobs (protocol §11b "Linking reports", E5).

Reports are linked when they describe the same sample: a preprint and its article, a thesis and its article, a dataset
record and its article, or secondary analyses of one dataset. The links below were set from the AI full-text proposals
(field possible_duplicate) and checked in the texts (same N, setting, years, ethics approval, or an explicit statement).
A study is a connected group of linked reports. Each sample is extracted once, from its main report (the most complete
one, E5); other reports of the sample are attached to the job for context while the input stays within MAX_CHARS.

Pairs that only might overlap (same university or lab, no evidence of shared participants) stay separate and are listed
in POSSIBLE, so R1 sees them in the verification file.

Writes extraction/study_map.csv (one row per report) and extraction/jobs.json (one job per main report).
Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/make_study_map.py --run 2026-10-10
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))
from common import eligible_reports, load_records  # noqa: E402
MAX_CHARS = 400_000

# main report -> (additional reports of the same samples, reason). Every report of a group is listed once.
GROUPS = [
    ("R0031", ["R0267"], "bioRxiv preprint (R0267) and article (R0031): same 140 adults, 128 from Prolific (Black et al.)"),
    ("R0196", ["R0195"], "medRxiv preprint (R0195) and article (R0196): same 1,050 autistic adults of the Netherlands Autism Register"),
    ("R0350", ["R0349", "R0197", "R0437"], "Wilfrid Laurier University undergraduate survey 2023-24 (N about 2,080-2,095): "
     "PsyArXiv preprint R0349 and PLoS ONE article R0350; R0197 and R0437 analyse the same survey and cite it"),
    ("R0941", ["R0260", "R0488"], "University of Oklahoma 343 undergraduates (Norris et al. 2022); the two tutorials R0260 and "
     "R0488 reuse a listwise-deleted subset of this dataset and cite it"),
    ("R0393", ["R0811"], "ALSPAC 'Life at 28+' wave, Sussex Screener for Misophonia: both report 333 of 4,253"),
    ("R0998", ["R0652", "R0440", "R0441"], "Williams et al.: Prolific general-population adults (n = 1,403; 'PROA' in R0441) and "
     "SPARK autistic adults (n = 936; also R0652, R0440 and the dissertation chapter R0441)"),
    ("R0057", ["R0441"], "NDD study (Dwyer et al. 2024): R0057 says the sample is described in Dwyer et al. 2024; R0441 "
     "reports it as the 'NDD' sample (n = 478 there, 492 in R0057)"),
    ("R0441", [], "Williams dissertation chapter: only the AUT sample (n = 295) is reported nowhere else; PROA is extracted from "
     "R0998 and NDD from R0057; ClinDST and LAB were recruited partly for sound intolerance (E1)"),
    ("R1086", ["R0489"], "Duke Misophonia Questionnaire development: the ResearchGate record R0489 carries the text of the "
     "Frontiers article R1086 (same MTurk Phase 2 sample, n = 424)"),
    ("R1188", ["R0810"], "Siepsiak et al. 2020, depression inpatients (n = 94): the doctoral thesis R0810 reproduces the article"),
    ("R0823", ["R0822", "R0986"], "UK representative Prolific sample (n = 772, S-Five): UK Data Service record R0822, "
     "preprint R0986, PLoS ONE article R0823"),
    ("R0963", ["R0940"], "UC Santa Cruz Study 3 (n = 102): OSF record R0940 and Frontiers article R0963"),
    ("R0972", ["R0973"], "23andMe chewing-rage item (n = 80,607): medRxiv preprint R0973 and article R0972"),
    ("R0985", ["R0984"], "Mandarin S-Five sample (n = 256): PsyArXiv preprint R0984 and article R0985"),
    ("R1056", ["R1055"], "Misokinesia samples (pilot 2,751; Study 1 650; Study 2 765): Research Square preprint R1055 and "
     "Scientific Reports article R1056"),
    ("R1137", ["R1146"], "Two Coimbra master's theses on the same 44 patients (primary care, Aveiro; psychiatric "
     "outpatients, Coimbra; Oct-Nov 2018)"),
    ("R0446", ["R0660"], "Japanese university students (n = 439, 2023): article R0446 and convention abstract R0660"),
    ("R0956", ["R0787"], "Multisense cohort, 142 children aged 10-14 tested Nov 2020-Mar 2021: R0787 Experiment 2 is the same "
     "sample as R0956"),
    ("R0625", ["R0522"], "Federal Institute of Goias students: both cite ethics approval 5.631.371; the 322 undergraduates of "
     "R0522 are probably part of the 549 students of R0625"),
]

# Samples to extract from a main report when it is not simply "every eligible sample in this report".
SAMPLES = {
    "R0998": "Extract two samples: (1) Prolific general-population adults (n = 1,403); (2) SPARK autistic adults (n = 936).",
    "R0057": "Extract the groups recruited by diagnostic status as separate samples (comparison group without autism or "
             "ADHD; ADHD only; autistic only; autistic and ADHD).",
    "R0441": "Extract only the AUT sample (autistic adults, n = 295). Do not extract PROA (extracted from R0998), NDD "
             "(extracted from R0057), ClinDST or LAB (recruited partly for sound intolerance); list them in excluded_samples.",
    "R0031": "Extract the Prolific subsample (n = 128) only; the 12 volunteers from misophonia newsletters are a selected group "
             "(E1): list them in excluded_samples.",
    "R0350": "One sample (Wilfrid Laurier undergraduates). Take the counts from the main report; where the attached reports "
             "give a different count for the same definition, keep the main report's value and describe the difference in "
             "consistency_notes.",
}

# Facts the extractor cannot see in the text.
JOB_NOTES = {
    "R0733": "A corrigendum to this article exists (10.1016/j.jad.2023.11.045, 2024; found through Crossref); its text was "
             "not available. Mention it in the sample notes.",
}

# Possible overlaps kept as separate studies (no evidence of shared participants); shown to R1.
POSSIBLE = [
    (["R0082", "R0941"], "Both University of Oklahoma students with the MQ (777 vs 343); R0082 calls its data 'collected for "
     "other purposes' and does not say it reuses Norris et al. 2022"),
    (["R0794", "R1182"], "Both Baskent University students, same first author (119 vs 638); R0794 cites R1182 as a separate study"),
    (["R0314", "R0368", "R0385", "R0910"], "Carnegie Mellon University experiments of one lab; separate experiments and years, "
     "participant pools may overlap"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = load_records(a.run)
    eligible = set(eligible_reports())

    # union-find over all reports named together in GROUPS
    parent = {k: k for k in eligible}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for main_rec, extra, _ in GROUPS:
        for k in [main_rec, *extra]:
            if k not in eligible:
                raise SystemExit(f"{k} is not an eligible report")
        for k in extra:
            parent[find(k)] = find(main_rec)
    mains = {m for m, _, _ in GROUPS}
    linked = {k for m, extra, _ in GROUPS for k in [m, *extra]}
    singles = sorted(eligible - linked)
    comps: dict[str, list[str]] = {}
    for k in sorted(eligible):
        comps.setdefault(find(k), []).append(k)
    # study order: by the smallest main report id of the group (singletons are their own main)
    def first_main(members):
        return min(k for k in members if k in mains or k in singles)
    order = sorted(comps.values(), key=first_main)
    study_of = {}
    for i, members in enumerate(order, 1):
        for k in members:
            study_of[k] = f"ST{i:03d}"

    possible_of: dict[str, list[str]] = {}
    for members, why in POSSIBLE:
        for k in members:
            others = ", ".join(f"{m} ({study_of[m]})" for m in members if m != k)
            possible_of.setdefault(k, []).append(f"possible overlap with {others}: {why}")

    def chars(k):
        raw = (PAPER / "fulltext" / "text" / f"{k}.txt").read_text(encoding="utf-8")
        return len(raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw)

    jobs, rows = [], []
    group_of = {m: (extra, why) for m, extra, why in GROUPS}
    for k in [*sorted(mains), *singles]:
        extra, why = group_of.get(k, ([], ""))
        budget = MAX_CHARS - chars(k)
        attached, listed = [], []
        for e in extra:
            if chars(e) <= budget:
                attached.append(e)
                budget -= chars(e)
            else:
                listed.append(e)
        jobs.append({"job_id": k, "study_id": study_of[k], "main": k, "attached": attached, "listed_only": listed,
                     "link_reason": why, "samples": SAMPLES.get(k, "Extract every eligible sample in the main report."),
                     "job_notes": JOB_NOTES.get(k, ""),
                     "possible_overlap": possible_of.get(k, [])})
    roles = {}
    for j in jobs:
        roles.setdefault(j["main"], []).append(f"main of job {j['job_id']}")
        for e in j["attached"] + j["listed_only"]:
            roles.setdefault(e, []).append(f"additional in job {j['job_id']}")
    for k in sorted(eligible, key=lambda x: (study_of[x], x)):
        u = recs[k]
        rows.append({"study_id": study_of[k], "rec_id": k, "role": "; ".join(roles.get(k, [])),
                     "first_author": u.get("first_author") or "", "year": u.get("year") or "",
                     "doi": u.get("doi") or "", "title": u.get("title") or "",
                     "link_reason": next((why for m, extra, why in GROUPS if k == m or k in extra), ""),
                     "possible_overlap": " | ".join(possible_of.get(k, []))})
    with (HERE / "study_map.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    (HERE / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    n_studies = len(order)
    print(f"{len(eligible)} reports -> {n_studies} studies, {len(jobs)} extraction jobs "
          f"({sum(1 for j in jobs if j['attached'])} with attached reports, "
          f"{sum(1 for j in jobs if j['listed_only'])} with reports listed only)")


if __name__ == "__main__":
    main()
