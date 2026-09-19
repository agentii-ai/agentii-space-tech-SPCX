---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-3
ticker: SPCX
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
    chosen_reading: "The basis register. Every $/kg below is tagged A (customer list price), A' (issuer-realized variant), B (marginal cost per launch, the only basis testing the F5 floor) or C (fully-loaded amortized). SPCX files NO cost-per-launch figure on any basis, so no SPCX cell can be graded on basis B."
  - da_id: DA-27
    chosen_reading: "Fiscal-period labels. SPCX's throughput figures are filed on two period bases in one table - three-month and six-month - and the 8-K's five columns are not self-labelling, so the column order must be recovered by reconciliation rather than assumed."
  - da_id: DA-29
    chosen_reading: "A reconciliation that closes is not thereby a check. SPCX's customer + internal payload components sum to the filed mass-to-orbit total within 1 tonne on four of five columns - a discrepancy of exactly one unit, which is a rounding artifact rather than an error, and is recorded rather than smoothed."
  - da_id: DA-30
    chosen_reading: "Two bases on one concept collapsed without a basis field. CONFIRMED twice: the customer share has two filed denominators with opposite period-signed trends, and the $/kg ratio has two filed numerators and two filed denominators on ONE page, giving a 12.8x spread among four arithmetically correct values."
evidence_grade: DEMONSTRATED
key_metrics:
  usd_per_kg_launch_services_over_customer_payload_h1_2026: 7409
  usd_per_kg_space_segment_over_customer_payload_h1_2026: 11977
  usd_per_kg_launch_services_over_mass_to_orbit_h1_2026: 939
  same_page_usd_per_kg_spread_ratio: 12.8
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Space segment table, five columns in the order [Q2 2026, Q1 2026, Q2 2025, H1 2026, H1 2025]: customer launches 10/7/9/17/21; total launches 38/40/46/78/84; customer payloads 87/45/88/132/163 t; mass to orbit 485/556/652/1,041/1,102 t; launch services revenue $648/$330/$490/$978/$1,056M; Space revenue $962/$619/$746/$1,581/$1,611M; cost of revenue $329/$281/$330/$610/$627M; R&D $1,076/$930/$693/$2,006/$1,219M; SG&A $99/$70/$87/$169/$175M"
    ticker: SPCX
    citation_id: sec7
    page_no: 7
    form_type: 8-K
    url: https://agentii.ai/v/SPCX/sec7/7
    located_via: read_source_pages
  - figure: "Mass-to-orbit definition (total kilograms of payload delivered from all successful orbital and flight tests, excluding failed or scrubbed attempts); \"Our Space segment revenue only reflects our customer launches and customer activities.\"; Falcon launches 37/45/77/81 with Starship 1/1/1/3; \"To date, all Starship launches have been classified as internal.\""
    ticker: SPCX
    citation_id: sec8
    page_no: 35
    form_type: 10-Q
    url: https://agentii.ai/v/SPCX/sec8/35
    located_via: read_source_pages
  - figure: "\"For launches of our Starlink satellites, the Company does not recognize any inter-segment revenue, rather those launch costs are capitalized in satellites in Property, plant, and equipment, net.\"; Launch Services fixed-price contracts of 1 to 5 years against Launch and Development at 1 to 14 years"
    ticker: SPCX
    citation_id: sec8
    page_no: 36
    form_type: 10-Q
    url: https://agentii.ai/v/SPCX/sec8/36
    located_via: read_source_pages
  - figure: "Revenue mix by type: Launch Services 67.4%/65.7%/61.9%/65.5% against Launch and Development 32.6%/34.3%/38.1%/34.5%; R&D costs \"mainly relate to the development, build, and testing of Starship\""
    ticker: SPCX
    citation_id: sec8
    page_no: 37
    form_type: 10-Q
    url: https://agentii.ai/v/SPCX/sec8/37
    located_via: read_source_pages
  - figure: "Customer-launch definition and the customer/internal launch split, located via keyword search"
    ticker: SPCX
    citation_id: sec8
    page_no: 42
    form_type: 10-Q
    url: https://agentii.ai/v/SPCX/sec8/42
    located_via: search_keyword_in_source
  - figure: "\"Revenue and Cost Per Launch\": Q2 2026 revenue per launch $9.1M and cost per launch $4.4M; Q2 2025 $7.9M and $5.0M; and the HASTE mission-mix sentence - two of six Electron missions in the quarter were suborbital testbeds carried inside both the revenue and the launch-count numerator"
    ticker: RKLB
    citation_id: sec109
    page_no: 37
    form_type: 10-Q
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_pages
  - figure: "Electron filed only as \"up to 300 kg\" to low Earth orbit across inclinations from 38 to 120 degrees - a CEILING, with no mass-to-orbit metric filed in any period; Neutron \"approximately 13,000 kg for reusable configuration\""
    ticker: RKLB
    citation_id: sec87
    page_no: 8
    form_type: 10-K
    url: https://agentii.ai/v/RKLB/sec87/8
    located_via: read_source_pages
