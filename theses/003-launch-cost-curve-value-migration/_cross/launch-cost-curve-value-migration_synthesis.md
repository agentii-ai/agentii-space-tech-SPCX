---
thesis_id: "003-launch-cost-curve-value-migration"
artifact: launch-cost-curve-value-migration
pillar: cross
ticker: cross
skill: synthesis
mode: default
task: T900/T901
generated_at: 2026-09-19T18:00:00+08:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-19
corpus_version: "agentii-2026-09-18"
schema: thesis_synthesis
schema_version: 1
evidence_grade: DERIVED
definitions_used:
  - da_id: DA-23
    chosen_reading: "Sign stripping at the platform's extraction layer. Confirmed at 9 of 9 universe tickers, but the sharpest instance in this thesis is an ARTIFACT rather than an issuer — the GSAT analysis written to document DA-23 was itself reproducing it on eight figures, including a claimed divergence that existed only because the artifact had read a stripped value, and all three automated gates passed on the stripped version. A clean gate result is not evidence of a clean number."
  - da_id: DA-26
    chosen_reading: "Annual figures mislabelled as quarterly in the metrics block. The register's entry reads 'universal, 19 of 19'; this thesis FALSIFIES universality — 20 tested, 19 exhibiting, with FLY the counterexample whose served rows carry interim cumulative figures and never annual ones. DA-26 is screen-conditional, not universal, and must not be applied without running the screen."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept, collapsed without a basis field. This is the spine's A2, and its canonical shape: SPCX's 8-K carries four arithmetically correct $/kg values spanning 12.8x on one page with zero basis fields among them. The decomposition is exact — numerator 1.617x, denominator 7.886x — which is why every rung of the ladder names its basis and no rung is averaged with another."
pillar_verdicts:
  PIL-1: "HOLDS — falsifier does not fire, on a population of one"
  PIL-2: "HOLDS at SPCX; UNEXERCISED everywhere else"
  PIL-3: "HOLDS — demonstrated, not argued"
  PIL-4: "CLOSES on the registered bar; FIRES on two other bases; knife-edge on a third"
  PIL-5: "FALSIFIED in tolerance; HOLDS in kind"
  PIL-6: "NON-FORMABLE at three of four demand-side names"
capability_timeline:
  note: >
    Not applicable — this thesis is `market_data_stage: none` and carries no
    capability-adoption timeline. The nearest equivalent is the trigger register (§7).
---

# Thesis 003 — Launch Cost Curve & Value Migration

> **This is the thesis-level synthesis.** It is the spine the letter-size report is authored
> from, and it consumes the two primary artifacts — `_cross/launch-cost-curve.md` (P1) and
> `_cross/value-pool-map.md` (P2) — which remain the citable references for 004 and 005.

**Claim.** Launch cost is the sector's master **cost** variable and not its master **value**
variable. The curve is real but thin — one vehicle has a measured marginal cost, and on the
corrected denominator its cost per kilogram **rose 32.0%** while its cost per launch fell
12.0%. The value pool migrated to whoever owns the demand, and the released value did not pass
through to the payload customer.

**as_of** 2026-09-19 · **constitution pin** 1.5.0 · **universe** 9 tickers · **corpus** 47 files

---

## §1 The curve is one point, and the point moves the wrong way

**Exactly one vehicle in the universe has a `DEMONSTRATED` marginal cost: Electron.** RKLB is
the only issuer disclosing `cost per launch` and `revenue per launch`; FLY discloses neither,
and neither does SPCX. Every other `$/kg` on the table is `CLAIMED` or `MODELED`.

Measured against the right denominator, that one point **inverts**:

