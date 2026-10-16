"""Recall of a search run on the seed set (protocol, section 9).

The seed set (seed_set.csv) is the 12 studies included by Gowda & Prabhu (2024), an independent systematic review.
DOIs were checked on 2026-10-10: the review's reference list gives a wrong DOI for Sujeeth et al. (a hyperacusis paper),
the correct one is used here; the Yektatalab et al. DOI is registered with mEDRA, not Crossref.

Run: .venv/Scripts/python.exe papers/misophonia-prevalence/search/recall.py --date 2026-10-10
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from dedup import norm_title

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    recs = [json.loads(line) for line in (run / "records_unique.jsonl").open(encoding="utf-8")]
    seeds = list(csv.DictReader((HERE / "seed_set.csv").open(encoding="utf-8")))
    rows = []
    for s in seeds:
        doi, nt = s["doi"].lower(), norm_title(s["title"])
        hit = next((r for r in recs if doi in (r.get("all_dois") or "").lower().split(";")), None) \
            or next((r for r in recs if norm_title(r["title"]).startswith(nt[:60])), None)
        rows.append({"study": s["study"], "year": s["year"], "doi": s["doi"], "found": bool(hit),
                     "rec_id": hit["rec_id"] if hit else "", "sources": hit["sources"] if hit else "",
                     "to_screen": bool(hit) and not hit["auto_removed"]})
    found = sum(r["to_screen"] for r in rows)
    report = {"run": a.date, "seed_studies": len(rows), "in_screening_list": found, "studies": rows}
    (run / "recall_seed_set.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    for r in rows:
        print(f"{'OK ' if r['to_screen'] else 'MISS'} {r['study']} {r['year']}  {r['rec_id']}  {r['sources']}")
    print(f"recall: {found} of {len(rows)}")


if __name__ == "__main__":
    main()
