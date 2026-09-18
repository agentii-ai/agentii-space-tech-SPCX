# Reproduce — 001 Technology Baseline

> Q8 contract 5 / Q36: the thesis-level reproduction recipe — the ONE file an
> external reviewer (compliance, LP, a new analyst) needs. Every artifact's
> frontmatter carries its own pins; this file aggregates them.

## Skills used

| skill | mode | vertical | depth |
|---|---|---|---|
| operational-kpi | all modes (`triggers`, `defaults`, `methodology`, `retrieval-scope`, `retrieval-strategy`) | business-intelligence | Deep — SPCX |
| operational-kpi | `essentials_modes` | business-intelligence | Standard — RKLB, FLY, YSS, TER |
| unit-economics | all modes | business-intelligence | Deep — SPCX |
| unit-economics | `essentials_modes` | business-intelligence | Standard — RKLB, UTHR, VRT |
| secular-trends | all modes | equity-research-core | Deep — GOOG |
| secular-trends | `essentials_modes` | equity-research-core | Standard — NVDA, MSFT, BWXT |
| supply-chain | `essentials_modes` | industry-analysis | Standard — RKLB, BA, KRMN |
| what-if | `essentials_modes` | business-intelligence | Standard — SPCX, GOOG |
| business-model | `essentials_modes` | equity-research-core | Standard — SPCX, RKLB, GOOG, UTHR |
| competitive | `essentials_modes` | equity-research-core | Standard — SPCX, RKLB, IRDM, SATS, GSAT |
| risk | `essentials_modes` | equity-research-core | Standard — SPCX, BWXT, SATS, IRDM |
| recent-quarter | `essentials_modes` | equity-research-core | Standard — SPCX, GOOG |
| sector-overview | `essentials_modes` | industry-analysis | Standard — SPCX |
| peer-bench | `essentials_modes` | industry-analysis | Standard — SPCX, RKLB |
| ratio-analysis | `essentials_modes` | quantitative-analysis | Light — SPCX |

**`skill_pin` — RESOLVED 2026-09-18.** The registry carries no per-skill hash, but
`dispatch.skill_version_hash()` computes the specified **content hash of the skill
directory** (`SKILL.md` + `references/`). The earlier whole-registry proxy is replaced
with real per-skill hashes:

| skill | version_hash |
|---|---|
| operational-kpi | `0730fd170124` |
| unit-economics | `e87ee63269a2` |
| secular-trends | `e6b41dbb2426` |
| supply-chain | `8cb3ac1de486` |
| competitive | `826995c722a4` |
| risk | `953fc5d396e7` |

Remaining skills hash on first use and are **appended** to `skill_pins.jsonl` (Q57 —
never overwritten). A version change mid-thesis uses the new hash and appends.

**`corpus_version` remains `UNPINNED`.** No corpus-version endpoint exists. It is
nonetheless one of `g1_gate.FIVE_PINS`, so it must be *present* in every artifact
frontmatter — `"UNPINNED"` is the honest value. An artifact missing it is classified
`resume` and silently re-run.

## Pins at generation

| pin | value |
|---|---|
| `constitution_pin` | **1.2.0** (`constitution.md` sha256 `857abf808f8007c1`) |
| `assumption_pin` | `assumptions.yaml` version 2 (sha256 `0d0264e58a736568`) |
| `as_of` | **2026-09-18** (provisional — Clarification Q-5) |
| `skill_pin` | registry version 1.0.0, sha256 `873734a747422b84` *(proxy — see caveat)* |
| `corpus_version` | **UNPINNED** — no corpus-version endpoint exposed; see `brief.md` |
| `spec_pin` | `spec.md` sha256 `6e904e3fba97630a` |

## Cited prices (evidence)

**None.** This thesis cites no prices. It sizes no positions and makes no trade
recommendation, so the Q71 `observed_at` / `evidence/quotes/` mechanism is unused.
That is a deliberate scope decision from `spec.md §1`, not an unfinished section.

For any downstream thesis that *does* trade this universe, the price-citation
obligation attaches there — this file is not the place it should be satisfied.

## Reproducing this thesis from scratch

1. Restore `constitution.md` at sha256 `857abf808f8007c1` and confirm
   `constitution_ratified()` returns `True`.
2. Confirm `assumptions.yaml` version 2 (sha256 `0d0264e8…`).
3. Regenerate the task set:
   `python3 scripts/agentii_cmd.py tasks --thesis theses/001-technology-baseline/thesis.md --spec theses/001-technology-baseline/spec.md`
   → expect **78 tasks** at 6 pillars.
4. Re-run the universe coverage audit — the snapshot in `constitution.md` is dated
   2026-09-18 and will drift. Per-ticker `get_ticker_coverage`, all seven source types.
5. Re-run `tools/clarify_scan.py theses/001-technology-baseline` → expect 0 candidates.

**What cannot be reproduced by retrieval.** Because the knowledge base contains no
space-domain strategies or cases (`brief.md`), an external reviewer cannot reconstruct
this thesis's *method* by pulling a strategy id. The reproducible unit is instead the
constitution's F1–F6 physics derivations plus the cited SEC accessions — which is why
those are pinned here and in `entities.md` rather than a strategy identifier.