| Period | Missions | Cost/launch | Revenue/launch | Basis B $/kg | Basis A $/kg | (rev−cost)/rev |
|---|---:|---:|---:|---:|---:|---:|
| FY2023 | 10 | $7.0M | $7.1M | $23,333/kg | $23,667/kg | 1.4% |
| FY2024 | 16 | $5.7M | $7.8M | $19,000/kg | $26,000/kg | 26.9% |
| FY2025 | 21 | $4.8M | $8.5M | $16,000/kg | $28,333/kg | 43.5% |
| Q2 2025 | 5 | $5.0M | $7.9M | $16,667/kg | $26,333/kg | 36.7% |
| Q1 2026 | 6 | $5.4M | $9.3M | $18,000/kg | $31,000/kg | 41.9% |
| **Q2 2026** | 6 | **$4.4M** | **$9.1M** | **$14,667/kg** | **$30,333/kg** | **51.6%** |

**Q2 2025 → Q2 2026: cost per launch −12.0% ($5.0M → $4.4M) while cost per kilogram +32.0%
($16,667 → $22,000/kg).** Both values are exact and both are filed — because **two of the six
Q2 2026 Electron missions were HASTE suborbital testbeds delivering zero kg to LEO**, and they
sit inside **both** the revenue numerator and the launch-count numerator. The filing says so
verbatim. The fleet denominator fell 1,500 → 1,200 kg (−20.0%) while the per-mission cost fell
only 12.0%, so the ratio rises. Two independent routes agree: `0.88 ÷ 0.6667 = 1.32` and
`1.056 ÷ 0.80 = 1.32`. **Breakeven fill-rate ratio: 0.758.**

> **The disclosed improvement is a denominator artefact in the optimistic direction.** The
> sector's cost-curve story rests on this vehicle, and at its best-measured point the story does
> not hold.

**PIL-3's falsifier does not fire, and it does not fire for the right reason.** The share of
universe cost-reduction claims with a filed, flown or audited basis is **1 of 4 = 25%**, below
the 50% threshold — and the one demonstrated reduction is on the **expendable** vehicle, the
architecture the sector's reusability narrative has written off. The admissibility frame is
Wright's Law: it needs a learning rate over **≥5 cumulative production doublings**; Electron
supplies **one point**, so the finding is **definitional, not evidential**.

## §2 The ambiguity is the denominator, and it is five times the basis question

SPCX's 8-K carries **four arithmetically correct $/kg values spanning 12.8×** — all on one page,
none a calculation error:

| Value | Construction | Denominator |
|---|---|---|
| **$939/kg** | launch services revenue ÷ **all** mass to orbit | 1,041 t |
| $1,519/kg | Space segment revenue ÷ all mass to orbit | 1,041 t |
| **$7,409/kg** | launch services revenue ÷ **customer** payload, 6M | 132 t |
| **$11,977/kg** | Space segment revenue ÷ customer payload, 6M | 132 t |

The decomposition is exact: **numerator factor 1.617×** (1,581/978) · **denominator factor
7.886×** (1,041/132) · product 12.75×. **The denominator axis is 4.9× the basis axis.**

The five-column table those values sit in is **unlabelled**, and its column order was
**recovered rather than assumed** — three independent reconciliations force it (`40 + 38 = 78`
launches; `330 + 648 = 978` revenue; `45 + 87 = 132` payload), confirmed 4/4 against the 10-Q's
Falcon/Starship split.

**The 20-cell census — 5 vehicles × 4 bases:**

| | Count |
|---|---|
| `DEMONSTRATED` | **2** — both Electron (basis A, basis B) |
| `DEMONSTRATED` figures / `MODELED` division | 2 — Falcon 9 A′, C |
| `CLAIMED` | 2 — Falcon 9 A, Neutron A |
| `MODELED` | 1 — Falcon 9 B |
| **ABSENT** | **13** |

Basis B — the only basis that tests an F5 floor — is `DEMONSTRATED` on **1 of 5 vehicles**.
Starship's entire row is **`UNEXERCISED`, not `CLEAN`**: zero customer launches means no price
exists to test.

