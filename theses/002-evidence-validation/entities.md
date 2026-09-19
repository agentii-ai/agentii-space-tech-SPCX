# Entities — 002 Evidence Validation

> Q36 side artifact. `entity_claims` schema + entity/metric map for the 17 universe names.
> **The Q42 bars schema is NOT required** — every matrix row in `spec.md` §3 declares
> `market_data_stage: none`, so `implement` will not demand it. Recorded here so the
> absence is a **decision, not an omission**.

## `entity_claims` schema

```yaml
entity_claims:
  - ticker:        str   # uppercase, as the platform keys it
  - company:       str
  - sector:        str   # as filed — see the taxonomy hazard below
  - role_in_thesis: str  # what this name is here to validate
  - validation_targets:
      - figure:      str    # the specific number under test
        claimed_value: number
        unit:          str
        current_grade: DEMONSTRATED | CLAIMED | MODELED
        source_artifact: str  # 001 artifact or constitution section
        target_grade:  DEMONSTRATED | DERIVED
        citation:      str    # https://agentii.ai/v/{ticker}/{citation_id}/{N}
        pillar:        PIL-N
        disposition_if_unresolvable: UNRESOLVABLE-FROM-PUBLIC-SOURCES | UNRESOLVABLE-FROM-PLATFORM
```

## Entity / metric map

| Ticker | Sector (as filed) | Role in this thesis | Primary validation targets | `citation_id` |
|---|---|---|---|---|
| **SPCX** | `industrial.aerospace_defense` | Largest validation surface | Falcon 9 22.8 t denominator (P1); **DA-11 1.4 GW nameplate** (P4); segment reconciliation producing the DA-23 census (P3); **entity-boundary classification** (P6) | **`sec8`** (Q2 2026 10-Q — the only one) |
| **RKLB** | `industrial.aerospace_defense` | **Electron's 300 kg denominator (P1)** — divisor of the universe's only `DEMONSTRATED` per-launch cost. Also DA-25's normalised `revenue per launch` | Electron payload mass; basis A/B/C recomputation; DA-25 | `sec109`, `sec104` |
| FLY | `industrial.aerospace_defense` | Alpha's payload denominator; DA-23 flip instance; EGC disclosure-quality variable | Alpha payload; DA-23 components | — |
| BWXT | `industrial.nuclear_energy` | **F2's nuclear case (P2)** — the 24× area reduction rests on the unsourced COP and areal-density inputs | Radiator areal density; heat-pump COP; R&D intensity 0.5% | — |
| GOOG | `tech.platform_internet` | Suncatcher's compute-per-satellite figure — 001 found it **not stated**, making PIL-2's falsifier untestable | Compute per satellite; R&D $18.2B/qtr | — |
| VRT | `industrial.machinery` | Terrestrial thermal comparator; supplies the PUE benchmark for P4 | PUE; cooling cost per kW; margin trend | — |
| MSFT | `tech.platform_internet` | The capex-derived capacity figure P4's restatement is compared against | FY2026 capex **$115,948M** → GW/yr | — |
| NVDA | `tech.semiconductors` | The H100 thermal-failure datapoint and the $/kW cost stack | H100 thermal limit; no rad-hard SKU | — |
| **MRCY** | `industrial.aerospace_defense` | The **0.03% margin edge case** where a sign error is **invisible by inspection** | $0.280M operating income on $983.6M revenue | — |
| **YSS** | `industrial.aerospace_defense` | **P3's named anomaly** — $110.466M operating figure on $116.343M revenue | The Q1 2026 anomaly | **`sec9`** (Q1 2026 10-Q) |
| UTHR | `med.medicines_biotech` | Clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case (P7); 87.3% gross-margin benchmark | Microgravity economics; margin | — |
| SATS | `tech.telecom_services` | **DA-24** asset-sale contamination, and proof DA-23 and DA-24 are independent | 2025 Q3 operating income = 4.6× revenue | — |
| **VOYG** | `industrial.aerospace_defense` | **DA-23 candidate, new sub-mechanism** — an unreconcilable *level*, not a sign | $51.408M operating vs $4.457M gross profit | — |
| **LUNR** | `industrial.aerospace_defense` | **DA-23 candidate with no available detector** | 42.1% operating margin; no gross-profit line | — |
| **HAWK** | `industrial.aerospace_defense` | **DA-28 site** — four non-agreeing share counts | EPS bridge fails by 72% | — |
| **BA** | `industrial.aerospace_defense` | **DA-23 flip instance #5** and a candidate | −5,761 → +5,761; 2025 Q3 margin | — |
| **IRDM** | `tech.telecom_services` | **DA-23 control group** — the positive control on the clean side | +34.0 → +34.0 | — |

## Two taxonomy hazards carried in the map

1. **`BWXT` files under `industrial.nuclear_energy`, `TER` under `tech.semiconductors`,
   `VRT` under `industrial.machinery`.** A sector screen on `aerospace_defense` will
   **silently miss them.**
2. **`GSAT` files under `tech.tech_hardware`, not `tech.telecom_services`** (found by 006
   during specification). A telecom-keyed screen drops the tier's second-largest name.
   **GSAT is not in 002's universe**, but the hazard is recorded here because 006 and 011
   both screen the same registry.

## Names deliberately absent

**`MOG-A` and `ENS`** carry fund-sourced cases in the corpus while showing **zero issuer
coverage** — they cannot host validation work. **`RDW`, `SPIR`, `SPCE`, `MDA`, `TSAT`,
`GILT`, `SGBAF`, `ATRO`, `AMPX`, `TMUS`** are `NOT_READY`. `AMZN`, `AAPL`, `ASTS`, `VSAT`,
`TRMB`, `GRMN`, `PLTR`, `LLY` are `PARTIAL` and require manual sector assignment before
any aggregate constraint can evaluate — **a precondition, not an assumption.**
