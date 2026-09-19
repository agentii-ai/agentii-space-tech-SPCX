---
thesis_id: "004-tier0-spacex-anchor"
pillar: cross
ticker: cross
skill: synthesis
mode: methodology
generated_at: 2026-09-19T16:10:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "none"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: fast
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "Every segment figure is read on the FILED sign. The segments sum to $(143)M and the served consolidated line returns +143,000,000 — 16 of 20 served SPCX OperatingIncomeLoss facts are sign-stripped."
pillar_verdicts:
  PIL-1: "HOLDS — 3 of 3 segments carry a discrete filed revenue line AND a discrete filed operating result. The Minimum Defensible View is delivered; the decomposition is real."
  PIL-2: "HOLDS, with the DA-10 bound carried — operating leverage is demonstrated (+79.4% income on +65.8% revenue) and the channel mix moves toward the higher-value channel. Price erosion cannot be fully separated from mix shift from public disclosure."
  PIL-3: "HOLDS AS A BOUND, not as a value — the AI segment has no admissible multiple from filed or peer data. Carried at INVESTED CAPITAL; advertising IS separable at 21.0% of the segment, Grok and compute are not."
  PIL-4: "HOLDS — the ex-R&D operating result is POSITIVE at +$534M, so launch carries standalone value. The numerator is MODELED (the filing does not split Starship from Falcon R&D) and the DA-06 non-comparability flag travels with the row."
  PIL-5: "HOLDS — coverage 0.1005x, an order of magnitude below the 1.0x falsifier. CAPITAL binds, and at this moment it binds through one unresolved disclosure (the Cursor dilution) now RESOLVED at 391,041,680 shares."
  PIL-6: "HOLDS — the comparability partition admits 0 of 11, and every published anchor row carries a boundary naming 005, 006 and 009 as its permitted consumers."
capability_timeline:
  - note: >
      Partial. This thesis is `market_data_stage: per_row` — `sotp-valuation` and `reverse-dcf`
      run at `late`, the other five executed rows at `none`. It is the FIRST thesis in the
      workspace with a live market-data dependency, and the first where `PRICE_ACCESS_PREMATURE`
      could fire. The nearest timeline equivalent is the seven-trigger register (T-1 … T-7),
      which is datability-driven rather than capability-adoption-driven.
key_metrics:
  separable_segments: 3
  live_market_cap_usd_t: 2.0718
  market_cap_to_connectivity_opinc: 312.8
  admissible_comparators: 0
  coverage_ratio: 0.1005
  cursor_shares_issued: 391041680
  challenge_findings_high: 4
  segment_capex_total_q2_2026_usd_m: 18369
  ai_capex_share_q2_2026: 0.8617
  connectivity_closure_residual_usd_m: 0
---

# Thesis 004 — Tier 0: SpaceX Anchor

**The synthesis.** What the anchor found, what it refused to claim, and what 005–009 may price off.

## The finding, in one line

> **SPCX's live market capitalisation — $2.0718T — is 312.8× the annualised operating income of
> Connectivity, and Connectivity is the ONLY profitable segment.**

Space runs **$(2.2)bn** annualised and AI **$(5.0)bn**. **So there is no conventional conglomerate
discount to measure.** The standard SOTP asks whether the parts exceed the whole; here the whole
already requires the one profitable segment to carry ~313×, and **the finding survives every
allocation** — even granting the two loss-making segments **$1.5T**, Connectivity carries **86×**.

## Where the value sits, and where it does not

**Four independent lines converge, and three were already in the workspace before this thesis:**

| Line | Source | What it says |
|---|---|---|
| **A1b falsified** | 001 | Value migrated **out of** launch |
| **27 of 37 internal** | 004's own §1 | Space is an **unpriced input** to the thing that earns — capitalised into satellites in PP&E |
| **The margin ladder** | 003 | Operating margin is **monotone in distance from programme risk** |
| **The extension is a mix shift** | 004 | Connectivity's growth is **channel mix toward Enterprise & Government (+108.3% vs +44.4%)**, not a rising tide |

