---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-4
ticker: FLY
skill: peer-bench
mode: methodology
generated_at: 2026-09-19T16:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "8c91d57a0d74"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-01
    chosen_reading: "The basis register. FLY's matrix is A x / A' x / B x / C x - four of four bases empty - because no launch price, no launch count and no launch cost line is filed. Alpha therefore cannot be placed on the cost curve on ANY basis, and this is an ABSENCE finding rather than a measurement."
  - da_id: DA-25
    chosen_reading: "Normalised per-unit metrics not reproducible from audited tables. FLY supplies the denominator that cannot exist: \"1,000-kilogram payload class\" is a CATEGORY, not a mass, and the filing itself discloses the category's width as 6x. A $/kg built on it is a normalisation over a label."
  - da_id: DA-28
    chosen_reading: "Capital-structure discontinuity. The 2025 comparative columns are PARTIAL-PERIOD as-reported figures, against separately filed full-period pro forma figures for the same periods - so any 2025 growth rate is measuring an acquisition date, not growth."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. FLY is the CONTROL case and it is an INVERSE one: the two revenue bases ARE both filed and both named (as-reported and pro forma), so the defect here would be a reader collapsing them, not the filer omitting the basis. FLY also files one reportable segment, so its revenue-type disaggregation is not a segment split."
evidence_grade: DEMONSTRATED
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "\"We are the only U.S. company with a liquid-powered orbital launch vehicle in the 1,000-kilogram payload class.\" and \"We operate as a single reportable segment\""
    ticker: FLY
    citation_id: sec21
    page_no: 34
    form_type: 10-Q
    url: https://agentii.ai/v/FLY/sec21/34
    located_via: read_source_pages
  - figure: "Revenue disaggregation, four columns in the order [Q2 2026, Q2 2025, H1 2026, H1 2025]: Launch $9,400 / $6,349 / $22,652 / $11,519 thousand; Spacecraft Solutions $108,283 / $9,200 / $175,910 / $59,885 thousand; Total $117,683 / $15,549 / $198,562 / $71,404 thousand. Pro forma comparatives for 2025: revenue $61,116 thousand and $159,314 thousand, net loss $(67,614) thousand and $(156,441) thousand"
    ticker: FLY
    citation_id: sec21
    page_no: 15
    form_type: 10-Q
    url: https://agentii.ai/v/FLY/sec21/15
    located_via: read_source_pages
  - figure: "Launch performance obligation: revenue recognized on \"the initiation of the launch\" - POINT IN TIME, with no over-time component"
    ticker: FLY
    citation_id: sec21
    page_no: 16
    form_type: 10-Q
    url: https://agentii.ai/v/FLY/sec21/16
    located_via: read_source_pages
  - figure: "Two instances of the 1,000-kilogram payload-class label in the business overview"
    ticker: FLY
    citation_id: sec16
    page_no: 7
    form_type: 10-K
    url: https://agentii.ai/v/FLY/sec16/7
    located_via: read_source_pages
  - figure: "\"Alpha is the only provider of small size launch that has achieved orbit and addresses a critical gap in the market in the 1,000 kilograms category\"; \"the global market right-sized toward satellites between 200 kilograms to 1,200 kilograms, according to analysis by BryceTech in 2025. While Starlink represents a significant number of these satellites, 64% of the satellites launched since 2015 fit within this range.\""
    ticker: FLY
    citation_id: sec16
    page_no: 9
    form_type: 10-K
    url: https://agentii.ai/v/FLY/sec16/9
    located_via: read_source_pages
  - figure: "The contrast vehicle: Electron filed only as \"up to 300 kg\" to low Earth orbit across inclinations from 38 to 120 degrees, while Neutron - the UNFLOWN F5b vehicle - is filed as \"approximately 13,000 kg for reusable configuration\""
    ticker: RKLB
    citation_id: sec87
    page_no: 8
    form_type: 10-K
    url: https://agentii.ai/v/RKLB/sec87/8
    located_via: read_source_pages
key_metrics:
  launch_share_of_revenue_pct_3m: 7.99
  spacecraft_solutions_share_of_revenue_pct_3m: 92.01
  spacecraft_to_launch_revenue_multiple_x: 11.52
  as_reported_over_pro_forma_pct_3m_2025: 25.44
---

