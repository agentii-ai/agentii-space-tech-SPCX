# Entity & Metric Map — 003 Launch Cost Curve & Value Migration

> **No bars schema required (Q42).** Every §3 row is `market_data_stage: none`, so the
> thesis consumes no OHLCV series and Q42 does not bind. What replaces it is the
> **definitional map** below: the DA class that bites each metric, per entity. On this
> thesis the definition *is* the data hazard — a $/kg without its basis is not a weaker
> number, it is a different number.

---

## `entity_claims` schema

Per `contracts/artifact-frontmatter.yaml`. Every artifact asserts claims of this shape:

```yaml
entity_claims:
  - ticker:          str      # required; must appear in §2 universe
    metric:          str      # required; from the map below, or added with a da_class
    value:           float    # required
    unit:            str      # required — a bare number fails (P2)
    basis:           str      # required WHERE a DA class applies (see map). DA-01 basis,
                              # DA-02 orbit, DA-21 boundary, or P11 pre-merger flag
    period:          str      # required; ISO period, issuer's fiscal calendar (DA-27)
    evidence_grade:  str      # required; DEMONSTRATED | CLAIMED | MODELED | DERIVED
    source:          str      # required; artifact path + page
    da_class:        [str]    # DA ids whose hazard this figure is exposed to
```

**Two hard rules.** (1) `basis` is mandatory wherever `da_class` is non-empty — a value
exposed to a definitional hazard and reported without its reading is the DA-30 collapse.
(2) `entity_claims` never carries a derived figure without its inputs — an artifact that
states a margin without the `gross_profit − opex` derivation is a DA-23/28 fail.

**⚠️ And the derivation obligation is CONDITIONAL on the opex definition — correct this before
using it.** 002 §4.2 item 15: **`gross profit − opex = operating_income` is FALSE at UTHR by
exactly cost of sales, six of six periods**, because the `us-gaap:CostsAndExpenses` tag is
**INCLUSIVE of cost of sales** while the identity assumes it is exclusive. 001's own AMGN
check passed only because it silently used opex **net** of cost of sales. **So the rule is
not "subtract opex" — it is "subtract opex *and state which definition of opex you used*."**
Where the exclusive figure is unavailable, **invoke the gross-profit bound instead** (operating
income cannot exceed gross profit at any sign) — which is itself a false negative at low gross
margin and is **UNEXERCISED at SPCX** for exactly that reason (no gross-profit line, ~65% GM).

---

## Entity map — nine names, and what each one is *for*

Weights are **analytical effort, not positions** (spec §2). This thesis sizes nothing.