**And the anchor's own addition: the AI segment cannot be valued from public disclosure at all.**
Its headline metric — **1.4 GW** — is **IT load** (DA-11), a capacity figure no disclosed $/kW
converts. **That is why P3's headline is invested capital, a COST basis.**

## What the anchor refused to claim

The refusals are the deliverable as much as the finding:

- **No blended multiple.** Valuing three businesses at one rate is a different claim, and the
  spread between the two is the finding.
- **No forward DCF.** Fails the ≥3-year positive-FCF limb. `reverse-dcf` is admissible **because
  it forecasts nothing**.
- **No borrowed comparator.** **The partition admits 0 of 11**, and the three segments fail for
  **three different reasons** — earnings, price formation, and disclosure. One screen would not
  have found them.
- **No external multiple for Space.** DA-06: a captive-integrated launcher has **no transaction
  price**. Comparing its margin to a peer is comparing a price to a non-price.
- **No point estimate.** Every regime is a `MODELED` range.

## The reverse-DCF, and the breach it exposes

At the constitution's **15–25% required return**, the live price implies **14.7–24.7% perpetual
growth** — `g ≈ r − 0.32%`. **Terminal value therefore approaches 100% of EV, breaching F1's own
50–70% cap.** Reported as three readings, not resolved: the price may be too high, the cap may be
wrong at this stage, or **the attribution may be the artefact** — the 313× sets Space and AI to
zero by construction.

## What this thesis could NOT value — recorded, never implied

| Item | Class |
|---|---|
| Aviation / maritime splits | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — inside `EnterpriseAndGovernmentMember` |
| Grok vs compute | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — advertising **is** separable |
| Subscribers / ARPU by channel | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — revenue decomposes, the denominator does not |
| The constitution's ~$1.62T basis | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` — **it implies $122.95/share against an IPO at $135.00** |

> ### ⚠️ RETRACTED ROW — "segment-level capex" was NOT unresolvable, and the claim is withdrawn
>
> An earlier version of this table listed **segment-level capex** as
> `UNRESOLVABLE-FROM-PUBLIC-SOURCES`, *"company-level attribution only."* **That is false.** The
> 10-Q's Note 18 supplemental segment table files **capital expenditures by segment** — Space
> **$1,174M**, Connectivity **$1,367M**, AI **$15,828M**, total **$18,369M**, 3M ended 2026-06-30.
> Source: [SPCX 10-Q p.30](https://agentii.ai/v/SPCX/sec8/30).
>
> **Why the retraction matters more than the row.** The claim was not a search failure — the figure
> is on **the same page as the segment income table this thesis is built on**. It was recorded as
> unresolvable because the artifact that produced it **did not open the page it was citing**. A
> bound asserted as `UNRESOLVABLE` is the most expensive kind of error here: it closes a question
> the filings answer, and no downstream thesis will re-open it.
>
> **What the figure adds — AI is 86.2% of capital expenditure and the largest loss.**
> `15,828 / 18,369 = 86.17%` of quarterly capex goes to the segment running a **$(1,257)M** quarterly
> operating loss on **$2,561M** of revenue. **Connectivity, the only profitable segment, receives
> 7.4%.** That is the capital-allocation finding stated as arithmetic, and it is available from the
> filings this thesis already reads.

## What 005, 006 and 009 may price off

**The Connectivity and AI rows are reusable references for 006 and 009** — SPCX appears in **neither
universe**. The boundaries are **partitions**: a name is in or out, with its excluded class named
(`P11` · `loss_making` · `PARTIAL` · `non_disclosure`). **A downstream thesis that prices off a name
this anchor excluded has re-opened a closed class without saying so** — the failure P6 is built to
prevent, and one that would be invisible because that thesis would look internally consistent.

**And per Q64, two challenge findings block knowledge-base entry**: the `entity_claims` schema names
`ticker` where every consumer reads `entity`, and carries no `retrieved_at`. See `challenge.md`.
