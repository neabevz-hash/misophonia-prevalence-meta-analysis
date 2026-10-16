"""Build the OSF registration package for protocol v1.0 -> registration/osf_package/ (git-ignored).

    .venv/Scripts/python.exe papers/misophonia-prevalence/registration/make_osf_package.py

Output:
  Rekhert_misophonia_protocol_v1.0.pdf   the protocol (pandoc -> docx -> LibreOffice -> PDF)
  misophonia-prereg-v1.0.zip             protocol, forms, search and screening code, AI screener prompt, logs,
                                         README and SHA-256 manifest, in the repository's folder layout
  llm_screener_prompt.md, extraction_codebook.md   loose copies for the two file fields of the OSF form
Files are taken from the commit tagged misophonia-prereg-v1.0 (git show), so the package matches the tag byte for byte.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))
from llmaudit.msbuild import make_reference_docx, to_docx  # noqa: E402

OUT = HERE / "osf_package"
TAG = "misophonia-prereg-v1.0"
P = "papers/misophonia-prevalence/"
FILES = [
    P + "protocol.md",
    P + "deviations.md",
    P + "forms/extraction_codebook.md",
    P + "forms/rob_jbi.md",
    P + "forms/instrument_thresholds.csv",
    P + "forms/samples.csv",
    P + "forms/estimates.csv",
    P + "search/search.py",
    P + "search/import_manual.py",
    P + "search/dedup.py",
    P + "search/recall.py",
    P + "search/seed_set.csv",
    P + "search/runs/2026-10-09-pilot/search_log.json",
    P + "search/runs/2026-10-09-pilot/dedup_report.json",
    P + "search/runs/2026-10-10-check/README.md",
    P + "search/runs/2026-10-10-check/search_log.json",
    P + "search/runs/2026-10-10-check/dedup_report.json",
    P + "search/runs/2026-10-10-check/recall_seed_set.json",
    P + "screening/llm_screener_prompt.md",
    P + "screening/llm_screen.py",
    P + "screening/calibration.py",
    P + "screening/screen_md.py",
    P + "screening/calibration_stats.py",
    P + "screening/llm/stand_test_2026-10-09_4records.jsonl",
    P + "screening/llm/stand_test_2026-10-10_4records.jsonl",
    "harness/llmaudit/__init__.py",
    "harness/llmaudit/env.py",
    "harness/llmaudit/judge.py",
]

README = """# Prevalence of misophonia: registration package (protocol v1.0)

Martin Rekhert, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com

Protocol v1.0 frozen on 2026-10-10, before the final search and before any screening.
Git tag `{tag}`, commit `{commit}`.

## Contents

- `Rekhert_misophonia_protocol_v1.0.pdf` (outside the zip) and `papers/misophonia-prevalence/protocol.md`: the protocol (PRISMA-P 2015).
- `papers/misophonia-prevalence/forms/`: extraction codebook, templates of the two extraction tables, instrument thresholds mapped to case-definition levels (protocol Table 1), JBI risk-of-bias decision rules.
- `papers/misophonia-prevalence/search/`:
  - `search.py`: automated searches (PubMed, Europe PMC, OpenAlex, Semantic Scholar, DataCite, OpenAIRE, CORE, instrument citations);
  - `import_manual.py`: imports the manual exports (Google Scholar via Publish or Perish, SciELO, LILACS/BVS);
  - `dedup.py`: de-duplication and the screening list;
  - `recall.py` and `seed_set.csv`: recall on the seed set (the 12 studies included by Gowda & Prabhu, 2024);
  - `runs/2026-10-09-pilot/`: pilot search log and de-duplication report;
  - `runs/2026-10-10-check/`: check of the PubMed parser, the three added sources (DataCite, OpenAIRE, CORE) and the v1.0 de-duplication rules.
- `papers/misophonia-prevalence/screening/`:
  - `llm_screener_prompt.md`: the AI screener's prompt and JSON schema, frozen with the protocol;
  - `llm_screen.py`: its runner;
  - `calibration.py`: draws the blind calibration sample (seed 20261010);
  - `screen_md.py`: writes the Markdown decision files (calibration, blind re-screening, verification) and parses them;
  - `calibration_stats.py`: calibration agreement, AI sensitivity and specificity, the anchoring safeguard;
  - `llm/stand_test_*.jsonl`: two 4-record technical tests of the runner.
