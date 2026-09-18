---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: SPCX
skill: recent-quarter
mode: methodology
generated_at: 2026-09-18T23:59:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "registry-1.0.0"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "sign stripping applies to ALL signed lines including net income and EPS (extended scope, RKLB-confirmed)"
  - da_id: "DA-26"
    chosen_reading: "Q4 rows carry ANNUAL figures — 23 of 23 issuers"
  - da_id: "DA-27"
    chosen_reading: "fiscal-period labels derive from calendar quarters — 4 of 4 non-calendar issuers"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# Freshness Anchor, Sector Overview, Peer Bench, Ratio Analysis, What-If

**Combined artifact covering five cross-cutting views** at panorama resolution. This is the
**freshness anchor** for every `DEMONSTRATED` metric in the thesis.

---

## 1. Freshness anchor — the latest reported quarter for the universe

**As of 2026-09-18, the thesis's `as_of` date, the freshest period available is Q2 2026
(calendar) for most issuers.** Non-calendar year-ends report different periods:

| Ticker | Latest period | Period end | Note |
|---|---|---|---|
| **SPCX** | **Q2 2026** | 2026-06-30 | **post-IPO; three segments; entity changed** |
| TER, CW, KTOS, HEI | Q2 2026 / Q1 FY2026 | varies | HEI is on a 31 Oct year, **DA-27 applies** |
| PL | Q1 FY2026 | 2026-04-30 | January year-end, **DA-27 applies** |
| AVAV | Q1 FY2026 (labelled) | 2026-04-30 | **unusable — no net income** |
| HAWK | Q2 2026 | 2026-06-30 | **unusable — post-IPO discontinuity** |
| WWD | Q2 FY2026 (labelled) | 2026-06-30 | September year-end, **DA-27 applies** |

**Rule for every DEMONSTRATED metric in this thesis: it is as of its issuer's latest filed
period, not as of `as_of`.** The two differ by up to one quarter, and for non-calendar issuers
the *label* differs from the issuer's own calendar (**DA-27**). **Any cross-issuer comparison
must normalise the period before comparing levels.**

## 2. Sector overview — the TAM question, answered structurally

**Total revenue, one quarter, all 35 universe tickers combined ≈ $100B.** Of that:

| Group | Quarterly revenue | Share |
|---|---:|---:|
| **SPCX (all three segments)** | **$7,814M** | 8% |
| Three pharma buyers | $39,634M | **40%** |
| Three enabling-layer names (ex-SPCX) | very large | — |
| **All pure-play space companies combined** | **~$1,100M** | **1%** |

**The "space economy" as this universe defines it is a rounding error inside the companies
that touch it.** The addressable market being measured is **~1% of the revenue of the
companies measured.**

**Concentration**: SPCX dominates space revenue entirely — its **$7,814M** quarterly total
exceeds the **~$1,100M** of every pure-play competitor combined by **7×**. **Even excluding
Connectivity and AI, SPCX's $962M Space segment is ~87% of the pure-play cohort's revenue.**

**Regulatory framing**: PIL-6's premise — spectrum and slots are finite, allocated, and
priced — is **DEMONSTRATED** (SATS $27B; SPCX–EchoStar $19.6B with $856M paid in cash in H1
2026). **The falsifier needs FCC IBFS / ITU sources outside the corpus.**

## 3. Peer bench — launch technology line

| Issuer | Revenue | Growth | Gross margin | Operating margin | R&D/revenue |
|---|---:|---:|---:|---:|---:|
| **SPCX** | $7,814M | **+91.9%** | **55.3%** | −1.8% | 45.4% |
| **SPCX Space** (segment) | $962M | +29.0% | **65.8%** | **−56.3%** | 111.9% |
| **RKLB** | $234.1M | +62.0% | 36.1% | **−24.6%** | 35.2% |
| **FLY** | — | **+657%** | 20.3% | −80.9% | **60.8%** |

**The launch cohort's defining feature: growth and margin are inversely related, and gross
margins span 20.3% to 65.8% while every operating margin is negative.**

