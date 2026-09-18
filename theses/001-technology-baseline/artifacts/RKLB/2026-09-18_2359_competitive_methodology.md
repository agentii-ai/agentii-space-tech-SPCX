---
thesis_id: "001-technology-baseline"
pillar: PIL-6
ticker: RKLB
skill: competitive
mode: methodology
generated_at: 2026-09-18T23:59:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "826995c722a4"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "SIGN STRIPPING EXTENDS TO net_income AND EPS, not just operating_income — 7th confirmation, new scope"
  - da_id: "DA-08"
    chosen_reading: "launch market share measured on launch COUNT, the only disclosed denominator"
  - da_id: "DA-26"
    chosen_reading: "Q4 rows carry ANNUAL figures"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# RKLB / SPCX / SATS / VRT — Competitive Position

**Combined artifact covering four competitive views**, written at panorama resolution per the
thesis owner's stated priority: breadth over depth for thesis 001.

---

## 1. ⚠️ DA-23 EXTENSION — the sign stripping reaches net income and EPS

**This is the most important platform finding of this pass.** RKLB Q2 2026:

```
gross profit       $84.576M
operating expenses $142.090M
                  ──────────
gross profit - opex = -$57.514M      <- arithmetic, unambiguous
XBRL OperatingIncomeLoss = +$57.514M  <- reported
```

**Seventh confirmation of the operating-line flip, exact magnitude.** But note what else the
extract reports for the same quarter:

| Line | Extract shows | What it must be |
|---|---:|---|
| Operating income | **+$57.514M** | **−$57.514M** (component identity proves it) |
| Net income | **+$49.258M** | **−$49.258M** |
| **EPS (diluted)** | **+$0.08** | **−$0.08** |

**Why net income must also be flipped**: if the operating line is truly a $(57.514)M loss,
then a positive net income of $49.258M would require **+$106.772M of below-the-line income in
one quarter.** RKLB holds $2.129B of cash and $187.9M of marketable securities — at a
generous 4% that is ~$21M/quarter — and it carries $152.4M of debt. **$106.8M of
below-the-line income is not available to it.**

**Consequence, and it is severe: DA-23 is not confined to one line.** The extract drops the
sign on **negative values**, so **every** negative figure in the block is affected.
**Reported figures affected at RKLB: operating income, net income, and diluted EPS — three
lines, one quarter.**

**Why this matters more than the earlier six confirmations.** The register previously
recorded DA-23 as an `operating_income` defect. **It is a whole-statement sign defect.** Any
screen or ratio using **net income** or **EPS** from the metrics block on a loss-making
issuer is **reading a positive number for a negative one** — which is a strictly larger blast
radius than the operating-line version, because net income is the input to P/E, ROE, margin
screens and every screening factor in common use.

**Escalate to the DA-23 amendment: re-scope from `operating_income` to ALL signed lines.**

## 2. RKLB's actual competitive position

| Metric | Q2 2026 (corrected) | Q2 2025 | Change |
|---|---:|---:|---:|
| Revenue | **$234.066M** | $144.498M | **+62.0%** |
| Gross profit | $84.576M | — | **36.1% margin** |
| **Operating income** | **$(57.514)M** | $(59.639)M | **improving** |
| **Operating margin** | **−24.6%** | −41.3% | **+16.7 pts** |
| R&D / revenue | **35.2%** | 45.8% | −10.6 pts |
| Cash | $2.129B | $564.1M | **+277%** |

**Corrected, RKLB is improving fast: revenue +62%, operating margin up 16.7 points, R&D
intensity down 10.6 points, and $2.1B of cash.** The apparent profitability the extract
reports is an artefact; **the real trajectory is a company converging on break-even from
below.**

**But launch is not what is driving it** — established earlier and unchanged: **revenue +62%
with launch revenue −$2.1M.** The growth is space systems.

## 3. Launch competition, measured on the only disclosed denominator

**SPCX discloses launch counts; nobody discloses market share.** Using launch count:

