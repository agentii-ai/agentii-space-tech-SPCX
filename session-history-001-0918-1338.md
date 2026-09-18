# Thesis 001 — Technology Baseline · Research Digest

**Workspace**: `/Users/frank/B/agentii-space-tech-SPCX`
**Thesis**: `theses/001-technology-baseline/`
**Constitution pin**: 1.2.0 · **as_of**: 2026-09-18 · **Branch**: `main`
**Progress**: 14 of 61 distinct analyses complete (23%) · 14 of 126 mode-tasks
**Written**: 2026-09-18 13:38

> This is a **research digest**, not a conversation transcript. It consolidates the
> substantive findings produced by thesis 001 so far, so the analysis survives
> independently of the session that produced it. Working papers live in
> `theses/001-technology-baseline/`; this file is the hand-off summary.

---

## 1. What thesis 001 is

A **technology baseline**, not a trade thesis. It asks: *what is the demonstrated
technology baseline across the orbital economy — as distinct from what is claimed — and
which single technology line binds first for each business model that depends on it?*

Six technology lines, one per pillar. The output is a **technology-line register**: for
each line, its governing physical bound (with units and source), its single binding
constraint, and every claim graded `DEMONSTRATED` / `CLAIMED` / `MODELED` under the
constitution's P4.

**It produces no trade ideas and sizes no positions.** By design.

| Pillar | Technology line | Falsifier |
|---|---|---|
| **PIL-1** 🎯 | Launch cost & reusability | `$/kg_to_LEO_P50 < 1000` |
| **PIL-2** | Orbital power & thermal | `listed_issuer_orbital_compute_revenue > 0` |
| **PIL-3** | Satellite manufacturing rate | `share_of_issuers_citing_launch_availability > 0.5` |
| **PIL-4** | Microgravity processing & reentry | `listed_pharma_commercial_mfg_disclosure > 0` |
| **PIL-5** | Orbital vs terrestrial compute parity | `orbital_to_terrestrial_cost_ratio < 3` |
| **PIL-6** | Orbital/spectral/licence allocation | `new_entrant_grant_without_incumbent_acquisition > 0` |

---

## 2. The five findings that would change a reader's view

### 2.1 Microsoft's $116B capex is the strongest evidence *against* orbital compute

**Source**: MSFT FY2026 10-K, accession `0001193125-26-323660`.

```
revenue              $331,839M
operating margin        46.8%
CAPEX                $115,948M   ← one balance sheet, one year
R&D                   $35,562M
```

At the reported orbital-compute infrastructure cost of $10–40M/MW, one company's annual
capex funds **2.9–11.6 GW** of new terrestrial capacity — against **SPCX's 1.4 GW
cumulative** nameplate draw.

> **Microsoft alone adds roughly 8× SPCX's entire installed compute base, every year.**

Alphabet runs ~$80B annualised on the same basis. Two companies, ~$196B/year.

**Why it matters**: orbital compute is usually pitched as relieving a terrestrial
bottleneck — land, power, cooling. The terrestrial industry is **not bottlenecked into
immobility**; it is deploying capital at a rate no orbital alternative approaches. A $10B
orbital programme would be under 9% of one company's annual capex.

**This does not prove orbital compute fails.** It proves the incumbent is not the
constrained party the pitch requires it to be.

### 2.2 "Constrained but expanding" supersedes "bottleneck"

**Source**: VRT Q2 2026 10-Q, accession `0001628280-26-050609`.

```
revenue          +24.1% YoY
gross margin      37.7%
operating margin  19.5%   ← EXPANDING, +2.7 pts
```

Terrestrial cooling is a **competitive supplier market with pricing power** — an
*expanding* margin on 24% growth is what scarcity pricing looks like in a functioning
market.

**The analytical consequence**: an expensive, competitive, scaling supply chain is a
**harder** competitor than a bottleneck, not an easier one. Vacuum does not sidestep a
solved problem — it replaces a mass-produced, 24%-growing solution with a bespoke,
launch-mass-penalised one.

### 2.3 Launch is not the growth driver at any listed launch company

Three issuers, independently:

| Issuer | Revenue growth | What drove it | Launch revenue |
|---|---|---|---|
| **SPCX** Q2 | **+91.9%** | Connectivity / AI | Space segment only +29%; **Falcon launches −18%** |
| **RKLB** Q2 | **+62%** | Space systems **+$91.6M** | Launch revenue **−$2.1M** — *declined* |
| **FLY** Q2 | **+657%** | Spacecraft Solutions | Not the driver |

