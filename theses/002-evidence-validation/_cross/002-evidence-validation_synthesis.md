---
thesis_id: "002-evidence-validation"
artifact: evidence-validation-synthesis
pillar: [PIL-1, PIL-2, PIL-3, PIL-4, PIL-5, PIL-6, PIL-7]
ticker: cross
skill: synthesis
mode: default
task: T903
generated_at: 2026-09-19T09:40:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
schema: evidence_validation_synthesis
schema_version: 1
evidence_grade: DERIVED
tickers_covered: [SPCX, RKLB, MRCY, UTHR, IRDM, SATS, GOOG, MSFT, NVDA, VRT, VOYG, FLY, BA, BWXT, HAWK, LUNR, YSS]
verdicts: {FALSIFIED: 1, HOLDS: 2, UNRESOLVABLE-FROM-PLATFORM: 3, UNRESOLVABLE-FROM-PUBLIC-SOURCES: 1}
definitions_used:
  - da_id: DA-23
    chosen_reading: "sign stripping at the platform's extraction layer — 14 of 17 issuers exhibit it; recompute from components before any use"
  - da_id: DA-29
    chosen_reading: "defective checks — a reconciliation that closes is not thereby a check; if any term appears nowhere in the source it is a back-solve"
  - da_id: DA-30
    chosen_reading: "two bases on one concept collapsed with no basis field — prior to, and not dischargeable by, the artifact contract's no_single_basis_collapse rule"
citations:
  - figure: "RKLB Q2 2026 filed cells, three months ended 2026-06-30 — the source of the served-vs-filed operating-income contradiction this synthesis rests on"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 6
    url: "https://agentii.ai/v/RKLB/sec109/6"
    located_via: read_source_pages
---

# Evidence Validation — Synthesis of Thesis 002

> **Why this file exists.** Thesis 002's `_cross/` deliverables were written as
> `{name}.md` — `validation-ledger.md`, `f2-constant-sourcing.md`,
> `spcx-nameplate-and-boundary.md` — none of which match the report packer's body glob
> (`_cross/*_synthesis.md`). **The packer's hash glob is wider (`_cross/**/*.md`), so the
> ledger counted toward the hash while being excluded from the body** — the report would
> have been built without its own primary artifact. Thesis 001 lost 3 of its 5 `_cross`
> files to the same mismatch. This synthesis is written in the matching form, and it also
> supplies the cover's `constitution_pin` and `as_of`, which the packer reads from the
> newest `_cross/*_synthesis.md`.

---

## 1. The headline: thesis 002 falsified its own pillar

**PIL-5 — *"at least half of 001's headline figures convert from `CLAIMED`/`MODELED` to
`DEMONSTRATED`"* — is partially falsified.** The falsifier is
`share_of_001_headline_figures_converted_to_DEMONSTRATED < 0.5`, and **the denominator is
unstated in the spec.** Rather than choose the reading that passes, the ledger publishes a
nine-reading ladder:

| Reading (denominator named) | Rows | Converted | Share | vs 0.5 |
|---|---:|---:|---:|---|
| All six headline lines | 6 | 3 | **0.5000** | not below — **zero margin** |
| same, CHK004-strict (Line 2 out) | 6 | 2 | **0.3333** | **TRIGGERED** |
| six + the `12.3%` claim | 7 | 3 | **0.4286** | **TRIGGERED** |
| the four value-bearing lines | 4 | 3 | 0.7500 | not below |
| same, CHK004-strict | 4 | 2 | **0.5000** | **zero margin** |
| every numeric claim in 001's register | 27 | 0–21 | **[0.0000, 0.7778]** | **UNRESOLVED** |
| SPCX — value / +components / +basis | 12 | 10/6/3 | 0.8333 / 0.5000 / **0.2500** | **TRIGGERED** |
| SPCX incl. null slot | 13 | 10/6/3 | 0.7692 / **0.4615** / **0.2308** | **TRIGGERED** |
| GOOG — cells / series | 140/14 | 79/2 | 0.5643 / **0.1429** | **TRIGGERED** |

**Nine readings: four fire; three land exactly on the threshold with zero margin.** The
register reading is **inert by 78%** — 21 of 27 claims are already `DEMONSTRATED` and cannot
move, so its uncertainty band is wider than the threshold distance.

