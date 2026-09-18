---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: operational-kpi
mode: methodology
generated_at: 2026-09-18T23:10:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "0730fd170124"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "operating_income verified; SPCX CONFIRMED flipped at consolidation (-143 reported as +143)"
  - da_id: "DA-20"
    chosen_reading: "AI segment revenue classified TERRESTRIAL — not in-orbit, not for-orbit. Reported side by side per §1c."
  - da_id: "DA-01"
    chosen_reading: "launch price/cost bases unchanged; this artifact adds VOLUME, not price"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# SPCX — Operating Baseline (Q2 2026, post-IPO)

Source: Form 10-Q, accession `0001628280-26-052535` (quarter ended 2026-06-30). **This is a
post-IPO filing that materially revises every prior SPCX artifact in this thesis.**

---

## 1. THE DECISIVE DATUM: launch volume is FALLING at the launch monopoly

| Key business metric | Q2 2026 | Q2 2025 | Change | H1 2026 | H1 2025 | Change |
|---|---:|---:|---:|---:|---:|---:|
| **Mass to orbit (t)** | **485** | 652 | **−25.6%** | **1,041** | 1,102 | **−5.5%** |
| — customer payloads | 87 | 88 | −1.1% | 132 | 163 | −19.0% |
| — **internal payloads** | **397** | 563 | **−29.5%** | 908 | 938 | −3.2% |
| **Falcon launches** | **37** | 45 | **−17.8%** | **77** | 81 | **−4.9%** |
| — customer launches | 10 | 9 | +11.1% | **17** | 21 | **−19.0%** |
| — **internal launches** | **27** | 36 | **−25.0%** | 60 | 60 | 0.0% |
| Starship launches | 1 | 1 | — | **1** | 3 | **−66.7%** |

**SPCX calls mass to orbit "a key indicator of SpaceX's capacity and scalability." It fell
25.6% year over year. Falcon launches fell 17.8%. Starship launches fell from 3 to 1.**

**This is the single most important operational datum the thesis has produced, and it runs
opposite to the premise the universe was built on.** The company with the world's only
high-cadence reusable launch franchise **launched fewer times this quarter than last**, and
the contraction is concentrated in **internal** launches (−25.0%) — i.e. **Starlink
deployment is slowing**, which is the demand that was supposed to justify the cadence.

**A1b is now falsified on the issuer's own metrics.** The constitution's A1 split proposed
A1a (launch cost is the master *cost* variable — holds) vs A1b (launch is the master *value*
variable — does not hold). **SPCX's own disclosure settles it**: launches −17.8% while
revenue +91.9%, and the Space segment is 12.3% of revenue and loss-making.

## 2. The segment structure: launch is a loss leader inside a connectivity company

| Segment | Q2 2026 revenue | % of total | Operating income | **Operating margin** |
|---|---:|---:|---:|---:|
| **Connectivity** (Starlink) | **$4,291M** | **54.9%** | **$1,656M** | **+38.6%** |
| **AI** (Grok, X, compute) | **$2,561M** | **32.8%** | not disclosed | — |
| **Space** (launch + Dragon) | **$962M** | **12.3%** | **$(542)M** | **−56.3%** |
| **Consolidated** | **$7,814M** | 100% | $(143)M | −1.8% |

**The company anchored as the thesis's core listed holding earns 12.3% of its revenue from
space launch and loses money doing it.** Connectivity — a terrestrial-market broadband
business delivered via satellites — is 54.9% of revenue at a 38.6% operating margin.

**And the Space segment's loss is NOT a launch-economics problem:**

```
Space Q2 2026:  revenue         $962M
                cost of revenue $329M   ->  gross profit $633M  =  65.8% gross margin
                R&D           $1,076M   <-   111.9% of segment revenue
                SG&A             $99M
                loss from ops  $(542)M   (identity closes exactly)
```

**A 65.8% gross margin — the highest in the universe — destroyed by Starship development
R&D.** Cost of revenue was **flat** (−0.3%) while revenue rose 29.0%, so **the marginal
Falcon launch is highly profitable**. The loss is a **development-funding decision**, not an
operating failure. **Register the distinction: Falcon launch economics are good; Starship
development consumes $1.08B per quarter.**

## 3. THE ORBITAL-COMPUTE DISCONFIRMATION — SPCX is building on the ground

**The strongest possible test of PIL-5 is the company with the cheapest orbital access. If
orbital compute were going to close anywhere, it would close here first.**

```
Q2 2026 nameplate compute draw:  1.4 GW     (Q2 2025: 0.4 GW)   +250%
H1 2026 capex increase:          $21,511M
  attributed first to:           "the build out of DATA CENTERS and related
                                  infrastructure, and space launch facilities"
Cursor Merger:                   $60,000M implied equity value, all-stock, closing Q3 2026
```

**SPCX is deploying 1.4 GW of terrestrial AI compute — 3.5× its own year-ago figure — and
its capital-expenditure narrative names data centers *before* launch facilities.** The AI
segment is described as *"AI computational infrastructure"* with **no mention of orbit
anywhere in the segment definition.**

