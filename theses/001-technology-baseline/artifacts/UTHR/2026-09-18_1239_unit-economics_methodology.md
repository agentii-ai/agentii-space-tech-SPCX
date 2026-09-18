---
thesis_id: "001-technology-baseline"
pillar: PIL-4
ticker: UTHR
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T15:55:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-22"
    chosen_reading: "Varda figures CLAIMED-only per Q-4; they can inform but never satisfy a falsifier"
  - da_id: "DA-16"
    chosen_reading: "Varda's ~50 kg/mission is CLAIMED (press); UTHR's partnership disclosure is DEMONSTRATED"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; UTHR clean (profitable issuer)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# UTHR — Microgravity Economics, Q2 2026

Source: Form 10-Q, accession `0001082554-26-000027`.

**Why UTHR matters**: it is the listed proxy (P6) for Varda Space Industries and the only
listed counterparty to a microgravity-manufacturing partnership. Phase 5's PIL-4 test
runs through this company.

---

## 1. UTHR is a high-margin specialty pharma — and microgravity is invisible in it

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---|---|---|
| Revenue | **$783.3M** | $798.6M | **−1.9%** |
| Gross profit | **$683.8M** | — | **87.3% margin** |
| Operating income | **$330.8M** | $364.5M | −9.2% |
| Operating margin | **42.2%** | 45.6% | −3.4 pts |
| R&D | $146.3M | $134.0M | +9.2% |
| Net income | $333.0M | $309.5M | +7.6% |
| EPS (diluted) | $7.27 | $6.41 | +13.4% |

**An 87.3% gross margin is the number that matters for PIL-4.** It sets the bar any
microgravity manufacturing process must clear: to be interesting to a company like UTHR,
an orbital process must beat — or enable something unavailable from — a terrestrial
process that already runs at 87% gross margin.

**And microgravity is nowhere in these numbers.** UTHR's revenue *declined* 1.9% year
over year. There is no microgravity revenue line, no orbital cost line, and no mention of
Varda in the XBRL extract at all. The partnership announced in May 2026 targets first
samples "as early as 2027" — so **at Q2 2026 it has produced zero financial footprint**,
exactly as expected.

## 2. PIL-4's falsifier, evaluated honestly

| Field | Value |
|---|---|
| metric | `listed_pharma_microgravity_commercial_manufacturing_disclosure` |
| threshold | 0, op `>` |
| **Observed** | **0** — no commercial-scale disclosure from UTHR, MRK, BMY or AMGN |
| **Verdict** | **HOLDS** — and this is a *measured* zero, not an unexamined one |

**PIL-4 holds.** No listed pharmaceutical company has disclosed commercial-scale
microgravity manufacturing. The UTHR–Varda partnership is a research/pilot arrangement by
its own description, targeting first samples in 2027.

**But the pillar's economic test remains unexecutable**, and it is worth being precise
about why. Phase 5's plan called for **value-per-kg-returned vs cost-per-kg-returned**.
Neither term is available:

| Term | Status |
|---|---|
| Value per kg returned | **Not disclosed.** Varda has no revenue; UTHR discloses no microgravity product economics |
| Cost per kg returned | **Not disclosed.** Varda is private; its ~$329M raised and ~50 kg/mission are `CLAIMED` press figures only |
| Fully-loaded comparison | **Not possible.** Under Q-4, private figures may inform but can never *satisfy* a falsifier |

**This is the clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case in the thesis.** Unlike
PIL-6 (data public but unreachable from the platform) and P5 (data commercially
licensed), PIL-4's missing figures **do not exist publicly at all** — they are inside a
private company's books. The disposition under §1c applies: the pillar is recorded
unresolvable with the specific disclosure that would resolve it named.

**What would resolve it**: Varda disclosing cost per kg returned (unlikely while
private), or UTHR disclosing economics of its microgravity programme in a quarterly
filing (possible from 2027 if samples progress), or Varda listing.

## 3. The structural read: microgravity is a *quality* play inside a quality business

UTHR's 42.2% operating margin on $783M quarterly revenue means the company can fund
microgravity experimentation from operating cash flow indefinitely without it mattering.
**That is both PIL-4's strength and its weakness**:

- **Strength**: the counterparty is financially robust; the partnership will not collapse
  for lack of funding.
- **Weakness**: precisely *because* it doesn't matter, there is no pressure to disclose
  how it is going. UTHR has no obligation to break out a programme that is immaterial —
  the same structural problem that makes PIL-2's falsifier hard to fire at Alphabet.

**A pattern across pillars**: in both cases, the listed counterparty is large enough that
the space initiative is immaterial, which suppresses the disclosure that would let the
falsifier fire. Worth stating once in the Phase 7 synthesis rather than rediscovering it
per pillar.

## 4. DA-23 — UTHR clean

UTHR's operating income ($330.8M) is correct: 87.3% gross margin less R&D and SG&A at
plausible ratios yields it. It is a profitable issuer and therefore untouched.

**CORRECTION (2026-09-18)**: this artifact originally claimed *"7 of 7 negative values
flipped, 5 of 5 positive values clean."* **Wrong** — the correct census was **4 of 4
negative, 5 of 5 positive.** The running total had been conflated with the negative
count. The rule is unaffected; the figure was not counted and is corrected here.

---

## Carry-forwards

1. **PIL-4 HOLDS but its economic test is `UNRESOLVABLE-FROM-PUBLIC-SOURCES`.** Name the
   resolving disclosure: Varda's cost per kg returned, or UTHR's programme economics.
2. **The "immaterial-to-the-counterparty" disclosure suppression** is now observed at two
   pillars (PIL-2/Alphabet, PIL-4/UTHR) and belongs in the synthesis as a named pattern.
3. **UTHR's 87.3% gross margin is the hurdle rate** any microgravity process must clear —
   carry it into Phase 6 as the terrestrial benchmark for pharmaceutical value.
4. **UTHR revenue declined 1.9% YoY** — a reminder that the counterparty's own business is
   not growing, so microgravity is optionality rather than a response to pressure.