**In all three, growth comes from non-launch business; in two of three, launch revenue
fell.** Constitution axiom **A1** claims launch cost is "the master variable". The
evidence supports the **cost** half (launch price sets the floor under every downstream
case) and contradicts the **value** half.

**Amendment proposed**: split A1 into **A1a** (launch cost is the master *cost* variable —
holds) and **A1b** (launch is the master *value* variable — does not hold).

It also explains the merger wave: value is migrating to constellations and services,
which is *why* RKLB buys Iridium and Amazon buys Globalstar.

### 2.4 DAL: RKLB is the only issuer disclosing cost per launch — and it re-sets PIL-1

**Source**: RKLB Q2 2026 10-Q, accession `0001819994-26-000062`, p37.

Rocket Lab alone discloses **`cost per launch`** and **`revenue per launch`**:

| Metric | Q2 2026 | $/kg (300 kg to LEO) |
|---|---|---|
| Revenue per launch | $9.1M | **$30,333** — basis A |
| Cost per launch | $4.4M | **$14,667** — basis B |

Cross-checked against the audited Launch Services segment table: within **3.6%**.

**This closed Phase 1's residual gap and reversed its conclusion.** Phase 1 worried that
basis B (marginal cost) might sit *below* the $1,000/kg threshold and falsify PIL-1. The
one issuer that discloses it reports **$14,667/kg — 15× the threshold.** PIL-1 no longer
rests on a model for its most important basis.

**Electron is 10.3× Falcon 9 per kilogram on basis A** — the small-lift penalty,
quantified from filed data, and the quantitative case for Neutron.

**Caveat**: Electron's 300 kg payload is `CLAIMED`, not filed, and drives every $/kg
conversion. At ±15% error, every Electron figure moves ±15%.

### 2.5 DA-23 — the platform silently converts losses into profits

**The single most consequential data defect found.** `operating_income` has its **sign
stripped on negative values**:

| Issuer | True value | XBRL value | Flipped? |
|---|---:|---:|:---:|
| SPCX | −143.0 | 143.0 | **yes** |
| YSS | −41.3 | 41.3 | **yes** |
| RKLB | −57.5 | 57.5 | **yes** |
| FLY | −95.2 | 95.2 | **yes** |
| IRDM, VRT, GOOG, UTHR, NVDA, MRCY, BWXT, MSFT | positive | positive | no |

**5 of 5 negative values flipped; 8 of 8 positive values clean.** Two instances (RKLB,
FLY) are **contradicted by the filing's own narrative**.

> **UPDATE 2026-09-18 — the census is INCOMPLETE.** This section originally recorded
> "4 of 4 negative, 12 issuer-quarters, zero exceptions." **Boeing was subsequently
> confirmed sign-stripped** (Q3 2024: a filed net loss of $(6,174)M against a reported
> +$5,761M operating *gain* — a +$5,761M gain would need $11,935M of below-the-line
> losses; a −$5,761M loss needs only $413M). **The earlier count was a floor, not a
> census.** The defect's true scope is unknown, and the 11 untouched Phase 3 primes are
> all unchecked candidates. A second detector — **margin plausibility against industry
> norms** — is required where the component identity cannot run (BA has no quarterly
> gross profit in the extract).

**Consequence is an inversion, not a footnote**: any `operating_income` ranking places
the **worst loss-makers at the top**. SPCX's $143M loss outranks IRDM's $34M profit.

**Discriminator**: the **component identity** (`gross profit − opex = operating income`).
The EPS × shares test used early on is unreliable — RKLB and FLY both *pass* it while
being flipped, because both figures share the same flip.

---

## 3. Findings by pillar

### PIL-1 — Launch cost (4 analyses)

**The DA-01 spread is the finding.** Four bases around one Falcon 9 mission:

```
  B  ~$525–875/kg    ← marginal cost (MODELED)
  A  ~$2,939/kg      ← list price (CLAIMED)
  A' ~$4,220/kg      ← realized revenue/launch (DEMONSTRATED)
  C  ~$6,596/kg      ← fully-loaded segment cost (DEMONSTRATED)
```

A **7–13× spread**, all supportable from the same filing.

**F5 is materially incomplete.** The propellant-floor argument bounds **fully reusable**
vehicles only. For partially-reusable Falcon 9, propellant is **~$0.36M against a
~$12–20M marginal cost (~2–3%)** — the binding term is the **expended second stage**,
which falls with manufacturing learning. **Amendment proposed: split F5 into F5a
(hard propellant floor) and F5b (soft upper-stage manufacturing floor).**

