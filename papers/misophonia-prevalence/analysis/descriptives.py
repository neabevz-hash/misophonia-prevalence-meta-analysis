"""Descriptive statistics of the included studies for the Results (from the verified tables forms/*.csv).

Writes analysis/results/descriptives.json: studies, samples, participants, countries, continents, populations,
sampling, publication types, years of publication and data collection, instruments of the whole-sample estimates,
estimates by level, JBI ratings per item, AI audit numbers.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/analysis/descriptives.py
"""
from __future__ import annotations

import csv
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent


def num(x):
    try:
        return float(str(x).replace(",", ""))
    except ValueError:
        return None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    s = list(csv.DictReader((PAPER / "forms" / "samples.csv").open(encoding="utf-8")))
    e = list(csv.DictReader((PAPER / "forms" / "estimates.csv").open(encoding="utf-8")))
    whole = [x for x in e if x["subgroup"].strip().lower() in ("all", "total", "whole sample")]
    countries = Counter()
    for x in s:
        for c in re.findall(r"\b[A-Z]{3}\b", x["country"].upper()):
            if c not in ("MULTI", "NR"):
                countries[c] += 1
    n_an = [num(x["n_analysed"]) for x in s]
    years_pub = [int(x["year"]) for x in s if str(x["year"]).isdigit()]
    years_data = [int(m.group(0)) for x in s if (m := re.search(r"(19|20)\d{2}", x["data_years"] or ""))]
    out = {
        "studies": len({x["study_id"] for x in s}), "samples": len(s),
        "participants": int(sum(v for v in n_an if v)), "median_n": statistics.median([v for v in n_an if v]),
        "samples_country_NR": sum(1 for x in s if x["country"] in ("NR", "")),
        "samples_multi_country": sum(1 for x in s if x["country"].upper().startswith("MULTI")),
        "countries": len(countries), "samples_by_country": dict(countries.most_common()),
        "samples_by_continent": dict(Counter(x["continent"] or "NR" for x in s).most_common()),
        "samples_by_population": dict(Counter(x["population"] for x in s).most_common()),
        "clinical_groups": dict(Counter(x["clinical_group"] for x in s if x["population"] == "clinical").most_common()),
        "samples_by_sampling": dict(Counter(x["sampling"] for x in s).most_common()),
        "samples_by_pub_status": dict(Counter(x["pub_status"] for x in s).most_common()),
        "samples_by_age_group": dict(Counter(x["age_group"] for x in s).most_common()),
        "samples_by_mode": dict(Counter(x["mode"] for x in s).most_common()),
        "topic_disclosed": dict(Counter(x["topic_disclosed"] for x in s).most_common()),
        "publication_years": [min(years_pub), max(years_pub)], "data_years": [min(years_data), max(years_data)],
        "estimates": len(e), "whole_sample_estimates": len(whole),
        "estimates_by_level": dict(Counter(x["level"] for x in e).most_common()),
        "whole_sample_estimates_by_level": dict(Counter(x["level"] for x in whole).most_common()),
        "whole_sample_estimates_by_instrument": dict(Counter(x["instrument"] for x in whole).most_common()),
        "jbi_yes_by_item": {f"jbi_{i}": dict(Counter(x[f"jbi_{i}"] for x in s)) for i in range(1, 10)},
    }
    for name in ("correction_stats.json", "quote_check.json"):
        p = PAPER / "extraction" / "decisions" / name
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            d.pop("not_found", None)
            out[name.replace(".json", "")] = {k: v for k, v in d.items() if k != "by_field"}
    (HERE / "results" / "descriptives.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8", newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
