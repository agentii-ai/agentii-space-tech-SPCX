---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: IRDM
skill: risk
mode: methodology
generated_at: 2026-09-19T15:15:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "953fc5d396e7"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-23
    chosen_reading: >-
      Treated as a PLATFORM extraction defect (a filed negative served as a positive of
      identical magnitude), NOT as a restatement of the issuer's results. The filed
      statement governs. At IRDM the strip is CONCEPT-SELECTIVE: it does not touch
      OperatingIncomeLoss, which is why 001's "5/5 clean" clearance tested nothing.
  - da_id: DA-24
    chosen_reading: >-
      Applied to the merger transaction costs inside SG&A and to the equity-method and
      hedge losses below the operating line. Contamination is measured, not assumed: the
      non-operating block is reported separately from operating income on the as-filed
      basis and is never netted into it.
  - da_id: DA-30
    chosen_reading: >-
      Every operating-margin statement carries its period basis (3M, 6M, or FY) and its
      opex definition, because IRDM's margin direction INVERTS between the 3M basis
      (falling) and the FY2025 basis (rising).
  - da_id: DA-29
    chosen_reading: >-
      The component identity is asserted only against cells that appear in the as-filed
      statement. No reconciliation is treated as a check merely because it closes.
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
citations:
  - figure: "IRDM sec191 p.24"
    ticker: IRDM
    citation_id: sec191
    page_no: 24
    url: https://agentii.ai/v/IRDM/sec191/24
    located_via: read_source_pages
  - figure: "IRDM sec191 p.26"
    ticker: IRDM
    citation_id: sec191
    page_no: 26
    url: https://agentii.ai/v/IRDM/sec191/26
    located_via: read_source_pages
  - figure: "IRDM sec151 p.52"
    ticker: IRDM
    citation_id: sec151
    page_no: 52
    url: https://agentii.ai/v/IRDM/sec151/52
    located_via: read_source_pages
  - figure: "IRDM sec191 p.36"
    ticker: IRDM
    citation_id: sec191
    page_no: 36
    url: https://agentii.ai/v/IRDM/sec191/36
    located_via: read_source_pages
  - figure: "IRDM sec191 p.5"
    ticker: IRDM
    citation_id: sec191
    page_no: 5
    url: https://agentii.ai/v/IRDM/sec191/5
    located_via: read_source_pages
  - figure: "IRDM sec151 p.53"
    ticker: IRDM
    citation_id: sec151
    page_no: 53
    url: https://agentii.ai/v/IRDM/sec151/53
    located_via: read_source_pages
  - figure: "IRDM sec151 p.31"
    ticker: IRDM
    citation_id: sec151
    page_no: 31
    url: https://agentii.ai/v/IRDM/sec151/31
    located_via: read_source_pages
  - figure: "IRDM sec151 p.36"
    ticker: IRDM
    citation_id: sec151
    page_no: 36
    url: https://agentii.ai/v/IRDM/sec151/36
    located_via: read_source_pages
  - figure: "IRDM sec151 p.50"
    ticker: IRDM
    citation_id: sec151
    page_no: 50
    url: https://agentii.ai/v/IRDM/sec151/50
    located_via: read_source_pages
  - figure: "IRDM sec151 p.26"
    ticker: IRDM
    citation_id: sec151
    page_no: 26
    url: https://agentii.ai/v/IRDM/sec151/26
    located_via: read_source_pages
  - figure: "IRDM sec151 p.40"
    ticker: IRDM
    citation_id: sec151
    page_no: 40
    url: https://agentii.ai/v/IRDM/sec151/40
    located_via: read_source_pages
  - figure: "IRDM sec191 p.22"
    ticker: IRDM
    citation_id: sec191
    page_no: 22
    url: https://agentii.ai/v/IRDM/sec191/22
    located_via: read_source_pages
  - figure: "IRDM sec191 p.39"
    ticker: IRDM
    citation_id: sec191
    page_no: 39
    url: https://agentii.ai/v/IRDM/sec191/39
    located_via: read_source_pages
  - figure: "IRDM sec191 p.28"
    ticker: IRDM
    citation_id: sec191
    page_no: 28
    url: https://agentii.ai/v/IRDM/sec191/28
    located_via: read_source_pages
  - figure: "IRDM sec191 p.30"
    ticker: IRDM
    citation_id: sec191
    page_no: 30
    url: https://agentii.ai/v/IRDM/sec191/30
    located_via: read_source_pages
  - figure: "IRDM sec191 p.21"
    ticker: IRDM
    citation_id: sec191
    page_no: 21
    url: https://agentii.ai/v/IRDM/sec191/21
    located_via: read_source_pages