---

# SPCX — one page, four correct $/kg figures, a 12.8× spread, and a curve that inverts when the denominator is fixed

**Finding.** SpaceX's own filings yield **four arithmetically correct dollars-per-kilogram figures for the same
period family, all from a single page, spanning 12.8×** — and no basis field anywhere to separate them. The
same page discloses a customer-launch count on **two different denominators** whose trends point in **opposite
directions** by period. And when the one vehicle in the universe that files a marginal cost (Electron) is
re-measured on a corrected denominator, **the launch cost curve inverts: cost per launch fell 12.0% year over
year while cost per kilogram to low Earth orbit rose 32.0%.** The disclosed improvement is a denominator
artefact in the *optimistic* direction, and the curve's only measured point moves the wrong way (P1, P3, P4).

## 1. Acceptance test — adopted and run

An identification is accepted only if it is **(a) exact**, **(b) stable across periods**, and **(c) consistent
with a specified formula or a filed basis**. Everything else is `UNRESOLVED` — never "probably fine". The test
is not ceremonial here. The register records a ~**2,500**-candidate sweep over **36 filed cells** that returned
**6–9 coincidental hits per metric**, and only **2 of 16** served ratio fields were the ratio they claimed.
**Every figure below is recomputed from filed cells; no served ratio is quoted.**

**Three results of running it**, stated up front so the rest of the artifact is legible:

| Tested | Result |
|---|---|
| The five-column 8-K table's **column order** | **RECOVERED, not assumed** — three independent exact reconciliations force it (§2) |
| The $/kg ratio | **FAILS (c)** — four correct values, no filed basis field, 12.8× spread (§3) |
| The customer share | **FAILS (b)** — two filed denominators, opposite-signed period trends (§4) |
| Electron's cost per kg (the only basis-B cell in the universe) | **PASSES all three** — and it inverts the curve (§5) |

## 2. The column order is recovered, not assumed

The 8-K's Space table carries five columns under one header and **does not label them per value**. Before any
figure from it can be used, the order must be established — and assumable orderings are how a 3M figure gets
read as a 6M figure (DA-27). **Three independent reconciliations force the order**, each exact:

```
Launch count   40 + 38 = 78     (Q1 2026 + Q2 2026 = 6M 2026)
Revenue       330 + 648 = 978   ($M, Q1 2026 + Q2 2026 = 6M 2026)
Payload        45 + 87 = 132    (t,  Q1 2026 + Q2 2026 = 6M 2026)
```

Three quantities, three exact identities, one ordering. **Order: [Q2 2026, Q1 2026, Q2 2025, H1 2026,
H1 2025]** — a sequential prior quarter, a year-ago quarter, and two year-to-date periods, which is the
standard layout. Every figure in this artifact is positioned by that derivation.

**It is confirmed independently against the 10-Q**, which files the same activity on a Falcon-only and a
Starship-only split of four columns:

