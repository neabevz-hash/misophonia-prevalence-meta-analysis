"""Verified extraction -> the two analysis tables of the protocol (forms/samples.csv, forms/estimates.csv).

Reads R1's verified values (extraction/decisions/samples_R1.csv and estimates_R1.csv, written by verify_md.py parse),
the drafts (for the JBI reasons), the study map and the record metadata, and writes the tables in the codebook's
format: sample_id S###, study_id ST###, report_ids (main report first), first author, year and DOI of the main report,
continent, WHO region and World Bank income group from analysis/country_lookup.csv, and estimate_id E####.
Dropped samples and deleted estimates are left out. By default only samples R1 marked verified are written.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/finalize.py --run 2026-10-10 --draft extract_<date>
     (--in DIR / --out DIR / --allow-unverified for code tests on unverified drafts)
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402

SAMPLE_COLS = ["sample_id", "study_id", "report_ids", "first_author", "year", "doi", "pub_status", "language", "country",
               "continent", "who_region", "income_group", "setting", "data_years", "design", "sampling",
               "topic_disclosed", "population", "clinical_group", "inclusion_exclusion", "n_invited", "n_responded",
               "n_analysed", "response_rate", "age_mean", "age_sd", "age_min", "age_max", "age_group", "pct_female",
               "informant", "mode", "instruments", "instrument_validated_in_language", "funding_coi",
               "jbi_1", "jbi_2", "jbi_3", "jbi_4", "jbi_5", "jbi_6", "jbi_7", "jbi_8", "jbi_9", "jbi_notes",
               "contact_author", "notes", "sample_key", "label", "income_basis"]
EST_COLS = ["estimate_id", "sample_id", "subgroup", "instrument", "threshold", "threshold_source", "author_label",
            "level", "table1_rule", "time_frame", "cases", "n", "derived", "weighted_pct", "primary_for_authors",
            "location", "notes"]
REC = re.compile(r"R\d{4}")


def income_for(iso3: str, data_years: str, pub_year, history: dict, current: str) -> tuple[str, str]:
    """World Bank group in force from July of the first year of data collection (fiscal year = that year + 1, set on
    the previous year's GNI); without a data year, the publication year minus 1. Beyond the last fiscal year of the
    historical file, the current classification of the World Bank API."""
    y = first_year(data_years)
    basis = "data year"
    if not y:
        try:
            y, basis = str(int(pub_year) - 1), "publication year - 1"
        except (TypeError, ValueError):
            return "", "no year"
    fy = int(y) + 1
    if (iso3, fy) in history:
        return history[(iso3, fy)], f"FY{fy % 100:02d} ({basis} {y})"
    last = max((f for (c, f) in history if c == iso3), default=None)
    if last is not None and fy > last and current:
        return current, f"current classification (FY{fy % 100:02d} not in OGHIST; {basis} {y})"
    return "", f"no classification for FY{fy % 100:02d}"


def first_year(data_years: str) -> str:
    m = re.search(r"(19|20)\d{2}", data_years or "")
    return m.group(0) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--draft", required=True)
    ap.add_argument("--in", dest="inp", default=str(HERE / "decisions"))
    ap.add_argument("--out", default=str(PAPER / "forms"))
    ap.add_argument("--allow-unverified", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    recs = load_records(a.run)
    drafts = {}
    for line in (HERE / "draft" / f"{a.draft}.jsonl").open(encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            drafts[d["conv_id"]] = d
    lookup = {}
    lp = PAPER / "analysis" / "country_lookup.csv"
    if lp.exists():
        lookup = {r["iso3"]: r for r in csv.DictReader(lp.open(encoding="utf-8"))}
    history = {}
    hp = PAPER / "analysis" / "data" / "wb_income_history.csv"
    if hp.exists():
        history = {(r["iso3"], int(r["fiscal_year"])): r["group"] for r in csv.DictReader(hp.open(encoding="utf-8"))}
    inp = Path(a.inp)
    samples = list(csv.DictReader((inp / "samples_R1.csv").open(encoding="utf-8")))
    ests = list(csv.DictReader((inp / "estimates_R1.csv").open(encoding="utf-8")))
    # JBI reasons from the drafts, by sample key order inside each job
    reasons = {}
    notes_ai = {}
    count = {}
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    for j in sorted(jobs, key=lambda x: (x["study_id"], x["job_id"])):
        d = drafts.get(j["job_id"])
        if not d:
            continue
        for s in d["codes"]["samples"]:
            count[j["study_id"]] = count.get(j["study_id"], 0) + 1
            reasons[f"{j['study_id']}-{count[j['study_id']]}"] = {i: s["jbi"][f"jbi_{i}"] for i in range(1, 10)}
            notes_ai[f"{j['study_id']}-{count[j['study_id']]}"] = s.get("notes", "")

    out_s, out_e, skipped = [], [], []
    sid = {}
    for s in samples:
        if s["dropped"]:
            skipped.append(f"{s['sample_key']} dropped by R1: {s['dropped']}")
            continue
        if s["verified"] != "yes" and not a.allow_unverified:
            skipped.append(f"{s['sample_key']} not verified")
            continue
        sid[s["sample_key"]] = f"S{len(sid) + 1:03d}"
        reps = list(dict.fromkeys(REC.findall(s["reports"]))) or [s["job_id"]]
        if s["job_id"] in reps:
            reps.remove(s["job_id"])
        reps = [s["job_id"], *reps]
        main = recs[s["job_id"]]
        c = (s["country"] or "").strip().upper()
        lk = lookup.get(c, {})
        notes_jbi = []
        for i in range(1, 10):
            r = s[f"jbi_{i}"]
            if r in ("no", "unclear"):
                ai = reasons.get(s["sample_key"], {}).get(i, {})
                why = ai.get("reason", "") if ai.get("rating") == r else "rating set by R1"
                notes_jbi.append(f"{i}: {r} - {why}")
        income, basis = income_for(c, s.get("data_years", ""), main.get("year"), history, lk.get("income_group", ""))
        out_s.append({
            **{k: s.get(k, "") for k in SAMPLE_COLS if k in s},
            "sample_id": sid[s["sample_key"]], "study_id": s["study_id"], "report_ids": ";".join(reps),
            "first_author": main.get("first_author") or "", "year": main.get("year") or "", "doi": main.get("doi") or "",
            "continent": lk.get("continent", "multi" if c.startswith("MULTI") else ""),
            "who_region": lk.get("who_region", ""),
            "income_group": income,
            "jbi_notes": " | ".join(notes_jbi),
            "contact_author": "not contacted (deviations.md, 2026-10-11)",
            "notes": " | ".join(x for x in (notes_ai.get(s["sample_key"], ""), s.get("r1_comments", "")) if x),
            "sample_key": s["sample_key"], "label": s["label"], "income_basis": basis,
        })
    for e in ests:
        if e["sample_key"] not in sid:
            continue
        out_e.append({"estimate_id": f"E{len(out_e) + 1:04d}", "sample_id": sid[e["sample_key"]],
                      **{k: e.get(k, "") for k in EST_COLS if k in e and k not in ("estimate_id", "sample_id")},
                      "notes": e.get("note", "")})
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, cols, rows in (("samples.csv", SAMPLE_COLS, out_s), ("estimates.csv", EST_COLS, out_e)):
        with (out / name).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
    missing_lk = sorted({r["country"] for r in out_s if r["country"] and not r["continent"]})
    print(f"samples {len(out_s)}, estimates {len(out_e)} -> {out}; skipped {len(skipped)}")
    if missing_lk:
        print("countries without lookup:", ", ".join(missing_lk))


if __name__ == "__main__":
    main()