key_metrics:
  operating_margin_3m_2026_pct: 15.10
  operating_margin_fy2025_pct: 27.07
  operating_margin_fy2024_pct: 24.12
  transaction_cost_share_of_sga_increase_3m_pct: 63.8
---

# IRDM × risk — P11 deal-security tagging and the falsifier-reachability census

## The finding

**The operating-margin decline the register carries as a PIL-6 signal at IRDM is majority a
deal-cost artifact, and the licence that the whole thesis would treat as the durable asset is
itself a deal-contingent asset because the merger cannot close without FCC consent to transfer
it.**

Two separate results, both of which change how IRDM may be used in this thesis:

1. **The margin decline is 64% transaction cost.** IRDM's operating margin on the
   **three-month basis** fell from **23.17%** to **15.10%**. Of the SG&A increase, **$14.3M of
   a $22,417 thousand rise is Rocket Lab Merger Agreement and Aireon transaction costs** —
   **63.8%** of the increase. On the six-month basis, **$15.0M of a $32,443 thousand rise** is
   transaction cost — **46.2%**. On the fiscal-year basis the same margin **ROSE**: **24.12%
   (FY2024) → 27.07% (FY2025)**. The direction of the "trend" therefore depends on the period
   basis chosen, and the only basis on which it is a *decline* is one contaminated by
   non-recurring deal costs. `[📄 IRDM 10-Q p.24](https://agentii.ai/v/IRDM/sec191/24)`
   `[📄 IRDM 10-Q p.26](https://agentii.ai/v/IRDM/sec191/26)`
   `[📄 IRDM 10-K p.52](https://agentii.ai/v/IRDM/sec151/52)`

2. **The general risk factors are not in the current-period document.** The Q2 2026 10-Q's
   Item 1A adds **only** "Risks Related to the Anticipated Merger with Rocket Lab Corporation"
   and "Risks Related to Aireon's Business", and **incorporates the general risk factors by
   reference to the FY2025 Form 10-K**. A P6 reachability consequence follows directly: the
   general-risk-factor set at IRDM is **reachable only through a different filing period**, and
   any census that reads Item 1A of the current 10-Q alone will find two risk blocks and
   wrongly conclude the set is small. `[📄 IRDM 10-Q p.36](https://agentii.ai/v/IRDM/sec191/36)`

## 1. Component identity, opex definition, units

Every operating figure below is the as-filed basis. The identity is stated in-line and the
opex definition is named, per §3.5 of the brief.

**Opex definition used throughout: the `Total operating expenses` line as filed at IRDM —
INCLUSIVE of cost of sales** (cost of services exclusive of D&A, plus cost of subscriber
equipment), research and development, selling, general and administrative, and depreciation
and amortisation.

| Period | Revenue ($k) | Opex ($k) | `revenue − opex` ($k) | Filed operating income ($k) | Margin |
|---|---|---|---|---|---|
| 3M 2026 | 225,237 | 191,229 | 34,008 | **34,008** ✓ | 15.10% |
| 3M 2025 | 216,906 | 166,648 | 50,258 | **50,258** ✓ | 23.17% |
| 6M 2026 | 444,294 | 359,573 | 84,721 | **84,721** ✓ | 19.07% |
| 6M 2025 | 431,784 | 321,138 | 110,646 | **110,646** ✓ | 25.63% |
| FY2025 | 871,659 | 635,679 | 235,980 | **235,980** ✓ | 27.07% |
| FY2024 | 830,682 | 630,298 | 200,384 | **200,384** ✓ | 24.12% |

