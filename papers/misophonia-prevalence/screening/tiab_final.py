"""Final title/abstract decisions (protocol, section 11b; deviations.md, 2026-10-11).

Every record gets R1's decision from one of three places:
  calibration   R1's blind label, when the AI label agrees; otherwise R1's decision in the verification files
                (both labels shown);
  re-screening  R1's blind label for AI-excluded records outside the calibration sample (safeguard triggered);
  verification  R1's decision with the AI label shown, for records outside the sample that the AI sent to full text.
Records R1 finally labels include or unsure go to full-text screening.

Writes screening/decisions/tiab_final.csv and tiab_summary.json (numbers for PRISMA and the Methods).
Run: .venv/Scripts/python.exe papers/misophonia-prevalence/screening/tiab_final.py --run 2026-10-10
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEC = HERE / "decisions"


def read(path: Path) -> dict[str, dict]:
    return {r["rec_id"]: r for r in csv.DictReader(path.open(encoding="utf-8-sig"))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    run = a.run
    verify_files = sorted((HERE / "verify" / run).glob("verify_R1_*.md"))
    subprocess.run([sys.executable, "-I", str(HERE / "screen_md.py"), "parse", *map(str, verify_files),
                    "--out", str(DEC / "verify_R1.csv")], check=True)
    screening = list(csv.DictReader((HERE.parent / "search" / "runs" / run / "screening.csv").open(encoding="utf-8-sig")))
    ai = {json.loads(l)["conv_id"]: json.loads(l)["codes"] for l in (HERE / "llm" / f"{run}.jsonl").open(encoding="utf-8")}
    sample = set(json.loads((HERE / "calibration" / run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"])
    cal, res, ver = read(DEC / "calibration_R1.csv"), read(DEC / "rescreen_R1.csv"), read(DEC / "verify_R1.csv")

    rows, problems = [], []
    for s in screening:
        rid = s["rec_id"]
        a_dec = ai[rid]["decision"]
        if rid in sample:
            blind = cal[rid]["decision"]
            if blind == a_dec:
                final, where = blind, "calibration (agreed with AI)"
            elif rid in ver:
                final, where = ver[rid]["decision"], "calibration (resolved, both labels shown)"
            else:
                final, where = "", "MISSING"
        elif rid in res:
            final, where = res[rid]["decision"], "re-screening (blind)"
        elif rid in ver:
            final, where = ver[rid]["decision"], "verification (AI label shown)"
        else:
            final, where = "", "MISSING"
        if not final:
            problems.append(rid)
        rows.append({"rec_id": rid, "final_decision": final, "full_text": final in ("include", "unsure"),
                     "decided_in": where, "ai_decision": a_dec, "ai_reason": ai[rid]["reason"],
                     "r1_blind": cal.get(rid, res.get(rid, {})).get("decision", ""),
                     "verify_code": ver.get(rid, {}).get("code", ""), "title": s["title"]})
    with (DEC / "tiab_final.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    full = lambda d: d in ("include", "unsure")  # noqa: E731
    v_out = [r for r in rows if r["decided_in"].startswith("verification")]
    accepted = sum(1 for r in v_out if r["verify_code"].startswith("="))
    overrides = Counter(f"{r['ai_decision']} -> {r['final_decision']}" for r in v_out if r["final_decision"] != r["ai_decision"])
    cal_res = [r for r in rows if r["decided_in"].startswith("calibration (resolved")]
    summary = {
        "run": run, "records_screened": len(rows), "missing_decisions": problems,
        "to_full_text": sum(r["full_text"] for r in rows),
        "excluded_title_abstract": sum(1 for r in rows if r["final_decision"] == "exclude"),
        "final_labels": dict(Counter(r["final_decision"] for r in rows)),
        "by_stage": {k: dict(Counter(r["final_decision"] for r in rows if r["decided_in"] == k))
                     for k in sorted({r["decided_in"] for r in rows})},
        "verification": {
            "records": len(v_out), "accepted_ai_label_with_equals": accepted,
            "overrides_by_direction": dict(overrides.most_common()),
            "ai_full_text_but_r1_excluded": sum(1 for r in v_out if full(r["ai_decision"]) and r["final_decision"] == "exclude"),
        },
        "calibration_resolutions": {
            "records": len(cal_res),
            "final_equals_r1_blind": sum(1 for r in cal_res if r["final_decision"] == r["r1_blind"]),
            "final_equals_ai": sum(1 for r in cal_res if r["final_decision"] == r["ai_decision"]),
            "full_text_after_resolution": sum(r["full_text"] for r in cal_res),
        },
        "safeguard": {"re_screened": sum(1 for r in rows if r["decided_in"].startswith("re-screening")),
                      "moved_to_full_text": sum(1 for r in rows if r["decided_in"].startswith("re-screening") and r["full_text"])},
    }
    (DEC / "tiab_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
