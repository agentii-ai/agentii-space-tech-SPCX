---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: SPCX
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "07d26b9c738b"  # Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132) validated 9/9 against the six pins tabled in theses/001-technology-baseline/reproduce.md, which resolve to four separate plugin roots. Supersedes the UNRESOLVED gap recorded at first write.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "sign strip on negative OperatingIncomeLoss — tested by the component identity (gross profit − opex) at consolidated and all three segment levels, never by EPS × shares; CONFIRMED"
  - da_id: "DA-24"
    chosen_reading: "disposal gain inside the operating line — REFUTED at SPCX: the $856M EchoStar flow is a cash outflow capitalized to prepaid assets and never enters the operating line"
  - da_id: "DA-25"
    chosen_reading: "issuer-defined per-unit metric not reproducible from the segment tables — CONFIRMED: Starlink ARPU's denominator is never disclosed and its numerator is a sub-line beneath Consumer revenues"
  - da_id: "DA-26"
    chosen_reading: "annual value mislabelled as quarterly — NOT TESTABLE at SPCX: no annual period exists in the corpus; register as unresolved, not clean"
  - da_id: "DA-27"
    chosen_reading: "fiscal labels generated from the calendar quarter — CONFIRMED on method (fiscal_year_end_month_source: default, periods synthesised into FY2027); benign on outcome (SPCX is a Dec-31 filer)"
  - da_id: "DA-28"
    chosen_reading: "IPO capital-structure discontinuity — CONFIRMED as an open exposure: seven disagreeing share counts on three axes across three dates, no basis label; the specific split-basis mechanism is NOT demonstrated"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
citations:
  - figure: "Consolidated Results of Operations: Revenue 7,814; cost of revenue 3,495 + R&D 3,548 + SG&A 912 + restructuring 2 + impairment 0 = total costs and expenses 7,957; Loss from operations (143); net loss (541). Six-month: 12,508 / 14,594 / (2,086) / (4,817)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 40
    url: https://agentii.ai/v/SPCX/sec8/40
    located_via: read_source_pages
  - figure: "Space segment: revenue 962, total costs 1,504, Loss from operations (542) [3M 2026]; (1,204) [6M 2026]; (369) [3M 2025]; (439) [6M 2025]"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 42
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: read_source_pages
  - figure: "Connectivity segment: revenue 4,291, cost of revenue 2,060, Income from operations 1,656 [3M 2026]; 2,844 [6M 2026]; 923 [3M 2025]; 1,956 [6M 2025] — the only genuinely positive operating line"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 43
    url: https://agentii.ai/v/SPCX/sec8/43
    located_via: read_source_pages
  - figure: "AI segment: revenue 2,561, cost of revenue 1,106, total costs 3,818, Loss from operations (1,257) [3M 2026]; (3,726) [6M 2026]; (1,524) [3M 2025]; (2,460) [6M 2025]"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 44
    url: https://agentii.ai/v/SPCX/sec8/44
    located_via: read_source_pages
  - figure: "Key business metrics: Falcon launches 37 (10 customer + 27 internal) and Starship launches 1 for 3M 2026; 77 (17 + 60) and 1 for 6M 2026; footnote 'all Starship launches have been classified as internal'"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 35
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "Starlink ARPU definition and $66 [3M 2026] / $66 [6M 2026] / $85 [3M 2025] / $85 [6M 2025]; Starlink subscribers 12.0M and 6.0M as of period end"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 36
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "EchoStar Spectrum Transaction: $856M paid to the Trust on 2026-05-22, recognized as prepaid assets in Other assets until the Spectrum Acquisition Closing"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 15
    url: https://agentii.ai/v/SPCX/sec8/15
    located_via: read_source_pages
  - figure: "Spectrum consideration ~$19.6B: ~$11.1B equity via ~261.8M Class A shares at a fixed value of $42.40 per share, plus up to $8.5B of EchoStar debt payoff; $1,241M of credit-agreement payments expected in 2026, of which $856M paid as of June 30, 2026"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 49
    url: https://agentii.ai/v/SPCX/sec8/49
    located_via: read_source_pages
  - figure: "Cash flows 6M 2026: operating 3,466; investing (34,487) including 'payments to EchoStar for the Spectrum Licenses of $856 million'; financing 100,291 including $85,675M of IPO proceeds"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 50
    url: https://agentii.ai/v/SPCX/sec8/50
    located_via: read_source_pages
  - figure: "Net income (loss) attributable to shareholders (541) [3M 2026] and (5,488) [6M 2026]; EPS basic and diluted $(0.09), $(0.34), $(1.12), $(0.53); weighted-average shares 5,864M / 2,929M / 4,879M / 2,902M"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec8/5
    located_via: read_source_pages
  - figure: "Cash and cash equivalents 24,747 + restricted cash 182 + 195 = 25,124 'Total as presented in the consolidated statements of cash flows' at 2025-12-31 (the figure the calculation run serves as us-gaap:Assets)"
    ticker: SPCX
    form_type: 10-Q
    citation_id: sec8
    page_no: 12
    url: https://agentii.ai/v/SPCX/sec8/12
    located_via: read_source_pages
  - figure: "8-K Space segment table: customer launches 10, internal launches 28, Total launches 38 for 3M 2026 (and 10/28/38 against the 10-Q's 37 Falcon + 1 Starship); 6M 2026 17 / 61 / 78"
    ticker: SPCX
    form_type: 8-K
    citation_id: sec7
    page_no: 7
    url: https://agentii.ai/v/SPCX/sec7/7
    located_via: read_source_pages
  - figure: "8-K Connectivity table: Starlink subscribers 12.0 / 10.3 / 6.0 (period end); ARPU $66 / $66 / $85; Consumer revenues 2,485 / 2,148 / 1,721; Enterprise & government 1,806 / 1,109 / 867; Connectivity revenues 4,291 / 3,257 / 2,588"
    ticker: SPCX
    form_type: 8-K
    citation_id: sec7
    page_no: 8
    url: https://agentii.ai/v/SPCX/sec7/8
    located_via: read_source_pages
  - figure: "8-K business highlights: Total Launches (YTD) 78; Mass to Orbit (YTD) 1,041 t; Starlink Subscribers 12.0M"
    ticker: SPCX
    form_type: 8-K
    citation_id: sec7
    page_no: 5
    url: https://agentii.ai/v/SPCX/sec7/5
    located_via: read_source_pages
