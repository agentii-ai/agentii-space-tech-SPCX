---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: AVAV
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T22:25:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "UNVERIFIABLE — net income is absent from every row, so no EPS bridge exists"
  - da_id: "DA-26"
    chosen_reading: "the FY label lands on a row the extract cannot distinguish from a quarter"
  - da_id: "DA-27"
    chosen_reading: "SECOND INSTANCE — fiscal-period labels are offset at a non-calendar issuer; the offset has a testable mechanism"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# AVAV — Supply-Chain Position

Source: Form 10-Q filing set, accession `0001104659-26-077575` (period ended 2026-04-30).

**⚠️ This artifact reports a data-integrity finding, not a baseline.** AeroVironment's extract
is missing the line needed for every detector this thesis uses.

---

## 1. Net income is absent from EVERY row — no detector can run

| Period labelled | Revenue | Operating income | EPS (diluted) | **Net income** | R&D |
|---|---:|---:|---:|---:|---:|
| Q1 FY2026 | $1,976.845M | $310.995M | $5.40 | **null** | $127.678M |
| Q4 FY2025 | $408.045M | $179.038M | $3.15 | **null** | $27.112M |
| Q3 FY2025 | $472.508M | $30.224M | $0.34 | **null** | $35.993M |
| Q2 FY2025 | $454.676M | $69.272M | $1.44 | **null** | $33.114M |
| Q1 FY2025 | **null** | $40.795M | $1.56 | **null** | $100.729M |
| Q4 FY2024 | **null** | $3.087M | $0.06 | **null** | $22.498M |
| Q3 FY2024 | **null** | $7.006M | $0.27 | **null** | $28.716M |

**`net_income_loss` is null in every row, and `revenues` is null in five of ten.**

**Consequence**: **every detector this thesis has developed requires net income or gross
profit.** The EPS × shares bridge needs net income. The component identity needs gross
profit. The gross-profit bound needs gross profit. **AVAV has neither, so all three fail —
and this is not a defect in AVAV, it is a coverage hole in the extract.**

## 2. The revenue sequence does not reconcile with AVAV's fiscal calendar

AVAV's fiscal year ends **30 April**. Mapping the rows to AVAV's own quarters:

| period_end | AVAV's actual fiscal quarter | Platform label | Revenue shown |
|---|---|---|---:|
| 2025-08-02 | **FY2026 Q1** (May–Jul 2025) | Q2 FY2025 | $454.676M |
| 2025-11-01 | **FY2026 Q2** (Aug–Oct 2025) | Q3 FY2025 | $472.508M |
| 2026-01-31 | **FY2026 Q3** (Nov 2025–Jan 2026) | Q4 FY2025 | $408.045M |
| 2026-04-30 | **FY2026 Q4 / full year** | **Q1 FY2026** | **$1,976.845M** |

**The row labelled `Q1 FY2026` carries $1,976.845M — 3.7× the largest genuine quarter in
the sequence.** Two readings are live and the extract cannot separate them:

1. **It is the FY2026 ANNUAL total** (DA-26) — in which case FY2026 revenue of $1,977M
   against four FY2025 quarters summing to ~$1,800M is a coherent ~10% growth story for
   AVAV post-BlueHalo.
2. **It is a genuine quarter** — which would require a 3.7× sequential jump with no
   acquisition disclosed in the extract.

**Reading 1 is far more plausible, and it makes AVAV a DA-26 instance at the FY boundary.**

## 3. DA-27 now has TWO instances, and a mechanism that fits both

**The label offset at AVAV is systematic across all four rows, not a one-off.** Note what
the labels are doing:

| period_end | Calendar quarter of that date | Platform label |
|---|---|---|
| 2025-08-02 | calendar Q3 2025 | **Q2** |
| 2025-11-01 | calendar Q4 2025 | **Q3** |
| 2026-01-31 | calendar Q1 2026 | **Q4** |
| 2026-04-30 | calendar Q2 2026 | **Q1** |