| Ticker | Company | Sector | Wt | Role | The claim it exists to carry | DA exposure |
|---|---|:---:|:---:|---|---|---|
| **SPCX** | SpaceX | industrial.aerospace_defense | 20% | **Reference vehicle** | Falcon 9 (partially reusable) + Starship (fully reusable) supply two of three architectures; the basis A/A′/B/C inputs; the three-segment structure P2 reads | **DA-01** (four bases, 7–13× spread), **DA-02**, **DA-03**, **DA-06** (captive — no transaction price) |
| **RKLB** | Rocket Lab | industrial.aerospace_defense | 20% | **Only measured point — ⚠️ TO BE RECONVERTED, DO NOT INHERIT** | Electron basis A `$30,333/kg`, basis B `$14,667/kg` — the universe's *only* DEMONSTRATED marginal cost. ⚠️ **002 correction 26: 001's published $/kg figures are 1.79×–2.62× TOO LOW, four of four periods**, and the realized denominator restates every demonstrated $/kg by **+79% to +162%** against a **±15%** tolerance. **Phase 1 reconverts these before plotting anything.** Also: the `cost/revenue per launch` series; Neutron (P4); SolAero solar-cell leg | **DA-25** (both legs), **DA-27**, **P11** pre-merger, **DA-28** |
| **FLY** | Firefly Aerospace | industrial.aerospace_defense | 10% | **Disclosure-uniqueness control** | Alpha — a second fully expendable vehicle — with **neither per-launch metric disclosed**. Makes RKLB's disclosure a finding, not a convention. An EGC: structural cause of thin disclosure | **DA-01** (bases absent — must be *named*, not proxied), F5 coverage gap |
| **PL** | Planet Labs | industrial.aerospace_defense | 10% | **Pass-through test** | Best gross margin in the universe (**53.5%**) yet −37% at the operating line. Tests whether the curve's pass-through can reach a customer whose binding problem is **fixed cost, not launch cost** | **DA-23/28** (component identity), **DA-21** (segment boundary) |
| **YSS** | York Space Systems | industrial.aerospace_defense | 10% | **Far end of the chain** | 24.0% gross margin against a **68.6% opex ratio**; fixed cost base **2.9× gross profit**; revenue **−20.5% QoQ** — a volume problem, not a unit-economics one | **DA-25** (normalised per-unit), **DA-27** |
| **SATS** | EchoStar | tech.telecom_services | 8% | **Counter-case to launcher capture — REFUTED AS STATED** | ⚠️ **Corrected 2026-09-18.** The *"~$27B spectrum gain"* **was not a gain**: it is a **non-cash 5G-Network IMPAIRMENT CHARGE of $16,481,468k**, the licences **remain on the balance sheet**, AT&T took only a **short-term spectrum-manager lease**, and **nothing has closed.** `~$27B` does not reproduce from any filing. **No proceeds and no realised price exist — so no $/unit figure may be derived from this event, which is exactly what a cost-curve thesis would be tempted to do.** Corrected margin run: `(2.28) → (5.73) → (460.46) → (20.54) → +10.71`; the `10.7%` corrects to **`8.91%`** ex-item | **DA-24 present as an INVERTED impairment**, **DA-23 C 12/12** |
| **IRDM** | Iridium Communications | tech.telecom_services | 8% | **P2 test — best operator** | 15.1% operating margin *falling* from 23.2% while revenue grew 3.8%. If value migrated to operators, this is where it should show | **P11** (RKLB deal security — pre-merger basis), **DA-23** |
| **GSAT** | Globalstar | ⚠️ **`tech.tech_hardware`** — *not* telecom_services | 7% | **Purest monopsony** | Thinnest operator margin in the universe — **7.4%** — on revenue that **declined 3.5%**. If value migrated to operators, it did not arrive here. ⚠️ **Carries NO DA census from 002** — and its sector assignment differs from SATS', so a node-derived peer set drops it silently | **P11** (AMZN deal security), **DA-23 UNTESTED** |
| **LUNR** | Intuitive Machines | industrial.aerospace_defense | 7% | **Payload customer** | Launch as a cost input. ⚠️ **RESOLVED 2026-09-18: the 42.1% DOES NOT EXIST.** It is **\|FY2025 ANNUAL operating margin\| mislabelled as a quarter** — a **DA-26 defect carrying a DA-23 sign strip**, not a genuine one-off. True standalone Q4 2025: revenue **$44,785k**, operating loss **$(33,095)k**, margin **−73.9%** — the worst quarter of 2025. True series: Q1 26 **$186.730M / $(39.201)M / −21.0%**; Q2 26 **$206.168M / $(47.136)M / −22.9%**; FY2025 **$210.059M / $(87.231)M / −41.5%** | **DA-23 instance #7** (12 of 12 periods, exact magnitude, opposite sign), **DA-26** |

### Sector-coverage note (carried, not assumed) — ⚠️ CORRECTED 2026-09-18

Sector values for **IRDM** and **GSAT** were to follow the platform's assignment for **SATS**
(`tech.telecom_services`). **That is half-confirmed, and the half that fails is load-bearing:**

| Ticker | Assumed | Actual | Consequence |
|---|---|---|---|
| **IRDM** | `tech.telecom_services` | **confirmed** | — |
| **GSAT** | `tech.telecom_services` | ⚠️ **`tech.tech_hardware`** | **A comparator set assembled by taxonomy node therefore SILENTLY OMITS the P6-subscribed `GSAT × competitive` leg.** The omission is invisible — it looks like a clean result. |
| **YSS** | (unstated) | **no source states a YSS sector value at all** | Unverifiable from these sources |

**This is why the universe is pinned by ticker, not by node.** Any 003 phase that derives its
peer set from a sector or taxonomy field must verify membership explicitly — 002's own
competitive artifact caught this only because GSAT failed to appear where it was expected.

---

## Metric → DA class map

The DA classes that bind on this thesis's core metrics. A figure in the left column
**cannot be quoted** without the reading in the right column.

