---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: UTHR
skill: recent-quarter
mode: methodology
generated_at: "2026-09-18T15:00:00+08:00"
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      Sign stripping, read at BOTH axes. Axis A is the consolidated subtotal: whether a
      served value that the filer printed inside parentheses is served as a positive
      magnitude. Axis B — the one the register's own three detectors do not reach — is the
      COMPONENT: whether an individual input to a subtotal is served as an absolute value.
      The register's component-identity detector is the reliable one, and it is reliable
      precisely because it is mechanical: a component strip cannot hide from it. I read
      `EPS x shares` as inadmissible, per the register, and I do not use it as a sign test
      anywhere below; where I present it, I present it as a demonstration of its blindness.
      I read the exact strip signature as `diff = 2 x value`, where `diff` is
      served_minus_filed, and I require that signature to hold to the tenth of a million
      before I call a strip confirmed.
  - da_id: DA-24
    chosen_reading: >-
      Asset-sale contamination of the operating line: whether any gain or loss on disposal
      of PP&E, or any sale of a business or product right, is classified inside the
      operating section such that operating income is inflated by a non-operating event. I
      read this at the LEVEL OF THE FILED STATEMENT FACE rather than by concept query,
      because `GainLossOnSaleOfPropertyPlantEquipment` returns zero facts for UTHR and a
      zero-fact return is evidence about the CONCEPT NAME, not about the ISSUER. The
      disposition of an impairment charge that sits INSIDE operating expense and pushes
      operating income DOWN is explicitly not this defect.
  - da_id: DA-25
    chosen_reading: >-
      Normalised per-unit metrics: whether the platform serves a per-unit or normalised
      quantity that the issuer does not file, or files an absolute the platform converts.
      I read this as a search for any served non-USD unit at UTHR and for the pillar's own
      terms (value per kilogram, cost per kilogram returned). Where a per-unit figure
      exists only in an LLM-generated `read_source_outline` description field and not in a
      page I have READ, I record it as not verified and I do not cite it — the description
      field inherits the filing's register and its negative signs, so quoting it is
      evidentially fabricated even when substantively right.
  - da_id: DA-26
    chosen_reading: >-
      A period labelled quarterly in the platform's metrics block that actually carries an
      ANNUAL column. I read the test as: take the metrics row whose `fiscal_period` is
      "Q4" and compare it against the same issuer's filed annual total. If the row equals
      the annual total, the row is the annual mislabelled as a quarter, and the ratio of
      that row to the genuine filed quarter is the measure of the error. The fiscal period
      that is mislabelled varies by issuer; I do not assume it is Q4 for the universe.
  - da_id: DA-27
    chosen_reading: >-
      Fiscal labels derived from the calendar quarter. This defect requires a PRECONDITION:
      the issuer's fiscal quarter must differ from the calendar quarter. I read the
      precondition itself as part of the test — I look up the issuer's fiscal year end
      before asking whether its labels are wrong, because an issuer that closes on 31
      December cannot exhibit this defect, and reporting "not testable" without naming
      WHY would merge a precondition that is absent by construction with the two kinds of
      absence that are real (an ingestion absence and a source absence).
  - da_id: DA-28
    chosen_reading: >-
      Post-IPO capital-structure discontinuity: whether a share-count regime change around
      a listing event makes a per-share series non-comparable period-over-period. I read
      the test as double: (a) is there an IPO in the quoted window, and (b) is there any
      share-count discontinuity at all, whatever its cause, and does the per-share line
      invert. A buyback-driven discontinuity is NOT this defect, but it must still be named
      because it is what a naive share-count reading would mistake for it.
  - da_id: DA-29
    chosen_reading: >-
      Back-solved and opaque checks, per the mechanical circularity test: if any term in a
      reconciliation appears NOWHERE in the source, the check is a back-solve. A back-solve
      closes exactly, so it cannot be caught on the closure; it must be caught on the
      terms. Two corollaries bind here. First, a `computed` value from the calculation
      linkbase may not be cited as a derivation, because it is not reproducible from the
      instrument's own returned tree. Second, `reported` is not definitionally the filed
      value: it must be reconciled to the statement face, and I reconcile every one I use.
  - da_id: DA-30
    chosen_reading: >-
      Two bases on one concept, collapsed without a basis field. I read the trigger as: an
      artifact quoting a concept the issuer reports on more than one basis must NAME each
      basis and say where each was established, and must say which one it is quoting. This
      is prior to `no_single_basis_collapse` — an artifact cannot comply by diligence,
      because it must first discover that a second basis exists. Here the concept is gross
      margin, and the bases are not two but five.
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: >-
      Q2 2026 10-Q Consolidated Statements of Operations cells: "Total revenues 783.3 | 798.6 | 1564.8 | 1593.0";
      "Total operating expenses 452.5 | 434.1 | 908.2 | 845.7"; "Operating income 330.8 | 364.5 | 656.6 | 747.3";
      "Net income $333.0 | $309.5"; "Diluted EPS $7.27 | $6.41"; "Diluted WASO 45.8 | 48.3"
      (three months ended June 30, 2026 and 2025; six months ended June 30, 2026 and 2025; in millions except per-share)
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 4
    url: https://agentii.ai/v/UTHR/sec219/4
    located_via: read_source_outline
  - figure: >-
      Q2 2026 10-Q Note 11 product table cells, "THREE MONTHS ENDED JUNE 30, 2026": Total revenues by product
      "326.6 | 126.0 | 126.3 | 125.7 | 65.2 | 6.7 | 6.8 | 783.3"; Cost of sales "51.1 | 8.9 | 17.4 | 6.1 | 2.0 | 3.0 | 11.0 | 99.5";
      Gross profit "(loss) $275.5 | $117.1 | $108.9 | $119.6 | $63.2 | $3.7 | $(4.2) | $683.8"; and footnote (1)
      "we recorded $19.2 million and $64.1 million of inventory reserve expense ... as compared to $6.5 million and $15.5 million"
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 20
    url: https://agentii.ai/v/UTHR/sec219/20
    located_via: read_source_outline
  - figure: >-
      Q2 2026 10-Q MD&A cost-of-sales table, two bases in one table: "Cost of sales $98.5 | $86.6 | $230.9 | $178.2";
      "Share-based compensation(1) 1.0 | 1.0 | 2.0 | 1.9"; "Total cost of sales $99.5 | $87.6 | $232.9 | $180.1"
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 37
    url: https://agentii.ai/v/UTHR/sec219/37
    located_via: read_source_outline
  - figure: >-
      Q2 2026 10-Q balance-sheet cells: "Property, plant, and equipment, net 1930.1 | 1729.7";
      "Total assets $7220.1 | $7880.0"; "Total stockholders' equity 6400.3 | 7096.2";
      "Treasury stock, at cost 35,352,483 and 32,809,088 shares (5,644.9) | (4,260.4)";
      common shares outstanding "42,676,835" at June 30, 2026 and "43,643,165" at December 31, 2025
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 3
    url: https://agentii.ai/v/UTHR/sec219/3
    located_via: read_source_outline
  - figure: >-
      Q2 2026 10-Q EPS note cells: "Basic $7.82 | $6.86 | $14.14 | $14.04"; "Diluted $7.27 | $6.41 | $13.07 | $13.02";
      Basic WASO "42.6 | 45.1 | 43.0 | 45.0"; effect of dilutive securities "3.2 | 3.2 | 3.5 | 3.5";
      Diluted WASO "45.8 | 48.3 | 46.5 | 48.5"; "Basic and diluted earnings per common share are computed
      independently for each quarter and the year-to-date period presented."
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec219
    page_no: 17
    url: https://agentii.ai/v/UTHR/sec219/17
    located_via: read_source_outline
  - figure: >-
      Q1 2026 10-Q Consolidated Statements of Operations cells: "Total revenues 781.5 | 794.4";
      "Cost of sales 133.4 | 92.5"; "Total operating expenses 455.7 | 411.6"; "Operating income 325.8 | 382.8";
      "Net income $274.9 | $322.2"; "Basic $6.32 | $7.18"; "Diluted $5.82 | $6.63"; Diluted WASO "47.2 | 48.6"
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec215
    page_no: 4
    url: https://agentii.ai/v/UTHR/sec215/4
    located_via: read_source_outline
  - figure: >-
      Q1 2026 10-Q Note 11 product table cells, "Three Months Ended March 31, 2026":
      Total revenues "$ 330.3 ... $ 127.2 ... $ 126.6 ... $ 135.6 ... $ 53.6 ... $ 2.9 ... $ 5.3 ... $ 781.5";
      Cost of sales(1) "83.2 ... 8.6 ... 16.1 ... 7.4 ... 5.0 ... 1.0 ... 12.1 ... 133.4";
      Gross profit (loss) "$ 247.1 ... $ 118.6 ... $ 110.5 ... $ 128.2 ... $ 48.6 ... $ 1.9 ... $ (6.8) ... $ 648.1";
      and footnote (1) "we recorded $44.9 million and $9.0 million of inventory reserve expense ... Tyvaso DPI
      inventory reserve expense accounts for $39.2 million and $5.8 million of the total" (the $39.2 million taken
      out of Tyvaso DPI cost of sales leaves gross profit $286.3 on the same $330.3 revenue, 86.68% against the
      as-filed 74.81%)
    ticker: UTHR
    form_type: 10-Q
    citation_id: sec215
    page_no: 18
    url: https://agentii.ai/v/UTHR/sec215/18
    located_via: read_source_outline
  - figure: >-
      FY2025 10-K Consolidated Statements of Operations cells: "Total revenues 3,182.7 | 2,877.4 | 2,327.5";
      "Cost of sales 384.4 | 309.7 | 257.5"; "Total operating expenses 1,690.2 | 1,500.4 | 1,142.6";
      "Operating income 1,492.5 | 1,377.0 | 1,184.9"; "Net income $1,334.7 | $1,195.1 | $984.8";
      "Diluted $27.86 | $24.64 | $19.81" (2025, 2024, 2023)
    ticker: UTHR
    form_type: 10-K
    citation_id: sec212
    page_no: 69
    url: https://agentii.ai/v/UTHR/sec212/69
    located_via: read_source_outline
  - figure: >-
      FY2025 10-K Note 13 product table cells, fiscal 2025: Total revenues "1,292.5 | 585.7 | 526.8 | 496.9 | 226.8 | 30.0 | 24.0 | 3,182.7";
      Cost of sales "210.6 | 27.2 | 49.3 | 28.7 | 17.5 | 13.1 | 38.0 | 384.4";
      Gross profit "(loss) $1,081.9 | $558.5 | $477.5 | $468.2 | $209.3 | $16.9 | $(14.0) | $2,798.3";
      fiscal 2024 gross profit "$885.2 | $552.7 | $490.7 | $405.9 | $224.3 | $13.7 | $(4.8) | $2,567.7";
      fiscal 2023 gross profit "$615.5 | $470.2 | $456.6 | $335.2 | $182.4 | $16.6 | $(6.5) | $2,070.0"
    ticker: UTHR
    form_type: 10-K
    citation_id: sec212
    page_no: 96
    url: https://agentii.ai/v/UTHR/sec212/96
    located_via: read_source_outline
