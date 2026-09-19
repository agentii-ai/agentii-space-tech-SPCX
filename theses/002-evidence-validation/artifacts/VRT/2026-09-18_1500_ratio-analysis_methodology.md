---
thesis_id: "002-evidence-validation"
pillar: PIL-5
ticker: VRT
skill: ratio-analysis
mode: methodology
generated_at: 2026-09-18T15:00:00Z
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "2d27c7f751fa"
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
deal_security_basis: not_applicable
definitions_used:
  - da_id: DA-23
    chosen_reading: >
      Sign stripping on a bidirectional concept whose filed cell is parenthesised. Applied
      here with the A8 weight discriminator AND the A17 directionality boundary: a concept
      entering its calculation parent at weight -1 carries a positive magnitude
      LEGITIMATELY, so a ratio built on such a concept is not evidence of a strip.
  - da_id: DA-24
    chosen_reading: >
      Non-operating contamination of operating income, in EITHER direction (gain or charge).
      At VRT applied as the component-level question: does every term inside the operating
      stack belong there, on the filed face?
  - da_id: DA-25
    chosen_reading: >
      Normalised per-unit / non-raw metrics. At the ratio layer this is read as: any served
      ratio whose numerator or denominator is a normalised, averaged, or period-blended
      quantity that no filed cell states.
  - da_id: DA-26
    chosen_reading: >
      Annual figures mislabelled as quarterly in the metrics block. Applied at the RATIO
      layer as a period-basis question: does a quarterly-labelled row carry a fiscal-year
      flow?
  - da_id: DA-27
    chosen_reading: >
      Fiscal-period labels derived from the calendar quarter rather than the issuer's fiscal
      calendar, with the A4 source discriminator: a label defect sourced from a POPULATED
      but incorrect registry field is material; one derived from an absent calendar is
      cosmetic. VRT's fiscal year IS the calendar year, so this discriminator is the only
      one that applies.
  - da_id: DA-28
    chosen_reading: >
      Capital-structure discontinuity invalidating share-count-based detectors. Tested as the
      A3 generalisation: any present multi-class structure with non-identical per-share
      economics, or any disclosed future share-count-changing event.
  - da_id: DA-29
    chosen_reading: >
      Back-solved and opaque checks. The mechanical test is run on the TERMS, not the
      closure: if any term in a reconstruction appears nowhere in the source, the check is a
      back-solve, and a back-solve closes exactly. Applied to every reconstruction attempted
      in this artifact, including my own.
  - da_id: DA-30
    chosen_reading: >
      Two bases on one concept, collapsed without a basis field. Applied at the ratio layer:
      a served ratio is a DA-30 instance when the concept it is built from is reported by the
      issuer on more than one basis and the served value names none.
evidence_grade: DEMONSTRATED
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
citations:
  - figure: "statement of earnings cells Q2/H1 2026 and Q2/H1 2025: net sales 3,274.3 / 2,638.1 / 5,923.8 / 4,674.1; cost of sales 2,039.4 / 1,741.5 / 3,689.2 / 3,091.0; SG&A 494.4 / 395.6 / 951.1 / 741.9; amortization 73.7 / 46.9 / 151.3 / 92.9; restructuring (3.9) / 1.9 / (8.8) / 3.0; FX 3.9 / 2.3 / 2.3 / 4.9; other operating 28.9 / 7.5 / 60.7 / 7.3; operating profit 637.9 / 442.4 / 1,078.0 / 733.1 — and NO gross-profit line"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 5
    url: https://agentii.ai/v/VRT/sec136/5
    located_via: read_source_pages
  - figure: "balance-sheet cells 2026-06-30 / 2025-12-31: cash 2,810.6 / 1,728.4; short-term investments 300.0 / 99.5; accounts receivable 3,750.3 / 3,109.0; inventories 2,522.7 / 1,456.5; total current assets 9,984.9 / 6,819.5; total assets 15,900.9 / 12,212.4; total current liabilities 7,243.0 / 4,407.0; long-term debt net 2,939.8 / 2,892.1; total liabilities 11,143.3 / 8,271.1; total equity 4,757.6 / 3,941.3"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 7
    url: https://agentii.ai/v/VRT/sec136/7
    located_via: read_source_pages
  - figure: "cash-flow cells H1 2026 / H1 2025: net income 887.9 / 488.7; depreciation 66.9 / 46.4; amortization 156.6 / 98.5; change in fair value of contingent consideration 62.0 / —; net cash from operating activities 1,866.6 / 626.2; capital expenditures (285.9) / (81.5); net cash from financing activities (3.0) / (32.9); beginning cash 1,789.8 / 1,232.2; ending cash 2,875.6 / 1,656.0"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 8
    url: https://agentii.ai/v/VRT/sec136/8
    located_via: read_source_pages
  - figure: "Note 4 disaggregation, three months ended 2026-06-30: Products 2,606.4; Services & spares 667.9; Total 3,274.3 (two months ended 2025-06-30: 2,118.9 / 519.2 / 2,638.1) — against the statement's own products 2,646.7 and services 627.6 on the same total"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 13
    url: https://agentii.ai/v/VRT/sec136/13
    located_via: read_source_pages
  - figure: "Note 11 segment cells, three months ended 2026-06-30: segment cost of sales(1) 2,024.4 (footnote 1: cost of sales EXCLUSIVE of engineering, research and development costs); segment operating profit 791.2; foreign currency (3.9); corporate (75.7); total corporate and other (79.6); amortization of intangibles (73.7); consolidated operating profit 637.9; Americas 2,070.8 less expenses 1,499.4 = 571.4; Asia Pacific 719.9 less 624.3 = 95.6; EMEA 483.6 less 359.4 = 124.2"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 21
    url: https://agentii.ai/v/VRT/sec136/21
    located_via: read_source_pages
  - figure: "MD&A results of operations table: Net sales 3,274.3 / 2,638.1; Cost of sales 2,039.4 / 1,741.5; Gross profit 1,234.9 / 896.6 / 338.3 / 37.7%; Operating profit 637.9 / 442.4 — and the prose 'Product sales increased $487.5 ... Services & Spares sales increased $148.7 ... Gross profit was $1,234.9 in the second quarter of 2026, or 37.7% of sales, compared to $896.6, or 34.0% of sales'"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec136
    page_no: 28
    url: https://agentii.ai/v/VRT/sec136/28
    located_via: read_source_pages
  - figure: "Q1 2026 statement of earnings cells: net sales - products 2,135.8; net sales - services 513.7; net sales 2,649.5; cost of sales - products 1,348.4; cost of sales - services 301.4; cost of sales 1,649.8; SG&A 456.7; amortization 77.6; restructuring (4.9); FX (1.6); other operating 31.8; operating profit 440.1; interest expense (income) net (4.4); loss on extinguishment 6.2; income before taxes 438.3; income tax 48.2; net income 390.1"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 5
    url: https://agentii.ai/v/VRT/sec134/5
    located_via: read_source_pages
  - figure: "Q1 2026 balance-sheet cells 2026-03-31 / 2025-12-31: cash 2,150.6 / 1,728.4; total current assets 7,984.6 / 6,819.5; total assets 13,400.1 / 12,212.4; total current liabilities 5,343.2 / 4,407.0; long-term debt net 2,922.2 / 2,892.1; total liabilities 9,155.2 / 8,271.1; total equity 4,244.9 / 3,941.3"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 7
    url: https://agentii.ai/v/VRT/sec134/7
    located_via: read_source_pages
  - figure: "Q1 2026 cash-flow cells: net income 390.1; change in fair value of contingent consideration 33.2; net cash from operating activities 766.8; capital expenditures (112.6); net cash from financing activities 11.9 (POSITIVE, filed)"
    ticker: VRT
    form_type: 10-Q
    citation_id: sec134
    page_no: 8
    url: https://agentii.ai/v/VRT/sec134/8
    located_via: read_source_pages