| Metric | Forbidden without | Why |
|---|---|---|
| `cost per kg to LEO` | which DA-01 basis (**A / A′ / B / C**) | The four bases span ~$500–$6,600/kg — a **7–13× spread around one Falcon 9 mission**. Only **B** tests the F5 propellant floor: A carries margin, C carries R&D. |
| any `$/kg` | the **denominator orbit** (DA-02) and the **payload kg** | GTO is ~3× harder than LEO per kg. Mixing them silently invalidates every comparison. |
| the word "reusable" | the **architecture label** (DA-03): fully expendable / partially reusable / fully reusable | Full-stack reuse changes DA-01's denominator far more than booster-only reuse. The word alone conveys neither. |
| `operating_income` / `operating_margin` | the **component derivation** `gross_profit − opex`, in-line, **with the opex definition stated** | **DA-23** sign stripping; **DA-24** non-operating contamination. `EPS × shares` is *not* an admissible sign test. ⚠️ **The identity is CONDITIONAL, not universal** — see the note below. |
| any per-unit metric | the **basis field** it was normalised against | **DA-25**. A normalised $/launch is a different quantity from an as-filed one. |
| any "quarterly" figure from the metrics block | the **issuer's fiscal calendar** | **DA-26** — annual mislabelled quarterly, **20 issuers tested, 19 exhibiting**. ⚠️ **Corrected 2026-09-18: "19 of 19 / universal" is WITHDRAWN.** FLY shows zero instances, falsifying universality (002 §3.3). **DA-27** — calendar-derived fiscal labels, **6 confirmed**. |
| any share count / per-share figure around an IPO | a **post-IPO check** | **DA-28** — capital-structure discontinuity invalidates share-count detectors. |
| any reconciliation that "closes" | the **derivation**, not the result | **DA-29** — a reconciliation that closes is not thereby a check. `computed` is an opaque assertion. |
| two figures on one concept | **both**, with the basis field (**DA-30**) | Collapsing two bases without recording which is which is the platform collapse. |
| `launch price` vs `launch cost` | which one, explicitly (DA-06) | For a **captive** integrated operator no transaction price exists at all — SPCX is exactly this case. |

---

## P11 deal-security register (mandatory tagging)

| Ticker | Deal | Basis to tag |
|---|---|---|
| **RKLB** | Acquirer | `standalone_pre_merger` |
| **IRDM** | Target (RKLB) | `standalone_pre_merger` |
| **GSAT** | Target (AMZN) | `standalone_pre_merger` |

Every figure drawn from these three describes a business **contractually ceasing to exist**.
The tag is carried on every claim; the `risk` light row in §3 exists to carry it.

---

## Load-bearing absences (named, never proxied)

| Absent | Why it matters | Owner |
|---|---|---|
| **BA** (Spectrolab) | Second leg of the space-solar-cell duopoly — **the first term in constitution bound F1**. SolAero (RKLB) is the only leg inside this universe. | 007 / 008 |
| **BWXT** | F2's nuclear escape hatch — the only path to the **order-10² m²/MW** cell at 500 K. ⚠️ **Do NOT quote `313 m²/MW` or `24×` as point values** (002 downgraded F2 to a **qualitative** bound; with a COP = 2 heat pump it is **470 m²/MW**, and the 24× becomes **9.6×–16.8×**) | 002 |
| ~~Every fully expendable vehicle's F5 floor~~ | **CLOSED — do not re-raise.** An earlier version of this table recorded "F5a/F5b do not reach Electron and Alpha" as an open amendment candidate. **That was wrong**: F5 was split **three** ways at constitution **v1.3.0**, and **F5c (fully expendable, whole-vehicle manufacturing)** completes it — *"the only architecture with a `DEMONSTRATED` price."* | **Resolved at v1.3.0** |

---

## `unresolvable` — the two classes, and why they differ

Per `contracts/artifact-frontmatter.yaml`, `unresolvable: true` requires a class:

- **`UNRESOLVABLE-FROM-PUBLIC-SOURCES`** — no disclosure exists. Remedy: name the specific
  disclosure that would settle it. On this thesis the standing instance is **Falcon 9 basis B**
  (the marginal-cost stack), for which 001 named the candidate anchor: NASA CRS/Commercial
  Crew contract values as a revealed-price floor.
- **`UNRESOLVABLE-FROM-PLATFORM`** — the disclosure exists but the platform does not carry it.
  Different remedy: a retrieval-coverage action, not a research one.

Conflating them sends the reader to look for a filing that does not exist, or to give up on
one that does.