The identity closes exactly on **6 of 6 period-pairs**, on the inclusive definition.
`[📄 IRDM 10-Q p.5](https://agentii.ai/v/IRDM/sec191/5)`
`[📄 IRDM 10-K p.52](https://agentii.ai/v/IRDM/sec151/52)`

**⚠️ The gross-profit bound is UNEXERCISED at IRDM, not passed.** IRDM files **no gross-profit
line**. The inclusive and exclusive opex formulations therefore cannot both be tested, and the
cross-check that catches a wrong opex definition at issuers that do file a gross-profit line
(RKLB, PL, YSS) is **unavailable here**. Recorded as `UNEXERCISED`; the identity above closes,
but only against the one definition IRDM permits. This is precisely the distinction §6 of the
brief requires: a check that could not run is not a check that passed.

**Units.** The as-filed statements are in **thousands**; the platform's `value_numeric` for the
same cells is in **dollars** (e.g. filed `34,008` thousands ↔ served `34008000`). Any consumer
mixing the two layers is off by 1,000×. All figures in this artifact are as-filed thousands
unless a unit is written.

## 2. DA-23 census at IRDM — PRESENCE, and the reason 001's clearance was wrong

**Result: ≥15 confirmed strip cells across 2 concepts.** The strip is live at IRDM and it is
**concept-selective**.

**Stripped (served positive against a filed negative parenthetical):**

| Concept | Periods served positive against a filed negative | Cells |
|---|---|---|
| `us-gaap:IncomeLossFromEquityMethodInvestments` | 1,510,000 (Q2 26); 732,000 (Q1 26); 2,242,000 (H1 26); 860,000 (Q2 25); 648,000 (Q1 25); 1,508,000 (H1 25); 734,000 (Q3 25); 2,242,000 (9M 25); 2,823,000 (FY25) | **9** |
| `us-gaap:OtherComprehensiveIncomeLossCashFlowHedgeGainLossAfterReclassificationAndTax` | 3,362,000 (Q2 26); 2,158,000 (Q1 26); 4,975,000 (Q2 25); 12,216,000 (H1 25); 7,241,000 (Q1 25); 4,575,000 (Q3 25) | **6** |

**NOT stripped — verified by exact match to the filed statements:**
`us-gaap:OperatingIncomeLoss` serves **34,008,000** / **84,721,000** against filed operating
income of **34,008** / **84,721** thousand — the same *positive* value with only the unit scale
changed. `us-gaap:IncomeTaxExpenseBenefit` likewise matches.

**Why this refutes 001's "5/5 clean".** The concepts 001 tested and cleared are the
top-of-statement concepts, and at IRDM those are the concepts the strip does not touch. The
clearance was therefore **not a passed check but an unengaged one**: it sampled the region of
the statement where the defect is absent and then generalised to the issuer. 003's finding F8
already records the refutation; the mechanism is stated here because it is the reusable part —
**a strip regime can be concept-selective, so a per-issuer clearance built from a concept
sample is a clearance of the sample, not of the issuer.** The detector that does not have this
failure mode is the component identity, which is why §1 above is the load-bearing section and
the census above is corroboration rather than proof.

## 3. Mode — general-risk-factors-identification-assessment

IRDM's identifiable general risk set, on the as-filed basis, ranked by what it threatens:

- **Concentration in one government contract with a known expiry.** The EMSS contract's
  service fee is **fixed at $110.5 million per year** and **is not based on subscribers or
  usage**; it **expires in September 2026**, with a federal-acquisition-regulation right for
  the government to unilaterally extend **six months**. Government service revenue was
  **$108.0M** of FY2025's **$871,659 thousand** total revenue (**12.4%**), and IRDM states it
  expects a new EMSS contract "later in 2026 or in 2027". **A 12.4% revenue line is on a fixed
  fee with no contracted successor and a filing date after the stated expiry.** This is the
  single largest dated risk at IRDM and it is a *demand-side* risk, which places it directly
  under PIL-6. `[📄 IRDM 10-K p.53](https://agentii.ai/v/IRDM/sec151/53)`