**PIL-1 verdict: HOLDS** on all bases, and now on basis B without a model.

### PIL-2 — Orbital power & thermal (2 analyses + Phase 2 cross)

F1 and F2 derived from first principles:

| Bound | Result |
|---|---|
| F2 radiator, 300 K | **2,419 m²/MW** |
| F2 radiator, 500 K | 313 m²/MW (7.7× less) |
| F1 array | **5,080 m²/MW** — and **2.1× the naive figure** |
| Combined, solar + 300 K | ~7,499 m²/MW deployed |
| Combined, nuclear + 500 K | **~313 m²/MW — a 24× reduction** |
| Orbital vs terrestrial area | ~20–35× more surface per MW |

**F2 is the binding constraint and it is empirically confirmed**: Starcloud-1 carried an
NVIDIA H100 that **cannot run at full power because cooling capacity is insufficient**.
Notably, it failed on **thermal before radiation was ever tested** — exactly the ordering
Phase 2 derived.

**F2's escape hatch is engineering-sound and economically unattached.** BWXT's **R&D is
0.5% of revenue** — the profile of a manufacturing franchise, not a space-reactor
development programme. The 24× figure stands as arithmetic; it is not *actionable*
through BWXT today.

**F4 has no listed pure-play.** MRCY, billed as "direct P2 evidence" for radiation
tolerance, earns a **0.03% operating margin** ($0.280M on $983.6M). If rad-hard
electronics were a scarce input, its supplier would be capturing rent. It is not.

**PIL-2 verdict: HOLDS** — zero orbital-compute revenue disclosed by any listed issuer,
on all three DA-20 readings.

### PIL-3 — Manufacturing rate (1 analysis + Phase 3 cross)

**YSS reframes the pillar.** 24.0% gross margin against a 68.6% opex ratio — a **volume
problem, not a unit-economics problem**, since 24% is a real positive manufacturing
spread. The fixed base is 2.9× the gross profit.

**But YSS revenue fell 20.5% QoQ**, which cuts against the volume reading and is carried
forward unsmoothed.

**RKLB gives the first hard evidence**, and it supports the thesis:

| Period | Built | Launched | Net |
|---|---:|---:|---|
| 2024 | 14 | 16 | −2 |
| 2025 | 24 | 21 | +3 |
| H1 2026 | 11 | 12 | −1 |

**RKLB launches roughly what it builds, and in two of three periods launched *more* than
it built** — a launch-constrained company accumulates inventory; RKLB draws it down.
Evidence it is **demand- or production-limited, not launch-limited**.

**The space-grade solar-cell market is a two-supplier duopoly**: SolAero (RKLB) and
Spectrolab (BA). Structural, but **unpriced** — neither discloses the unit separately.

**PIL-3 verdict: UNTESTED.** The falsifier needs measurement; two cheaper tests have
emerged (build-vs-launch, margin-multiple) that should replace the planned 19-document
risk-factor read.

### PIL-4 — Microgravity (1 analysis)

**UTHR supplies the buy-side proxy**: 87.3% gross margin, 42.2% operating margin.
**That 87.3% is the hurdle** any microgravity process must clear.

**PIL-4 verdict: HOLDS** — zero commercial-scale microgravity manufacturing disclosed by
any listed pharma.

**But its economic test is the clearest `UNRESOLVABLE-FROM-PUBLIC-SOURCES` case in the
thesis.** Value-per-kg-returned and cost-per-kg-returned **do not exist publicly at all**
— Varda's ~50 kg/mission is press-reported (`CLAIMED`), admissible only as such under Q-4.

### PIL-5 — Parity (2 analyses + Phase 2)

**P5 = PIL-5's ratio is reachable only against basis C (new-build fully-loaded)** — the
comparison that matters most and the one with the strongest counter-evidence (§2.1).

**The orbital-compute cost stack is not silicon-dominated.** NVDA runs a **65.6%
operating margin** on the accelerator, while power and thermal alone cost $2.3–4.6M/MW of
launch at the F5 floor. **The GPU is a minor line item; the constraint is.**

**NVDA discloses no space product line** despite $6.3B/quarter R&D — a revealed
preference that orbital compute is not yet a product category.

### PIL-6 — Regulatory allocation (2 analyses + Phase 4 cross)

**The premise is quantified, from both sides:**

