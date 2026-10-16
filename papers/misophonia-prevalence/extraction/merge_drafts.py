"""Add the drafts of re-run jobs to the main draft file (unchanged JSON lines), once per job.

A job that failed in the main run (network errors are listed in <main>.jsonl.errors.jsonl) is re-run into a separate
file; this script appends its line to the main file only if the main file has no draft for that job, and stops if a
job would appear twice. The re-run file is kept as it is.

Run: .venv/Scripts/python.exe -I papers/misophonia-prevalence/extraction/merge_drafts.py --main extract_2026-10-15 --add extract_2026-10-15_rerun
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", required=True)
    ap.add_argument("--add", required=True)
    a = ap.parse_args()
    main_p, add_p = HERE / "draft" / f"{a.main}.jsonl", HERE / "draft" / f"{a.add}.jsonl"
    have = [json.loads(l)["conv_id"] for l in main_p.open(encoding="utf-8") if l.strip()]
    if len(have) != len(set(have)):
        raise SystemExit("the main file already has a job twice")
    added = []
    with main_p.open("a", encoding="utf-8", newline="\n") as out:
        for line in add_p.open(encoding="utf-8"):
            if not line.strip():
                continue
            jid = json.loads(line)["conv_id"]
            if jid in have or jid in added:
                continue
            out.write(line if line.endswith("\n") else line + "\n")
            added.append(jid)
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    now = {json.loads(l)["conv_id"] for l in main_p.open(encoding="utf-8") if l.strip()}
    missing = [j["job_id"] for j in jobs if j["job_id"] not in now]
    print(f"added {len(added)}: {', '.join(added)}; main file now {len(now)} of {len(jobs)} jobs"
          + (f"; missing: {', '.join(missing)}" if missing else ""))
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
