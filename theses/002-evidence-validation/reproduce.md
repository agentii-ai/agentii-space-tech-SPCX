# Reproduce — 002 Evidence Validation

> The one file an external reviewer needs. Skills + five pins + `as_of`.

## The five pins (Q33 / Q8 contract 5)

| Pin | Value | Note |
|---|---|---|
| `constitution_pin` | **1.4.0** | MINOR-amended twice on 2026-09-18: 1.2.0 → 1.3.0 (A1a/A1b, F5a/F5b/F5c, Data-Integrity Register, disposition classes) → 1.4.0 (Sector Preferences rationales restated). |
| `assumption_pin` | **2** | `assumptions.yaml` v2. Effective 2026-09-18. |
| `skill_pin` | per-artifact | `dispatch.skill_version_hash()` — true per-skill content hashes. Not a registry proxy. |
| `as_of` | **2026-09-18** | The market-data reference date. **Market Data Stage is `none` for every matrix row**, so no price is quoted live; the anchor figure is the constitution's **~$1.62T** market-cap print, which is `CLAIMED` and dated. |
| `corpus_version` | `UNPINNED` | No corpus-version endpoint is exposed by the installed plugin. Recorded as a known gap rather than a fabricated pin. |

**Pins that must travel with any artifact:** all five. An artifact missing any one is
classified `resume` (partial-write class) by `dispatch.resume_verdict` and silently
re-run — the filesystem is the checkpoint (Q56), so a missing pin is a correctness bug,
not a cosmetic one.

## Skills deployed

| Skill | Depth | Tickers | Mode set |
|---|:---:|---|---|
| `unit-economics` | Deep | RKLB, SPCX | all modes (**5**) |
| `operational-kpi` | Deep | SPCX, RKLB, YSS | all modes (**5**) |
| `secular-trends` | Deep | BWXT, GOOG, NVDA, MRCY | all modes (**8**) |
| `recent-quarter` | Standard | all 17 universe names | essentials (**3**: `margin-analysis`, `earnings-vs-consensus`, `consolidated-p-and-l`) |
| `ratio-analysis` | Standard | SPCX, RKLB, VRT, GOOG | essentials |
| `unit-economics` | Standard | VRT, UTHR, FLY | essentials |
| `risk` | Standard | SATS, SPCX | essentials |
| `competitive` | Light | IRDM, SATS | essentials, min scope |
| `business-model` | Light | SPCX | essentials, min scope |
| `supply-chain` | Light | BWXT, MRCY | essentials, min scope |

**40 `(ticker, skill)` pairs → 132 mode-tasks** (expansion **3.30×**). Coverage:
**17 / 17 universe tickers.**

## What an external reviewer must be able to do

1. **Resolve every citation.** Each `citations[].url` must open
   `https://agentii.ai/v/{ticker}/{citation_id}/{N}` and land on the cited page. The
   URL form is canonical — **the ticker is mandatory**; a ticker-less route cannot
   perform the `src_documents JOIN sec_filings` join the portal requires.
2. **Recompute every `operating_income` from components.** `gross profit − opex` must
   equal the quoted figure. **`EPS × shares` is NOT an admissible sign test** — it passes
   on both sides of a flip at RKLB, FLY and VOYG (constitution, Data-Integrity Register).
3. **Re-derive each break-even multiple** as `opex ratio ÷ gross margin`.
4. **Re-run the audit:** `python3 tools/plan_audit.py theses/002-evidence-validation/spec.md`
   → expects **4/4 invariants**.

## Reproducibility limits — stated, not papered over

| Limit | Consequence |
|---|---|
| **`corpus_version` is `UNPINNED`** | Retrieval is live, not snapshotted. A reviewer running this later may get different source documents if the platform re-ingests. Nearest freshness markers: `list_domains` **2026-08-26**, `list_sources` **2027-04-12**. |
| **Market Data Stage is `none`** | No price is reproducible. Nothing in this thesis depends on a live quote — but the ~$1.62T anchor is a dated print. |
| **`agentii.plan`, `agentii.clarify` and `agentii.implement` are not implemented as scripts** in the installed plugin (only `specify`, `tasks`, `constitution` are). | The plan, the clarify rounds and the dispatch are **hand-authored against the SKILL.md methodology**, not generated. `tools/clarify_scan.py` is a local implementation of the documented scan. |
| **The task generator emits mis-bracketed pillars** (79 of 132, 60%) | `tasks.md` must be produced via a parameterized `tools/gen_tasks_md.py`, **not** raw `agentii_cmd.py tasks`. See `plan.md` for the measurement. |

## Reproduction recipe

