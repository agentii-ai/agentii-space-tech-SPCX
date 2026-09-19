---
thesis_id: "002-evidence-validation"
pillar: PIL-3
ticker: MSFT
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
# constitution_pin: the brief for this task said 1.4.0; contracts/artifact-frontmatter.yaml
# line 28 pins the field to const "1.5.0" — raised at 002 Phase 3 (this phase) when DA-29 and
# DA-30 were added. This artifact APPLIES DA-29 (every reconciliation term named, §7) and DA-30
# (the capex basis named before it is used, §3), so it is written at the pin whose rules it obeys.
# `pins_match_thesis` accepts {1.4.0, 1.5.0}; 1.4.0 is the grandfathered set for the 23 artifacts
# written before the bump. Recording 1.5.0 rather than 1.4.0 is a RECORDED, not an assumed, pin.
constitution_pin: "1.5.0"
assumption_pin: "2"
# UNRESOLVED — reason: `recent-quarter` does not appear in 001's six-hash skill table, and the
# Q57 ledger that would carry its hash does not exist. No hash is invented, and none is copied
# from a sibling skill (a copied hash would certify a contract this artifact was not run against).
skill_pin: "07d26b9c738b"  # Q57 resolved 2026-09-18: re-derived from plugins/agent-plugins/agentii-equity-agent/skills/agentii/recent-quarter AND plugins/vertical-plugins/equity-research-core/skills/agentii/recent-quarter — two independent roots AGREE. Algorithm dispatch.skill_version_hash() (scripts/dispatch.py:132) validated 9/9 against the six pins tabled in theses/001-technology-baseline/reproduce.md. Four packaging/targets trees FAIL 0/6 and are decoys. Supersedes the UNRESOLVED gap recorded at first write.
as_of: 2026-09-18
# 001's MSFT artifact used "UNPINNED". Every fact and page in this artifact was retrieved this
# session; the platform reported `data_freshness: 2027-04-12` on every call, which is a
# forward-dated marker and cannot be used as a corpus version. Nothing to pin.
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "|x| absolute-value stripping of a fact's sign — concept-agnostic, and PER-FACT, not per-period. Inversion (negation) is a DIFFERENT defect and is not what MSFT exhibits: the platform never turns a positive into a negative, only a negative into its absolute value."
  - da_id: "DA-24"
    chosen_reading: "a disposal gain sitting ABOVE the operating subtotal, tested on the calculation linkbase as an arc child of OperatingIncomeLoss"
  - da_id: "DA-25"
    chosen_reading: "an issuer-defined per-unit metric that cannot be reproduced from the filed reconciliation terms (the DA-29 corridor test applied to per-unit metrics)"
  - da_id: "DA-26"
    chosen_reading: "a twelve-month value served under a quarterly label; mechanism = fiscal_period derived as calendar_quarter(period_end)"
  - da_id: "DA-27"
    chosen_reading: "fiscal labels derived from the calendar rather than from the issuer's fiscal calendar; tested on fiscal_year_end_month and its source field"
  - da_id: "DA-28"
    chosen_reading: "IPO capital-structure discontinuity — new-issue step or preferred-stock conversion; tested on the equity rollforward's linkbase children"
  - da_id: "DA-29"
    chosen_reading: "defective checks — every reconciliation term must be NAMED and located in the source; the residue is the total a back-solve cannot be caught by, so the terms must be checked, not the closure"
  - da_id: "DA-30"
    chosen_reading: "a basis the platform collapses before an artifact sees it; the artifact must NAME the basis and state where the basis was established, PRIOR to any use"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
citations:
  - figure: "Other income (expense), net 10,697 / (4,901) / (1,646) for FY2026/FY2025/FY2024 — the three DA-23 income-statement instances, one row of one table"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 52
    url: https://agentii.ai/v/MSFT/sec185/52
    located_via: search_keyword_in_source
  - figure: "Net cash used in financing (52,546); Net cash used in investing (139,500); Net change in cash and cash equivalents (9,307); Additions to property and equipment (35,802) / (17,079) / (115,948) / (64,551) — the capex figure validated and the cash-flow DA-23 strips"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 55
    url: https://agentii.ai/v/MSFT/sec185/55
    located_via: read_source_pages
  - figure: "Segment revenue / cost of revenue / operating expenses / operating income for the three segments and the Total row (331,839 − 106,374 − 70,228 = 155,237) — multi-level component identity"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 86
    url: https://agentii.ai/v/MSFT/sec185/86
    located_via: search_keyword_in_source
  - figure: "Total, at cost 431,767 / 298,619; Accumulated depreciation (118,691) / (93,653); Servers, network equipment, and software 215,874 / 132,836 — the second and third capex BASES (DA-30)"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 71
    url: https://agentii.ai/v/MSFT/sec185/71
    located_via: read_source_pages
  - figure: "GAAP to non-GAAP reconciliation: Net income 133,749; Net (gains) losses from investments in OpenAI, net of tax of $1,567, (4,963); Adjusted net income (non-GAAP) 128,786; Diluted EPS 17.95; Adjusted diluted EPS (non-GAAP) 17.28 — every DA-29 term named and located"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 44
    url: https://agentii.ai/v/MSFT/sec185/44
    located_via: read_source_pages
  - figure: "MD&A: Microsoft Cloud revenue $214.4 billion (+27%), commercial RPO $678B (+84%) — the DA-25 candidate, an issuer-defined cross-segment aggregation"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 36
    url: https://agentii.ai/v/MSFT/sec185/36
    located_via: read_source_pages
  - figure: "Other income (expense), net included $6.5 billion of net gains and $4.8 billion of net losses for fiscal years 2026 and 2025, respectively, from investments in OpenAI"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 43
    url: https://agentii.ai/v/MSFT/sec185/43
    located_via: read_source_pages
  - figure: "OpenAI equity-method investee, ~25% as-converted, related party per ASC 850, HLBV method, $13.0B commitments of which $11.9B funded — the cross-holding basis"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 62
    url: https://agentii.ai/v/MSFT/sec185/62
    located_via: read_source_pages
  - figure: "Q4 FY2026 three-month income statement: Gross margin 60,482; Total operating expenses 19,879; Operating income 40,603; Net impact from OpenAI $(8,583) / $480M, $0.07"
    ticker: MSFT
    form_type: 8-K
    citation_id: sec184
    page_no: 10
    url: https://agentii.ai/v/MSFT/sec184/10
    located_via: read_source_pages
  - figure: "Q4 FY2026 cash-flow cells: Net cash used in investing (54,831); Additions to property and equipment (35,802)"
    ticker: MSFT
    form_type: 8-K
    citation_id: sec184
    page_no: 13
    url: https://agentii.ai/v/MSFT/sec184/13
    located_via: read_source_pages
  - figure: "Q4 FY2026 segment table incl. More Personal Computing operating income 14,386 — the value the instrument serves as consolidated OperatingIncomeLoss"
    ticker: MSFT
    form_type: 8-K
    citation_id: sec184
    page_no: 14
    url: https://agentii.ai/v/MSFT/sec184/14
    located_via: read_source_pages
  - figure: "Consolidated balance sheet: total stockholders' equity 442,387; cash and cash equivalents 30,242 / 20,935"
    ticker: MSFT
    form_type: 10-K
    citation_id: sec185
    page_no: 54
    url: https://agentii.ai/v/MSFT/sec185/54
    located_via: read_source_pages
