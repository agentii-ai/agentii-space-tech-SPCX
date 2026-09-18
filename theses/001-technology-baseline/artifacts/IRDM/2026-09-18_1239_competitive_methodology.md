---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: IRDM
skill: competitive
mode: methodology
generated_at: 2026-09-18T15:10:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-09"
    chosen_reading: "subscribers as reported by IRDM — not restated to the SPCX service-line convention"
  - da_id: "DA-17"
    chosen_reading: "spectrum valued via the EchoStar transaction mark, not MHz"
  - da_id: "DA-21"
    chosen_reading: "IRDM's own segment definitions; no cross-issuer aggregation"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; IRDM is NOT flipped (profitable issuer)"
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: false
---

# IRDM — Competitive Position, Q2 2026

Source: Form 10-Q, accession `0001418819-26-000045`. **IRDM is a P11 deal security**
(being acquired by RKLB at $54/share, announced 2026-06-29) — all figures are
**pre-merger standalone basis**.

**Why this analysis was prioritised**: Phase 4 closed with an explicit gap — the
EchoStar spectrum datapoint proved PIL-6's premise but from the **sell side**. EchoStar
realised value by *exiting* spectrum. PIL-6's actual investment claim is that *holding* a
licensed position is a durable asset, and that needed a buy-side test. `thesis.md`
recorded: *"IRDM is the correct buy-side test of PIL-6, and now the highest-value
unexamined name in the thesis."* This is that test.

---

## The buy-side test: PIL-6 passes

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$225.237M** | $216.906M | +3.8% |
| Operating income | **$34.008M** | $50.258M | **−32.3%** |
| Operating margin | **15.1%** | 23.2% | −8.1 pts |
| Net income | $9.679M | $21.968M | −55.9% |
| R&D | $5.53M | $4.279M | +29.2% |
| EPS (diluted) | $0.09 | $0.20 | −55% |

**IRDM is profitable, at the operating and net lines, on licensed L-band spectrum.**
That is the confirmation EchoStar could not provide: a licensee that **keeps** its
spectrum and monetises it through an operating business, rather than selling it.

**PIL-6's premise therefore survives both sides of the trade.** The sell side (EchoStar)
established the price of the asset — ~$27B of 2025 H2 gains against $15.0B of full-year
revenue. The buy side (IRDM) establishes that the asset can be *held* and made to
generate sustainable operating profit. A resource that can be profitably held **and**
profitably sold at 1.8× the holder's annual revenue is, by any reasonable definition, a
real asset rather than a permit.

**But note the direction of the margin.** IRDM's operating margin fell from 23.2% to
**15.1%** year over year while revenue grew 3.8%, and net income fell 55.9%. The asset is
durable; the *operating* business on top of it is under pressure. That distinction is
exactly what PIL-6 asserts — the licence is the asset, the service business is a
separate (and harder) proposition.

## The structural asymmetry: 66 satellites, licensed spectrum, and a duopoly that just consolidated

IRDM operates **66 LEO satellites with globally licensed L-band spectrum** and ~2.5M
subscribers across government, aviation, maritime and emergency services (per the
constitution's Tier 2 record). Three observations:

1. **The spectrum, not the constellation, is the scarce input.** Satellites can be
   rebuilt; L-band licences cannot be created. This is the same asymmetry EchoStar's
   gain quantifies.
2. **IRDM is being acquired by a launch company.** RKLB buys Iridium specifically to
   obtain spectrum, a constellation and a customer base it could not build — its own
   10-Q frames the deal as vertical integration toward a Starlink-like position.
3. **Under A1a/A1b** (proposed in the FLY artifact), this is coherent: RKLB's launch
   business is not where growth comes from, so it is buying the layer that does
   generate it. IRDM is a **value-pool acquisition**, not a capacity acquisition.

## DA-23 refinement — IRDM is clean, and that sharpens the rule

IRDM's reported operating income ($34.0M positive) is **correct** — verified by component
consistency and by operating margin plausibility (15.1% for a satellite telecom). VRT,
checked in the same batch, is likewise clean.

Combined with the four flipped cases, the pattern is now exact:

| Issuer | True value | XBRL value | Flipped? |
|---|---:|---:|:---:|
| SPCX | −143.0 | 143.0 | **yes** |
| YSS | −41.3 | 41.3 | **yes** |
| RKLB | −57.5 | 57.5 | **yes** |
| FLY | −95.2 | 95.2 | **yes** |
| IRDM | +34.0 | 34.0 | no |
| VRT | +637.9 | 637.9 | no |

**4 of 4 negative values flipped; 0 of 2 positive values flipped.**

**DA-23 is not a "sign-convention issue" — it is sign stripping.** The extract drops the
sign on negative values, so **every loss is reported as a gain of identical magnitude**,
and profitable issuers are untouched.

**The consequence is worse than the earlier framing implied.** Any screen ranking on
`operating_income` places the **worst loss-makers at the very top**: SPCX's $143M loss
outranks IRDM's $34M profit. This is not a data-quality footnote; it is an
inversion-generating defect, and DA-23 should be re-worded accordingly in the amendment
proposal.

---

## Carry-forwards

1. **PIL-6's evidence base is now two-sided** (sell side and buy side) and no longer
   rests on EchoStar alone.
2. **DA-23's amendment text should be rewritten**: "sign stripping on negative values"
   rather than "sign convention", with the ranking-inversion consequence stated.
3. **IRDM's declining margin is itself a finding** — the licence is durable, the service
   business is not automatically so. Phase 6 should test whether that decay is
   competitive (Starlink/D2D pressure) or cyclical.
4. **RKLB's acquisition of IRDM is now interpretable**: under A1a/A1b it is a
   value-pool purchase. That makes the deal thesis directly relevant to A1 and should be
   carried into the Phase 7 synthesis.
