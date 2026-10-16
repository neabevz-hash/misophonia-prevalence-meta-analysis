"""Records for full-text assessment from the citation search (protocol §9; deviations.md, 2026-10-15).

citation_chase.py found the works citing or cited by the included studies that the main search had not found; none
had a condition term in the title or abstract. The OpenAlex full-text search for the condition terms selected those
whose full text mentions misophonia (fulltext_hits.jsonl). This script gives them record IDs R2001, R2002, ... (in
OpenAlex ID order) in the record format of the main search and writes records_unique.jsonl in the same run folder,
so that fetch_oa.py, ft_screen.py and ft_md.py can process them like the main records.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/search/chase_records.py --run 2026-10-15-citations
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIRST_ID = 2001


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.run
    hits = [json.loads(l) for l in (run / "fulltext_hits.jsonl").open(encoding="utf-8")]
    hits.sort(key=lambda r: r["source_id"])
    out = []
    for i, h in enumerate(hits):
        out.append({
            "rec_id": f"R{FIRST_ID + i}", "title": h["title"], "abstract": h.get("abstract", ""), "year": h.get("year"),
            "first_author": h.get("first_author", ""), "venue": h.get("venue", ""), "doi": h.get("doi", ""),
            "all_dois": h.get("doi", ""), "pmid": h.get("pmid", ""), "types": f"openalex:{h.get('type', '')}",
            "language": h.get("language", ""), "sources": h["source"], "n_sources": 1,
            "source_ids": h["source_id"], "url": f"https://doi.org/{h['doi']}" if h.get("doi") else
            f"https://openalex.org/{h['source_id']}", "fulltext_terms": ";".join(h.get("fulltext_terms", [])),
        })
    with (run / "records_unique.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(out)} records: {out[0]['rec_id']}..{out[-1]['rec_id']} -> {run / 'records_unique.jsonl'}")


if __name__ == "__main__":
    main()