- **Single points of failure in the ground segment.** Primary commercial gateway Tempe,
  Arizona; a second gateway in **Izhevsk, Russia** used for traffic within Russian boundaries
  only; network operations centre Leesburg, Virginia. IRDM states a switch to the backup
  facility "could take us up to several hours" and that "when operating on our backup facility,
  any further failure could leave us unable to offer services for an extended period."
  `[📄 IRDM 10-K p.31](https://agentii.ai/v/IRDM/sec151/31)`
- **Concentration of traffic origin outside the United States.** Commercial data traffic
  originating outside the US was **96%** (2025) and **94%** (2024); commercial voice traffic
  **92%** and **91%**. `[📄 IRDM 10-K p.36](https://agentii.ai/v/IRDM/sec151/36)`
- **Russia exposure.** Two local subsidiaries, ~40 people, a dedicated gateway, **~2% of total
  revenue in each of 2023, 2024 and 2025**, ruble-denominated and translated, plus a stated
  reputational risk. `[📄 IRDM 10-K p.36](https://agentii.ai/v/IRDM/sec151/36)`
- **Supply chain and tariffs.** IRDM states plainly that "**U.S. trade policy changes in 2025
  increased our costs** and caused us to evaluate alternative sourcing arrangements", and that
  it relies on a limited number of manufacturers with **sole-source suppliers for some
  components**. `[📄 IRDM 10-K p.36](https://agentii.ai/v/IRDM/sec151/36)`
- **A five-year useful-life extension taken in Q4 2023.** Second-generation satellite useful
  lives were extended from **12.5 to 17.5 years**, and this was a **KPMG critical audit
  matter**. Every depreciation figure in §1 — including the $191,229 and $359,573 thousand opex
  figures — rests on that estimate. It is an accounting estimate, not an event, and it sits
  inside the opex definition this artifact uses. `[📄 IRDM 10-K p.52](https://agentii.ai/v/IRDM/sec151/52)`

**What this mode could not resolve.** The specification of *which* of these is material in the
sense the register's PIL-6 claim requires: IRDM does not disclose a launch-cost line, a
programme-cost line, or any demand-side programme cost share, so the PIL-6 threshold quantity
is **NON-FORMABLE at this issuer** (§5 below).

## 4. Mode — technology-disruption-risk-analysis

IRDM files an explicit technological-disruption block, and — unusually for this universe — it
names **artificial intelligence** as a first-order risk in its own words:

> "Artificial intelligence technologies have rapidly developed in recent years, and our
> business may be adversely affected if we are unable to successfully integrate the technology
> into our business processes, products and service offerings as effectively as our
> competitors." `[📄 IRDM 10-K p.31](https://agentii.ai/v/IRDM/sec151/31)`

That is a **CLAIMED** grade item (an issuer assertion) and it is about IRDM's *capacity to
adopt*, not about AI as a demand driver. It is not evidence of AI exposure in the sense the
`secular-trends` deep-dive mode requires, and it must not be promoted to one.

The filed disruption channels, in the filing's own ordering:

1. **Competitor constellations with greater capability** — "the deployment by our competitors of
   new satellites and satellite constellations with greater power, flexibility, efficiency or
   capabilities than ours". `[📄 IRDM 10-K p.31](https://agentii.ai/v/IRDM/sec151/31)`
2. **Direct-to-device**, named elsewhere in the same 10-K as a specific competitor action:
   IRDM lists as a challenge "**increased competition or potential competition from other
   satellite service providers, including SpaceX following its recently announced plans to
   acquire a significant amount of spectrum enabling global D2D services**, and, to a lesser
   extent, from the expansion of terrestrial-based cellular phone systems".
   `[📄 IRDM 10-K p.50](https://agentii.ai/v/IRDM/sec151/50)` — **this is the demand-side
   citation PIL-6 needs**, and its grade is `CLAIMED` (IRDM's characterisation of a competitor
   plan), not DEMONSTRATED.
