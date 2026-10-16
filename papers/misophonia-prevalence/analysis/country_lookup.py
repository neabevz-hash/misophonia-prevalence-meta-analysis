"""Country lookup for the samples table: UN M49 continent, WHO region, World Bank income group.

Codebook: continent by the UN M49 geoscheme, WHO region, and the World Bank income group of the country in the year of
data collection, all filled automatically from the ISO 3166 alpha-3 country code. Sources, read through their APIs:
- UN M49 continental regions: UN Statistics Division SDG API, GeoArea tree "World (total) by continental regions";
- WHO regions: WHO Global Health Observatory OData API, dimension COUNTRY (ParentCode = region);
- World Bank income group: World Bank API v2 country list (the current classification; historical groups by year
  need the World Bank's OGHIST file, see the note column).
The ISO numeric codes in ISO_NUM are checked against the UN tree: the script stops if a code is missing there.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/analysis/country_lookup.py --draft extract_<date>
Writes analysis/country_lookup.csv for every country in the extraction drafts.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
# ISO 3166-1 alpha-3 -> numeric (= UN M49 code of the country); extend when a new country appears.
ISO_NUM = {
    "AUS": 36, "AUT": 40, "BRA": 76, "CAN": 124, "CHN": 156, "DEU": 276, "EGY": 818, "ESP": 724, "FRA": 250,
    "GBR": 826, "IND": 356, "IRL": 372, "IRN": 364, "ITA": 380, "JPN": 392, "KOR": 410, "NLD": 528, "NOR": 578,
    "NPL": 524, "NZL": 554, "PAK": 586, "POL": 616, "PRT": 620, "SAU": 682, "SRB": 688, "SWE": 752, "TUR": 792,
    "USA": 840, "BEL": 56, "CHE": 756, "DNK": 208, "FIN": 246, "GRC": 300, "ISR": 376, "MEX": 484, "NGA": 566,
    "RUS": 643, "SGP": 702, "ZAF": 710, "ARE": 784, "JOR": 400, "LBN": 422, "MYS": 458, "IDN": 360, "TWN": 158,
    "HKG": 344, "CZE": 203, "HUN": 348, "ROU": 642, "UKR": 804, "ARG": 32, "CHL": 152, "COL": 170, "PER": 604,
    "IRQ": 368, "KAZ": 398, "BGD": 50, "LKA": 144, "VNM": 704, "THA": 764, "PHL": 608,
}
CONTINENTS = {2: "Africa", 19: "Americas", 142: "Asia", 9: "Oceania", 150: "Europe", 10: "Antarctica"}


def draft_countries(draft: str) -> set[str]:
    out = set()
    for line in (PAPER / "extraction" / "draft" / f"{draft}.jsonl").open(encoding="utf-8"):
        if not line.strip():
            continue
        for s in json.loads(line)["codes"]["samples"]:
            v = s["country"]["value"].upper()
            out.update(re.findall(r"\b[A-Z]{3}\b", v))
    return out - {"MULTI", "NR", "NA"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    c = httpx.Client(timeout=60, follow_redirects=True,
                     headers={"User-Agent": "misophonia-prevalence/1.0 (mailto:mrexert@gmail.com)"})
    countries = sorted(draft_countries(a.draft))
    missing = [k for k in countries if k not in ISO_NUM]
    if missing:
        raise SystemExit(f"add ISO numeric codes for: {', '.join(missing)}")
    tree = c.get("https://unstats.un.org/sdgapi/v1/sdg/GeoArea/Tree").json()
    cont_root = next(r for r in tree if r["geoAreaName"] == "World (total) by continental regions")
    continent_of, names = {}, {}

    def walk(node, cont):
        for ch in node.get("children") or []:
            if ch["type"] == "Country":
                continent_of[ch["geoAreaCode"]] = cont
                names[ch["geoAreaCode"]] = ch["geoAreaName"]
            walk(ch, cont)

    for top in cont_root["children"]:
        walk(top, CONTINENTS.get(top["geoAreaCode"], top["geoAreaName"]))
    who = {v["Code"]: v for v in c.get("https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues").json()["value"]}
    wb = {x["id"]: x for x in c.get("https://api.worldbank.org/v2/country", params={"format": "json", "per_page": 400}).json()[1]}
    rows = []
    for k in countries:
        num = ISO_NUM[k]
        if num not in continent_of:
            raise SystemExit(f"{k}: M49 code {num} not in the UN continental tree")
        rows.append({"iso3": k, "m49": num, "un_name": names[num], "continent": continent_of[num],
                     "who_region": who.get(k, {}).get("ParentCode", ""),
                     "income_group": {"High income": "high", "Upper middle income": "upper-middle",
                                      "Lower middle income": "lower-middle", "Low income": "low"}.get(
                                          wb.get(k, {}).get("incomeLevel", {}).get("value", ""), ""),
                     "note": f"WHO GHO and UN SDG APIs, World Bank API v2 current classification, read {date.today()}"})
    out = HERE / "country_lookup.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r["iso3"], r["un_name"], r["continent"], r["who_region"], r["income_group"])


if __name__ == "__main__":
    main()
