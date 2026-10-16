"""Supplementary files built from the logs, so that every number matches the record of the work.

S1_search.md        - search strategies, dates and counts per source (PRISMA-S), de-duplication, seed-set recall,
                      citation search
S4_ai.md            - the AI assistant's roles, model, prompts and their hashes, runs and agreement with R1
S5_excluded.md      - reports excluded at full text (database search and citation search), with the primary reason
S2_table1.md        - case-definition levels: Table 1 (forms/instrument_thresholds.csv) and the mapping rules G1-G12
S3_deviations.md    - every change and clarification after registration (deviations.md)
S6_studies.md       - characteristics of the included samples and their whole-sample estimates (forms/*.csv)
S7_jbi.md           - JBI risk-of-bias ratings per sample (reasons: forms/samples.csv, jbi_notes)

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/manuscript/make_supplement.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
OUT = HERE / "supplement"
RUN = PAPER / "search" / "runs" / "2026-10-10"
CHASE = PAPER / "search" / "runs" / "2026-10-15-citations"
REASON_TEXT = {"E1_selected_sample": "sample recruited for misophonia or sound sensitivity (E1)",
               "I3_no_counts": "no number of cases with a denominator (I3)",
               "E4_design": "design: review, case report, qualitative or theoretical (E4)",
               "E2_no_misophonia_measure": "no misophonia-specific case definition (E2)",
               "not_misophonia": "not about misophonia", "E5_duplicate": "duplicate report of the same sample (E5)",
               "other": "other"}


def fmt(n) -> str:
    return f"{n:,}"


def protocol_block(name: str) -> str:
    md = (PAPER / "protocol.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*" + re.escape(name) + r"\*\*[^\n]*\n```\n(.*?)```", md, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def s1() -> str:
    log = json.loads((RUN / "search_log.json").read_text(encoding="utf-8"))
    dd = json.loads((RUN / "dedup_report.json").read_text(encoding="utf-8"))
    rc = json.loads((RUN / "recall_seed_set.json").read_text(encoding="utf-8"))
    ch = json.loads((CHASE / "chase_log.json").read_text(encoding="utf-8"))
    rows = [
        ("PubMed", "NCBI E-utilities", log["pubmed"]["searched_at_utc"], log["pubmed"]["meta"]["query"], log["pubmed"]["records"]),
        ("Europe PMC", "REST API", log["europepmc"]["searched_at_utc"], log["europepmc"]["meta"]["query"], log["europepmc"]["records"]),
        ("OpenAlex", "API, title and abstract", log["openalex"]["searched_at_utc"], log["openalex"]["meta"]["filter"], log["openalex"]["records"]),
        ("Semantic Scholar", "Graph API, bulk search", log["s2"]["searched_at_utc"], log["s2"]["meta"]["query"], log["s2"]["records"]),
        ("DataCite", "REST API", log["datacite"]["searched_at_utc"], log["datacite"]["meta"]["query"], log["datacite"]["records"]),
        ("OpenAIRE Graph", "API v1, research products, type publication; three queries (at most four OR operators each)",
         log["openaire"]["searched_at_utc"], " | ".join(log["openaire"]["meta"]["queries"]), log["openaire"]["records"]),
        ("CORE", "API v3, title or abstract, one query per term; records kept only if the term occurs in the title or abstract",
         log["core"]["searched_at_utc"], " | ".join(log["core"]["meta"]["queries"]), log["core"]["records"]),
        ("Instrument citations", "OpenAlex, works citing the development papers of ten instruments",
         log["citations"]["searched_at_utc"],
         "; ".join(f"{k} ({v['doi']}): {v['citing_records']}" for k, v in log["citations"]["meta"].items()),
         log["citations"]["records"]),
        ("SciELO", "SciELO Search in a browser, all indexes", "2026-10-10", protocol_block("LILACS / BVS and SciELO:") or
         "misofonia OR misophonia OR misofonía", dd["records_per_source"]["scielo"]),
        ("Google Scholar", "browser, first 200 results per query, pages saved by the reviewer", "2026-10-10",
         "misophonia prevalence | misophonia \"cut-off\" OR \"clinically significant\"", dd["records_per_source"]["scholar"]),
    ]
    L = ["# Supplementary File S1. Search strategies (PRISMA-S)", "",
         "No date, language or publication-type limits. Condition terms only, no prevalence filter. Searches ran after the "
         "OSF registration (10.17605/OSF.IO/39MQ2). Code: `search/search.py`; logs: `search/runs/2026-10-10/`.", "",
         "| Source | Interface | Searched (UTC) | Query | Records |", "| --- | --- | --- | --- | --- |"]
    for src, iface, when, q, n in rows:
        L.append(f"| {src} | {iface} | {when} | `{q.replace('|', '¦')}` | {fmt(n)} |")
    L += ["", "## De-duplication", "",
          f"- Records retrieved: {fmt(dd['records_total'])}; unique records: {fmt(dd['unique_records'])}; duplicates removed: "
          f"{fmt(dd['duplicates_removed'])} (of which {fmt(dd['pointer_or_component_records_attached'])} pointer or component "
          "records attached to their database record).",
          f"- Removed automatically as non-study records (every source types them as datasets, peer-review reports, "
          f"paratext, book reviews, software, registrations or figures): {fmt(dd['auto_removed_non_study_records'])}.",
          f"- Records screened: {fmt(dd['records_to_screen'])}; found only through instrument citations: "
          f"{fmt(dd['unique_only_via_instrument_citations'])}; only through DataCite, OpenAIRE, CORE or Google Scholar: "
          f"{fmt(dd['unique_only_via_pointer_sources'])}.",
          f"- Recall on the seed set (the {rc['seed_studies']} studies of Gowda & Prabhu, 2024): "
          f"{rc['in_screening_list']} of {rc['seed_studies']}.", "",
          "LILACS (BVS) could not be searched: its search servers refused connections from our network (deviations.md).", "",
          "## Citation searching of the included studies", "",
          f"Run on {ch['run_at_utc']} through OpenAlex (`search/citation_chase.py`). Seeds: the {fmt(119)} included reports and "
          f"four systematic reviews; {ch['seeds_found']} found in OpenAlex; not found: {', '.join(ch['seeds_not_found'])} "
          "(reference lists checked by hand).",
          f"- Backward: {fmt(ch['backward']['works'])} cited works, {fmt(ch['backward']['already_in_main_set'])} already in the "
          f"record set. Forward: {fmt(ch['forward']['links'])} citing links, {fmt(ch['forward']['already_in_main_set'])} already "
          "in the set.",
          f"- New records: {fmt(ch['new_unique_records'])}; with a condition term in the title or abstract: "
          f"{ch['new_with_condition_term_in_title_or_abstract']}.",
          f"- OpenAlex full-text search for {', '.join(ch['fulltext_search']['terms'])}: "
          f"{fmt(ch['fulltext_search']['records_with_openalex_fulltext'])} of the new records have a full text in OpenAlex, "
          f"{ch['fulltext_search']['records_matching']} mention a term and went to full-text assessment (deviations.md)."]
    return "\n".join(L) + "\n"


def jl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8") if l.strip()]


def dual_pass() -> tuple[int, int]:
    """Key counts of the extraction drafts that the independent full-text proposals also give (same report)."""
    sys.path.insert(0, str(PAPER / "extraction"))
    import verify_md as V
    for f in sorted((PAPER / "fulltext" / "llm").glob("ft_*.jsonl")):
        if ".errors." in f.name:
            continue
        for p in jl(f):
            V.FT_PROPOSALS[p["conv_id"]] = p
    jobs = {j["job_id"]: j for j in json.loads((PAPER / "extraction" / "jobs.json").read_text(encoding="utf-8"))}
    drafts = {}
    for f in sorted((PAPER / "extraction" / "draft").glob("extract_*.jsonl")):
        if ".errors." in f.name:
            continue
        for d in jl(f):
            drafts.setdefault(d["conv_id"], d)
    checked = agree = 0
    for jid, d in drafts.items():
        pairs = V.ft_pairs([jobs[jid]["main"], *jobs[jid]["attached"]])
        if not pairs:
            continue
        for s in d["codes"]["samples"]:
            for e in s["estimates"]:
                if e["level"] not in ("L1", "L2", "L3") or e["subgroup"].strip().lower() != "all" or e["derived"] == "yes":
                    continue
                try:
                    c, n = int(float(e["cases"].replace(",", ""))), int(float(e["n"].replace(",", "")))
                except ValueError:
                    continue
                checked += 1
                agree += any(c in pc and n in pn for pc, pn, _ in pairs)
    return checked, agree


def s4() -> str:
    cal = json.loads((PAPER / "screening" / "decisions" / "calibration_stats.json").read_text(encoding="utf-8"))
    runs = [
        ("Title and abstract screening labels", "screening/llm_screener_prompt.md", PAPER / "screening" / "llm" / "2026-10-10.jsonl"),
        ("Full-text eligibility proposals", "fulltext/ft_prompt.md (git tag misophonia-ft-prompt-v1.0)",
         PAPER / "fulltext" / "llm" / "ft_2026-10-10.jsonl"),
        ("Full-text proposals, citation search", "fulltext/ft_prompt.md (same frozen prompt)",
         PAPER / "fulltext" / "llm" / "ft_chase_2026-10-15.jsonl"),
        ("Extraction and risk-of-bias drafts", "extraction/extract_prompt.md (git tag misophonia-extraction-prompt-v1.0)",
         PAPER / "extraction" / "draft" / "extract_2026-10-15.jsonl"),
    ]
    L = ["# Supplementary File S4. Use of an AI assistant", "",
         "Claude Opus 5.5 (Anthropic; model `claude-opus-5-5`, reasoning effort high) ran through Claude Code in headless mode "
         "(`claude -p`) with a fixed system prompt, a JSON output schema, no tools and an empty working directory; one item per "
         "call. Every output is stored with the hash of the system prompt and of the rendered prompt, the model actually used "
         "and the Claude Code version. Every label, proposal, extracted value and rating was a draft that the reviewer (R1) "
         "accepted or corrected.", "",
         "| Task | Prompt | Items | Run (UTC) | System prompt SHA-256 (first 16) | Claude Code | Models used |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    for task, prompt, path in runs:
        if not path.exists():
            continue
        rows = jl(path)
        shas = sorted({r["judge"]["system_prompt_sha"] for r in rows})
        cli = sorted({r["judge"]["cli_version"] for r in rows})
        models = sorted({m for r in rows for m in r.get("models_used", [])})
        when = f"{min(r['judged_at'] for r in rows)[:16]} to {max(r['judged_at'] for r in rows)[:16]}"
        L.append(f"| {task} | `{prompt}` | {fmt(len(rows))} | {when} | {', '.join(shas)} | {', '.join(cli)} | {', '.join(models)} |")
    ft = list(csv.DictReader((PAPER / "fulltext" / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig")))
    agree = sum(1 for r in ft if r["code"] == r["ai_code"] or r["code"].startswith("="))
    chase_p = PAPER / "fulltext" / "decisions" / "ft_R1_chase.csv"
    chase = list(csv.DictReader(chase_p.open(encoding="utf-8-sig"))) if chase_p.exists() else []
    agree_c = sum(1 for r in chase if r["code"] == r["ai_code"] or r["code"].startswith("="))
    tiab = {r["rec_id"]: r for r in csv.DictReader((PAPER / "screening" / "decisions" / "tiab_final.csv").open(encoding="utf-8-sig"))}
    incl = [r["rec_id"] for r in ft if r["decision"] == "eligible"]
    ai_excl = [k for k in incl if tiab[k]["ai_decision"] == "exclude"]
    rescued = [k for k in ai_excl if tiab[k]["decided_in"].startswith("re-screening")]
    L += ["", "## Agreement with the reviewer", "",
          f"- Title and abstract, blind calibration sample (n = {cal.get('n', 151)}): see `screening/decisions/calibration_stats.json` "
          "(κ, Gwet's AC1, sensitivity and specificity of the AI for sending a record to full text).",
          f"- Included reports that the AI had labeled exclude at title and abstract: {len(ai_excl)} of {len(incl)} "
          f"({', '.join(ai_excl) or 'none'}); {len(rescued)} of them reached full text only through the reviewer's blind "
          "re-screening of the AI-excluded records (the pre-specified safeguard).",
          f"- Full text: the reviewer's decision matched the AI proposal for {agree} of {len(ft)} reports from the database "
          f"search and {agree_c} of {len(chase)} from the citation search."]
    cs_p = PAPER / "extraction" / "decisions" / "correction_stats.json"
    if cs_p.exists():
        cs = json.loads(cs_p.read_text(encoding="utf-8"))
        L.append(f"- Extraction: the reviewer verified {fmt(cs['drafted_values'])} drafted values ({cs['verified_samples']} "
                 f"samples, {cs['drafted_estimates']} estimates) against the sources and corrected {cs['values_corrected']}, "
                 f"including {cs['key_values_corrected']} of {fmt(cs['key_values'])} key values (sample size, population "
                 f"type and sampling of each sample; instrument, threshold, level, cases and denominator of each "
                 f"estimate); estimates added by the reviewer: "
                 f"{cs['estimates_added_by_R1']} (`extraction/decisions/correction_stats.json`).")
    qc_p = PAPER / "extraction" / "decisions" / "quote_check.json"
    if qc_p.exists():
        qc = json.loads(qc_p.read_text(encoding="utf-8"))
        e, k = qc["estimates"], qc["key_fields"]
        L.append(f"- Supporting quotes: {e['found_verbatim']} of {e['quotes_checked']} quotes for estimates and "
                 f"{k['found_verbatim']} of {k['quotes_checked']} for key sample fields were found verbatim in the source "
                 "text after normalizing spacing and punctuation; the others joined cells of a table or paraphrased it "
                 "(`extraction/quote_check.py`).")
    checked, agreed = dual_pass()
    if checked:
        L.append(f"- Two independent AI passes over the same full texts: for {agreed} of {checked} case counts read directly from "
                 "a report (levels L1–L3, whole sample, not derived), the extraction draft and the earlier full-text "
                 "proposal gave the same number of cases and denominator.")
    L.append("")
    return "\n".join(L) + "\n"


def s5() -> str:
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in (RUN / "records_unique.jsonl").open(encoding="utf-8")}
    cp = CHASE / "records_unique.jsonl"
    if cp.exists():
        recs.update({json.loads(l)["rec_id"]: json.loads(l) for l in cp.open(encoding="utf-8") if l.strip()})
    L = ["# Supplementary File S5. Reports excluded at full text", ""]
    for part, name in (("Database search", "ft_R1.csv"), ("Citation searching of the included studies", "ft_R1_chase.csv")):
        p = PAPER / "fulltext" / "decisions" / name
        if not p.exists():
            continue
        ft = [r for r in csv.DictReader(p.open(encoding="utf-8-sig")) if r["decision"] == "not_eligible"]
        L += [f"## {part}", "", f"{len(ft)} reports, with the primary reason (PRISMA 2020).", "",
              "| Record | First author | Year | Title | DOI | Reason |", "| --- | --- | --- | --- | --- | --- |"]
        for r in sorted(ft, key=lambda x: (x["reason"], x["rec_id"])):
            u = recs[r["rec_id"]]
            title = re.sub(r"\s+", " ", u.get("title") or "").replace("|", "/")
            L.append(f"| {r['rec_id']} | {u.get('first_author') or ''} | {u.get('year') or ''} | {title} | "
                     f"{u.get('doi') or ''} | {REASON_TEXT.get(r['reason'], r['reason'])} |")
        L.append("")
    return "\n".join(L)


def s2() -> str:
    rows = list(csv.DictReader((PAPER / "forms" / "instrument_thresholds.csv").open(encoding="utf-8")))
    L = ["# Supplementary File S2. Case-definition levels (Table 1, complete version)", "",
         "Levels: L0 any bothersome sound, described only; L1 symptom level; L2 clinically significant; L3 diagnosed by "
         "interview. Completed before extraction from the instruments' development and validation papers only "
         "(protocol section 13; deviations, 2026-10-15).", "",
         "| Instrument | Full name | Range | L1 | L2 | Source of thresholds | Notes |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows:
        cells = [r["instrument"], r["full_name"], r["score_range"], r["L1_rule"], r["L2_rule"], r["threshold_source"],
                 r["notes"]]
        L.append("| " + " | ".join(re.sub(r"\s+", " ", c or "").replace("|", "/") for c in cells) + " |")
    rules = (PAPER / "forms" / "table1_completion.md").read_text(encoding="utf-8").split("## General rules", 1)[1]
    rules = rules.split("\n## ", 1)[0]
    L += ["", "## Mapping rules", rules.rstrip()]
    return "\n".join(L) + "\n"


def s3() -> str:
    md = (PAPER / "deviations.md").read_text(encoding="utf-8")
    body = md.split("\n", 1)[1]
    return "# Supplementary File S3. Changes and clarifications after registration\n" + body


def num(x: str) -> float | None:
    try:
        return float(str(x).replace(",", ""))
    except ValueError:
        return None


def s6(forms: Path) -> str:
    """Characteristics of the included samples and every estimate (whole sample), from the verified tables."""
    samples = list(csv.DictReader((forms / "samples.csv").open(encoding="utf-8")))
    ests = list(csv.DictReader((forms / "estimates.csv").open(encoding="utf-8")))
    by_s: dict[str, list[dict]] = {}
    for e in ests:
        by_s.setdefault(e["sample_id"], []).append(e)
    L = ["# Supplementary File S6. Characteristics of the included samples and their estimates", "",
         f"{len({s['study_id'] for s in samples})} studies, {len(samples)} independent samples. Estimates for the whole "
         "sample; subgroup estimates are in the data release (`forms/estimates.csv`). Level: L1 symptoms, L2 clinically "
         "significant, L3 interview; L0, E3 (distribution-based), E2 (not misophonia-specific) and NR (definition not "
         "stated) are listed, not pooled.", "",
         "| Sample | Study (report) | Country | Population | Sampling | n | Age | % female | Instrument and threshold | Level | Cases / n (%) |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for s in samples:
        age = s["age_mean"] if s["age_mean"] not in ("NR", "NA", "") else (
            f"{s['age_min']}-{s['age_max']}" if s["age_min"] not in ("NR", "NA", "") else "NR")
        rows = [e for e in by_s.get(s["sample_id"], []) if e["subgroup"].strip().lower() in ("all", "total", "whole sample")]
        first = True
        for e in rows or [None]:
            if e is None:
                cells_e = ["", "", ""]
            else:
                c, n = num(e["cases"]), num(e["n"])
                pct = f" ({100 * c / n:.1f}%)" if c is not None and n else ""
                cells_e = [f"{e['instrument']}: {e['threshold']}", e["level"], f"{e['cases']} / {e['n']}{pct}"]
            lead = [s["sample_id"], f"{s['first_author']} {s['year']} ({s['report_ids'].split(';')[0]})", s["country"],
                    s["population"] + (f" ({s['clinical_group']})" if s["population"] == "clinical" else ""),
                    s["sampling"], s["n_analysed"], age, s["pct_female"]] if first else [""] * 8
            L.append("| " + " | ".join(re.sub(r"\s+", " ", x or "").replace("|", "/") for x in lead + cells_e) + " |")
            first = False
    # Reports of the included studies (main report first), from the record metadata.
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in (RUN / "records_unique.jsonl").open(encoding="utf-8")}
    cp = CHASE / "records_unique.jsonl"
    if cp.exists():
        recs.update({json.loads(l)["rec_id"]: json.loads(l) for l in cp.open(encoding="utf-8") if l.strip()})
    reports: dict[str, list[str]] = {}
    for s in samples:
        for rid in s["report_ids"].split(";"):
            if rid and rid not in reports.setdefault(s["study_id"], []):
                reports[s["study_id"]].append(rid)
    L += ["", "## Reports of the included studies", "",
          "Study code, then each report: first author (year). Title. Source. DOI or record identifier.", ""]
    for st in sorted(reports):
        refs = []
        for rid in reports[st]:
            u = recs.get(rid, {})
            title = re.sub(r"\s+", " ", u.get("title") or "").strip().rstrip(".")
            doi = f"https://doi.org/{u['doi']}" if u.get("doi") else rid
            refs.append(f"{u.get('first_author') or ''} ({u.get('year') or 'n.d.'}). {title}. *{u.get('venue') or ''}*. {doi}")
        L.append(f"- **{st}.** " + " — ".join(refs))
    return "\n".join(L) + "\n"


def s7(forms: Path) -> str:
    """JBI ratings per sample."""
    samples = list(csv.DictReader((forms / "samples.csv").open(encoding="utf-8")))
    L = ["# Supplementary File S7. Risk of bias: JBI checklist for prevalence studies", "",
         "Items: 1 sample frame; 2 sampling; 3 sample size; 4 description; 5 coverage; 6 valid identification of the "
         "condition; 7 standard measurement; 8 statistical analysis; 9 response rate. Y yes, N no, U unclear, NA not "
         "applicable. Decision rules: `forms/rob_jbi.md` and rule G12. The reason for every rating no or unclear is "
         "in the data release (`forms/samples.csv`, column `jbi_notes`).", "",
         "| Sample | Study | Population | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    ab = {"yes": "Y", "no": "N", "unclear": "U", "NA": "NA"}
    for s in samples:
        cells = [s["sample_id"], f"{s['first_author']} {s['year']}", s["population"]] + [
            ab.get(s[f"jbi_{i}"], s[f"jbi_{i}"]) for i in range(1, 10)]
        L.append("| " + " | ".join(re.sub(r"\s+", " ", x or "").replace("|", "/") for x in cells) + " |")
    tot = {i: sum(1 for s in samples if s[f"jbi_{i}"] == "yes") for i in range(1, 10)}
    L += ["", "Samples rated yes per item: " + "; ".join(f"item {i}: {tot[i]} of {len(samples)}" for i in range(1, 10)) + "."]
    return "\n".join(L) + "\n"


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--forms", default=str(PAPER / "forms"), help="folder with the verified samples.csv and estimates.csv")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    jobs = [("S1_search.md", s1), ("S2_table1.md", s2), ("S3_deviations.md", s3), ("S4_ai.md", s4), ("S5_excluded.md", s5)]
    forms = Path(a.forms)
    if (forms / "samples.csv").exists() and len((forms / "samples.csv").read_text(encoding="utf-8").splitlines()) > 1:
        jobs += [("S6_studies.md", lambda: s6(forms)), ("S7_jbi.md", lambda: s7(forms))]
    for name, fn in jobs:
        (out / name).write_text(fn(), encoding="utf-8", newline="\n")
        print("wrote", out / name)


if __name__ == "__main__":
    main()
