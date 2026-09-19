---
thesis_id: "002-evidence-validation"
pillar: PIL-2
ticker: BWXT
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-04"
    chosen_reading: "1 MW = continuous delivered electrical load at the payload, not nameplate and not including conversion losses. Every figure in §2 is per MW of PAYLOAD load. The heat-pump work is parasitic and is therefore NOT part of the 1 MW — it is added on top, which is the whole point of §2.3."
  - da_id: "DA-15"
    chosen_reading: "rejection temperature reported as an explicit variable, never a single assumed value. Extended here: the temperature must be reported WITH its source-side temperature T_c, because a lift ratio is only defined by a pair. A bare T_rad = 500 K is as uninterpretable as a bare radiator area."
  - da_id: "DA-16"
    chosen_reading: "all F2 derivations remain MODELED/DERIVED. No flown orbital radiator has been demonstrated by any listed issuer, and none is disclosed by BWXT — verified as a six-source null in §2.1."
  - da_id: "DA-23"
    chosen_reading: "operating_income component identity run in-line at two levels in each of two filings. All four close exactly. BWXT is clean on DA-23, but 001's own DA-23 clearance for BWXT is CIRCULAR and does not discharge the rule — corrected in §5.2."
  - da_id: "DA-25"
    chosen_reading: "normalised per-unit metrics. Radiator mass per MW and the COP penalty factor are both normalised and both basis-dependent; every competing basis is reported (two T_c values, two COP efficiencies) rather than collapsed to one, per §1c."
evidence_grade: DERIVED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Radiator areal density — null result. This is the Q2 2026 Note 1 segment-description page, read IN FULL: it is the page on which a radiator capability would appear if BWXT disclosed one, and it discloses none. Corroborated by a document-wide keyword search: 'radiator' returns zero occurrences in this filing, in the FY2025 10-K, in the Q1 FY2026 10-Q, and in all three FY2026 earnings calls. NOTE: the null is a search finding, so no page number can 'locate' it; the page cited is the verified content page, not a keyword hit."
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 10
    url: https://agentii.ai/v/BWXT/sec164/10
    located_via: read_source_pages
  - figure: "'we are the only commercial heavy nuclear component manufacturer in North America'; 'proprietary and sole-source valves, manifolds and fittings'; '3-D thermal-hydraulic engineering analysis' — the disclosed thermal capability is HYDRAULIC, not radiative"
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 10
    url: https://agentii.ai/v/BWXT/sec164/10
    located_via: read_source_pages
  - figure: "Advanced Reactor Design and Engineering product line: $147,138K FY2025 vs $203,808K FY2024 (−27.8%) — 4.6% of FY2025 revenue and falling; the closest filed proxy for space nuclear, and it is an UPPER bound because it mixes space and terrestrial"
    ticker: BWXT
    form_type: 10-K
    citation_id: sec126
    page_no: 94
    url: https://agentii.ai/v/BWXT/sec126/94
    located_via: read_source_pages
  - figure: "Advanced Reactor Design and Engineering $24,361K vs $38,717K in Q2 (−37.1%) and $52,577K vs $69,760K in H1 (−24.6%)"
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 21
    url: https://agentii.ai/v/BWXT/sec164/21
    located_via: read_source_pages
  - figure: "Operating income $114,136K closes exactly on the filed component identity: 901,625 revenues − 811,917 total costs and expenses + 24,428 equity in income of investees"
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 3
    url: https://agentii.ai/v/BWXT/sec164/3
    located_via: read_source_pages
  - figure: "Operating income $106,691K closes exactly: 860,217 − 775,091 + 21,565; and no gross-profit line exists on the face of the income statement"
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec162
    page_no: 3
    url: https://agentii.ai/v/BWXT/sec162/3
    located_via: read_source_pages
  - figure: "Segment operating income Q2 2026: Government Operations $105,678K vs $109,417K (−$3,739K, margin 17.6% vs 18.6%); Commercial Operations $24,332K vs $6,877K; unallocated corporate $(15,874)K; total $114,136K"
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 26
    url: https://agentii.ai/v/BWXT/sec164/26
    located_via: read_source_pages
  - figure: "'a decrease in revenues associated with our advanced technologies business' — the Government Operations segment's own stated driver for H1"
    ticker: BWXT
    form_type: 10-Q
    citation_id: sec164
    page_no: 27
    url: https://agentii.ai/v/BWXT/sec164/27
    located_via: read_source_pages
  - figure: "NASA, the Department of War and the DOE named as U.S. Government customers for advanced reactors for 'power and propulsion applications in the space and terrestrial domains'"
    ticker: BWXT
    form_type: 10-K
    citation_id: sec126
    page_no: 5
    url: https://agentii.ai/v/BWXT/sec126/5
    located_via: read_source_pages
  - figure: "'space nuclear propulsion' named in the patent portfolio; 'space nuclear power and propulsion' named in R&D activity; and the filed MAJORITY-of-R&D list omits space nuclear, naming medical radioisotopes, radiopharmaceuticals, additive and autonomous manufacturing, advanced reactors and nuclear fuel instead"
    ticker: BWXT
    form_type: 10-K
    citation_id: sec126
    page_no: 12
    url: https://agentii.ai/v/BWXT/sec126/12
    located_via: read_source_pages
  - figure: "'in the space domain, we continue to develop the technology required for nuclear thermal propulsion with NASA' — NTP is thrust, not the closed-cycle power architecture F2 requires"
    ticker: BWXT
    form_type: earnings_call_transcript
    citation_id: ect59
    page_no: 1
    url: https://agentii.ai/v/BWXT/ect59/1
    located_via: read_source_pages
  - figure: "Geveden: NASA interest in 'nuclear electric propulsion' and 'efficient surface power for a lunar based'; civil space nuclear is 'kind of a one-off market in the sense that you do one of those systems typically'; 'the more fertile ground for us is national security space'; and 'lower microreactor volumes'"
    ticker: BWXT
    form_type: earnings_call_transcript
    citation_id: ect60
    page_no: 2
    url: https://agentii.ai/v/BWXT/ect60/2
    located_via: read_source_pages
  - figure: "Golden Dome microreactors: 'we could play there as a fuel supplier ... but it's pretty undefined at this point for us'"
    ticker: BWXT
    form_type: earnings_call_transcript
    citation_id: ect60
    page_no: 4
    url: https://agentii.ai/v/BWXT/ect60/4
    located_via: read_source_pages
  - figure: "Backlog $8.4B +40% y/y, trailing-12-month book-to-bill 1.7x; Antares Mark-0 first advanced-reactor criticality on BWXT-supplied TRISO and HALEU; $21M DOE award; $17.5B DOE loan commitment; mPower licence with Applied Atomics; Core Power feasibility study"
    ticker: BWXT
    form_type: earnings_call_transcript
    citation_id: ect61
    page_no: 1
    url: https://agentii.ai/v/BWXT/ect61/1
    located_via: read_source_pages
  - figure: "Supply chain: 'zirconium tubes, large forgings ... we've been able to get those materials now'; labour 'challenging to find all the trades' with turnover 'mid-single digit or below 4%'; 'we've delivered 420 essentially small modular reactors ... over the last 50 years'"
    ticker: BWXT
    form_type: earnings_call_transcript
    citation_id: ect61
    page_no: 6
    url: https://agentii.ai/v/BWXT/ect61/6
    located_via: read_source_pages
  - figure: "Backlog $7,260.7M at 2025-12-31 (Government Operations $5,541M / 76%); competition named as Framatome, Cameco, Doosan and Westinghouse"
    ticker: BWXT
    form_type: 10-K
    citation_id: sec126
    page_no: 8
    url: https://agentii.ai/v/BWXT/sec126/8
    located_via: read_source_pages