# FLY — a payload CLASS LABEL where every peer files a mass, and four of four bases empty

**Finding.** Firefly's Alpha is described only as a **"1,000-kilogram payload class"** vehicle — a category, not
a quantity. There is **no mass, no orbit, no inclination and no configuration** attached to it, and the filing
itself discloses the category's width as **6×** (`200 kg` to `1,200 kg`). So **Alpha cannot be placed on the
cost curve on any basis: A ✗ / A′ ✗ / B ✗ / C ✗ — four of four empty**, and the emptiness is a property of the
disclosure, not of the vehicle. Meanwhile **92.0% of FLY's revenue is Spacecraft Solutions against 8.0% from
launch**, in a company that files **one reportable segment**. FLY's value in this thesis is as the
**disclosure-uniqueness control**: it is the case that shows a peer-bench table can absorb a deficient
*quantity* (Electron's 300 kg ceiling) but cannot absorb a *category* at all (P4).

## 1. Acceptance test — adopted and run

An identification is accepted only if it is **(a) exact**, **(b) stable across periods**, and **(c) consistent
with a specified formula or a filed basis**. Everything else is `UNRESOLVED` — never "probably fine". The
register records a ~**2,500**-candidate sweep over **36 filed cells** returning **6–9 coincidental hits per
metric**, with only **2 of 16** served ratio fields being the ratio they claimed. **Every figure below is
recomputed from filed cells; no served ratio is quoted.**

**Rows this artifact is entitled to add to the cross-vehicle table: none.** That is the result. The
section-by-section accounting:

| Test | Result |
|---|---|
| Basis A — a filed customer price per launch | **ABSENT** |
| Basis A′ — realized revenue ÷ filed launch count | **ABSENT** — the count is not filed |
| Basis B — a filed marginal cost per launch | **ABSENT** — one reportable segment, no launch cost line |
| Basis C — fully-loaded amortized | **ABSENT** |
| A filed mass to place in the denominator | **ABSENT** — a class label stands in its place |
| The 2025 growth rates | **`UNRESOLVED`** — the comparatives are partial-period (§4) |

## 2. The class label is not a mass

| Filed string | Source | What it supplies |
|---|---|---|
| *"the 1,000-kilogram payload class"* | [sec21 p.34](https://agentii.ai/v/FLY/sec21/34) | a category name |
| *"the 1,000-kilogram payload class"* (×2) | [sec16 p.7](https://agentii.ai/v/FLY/sec16/7) | a category name |
| *"the 1,000 kilograms category"* | [sec16 p.9](https://agentii.ai/v/FLY/sec16/9) | a category name |
| *"satellites between 200 kilograms to 1,200 kilograms, according to analysis by BryceTech in 2025"* | [sec16 p.9](https://agentii.ai/v/FLY/sec16/9) | **the category's own filed width** |

**Mass: not stated. Orbit: not stated. Inclination: not stated. Configuration: not stated. Reference mission:
not stated.** The label appears four times across two filings and is never accompanied by a quantity of payload
delivered.

**And the width is filed.** The same page that names the `1,000 kilograms category` discloses that the market
it addresses is *"satellites between 200 kilograms to 1,200 kilograms"*. **1,200 ÷ 200 = 6×.** Even taking the
label entirely at face value, any dollars-per-kilogram derived from it carries a **6× denominator
uncertainty** — and that is the *most favourable* reading, because it assumes the label means the category's
midpoint, which the filing never says. Under clause (c) the class label has **no specified formula and no filed
basis**; it is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` in the strict sense that no further arithmetic on the filed
cells can produce a mass.

### 2.1 Why FLY is the control: a ceiling is usable, a category is not

The peer-bench table's other deficient entry is Electron, and the two failures are **different in kind**:

| Vehicle | Filed payload statement | Orbit | Nature | Usable in a ratio? |
|---|---|---|---|---|
| **Electron** (RKLB) | *"up to 300 kg"* | **LEO, inclinations 38–120°** | a **CEILING** on a stated orbit | **YES — as an upper bound** |
| **Alpha** (FLY) | *"1,000-kilogram payload class"* | **not stated** | a **CATEGORY** with a 6× width | **NO** |

Sources: [📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8) and
[📄 FLY 10-K p.9](https://agentii.ai/v/FLY/sec16/9).

**This is the control's function.** Electron's correction is `1.00×–1.50×` and is reportable *because* the
deficiency is one-directional: `"up to"` bounds the answer, so the correction is an **upper bound** and still
carries information. Alpha's deficiency is **unbounded in both directions** — the same label covers a 200 kg
payload and a 1,200 kg payload — so no correction exists and none is attempted. **The peer-bench table can
absorb an upper bound. It cannot absorb a category**, and FLY is the vehicle that proves the distinction is
real rather than a matter of degree.

**The inversion is worth stating plainly.** In this universe, the vehicle that has **never flown** (Neutron,
RKLB's F5b) is filed with a usable reusable payload of *"approximately 13,000 kg"*, while the vehicle that
**has achieved orbit** (Alpha, FLY's F5c) is filed with a class label. **The disclosure is better for the
unflown vehicle than for the flown one.** PIL-4 turns on a payload bar; for FLY's vehicles that bar cannot be
evaluated at all, and the reason is disclosure rather than physics.

## 3. Four of four bases empty, and the revenue is not a launch business

**Basis matrix — every cell ABSENT, on filed evidence:**

| Basis | Definition | FLY's filed position | Verdict |
|---|---|---|---|
| **A** | customer list price per launch | no price per launch filed anywhere | ✗ |
| **A′** | issuer-realized variant (revenue ÷ launches) | **no launch count filed** — the divisor does not exist | ✗ |
| **B** | marginal cost per launch | one reportable segment; no launch cost-of-revenue line | ✗ |
| **C** | fully-loaded amortized | no launch-level capital or amortization isolated | ✗ |

The single-segment fact is filed explicitly: *"We operate as a single reportable segment"*
([📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34)). **The revenue-type disaggregation below is therefore
NOT a segment split**, and treating `Launch` as a segment is precisely the DA-30 collapse this artifact exists
to avoid.

**Revenue disaggregation, four columns in the order [Q2 2026, Q2 2025, H1 2026, H1 2025]** — the order is
recovered, not assumed, because **all four columns close exactly**:

| Line | Q2 2026 | Q2 2025 | H1 2026 | H1 2025 |
|---|---|---|---|---|
| Launch | $9,400k | $6,349k | $22,652k | $11,519k |
| Spacecraft Solutions | $108,283k | $9,200k | $175,910k | $59,885k |
| **Total** | **$117,683k** | **$15,549k** | **$198,562k** | **$71,404k** |
| **Launch share** | **7.99%** | 40.83% | **11.41%** | 16.13% |
| **Spacecraft Solutions share** | **92.01%** | 59.17% | **88.59%** | 83.87% |

Source: [📄 FLY 10-Q p.15](https://agentii.ai/v/FLY/sec21/15). Four of four columns reconcile
(`9,400 + 108,283 = 117,683`; `6,349 + 9,200 = 15,549`; `22,652 + 175,910 = 198,562`;
`11,519 + 59,885 = 71,404`), all exact — which is how the column order is established.

**The finding is the composition.** FLY is a **satellite manufacturer with a launch vehicle attached**: launch
is **7.99%** of revenue in the most recent quarter and Spacecraft Solutions is **92.01%**. The segment whose
name matches the thesis's subject is the *smaller* one by a factor of **11.5×** (`108,283 ÷ 9,400 = 11.52`).
This is a peer-bench warning as much as a FLY finding: **a vehicle's manufacturer is not necessarily a launch
business**, and any cross-vehicle comparison that aligns FLY with RKLB as "launchers" is aligning 8% of one
company against the whole of another.

## 4. The 2025 comparatives are partial-period — so the growth rates are `UNRESOLVED`

**This is the sharpest caution in the artifact and it is FLY-specific.** The filing discloses **two bases for
the same 2025 periods**, both named:

| Period | As-reported revenue | Pro forma revenue | As-reported ÷ pro forma |
|---|---|---|---|
| Q2 2025 (3M) | **$15,549k** | **$61,116k** | **25.44%** |
| H1 2025 (6M) | **$71,404k** | **$159,314k** | **44.82%** |

Source: [📄 FLY 10-Q p.15](https://agentii.ai/v/FLY/sec21/15). The pro forma comparatives are filed alongside
net losses of **$(67,614)k** and **$(156,441)k** for the same two periods.

**The as-reported comparative quarter is roughly a quarter of the period's combined activity.** So the naive
growth rates — launch revenue **+48.0%** on the quarter (`9,400 ÷ 6,349 = 1.480`) and **+96.6%** on the six
months (`22,652 ÷ 11,519 = 1.966`) — are computed between a **full** period and a **partial** one. Under
clause (b) — stable across periods — these **fail**, and they fail in the *optimistic* direction cited
everywhere in this workspace.

**Why this is the inverse of the usual DA-30 defect.** Both bases are filed **and both are named**
(`as-reported` and `pro forma`), so the filer has done the work. The defect would be a **reader** collapsing
them — and a reader who takes `+48.0%` without the basis is quoting a partial-period comparison as growth.
**FLY is therefore the DA-30 control: the universe's one case where the filer supplies the basis field and the
hazard lies entirely with the consumer.** This is why DA-26's register entry marks FLY the counterexample and
why FLY must not be reported as universally defective.

**A second, smaller basis note on the same figure.** FLY's launch revenue is recognized at a **point in time**:
the performance obligation is *"the initiation of the launch"*, and revenue is recognized *"at that point in
time"* ([📄 FLY 10-Q p.16](https://agentii.ai/v/FLY/sec21/16)). RKLB's HASTE missions are recognized **over
time** (filed verbatim at RKLB's per-launch page). **So a "revenue per launch" denominator counts a
point-in-time orbital mission and an over-time suborbital testbed identically while their recognition differs** —
which is exactly the contamination that drives Electron's `1.00×–1.50×` correction. FLY is clean of that
particular defect and cannot be compared to RKLB on a per-launch basis for the opposite reason: it files no
count at all.

## 5. What this artifact could NOT resolve

| Unresolved | Why | Class | Disclosure that would resolve it |
|---|---|---|---|
| Alpha's payload mass | Filed only as a class label with a filed 6× width | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A payload mass to a stated orbit on a stated configuration |
| Alpha's and Eclipse's position on the cost curve | Four of four bases absent; no price, count or cost line filed | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A per-launch price or a per-launch cost, on any named basis |
| FLY's launch and Spacecraft Solutions revenue growth, like-for-like | The 2025 comparatives are partial-period as-reported against full-period pro forma; the pro forma **launch** revenue is not filed | `UNRESOLVED` | Pro forma revenue by revenue type, on the same basis as the as-reported columns |
| Eclipse (F5b) — PIL-4's payload bar | Vehicle is unflown, so no demonstrated mass exists; FLY files no target payload for it either | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A filed payload spec for Eclipse in its reusable configuration |

**Two different dispositions, two different remedies, kept apart deliberately.**
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` here means the *issuer does not file the quantity* — re-querying the
platform will never produce it. The partial-period `UNRESOLVED` row is different again: the *filer has the
information and files one arm of it*, so the gap is narrower and the resolving disclosure is specific.

**`ABSENT` is not `CLEAN`.** Four of four bases being empty is a **result about disclosure**, not a
measurement that came back zero. No FLY vehicle has been shown to be uncompetitive on cost — the comparison
**could not be run**, and this artifact records it as unrun.

---

## Sources

| Figure | Source |
|---|---|
| The 1,000-kilogram payload class; single reportable segment | [📄 FLY 10-Q p.34](https://agentii.ai/v/FLY/sec21/34) |
| Revenue disaggregation and 2025 pro forma comparatives | [📄 FLY 10-Q p.15](https://agentii.ai/v/FLY/sec21/15) |
| Launch revenue recognized at a point in time | [📄 FLY 10-Q p.16](https://agentii.ai/v/FLY/sec21/16) |
| Two class-label instances in the business overview | [📄 FLY 10-K p.7](https://agentii.ai/v/FLY/sec16/7) |
| The 1,000 kilograms category and the filed 200–1,200 kg width | [📄 FLY 10-K p.9](https://agentii.ai/v/FLY/sec16/9) |
| Contrast vehicle: Electron's 300 kg ceiling and Neutron's 13,000 kg | [📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8) |

> Every figure asserted above resolves to the page cited, and every ratio is recomputed from filed cells. Pages
> were read directly; the served metrics block was not used. This artifact's central claim is an **absence**,
> and an absence cannot be established from a metrics block that reports only what it found.
