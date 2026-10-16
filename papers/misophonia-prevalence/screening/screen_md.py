"""Screening decision files in Markdown (protocol, section 11b).

R1 screens in Markdown files: one block per record (title, abstract, year, venue, record type, language, DOI link;
no author names) with a line "**Решение:**" for the decision. Codes, the same on Russian and English keyboard layouts:
  +        include (goes to full text)
  ?        unsure (goes to full text)
  -1 … -7  exclude, the digit is the reason (REASONS below)
  =        verification files only: agree with the AI label shown above the line
Anything after the code is a note.

  make  --phase calibration --run RUN   blind calibration sample (calibration/<run>/sample.csv), no AI labels
  make  --phase rescreen --run RUN      blind re-screening of AI-excluded records outside the calibration sample
  make  --phase verify --run RUN        every record with its AI label, in files of FILE_SIZE records
  parse FILE... --out CSV               decisions -> CSV, and a check that every record has a valid code

Run: .venv/Scripts/python.exe papers/misophonia-prevalence/screening/screen_md.py make --phase calibration --run 2026-10-10
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent / "search" / "runs"
FILE_SIZE = 150
REASONS = {
    "1": ("review", "обзор, редакционная статья, комментарий, письмо без данных"),
    "2": ("case", "клинический случай или серия случаев"),
    "3": ("selected", "выборка набрана из-за мизофонии или чувствительности к звукам"),
    "4": ("measure", "нет инструмента именно для мизофонии (гиперакузия, шумочувствительность…)"),
    "5": ("nonempirical", "качественное, теоретическое, на животных, не эмпирическое"),
    "6": ("offtopic", "не про мизофонию"),
    "7": ("other", "другое — напишите почему"),
}
AI_CODE = {"include": "+", "unsure": "?"}
AI_REASON_TO_DIGIT = {"exc_review_or_commentary": "1", "exc_case_report": "2", "exc_selected_for_misophonia": "3",
                      "exc_no_misophonia_measure": "4", "exc_qualitative": "5", "exc_not_empirical": "5",
                      "exc_off_topic": "6", "exc_other": "7"}
AI_REASON_RU = {"inc_prevalence": "исследование распространённости", "inc_unselected_sample": "ненабранная выборка",
                "inc_validation": "валидация шкалы", "inc_clinical_group": "клиническая группа",
                "inc_screened_pool": "скрининг пула", "unsure_sample_unclear": "выборка неясна",
                "unsure_no_abstract": "нет аннотации", "unsure_other": "другое"}
HEADER_RE = re.compile(r"^###\s+(\d+)\s*·\s*(R\d{4,5})\b")
DECISION_RE = re.compile(r"^\**\s*Решение\s*:?\s*\**\s*:?\s*(.*)$", re.I)
AI_RE = re.compile(r"^\**\s*ИИ\s*:?\s*\**\s*:?\s*(\S+)")

GUIDE = """**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: исследование может дать долю людей с мизофонией в выборке, набранной **не** из-за мизофонии |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
{reasons}

