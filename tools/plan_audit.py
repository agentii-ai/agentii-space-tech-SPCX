#!/usr/bin/env python3
"""plan_audit.py — mechanical cross-check of a thesis spec/plan for coverage gaps.

Three invariants:

  I1  Universe ⊆ Matrix ∪ Excluded   — every ticker in the Universe Definition must
      appear in the Skill Deployment Matrix, or be explicitly excluded with a reason.
      A universe row that is in no phase is research that was scoped and then dropped.

  I2  Subscribed ⊆ Matrix            — a `TICKER × skill` pair named in a pillar's
      `**Subscribed**` line must exist as a (skill, ticker) pair in the matrix.
      Otherwise `tasks_from_spec` iterates matrix rows and the subscription silently
      generates zero tasks.

  I3  Subscribed skills resolve      — every skill named in a Subscribed line must
      exist in the skill registry, or depth_to_modes falls back to ["default"].

  I4  Matrix skills ⊆ Subscribed     — every skill in the matrix must be named in at
      least one pillar's `**Subscribed**` line. A matrix skill named nowhere gets the
      `[P1]` fallback bracket from `tasks_from_spec`, silently mis-labelling
      cross-cutting work as Minimum-Defensible-View work.
"""
from __future__ import annotations

import re
import sys
import yaml
from pathlib import Path

REGISTRY = Path("/Users/frank/.claude/plugins/marketplaces/agentii-investment-intelligence/skill-registry.yaml")


def parse_universe(spec: str) -> set[str]:
    sec = spec.split("## 2. Universe Definition")[1].split("## 3.")[0]
    out = set()
    for line in sec.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("Ticker", "--------"):
            continue
        if re.match(r"^[A-Z]{1,5}([.-][A-Z])?$", cells[0]):
            out.add(cells[0])
    return out


def parse_matrix(spec: str) -> list[tuple[str, str]]:
    sec = spec.split("## 3. Skill Deployment Matrix")[1].split("## 4.")[0]
    pairs = []
    for line in sec.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("Skill", "---"):
            continue
        skill = cells[0].strip("`")
        for t in cells[3].replace("，", ",").split(","):
            t = t.strip()
            if t and re.match(r"^[A-Z]{1,5}([.-][A-Z])?$", t):
                pairs.append((skill, t))
    return pairs


def parse_subscriptions(spec: str) -> list[tuple[str, str, str]]:
    out = []
    pil = None
    for line in spec.splitlines():
        m = re.match(r"^### Pillar (\d+)", line)
        if m:
            pil = f"PIL-{m.group(1)}"
        if pil and line.startswith("**Subscribed**"):
            for tok in re.findall(r"`([^`]+)`", line):
                if "×" in tok:
                    t, s = [x.strip() for x in tok.split("×")]
                    out.append((pil, s, t))
    return out


def main() -> int:
    spec = Path(sys.argv[1]).read_text(encoding="utf-8")
    universe = parse_universe(spec)
    matrix = parse_matrix(spec)
    subs = parse_subscriptions(spec)
    matrix_tickers = {t for _, t in matrix}
    matrix_pairs = {(s, t) for s, t in matrix}

    registry = {s["skill_name"] for s in yaml.safe_load(REGISTRY.read_text())["skills"]}

    print(f"universe: {len(universe)} | matrix pairs: {len(matrix)} | "
          f"matrix tickers: {len(matrix_tickers)} | subscriptions: {len(subs)}\n")

    fail = 0

    print("I1 — universe tickers absent from the matrix")
    orphan = sorted(universe - matrix_tickers)
    if orphan:
        fail += 1
        print(f"  FAIL — {len(orphan)} of {len(universe)} universe names appear in NO phase:")
        for t in orphan:
            print(f"      {t}")
    else:
        print("  pass")

    print("\nI2 — Subscribed pairs absent from the matrix")
    bad = [(p, s, t) for p, s, t in subs if (s, t) not in matrix_pairs]
    if bad:
        fail += 1
        print(f"  FAIL — {len(bad)} subscribed pairs generate ZERO tasks:")
        for p, s, t in bad:
            print(f"      {p}: {t} × {s}")
    else:
        print("  pass")

    print("\nI3 — Subscribed skills missing from the registry")
    bad3 = [(p, s, t) for p, s, t in subs if s not in registry]
    if bad3:
        fail += 1
        for p, s, t in bad3:
            print(f"  FAIL {p}: {t} × {s} (unknown skill)")
    else:
        print("  pass")

    print("\nI4 — matrix skills absent from every Subscribed line")
    sub_skills = {s for _, s, _ in subs}
    matrix_skills = {s for s, _ in matrix}
    orphan_skills = sorted(matrix_skills - sub_skills)
    if orphan_skills:
        fail += 1
        print(f"  FAIL — {len(orphan_skills)} skill(s) get the [P1] fallback bracket:")
        for s in orphan_skills:
            print(f"      {s}")
    else:
        print("  pass")

    print(f"\n{4-fail}/4 invariants hold.")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