**The finding worth more than the number: converting a figure to `DEMONSTRATED` does not
convert its BASIS.** The two come apart by **46.47 percentage points on a single ratio** —
SPCX `operating_margin` is an AI-segment loss divided by consolidated revenue, turning a
filed **−16.68%** into a platform-served **+29.79%**. **A figure can be reproduced exactly
from filed cells and still not be the quantity its label names.**

**This implies that `DEMONSTRATED` is not a sufficient grade for an input.** A downstream
thesis citing 002's validated set must carry **the basis as well as the grade**, or it
inherits a figure that reproduces and means something else. That is the single change with
the widest blast radius in the programme, and it **points to** every thesis from 003 onward
restating its inputs.

## 2. What survived — 001's arithmetic largely held

001's **numbers are mostly right; several of its labels are wrong.** Per-ticker arithmetic
reproduced in every case examined:

- **IRDM** — `225,237 − 191,229 = 34,008`; `50,258/216,906 = 23.17%`; `+3.84%`. Correct.
- **MRCY** — revenue `$983.6M/$912.0M/+7.9%` and R&D `$59.7M/$67.6M/−11.7%` reproduced exactly.
- **UTHR** — all ten per-ticker figures reproduce (`−1.917%`, `−9.246%`, `+9.179%`, `+7.593%`,
  `+13.417%`, `42.23%/45.64%`, `18.68%`, 7% weight).
- **SPCX** — `$15.0B` reproduces exactly; the `$(1,257)M` AI operating line is **filed**.

**What failed is the clearance and the labelling, not the sums.** And the labels are what
downstream theses price.

## 3. The defect register

**DA-23 sign stripping is a census of a default, not a rare defect: 14 of 17 issuers exhibit
it.** It is a defect in the *platform's* extraction layer — a filed negative served as a
positive of identical magnitude. At RKLB Q2 2026 the served `OperatingIncomeLoss` is
`+57,514,000` against a filed `(57,514)` thousand, where the components give
`84,576,000 − 142,090,000 = −57,514,000` — the filed cells are at
[📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6). **Any screen on the raw field
inverts: the worst loss-makers rank at the top.**

Corrections to the register carried by this thesis: the `Clean` row is **subtotal-level
only** and **MRCY, UTHR and SATS were removed from it**; **NVDA is `UNEVIDENT`** (zero
negatives — the test can neither pass nor fail); **VRT is `UNEXERCISED`**; **BWXT and VRT are
clean at subtotals and stripped elsewhere on the statement**; **DA-26's count moved 19 → 20
with its universality falsified** (FLY is a counterexample); and **DA-24's defining instance
is an inverted impairment, not a sale — its independence proof withdrawn.**

### The census, per issuer

Legend: **C** CONFIRMED · **K** CLEAN (subtotal-level only) · **R** REFUTED · **N** NOT
TESTABLE · **U** UNEXERCISED · **E** UNEVIDENT · **P** PRESENT (unregistered class or
adjacent mechanism) · **V** UNVALIDATED-BY-PLATFORM · **X** not engaged.

| Issuer | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|
| **BA** | C ×2 | P | P | P | N/A-checked | N/A + P | X | X |
| **BWXT** | **C at component / K at subtotal** | P | R | X | N-A by construction | X | X | **defining instance** |
| **FLY** | **C 4/4, 15/15** | R | R | **R — falsifies universality** | R | C | X | X |
| **GOOG** | **K on issuer / C on instrument** | C on NI ratios / R on operating | N (kind 7) | C ×2 | N (kind 7) | C | X | C |
| **HAWK** | **C 5/6** | R | P | N (no 10-K) | N/A-checked | **C site / R mechanism** | X | X |
| **IRDM** | **K scoped; 001 clearance REFUTED** | R | **N — kind 5** | C ×2 | R | **N — kind 6** | P | P |
| **LUNR** | **C** | R | R | C | N-A by construction | X | X | X |
| **MRCY** | **C 11/13** | R | R | C | **C + self-contradiction** | R | **P** | R |
| **MSFT** | **C — "the default"** | R | X | C | **C + third source value** | X | **C** | P |
| **NVDA** | **E income / P cash-flow** | R | R | P 3/3 | **P 11/11** | N/A + P | **C** | **C** |
| **RKLB** | **C (two regimes)** | E | X | C ×2 | **N — kind 4** | U / P | P | P |
| **SATS** | **C 12/12** | **R recorded / C INVERTED** | R | C 4/4 | **N — kind 4** | **N — kind 2** | **P + new kind** | C ×4 |
| **SPCX** | **C 7/7** | R | C | **N (no annual row)** | C method | **C as open exposure** | **F + P** | **C, quantified** |
| **UTHR** | **C 11/11 component** | R | X | R | X | X | P | **9 sites** |
| **VOYG** | **C** | X | R | R | N/A | **P — promoted** | X | X |
| **VRT** | **C cash-flow / U income** | R | **N — no object** | C (Q4) | **N — kind 4** | R | **C** | C |
| **YSS** | **C (FLIPPED)** | X | **C ×2** | **N — kind 1** | C method | **C — cleanest** | X | X |