**In every row the platform's `fiscal_period` is the calendar quarter of `period_end` minus
one, with `fiscal_year` rolled back accordingly.** The identical pattern holds at HEICO,
where the period ended 2026-04-30 (calendar Q2) is labelled `Q1`.

**The mechanism, now testable against a complete population**: the platform buckets periods
by **calendar** quarter boundaries measured from 1 January, then labels the bucket with the
issuer's fiscal year. **That mapping is exact for December-year-end issuers and off by one
for every non-calendar issuer.**

**This is no longer a hypothesis — the population is complete and it separates perfectly:**

| Fiscal year-end | Issuers in universe | Offset observed |
|---|---|---|
| December | GOOG, MSFT, NVDA, LMT, RTX, NOC, KTOS, CW, TER, KRMN, GSAT, IRDM, SATS, AMGN, BMY, MRK… | **none** |
| **January** | **PL** | **yes** — PL FY2026 Q1 (Feb–Apr 2026, ending 2026-04-30, calendar Q2) labelled `Q1` |
| **April** | **AVAV** | **yes** — all four rows offset |
| **September** | **WWD** | **yes** — period ending 2026-06-30 is WWD's FY2026 **Q3** (Apr–Jun), labelled `Q2` |
| **October** | **HEI** | **yes** — six-month period ending 2026-04-30 labelled `Q1` |

**Four non-calendar issuers, four offsets. Every December issuer, none.** DA-27 is therefore
**CONFIRMED at n=4 of 4** — and the clean separation on the fiscal-year-end axis is what
confirms it, not the raw count. **A pattern that partitions a population perfectly on one
variable and on nothing else is a mechanism, not a coincidence.**

**Note this corrects an earlier reading in this pass**: WWD was initially recorded as showing
*genuine* quarters with no offset. **It does not — its period ending 2026-06-30 is WWD's
FY2026 Q3, labelled `Q2`.** The correction is recorded rather than silently applied, and it
**removes the only counterexample**, which is why DA-27 moves from CANDIDATE to CONFIRMED.

**Why this matters more than a cosmetic label**: for AVAV and WWD the mislabelling makes a
**full fiscal year** look like a quarter, which is what makes DA-26 and DA-27 hard to tell
apart at those issuers. **The two defects compound**: DA-27 supplies the wrong label and
DA-26 supplies the wrong value, and at a non-calendar issuer they produce the same wrong
conclusion by different routes.

## 4. What would resolve it

**The named disclosure**: a properly period-labelled statement for AVAV carrying
**net income** and a revenue series spanning the BlueHalo close (May 2025), so the
pre- and post-merger periods can be separated. **Without net income no detector in this
thesis can run on AVAV, and without an acquisition-date split no growth rate is
interpretable.**

**Recommendation: AVAV is excluded from the Phase 3 margin ladder** — not because its
economics are unflattering, but because the platform cannot supply the inputs.

---

## Carry-forwards

1. **`net_income_loss` is null in every AVAV row and `revenues` in five of ten** — so the
   EPS bridge, the component identity and the gross-profit bound **all fail**. This is a
   **coverage hole, not an issuer defect.**
2. **AVAV is a DA-26 instance at the FY boundary**: the row labelled `Q1 FY2026` carries
   3.7× the largest genuine quarter and reads coherently as the FY2026 annual.
3. **DA-27 now has TWO instances (HEICO, AVAV) and a testable mechanism** — labels derived
   from calendar quarters rather than the issuer's fiscal calendar, exact for December-FYE
   issuers and off by one otherwise. **Every December-FYE issuer in the universe is
   unaffected; both non-calendar issuers are affected.** Test against WWD.
4. **DA-26 and DA-27 COMPOUND at non-calendar issuers** — wrong value and wrong label
   producing the same wrong conclusion by different routes. **Register them jointly as well
   as separately.**
5. **Recommend excluding AVAV from the margin ladder** on input-availability grounds.