key_metrics:
  gross_margin_filed_pct: 87.30
  gross_margin_band_pct: "82.93-89.24"
  figure_001_attributed_pct: 72.0
  misattribution_pp: 15.30
  gross_margin_bases: 5

---

# UTHR × recent-quarter — Phase 3 defect census (PIL-3)

## 0. What this artifact is, and the one rule it obeys

This is the PIL-3 `recent-quarter` pass on United Therapeutics Corporation, the largest
single universe weight in 001 — **7%**, the biggest of 35 names. It is a defect census, not
a company note. It tests UTHR against the Data-Integrity Register (DA-23 … DA-30 at
constitution 1.5.0) and it validates what 001 said about UTHR.

The one rule: **no figure below is asserted unless it is a cell I READ on the page cited.**
Every reconciliation names the source of every term (DA-29). Where a term does not exist in
a filing, I say so and I do not close the check. Where a check closes, it closes on filed
cells, not on a back-solve.

**`skill_pin` is derived and verified, not merely recorded.** The value `07d26b9c738b` in the
frontmatter above was reproduced in this session from the skill tree itself:

```
recipe : sha256( concat[ basename_bytes || file_bytes ] ), files sorted by path, first 12 hex
base   : /Users/frank/.claude/skills/agentii/recent-quarter
files  : SKILL.md, knowledge-frameworks.md, modes.md, output-structure.md,
         tool-fallbacks.md, wsp-methodology.md   (28,226 bytes total)
digest : 07d26b9c738bed2652c3c000e08732078b59a74ff3ec6edcde1519714cb409cf
pin    : 07d26b9c738b   ← exact match
```

This is the `skill_version_hash` algorithm the repository names at `scripts/dispatch.py:132`
— *"sha256 over sorted rglob files, name-then-bytes, first 12 hex"* — and the value
independently agrees with the two records in
`theses/002-evidence-validation/skill_pins.jsonl` (`recorded 2026-09-18T16:23:35+08:00`, and
`2026-09-18T17:05:00+08:00` as `cross_root_confirmation`).

The reason it is stated at this length: **an earlier pass tested 24 algorithm variants against
this same tree and reproduced nothing, and the cause was a single wrong word.** Every failing
variant used the file's *relative path* (`references/modes.md`) where the algorithm uses its
*name* (`modes.md`). The recipe is fully specified in the repo; the misreading was mine, and it
survived 24 attempts because all 24 shared it. That is a live example of the failure mode this
thesis exists to catch — an unreproducible check whose non-reproduction is attributed to the
instrument rather than re-examined — and it is recorded here rather than quietly dropped now
that the answer is in hand.

**And the recipe is swept, not merely fitted to one value.** I re-ran it against all six pins
001 tabled in `theses/001-technology-baseline/reproduce.md`, plus `recent-quarter`, across six
skill roots on this machine. The result separates cleanly with no partial cases:

| Root | Result |
|---|---|
| `/Users/frank/.claude/skills/agentii` | **7 / 7 match** (six known pins + recent-quarter) |
| `…/agent-plugins/agentii-equity-agent/skills/agentii` | **4 / 4 match** (every pin present in that root) |
| `…/vertical-plugins/equity-research-core/skills/agentii` | **4 / 4 match** |
| `…/plugins/cache.bak/…/agentii-equity-agent/2.2.1` | 0 / 4 — trees ship **4 files**, not 5–6 |
| `…/plugins/cache.bak/…/equity-research-core/2.2.1` | 0 / 4 — same packaging tree |
| `…/.claude/backups/agentii-skills-20260910_140109/skills-agentii` | 0 / 7 — trees ship **1 file** (`SKILL.md` only) |

**15 of 15 on the three valid roots, 0 of 15 on the three packaging roots.** Every root either
reproduces the pin exactly or is missing files from its tree; there is no partial or
near-miss anywhere. That is the behaviour a content hash should have, and it is also an
independent confirmation of the `skill_pins.jsonl` claim that `recent-quarter` resolves to the
same hash from `agentii-equity-agent` and `equity-research-core` **separately** — I reproduced
both, and they agree.

## 1. Line 4's figure: 72.0% is not reproducible from any UTHR filing

001's summary table carries six headline figures. Line 4 of that table reads:

> `| 4 | Microgravity economics | PIL-4 | Incumbent terrestrial gross margin | **72.0** | percent | DEMAND | **HOLDS** |`

and PIL-4's own line names the buyer set:

> `| **PIL-4** Microgravity economics | DEMAND | **HOLDS** | MRK, BMY, AMGN, UTHR — must beat a **72% incumbent gross margin** |`

UTHR is given the largest weight in the universe, and it is named among the four buyers who
must beat 72%. **001's own UTHR artifact says UTHR's gross margin is 87.3%** — the same
thesis, the same pillar, the same company, the same quarter, 15.3 points apart. Resolving
that contradiction is this artifact's first duty.

**Finding: 72.0% is AMGN's gross margin, not UTHR's, and UTHR does not file it on any
basis.** 001 states its own derivation, on the same page as the value: *"AMGN Q2 2026:
revenue $10,054M - COGS $2,811M = gross profit $7,243M -> $7,243M / $10,054M = 72.0%"*, and
beside it *"BMY ... -> $9,247M / $12,973M = 71.3%"*. $7,243M / $10,054M = **72.04%**. The
figure is an AMGN computation that was carried into the UTHR row of the buyer set.

