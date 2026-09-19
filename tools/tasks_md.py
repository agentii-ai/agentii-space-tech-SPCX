#!/usr/bin/env python3
"""tasks_md.py — generic `tasks.md` generator for any thesis in this workspace.

Supersedes `tools/gen_tasks_md.py`, which is hard-coded to `theses/001-technology-baseline`
and whose convergence sections are 001's own history (they must not be copied forward).

It performs three things the platform's `agentii_cmd.py tasks` does not:

  1. **Re-attributes pillar brackets from `(ticker, skill)`.** The platform's
     `_pillars_of_skills` keys by SKILL ONLY, so every task for a skill inherits the
     union of all pillars subscribing that skill anywhere. Measured at 57/103 (55%) on
     001 and ~60% on 002 — a property of the shared plugin, not of any thesis.

  2. **Files each task under the phase of its FIRST pillar** per a supplied map. The
     platform emits no phase at all.

  3. **Verifies per-`(ticker, skill)` coverage after generation and FAILS LOUDLY** if a
     pair present in the matrix produced zero tasks. This is the I2 / E4 silent-drop
     class: a matrix row and a subscription mismatch produces *no error and no task* —
     the work simply never happens. It caught a real regression during 002's plan
     evaluation, where splitting a matrix row left BWXT with zero tasks.

Usage
-----
  python3 tools/tasks_md.py --thesis theses/002-evidence-validation \
      --phases "PIL-1:1,PIL-2:2,PIL-3:3,PIL-4:4,PIL-6:4,PIL-7:5,PIL-5:6"

`--phases` may be omitted if `<thesis>/phases.yaml` exists (see PHASES_FILE schema below).
Exit code is non-zero on any verification failure.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMD = Path.home() / (".claude/plugins/marketplaces/agentii-investment-intelligence"
                     "/scripts/agentii_cmd.py")

BRACKET = re.compile(r"\[(PIL-[0-9]+(?:/PIL-[0-9]+)*)\]")
PAIR = re.compile(r"^- \[.\] T\d+.*?\] (\S+) × ([a-z0-9-]+) × ([a-z0-9-]+)")
MATRIX_ROW = re.compile(r"^\| ([a-z-]+) \| [a-z-]+ \| (\w+) \| ([^|]+) \|")

PHASES_FILE = """\
# phases.yaml — pillar -> phase for tools/tasks_md.py
# schema:  phases: {PIL-N: <int>};  names: {<int>: "<label>"};  depends: {<int>: "<text>"}
"""

# --- mode differentiation ----------------------------------------------------
# The platform copies the skill's Purpose cell verbatim onto every mode of a pair, so
# five modes of `unit-economics` arrive with five IDENTICAL descriptions. Measured on
# 002: 112 tasks carried 11 distinct purposes. 001 had the same defect.
#
# These clauses are appended per mode. The generic five are the shared *methodology
# sections* of any analysis — what would overturn it, what was assumed, how it was
# derived, what was in scope, how the sources were found. The domain overrides name
# what the mode actually tests in THIS workspace.
MODE_CLAUSE = {
    "triggers":           "· mode: the trigger set — what would overturn this conclusion",
    "defaults":           "· mode: the default assumptions used where no filed figure exists",
    "methodology":        "· mode: the derivation path, stated so the number is reproducible",
    "retrieval-scope":    "· mode: which sources are admitted and which are excluded",
    "retrieval-strategy": "· mode: how the sources were located, so the search repeats",
    "consolidated-p-and-l": "· mode: the income statement — the DA-23 SIGN TEST runs here",
    "margin-analysis":      "· mode: margin structure — the DA-26/DA-27 PERIOD TRAPS bite here",
    "default":            "",
}


def cross_tasks(spec_text: str) -> list[str]:
    """Emit one task per `_cross/` artifact named in the spec.

    The platform generator emits only `ticker × skill × mode` rows and has **no concept
    of a cross-cutting task** — 001 documented this and hand-added its synthesis task;
    002 inherited the same gap. Parsing the Output Contract is the general fix: any
    thesis that names a `_cross/` artifact gets a task pointing at it.

    Cross tasks are NEVER `[P]` (skill contract): they depend on every prior phase.
    """
    out, seen = [], set()
    # SCOPE: the Output Contract section ONLY. Scanning the whole spec picks up 001's
    # inherited artifacts (`_cross/phase-2-constraint-envelope.md` appears in 002's
    # Inherited baseline table as a *citation*, not as this thesis's deliverable) —
    # and emitting a task for another thesis's artifact is worse than emitting none.
    m = re.search(r"^## 6\. Output Contract(.*?)^## 7\.", spec_text, re.S | re.M)
    section = m.group(1) if m else ""
    for mm in re.finditer(r"`_cross/([A-Za-z0-9._-]+\.md)`", section):
        name = mm.group(1)
        if name not in seen:
            seen.add(name)
            out.append(name)
    return out


def pair_pillars(spec_text: str) -> dict[tuple[str, str], list[str]]:
    """`(ticker, skill) -> [pillars]`, from the `Subscribed` lines under each Pillar heading."""
    out: dict[tuple[str, str], list[str]] = {}
    pil = None
    for line in spec_text.splitlines():
        m = re.match(r"^### Pillar (\d+)", line)
        if m:
            pil = f"PIL-{m.group(1)}"
        if pil and line.startswith("**Subscribed**"):
            for tok in re.findall(r"`([^`]+)`", line):
                if "×" in tok:
                    t, s = (x.strip() for x in tok.split("×"))
                    out.setdefault((t, s), [])
                    if pil not in out[(t, s)]:
                        out[(t, s)].append(pil)
    return out


def matrix_pairs(spec_text: str) -> set[tuple[str, str]]:
    """`(ticker, skill)` pairs declared in the spec's Skill Deployment Matrix."""
    sec = spec_text.split("## 3. Skill Deployment Matrix")[1].split("\n## ")[0]
    out: set[tuple[str, str]] = set()
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("Skill", "---"):
            continue
        skill = cells[0].strip("`")
        for t in cells[3].replace("，", ",").split(","):
            t = t.strip().strip("`")
            if re.fullmatch(r"[A-Z][A-Z0-9.\-]{0,6}", t):
                out.add((t, skill))
    return out