3. **Continuing improvements in terrestrial wireless** technologies.
4. **Customized hardware and software that cannot be serviced or upgraded.** Some gateway
   hardware is sufficiently customised that "for certain equipment, the OEM no longer supports
   the equipment". `[📄 IRDM 10-K p.31](https://agentii.ai/v/IRDM/sec151/31)`
5. **Obsolescence of the constellation itself** — the same paragraph contemplates that new
   technology "could render our system obsolete or less competitive".

**Directional reading, stated as a reading.** The filing's own risk language locates IRDM's
technological exposure on the **capability of the constellation it already operates**, and the
constellation is fixed: second-generation satellites are subject to a **25-year de-orbit
standard** under the FCC authorisation. `[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)`
The disruption risk is therefore not "will a cheaper launch let IRDM deploy more" — the
constellation is built and depreciating — but "can a capability fixed at launch be defended
against a constellation whose capability is not". That asymmetry is the technology-disruption
answer for a *demand-side* name, and it is the mirror image of the launcher-side question.

## 5. Mode — regulatory-compliance-risk-assessment

IRDM's regulatory surface is the widest in the operator cohort, and one feature of it is
unusual enough to state first.

**The United States files IRDM's spectrum paperwork, not IRDM.** "Only member states have full
standing within this inter-governmental organization. **Filings to the ITU are made on our
behalf by the United States.**" `[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)`
IRDM holds:

- **8.725 MHz of contiguous L-band** — filed as `1617.775–1626.0 GHz`, which is a **unit error
  in the filing** (the band is MHz; 1617 GHz would be soft X-ray). Quoted as filed, flagged as
  a source-quality observation, and not corrected silently — the number is the band, the unit
  label attached to it is wrong. `[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)`
- **200 MHz of K-band (23 GHz)** for inter-satellite links and **400 MHz of Ka-band**
  (19.4–19.6 / 29.1–29.3 GHz) for feeder links.
- **AIS reception** at 156.0125–162.0375 MHz and **ADS-B reception** at 1087.7–1092.3 MHz.
- ITU country codes **8816** and **8817**.

**Three regulatory exposures with named live proceedings:**

1. **Ligado / L-band interference — live, adversarial, and now in bankruptcy.** The FCC granted
   Ligado a **2020 waiver** to operate a terrestrial nationwide network on MSS spectrum
   including **a 10 MHz band close to IRDM's**; IRDM and others filed **petitions for
   reconsideration** which "remain pending". **October 2023**: Ligado sued the US government
   seeking damages. **January 2025**: Ligado and affiliates filed **Chapter 11**, and "as part
   of its reorganization, it executed an agreement to lease and **potentially transfer its
   satellites, ground assets and L-band spectrum to AST SpaceMobile, Inc**".
   `[📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40)` **This is the single most
   load-bearing regulatory fact in the artifact**: IRDM's interference risk is not a generic
   spectrum-sharing risk — it is an identified counterparty (AST SpaceMobile) acquiring an
   adjacent L-band position through a bankruptcy process that IRDM does not control and whose
   outcome IRDM states "may impact the outcome of the pending petitions for reconsideration".
2. **Common-carrier regulation with foreign-ownership limits.** The subsidiary **Iridium
   Carrier Services LLC holds a common carrier radio license**, and is therefore subject to
   regulation as a common carrier "including limitations and prior approval requirements with
   respect to direct or indirect foreign ownership". A change in the manner of service, or
   non-compliance, could produce "fines, loss of authorizations, or the denial of applications
   for new authorizations or the renewal of existing authorizations".
   `[📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40)`
