# Entities — 001 Technology Baseline

> Q20/Q36: the entity_claims schema and the entity/metric map for this thesis.
> For `market_data_stage: early` theses this file MUST additionally define the
> bars schema of `get_price_history` (Q42) — no bars schema, no implement.

**Q42 bars schema: NOT REQUIRED, and deliberately omitted.** Every row of the spec's
Skill Deployment Matrix declares `market_data_stage: none`, so `implement` will not
demand a bars schema. This is a decision, not an omission: the thesis consumes filings,
XBRL facts and source documents — no price series is read, and no position is sized.
The omission is stated here so a reader does not mistake it for an unfinished file.

## entity_claims schema

Every claim written into an artifact must conform. Note the two additions this thesis
requires beyond the base template: **`definition`** (which DA-register meaning is being
used — mandatory under the §1c standing rule) and **`evidence_grade`** (P4's
`DEMONSTRATED` / `CLAIMED` / `MODELED`).

```yaml
entity_claims:
  - entity: SPCX
    metric: mass_to_orbit
    value: 485
    unit: metric_tons
    period: 2026Q2
    definition: DA-07_verified_successful_launches_only   # excludes failed/scrubbed
    evidence_grade: DEMONSTRATED                          # filed in the 10-Q
    source: sec:0001628280-26-052535:p35
    retrieved_at: 2026-09-18T10:30:00-04:00
    observed_at: null        # market-derived claims only (Q71); null for filings

  - entity: SPCX
    metric: nameplate_compute_draw
    value: 1.4
    unit: gigawatts
    period: 2026Q2
    definition: DA-11_it_load_only_excludes_cooling_and_facility_overhead
    evidence_grade: DEMONSTRATED
    source: sec:0001628280-26-052535:p36
    retrieved_at: 2026-09-18T10:30:00-04:00
    observed_at: null
```

**Rule.** A claim missing `definition` for a DA-registered metric is malformed and must
not be written to an artifact. A claim missing `evidence_grade` defaults to the *weakest*
grade, `CLAIMED` — never to `DEMONSTRATED`.

## Entity / metric map

| entity | metric | unit | definition (DA ref) | source |
|---|---|---|---|---|
| SPCX | mass_to_orbit | metric tons | DA-07 — verified, successful launches only | 10-Q `sec8` p35 |
| SPCX | falcon_launches | count | DA-08 — split customer vs internal | 10-Q `sec8` p35 |
| SPCX | starship_launches | count | DA-08 — all classified internal to date | 10-Q `sec8` p35 |
| SPCX | starlink_subscribers | millions | DA-09 — service lines, not people | 10-Q `sec8` p36 |
| SPCX | starlink_arpu | USD/month | DA-10 — subscriber service revenue only | 10-Q `sec8` p36 |
| SPCX | nameplate_compute_draw | GW | **DA-11 — IT load only** | 10-Q `sec8` p36 |
| SPCX | revenue_by_segment | USD M | DA-21 — issuer segment definition | 10-Q `sec8` p42–44 |
| SPCX | space_r_and_d | USD M | — | 10-Q `sec8` p42 |
| RKLB | launch_count / revenue / backlog | count / USD M | DA-08, DA-03 | 10-Q, 8-K |
| FLY | launch_count / revenue | count / USD M | DA-08 | 10-Q |
| YSS | satellite_production_rate | units/period | **DA-13 — manufactured vs launched** | 10-Q |
| PL | constellation_size | count | **DA-12 — licensed vs launched vs operational** | 10-Q |
| IRDM | revenue / net_income / subscribers | USD M / count | DA-09, P11 pre-merger basis | 10-Q |
| GSAT | revenue / spectrum_holding | USD M / MHz | DA-17 | 10-Q |
| SATS | spectrum_holding | MHz | **DA-17 — MHz vs MHz-pop** | 10-Q, 8-K |
| GOOG | suncatcher_satellite_count / TPU config | count | — (CLAIMED, no filing) | press, Google Research |
| NVDA | gpu_power_draw | kW/unit | DA-04 — nameplate vs actual | 10-K |
| VRT | cooling_capacity / capex_per_kW | kW / USD | **DA-05 — which terrestrial basis** | 10-K |
| BWXT | space_nuclear_revenue | USD M | separable from terrestrial? (known-open) | 10-K segment |
| UTHR | varda_partnership_terms | — | DA-22, P4 CLAIMED-only | 10-Q narrative |
| — (private) | varda_kg_returned_per_mission | kg | DA-22, P4 **CLAIMED only** | press only |

## Metrics this thesis will need but that no issuer discloses

Recorded so Phase 1–6 do not waste effort searching for them. Each is a candidate for
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` under the §1c disposition.

| metric | why it matters | status |
|---|---|---|
| $/kg to LEO on basis B (marginal cost) | the only basis testing the F5 floor | not disclosed; must be `MODELED` |
| $/kg to LEO on basis C (fully-loaded) | the economically complete basis | not disclosed; must be `MODELED` |
| radiator mass per kW, any flown system | P2's core measurable | not disclosed by any issuer |
| array area per MW, actual | P2's second measurable | not disclosed |
| cost per kg returned, microgravity | P4's economic test | not disclosed; Varda private |
| orbital compute revenue, any issuer | P2's falsifier | does not exist yet |