```bash
# 1. Audit the spec's internal consistency
python3 tools/plan_audit.py theses/002-evidence-validation/spec.md      # expect 4/4

# 2. Generate the raw task list (note: brackets will be wrong — see plan.md)
python3 scripts/agentii_cmd.py tasks \
  --thesis theses/002-evidence-validation/thesis.md \
  --spec   theses/002-evidence-validation/spec.md

# 3. Re-attribute brackets and phase the list  [PREREQUISITE — not yet parameterized]
python3 tools/gen_tasks_md.py --thesis theses/002-evidence-validation   # currently 001-hardcoded

# 4. Verify a citation resolves to the cited page
#    read_source_pages(ticker="SPCX", citation_id="sec8", pages="page43")
#    -> must return the Connectivity segment table: revenue $4,291M, income from ops $1,656M
```

## Report build — letter-size HTML + PDF (spec 046 Q46–Q50)

**Run from the kit's working tree, not this repo**, and not from the marketplace copy —
`render_report.py` is absent from the marketplace skill tree.

```bash
cd /Users/frank/A/agenzym/agentii-investment-intelligence
T=/Users/frank/B/agentii-space-tech-SPCX/theses/002-evidence-validation

# 1. PACK — bundles every source verbatim, emits report/metrics.json
rm -f "$T/report-input.md" "$T/report/metrics.json"     # see ⚠️ 1 below
python3 scripts/synthesize_report.py pack --thesis "$T"

# 2. AUTHOR — the LLM writes report/content.html (not scriptable; see SKILL.md)
#    Fragment only: <section class="page"> blocks; no cover, no disclaimer, no
#    reserved classes, no <img>. ≤40 prose lines and ≤18 table rows per page.

# 3. ASSEMBLE — deterministic; template injection, Q50 pins, Q47 overflow gate
rm -f "$T/thesis-report.html"                           # see ⚠️ 1 below
python3 scripts/synthesize_report.py assemble --thesis "$T" --check-only   # fit loop
python3 scripts/synthesize_report.py assemble --thesis "$T"

# 4. RENDER — Chrome headless → letter PDF → per-page PNGs at 192 dpi
rm -f "$T/report/pages/thesis-report.pdf"
python3 scripts/render_report.py render --thesis "$T" --keep-pdf --verify

# 5. PLACE — both copies, matching 001
cp "$T/report/pages/thesis-report.pdf" "$T/Evidence Validation — agentii Thesis Report.pdf"
```

**⚠️ 1 — `--keep-pdf` is mandatory, and two `rm -f` steps are not optional.**
`render_report.py` writes the PDF to a temp dir and copies it in **only** under
`--keep-pdf`; without the flag the PDF is silently discarded and the PNGs still
look correct. Separately, `pack` and `assemble` both call `write_boundary.write()`
and **discard its return value**, so a `refused` write prints `OK` and produces
nothing. The refusal is Q127's fail-safe firing on a file that declares no
`writer:` (APPEND-ONLY) when the write *rewrites* rather than appends — which is
exactly what a re-pack or a re-assemble is. **Every rebuild after the first is a
silent no-op without the `rm`.** Verify by mtime, never by the `OK`:

```bash
stat -f "%Sm %N" -t "%H:%M:%S" "$T/thesis-report.html" "$T/report/content.html"  # html must be newer
```

**⚠️ 2 — the cover's `claim:` must occupy exactly one line in `spec.md`.**
`synthesize_report.py:133` extracts it with `^\*\*Claim\*\*:\s*(.+)$` under
`re.MULTILINE`, and `.+` does not cross a newline, so a wrapped claim ships
**truncated mid-sentence** on the cover. The first build of this report did
exactly that. Note also that `spec.md` is **not** in `SOURCE_GLOBS`
(`artifacts/**`, `_cross/**`, `snapshots/**`) — so the claim, pins and universe
the cover displays are read from `spec.md` but not covered by `sources_hash`.

**Verification of a good build** — all four must hold:

```bash
pdfinfo "$T/report/pages/thesis-report.pdf" | grep -E "^Pages|^Page size"   # 13 · 612 x 792 pts (letter)
file "$T/report/pages/page-01.png"                                          # 1632 x 2112 (letter @ 192 dpi)
grep -o 'data-overflow-check="[^"]*"' "$T/thesis-report.html"               # must read "engine", not "approximate"
ls "$T"/*.pdf "$T/report/pages"/*.pdf                                       # 2 copies
```

`data-overflow-check` is the one to insist on: the ±5% estimator passed five
genuinely overflowing pages before the engine probe replaced it (Q99/Q105), and a
report must never imply a precision it did not have.



**Step 3 is the open prerequisite.** `tools/gen_tasks_md.py` carries the correct
`(ticker, skill)` attribution logic but is hard-coded to `theses/001-technology-baseline`
at module level. Parameterizing it is required before this thesis's `tasks.md` can be
written — without it, 60% of tasks carry the wrong pillar bracket and `dispatch` reads
that bracket.