---

# BWXT — F2 Constant Sourcing and the Attachability Test (PIL-2)

**Phase 2 question**: source the two constants F2 rests on — the **radiator areal
density** (001 admitted **8 kg/m² is a placeholder**) and the **heat-pump COP at
elevated rejection temperature** (001's F2 table is *rejection-side only*) — and re-derive
radiator mass per MW **with and without** the COP penalty.

**Headline**: **both constants are `UNRESOLVABLE-FROM-PUBLIC-SOURCES` as issuer values.**
`"radiator"` appears **zero times** across six BWXT sources. `"heat pump"` appears zero
times. `"microreactor"` appears zero times in the FY2025 10-K. That is a finding about
**disclosure quality**, and it is dispositive for the phase regardless of the physics.

**And the physics still moves.** The COP penalty can be derived from thermodynamics —
it needs no source — and it **breaks the ±50% acceptance test on its own**. F2's
headline **24× becomes 9.6×–16.8×**, and the corrected result is that **the heat pump
does not threaten nuclear's advantage; it threatens solar's.** Details in §2–§3.

---

## 1. What PIL-2 asked for, and what was found

| Constant | Sought from | Found | Disposition |
|---|---|---|---|
| Radiator areal density (kg/m²) | issuer disclosure, or peer-reviewed / flown hardware | **8 kg/m² remains a placeholder.** Zero sourced values in any BWXT filing or call | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (issuer) |
| Heat-pump COP at elevated T_rad | issuer disclosure, or peer-reviewed | **Not disclosed.** Derivable from thermodynamics with a stated T_c, but not *sourced* | **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** (issuer) |
| Heat-pump COP, generic engineering value | `peer_reviewed_literature_or_flown_hardware_disclosure` | Exists in public literature; **not reachable from this corpus** — no skill in the registry is a literature review | **`UNRESOLVABLE-FROM-PLATFORM`** (secondary) |

**Why the two dispositions are recorded separately.** The contract requires
`unresolvable_class` because "the two dispositions have different remedies." Here the
remedies genuinely differ, and conflating them would hide the actionable one:

- **Issuer disposition** (`UNRESOLVABLE-FROM-PUBLIC-SOURCES`): BWXT does not disclose a
  radiator or a heat pump. Remedy: **monitor disclosure.** Nothing else can be done —
  the company is not going to file a radiator spec it does not sell.
- **Platform disposition** (`UNRESOLVABLE-FROM-PLATFORM`): the *generic* constants exist
  in NASA technical reports, ISS thermal-control documentation and the peer-reviewed
  space-thermal literature. Remedy: **a literature/hardware review, which is outside
  every skill in this registry.** `secular-trends` reads securities filings; it cannot
  read a NASA TM. This is a scope limit of the toolchain, not of the world.

F2's falsifier specifies `source=peer_reviewed_literature_or_flown_hardware_disclosure`.
**That source class is not reachable by any skill in this registry.** The falsifier is
therefore not evaluable *as written* — which is itself a finding, and is why the
threshold is instead evaluated against the derivable component in §3.

## 2. The null result, at full strength

### 2.1 Six sources, zero occurrences

`search_keyword_in_source` for **`radiator`** across every BWXT source retrieved:

| Source | Form | Period | `radiator` hits |
|---|---|---|---|
| `sec126` | 10-K | FY2025 | **0** (one keyword hit at p.27 was inspected and **is false** — the page is EO 14372 / environmental compliance and contains no instance of the word) |
| `sec162` | 10-Q | Q1 FY2026 | **0** |
| `sec164` | 10-Q | Q2 FY2026 | **0** |
| `ect59` | transcript | Q4/FY2025 | **0** |
| `ect60` | transcript | Q1 FY2026 | **0** |
| `ect61` | transcript | Q2 FY2026 | **0** |

Also zero: **`heat pump`** (sec164), **`microreactor`** (sec126 — while the Q1 FY2026 call
discusses "lower microreactor volumes" [📄 BWXT ect60 p.2](https://agentii.ai/v/BWXT/ect60/2)),
**`zirconium`** (sec164), **`Pele`** (sec126).

**The `Pele` null is the one to note.** Project Pele's first TRISO core — Geveden's most
concrete funded nuclear milestone, delivered to Idaho National Laboratory — is stated on
the Q4 FY2025 earnings call [📄 BWXT ect59 p.1](https://agentii.ai/v/BWXT/ect59/1) and
**appears nowhere in the annual report filed the same day.** This is the identical
pattern Phase 1 established for SPCX's PUE: **a physical programme that exists in the
spoken record and is absent from the filed record.** The transcript layer is not
supplementary here; it is the only layer on which BWXT's nuclear activity is legible.

### 2.2 The disclosed thermal capability is the wrong heat-transfer mode

The single closest thing BWXT files to a thermal-engineering claim is this, in Note 1:

> "This segment also provides specialized engineering services that include structural
> component design, **3-D thermal-hydraulic engineering analysis**, weld and robotic
> process development, …" [📄 BWXT 10-Q p.10](https://agentii.ai/v/BWXT/sec164/10)

**`thermal-hydraulic` is convective and single-phase-fluid engineering.** It is the
correct capability for a terrestrial reactor coolant loop and for the "**heat
exchangers**" the same sentence list has BWXT fabricating. It is **not** the capability
for rejecting heat by radiation in vacuum, which is a `T⁴` surface-area problem with no
fluid and no convection term. BWXT's filed thermal capability describes the physics mode
F2 does *not* use.

This is treated at length in the companion supply-chain artifact.
**§1d / §6: the attachability question is answered here, and it is answered negatively.**

### 2.3 What is disclosed — and why it is the wrong architecture

BWXT's space-nuclear disclosures are real, citable, and consistently **NTP**:

| Disclosure | Source |
|---|---|
| NASA, the **Department of War** and the **DOE** named as U.S. Government customers for advanced reactors for "power and propulsion applications in the **space and terrestrial domains**" | [📄 BWXT 10-K p.5](https://agentii.ai/v/BWXT/sec126/5) |
| "**space nuclear propulsion**" named in the patent portfolio; "**space nuclear power and propulsion**" named in R&D activity | [📄 BWXT 10-K p.12](https://agentii.ai/v/BWXT/sec126/12) |
| "in the space domain, we continue to develop the technology required for **nuclear thermal propulsion with NASA**" | [📄 BWXT ect59 p.1](https://agentii.ai/v/BWXT/ect59/1) |
| Geveden: NASA interest in "**nuclear electric propulsion**" and "efficient surface power for a lunar bas[e]" | [📄 BWXT ect60 p.2](https://agentii.ai/v/BWXT/ect60/2) |

**The architecture mismatch is decisive and it is new to 002.** F2's nuclear escape hatch
requires a **closed-cycle power reactor whose waste heat is rejected by a radiator** —
i.e. nuclear *electric* power (NEP). BWXT's named, funded, NASA-facing programme is
**nuclear *thermal* propulsion (NTP)**, which produces thrust and **throws its heat out
the nozzle**. An NTP reactor has no radiator because it does not reject heat radiatively;
it dumps it in the exhaust.

**So BWXT's most-advanced named space programme is structurally incapable of delivering
F2's escape hatch.** NEP is mentioned exactly once, as a customer-interest item on a
call, with no programme, no award, no design and no revenue line attached. 001's verdict
was "physics claim stands; investment claim does not." 002 sharpens it:

> **The gap is not only that the space-nuclear business is small. It is that the named
> programme is the wrong physics.**

## 3. Re-derivation: F2 with the heat-pump COP penalty

001's F2 table is the **rejection side only** — it sizes the radiator for `Q_c` and never
asks where `Q_c` came from or what it costs to move it up the temperature gradient. 002
closes the loop.

### 3.1 The physics, stated exactly

Heat pump lifting `Q_c` from chip-junction `T_c` to radiator `T_r`. Energy balance
`Q_r = Q_c + W`, so with `COP ≡ Q_r/W`:

```
Q_r = Q_c / (1 − 1/COP)          f ≡ Q_r/Q_c = 1/(1 − 1/COP)
Carnot:  COP_C = T_r / (T_r − T_c)
```

**The pump work `W` is electrical, drawn from the bus, and becomes additional heat.** It
is therefore *not* part of the 1 MW of "delivered electrical load at the payload"
(DA-04) — it is parasitic load on top. That is why the factor `f` multiplies the power
system as well as the radiator.

`T_c = 350 K` is taken from 001's own stated junction range (~350–400 K); the low end is
used because it *minimises* pump work and is therefore **favourable** to the thesis. Two
COP efficiencies are carried, per §1c — Carnot (an unreachable bound) and 50 % of Carnot
(realistic for a 100–150 K lift):

| `T_r` | `COP_Carnot` | **f** (Carnot) | `COP` @ 50 % | **f** @ 50 % |
|---|---|---|---|---|
| 300 K | *no lift — `T_r < T_c`, passive* | **1.000** | — | **1.000** |
| 400 K | 8.00 | 1.143 | 4.00 | 1.333 |
| 450 K | 4.50 | 1.286 | 2.25 | 1.800 |
| **500 K** | **3.333** | **1.429** | **1.667** | **2.500** |

### 3.2 The corrected table — radiator mass per MW, with and without the pump

Radiator area from 001's confirmed arithmetic (`P = εσA(T_r⁴ − T_sink⁴)`, ε = 0.9,
T_sink = 3 K — 001's five rows reproduce exactly). Mass at the **unsourced 8 kg/m²
placeholder**, flagged as such:

| Configuration | Radiator m²/MW | **f** | Pumped m²/MW | Mass @ 8 kg/m² | vs 001 |
|---|---|---|---|---|---|
| **001's figure: nuclear + 500 K, no pump** | 313 | 1.000 | **313** | **2.50 t** | — |
| Nuclear + 500 K, Carnot pump | 313 | 1.4286 | **447** | **3.58 t** | **+42.9 %** |
| **Nuclear + 500 K, realistic pump** | 313 | 2.500 | **783** | **6.26 t** | **+150.0 %** |
| Nuclear + 450 K, realistic pump | 478 | 1.800 | **860** | 6.88 t | +174.9 % |
| Nuclear + 400 K, Carnot pump | 765 | 1.1429 | **874** | 6.99 t | +179.3 % |
| Nuclear + 300 K, **no pump needed** | 2,419 | 1.000 | **2,419** | 19.35 t | +672.8 % |

**Read the last row.** A **300 K radiator needs no heat pump at all** — the radiator sits
below the chip junction, so heat flows down the gradient passively. The pump is a
*penalty incurred by raising `T_r`, not by nuclear power*. This is the fact 001's
"rejection side only" note identified but did not price.

### 3.3 The comparison 001 actually made — and the effect it conflated

001's 24× compares **solar + 300 K** against **nuclear + 500 K**. That is not a
like-for-like comparison: it varies **two** things at once. Decomposed:

| Effect | Ratio | Whose is it? |
|---|---|---|
| **Array removal** (nuclear), at constant `T_r = 300 K`: 7,499 → 2,419 | **3.10×** | **This is the only effect nuclear uniquely provides** |
| **Rejection temperature** 300 → 500 K, no pump (001's figure, unphysical) | 7.72× | available to *any* source — but see below |
| Rejection temperature 300 → 500 K, **Carnot pump** | **5.41×** | |
| Rejection temperature 300 → 500 K, **realistic pump** | **3.09×** | |
| **001's combined claim** | 3.10 × 7.72 = **24.0×** | conflates the two |
| **002 corrected, Carnot pump** | 3.10 × 5.41 = **16.8×** | |
| **002 corrected, realistic pump** | 3.10 × 3.09 = **9.6×** | |

> **The 24× is not arithmetically wrong. It is a different comparison than it appears to
> be.** 001 presents 24× as what *nuclear* delivers; in fact **7.72× of it comes from the
> rejection temperature**, and only **3.10×** comes from removing the array. **The
> corrected nuclear advantage is 9.6×–16.8×.**

### 3.4 The finding that survives — and it points the other way from the criticism

Pricing the pump turns out to **strengthen the structural case for nuclear** while
**weakening the case for simply running solar hot.** The mechanism is a marginal-cost
asymmetry:

| System | Marginal cost of one extra watt of parasitic load |
|---|---|
| **Solar** | **~5,080 m² of array per MW** — the dominant area term in the entire envelope |
| **Nuclear** | **~313 m² of radiator per MW** — a 16× cheaper penalty |

At `T_r = 500 K` with a realistic pump (`f = 2.5`):

| Configuration | Array m²/MW | Radiator m²/MW | **Total m²/MW** | vs solar @ 300 K |
|---|---|---|---|---|
| Solar + 300 K, no pump (001's baseline) | 5,080 | 2,419 | **7,499** | 1.00× |
| Solar + 500 K, Carnot pump | 7,255 | 447 | **7,702** | **1.03× — WORSE** |
| **Solar + 500 K, realistic pump** | 12,700 | 783 | **13,483** | **1.80× — much WORSE** |
| Nuclear + 500 K, Carnot pump | 0 | 447 | **447** | 16.8× better |
| **Nuclear + 500 K, realistic pump** | 0 | 783 | **783** | **9.6× better** |

**For a solar-powered system, raising the rejection temperature is neutral at a Carnot
pump and strongly negative at a realistic one** — because every watt the heat pump eats
must be harvested by an array whose area is the dominant term. **Nuclear is what unlocks
the temperature effect**, not because a reactor runs hotter, but because it can absorb
the pump's power penalty at 1/16th the area cost.

That is a cleaner statement of why nuclear matters than "24×," and it is the version 003
should carry.

### 3.5 A further term 001's nuclear row omits — recorded, not relied on

The nuclear row also ignores the **reactor's own conversion waste heat**. A reactor
producing `P_e` electric at conversion efficiency `η` must radiate `(1−η)/η · P_e` as
well, and in vacuum that requires surface area. At `η = 0.30` and `f = 1.429`, per MW of
payload the nuclear system rejects ~4.76 MW total, not 1.43 MW — **~1,490 m²/MW** rather
than 447 m²/MW.

**This term is NOT used in the §3.3 band**, because `η` is not disclosed by any source and
introducing it would be exactly the unsourced-assumption padding this phase exists to
remove. It is recorded because it is structurally real, it moves the figure by 2–6×, and
it is **another reason the interval cannot close at ±50 %.** Phase 6 should carry it
explicitly or state why it is excluded.

## 4. Acceptance test — the falsifier FIRES

PIL-2's falsifier: `metric=f2_radiator_mass_per_MW_uncertainty_band_pct`, `threshold=0.50`,
`source=peer_reviewed_literature_or_flown_hardware_disclosure`, `op=>`.

**Verdict: the threshold is breached. On two independent grounds, either sufficient.**

**Ground 1 — no sourced value exists, so no interval can be constructed.**
`source=peer_reviewed_literature_or_flown_hardware_disclosure` names a source class
**unreachable by any skill in this registry**. With zero sourced inputs, the band is
**unbounded**; ±50 % is a floor, not a ceiling. This ground is convention-independent and
decisive on its own.

**Ground 2 — the derivable component alone straddles the threshold.**
The COP penalty needs no source; it is thermodynamics plus a stated `T_c`. It moves the
radiator mass from **2.50 t to 3.58 t–6.26 t**:

| Measure | Value | Test |
|---|---|---|
| Endpoints vs 001's stated point estimate (2.50 t) | **+42.9 % … +150.0 %** | **upper end is 3× the threshold; the band straddles it** |
| Spread, max/min | **1.75×** | a 75 % spread |
| Endpoints vs band midpoint (4.95 t) | ±27 % | *does not* breach under this convention |
| Radiator mass/m² axis, if `η` is included (§3.5) | 1.8 t – 14.3 t | ~8× spread |

**Convention is disclosed rather than selected.** The midpoint convention would give
±27 %, below threshold. But the metric as specified is the uncertainty band on F2's
**radiator mass per MW** — a figure 001 states as **2.5 t** — and against *that* figure
the band is +42.9 %/+150.0 %. **Reporting the convention that fails while suppressing the
one that passes would be the inversion of §1c.** Both are shown; Ground 1 decides it
regardless.

> ### ⚠️ CONSEQUENCE — REQUIRED NOTIFICATION
>
> Per spec §6: *"If the band exceeds ±50 %, F2 downgrades to a qualitative bound and
> **003 and 009 must be notified**."*
>
> **The band exceeds ±50 %. F2 downgrades to a qualitative bound.**
>
> **003 must be notified** — it frames the compute narrative on F2.
> **009 must be notified** — it sells into that narrative.
>
> The downgraded form 003/009 may rely on: *"A nuclear source removes the solar array
> entirely and permits a hotter radiator, reducing total deployed area per MW by roughly
> an order of magnitude (9.6×–16.8×), not 24×. The exact figure is not quantifiable from
> public filings because no issuer discloses radiator areal density or heat-pump COP."*
>
> **This is a restatement, not a refutation.** The direction of F2 is unchanged and
> nuclear's structural role is *reinforced* (§3.4). What is removed is the entitlement to
> three significant figures.

## 5. The adversarial test: is there a funded programme?

The task required this be tested rather than accepted. 001's own three reversal
conditions, checked individually.

### 5.1 Condition 2 — R&D step-change: **NOT MET, and the instrument is basis-mismatched**

001's instrument was R&D/revenue: **BWXT 0.5 %** vs FLY 60.8 % and RKLB 35.2 %
[inherited from `BWXT/2026-09-18_1239_secular-trends_methodology.md` §1; **cited, not
re-derived**].

**002 finding: the instrument measures a different quantity at BWXT than at its
comparators.** BWXT's XBRL `ResearchAndDevelopmentExpensePolicy` states that
company-funded R&D is expensed in the `Research and development costs` line while
**customer-sponsored R&D is booked as a contract cost inside `Cost of operations`**:

> "Amounts expensed as incurred for **company-funded** research and development projects
> are included in research and development costs. Costs related to contracts with
> customers for **customer-sponsored** research and development projects are included as
> a contract cost in **Cost of operations** …"

**Therefore the $4.1 M line 001 used is company-funded IR&D only.** BWXT's
government-funded development — NASA NTP, DOE, naval — sits in cost of operations and is
**structurally invisible** in the ratio 001 built. An R&D-intensity comparison that puts
BWXT's *company-funded* R&D beside a comparator's *total* R&D is not like-for-like.

**Honest scope limit, recorded rather than glossed**: this is **verified on BWXT's side
only**. RKLB's and FLY's R&D recognition policies were **not** verified in this artifact
(one filing read = BWXT; the comparators are out of scope). So the table is
**confirmed-mismatched on one side and unverified on the other**. It cannot be closed
here, and it should not be cited as a clean cross-issuer comparison until it is.

**But 001's verdict survives on a better instrument.** The R&D ratio was the weak
evidence. The strong evidence is a filed revenue line — **Advanced Reactor Design and
Engineering**, the only product line that could contain space-nuclear revenue:

| Advanced Reactor Design and Engineering | Value | Change |
|---|---|---|
| FY2025 | **$147,138 K** | **−27.8 %** vs $203,808 K (FY2024) |
| FY2024 | $203,808 K | +41.1 % vs $144,464 K (FY2023) |
| FY2023 | $144,464 K | — |
| Q2 2026 | **$24,361 K** | **−37.1 %** vs $38,717 K |
| H1 2026 | **$52,577 K** | **−24.6 %** vs $69,760 K |

[📄 BWXT 10-K p.94](https://agentii.ai/v/BWXT/sec126/94) ·
[📄 BWXT 10-Q p.21](https://agentii.ai/v/BWXT/sec164/21)

At FY2025 that is **4.6 % of total revenue** — and **it is an upper bound, not a
measurement**, because the line explicitly mixes space and terrestrial advanced-reactor
work. The space-nuclear share is strictly smaller. Management confirms the direction in
the segment discussion: Government Operations H1 growth was partly offset by
"**a decrease in revenues associated with our advanced technologies business**"
[📄 BWXT 10-Q p.27](https://agentii.ai/v/BWXT/sec164/27).

> **Space-nuclear revenue is bounded above by a line that is 4.6 % of the company and
> shrinking at −25 % to −37 % year over year.** 001's conclusion holds; its instrument
> did not deserve to carry it.

### 5.2 Condition 3 — a named programme with a government customer: **PARTIALLY MET**

| Requirement | Status | Evidence |
|---|---|---|
| Government customer named | **MET** | NASA, Department of War, DOE [📄 10-K p.5](https://agentii.ai/v/BWXT/sec126/5) |
| Funded activity | **MET** | NTP development with NASA [📄 ect59 p.1](https://agentii.ai/v/BWXT/ect59/1); Antares Mark-0 first criticality on BWXT TRISO/HALEU; $21 M DOE award; $17.5 B DOE loan commitment; Golden Dome/SHIELD awardee [📄 ect61 p.1](https://agentii.ai/v/BWXT/ect61/1) |
| **Named space reactor DESIGN** | **NOT MET** | Every named design is terrestrial: Project Pele (DOE, transportable), Antares (Kairos), mPower (licensed to Applied Atomics), Core Power floating platforms. **No space reactor is named in any filing or call.** |
| **Correct architecture (NEP)** | **NOT MET** | The funded, named NASA programme is **NTP** — thrust, no radiator (§2.3) |
| Disclosed space-nuclear revenue line | **NOT MET** | Absent from both segments and all five product/service lines |

**And the demand-side read is worse than the supply-side read.** Geveden on civil space
nuclear:

> "It's kind of a **one-off market in the sense that you do one of those systems
> typically**. I think probably **the more fertile ground for us is national security
> space**." [📄 BWXT ect60 p.2](https://agentii.ai/v/BWXT/ect60/2)

The CEO is telling you the civil space-nuclear TAM is **one unit per programme**. That is
not a secular trend; it is a bespoke-procurement market. The adjacent growth vector he
names — Golden Dome microreactors — he immediately qualifies: "**it's pretty undefined at
this point for us**" [📄 BWXT ect60 p.4](https://agentii.ai/v/BWXT/ect60/4), while
microreactor volumes are already **falling** [📄 ect60 p.2](https://agentii.ai/v/BWXT/ect60/2).

**Attachability verdict: NOT ATTACHED.** There is a real, funded, government-customer
nuclear franchise — 001 was right that it exists and right that it is not a space
business. 002 adds that **the one space programme with a named customer is the wrong
physics**, that **space-nuclear revenue is bounded above by a shrinking 4.6 % line**, and
that **the CEO describes the civil space market as one-off**.

## 6. DA-23 — BWXT clean, but 001's clearance is circular

**002's independent verification** (component identity, in-line, per the contract rule):

```
Q2 2026 (sec164 p.3):  901,625 − 811,917 + 24,428 = 114,136  ✓ exact
  total costs and expenses close: 699,320 + 4,167 + (2) + 108,432 = 811,917  ✓ exact
Q1 2026 (sec162 p.3):  860,217 − 775,091 + 21,565 = 106,691  ✓ exact
  total costs and expenses close: 662,849 + 4,100 + 125 + 108,017 = 775,091  ✓ exact
```

Cross-checked against XBRL `OperatingIncomeLoss` (Q1 2026 = $106,691 K; Q1 2025 =
$96,630 K; Q2 2025 = $102,424 K; H1 2025 = $199,054 K; FY2025 = $404,459 K) and against
the segment table [📄 BWXT 10-Q p.26](https://agentii.ai/v/BWXT/sec164/26). **Filed and
XBRL agree on sign. BWXT is profitable and clean on DA-23.**

Three corrections to 001's §4, recorded per the frozen-001 policy (001 is not rewritten;
corrections are recorded here and cited by location):

1. **BWXT has no gross-profit line.** The face of the income statement runs Revenues →
   Costs and Expenses → Total Costs and Expenses → Equity in Income of Investees →
   Operating Income. 001's "gross profit $197.4 M" is **derived** (860,217 − 662,849 =
   197,368) and was presented as a filed figure with no derivation shown. It is a valid
   derived subtotal; it is not a disclosed one.
2. **§4's "reconciles: gross profit less operating expenses $90.7 M" is circular.**
   Actual operating expenses are 4,100 + 125 + 108,017 = **$112.2 M**, and equity income
   **+$21.6 M** must be added back: 197.4 − 112.2 + 21.6 = 106.7. 001's "$90.7 M" is
   112.2 − 21.6 — **back-solved from the answer it was meant to verify.** A check
   constructed from its own output cannot detect a sign error. **The verdict (BWXT clean)
   is correct; the instrument did not discharge DA-23.**
3. **§4 used `EPS × shares`**, which the contract explicitly rules inadmissible as a sign
   test. 001 was written under `constitution_pin 1.2.0`; this artifact does not repeat it.

**Structural consequence for PIL-3.** BWXT files **no quarterly gross-profit line**, so
the gross-profit bound — one of PIL-3's three detectors — **cannot run on BWXT**. Same
class as the LUNR finding. PIL-3 must either use the full cost-stack identity (as used
here) or record BWXT as a detector-coverage gap.

## 7. Competing bases reported, not collapsed (§1c)

| Basis | Value | Note |
|---|---|---|
| Radiator areal density | 8 kg/m² (`MODELED`, 001) | **unsourced placeholder**; no competing issuer value exists to report |
| Heat-pump COP efficiency | Carnot (f = 1.429) | unreachable upper bound |
| Heat-pump COP efficiency | 50 % of Carnot (f = 2.500) | realistic for a 100–150 K lift |
| `T_c` (junction) | 350 K | 001's stated range low end — favourable to the thesis |
| `T_c` (junction) | 400 K | 001's stated range high end → f falls to 1.25 (Carnot) |
| Nuclear advantage | 24× (001) / 16.8× (Carnot) / 9.6× (realistic) | **all three reported** |
| Advanced-reactor revenue | $147.1 M FY2025 = 4.6 % | **upper bound**; mixes space and terrestrial |
| R&D intensity | 0.5 % | **company-funded only** (§5.1) |

## 8. What could NOT be verified

1. **Any radiator areal density from any source.** Zero occurrences, six sources.
2. **Any heat-pump COP or heat-pump mention at all.** Zero occurrences.
3. **A named space reactor design.** None exists in the corpus.
4. **RKLB's and FLY's R&D recognition policies** — out of scope (one filing read = BWXT).
   The §5.1 basis mismatch is confirmed on BWXT's side only.
5. **Reactor conversion efficiency `η`** — not disclosed; §3.5's term is recorded, not used.
6. **The generic engineering constants themselves** — exist in NASA/peer-reviewed
   literature, unreachable from this corpus (`UNRESOLVABLE-FROM-PLATFORM`).

## Carry-forwards

1. **F2 downgrades to a qualitative bound. Notify 003 and 009.** This is the spec's
   binding consequence and it is triggered (§4).
2. **003 should carry 9.6×–16.8×, not 24×**, and should carry the §3.4 mechanism — the
   heat pump penalises *solar* 16× harder than *nuclear*, which is why nuclear unlocks the
   temperature effect. That framing is stronger than the number it replaces.
3. **The NTP/NEP architecture mismatch is a new falsifier-adjacent finding** and should
   be promoted into the validation ledger: BWXT's named space programme cannot deliver
   F2's escape hatch.
4. **Phase 6 must close the §3.5 reactor-waste-heat term or state why it is excluded.**
5. **The `Pele` null (transcript-only milestone) joins the Phase 1 PUE finding** as the
   second instance of a physical parameter present in the call and absent from the
   filing. Name the pattern once.
6. **A literature/hardware review is required to source F2's constants**, and **no skill
   in this registry can execute it.** That is a toolchain gap, not a research finding, and
   it should be logged as such.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| Radiator areal density — null result. This is the Q2 2026 Note 1 segment-description page, read IN FULL: it is the page on which a radiator capability | [📄 BWXT 10-Q p.10](https://agentii.ai/v/BWXT/sec164/10) |
| 'we are the only commercial heavy nuclear component manufacturer in North America'; 'proprietary and sole-source valves, manifolds and fittings'; '3-D | [📄 BWXT 10-Q p.10](https://agentii.ai/v/BWXT/sec164/10) |
| Advanced Reactor Design and Engineering product line: $147,138K FY2025 vs $203,808K FY2024 (−27.8%) — 4.6% of FY2025 revenue and falling; the closest  | [📄 BWXT 10-K p.94](https://agentii.ai/v/BWXT/sec126/94) |
| Advanced Reactor Design and Engineering $24,361K vs $38,717K in Q2 (−37.1%) and $52,577K vs $69,760K in H1 (−24.6%) | [📄 BWXT 10-Q p.21](https://agentii.ai/v/BWXT/sec164/21) |
| Operating income $114,136K closes exactly on the filed component identity: 901,625 revenues − 811,917 total costs and expenses + 24,428 equity in inco | [📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec164/3) **(newly surfaced)** |
| Operating income $106,691K closes exactly: 860,217 − 775,091 + 21,565; and no gross-profit line exists on the face of the income statement | [📄 BWXT 10-Q p.3](https://agentii.ai/v/BWXT/sec162/3) **(newly surfaced)** |
| Segment operating income Q2 2026: Government Operations $105,678K vs $109,417K (−$3,739K, margin 17.6% vs 18.6%); Commercial Operations $24,332K vs $6 | [📄 BWXT 10-Q p.26](https://agentii.ai/v/BWXT/sec164/26) |
| 'a decrease in revenues associated with our advanced technologies business' — the Government Operations segment's own stated driver for H1 | [📄 BWXT 10-Q p.27](https://agentii.ai/v/BWXT/sec164/27) |
| NASA, the Department of War and the DOE named as U.S. Government customers for advanced reactors for 'power and propulsion applications in the space a | [📄 BWXT 10-K p.5](https://agentii.ai/v/BWXT/sec126/5) |
| 'space nuclear propulsion' named in the patent portfolio; 'space nuclear power and propulsion' named in R&D activity; and the filed MAJORITY-of-R&D li | [📄 BWXT 10-K p.12](https://agentii.ai/v/BWXT/sec126/12) |
| 'in the space domain, we continue to develop the technology required for nuclear thermal propulsion with NASA' — NTP is thrust, not the closed-cycle p | [📄 BWXT earnings call transcript p.1](https://agentii.ai/v/BWXT/ect59/1) |
| Geveden: NASA interest in 'nuclear electric propulsion' and 'efficient surface power for a lunar based'; civil space nuclear is 'kind of a one-off mar | [📄 BWXT earnings call transcript p.2](https://agentii.ai/v/BWXT/ect60/2) |
| Golden Dome microreactors: 'we could play there as a fuel supplier ... but it's pretty undefined at this point for us' | [📄 BWXT earnings call transcript p.4](https://agentii.ai/v/BWXT/ect60/4) |
| Backlog $8.4B +40% y/y, trailing-12-month book-to-bill 1.7x; Antares Mark-0 first advanced-reactor criticality on BWXT-supplied TRISO and HALEU; $21M  | [📄 BWXT earnings call transcript p.1](https://agentii.ai/v/BWXT/ect61/1) |
| Supply chain: 'zirconium tubes, large forgings ... we've been able to get those materials now'; labour 'challenging to find all the trades' with turno | [📄 BWXT earnings call transcript p.6](https://agentii.ai/v/BWXT/ect61/6) **(newly surfaced)** |
| Backlog $7,260.7M at 2025-12-31 (Government Operations $5,541M / 76%); competition named as Framatome, Cameco, Doosan and Westinghouse | [📄 BWXT 10-K p.8](https://agentii.ai/v/BWXT/sec126/8) **(newly surfaced)** |