**SPCX's Space segment has the best gross margin in the universe (65.8%) and the worst
operating margin (−56.3%) in this cohort** — the fixed-cost-absorption finding in its purest
form, and the reason the thesis distinguishes **gross economics** from **funding decisions**.

**No issuer discloses a launch price at cadence except RKLB** ($14,667/kg, basis B) — and
RKLB's launch revenue is **declining**.

## 4. Ratio analysis — and why it is mostly not safe here

**The thesis's ratio toolkit is badly constrained, and the constraint is the finding:**

| Ratio | Availability |
|---|---|
| **$ / kg to orbit** | **one issuer only** (RKLB, basis B) |
| **P/E, ROE, margin screens on net income** | **UNSAFE** — DA-23 strips signs on **net income and EPS**, so loss-makers read positive |
| **Quarterly trend ratios** | **UNSAFE** — DA-26 puts annual figures in quarter rows, 23 of 23 issuers |
| **Fiscal-period comparisons** | **UNSAFE** for non-calendar issuers — DA-27, 4 of 4 |
| **Component-identity checks** | **SAFE** — gross profit and opex are positive and unaffected; **this is the only reliable detector** |
| **Gross margin** | **SAFE** — computed from unsigned lines |
| **Operating margin** | **UNSAFE on loss-makers** (DA-23); safe on profitable issuers |
| **Equity/assets, leverage** | **SAFE** |

**The safe set is narrow: gross margins, balance-sheet ratios, and component identities.**
**Everything computed from net income, EPS, or a quarterly series must be rebuilt from the
filing rather than from the metrics block.**

**The extended DA-23 scope makes this materially worse than previously recorded**: a
loss-making issuer reads as **profitable on every screen built from the metrics block**,
because operating income, net income and EPS are all flipped consistently.

## 5. What-if — the two theses that would change the answer

**What if launch cost reached the propellant floor ($46/kg)?**
- **The floor changes no verdict.** PIL-1's falsifier needs **price**, and price is not cost —
  and no issuer discloses price at cadence. **Cheaper launch does not fire the falsifier.**
- **It would not fund orbital compute either.** SPCX's constraint on AI compute is **power and
  customer concentration**, not launch cost; VRT's is **manufacturing scale**. **Both would
  still bind at $0/kg.**
- **What it would do**: change **Space segment economics**, which are already 65.8% gross
  margin. **The binding term there is Starship R&D, not launch cost.**

**What if a listed pharma disclosed commercial microgravity manufacturing?**
- **PIL-4's falsifier fires immediately** — it is binary and observable. **That single
  disclosure would convert PIL-4 from HOLDS to FALSIFIED**, and it is the cheapest possible
  test in the thesis.
- **What would have to be true**: the process must beat a **72% incumbent gross margin**.
  **No such number exists publicly**, which is why the line's economic test is UNRESOLVABLE.

**The common structure**: **both what-ifs turn on a disclosure that does not exist**, and in
both cases the physical or economic bound is **not** the binding term. **The thesis's open
questions are disclosure questions, not physics questions.**

---

## Carry-forwards

1. **Freshness rule**: every DEMONSTRATED metric is as of its issuer's latest filed period,
   **not `as_of`** — and for non-calendar issuers the *label* differs from the issuer's
   calendar (DA-27). **Normalise periods before comparing levels.**
2. **The "space economy" here is ~1% of the revenue of the companies that touch it**, and
   SPCX is **7× every pure-play competitor combined.** **The market being measured is a
   rounding error inside the companies measuring it.**
3. **The ratio toolkit's safe set is narrow**: gross margins, balance-sheet ratios, component
   identities. **Everything from net income, EPS or a quarterly series must be rebuilt from
   the filing** — and the extended DA-23 scope makes that worse than previously recorded,
   because **loss-makers read profitable on every metrics-block screen.**
4. **Both what-ifs turn on disclosures that do not exist, not on bounds that bind.** The
   thesis's open questions are **disclosure questions, not physics questions** — which is the
   same conclusion the register reached from three different UNRESOLVABLE verdicts.
