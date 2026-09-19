---
thesis_id: "002-evidence-validation"
pillar: PIL-1
ticker: RKLB
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.4.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "basis A (price) and basis B (marginal cost) BOTH reported; this artifact adds no new basis and re-prices nothing"
  - da_id: "DA-02"
    chosen_reading: "LEO. The filed figure is a CAPACITY CEILING ('up to 300 kg to low Earth orbit'), not a delivered mass. The ceiling resolves; the delivered-mass denominator does not."
  - da_id: "DA-06"
    chosen_reading: "RKLB DOES distinguish price from cost — two separately defined metrics in adjacent paragraphs. Verified by reading both definitions."
  - da_id: "DA-07"
    chosen_reading: "RKLB files NO mass-to-orbit metric. Launch COUNTS only. Cross-issuer mass comparisons remain invalid."
  - da_id: "DA-08"
    chosen_reading: "RKLB's count basis = ALL Electron-family vehicles (Electron + suborbital HASTE), orbital and suborbital, no internal-payload exclusion. NOT comparable to SPCX's customer-launch basis without restatement."
  - da_id: "DA-23"
    chosen_reading: "operating_income component identity run in-line (gross profit − opex). RKLB IS flipped; the flip is now confirmed by the platform's own calculation tree, not only by arithmetic."
  - da_id: "DA-25"
    chosen_reading: "normalised per-unit metrics. Both bases reported side by side: disclosed revenue/cost per launch AND the audited segment table. Neither recomputed as authoritative."
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: false
denominator_residual: "UNRESOLVABLE-FROM-PUBLIC-SOURCES"
citations:
  - figure: "Electron — 'spacecraft up to 300 kg' to LEO (the PIL-1 denominator, FILED)"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 7
    url: https://agentii.ai/v/RKLB/sec87/7
    located_via: search_keyword_in_source
  - figure: "Electron — 'capable of deploying spacecraft of up to 300 kg to low Earth orbit'; inclinations 38–120°; lift-off mass ~14,000 kg; 18 m × 1.2 m"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 8
    url: https://agentii.ai/v/RKLB/sec87/8
    located_via: search_keyword_in_source
  - figure: "Neutron — 'payloads up to 13,000 kg for reusable configuration launches to low Earth orbit' (repeated verbatim across four filings)"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 7
    url: https://agentii.ai/v/RKLB/sec87/7
    located_via: search_keyword_in_source
  - figure: "Launch opportunity capacity — 'up to 120 launch opportunities every year from LC-1' + 'up to 8 launch opportunities every year from LC-2'"
    ticker: RKLB
    form_type: 10-K
    citation_id: sec87
    page_no: 7
    url: https://agentii.ai/v/RKLB/sec87/7
    located_via: search_keyword_in_source
  - figure: "Electron launch cadence — built ~14 (2024), ~24 (2025), ~11 (H1 2026); launched 16 (2024), 21 (2025), 12 (H1 2026)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 37
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_outline
  - figure: "Revenue/cost per launch — Q2 2026 $9.1M/$4.4M; Q2 2025 $7.9M/$5.0M; H1 2026 $9.2M/$4.9M; H1 2025 $7.5M/$5.3M — with both definitions stated"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 37
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_outline
  - figure: "'Two of the six Electron launch missions completed for the three months ended June 30, 2026 were HASTE launch missions' — the suborbital-contamination disclosure (DA-08)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 37
    url: https://agentii.ai/v/RKLB/sec109/37
    located_via: read_source_outline
  - figure: "Backlog $2,355.9M at 2026-06-30, of which $1,415.8M space systems and $940.2M launch services (from $1,847.3M at 2025-12-31)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 38
    url: https://agentii.ai/v/RKLB/sec109/38
    located_via: search_keyword_in_source
  - figure: "Audited Launch Services segment — Q2 2026 revenue $44,586k, cost of revenue $25,476k, gross profit $19,110k; H1 2026 $108,249k/$60,916k/$47,333k"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 32
    url: https://agentii.ai/v/RKLB/sec109/32
    located_via: read_source_outline
  - figure: "Consolidated statements of operations, primary — Q2 2026 gross profit $84,576k, total operating expenses $142,090k, OPERATING LOSS $(57,514)k, net loss $(49,258)k, EPS $(0.08); Q2 2025 operating loss $(59,639)k (the DA-23 flip, both periods exact)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 6
    url: https://agentii.ai/v/RKLB/sec109/6
    located_via: read_source_pages
  - figure: "Consolidated H1 2026 — gross profit $161,069k − total operating expenses $274,552k = operating loss $(113,483)k as filed (DA-23 component identity)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 42
    url: https://agentii.ai/v/RKLB/sec109/42
    located_via: search_keyword_in_source
  - figure: "'12 Electron launch missions completed for the six months ended June 30, 2026, versus 10 launch missions completed in the six months ended June 30, 2025'"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 42
    url: https://agentii.ai/v/RKLB/sec109/42
    located_via: search_keyword_in_source
  - figure: "Q1 2026 cadence — built ~5, launched 6; revenue/cost per launch $9.3M/$5.4M vs $7.1M/$5.7M (Q1 2025)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec104
    page_no: 31
    url: https://agentii.ai/v/RKLB/sec104/31
    located_via: search_keyword_in_source
  - figure: "Neutron schedule risk — 'target delivery of Neutron to the launch pad in Q4 2026'; 'the window for an end-of-year launch date is narrowing'"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 35
    url: https://agentii.ai/v/RKLB/sec109/35
    located_via: search_keyword_in_source
  - figure: "'We have successfully launched Electron 87 times … , including suborbital launches, through June 30, 2026' — the cumulative count runs on a mixed orbital+suborbital basis"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 36
    url: https://agentii.ai/v/RKLB/sec109/36
    located_via: search_keyword_in_source
  - figure: "Neutron 13,000 kg reusable-configuration to LEO, restated in the Q1 2026 10-Q; Electron 81 missions through 2026-03-31"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec104
    page_no: 29
    url: https://agentii.ai/v/RKLB/sec104/29
    located_via: search_keyword_in_source
  - figure: "'87 successful missions … including suborbital launches' — proof the cumulative Electron count is a mixed orbital+suborbital basis (DA-08)"
    ticker: RKLB
    form_type: 10-Q
    citation_id: sec109
    page_no: 34
    url: https://agentii.ai/v/RKLB/sec109/34
    located_via: search_keyword_in_source