| Operator | Q2 2026 launches | Note |
|---|---:|---|
| **SPCX (Falcon)** | **37** | of which **27 internal** (Starlink), 10 customer |
| **SPCX (Starship)** | **1** | all classified internal |
| **RKLB (Electron/Neutron)** | not separately disclosed | revenue fell |
| **ULA** | not disclosed | **equity-method; invisible at both parents** |
| **Blue Origin, Firefly, others** | FLY discloses no launch count | — |

**The competitive conclusion is the same one four other lines reached by different routes:
launch competition cannot be measured economically in this universe.** SPCX's 27 internal
launches carry **no inter-segment revenue** — they are capitalised into satellites. **So 73%
of the dominant provider's launches produce zero reported revenue**, and the remainder of the
market does not disclose counts at all. **A launch market-share table is not constructible
from public filings.**

**Register as a DA-08 consequence**, and note it is a **stronger** version of the earlier
"four critical duopolies are unpriced" finding: launch is not merely unpriced, it is
**denominatorless.**

## 4. Vertiv — the enabling layer is the healthiest business in the universe

| Metric | Q2 2026 | Q2 2025 | Change |
|---|---:|---:|---:|
| Revenue | **$3,274.3M** | $2,638.1M | **+24.1%** |
| Implied gross profit | $1,234.9M | — | **37.7% margin** |
| Operating income | **$637.9M** | $442.4M | **+44.2%** |
| **Operating margin** | **19.5%** | 16.8% | **+2.7 pts** |
| Net income | $497.8M | $324.2M | +53.5% |
| EPS (diluted) | $1.27 | $0.83 | +53.0% |

**VRT is clean** (EPS × 392.747M = $498.8M vs net income $497.8M — 0.2% gap).

**VRT's 19.5% operating margin puts it in the same tier as CW (19.3%) and KRMN (19.1%)** —
three unrelated industrial businesses converging on ~19%. **And it is expanding margin 2.7
points on 24.1% growth**, which is scarcity pricing in a functioning market, not a
bottleneck.

**This closes the loop on the orbital-compute case from the supply side.** The thermal
management supplier that an orbital compute buildout would need is **already growing 24% at a
19.5% margin serving terrestrial data centers.** It has no reason to prefer a new, smaller,
harder market — **the same revealed-preference structure SPCX showed from the demand side.**

## 5. DA-26 — VRT confirms in both lines, twice

| Row | Revenue | Operating income | What they are |
|---|---:|---:|---|
| Q2 2026 | $3,274.3M | $637.9M | genuine quarters |
| **Q4 2025** | **$10,229.9M** | **$1,829.7M** | **FY2025 ANNUAL figures** |
| **Q4 2024** | **$8,011.8M** | **$1,367.4M** | **FY2024 ANNUAL figures** |

**Twenty-third issuer confirmed**, and **the fourth where the defect propagates to both
revenue and operating income** (AMGN, TER, CW, VRT). FY2025 = Q1–Q3 $7,349.9M so annual
$10,229.9M implies Q4 2025 of $2,880.0M. **The annual reading is internally consistent.**

---

## Carry-forwards

1. **⚠️ DA-23 IS A WHOLE-STATEMENT SIGN DEFECT, NOT AN `operating_income` DEFECT.** At RKLB,
   **operating income, net income AND diluted EPS are all flipped** — three lines, one
   quarter. **Re-scope the DA-23 amendment.** The blast radius is larger than recorded:
   **net income is the input to P/E, ROE and every common screening factor**, so a loss-making
   issuer reads as profitable on any screen built from the metrics block.
2. **Corrected, RKLB is improving fast** — revenue +62%, operating margin **+16.7 pts** to
   −24.6%, R&D intensity −10.6 pts, $2.1B cash. **The trajectory is convergence on break-even
   from below.**
3. **Launch market share is not constructible.** 73% of SPCX's launches are internal and carry
   **no inter-segment revenue**; ULA is equity-method; RKLB and FLY do not disclose counts.
   **Launch is not just unpriced — it is denominatorless.** Stronger than the four-duopolies
   finding.
4. **VRT at 19.5% margin and +24.1% growth** joins CW (19.3%) and KRMN (19.1%) — three
   unrelated industrials converging at ~19%, while **expanding** margin on growth. **Scarcity
   pricing, not a bottleneck.**
5. **DA-26 at 23 of 23 issuers**, fourth with both-line propagation.