key_metrics:
  capex_bases_disclosed: 4
  capex_spread_pct: 63
  facts_stripped: 27
  facts_clean: 11

---

# MSFT × recent-quarter — Defect Census

**Pillar** PIL-3 · **Ticker** MSFT · **Skill** `recent-quarter` · **Mode** methodology

**Role in this thesis.** MSFT is the terrestrial-compute comparator the orbital case must beat,
and it is 001's strongest single datum: **FY2026 capex $115,948M**, which at the reported
$10–40M/MW implies **2.9–11.6 GW of new capacity annually**. That number is re-validated here
from the statement face (§3) and it is **correct**. What is not correct is the sentence built
on it, and — far more seriously — the claim 001 made *about the platform itself* (§2).

**Scope of the census.** Every period, every fact, per the DA-23 rule. 38 facts measured on
three statement surfaces across five fiscal years. Four defect classes confirmed, four tested
and discharged clean, one non-applicable, one basis collapse found on the very figure PIL-3
exists to validate.

**Provenance of every page number.** All citations use **platform** page numbers. The printed
footers on the seven pages I read in `sec185` (52, 36, 43, 44, 62, 71, 86) are each **+2** below
the platform number (page 52 prints "50"; page 86 prints "84"). The offset is *not* corrected
anywhere in this artifact, and I did not measure the footer on p.55 — so no offset claim is made
about it. A right citation turned into a wrong one by "correcting" it is worse than no citation.

---

## 1. Headline: 001's own conclusion about MSFT is falsified, and the method is the reason

001's §3 concluded:

> "MSFT is profitable and therefore unaffected by DA-23, extending the rule to **8 of 8 positive
> values clean** (against 4 of 4 negatives stripped) — 12 issuer-quarters, zero exceptions."

**This is false, and it is falsified by a single row of a single table on one page.**

