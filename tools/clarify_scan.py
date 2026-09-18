#!/usr/bin/env python3
"""clarify_scan.py — the deterministic scanner for `agentii.clarify`.

The clarify SKILL.md documents `agentii_cmd.py clarify --thesis <dir> --questions`,
but that subcommand is NOT implemented in the installed plugin (available: specify,
tasks, constitution). This is a local implementation of the documented scan so the
methodology can be followed without patching a shared marketplace install.

Checks (verbatim from SKILL.md "Candidates come from a deterministic scanner"):
  1. prose `wrong_if`      — missing metric= / threshold= / source=
  2. universe rows         — without rationale
  3. missing `budget`
  4. missing `expiry_triggers`
  5. subscription tokens   — not in `TICKER × skill` form
  6. missing `as_of` / pins
  7. pillars without priority

Each finding carries a stable content-derived id, the target it unblocks, a question,
and derived options where possible (null = free-form).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


def qid(target: str, check: str) -> str:
    return "Q-" + hashlib.sha256(f"{target}|{check}".encode()).hexdigest()[:8]


def scan_thesis(thesis_dir: Path) -> list[dict]:
    spec_path = thesis_dir / "spec.md"
    thesis_path = thesis_dir / "thesis.md"
    spec = spec_path.read_text(encoding="utf-8")
    thesis = thesis_path.read_text(encoding="utf-8") if thesis_path.is_file() else ""
    both = spec + "\n" + thesis
    out: list[dict] = []

    # 1 — prose wrong_if (missing metric/threshold/source)
    for m in re.finditer(r"^\*\*wrong_if\*\*:\s*(.+)$", spec, re.M):
        body = m.group(1)
        block_start = spec.rfind("### Pillar", 0, m.start())
        title = spec[block_start:spec.find("\n", block_start)].strip("# ").strip()
        missing = [k for k in ("metric=", "threshold=", "source=") if k not in body]
        if missing:
            out.append({
                "id": qid(title, "prose_wrong_if"),
                "target": title,
                "check": "prose_wrong_if",
                "question": f"Pillar \"{title}\" has a wrong_if missing {', '.join(missing)}. "
                            f"What is the intended falsifier?",
                "options": None,
                "unblocks": "spec §1b falsifier decidability (Q8 contract 4)",
            })

    # 2 — universe rows without rationale
    if "## 2. Universe Definition" in spec:
        uni = spec.split("## 2. Universe Definition")[1].split("## 3.")[0]
        for line in uni.splitlines():
            if not line.strip().startswith("|") or line.startswith("|---") or "Ticker" in line:
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 5:
                out.append({
                    "id": qid(line[:40], "universe_short_row"),
                    "target": f"universe row {cells[0] if cells else '?'}",
                    "check": "universe_short_row",
                    "question": f"Universe row for {cells[0] if cells else '?'} has fewer "
                                f"than 5 columns. What is its inclusion rationale?",
                    "options": None,
                    "unblocks": "spec §2 inclusion criteria (CHK002)",
                })
                continue
            if len(cells[4]) < 15:
                out.append({
                    "id": qid(cells[0], "universe_no_rationale"),
                    "target": f"universe row {cells[0]}",
                    "check": "universe_no_rationale",
                    "question": f"Universe row {cells[0]} has no substantive rationale. "
                                f"Why is it in scope?",
                    "options": None,
                    "unblocks": "spec §2 inclusion criteria (CHK002)",
                })

    # 3 / 4 — missing budget / expiry_triggers (either file satisfies)
    budget_in_spec = re.search(r"^\s*budget:", spec, re.M)
    budget_in_thesis = re.search(r"^\s*budget:", thesis, re.M)
    if not (budget_in_spec or budget_in_thesis):
        out.append({
            "id": qid("thesis", "missing_budget"),
            "target": "thesis.md frontmatter",
            "check": "missing_budget",
            "question": "No budget is declared. What is max_tasks for this thesis?",
            "options": ["40", "60", "70", "100"],
            "unblocks": "thesis.md budget (Q58)",
        })

    exp_in_spec = re.search(r"expiry_triggers", spec)
    exp_in_thesis = re.search(r"expiry_triggers", thesis)
    if not (exp_in_spec or exp_in_thesis):
        out.append({
            "id": qid("thesis", "missing_expiry"),
            "target": "thesis.md frontmatter",
            "check": "missing_expiry_triggers",
            "question": "No expiry_triggers declared. What should invalidate this thesis?",
            "options": ["earnings_release", "constitution_bump", "skill_version_mix",
                        "issuer_discloses_orbital_compute_revenue"],
            "unblocks": "thesis.md expiry policy",
        })

    # 5 — subscription tokens not in TICKER × skill form
    for m in re.finditer(r"^\*\*Subscribed\*\*:\s*(.+)$", spec, re.M):
        for tok in re.findall(r"`([^`]+)`", m.group(1)):
            if not re.match(r"^[A-Z][A-Z0-9.-]*\s*×\s*[a-z][a-z0-9-]*$", tok.strip()):
                out.append({
                    "id": qid(tok, "bad_subscription_token"),
                    "target": tok,
                    "check": "bad_subscription_token",
                    "question": f"Subscription token `{tok}` is not in `TICKER × skill` form. "
                                f"What did you mean?",
                    "options": None,
                    "unblocks": "spec §1b subscription parsing (Q9)",
                })

    # 6 — missing as_of / pins
    if "constitution_pin" not in both:
        out.append({
            "id": qid("spec", "missing_constitution_pin"),
            "target": "spec.md header",
            "check": "missing_constitution_pin",
            "question": "No constitution_pin declared. Which constitution version governs?",
            "options": None,
            "unblocks": "pin integrity (Q33)",
        })
    if "as_of" not in both:
        out.append({
            "id": qid("spec", "missing_as_of"),
            "target": "spec.md header",
            "check": "missing_as_of",
            "question": "No as_of date declared. What is the market-data reference date "
                        "for this thesis?",
            "options": None,
            "unblocks": "temporal consistency (CHK005)",
        })

    # 7 — pillars without priority
    for m in re.finditer(r"^### Pillar \d+ — (.+)$", spec, re.M):
        title = m.group(1)
        if "Priority:" not in title:
            out.append({
                "id": qid(title, "pillar_no_priority"),
                "target": title,
                "check": "pillar_no_priority",
                "question": f"Pillar \"{title}\" has no priority. What is it?",
                "options": ["P1", "P2", "P3", "P4", "P5"],
                "unblocks": "spec §1b pillar ordering (Q30)",
            })

    return out


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    findings = scan_thesis(Path(sys.argv[1]))
    print(json.dumps(findings, indent=2, ensure_ascii=False))
    print(f"\n{len(findings)} candidate question(s) found.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