3. **Orbital debris.** A **25-year de-orbit standard** applies to all second-generation
   satellites under the FCC authorisation, and IRDM names "our orbital debris mitigation
   obligations" as a thing regulators may expand.
   `[📄 IRDM 10-K p.26](https://agentii.ai/v/IRDM/sec151/26)`
   `[📄 IRDM 10-K p.40](https://agentii.ai/v/IRDM/sec151/40)`

## 6. P11 — why `standalone_pre_merger` is load-bearing here, not a tag

Every operational metric in this artifact describes a business that **contractually ceases to
exist** on the terms filed. The Merger Agreement with Rocket Lab is dated **June 28, 2026**, at
**$27.00 in cash plus Rocket Lab stock** (exchange ratio 0.4000 at ≤$67.50; $27.00 ÷ price in
between; 0.2400 at ≥$112.50), with a **$223.6 million termination fee payable by IRDM**, and
closing expected **mid-2027**. `[📄 IRDM 10-Q p.22](https://agentii.ai/v/IRDM/sec191/22)`

**Closing conditions, quoted for the parts that matter to a licence-holding thesis:**

- majority stockholder vote;
- **HSR** expiration;
- **"consent of the U.S. Federal Communications Commission to the transfer of control of
  certain of our telecommunication authorizations"**;
- other foreign investment and satellite/telecom clearances;
- no injunctive order, no material adverse effect, Form S-4 effectiveness.
`[📄 IRDM 10-Q p.22](https://agentii.ai/v/IRDM/sec191/22)`

**The FCC consent condition is the reason the P11 tag changes the analysis rather than merely
annotating it.** The asset the thesis treats as durable — the globally coordinated L-band
authorisation, made durable by an ITU filing the *United States* makes on IRDM's behalf — is
not transferable without a regulator's affirmative consent, and the same regulator is the forum
in which the adjacent-band interference petitions remain pending. **The durability of the
licence and the consummation of the deal are decided in the same venue.** A standalone
operating metric at IRDM therefore describes a licence position that is simultaneously (a) the
thing being valued and (b) the thing whose transfer is a condition precedent.

**Post-close boundary note.** Aireon closed **July 2, 2026** for approximately **$366.7
million** (50% cash, 50% deferred loan) — **four days after** the June 28 merger agreement and
after the Q2 balance-sheet date. The term loan is **$1,774.7 million** and IRDM drew **$100.0
million** on the Revolving Facility on **July 1, 2026**. `[📄 IRDM 10-Q p.39](https://agentii.ai/v/IRDM/sec191/39)`
Any post_close basis for IRDM must carry Aireon *and* the Rocket Lab transaction, and neither
appears in the as-filed Q2 2026 income statement. This artifact reports the
`standalone_pre_merger` basis exclusively.

## 7. Falsifier-reachability census