p.52, "INCOME STATEMENTS", the row `Other income (expense), net` [📄 MSFT 10-K p.52](https://agentii.ai/v/MSFT/sec185/52):

| Fiscal year | Filed cell (p.52) | Platform served value | DA-23 |
|---|---|---|---|
| 2026 | `10,697` | `+10,697,000,000` | clean |
| 2025 | `(4,901)` | `+4,901,000,000` | **STRIPPED** |
| 2024 | `(1,646)` | `+1,646,000,000` | **STRIPPED** |

**Two of three facts in one row, in one filing, in one table are sign-stripped — on a
profitable issuer.** The strip tracks **the sign of the individual fact**, not the issuer's
profitability, not the period, and not the concept.

**Why 001 missed it.** 001 sampled `OperatingIncomeLoss` — a positive subtotal that a profitable
company will always report positive — found 8 of 8 clean, and generalised from the fact to the
concept class and then to the issuer. That is a **sampling error with a direction**: a
profitable issuer's *subtotal* facts are all positive by construction, so an instrument that
strips negatives will pass every one of them and the test cannot fail. **The register's own rule
— "DA-23 MUST RUN ON EVERY PERIOD AND EVERY FACT" — is exactly the rule that 001's method, as
executed, could not satisfy while it held only the profitable side of the ledger.**

---

## 2. DA-23 census — per period, per fact

### 2.1 Income statement: `NonoperatingIncomeExpense` (parent)

Sign convention fixed by the linkbase: `NonoperatingIncomeExpense` enters
`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` at **weight +1**, so its own signed value
must be used as filed. Filed cells read from p.52 and corroborated by the note's own component
table; served values read from `search_xbrl_facts`.

| Period end | Filed | Served | DA-23 |
|---|---|---|---|
| 2026-06-30 (12M) | `10,697` | +10,697,000,000 | clean |
| 2026-03-31 (9M) | `7,253` | +7,253,000,000 | clean |
| 2026-03-31 (3M) | `942` | +942,000,000 | clean |
| 2025-12-31 (6M) | `6,311` | +6,311,000,000 | clean |
| 2025-12-31 (3M) | `9,971` | +9,971,000,000 | clean |
| **2025-09-30 (3M)** | **`(3,660)`** | **+3,660,000,000** | **STRIPPED** |
| **2025-06-30 (12M)** | **`(4,901)`** | **+4,901,000,000** | **STRIPPED** |
| **2025-03-31 (9M)** | **`(3,194)`** | **+3,194,000,000** | **STRIPPED** |
| **2025-03-31 (3M)** | **`(623)`** | **+623,000,000** | **STRIPPED** |
| **2024-12-31 (6M)** | **`(2,571)`** | **+2,571,000,000** | **STRIPPED** |
| **2024-12-31 (3M)** | **`(2,288)`** | **+2,288,000,000** | **STRIPPED** |
| **2024-09-30 (3M)** | **`(283)`** | **+283,000,000** | **STRIPPED** |
| **2024-06-30 (12M)** | **`(1,646)`** | **+1,646,000,000** | **STRIPPED** |
| **2024-03-31 (9M)** | **`(971)`** | **+971,000,000** | **STRIPPED** |
| **2024-03-31 (3M)** | **`(854)`** | **+854,000,000** | **STRIPPED** |

**15 facts. 9 stripped. 6 clean. Every stripped fact was filed negative. Every fact filed
positive was served positive — including all six.** There is no inversion anywhere: the platform
never produced a negative from a positive. `|x|`, not `−x`.

### 2.2 Income statement: `OtherNonoperatingIncomeExpense` (child of the above, weight +1)

| Period end | Filed | Served | DA-23 |
|---|---|---|---|
| 2026-06-30 (12M) | `4,722` | +4,722,000,000 | clean |
| 2026-03-31 (9M) | `4,127` | +4,127,000,000 | clean |
| **2026-03-31 (3M)** | **`(491)`** | **+491,000,000** | **STRIPPED** |
| 2025-12-31 (6M) | `4,618` | +4,618,000,000 | clean |
| 2025-12-31 (3M) | `9,541` | +9,541,000,000 | clean |
| **2025-09-30 (3M)** | **`(4,923)`** | **+4,923,000,000** | **STRIPPED** |
| **2025-06-30 (12M)** | **`(4,725)`** | **+4,725,000,000** | **STRIPPED** |
| **2025-03-31 (9M)** | **`(2,861)`** | **+2,861,000,000** | **STRIPPED** |
| **2025-03-31 (3M)** | **`(1,013)`** | **+1,013,000,000** | **STRIPPED** |
| **2024-12-31 (3M)** | **`(1,165)`** | **+1,165,000,000** | **STRIPPED** |
| **2024-09-30 (3M)** | **`(683)`** | **+683,000,000** | **STRIPPED** |
| **2024-06-30 (12M)** | **`(1,319)`** | **+1,319,000,000** | **STRIPPED** |
| **2024-03-31 (9M)** | **`(792)`** | **+792,000,000** | **STRIPPED** |
| **2024-03-31 (3M)** | **`(486)`** | **+486,000,000** | **STRIPPED** |

**14 facts. 10 stripped. 4 clean.** Same signature. The parent and the child are stripped
*independently* — `NonoperatingIncomeExpense` is clean at 2026-06-30 while its child is clean
there too, and both are stripped at 2025-03-31; but at 2026-03-31 the parent is clean (`942`)
while the child is stripped (`(491)`). **Per-fact, not per-line, not per-period.**

### 2.3 Cash flow: three subtotal concepts, three fiscal years

Filed cells read from p.55 [📄 MSFT 10-K p.55](https://agentii.ai/v/MSFT/sec185/55):
`Net cash used in financing (52,546)`, `Net cash used in investing (139,500)`,
`Net change in cash and cash equivalents (9,307)`.

| Concept | FY | Filed | Served | DA-23 |
|---|---|---|---|---|
| `NetCashProvidedByUsedInFinancingActivities` | 2026 | `(52,546)` | +52,546,000,000 | **STRIPPED** |
| | 2025 | `(51,699)` | +51,699,000,000 | **STRIPPED** |
| | 2024 | `(37,757)` | +37,757,000,000 | **STRIPPED** |
| `NetCashProvidedByUsedInInvestingActivities` | 2026 | `(139,500)` | +139,500,000,000 | **STRIPPED** |
| | 2025 | `(72,599)` | +72,599,000,000 | **STRIPPED** |
| | 2024 | `(96,970)` | +96,970,000,000 | **STRIPPED** |
| `CashCashEquivalents…PeriodIncreaseDecrease…` | 2026 | `(9,307)` | +9,307,000,000 | **STRIPPED** |
| | 2025 | `11,927` | +11,927,000,000 | **clean (positive control)** |
| | 2024 | `(16,389)` | +16,389,000,000 | **STRIPPED** |

**8 stripped, 1 clean — and the clean one is the only positive.** The FY2025 `11,927` is the
control that makes the FY2024/FY2026 strips unambiguous: same concept, same table, same column
group, three consecutive years, and the served values are `+9,307 / +11,927 / +16,389` against
filed `(9,307) / 11,927 / (16,389)`. **The strip follows the sign of the fact, exactly.**

**Census total: 38 facts measured, 27 stripped, 11 clean. Zero inversions. Zero stripped
positives. Zero clean negatives.** DA-23 at MSFT is not an edge case; it is the default
behaviour for any negative fact, and it is invisible to any test built on positive subtotals.

### 2.4 🔴 The filing-free proof: the platform contradicts *itself*

**First: the platform contradicts itself.** At 2025-03-31 (FY2025 Q3), summing the platform's
own served components of `Other income (expense), net`:

```
served: 597 − 594 + 111 + 187 + 89 + 1,013  =  1,403
platform's OWN served parent NonoperatingIncomeExpense  =     623
                              irreconcilable by           780
```

No filing is needed to see that these two numbers cannot both be right — the platform's own
returned data is internally inconsistent. **Second: exactly one of them matches the filing.**
Run the identity on the **filed** values (the note's cells: `Interest and dividends income 597`,
`Interest expense (594)`, `Net recognized gains (losses) on investments 111`,
`Net gains (losses) on derivatives 187`, `Net gains (losses) on foreign currency remeasurements
89`, `Other, net (1,013)`, `Total $(623)`):

```
filed:  597 − 594 + 111 + 187 + 89 − 1,013  =  −623   ✓ EXACT
```

**The filed row closes exactly at −623. The served values do not close at all.** And the
discrepancy is not noise — it is exactly twice the stripped term:

```
served sum with +1,013 minus filed total (−623)  =  1,403 − (−623)  =  2,026  =  2 × 1,013  ✓
```

Replicated at 2026-03-31 (FY2026 Q3): filed `730 − 778 + 1,652 + 124 − 295 − 491 = 942` ✓ EXACT;
served with the stripped `+491` gives `1,924`, against the platform's own served parent of
`+942` → discrepancy `982 = 2 × 491` ✓.

**Error algebra (the DA-23 fingerprint): for every stripped fact, platform error = 2·|filed|;
for a sum, residual = 2·Σ|negative terms|.** Three independent replicas at MSFT — 2,026; 982;
and 384,484 on the cash-flow bridge (§2.5). A detector can be written against this and it needs
no filing at all: **a platform subtotal that exceeds the sum of its served components by twice
the sum of the parenthesised terms is a DA-23 signature.**

### 2.5 The strip propagates into the instrument's own arithmetic

The cash-change row's `computed` = **375,177,000,000**:

```
182,935 + 139,500 + 52,546 + 196  =  375,177   ← the STRIPPED children, summed
182,935 − 139,500 − 52,546 − 196  =   −9,307   ← the filed bridge, p.55
```

The instrument's `computed` is built from the corrupted children, so it agrees with the
corruption and not with the filing — a **40.3× error with the sign inverted**. This is the one
row in the whole instrument where the `fail` verdict is a **true positive**: the `reported` sign
is genuinely wrong. It is a true positive *for the wrong reason* (the fail fires because
`computed` is garbage), which the register's failure mode 1 does not currently distinguish.
**A `fail` can be right about the fact and wrong about the cause — and the remedy differs.**

---

## 3. The capex figure — validated, and its basis collapse (DA-30)

### 3.1 The figure 001 quoted is correct

p.55 [📄 MSFT 10-K p.55](https://agentii.ai/v/MSFT/sec185/55), investing activities, cells for
three months / three months / **twelve months** / twelve months:

```
Additions to property and equipment   (35,802)   (17,079)   (115,948)   (64,551)
```

**001's $115,948M is the twelve-month figure and it is filed exactly as stated.** Validated.

### 3.2 But the concept has three bases, and the platform collapses them (DA-30)

Per the contract's `basis_named` rule, which is **prior** to `no_single_basis_collapse`: the
basis must be named and its establishment located **before** the figure is used.

**(a) Cash additions to property and equipment — $115,948M.**
Established at p.55, cash-flow statement, as above. This is the **only** basis the platform
serves, under `us-gaap:PaymentsToAcquirePropertyPlantAndEquipment`, and it carries **no basis
field**. Note its sign is *legitimately* positive as served: the linkbase enters it into
`NetCashProvidedByUsedInInvestingActivities` at **weight −1**, so a positive magnitude is the
linkbase-consistent value. **This is the discriminator that separates it from §2.3's strips** —
see §5.

**(b) Total additions at cost — $133,148M.**
Established at p.71, Note 6 [📄 MSFT 10-K p.71](https://agentii.ai/v/MSFT/sec185/71), cells:

```
Total, at cost                          431,767      298,619
Accumulated depreciation               (118,691)     (93,653)
```

431,767 − 298,619 = **133,148** — **+14.8%** above the cash basis. The gap is the accrual and
non-cash component of additions.

**(c) Compute-bearing asset class only — $83,038M.**
Same page, cells: `Servers, network equipment, and software 215,874 / 132,836`.
215,874 − 132,836 = **83,038**, which is **62.4%** of total additions at cost — and exactly
**50.0%** of gross PP&E at cost. This is the basis that matters for a compute comparison, and it
is **28% below** the figure 001 used.

A fourth, named term sits on the same page: *"purchases of property and equipment remaining in
accounts payable were $26.7 billion, $6.9 billion, and $4.3 billion"* — so cash + Δpayable
≈ **135,748**, a fifth basis.

**The platform serves basis (a) and only basis (a), with no basis field, for a concept MSFT
reports on at least four bases spanning 83,038 → 135,748 — a 63% spread.** Doing the arithmetic
on the wrong basis is not a diligence failure an artifact can avoid, because the artifact cannot
see that a second basis exists. **DA-30 fires at MSFT on the precise figure PIL-3 was convened
to validate.** This is a second issuer (after BWXT) and an entirely different mechanism (asset
class / accrual coverage, not equity-inclusive income).

### 3.3 The GW table, against the RESTATED SPCX base

Phase 1 has restated SPCX's cumulative nameplate compute draw to **2.1 GW central / 2.8 GW at
target** (from the un-restated 1.4 GW). 001's comparison used the un-restated figure and must
not be reproduced.

| Capex basis | $M | @ $10M/MW | @ $40M/MW | ÷ 2.1 GW | ÷ 2.8 GW |
|---|---|---|---|---|---|
| (a) cash additions to PP&E | 115,948 | 11.6 GW | 2.90 GW | 5.52× / 1.38× | 4.14× / 1.04× |
| (b) total additions at cost | 133,148 | 13.3 GW | 3.33 GW | 6.34× / 1.59× | 4.76× / 1.19× |
| **(c) compute-bearing class only** | **83,038** | **8.30 GW** | **2.08 GW** | **3.95× / 0.99×** | **2.97× / 0.74×** |
| (a′) Q4 FY2026 quarter alone | 35,802 | 3.58 GW | 0.90 GW | 1.70× / 0.43× | 1.28× / 0.32× |

### 3.4 Autopsy of "roughly 8×"

**001's "8×" is 11,595 ÷ 1,400 = 8.28×** — i.e. the **top** of its own $10M/MW range divided by
the **un-restated** SPCX base, and the artifact never stated which end of the range it was using.

The same computation, correctly stated:

- against the restated **2.1 GW** central: **5.52×** at $10M/MW, **1.38×** at $40M/MW
- against the restated **2.8 GW** target: **4.14×** / **1.04×**
- on the **compute-only** basis (c), which is the only basis that is *about compute*:
  **3.95× / 0.99×** — and at $40M/MW against the 2.8 GW target, **0.74×**

**At the pessimistic end MSFT's annual build is 0.99–1.04× SPCX's entire cumulative base:
equal, not an order of magnitude above.** The direction survives — MSFT's annual build is
comparable to or larger than SPCX's cumulative base — and **the words "dwarfs" and "8×" do not
survive, and "roughly equal at the pessimistic end" is the honest top-line.** A factor of 3.95×
worst-to-best against a *cumulative-vs-annual* comparison, with the ratio crossing 1.0 inside
the reported cost range, is a **contested** comparison, not a decided one — which is a different
and much weaker claim than the one 001's "strongest single datum" carries.

**One further basis defect in 001, recorded but not adjudicated here:** 001's *"Two companies,
~$196B/year"* sums a **DEMONSTRATED** FY figure (MSFT, filed) with a **MODELED** annualisation of
Alphabet's H1 (≈$80B, different ticker, outside this artifact's scope). The sum is presented as
one measured quantity. I did not verify the Alphabet leg.

---

## 4. DA-26 and DA-27 — the fiscal label, and the mechanism

### 4.1 DA-27 — confirmed, with a wrong outcome and a third source value

`get_company_fiscal_calendar(MSFT)` returns `fiscal_year_end_month: 7`,
`fiscal_year_end_month_source: "gold_companies"`, `cross_validation_hint: null`.

**MSFT's FY2026 ended 2026-06-30 — June is month 6.** A fiscal-year-end month of **7 (July)**
for a June-30 filer is a calendar-derived label that is **off by one month**, and its `source` is
`gold_companies`, **not** `default` — refuting a detector keyed on `source == "default"` at a
**third** issuer (FLY was the first; the register's n=5 becomes n=6 with a distinct mechanism:
a *one-month* error rather than a *quarter* error).

**The earnings calendar is the correct surface, and it is correct where it is modern.** The
FY2026 Q4 row (report_date 2026-07-29) is labelled `2026 (Q4)` with `fiscal_source: "ect_exact"`
— **right**. The legacy rows (`fiscal_source: "calendar_estimate"`, back to 1985) are **wrong on
both fields** (a 1985-09-30 report date labelled "1985 (Q3)" when the quarter ending 1985-09-30
is FY1986 Q1). So the same platform holds a correct fiscal calendar on one surface and a
calendar-derived one on another, and **the artifact-visible surface is the wrong one.**

### 4.2 DA-26 — confirmed, and now a single computable screen

The `mislabelled period` varies by issuer (BA = Q4, MRCY = Q2) and the register recorded this as
not screenable by row position. **The mechanism is now identified and it makes it screenable:**

> **`search_xbrl_facts.fiscal_period` = `calendar_quarter(period_end)`, and `fiscal_year` =
> `calendar_year(period_end)`.**

Proven by three independent measurements on MSFT facts:
1. Isolated `fiscal_period` filters return facts whose `period_end` falls in that calendar
   quarter — `Q1` → 14/14 Jan–Mar, `Q2` → 7/7 Apr–Jun, `Q3` → 15/15 Jul–Sep, `Q4` → 13/13
   Oct–Dec (**49 of 49**).
2. Isolated `fiscal_year` filters return facts whose `period_end` falls in that calendar year:
   `fiscal_year=2025` → 16 facts, **all ending in calendar 2025** (2025-12-31, 2025-09-30,
   2025-06-30, 2025-03-31); `fiscal_year=2024` → 14 facts, **all ending in calendar 2024**
   (2024-12-31, 2024-09-30, 2024-06-30, 2024-03-31). The two sets are **disjoint**, and each is
   internally consistent under the calendar rule.
3. The 12-month facts correctly land in the `FY` bucket of the facts layer.

**The defect is therefore in the METRICS layer, not the facts layer**, and it is visible as a
disagreement between two platform surfaces about the *same* fact:

| Surface | FY2026 annual revenue 331,839 labelled |
|---|---|
| `search_xbrl_facts` (`fiscal_period=FY`) | **FY** ✓ |
| `get_company_financials` / `get_company_calculation_tree` header | **"Q2"** ✗ |

**For a June-30 filer, every fiscal quarter maps to a calendar quarter two ahead** (fiscal Q1
Jul–Sep → "Q3"; fiscal Q2 Oct–Dec → "Q4"; fiscal Q3 Jan–Mar → "Q1"; fiscal Q4 Apr–Jun → "Q2"),
**and because the annual figures also end June 30, the twelve-month value inherits the quarterly
label "Q2".**

**Screen for DA-26 (single computation, no row position):** `mislabelled fiscal_period =
calendar_quarter(fiscal_year_end)`. Measured at MSFT (June end → Q2 ✓, confirmed in the 10-K's
own served header). Against the register's recorded values it also fits BA (Dec-31 → Q4 ✓) and
MRCY (June-30 → Q2 ✓). **Graded DERIVED for BA/MRCY/TDG/HWM — I did not re-measure them, and
HWM's registered Q1 value remains unexplained by the rule.**

### 4.3 A discovered consequence: the compound filter is internally inconsistent

`search_xbrl_facts(concept=NonoperatingIncomeExpense, fiscal_year=2025, fiscal_period=Q2)`
returns **zero rows** — while `fiscal_year=2025` alone returns 16 facts *including* one ending
2025-06-30, which by rule 2 above **is** calendar Q2. **The two filters do not compose on a
common key**, so a compound query silently returns nothing rather than erroring. This cost this
census one round of investigation and it is recorded as a failure mode: **silence from a compound
filter is not evidence of absence.** (It was caught here only because the same concept returned
rows under each filter *separately*.)

### 4.4 A coverage consequence at MSFT

`fiscal_period=Q2` returns **zero** `NonoperatingIncomeExpense` facts, and no 3-month fact
ending 2026-06-30 appears anywhere — **MSFT's fiscal Q4 quarter is absent from the fact table,
and the 12-month figure occupies the slot.** The `is_primary` election prefers the 10-K's
authority-3 annual value over the 8-K's authority-1 quarterly value, so **the fiscal Q4 quarter
is silently dropped**. Any artifact computing a Q4 series from this layer gets the annual value
where the quarter belongs — which is DA-26's *effect*, with DA-26's *cause* now named.

---

## 5. The discriminator: which positive values are strips and which are correct

A naive detector — "strip all cash-flow concepts" — would produce false positives at MSFT,
because **`PaymentsToAcquirePropertyPlantAndEquipment` is served +115,948 and that is correct**,
while `NetCashProvidedByUsedInInvestingActivities` is served +139,500 and **that is a strip.**
Both are cash outflows. Both enter the same subtree. One is right and one is wrong.

The linkbase resolves it, and the rule generalises:

> **A concept entering its calculation parent at weight −1 carries its own POSITIVE magnitude
> legitimately — serving it positive is not a strip. A concept entering at weight +1 whose filed
> cell is parenthesised IS stripped.**

Verified on the FY2026 10-K linkbase:
- `PaymentsToAcquirePropertyPlantAndEquipment` → `NetCashProvidedByUsedInInvestingActivities`,
  **w = −1** → served +115,948 is **correct**.
- `InterestExpenseNonoperating` → `NonoperatingIncomeExpense`, **w = −1** → positive expense
  amount, correct.
- `OtherNonoperatingIncomeExpense` → `NonoperatingIncomeExpense`, **w = +1** → its own value
  must be negative when filed `(491)`; **served +491 is a strip** ✓.
- `NetCashProvidedByUsedInInvestingActivities` → `CashCashEquivalents…IncreaseDecrease`, **w = +1**
  → filed `(139,500)`; **served +139,500 is a strip** ✓.

**This is a derivable, mechanical DA-23 test that needs no external reference and no
profitability assumption** — which is precisely what the register's DA-23 entry lacks. Verified
on 38 facts with zero miscalls.

---

## 6. DA-24 — discharged, clean negative, from the linkbase

The complete arc set into `us-gaap:OperatingIncomeLoss` in the FY2026 10-K calculation linkbase
(`Role_StatementINCOMESTATEMENTS`) is **exactly four** arcs:

| Parent | Child | Weight |
|---|---|---|
| `us-gaap:OperatingIncomeLoss` | `us-gaap:GrossProfit` | +1 |
| `us-gaap:OperatingIncomeLoss` | `us-gaap:ResearchAndDevelopmentExpense` | −1 |
| `us-gaap:OperatingIncomeLoss` | `us-gaap:SellingAndMarketingExpense` | −1 |
| `us-gaap:OperatingIncomeLoss` | `us-gaap:GeneralAndAdministrativeExpense` | −1 |

**No disposal gain. No `GainOnDispositions` of any kind.** Contrast BA, where `Gain on
dispositions` is an arc child of `OperatingIncomeLoss` at **w = +1**. **DA-24 does not fire at
MSFT — DEMONSTRATED from the linkbase, not inferred from the absence of a line on the face.**

**Also structurally proven here:** `NonoperatingIncomeExpense` is an arc child of
`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` at **w = +1** — a **sibling** of
`OperatingIncomeLoss`, not a component of it. **MSFT's operating income ($155,237M) cannot
contain the OpenAI gain; its pre-tax and net income can.** This is the linkbase proof of the
separation asserted in §8.

---

## 7. DA-25 and DA-29 — does not fire, with all terms located

The contract's `reconciliation_terms_located` (DA-29) requires every term of a reconciliation to
be NAMED and located, because a back-solve closes exactly and cannot be caught on its closure.
Run against the issuer's non-GAAP reconciliation on p.44
[📄 MSFT 10-K p.44](https://agentii.ai/v/MSFT/sec185/44), cells:

```
Other income (expense), net                        10,697    (4,901)   (1,646)
Net (gains) losses from investments in OpenAI      (6,530)    4,763     1,482
Adjusted other income (expense), net (non-GAAP)     4,167      (138)     (164)
Net income                                        133,749   101,832    88,136
Net (gains) losses from OpenAI, net of tax
  of $1,567, $(1,143), and $(356)                  (4,963)    3,620     1,126
Adjusted net income (non-GAAP)                    128,786   105,452    89,262
Diluted EPS                                         17.95     13.64     11.80
Net (gains) losses from OpenAI                      (0.67)     0.49      0.15
Adjusted diluted EPS (non-GAAP)                     17.28     14.13     11.95
```

**Every term is named and located on the page** — including the tax effect ($1,567M), which is
the term most likely to be a hidden plug. The bridges close:

```
FY2026  133,749 − 4,963 = 128,786   ✓     17.95 − 0.67 = 17.28   ✓
        128,786 ÷ 7,453 = 17.2799… → 17.28  ✓
        pre-tax bridge: (6,530) + 1,567 = (4,963)  ✓  (implied rate 24.0%; 6,530 × 0.24 = 1,567.2 ✓)
```

**DA-29 passes: no term is a back-solve, and the closure is not the evidence — the terms are.**
(Contrast 001's BWXT artifact, which closed on a `$90.7M` term found in no filing.)

**DA-25 therefore does not fire on the per-unit metric**: `Adjusted diluted EPS` is fully
reproducible from filed terms, by two independent routes.

**Three residuals recorded honestly rather than smoothed:**
1. The Q4 8-K states an OpenAI net-income impact of **$480M / $0.07**; 480 ÷ 7,443 diluted =
   **$0.0645**, which rounds to $0.06, not $0.07. The per-share term implies ≥$521M — an **$41M
   (8.5%) gap** in an issuer-defined per-unit metric. Not adjudicated; it may be a denominator
   choice I cannot see. **UNRESOLVED.**
2. **`IncomeTaxExpenseBenefit` `computed` = 70,454** — no located source. `NetIncomeLoss`
   `computed` = 133,749 = 165,934 − **32,185**, i.e. **the parent's arithmetic uses the child's
   REPORTED value while the child's own `computed` disagrees with it.** The instrument is not
   self-consistent across adjacent rows. **UNRESOLVED-FROM-PLATFORM.**
3. **`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` `computed` = 191,017** vs reported
   165,934, where **reported is right** (155,237 + 10,697 = 165,934 ✓, p.52). The residual
   191,017 − 155,237 = **35,780** appears **nowhere in the filing.** Per DA-29 a term with no
   located source is not a derivation: **I refuse to explain this number and record it as a
   back-solve-shaped residual. UNRESOLVED-FROM-PLATFORM.**

**DA-25 candidate (CLAIMED, definitionally caveated).** p.36
[📄 MSFT 10-K p.36](https://agentii.ai/v/MSFT/sec185/36) states *"Microsoft Cloud revenue
increased 27% to $214.4 billion"* and *"commercial RPO $678 billion"*. **Neither is reproducible
from the three reportable segments** in the p.86 table (segment revenues 139,996 / 137,791 /
54,052; no line equals or sums to 214.4B). Microsoft Cloud is an issuer-defined cross-segment
aggregation, and the segment table on p.86 carries its own cost-revenue allocation narrative
explaining why. **But DA-25 as registered is a PER-UNIT metric test, and this is a dollar
aggregation** — so I record it as a candidate with the reproducibility test shown, not as a
firing. If DA-25 is intended to reach across-segment revenue aggregations, this is its MSFT
instance and the register entry should say so.

---

## 8. The cross-holding asymmetry — discharged, with a positive control

**The brief's test: does MSFT hold a position comparable to Alphabet's $99.0B unrealized gain
"from SpaceX" — a mark on the anchor's own equity?**

**NO. And the null is real, not a matcher failure.** `search_keyword_in_source(MSFT, sec185,
"SpaceX")` → **0 hits**; the identical call shape on the same filing for **"OpenAI" → 8 pages**
(62, 44, 43, 36, 64, 40, 39, 19). **The positive control is what makes the null admissible.**

**But the CLASS replicates at MSFT, at a different counterparty, and it is not small.**
p.43 [📄 MSFT 10-K p.43](https://agentii.ai/v/MSFT/sec185/43): *"Other income (expense), net
included $6.5 billion of net gains and $4.8 billion of net losses for fiscal years 2026 and 2025,
respectively, from investments in OpenAI… The net gains recorded for fiscal year 2026 primarily
relate to the dilution gain from the OpenAI Recapitalization."*
p.62 [📄 MSFT 10-K p.62](https://agentii.ai/v/MSFT/sec185/62): an **equity-method** investee,
*"an approximate 25% interest on an as-converted basis"*, a **related party as defined in ASC
850**, income measured by the **HLBV** method *"because our liquidation rights and priorities
differ from our underlying ownership interest"*, with **$13.0B commitments of which $11.9B is
funded**, **$24.1B** of revenue from commercial arrangements with OpenAI, and **$6.0B** of
receivables.

| | Alphabet | MSFT |
|---|---|---|
| Counterparty | **the anchor (SpaceX)** | OpenAI — not the anchor |
| Amount in net income | $99.0B | **+$4,963M after tax = 3.71% of $133,749M** |
| Basis | mark on the anchor's equity | **equity method under HLBV + a dilution gain** |
| Fiscal swing | — | **+$4,963M vs −$3,620M the prior year: an $8,583M swing** |
| Issuer's own non-GAAP strips it | — | **yes** (`Adjusted net income` removes it, p.44) |

**The mechanism is worth naming precisely, because it is *not* a market mark: the FY2026 gain
arises because MSFT's proportionate ownership of OpenAI DECREASED.** A dilution gain is
recognised as your stake falls. **MSFT's reported net income grew, in part, because its stake in
its most important counterparty shrank** — and the HLBV convention computes the gain on a
hypothetical liquidation of book value under rights that differ from ownership. p.55 confirms
the gain is not cash. **A cross-holding mark can be constructed out of a *declining* stake, which
is a distinct failure mode from Alphabet's:** the register's cross-holding entry should not
assume the mark is an appreciation.

**And note the pre-tax figure (6,530) EXCEEDS the entire "Other, net" line containing it
(4,722)** — so the rest of that line was a net loss of ~$1,808M. A reader who treats
`Other income (expense), net` as "other income" reads a gain that is one counterparty's
dilution effect netted against a larger loss elsewhere.

**Structural separation is proven from the linkbase, not asserted:** `NonoperatingIncomeExpense`
is an arc child of pre-tax income and a **sibling** of `OperatingIncomeLoss` (§6). **MSFT's
operating income ($155,237M) is uncontaminated; its pre-tax and net income are not.** Any
PIL-3 comparison that uses MSFT's *operating* margin is clean; any that uses *net* income or EPS
carries a 3.71% related-party, non-operating, non-cash, stake-reduction artefact.

---

## 9. The instrument — failure modes measured at MSFT

| # | Register's mode | MSFT |
|---|---|---|
| 1 | 93% false-positive on `fail` | **24 fails; ≥11 have a `reported` matching the filing exactly, so the fail is purely a corrupt `computed`; 2 more have a corrupt `reported`.** ≥13 of 24 (54%) are false positives against the fact — and **one is a true positive for the wrong reason** (§2.5) |
| 2 | `pass` does not certify a sign | Confirmed. `NetIncomeLoss`, `AssetsCurrent`, `Liabilities`, `PropertyPlantAndEquipmentNet`, WASO all `pass` and all match the filing. **And 27 stripped facts would still pass any test built on positive subtotals** |
| 3 | `reported` can be a SEGMENT TOTAL | **Confirmed, with the mechanism now located.** `OperatingIncomeLoss` `reported` = **14,386,000,000** = the **More Personal Computing** segment operating income — the third segment's row on p.86 — against the consolidated **155,237** on the same table's Total row and on p.52's face. **A 10.8× understatement.** The p.86 table carries four `Operating income` rows in one column, and the extraction took one of them |
| 4 | NO ROW for a heavily-arc'd concept | **Confirmed as a live risk:** `CashCashEquivalents…IncreaseDecrease` has **4** arcs into it and *does* appear (as the corrupt 375,177 row); `StockholdersEquity` has **3** and appears corrupted both ways (below). Silence elsewhere is not evidence |
| 5 | `reported` sign-stripped | **Confirmed, 27 instances** (§2) |
| 6 | `computed` short by one cost line, flipping between filings | **Confirmed in a new shape:** `GrossProfit` `computed` 190,919 vs reported **225,465** (correct per p.52) — a **34,546** shortfall localised by the tree to the revenue/COGS pair; and `GrossProfit` FY2024 `computed` = **−2,966,000,000** vs reported 171,008,000,000 |
| 7 | Period collapse (`validate_calculation`) | Not re-tested here; recorded as carried |

**The new shape this census adds: `computed` and `reported` each corrupt on ADJACENT rows, in
OPPOSITE columns.**

| Concept | `computed` | `reported` | Which column matches the filing |
|---|---|---|---|
| `GrossProfit` | 190,919 ✗ | 225,465 ✓ | reported |
| `OperatingIncomeLoss` | 155,237 ✓ | 14,386 ✗ | computed |
| `IncomeTaxExpenseBenefit` | 70,454 ✗ | 32,185 ✓ | reported |
| `NetIncomeLoss` | 133,749 ✓ | 133,749 ✓ | both |

**There is no rule of thumb.** "Trust `computed`" is wrong on row 1; "trust `reported`" is wrong on
row 2; and row 4 shows the parent's arithmetic using a child's `reported` while that child's own
`computed` disagrees. **The only admissible method remains the one the register prescribes: read
the `computed`/`reported` PAIR through the component identity, and where the instrument is silent,
derive from the filing. `EPS × shares` was not used anywhere in this artifact.**

**One more, on a heavily-arc'd concept:** `StockholdersEquity` `computed` = 449,018,000,000 and
`reported` = 3,347,000,000, against a filed total equity of **442,387** (p.54
[📄 MSFT 10-K p.54](https://agentii.ai/v/MSFT/sec185/54), "total stockholders' equity of
$442,387M"). **Neither column matches**, and 3,347 is the FY2025 AOCI element — a **wrong-element
substitution inside the equity rollforward**, exactly the shape the heavily-arc'd-concepts rule
predicts.

**Contrast that did NOT replicate:** SPCX's "`Assets` is a cash-flow subtotal" defect does **not**
recur — `Assets` `reported` 758,376 matches p.54. A cross-issuer detector cannot be generalised
from one issuer's instance in either direction.

---

## 10. Component identity — in-line, every period, every fact

Consolidated, from **p.86's segment table Total row**
[📄 MSFT 10-K p.86](https://agentii.ai/v/MSFT/sec185/86) (`Cost of revenue` and `Operating expenses`
are on the Total row — cells `106,374 / 87,831 / 74,114` and `70,228 / 65,365 / 61,575` — so the
identity is runnable from a single table without a subtraction outside the filing):

```
FY2026   331,839 − 106,374 − 70,228 = 155,237   ✓   (p.52 face: Operating income 155,237)
FY2025   281,724 −  87,831 − 65,365 = 128,528   ✓   (p.52 face: 128,528)
FY2024   245,122 −  74,114 − 61,575 = 109,433   ✓   (p.52 face: 109,433)
```

and in the `gross profit − opex` form the contract requires, from p.52's face:

```
FY2026   225,465 − (35,562 + 26,710 + 7,956 = 70,228) = 155,237   ✓
FY2025   193,893 − (32,488 + 25,654 + 7,223 = 65,365) = 128,528   ✓
FY2024   171,008 − (29,510 + 24,456 + 7,609 = 61,575) = 109,433   ✓
```

Non-operating line, same face: `155,237 + 10,697 = 165,934` ✓ (filed `Income before income
taxes 165,934`); `165,934 − 32,185 = 133,749` ✓ (filed `Net income $133,749`).

**Segment level, FY2026 (p.86) — the identity closes at every level AND sums to the consolidated:**

```
Productivity and Business Processes   139,996 − 25,017 − 31,100 =  83,879   ✓
Intelligent Cloud                     137,791 − 57,876 − 22,943 =  56,972   ✓
More Personal Computing                54,052 − 23,481 − 16,185 =  14,386   ✓
                                                       sum  =  155,237   ✓ = consolidated
```

**Four levels, three fiscal years, zero residual.** Note what the segment closure buys: the
`14,386` in the third row is the value the instrument serves as *consolidated* operating income
(§9 mode 3) — **the identity locates the mis-selection to a named segment row.**

**Q4 FY2026 (three months), from the 8-K p.10 and p.14**
[📄 MSFT 8-K p.10](https://agentii.ai/v/MSFT/sec184/10) /
[📄 MSFT 8-K p.14](https://agentii.ai/v/MSFT/sec184/14):
`60,482 − (9,997 + 7,595 + 2,287 = 19,879) = 40,603` ✓, and p.14's own `Total operating
expenses 19,879` matches the derived 19,879 exactly.

**Cash bridge**, from p.55's filed cells: `182,935 − 139,500 − 52,546 − 196 = −9,307` ✓, and the
balance sheet corroborates (cash 30,242 → 20,935, p.54). **The platform's `computed` on this row
is 375,177 (§2.5) — the identity closes on the filing and not on the platform, which is what
makes the strip undeniable.**

**Quarterly replica of the same bridge, from the Q4 8-K's investing section**
[📄 MSFT 8-K p.13](https://agentii.ai/v/MSFT/sec184/13) — six filed cells, all quoted:

```
(35,802) (452) (18,829) 4,181 6,487 (10,416)
−35,802 − 452 − 18,829 + 4,181 + 6,487 − 10,416 = −54,831   ✓  = filed "Net cash used in investing (54,831)"

if every sign were stripped:   35,802 + 452 + 18,829 + 4,181 + 6,487 + 10,416 = 76,167
fingerprint:  76,167 − (−54,831) = 130,998 = 2 × (35,802 + 452 + 18,829 + 10,416)  ✓ EXACT
```

**A fourth independent replica of the `2·Σ|negatives|` fingerprint.** The quarterly bridge closes
on the filing exactly as the annual one does, so the defect is not a period artefact — and the
fingerprint is reproducible from filed cells alone, on a quarter, on a year, and on a single
income-statement row (§2.4).

---

## 11. What could NOT be verified

1. **The FY2025 and FY2024 quarterly `NonoperatingIncomeExpense` facts are located only in the
   platform's rendering of the filing's Note text block** (`ScheduleOfOtherNonoperatingIncome
   ExpenseTableTextBlock`, `source_file: msft-20260331.htm`, `msft-20251231.htm`,
   `msft-20250930.htm`, `msft-20250331.htm`, `msft-20240930.htm`). **I did not read those pages.**
   Their filed signs are therefore corroborated by a filing-derived surface that I did not
   page-verify. **The three ANNUAL instances that carry the verdict rest on p.52's face, which I
   did read and quote — so the verdict does not depend on the unverified leg.** Graded
   accordingly: annual = DEMONSTRATED; quarterly = DERIVED.
2. **`IncomeLossFromContinuingOperationsBeforeIncomeTaxes…` `computed` = 191,017** — unexplained;
   residual 35,780 located nowhere in the filing. Refused as a derivation (DA-29).
3. **`IncomeTaxExpenseBenefit` `computed` = 70,454** — source unidentified.
4. **`GrossProfit` `computed` 190,919 vs 225,465** — residual 34,546 localised by the tree to
   exactly two candidate concepts (revenue or COGS), not decomposed further.
5. **`GrossProfit` FY2024 `computed` = −2,966,000,000** vs reported 171,008,000,000 — unexplained.
6. **Additional instrument residuals not decomposed:** `CashCashEquivalentsAndShortTermInvestments`
   13,059 vs 76,843 (76,843 correct per p.54); `DerivativeLiabilities` −935 vs 495;
   `DebtInstrumentCarryingAmount` 46,136 vs 7,930; `DerivativeAssets` 868 vs 282;
   `FiniteLivedIntangibleAssetsNet` 26,210 vs 7,601.
7. **The compound `fiscal_year` + `fiscal_period` filter returns zero rows** where either filter
   alone returns the fact (§4.3) — the platform's own keys do not compose. Reported as a defect,
   but the *intended* key semantics are not documented anywhere I could reach, so the fix is not
   mine to specify.
8. **001's Alphabet leg (~$39,643M H1, ≈$80B annualised)** — different ticker, out of scope, not
   verified by me.
9. **The GW conversion is MODELED, not DEMONSTRATED.** No MSFT filing states a MW figure for its
   capex. The conversion is a modelled bridge from a DEMONSTRATED dollar figure to a capacity
   figure using a reported cost-per-MW range, and the range spans 4× — which is why the ratio in
   §3.3 crosses 1.0 inside it. **A range whose endpoints straddle the conclusion cannot support
   the conclusion.**
10. **`validate_calculation` period collapse (mode 7) was not re-tested** in this artifact.

---

## 12. Carry-forwards

1. **DA-23's register entry needs the weight-sign discriminator (§5) and the `2·Σ|negatives|`
   error algebra (§2.4).** Together they turn DA-23 from a measured phenomenon into a mechanical
   test requiring no external reference — and the discriminator is what prevents the naive
   "strip all cash-flow concepts" detector, which would produce a false positive on
   `PaymentsToAcquirePropertyPlantAndEquipment` at MSFT.
2. **DA-23 is not conditioned on profitability and 001's §3 is to be corrected, not extended.**
   The claim "MSFT is profitable and therefore unaffected by DA-23" is falsified at 9 of 15 facts
   on one concept. **The remedy is not a wider sample of the same kind — it is a sample that
   includes the negative side, because a test restricted to positive facts cannot fail.**
3. **DA-30's second instance is a CAPEX BASIS collapse, not an income-basis collapse**, and it is
   on the figure 001 calls its strongest datum. Any artifact quoting MSFT capex must name the
   basis: 83,038 (compute-bearing class) / 115,948 (cash additions) / 133,148 (total additions at
   cost) / ~135,748 (cash + Δpayable).
4. **The restated comparison must propagate into 001's text.** "8×" and "dwarfs" are not
   supportable against 2.1 GW / 2.8 GW; the supportable statement is **3.95×–5.52× on the central
   case, and 0.74×–1.04× at the pessimistic end — i.e. the comparison crosses parity within the
   reported cost range.**
5. **DA-26 is now a single computable screen** (`calendar_quarter(fiscal_year_end)`), verified at
   MSFT and consistent with BA and MRCY. Re-measure TDG and HWM, whose registered values this
   rule does not fully explain.
6. **The metrics layer and the facts layer disagree about `fiscal_period` for the same fact**
   (§4.2). Any artifact that reads `fiscal_period` from `get_company_financials` inherits a
   calendar-derived label; the facts layer's `FY` bucket is the correct one.
7. **Cross-holding: the register entry should not assume the mark is a gain from APPRECIATION.**
   MSFT's is a dilution gain recognised as its stake *falls*, measured under HLBV on a
   hypothetical liquidation — a different construction with the same contamination signature.