key_metrics:
  debt_to_equity_overstatement_x: 3.79
  quick_ratio_understatement_x: 2.33
  ratio_fields_correct: "2/16"
  validator_false_positive_pct: 92.9

---

# VRT × ratio-analysis — methodology: cross-checking every derived ratio against the component identity

**Task (spec §3):** *"Cross-check every derived ratio against the component identity; catches
DA-23/DA-24 residuals (P3, P5)."* **Discharge:** every one of the 22 ratio fields the platform
serves on VRT is cross-checked below against the filed component identity at the primary
period (Q2 2026), and every residual is traced to a named defect or declared unresolved.

**The headline, stated before the evidence.** The component identity closes **exactly, 5 of 5
periods** at VRT — and it is **VACUOUS there**, because both of its terms are derived. The
non-vacuous replacement is a **seven-term filed identity** that also closes 5 of 5. Applying
it, the ratio layer yields **four exact reproductions, one null-by-gap, one duplicate, and
twelve unresolved residuals** — and the largest single finding is not a sign strip at all. It
is that **the served "Q2 2026" ratio row is computed on a mixture of period bases with no
basis field**, which is DA-30 arriving at the ratio layer rather than the statement layer.

---

## 1. The skill pin, computed — and the six-pin validation that licenses it

`skill_pin` for `ratio-analysis` is **`2d27c7f751fa`**, computed — not guessed — by
`scripts/dispatch.py:132`'s `skill_version_hash()`, sha256 over `sorted(skill_dir.rglob("*"))`
updating `p.name.encode()` then `p.read_bytes()`, first 12 hex.

The algorithm was **validated before it was used**, by re-deriving all six pins published in
`theses/001-technology-baseline/reproduce.md`:

| skill | expected | computed | result |
|---|---|---|---|
| operational-kpi | `0730fd170124` | `0730fd170124` | MATCH |
| unit-economics | `e87ee63269a2` | `e87ee63269a2` | MATCH |
| secular-trends | `e6b41dbb2426` | `e6b41dbb2426` | MATCH (2 roots) |
| supply-chain | `8cb3ac1de486` | `8cb3ac1de486` | MATCH |
| competitive | `826995c722a4` | `826995c722a4` | MATCH (2 roots) |
| risk | `953fc5d396e7` | `953fc5d396e7` | MATCH (2 roots) |

**Six of six reproduced**, resolving to **15 separate plugin roots across five plugin
directories** — so the base directory is confirmed:
`/Users/frank/.claude/plugins/marketplaces/agentii-investment-intelligence/`. The skills are
byte-duplicated across `agent-plugins/agentii-equity-agent` (3 roots),
`agentii-plugin` (6), `vertical-plugins/business-intelligence` (2),
`vertical-plugins/equity-research-core` (3) and `vertical-plugins/industry-analysis` (1). **That
redundancy is itself a check:** an algorithm that had hashed absolute paths rather than file
names would have split these duplicates and produced six *mismatches*. It did not. The hashing
function is name-and-bytes only, and 15 byte-identical roots collapsing onto 6 distinct hashes
demonstrates it empirically.

**A second full mirror of the tree was found and independently clears the same bar.**
`/Users/frank/A/agenzym/agentii-investment-intelligence/` reproduces **all six pins identically**,
root-for-root, with the same 15 roots and the same `ratio-analysis` hashes (below). So there are
**two valid base directories and they agree** — which is a stronger position than one: the pin
does not depend on which mirror is read.

`ratio-analysis` has **three roots, and they disagree 2-to-1** — a different situation from every
validated pin above:

| root | hash |
|---|---|
| `plugins/vertical-plugins/quantitative-analysis/skills/agentii/ratio-analysis` | **`2d27c7f751fa`** |
| `plugins/agentii-plugin/skills/agentii/ratio-analysis` | **`2d27c7f751fa`** |
| `plugins/vertical-plugins/models-and-pitches/skills/agentii/ratio-analysis` | `9b1d7a504789` |

`2d27c7f751fa` is the defensible pin on **two independently sufficient grounds**:

1. **Registry membership.** `spec.md` §3 places `ratio-analysis` in the **quantitative-analysis**
   vertical, and `reproduce.md` line 25 records it as
   `| ratio-analysis | essentials_modes | quantitative-analysis | Light — SPCX |`. Two independent
   statements of the thesis's own definition agree.
2. **Tree majority, now established.** `2d27c7f751fa` is carried by **two** roots against one for
   `9b1d7a504789` — the aggregate `agentii-plugin` root agrees with `quantitative-analysis`.
   **Weight-bearing additional discriminator:** of the six skills whose pins are externally
   validated, **not one lives in `models-and-pitches`.** The validated verticals are
   business-intelligence, equity-research-core, industry-analysis and the two aggregate plugins.
   `models-and-pitches` is the sole home of the dissenting hash and hosts **zero** independently
   validated pins — so the one root that disagrees is also the one root with no corroboration
   anywhere in the corpus.

**Method finding.** A duplicated skill is harmless when the copies agree and ambiguous when they
do not — and when they disagree, **majority-in-tree and thesis-membership are different tests that
here coincide.** They need not: had `models-and-pitches` carried a validated pin, the two tests
could have pointed opposite ways and the tie-break would have had to be declared rather than
found. Recorded because the `recent-quarter` case gave the opposite reading (two roots agreed, pin
uncontested) and a future artifact could face a genuine conflict.

**Decoy check — could not be executed as specified, and the substitute evidence is stronger than
expected.** The brief warns that `packaging/targets/{claude-code,codex,generic-cli,cowork}` hold
decoy copies that all fail the six hashes. **That directory does not exist** under the marketplace
root: `packaging/` contains only `README.md`, `export.py`, `export.sh`, and
`skillseekers.config.yaml`. Two substitute checks were run instead and **both pass**: the six known
hashes match **only** under `plugins/`; `2d27c7f751fa` / `9b1d7a504789` are the **only two**
`ratio-analysis` hashes in either tree; and the second tree is a **mirror that agrees** rather than
a divergent copy that would have split them. The decoy risk the brief anticipated is therefore
**not present in this environment in the form described**, and is reported as such rather than
silently dropped.

---

## 2. The component identity at VRT — it closes 5 of 5, and it is VACUOUS

The contract rule `data_integrity_register_applied` requires the component derivation in-line.
It is given here — together with the finding that **at this issuer it cannot fail.**

### 2a. The registered identity is a tautology at VRT

`gross profit − opex = operating_income`, run on all five filed periods:

| period | gross profit | − opex | = | filed operating profit | residual |
|---|---|---|---|---|---|
| Q2 2026 | 1,234.9 | 597.0 | | 637.9 | **+0.0** |
| H1 2026 | 2,234.6 | 1,156.6 | | 1,078.0 | **+0.0** |
| Q2 2025 | 896.6 | 454.2 | | 442.4 | **+0.0** |
| H1 2025 | 1,583.1 | 850.0 | | 733.1 | **+0.0** |
| Q1 2026 | 999.7 | 559.6 | | 440.1 | **+0.0** |

