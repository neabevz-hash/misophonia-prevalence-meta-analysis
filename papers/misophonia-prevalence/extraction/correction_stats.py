"""Share of AI-drafted values R1 corrected (protocol §11c), overall, for the key items and by field.

Compares the stored drafts with R1's corrections (extraction/decisions/corrections_R1.csv, from verify_md.py parse).
Denominator: every drafted value of the verified samples - the sample fields, the nine JBI ratings and the estimate
fields. Key items: n_analysed, population, sampling (samples) and instrument, threshold, level, cases, n (estimates).
A deleted estimate counts as one corrected key value; an added estimate as one missed key value.
Writes extraction/decisions/correction_stats.json.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/correction_stats.py --draft extract_<date>
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_md import EST_FIELDS, KEY_EST, KEY_SAMPLE, SAMPLE_FIELDS  # noqa: E402

# Estimate fields that carry a value R1 checks (location, quote and note are evidence, not data).
EST_DATA = [f for f in EST_FIELDS if f not in ("location", "quote", "note", "derivation", "table1_rule")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    ap.add_argument("--dec", help="folder of the parsed decisions (default extraction/decisions)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    dec = Path(a.dec) if a.dec else HERE / "decisions"
    samples = list(csv.DictReader((dec / "samples_R1.csv").open(encoding="utf-8")))
    ests = list(csv.DictReader((dec / "estimates_R1.csv").open(encoding="utf-8")))
    corr = list(csv.DictReader((dec / "corrections_R1.csv").open(encoding="utf-8"))) if (dec / "corrections_R1.csv").exists() else []
    verified = {s["sample_key"] for s in samples if s["verified"] == "yes" and not s["dropped"]}
    n_est_drafted = sum(1 for e in ests if e["sample_key"] in verified and e["est"].startswith("E")) + \
        sum(1 for c in corr if c["sample_key"] in verified and c["r1_value"] == "deleted")
    total = len(verified) * (len(SAMPLE_FIELDS) + 9) + n_est_drafted * len(EST_DATA)
    key_total = len(verified) * len(KEY_SAMPLE) + n_est_drafted * len(KEY_EST)
    c_ver = [c for c in corr if c["sample_key"] in verified and c["field"] not in ("location", "quote", "note", "derivation", "table1_rule")]
    changed = [c for c in c_ver if c["target"] != "new"]
    key_changed = [c for c in changed if c["key_field"] == "yes"]
    added = [c for c in c_ver if c["target"] == "new"]
    by_field = Counter((c["target"] if c["target"] in ("sample",) or c["target"].startswith("jbi") else "estimate", c["field"])
                       for c in changed)
    out = {
        "verified_samples": len(verified), "drafted_estimates": n_est_drafted,
        "drafted_values": total, "values_corrected": len(changed),
        "share_corrected": round(len(changed) / total, 4) if total else None,
        "key_values": key_total, "key_values_corrected": len(key_changed),
        "share_key_corrected": round(len(key_changed) / key_total, 4) if key_total else None,
        "estimates_added_by_R1": len(added),
        "by_field": {f"{t}.{f}": n for (t, f), n in by_field.most_common()},
    }
    (dec / "correction_stats.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
                                               newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