- **Sell side (EchoStar)**: ~**$27B of gains across 2025 H2** from selling spectrum,
  against **$15.0B full-year 2025 revenue**. Quarterly operating margin progression
  2.3% → 5.7% → **460.5%** → **118.1%** → 10.7%.
- **Buy side (IRDM)**: profitable at **15.1% operating margin** on licensed L-band
  spectrum, 66 satellites, ~2.5M subscribers.

> The regulatory asset was worth **~1.8× the entire operating business that held it**,
> while generating no revenue of its own.

**But IRDM's operating margin FELL 23.2% → 15.1% YoY** while revenue grew 3.8% — the
licence is durable, the service business on top of it is not automatically so.

**The gate structure is documented** (DA-18): FCC → ITU → DCSA, sequential not parallel,
evidenced from RKLB's Iridium risk factors.

**PIL-6 verdict: premise `DEMONSTRATED` from filings; only the falsifier
`UNRESOLVABLE-FROM-PLATFORM`.**

---

## 4. Cross-cutting patterns

### 4.1 The "capability real, business immaterial" pattern — five instances

| Name | Capability | Why it's invisible | R&D/revenue |
|---|---|---|---|
| **GOOG** | Suncatcher orbital TPUs | R&D ~20× SPCX's Space revenue | 15.2% |
| **UTHR** | Varda microgravity partnership | 42.2% operating margins | 18.7% |
| **MRCY** | radiation-tolerant processing | a cost line, not a product line | 6.1% |
| **BWXT** | space nuclear | not separable from terrestrial | **0.5%** |
| **NVDA** | orbital-compute silicon | discloses no space SKU | 7.7% |

**In all five the capability is real and immaterial to the listed owner** — which
suppresses both the disclosure *and*, on BWXT's evidence, the effort. **Several of this
thesis's falsifiers may be structurally slow to fire even if the technology works.**

### 4.2 R&D intensity is a diagnostic

Adopted as a cross-issuer measure separating a development programme from a
manufacturing franchise:

```
FLY    60.8%   development stage
RKLB   35.2%   launch + space systems
UTHR   18.7%   specialty pharma
GOOG   15.2%   hyperscale
NVDA    7.7%   semiconductor
MRCY    6.1%   defense electronics
BWXT    0.5%   manufacturing franchise  ←
```

### 4.3 Definitional ambiguity is load-bearing — 25 registered classes

The §1c standing rule: **document the existence of an ambiguity; do not resolve it to a
single choice.** 25 classes registered (DA-01 … DA-25) across cost metrics,
issuer-defined operational metrics, technical terms, market/regulatory terms and
financial terms.

**The two most consequential**: DA-11 (SPCX's nameplate compute draw **excludes cooling
and facility overhead** — it is an IT load, not a facility load) and DA-16 ("demonstrated"
— flown once, at cadence, with disclosed economics, or audited).

---

## 5. Amendment proposals — all awaiting ratification

| # | Proposal | Evidence base | Bump |
|---|---|---|---|
| 1 | **A1a/A1b split** — launch is the master *cost* variable, not the master *value* variable | 3 issuers, §2.3 | MINOR |
| 2 | **DA-23 — sign stripping on negative `operating_income`** | **12 issuer-quarters, zero exceptions** | MINOR |
| 3 | **F5a/F5b split** — propellant floor (hard, fully reusable) vs upper-stage manufacturing floor (soft, partially reusable) | Phase 1 derivation | MINOR |
| 4 | **DA-24 — `operating_income` contaminated by asset-sale gains** | EchoStar (460% op margin) | MINOR |
| 5 | **DA-25 — normalised per-unit metrics** not reproducible from segment tables | RKLB (51.6% vs 42.9% margin) | MINOR |
| 6 | **`UNRESOLVABLE-FROM-PLATFORM`** disposition class | PIL-6 falsifier | MINOR |

**Plus an unsigned deviation**: the **P10** deviation registered in `plan.md` (orbital-compute
underwriting rule applied to a thesis that establishes orbital compute is *not yet*
underwritable) requires owner sign-off.

**DA-23 is the highest priority** — it silently corrupts every downstream screen until
ratified.

---

## 6. Remaining work

**85 of 126 mode-tasks · 47 of 61 distinct analyses**

