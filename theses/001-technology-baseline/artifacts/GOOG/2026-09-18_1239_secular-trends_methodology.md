---
thesis_id: "001-technology-baseline"
pillar: PIL-2
ticker: GOOG
skill: secular-trends
mode: methodology
generated_at: 2026-09-18T15:45:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e6b41dbb2426"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-04"
    chosen_reading: "orbital compute = compute IN orbit (Suncatcher). Compute-for-orbit and comms-from-orbit excluded"
  - da_id: "DA-11"
    chosen_reading: "Alphabet discloses no compute-draw metric; SPCX's IT-load convention does not transfer"
  - da_id: "DA-16"
    chosen_reading: "Suncatcher graded CLAIMED throughout — no flight, no prototype, no filing"
evidence_grade: CLAIMED
deal_security_basis: not_applicable
unresolvable: false
---

# GOOG — Orbital Compute Exposure, Q2 2026

Source: Form 10-Q, accession `0001652044-26-000071`; **Project Suncatcher is `CLAIMED`
only** — press and Google Research publications, no SEC filing.

**Why GOOG is Deep-tier**: it is the only listed issuer with a disclosed orbital-compute
*engineering* programme, and Phase 2 identified it as the sector's reference design.

---

## 1. Alphabet's financial scale — the asymmetry that makes Suncatcher credible and irrelevant

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$119,796M** | $96,428M | +24.2% |
| Operating income | **$40,770M** | $31,271M | +30.4% |
| Operating margin | **34.0%** | 32.4% | +1.6 pts |
| Net income | **$112,193M** | $28,196M | +298% |
| R&D | $18,219M | $13,808M | +32.0% |

**Two observations, in tension:**

**(a) Suncatcher is affordable at a scale no space company can match.** Alphabet's
*quarterly R&D* is **$18.2B** — roughly **20×** SPCX's entire Space segment revenue
($962M/quarter) and about **78×** RKLB's quarterly revenue ($234M). A programme of two
prototype satellites is a rounding error to Alphabet and an existential bet to anyone
else in the universe. That asymmetry is real and structural.

**(b) The same scale makes Suncatcher financially irrelevant to Alphabet.** Even a
wildly successful orbital-compute business would be immaterial against a $119.8B
quarterly revenue base. **Alphabet has no financial need to make Suncatcher work,
which is precisely why its timeline should be discounted** — a programme with no
revenue pressure slips. This is the opposite of SPCX, where orbital compute is
narratively load-bearing.

**For PIL-2's falsifier this cuts both ways**: an Alphabet orbital-compute revenue
disclosure is the *most likely* to appear (they have the engineering depth) and the
*least likely* to be segmented (it would be immaterial). The falsifier may fire late
even if the technology works.

## 2. A real anomaly in Alphabet's own numbers — flagging, not explaining

```
operating income  $40,770M
net income       $112,193M
ratio              2.75x
```

**$71.4B of below-the-line income** — more than the entire operating profit. This is
possible (unrealised investment gains, notably in non-marketable securities) but it is
large enough to distort any margin comparison drawn on net income. Alphabet's
**operating** margin (34.0%) is the clean comparator; the **net** margin is not.

**Cross-check**: EPS $9.23 × 12,122M weighted shares = **$111.9B** ≈ reported $112.193B
(0.3% gap), so the figure is internally consistent and **not** a DA-23 sign-stripping
case. Alphabet is profitable and therefore untouched by that defect.

**Carry to Phase 6**: any orbital-vs-terrestrial comparison using Alphabet's *net*
margin would be comparing investment gains to an operating business.

## 3. Suncatcher against Phase 2's derived envelope

Phase 2 derived that 1 MW of continuous orbital load requires **~5,080 m² of array** and
**~2,419 m² of radiator at 300 K**. Against Alphabet's published claims:

| Suncatcher claim | Status | Phase 2 test |
|---|---|---|
| TPUs in LEO, two prototypes targeted early 2027 | `CLAIMED` | No flight data; F4 radiation tolerance unproven for TPUs at LEO |
| "Solar panels up to 8× more productive in the right orbit" | `CLAIMED` | **Directionally supported** by F1 — no eclipse duty cycle in sun-synchronous dawn-dusk orbit, and no atmosphere. But "8×" is orbit-dependent and the claim does not state the reference terrestrial capacity factor |
| 81-satellite reference configuration | `CLAIMED` | Nothing in F1/F2 contradicts a small constellation |
| Compute throughput per satellite | **not stated** | Cannot be tested against the envelope |

**The honest assessment**: Alphabet's claims are **not contradicted** by the physics —
the 8× figure is plausible for a dawn-dusk SSO with no eclipse. But the claims are also
**not yet testable**, because no compute-per-satellite figure has been published, and
without it the radiator and array derivations cannot be checked.

**This is PIL-2's cleanest open item**: the reference design exists, the physics is
consistent with it, and the one number that would settle it has not been disclosed.

## 4. DA-23 extended — Alphabet clean

| Issuer | True | XBRL | Flipped? |
|---|---:|:---:|:---:|
| SPCX, YSS, RKLB, FLY | negative | positive | **yes (4/4)** |
| GOOG, IRDM, VRT, UTHR, NVDA | positive | positive | no (5/5) |

**CORRECTION (2026-09-18)**: this artifact originally read *"7 of 7 negative values
flipped; 5 of 5 positive values clean, across 12 issuer-quarters."* **That was wrong.**
The correct census at the time was **4 of 4 negative, 5 of 5 positive — 9
issuer-quarters.** I had conflated the running total with the negative count. The *rule*
is unaffected (zero exceptions either way), but the number was not counted and is
corrected here.

The rule — *the extract strips the sign on negative values* — remains one of the
best-evidenced findings in the thesis and carries no exceptions.

---

## Carry-forwards

1. **Suncatcher's missing number is compute-per-satellite.** Phase 6 should state that
   PIL-2's falsifier is untestable against Suncatcher until it is published.
2. **Alphabet's scale cuts both ways** — capability and indifference. Both belong in the
   synthesis; neither alone.
3. **The net/operating income gap (2.75×)** should not propagate into Phase 6 ratios.
4. **DA-23 now carries 12 issuer-quarters of evidence with zero exceptions** and should
   be ratified. Its remedy — verify against components — belongs in the constitution,
   not in every artifact.