---

# RKLB — Operational KPI Baseline (Q2 2026) — the denominator, from the operational side

Source filings: **FY2025 10-K** (accession `0001819994-26-000013`, filed 2026-02-26,
`sec87`) · **Q1 2026 10-Q** (`0001819994-26-000028`, filed 2026-05-07, `sec104`) ·
**Q2 2026 10-Q** (`0001819994-26-000062`, filed 2026-08-10, `sec109`). All three
resolved via `search_sec_filings`; every page cited below was located by tool and then
**read in full** — none is guessed.

RKLB is a **P11 deal security** (acquiring Iridium, announced 2026-06-29, close expected
2027). All figures are **pre-merger standalone basis**.

---

## Headline: PIL-1's Electron denominator RESOLVES — and its 003-owned Neutron hole closes with it

Two findings, one of which 001 explicitly asked for and could not find.

1. **Electron's 300 kg is FILED.** 001 carried it as `CLAIMED` and wrote *"a filed source
   should be sought."* It is filed, in the issuer's own annual report, and the filed value
   is **exactly 300 kg**. The denominator moves **0.00%**, against a ±15% threshold.
2. **Neutron's payload is FILED at ~13,000 kg** — a figure **001 never recorded at all**,
   and which the task notes 003's Pillar 4 depends on. It appears in **four** filings.

**PIL-1's falsifier does not fire.** But — and this is the part that matters — the
denominator that resolved is the **capacity ceiling**, not the mass actually delivered.
The residual is recorded in §2 and is **one-signed**, which is the strongest form the
answer could take.

---

## 1. Electron's payload to LEO, as filed

| Vehicle | Filed payload to LEO | Where | As of |
|---|---|---|---|
| **Electron** | **up to 300 kg** | `sec87` p.7 ("spacecraft up to 300 kg"); `sec87` p.8 | FY2025 |
| **Neutron** | **~13,000 kg, reusable configuration** | `sec87` p.7, p.8; `sec104` p.29; `sec109` p.34 | FY2025 → Q2 2026 |

