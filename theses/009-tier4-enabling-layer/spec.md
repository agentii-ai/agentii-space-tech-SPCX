# Research Thesis: 009 — Tier 4: Enabling Layer (Power, Thermal, Compute)

**Constitution Ref**: constitution.md v1.4.0 (`constitution_pin: 1.4.0`)
**Created**: 2026-09-18
**Status**: **PLANNED — stub spec. Not frozen. No tasks may be generated.**
**Wave**: 2 (activates when a slot opens under `max_theses_active: 6`)
**板块**: Tier 4 · **Binding constraint**: **MULTI — DECLARED** (P3 compromise, to be justified on activation)

> This file reserves the thesis ID and records the design intent. It is **not** a
> specification. Replace wholesale on activation.

## 0. Inherited baseline (to be completed on activation)

001 produced more on this tier than on any other, because it is where **A2's
constraints actually bind**. Inherited results, not to be re-derived:

- **Terrestrial compute is constrained but expanding, and highly profitable.** MSFT
  FY2026 capex **$115,948M** — at the reported $10–40M/MW that is **2.9–11.6 GW of new
  capacity annually**, against **SPCX's 1.4 GW cumulative** nameplate draw. *"Microsoft
  alone adds ~8× SPCX's entire installed base every year."* Alphabet adds ~$80B
  annualised. 001 called this **"the strongest single datum against the orbital-compute
  case produced anywhere in this thesis."**
- **"Bottleneck" is superseded as a framing.** VRT's operating margin *expanded 2.7 pts
  on +24.1% revenue* — scarcity pricing, which is what a functioning market produces. An
  expensive competitive scaling supply chain is a **harder** competitor than a bottleneck.
- **F2 precedes F4 empirically.** Starcloud-1's H100 failed on **thermal**, not
  radiation — the first gate stopped it before the second was tested. 001's clearest
  theory-to-observation match.
- **The GPU is not the dominant cost term.** NVDA's 65.6% margin sits against
  $2.3–4.6M/MW of power+thermal at the F5a floor and $10–40M/MW all-in.
- **NVDA has no space product line** and is **R&D-intensive at 7.7%** — so its absent
  rad-hard SKU is a **revealed preference about market size**, not a capability gap.
- **P5's terrestrial denominator is `UNRESOLVABLE-FROM-PLATFORM`** — colocation and
  greenfield costs are **commercially licensed** data, a stronger condition than merely
  unreachable. VRT bounds the **cooling equipment share only**.
- **The "capability real, business immaterial" pattern** has 4–5 instances here and
  across the universe, suppressing the very disclosure P10's falsifiers need.

**P10 gate status: UNMET on all five conditions.** No listed issuer reports
orbital-compute revenue. 009 **must not underwrite it.**

## 1. Research Question

**If the enabling layer is where A2's constraints bind, which listed issuers are
*positioned* to sell into an orbital build-out regardless of which operator wins — and
how much of that positioning is already priced?**

The question is deliberately **not** "is orbital compute viable." That is 003's framing
problem and P10's gate. 009 asks the narrower, investable question.

## 2. Universe Definition

| Ticker | Company | Relevance to A2 | Coverage |
|---|---|---|---|
| VRT | Vertiv | Thermal management at scale — the terrestrial comparator defining the orbital cooling penalty | READY — 90 filings (sector: `machinery`) |
| NVDA | NVIDIA | Compute silicon; H100 flew on Starcloud-1 with the F2 cooling failure | READY — 169 filings |
| GOOG | Alphabet | **Project Suncatcher** — TPU orbital data centers, 81-satellite reference config | READY — 146 filings. **Query as `GOOG`, never `GOOGL`** |
| MSFT | Microsoft | Azure Space; the terrestrial comparator at hyperscale | READY — 52 filings |
| AMZN | Amazon | **Amazon Leo** (~180–200 sats, 3,200 by 2029, ~$17B capex committed); acquiring Globalstar | **PARTIAL** — sector unassigned |
| AAPL | Apple | ~20% of Globalstar + rights to 85% of its network capacity; D2D anchor demand | **PARTIAL** — sector unassigned |
| AMPX | Amprius Technologies | High-specific-energy silicon-anode cells; space/HAPS heritage | **NOT_READY** — no data |
| ENS | EnerSys | Battery systems including space-qualified cells | **NOT_READY** — no data |
| TMUS | T-Mobile US | Starlink direct-to-cell commercial partner | **NOT_READY** — no data |

**`ENS` carries a fund-sourced case in the corpus (Brown Advisory, Sustainable Small Cap
Core) with no issuer coverage** — the same asymmetry as MOG-A in 008. Record it.

**`PARTIAL` names require manual sector assignment before any aggregate constraint
evaluates.** That assignment is a precondition, not an assumption.

## 3. Skill Deployment Matrix (outline — not frozen)

1. **Picks-and-shovels positioning**: for each name, is there a *signed or contracted*
   path to orbital revenue, or only a capability narrative? Grade every claim.
2. **The terrestrial comparator as the real competitor.** VRT/MSFT/NVDA are not just
   suppliers — they are the **alternative** the orbital case must beat. Model both sides.
3. **P10 gate audit** — the five conditions (revenue/offtake, radiator derivation, array
   derivation, launch cost vs F5a, radiation TID/SEU) assessed per named operator, with
   the verdict that orbital compute is a **watch item, not a thesis**, unless all five
   are met. **003 owns the framing; 009 owns the investable consequence.**
4. **Power and battery storage** (AMPX, ENS) as the layer beneath the layer — and the
   `NOT_READY` gap that makes it currently unresearched.

**Candidate binding constraint — MULTI, declared.** Thermal (F2) binds the compute
narrative; `CAPITAL` binds the terrestrial comparator; regulatory (F6) binds the D2D
demand side. **These do not reduce to one constraint**, and P3's rule is met by saying
so explicitly rather than naming one falsely — the same compromise 005 declares.

## 4. Dependencies

- **002** owns F2's physics validation; **003** owns the cost-curve framing. 009 must not
  duplicate either.
- **006** (Tier 2) — D2D is a compute-adjacent demand signal.
- **010** — the microgravity demand side shares the "immaterial-to-counterparty" pattern.
