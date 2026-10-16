"""Manuscript tables from the analysis results (analysis/results/*.csv), so that the text never retypes a number.

Table 1 - case-definition levels (forms/instrument_thresholds.csv, compact);
Table 2 - pooled prevalence: primary outcome, each case-definition level, population types, age groups, continents,
          clinical groups (k, participants, prevalence with 95% CI and 95% prediction interval, tau-squared), with the
          test of subgroup differences; strata with fewer than three samples list their estimates;
Table 3 - sensitivity analyses of the primary outcome;
Table 4 - summary of findings with the GRADE rating (protocol section 17; rules in the table note).
Writes manuscript/tables.md.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/manuscript/make_tables.py [--results DIR]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent

POPTYPE = {"gp_probability": "probability general population", "gp_other": "other general population",
           "university_students": "university students", "medical_students": "university students",
           "school_pupils": "school children and adolescents", "workers": "other non-clinical",
           "other_nonclinical": "other non-clinical"}
AGEGRP = {"children": "children (<13)", "adolescents": "adolescents (13-17)", "adults": "adults"}
LABEL = {"other general population": "Other general population", "probability general population":
         "Probability samples, general population", "university students": "University students",
         "school children and adolescents": "School children and adolescents", "other non-clinical": "Other non-clinical",
         "adolescents (13-17)": "Adolescents (13–17 years)", "adults": "Adults", "mixed or NR": "Mixed ages or not reported",
         "Americas": "Americas", "Asia": "Asia", "Europe": "Europe", "other": "Other",
         "autism": "Autism", "depression": "Depression", "mixed_psychiatric": "Mixed psychiatric",
         "Level L1": "L1, symptom level", "Level L2": "L2, clinically significant", "Level L3": "L3, diagnosed by interview"}


def pct(x) -> str:
    try:
        return f"{100 * float(x):.1f}"
    except (TypeError, ValueError):
        return "–"


def p_txt(p: float) -> str:
    return "p < 0.001" if p < 0.001 else f"p = {p:.3f}"


def membership(s: dict) -> dict:
    """The subgroup codes of the analysis script (analysis.R, samples mutate) for one sample."""
    cont = s["continent"]
    return {"poptype": POPTYPE.get(s["population"], "clinical"),
            "agegrp": AGEGRP.get(s["age_group"], "mixed or NR"),
            "contgrp": cont if cont in ("Asia", "Europe", "Americas") else ("other" if cont in ("Africa", "Oceania") else None),
            "clin": re.sub(r"[ :(].*$", "", s["clinical_group"]) if s["population"] == "clinical" else None}


def author(s: dict) -> str:
    a = s["first_author"]
    return (a.title() if a.isupper() else a) + " " + s["year"]


def listed(analysis: str, log: list[dict], samples: dict) -> str:
    """Estimates of a stratum with fewer than three samples: 'Author year (detail) %'."""
    if analysis.startswith("Level "):
        key, rows = None, [r for r in log if r["analysis"] == "level " + analysis.split()[1]]
    elif analysis.startswith("Clinical group: "):
        key, rows = ("clin", analysis.split(": ", 1)[1]), [r for r in log if r["analysis"] == "clinical L2/L3"]
    else:
        var, val = analysis[len("Primary by "):].split(": ", 1)
        key, rows = (var, val), [r for r in log if r["analysis"] == "primary L2/L3"]
    out = []
    for r in rows:
        s = samples[r["sample_id"]]
        if key and membership(s)[key[0]] != key[1]:
            continue
        detail = ""
        if key and key[0] == "clin" and key[1] == "other":
            detail = " (" + re.sub(r"\s*\(.*$", "", s["clinical_group"].split(":", 1)[-1]).strip() + ")"
        out.append(f"{author(s)}{detail} {100 * float(r['cases']) / float(r['n']):.1f}")
    return "; ".join(out)


def row(r: dict, label: str, log=None, samples=None) -> str:
    if r["prev"] in ("", "NA"):
        est = listed(r["analysis"], log, samples) if log else "not pooled"
        return f"| {label} | {r['k']} | {int(float(r['n_total'] or 0)):,} | not pooled: {est} | | |"
    return (f"| {label} | {r['k']} | {int(float(r['n_total'])):,} | {pct(r['prev'])} "
            f"({pct(r['ci.lb'])}–{pct(r['ci.ub'])}) | {pct(r['pi.lb'])}–{pct(r['pi.ub'])} | {float(r['tau2']):.2f} |")


def grade_rows(res: Path) -> list[str]:
    """Summary of findings. Start: high certainty (event rates from observational studies; Iorio et al., 2015); one
    level down for each serious domain, by the rules printed in the table note."""
    g = list(csv.DictReader((res / "grade_inputs.csv").open(encoding="utf-8")))
    levels = ["High", "Moderate", "Low", "Very low"]
    out = []
    for r in g:
        f = {k: float(v) if v not in ("", "NA") else None for k, v in r.items() if k not in ("outcome", "measure")}
        prev = r["measure"] == "prevalence"
        why = []
        if f["weight_any_no"] > 0.5:
            why.append(f"risk of bias ({100 * f['weight_any_no']:.0f}% of weight rated no on JBI 2, 6 or 9)")
        if prev and f["pi.lb"] < 0.05 and f["pi.ub"] > 0.20 or not prev and f["pi.lb"] < 1 < f["pi.ub"]:
            why.append("inconsistency (prediction interval " + (f"{pct(f['pi.lb'])}–{pct(f['pi.ub'])}%" if prev else
                                                             f"{f['pi.lb']:.2f}–{f['pi.ub']:.2f}") + ")")
        if prev and (f["ci.ub"] - f["ci.lb"]) / 2 > 0.05 or not prev and f["ci.lb"] < 1 < f["ci.ub"]:
            why.append("imprecision (" + (f"CI half-width {100 * (f['ci.ub'] - f['ci.lb']) / 2:.1f} points" if prev
                                          else "CI includes 1") + ")")
        if f["countries"] < 5 or f["continents"] < 3:
            why.append(f"indirectness ({int(f['countries'])} countries, {int(f['continents'])} continents)")
        if f["small_study_p"] is not None and f["small_study_p"] < 0.10:
            why.append(f"publication bias (small-study regression p = {f['small_study_p']:.2f})")
        cert = levels[min(len(why), 3)]
        est = (f"{pct(f['estimate'])}% ({pct(f['ci.lb'])}–{pct(f['ci.ub'])})" if prev else
               f"OR {f['estimate']:.2f} ({f['ci.lb']:.2f}–{f['ci.ub']:.2f})")
        pi = f"{pct(f['pi.lb'])}–{pct(f['pi.ub'])}%" if prev else f"{f['pi.lb']:.2f}–{f['pi.ub']:.2f}"
        out.append(f"| {r['outcome']} | {int(f['k'])} ({int(f['participants']):,}) | {est} | {pi} | {cert} | "
                   f"{'; '.join(why) or 'none'} |")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default=str(PAPER / "analysis" / "results"))
    ap.add_argument("--out", default=str(HERE / "tables.md"))
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    res = Path(a.results)
    pooled = list(csv.DictReader((res / "pooled.csv").open(encoding="utf-8")))
    sens = list(csv.DictReader((res / "sensitivity.csv").open(encoding="utf-8")))
    tests = {r["moderator"]: r for r in csv.DictReader((res / "subgroup_tests.csv").open(encoding="utf-8"))}
    log = list(csv.DictReader((res / "selection_log.csv").open(encoding="utf-8")))
    samples = {s["sample_id"]: s for s in csv.DictReader((PAPER / "forms" / "samples.csv").open(encoding="utf-8"))}
    head = ["| Analysis | Samples (k) | Participants | Prevalence, % (95% CI) | 95% PI, % | τ² (logit) |",
            "| --- | --- | --- | --- | --- | --- |"]
    t1 = list(csv.DictReader((PAPER / "forms" / "instrument_thresholds.csv").open(encoding="utf-8")))
    short_src = {
        "A-MISO-S": "Schröder et al. (2013); Möllmann et al. (2023)", "MQ": "Wu et al. (2014); Möllmann et al. (2023)",
        "MisoQuest": "Siepsiak et al. (2020)", "S-Five": "Vitoratou et al. (2023)", "SMS-Adult": "Simner et al. (2024)",
        "SMS-Adolescent": "Rinaldi et al. (2022)", "DVMSQ": "Williams et al. (2022)", "DMQ": "Rosenthal et al. (2021)",
        "AMISOS-R": "Möllmann et al. (2023); Cakiroglu et al. (2022)", "MAQ": "Aryal and Prabhu (2022); Möllmann et al. (2023)",
        "DSTS-S": "Allusoglu and Aksoy (2022)", "MSL-CY": "Rappoldt et al. (2026)", "SSSQ4": "Aazh et al. (2022)",
        "SSfM": "Rinaldi and Simner (2025)"}
    L = ["# Tables", "", "**Table 1.** Case-definition levels: thresholds for L1 (symptom level) and L2 (clinically significant) "
         "by instrument, set before extraction from development and validation papers (full version with notes: "
         "Supplementary File S2).", "",
         "| Instrument | L1 | L2 | Source |", "| --- | --- | --- | --- |"]
    for r in t1:
        if r["instrument"] in ("NYMS", "BMQ-R", "interview", "adhoc"):
            continue
        L.append(f"| {r['instrument']} | {r['L1_rule']} | {r['L2_rule']} | {short_src.get(r['instrument'], '')} |".replace(">=", "≥"))
    L += ["| Interview | — | — | L3: interview applying explicit diagnostic criteria (e.g., Schröder et al., 2013; Swedo et al., 2022) |",
          "| Ad hoc items | self-identification, self-reported diagnosis, frequency (\"often\" or more), intensity, symptom counts | "
          "only if both the misophonic reaction and distress or impairment are required | rules of Supplementary File S2 |",
          "", "Any bothersome sound or trigger without severity is L0 (described, not pooled); cut-offs from the same sample's "
          "distribution (E3) are listed, not pooled. Where an instrument has several L2 thresholds, the first is the "
          "recommended one used for the primary estimate.", "",
          "**Table 2.** Pooled prevalence of misophonia (random-effects binomial–normal generalized linear mixed models, "
          "logit scale).", ""]
    L += head
    L += [row(r, "**Clinically significant (L2/L3), non-clinical samples**") for r in pooled
          if r["analysis"] == "Primary: L2/L3, non-clinical"]
    L.append("| *By case-definition level, non-clinical samples* | | | | | |")
    L += [row(r, "  " + LABEL[r["analysis"].replace(" non-clinical", "")], log, samples) for r in pooled
          if r["analysis"].startswith("Level ")]
    for prefix, var, title in (("Primary by poptype: ", "poptype", "By population type (L2/L3)"),
                               ("Primary by agegrp: ", "agegrp", "By age group (L2/L3)"),
                               ("Primary by contgrp: ", "contgrp", "By continent (L2/L3)"),
                               ("Clinical group: ", None, "Clinical samples, by diagnosis (L2/L3)")):
        rows = [r for r in pooled if r["analysis"].startswith(prefix)]
        if not rows:
            continue
        t = tests.get(var) if var else None
        test = (f"; difference between subgroups: Q = {float(t['QM']):.1f}, df = {t['df']}, {p_txt(float(t['p']))}"
                if t and t["p"] not in ("", "NA") else "")
        L.append(f"| *{title}{test}* | | | | | |")
        if var == "poptype":
            order = ["probability general population", "other general population", "university students",
                     "school children and adolescents", "other non-clinical"]
            rows.sort(key=lambda r: order.index(r["analysis"][len(prefix):]))
        L += [row(r, "  " + LABEL.get(r["analysis"][len(prefix):], r["analysis"][len(prefix):]), log, samples)
              for r in rows]
    L += ["", "CI, confidence interval; PI, prediction interval. Pooling needs at least three samples; strata with fewer "
          "list each sample's estimate (%), named by first author and year (references: Supplementary File S6). "
          "Subgroup differences: Wald test of the subgroup term in the binomial–normal model.", "",
          "**Table 3.** Sensitivity analyses of the primary outcome (clinically significant misophonia, non-clinical "
          "samples).", ""] + head
    main_sens = [r for r in sens if " by poptype: " not in r["analysis"]]
    L += [row(r, r["analysis"].replace(">=", "≥")) for r in main_sens]
    pg = next((r for r in sens if r["analysis"].endswith("by poptype: probability general population")), None)
    sp = res / "sex_or.csv"
    note = ["", "S9 (leave-one-out and influence diagnostics) is reported in the text. S11 was added after the data were "
            "seen (Supplementary File S3)."]
    if pg:
        note[-1] += (f" In the probability samples of the general population, S11 gives {pct(pg['prev'])}% "
                     f"(95% CI {pct(pg['ci.lb'])}–{pct(pg['ci.ub'])}; k = {pg['k']}).")
    L += note
    if sp.exists():
        s = next(csv.DictReader(sp.open(encoding="utf-8")))
        L += ["", f"Female-to-male odds ratio (REML, Hartung–Knapp; k = {s['k']}): {float(s['OR']):.2f} "
                  f"(95% CI {float(s['ci.lb']):.2f}–{float(s['ci.ub']):.2f}; 95% PI {float(s['pi.lb']):.2f}–{float(s['pi.ub']):.2f})."]
    if (res / "grade_inputs.csv").exists():
        L += ["", "**Table 4.** Summary of findings and certainty of evidence (GRADE for event rates).", "",
              "| Outcome | Samples (participants) | Estimate (95% CI) | 95% PI | Certainty | Reasons for downgrading |",
              "| --- | --- | --- | --- | --- | --- |"]
        L += grade_rows(res)
        L += ["", "Certainty starts high for event rates from observational studies (Iorio et al., 2015) and goes down one "
              "level for each serious domain. Rules: risk of bias, more than half of the inverse-variance weight from "
              "samples rated no on JBI item 2 (sampling), 6 (valid case definition) or 9 (response rate); inconsistency, "
              "a 95% prediction interval reaching both below 5% and above 20% (odds ratio: both sides of 1); "
              "imprecision, a CI half-width above 5 percentage points (odds ratio: CI including 1); indirectness, fewer "
              "than five countries or three continents; publication bias, small-study regression p < 0.10 (assessed for "
              "prevalence outcomes when k ≥ 10)."]
    Path(a.out).write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", a.out)


if __name__ == "__main__":
    main()
