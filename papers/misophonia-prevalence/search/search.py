"""Automated searches for the misophonia prevalence meta-analysis (protocol, sections 9-10).

Runs every automated search and writes the raw records to
search/runs/<date>/raw/<source>.jsonl and the run log (query strings, record
counts, timestamps) to search/runs/<date>/search_log.json. dedup.py then merges
duplicates and builds the screening list.

Sources:
  pubmed     PubMed (E-utilities), PUBMED_QUERY; journal and book records;
  europepmc  Europe PMC including preprints, EPMC_QUERY;
  openalex   OpenAlex, title-and-abstract search, OPENALEX_TERMS;
  s2         Semantic Scholar bulk search, S2_QUERY;
  datacite   DataCite REST API (theses, posters, repository deposits), DATACITE_QUERY;
  openaire   OpenAIRE Graph API (repository publications, theses), OPENAIRE_QUERIES;
  core       CORE API v3 (open-access repository records), CORE_TERMS;
  citations  OpenAlex: every record citing a development paper of ten misophonia
             instruments (INSTRUMENT_DOIS).
Manual sources (SciELO, LILACS/BVS, Google Scholar via Publish or Perish) are converted
by import_manual.py into the same raw format.

Run:  .venv/Scripts/python.exe papers/misophonia-prevalence/search/search.py [sources...] [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
from datetime import date, datetime, timezone
from pathlib import Path

import httpx
from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

# ---------------------------------------------------------------- query strings
PUBMED_QUERY = (
    'misophonia[All Fields] OR misophon*[tw] OR "selective sound sensitivity"[tw] OR misokinesia[tw] '
    'OR "decreased sound tolerance"[tw] OR "sound intolerance"[tw] OR "sound tolerance disorder*"[tw] '
    'OR "misophonia"[Supplementary Concept]'
)
EPMC_QUERY = (
    '(TITLE_ABS:misophon* OR KW:misophon* OR TITLE_ABS:"selective sound sensitivity" OR TITLE_ABS:misokinesia '
    'OR TITLE_ABS:"decreased sound tolerance" OR TITLE_ABS:"sound intolerance" OR TITLE_ABS:"sound tolerance disorder" '
    'OR TITLE_ABS:"sound tolerance disorders" OR TITLE_ABS:misofonia OR TITLE_ABS:mizofoni OR TITLE_ABS:misophonie)'
)
OPENALEX_TERMS = [
    "misophonia", "misophonic", "misophonics", '"selective sound sensitivity"', "misokinesia",
    '"decreased sound tolerance"', '"sound intolerance"', '"sound tolerance disorder"', '"sound tolerance disorders"',
    "misofonia", "misofonía", "mizofoni", "misophonie", "мизофония", "ミソフォニア", "미소포니아",
]
S2_QUERY = (
    'misophonia | misophonic | "selective sound sensitivity" | misokinesia | "decreased sound tolerance" '
    '| "sound intolerance" | misofonia | mizofoni | misophonie'
)
_DC_TERMS = ('(misophon* OR misofon* OR mizofon* OR "selective sound sensitivity" OR misokinesia '
             'OR "decreased sound tolerance" OR "sound intolerance" OR "sound tolerance disorder" '
             'OR "sound tolerance disorders")')
DATACITE_QUERY = f"titles.title:{_DC_TERMS} OR descriptions.description:{_DC_TERMS} OR subjects.subject:{_DC_TERMS}"
# OpenAIRE allows at most four OR operators per query: the terms are split into three queries.
OPENAIRE_QUERIES = [
    "misophonia OR misophonic OR misofonia OR misofonía OR mizofoni",
    'misophonie OR misokinesia OR "selective sound sensitivity" OR "decreased sound tolerance" OR "sound intolerance"',
    '"sound tolerance disorder" OR "sound tolerance disorders"',
]
# CORE rejects OR lists inside field queries: one title-or-abstract query per term.
CORE_TERMS = ["misophonia", "misophonic", "misofonia", "misofonía", "mizofoni", "misophonie", "misokinesia",
              '"selective sound sensitivity"', '"decreased sound tolerance"', '"sound intolerance"',
              '"sound tolerance disorder"', '"sound tolerance disorders"']
# Development papers of misophonia instruments: whoever measured misophonia almost always cites one of them.
INSTRUMENT_DOIS = {
    "A-MISO-S (Schröder et al., 2013)": "10.1371/journal.pone.0054706",
    "MQ (Wu et al., 2014)": "10.1002/jclp.22098",
    "AMISOS-R (Jager et al., 2020)": "10.1371/journal.pone.0231390",
    "MisoQuest (Siepsiak et al., 2020)": "10.3390/ijerph17051797",
    "S-Five (Vitoratou et al., 2021)": "10.3390/psych3040041",
    "DMQ (Rosenthal et al., 2021)": "10.3389/fpsyg.2021.709928",
    "BMQ-R (Remmert et al., 2022)": "10.1371/journal.pone.0269428",
    "DVMSQ (Williams et al., 2022)": "10.3389/fpsyg.2022.897901",
    "SMS-Adolescent (Rinaldi et al., 2022)": "10.3389/fpsyg.2022.808379",
    "SMS-Adult (Simner et al., 2024)": "10.1177/10731911241234104",
}
# The consensus definition (Swedo et al., 2022, 10.3389/fnins.2022.841816) is not in the set: it is widely
# cited as a Delphi exemplar, and all 22 pilot records that arrived only through it were off-topic.

UA = "misophonia-prevalence-search/1.0 (mailto:mrexert@gmail.com)"


def load_env() -> dict[str, str]:
    env = {}
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


ENV = load_env()
client = httpx.Client(headers={"User-Agent": UA}, timeout=90, follow_redirects=True)


def get(url: str, params: dict | None = None, tries: int = 6, **kw) -> httpx.Response:
    last = None
    for i in range(tries):
        try:
            r = client.get(url, params=params, **kw)
        except httpx.HTTPError as e:  # network
            last = e
            time.sleep(3 * (i + 1))
            continue
        if r.status_code == 200:
            return r
        last = r
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(3 * (i + 1))
            continue
        r.raise_for_status()
    raise RuntimeError(f"GET failed: {url} {params} -> {last}")


def inv_to_text(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def norm_doi(d: str | None) -> str:
    d = (d or "").strip().lower()
    for p in ("https://doi.org/", "http://doi.org/", "doi:"):
        if d.startswith(p):
            d = d[len(p):]
    return d


# ---------------------------------------------------------------- sources
def pubmed() -> tuple[list[dict], dict]:
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    r = get(base + "esearch.fcgi", {"db": "pubmed", "term": PUBMED_QUERY, "retmax": 10000, "retmode": "json"})
    es = r.json()["esearchresult"]
    ids = es["idlist"]
    out = []
    for i in range(0, len(ids), 200):
        x = get(base + "efetch.fcgi", {"db": "pubmed", "id": ",".join(ids[i:i + 200]), "retmode": "xml"}).content
        root = etree.fromstring(x)
        for art in root.findall(".//PubmedArticle"):
            pmid = art.findtext(".//MedlineCitation/PMID")
            title = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
            abstract = " ".join("".join(a.itertext()) for a in art.findall(".//Abstract/AbstractText"))
            doi = ""
            for aid in art.findall(".//PubmedData/ArticleIdList/ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = aid.text or ""
            year = art.findtext(".//JournalIssue/PubDate/Year") or (art.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]
            au = art.find(".//AuthorList/Author")
            first = (au.findtext("LastName") or au.findtext("CollectiveName") or "") if au is not None else ""
            out.append({
                "source": "pubmed", "source_id": f"PMID:{pmid}", "pmid": pmid, "doi": norm_doi(doi), "title": title,
                "abstract": abstract, "year": year, "venue": art.findtext(".//Journal/Title") or "",
                "first_author": first, "type": ";".join(p.text or "" for p in art.findall(".//PublicationType")),
                "language": ";".join(l.text or "" for l in art.findall(".//Language")),
            })
        # Book chapters (e.g., StatPearls) come as PubmedBookArticle; the pilot parser dropped them (480 hits, 478 records).
        for art in root.findall(".//PubmedBookArticle"):
            pmid = art.findtext(".//BookDocument/PMID")
            node = art.find(".//BookDocument/ArticleTitle")
            if node is None:
                node = art.find(".//BookDocument/Book/BookTitle")
            title = "".join(node.itertext()) if node is not None else ""
            abstract = " ".join("".join(a.itertext()) for a in art.findall(".//BookDocument/Abstract/AbstractText"))
            au = art.find(".//BookDocument/AuthorList/Author")
            first = (au.findtext("LastName") or au.findtext("CollectiveName") or "") if au is not None else ""
            out.append({
                "source": "pubmed", "source_id": f"PMID:{pmid}", "pmid": pmid, "doi": "", "title": title,
                "abstract": abstract,
                "year": art.findtext(".//BookDocument/Book/PubDate/Year") or "",
                "venue": art.findtext(".//BookDocument/Book/BookTitle") or "",
                "first_author": first,
                "type": ";".join(p.text or "" for p in art.findall(".//BookDocument/PublicationType")) or "Book Chapter",
                "language": ";".join(l.text or "" for l in art.findall(".//BookDocument/Language")),
            })
        time.sleep(0.4)
    return out, {"query": PUBMED_QUERY, "translation": es.get("querytranslation"), "count": int(es["count"])}


def europepmc() -> tuple[list[dict], dict]:
    out, cursor, hit = [], "*", None
    while True:
        r = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search", {
            "query": EPMC_QUERY, "format": "json", "pageSize": 1000, "cursorMark": cursor, "resultType": "core",
        })
        d = r.json()
        hit = d.get("hitCount")
        res = d.get("resultList", {}).get("result", [])
        for it in res:
            out.append({
                "source": "europepmc", "source_id": f"{it.get('source')}:{it.get('id')}", "pmid": it.get("pmid") or "",
                "doi": norm_doi(it.get("doi")), "title": it.get("title", ""), "abstract": it.get("abstractText", ""),
                "year": it.get("pubYear", ""),
                "venue": ((it.get("journalInfo") or {}).get("journal") or {}).get("title")
                or ((it.get("bookOrReportDetails") or {}).get("publisher")) or "",
                "first_author": (it.get("authorString") or "").split(",")[0].split(" ")[0],
                "type": ";".join((it.get("pubTypeList") or {}).get("pubType", [])) + f"|src={it.get('source')}",
                "language": it.get("language", ""),
            })
        nxt = d.get("nextCursorMark")
        # Europe PMC returns a new cursor even after the last page, so stop on hitCount
        if not res or nxt == cursor or len(out) >= (hit or 0):
            break
        cursor = nxt
    return out, {"query": EPMC_QUERY, "count": hit}


def _openalex_page(filter_str: str) -> list[dict]:
    out, cursor = [], "*"
    while cursor:
        r = get("https://api.openalex.org/works", {
            "filter": filter_str, "per_page": 200, "cursor": cursor, "api_key": ENV["OPENALEX_API_KEY"],
            "select": "id,doi,title,publication_year,type,primary_location,abstract_inverted_index,authorships,ids,language,cited_by_count",
        })
        d = r.json()
        out.extend(d["results"])
        cursor = d["meta"].get("next_cursor") if d["results"] else None
    return out


def _openalex_rec(w: dict, source: str, extra: dict | None = None) -> dict:
    loc = w.get("primary_location") or {}
    auth = w.get("authorships") or []
    rec = {
        "source": source, "source_id": w["id"].replace("https://openalex.org/", ""),
        "pmid": ((w.get("ids") or {}).get("pmid") or "").replace("https://pubmed.ncbi.nlm.nih.gov/", ""),
        "doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "abstract": inv_to_text(w.get("abstract_inverted_index")),
        "year": w.get("publication_year"), "venue": (loc.get("source") or {}).get("display_name") or "",
        "first_author": ((auth[0].get("author") or {}).get("display_name") or "").split(" ")[-1] if auth else "",
        "type": w.get("type") or "", "language": w.get("language") or "",
    }
    if extra:
        rec.update(extra)
    return rec


def openalex() -> tuple[list[dict], dict]:
    flt = "title_and_abstract.search:" + "|".join(OPENALEX_TERMS)
    raw = _openalex_page(flt)
    return [_openalex_rec(w, "openalex") for w in raw], {"filter": flt, "count": len(raw)}


def citations() -> tuple[list[dict], dict]:
    out, meta = [], {}
    for label, doi in INSTRUMENT_DOIS.items():
        r = get(f"https://api.openalex.org/works/doi:{doi}", {"api_key": ENV["OPENALEX_API_KEY"], "select": "id,cited_by_count"})
        wid = r.json()["id"].split("/")[-1]
        raw = _openalex_page(f"cites:{wid}")
        meta[label] = {"doi": doi, "openalex": wid, "citing_records": len(raw)}
        out.extend(_openalex_rec(w, "citations", {"cites": label}) for w in raw)
    return out, meta


def semantic_scholar() -> tuple[list[dict], dict]:
    out, token = [], None
    fields = "title,year,externalIds,publicationTypes,venue,abstract,authors"
    while True:
        params = {"query": S2_QUERY, "fields": fields}
        if token:
            params["token"] = token
        r = None
        for i in range(10):
            r = client.get("https://api.semanticscholar.org/graph/v1/paper/search/bulk", params=params)
            if r.status_code == 200:
                break
            time.sleep(4 * (i + 1))
        if r is None or r.status_code != 200:
            raise RuntimeError(f"S2 failed: {r.status_code if r is not None else None}")
        d = r.json()
        for it in d.get("data", []):
            ext = it.get("externalIds") or {}
            out.append({
                "source": "s2", "source_id": f"S2:{it.get('paperId')}", "pmid": str(ext.get("PubMed") or ""),
                "doi": norm_doi(ext.get("DOI")), "title": it.get("title") or "", "abstract": it.get("abstract") or "",
                "year": it.get("year"), "venue": it.get("venue") or "",
                "first_author": ((it.get("authors") or [{}])[0].get("name") or "").split(" ")[-1] if it.get("authors") else "",
                "type": ";".join(it.get("publicationTypes") or []), "language": "",
            })
        token = d.get("token")
        if not token:
            break
        time.sleep(1.5)
    return out, {"query": S2_QUERY, "count": len(out)}


def datacite() -> tuple[list[dict], dict]:
    """DataCite DOIs: theses, posters and other repository deposits that Crossref-based indexes miss.

    Added on 2026-10-10, before registration: the author's Google Scholar check found a 2025 University of Surrey
    thesis (10.15126/thesis.901519) that is registered with DataCite but absent from the five pilot sources.
    """
    out, raw = [], []
    url, params = "https://api.datacite.org/dois", {"query": DATACITE_QUERY, "page[size]": 1000, "page[cursor]": 1}
    total = None
    while url:
        d = get(url, params).json()
        total = (d.get("meta") or {}).get("total", total)
        raw.extend(d.get("data", []))
        url = (d.get("links") or {}).get("next")
        params = None
    for it in raw:
        a = it["attributes"]
        types = a.get("types") or {}
        descs = [dd for dd in a.get("descriptions") or [] if isinstance(dd.get("description"), str)]
        abstract = next((dd["description"] for dd in descs if dd.get("descriptionType") == "Abstract"), "") \
            or " ".join(dd["description"] for dd in descs)
        creator = (a.get("creators") or [{}])[0] if a.get("creators") else {}
        publisher = a.get("publisher")
        container = (a.get("container") or {}).get("title")
        out.append({
            "source": "datacite", "source_id": f"DataCite:{(a.get('doi') or '').lower()}", "pmid": "",
            "doi": norm_doi(a.get("doi")),
            "title": " ".join(t.get("title", "") for t in (a.get("titles") or [])[:1]),
            "abstract": abstract[:5000], "year": a.get("publicationYear") or "",
            "venue": container or (publisher.get("name") if isinstance(publisher, dict) else publisher) or "",
            "first_author": creator.get("familyName") or (creator.get("name") or "").split(",")[0],
            "type": f"{types.get('resourceTypeGeneral') or ''}/{types.get('resourceType') or ''}",
            "language": a.get("language") or "",
        })
    return out, {"query": DATACITE_QUERY, "count": total}


def openaire() -> tuple[list[dict], dict]:
    """OpenAIRE Graph API: publications harvested from repositories (theses, conference objects, preprints).

    Replaces BASE and OATD, whose web interfaces block automated access (bot checks) and could not be opened by
    the author either; BASE's own API requires IP registration. The API allows at most four OR operators per
    query, so OPENAIRE_QUERIES split the terms; the results are pooled.
    """
    out, meta = [], {}
    for q in OPENAIRE_QUERIES:
        cursor, n, found = "*", 0, None
        while cursor:
            d = get("https://api.openaire.eu/graph/v1/researchProducts",
                    {"search": q, "type": "publication", "pageSize": 100, "cursor": cursor}).json()
            head = d.get("header") or {}
            found = head.get("numFound", found)
            res = d.get("results") or []
            for w in res:
                pids = {(p.get("scheme") or "").lower(): p.get("value") for p in (w.get("pids") or [])}
                inst = w.get("instances") or []
                for i in inst:
                    for p in (i.get("pids") or []) + (i.get("alternateIdentifiers") or []):
                        pids.setdefault((p.get("scheme") or "").lower(), p.get("value"))
                auth = (w.get("authors") or [{}])[0] if w.get("authors") else {}
                container = (w.get("container") or {}).get("name")
                out.append({
                    "source": "openaire", "source_id": f"OpenAIRE:{w.get('id')}", "pmid": str(pids.get("pmid") or ""),
                    "doi": norm_doi(pids.get("doi")), "title": w.get("mainTitle") or "",
                    "abstract": " ".join(w.get("descriptions") or [])[:5000],
                    "year": (w.get("publicationDate") or "")[:4], "venue": container or w.get("publisher") or "",
                    "first_author": auth.get("surname") or (auth.get("fullName") or "").split(",")[0],
                    "type": "; ".join(sorted({i.get("type") for i in inst if i.get("type")})) or w.get("type") or "",
                    "language": (w.get("language") or {}).get("code") or "",
                    "url": next((u for i in inst for u in (i.get("urls") or [])), ""),
                })
            n += len(res)
            cursor = head.get("nextCursor") if res else None
            time.sleep(1)
        meta[q] = {"numFound": found, "retrieved": n}
    return out, {"type": "publication", "queries": meta}


def _fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()


def term_in(term: str, text: str) -> bool:
    """True if the (possibly quoted) term occurs as a word or phrase; case, accents and plural endings ignored."""
    words = _fold(term.strip('"')).split()
    pattern = r"\b" + r"\s+".join(re.escape(w) for w in words) + r"\w*"
    return re.search(pattern, _fold(text)) is not None


def core() -> tuple[list[dict], dict]:
    """CORE API v3: open-access full texts and metadata from repositories, searched in title and abstract.

    Without a key CORE allows 100 tokens a day (a field query costs several); a free academic key (CORE_API_KEY in
    .env) allows 5,000 a day. Both allow at most 10 requests a minute, so the client paces itself and honours 429.
    CORE matches phrases loosely (in the 2026-10-10 run many hits lacked the term), so, as the registered query
    says "term in title or abstract", only records whose title or abstract contains the term are kept.
    """
    out, meta = [], {}
    headers = {"Authorization": f"Bearer {ENV['CORE_API_KEY']}"} if ENV.get("CORE_API_KEY") else {}
    for term in CORE_TERMS:
        q = f"title:{term} OR abstract:{term}"
        offset, total, dropped = 0, None, 0
        while True:
            for attempt in range(10):
                r = client.get("https://api.core.ac.uk/v3/search/works/", headers=headers,
                               params={"q": q, "limit": 100, "offset": offset, "exclude": "fullText"})
                if r.status_code == 200:
                    break
                # about ten requests per window without a key; the 429 names the moment to retry
                until = r.headers.get("x-ratelimit-retry-after")
                try:
                    wait = (datetime.fromisoformat(until.replace("+0000", "+00:00")) - datetime.now(timezone.utc)).total_seconds() + 5
                except (AttributeError, ValueError):
                    wait = 30 * (attempt + 1)
                print(f"core: HTTP {r.status_code}, waiting {max(wait, 5):.0f} s", flush=True)
                time.sleep(min(max(wait, 5), 1200))
            else:
                raise RuntimeError(f"CORE failed for {q!r} at offset {offset}: {r.status_code} {r.text[:200]}")
            d = r.json()
            total = d.get("totalHits", total)
            res = d.get("results") or []
            for w in res:
                if not term_in(term, f"{w.get('title') or ''} {w.get('abstract') or ''}"):
                    dropped += 1
                    continue
                auth = (w.get("authors") or [{}])[0] if w.get("authors") else {}
                journals = w.get("journals") or []
                out.append({
                    "source": "core", "source_id": f"CORE:{w.get('id')}", "pmid": str(w.get("pubmedId") or ""),
                    "doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "abstract": (w.get("abstract") or "")[:5000],
                    "year": w.get("yearPublished") or "",
                    "venue": (journals[0].get("title") if journals else "") or w.get("publisher") or "",
                    "first_author": (auth.get("name") or "").split(",")[0].split(" ")[-1],
                    "type": w.get("documentType") or "", "language": ((w.get("language") or {}).get("code") or ""),
                    "url": w.get("downloadUrl") or "",
                })
            offset += len(res)
            time.sleep(7)
            if not res or offset >= (total or 0):
                break
        meta[q] = {"totalHits": total, "retrieved": offset, "dropped_term_not_in_title_or_abstract": dropped}
    return out, {"queries": meta, "authenticated": bool(headers)}


SOURCES = {"pubmed": pubmed, "europepmc": europepmc, "openalex": openalex, "s2": semantic_scholar,
           "datacite": datacite, "openaire": openaire, "core": core, "citations": citations}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="*", default=list(SOURCES))
    ap.add_argument("--date", default=date.today().isoformat())
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    (run / "raw").mkdir(parents=True, exist_ok=True)
    log_path = run / "search_log.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    for name in a.sources:
        t0 = time.time()
        try:
            recs, meta = SOURCES[name]()
        except Exception as e:  # noqa: BLE001
            print(f"{name}: FAILED {e!r}", file=sys.stderr, flush=True)
            log[name] = {"error": repr(e), "at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
            continue
        with (run / "raw" / f"{name}.jsonl").open("w", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        log[name] = {"records": len(recs), "meta": meta,
                     "searched_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "seconds": round(time.time() - t0, 1)}
        print(f"{name}: {len(recs)} records", flush=True)
        log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")   # after every source


if __name__ == "__main__":
    main()
