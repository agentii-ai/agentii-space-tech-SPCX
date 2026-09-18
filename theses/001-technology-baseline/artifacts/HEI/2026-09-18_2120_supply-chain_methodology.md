---
thesis_id: "001-technology-baseline"
pillar: PIL-3
ticker: HEI
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
    chosen_reading: "operating_income verified against components on the H1 block; HEI CLEAN"
  - da_id: "DA-26"
    chosen_reading: "the year-end row carries ANNUAL revenue (HEI's FY ends 31 Oct)"
  - da_id: "DA-27"
    chosen_reading: "CONFIRMED at n=4 of 4 — fiscal_period labels come from the calendar quarter, not the issuer's fiscal calendar; HEICO was the first instance, PL/AVAV/WWD confirm it"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# HEI — Supply-Chain Position (Flight-Critical Components & Aftermarket)

Source: Form 10-Q, accession `0000046619-26-000016` (period ended 2026-04-30).

---

## 1. HEICO earns a 25.5% operating margin — the highest of any hardware supplier yet

| Metric | Q1 FY2026 | Q1 FY2025 | Change |
|---|---|---|---|
| Revenue | **$1,375.713M** | $1,097.820M | +25.3% |
| Operating income | **$350.437M** | $248.152M | +41.2% |
| **Operating margin** | **25.5%** | 22.6% | **+2.9 pts** |
| Net income | $233.801M | $156.793M | +49.1% |
| EPS (diluted) | $1.66 | $1.12 | +48.2% |
| R&D / revenue | 2.6% | 2.6% | — |

**25.5% operating margin.** The supplier margin ladder now reads:

| Tier | Issuer | Operating margin |
|---|---|---:|
| **Component supplier** | **HEI** | **25.5%** |
| Component supplier | KRMN | 19.1% |
| Prime | LMT | 12.4% |
| Prime | RTX | 11.4% |
| Prime | LHX | 11.1% |
| Prime | NOC | 10.1% |

**Two independent component suppliers sit at 19.1% and 25.5%; five primes sit in a 10.1–12.4%
band.** The gap is not marginal — **component suppliers earn roughly 2× the primes whose
programmes they supply.**

**This substantially strengthens the KRMN finding and weakens the "levered roll-up"
alternative explanation.** Karman's 19.1% could have been purchase accounting; HEICO is a
67-year-old, low-leverage operator (liabilities $3,654M vs equity $4,305M — 0.85×, the
*least* levered issuer in the universe) earning a *higher* margin. **The pattern is a
property of the supply-chain position, not of any one company's accounting.**

**Refined rule, superseding the NOC version**: *component concentration predicts margin when
the supplier sells a differentiated part into many programmes.* Buyers being concentrated is
not the discriminator — **the primes' buyers are the same DoD that buys HEICO's parts.** The
discriminator is whether the supplier's revenue is spread across programmes or tied to one.

## 2. The two high-margin suppliers share one structural feature: aftermarket and PMA

Both HEICO and Karman sell into **installed bases** — HEICO through replacement parts and
PMA approvals, Karman through structures on fielded platforms. Neither depends on a new
programme winning to earn its margin. **The primes' margins, by contrast, are set by
cost-plus programme economics on a small number of large programmes.**

**Consequence for PIL-3**: the highest-quality exposure to launch growth is **not** the
primes and **not** the launch companies — it is the component layer serving installed
bases, because that layer's margin is insensitive to which programme wins. **This inverts
the universe's implicit ordering, which treats primes as the safe tier and suppliers as
derivative.**

## 3. HEI is clean on DA-23

The extract carries HEICO's **six-month block** (2025-11-01 → 2026-04-30):

```
revenue        $2,554.295M
cost of revenue $1,529.806M
               ─────────────
gross profit   $1,024.489M
gross profit - opex ($414.153M) = operating income $610.336M  ✓

EPS (diluted) $3.01 x 141.049M = $424.6M  vs  net income $423.989M   (0.14% gap)
```

**Both detectors pass.** HEICO is profitable and unaffected.

**Clean-positive count: 18 of 18.**

## 4. DA-26 — HEI shows it at the year-end quarter, the subtlest form

HEICO's fiscal year ends **31 October**, so its Q3 *is* its year-end quarter — the same
structure as PL. The mislabelling is hardest to spot here because a year-end quarter is
legitimately the largest of the year.

| Row | Revenue shown | What it is |
|---|---:|---|
| Q1 FY2026 | $1,375.713M | a genuine quarter |
| **Q3 FY2025** | **$4,485.044M** | **HEI's FY2025 ANNUAL revenue** |
| **Q3 FY2024** | **$3,857.669M** | **HEI's FY2024 ANNUAL revenue** |

**Eighteenth issuer confirmed.**

## 5. NEW — DA-27 CANDIDATE: fiscal-period *labels* do not match the issuer's own calendar

**Separate from DA-26, and a different class of defect.** DA-26 is a wrong *value* in a
quarter row. At HEICO there is also a wrong *label*:

| Row's period_end | HEI's own fiscal quarter | Platform label |
|---|---|---|
| 2026-04-30 | **Q2 FY2026** (Feb–Apr) | **Q1 FY2026** |
| 2026-01-31 | **Q1 FY2026** (Nov–Jan) | **Q4 FY2025** |

The cash-flow and income-statement blocks confirm the filing covers **2025-11-01 →
2026-04-30, a six-month period** — HEICO's H1. The platform labels it `Q1`.

**Why this is a CANDIDATE and not a confirmation**: the *values* on each row are internally
consistent (HEICO's quarters are genuine quarters here), so only the label is wrong. **A
labelling error and a value error have different blast radii** — a wrong label misorders a
time series; a wrong value corrupts every ratio computed from it.

**The distinguishing test has since been run, and it confirms.** Three further non-calendar
issuers were checked: **PL (January year-end), AVAV (April) and WWD (September) — all three
show the same one-quarter offset.** Every December-year-end issuer in the universe shows
none.

**DA-27 is therefore CONFIRMED at n=4 of 4**, with the offset partitioning the population
perfectly on the fiscal-year-end axis. **The mechanism**: the platform buckets periods by
calendar quarter measured from 1 January and labels the bucket with the issuer's fiscal
year — exact for December year-ends, off by one otherwise.

**One correction to record**: WWD was initially read as *not* showing the offset, on the
grounds that its values are internally consistent. **Internal consistency of values is not
evidence about labels** — WWD's period ending 2026-06-30 is its FY2026 Q3, labelled `Q2`.
That correction removes the only counterexample, which is what promotes DA-27 from CANDIDATE
to CONFIRMED.

---

## Carry-forwards

1. **HEI's 25.5% operating margin makes the supplier-tier finding structural, not
   accounting.** Two suppliers at 19.1% and 25.5%, five primes at 10.1–12.4%. **Refined
   rule: the discriminator is programme spread, not buyer concentration.**
2. **The best launch exposure in the universe is the installed-base component layer**, whose
   margin does not depend on which programme wins. **This inverts the universe's implicit
   prime-safe/supplier-derivative ordering.**
3. **DA-27 CONFIRMED at n=4 of 4** — fiscal-period *label* offset, mechanism identified,
   distinct from DA-26's value defect and compounding with it at non-calendar issuers.
4. **Clean-positive 18 of 18; DA-26 at 18 of 18 issuers.**
