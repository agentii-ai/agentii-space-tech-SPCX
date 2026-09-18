---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: WWD
skill: supply-chain
mode: methodology
generated_at: 2026-09-18T21:20:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "8cb3ac1de486"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "consolidated OperatingIncomeLoss NOT available (segment-only); gross-profit bound used and holds; EPS identity 0.16%"
  - da_id: "DA-26"
    chosen_reading: "year-end row carries ANNUAL revenue (WWD's FY ends 30 Sep) — confirmed for FY2024, ANOMALOUS for FY2025"
  - da_id: "DA-27"
    chosen_reading: "fiscal_period labels vs issuer calendar — flagged for cross-check, not asserted"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# WWD — Supply-Chain Position (Actuation, Control & Combustion)

Source: Form 10-Q, accession `0001193125-26-325790` (quarter ended 2026-06-30).

---

## 1. Woodard's second disclosure gap: consolidated operating income is absent

| Metric | Q2 FY2026 | Q2 FY2025 | Change |
|---|---|---|---|
| Revenue | **$1,109.705M** | $915.446M | +21.2% |
| COGS | $759.799M | — | 68.5% of revenue |
| Implied gross profit | **$349.906M** | — | **31.5% margin** |
| Net income | $146.675M | $108.448M | +35.2% |
| EPS (diluted) | $2.40 | $1.76 | +36.4% |
| R&D / revenue | 4.4% | 4.5% | — |

**`OperatingIncomeLoss` is absent at the consolidated level.** The only
`OperatingIncomeLoss` fact in the extract is **dimensional** — `$170.020M`, tagged to the
**Aerospace segment**. The metrics array returns `operating_income: null`.

**This is the third issuer with a missing consolidated operating line** (MRK, BMY, WWD).
**The component-identity detector — the only reliable DA-23 test — cannot run at the
consolidated level on any of them.**

**The gross-profit bound still runs and holds:**

```
revenue $1,109.705M - COGS $759.799M = gross profit $349.906M
Aerospace segment operating income $170.020M < $349.906M  ✓  (bound holds)
EPS (diluted) $2.40 x 61.018M = $146.443M  vs  net income $146.675M   (0.16% gap)
```

**WWD is CLEAN.** Clean-positive count: **19 of 19.**

**Register the coverage caveat once, at three issuers**: `OperatingIncomeLoss` absent or
segment-only at **MRK, BMY and WWD** — a material hole in the platform's ability to run the
one detector that works.

## 2. Woodward is mid-tier — and the tier structure is now a trend

| Tier | Issuer | Operating margin |
|---|---|---:|
| Component supplier (installed base) | HEI | 25.5% |
| Component supplier | KRMN | 19.1% |
| **Subsystem supplier** | **WWD (Aerospace segment)** | **~17%** |
| Primes | LMT / RTX / LHX / NOC | 10.1–12.4% |

**Woodward's implied gross margin of 31.5% sits between the primes (LMT 12.2% gross) and
the installed-base suppliers (HEI, KRMN at 43%)**, consistent with a subsystem supplier that
carries more integration cost than a parts maker but less programme risk than a prime.

**Consequence for PIL-3**: the margin ladder is not a two-tier split but a **graded
function of distance from the programme-level risk.** Register as a three-tier structure
with the *mechanism* (programme-risk absorption) rather than a binary prime/supplier claim.

## 3. DA-26 — confirmed for FY2024, and the FY2025 instance is anomalous

WWD's fiscal year ends **30 September**, so its Q3 *is* its year-end quarter (the subtlest
form, as at PL and HEI).

| Row | Revenue shown | Implied year-end quarter | Assessment |
|---|---:|---:|---|
| **Q3 FY2024** | **$3,324.249M** | $868.493M | **consistent** — between Q2 $847.688M and Q4 $772.725M |
| **Q3 FY2025** | **$3,567.064M** | **$771.535M** | **ANOMALOUS** — breaks the sequence $883.629M → $915.446M → **$771.535M** → $996.454M |

**Nineteenth issuer, with the first non-conforming instance.** The FY2024 reading implies a
year-end quarter that fits the surrounding quarters. **The FY2025 reading implies a
year-end quarter that dips 16% sequentially in the middle of a rising year** — which no
other issuer's annual reading requires.

**Recorded honestly as: DA-26 confirmed at WWD for FY2024, unconfirmed for FY2025.** Two
readings are live and the extract cannot separate them:

1. The FY2025 row is the annual, and WWD genuinely had a weak Apr–Jun 2025 quarter.
2. The FY2025 row is contaminated differently — e.g. a trailing-twelve-month or
   fiscal-year-to-date figure rather than a full year.

**This is the first evidence that DA-26 is not uniform in *what* the row holds**, only in
*that* it is not a quarter. Carried to the DA-26 amendment as a scope question.

## 4. DA-27 CONFIRMED — WWD is an instance, and this corrects the artifact's first reading

Woodward's fiscal year ends **30 September**, so **FY2026 Q3 = Apr–Jun 2026**. The row whose
`period_end` is **2026-06-30** is labelled **`Q2 FY2026`**.

**That is a one-quarter label offset — WWD IS affected.**

**This corrects an earlier claim in this pass.** WWD was first recorded as showing genuine
quarters with no offset, on the grounds that its values are internally consistent. **Internal
consistency of the values is not evidence about the labels**, and the labels are wrong.

**DA-27 now stands at n=4 of 4**, with a clean partition on the fiscal-year-end axis:

| Fiscal year-end | Issuers | Offset |
|---|---|---|
| December | every other issuer in the universe | **none** |
| **January** | PL | **yes** |
| **April** | AVAV | **yes** |
| **September** | **WWD** | **yes** |
| **October** | HEI | **yes** |

**Four non-calendar issuers, four offsets. Every December issuer, none.** The mechanism — the
platform buckets by calendar quarter from 1 January and labels the bucket with the issuer's
fiscal year — fits all four and is exact for December year-ends.

**Removing WWD as a counterexample is what promotes DA-27 from CANDIDATE to CONFIRMED.**
Recorded rather than silently applied.

---

## Carry-forwards

1. **Third issuer with no consolidated operating income** (MRK, BMY, WWD). **The component-
   identity detector cannot run on any of them** — register the coverage caveat once.
2. **The margin ladder is graded, not binary**: HEI 25.5% → KRMN 19.1% → WWD ~17% → primes
   10.1–12.4%. **The mechanism is distance from programme-level risk**, not prime vs
   supplier.
3. **FIRST NON-CONFORMING DA-26 INSTANCE.** WWD FY2024 conforms; FY2025 implies a year-end
   quarter that dips 16% mid-sequence. **Scope question for the DA-26 amendment: the rows
   are reliably "not a quarter," but not reliably "a full year."**
4. **Clean-positive 19 of 19; DA-26 at 19 of 19 issuers** (one with an open sub-question).