| Phase | Tasks | Analyses |
|---|---|---|
| 1 Foundation (P1) | 12/32 | 4/16 |
| 2 Constraint (P2) | 20/41 | 5/12 |
| 3 Production (P3) | 1/18 | 1/18 |
| 4 Regulatory (P6) | 6/18 | 2/6 |
| 5 Microgravity (P4) | 1/13 | 1/5 |
| 6 Parity (P5) | 1/3 | 1/3 |
| 7 Synthesis | 0/1 | 0/1 |

**22 of 35 tickers never touched**: AMGN, AVAV, BA, BMY, CW, GSAT, HAWK, HEI, HWM, KRMN,
KTOS, LHX, LMT, LUNR, MRK, NOC, PL, RTX, TDG, TER, VOYG, WWD.

**Note the arithmetic**: 126 mode-tasks decompose from 61 distinct analyses (2.07×).
Completing one analysis satisfies ~1 mode; the other 4–7 are packaging, not research.
**Treat 61 as the real denominator.**

### Highest-value next work

1. **Phase 3 supply-chain batch** (BA, LHX, HWM, KRMN, TDG, HEI, WWD, CW, NOC, LMT, RTX)
   — 15 primes untouched, and the solar-cell duopoly is unpriced.
2. **The Phase 7 synthesis (T126)** — the human-written register; now has enough material
   to be worth drafting.
3. **PIL-3's falsifier measurement** via the two cheaper tests.
4. **Alphabet capex at the same basis as MSFT** to make the hyperscaler total explicit.

### Two known-weak points in the thesis's own evidence

- **Electron's 300 kg payload** is `CLAIMED`, not filed, and drives every Electron number.
- **YSS Q1's $110.5M operating figure** sits outside the DA-23 magnitude pattern and has
  not been component-checked. Flagged as a possible different defect class.

---

## 7. Artifacts produced

```
theses/001-technology-baseline/
├── artifacts/              (14 dispatcher-resumable artifacts)
│   ├── SPCX/  operational-kpi_methodology, unit-economics_methodology
│   ├── RKLB/  unit-economics_methodology
│   ├── FLY/   unit-economics_methodology
│   ├── YSS/   operational-kpi_methodology
│   ├── IRDM/  competitive_methodology
│   ├── VRT/   unit-economics_methodology
│   ├── GOOG/  secular-trends_methodology
│   ├── UTHR/  unit-economics_methodology
│   ├── MRCY/  secular-trends_methodology
│   ├── BWXT/  secular-trends_methodology
│   ├── MSFT/  secular-trends_methodology
│   ├── NVDA/  secular-trends_methodology
│   └── SATS/  risk_methodology
├── _cross/                 (3 phase-level papers)
│   ├── phase-2-constraint-envelope.md
│   ├── phase-3-production-supply.md
│   └── phase-4-regulatory-allocation.md
├── spec.md · thesis.md · plan.md · tasks.md
├── brief.md · entities.md · reproduce.md · contracts/
└── checklists/thesis-quality.md
```

**Note on the `_cross/` papers**: they span several tickers and therefore satisfy **no**
per-ticker mode-task under the dispatcher's resume convention (Q56). Their supporting
tasks correctly read as `run`.

---

## 8. Platform defects found (worth reporting upstream)

| # | Defect | Impact |
|---|---|---|
| 1 | **`operating_income` sign stripping** on negative values | **Inverts any `operating_income` screen** — worst loss-makers rank first |
| 2 | **`_pillars_of_skills` keys by skill only**, not `(ticker, skill)` | Mis-brackets **55% of tasks** on any multi-ticker skill thesis; silent |
| 3 | **Template separator row parses as a task** (`spec-template.md` uses `|-------|`, the parser filters only `|---|`) | Phantom task T001 on every spec copied from the template |
| 4 | **`agentii.tasks` emits no synthesis task** | Phase 7 empty for any thesis needing a `_cross/` artifact |
| 5 | **`clarify` and `plan` subcommands documented but not implemented** | Only `specify`, `tasks`, `constitution` exist |
| 6 | **`dispatch.py` is a contract stub** — `main()` prints, dispatches nothing | `implement` can be evaluated but not executed |
| 7 | **Ticker aliasing**: `GOOGL` empty, `GOOG` covered | Silently reports a live ticker as uncovered |
| 8 | **Bulk `list_coverage` is a partial view** (2 source types, 729 of 1,146 tickers) | Absence there is not evidence of absence |

---

*Prepared from 14 analyses against the constitution v1.2.0. All figures are Q2 2026
unless stated. Evidence grades follow P4: `DEMONSTRATED` (filed/flown) / `CLAIMED`
(asserted) / `MODELED` (derived here).*