**The nine-rung ladder** ($939 → $11,977/kg, all LEO, every rung basis-named): four axes move
it — basis **1.617×** · denominator **7.886×** · capacity-vs-realized convention **2.621×** ·
period, matched-pair **1.34×**. **Nothing in the spread is uncertainty. All of it is definition.**

**Falcon 9 basis A at $2,939/kg is denominator-failed** — `"22.8"` returns **zero located
pages** across SPCX filings, verified twice. The internally consistent SPCX series is the
matched-pair band **$5,567–7,448/kg** (1.34×).

## §3 The value pool went to whoever owns the demand

**Both independent operators in the universe were acquired within twelve months.**

| | GSAT → Amazon | IRDM → RKLB |
|---|---|---|
| Agreed | **2026-04-13** | **2026-06-28** |
| Price | **$90.00/share** | **$54.00/share** |
| Stockholder approval | **NONE SOUGHT** — Thermo 57.6% written consent | Required (Form S-4) |
| Target operating margin | **−7.37%** (from +9.15%) | **+15.10%** (from +23.17%) |
| Implied equity | **$11,660.7M** ($90.00 × 129,563,390) | $5,721.9M |
| TTM revenue | $280,642k | $884,169k |
| **Multiple** | **41.4×–41.6×** | **≈8.3×** — ⚠ `UNRESOLVED`, armed band **6.5×–8.5×** |

Amazon pays ≈**41.4×** TTM revenue for a **loss-making** operator; RKLB pays ≈**8.3×** for a
profitable one — a ≈**5.0×** multiple ratio **against** a 22.5-point margin differential in the
**opposite** direction. **Neither acquirer priced the target's income statement.** Both priced
the customer relationship underneath it — at GSAT, 64% of 6M revenue is a single counterparty
who is also the financier.

**The margin ladder is BIMODAL, not monotone.**

| Rung | Mean / value |
|---|---|
| Component suppliers (TER 32.9 · HEI 25.5 · CW 19.3 · KRMN 19.1 · WWD ~17.0) | **22.76%** |
| Prime integrators (LMT 12.4 · RTX 11.4 · LHX 11.1 · NOC 10.1) | **11.25%** |
| **ANCHOR (a): 22.76 / 11.25** | **HOLDS at 2.02×** |
| Demand-owning operator — SPCX Connectivity | **+38.59%** |
| Single-customer operator — GSAT | **−7.37%** |
| Launchers / manufacturers — RKLB −24.57 · LUNR −22.86 · PL −37.06 · YSS −44.64 · SPCX Space −56.34 · FLY −80.90 | negative |

**ANCHOR (b) is FALSIFIED**: the worst verified margin is **FLY's −80.90%, a manufacturer**,
24.56 pp below the next-worst row — while the single-customer operator runs at −7.37%, *better*
than seven other rows.

**SPCX's launch segment holds both ends at once.** Q2 2026: gross margin **65.80%** (1st of 3)
against operating margin **−56.34%** (3rd of 3) — a **122.14 pp** within-segment swing,
decomposed exactly as **R&D 111.85 pp + SG&A 10.29 pp**. Against Connectivity the spread is
**94.93 pp** = +105.00 pp R&D + 3.74 pp SG&A − 13.81 pp gross. **Which ladder you pick decides
whether launch looks like the best business in the sector or the worst.**

## §4 The demand side does not price off the curve — and the number cannot be drawn

PIL-6's falsifier needs launch cost as a share of **programme** cost. At **three of four**
demand-side names the quantity is **`NON-FORMABLE`**, and each for a different reason:

- **YSS — a PRESENCE finding.** Cost of revenues decomposes **exhaustively** into four components
  that close exactly across four periods (Q2 2026: 53,240 + 17,127 = 70,367 ✓; FY2025:
  264,007 + 46,736 = 310,743 ✓). **Launch is excluded because the decomposition is complete** —
  this is the strongest form of non-formability available.
