"""Retractions and expressions of concern for the eligible reports (protocol §11c, "Checks").

Crossref carries the Retraction Watch data: a retracted or corrected work lists the notices in "updated-by", and
notices point back with "update-to". For every eligible report with a DOI this script reads the Crossref record
and writes extraction/retraction_check.csv (rec_id, doi, crossref status, updates found).
Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/retraction_check.py --run 2026-10-10
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import date
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
EMAIL = "mrexert@gmail.com"
sys.path.insert(0, str(HERE))
from common import eligible_reports, load_records  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = load_records(a.run)
    ft = eligible_reports()
    client = httpx.Client(timeout=30, follow_redirects=True,
                          headers={"User-Agent": f"misophonia-prevalence/1.0 (mailto:{EMAIL})"})
    rows = []
    for k in sorted(ft):
        doi = (recs[k].get("doi") or "").strip()
        if not doi:
            rows.append({"rec_id": k, "doi": "", "crossref": "no DOI", "updates": ""})
            continue
        r = client.get(f"https://api.crossref.org/works/{doi}", params={"mailto": EMAIL})
        if r.status_code != 200:
            rows.append({"rec_id": k, "doi": doi, "crossref": f"HTTP {r.status_code} (DOI not registered with Crossref)",
                         "updates": ""})
            continue
        m = r.json()["message"]
        ups = []
        for u in m.get("updated-by", []) or []:
            ups.append(f"{u.get('type')} by {u.get('DOI')} ({u.get('source', '')})")
        for rel, items in (m.get("relation") or {}).items():
            if any(w in rel for w in ("retract", "concern", "correct")):
                ups += [f"{rel}: {i.get('id')}" for i in items]
        rows.append({"rec_id": k, "doi": doi, "crossref": "found", "updates": "; ".join(ups)})
        time.sleep(0.1)
    out = HERE / "retraction_check.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["rec_id", "doi", "crossref", "updates"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    flagged = [r for r in rows if r["updates"]]
    print(f"checked {len(rows)} reports on {date.today()}: Crossref records {sum(r['crossref'] == 'found' for r in rows)}, "
          f"with updates {len(flagged)}")
    for r in flagged:
        print(" ", r["rec_id"], r["doi"], "->", r["updates"])


if __name__ == "__main__":
    main()