**5/5, zero residual — and the check has no power.** The reason is that **neither term is a
filed cell at VRT.** `us-gaap:GrossProfit` returns **0 facts for VRT** (it returns 5,551 facts
across 87 tickers platform-wide, latest 2026-03-31 — so the tag is live and VRT simply does not
file it), and `us-gaap:OperatingExpenses` returns **0 facts for VRT**. The statement of earnings
has **no gross-profit line at all**: its structure runs Net sales → Costs and expenses →
Operating expenses → Operating profit ([sec136 p.5](https://agentii.ai/v/VRT/sec136/5)). Both
terms of the identity are therefore *derived* — `GP = revenue − COGS` and `opex = GP − OP` — and
the identity reduces algebraically to `(rev − COGS) − ((rev − COGS) − OP) = OP`. **It is true
whatever the data says.** This artefact records it as **`VACUOUS`**, not `CLEAN`. A test that
cannot fail is not a passing test.

### 2b. The non-vacuous replacement: a seven-term FILED identity

Every term below is a filed cell on the face of the statement of earnings
([sec136 p.5](https://agentii.ai/v/VRT/sec136/5), [sec134 p.5](https://agentii.ai/v/VRT/sec134/5)):

```
Net sales − Cost of sales − SG&A − Amortization − Restructuring − FX − Other operating = Operating profit
```

| period | arithmetic | = | filed OP | residual |
|---|---|---|---|---|
| Q2 2026 | 3,274.3 − 2,039.4 − 494.4 − 73.7 − (−3.9) − 3.9 − 28.9 | 637.9 | 637.9 | **0.0** |
| H1 2026 | 5,923.8 − 3,689.2 − 951.1 − 151.3 − (−8.8) − 2.3 − 60.7 | 1,078.0 | 1,078.0 | **0.0** |
| Q2 2025 | 2,638.1 − 1,741.5 − 395.6 − 46.9 − 1.9 − 2.3 − 7.5 | 442.4 | 442.4 | **0.0** |
| H1 2025 | 4,674.1 − 3,091.0 − 741.9 − 92.9 − 3.0 − 4.9 − 7.3 | 733.1 | 733.1 | **0.0** |
| Q1 2026 | 2,649.5 − 1,649.8 − 456.7 − 77.6 − (−4.9) − (−1.6) − 31.8 | 440.1 | 440.1 | **0.0** |

**5/5 EXACT, and this one can fail**: the seven terms are seven independent filed cells; a
sign strip on any one of them would break the closure. **This is the identity used for the rest
of the artifact.** It is also the reason the DA-23 disposition at VRT is not `CLEAN`: the
registered identity is vacuous here, and the seven-term identity that replaces it is a
*substitute*, which must be declared.

**DA-23 directionality scoping (A17).** The seven-term identity is only informative on
**bidirectional** concepts. At VRT, `Restructuring` and `FX` are bidirectional — Q2 2026 files
restructuring at `(3.9)` and FX at `3.9`, and both are served with signs intact. Since the
identity closes, **no sign strip exists inside VRT's operating stack.** That is a scoped positive
result, not a general clearance.

---

## 3. The ratio-by-ratio cross-check — the served row versus the filed cells

The platform serves 22 fields on the `fiscal_year: 2026, fiscal_period: Q2` row
(`get_financial_ratios`, `computed_at: 2026-08-21T15:47:40.346Z`). Every one is checked below
against filed cells from [sec136 p.5](https://agentii.ai/v/VRT/sec136/5),
[sec136 p.7](https://agentii.ai/v/VRT/sec136/7), and [sec136 p.8](https://agentii.ai/v/VRT/sec136/8).
Column "basis that reproduces it" is what the served number actually equals — not what it should.

### 3a. The four EXACT reproductions

| served ratio | served | basis that reproduces it | exact? |
|---|---|---|---|
| `current_ratio` | 1.3786 | CA 9,984.9 / CL 7,243.0 = **1.3786** | **EXACT** |
| `cash_ratio` | 0.3880 | cash 2,810.6 / CL 7,243.0 = **0.3880** | **EXACT** |
| `inventory_turnover` | 1.4624 | **H1** COGS 3,689.2 / inventories 2,522.7 = **1.4624** | **EXACT (YTD flow)** |
| `operating_cf_ratio` | 0.2577 | **H1** OCF 1,866.6 / CL 7,243.0 = **0.2577** | **EXACT (YTD flow)** |
| `roa` | 0.0558 | **H1** NI 887.9 / **end** assets 15,900.9 = **0.0558** | **EXACT (YTD flow)** |
| `roe` | 0.1866 | **H1** NI 887.9 / **end** equity 4,757.6 = **0.1866** | **EXACT (YTD flow)** |
| `debt_to_equity` | 2.3422 | **total liabilities** 11,143.3 / equity 4,757.6 = **2.3422** | **EXACT (wrong numerator)** |

That is **seven** exact reproductions, and only the first two are the ratio the skill's
`references/methodology.md` defines. The other five reproduce exactly — and each is the wrong
ratio. They are separated out below, because an exact reproduction of an unnamed basis is a
*defect identification*, not a pass.

### 3b. Three named defects found by exact reproduction

**DEFECT 1 — `debt_to_equity` is a LIABILITIES-to-equity ratio.** The served 2.3422 equals
total liabilities / equity exactly at Q2 2026 (11,143.3 / 4,757.6 = 2.34221). The skill's
formula is `Total Debt / Total Equity`; on that formula the answer is **0.6179** (long-term
debt 2,939.8 / 4,757.6) or 0.6223 including the current portion. **The served value is 3.79×
the correct one**, and its numerator includes accounts payable 2,473.1, deferred revenue
3,633.7, accrued expenses 1,061.4 and income taxes 74.8 — **$7,243.0M of current liabilities,
none of which is debt.** Confirmed on two further periods, both requiring zero assumptions:
Q1 2026 served **2.1568** vs 9,155.2 / 4,244.9 = **2.1567**
([sec134 p.7](https://agentii.ai/v/VRT/sec134/7)); Q4 2025 served **2.0986** vs
8,271.1 / 3,941.3 = **2.0986**. **Three of three testable periods confirm the
identification.** The 2024 periods are a separate matter and are recorded under §5.

**DEFECT 2 — the four "YTD-flow" ratios: a period basis with no basis field.** `roa`, `roe`,
`inventory_turnover` and `operating_cf_ratio` all reproduce **exactly** when the numerator is
the **six-month** flow while the row is labelled `fiscal_period: Q2`, and all four are wrong by
roughly 2× on the quarterly flow:

| ratio | served | six-month flow (matches) | quarterly flow (mismatches) | error if read quarterly |
|---|---|---|---|---|
| `inventory_turnover` | 1.4624 | 3,689.2 / 2,522.7 = **1.4624** | 2,039.4 / 2,522.7 = 0.8084 | **1.81×** |
| `operating_cf_ratio` | 0.2577 | 1,866.6 / 7,243.0 = **0.2577** | 1,099.8 / 7,243.0 = 0.1518 | **1.70×** |
| `roa` | 0.0558 | 887.9 / 15,900.9 = **0.0558** | 497.8 / 15,900.9 = 0.0313 | **1.78×** |
| `roe` | 0.1866 | 887.9 / 4,757.6 = **0.1866** | 497.8 / 4,757.6 = 0.1046 | **1.78×** |

Two things follow, and the second is the more serious. (i) These four are **not normalised
over an average balance** — the skill's own `methodology.md` specifies *average* equity and
*average* assets, and both are used at their **end-of-period** values here, which on a rapidly
growing balance sheet is not a rounding matter (average assets 14,650.5 vs end 15,900.9, an 8.5%
difference). (ii) **The row mixes bases**: `current_ratio`, `quick_ratio` and `cash_ratio` are
point-in-time and dimensionally unaffected, but within the same served row some flow ratios are
six-month and others are not — `net_margin`, `operating_margin` and `roic` reproduce on
**neither** basis (§4). **A consumer reading one row cannot tell which basis any given field
sits on, because no field carries a basis label.** That is DA-30's exact shape, one layer up
from where the register found it at BWXT: not two bases on one *concept*, but **two period bases
on one row, collapsed with no basis field.**

**DEFECT 3 — `quick_ratio` is `cash_ratio`, and the receivables term is identically zero.**
The two are **byte-identical in 8 of 8 non-null periods** (both `null` at Q4 2024). At Q2 2026
both serve `0.3880`; the correct quick ratio is `(2,810.6 + 3,750.3) / 7,243.0 = **0.9058**`, a
**2.33× understatement**. The receivables term is zero in the numerator, and it is zero
everywhere: **`receivables_turnover: null` and `dso: null` in all 10 periods**, and
`quick_ratio ≡ cash_ratio` in all 8. **Three symptoms, one cause** — the accounts-receivable
input to the ratio engine is absent at VRT, even though the filed balance sheet states AR of
3,750.3 ([sec136 p.7](https://agentii.ai/v/VRT/sec136/7)) and `us-gaap:AccountsReceivableNetCurrent`
returns facts. This is a **silent component-drop**: the platform does not return `null`, it
returns a *different, plausible ratio* — the exact failure mode that makes the artefact's
citation discipline load-bearing.

### 3c. `dio` is not an independent metric

`dio` served `250` against a correct YTD value of `2,522.7 / 3,689.2 × 365 = 249.59`. It is
**`365 / inventory_turnover`, rounded**. The identity `IT × DIO = 365` holds in 6 of 10 periods
to within one unit (365.25, 364.97, 364.80, 365.28, 365.12, 365.60); the four "off" cases are
rounding on a 1-decimal inventory input (365.92, 367.48, 364.04, 366.77). **`dio` carries no
information beyond `inventory_turnover`** — it is a transformation of the same two cells, so
reporting both as independent findings double-counts one measurement.

### 3d. `gross_margin` — `null` in 10 of 10 periods, by gap and not by absence

`gross_margin` is `null` on every row. **The issuer publishes it.** The MD&A results-of-operations
table prints it as a line item —
`| Gross profit | 1,234.9 | 896.6 | 338.3 | 37.7 |`
— and the prose states *"Gross profit was $1,234.9 in the second quarter of 2026, or 37.7% of
sales, compared to $896.6, or 34.0% of sales"* ([sec136 p.28](https://agentii.ai/v/VRT/sec136/28)).
Both percentages check out exactly: 1,234.9 / 3,274.3 = **37.7149%**, 896.6 / 2,638.1 = **33.9866%**.
The ratio is also reconstructible from the statement's own cells: (3,274.3 − 2,039.4) / 3,274.3
= **0.3771**.

**Verdict: fallback-contract breach, not source absence.** The skill's own Error Handling table
mandates, for `XBRL returns empty for key concepts`, to *"widen date range and retry once"*, and
its `references/tool-fallbacks.md` mandates, for `Concept not found`, to *"try alternative
concept names via `list_xbrl_concepts`"* with the fallback notice *"XBRL concept unavailable;
used alternative"*. Neither was done or reported: `gross_margin` is `null` with no coverage
annotation. The platform's `validate_calculation` ALSO returns zero rows on this issuer's
`OperatingIncomeLoss` (7 arcs, 3 accessions, 35 stored facts, **zero rows**) — a second,
independent instrument gap. Both are recorded as **`UNVALIDATED-BY-PLATFORM`**.

### 3e. The full census of the served row, with a disposition on each field

| # | served field | served value | cross-check result | disposition |
|---|---|---|---|---|
| 1 | `current_ratio` | 1.3786 | EXACT on CA/CL | **CLEAN** |
| 2 | `cash_ratio` | 0.3880 | EXACT on cash/CL | **CLEAN** |
| 3 | `quick_ratio` | 0.3880 | equals `cash_ratio`; correct 0.9058 | **DEFECT — component dropped (AR)** |
| 4 | `debt_to_equity` | 2.3422 | EXACT on TOTAL LIABILITIES/equity | **DEFECT — wrong numerator (DA-30 basis)** |
| 5 | `inventory_turnover` | 1.4624 | EXACT, six-month COGS over end inventory | **DEFECT — unnamed period basis** |
| 6 | `operating_cf_ratio` | 0.2577 | EXACT, six-month OCF over end CL | **DEFECT — unnamed period basis** |
| 7 | `roa` | 0.0558 | EXACT, six-month NI over END assets (not average) | **DEFECT — unnamed period basis + no averaging** |
| 8 | `roe` | 0.1866 | EXACT, six-month NI over END equity (not average) | **DEFECT — unnamed period basis + no averaging** |
| 9 | `dio` | 250 | = 365 / `inventory_turnover`, rounded | **NOT INDEPENDENT — duplicate of #5** |
| 10 | `gross_margin` | `null` | issuer publishes 37.7%; reconstructible as 0.3771 | **PLATFORM GAP — fallback-contract breach** |
| 11 | `operating_margin` | 0.2102 | no filed basis, quarterly **or** six-month | **UNRESOLVED** |
| 12 | `net_margin` | 0.1331 | no filed basis, quarterly **or** six-month | **UNRESOLVED** |
| 13 | `roic` | 0.1822 | nearest reconstruction 0.1765 (3.2% off) — not a match | **UNRESOLVED** |
| 14 | `asset_turnover` | 0.4196 | nearest reconstruction 0.4214 (0.4% off) — not a match | **UNRESOLVED** |
| 15 | `interest_coverage` | 30.0923 | implied denominator 21.198; face states only NET interest 17.4 | **UNRESOLVED — basis not on the face** |
| 16 | `debt_to_ebitda` | 2.0964 | implied EBITDA 1,402.4 vs filed H1 EBITDA 1,301.5 | **UNRESOLVED** |
| 17 | `receivables_turnover` | `null` | AR is filed and non-zero | **DEFECT — same dropped component as #3** |
| 18 | `dso` | `null` | AR is filed and non-zero | **DEFECT — same dropped component as #3** |
| 19 | `revenue_cagr_3yr` | 0.2703 | — | see §3f |
| 20 | `revenue_cagr_5yr` | 0.2711 | differs from 3yr by 0.0008 | see §3f |
| 21 | `eps_cagr_3yr` | **2.5622** | a 256% three-year EPS CAGR | see §3f |
| 22 | `eps_cagr_5yr` | 0.6855 | — | see §3f |

**Tally: 2 CLEAN, 6 reproductions that identify a named defect, 3 duplicate/symptomatic fields
(#3's two correlates), 1 platform gap, 6 UNRESOLVED.** Of 16 ratio fields a consumer would read
as quantitative facts, **2 are the ratio they claim to be.**

### 3f. Growth ratios: the 5-year label is a 3-year computation in 7 of 10 periods

`revenue_cagr_5yr == revenue_cagr_3yr` **and** `eps_cagr_5yr == eps_cagr_3yr` in **7 of the 10
periods** — every 2024 row, plus Q1 2025, Q2 2025 and Q3 2025. They separate only at Q4 2025,
Q1 2026 and Q2 2026 (0.2703 vs 0.2711; 0.3416 vs 0.2636; 0.2711 — Q2 is the first row where the
two genuinely differ). **14 of 20 served growth figures carry a five-year label on a
three-year computation.** A duplicate under two names is the same independence failure as `dio`.

`eps_cagr_3yr = 2.5622` at Q2 2026 is a **256% three-year EPS CAGR**. VRT's diluted EPS ran
$0.83 (Q2 2025) → $1.27 (Q2 2026); a 256% CAGR over three years from the served base is not
reconcilable with the filed EPS series, and **no filed EPS cell is cited to it.** Recorded as a
magnitude anomaly with no located basis — the register's `UNRESOLVED` class, flagged because a
growth rate that large propagates directly into any PEG or reverse-DCF use.

---

## 4. The residual triage — every unresolved residue, with the search that was run

**A brute-force search was run and is reported as a NEGATIVE result**, because it constrains
what can be claimed. For each unresolved ratio at Q2 2026, an exhaustive search was made over
all ordered pairs (and ×0.8, ×365 variants) of 36 filed cells. It found matches — and **the
matches are not findings**: with ~2,500 candidate expressions at 0.5% tolerance, `roic` produced
7 coincidental hits, `asset_turnover` 9, `roe` 6. **That is the DA-29 lesson arriving in a new
place: a search that produces a closing answer is not thereby a derivation.** The only
identifications accepted in §3 are those that are (a) **exact**, (b) **stable across periods**,
and (c) **consistent with a formula the skill actually specifies or a basis the issuer actually
files**. Everything else is `UNRESOLVED`, not "probably fine".

**`operating_margin` (0.2102).** Implied numerator 688.3 against a filed OP of 637.9 — **+7.9%**.
Tested and FAILED: quarterly OP/rev = 0.1948; six-month OP/rev = 0.1820; segment OP 791.2/rev =
0.2416; segment OP less amortization /rev = 0.2191; gross sales denominator (3,724.3) = 0.1713;
EBITA = 0.2173. Across all 10 periods, the served value matches a filed basis in **1 of 10** —
Q4 2024, where 0.1707 = FY2024 OP 1,367.4 / FY2024 revenue 8,011.8 = 0.17067 **EXACT**, i.e. the
**annual** figure on a quarterly row (DA-26's signature). Q4 2025 does **not** follow: served
0.2088 against FY2025 OP/revenue = 1,829.7 / 10,229.9 = **0.17886** (implied numerator 2,136.0
matches no fiscal-year aggregate). **DA-26 is therefore confirmed at the ratio layer in one Q4
and absent in the next**, and the 10-period census cannot claim it universally.

**`net_margin` (0.1331).** Implied NI 435.8 against a filed 497.8. The **only** filed-item
reconstruction that closes exactly is `NI − 62.0`, where 62.0 is the **six-month** change in
fair value of contingent consideration ([sec136 p.8](https://agentii.ai/v/VRT/sec136/8)):
497.8 − 62.0 = 435.8, and 435.8 / 3,274.3 = **0.13310**. **It is rejected as a derivation**, on
two independent grounds: (i) it applies a *six-month* adjustment to a *quarterly* NI, mixing
period bases to manufacture a closure — the DA-29 shape exactly; (ii) it **fails at Q1 2026**,
where the same construction gives 390.1 − 33.2 = 356.9, i.e. 0.1347 against a served **0.0558**.
**A closure that reproduces at one period and fails at the next is a coincidence, not a
mechanism.** The implied numerators match none of the ten filed quarterly net incomes
(5.9, 178.1, 176.6, 135.2, 164.5, 324.2, 398.5, 445.6, 390.1, 497.8) — **9 of 9 mismatch** on
the periods where both are computable below the two ends.

**`interest_coverage` (30.0923).** Implied denominator **21.198**. The face's only interest line
is **net** — "Interest expense (income), net 17.4" ([sec136 p.5](https://agentii.ai/v/VRT/sec136/5))
— and at Q1 2026 that line is **negative, (4.4)**, an interest *income*, while the served Q1 2026
denominator is a **positive 3.169**. So the platform's denominator is neither the net figure nor
its absolute value. The admissible reading is that the platform computes the standard
EBIT / **gross** interest expense, and **gross interest expense is not a line on the face** —
it would have to come from the debt note, which this skill's `retrieval_scope: structured_only`
bars. **Disposition: UNRESOLVED — a basis the face does not expose.** Recorded as DA-30-family
(interest expense reported on a gross and a net basis, collapsed with no basis field) and
declared **`UNRESOLVABLE-FROM-PLATFORM`** rather than guessed.

**`roic` (0.1822), `asset_turnover` (0.4196), `debt_to_ebitda` (2.0964).** Each has a nearest
reconstruction that is close but not exact — roic 0.1765 (3.2% off, six-month OP × (1−20%) over
debt + equity − cash), asset_turnover 0.4214 (0.4% off, six-month revenue over average assets),
debt_to_ebitda implied EBITDA 1,402.4 against filed H1 EBITDA 1,301.5 (7.8% off). **A near miss
is not a match and is not reported as one.** All three are `UNRESOLVED`. The asset_turnover case
is the instructive one: 0.4% is far beyond the rounding of the filed cells (0.1% on a $5.9bn
flow is $5.9M, against a 0.4% gap of $24M), so the platform is using values this dataset does
not expose.

---

## 5. The line-level basis detector on ratios — and the negative control

The predecessor artefact proposed a DA-30 detector: **compare LINE-LEVEL, not total-to-total;
trigger on any line-level difference exceeding rounding with no footnote reconciling the two
bases.** This artifact applies it to *ratios*, which is the test the proposal did not itself run.

### 5a. Negative control (must NOT fire) — PASSES

The §1 segment/consolidated cost-of-sales difference. Note 11 reports **segment cost of sales
2,024.4** against the statement's **2,039.4**, a **$15.0M** difference
([sec136 p.21](https://agentii.ai/v/VRT/sec136/21)) — and the note **footnotes it**: `Cost of
sales(1)` with *"(1) Cost of sales exclusive of engineering, research and development costs."*
Segment cost of sales 2,024.4 + Engineering/R&D 139.9 + Marketing 191.2 + IT 57.8 + Other 69.8 =
**2,483.1**, against segment net sales 3,274.3 → segment operating profit **791.2**, which then
reconciles to consolidated 637.9 by the two footnoted exclusions:

```
791.2 − 79.6 (corporate and other) − 73.7 (amortization of intangibles) = 637.9   EXACT
```

and the segments' own internal identity closes exactly at every level — Americas
2,070.8 − 1,499.4 = 571.4; Asia Pacific 719.9 − 624.3 = 95.6; EMEA 483.6 − 359.4 = 124.2; sum
**791.2** — each matching the filed operating-profit cell to the decimal.

**Detector behaviour:** gross margin on the statement basis is **37.715%**; on the segment basis
it is (3,274.3 − 2,024.4) / 3,274.3 = **38.173%** — a spread of **+45.8 bps**, which is ~90× the
±0.5 bp rounding tolerance of the filed cells and therefore **exceeds rounding**. The detector
**does not fire**, because the difference is footnoted and reconciles.
**NEGATIVE CONTROL: PASS.**

### 5b. Positive case (must fire) — FIRES

Note 4's disaggregation against the statement's own revenue lines. On the identical total of
**3,274.3**, Note 4 reports **Products 2,606.4 / Services & spares 667.9**
([sec136 p.13](https://agentii.ai/v/VRT/sec136/13)), while the statement of earnings reports
**Net sales - products 2,646.7 / Net sales - services 627.6**
([sec136 p.5](https://agentii.ai/v/VRT/sec136/5)). The differences are **+40.3 and −40.3** —
**exactly compensating, so every total ties**, and there is **no footnote reconciling the two
bases.** The product mix ratio is **80.833%** on the statement basis and **79.602%** on the Note 4
basis — a spread of **−123.1 bps**, against ±0.5 bp of rounding tolerance.
**POSITIVE CASE: FIRES.** The detector catches a *ratio* (a mix ratio), not merely a total, which
is what the task required it to do.

**Why this is the decisive shape, and not merely a curiosity.** VRT's own MD&A resolves the
question of which basis is real. Its commentary states *"Product sales increased $487.5 ... 
Services & Spares sales increased $148.7"* ([sec136 p.28](https://agentii.ai/v/VRT/sec136/28)).
Those two numbers match **Note 4** (2,606.4 − 2,118.9 = **487.5**; 667.9 − 519.2 = **148.7**) and
**not** the statement of earnings (2,646.7 − 2,166.0 = 480.7; 627.6 − 472.1 = 155.5). **The
issuer's own growth narrative is computed off the Note 4 basis while its gross-profit line on the
same page is computed off the statement basis** — two bases, one page, no basis field. This
upgrades the predecessor's finding from an internal inconsistency to a *documented* one, and it
establishes the direction: the Note 4 disaggregation is the basis the issuer's management actually
reasons on.

**Consequence for the ratio layer.** Every revenue-derived ratio is affected, and the affected
set is not small: product mix moves 123 bps, service mix the same in the opposite direction, and
any segment-mix or product-margin ratio inherits the $40.3M. **`no_single_basis_collapse` cannot
be discharged at VRT by quoting one basis, because the platform serves one undimensioned revenue
figure and the filing files two.**

---

## 6. The six-DA census — each verdict, and each not-testable KIND named

Verdicts use the register's four dispositions distinctly. **`CLEAN` is used only where a test
ran and COULD have failed**; `UNEXERCISED` where the test could run but the data cannot exercise
it; `UNEVIDENT` where the source lacks the object entirely.

| DA | verdict at VRT | evidence |
|---|---|---|
| **DA-23** sign stripping | **PARTIAL — present on the cash flow, absent inside the operating stack** | The seven-term identity closes 5/5 EXACT, so no strip exists among the seven operating terms. But `NetCashProvidedByUsedInFinancingActivities` is served **+11.9** at Q1 2026 where the filing prints **11.9** (correct), and **−3.0** at H1 2026 where the filing prints **(3.0)** — same tag, same issuer, six months apart ([sec134 p.8](https://agentii.ai/v/VRT/sec134/8), [sec136 p.8](https://agentii.ai/v/VRT/sec136/8)). The discriminator is the **sign of the value**, not the concept and not the statement. |
| **DA-24** non-operating contamination | **CLEAN — and this reverses the direction the register assumed** | Every term inside the operating stack is an operating term: SG&A, amortization of intangibles, restructuring, FX, other operating. The only acquisition item is **contingent consideration**, filed on the **cash-flow** statement as a non-cash add-back of **62.0** (H1 2026) and **33.2** (Q1 2026) — *below* the operating line, contaminating nothing. **Confirmed independently at VRT by two routes**: the seven-term identity closes with no residual, and there is no above-the-line acquisition item to admit. |
| **DA-25** normalised per-unit metrics | **CONFIRMED — new instance at the ratio layer** | `roa` and `roe` use **end-of-period** balances where the skill's own formula specifies **average** (0.0558 vs 0.0354 on the average; 0.1866 vs 0.1145). `dio` is a rounded transform of `inventory_turnover`. `debt_to_ebitda`'s implied EBITDA (1,402.4) matches no filed EBITDA. **Three served ratios are normalised quantities no filed cell states.** |
| **DA-26** annual mislabelled as quarterly | **CONFIRMED at the metrics layer (twice), PARTIAL at the ratio layer** | Metrics rows `Q4 2025` revenues **10,229,900,000** and `Q4 2024` revenues **8,011,800,000** are both **annual** figures. At the ratio layer, Q4 2024 `operating_margin` 0.1707 = FY2024 1,367.4 / 8,011.8 = **0.17067 EXACT**; Q4 2025 does **not** follow (0.2088 vs FY2025 0.17886). Reported as partial: **the signature reproduces in one Q4 and not the next.** |
| **DA-27** calendar-derived fiscal labels | **NOT TESTABLE — MECHANISM-POPULATION IDENTITY (kind 4)** | VRT's fiscal year **is** the calendar year, so a label defect derived from the calendar quarter is *by construction* invisible here. Per A13 kind 4 the sample is defined by the mechanism's own property and the statistic carries **no information about the remainder** — VRT must be **removed from the denominator**, not reported clean. This is the fifth issuer so excluded (SATS, UTHR, VRT, MRCY and GOOG on the registry-field discriminator). |
| **DA-28** capital-structure discontinuity | **UNEVIDENT — kind 2, genuine absence from the source** | No listing event appears in any served period; VRT's SEC coverage in this corpus opens well after its 2020 de-SPAC. **A3's generalisation was tested too**: there is no present multi-class structure (preferred stock 5,000,000 shares authorized, **none issued**; one class of common, 700,000,000 authorized, 384,936,985 outstanding at 2026-06-30, one undimensioned EPS pair $1.29 / $1.27), and **no disclosed future share-count-changing event** — no convertibles, no forward issuance. Absence of object, not a clean result. |
| **DA-29** back-solved and opaque checks | **FIRED — and self-applied** | The predecessor's §1 identity is a back-solve: `gross profit` and `opex` are *derived*, so `GP − opex = OP` is true by construction. 13/13 closed and **it could not have failed**. Replaced by the seven-term filed identity (§2b). Additionally, the exhaustive brute force produced 7–9 coincidental "hits" per ratio — recorded as a negative result so that no near-miss is later mistaken for a derivation, and the one exact single-period closure found (`net_margin` = NI − 62.0) was **rejected** precisely for failing the stability test. |
| **DA-30** two bases, no basis field | **FIRED — three distinct instances, one of them new in kind** | (i) **Cost of sales**: segment 2,024.4 vs statement 2,039.4 (footnoted, reconciles; the negative control). (ii) **Revenue disaggregation**: Note 4 products 2,606.4 vs statement 2,646.7, Δ $40.3M each way, **unfootnoted**, with the issuer's own MD&A growth figures computed off the Note 4 basis. (iii) **NEW — period basis**: four served ratios reproduce exactly on *six-month* flows on a row labelled `fiscal_period: Q2`, while `net_margin`, `operating_margin` and `roic` reproduce on neither basis; **one served row, at least two period bases, no basis field** ([sec136 p.28](https://agentii.ai/v/VRT/sec136/28)). |

**Named not-testable KINDS at VRT.** DA-27 is kind 4 (**mechanism-population identity**). DA-28
is kind 2 (**genuine absence from the source**). The validator gap on `OperatingIncomeLoss` is
kind 3 (**validator-completeness** — concept present, fully filed, 35 stored facts, 7 arcs, 3
accessions, **zero validator rows**; recorded `UNVALIDATED-BY-PLATFORM`, never as a pass). The
`gross_margin` null is a **fifth** shape not in the A13 taxonomy: **the datum is present, filed,
published by the issuer in its own words, and reconstructible — and the platform returns null
without a fallback notice.** Proposed as **kind 7: detector gap at a computable datum** (remedy:
the instrument, not the pipeline, and not the source).

**Cross-holding (queued DA-31) — closed by absence of object.** `us-gaap:EquityMethodInvestments`
returns **0 facts** for VRT, and `us-gaap:InterestExpenseNonoperating` returns 0. The balance
sheet carries **no equity-method investment line** — read and confirmed cell-by-cell at
[sec136 p.7](https://agentii.ai/v/VRT/sec136/7): the asset side is cash, short-term investments,
AR, inventories, other current assets, PP&E, goodwill, other intangibles, deferred income taxes,
ROU assets and other. VRT is a plain industrial with long-term debt and no stake to appreciate or
dilute. **The DA-31 mechanism has no object here.** Corollary recorded because it is the sharp
part: a keyword search for `equity method` in `sec136` returns **zero** — and **a zero from
`search_keyword_in_source` is not evidence the filing lacks the term** (the outline `description`
field is `null` on these pages, so the search has no text to match). The absence here is
established by **reading the balance-sheet page**, and the method is stated so the claim can be
audited. Two independent routes were used (structured query returning 0 facts, and page read),
and both are reported.

---

## 7. Corrections — to 001, and to the predecessor artifact

**001 is frozen and is not rewritten.** These are recorded corrections for the ledger.

**Correction 1 — `gross profit 1,234.9` is not a derivative; it is a FILED cell, on p.28 not p.5.**
The predecessor's §1 records that "gross profit 1,234.9 is NOT a filed cell ... Page 5 confirms no
gross-profit line exists; 1,234.9 = 3,274.3 − 2,039.4, a derived value." **The first half is right
and the second half is only half right.** No gross-profit line exists on the *statement of
earnings* — confirmed a second time by reading [sec136 p.5](https://agentii.ai/v/VRT/sec136/5),
which runs Net sales → Costs and expenses → Operating expenses → Operating profit. **But the MD&A
table on [sec136 p.28](https://agentii.ai/v/VRT/sec136/28) prints `Gross profit | 1,234.9 | 896.6
| 338.3 | 37.7` as a line item, and the prose states it as a sentence.** So 1,234.9 **is**
citable to a filed cell — at p.28. This matters materially: it changes `gross_margin: null` from
"there is no filed basis" to "**the issuer publishes the ratio and the platform does not return
it**", which is a platform-gap finding rather than a source limitation, and it is the difference
between a scope claim and a defect claim.

**Correction 2 — the registered component identity is VACUOUS at VRT, not merely satisfied.**
Recorded in §2a. The predecessor computed 13/13 with zero residual, which is correct and is a
tautology. The seven-term filed identity replaces it.

**Correction 3 — `quick_ratio` is not a rounding artifact; the receivables input is absent.**
`quick_ratio ≡ cash_ratio` in 8 of 8 non-null periods, correlating exactly with
`receivables_turnover: null` and `dso: null` in 10 of 10. Three fields, one cause.

**Correction 4 — `debt_to_equity`'s numerator is TOTAL LIABILITIES.** Confirmed at three periods
(Q1 2026, Q2 2026, Q4 2025). 001's headline figure set should not carry a VRT leverage ratio
derived from this field.

**Correction 5 — the outline `description` field is `null` on every page read here** — sec136
p.5, p.7, p.8, p.13, p.21, p.28 and sec134 p.5, p.7, p.8 all return `"description": null`. The
predecessor verified two attributed sentences at source and found the same. **The brief required
checking this in both directions, and both directions now agree: at VRT there was nothing in the
outline description to misquote.** The `table_pages_quote_cells_not_prose` rule therefore bites
*vacuously* on this issuer — the cells quoted above are read from the page text, not from a
description. The `R1`-class risk it guards against is not what is wrong at VRT.

**Correction 6 — DA-24's direction, at the register level.** The register's DA-24 entry was
widened at Phase 3 to admit a **charge**, having been defined by a gain. VRT supplies a **second
charge-direction falsification of the gain reading and simultaneously a clean DA-24 result**: the
only acquisition item above the operating line is contingent consideration at a **62.0** charge
(H1 2026), and it sits **below** the operating line as a cash-flow add-back, so it contaminates
nothing. **The predicate is absent; the falsification is not needed.**

---

## 8. What this does to PIL-5's falsifier

PIL-5's falsifier is
`metric=share_of_001_headline_figures_converted_to_DEMONSTRATED threshold=0.5 source=validation_ledger op=<`
— **fewer than half of 001's headline figures convert to DEMONSTRATED.**

**This artifact moves no 001 headline figure toward conversion, and it pushes at least one
away.** It converts **0 of 001's headline figures**. What it does is supply a **per-issuer bound
on one candidate population**, and the bound is severe:

- **At VRT, of the 16 ratio fields a reader would treat as quantitative facts, 2 are the ratio
  they claim to be** (`current_ratio`, `cash_ratio`). **2/16 = 0.125**, against a threshold of 0.5.
- Counting only *defect-attributable* outcomes as non-conversions — the conservative reading that
  gives the platform the benefit of every doubt, treating all 6 UNRESOLVED as neutral — the
  conversion share is **2/10 = 0.20**, still below the threshold.
- The most generous reading available, crediting the platform for every field that is *correct or
  merely absent* and counting only the 6 positively-identified defects as failures, gives
  **2/10 = 0.20**.

**Every admissible reading at this issuer is below 0.5, and none of them is close.**

**But the denominator is UNSTATED, and the artifact cannot close that (Clarification Q-5 still
open).** Two pieces of evidence bear on it, both negative:

1. **The numerator is undefined before the denominator is.** PIL-5 says a figure "converts to
   DEMONSTRATED". Per the CHK004 preflight, a figure that P6 classifies boundary-contaminated, or
   that P2 leaves unbounded, becomes `DERIVED` or stays `CLAIMED`. So the same figure can be
   counted in opposite directions by two pillars, and **the ledger must fix the counting unit
   before the threshold means anything.**
2. **The population is not the ratio layer.** 001's headline figures are the thesis-level
   numbers; a served platform ratio is not one of them unless the ledger decides that a ratio the
   platform publishes **is** a headline figure. This artifact's 2/16 is therefore **conditional**:
   true **if** ratios are in the denominator, and silent if they are not. It is reported with that
   condition attached rather than asserted as the falsifier's value.

**Direction of travel, stated plainly.** P6 succeeding can push PIL-5's share **down** — the
spec says so explicitly, and VRT is a worked instance: DA-24 resolves *clean*, which removes
nothing from the numerator, while DA-30 fires **three ways** and DA-25 fires at the ratio layer,
which moves three ratios out of any conversion count. **The two pillars are not in tension; they
are the same measurement read twice.** The artifact therefore *supports the falsifier's firing*
without being sufficient to decide it.

---

## 9. What could NOT be verified, and why

1. **The `skill_pin` decoy check could not be executed as written.**
   `packaging/targets/{claude-code,codex,generic-cli,cowork}` **does not exist** under the

> **⚠️ CORRECTION, appended 2026-09-18 — the line above is UNQUALIFIED, not false.**
> **There are TWO `agentii-investment-intelligence` trees and their `packaging/` directories differ.**
> The **working tree** (`/Users/frank/A/agenzym/…/packaging/`) **DOES contain `targets/`** — four
> subdirs, each with a real `SKILL.md`, **all four failing the six known hashes (0/6)**; the decoy
> check is runnable and is now run. The **marketplace tree**
> (`~/.claude/plugins/marketplaces/agentii-investment-intelligence/packaging/`) contains the same
> five files **and no `targets/`** — **so the statement below is an accurate description of the
> marketplace copy, which is the tree this artifact worked in.** Neither party named its tree.
> **The failure class is DA-30's (one quantity, two bases, no basis field), not a fabricated
> negative.** And note the asymmetry: the decoys exist **only in the working tree**.
> **⚠️ Second correction to this artifact's pin reasoning:** the corroboration reported as
> "15 roots across 5 plugin directories" is **inflated by a symlink farm** —
> `plugins/agentii-plugin/skills/agentii` has **70 of 70 entries as symlinks**, so it agrees with
> `vertical-plugins/quantitative-analysis` by construction rather than independently.
> **`2d27c7f751fa` still stands, on thesis membership and on `models-and-pitches` lacking a
> `SKILL.md` — but not on a majority vote.** *A root only corroborates if it is a real directory
> with a distinct inode.*
   marketplace root. Two substitute checks were run instead and both pass (15 roots / 6 distinct
   hashes, and a second mirror tree reproducing all six pins identically). **Residual uncertainty,
   stated rather than papered over:** the decoy directories may exist in an environment this
   session did not enumerate, and the six-of-six validation cannot exclude that. What it does
   establish is that the pins recorded in 001 are reproduced by exactly one compact set of
   directories here, and that the two trees available both agree.
2. **Six of the twenty-two served fields are UNRESOLVED** (`operating_margin`, `net_margin`,
   `roic`, `asset_turnover`, `interest_coverage`, `debt_to_ebitda`) — no filed-cell basis
   reproduces them at any period tested. Declared `UNRESOLVABLE-FROM-PLATFORM`, not guessed. The
   brute-force search that could have manufactured answers was run and is reported as a **negative
   result**.
3. **`interest_coverage`'s denominator requires the debt note**, which
   `retrieval_scope: structured_only` bars this skill from reading. The gross-versus-net interest
   basis is stated as a hypothesis and is **not** claimed as established.
4. **`debt_to_equity` at the 2024 periods.** The liabilities-as-numerator identification is
   confirmed at three periods but **fails at Q1 2024**, where served `56.2432` implies an equity of
   ~132.6 against a filed 1,393.4 — a **10.5×** discrepancy requiring a different explanation. The
   same row also serves `roe: 0.4564` against a filed-basis 0.0035 (**~132×**) and
   `interest_coverage: null`. **Q1 2024 is declared separately UNRESOLVED and is not used to
   support the three-period confirmation.**
5. **`eps_cagr_3yr: 2.5622`** — no filed EPS cell is cited to it and the magnitude is not
   reconcilable with the served diluted EPS series; recorded as an anomaly with no located basis.
6. **`us-gaap:LiabilitiesCurrent` returns ZERO parent facts for VRT** — only components
   (`AccruedLiabilitiesCurrent` 1,061.4 at 2026-06-30, matching the filed "Accrued expenses and
   other liabilities 1,061.4") — **yet the balance sheet prints "Total current liabilities 7,243.0
   | 4,407.0" on the face.** The subtotal exists in the filing and **no fact in the platform
   carries it.** Every ratio built on current liabilities (`current_ratio`, `quick_ratio`,
   `cash_ratio`, `operating_cf_ratio`) is therefore computed from components the platform
   reassembles, and **the reassembly matched the filed subtotal exactly in the two cases where it
   was checkable** — which is the good news, and it is only two cases.
7. **Concept-absence traps confirmed for this issuer.** `us-gaap:Revenues`, `us-gaap:CostOfRevenue`,
   `us-gaap:CostOfGoodsSold`, `us-gaap:GrossProfit`, `us-gaap:OperatingExpenses`,
   `us-gaap:EquityMethodInvestments` and `us-gaap:InterestExpenseNonoperating` all return **0
   facts** at VRT. VRT files under `RevenueFromContractWithCustomerExcludingAssessedTax`,
   `CostOfGoodsAndServicesSold`, `SellingGeneralAndAdministrativeExpense` and `OperatingIncomeLoss`.
   **A zero from a `us-gaap`-keyed query is evidence about the TAG, not about the filing** — and
   the extension-tag corollary applies: a filer extension would be missed silently, so the
   `InterestExpenseNonoperating` zero is **not** used to conclude anything about VRT's debt note.
8. **`meta.data_freshness: "2027-04-12"`** is returned on every ratios and XBRL response — a
   **future-dated** freshness stamp against an `as_of` of 2026-09-18. Recorded as an instrument
   defect (queued A11). It is stated here because it affects the reproducibility claim: the
   responses are as-of a date that has not occurred.
9. **The metrics-block `Assets` / `StockholdersEquity` pair.** `Assets` 12,212,400,000 at
   2025-12-31 and `StockholdersEquity` 2,434,300,000 at 2024-12-31 are **both the correct filed
   values for their own dates** ([sec136 p.7](https://agentii.ai/v/VRT/sec136/7) confirms 12,212.4
   at 2025-12-31). The defect is not a wrong value: the block **mixes two balance-sheet dates
   without a label.** A milder and more precise finding than "misdated", and it is recorded that
   way deliberately.

**One instrument note carried forward.** `validate_calculation` returns **zero rows** on VRT's
`OperatingIncomeLoss` while **35 facts are stored** — so the platform's own validator is
`UNVALIDATED-BY-PLATFORM` on the exact concept this artifact's identity is built from. **Every
closure in §2b is my arithmetic on filed cells, not a platform validation, and is reported as
such.** The validator's `reported` column shares the stripped store (A14), so a pass would not
have been admissible evidence about sign in any case.

---

## Sources

| Figure | Source |
|---|---|
| Statement of earnings, Q2/H1 2026 and Q2/H1 2025 — seven filed operating terms, no gross-profit line | [VRT 10-Q sec136 p.5](https://agentii.ai/v/VRT/sec136/5) |
| Balance sheet 2026-06-30 / 2025-12-31 — cash, AR, inventories, CA, CL, debt, equity, total liabilities | [VRT 10-Q sec136 p.7](https://agentii.ai/v/VRT/sec136/7) |
| Cash flow H1 2026 / H1 2025 — OCF 1,866.6, contingent consideration 62.0, capex (285.9), financing (3.0) | [VRT 10-Q sec136 p.8](https://agentii.ai/v/VRT/sec136/8) |
| Note 4 disaggregation — products 2,606.4 / services 667.9 vs statement 2,646.7 / 627.6 | [VRT 10-Q sec136 p.13](https://agentii.ai/v/VRT/sec136/13) |
| Note 11 segments — cost of sales(1) 2,024.4 footnoted, operating profit 791.2 reconciling to 637.9 | [VRT 10-Q sec136 p.21](https://agentii.ai/v/VRT/sec136/21) |
| MD&A results of operations — gross profit 1,234.9 / 896.6 / 37.7%, and the $487.5 / $148.7 growth figures | [VRT 10-Q sec136 p.28](https://agentii.ai/v/VRT/sec136/28) |
| Q1 2026 statement of earnings cells | [VRT 10-Q sec134 p.5](https://agentii.ai/v/VRT/sec134/5) |
| Q1 2026 balance sheet — total liabilities 9,155.2, equity 4,244.9 | [VRT 10-Q sec134 p.7](https://agentii.ai/v/VRT/sec134/7) |
| Q1 2026 cash flow — financing +11.9 (filed positive), contingent consideration 33.2 | [VRT 10-Q sec134 p.8](https://agentii.ai/v/VRT/sec134/8) |

**Method note.** All nine pages were located by `read_source_pages`; the `citation_id` and page
numbers come from that tool's responses, not from inference. Every cell quoted above is the
**cell text as the page serves it** — read from the page, not from an outline `description`, which
is `null` on all nine. Two attributed sentences were re-verified at source in both directions:
the MD&A gross-profit sentence and its table row reproduce exactly
([sec136 p.28](https://agentii.ai/v/VRT/sec136/28)).