- **PL** — launch is *named* verbatim (*"third-party fees for launch procurement"*) and
  quantified **nowhere**. The only filed launch figure is a forward **stock**: $4.7M of FY2028
  commitments, absent from the 10-K's commitments note entirely. **With cost of revenue at zero,
  PL's operating margin is still only +9.4% quarter / +13.1% annual.**
- **SATS** — named launch agreements on EchoStar XXV and XXVI with **no dollar amount on either
  side**.
- **LUNR 14.19% FY2025** is the only value above the 0.10 bar — and it is a **consolidated**
  denominator, collapsing to 2.80–4.37% in 2026 as a **denominator event**: the numerator fell
  6.6% while cost of revenues rose **174.0%** as Lanteris (acquired January 2026) added $166,735K
  of product revenue containing no launch. **Same defect class as SPCX's `+$1,824M`.**

**The pass-through arm points the opposite way at RKLB** — the only issuer disclosing both
series: revenue per launch **+15.2%** while cost per launch **−12.0%**. The released cost was
**captured, not passed through.** Direction `DEMONSTRATED`; levels not.

**YSS is carried as the positive counterexample**: non-GAAP contribution margin rose on every
basis (33→34, 24→42, 29→38), with direct material per revenue dollar falling **$0.758 → $0.575**.
**This keeps PIL-6 from being a universal claim.**

## §5 The data-integrity register is now the finding

**DA-23 — the platform serves a filed negative as a positive of identical magnitude (`|x|`, not
inversion) — is confirmed at 9 of 9 universe tickers.** Its sharpest instances:

| Issuer | Incidence |
|---|---|
| **PL** | **33 of 33** facts — the universe's cleanest instance (gross profit 50,401 − opex 85,289 = (34,888), filed as +34,888) |
| **RKLB** | 12 of 12 facts; **three lines flip in one quarter** (operating, net income, diluted EPS). Invisible to any heuristic — RKLB has never had positive operating income |
| **SATS** | **12 of 12** and **8 of 8** across **four independent axes** |
| **SPCX** | 14 of 14 facts, 4 of 4 periods; served `+143` against filed `(143)` |
| **GSAT** | ≥18 cells; Q2 2025 `+6,146` preserved against Q2 2026 `(4,775)` stripped — a **bidirectional control inside one concept** |

**The four classes kept distinct, because their remedies differ:**