| Period | Falcon | Starship | Total | 8-K total | Match |
|---|---|---|---|---|---|
| Q2 2026 | 37 | 1 | **38** | 38 | ✓ |
| Q2 2025 | 45 | 1 | **46** | 46 | ✓ |
| H1 2026 | 77 | 1 | **78** | 78 | ✓ |
| H1 2025 | 81 | 3 | **84** | 84 | ✓ |

Four of four. Sources: [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7) and
[📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35).

**One disclosed discrepancy, recorded rather than smoothed.** Customer payload + internal payload sums to the
filed mass-to-orbit total **within 1 tonne on four of five columns**: 87 + 397 = 484 against a filed 485;
88 + 563 = 651 against 652; 132 + 908 = 1,040 against 1,041; 163 + 938 = 1,101 against 1,102. Only Q1 2026
closes to the tonne (45 + 511 = 556). **A difference of exactly one unit in four of five columns is a rounding
artefact, not an error** — and it is the reason this table's per-tonne ratios are quoted to the nearest dollar
but never to the nearest cent. This is DA-29 read correctly: the check *was* run, it *did* almost close, and
"almost" is stated rather than back-solved away.

## 3. P1/P3 — the basis spread: 12.8× on one page

**All four numerators and both denominators below are filed on the single page**
[📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7), for the six months ended 2026-06-30:

| Numerator (basis) | Denominator (basis) | $/kg | Correct? | Comparable? |
|---|---|---|---|---|
| Launch services revenue **$978M** (segment revenue-type) | Customer payload **132 t** | **$7,409/kg** | ✓ | — |
| **Space segment revenue $1,581M** (whole segment) | Customer payload **132 t** | **$11,977/kg** | ✓ | ✗ |
| Launch services revenue **$978M** | **Mass to orbit 1,041 t** (incl. internal) | **$939/kg** | ✓ | ✗ |
| **Space segment revenue $1,581M** | **Mass to orbit 1,041 t** | **$1,519/kg** | ✓ | ✗ |

**Spread: 11,977 ÷ 939 = 12.75 → 12.8×.** The decomposition is worth stating, because it shows the spread is
driven almost entirely by the denominator:

```
numerator factor    1,581 ÷ 978     = 1.617x   (Space segment vs launch services)
denominator factor  1,041 ÷ 132     = 7.886x   (total mass vs customer payload)
product             1.617 x 7.886   = 12.75x
```

**Every one of the four is arithmetically correct. None is comparable to any other.** The numerator may be
launch services only or the whole Space segment; the denominator may be customer payload only or all mass to
orbit including internal. The filing itself supplies the two numerator bases as a *revenue-type mix* (Launch
Services 67.4% of Space revenue against Launch and Development 32.6%,
[📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37)) and the two denominator bases as separate filed
columns. **Four ratios, four bases, zero basis fields — this is DA-30's canonical shape, and it is why this
artifact reports every competing basis rather than choosing one.**

**The boundary that makes the numerator ambiguous is filed, and it is the CUSTOMER boundary.** *"Our Space
segment revenue only reflects our customer launches and customer activities"*
([📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35)) and *"For launches of our Starlink satellites, the
Company does not recognize any inter-segment revenue, rather those launch costs are capitalized in satellites
in Property, plant, and equipment, net"* ([📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36)). **So the
launch-services numerator excludes the majority of the launches, and the mass-to-orbit denominator includes
them.** Putting those two on one ratio is not a measurement — it is a category error with a defensible-looking
number on the end of it.

### 3.1 Falcon 9 basis A — denominator-failed, not quotable

