---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T12:39:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"   # no corpus-version endpoint exposed by the platform; see brief.md
definitions_used:
  - da_id: "DA-07"
    chosen_reading: "verified mass from successful launches only; excludes failed and scrubbed"
  - da_id: "DA-08"
    chosen_reading: "customer launch = external payload is primary payload and mission params designed around it"
  - da_id: "DA-09"
    chosen_reading: "subscriber = a service line, not a person, household or device"
  - da_id: "DA-10"
    chosen_reading: "Starlink subscriber service revenue only; excludes enterprise, government, aviation, maritime"
  - da_id: "DA-11"
    chosen_reading: "IT load only — excludes cooling, power distribution, lighting, security, facility overhead"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SPCX — Operational Baseline, Q2 2026

Source: Form 10-Q for the quarter ended 2026-06-30, accession
`0001628280-26-052535`, filed 2026-08-04. Pages 35, 36, 42–44 read in full.

**Why SPCX carries Deep depth**: it is the only issuer in the universe that discloses
hard throughput metrics rather than narrative. Every figure below is `DEMONSTRATED` —
filed and auditable. That makes it the sector's measurement anchor, and simultaneously
the source of the DA-07…DA-11 definitional traps that make cross-issuer comparison
fail silently.

## Space segment — throughput

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Mass to orbit (t) | **485** | 652 | **−26%** |
| — attributable to customer payloads | 87 | 88 | −1% |
| — attributable to internal payloads | 397 | 563 | −29% |
| Falcon launches | **37** | 45 | −18% |
| — customer launches | 10 | 9 | +11% |
| — internal launches | 27 | 36 | −25% |
| Starship launches | 1 | 1 | — |

**The headline is negative and easy to miss.** Mass to orbit fell 26% year over year
while total revenue rose 91.9%. The decline is entirely internal-payload decline
(−29%), i.e. fewer Starlink satellites launched — not a customer-demand problem, whose
payload mass was flat at 87 t vs 88 t.

**DA-07 application**: mass to orbit counts only *verified* mass from *successful*
launches, explicitly excluding failed and scrubbed attempts. A competitor reporting
launched mass rather than delivered mass would show a higher number on an identical
campaign. Not comparable without restatement.

**DA-08 application**: only 10 of 37 Falcon launches count as customer launches.
Internal Starlink deployments generate **no inter-segment revenue** — the cost is
capitalized into satellites in PP&E. So SPCX's Space segment revenue reflects customer
activity only, and any "launches" comparison against RKLB or FLY that does not restate
for this is invalid. This is the single largest restatement requirement in the universe.

## Space segment — financials

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue | $962M | $746M | +29.0% |
| Cost of revenue | $329M | $330M | −0.3% |
| R&D | **$1,076M** | $693M | **+55.3%** |
| SG&A | $99M | $87M | +13.8% |
| Total costs | $1,504M | $1,115M | +34.9% |
| Operating loss | **$(542)M** | $(369)M | **+46.9% widening** |

**R&D is 3.3× cost of revenue**, driven by Starship production, engineering and test.
The Space segment loses money at the operating line and the loss is widening while
revenue grows — a development-phase signature, not a scale problem.

## Connectivity segment — the profitable business

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue | $4,291M | $2,588M | +65.8% |
| Operating income | **$1,656M** | $923M | **+79.4%** |
| Starlink subscribers | **12.0M** | 6.0M | **+101%** |
| Starlink ARPU | **$66/mo** | $85/mo | **−22.4%** |

**DA-09 / DA-10 application.** Subscribers are *service lines* — an individual or
household with both a residential and a roam line counts **twice**, and managed
enterprise and government customers are excluded entirely. ARPU is computed on
subscriber service revenue only, excluding the enterprise, government, aviation and
maritime lines. SPCX attributes the ARPU decline to "international expansion and the
addition of lower priced service plans" — which under DA-10 means **at least part of the
22.4% decline is a mix-shift artifact**, not price erosion. The two readings are not
distinguishable from public disclosure.

This is the only segment with real operating leverage in the entire 35-name universe:
income from operations grew 79.4% on 65.8% revenue growth.

## AI segment — and the DA-11 trap

| Metric | Q2 2026 | Q2 2025 | Δ |
|---|---|---|---|
| Revenue | $2,561M | $737M | +247.5% |
| Operating loss | $(1,257)M | $(1,524)M | −17.5% narrowing |
| **Nameplate compute draw** | **1.4 GW** | 0.4 GW | **+250%** |

**DA-11 is the most dangerous figure in this thesis.** SPCX defines nameplate compute
draw as *GPUs installed × all-in power draw*, and states explicitly that it **excludes
power for cooling systems, power distribution losses, lighting, security systems and
facility-level overhead**. So 1.4 GW is an **IT load**, not a facility load. True
facility draw is materially higher — typically 1.2–1.5× for a modern data centre, more
for high-density AI racks.

Any orbital-vs-terrestrial comparison that takes 1.4 GW as a facility load understates
the terrestrial denominator and overstates orbital compute's relative position. Phase 6
must restate this; it is flagged as plan risk #2.

**A4 boundary check (constitution).** This segment is **ground-based**. SPCX's separate
filing for up to 1 million satellites at 100 kW/tonne is a `CLAIMED` aspiration with no
revenue line. No listed issuer reports orbital compute revenue — PIL-2 holds.

## Segment reconciliation — and a sign-convention trap

```
  Space          −542
  AI           −1,257
  Connectivity +1,656
  ─────────────────────
  Consolidated   −143   ← operating LOSS
```

`get_company_financials` returns `OperatingIncomeLoss: +143,000,000` — **positive**. The
inconsistency is a platform sign-convention artefact (see the Phase 1 cross artifact,
data-quality note). An `operating_income > 0` screen would misclassify SPCX as
profitable. **Verified against narrative**: the 10-Q reports a net loss of $541M, and
the segment arithmetic independently confirms −143.

## Hand-off to Phase 2

- Mass to orbit is the only sector-wide throughput metric that is actually delivered
  rather than claimed. Phase 3 should test whether RKLB/FLY/YSS disclose anything
  comparable; if not, no cross-issuer throughput comparison is possible and PIL-3's
  falsifier must be evaluated on issuer-specific restatements.
- The 1.4 GW figure needs a cooling-inclusive restatement before Phase 6.
- Subscriber/ARPU mix-shift ambiguity (DA-09/DA-10) should be carried into the Phase 3
  Connectivity analysis rather than resolved here.
