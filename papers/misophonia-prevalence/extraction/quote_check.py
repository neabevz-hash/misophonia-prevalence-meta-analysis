"""Are the AI's quotes in the source? An automatic audit of the extraction drafts.

For every estimate and every key sample field (n_analysed, population, sampling) of the drafts, the quote is searched
in the full texts of the job (main and attached reports) after normalisation: case, whitespace, punctuation and
hyphenation are ignored, an ellipsis ("...", "…") splits a quote into fragments that must all be found, and English
translations in square brackets are removed. A quote counts as found when every fragment of at least 12 characters
occurs in the text. Table rows ("a | b | c") are matched cell by cell. Writes extraction/decisions/quote_check.json
and lists quotes not found.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/quote_check.py --draft extract_2026-10-15
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent


def norm(t: str) -> str:
    """Letters and digits only: spacing, punctuation, line-end hyphens and PDF spacing between characters vanish."""
    t = unicodedata.normalize("NFKC", t or "").lower()
    return re.sub(r"[\W_]+", "", t)


def fragments(q: str) -> list[str]:
    q = re.sub(r"\[[^\]]*\]", " ", q)          # translations in brackets
    parts = re.split(r"\.\.\.|…|\s\|\s|\|", q)
    return [norm(p) for p in parts if len(norm(p)) >= 10]


def text_of(rec: str) -> str:
    p = PAPER / "fulltext" / "text" / f"{rec}.txt"
    return norm(p.read_text(encoding="utf-8", errors="replace")) if p.exists() else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    jobs = {j["job_id"]: j for j in json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))}
    cache: dict[str, str] = {}
    stats = {"estimates": [0, 0, 0], "key_fields": [0, 0, 0]}   # quotes checked, found, not checkable (too short)
    missing = []
    for line in (HERE / "draft" / f"{a.draft}.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        j = jobs[d["conv_id"]]
        recs = [j["main"], *j["attached"], *j["listed_only"]]
        for r in recs:
            cache.setdefault(r, text_of(r))
        hay = " ".join(cache[r] for r in recs)
        for s in d["codes"]["samples"]:
            items = [("estimates", f"E{i}", e["quote"]) for i, e in enumerate(s["estimates"], 1)]
            items += [("key_fields", f, s[f]["quote"]) for f in ("n_analysed", "population", "sampling")]
            for kind, what, q in items:
                fr = fragments(q)
                if not fr:
                    stats[kind][2] += 1
                    continue
                stats[kind][0] += 1
                if all(f in hay for f in fr):
                    stats[kind][1] += 1
                else:
                    lost = [f for f in fr if f not in hay]
                    missing.append({"job": d["conv_id"], "sample": s["label"][:80], "item": what, "quote": q[:300],
                                    "not_found": lost[0][:160]})
    out = {k: {"quotes_checked": v[0], "found_verbatim": v[1], "too_short_to_check": v[2],
               "share_found": round(v[1] / v[0], 4) if v[0] else None} for k, v in stats.items()}
    out["not_found"] = missing
    dec = HERE / "decisions"
    dec.mkdir(exist_ok=True)
    (dec / "quote_check.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
                                          newline="\n")
    print(json.dumps({k: v for k, v in out.items() if k != "not_found"}, indent=1))
    print(f"not found: {len(missing)}")
    for m in missing[:40]:
        print(f"  {m['job']} {m['item']} | {m['not_found']}")


if __name__ == "__main__":
    main()
