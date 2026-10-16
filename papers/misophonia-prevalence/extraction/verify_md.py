"""Verification files for R1 (protocol §11c, §14): the AI extraction drafts as Markdown, and the parser of R1's corrections.

make  - writes extraction/verify/verify_R1_NN.md from the drafts: one block per study, one sub-block per sample with the
        estimates (key numbers in a table), the key fields, the other fields and the nine JBI items, each with its
        location and quote. Under every sample R1 writes corrections in "Правки" and "да" after "Проверено:".
parse - reads the filled files, applies R1's corrections to the stored drafts and writes
        extraction/decisions/samples_R1.csv, estimates_R1.csv and corrections_R1.csv (AI value vs R1 value, for the
        share of corrected values); lists unverified samples and lines it could not read.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/verify_md.py make --run 2026-10-10 --draft extract_<date>
     .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/verify_md.py parse --run 2026-10-10 --draft extract_<date>
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
VERIFY = HERE / "verify"
sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402
STUDIES_PER_FILE = 10

KEY_SAMPLE = ["n_analysed", "population", "sampling"]
OTHER_SAMPLE = ["clinical_group", "country", "setting", "data_years", "design", "topic_disclosed", "inclusion_exclusion",
                "n_invited", "n_responded", "response_rate", "age_mean", "age_sd", "age_min", "age_max", "age_group",
                "pct_female", "informant", "mode", "instruments", "instrument_validated_in_language", "pub_status",
                "language", "funding_coi"]
SAMPLE_FIELDS = KEY_SAMPLE + OTHER_SAMPLE
EST_FIELDS = ["subgroup", "instrument", "threshold", "threshold_source", "author_label", "level", "table1_rule",
              "time_frame", "cases", "n", "derived", "derivation", "weighted_pct", "primary_for_authors", "location",
              "quote", "note"]
KEY_EST = ["instrument", "threshold", "level", "cases", "n"]
JBI_Q = {1: "рамка выборки", 2: "способ отбора", 3: "размер выборки", 4: "описание выборки и условий",
         5: "охват (пропуски)", 6: "валидность определения случая", 7: "единое надёжное измерение",
         8: "статистика (числитель и знаменатель)", 9: "отклик"}
VERIFIED = {"да", "+", "x", "х", "yes", "ok"}

HEADER = """# Проверка выписывания — файл {i} из {n}

Черновик заполнил ИИ (Claude Opus 5.5) по полному тексту; у каждого значения указано место и цитата. Проверяете вы, один проход.

**Как проверять выборку:**
1. Откройте полный текст по ссылке у исследования.
2. **Ключевые числа** — сверить с таблицей или текстом статьи всегда: в таблице оценок шкала, порог, уровень, случаи и n; под таблицей n_analysed, population, sampling.
3. Остальные поля и пункты JBI: проверить, что значение есть в цитате и место указано верно.
4. Неверное — исправьте строкой в блоке «Правки» этой выборки (по одной правке на строку):
   - `n_analysed = 1400`, `sampling = convenience` — поле выборки;
   - `E2.cases = 103`, `E2.level = L1` — поле оценки E2 (subgroup, instrument, threshold, level, cases, n, time_frame, primary_for_authors и др.);
   - `E2 удалить` — убрать оценку;
   - `+ оценка: subgroup=all; instrument=MQ; threshold=MSS>=7; level=L2; cases=50; n=300; location=Table 2` — добавить оценку;
   - `jbi_6 = no` — пункт JBI;
   - `выборка удалить: причина` — если это не отдельная выборка или её нельзя брать;
   - после `#` — комментарий для Claude.
5. Когда выборка проверена, напишите `да` после «Проверено:».

**Подсказки в файле:** «⚠ Проверка скриптом» — места, где скрипт нашёл повод присмотреться (уровень не совпадает с Таблицей 1, n оценки не равно n выборки, числа расходятся с независимым проходом ИИ по полному тексту, L2 по самодельным вопросам). «Расхождения в тексте» — ошибки самих авторов, которые нашёл ИИ (например, процент не равен случаи/n); в этом случае ИИ берёт числа из таблицы статьи. Посчитанные ИИ значения (суммы полос, % × n) выделены строкой **расчёт**.