def parse_phases(spec: str) -> tuple[dict[str, int], str | None]:
    m = re.search(r"phases:\s*\{([^}]*)\}", spec)
    if not m:
        return {}, None
    out = {}
    for tok in m.group(1).split(","):
        if ":" in tok:
            k, v = tok.split(":")
            out[k.strip()] = int(v.strip())
    n = re.search(r"names:\s*\{([^}]*)\}", spec)
    return out, (n.group(1) if n else None)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--thesis", required=True, help="thesis directory")
    ap.add_argument("--phases", default=None,
                    help='e.g. "PIL-1:1,PIL-2:2,PIL-3:3,PIL-6:4" (overrides phases.yaml)')
    ap.add_argument("--declared-na", default="",
                    help="comma-separated SKILL:MODE_PREFIX pairs declared N/A")
    args = ap.parse_args()

    d = (ROOT / args.thesis) if not Path(args.thesis).is_absolute() else Path(args.thesis)
    spec_text = (d / "spec.md").read_text(encoding="utf-8")

    # --- phase map -----------------------------------------------------------
    if args.phases:
        ph_of = {k.strip(): int(v) for k, v in
                 (t.split(":") for t in args.phases.split(","))}
    elif (d / "phases.yaml").is_file():
        ph_of, _ = parse_phases((d / "phases.yaml").read_text(encoding="utf-8"))
    else:
        ph_of = {}
    if not ph_of:
        print("ERROR: no phase map. Pass --phases or add phases.yaml.", file=sys.stderr)
        return 2

    na = {}
    for tok in filter(None, (t.strip() for t in args.declared_na.split(","))):
        s, _, pre = tok.partition(":")
        na.setdefault(s, []).append(pre)

    # --- generate ------------------------------------------------------------
    raw = subprocess.run(
        [sys.executable, str(CMD), "tasks",
         "--thesis", str(d / "thesis.md"), "--spec", str(d / "spec.md")],
        capture_output=True, text=True, check=True).stdout.strip().splitlines()
    lines = [l for l in raw if l.startswith("- [ ]")]

    correct = pair_pillars(spec_text)
    matrix = matrix_pairs(spec_text)

    buckets: dict[int, list[str]] = defaultdict(list)
    true_load: dict[int, int] = Counter()
    pairs_seen: dict[tuple[str, str], int] = Counter()
    reattributed = declared_na = 0
    for line in lines:
        m, b = PAIR.match(line), BRACKET.search(line)
        if m:
            key = (m.group(1), m.group(2))
            pairs_seen[key] += 1
            want = correct.get(key)
            if want and b and set(want) != set(b.group(1).split("/")):
                line = line[:b.start()] + "[" + "/".join(want) + "]" + line[b.end():]
                reattributed += 1
                b = BRACKET.search(line)
            clause = MODE_CLAUSE.get(m.group(3))
            if not clause:
                for pre, cl in MODE_CLAUSE.items():
                    if cl and m.group(3).startswith(pre):
                        clause = cl
                        break
            if clause and "(src:" in line:
                line = line.replace("(src:", f"{clause} (src:", 1)
            if any(m.group(3).startswith(p) for p in na.get(m.group(2), [])):
                declared_na += 1
                line += "  ⚠️ DECLARED N/A — see plan.md §Declared-N/A Register"
            first = want[0] if want else (b.group(1).split("/")[0] if b else None)
            # TRUE load: a task serves EVERY pillar in its bracket, not just the first.
            # The gap is not cosmetic — on 002 it made Phase 4 read 3 against 23 real.
            for p in (want or [b.group(1).split("/")[0]] if b else []):
                true_load[ph_of.get(p, max(ph_of.values(), default=1))] += 1
        else:
            first = b.group(1).split("/")[0] if b else None
        buckets[ph_of.get(first, max(ph_of.values(), default=1))].append(line)

    # --- verify: every matrix pair produced at least one task (I2 / E4 class) --
    orphans = sorted(matrix - set(pairs_seen))
    ghosts = sorted(set(pairs_seen) - matrix)

    print(f"matrix pairs {len(matrix)} | generated pairs {len(pairs_seen)} | "
          f"tasks {len(lines)} | re-attributed {reattributed} | declared N/A {declared_na}")
    if orphans:
        print(f"\n!! FAIL — {len(orphans)} matrix pair(s) produced ZERO tasks "
              f"(silent work loss):", file=sys.stderr)
        for t, s in orphans:
            print(f"     {t} × {s}", file=sys.stderr)
    if ghosts:
        print(f"\n!! WARN — {len(ghosts)} pair(s) generated tasks but are NOT in the matrix:",
              file=sys.stderr)
        for t, s in ghosts:
            print(f"     {t} × {s}", file=sys.stderr)
    if orphans:
        return 1

    # --- emit ----------------------------------------------------------------
    L = [f"# Research Tasks: {d.name}\n"]
    L.append("> **APPEND-ONLY (Q26)**: never rewritten, renumbered, reordered or deleted")
    L.append("> from. `[x]` is written by `agentii.implement` and is a display hint —")
    L.append("> `agentii.converge` evaluates artifact state, not `[x]`. Corrections arrive as")
    L.append("> appended `## Phase N: Convergence` sections.\n")
    L.append("Task format: `- [ ] T### [P] [pillar] TICKER × SKILL × MODE — purpose (src: …)`\n")
    L.append("- **Brackets are re-attributed from `(ticker, skill)`** — the platform keys by")
    L.append("  skill only, so ~60% arrive wrong. See `plan.md`.")
    L.append("- **Phase = the FIRST pillar in the bracket.** Multi-pillar tasks serve every")
    L.append("  pillar listed; phase is a filing heuristic, not a scope limit.")
    L.append("- **A task's phase does not bound its scope.** A `[PIL-1/PIL-4/PIL-6]` task")
    L.append("  filed under Phase 1 does Phase 4 work too.\n")
    dedup = " · ".join(f"{k}:{v}" for k, v in sorted(ph_of.items()))
    # The date was HARDCODED as 2026-09-18 and never advanced — so a file regenerated
    # on the 19th still claimed the 18th, and every thesis carried the same stale stamp.
    # Read it from the clock instead. (The `{len(lines)}` count was already dynamic.)
    _gen_date = datetime.now().strftime("%Y-%m-%d")
    L.append(f"**Generated** {_gen_date} · **{len(lines)} tasks** · phase map {dedup}")
    tot_na = f" · **{declared_na} declared N/A**" if declared_na else ""
    L.append(f"· re-attributed **{reattributed}** brackets{tot_na}\n")
    L.append("| Phase | Filed here | **True load** |")
    L.append("|:---:|---:|---:|")
    for p in sorted(buckets):
        gap = true_load[p] - len(buckets[p])
        flag = f" **← +{gap} more**" if gap else ""
        L.append(f"| {p} | {len(buckets[p])} | **{true_load[p]}**{flag} |")
    L.append(f"| **Total** | **{sum(len(v) for v in buckets.values())}** | "
             f"**{sum(true_load.values())}** |\n")
    L.append("> **Filed-here counts UNDERSTATE the work whenever a pillar's tasks are")
    L.append("> carried by pairs whose first pillar is something else.** A task bracketed")
    L.append("> `[PIL-1/PIL-4/PIL-6]` is *filed* under Phase 1 but *serves* Phases 1, 4 and 4.")
    L.append("> **Plan the schedule off True load, not Filed here.** On 002 the gap reaches")
    L.append("> 8× — Phase 4 files 3 tasks while carrying 23 — because the entity-boundary")
    L.append("> pillar is entirely fed by SPCX pairs that name PIL-1 first.\n")
    L.append("---\n")
    for p in sorted(buckets):
        L.append(f"## Phase {p}\n")
        L.extend(buckets[p])
        L.append("")

    # --- cross-cutting tasks (hand-emitted; the platform cannot produce these) -----
    xs = cross_tasks(spec_text)
    if xs:
        last = max(buckets) + 1
        L.append(f"## Phase {last} — Cross-cutting\n")
        L.append("> ⚠️ **Hand-emitted by `tools/tasks_md.py`.** The platform generator emits only")
        L.append("> `ticker × skill × mode` rows and has **no concept of a cross-cutting task** —")
        L.append("> 001 documented this gap and hand-added its synthesis task every time. These are")
        L.append("> parsed from the spec's Output Contract. **Never `[P]`** (skill contract): a")
        L.append("> `_cross/` artifact depends on every prior phase.\n")
        base = 900
        for i, name in enumerate(xs):
            primary = " 🔴 **PRIMARY ARTIFACT**" if i == 0 or "ledger" in name else ""
            # ⚠️ `[cross]`, NOT `[PIL-cross]`. Fixed 2026-09-19. The pillar enum in
            # `contracts/artifact-frontmatter.yaml` is [PIL-1..PIL-6, cross] — there is no
            # `PIL-cross`, so the old string named a pillar that does not exist and that
            # `check_contract.py`'s `da_id_registered`/enum checks would reject if it ever
            # reached an artifact's frontmatter. It shipped in thesis 002 (3 tasks) and
            # 003 (2 tasks) before being caught; `[cross]` appeared nowhere in the workspace.
            L.append(f"- [ ] T{base+i} [cross] cross × synthesis × default — "
                     f"publish `_cross/{name}`{primary}  "
                     f"⚠️ hand-emitted; not `[P]` (src: spec-§6 Output Contract)")
        L.append("")
    L.append("<!-- agentii.converge appends below this point; never edit above it -->")
    L.append("")
    (d / "tasks.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {d / 'tasks.md'}")
    if xs:
        print(f"  cross-cutting tasks hand-emitted: {len(xs)} -> {', '.join(xs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