- `harness/llmaudit/`: the headless Claude Code runner used by `llm_screen.py`.
- `papers/misophonia-prevalence/deviations.md`: log of changes after registration (empty at registration).
- `MANIFEST.sha256`: SHA-256 of every file in this package.

## Reproducing

Python 3.12 with httpx, lxml and jsonschema; Claude Code CLI (2.1.289 at registration) for the AI screener. Keys go into `.env` at the repository root: `OPENALEX_API_KEY` for OpenAlex; `CLAUDE_CODE_OAUTH_TOKEN` for Claude Code.

    python papers/misophonia-prevalence/search/search.py --date YYYY-MM-DD
    python papers/misophonia-prevalence/search/import_manual.py --date YYYY-MM-DD
    python papers/misophonia-prevalence/search/dedup.py --date YYYY-MM-DD
    python papers/misophonia-prevalence/search/recall.py --date YYYY-MM-DD
    python papers/misophonia-prevalence/screening/calibration.py --run YYYY-MM-DD
    python papers/misophonia-prevalence/screening/screen_md.py make --phase calibration --run YYYY-MM-DD
    python papers/misophonia-prevalence/screening/llm_screen.py --run YYYY-MM-DD

Raw search exports are not included: the databases change, so a re-run reproduces the procedure, not the exact records. The raw exports of the final search will be archived with the data release.
"""


def blob(path: str, rev: str | None) -> bytes:
    """File content as committed at rev (byte-identical to the tag), or from the working tree without a tag."""
    if rev:
        return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
    return (ROOT / path).read_bytes()


def protocol_pdf(rev: str | None) -> Path:
    ref = make_reference_docx(OUT / "_reference.docx", double=False)
    md = blob(P + "protocol.md", rev).decode("utf-8")
    docx = to_docx(md, OUT / "protocol_v1.0.docx", ref, PAPER)
    soffice = Path(r"C:\Program Files\LibreOffice\program\soffice.exe")
    subprocess.run([str(soffice), "--headless", "--convert-to", "pdf", "--outdir", str(OUT), str(docx)],
                   check=True, capture_output=True)
    pdf = OUT / "Rekhert_misophonia_protocol_v1.0.pdf"
    (OUT / "protocol_v1.0.pdf").replace(pdf)
    for tmp in (docx, ref):
        tmp.unlink()
    return pdf


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    tagged = subprocess.run(["git", "rev-list", "-n", "1", TAG], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + FILES, cwd=ROOT, capture_output=True, text=True).stdout.strip()
    rev = tagged or None
    if not tagged:
        print(f"WARNING: no tag {TAG}; packing the working tree (draft only)", file=sys.stderr)
    elif tagged != commit or dirty:
        print(f"note: HEAD {commit[:10]} differs from the tag {tagged[:10]}; packing the tagged files", file=sys.stderr)
    pdf = protocol_pdf(rev)
    readme = README.format(tag=TAG, commit=tagged or commit + " (working tree, untagged)")
    files = {f: blob(f, rev) for f in FILES}
    manifest = [f"{hashlib.sha256(b).hexdigest()}  {f}" for f, b in files.items()]
    manifest.append(f"{hashlib.sha256(readme.encode('utf-8')).hexdigest()}  README.md")
    with zipfile.ZipFile(OUT / f"{TAG}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("README.md", readme)
        for f, b in files.items():
            z.writestr(f, b)
        z.writestr("MANIFEST.sha256", "\n".join(manifest) + "\n")
    for f in (P + "screening/llm_screener_prompt.md", P + "forms/extraction_codebook.md"):
        (OUT / Path(f).name).write_bytes(files[f])
    print(f"{OUT}:")
    for p in sorted(OUT.iterdir()):
        print(f"  {p.name}  {p.stat().st_size:,} bytes")
    print(f"zip sha256: {hashlib.sha256((OUT / f'{TAG}.zip').read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
