---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: SATS
skill: risk
mode: methodology
generated_at: 2026-09-18T17:15:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-17"
    chosen_reading: "spectrum quantified by transaction value ($), not MHz — the only basis disclosed"
  - da_id: "DA-18"
    chosen_reading: "regulatory approval = FCC licence transfer completed; ITU coordination not separately confirmed"
  - da_id: "DA-24"
    chosen_reading: "operating_income is asset-sale-contaminated; the operating business must be read separately"
  - da_id: "DA-23"
    chosen_reading: "verified; SATS is NOT sign-stripped (EPS x shares reconciles to 0.3%)"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SATS — Regulatory Risk, Q1 2026

Source: Form 10-Q, accession `0001104659-26-058150`, quarter ended 2026-03-31;
consolidated with the Phase 4 cross artifact.

**Why SATS carries the P6 regulatory analysis**: it is the counterparty to the sector's
pricing reference — the ~$19.6B sale of AWS-4, H-Block and AWS-3 spectrum to SPCX — and
therefore the cleanest case of a regulatory asset changing hands.

---

## 1. The regulatory asset, separated from the operating business

The problem with reading SATS is that **DA-24 contaminates the income statement**:
2025 Q3 and Q4 operating income (460% and 118% of revenue) reflects a licence sale, not
operations. The Q1 2026 quarter is clean:

| Metric | Q1 2026 |
|---|---|
| Revenue | **$3,667.5M** |
| Operating income | **$392.8M** |
| Operating margin | **10.7%** |
| Net income | $146.9M |
| Net margin | 4.0% |

**Strip out the spectrum gain and EchoStar is a 10.7%-operating-margin, 4.0%-net-margin
telecom.** Against Phase 4's finding that the licences were worth ~1.8× annual revenue,
the read is:

> **The regulatory asset was worth more than the business that held it was earning from
> operations — roughly 27× the *gain-equivalent* of a single year of operating income.**

That is the cleanest available quantification of PIL-6's premise: the licence is the
asset, and the operating business is a thin margin on top of it.

## 2. Regulatory risk, enumerated

PIL-6 asserts that spectrum and orbital slots are **allocated before capital can be
deployed**. SATS's own transaction demonstrates the gates in sequence:

| Gate | Authority | Evidence |
|---|---|---|
| 1. Licence transfer approval | **FCC** | The SPCX–EchoStar transaction required FCC consent before closing; the transfer **completed**, so this gate passed |
| 2. International coordination | **ITU** | RKLB's 10-Q Iridium risk factors name the ITU explicitly alongside the FCC and DCSA as required consents — documentary evidence that ITU coordination is a live, named gate, not background |
| 3. Foreign investment review | **DCSA / CFIUS-adjacent** | Also named in the RKLB risk factors; for spectrum with defence users this is a separate, non-trivial gate |
| 4. Market access | national regulators | Per-country; not evidenced here |

**The structural point**: these are **sequential, not parallel** gates. Passing one says
nothing about the next — which is exactly the **DA-18** ambiguity (approval ≠ approval).
A thesis treating "regulatory approval" as a single event is understating the process by
three gates.

## 3. PIL-6's falsifier — and a disposition problem

| Field | Value |
|---|---|
| metric | `new_entrant_primary_spectrum_or_slot_grant_without_incumbent_acquisition` |
| threshold | 0, op `>` |
| source | `FCC_IBFS_or_ITU_Space_Network_List` |
| **Observed** | **not measured** |
| **Verdict** | **PENDING** — and structurally so |

**This analysis adds a third distinction to the disposition taxonomy.** Phase 4 proposed
`UNRESOLVABLE-FROM-PLATFORM` for PIL-6 because the FCC/ITU sources are public but
unreachable. Working the transaction in detail sharpens it:

- **The gate evidence is partially obtainable indirectly.** RKLB's Iridium risk factors
  *name* the FCC, ITU and DCSA as required consents — so the **existence and identity of
  the gates** is `DEMONSTRATED` from filings, even without FCC data.
- **The falsifier itself** (whether a new entrant ever gets primary coordination without
  buying it) still requires FCC IBFS / ITU Space Network List.

So PIL-6 splits: **the premise is evidenced from filings; the falsifier is not.** That is
a better outcome than Phase 4 recorded, and it means PIL-6 need not wait on external data
to contribute to the synthesis.

## 4. DA-23 / DA-24 — SATS is the instructive non-case

SATS is **not** sign-stripped (EPS × shares reconciles to 0.3%), but **is**
asset-sale-contaminated under **DA-24**. Two different defects, and SATS exhibits exactly
one of them.

**This is the cleanest demonstration that the two are independent**, and it validates
keeping them as separate register entries rather than merging them into one
"operating_income is unreliable" rule. The remedies coincide — verify against components —
but the diagnoses differ, and a merged entry would have obscured that SATS is a genuine
10.7% margin business whose statement was inflated, rather than a loss-maker whose sign
was dropped.

---

## Carry-forwards

1. **PIL-6's premise is now evidenced directly from SATS** — a 10.7% operating margin
   business holding an asset worth ~1.8× annual revenue. The strongest P6 datapoint
   after Phase 4's gain quantification.
2. **DA-18 (approval ≠ approval) is now documented with named gates** (FCC → ITU → DCSA),
   which upgrades it from an ambiguity to a checklist.
3. **PIL-6's disposition should be split**: premise `DEMONSTRATED` from filings; falsifier
   `UNRESOLVABLE-FROM-PLATFORM`. Phase 4's monolithic framing was too coarse.
4. **DA-23 and DA-24 validated as independent** — SATS exhibits one and not the other.