Per-falsifier, with the disposition class. Classes are the register's three:
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` (disclosure does not exist → name it, monitor);
`UNRESOLVABLE-FROM-PLATFORM` (public but unreachable → platform reach);
**`REACHABLE-BUT-NOT-RECORDABLE`** (datum reachable, the **CONTRACT** cannot record it → amend
the contract; the one class research cannot fix).

| Falsifier | Reachability at IRDM | Class | Why |
|---|---|---|---|
| **PIL-6 `independently_falsifiable`** — "a demonstrated fall in revenue per launch at least as large as the fall in cost per launch" | **NON-FORMABLE**, not PASS | n/a — the quantity does not exist at this entity | IRDM does not launch. It files no per-launch revenue and no per-launch cost in any period. The falsifier's numerator and denominator are launcher-side constructs. **NON-FORMABLE ≠ PASS (F16).** |
| **PIL-6 `wrong_if`** — launch-cost share of total programme cost > 0.10 | **NON-FORMABLE**, not PASS | `REACHABLE-BUT-NOT-RECORDABLE` | IRDM files no programme-cost breakdown into which a launch-cost term could enter. The datum (a programme cost) is reachable in the sense that IRDM's capex is filed; it is **not recordable**, because the contract admits no field in which a launch-cost share of a demand-side programme cost can be carried. |
| **F17 threshold reachability** (10% bar above the 8.29% datum at SPCX) | **NOT REACHABLE — and not even addressable here** | n/a | F17 is a property of SPCX's segment boundary. At IRDM the datum is not formable at all, so the threshold has nothing to sit above. **The F17 finding does not generalise to the operator cohort; it is an SPCX-specific defect.** Recorded because a census that reported F17 as "holds across the universe" would over-read it. |
| **A1a reconciliation statement** (`12.3%` / `8.29%`, ex-AI growth rates) | **UNEXERCISED** | n/a | Requires SPCX segment data. Not reachable from IRDM's filings, and not attempted. |
| **F2 — Falcon 9 basis B** | `UNRESOLVABLE-FROM-PUBLIC-SOURCES` | inherited | 002 §5.1; not re-derived here. |
| **F3 — propellant price** | **`REACHABLE-BUT-NOT-RECORDABLE`** | canonical case | The register's canonical instance of the class. The price is reachable; `citation_url_wellformed` is level `fail` and admits only `agentii.ai` URLs, so a source class outside `agentii.ai` cannot be recorded. **The remedy is to amend the contract.** |
| **PIL-6 FCC IBFS resolver** | `UNRESOLVABLE-FROM-PLATFORM` | platform reach | No resolver reachable. The specific transfer-of-control application — the docket that decides the closing condition quoted in §6 — **is not identified in the filing**: IRDM names "the consent of the U.S. Federal Communications Commission" and no docket number. Two dispositions compose here: the *docket number* is `UNRESOLVABLE-FROM-PUBLIC-SOURCES` at the filing level (the filer did not state it), and the *resolver* is `UNRESOLVABLE-FROM-PLATFORM`. |
| **PIL-6 ITU Space Network List resolver** | `UNRESOLVABLE-FROM-PLATFORM` | platform reach | Same. Note the compounded reachability problem specific to IRDM: the ITU filing is made by the **United States** on IRDM's behalf, so the recorded network is not keyed to the issuer at all. |
| **VZ / T / TMUS** (comparator telecoms) | **`TICKER_NOT_FOUND`** — confirmed 2026-09-19 | n/a | All three verified this session: `Ticker 'VZ' not found`, `Ticker 'T' not found`, `Ticker 'TMUS' not found`. **The telecom comparator leg is absent by construction**, so any peer set for an operator cohort at IRDM is a satellite-operator peer set, not a telecom peer set. |

### The one class research cannot fix

`REACHABLE-BUT-NOT-RECORDABLE` appears **three times** in the census above (PIL-6 `wrong_if`,
F3, and the pilot effect at PIL-6's threshold), and it is worth stating why it is not a
research failure. The datum is reachable. The **contract** cannot record it, because
`citation_url_wellformed` admits only `agentii.ai` URLs. Every artifact in this thesis is
therefore structurally unable to cite the class of source — a regulator's docket, an ITU
register entry, a trade-press price — that would discharge the falsifier. **Carrying it as
`UNRESOLVABLE-FROM-PUBLIC-SOURCES` would be wrong** (the disclosure exists) and
**`UNRESOLVABLE-FROM-PLATFORM` would also be wrong** (the platform is not the obstacle; the
contract is). The remedy is a contract amendment, and it is the one disposition no amount of
retrieval closes.

## 8. What this artifact could not resolve

- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the PIL-6 threshold quantity at IRDM, permanently.**
  The resolving disclosure is a **programme-cost breakdown at IRDM naming a launch-cost term**.
  IRDM's business has no launch procurement of the kind the quantity assumes; the nearest
  filed lines are the satellite capex and the Aireon hosting arrangement, and neither is a
  programme cost. Named so it can be monitored; expected never to appear.
- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES` — the FCC docket for the transfer of control.** The
  resolving disclosure is the **IBFS application file number** for the consent IRDM's merger
  condition requires. IRDM names the consent and not the docket.
