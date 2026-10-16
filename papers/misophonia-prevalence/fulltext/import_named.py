"""Match full texts R1 saved under the publisher's file name to the reports that are still missing.

Looks at every file in a folder whose name is not <rec_id>.pdf (PDF or Word), reads its first pages, and matches it
to a not-yet-retrieved report by a DOI printed in the text, else by the report's title. Byte-identical copies of files
already imported are skipped. Matched files are copied to fulltext/manual/<rec_id>.<ext>; then run
fetch_oa.py --import-manual. Nothing is matched by guesswork: unmatched files are listed for R1.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/fulltext/import_named.py --run 2026-10-10 --folder <folder>
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>,;]+)", re.I)


def compact(t: str | None) -> str:
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", t)


def read_text(p: Path) -> str:
    if p.suffix.lower() == ".pdf":
        import pymupdf
        doc = pymupdf.open(str(p))
        return "\n".join(doc[i].get_text() for i in range(min(3, doc.page_count)))
    if p.suffix.lower() == ".docx":
        from docx import Document
        d = Document(str(p))
        return "\n".join(par.text for par in d.paragraphs[:200])
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--folder", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in
            (PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")}
    log = {r["rec_id"]: r for r in csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig"))}
    missing = [k for k, r in log.items() if r["status"] != "retrieved"]
    known = {r["sha256"] for r in log.values() if r["sha256"]}
    by_doi = {}
    for k in missing:
        for d in (recs[k].get("all_dois") or "").split(";"):
            if d:
                by_doi[d.lower().rstrip(".")] = k
    (HERE / "manual").mkdir(exist_ok=True)
    for p in sorted(Path(a.folder).iterdir()):
        if not p.is_file() or re.fullmatch(r"R\d{4,5}\.pdf", p.name) or p.suffix.lower() not in (".pdf", ".docx"):
            continue
        data = p.read_bytes()
        if hashlib.sha256(data).hexdigest() in known:
            print(f"SAME AS AN IMPORTED FILE, skipped: {p.name}")
            continue
        text = read_text(p)
        hit = next((by_doi[d.lower().rstrip(".)")] for d in DOI_RE.findall(text) if d.lower().rstrip(".)") in by_doi), None)
        how = "doi"
        if not hit:
            body = compact(text) + compact(p.stem)
            cands = [k for k in missing if len(compact(recs[k]["title"])) >= 30 and compact(recs[k]["title"])[:45] in body]
            hit, how = (cands[0], "title") if len(cands) == 1 else (None, f"title ({len(cands)} candidates)")
        if hit:
            dest = HERE / "manual" / f"{hit}{p.suffix.lower()}"
            shutil.copy2(p, dest)
            print(f"{p.name} -> {hit} by {how} | {recs[hit]['title'][:80]}")
        else:
            print(f"NOT MATCHED ({how}): {p.name}")


if __name__ == "__main__":
    main()