The Electron figure is stated twice in the 10-K in two different constructions, which is
why it is quotable rather than incidental:

> *"We currently provide reliable and responsive launch services into low earth orbit on
> Electron for spacecraft **up to 300 kg**."*
> — [📄 RKLB 10-K p.7](https://agentii.ai/v/RKLB/sec87/7)

> *"It is capable of deploying **spacecraft of up to 300 kg to low Earth orbit** across a
> wide range of orbital inclinations from 38 to 120 degrees…"*
> — [📄 RKLB 10-K p.8](https://agentii.ai/v/RKLB/sec87/8)

A keyword sweep for `300 kg` across the 10-K returns **exactly two pages** — p.7 and p.8 —
and **no competing payload figure anywhere in the document**. There is no second number
to dispute.

### The ±15% test

| Step | Value |
|---|---|
| 001's denominator (`CLAIMED`, press) | 300 kg |
| Filed denominator (`sec87` p.7–8) | **300 kg** |
| **Movement** | **0.00%** |
| PIL-1 threshold | 0.15 |
| **Falsifier** | **DOES NOT FIRE** |

Because the demonstrated $/kg is inverse-linear in the denominator and the denominator is
unchanged, the inherited values carry through **unaltered** — cited, not recomputed, per
§0:

> **$14,667/kg** (basis B, marginal cost) and **$30,333/kg** (basis A, revenue per launch)
> — 001's `RKLB/…_unit-economics_methodology.md`. **Electron is 10.3× Falcon 9 per kg on
> basis A** (same artifact).

Basis A and basis B are reported together per the §1c standing rule
(`no_single_basis_collapse`); this artifact adds no third basis and re-prices nothing.

**What the resolution is and is not.** Per spec §1b, an admissible source is *"a
government manifest, a filed document, or a customer contract"*, and the P1 claim text
names *"the issuer's own SEC disclosure"* explicitly. A 10-K is a filed document, so the
figure is admissible. It is **not, however, independent of the issuer** — it is Rocket
Lab's own assertion about Rocket Lab's own vehicle, corroborated by no second party in the
document. It has moved evidence *class* (`CLAIMED` → filed, and stated twice across two
constructions) without acquiring an independent *witness*. **The 300 kg should be graded
`DEMONSTRATED` as a filed figure and `CLAIMED` as a physical capability** — and PIL-1's
band should be quoted as *"filed at 300 kg, self-asserted by issuer"*, because the
strongest available resolution (a NASA launch manifest, a range safety document, or a
customer contract stating payload mass) is not on the platform.

---

## 2. The residual hole: capacity is filed, **delivered mass is not** — and it is one-signed

This is the finding that survives after the denominator "resolves", and it is worth
stating precisely, because it is where PIL-1's remaining ±15% actually lives.

**The filed figure is a ceiling** — *"up to 300 kg"*, *"capable of deploying … up to
300 kg"*. Two independent reasons the operative denominator sits **below** 300 kg, both
filed:

1. **Utilisation.** A dedicated smallsat launch rarely cubes out at the vehicle's maximum
   capacity. **RKLB discloses no mass-to-orbit metric** — verified by keyword sweep across
   the 10-K and the Q2 10-Q. Contrast SPCX, which files mass to orbit as a key business
   metric. So the ratio of delivered mass to capacity is **not obtainable from RKLB's
   filings at all**.
2. **Suborbital missions are inside the launch count.** The count and the per-launch
   metric both include HASTE, which delivers **nothing to LEO**. See §4.

**Direction of the error.** Both effects push the true $/kg-to-LEO **above** 001's
$14,667/kg — a lighter average payload, or a denominator of zero for a suborbital mission,
raises cost per kg delivered. So:

> **001's $14,667/kg (basis B) and $30,333/kg (basis A) are FLOORS, not central
> estimates. The unquantified residual error is ONE-SIGNED — it can only raise them.**

That is the opposite of the failure mode PIL-1 was written to catch. A denominator error
that moved the answer *down* would threaten the pillar's $1,000/kg conclusion; a
one-signed upward error **strengthens** it. The conclusion is safe by a wide margin
regardless of where in the 0–300 kg band the true delivered mass sits.

**Recorded as the artifact's residual:**
`denominator_residual: UNRESOLVABLE-FROM-PUBLIC-SOURCES`. The capacity denominator
resolves; the **mass-delivered denominator does not exist in RKLB's public filings**, and
no amount of platform access recovers it, because the issuer does not disclose it. Under
spec §1b this is recorded, **not** estimated — *"recording it is more valuable than
estimating."*

### A filed-input plausibility bound on the ceiling

Using only filed numbers — payload 300 kg (`sec87` p.8), lift-off mass ~14,000 kg
(same page) — the maximum payload fraction is **2.14%**. (Cross-check: ten Rutherford
engines at 5,600 lbf each = 56,000 lbf against 14,000 kg gives T/W ≈ 1.8, consistent with
a real small launcher.) A 2.1% payload fraction is characteristic of a **maxed-out**
configuration, not a typical one. This is `MODELED` — offered as corroboration that
300 kg is a ceiling, and it is what makes §2's one-signed argument concrete rather than
rhetorical.

---

## 3. Neutron — the gap 001 left open, now closed

001 recorded Electron's 300 kg and **never recorded Neutron's payload at all**. The task
flags this as a known hole that **003's Pillar 4 depends on**. It is filed, and it is
stable:

> *"In March 2021, we announced plans to develop our reusable-ready medium-capacity
> Neutron launch vehicle that will increase the payload capacity of our space launch
> vehicles to **approximately 13,000 kg for reusable configuration launches to low Earth
> orbit** and support lighter payloads for higher orbits."*
> — [📄 RKLB 10-K p.7](https://agentii.ai/v/RKLB/sec87/7), repeated verbatim at
> [📄 10-K p.8](https://agentii.ai/v/RKLB/sec87/8),
> [📄 Q1 2026 10-Q p.29](https://agentii.ai/v/RKLB/sec104/29),
> [📄 Q2 2026 10-Q p.34](https://agentii.ai/v/RKLB/sec109/34)

**Three qualifications, each load-bearing for 003:**

1. **"Reusable configuration" is the qualifier.** The figure is the *reusable*-config
   payload. An **expendable**-configuration payload is **not filed** — a keyword sweep for
   `expendable` across the 10-K returns no payload statement. The commonly-quoted
   expendable figure has **no filed source on this platform** and must not be used as if
   it did.
2. **It is a development target, not a demonstrated capability.** Neutron **has not
   flown**. The filing's own schedule language has moved *away*: *"Production of the Stage
   1 tank is currently aligned with the target delivery of Neutron to the launch pad in Q4
   2026. **While the window for an end-of-year launch date is narrowing**… Exact launch
   timing will also depend on the outcome of first stage qualification and other critical
   tests occurring later in 2026."*
   — [📄 RKLB 10-Q p.35](https://agentii.ai/v/RKLB/sec109/35)
   Grading: the **figure** is filed (`DEMONSTRATED` as a disclosure); the **capability**
   is not demonstrated. 003 must not price Neutron kg against a denominator that has never
   reached orbit.
3. **"Approximately 13,000 kg" is the filer's own hedge** — carry it into any 003
   derivation rather than tightening it to 13,000.

Also filed, and relevant to any 003 derivation of Neutron $/kg: Neutron is **43 m tall
with a 5.5 m fairing**, and its first stage is designed to **return to launch site or land
on an ocean platform** ([📄 10-K p.8](https://agentii.ai/v/RKLB/sec87/8)). Recovery mode
changes the denominator the same way DA-03 records for Falcon 9 vs Starship — a
reusable-config payload and an expendable-config payload are **different denominators**.
This is recorded as a **pointer**, not a finding: no 003 artifact was read.

---

## 4. Launch counts and cadence — verified, with the basis named (DA-07/DA-08)

### The counts are verified exactly as 001 recorded them

> *"We built approximately 14 Electron launch vehicles in 2024 and approximately 24
> Electron launch vehicles in 2025. We built approximately 11 Electron launch vehicles
> during the six months ended June 30, 2026. We launched 16 Electron vehicles in 2024 and
> 21 Electron vehicles in 2025. We launched 12 Electron vehicles during the six months
> ended June 30, 2026."*
> — [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37)

| Period | Filed basis | Built | Launched | Net |
|---|---|---|---:|---:|---:|
| CY2024 | 12 months | ~14 | 16 | **−2** |
| CY2025 | 12 months | ~24 | 21 | **+3** |
| Q1 2026 | 3 months | ~5 | 6 | **−1** |
| H1 2026 | 6 months | ~11 | 12 | **−1** |
| **CY2024 – H1 2026** | **30 months** | **~49** | **49** | **0** |

Q1 2026 from [📄 RKLB 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31); all others from
[📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37).

**Basis, stated explicitly (DA-07/DA-08 discipline).** The count is the issuer's own:
**all Electron-family launch vehicles — Electron and Electron-derived HASTE — orbital and
suborbital, counted in the period of launch, with no internal-payload exclusion.**
Calendar years for 2024–2025; interim periods for 2026. Build counts are the filer's
approximations (*"approximately"*); **launch counts are exact**.

### The 30-month sum is the more precise finding, and 001 did not have it

001 framed this as *"in two of three periods launched more than it built"*. True, but the
periods are **not commensurable** — 001's table set an **11-vehicle six-month** figure
beside a **14-vehicle twelve-month** figure. The net column is internally valid; the level
comparison is not. Summed over the full window the individual drawdowns **cancel exactly**:

> **~49 built, 49 launched. Over 30 months, Rocket Lab built and launched the same number
> of Electron vehicles.**

This is a cleaner statement of 001's conclusion and it removes an alternative explanation.
Under "build-rate ≠ launch-rate", the −2 / +3 / −1 pattern could be inventory management
around lumpy demand. At **net zero over the window**, production and launch cadence are
**matched**, not diverging — which is what a launch-constrained operator would *not* look
like, and what a demand- or production-limited operator would.

### Pad capacity: filed, and 6× the actual cadence

The strongest filed evidence on the launch-constraint question is not the build/launch
ratio — it is that Rocket Lab states its **own throughput ceiling**:

> *"Our operational launch facilities can support Electron and HASTE for up to **120
> launch opportunities every year from LC-1** … and up to **8 launch opportunities every
> year from LC-2** at NASA's Wallops Flight Facility."*
> — [📄 RKLB 10-K p.7](https://agentii.ai/v/RKLB/sec87/7)

| Filed pad capacity | FY2025 actual | Utilisation |
|---|---:|---:|
| **128 launch opportunities/year** (120 LC-1 + 8 LC-2) | **21 launches** | **16.4%** |

On H1 2026's annualised run-rate (12 → 24) utilisation is ~18.8%. **Rocket Lab used under
a fifth of its own filed launch capacity in the most recent full year.** The binding
constraint is not pad throughput. This is `DEMONSTRATED` from filed figures and it is
stronger than the drawdown argument 001 rested on.

### The DA-08 defect in the count basis — cross-issuer comparisons remain invalid

The count is **contaminated with suborbital missions**, and the filing says so:

- The cumulative mission count **includes suborbital launches**: *"…delivering over 250
  spacecraft to orbit for government and commercial customers across 87 successful
  missions through June 30, 2026"*
  ([📄 p.34](https://agentii.ai/v/RKLB/sec109/34)) and, unambiguously, *"We have
  successfully launched Electron 87 times … , **including suborbital launches**, through
  June 30, 2026"* ([📄 p.36](https://agentii.ai/v/RKLB/sec109/36)).
- **HASTE is Electron-derived**: *"HASTE is a suborbital testbed launch vehicle derived
  from Rocket Lab's heritage Electron rocket"*
  ([📄 10-K p.8](https://agentii.ai/v/RKLB/sec87/8)).
- **HASTE is inside the quarterly launch count**: *"Two of the six Electron launch
  missions completed for the three months ended June 30, 2026 were Hypersonic Accelerator
  Suborbital Test Electron ('HASTE') launch missions"*
  ([📄 p.37](https://agentii.ai/v/RKLB/sec109/37)).

So of H1 2026's **12** filed "Electron launches", **≥2 (≥17%) were suborbital and
delivered nothing to LEO**. Q1's HASTE count is not disclosed numerically, so the H1 total
**cannot be completed** from the filing.

**Why this makes cross-issuer comparison invalid without restatement (DA-08).** DA-08
registers that SPCX counts a *"customer launch"* only when an external payload is primary,
excluding internal Starlink launches. RKLB is the **opposite** contaminant: it has **no
internal payloads** (so it needs no customer-only filter) but it **includes suborbital
missions** that a purely-orbital peer count would exclude. The two counts are therefore
wrong in **different directions** and do not cancel:

| To compare on a common basis | Restatement RKLB requires |
|---|---|
| Orbital customer launches | remove HASTE from RKLB's count — **H1 2026: ≤10, not 12**; full figure **not disclosed** |
| All launches incl. suborbital | restate SPCX upward — **not available on this platform** |
| Internal-payload exclusion | **none needed** — RKLB launches no internal payloads |

**Consequence for PIL-1:** the per-launch $ figures in §5 are **blended** across orbital
and suborbital missions. HASTE vehicles are cheaper than orbital Electrons, so the blend
**drags the average down** — a third route by which 001's $/kg is a **floor**, consistent
with §2.

---

## 5. DA-06 — does the filing distinguish price from cost? **Yes, explicitly, and defines both**

This is the question RKLB uniquely answers in the universe, and the answer is filed in
**adjacent paragraphs with two separate definitions**:

> *"**Revenue per launch** represents the average transaction price attributable to launch
> contract performance obligations during the period in which the launch occurs, regardless
> of whether the revenue is recognized using the point-in-time or over-time method of
> revenue recognition."*
>
> *"**Cost per launch** is calculated by taking actual costs of the launch vehicles that
> occur in the period, regardless of whether the costs were recognized using the
> point-in-time or over-time method **and all period costs in the period of launch**."*
> — [📄 RKLB 10-Q p.37](https://agentii.ai/v/RKLB/sec109/37); identical text at
> [📄 Q1 2026 10-Q p.31](https://agentii.ai/v/RKLB/sec104/31)

They are **not** the same number divided differently, and the filing does not conflate
them. Two consequences:

- **DA-01 basis A and basis B are separately sourced** — basis A from the price
  definition, basis B from the cost definition. That is what let 001's basis B be
  `DEMONSTRATED` rather than modelled. **DA-06 discipline is satisfied by the issuer.**
- **The disclosure is a normalisation, not a derivation** — the price definition says so
  itself (*"regardless of whether the revenue is recognized using the point-in-time or
  over-time method"*). That is **DA-25**, and it is why the metric does not reconcile to
  the audited segment table. Neither figure is wrong; they answer different questions.

### The filed per-launch series — six points, two of which 001 did not have

| Period | Revenue/launch | Cost/launch | Implied spread | Source |
|---|---:|---:|---:|---|
| Q1 2025 | $7.1M | $5.7M | $1.4M | Q1 10-Q p.31 |
| Q2 2025 | $7.9M | $5.0M | $2.9M | Q2 10-Q p.37 |
| H1 2025 | $7.5M | $5.3M | $2.2M | Q2 10-Q p.37 |
| Q1 2026 | **$9.3M** | $5.4M | $3.9M | Q1 10-Q p.31 |
| Q2 2026 | **$9.1M** | **$4.4M** | $4.7M | Q2 10-Q p.37 |
| H1 2026 | **$9.2M** | **$4.9M** | $4.3M | Q2 10-Q p.37 |

001 recorded only the Q2 2026 and H1 2026 rows. The full series shows **price rising while
cost falls** — the spread widens in **every** period, $1.4M → $4.7M quarter-on-quarter.
The filing attributes the price move to *"changes in customer mix and mission
complexity during the period in which the launches occurred"* (p.37), **not** to
list-price increases — a mix-shift reading, not a pricing-power reading.

**Both bases reported side by side** (`no_single_basis_collapse`, DA-25):

| Launch Services margin | Q2 2025 | H1 2025 | Q2 2026 | H1 2026 |
|---|---:|---:|---:|---:|
| **Normalised** (disclosed per-launch pair) | 36.7% | 29.3% | **51.6%** | 46.7% |
| **Audited** (segment table) | 30.5% | 26.1% | **42.9%** | 43.7% |

Audited segment figures — Q2 2026 revenue **$44,586k**, cost of revenue **$25,476k**,
gross profit **$19,110k**; H1 2026 **$108,249k / $60,916k / $47,333k**
([📄 RKLB 10-Q p.32](https://agentii.ai/v/RKLB/sec109/32)).

The two bases **reproduce 001's DA-25 numbers exactly** (51.6% normalised vs 42.9%
audited) — independently confirming the arithmetic behind the registered defect while
leaving the **registration** to 001, per §0. The gap is **8.7 points** and it is the
reason a downstream thesis must not read the disclosed per-launch pair as a segment
margin.

**Backlog, cited not recomputed** (§0): **$2,355.9M at 2026-06-30**, from $1,847.3M at
2025-12-31, **of which $1,415.8M space systems and $940.2M launch services** — the
segment split is new here; the total matches the inherited figure
([📄 RKLB 10-Q p.38](https://agentii.ai/v/RKLB/sec109/38)).

---

## 6. DA-23 — the flip, now confirmed by the platform's own calculation tree

001 established this by arithmetic. This artifact re-runs it through the **platform's
instruments** and finds the defect **at the extraction layer**, not merely in the numbers.

**Component identity, in-line, from the primary statement of operations:**

```
  Q2 2026 — three months
    gross profit              $84,576k     ← 10-Q p.6
    total operating expenses $142,090k     ← same statement
                            ───────────
    gross profit − opex     = $(57,514)k   ← arithmetic
    Operating loss (57,514)                 ← AS FILED, same statement ✓ SIGN AGREES
```

**The same identity through the platform's extraction layer — here it flips, on TWO periods:**

| Period | As filed (p.6) | XBRL `OperatingIncomeLoss` | Flip |
|---|---:|---:|---|
| Q2 2026 | **$(57,514)k** | **+57,514,000** | exact, ±magnitude |
| Q2 2025 | **$(59,639)k** | **+59,639,000** | exact, ±magnitude |

Both filed values are read directly off the condensed consolidated statements of
operations: *"Operating loss … (57,514) … (59,639)"* for the three months ended June 30,
2026 and 2025 respectively
([📄 RKLB 10-Q p.6](https://agentii.ai/v/RKLB/sec109/6)). Both XBRL values are
`is_primary: true`, `source_authority: 2`, source file `rklb-20260630.htm`
(`search_xbrl_facts`).

**Three independent confirmations, none of which relies on 001:**

1. **The primary statement itself** (p.6) — the filed operating loss is negative in both
   periods, and `gross profit − total operating expenses` reproduces it exactly. The
   H1 2026 column checks identically: $161,069k − $274,552k = $(113,483)k, as filed
   ([📄 p.42](https://agentii.ai/v/RKLB/sec109/42) and [📄 p.6](https://agentii.ai/v/RKLB/sec109/6)).
2. **`validate_calculation`** on accession `0001819994-26-000062` returns
   `us-gaap:OperatingIncomeLoss` **computed −57,514,000 / reported +57,514,000**
   (`status: fail`). The platform's **calculation-arc engine** — the instrument P3 is
   built on — computes the *correct* value and the *reported* one is the stripped one.
3. **The filed net loss and EPS agree in direction**: net loss $(49,258)k and EPS
   $(0.08) ([📄 p.6](https://agentii.ai/v/RKLB/sec109/6)) — loss, negative EPS, while the
   same extract reports +49,258 / +0.08.

> **DA-23 confirmed for RKLB at the extraction layer, on two consecutive-year quarters,
> each an exact ±magnitude flip.** Sign stripping is not a one-period accident here.
> `EPS × shares` remains inadmissible (001: *"RKLB passes it while being flipped"* —
> $0.08 × 629.7M ≈ $50.4M ≈ $49.258M; both figures share the same inversion, so the test
> clears the issuer it should catch). The **component identity is the admissible test**,
> and it is the one used here. **No figure in this artifact is derived via `EPS ×
> shares`.**

**One caveat, and it is the tool's not the issuer's — recorded because P3 depends on this
instrument.** The same `validate_calculation` run reports the 2025 row as *computed*
−186,242,000 against *reported* +59,639,000 — the **reported** side is correct (Q2 2025's
stripped operating loss, matching p.6), but the **computed** side is not: −186,242,000
corresponds to no filed period, and the arc is **mixing the three-month and six-month 2025
columns**. The 2026-Q2 row is clean on both sides; the 2025 row is clean only on the
reported side.

> **P3 implication:** the calculation-arc instrument needs a **period-alignment guard**
> before it is applied universe-wide. Unguarded, it reports `fail` rows that are
> period-mixing artefacts rather than defects — and a detector that fires on its own bug
> is not a detector. This is a *method* finding for P3, distinct from DA-23 itself.

### The denominator is narrative-only — no XBRL instrument can ever validate it

`list_xbrl_concepts(search="payload")` returns **zero concepts** in the `us-gaap`
namespace. Electron's 300 kg and Neutron's 13,000 kg exist **only as narrative text**.
This is a **structural** finding for P1 and P3: **no calculation-arc or XBRL test can ever
reach the payload denominator.** P1's denominator can only be validated by document
reading — which is why §1d's citation requirement is the load-bearing instrument for
PIL-1, and why §2's residual cannot be closed by any amount of platform access.

---

## 7. What this artifact does NOT do

- **No re-derivation of inherited figures** (§0). $14,667/kg, $30,333/kg, the 10.3×
  Falcon 9 ratio, DA-25's registration, and backlog $2,355.9M are **cited** to 001's
  `RKLB/2026-09-18_1239_unit-economics_methodology.md`. Where this artifact adds a filed
  citation for an inherited figure (backlog), the figure is the **same value** — the
  citation is the addition, not the number. **No file under
  `001-technology-baseline/` was modified** — frozen-file policy (Q-4).
- **No cross-issuer $/kg arithmetic.** That is the parallel `RKLB × unit-economics` task.
  This artifact supplies the **operational** side: the filed denominator, the cadence, the
  capacity, and the basis defects a cross-issuer comparison must restate around.
- **No price**. No market data was used; this artifact is price-independent.
- **No mass-to-orbit estimate.** Recorded as unavailable (§2), not modelled.

---

## Carry-forwards

1. **PIL-1 is closeable on the Electron denominator, with the band stated correctly.**
   Filed at 300 kg, movement **0.00%**, falsifier **does not fire**. But quote it as
   *"capacity ceiling, self-asserted by issuer"*, with the **mass-delivered** denominator
   recorded `UNRESOLVABLE-FROM-PUBLIC-SOURCES` and the residual **one-signed upward**. The
   pillar should not be presented as "denominator validated, ±15% met" without that
   qualifier — the ±15% that remains is entirely in the delivered-mass term.
2. **003's Neutron hole is closed, with two guards.** `~13,000 kg` **reusable
   configuration** to LEO, filed, four sources. The **expendable**-config payload has
   **no filed source**. Neutron **has not flown**, and the filing says the end-of-year
   window is *"narrowing"* — the **figure** is filed; the **capability** is not
   demonstrated. 003 must not price Neutron kg against an unflown vehicle.
3. **The HASTE contamination should propagate to P3.** ≥2 of H1 2026's 12 filed Electron
   launches were **suborbital**, and the cumulative count explicitly includes suborbital
   launches. Any downstream screen counting RKLB launch events is counting non-orbital
   missions. Full HASTE share **not disclosed** — recommend the Q1 2026 HASTE count be
   sought from the transcript or an 8-K, where the platform does carry RKLB sources.
4. **The calculation-arc instrument needs a period guard before P3 goes universe-wide**
   (§6). One `fail` row in this single filing is a period-mixing artefact. 002's P3
   deliverable depends on this instrument; an unguarded sweep will produce false
   positives at unknown rate.
5. **PIL-1's remaining resolution path is named and reachable in principle:** a NASA
   launch manifest, a range safety document, or a customer contract stating Electron
   payload mass. None is on the platform. **This is a source gap, not a platform gap** —
   the disposition class is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` for the delivered-mass
   denominator, and `UNRESOLVABLE-FROM-PLATFORM` for nothing in this artifact.
6. **Neutron's expendable payload and RKLB's mass-to-orbit** are the two figures this
   artifact looked for and did **not** find. Both are recorded as absences rather than
   filled by estimate.

---

*Citations verified by reading each page. Page numbers located via
`search_keyword_in_source` / `read_source_outline`; none guessed. No file under
`theses/001-technology-baseline/` was modified.*