**And SPCX states its own allocation intent explicitly**: *"We allocate a significant amount
of launch capacity to our Connectivity segment, and expect to allocate a significant amount
to our AI segment in the future."* **Launch capacity is being allocated to a segment whose
compute sits on the ground.**

**PIL-2's falsifier does not fire — but this is the closest call in the thesis, and the
DA-20 distinction is what decides it.** SPCX discloses AI-infrastructure revenue. Applying
the four readings side by side, as §1c requires:

| Reading | Applies to SPCX's AI segment? |
|---|---|
| compute **in** orbit | **No** — data centers are terrestrial; "nameplate compute draw" counts installed GPUs in data centers |
| compute **for** orbit | No |
| communications **from** orbit | No |
| **terrestrial compute, satellite-delivered connectivity** | **Yes** |

**Verdict: not orbital-compute revenue on any of the three readings the falsifier intends.
PIL-2 HOLDS.** But the case for `UNRESOLVABLE` weakens: **the disclosure SPCX would need to
make is now adjacent to one it actually makes**, and a reader who conflates "AI
infrastructure" with "orbital compute" would wrongly fire the falsifier. **Register as a
false-positive trap for any future analyst on this pillar.**

**The economic reading is unambiguous**: the one company that could put compute in orbit for
the least money is putting it on the ground, at scale, and financing it with the largest IPO
in history. **Orbital compute is not being out-competed by terrestrial compute — it is being
out-*chosen* by the only company positioned to do both.**

## 4. Starlink: volume-driven growth at a halving price

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---:|---:|---:|
| Starlink subscribers | **12.0M** | 6.0M | **+101.2%** |
| **Starlink ARPU** | **$66/mo** | $85/mo | **−22.4%** |
| Connectivity revenue | $4,291M | $2,588M | +65.8% |
| — consumer subscribers | +$764M | | |
| — **government / aviation / maritime / enterprise** | **+$939M** | | |
| Connectivity gross margin | **52.0%** | — | |
| Connectivity R&D | $294M | $143M | **+105.6%** |

**Subscribers doubled; ARPU fell 22.4%.** SPCX attributes it to *"international expansion
and the addition of lower priced service plans."* **Revenue per subscriber is falling at
half the rate subscribers are being added — growth is being bought with price.**

**And the enterprise/government half grew MORE than the consumer half** ($939M vs $764M).
**The consumer business — the one the Starlink narrative is built on — is the slower and
lower-quality half of Connectivity's growth.**

## 5. Capital structure: the largest IPO in history, and what it is funding

```
H1 2026 operating cash flow    +$3,466M
H1 2026 investing              $(34,487)M
H1 2026 financing             +$100,291M
   IPO net proceeds             $85,675M   (638.9M shares at $135.00)
   SpaceX Notes               +$40,869M   (6.03% effective rate)
   bridge loan repayment      $(33,406)M
   EchoStar spectrum payments     $856M   (installments on the $19.6B deal)
```

**A company with a $541M quarterly net loss raised $85.7B and is spending $34.5B per half
on investing — most of it data centers.** The EchoStar spectrum payments appearing as a
cash-flow line confirms PIL-6's premise **in cash**, not just in a headline price.

**Cursor Merger**: a call option exercised in June 2026 to acquire Anysphere (Cursor) at a
**$60B implied equity value in Class A stock**, expected to close Q3 2026. **A $60B all-stock
acquisition by a loss-making issuer — P11 in-flight M&A treatment applies, and the
dilution math is not yet determinable.**

## 6. DA-23 re-confirmed at consolidation

Consolidated loss from operations **$(143)M** — matching the earlier SPCX artifact's finding
that the extract reports this loss with the sign stripped as **+143**. **Independent
re-confirmation from the MD&A table, which prints the loss with its sign intact.**

---

## Carry-forwards

1. **LAUNCH VOLUME IS FALLING AT THE LAUNCH MONOPOLY.** Mass to orbit **−25.6%**, Falcon
   launches **−17.8%**, internal launches **−25.0%**, Starship launches 3→1. **A1b is
   falsified on the issuer's own key metrics.** Escalate to the synthesis and the
   constitution amendment queue.
2. **The Space segment is 12.3% of revenue and loses $(542)M/quarter — but at a 65.8% GROSS
   margin.** The loss is **Starship development R&D ($1,076M/qtr), not launch economics**.
   **Falcon launch economics are good; this is a funding decision.** Register the distinction.
3. **THE ORBITAL-COMPUTE DISCONFIRMATION: SPCX is deploying 1.4 GW of TERRESTRIAL compute**
   (3.5× y/y), with capex naming data centers *before* launch facilities, and allocating
   launch capacity to that segment. **The one company positioned to do both chose the
   ground.** PIL-2 HOLDS on the DA-20 four-way reading — **and that reading is now a
   documented false-positive trap**, since "AI infrastructure" is adjacent to but not
   "orbital compute."
4. **Starlink ARPU −22.4% against subscribers +101.2%**, and the enterprise/government half
   outgrew the consumer half. **Growth is being bought with price, and the consumer story is
   the weaker half.**
5. **$60B all-stock Cursor acquisition pending, Q3 2026 close** — P11 in-flight M&A, dilution
   undeterminable.
6. **DA-23 re-confirmed at consolidation** against the MD&A table.
