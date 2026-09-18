---
thesis_id: "001-technology-baseline"
pillar: PIL-1
ticker: FLY
skill: unit-economics
mode: methodology
generated_at: 2026-09-18T14:50:00-04:00
constitution_pin: "1.2.0"
assumption_pin: "2"
skill_pin: "e87ee63269a2"
as_of: 2026-09-18
corpus_version: "UNPINNED"
definitions_used:
  - da_id: "DA-01"
    chosen_reading: "bases A and B are NOT DISCLOSED by FLY — reported as an absence, not estimated"
  - da_id: "DA-07"
    chosen_reading: "no mass-to-orbit disclosure; revenue only"
  - da_id: "DA-21"
    chosen_reading: "Launch vs Spacecraft Solutions — FLY's own segment split"
  - da_id: "DA-23"
    chosen_reading: "operating_income verified against components; confirmed flipped a 4th time"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: false
---

# FLY — Unit Economics, Q2 2026

Source: Form 10-Q, accession `0001860160-26-000023`, filed 2026-08-11. Pages 6, 15, 34,
36, 40 read via outline.

---

## 1. RKLB's per-launch disclosure is unique — confirmed

FLY's 10-Q contains **no `cost per launch` and no `revenue per launch` metric**. Neither
does SPCX's. RKLB alone discloses both. **This is now a settled question**: the
demonstrated basis-B anchor established in the RKLB artifact is a single-issuer
disclosure, not an industry convention.

**Consequence for PIL-1**: basis B is `DEMONSTRATED` for exactly one vehicle-and-issuer
pair (Electron/RKLB). For Falcon 9 and Alpha it remains `MODELED` or absent. PIL-1's
verdict still holds — the one demonstrated marginal cost is 15× the threshold — but it
rests on a narrow evidential base that will not widen without a comparable disclosure.

## 2. DA-23 confirmed a fourth time, again against the filing's own prose

```
  FLY Q2 2026
    gross profit − operating expenses = $23.875M − $119.072M = −$95.197M   ← arithmetic
    XBRL OperatingIncomeLoss                                 =  +$95.197M  ← reported
```

Page 6 states it in the filing's own words: *"gross profit of $23.9M, **operating loss
of $95.2M**, net loss of $92.3M, and basic/diluted EPS of **−$0.57**."*

**DA-23 is now 4 of 4 issuers** (SPCX, YSS, RKLB, FLY) and **6 of 6 issuer-quarters**
where components could be checked. Every instance has matching magnitude and inverted
sign; two instances (RKLB, FLY) are contradicted by the filing's own narrative.

**Also note**: FLY again passes the weak EPS test ($0.57 × 161.8M = $92.2M ≈ $92.3M
reported net loss) *while being flipped*. This is the third confirmation that the EPS
test is unreliable and the **component identity is the correct discriminator** — as
refined in the RKLB artifact.

## 3. The finding that matters most: launch is not the growth driver at any launch company

FLY page 40 states revenue rose **657% to $117.7M "driven by Spacecraft Solutions
growth."** Launch revenue is not the driver.

Placed beside the other two:

| Issuer | Revenue growth | What drove it | Launch revenue |
|---|---|---|---|
| **SPCX** Q2 | **+91.9%** | Connectivity (+65.8%) and AI (+247.5%) | Space segment only +29.0%; **Falcon launches −18%** |
| **RKLB** Q2 | **+62%** | Space systems **+$91.6M** | Launch revenue **−$2.1M** (declined) |
| **FLY** Q2 | **+657%** | Spacecraft Solutions | Not the driver |

**In all three cases, revenue growth comes from non-launch business, and in two of three
launch revenue actually declined.**

**This refines A1, and the refinement is a proposed amendment.** A1 says *"launch cost is
the master variable — every orbital business case is a derivative of cost-per-kilogram-
to-orbit."* The evidence supports the *cost* half: launch price sets the floor under
every downstream business case. But it **contradicts the implied value-capture half**:
none of the three listed launch providers generates its growth from launch. Launch is
behaving as a **cost input and internal capability**, not as the profit pool.

**Proposed: split A1 into A1a (launch cost is the sector's master *cost* variable — holds)
and A1b (launch is the sector's master *value* variable — does not hold on current
disclosure).** This is the same shape as the F5a/F5b proposal and should be reviewed with
it. It is also consistent with what Phase 1 found at SPCX and what A5's merger wave
implies: the value is migrating to constellations and services, which is precisely why
RKLB is buying Iridium and Amazon is buying Globalstar.

## 4. FLY's margin is the weakest of the three manufacturers checked

| Issuer | Q2 2026 gross margin | Operating result | R&D / revenue |
|---|---|---|---|
| RKLB | **36.1%** | $(57.5)M loss | 35.2% |
| YSS | 24.0% | $(41.3)M loss | 6.2% |
| **FLY** | **20.3%** | **$(95.2)M loss** | **60.8%** |

FLY combines the **lowest gross margin** with the **highest R&D intensity** and the
**largest operating loss** — the profile of a company simultaneously scaling a launch
vehicle (Alpha Block II) and integrating an acquisition (SciTec, $550.3M, closed
2025-10-31). Its revenue base ($117.7M/quarter) is roughly half RKLB's, so the fixed-cost
burden is proportionally heavier.

Note also: FLY is an **emerging growth company** (page 1), which relaxes its disclosure
obligations — a structural reason its filings reveal less than RKLB's. Worth remembering
when comparing disclosure richness across the universe.

## 5. Backlog — the demand-side cross-check

| Issuer | Backlog at 2026-06-30 | vs prior |
|---|---|---|
| RKLB | **$2,355.9M** | increased |
| FLY | **$1,468.1M** | up from $1,351.1M (+8.7%) |

Both have substantial backlog, and FLY explicitly cites a **multi-launch agreement**
component. That is a demand-side datum supporting PIL-3's claim that these firms are
demand-constrained rather than launch-constrained — consistent with RKLB's build-vs-launch
evidence.

---

## Carry-forwards

1. **A1a/A1b split proposed** — the strongest constitution-level finding of Phase 1, and
   it now has three independent issuer confirmations.
2. **Basis B cannot be widened** without another per-launch disclosure. PIL-1 should
   state explicitly that its demonstrated anchor is single-source.
3. **`DA-23` should be treated as guaranteed, not suspected** — 4 of 4. Any
   `operating_income`-based screen over this universe is unsafe without component
   verification, and the remedy belongs in the constitution rather than in artifact
   footnotes.
4. **FLY's EGC status** is a disclosure-quality variable worth carrying into any
   cross-issuer comparison — it is a structural explanation for missing data, not an
   oversight by the analyst.
