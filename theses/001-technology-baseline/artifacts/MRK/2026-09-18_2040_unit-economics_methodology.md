---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: MRK
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T20:40:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-26"
    chosen_reading: "Q4 FY2025 and Q4 FY2024 rows carry ANNUAL revenue"
  - da_id: "DA-23"
    chosen_reading: "operating_income is NULL for MRK in the extract; EPS identity used instead and reconciles to 0.1%"
  - da_id: "DA-22"
    chosen_reading: "microgravity R&D is not separately disclosed; scale comparison used"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# MRK — Microgravity Demand End (Unit Economics of the Buyer)

Source: Form 10-Q, accession `0000310158-26-000212` (Q2 2026, quarter ended 2026-06-30).

---

## 1. The demand side is 30× the supply side — and the constraint is not capital

The microgravity thesis is usually framed as a supply problem: *if only there were more
capacity and lower launch cost, orbital R&D would scale.* **The financials invert that
framing.** The buyers are not capital-constrained. They are the largest R&D spenders on
earth.

**Merck, FY2025: revenue $65,011M, R&D $15,789M.**

Now compare against the **entire pure-play space cohort** in this universe — the seven
companies whose business *is* space:

| Company | FY2025 revenue (from the DA-26 annual rows) |
|---|---:|
| KRMN | $471.5M |
| PL | $307.7M |
| LUNR | ~$371M |
| RKLB | ~$500M |
| FLY | ~$200M |
| VOYG | $166.4M |
| YSS | ~$150M |
| **Combined** | **≈ $2.17B** |

```
Merck revenue          $65.0B  =  30x the entire pure-play space cohort
Merck R&D alone        $15.8B  =   7.3x the entire pure-play space cohort
```

**Merck spends 7.3× the combined revenue of every pure-play space company in the universe
on R&D — every year.** And Merck is one of four pharma buyers in this pillar.

**The binding constraint on orbital R&D is therefore not capacity and not launch cost.
It is the absence of a reason for a $15.8B/year R&D organisation to prefer orbit over the
terrestrial alternatives it already owns.** That is a demand-side problem, and no amount
of launch-cost reduction addresses it.

## 2. MRK's quarterly R&D is itself larger than the sector it would buy from

**Q2 2026 R&D: $9,741M** — 58.7% of the quarter's $16,607M revenue. **Q1 2026 R&D:
$12,592M** — 77.3% of revenue.

Those are not steady-state R&D ratios. They are **acquired IPR&D charges** — Merck has been
buying pipeline assets, and the accounting puts the charge in R&D. The relevant observation
is structural: **a single quarter of Merck's R&D is 4.5× the annual revenue of the largest
pure-play space company in the universe.**

**Consequence for PIL-4**: a single Merck programme decision, funded out of a rounding error
in one quarter's R&D, would exceed the entire addressable market of the space sector. **The
asymmetry is so large that the space sector's growth is not gated by its own capacity to
serve — it is gated entirely by whether any pharma programme chooses orbit.**

## 3. MRK is clean, but the operating line is absent

```
EPS (diluted) $0.54 x 2,470M weighted diluted shares = $1,333.8M
reported net income                                  = $1,335.0M
gap: 0.1%
```

**MRK is profitable and unaffected by sign stripping.**

**But note the coverage gap: `OperatingIncomeLoss` is NULL for MRK in the extract.** A
large accelerated filer with $65B of annual revenue has no operating income concept
available. **This is a data-coverage limitation, not a finding about Merck** — and it means
**the component-identity detector cannot be run on MRK at all.** The EPS identity is the
only available check, and it is the detector already shown to be unreliable (it passes on
both sides of a flip at RKLB, FLY and VOYG).

**Register as a coverage caveat**: for issuers whose primary statement does not tag
`OperatingIncomeLoss`, the universe has no reliable DA-23 detector. MRK, BMY and others in
this cohort are in that class.

## 4. DA-26 — MRK shows it twice

| Row | Revenue shown | What it is |
|---|---:|---|
| Q2 2026 | $16,607M | a genuine quarter |
| **Q4 2025** | **$65,011M** | **MRK's FY2025 ANNUAL revenue** |
| **Q4 2024** | **$64,168M** | **MRK's FY2024 ANNUAL revenue** |

**Fifteenth issuer confirmed.** FY2025 = Q1–Q3 $48,611M, so annual $65,011M implies Q4 2025
of $16,400M — plausible against Q3's $17,276M. **The annual reading is internally
consistent; a 3.8× quarterly jump is not.**

---

## Carry-forwards

1. **The demand side is 30× the supply side in revenue and 7.3× in R&D alone.** The
   microgravity constraint is **demand-side willingness, not supply-side capacity** — and
   launch-cost reduction does not touch it. **This is PIL-4's central finding.**
2. **One quarter of MRK's R&D ($9.7B) exceeds the annual revenue of the largest pure-play
   space company by 4.5×.**
3. **NEW COVERAGE CAVEAT**: `OperatingIncomeLoss` is NULL for MRK — **the component-identity
   detector cannot run.** Issuers tagging differently have no reliable DA-23 detector.
   Register for MRK, BMY and the cohort.
4. **DA-26 at 15 of 15 issuers.**