| Class | Count | Remedy |
|---|---|---|
| `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | many | wait for, or request, a disclosure |
| `UNRESOLVABLE-FROM-PLATFORM` | several | tooling |
| **`REACHABLE-BUT-NOT-RECORDABLE`** | **8 rows** | **a contract amendment — research cannot fix it** |
| `NON-FORMABLE` | 4 | report the refusal, never PASS |

**Six of the thirteen curve absences sit in the third class** — the datum is reachable and the
contract has no admissible field for it. **Falcon 9's 22.8 t is the denominator of all four
basis letters** and is uncitable; so is the $67M list price, Neutron's expendable payload, and
Alpha's mass.

**`UNEXERCISED` is not `CLEAN`.** The following are tests that **could not run**, and are
reported as such: Starship's entire row; SPCX DA-26 (no 10-K exists); RKLB/FLY/SATS/GSAT DA-27;
LUNR DA-27 (excluded, not clean); and PIL-2's `wrong_if` census at every issuer except SPCX —
*"a census reporting '0 of N operators exceeding' would be claiming a test that could not run."*

**Named defects with no register entry — and deliberately not numbered (`no DA-31 exists`):**
GSAT's `common_shares_outstanding` serves the **preferred** count (`149425`) against a filed
common of **129,563,390** — an **867× error**, wrong in the *conservative* direction so it never
announces itself. `get_segment_data` is unusable; `data_freshness` reports **2027-04-12**.

**PIL-2 holds at SPCX on `DEMONSTRATED` segment data** — Space **−56.34%** (3M) / **−76.15%**
(6M) sits below Connectivity **+38.59%** and AI **−49.08%** in both periods. Everywhere else the
test is `UNEXERCISED`, because no other issuer files a segment operating margin.

## §6 What this thesis corrected in 001 and 002

Five corrections with the widest reach; the full register is 27 rows in `plan.md`.

| # | Old → New | Why |
|---|---|---|
| 1 | Electron `$14,667/kg` as settled → **reconverted**, `1.00×–1.50×` | The register's `1.79×–2.62×` was **Falcon 9's arithmetic from SPCX's table**; RKLB files no mass-to-orbit in any period. **"Four of four periods" falsified** — the correction is **zero** in the one fully-filed-mix period |
| 2 | PIL-4 threshold `2939` → **`5567`** (band `[5567,7448]`) | Denominator-failed **and** a basis collapse inside its own definition — an Electron price over a Neutron denominator |
| 3 | PIL-5 `timing` → **`period_normalisation`** | Q2 2025 is the zero-HASTE control and the gap still diverges −15.3% / −22.9% |
| 4 | DA-26 "19 of 19, universal" → **"20 tested, 19 exhibiting"** | **FLY is the falsifying counterexample** |
| 5 | F5a/F5b "do not reach Electron — open amendment" → **CLOSED at v1.3.0** with **F5c** | The real finding is an **inversion**: the tiers with unproven floors dominate the conversation while **F5c holds the only `DEMONSTRATED` price** |

Others of note: SATS' *"~$27B spectrum gain"* is a **non-cash $(16,481,468)k impairment charge**
(nothing closed); LUNR's *"42.1% operating margin"* **does not exist** (it is `|FY2025 annual|`
on a quarterly label carrying a DA-23 strip); GSAT's *"7.4% margin"* is the **stripped sign** —
the filed figure is **−7.37%**; and the component identity `gross profit − opex` is
**conditional on the opex definition** — false at UTHR by exactly cost of sales, 6 of 6 periods.

## §7 The trigger register — what would move this

Eight triggers, **none triggered**. Cheapest: a per-launch cost disclosure in Neutron's first
flight quarter. Highest-value: a filed Starship price or payload mass — **Starship carries four
of the thirteen absences**.

## §8 The finding about this work itself

**The GSAT analysis written to document DA-23 was itself reproducing it — on eight figures** —
including a claimed divergence that existed only because the artifact had read a stripped value.
**All three automated gates passed on the stripped version.** What caught it was tracing each
platform output back to the filed page and *reading* it.

> *A check that closes cleanly can be testing nothing.* Every figure a downstream thesis
> inherits should carry **the basis it was read on**, not only its grade.

## §9 Dispositions — what could not be resolved

**`UNRESOLVABLE-FROM-PUBLIC-SOURCES`:** Starship A/A′/B/C · Falcon 9 A (denominator) and B ·
Electron mass-to-orbit · Alpha all four bases · SPCX DA-26 (needs an FY2026 10-K, ~Feb 2027 —
the single highest-value resolution) · SATS programme cost (both legs).
**Permanently unresolvable, by the issuers' own filings:** RKLB basis C and Neutron basis C —
*"Management does not regularly review either reporting segment's total assets or operating
expenses."*
**`UNRESOLVABLE-FROM-PLATFORM`:** `list_xbrl_concepts` returns **zero** concepts platform-wide
containing `"Launch"` or `"Satellite"` — the structured vocabulary has no term for this thesis's
domain.
**`UNRESOLVED`:** the 8.3× IRDM multiple (band 6.5×–8.5×) · the SATS cash collision ($1.516bn
filed vs *"$14bn or $15bn"* on the call — a **9.6× gap** with opposite solvency implications).

---

*Citable primaries: `_cross/launch-cost-curve.md` (P1) and `_cross/value-pool-map.md` (P2).
Source corpus: 45 artifacts across 9 tickers, `artifacts/`.*
