"""Converts exports of the manual searches into the raw record format of search.py (protocol, section 9).

Put the exports into search/runs/<date>/manual/ and run this script before dedup.py. The source is read
from the file name prefix:
  scholar_*.html  Google Scholar result pages saved from the browser (search/SCHOLAR_PAGES.md: num=20, 10 pages a query);
  scholar_*.csv   Google Scholar via Publish or Perish ("Save as CSV"), if used instead;
  scielo_*.ris / scielo_*.csv / scielo_*.txt   SciELO Search (RIS or CSV export, or the page text);
  bvs_*.ris / bvs_*.csv     LILACS through the BVS portal, if it can be reached;
  hand_*.csv      records found by hand (columns title, year, first_author, venue, doi, url, abstract).
Each source gets one file raw/<source>.jsonl with every record of all its exports, in file order;
the files are listed in raw/manual_import_log.json with their SHA-256.

Run: .venv/Scripts/python.exe papers/misophonia-prevalence/search/import_manual.py --date 2026-10-10
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = ["scholar", "scielo", "bvs", "hand"]
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>]+)", re.I)


def norm_doi(d: str | None) -> str:
    d = (d or "").strip().lower()
    for p in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "doi:"):
        if d.startswith(p):
            d = d[len(p):]
    return d.rstrip(".,;)")


def rec(source: str, n: int, *, title="", abstract="", year="", venue="", first_author="", doi="", url="",
        type_="", language="") -> dict:
    return {"source": source, "source_id": f"{source}:{n}", "pmid": "", "doi": norm_doi(doi),
            "title": " ".join((title or "").split()), "abstract": " ".join((abstract or "").split()),
            "year": str(year or "")[:4], "venue": venue or "", "first_author": first_author or "",
            "type": type_ or "", "language": language or "", "url": url or ""}


def read_ris(path: Path) -> list[dict]:
    out, cur = [], defaultdict(list)
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", line)
        if not m:
            continue
        tag, val = m.groups()
        if tag == "ER":
            out.append(dict(cur))
            cur = defaultdict(list)
        else:
            cur[tag].append(val.strip())
    if cur:
        out.append(dict(cur))
    rows = []
    for r in out:
        first = lambda *tags: next((r[t][0] for t in tags if r.get(t)), "")  # noqa: E731
        doi = first("DO") or next((m.group(1) for v in r.get("UR", []) + r.get("L2", []) for m in [DOI_RE.search(v)] if m), "")
        rows.append({"title": first("TI", "T1", "CT", "BT"), "abstract": " ".join(r.get("AB", []) or r.get("N2", [])),
                     "year": (first("PY", "Y1", "DA") or "")[:4], "venue": first("JO", "JF", "T2", "PB"),
                     "first_author": first("AU", "A1").split(",")[0], "doi": doi, "url": first("UR", "L2"),
                     "type_": first("TY"), "language": first("LA")})
    return rows


def read_csv(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    dialect = csv.Sniffer().sniff(text[:5000], delimiters=",;\t")
    rows = []
    for r in csv.DictReader(text.splitlines(), dialect=dialect):
        r = {(k or "").strip().lower(): (v or "").strip() for k, v in r.items()}
        get = lambda *ks: next((r[k] for k in ks if r.get(k)), "")  # noqa: E731
        authors = get("authors", "author", "first_author", "au")
        rows.append({"title": get("title", "ti"), "abstract": get("abstract", "ab"), "year": get("year", "py"),
                     "venue": get("source", "journal", "venue", "publisher"),
                     "first_author": re.split(r"[,;]", authors)[0].strip().split(" ")[-1] if authors else "",
                     "doi": get("doi") or next((m.group(1) for m in [DOI_RE.search(get("articleurl", "url", "fulltexturl"))] if m), ""),
                     "url": get("articleurl", "url", "link"), "type_": get("type"), "language": get("language", "la")})
    return rows


def read_scielo_text(path: Path) -> list[dict]:
    """SciELO Search result page as plain text (browser get_page_text): numbered records with a DOI line."""
    t = path.read_text(encoding="utf-8")
    rows = []
    for block in re.split(r"\n\s*(?=\d+\.\s{1,3}\S)", t)[1:]:
        lines = [x.strip() for x in block.splitlines() if x.strip()]
        title = re.sub(r"^\d+\.\s+", "", lines[0])
        authors = lines[2] if len(lines) > 2 else ""
        venue_line = next((x for x in lines if re.search(r"\b(19|20)\d{2}\b", x) and ("Volume" in x or "vol" in x.lower())), "")
        year = (re.search(r"\b(19|20)\d{2}\b", venue_line) or re.search(r"\b(19|20)\d{2}\b", block)).group(0)
        doi = next((m.group(1) for m in [DOI_RE.search(block)] if m), "")
        rows.append({"title": title, "first_author": authors.split(",")[0].strip(), "year": year,
                     "venue": re.split(r"\s+(?:[a-z]{3}\s+)?(?:19|20)\d{2}", venue_line)[0], "doi": doi})
    return rows


def read_scholar_html(path: Path) -> list[dict]:
    """A Google Scholar result page saved from the browser (20 results with num=20)."""
    t = path.read_text(encoding="utf-8", errors="replace")
    # inline tags (bold search terms) go without a space, so "<b>Prevalence</b>," stays "Prevalence,"
    strip = lambda x: html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"</?(?:b|i|em|strong|sup|sub)\b[^>]*>", "", x or "")))  # noqa: E731
    rows = []
    for chunk in re.split(r'<div class="gs_ri">', t)[1:]:
        h3 = re.search(r'<h3 class="gs_rt"[^>]*>(.*?)</h3>', chunk, re.S)
        if not h3:
            continue
        link = re.search(r'href="([^"]+)"', h3.group(1))
        title = re.sub(r"^\s*(\[[A-Z]+\]\s*)+", "", " ".join(strip(h3.group(1)).split()))
        meta = " ".join(strip((re.search(r'<div class="gs_a"[^>]*>(.*?)</div>', chunk, re.S) or [None, ""])[1]).split())
        snippet = " ".join(strip((re.search(r'<div class="gs_rs"[^>]*>(.*?)</div>', chunk, re.S) or [None, ""])[1]).split())
        parts = [x.strip() for x in meta.split(" - ")]
        year = re.search(r"\b(19|20)\d{2}\b", meta)
        url = html.unescape(link.group(1)) if link else ""
        doi = next((m.group(1) for m in [DOI_RE.search(url)] if m), "")
        rows.append({"title": title, "abstract": snippet, "year": year.group(0) if year else "",
                     "venue": re.sub(r",?\s*(19|20)\d{2}$", "", parts[1]).strip() if len(parts) > 1 else "",
                     "first_author": parts[0].split(",")[0].strip().split(" ")[-1] if parts and parts[0] else "",
                     "doi": doi, "url": url, "type_": "google scholar result"})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    manual, raw = run / "manual", run / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    log = {}
    for src in SOURCES:
        files = sorted(p for p in manual.glob(f"{src}_*") if p.is_file())
        if not files:
            continue
        recs = []
        for p in files:
            if p.suffix.lower() == ".ris":
                rows = read_ris(p)
            elif p.suffix.lower() == ".csv":
                rows = read_csv(p)
            elif p.suffix.lower() in (".html", ".htm") and src == "scholar":
                rows = read_scholar_html(p)
            elif p.suffix.lower() == ".txt" and src == "scielo":
                rows = read_scielo_text(p)
            else:
                raise SystemExit(f"unsupported file: {p.name}")
            for r in rows:
                if r.get("title"):
                    recs.append(rec(src, len(recs) + 1, **r))
            log[p.name] = {"source": src, "records": len(rows),
                           "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
        with (raw / f"{src}.jsonl").open("w", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{src}: {len(recs)} records from {len(files)} file(s)")
    (raw / "manual_import_log.json").write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