**Уровни** (Таблица 1 и правила G1–G12, `forms/table1_completion.md`): L1 — симптомы; L2 — клинически значимый порог; L3 — интервью с критериями; L0 — любой «раздражающий звук»; E3 — порог по распределению той же выборки; E2 — не специфично для мизофонии; NR — определение не установить. L0, E3, E2 и NR в объединение не идут, но в таблицы статьи попадают.
**population:** gp_probability, gp_other, university_students, medical_students, school_pupils, workers, other_nonclinical, clinical. **sampling:** probability, census, quota, convenience, snowball, NR.
"""


def load(run: str, draft: str):
    recs = load_records(run)
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    drafts = {}
    for line in (HERE / "draft" / f"{draft}.jsonl").open(encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            drafts[d["conv_id"]] = d
    return recs, jobs, drafts


def sample_keys(jobs: list[dict], drafts: dict) -> list[tuple[str, dict, int, dict]]:
    """(sample_key, job, index in job, sample) in study order; keys are <study_id>-<n>."""
    out, count = [], {}
    for j in sorted(jobs, key=lambda x: (x["study_id"], x["job_id"])):
        d = drafts.get(j["job_id"])
        if not d:
            continue
        for i, s in enumerate(d["codes"]["samples"]):
            count[j["study_id"]] = count.get(j["study_id"], 0) + 1
            out.append((f"{j['study_id']}-{count[j['study_id']]}", j, i, s))
    return out


def clip(t: str, n: int) -> str:
    t = re.sub(r"\s+", " ", t or "").strip()
    return t if len(t) <= n else t[: n - 1] + "…"


def cell(t: str) -> str:
    return (t or "").replace("|", "/").replace("\n", " ")


def pct(cases: str, n: str) -> str:
    try:
        c, m = float(cases.replace(",", "")), float(n.replace(",", ""))
        return f"{100 * c / m:.1f}" if m > 0 else ""
    except (ValueError, AttributeError):
        return ""


def link(rec: str, label: str) -> str:
    pdf = PAPER / "fulltext" / "pdf" / f"{rec}.pdf"
    parts = [f"[текст](../../fulltext/text/{rec}.txt)"]
    if pdf.exists():
        parts.append(f"[PDF](../../fulltext/pdf/{rec}.pdf)")
    else:
        for ext in (".docx", ".pdf"):
            m = PAPER / "fulltext" / "manual" / f"{rec}{ext}"
            if m.exists():
                parts.append(f"[файл](../../fulltext/manual/{rec}{ext})")
                break
    return f"{label} {rec}: " + " · ".join(parts)


NUM_IN_THR = re.compile(r"(>=|≥|>|=>)\s*(\d+(?:\.\d+)?)")


def expected_level(instrument: str, threshold: str) -> str | None:
    """Level implied by Table 1 for a simple 'instrument >= x' threshold, or None if the rule cannot tell."""
    t = (threshold or "").lower()
    m = NUM_IN_THR.search(t)
    if not m or "and" in t or " or " in t or "percentile" in t or "median" in t or "top" in t:
        return None
    x = float(m.group(2)) + (0.5 if m.group(1) == ">" else 0)   # '> 9' means at least 10 on an integer scale
    bands = {
        "A-MISO-S": [(10, "L2"), (5, "L1"), (0, "L0")],
        "AMISOS-R": [(21, "L2"), (11, "L1"), (0, "L0")],
        "MisoQuest": [(61, "L2")],
        "S-Five": [(87, "L2")],
        "SMS-Adult": [(50.5, "L2")],
        "MAQ": [(22, "L2"), (11, "L1"), (0, "L0")],
        "DSTS-S": [(4, "L1"), (0, "L0")],
        "SSSQ4": [(2, "L1"), (0, "L0")],
    }
    if instrument == "MQ":
        if any(k in t for k in ("mss", "severity", "item 18")):
            b = [(7, "L2"), (4, "L1"), (0, "L0")]
        elif "total" in t:
            b = [(30, "L2")]
        elif "symptom" in t:
            b = [(14, "L1")]
        else:
            return None
    elif instrument in bands:
        b = bands[instrument]
    else:
        return None
    for cut, lv in b:
        if x >= cut:
            return lv
    return None


FT_PROPOSALS: dict[str, dict] = {}   # rec_id -> full-text proposal (fulltext/llm/*.jsonl), filled by make()
INTS = re.compile(r"\d[\d,]*")


def ints(text: str) -> set[int]:
    return {int(x.replace(",", "")) for x in INTS.findall(text or "")}


def ft_pairs(recs: list[str]) -> list[tuple[set[int], set[int], str]]:
    out = []
    for r in recs:
        p = FT_PROPOSALS.get(r)
        if p:
            for d in p["codes"]["case_definitions"]:
                out.append((ints(d["cases"]), ints(d["denominator"]), f"{d['cases']}/{d['denominator']}"))
    return out


def flags(s: dict, recs: list[str] | None = None) -> list[str]:
    """Checks by script, shown to R1 next to the estimates; the drafts themselves are not changed."""
    groups: dict[str, list[str]] = {}
    pairs = ft_pairs(recs or [])
    for i, e in enumerate(s["estimates"], 1):
        if not pairs or e["level"] not in ("L1", "L2", "L3") or e["subgroup"].strip().lower() != "all" \
                or e["derived"] == "yes":   # derived sums are shown with their calculation anyway
            continue
        try:
            c, n = int(float(e["cases"].replace(",", ""))), int(float(e["n"].replace(",", "")))
        except ValueError:
            continue
        if not any(c in pc and n in pn for pc, pn, _ in pairs):
            groups.setdefault("пары «случаи / n» нет в независимом предложении ИИ по полному тексту (там: "
                              + "; ".join(sorted({t for _, _, t in pairs}))[:300] + ") — сверьте числа", []).append(f"E{i}")
    n_sample = s["n_analysed"]["value"].replace(",", "")
    for i, e in enumerate(s["estimates"], 1):
        c, n = e["cases"].replace(",", ""), e["n"].replace(",", "")
        try:
            if float(c) > float(n):
                groups.setdefault("случаев больше, чем n", []).append(f"E{i}")
        except ValueError:
            pass
        exp = expected_level(e["instrument"], e["threshold"])
        if exp and e["level"] in ("L0", "L1", "L2", "L3") and exp != e["level"]:
            groups.setdefault(f"по Таблице 1 порог «{e['threshold']}» даёт {exp}, в черновике {e['level']}", []).append(f"E{i}")
        if e["level"] == "L3" and e["instrument"] not in ("interview", "multiple"):
            groups.setdefault("L3 без интервью: L3 — только интервью с явными критериями", []).append(f"E{i}")
        if e["level"] == "L2" and e["instrument"] == "adhoc":
            groups.setdefault("самодельные вопросы на L2: верно, только если требуются и реакция, и нарушения", []).append(f"E{i}")
        if e["subgroup"].strip().lower() == "all" and n not in ("NR", "NA") and n_sample not in ("NR", "NA") and n != n_sample:
            groups.setdefault(f"n оценки не равно n_analysed выборки ({n_sample}): проверьте знаменатель", []).append(f"E{i}")
    return [f"{', '.join(v)}: {k}" for k, v in groups.items()]


def render_sample(key: str, s: dict, recs: list[str] | None = None) -> list[str]:
    L = [f"### {key} · {clip(s['label'], 160)}", f"Отчёты: {s['reports']}", ""]
    L.append("**Оценки — ключевые числа сверить по таблице статьи:**")
    L.append("")
    L.append("| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |")
    L.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    extra = []
    for i, e in enumerate(s["estimates"], 1):
        L.append(f"| E{i} | {cell(e['subgroup'])} | {cell(e['instrument'])} · {cell(e['threshold'])} | **{e['level']}** | "
                 f"**{cell(e['cases'])} / {cell(e['n'])}** | {pct(e['cases'], e['n'])} | {cell(clip(e['location'], 60))} | "
                 f"«{cell(clip(e['quote'], 220))}» |")
        bits = [f"источник порога: {e['threshold_source']}", f"правило: {clip(e['table1_rule'], 120)}",
                f"у авторов: «{clip(e['author_label'], 80)}»", f"главная у авторов: {e['primary_for_authors']}",
                f"период: {e['time_frame']}"]
        if e["derived"] == "yes":
            bits.append(f"**расчёт: {clip(e['derivation'], 160)}**")
        if e["weighted_pct"] not in ("", "NA", "NR"):
            bits.append(f"взвешенная доля: {e['weighted_pct']}")
        if e["note"]:
            bits.append(f"заметка: {clip(e['note'], 300)}")
        extra.append(f"- E{i}: " + "; ".join(bits))
    L += [""] + extra
    fl = flags(s, recs)
    if fl:
        L += ["", "**⚠ Проверка скриптом (обратите внимание):**"] + [f"- {x}" for x in fl]
    L += ["", "**Ключевые поля выборки:**"]
    for f in KEY_SAMPLE:
        v = s[f]
        L.append(f"- **{f}: {v['value']}** — {clip(v['loc'], 80)} — «{clip(v['quote'], 260)}»")
    L += ["", "**Остальные поля:**"]
    for f in OTHER_SAMPLE:
        v = s[f]
        q = f" — «{clip(v['quote'], 160)}»" if v["quote"] else ""
        loc = f" — {clip(v['loc'], 60)}" if v["loc"] else ""
        L.append(f"- {f}: {clip(v['value'], 300)}{loc}{q}")
    if s.get("notes"):
        L.append(f"- notes: {clip(s['notes'], 600)}")
    L += ["", "**Риск смещения (JBI):**"]
    for i in range(1, 10):
        b = s["jbi"][f"jbi_{i}"]
        q = f" — «{clip(b['quote'], 160)}»" if b["quote"] else ""
        L.append(f"{i}. {JBI_Q[i]}: **{b['rating']}** — {clip(b['reason'], 220)} — {clip(b['loc'], 60)}{q}")
    L += ["", "Правки:", "- ", "", "Проверено: ", ""]
    return L


def make(a):
    recs, jobs, drafts = load(a.run, a.draft)
    for f in sorted((PAPER / "fulltext" / "llm").glob("ft_*.jsonl")):   # independent AI pass over the same full texts
        if ".errors." in f.name:
            continue
        for line in f.open(encoding="utf-8"):
            if line.strip():
                p = json.loads(line)
                FT_PROPOSALS[p["conv_id"]] = p
    missing = [j["job_id"] for j in jobs if j["job_id"] not in drafts]
    if missing and not a.allow_missing:
        raise SystemExit(f"no draft for {len(missing)} jobs: {', '.join(missing)}")
    smap = {}
    for r in csv.DictReader((HERE / "study_map.csv").open(encoding="utf-8")):
        smap.setdefault(r["study_id"], []).append(r)
    keyed = sample_keys(jobs, drafts)
    by_study: dict[str, list] = {}
    for key, j, i, s in keyed:
        by_study.setdefault(j["study_id"], []).append((key, j, s))
    studies = sorted(by_study)
    if a.studies:   # only these studies, in new files numbered from --first-file (files of R1 are never touched)
        studies = [s for s in studies if s in set(a.studies)]
    chunks = [studies[i:i + STUDIES_PER_FILE] for i in range(0, len(studies), STUDIES_PER_FILE)]
    outdir = Path(a.out) if a.out else VERIFY
    outdir.mkdir(exist_ok=True)
    first = a.first_file
    names = [outdir / f"verify_R1_{fi:02d}.md" for fi in range(first, first + len(chunks))]
    clash = [p for p in names if p.exists()]
    if a.studies and clash:
        raise SystemExit(f"refusing to overwrite: {', '.join(p.name for p in clash)}")
    existing = sorted(outdir.glob("verify_R1_*.md"))
    if existing and not a.force and not a.studies:
        raise SystemExit(f"{len(existing)} verification files exist; use --force to overwrite")
    n_samples = n_est = 0
    for fi, chunk in enumerate(chunks, first):
        L = [HEADER.format(i=fi, n=first - 1 + len(chunks))]
        for st in chunk:
            rows = smap[st]
            jobs_here = sorted({j["job_id"] for _, j, _ in by_study[st]})
            first = recs[jobs_here[0]]
            L += ["---", "", f"## {st} · {first.get('first_author') or ''} {first.get('year') or ''} · "
                             f"{clip(first.get('venue') or '', 80)}", ""]
            for jid in jobs_here:
                j = next(x for x in jobs if x["job_id"] == jid)
                d = drafts[jid]["codes"]
                u = recs[jid]
                L.append(link(jid, "Основной отчёт") + f" — «{clip(u['title'], 160)}»" +
                         (f" — [DOI](https://doi.org/{u['doi']})" if u.get("doi") else ""))
                for e in j["attached"]:
                    L.append(link(e, "Приложен") + f" — «{clip(recs[e]['title'], 120)}»")
                for e in j["listed_only"]:
                    L.append(link(e, "Не приложен (длинный)") + f" — «{clip(recs[e]['title'], 120)}»")
                if j["link_reason"]:
                    L.append(f"Связь отчётов: {j['link_reason']}")
                for po in j["possible_overlap"]:
                    L.append(f"⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): {po}")
                if d["excluded_samples"] and not d["excluded_samples"].lower().startswith("none"):
                    L.append(f"Не выписано ИИ: {clip(d['excluded_samples'], 700)}")
                if d["consistency_notes"]:
                    L.append(f"Расхождения в тексте: {clip(d['consistency_notes'], 900)}")
                if d["note"]:
                    L.append(f"Заметка ИИ: {clip(d['note'], 600)}")
                L.append("")
            for key, j, s in by_study[st]:
                L += render_sample(key, s, [j["main"], *j["attached"]])
                n_samples += 1
                n_est += len(s["estimates"])
        out = outdir / f"verify_R1_{fi:02d}.md"
        out.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(studies)} studies, {n_samples} samples, {n_est} estimates -> {len(chunks)} files in {outdir}")
    if missing:
        print(f"WARNING: no draft yet for {len(missing)} jobs: {', '.join(missing)}")


EST_RE = re.compile(r"^E(\d+)\.(\w+)\s*=\s*(.*)$")
DEL_RE = re.compile(r"^E(\d+)\s+удалить\b(.*)$", re.I)
ADD_RE = re.compile(r"^\+\s*оценка\s*:\s*(.*)$", re.I)
JBI_RE = re.compile(r"^jbi_([1-9])\s*=\s*(yes|no|unclear|NA)\b(.*)$", re.I)
DROP_RE = re.compile(r"^выборка\s+удалить\b[:\s]*(.*)$", re.I)
FIELD_RE = re.compile(r"^(\w+)\s*=\s*(.*)$")


def parse(a):
    recs, jobs, drafts = load(a.run, a.draft)
    keyed = {key: (j, s) for key, j, i, s in sample_keys(jobs, drafts)}
    blocks = {}
    for p in sorted((Path(a.out) if a.out else VERIFY).glob("verify_R1_*.md")):
        text = p.read_text(encoding="utf-8")
        for m in re.finditer(r"^### (ST\d{3}-\d+) .*?(?=^### |^---|\Z)", text, re.S | re.M):
            blocks[m.group(1)] = (p.name, m.group(0))
    samples_out, est_out, corr, problems, unverified = [], [], [], [], []
    for key, (j, s) in keyed.items():
        if key not in blocks:
            problems.append(f"{key}: block not found")
            continue
        fname, body = blocks[key]
        pr = re.search(r"^Правки:\s*\n(.*?)^Проверено:(.*)$", body, re.S | re.M)
        if not pr:
            problems.append(f"{fname} {key}: no 'Правки'/'Проверено' lines")
            continue
        ver = pr.group(2).strip().lower()
        if ver not in VERIFIED:
            unverified.append(key)
        fields = {f: s[f]["value"] for f in SAMPLE_FIELDS}
        ests = {i: dict(e) for i, e in enumerate(s["estimates"], 1)}
        jbi = {i: s["jbi"][f"jbi_{i}"]["rating"] for i in range(1, 10)}
        dropped, added, comments = "", [], []
        for raw in pr.group(1).splitlines():
            line = raw.strip().lstrip("-").strip()
            if not line:
                continue
            line, _, comment = line.partition("#")
            line = line.strip()
            if comment.strip():
                comments.append(comment.strip())
            if not line:
                continue
            if m := DEL_RE.match(line):
                k = int(m.group(1))
                if k in ests:
                    corr.append({"sample_key": key, "target": f"E{k}", "field": "*", "ai_value": "estimate",
                                 "r1_value": "deleted", "key_field": "yes"})
                    ests.pop(k)
                else:
                    problems.append(f"{fname} {key}: no estimate E{k}: {raw}")
            elif m := EST_RE.match(line):
                k, f, v = int(m.group(1)), m.group(2), m.group(3).strip()
                if k not in ests or f not in EST_FIELDS:
                    problems.append(f"{fname} {key}: unknown estimate field: {raw}")
                    continue
                corr.append({"sample_key": key, "target": f"E{k}", "field": f, "ai_value": ests[k][f], "r1_value": v,
                             "key_field": "yes" if f in KEY_EST else "no"})
                ests[k][f] = v
            elif m := ADD_RE.match(line):
                e = {f: "" for f in EST_FIELDS}
                for part in m.group(1).split(";"):
                    if "=" in part:
                        f, v = part.split("=", 1)
                        if f.strip() in EST_FIELDS:
                            e[f.strip()] = v.strip()
                        else:
                            problems.append(f"{fname} {key}: unknown field in added estimate: {f.strip()}")
                added.append(e)
                corr.append({"sample_key": key, "target": "new", "field": "*", "ai_value": "", "r1_value": m.group(1),
                             "key_field": "yes"})
            elif m := JBI_RE.match(line):
                i, v = int(m.group(1)), m.group(2).lower().replace("na", "NA")
                corr.append({"sample_key": key, "target": f"jbi_{i}", "field": "rating", "ai_value": jbi[i],
                             "r1_value": v, "key_field": "no"})
                jbi[i] = v
            elif m := DROP_RE.match(line):
                dropped = m.group(1).strip() or "R1"
            elif (m := FIELD_RE.match(line)) and m.group(1) in SAMPLE_FIELDS:
                f, v = m.group(1), m.group(2).strip()
                corr.append({"sample_key": key, "target": "sample", "field": f, "ai_value": fields[f], "r1_value": v,
                             "key_field": "yes" if f in KEY_SAMPLE else "no"})
                fields[f] = v
            else:
                problems.append(f"{fname} {key}: unreadable correction: {raw.strip()}")
        samples_out.append({"sample_key": key, "study_id": j["study_id"], "job_id": j["job_id"], "label": s["label"],
                            "reports": s["reports"], **fields,
                            **{f"jbi_{i}": jbi[i] for i in range(1, 10)},
                            "verified": "yes" if ver in VERIFIED else "no", "dropped": dropped,
                            "r1_comments": " | ".join(comments)})
        for i, e in list(ests.items()) + [(f"new{n}", e) for n, e in enumerate(added, 1)]:
            est_out.append({"sample_key": key, "est": f"E{i}" if isinstance(i, int) else i, **e})
    dec = Path(a.dec) if a.dec else HERE / "decisions"
    dec.mkdir(parents=True, exist_ok=True)
    for name, rows in (("samples_R1.csv", samples_out), ("estimates_R1.csv", est_out), ("corrections_R1.csv", corr)):
        if rows:
            with (dec / name).open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
                w.writeheader()
                w.writerows(rows)
    n_vals = sum(len(SAMPLE_FIELDS) + 9 + len(s["estimates"]) * len(EST_FIELDS) for j, s in keyed.values())
    print(f"samples {len(samples_out)} (unverified {len(unverified)}), estimates {len(est_out)}, corrections {len(corr)} "
          f"of about {n_vals} drafted values")
    if unverified:
        print("unverified:", ", ".join(unverified))
    for p in problems:
        print("PROBLEM:", p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["make", "parse"])
    ap.add_argument("--run", required=True)
    ap.add_argument("--draft", required=True)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--studies", nargs="*", help="make: only these study IDs, into new files")
    ap.add_argument("--first-file", type=int, default=1, help="make: number of the first file")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--out", help="folder of the verification files (default extraction/verify)")
    ap.add_argument("--dec", help="output folder for parse (default extraction/decisions)")
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