Пример: `**Решение:** -4 только гиперакузия`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Что включаем:** опросы распространённости; опросы студентов, школьников, работников, общих выборок со шкалой мизофонии (A-MISO-S, AMISOS-R, MQ, MisoQuest, S-Five, DMQ, DVMSQ, BMQ-R, SMS, MAQ, NYMS, свои вопросы) или интервью; валидации шкал на неклинических выборках; клинические группы, набранные по другому поводу (ОКР, тревога, депрессия, СДВГ, аутизм, тики, тиннитус, гиперакузия…), если мизофонию измеряли; эксперименты, где сначала просеяли ненабранный пул; диссертации, препринты, постеры и тезисы любого из этого. Подробно — протокол, §8.
"""


def reasons_rows() -> str:
    return "\n".join(f"| `-{d}` | исключить: {text} |" for d, (_, text) in REASONS.items())


def tidy_types(plain: str) -> str:
    seen = []
    for part in (plain or "").replace("|", ";").split(";"):
        part = part.strip().lower()
        if part and not part.startswith("src=") and part not in seen:
            seen.append(part)
    return ", ".join(seen[:3])


def types_plain(types: str) -> str:
    return "; ".join(sorted({t.split(":", 1)[1] for t in (types or "").split(" | ") if ":" in t and t.split(":", 1)[1]}))


def one_line(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def block(n: int, r: dict, ai: dict | None = None, blind: dict | None = None) -> str:
    meta = " · ".join(x for x in [str(r.get("year") or ""), one_line(r.get("venue")), r.get("types_plain") or "",
                                  r.get("language") or "", r.get("link") or ""] if x)
    abstract = one_line(r.get("abstract")) or "_Аннотации нет — решайте по названию или ставьте `?`._"
    lines = ["---", "", f"### {n} · {r['rec_id']}", "", f"**{one_line(r.get('title')) or '[без названия]'}**", "",
             meta, "", abstract, ""]
    if blind is not None:
        lines += [f"**Ваша слепая метка (калибровка):** {blind['code']} {blind.get('note') or ''}".rstrip(), ""]
    if ai is not None:
        c = ai["codes"]
        code = AI_CODE.get(c["decision"]) or f"-{AI_REASON_TO_DIGIT.get(c['reason'], '7')}"
        why = REASONS[code[1:]][1] if code.startswith("-") else AI_REASON_RU.get(c["reason"], c["reason"])
        lines += [f"**ИИ:** {code} · {why} · {one_line(c.get('note'))}", ""]
    lines += ["**Решение:** ", ""]
    return "\n".join(lines)


def write(path: Path, title: str, intro: str, blocks: list[str], force: bool) -> None:
    if path.exists() and not force:
        sys.exit(f"{path} already exists; refusing to overwrite R1's work (use --force only for an untouched file)")
    path.parent.mkdir(parents=True, exist_ok=True)
    text = f"# {title}\n\n{intro}\n\n{GUIDE.format(reasons=reasons_rows())}\n" + "\n".join(blocks)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"{path}  ({len(blocks)} records)")


def screening_rows(run: str) -> dict[str, dict]:
    rows = list(csv.DictReader((RUNS / run / "screening.csv").open(encoding="utf-8-sig")))
    return {r["rec_id"]: {**r, "types_plain": tidy_types(types_plain(r["types"]))} for r in rows}


def make(a) -> None:
    if a.phase == "calibration":
        rows = list(csv.DictReader((HERE / "calibration" / a.run / "sample.csv").open(encoding="utf-8-sig")))
        blocks = [block(i, {**r, "types_plain": tidy_types(r.get("types_plain"))}) for i, r in enumerate(rows, 1)]
        total = len(screening_rows(a.run))
        intro = (f"Случайные 10% списка к отбору финального поиска {a.run}: {len(rows)} из {total}, зерно 20261010, "
                 "порядок случайный. **Меток ИИ в этом файле нет.** Размечайте в любом порядке и в несколько заходов. "
                 "Когда закончите, скажите: я проверю, что всё размечено, и закоммичу файл до того, как открою метки ИИ.")
        write(HERE / "calibration" / a.run / f"calibration_{a.screener}.md", "Калибровка вслепую",
              intro, blocks, a.force)
    elif a.phase == "rescreen":
        recs = screening_rows(a.run)
        sample = set(json.loads((HERE / "calibration" / a.run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"])
        labels = {json.loads(l)["conv_id"]: json.loads(l) for l in (HERE / "llm" / f"{a.run}.jsonl").open(encoding="utf-8")}
        ids = sorted(i for i, x in labels.items() if x["codes"]["decision"] == "exclude" and i not in sample)
        random.Random(20261011).shuffle(ids)
        for part, start in enumerate(range(0, len(ids), FILE_SIZE), 1):
            chunk = ids[start:start + FILE_SIZE]
            blocks = [block(start + i, recs[rid]) for i, rid in enumerate(chunk, 1)]
            intro = (f"Записи {start + 1}–{start + len(chunk)} из {len(ids)}: всё, что ИИ исключил, кроме калибровочной выборки. "
                     "Повторный отбор вслепую по правилу защиты (протокол, §11b). **Меток и причин ИИ в этом файле нет** — "
                     "решайте с нуля по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261011).\n\n"
                     "**Быстрый режим:** достаточно одного символа — `+`, `?` или просто `-` (исключить, причина не нужна). "
                     "Заметки не нужны. Если по названию всё ясно, аннотацию можно не читать.")
            write(HERE / "rescreen" / a.run / f"rescreen_{a.screener}_{part:02d}.md",
                  f"Повторный отбор вслепую, часть {part}", intro, blocks, a.force)
    else:  # verify
        # Scope (deviations.md, 2026-10-11): records outside the calibration sample that the AI sent to full text, and
        # calibration records where R1's blind label and the AI label differ. AI-excluded records outside the sample are
        # decided by the blind re-screening when the safeguard is triggered, so they are not shown with AI labels.
        recs = screening_rows(a.run)
        labels = {json.loads(l)["conv_id"]: json.loads(l) for l in (HERE / "llm" / f"{a.run}.jsonl").open(encoding="utf-8")}
        sample = set(json.loads((HERE / "calibration" / a.run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"])
        blind = {r["rec_id"]: r for r in csv.DictReader((HERE / "decisions" / f"calibration_{a.screener}.csv").open(encoding="utf-8-sig"))}
        rescreen_done = a.safeguard
        ids = sorted(rid for rid in recs if rid not in sample and (labels[rid]["codes"]["decision"] != "exclude" or not rescreen_done))
        ids += sorted(rid for rid in sample if blind[rid]["decision"] != labels[rid]["codes"]["decision"])
        for part, start in enumerate(range(0, len(ids), FILE_SIZE), 1):
            chunk = ids[start:start + FILE_SIZE]
            blocks = [block(start + i, recs[rid], labels.get(rid), blind.get(rid) if rid in sample else None)
                      for i, rid in enumerate(chunk, 1)]
            n_cal = sum(1 for rid in chunk if rid in sample)
            intro = (f"Записи {start + 1}–{start + len(chunk)} из {len(ids)}, с меткой ИИ над строкой решения. "
                     "Согласны с ИИ — поставьте `=`; не согласны — свой код (`+`, `?` или `-`, причина и заметка не нужны). Решаете вы."
                     + (f" Последние {n_cal} — калибровочные записи, где ваша слепая метка разошлась с ИИ: она показана над меткой ИИ."
                        if n_cal else ""))
            write(HERE / "verify" / a.run / f"verify_{a.screener}_{part:02d}.md", f"Проверка с метками ИИ, часть {part}",
                  intro, blocks, a.force)


def parse_code(raw: str) -> tuple[str, str, str, str]:
    """-> (code, decision, reason, note); decision '' when the code is missing or invalid."""
    text = raw.strip().replace("−", "-").replace("–", "-").replace("—", "-")
    text = re.sub(r"^-\s+(\d)", r"-\1", text)
    if not text:
        return "", "", "", ""
    head, _, note = text.partition(" ")
    note = note.strip()
    if head == "+":
        return head, "include", "", note
    if head == "?":
        return head, "unsure", "", note
    if head == "=":
        return head, "agree", "", note
    m = re.fullmatch(r"-([1-7])", head)
    if m:
        return head, "exclude", REASONS[m.group(1)][0], note
    if head == "-":   # exclude without a reason: allowed in re-screening and verification files
        return head, "exclude", "", note
    return head, "", "", text


def parse(a) -> None:
    out_rows, problems, seen = [], [], set()
    for f in a.files:
        path = Path(f)
        lines = [x.strip() for x in path.read_text(encoding="utf-8").splitlines()]
        cur = None
        for i, line in enumerate(lines):
            h = HEADER_RE.match(line)
            if h:
                cur = {"file": path.name, "k": int(h.group(1)), "rec_id": h.group(2), "ai_code": ""}
                continue
            if cur is None:
                continue
            m = AI_RE.match(line)
            if m:
                cur["ai_code"] = m.group(1)
                continue
            d = DECISION_RE.match(line)
            if d:
                raw = d.group(1)
                if not raw.strip():   # the code written on the next line instead
                    nxt = next((x for x in lines[i + 1:] if x), "")
                    if nxt and not nxt.startswith("---") and not HEADER_RE.match(nxt):
                        raw = nxt
                code, decision, reason, note = parse_code(raw)
                if decision == "agree":
                    if not cur["ai_code"]:
                        decision = ""
                        problems.append(f"{cur['rec_id']}: '=' but no AI label in this block")
                    else:
                        _, decision, reason, _ = parse_code(cur["ai_code"])
                        code = f"={cur['ai_code']}"
                if not code:
                    problems.append(f"{cur['rec_id']}: no decision")
                elif not decision:
                    problems.append(f"{cur['rec_id']}: cannot read the code {code!r}")
                elif reason == "other" and not note:
                    problems.append(f"{cur['rec_id']}: -7 without a note (allowed, but say why)")
                if cur["rec_id"] in seen:
                    problems.append(f"{cur['rec_id']}: appears twice")
                seen.add(cur["rec_id"])
                out_rows.append({**cur, "code": code, "decision": decision, "reason": reason, "note": note})
                cur = None
    counts = {k: sum(1 for r in out_rows if r["decision"] == k) for k in ("include", "unsure", "exclude", "")}
    if a.out:
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["rec_id", "k", "file", "code", "decision", "reason", "note", "ai_code"])
            w.writeheader()
            w.writerows(out_rows)
    print(f"{len(out_rows)} records: include {counts['include']}, unsure {counts['unsure']}, "
          f"exclude {counts['exclude']}, not decided {counts['']}")
    missing = [p.split(":")[0] for p in problems if p.endswith(": no decision")]
    for p in problems:
        if not p.endswith(": no decision"):
            print("  " + p)
    if missing:
        print(f"  no decision yet: {len(missing)} records ({', '.join(missing[:10])}{', …' if len(missing) > 10 else ''})")
    if a.expect and len(out_rows) != a.expect:
        print(f"  expected {a.expect} records, found {len(out_rows)}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--phase", required=True, choices=["calibration", "rescreen", "verify"])
    m.add_argument("--run", required=True)
    m.add_argument("--screener", default="R1")
    m.add_argument("--force", action="store_true")
    m.add_argument("--safeguard", action="store_true",
                   help="verify: the safeguard was triggered, so AI-excluded records outside the sample are left to the re-screening")
    p = sub.add_parser("parse")
    p.add_argument("files", nargs="+")
    p.add_argument("--out")
    p.add_argument("--expect", type=int)
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
