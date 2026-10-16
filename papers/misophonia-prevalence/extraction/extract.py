"""AI extraction and risk-of-bias drafts (protocol §11c, §14): Claude Opus 5.5 fills the extraction form for every job.

Reads the fixed prompt from extract_prompt.md, Table 1 from forms/instrument_thresholds.csv, the rules G1-G12 from
forms/table1_completion.md and the jobs from jobs.json (make_study_map.py). Appends one JSON line per job to
extraction/draft/<name>.jsonl (resumable). The drafts are stored unchanged; R1 verifies every value.

Run (pilot): .venv/Scripts/python.exe papers/misophonia-prevalence/extraction/extract.py --run 2026-10-10 --name pilot_2026-10-15 --only R1062 R0998 R0236 R0766 R0446
Run (all):   .venv/Scripts/python.exe papers/misophonia-prevalence/extraction/extract.py --run 2026-10-10 --name extract_<date>
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))

from llmaudit.judge import Judge, judge_all  # noqa: E402

sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402

SEED = 20261015
MAX_CHARS = 400_000  # per report; jobs.json keeps the attached reports within this budget


def blocks(md: str) -> list[tuple[str, str]]:
    return re.findall(r"```(\w*)\n(.*?)```", md, re.S)


def field(enum: list[str] | None = None) -> dict:
    value = {"type": "string", "maxLength": 400}
    if enum:
        value = {"type": "string", "enum": enum}
    return {"type": "object",
            "properties": {"value": value, "loc": {"type": "string", "maxLength": 160},
                           "quote": {"type": "string", "maxLength": 600}},
            "required": ["value", "loc", "quote"], "additionalProperties": False}


def text_(n: int) -> dict:
    return {"type": "string", "maxLength": n}


def build_schema(spec: dict) -> dict:
    sf = spec["sample_fields"]
    en = spec["estimate_enums"]
    jbi_item = {"type": "object",
                "properties": {"rating": {"type": "string", "enum": spec["jbi_ratings"]}, "reason": text_(400),
                               "loc": text_(160), "quote": text_(600)},
                "required": ["rating", "reason", "loc", "quote"], "additionalProperties": False}
    jbi = {"type": "object", "properties": {f"jbi_{i}": jbi_item for i in range(1, 10)},
           "required": [f"jbi_{i}" for i in range(1, 10)], "additionalProperties": False}
    est_props = {
        "subgroup": text_(120), "instrument": {"type": "string", "enum": en["instrument"]}, "threshold": text_(300),
        "threshold_source": {"type": "string", "enum": en["threshold_source"]}, "author_label": text_(200),
        "level": {"type": "string", "enum": en["level"]}, "table1_rule": text_(200),
        "time_frame": {"type": "string", "enum": en["time_frame"]}, "cases": text_(40), "n": text_(40),
        "derived": {"type": "string", "enum": en["derived"]}, "derivation": text_(300), "weighted_pct": text_(40),
        "primary_for_authors": {"type": "string", "enum": en["primary_for_authors"]}, "location": text_(160),
        "quote": text_(600), "note": text_(500),
    }
    est = {"type": "object", "properties": est_props, "required": list(est_props), "additionalProperties": False}
    s_props = {"label": text_(200), "reports": text_(300),
               **{k: field(v) for k, v in sf.items()},
               "notes": text_(1000), "jbi": jbi, "estimates": {"type": "array", "maxItems": 40, "items": est}}
    sample = {"type": "object", "properties": s_props, "required": list(s_props), "additionalProperties": False}
    top = {"samples": {"type": "array", "maxItems": 12, "items": sample}, "excluded_samples": text_(1000),
           "consistency_notes": text_(2000), "note": text_(1000)}
    return {"type": "object", "properties": top, "required": list(top), "additionalProperties": False}


def load_prompt() -> tuple[str, str, str, dict]:
    md = (HERE / "extract_prompt.md").read_text(encoding="utf-8")
    b = blocks(md)
    system = next(body for lang, body in b if lang == "" and body.startswith("You are extracting"))
    preamble = next(body for lang, body in b if lang == "" and body.startswith("EXTRACTION FORM"))
    job_tpl = next(body for lang, body in b if lang == "" and body.startswith("TABLE 1"))
    spec = json.loads(next(body for lang, body in b if lang == "json"))
    return system.strip(), preamble, job_tpl, build_schema(spec)


def table1_text() -> str:
    rows = list(csv.DictReader((PAPER / "forms" / "instrument_thresholds.csv").open(encoding="utf-8")))
    out = []
    for r in rows:
        out.append(f"- {r['instrument']} ({r['full_name']}); range {r['score_range'] or 'NA'}; "
                   f"L1: {r['L1_rule'] or 'none'}; L2: {r['L2_rule'] or 'none'}; source: {r['threshold_source'] or 'NA'}; "
                   f"notes: {r['notes'] or 'none'}")
    return "\n".join(out)


def rules_text() -> str:
    md = (PAPER / "forms" / "table1_completion.md").read_text(encoding="utf-8")
    sec = md.split("## General rules", 1)[1].split("\n## ", 1)[0]
    return sec.strip().replace("**", "")


def report_text(k: str) -> str:
    raw = (PAPER / "fulltext" / "text" / f"{k}.txt").read_text(encoding="utf-8")
    return raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--only", nargs="*", help="job ids (main rec_ids) to process")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--concurrency", type=int, default=3)
    a = ap.parse_args()
    system, preamble, job_tpl, schema = load_prompt()
    recs = load_records(a.run)
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    t1, rules = table1_text(), rules_text()
    items = []
    for j in jobs:
        if a.only and j["job_id"] not in a.only:
            continue
        main_rec = recs[j["main"]]
        main_text = report_text(j["main"])
        links = []
        if j["link_reason"]:
            links.append(f"Linked reports: {j['link_reason']}")
        if j["attached"]:
            links.append("Attached below (use them only to fill values the main report does not give, or to note "
                         f"differences): {', '.join(j['attached'])}")
        if j["listed_only"]:
            links.append(f"Other reports of these samples, not attached (too long): {', '.join(j['listed_only'])}")
        for po in j["possible_overlap"]:
            links.append(f"Note for the sample notes: {po}")
        if j.get("job_notes"):
            links.append(f"Note for the sample notes: {j['job_notes']}")
        att = []
        for e in j["attached"]:
            u = recs[e]
            t = report_text(e)
            att.append(f"\nATTACHED REPORT {e}\nTitle: {u['title']}\nYear: {u.get('year')}; venue: {u.get('venue')}; "
                       f"DOI: {u.get('doi') or 'none'}\nFull text ({len(t):,} characters):\n{t[:MAX_CHARS]}")
        body = job_tpl.format(
            table1=t1, rules=rules, job_id=j["job_id"], study_id=j["study_id"], samples=j["samples"],
            links="\n".join(links), main_id=j["main"], main_title=main_rec["title"], main_year=main_rec.get("year"),
            main_venue=main_rec.get("venue"), main_doi=main_rec.get("doi") or "none", main_chars=f"{len(main_text):,}",
            main_truncated=f"; cut to the first {MAX_CHARS:,} characters" if len(main_text) > MAX_CHARS else "",
            main_text=main_text[:MAX_CHARS], attached="\n".join(att))
        items.append({"conv_id": j["job_id"], "prompt": preamble + "\n" + body})

    # One job can hold several samples with many subgroup estimates (a two-sample pilot job used 28.6k output tokens).
    judge = Judge(system_prompt=system, schema=schema, model="claude-opus-5-5", effort="high", timeout=2400,
                  extra_env={"CLAUDE_CODE_MAX_OUTPUT_TOKENS": "64000"})
    out = HERE / "draft" / f"{a.name}.jsonl"
    asyncio.run(judge_all(items, lambda it: it["prompt"], judge, out, concurrency=a.concurrency, seed=SEED,
                          limit=a.limit))


if __name__ == "__main__":
    main()