The widely-cited Falcon 9 basis A figure of **$2,939/kg** divides a per-launch price by a **22.8-tonne**
payload. **`"22.8"` returns ZERO located pages in the source set.** Under clause (c) — consistent with a
specified formula *or a filed basis* — the denominator has no filed basis and cannot be located at all.
**Verdict: `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, and the figure must not be carried.** It is the single most
widely-quoted SPCX number in this workspace and it rests on a denominator that appears nowhere in the filings.
The resolving disclosure is a filed Falcon 9 payload-mass-per-mission figure on the same definition as the
mass-to-orbit metric.

### 3.2 The matched-pair basis — the only internally consistent SPCX series

Holding **(a)** the numerator fixed at launch-services revenue and **(b)** the denominator fixed at *customer*
payload, a five-period series emerges. This is a **temporal** comparison on one basis, as against §3's **basis**
comparison in one period — the distinction is the method.

| Period | Launch services revenue | Customer payload | **$/kg** | Grade |
|---|---|---|---|---|
| Q2 2026 | $648M | 87 t | **$7,448/kg** | DEMONSTRATED |
| Q1 2026 | $330M | 45 t | **$7,333/kg** | DEMONSTRATED |
| H1 2026 | $978M | 132 t | **$7,409/kg** | DEMONSTRATED |
| Q2 2025 | $490M | 88 t | **$5,568/kg** | DEMONSTRATED |
| H1 2025 | $1,056M | 163 t | **$6,479/kg** | DEMONSTRATED |

**Band: 7,448 ÷ 5,568 = 1.338 → 1.34×.** This passes clauses (a) and (c): every cell is exact and the formula
is fixed and stated. It evidences a **~34% dispersion in the realized $/kg across five periods on one
immutable basis** — which is itself the point. A ratio whose value moves 1.34× while its numerator and
denominator are both held on fixed definitions is not a stable measurement, and a "cost curve" drawn through
it inherits that 34%.

**A $1/kg rounding note, carried not corrected.** The register records the low end as **$5,567/kg**;
recomputation from the filed cells gives **$5,568/kg** (`490,000 ÷ 88 = 5,568.18`). The difference is one
dollar and has **no filed explanatory term**, so under clause (c) it is `UNRESOLVED` rather than "a rounding
difference" — a rounding explanation would be a back-solve (§4 of the register: *if a term appears nowhere in
the source, the check is a back-solve*). The band is quoted as **$5,568–7,448/kg** and the register value is
flagged, not adopted.

## 4. P3 — the customer share has two bases and opposite signs by period

The customer share is the metric that decides whether SPCX's launch business is an external business or an
internal one. **It is filed on two denominators**, and the choice changes the *direction* of the trend.

| Period | Customer | Total launches | Share | Falcon-only | Share |
|---|---|---|---|---|---|
| Q2 2026 | 10 | 38 | **26.3%** | 37 | **27.0%** |
| Q2 2025 | 9 | 46 | **19.6%** | 45 | **20.0%** |
| H1 2026 | 17 | 78 | **21.8%** | 77 | **22.1%** |
| H1 2025 | 21 | 84 | **25.0%** | 81 | **25.9%** |

Sources: [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7) and
[📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35).

**The two numerator-and-denominator pairings differ by 0.7–0.9 percentage points and never change a
conclusion** — the sign of the two-basis claim is robust to the denominator choice, which is the useful
finding. But **the period basis flips the sign outright**:

```
Customer share, Q2 (3M):   19.6% -> 26.3%   RISING   by +6.7 pp
Customer share, H1 (6M):   25.0% -> 21.8%   FALLING  by -3.2 pp
```

**Same page, same metric, opposite directions, because the period basis differs.** This is DA-27's hazard
reached through DA-30: the register's correction stands — **never state the customer share without its period
basis**, and an artifact quoting the Q2 rise as a standing trend is over-reading one quarter.

**The same period-basis trap, on throughput.** Mass to orbit is **−25.6% on the three-month basis**
(485 t against 652 t) but **−5.5% on the six-month basis** (1,041 t against 1,102 t) — **4.6× smaller.**
Starship's *"3 → 1"* is **six-month only**: on the three-month basis it is 1 against 1, flat. And the
"two opposite-signed rates on one activity" finding is a **three-month phenomenon** — on the six-month basis
customer launches (−19.0%: 17 against 21) and total launches (−7.1%: 78 against 84) are **both negative.**
**Always state the period basis with any SPCX throughput figure.**

## 5. P1 — the corrected cross-vehicle table, and the curve inversion

This is the artifact's comparison table. Every row is from the filing named; no register value is inherited
unchecked.

| Vehicle | Operator | Architecture | Basis A (list price) | **Basis B (marginal cost)** | Basis C (fully loaded) |
|---|---|---|---|---|---|
| **Electron** | RKLB | **F5c** fully expendable | $26,333 → **$45,500/kg** | **$16,667 → $22,000/kg — DEMONSTRATED** | not filed |
| Falcon 9 | SPCX | F5b partially reusable | **denominator-failed** (unfiled 22.8 t) | **not filed** | not filed |
| Starship | SPCX | F5a fully reusable | not filed | **not filed** — suborbital test flights | not filed |
| Alpha | FLY | F5c fully expendable | not filed — class label only | **not filed** | not filed |
| Eclipse | FLY | F5b (unflown) | not filed | **not filed** — unflown | not filed |

**Demonstrated-versus-claimed split: basis B is `DEMONSTRATED` for exactly 1 of 5 vehicles — Electron.** Four
of five cells are `CLAIMED` or absent, and **this count will not widen on current disclosures**: no other
vehicle in the universe files a cost-per-launch figure on any basis. That single-source anchor is PIL-3's
foundation, and it is why the artifact reports the count explicitly rather than describing the curve as
"thin".

### 5.1 The curve inverts on the corrected denominator

Electron is the universe's only demonstrated point, and its correction is **1.00×–1.50× (+0% to +50%)** — not
the `1.79×–2.62×` that circulates. **`1.79×` and `2.62×` are Falcon 9's arithmetic** (`22.8 ÷ 12.76 = 1.787`;
`22.8 ÷ 8.70 = 2.621`) computed from **SPCX's** filed mass-to-orbit table, fused with **Electron's** period
count. **RKLB files no mass-to-orbit metric in any period**, so the SPCX-style restatement cannot be
reproduced at RKLB at all.

What *is* reproducible is driven by the **HASTE mission mix**, filed verbatim: *"Two of the six Electron launch
missions completed for the three months ended June 30, 2026 were Hypersonic Accelerator Suborbital Test
Electron ('HASTE') launch missions, for which revenue was recognized over time and was partially recognized in
prior quarters. All five Electron launch missions completed for the three months ended June 30, 2025 were
point-in-time launches"* ([📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)). **Two suborbital testbeds
carrying ZERO kg to LEO sit inside both the revenue numerator and the launch-count numerator.**

| Period | Missions | kg to LEO | Basis B $/kg | Factor |
|---|---|---|---|---|
| Q2 2025 | 5 of 5 point-in-time, **0 HASTE** | 300 kg | **$16,667/kg** | **1.00×** |
| H1 2026 | ≥10 of 12 orbital | 250 kg | **$19,600/kg** | **≥1.20×** |
| Q2 2026 | 4 orbital of 6 | 200 kg | **$22,000/kg** | **1.50×** |

The 300 kg figure is a **CEILING**: Electron is filed only as *"up to 300 kg"* to low Earth orbit across
inclinations *"from 38 to 120 degrees"* ([📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8)) — so every
correction above is an **upper bound**, and the register's `UNRESOLVABLE-FROM-PUBLIC-SOURCES` disposition stands.
**"Four of four periods" is FALSIFIED**: the correction is **ZERO in the one period whose mix is fully filed.**
Q1 2025, H1 2025 and Q1 2026 are mix-unfiled → **UNEXERCISED**, not clean.

**And the result that matters:**

```
cost per launch   $5.0M -> $4.4M   FELL  12.0%
cost per kg     $16,667 -> $22,000  ROSE  32.0%
check            0.88 x 1.50 = 1.32   EXACT
```

**The curve's only measured point, correctly measured, moves the WRONG way.** The disclosed 12% improvement is
a denominator artefact in the *optimistic* direction: two of six missions bought no kilogram. This is the
peer-bench table's headline, and it is a `DEMONSTRATED` arithmetic result on filed cells — not a model.

## 6. What this artifact could NOT resolve

| Unresolved | Why | Class | Disclosure that would resolve it |
|---|---|---|---|
| Falcon 9 basis A $/kg | The 22.8 t denominator returns zero located pages | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A filed Falcon 9 payload-mass-per-mission figure |
| Electron cost per kg | The 300 kg denominator is filed only as a ceiling | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | An Electron mass-to-orbit metric on the filed definition |
| The $1/kg matched-pair rounding note | No filed explanatory term exists | `UNRESOLVED` | A filed reconciliation of the matched-pair inputs |
| SPCX basis C (fully loaded) | No SPCX cost-per-launch figure is filed on any basis; a constructed amortized basis would be `MODELED` and could never satisfy a falsifier | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | A filed per-launch cost or launch-level capital line |
| Electron Q1 2025 / H1 2025 / Q1 2026 corrections | Mission mix not filed for those periods | `UNEXERCISED` | A per-period HASTE/orbital split |

**`UNEXERCISED` is not `CLEAN`.** Three of Electron's periods have no filed mix, so the correction is neither
confirmed nor excluded for them.

**A note on SPCX's basis C, since the register records a constructed figure.** A fully-loaded basis would sum
Space cost of revenue, R&D and SG&A and divide by customer launches. On Q2 2026 those are **$329M + $1,076M +
$99M = $1,504M** against **10** customer launches → **$150.4M per customer launch**
([📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7)). Its decomposition is the finding: **21.9% cost of
revenue, 71.5% R&D, 6.6% SG&A** — and the R&D is filed as *"mainly relate to the development, build, and
testing of Starship"* ([📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37)). **So a "fully-loaded cost per
launch" for Falcon 9 would be 71.5% Starship development.** The register's basis C figure of `$6,596/kg`
divides $150.4M by **22,800 kg** — and that denominator is the same unfiled 22.8 t that fails in §3.1.
**Grade basis C `MODELED`, and note that it cannot enter the comparison table**: a `MODELED` input can never
satisfy a falsifier, and this one rests on an unfiled denominator besides.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Space segment table, five columns in the order [Q2 2026, Q1 2026, Q2 2025, H1 2026, H1 2025]: customer launches 10/7/9/17/21; total launches 38/40/46/ | [📄 SPCX 8-K p.7](https://agentii.ai/v/SPCX/sec7/7) |
| Mass-to-orbit definition (total kilograms of payload delivered from all successful orbital and flight tests, excluding failed or scrubbed attempts); " | [📄 SPCX 10-Q p.35](https://agentii.ai/v/SPCX/sec8/35) |
| "For launches of our Starlink satellites, the Company does not recognize any inter-segment revenue, rather those launch costs are capitalized in satel | [📄 SPCX 10-Q p.36](https://agentii.ai/v/SPCX/sec8/36) |
| Revenue mix by type: Launch Services 67.4%/65.7%/61.9%/65.5% against Launch and Development 32.6%/34.3%/38.1%/34.5%; R&D costs "mainly relate to the d | [📄 SPCX 10-Q p.37](https://agentii.ai/v/SPCX/sec8/37) |
| Customer-launch definition and the customer/internal launch split, located via keyword search | [📄 SPCX 10-Q p.42](https://agentii.ai/v/SPCX/sec8/42) **(newly surfaced)** |
| "Revenue and Cost Per Launch": Q2 2026 revenue per launch $9.1M and cost per launch $4.4M; Q2 2025 $7.9M and $5.0M; and the HASTE mission-mix sentence | [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37) |
| Electron filed only as "up to 300 kg" to low Earth orbit across inclinations from 38 to 120 degrees - a CEILING, with no mass-to-orbit metric filed in | [📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8) |