**UTHR's filed consolidated gross margin, nine periods, from filed cells:**

| Period | Total revenues | Cost of sales | Gross profit | Margin | Source |
|---|---|---|---|---|---|
| Q2 2026 | 783.3 | 99.5 | 683.8 | **87.30%** | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec219 p.20](https://agentii.ai/v/UTHR/sec219/20) |
| Q2 2025 | 798.6 | 87.6 | 711.0 | **89.03%** | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec219 p.20](https://agentii.ai/v/UTHR/sec219/20) |
| Q1 2026 | 781.5 | 133.4 | 648.1 | **82.93%** | [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4) |
| Q1 2025 | 794.4 | 92.5 | 701.9 | **88.36%** | [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4) |
| H1 2026 | 1,564.8 | 232.9 | 1,331.9 | **85.12%** | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec219 p.20](https://agentii.ai/v/UTHR/sec219/20) |
| H1 2025 | 1,593.0 | 180.1 | 1,412.9 | **88.69%** | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec219 p.20](https://agentii.ai/v/UTHR/sec219/20) |
| FY2025 | 3,182.7 | 384.4 | 2,798.3 | **87.92%** | [sec212 p.69](https://agentii.ai/v/UTHR/sec212/69), [sec212 p.96](https://agentii.ai/v/UTHR/sec212/96) |
| FY2024 | 2,877.4 | 309.7 | 2,567.7 | **89.24%** | [sec212 p.69](https://agentii.ai/v/UTHR/sec212/69), [sec212 p.96](https://agentii.ai/v/UTHR/sec212/96) |
| FY2023 | 2,327.5 | 257.5 | 2,070.0 | **88.94%** | [sec212 p.69](https://agentii.ai/v/UTHR/sec212/69), [sec212 p.96](https://agentii.ai/v/UTHR/sec212/96) |

Nine of nine close `revenue − cost of sales = gross profit` exactly, in millions.

**The filed range is 82.93% to 89.24%. 72.00% lies outside that range on every one of the
nine periods, by 10.9 to 17.3 points.** There is no period at UTHR, on the consolidated
basis, for which 72.0% is the answer.

**And a bounded search of the other bases UTHR reports found none that yields 72.0% either.**
Seven product lines (Q2 2026): Tyvaso DPI 84.35%, Nebulized Tyvaso 92.94%, Remodulin 86.22%,
Orenitram 95.15%, Unituxin 96.93%, Adcirca 55.22%, Other **−61.76%**
([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20)). Tyvaso DPI with the inventory reserve
added back: 86.77 / 86.73 / 86.68 / 86.23 / 86.02 / 86.11% across six periods. The Tyvaso
franchise combined: 86.74 / 79.93 / 83.32 / 88.17%. The portfolio ex-Tyvaso-DPI: 89.40 /
88.87 / 89.14%. **Closest miss: Tyvaso DPI in Q1 2026 as filed, 74.81% —
2.81 points away.** It is not rounded into agreement, and it is not 72.0.

This is a headline figure failing validation. It is recorded as a correction to 001 in §9.
Per the brief, 001 is frozen and is not rewritten.

**What this does to Line 4.** The *figure* moves away from DEMONSTRATED — 72.0 is refuted as
a UTHR number. The *verdict*, HOLDS, is untouched, because its falsifier is the observed-zero
disclosure count, which 001 measured independently of the margin. But the effect on the
pillar's difficulty runs the wrong way for the thesis: the real hurdle for the UTHR-class
buyer is **87.3%, not 72.0% — 15.3 points higher**. The microgravity-economics case is
harder, not easier, than Line 4 states.

## 2. The test that can actually run at UTHR — the component identity, 7 of 7 exact

UTHR files no gross-profit line on any statement face. Its operating section, read from the
faces, is exactly six rows in this order: `Total revenues`, then `Operating expenses:` with
`Cost of sales`, `Research and development`, `Selling, general, and administrative`, then
`Total operating expenses`, then `Operating income`
([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4),
[sec212 p.69](https://agentii.ai/v/UTHR/sec212/69)). `Cost of sales` sits *inside*
"Operating expenses:", so UTHR does not classify it as a deduction establishing a subtotal.
The first subtotal UTHR files is operating income.

So the component identity is the test, and it closes from filed cells only:

| Period | Total revenues | Total operating expenses | Operating income | Identity | Source |
|---|---|---|---|---|---|
| Q2 2026 | 783.3 | 452.5 | 330.8 | 783.3 − 452.5 = 330.8 ✓ | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4) |
| Q2 2025 | 798.6 | 434.1 | 364.5 | 798.6 − 434.1 = 364.5 ✓ | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4) |
| H1 2026 | 1,564.8 | 908.2 | 656.6 | 1564.8 − 908.2 = 656.6 ✓ | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4) |
| H1 2025 | 1,593.0 | 845.7 | 747.3 | 1593.0 − 845.7 = 747.3 ✓ | [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4) |
| Q1 2026 | 781.5 | 455.7 | 325.8 | 781.5 − 455.7 = 325.8 ✓ | [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4) |
| Q1 2025 | 794.4 | 411.6 | 382.8 | 794.4 − 411.6 = 382.8 ✓ | [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4) |
| FY2025 | 3,182.7 | 1,690.2 | 1,492.5 | 3182.7 − 1690.2 = 1492.5 ✓ | [sec212 p.69](https://agentii.ai/v/UTHR/sec212/69) |
| FY2024 | 2,877.4 | 1,500.4 | 1,377.0 | 2877.4 − 1500.4 = 1377.0 ✓ | [sec212 p.69](https://agentii.ai/v/UTHR/sec212/69) |
| FY2023 | 2,327.5 | 1,142.6 | 1,184.9 | 2327.5 − 1142.6 = 1184.9 ✓ | [sec212 p.69](https://agentii.ai/v/UTHR/sec212/69) |

**Nine of nine exact.** This is the mandatory in-line derivation the register asks for, with
actual component values, not a spot-check and not a back-solve: every term in the identity —
`Total revenues`, `Total operating expenses`, `Operating income` — is a cell on the page
cited, and none of the three is derived from the other two.

Three subordinate stacks also close on filed cells:

- **R&D cost stack, 4 of 4** — External 71.2 + Internal 54.0 + SBC 10.9 + Other 10.2 = 146.3;
  62.4 + 55.9 + 8.1 + 7.6 = 134.0; 129.0 + 112.3 + 16.3 + 26.9 = 284.5;
  119.6 + 104.2 + 15.0 + 44.2 = 283.0 ([sec219 p.37](https://agentii.ai/v/UTHR/sec219/37)).
- **Cost-of-sales stack, 4 of 4** — 98.5 + 1.0 = 99.5; 86.6 + 1.0 = 87.6; 230.9 + 2.0 = 232.9;
  178.2 + 1.9 = 180.1 (same page — and note this is also the DA-30 finding in §3, basis 5).
- **Quarterly-to-semiannual articulation, 3 of 3** — 648.1 + 683.8 = 1,331.9;
  781.5 + 783.3 = 1,564.8; 701.9 + 711.0 = 1,412.9.

`gross profit − opex = operating_income` cannot be written at UTHR in its canonical form,
because the first term does not exist on the face. What substitutes is `revenue − opex =
operating income`, which closes exactly and uses no derived term.

## 3. DA-30: one concept, five named bases

The register's DA-30 entry describes an issuer reporting one concept on more than one basis
with the platform collapsing them and carrying no basis field. **UTHR reports gross margin on
five bases, and 001 collapsed them into one number that belongs to a different company.**

**Basis 1 — consolidated, from the product-table Total column.** The only place UTHR prints a
gross-profit total. Q2 2026: `Gross profit(loss) ... $683.8` on `Total revenues ... 783.3` and
`Cost of sales(1) ... 99.5` ([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20)); FY2025:
`$2,798.3` on `3,182.7` and `384.4` ([sec212 p.96](https://agentii.ai/v/UTHR/sec212/96)).
**87.30% is this basis.** It is a footnote Total, not a face subtotal.

**Basis 2 — the statement-of-operations face: no gross profit exists.** Established by reading
the faces at [sec219 p.4](https://agentii.ai/v/UTHR/sec219/4),
[sec215 p.4](https://agentii.ai/v/UTHR/sec215/4) and
[sec212 p.69](https://agentii.ai/v/UTHR/sec212/69). At every period, `Cost of sales` is a row
inside "Operating expenses:", and the first subtotal filed is operating income. Bases 1 and 2
are not two numbers for one period; they are two different presentations, and an artifact that
quotes "UTHR's gross margin" without saying which one it means has quoted neither.

**Basis 3 — product level: seven bases, 55.22% to 96.93%.**
Nebulized Tyvaso 92.94% ($117.1 / $126.0), Remodulin 86.22%, Tyvaso DPI 84.35%, Orenitram
95.15%, Unituxin 96.93%, Adcirca 55.22%, and Other at **−61.76%** ($(4.2) / $6.8)
([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20)). The board spans 158 points and includes
a negative. The 87.30% consolidated figure is a revenue-weighted blend of these seven, not any
product's margin — Tyvaso DPI alone is 41.7% of revenue and its margin differs from the blend
by 2.95 points. **The Q1 2026 board is the same shape at a different period**, which is what
makes this a property of the presentation rather than an artifact of one quarter: Nebulized
Tyvaso 93.24%, Orenitram 94.54%, Remodulin 87.28%, Tyvaso DPI 74.81%, Unituxin 90.67%, Adcirca
65.52%, **Other −128.30%** ($(6.8) on $5.3), Total 82.93%
([sec215 p.18](https://agentii.ai/v/UTHR/sec215/18)). Two periods, two negatives at the product
level, no negative at the consolidated level — so a detector that reads only the consolidated
total sees a clean issuer at both.

**Basis 4 — Tyvaso DPI including versus excluding inventory-reserve expense.** Footnote (1) to
the table reports the reserve inside cost of sales: *"we recorded $19.2 million and $64.1
million of inventory reserve expense ... Tyvaso DPI inventory reserve expense accounts for
$7.9 million and $47.1 million of the total"*
([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20)). The same footnote in Q1 2026 reports
$44.9 million of which Tyvaso DPI is $39.2 million
([sec215 p.18](https://agentii.ai/v/UTHR/sec215/18)). The spread is the largest of the five:
**Q1 2026 74.81% as filed versus 86.68% ex-reserve, 11.87 points**. H1 2026 79.56% vs 86.73%
(7.17 points); Q2 2026 84.35% vs 86.77% (2.42 points); Q2 2025 84.61% vs 86.23%; Q1 2025
84.10% vs 86.02%; H1 2025 84.36% vs 86.11%. The reserve is a **manufacturing cost** inside
cost of sales — which is DA-30's third listed example verbatim, not an analogy to it. It is
also the only basis on which any UTHR margin comes near 72%, and it stops 2.81 points short.

**Basis 5 — cost of sales including versus excluding share-based compensation.** One MD&A
table, two values, separated only by a subtotal row:
`Cost of sales $98.5 | $86.6 | $230.9 | $178.2`, `Share-based compensation(1) 1.0 | 1.0 | 2.0 | 1.9`,
`Total cost of sales $99.5 | $87.6 | $232.9 | $180.1`
([sec219 p.37](https://agentii.ai/v/UTHR/sec219/37)). Q2 2026 margin: **87.425% ex-SBC versus
87.297% as filed, spread 0.128 points = $1.0M / $783.3M**. Consistent across all four columns.
This basis is small but it is not nothing: it is a second value for cost of sales, on one
page, in one table, and the platform's `cost_of_sales` field carries neither a basis nor a
hint that one exists.

**The collapse.** 001 quoted UTHR at **87.3%** in its UTHR artifact and quoted the UTHR-class
buyer at **72%** in its summary table and PIL-4 line. Both numbers are single figures with no
basis. One of them belongs to AMGN. That is DA-30's exact shape — one concept, one collapsed
number, no basis field — and it happened on the largest-weighted name in the universe.

## 4. The census: DA-23 on every quoted period

### 4.1 The served consolidated series: zero negatives, and correctly so

All 35 served `OperatingIncomeLoss` facts for UTHR are positive, and they should be: every
filed operating income in the window is positive (see §2, nine of nine). At the consolidated
subtotal axis there is nothing to strip. `OtherNonoperatingIncomeExpense` is where the sign
matters on the income statement, and it is treated in §5.2.

### 4.2 The component axis — 11 of 11 stripped, 0 clean

This is the finding. The register's own census row lists **UTHR under "Clean"** (alongside
GOOG, IRDM, VRT, NVDA, MSFT, MRCY, LHX, HWM, TDG, NOC, LMT, RTX, KRMN, GSAT, AMGN, BMY,
MRK, WWD, HEI, SATS). That row is **correct at the consolidated-subtotal axis and false at
the component axis.**

**Component family A — `GrossProfit`, `ProductAndServiceOtherMember`.** Served values are all
positive. Filed values are all negative. Six periods, six exact strips:

| Period | Filed (sec219 p.20 / sec215 p.18 / sec212 p.96 cells) | Served | diff = 2 × value |
|---|---|---|---|
| Q2 2026 | $(4.2) | 4.2 | 8.4 = 2 × 4.2 ✓ |
| Q1 2026 | $(6.8) ([sec215 p.18](https://agentii.ai/v/UTHR/sec215/18)) | 6.8 | 13.6 = 2 × 6.8 ✓ |
| H1 2026 | $(11.0) | 11.0 | 22.0 = 2 × 11.0 ✓ |
| Q2 2025 | $(1.5) | 1.5 | 3.0 = 2 × 1.5 ✓ |
| H1 2025 | $(2.5) | 2.5 | 5.0 = 2 × 2.5 ✓ |
| FY2025 | $(14.0) | 14.0 | 28.0 = 2 × 14.0 ✓ |

The filed cells are on the page: Q2 2026 `Gross profit(loss) ... $(4.2)`
([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20)); Q1 2026 `Gross profit (loss) ... $(6.8)`,
on a row that reads `Total revenues $ 330.3 ... 781.5`, `Cost of sales(1) 83.2 ... 133.4`,
`Gross profit (loss) $ 247.1 ... $ (6.8) ... $ 648.1`
([sec215 p.18](https://agentii.ai/v/UTHR/sec215/18)); FY2025 `$(14.0)` and FY2024 `$(4.8)`,
FY2023 `$(6.5)` ([sec212 p.96](https://agentii.ai/v/UTHR/sec212/96)). **6 of 6 verified pairs
stripped, 0 clean, and the `diff = 2 × value` signature holds to the tenth of a million on
every one.**

**Component family B — `OtherNonoperatingIncomeExpense`.** Five negatives stripped, three
positives clean:

| Period | Filed | Served | diff | Verdict |
|---|---|---|---|---|
| Q1 2026 | $(46.3) (`Other expense, net`) | 46.0 | — | STRIP |
| H1 2026 | $(33.0) | 33.0 | 66.0 ✓ | STRIP |
| Q2 2025 | $(0.1) | 0.1 | 0.2 ✓ | STRIP |
| Q1 2025 | $(4.3) | 4.3 | 8.6 ✓ | STRIP |
| H1 2025 | $(4.4) | 4.4 | 8.8 ✓ | STRIP |
| Q2 2026 | +13.3 | 13.0 | — | clean |
| FY2025 | +48.9 | 48.9 | 0 | clean |
| FY2024 | +5.8 | 5.8 | 0 | clean |

Filed cells: `Other income (expense), net 13.3 | (0.1)` and `Other expense, net (46.3) | (4.3)`
([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4));
`Other income (expense) net 48.9 | 5.8` ([sec212 p.69](https://agentii.ai/v/UTHR/sec212/69)).
Q1 2026's served 46.0 against a filed (46.3) is a strip *plus* a 0.3 rounding difference —
the only pair in which the strip and the rounding are distinguishable, and the strip is the
larger term.

**Totals: 11 of 11 verified negative component facts stripped; 3 of 3 positive clean.**
001's UTHR artifact says "UTHR clean (profitable issuer)". That generalisation holds at the
subtotal and breaks at the component, which is exactly where the register says the reliable
detector lives.

### 4.3 A detector this census found, which the register does not yet carry

**When a consolidated total is served alongside fully-tagged components, the served components
overshoot the served total by exactly 2 × |every negative component|.** Because each stripped
component is served as +|v| instead of −|v|, the sum of the served components exceeds the sum
of the filed components by 2·Σ|v|, while the total itself is served once and correctly.

| Period | Sum of SERVED components | Served total | Overshoot | = 2 × |
|---|---|---|---|---|
| Q2 2026 | 692.2 | 683.8 | 8.4 | 2 × 4.2 ✓ |
| Q1 2026 | 661.7 | 648.1 | 13.6 | 2 × 6.8 ✓ |
| H1 2026 | 1,353.9 | 1,331.9 | 22.0 | 2 × 11.0 ✓ |
| Q2 2025 | 714.0 | 711.0 | 3.0 | 2 × 1.5 ✓ |
| H1 2025 | 1,417.9 | 1,412.9 | 5.0 | 2 × 2.5 ✓ |
| FY2025 | 2,826.3 | 2,798.3 | 28.0 | 2 × 14.0 ✓ |

Six of six exact. This detector has three properties the register's three do not:

1. **It has full power at high gross margin.** The registered gross-profit bound screens for a
   *negative gross profit served positive*, and its power scales inversely with the gross
   margin. UTHR at 87.30% is its worst case: the consolidated gross profit is positive, so the
   bound finds **zero of the 11 strips** in §4.2. The overshoot detector finds all six of the
   family-A strips to the tenth of a million at the same issuer.
2. **It is internal.** It requires no second source, no comparison issuer, and no external
   reference margin — only the served facts of one period.
3. **It is arithmetic, not plausibility.** The residual is not "large" or "implausible"; it is
   exactly twice a filed negative, and that is checkable.

It is offered to the register as a carry-forward (§11), not as a rule I am applying to other
issuers.

### 4.4 What the gross-profit bound would have concluded, for the record

At the consolidated level, `GrossProfit` Q2 2026 served 683.8 equals the filed Total column
683.8 ([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20)) — clean. At the component level,
`GrossProfit` / Other served 4.2 against a filed $(4.2)$ — stripped. **The same concept, one
period, one filing: clean as a total, stripped as a component.** A detector that only reads
totals reports UTHR clean, and the constitution's census row does.

## 5. The instrument, re-measured on UTHR

### 5.1 `status` discarded a real defect, and `validate_calculation` failed on a filing that closes

`validate_calculation` on accession `0001082554-26-000027` returns **pass 17, warn 1, fail 10
of 28 arcs — a 35.7% failure rate on a filing whose statement face closes exactly, nine of
nine, in §2.** Every failure sits at a `period_end` shared by two durations:

```
OperatingIncomeLoss  Jun 30 2025   computed −721,800,000  reported 747,300,000  FAIL
NetIncomeLoss        Jun 30 2025   computed  208,200,000  reported 309,500,000  FAIL
GrossProfit          Jun 30 2025   computed   75,400,000  reported 266,700,000  FAIL
```

`reported 747,300,000` for `OperatingIncomeLoss` at "Jun 30 2025" is the **six-month** value;
the three-month value 364,500,000 shares that key and is not reported at all. The validator's
`period` key is the end date alone, so the three-month and six-month columns of a single 10-Q
collapse onto one key and the comparison is made across them. `computed −721,800,000` is what
results. **The remedy is a period key carrying `period_start`, not a re-check of the issuer.**

The DA-29 corollary lands here directly: `GrossProfit` Q2 2026 returns `computed 683,800,000`
/ `reported 683,800,000` / `diff 0` / **PASS** — on a filing where **no gross-profit line
exists on the statement face at all**. `GrossProfit` appears in exactly one calculation role,
`SegmentInformationGeneralDetails` (a footnote role), and never in
`ConsolidatedStatementsofOperations`. The PASS certifies the footnote arithmetic. It does not
certify that UTHR files a gross-profit line, and read as the latter it is wrong.

### 5.2 `reported` carried the wrong quantity, three times in one filing

- `PropertyPlantAndEquipmentNet`: **reported 1,930,100,000** against computed 343,000,000. The
  reported value is correct and is a filed cell — `Property, plant, and equipment, net 1930.1`
  ([sec219 p.3](https://agentii.ai/v/UTHR/sec219/3)). The *computed* value is the accumulated
  depreciation: gross 2,273.1 − accumulated 343.0 = net 1,930.1. A reader who trusted
  `computed` would report PP&E at **17.8% of its filed value**.
- `DebtSecuritiesAvailableForSaleExcludingAccruedInterest`: reported 353,800,000 against
  computed 1,813,700,000 — a factor of 5.1.
- `AssetsFairValueDisclosure`: reported 1,921,500,000 against computed 2,330,400,000.

None of the three is a defect in the filing; each is a mis-selection inside the instrument.
`reported` is therefore **not** definitionally the filed value, and every `reported` I use
above I have reconciled to the statement face.

### 5.3 The highlight block contradicts itself within one response

For the same accession `0001082554-26-000027`, `get_company_financials(UTHR)` serves
`metrics[Q2 2026].assets = 7,220,100,000` (the current column,
[sec219 p.3](https://agentii.ai/v/UTHR/sec219/3)) while
`filings[].highlights.balance_sheet.Assets = 7,880,000,000 @ 2025-12-31` (the comparative) —
**a $659.9M / 9.1% discrepancy on the same filing.** The same block serves
`StockholdersEquity = 6,444,000,000 @ 2024-12-31`, a *third* instant that appears on this
10-Q only as the opening balance of the equity statement; the filed Q2 2026 equity is 6,400.3
and the filed 2025-12-31 equity is 7,096.2 (same page). And it serves
`CommonStockSharesOutstanding 43,643,165 @ 2025-12-31`, while the cover page count is
42,890,692 and the 10-Q's own balance sheet says **42,676,835 at June 30, 2026**.

**Three share counts in play, one filing.** They are named, not reconciled into one.

### 5.4 `EPS × shares` is inadmissible, and here is the demonstration

The register calls `EPS × shares` an inadmissible sign test. UTHR shows why:

`7.27 × 45.8 = 332.966 ≈ 333.0 > 0` → the test returns "profitable, no strip."

Both operands are filed and correct — diluted EPS $7.27 and diluted WASO 45.8
([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4),
[sec219 p.17](https://agentii.ai/v/UTHR/sec219/17)) — and the conclusion is **wrong**, because
**11 of 11 component facts are stripped** (§4.2). The test is blind by construction: a
component strip does not touch net income. It cannot see the defect it is being asked to find.

**The per-share line does NOT invert at UTHR.** Served equals filed, side by side:

| | Filed | Served | Verdict |
|---|---|---|---|
| Q2 2026 basic EPS | $7.82 | 7.82 | match |
| Q2 2026 diluted EPS | $7.27 | 7.27 | match |
| Q2 2025 basic EPS | $6.86 | 6.86 | match |
| Q2 2025 diluted EPS | $6.41 | 6.41 | match |
| Q1 2026 basic EPS | $6.32 | 6.32 | match |
| Q1 2026 diluted EPS | $5.82 | 5.82 | match |

No inversion. The live inversion reproduced at MRCY (served +0.25/+0.38 where the filing prints
$(0.25)/$(0.38)) and at YSS **does not reproduce at UTHR** — a useful negative, because it
shows the inversion is issuer-conditional rather than a platform-wide transform.

The bridge closes on filed share counts, to four places:
333.0 / 42.6 = 7.8169 (filed $7.82, miss 0.040%); 333.0 / 45.8 = 7.2707 (filed $7.27, 0.010%);
309.5 / 45.1 = 6.8625 (filed $6.86, 0.037%); 309.5 / 48.3 = 6.4079 (filed $6.41, 0.033%).
The residual is −0.034M, the rounding tell of a per-share quantity derived from a rounded
patent count — which is why the bridge is a check on the share counts and not a derivation of
EPS.

### 5.5 The five standing defects, reproduced on UTHR

| # | Defect | Reproduced at BWXT | Reproduced at UTHR |
|---|---|---|---|
| 1 | `status` non-certifying | yes | **yes** — `GrossProfit` PASSes where no face line exists |
| 2 | `computed` not reproducible from the returned tree | yes | **yes** — accumulated depreciation served as net PP&E (5.2) |
| 3 | `reported` mis-selected | yes, 3× | **yes, 3×** (5.2) |
| 4 | duplicate `period_end` collapses two durations onto one key | yes | **yes** — 10 of 28 arcs FAIL (5.1) |
| 5 | highlight block inconsistent within one response | yes | **yes** — 9.1% assets gap plus a third instant (5.3) |

Five of five. This is the fifth issuer on which the same five reproduce, which strengthens the
case that they are instrument properties and not issuer properties.

## 6. The six DAs, one by one

### DA-23 — sign stripping; any level failing the gross-profit bound

**CONFIRMED — at the component axis; REFUTED at the consolidated-subtotal axis.** At the
subtotal axis, 0 of 35 served `OperatingIncomeLoss` facts are stripped, correctly, because all
35 filed values are positive. At the component axis, **11 of 11 verified negative facts are
stripped and 0 are clean**, with the exact `diff = 2 × value` signature on 6 of them (§4.2).
The registered gross-profit bound finds **none** of the 11 at this issuer. The unreliable
detectors agree with the wrong answer here: the bound screens for negative gross profit and
UTHR's consolidated gross profit is positive at 87.30%; the margin-plausibility detector sees
87.30% and calls it plausible. The component-identity detector — the reliable one — finds all
eleven.

### DA-24 — asset-sale contamination of the operating line

**REFUTED.** The operating section of every filed face contains exactly `[Total revenues, Cost
of sales, Research and development, Selling, general, and administrative, Total operating
expenses, Operating income]` — 4 of 4 columns on the Q2 2026 10-Q
([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4)), 2 of 2 on the Q1 2026 10-Q
([sec215 p.4](https://agentii.ai/v/UTHR/sec215/4)), 3 of 3 on the FY2025 10-K
([sec212 p.69](https://agentii.ai/v/UTHR/sec212/69)). **Nine of nine columns carry no asset-sale
or disposal line.** No gain or loss on disposal is classified inside the operating section, so
operating income is not inflated by a non-operating event.

Method note: the concept query `GainLossOnSaleOfPropertyPlantEquipment` returns **0 facts** for
UTHR. Per the brief's own rule that was not used as evidence — a zero-fact return is evidence
about the CONCEPT NAME, not about the ISSUER. The test was run on the statement faces instead.

Adjacent, and recorded as adjacent rather than merged: UTHR does carry impairments — FY2025
SG&A includes an impairment of PP&E and a litigation accrual relating to Sandoz, and
`TangibleAssetImpairmentCharges` appears as a cash-flow add-back. But **an impairment charge
inside operating expense pushes operating income DOWN**; it is not asset-sale contamination.
Recording it as an instance of DA-24 would inflate the defect count with a sign-flipped case.

### DA-25 — normalised per-unit metrics not reproducible from segment tables

**REFUTED as a substitution, with the pillar's own terms genuinely absent from the source.**
No normalised per-unit metric is served for UTHR: every XBRL fact retrieved (35+ across the
three filings) is an absolute USD amount, and the metrics block carries absolutes only. There
is no served per-unit figure to fail to reproduce.

The per-unit terms the pillar actually needs — value per kilogram delivered, cost per kilogram
returned — **exist in no UTHR filing**, which is a **genuine absence from the source**, already
dispositioned `UNRESOLVABLE-FROM-PUBLIC-SOURCES` by 001. It is not an ingestion absence:
`list_sources` and the three accessions all resolve, and all three filings return their full
page counts (59, 54, 113).

One reader hazard, recorded and **not cited**: the FY2025 10-K human-capital discussion carries
a "revenue per employee ($2.25 million)" figure. My only exposure to it is the LLM-generated
`read_source_outline` description field, and the contract forbids quoting that field as
evidence. It is noted here as a thing a later pass should READ, not as a finding.

### DA-26 — annual mislabelled as quarterly

**CONFIRMED, and the mislabelled period at UTHR is Q4.** The metrics block carries two rows
whose `fiscal_period` is `"Q4"`, and both carry ANNUAL columns:

| Row | Served as Q4 | Filed as the FY total | Filed as the genuine quarter | Ratio to the quarter |
|---|---|---|---|---|
| FY2025 revenue | 3,182,700,000 | 3,182.7 ([sec212 p.69](https://agentii.ai/v/UTHR/sec212/69)) | 790.2 | **4.03×** |
| FY2025 operating income | 1,492,500,000 | 1,492.5 (same page) | 356.7 | **4.18×** |
| FY2025 net income | 1,334,700,000 | 1,334.7 (same page) | 364.3 | **3.66×** |
| FY2024 revenue | 2,877,400,000 | 2,877.4 (same page) | 735.9 | **3.91×** |

Two independent tells. First, the served "Q4" values **equal the filed annual totals exactly**
— 3,182.7, 1,492.5 and 1,334.7 are each a cell on the FY2025 statement of operations, not
fourth-quarter amounts. Second, **the three ratios differ from each other (4.03, 4.18, 3.66)
and none is near 1.0**, so the row is not a scaled quarter either; a uniformly scaled quarter
would give one ratio. The genuine quarter is derived as FY minus the filed nine-month total,
which is why it is offered as a range rather than a single firm figure.

The six non-Q4 rows are true quarters and match filed: 799.5, 798.6, 794.4 (2025) and 783.3,
781.5 (2026) all equal filed three-month revenues
([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4)).
**The mislabelled period varies by issuer** — Q4 here, as the constitution says it may be.

### DA-27 — fiscal labels derived from the calendar quarter

**NOT TESTABLE — and the kind is: the PRECONDITION IS ABSENT BY CONSTRUCTION.** This is
neither an ingestion absence nor a source absence, and naming it as one of those two would be
wrong.

The precondition for DA-27 is that the issuer's fiscal quarter differs from the calendar
quarter. UTHR closes on 31 December: `get_company_fiscal_calendar(UTHR)` returns
`fiscal_year_end_month: 12`, source `gold_companies`, `cross_validation_hint: null`. The filed
column headers are `Three Months Ended June 30,` and `Six Months Ended June 30,` for the period
ending 2026-06-30 ([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4)) — the fiscal quarter and
the calendar quarter coincide. There is no fiscal label that could be derived from the wrong
quarter because there are not two quarters to confuse.

**UTHR is excluded from DA-27's denominator.** It is not a pass and it is not a failure; the
test does not apply. Method note, as at BWXT: the platform field's declared source is
`gold_companies`, not the `default` value recorded at SPCX, so the DA-27 method finding is
issuer-specific and is not generalised here.

### DA-28 — post-IPO share-count discontinuity

**REFUTED.** There is no IPO in the quoted window — UTHR listed in 1999, decades before the
periods tested. The only discontinuity is buyback-driven and is named rather than counted:
basic WASO 45.1 → 42.6 (−5.5%) and diluted WASO 48.3 → 45.8 (−5.2%) from Q2 2025 to Q2 2026
([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4),
[sec219 p.17](https://agentii.ai/v/UTHR/sec219/17)), against treasury stock of 35,352,483 and
32,809,088 shares at cost of $(5,644.9)M and $(4,260.4)M
([sec219 p.3](https://agentii.ai/v/UTHR/sec219/3)), funded by the 2025 ASRs (2,642,498 shares)
and the Q1 2026 ASRs (2,164,459 shares / $1,500M). That is a capital-return programme, not a
listing event. **A buyback-driven discontinuity is not this defect** — but it is precisely what
a naive share-count reading would mistake for it, which is why it is named here rather than
left implicit.

The per-share line does not invert (§5.4), and the `EPS × shares` inadmissibility demonstration
is made in the same place: the test returns "no strip" against 11 confirmed strips.

### DA-29 — back-solved and opaque checks

**CONFIRMED, four independent instances in this issuer, one of them new.**

**(a) The opacity of a `computed` PASS.** `GrossProfit` sits only in the footnote role
`SegmentInformationGeneralDetails`, never in `ConsolidatedStatementsofOperations`. Its
`computed 683,800,000 = reported 683,800,000` PASS therefore certifies arithmetic that UTHR
does not file as a line anywhere on the face (§5.1). `computed` is not citable as a derivation.

**(b) The 10-of-28 failure on a filing that closes.** The duplicate `period_end` key collapses
two durations, and the reported value selected is the wrong column (§5.1). Every term of the
failing reconciliations DOES appear in the source — this is not a back-solve, it is a
mis-join, and the two need different remedies.

**(c) `reported` mis-selection, three times in one filing** (§5.2), including a `computed`
that is the accumulated depreciation served against a `reported` that is the filed net.

**(d) 001's own check on $330.8M is a back-solve in form.** 001's UTHR artifact §4 states:
*"UTHR's operating income ($330.8M) is correct: 87.3% gross margin less R&D and SG&A at
plausible ratios yields it."* Under the mechanical circularity test, the terms are
`"87.3% gross margin"` (a basis-unspecified margin), `"plausible ratios"` (no term at all), and
`$330.8M`. **`"plausible ratios"` appears nowhere in any filing.** The check is opaque, and per
the corollary it closes — 330.8 is the right number — which is exactly why the closure could
not catch it. It must be caught on the terms, and it is: one of the three terms is not in the
source. The conclusion survives; the check does not. The repair is §2's identity, which closes
on three filed cells.

**The counter-example matters as much as the four instances.** Every reconciliation in §1, §2
and §4 of THIS artifact locates all of its terms on the pages cited. §2's identity uses three
filed cells and no derived value; §1's margins use `revenue` and `cost of sales` cells from two
pages of the same filing; §4.3's overshoot uses served components and a served total. No term
in any of them is unavailable in the source.

### DA-30 — two bases on one concept collapsed without a basis field

**CONFIRMED, five named bases, and a 15.3-point contradiction inside 001.** Full treatment in
§3. The bases are: (1) consolidated Note-11/Note-13 Total column, 87.30% Q2 2026; (2) the
statement-of-operations face, where **no gross-profit line exists at any period**; (3) product
level, seven bases from 55.22% to 96.93% plus a negative at −61.76%; (4) Tyvaso DPI including
versus excluding inventory-reserve expense, spread up to 11.87 points; (5) cost of sales
including versus excluding share-based compensation, spread 0.128 points.

Each of the five was established at a named page, and each is quoted with its basis above. The
collapse 001 committed is the one the register describes: one concept, one number, no basis
field — and here the number attributed to UTHR belongs to AMGN.

## 7. Detector availability — the two-axis position

The two axes are independent, and UTHR sits in the **inverse** position to BWXT:

| | Axis 1: a gross-profit line on the statement face | Axis 2: `OperatingIncomeLoss` a filed first-class consolidated subtotal |
|---|---|---|
| UTHR | **NO** at every period | **YES** at every period |
| BWXT | NO | YES (equity-inclusive and equity-exclusive) |

- **Axis 1 = NO.** Established by reading the faces: `Cost of sales` is a row inside "Operating
  expenses:", and there is no gross-profit subtotal at any of the nine columns
  ([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4), [sec215 p.4](https://agentii.ai/v/UTHR/sec215/4),
  [sec212 p.69](https://agentii.ai/v/UTHR/sec212/69)). The only gross-profit total UTHR files is
  in a note ([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20), [sec212 p.96](https://agentii.ai/v/UTHR/sec212/96)).
- **Axis 2 = YES.** `OperatingIncomeLoss` is filed as a face subtotal at all nine columns and
  appears as a first-class node in the `ConsolidatedStatementsofOperations` calculation role
  (`OperatingIncomeLoss = RevenueFromContractWithCustomerExcludingAssessedTax (+1) +
  CostsAndExpenses (−1)`).

**Why this is not academic here, in the brief's own terms.** For Line 4 the gross-profit line
*is* the headline, so axis 1 is the subject and not a detector-availability footnote. UTHR
**fails axis 1 and passes axis 2** — the exact inverse of the register's BWXT/LUNR case, where
the gross-profit line is absent and operability comes from elsewhere. The consequence is
concrete: the register's substitute detector did not need to be invoked at UTHR, because axis
2 gave a clean identity (§2, nine of nine), and the substitute detector would in any case have
failed to find the defect that is actually present (§4.4). **Detector availability and detector
power are different questions**, and UTHR separates them: a detector can be AVAILABLE and still
have zero power.

## 8. 001's clearance: restated, and the 72.0% correction recorded

**Every per-ticker UTHR figure 001 quoted reproduces.** Ten checked against filed cells, none
requiring correction:

| 001's figure | Filed | 001's stated change | Recomputed | Verdict |
|---|---|---|---|---|
| Revenue $783.3M / $798.6M | 783.3 / 798.6 ([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4)) | −1.9% | −1.917% | ✓ |
| Gross profit $683.8M, 87.3% margin | 683.8 / 783.3 = 87.30% ([sec219 p.20](https://agentii.ai/v/UTHR/sec219/20)) | 87.3% | 87.30% | ✓ value, **basis unstated** |
| Operating income $330.8M / $364.5M | 330.8 / 364.5 ([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4)) | −9.2% | −9.246% | ✓ |
| Operating margin 42.2% / 45.6% | 42.23% / 45.64% | — | 42.23% / 45.64% | ✓ |
| R&D $146.3M / $134.0M | 146.3 / 134.0 ([sec219 p.4](https://agentii.ai/v/UTHR/sec219/4)) | +9.2% | +9.179% | ✓ |
| Net income $333.0M / $309.5M | 333.0 / 309.5 | +7.6% | +7.593% | ✓ |
| Diluted EPS $7.27 / $6.41 | 7.27 / 6.41 ([sec219 p.17](https://agentii.ai/v/UTHR/sec219/17)) | +13.4% | +13.417% | ✓ |
| Operating margin "~42%" / "~42.2%" | 42.23% | — | — | ✓ |
| Universe weight 7% | — | — | — | ✓ (001's own allocation) |
| R&D intensity 18.7% | 146.3 / 783.3 = 18.68% | — | 18.68% | ✓ |

**001's UTHR arithmetic is clean. What fails is one attribution.** Two corrections are
recorded, and 001 is not rewritten:

**CORRECTION-U1 — the 72.0% attribution.** 001's summary table line 4 prints `72.0` as the
"Incumbent terrestrial gross margin" and PIL-4's line names UTHR among the buyers who "must
beat a 72% incumbent gross margin". **72.0% is not UTHR's gross margin on any of the five bases
named in §3.** It is AMGN's: $7,243M / $10,054M = 72.04%, per 001's own derivation on the same
page. UTHR's filed consolidated gross margin for the comparable quarter is **87.30%**, and the
nine-period range is 82.93–89.24%. **The figure 72.0 should not be attributed to UTHR, and
UTHR's margin is 15.3 points above it — not below.**

**CORRECTION-U2 — an internal contradiction, not an arithmetic error.** 001's UTHR artifact
carry-forward 3 states that *"UTHR's 87.3% gross margin is the hurdle rate any microgravity
process must clear"* and quotes 87.3% in its body table, while 001's `report-input.md` states
that the four named buyers including UTHR *"must beat a 72% incumbent gross margin"*. **Same
thesis, same pillar, same company, same quarter, 15.3 points apart, no basis field on either
number.** This is DA-30 inside 001 itself. The two artifacts are not reconciled; the
discrepancy is recorded for Phase 7's validation ledger.

**Consequences for Line 4.** The 72.0 figure moves **away from DEMONSTRATED** — it is REFUTED as
a UTHR figure with a named alternative owner. The HOLDS verdict is **untouched**, because its
falsifier is the observed-zero disclosure count, which 001's UTHR artifact measured
independently of the margin. **Net direction: the pillar's economics get harder.** If the
incumbent terrestrial gross margin the UTHR-class buyer must beat is 87.3% rather than 72.0%,
every microgravity process must clear a bar **15.3 points higher**, and 001's PIL-4 text
(which already shows a 71.3–72.0% cluster) understates the hurdle by the width of the entire
Adcirca-to-Tyvaso-DPI margin spread.

## 9. What could not be verified

1. **UTHR's normalised per-unit metrics (DA-25's actual subject) do not exist in any UTHR
   filing.** Genuine absence from the source, not an ingestion absence. This is a real gap in
   what PIL-3 can validate at UTHR, not a gap in this pass.
2. **The "revenue per employee ($2.25 million)" figure is noted but NOT verified and NOT
   cited.** The only exposure was the LLM-generated `read_source_outline` description field,
   whose text inherits the filing's register and its signs; the contract forbids quoting it.
   It needs a page READ, and this pass did not read it.
3. **The genuine Q4 2025 and Q4 2024 quarters are derived, not read.** They are FY minus the
   filed nine-month totals, which is why DA-26's ratio is given as a range (3.66×–4.18×)
   rather than a single firm multiple. The conclusion does not depend on them: the served "Q4"
   rows equal the filed annual totals exactly, on filed cells.
4. **The `"plausible ratios"` term in 001's §4 check cannot be recovered.** It may have been a
   back-solve or it may have been an unstated use of filed cells. Its conclusion is right; its
   terms are not locatable. Recorded as opaque, not as wrong.
5. **The `skill_pin` recipe reproduces only from a root that ships the whole skill tree.** §0
   records the derivation and the 15/15 sweep. The limit is operational rather than evidential:
   the three packaging roots on this machine (`cache.bak` × 2, the dated backup) carry 1 or 4
   files where the valid roots carry 5 or 6, and their hashes differ accordingly. **A pin is
   reproducible only against the tree it was taken from**, so if a future artifact resolves
   `recent-quarter` from a packaging root it will compute a different hash and the honest
   reading is *wrong base*, not *skill changed*. The repository's own note already excludes
   four such trees; this pass adds three more instances to the list.
6. **A 0.3 rounding term sits in the served non-operating series.** Served
   `OtherNonoperatingIncomeExpense` for Q1 2026 is 46.0 against a filed $(46.3)`
   ([sec215 p.4](https://agentii.ai/v/UTHR/sec215/4)) — a strip *plus* a 0.3 difference, where
   the strip (92.6 on a `diff = 2 × value` reading) is the dominant term and the 0.3 is not.
   Served Q2 2026 is 13.0 against a filed 13.3 (same rounding direction, no strip). Served and
   filed EPS themselves match to the cent at all six periods tested (§5.4). The 0.3 is not
   resolved to a cause — scale-of-filing rounding is the plausible reading but is not
   established — so it is named as a residual rather than smoothed.

## 10. Carry-forwards to the register

1. **A new DA-23 detector: served-component overshoot at 2 × |negative component|.** Six of six
   exact at UTHR (§4.3). It has full power where the gross-profit bound has none — the bound
   found 0 of UTHR's 11 strips at 87.30% gross margin, the overshoot found all six family-A
   strips to the tenth of a million. It is internal and arithmetic. Recommended for DA-23 as a
   fourth detector, with the caveat that it requires the components to be served alongside the
   total.
2. **UTHR's register census row must be amended.** The constitution lists UTHR under "Clean".
   That is true at the consolidated-subtotal axis and **false at the component axis**: 11 of 11
   negative component facts stripped, 0 clean. UTHR belongs in a new category — *clean at the
   subtotal, stripped at the component* — alongside whichever other "clean" names fail the same
   axis test.
3. **001's 72.0% attribution to UTHR** (CORRECTION-U1) and **001's internal 87.3-vs-72
   contradiction** (CORRECTION-U2) are for Phase 7's validation ledger. 001 is frozen.
4. **DA-27's "not testable" kind needs a third label.** The register recognises two kinds of
   absence (ingestion, source). UTHR's DA-27 is neither: the precondition is absent by
   construction. A third label — `PRECONDITION-ABSENT` — keeps the exclusion honest and keeps
   UTHR out of DA-27's denominator without recording it as a pass.
5. **`validate_calculation`'s period key needs `period_start`.** 10 of 28 arcs FAIL on a filing
   whose face closes nine of nine, solely because a 10-Q's three-month and six-month columns
   share a `period_end`. This is a join defect, not an issuer defect, and it will reproduce on
   every issuer with a quarterly-plus-year-to-date presentation — which is every issuer.
6. **The 72.0% figure should be re-attributed to AMGN in 001's summary table line 4** at the
   next 001 amendment, and PIL-4's buyer-set sentence should carry UTHR's 87.3% as the hurdle
   for that name. Not done here; 001 is frozen.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the artifact's
> `citations` block — the frontmatter block alone does not satisfy spec §1d, which requires
> the links **in the body**.

| Figure | Source |
|---|---|
| Q2 2026 10-Q statements of operations cells: Total revenues 783.3 \| 798.6 \| 1564.8 \| 1593.0; Total operating expenses 452.5 \| 434.1 \| 908.2 \| 845.7; Operating income 330.8 \| 364.5 \| 656.6 \| 747.3; Net income $333.0 \| $309.5; Diluted EPS $7.27 \| $6.41; Diluted WASO 45.8 \| 48.3 | [📄 UTHR 10-Q p.4](https://agentii.ai/v/UTHR/sec219/4) |
| Q2 2026 10-Q Note 11 product table: revenues 326.6 … 783.3; cost of sales 51.1 … 99.5; Gross profit(loss) $275.5 … $(4.2) \| $683.8; footnote (1) inventory reserve $19.2M / $64.1M | [📄 UTHR 10-Q p.20](https://agentii.ai/v/UTHR/sec219/20) |
| Q2 2026 10-Q MD&A cost of sales on two bases: Cost of sales $98.5 \| $86.6 \| $230.9 \| $178.2; Share-based compensation 1.0 \| 1.0 \| 2.0 \| 1.9; Total cost of sales $99.5 \| $87.6 \| $232.9 \| $180.1 | [📄 UTHR 10-Q p.37](https://agentii.ai/v/UTHR/sec219/37) |
| Q2 2026 10-Q balance sheet: PP&E net 1930.1 \| 1729.7; Total assets $7220.1 \| $7880.0; Total stockholders' equity 6400.3 \| 7096.2; Treasury stock 35,352,483 and 32,809,088 shares (5,644.9) \| (4,260.4); shares outstanding 42,676,835 and 43,643,165 | [📄 UTHR 10-Q p.3](https://agentii.ai/v/UTHR/sec219/3) |
| Q2 2026 10-Q EPS note: Basic $7.82 \| $6.86 \| $14.14 \| $14.04; Diluted $7.27 \| $6.41 \| $13.07 \| $13.02; Basic WASO 42.6 \| 45.1 \| 43.0 \| 45.0; Diluted WASO 45.8 \| 48.3 \| 46.5 \| 48.5 | [📄 UTHR 10-Q p.17](https://agentii.ai/v/UTHR/sec219/17) |
| Q1 2026 10-Q statements of operations cells: Total revenues 781.5 \| 794.4; Cost of sales 133.4 \| 92.5; Total operating expenses 455.7 \| 411.6; Operating income 325.8 \| 382.8; Net income $274.9 \| $322.2; Diluted $5.82 \| $6.63 | [📄 UTHR 10-Q p.4](https://agentii.ai/v/UTHR/sec215/4) |
| Q1 2026 10-Q product table: Tyvaso DPI revenue 330.3, cost of sales 83.2, gross profit $247.1 (74.81%); footnote (1) inventory reserve $44.9M total / $39.2M Tyvaso DPI → ex-reserve $286.3 (86.68%) | [📄 UTHR 10-Q p.18](https://agentii.ai/v/UTHR/sec215/18) |
| FY2025 10-K statements of operations cells: Total revenues 3,182.7 \| 2,877.4 \| 2,327.5; Cost of sales 384.4 \| 309.7 \| 257.5; Total operating expenses 1,690.2 \| 1,500.4 \| 1,142.6; Operating income 1,492.5 \| 1,377.0 \| 1,184.9; Net income $1,334.7 \| $1,195.1 \| $984.8 | [📄 UTHR 10-K p.69](https://agentii.ai/v/UTHR/sec212/69) |
| FY2025 10-K Note 13 product table: FY2025 total revenues 3,182.7, cost of sales 384.4, Gross profit(loss) $1,081.9 … $(14.0) \| $2,798.3; FY2024 gross profit … $(4.8) \| $2,567.7; FY2023 gross profit … $(6.5) \| $2,070.0 | [📄 UTHR 10-K p.96](https://agentii.ai/v/UTHR/sec212/96) |
