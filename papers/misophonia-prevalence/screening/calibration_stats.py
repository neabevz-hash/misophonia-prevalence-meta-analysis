"""Calibration results (protocol, section 11b): R1's blind labels against the AI draft labels.

Checks the AI label file against the SHA-256 committed before unblinding, then reports
- Cohen's kappa for include / unsure / exclude;
- kappa and Gwet's AC1 for "full text" (include or unsure) vs exclude, with bootstrap 95% CIs;
- AI sensitivity and specificity against R1 for "full text", with Clopper-Pearson 95% CIs;
- the anchoring safeguard: calibration records R1 labelled include or unsure and the AI labelled exclude.

Run: .venv/Scripts/python.exe papers/misophonia-prevalence/screening/calibration_stats.py --run 2026-10-10
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "harness"))
from llmaudit.agreement import bootstrap_ci, cohen_kappa, gwet_ac1, percent_agreement  # noqa: E402


def binom_cdf(k: int, n: int, p: float) -> float:
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def clopper_pearson(x: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact binomial CI by bisection (no scipy in the environment)."""
    if n == 0:
        return float("nan"), float("nan")

    def solve(f, lo=0.0, hi=1.0):
        for _ in range(80):
            mid = (lo + hi) / 2
            if f(mid):
                hi = mid
            else:
                lo = mid
        return (lo + hi) / 2

    lower = 0.0 if x == 0 else solve(lambda p: 1 - binom_cdf(x - 1, n, p) >= alpha / 2)
    upper = 1.0 if x == n else solve(lambda p: binom_cdf(x, n, p) <= alpha / 2)
    return lower, upper


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--decisions", help="CSV from screen_md.py parse (default screening/decisions/calibration_R1.csv)")
    a = ap.parse_args()
    labels_path = HERE / "llm" / f"{a.run}.jsonl"
    sha_path = labels_path.with_name(labels_path.name + ".sha256")
    digest = hashlib.sha256(labels_path.read_bytes()).hexdigest()
    committed = json.loads(sha_path.read_text(encoding="utf-8"))["sha256"] if sha_path.exists() else None
    if committed != digest:
        sys.exit(f"AI label file does not match the committed hash ({committed} vs {digest})")
    ai = {json.loads(l)["conv_id"]: json.loads(l)["codes"]["decision"] for l in labels_path.open(encoding="utf-8")}
    sample = json.loads((HERE / "calibration" / a.run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"]
    dec_path = Path(a.decisions) if a.decisions else HERE / "decisions" / "calibration_R1.csv"
    r1 = {r["rec_id"]: r["decision"] for r in csv.DictReader(dec_path.open(encoding="utf-8-sig"))}
    missing = [i for i in sample if not r1.get(i)]
    if missing:
        sys.exit(f"R1 has no decision for {len(missing)} calibration records: {missing[:10]}")
    ids = [i for i in sample if i in ai]
    unlabeled = [i for i in sample if i not in ai]
    a3, b3 = [r1[i] for i in ids], [ai[i] for i in ids]
    full = lambda d: "full_text" if d in ("include", "unsure") else "exclude"  # noqa: E731
    a2, b2 = [full(x) for x in a3], [full(x) for x in b3]
    tp = sum(x == "full_text" and y == "full_text" for x, y in zip(a2, b2))
    fn = sum(x == "full_text" and y == "exclude" for x, y in zip(a2, b2))
    tn = sum(x == "exclude" and y == "exclude" for x, y in zip(a2, b2))
    fp = sum(x == "exclude" and y == "full_text" for x, y in zip(a2, b2))
    cats3 = ["include", "unsure", "exclude"]
    confusion = {f"R1_{x}": {f"AI_{y}": sum(p == x and q == y for p, q in zip(a3, b3)) for y in cats3} for x in cats3}
    false_negatives = [i for i in ids if full(r1[i]) == "full_text" and ai[i] == "exclude"]
    out = {
        "run": a.run, "ai_labels_sha256": digest, "n_calibration": len(sample), "n_compared": len(ids),
        "calibration_records_without_ai_label": unlabeled,
        "three_labels": {"agreement": percent_agreement(a3, b3), "kappa": cohen_kappa(a3, b3),
                         "kappa_ci": bootstrap_ci(cohen_kappa, a3, b3), "confusion": confusion},
        "full_text_vs_exclude": {
            "agreement": percent_agreement(a2, b2), "kappa": cohen_kappa(a2, b2), "kappa_ci": bootstrap_ci(cohen_kappa, a2, b2),
            "ac1": gwet_ac1(a2, b2, ["full_text", "exclude"]),
            "ac1_ci": bootstrap_ci(gwet_ac1, a2, b2, categories=["full_text", "exclude"]),
            "ai_sensitivity": tp / (tp + fn) if tp + fn else float("nan"), "ai_sensitivity_ci": clopper_pearson(tp, tp + fn),
            "ai_specificity": tn / (tn + fp) if tn + fp else float("nan"), "ai_specificity_ci": clopper_pearson(tn, tn + fp),
            "counts": {"tp": tp, "fn": fn, "tn": tn, "fp": fp}},
        "safeguard_triggered": bool(false_negatives),
        "ai_false_negatives": false_negatives,
    }
    dest = HERE / "decisions" / "calibration_stats.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    f2 = out["full_text_vs_exclude"]
    print(f"{len(ids)} calibration records compared; R1 full text {tp + fn}, R1 exclude {tn + fp}")
    print(f"three labels: kappa {out['three_labels']['kappa']:.2f}")
    print(f"full text vs exclude: kappa {f2['kappa']:.2f}, AC1 {f2['ac1']:.2f}; "
          f"AI sensitivity {f2['ai_sensitivity']:.2f} {tuple(round(v, 2) for v in f2['ai_sensitivity_ci'])}, "
          f"specificity {f2['ai_specificity']:.2f} {tuple(round(v, 2) for v in f2['ai_specificity_ci'])}")
    print("safeguard TRIGGERED: R1 re-screens all AI-excluded records blind" if false_negatives
          else "safeguard not triggered", false_negatives or "")
    print(f"-> {dest}")


if __name__ == "__main__":
    main()