- **`UNRESOLVABLE-FROM-PLATFORM` — both PIL-6 resolvers.** FCC IBFS and the ITU Space Network
  List. Stated per the brief.
- **UNEXERCISED — the gross-profit bound.** IRDM files no gross-profit line; the inclusive vs
  exclusive opex cross-check could not run. Noted as `UNEXERCISED`, **never CLEAN**.
- **UNEXERCISED — DA-24 and DA-30 at the platform layer.** The *substance* of both is handled
  in §1 and §6 (non-operating items are reported separately as filed; the period basis is
  stated for every margin). What was **not** exercised is the platform-layer test: whether
  `us-gaap:OperatingIncomeLoss` at IRDM carries a non-operating component. The filed statement
  says it does not, and the served value matches the filed value exactly, so the platform layer
  is *consistent* — but consistency is not the same as a test having run. Recorded
  `UNEXERCISED`.
- **NOT ATTEMPTED — DA-25, DA-26, DA-27, DA-28, DA-29 at IRDM.** This artifact does not assert
  a normalised per-unit metric (DA-25), does not use an annual-as-quarterly figure (DA-26),
  does not rely on a calendar-derived fiscal label (DA-27), does not use a share-count detector
  across a capital-structure discontinuity (DA-28), and asserts no reconciliation whose terms
  are not in the source (DA-29). **Each is recorded here as not attempted, which is not the
  same as passing.** The ARPU figures at IRDM (Voice and data $47; IoT $7.78; broadband $259,
  FY2025) are exposure to DA-25 and are handled in the companion `secular-trends` artifact for
  this ticker, not here.

---

## Sources

> Every figure asserted above resolves to the page cited. Regenerated from the
> artifact's `citations` block — the frontmatter block alone does not satisfy
> spec §1d, which requires the links **in the body**.

| Figure | Source |
|---|---|
| IRDM sec191 p.24 | [📄 IRDM  p.24](https://agentii.ai/v/IRDM/sec191/24) |
| IRDM sec191 p.26 | [📄 IRDM  p.26](https://agentii.ai/v/IRDM/sec191/26) |
| IRDM sec151 p.52 | [📄 IRDM  p.52](https://agentii.ai/v/IRDM/sec151/52) |
| IRDM sec191 p.36 | [📄 IRDM  p.36](https://agentii.ai/v/IRDM/sec191/36) |
| IRDM sec191 p.5 | [📄 IRDM  p.5](https://agentii.ai/v/IRDM/sec191/5) |
| IRDM sec151 p.53 | [📄 IRDM  p.53](https://agentii.ai/v/IRDM/sec151/53) |
| IRDM sec151 p.31 | [📄 IRDM  p.31](https://agentii.ai/v/IRDM/sec151/31) |
| IRDM sec151 p.36 | [📄 IRDM  p.36](https://agentii.ai/v/IRDM/sec151/36) |
| IRDM sec151 p.50 | [📄 IRDM  p.50](https://agentii.ai/v/IRDM/sec151/50) |
| IRDM sec151 p.26 | [📄 IRDM  p.26](https://agentii.ai/v/IRDM/sec151/26) |
| IRDM sec151 p.40 | [📄 IRDM  p.40](https://agentii.ai/v/IRDM/sec151/40) |
| IRDM sec191 p.22 | [📄 IRDM  p.22](https://agentii.ai/v/IRDM/sec191/22) |
| IRDM sec191 p.39 | [📄 IRDM  p.39](https://agentii.ai/v/IRDM/sec191/39) |
| IRDM sec191 p.28 | [📄 IRDM  p.28](https://agentii.ai/v/IRDM/sec191/28) **(newly surfaced)** |
| IRDM sec191 p.30 | [📄 IRDM  p.30](https://agentii.ai/v/IRDM/sec191/30) **(newly surfaced)** |
| IRDM sec191 p.21 | [📄 IRDM  p.21](https://agentii.ai/v/IRDM/sec191/21) **(newly surfaced)** |
