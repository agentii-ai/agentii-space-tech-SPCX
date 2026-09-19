---
thesis_id: "004-tier0-spacex-anchor"
pillar: "PIL-5"
ticker: SPCX
skill: risk
mode: general-risk-factors-identification-assessment
generated_at: 2026-09-19T12:40:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-18
corpus_version: agentii-2026-09-18
data_class: slow
definitions_used:
  - da_id: "DA-19"
    chosen_reading: "Entity discontinuity — X merger 2025-03-28, xAI merger 2026-02-02 under common control, IPO 2026-06, five-for-one split 2026-05, Cursor pending. Growth rates across these boundaries mix real growth with entity change, so no risk figure below is quoted across a boundary without saying so."
entity_claims:
  - claim_id: "risk-coverage-ratio-h1-2026"
    ticker: SPCX
    metric: operating_cash_flow_coverage_of_investing
    value: 0.1005
    unit: ratio
    basis: "operating 3,466 / investing 34,487, H1 2026; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "SPCX 10-Q — cash flow statement, via 001's capital row; consumed"
  - claim_id: "risk-notes-coupon"
    ticker: SPCX
    metric: effective_interest_rate
    value: 0.0603
    unit: ratio
    basis: "40,869 notes at a 6.03% effective rate; 6M duration, six months ended 2026-06-30"
    period: "2026Q2"
    evidence_grade: DEMONSTRATED
    source: "001/artifacts/SPCX — consumed"
key_metrics:
  coverage_ratio_h1_2026: 0.1005
  notes_effective_interest_rate: 0.0603
---

# SPCX × risk × general-risk-factors-identification-assessment

**The funding structure, ranked by what would actually stop the build.** P5's claim is that
`CAPITAL` is the binding constraint; this artifact tests whether the risks that bind are capital
risks or something else.

## 1. 🔴 R-1 — The Cursor dilution is BLOCKING, and it is the only risk on the critical path

| | |
|---|---|
| **What** | **$60B all-stock** acquisition of Cursor (Anysphere, Inc.). Merger agreement entered **2026-06-16**; re-affirmed in an **8-K of 2026-08-14** |
| **Status** | **Pending — closing Q3 2026** |
| **Why it is `blocking`** | Round 4 made the headline SOTP **PRO-FORMA**. Cursor is now **inside** the anchor, so its consideration and **dilution are inputs to P1**, not sensitivities |
| **The exposure** | **V-5 previously recorded the dilution as *not determinable*.** The pre-close provisional existed precisely to avoid this dependency; the owner overrode it, and **the cost is stated rather than hidden** |
| **Severity** | **Blocking for P1.** Not "a risk" — a **prerequisite** |

**What must be found:** the share consideration. The 8-K of **2026-08-14** is the most recent
filing; `search_documents` located it, and `read_source_pages` is the route to its terms.
**A pro-forma headline cannot be computed without it.**

## 2. R-2 — The coverage ratio, and why it is the claim rather than a risk

```
H1 2026 operating cash flow   +$3,466M
H1 2026 investing            $(34,487)M     ← coverage ≈ 0.10×
H1 2026 financing           +$100,291M      ← IPO $85,675M + notes $40,869M
```

**A company with a $(143)M quarterly operating loss raised $85.7B in equity and $40.9B in notes,
and named data centers before launch facilities when describing the capex.**

**P5's falsifier** is `coverage >= 1.0×`. At **0.1005×** it is **an order of magnitude away** — so
this is not a near-threshold risk; it is the structural condition. **Internal cash flow covers
about a tenth of the build.**

## 3. R-3 — The notes are priced at a level that is itself a risk signal

**$40,869M at a 6.03% effective rate.** For a company of SPCX's scale and narrative, **6.03% is not
an investment-grade cost of debt.** It is a rate that embeds the funding-structure risk this pillar
names.

**And a further tranche followed:** an 8-K of **2026-06-26** records **$7.0B of 5.350% Senior Notes
due 2031** — **priced 68 bp inside** the earlier effective rate. **The direction matters:** the
second raise priced tighter, which is evidence the market's read of the structure **improved**
between the two. **Recorded because it cuts against the risk narrative**, and a risk register that
only accumulates confirming evidence is not a register.

## 4. R-4 — Control, float, and who can price the dilution

**P5's claim names the single-class control structure as determining who can price the Cursor
dilution.** Two facts:

1. **The constitution records NO index inclusion at ratification.** So the marginal buyer of the
   equity that funds the build is a **dated catalyst, not a standing assumption** — it must be
   recorded as such or dropped.
2. **Post-IPO equity moved 2,573 → 127,224 (49.5×).** A structural change of that magnitude means
   **the shareholder base that will vote on any further dilution is not the one that existed at
   IPO.**

**Unresolved here:** whether the Cursor consideration is Class A and whether the control structure
gives any holder a veto. **That is the same 8-K R-1 needs**, and it is why the two risks are one
investigation.

## 5. Risk register, ranked

| # | Risk | Class | Binds? |
|---|---|---|---|
| **R-1** | **Cursor dilution** | **Execution / event** | 🔴 **BLOCKING — P1 cannot be delivered without it** |
| **R-2** | Coverage **0.1005×** | **Structural** | ✅ **This IS P5's claim**, not a risk against it |
| **R-3** | Cost of debt **6.03% → 5.350%** | Market | ⚠️ **Improving**, and recorded as such |
| **R-4** | Control / float / index inclusion | Governance | ⚠️ **Open — same 8-K as R-1** |
| R-5 | **A4's ceiling on orbital compute** | **Constitutional** | ✅ Not a risk but a **bound** — the 1M-satellite filing is inadmissible as a valuation input. **Not a threat to the anchor; a limit on what the anchor may claim** |

## 6. What this establishes

**P5's claim is that internal cash flow does not cover the compute build, so the anchor's downside
is governed by the funding structure rather than any physical or demand constraint.**

**This artifact confirms it — with one qualification the plan did not anticipate:** the *binding*
item is not the funding structure in general but **one specific unbounded liability (R-1)**.
`CAPITAL` binds; but at this moment **`CAPITAL` binds through a single, dated, unresolved
disclosure.** That is a sharper statement of the constraint than "capital is scarce", and it is
what P5 should carry.