**Counts.** **DA-23: 14 of 17 issuers carry an exhibited instance**; 2 clean at subtotal level
only (GOOG, IRDM); 1 UNEVIDENT (NVDA); 1 UNEXERCISED (VRT on the income statement). **This is
not a census of a rare defect — it is a census of a default.** **DA-24: 4 exhibited or
present, 1 unevident, 11 refuted or clean.** **DA-25: 8 confirmed or present, 5 refuted, 2
not testable with named kinds.** **DA-26: 9 confirmed, 4 not testable, 1 falsifies
universality** (FLY). **DA-27: 6 confirmed, 5 not-testable with kind 4, 4 not
applicable/refuted.** **DA-28: 8 present or confirmed, 2 not testable (kinds 2 and 6), 3
refuted.** **DA-29 and DA-30 are each engaged at only 7 of 17 issuers — 10 never engage
them, and an unengaged cell is not a passed check.**

## 3b. The disposition census

| Class | Count | Named resolving source |
|---|---:|---|
| **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** | **9** | each carries the disclosure that would resolve it — Varda is private; UTHR's programme economics are immaterial to a **$783M/quarter** issuer; MRCY's capability margin is withheld by policy; the heat-pump COP sits in literature outside every registry skill |
| **`UNRESOLVABLE-FROM-PLATFORM`** | **12** | record as **platform reach**, never as absence of evidence — the MRK/BMY/WWD coverage hole where no detector can run; YSS's pending 10-K; IRDM's datum class and coverage window; PIL-5's licensed colocation data; PIL-6's FCC IBFS / ITU registries |
| **`REACHABLE-BUT-NOT-RECORDABLE`** *(third situation, proposed — not yet a registered class)* | **2** | the datum **is** reachable; the **contract** cannot record it — PIL-2's named source class, and the citation contract's `agentii.ai`-only URL pattern |
| **`UNVALIDATED-BY-PLATFORM`** *(refined to `PARTIALLY-VALIDATED-BY-PLATFORM` at IRDM, scoped to the missing linkbase ARC)* | **3** | the validator ran and its result is not admissible |
| **`UNEXERCISED` / `UNEVIDENT` / `NOT TESTABLE` with a named kind** | **31** | the kind's own remedy |
| **`EVALUABLE — blocked by EFFORT`** | **1** | on-platform work: 001:PIL-3's ~19 issuer Item 1A reads |

**Nine, twelve, two, three, thirty-one and one.** The distribution is the finding: **the
largest single class is not "unresolvable" but "testable and not tested"** — 31 cells that a
named remedy could move.

## 4. Corrections do not propagate — the finding that outlives the thesis

**Corrections ledger: 3 of 32 propagated.** `upstream_stale` is mandatory in all 41
artifacts, **correct in all 41, and consumed by none.** The UTHR `72.0` was derived three
times and absorbed zero times.

**This means a correction that is recorded and never propagated is indistinguishable in
effect from one never made** — and **it therefore suggests** the programme needs a
resumption queue that a human or Phase 7 discharges by name, not a pin that records
staleness and dispatches nothing.

## 5. Falsifier reachability — PIL-7's metric is 0

**11 falsifier-blocks classified (001's six + 002's seven), every one with a named resolving
source.** The unreachable set is corrected to **001:PIL-4, 5, 6** — not 3, 5, 6, since
PIL-3 is blocked by *effort*, not reachability. Seven not-testable kinds were catalogued,
and **kind 7 — detector gap at a computable datum — is the only kind that is a defect of
this programme rather than of the world.**

## 6. The main line, and what this thesis did to it

`PROGRAM.md` §0b states the programme's main line as **"Space is a cost curve, not a value
pool."** 002 does not overturn it. What 002 does is **narrow the evidentiary base it can be
asserted from** — and **this means** every downstream thesis inherits a harder standard than
the one 001 was written to.

---

*Full detail, including the per-row citation table, is in `_cross/validation-ledger.md` —
this thesis's primary artifact.*