---

# SPCX — Recent-Quarter Register Census, Q2 2026 (Phase 3, PIL-3)

Source: Form 10-Q, accession `0001628280-26-052535`, `sec8`, report date 2026-06-30, filed
2026-08-04 — the only 10-Q SPCX has on the platform — read against the same-day earnings
8-K `sec7` (accession `0001628280-26-052515`).

This artifact does three things: it establishes the true consolidated operating income from
the filing's own arithmetic, it discharges the six-defect census (DA-23 … DA-28) at SPCX, and
it resolves the launch-count "phantom discrepancy" between the 10-Q and the 8-K.

**Summary of verdicts**

| DA | Verdict at SPCX | Basis |
|---|---|---|
| DA-23 | **CONFIRMED** (16 of 16 operating facts sign-stripped) | component identity; detectors 2 and 3 both fail |
| DA-24 | **REFUTED** | the $856M EchoStar flow is a capitalized outflow, never in the operating line |
| DA-25 | **CONFIRMED** | ARPU not reproducible from any disclosed line (three bases recorded) |
| DA-26 | **NOT TESTABLE** | no annual period exists in the corpus — unresolved, not clean |
| DA-27 | **CONFIRMED (method), benign (outcome)** | `fiscal_year_end_month_source: "default"`; labels synthesised |
| DA-28 | **CONFIRMED as exposure** | seven share counts, three axes, no basis label; split mechanism not demonstrated |

---

## 1. The true consolidated operating income is **$(143)M** for Q2 2026

Derived from the filing's own arithmetic, at the consolidated line, showing every component.
All four periods close exactly, at two independent levels.

**Level 1 — the consolidated statement identity** (revenue less the sum of the cost lines):
[📄 SPCX 10-Q p.40](https://agentii.ai/v/SPCX/sec8/40)

```
Revenue                                                        7,814
Costs and expenses
  Cost of revenue                                              3,495
  Research and development                                     3,548
  Selling, general, and administrative                           912
  Restructuring charges (credits)                                  2
  Impairment                                                       —
                                                -----------------------
  Total costs and expenses                                     7,957   ← equals the filed total
Loss from operations                                          (143)     ← the filing's own result
```

**Level 2 — the segment cross-check** (the three segment operating lines sum to the same number):
[📄 SPCX 10-Q p.44](https://agentii.ai/v/SPCX/sec8/44) ·
[📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) ·
[📄 SPCX 10-Q p.43](https://agentii.ai/v/SPCX/sec8/43)

```
AI segment loss from operations            (1,257)
Space segment loss from operations           (542)
Connectivity segment income from ops        1,656
                                     ---------------
Consolidated                                 (143)   ← closes exactly
```

Both levels, all four periods:

| Period | Revenue − Σcosts | Segment sum | Filing's line |
|---|---|---|---|
| 3M 2026 | 7,814 − 7,957 | (1,257) + (542) + 1,656 | **(143)** |
| 6M 2026 | 12,508 − 14,594 | (3,726) + (1,204) + 2,844 | **(2,086)** |
| 3M 2025 | 4,071 − 5,041 | (1,524) + (369) + 923 | **(970)** |
| 6M 2025 | 8,138 − 9,081 | (2,460) + (439) + 1,956 | **(943)** |

**8 of 8 identities close with zero residual.** The 6M 2025 cost lines are
4,244 + 3,515 + 1,099 + 194 + 29 = 9,081 and the 3M 2025 lines are
2,282 + 1,958 + 606 + 190 + 5 = 5,041, both equal to the filed totals
[📄 SPCX 10-Q p.40](https://agentii.ai/v/SPCX/sec8/40).

The filing states the sign in prose as well as in figures: "Space loss from operations …
increased by $173 million, or 46.9%" [📄 p.42](https://agentii.ai/v/SPCX/sec8/42);
"Connectivity income from operations … increased by $733 million, or 79.4%"
[📄 p.43](https://agentii.ai/v/SPCX/sec8/43). The prose and the tables agree. **The result is
a loss of $143 million, and there is no reading of this filing under which SPCX earned
operating income in Q2 2026.**

Phase 1's segment identities (`962 − 329 − 1,076 − 99 = −542`) are not re-derived here; they
stand as written in `2026-09-18_1500_operational-kpi_methodology.md` §5. This artifact adds
the **consolidated** identity, which Phase 1 did not close.

---

## 2. Which of the three instrument values is closest — and why none is usable

| Basis | Value, 3M 2026 | Error vs. the filed $(143)M |
|---|---|---|
| `computed` | **$(4,578)M** | **32.0×** the true magnitude |
| `reported` | **+$143M** | magnitude exact, **sign inverted** |
| filed (statement face) | **$(143)M** | correct |

**`reported` is closest, and it is not usable.** Its magnitude is exactly right; only the sign
differs. That makes it the nearer of the two instrument columns on any metric, and it is the
more dangerous of the two on every decision that follows — a $143M operating loss is served as
$143M of operating income. The error direction is the value-destroying one.

**`computed` is wrong by 32.0× and wrong in the opposite direction** (excessively negative):
4,578 / 143 = 32.01. The task brief's "wrong by 30×" is the same finding to one significant
figure. Its error is not a sign artefact but a corrupted cost base:

```
Implied engine cost base = computed(OI) inverted = 7,814 + 4,578 = 12,392
Filed total costs and expenses (p.40)                               = 7,957
Overstatement                                                     + 4,435  (+55.7%)
```

That implied base is **exactly reproducible** from the filing's own lines as the current *and*
comparative three-month columns with one line dropped:

```
3,495 + 3,548 + 912 + 2 + 0   (all of 3M 2026)      =  7,957
+ 2,282 + 1,958 + 190 + 5     (3M 2025 less SG&A)   =  4,435
                                                      -------
                                                      12,392   ← matches to the dollar
```

The omitted item is the 2025 three-month SG&A of 606. I pulled that fact specifically to test
whether it was tagged differently: it carries `us-gaap:SellingGeneralAndAdministrativeExpense`
at 606,000,000 under the identical dimension as its 2026 counterpart, so **the omission is not
a tagging difference and the mechanism is only partly explained.** The 2025 row's implied cost
base (4,071 + 4,615 = 8,686 against a filed 5,041, +72.3%) is **not decomposed**. The 12,392
decomposition above is an arithmetic identity and is labelled `DEMONSTRATED`; the engine's
rule is labelled `MODELED` and is stated as a bounded observation, not a conclusion.

**A contradiction inside the same calculation run** removes any hope of repairing `computed`:
for the 2025 three-month period the run prints `CostsAndExpenses` computed = reported = 5,041
(status pass), while its parent `OperatingIncomeLoss` for the same period implies a cost base
of 8,686 — because 4,071 − 5,041 = (970), not (4,615). The parent's computed value is **not
derived from the child computed value printed beside it in the same run.**

**Neither column is usable, for a reason that does not depend on magnitude.** The strip is in
the XBRL fact itself, not in the display layer. `search_xbrl_facts` with `include_all_sources=true`
— the audit view — returns exactly four undimensioned `OperatingIncomeLoss` facts for this
issuer, all positive: 143 (3M 2026), 2,086 (6M 2026), 970 (3M 2025), 943 (6M 2025). The
negative values do not exist at any access level, so no re-read, no wider source setting and
no sign heuristic can recover them from the platform. The sign must come from the document.

**The strip is not confined to the operating line**, which is why the contract's `EPS × shares`
prohibition is load-bearing rather than stylistic:

```
EarningsPerShareBasic served  = +0.09     (filed: $(0.09)  — p.5)
WeightedAverage shares served = 5,864M
EPS × shares                  = +528      for a quarter the filing reports as a $541M net loss
```

Both inputs are independently sign-stripped, so the reconstruction returns a **profit** of
$528M. Its error looks like a mere sign flip while the underlying defect is a double strip —
exactly the ambiguity the contract rules inadmissible.

**And the status column cannot be used to filter any of this.** The row
`NetIncomeLossAvailableToCommonStockholdersDiluted`, period 2026-06-30, carries computed = 541,
reported = 541, status **pass** — and 541 is the sign-stripped magnitude of the $541M net loss
the filing reports at [📄 p.40](https://agentii.ai/v/SPCX/sec8/40). **A passing row carrying a
sign-stripped fact.** The instruction not to report the status column is therefore not a
precaution at SPCX; it is required, and this artifact treats pass/fail as uninformative
throughout.

---

## 3. DA-23 verdict: confirmed, and the register's detectors would have missed it

**DA-23 is CONFIRMED at SPCX, at every level.** 16 of 16 `OperatingIncomeLoss` facts are
sign-stripped where negative, and none where positive:

| Member | 3M 2026 | 6M 2026 | 3M 2025 | 6M 2025 | served sign |
|---|---|---|---|---|---|
| AI (`spcx:AIMember`) | (1,257) → 1,257 | (3,726) → 3,726 | (1,524) → 1,524 | (2,460) → 2,460 | stripped |
| Space (`spcx:SpaceMember`) | (542) → 542 | (1,204) → 1,204 | (369) → 369 | (439) → 439 | stripped |
| Connectivity | 1,656 | 2,844 | 923 | 1,956 | clean |
| Total row | (143) → 143 | (2,086) → 2,086 | (970) → 970 | (943) → 943 | stripped |

12 of 12 negative values stripped; 4 of 4 positive values clean; **zero exceptions.** The
Connectivity line is the control: it is genuinely positive in all four periods and is served
positive in all four — the strip is sign-conditional, not a scaling or concept error.

**Detector 2 (sign reconciliation) does not fire.** The test `|computed| == |reported|` with
opposite signs fails arithmetically: |4,578| ≠ 143 and |4,615| ≠ 970. At SPCX the detector
would have to equate two independently corrupt numbers to fire, and they are corrupt
differently. It is silent.

**Detector 3 (the gross-profit bound) does not fire at any level.** Operating income must not
exceed gross profit; here the served value sits comfortably inside gross profit everywhere:

| Level | Revenue | Cost of revenue | Gross profit | Served OI | Bound |
|---|---|---|---|---|---|
| Consolidated | 7,814 | 3,495 | 4,319 | 143 | passes |
| Space | 962 | 329 | 633 | 542 | passes |
| Connectivity | 4,291 | 2,060 | 2,231 | 1,656 | passes |
| AI | 2,561 | 1,106 | 1,455 | 1,257 | passes |

The AI case is the closest miss in the filing — a $1,257M *loss* served as income sits only
$198M inside a $1,455M gross profit — but it passes, and a bound test that passes on the
worst case in the document carries no information.

**Only detector 1 — the component identity — catches it**, and it catches it at all four
periods because the identity closes to zero (§1). This is the same result Phase 1 recorded in
its carry-forward #10 for the segment identities; this artifact extends it to the consolidated
line and to the four undimensioned facts.

**Corollary for the register:** at SPCX the served operating income is *positive where the
truth is a loss*. On the two detectors the register relies on for scale, SPCX is a **false
negative**. DA-23's coverage claim ("6 of 6 loss-making stripped") survives; its *detection*
claim does not, and the failure is silent.

---

## 4. DA-24 — REFUTED at SPCX, and the brief's premise is inverted

The register's test is a disposal gain landing inside the operating line, and the brief points
at "$856M EchoStar spectrum instalment" received. The filing says SPCX **paid** it:

- "the Company has made contractual payments under the Spectrum Credit Agreement to the Trust
  of **$856 million**, which is recognized as **prepaid assets in Other assets** until the
  Spectrum Acquisition Closing, at which point they will be recognized as intangible assets."
  [📄 SPCX 10-Q p.15](https://agentii.ai/v/SPCX/sec8/15)
- "Total payments expected to be made under the Spectrum Credit Agreement are $1,241 million in
  2026, of which $856 million was paid as of June 30, 2026, and $828 million in 2027"
  [📄 SPCX 10-Q p.49](https://agentii.ai/v/SPCX/sec8/49)
- The transfer close was 2026-05-22; SPCX is the **acquirer**, for total consideration of
  approximately $19.6B (≈$11.1B of equity plus up to $8.5B of EchoStar debt payoff)
  [📄 p.49](https://agentii.ai/v/SPCX/sec8/49)
- In the cash-flow statement the $856M appears in **investing activities**, as "an increase in
  payments to EchoStar for the Spectrum Licenses of $856 million"
  [📄 SPCX 10-Q p.50](https://agentii.ai/v/SPCX/sec8/50)

The flow is: cash **out**, capitalized to a **balance-sheet** prepaid asset, then reclassified
to intangibles at closing. It never enters the operating line and no gain is recognized. The
structured loan-forgiveness is explicitly "accounted for as additional consideration for the
acquisition of the Spectrum Licenses" [📄 p.15](https://agentii.ai/v/SPCX/sec8/15) — i.e. it
increases an asset, it does not create income.

**Verdict: DA-24 is not exhibited at SPCX. The defect present is in the brief, not the data —
the direction of the cash flow is inverted.** Recorded here under the frozen-001 policy rather
than corrected upstream: the premise "SPCX received an ~$856M EchoStar spectrum instalment"
should read "SPCX paid $856M, capitalized as a prepaid asset".

*Scope of this refutation:* I read 8 of the 10-Q's 55 rows. The finding is that the specific
flow the register names does not touch the operating line; it is not an exhaustive scan for
disposal gains elsewhere in the document.

---

## 5. DA-25 — CONFIRMED: Starlink ARPU is not reproducible from the segment tables

The issuer defines the metric as "service revenue generated from Starlink subscribers during
the period divided by (i) the **average** number of Starlink subscribers during the period and
by (ii) the number of months in the period"
[📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36).

Both inputs are undisclosed:

1. **The denominator is never disclosed.** The filing publishes only **period-end** subscriber
   counts — 12.0M at 2026-06-30, 10.3M at 2026-03-31, 6.0M at 2025-06-30
   [📄 p.36](https://agentii.ai/v/SPCX/sec8/36) · [📄 SPCX 8-K p.8](https://agentii.ai/v/SPCX/sec7/8).
   The **average** does not appear anywhere in the corpus.
2. **The numerator is a sub-line beneath the smallest disclosed revenue line.** Connectivity
   revenue is split only into Consumer revenues and Enterprise & government revenues
   [📄 SPCX 8-K p.8](https://agentii.ai/v/SPCX/sec7/8), and the subscriber definition
   *excludes* "managed enterprise and government customers with contracts in domains including
   aviation, maritime, land mobility, fixed sites, and government entities"
   [📄 p.35](https://agentii.ai/v/SPCX/sec8/35).

Testing every disclosed basis against the reported $66 [📄 p.36](https://agentii.ai/v/SPCX/sec8/36)
for Q2 2026 — the §1c `no_single_basis_collapse` rule requires all three be reported and none
be collapsed to:

| Basis used | Arithmetic | Result | vs. reported $66 |
|---|---|---|---|
| Connectivity revenue ÷ period-end subs | 4,291 / 12.0 / 3 | **$119/mo** | +80% |
| Consumer revenue ÷ period-end subs | 2,485 / 12.0 / 3 | **$69/mo** | +5% |
| Implied numerator ÷ true average subs | see bound below | **$66/mo** | requires an undisclosed numerator |

Because subscribers grew 10.3M → 12.0M across the quarter, the average lies in (10.3M, 12.0M),
which **bounds** the issuer's numerator:

```
Implied service revenue ∈ $66 × 3 × (10.3M, 12.0M) = ($2,039M, $2,376M)
Disclosed Consumer revenues                        =  $2,485M
Unexplained gap                                    =  $109M – $446M
```

**The ARPU numerator is strictly smaller than the smallest revenue line the filing discloses,
and by an amount the filing never explains.** The metric is not merely hard to reproduce from
the segment tables — it is unreproducible by construction, and the same test fails in the
other direction at the prior-year comparative: $85 × 3 × 6.0M = $1,530M against Consumer
revenues of $1,721M, and the implied average of 1,721 / (85 × 3) = **6.75M** exceeds the
period-end count of 6.0M — impossible for a base that doubled year over year
[📄 p.36](https://agentii.ai/v/SPCX/sec8/36) · [📄 p.43](https://agentii.ai/v/SPCX/sec8/43).

**Verdict: DA-25 CONFIRMED.** ARPU cannot be recomputed, cannot be audited against the segment
tables, and — because its numerator excludes the fastest-growing revenue bucket (Enterprise &
government, +108% YoY, [📄 8-K p.8](https://agentii.ai/v/SPCX/sec7/8)) — it understates the
business it is used to describe.

---

## 6. DA-26 — NOT TESTABLE: there is no Q4 row to check

The register's test is an annual value mislabelled as quarterly. At SPCX the test cannot run:

- `search_xbrl_facts(SPCX, fiscal_period="Q4")` returns **0 facts**.
- The corpus holds 10 SPCX documents: **one 10-Q, eight 8-Ks** (six of them the June 2026 IPO
  sequence, 2026-06-15 through 2026-06-26, plus 2026-08-04 and 2026-08-14) and one
  earnings-call transcript. **There is no 10-K and no annual period.**
- `get_company_financials(SPCX)` reports `statements_available: false` with the note that
  rendered statements are pending.
- The one row that does exist is correctly quarterly: the earnings calendar carries
  `fiscal_quarter: "2026 (Q2)"`, `eps_actual: "-0.09"`, `revenue_actual: "7814000000"`,
  `fiscal_source: "ect_exact"` — all three-month values, correctly labelled. (The same row has
  `eps_prior_year: null` although the 10-Q discloses the prior-year figure
  [📄 p.5](https://agentii.ai/v/SPCX/sec8/5) — a coverage gap, not a mislabel, and not a DA-26
  instance.)

**Verdict: DA-26 is not exhibited because it is not testable.** The register entry must read
**unresolved (no test possible)**, **not clean** — the distinction is load-bearing for PIL-3's
own falsifier, `count_of_universe_issuer_quarters_with_unresolved_defect_status`, which counts
exactly this state. A no-10-K issuer is a structural blind spot for a defect defined on annual
periods, and SPCX will remain one until it files a 10-K.

---

## 7. DA-27 — CONFIRMED on method, benign on outcome

`get_company_fiscal_calendar(SPCX)` returns:

```
fiscal_year_end_month:        12
fiscal_year_end_month_source: "default"        ← not read from the filing
cross_validation_hint:        "No XBRL data available for this ticker — fiscal calendar
                               may be inaccurate. Confirm fiscal year-end manually…"
```

Three findings, in descending order of importance:

1. **The fiscal year-end is a defaulted constant, not evidence.** The source field says
   `default`, so the label carries no documentary trail. The tool also synthesises quarter
   boundaries it cannot have read from any document — it enumerates **FY2027 Q1 through Q4**,
   including 2027-10-01..2027-12-31, for a company whose latest filing is dated 2026-08-04.
   That is DA-27's mechanism exactly: **fiscal labels generated from the calendar, not from the
   filing.**
2. **The tool's own cross-validation hint is false.** It asserts "No XBRL data available for
   this ticker" while the same ticker serves **1,647 XBRL facts** from
   `get_company_financials(SPCX)`. A cross-validation path that cannot see 1,647 facts it is
   warning about is not a cross-check; it is a second coverage path in disagreement with the
   first.
3. **The outcome happens to be correct.** SPCX is a Dec-31 filer: the 10-Q's interim period is
   January 1 – June 30, 2026 with report date 2026-06-30
   [📄 p.40](https://agentii.ai/v/SPCX/sec8/40), so "FY2026 Q2 = 2026-04-01..2026-06-30" is
   right. It is right **by coincidence of the filer's own calendar year**, not because the
   label was derived.

**Verdict: DA-27 is exhibited (the method is defective) and the output is correct (the outcome
is not).** The register should record method and outcome as separate fields; otherwise a label
that is right by accident reads as clean, and the next non-calendar-year issuer inherits the
same code path unexamined.

---

## 8. DA-28 — CONFIRMED as an open exposure; the split mechanism is not demonstrated

**Seven share counts in one extract, disagreeing by 2.7×, on three axes, with no basis label
anywhere:**

| Value | Label | Date | Axis / class |
|---|---|---|---|
| 5,485,486,276 | `common_shares_outstanding` | 2026-06-30 | none (scalar field) |
| 5,864,000,000 | WeightedAverage…Basic / Diluted | 3M 2026 | none |
| 4,879,000,000 | WeightedAverage…Basic | 6M 2026 | none |
| 2,929,000,000 | WeightedAverage…Basic | 3M 2025 | none |
| 2,902,000,000 | WeightedAverage…Basic | 6M 2025 | none |
| 2,036,000,000 | `CommonStockSharesIssued` | 2025-12-31 | `StatementClassOfStockAxis` = CommonClassAMember |
| 3,023,000,000 | `CommonStockSharesOutstanding` | 2024-12-31 | `StatementEquityComponentsAxis` = CommonStockMember |

The June 2026 IPO (net proceeds $85,675M,
[📄 SPCX 10-Q p.50](https://agentii.ai/v/SPCX/sec8/50)) and a five-for-one split in 2026-05
(per spec §1b) both fall inside this window, which is precisely DA-28's stated hazard.

**What is demonstrated:** the artifact cannot establish a single share-count basis for SPCX,
and the counts it does serve carry no basis label — Issued vs Outstanding, three dates, two
different axis members, and a scalar field with no axis at all are mixed without
qualification.

**What is *not* demonstrated — and I decline to assert it:** that the disagreement is caused by
split-basis mixing. The heterogeneity above explains the spread on its own, and under SAB
Topic 4.C a post-balance-sheet split must be reflected retroactively in every presented share
count, so the counts are probably already on one basis. The 5:1 ratio does not close the
bridge in either direction: 2,036M × 5 = 10,180M, against 5,485,486,276 served as current
outstanding. **The share-count bridge is not derivable from the facts I verified; it requires
the 10-Q's equity note or the Prospectus, neither of which I read.**

**What is demonstrated as a defect:** the capital-structure bridge does not close in the
calculation run. `NetIncomeLossAvailableToCommonStockholdersBasic` computed 4,146 against
reported 541 (fail), in the same run whose `NetIncomeLossAvailableToCommonStockholdersDiluted`
**passes** at 541 — while the calculation tree declares Diluted ← Basic at weight 1. Two
different computed values for the same declared node in one run. The attributable-to-common
bridge *is* the capital-structure bridge (preferred dividends and the $37,475M conversion,
[📄 p.50](https://agentii.ai/v/SPCX/sec8/50)).

**Forward exposure, and the reason to register this as open rather than closed:** the Spectrum
consideration is a **fixed-value, fixed-count** instrument — approximately **261.8 million
Class A shares at a fixed value of $42.40 per share** (≈$11.1B)
[📄 SPCX 10-Q p.49](https://agentii.ai/v/SPCX/sec8/49). The filing states both the count and
the fixed value and **never states their split basis**, so the count is not comparable with the
5,485,486,276 currently served. When the Spectrum Acquisition Closing occurs, any share-count
detector at SPCX will be off by up to 5× on the largest single share issuance the company has
disclosed. The DA-28 detector spec should require a fixed-value/fixed-count instrument to
declare its split basis.

---

## 9. The phantom discrepancy: the correct reconciliation is **10 + 28 = 38**, not 27 + 1 = 28

Two documents state the quarter's launch count on different bases, and a naive diff produces a
one-launch "discrepancy" that is not there.

The 10-Q [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35):

```
Falcon launches                    37   = 10 customer + 27 internal
Starship launches                   1
```

The 8-K [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7):

```
Customer launches (#)              10
Internal launches (#)              28
Total launches (#)                 38
```

**The correct reconciliation:**

```
10 customer launches                                 10
27 internal Falcon launches                        + 27
 1 internal Starship launch                        +  1
                                                  -----
Total launches for Q2 2026                           38
```

**28 is the internal *subtotal*; 38 is the *total*.** The phantom arises because "Falcon 37" is
a Falcon-only **total** and "internal 28" is an all-vehicle **subset** — pairing them is a
basis error, and "repairing" the apparent gap as 27 + 1 = 28 silently discards the **10
customer launches**. The 10-Q footnote makes the mechanism explicit: "To date, all Starship
launches have been classified as internal," so the 8-K's internal line carries Starship while
the 10-Q reports Starship on its own row and gives the internal split only within the Falcon
row [📄 p.35](https://agentii.ai/v/SPCX/sec8/35).

**The reconciliation closes at all four periods, which proves it is the mechanism and not a
coincidence.** Note the signature: in every period the two documents' internal figures differ
by exactly the Starship count.

| Period | 10-Q Falcon (customer + internal) | 10-Q Starship | 10-Q total | 8-K customer | 8-K internal | 8-K total | internal gap = Starship |
|---|---|---|---|---|---|---|---|
| 3M 2026 | 37 (10 + 27) | 1 | 38 | 10 | 28 | 38 | 28 − 27 = **1** ✓ |
| 3M 2025 | 45 (9 + 36) | 1 | 46 | 9 | 37 | 46 | 37 − 36 = **1** ✓ |
| 6M 2026 | 77 (17 + 60) | 1 | 78 | 17 | 61 | 78 | 61 − 60 = **1** ✓ |
| 6M 2025 | 81 (21 + 60) | 3 | 84 | 21 | 63 | 84 | 63 − 60 = **3** ✓ |

Every row closes on both identities, and the 8-K's headline "Total Launches (YTD) 78"
[📄 SPCX 8-K p.5](https://agentii.ai/v/SPCX/sec7/5) equals the 6M 2026 total (77 Falcon + 1
Starship) [📄 p.35](https://agentii.ai/v/SPCX/sec8/35).

**There is no data defect here.** Both documents are internally consistent and consistent with
each other. The phantom is an analyst basis error, and the correct pair to carry is
**"38 total vs 28 internal"** — never "37 vs 28". No downstream artifact should restate the
launch count as a discrepancy.

---

## 10. Instrument observations outside the six DAs (register candidates)

Recorded because PIL-3 owns the register, and each is a defect class no DA currently covers.

**1. `us-gaap:Assets` is a cash subtotal, not total assets.** The calculation run reports
`Assets` reported = 25,124,000,000 for the 2025-12-31 instant. That number is the cash-flow
reconciliation total: cash and cash equivalents 24,747 + restricted cash 182 + 195 =
**25,124**, labelled "Total as presented in the consolidated statements of cash flows"
[📄 SPCX 10-Q p.12](https://agentii.ai/v/SPCX/sec8/12). Total assets at the same instant are
served as **92,079,000,000** elsewhere in the same payload, and as **192,770,000,000** in the
metrics block for 2026-06-30. **Four different "assets" values appear across the fact layer
(25,124 / 78,871 computed / 92,079 / 192,770), and the one the calculation run uses is the
cash-flow subtotal — 3.66× below the balance-sheet figure.** This is concept mis-tagging, and
no registered DA describes it.

**2. `NetIncomeLoss` gives two unusable columns on one row.** The run's computed value (489)
matches nothing in the filing, while its reported value for the same 2026-06-30 label is
4,817 — the **six-month** figure, in a run where `NetIncomeLossAvailableToCommonStockholdersBasic`
carries the **three-month** 541 under an identical label. Both facts exist for this issuer. The
period key is the period **end date only** and does not encode duration, so three-month and
six-month values collide silently under one label. This is a plausible upstream cause of the
operating-income corruption in §2 and it is testable; I record it as an observation, not a
diagnosis.

**3. The `fiscal_period` filter does not discriminate.** `fiscal_period="Q4"` returns 0 facts;
`fiscal_period="FY"` returns **299** facts for a filing whose fiscal period is Q2, spanning
both three-month and six-month durations. I could not determine the intended semantics.
Recorded, not explained.

**4. Entity-boundary recasting remains unregistered** (inherited from Phase 1's carry-forward
#10, unchanged here). The AI segment reports revenue of 2,561 in 3M 2026 and **737 in the 3M
2025 comparative** [📄 p.44](https://agentii.ai/v/SPCX/sec8/44), which means the comparative
already contains xAI/X businesses that closed 2025-03-28 and 2026-02-02 — the comparatives are
recast. No DA covers common-control recasting, and the practical consequence is that
`2026 vs. 2025` changes in this filing are not like-for-like at the segment level. Phase 1's
recommendation of a DA-29 stands, and the AI comparative is now a worked example for it.

---

## Carry-forwards

1. **SPCX is unresolved, not clean, on DA-26 and DA-28.** DA-26 is untestable (no annual period
   in the corpus); DA-28 is an open exposure with a named forward trigger. These are the two
   entries that feed PIL-3's falsifier
   (`count_of_universe_issuer_quarters_with_unresolved_defect_status`), and SPCX contributes to
   that count rather than to the clean set.
2. **DA-23's detection, not its coverage, is what failed at SPCX.** Two of the register's three
   detectors produce a false negative on the worst case in the document. Detector 1 (component
   identity) is the only one that works, and it needs the document. The register should record
   detection rate separately from coverage rate.
3. **Record DA-27 as method-and-outcome, separately.** The label is calendar-derived
   (`fiscal_year_end_month_source: "default"`) and correct only because SPCX is a Dec-31 filer.
   Correct-by-accident must not read as clean.
4. **Two new DA candidates from SPCX**, both outside the current six: `Assets` served as a
   cash-flow subtotal (concept mis-tagging), and the period key that omits duration so
   three-month and six-month facts collide under one label. Add Phase 1's DA-29
   (entity-boundary recasting) to the same list.
5. **Fix the fiscal-calendar cross-validation hint.** It asserts "No XBRL data available for
   this ticker" for a ticker serving 1,647 facts. Whatever the intended check is, it is
   currently inverted.
6. **The instrument rule is now filed evidence, not a precaution.** A row with
   computed = reported = 541 is marked **pass** while carrying the sign-stripped magnitude of a
   $541M net loss. Do not report the status column.
7. **Do not restate the launch count as a discrepancy.** The correct pair is 38 total vs 28
   internal; 37 vs 28 is a basis error and 27 + 1 = 28 drops the 10 customer launches.
8. **Phase 1's segment identities stand and are not re-derived here.** This artifact adds the
   consolidated identity, which closes at all four periods: (1,257) + (542) + 1,656 = (143).

## Could not be verified

- **The 2025 `computed` cost base (implied $8,686M vs filed $5,041M) is not decomposed.** The
  2026 case reproduces exactly; the 2025 case does not, and I did not chase it further.
- **The share-count bridge is not closed.** Reconciling 2,036,000,000 (2025-12-31) to
  5,485,486,276 (2026-06-30) requires the 10-Q's equity note or the Prospectus; neither was
  read. The five-for-one split (2026-05) is `CLAIMED` from spec §1b — no page read in this pass
  confirms it, and the counts neither confirm nor refute a 5:1 ratio.
- **DA-24's refutation is scoped.** It establishes that the EchoStar flow the register names
  does not touch the operating line. It is not an exhaustive scan of all 55 pages for other
  disposal gains; I read 8.
- **DA-26's status cannot be raised to "clean".** With no 10-K in the corpus the defect defined
  on annual periods is untestable at SPCX, and will stay untestable until SPCX files one.
