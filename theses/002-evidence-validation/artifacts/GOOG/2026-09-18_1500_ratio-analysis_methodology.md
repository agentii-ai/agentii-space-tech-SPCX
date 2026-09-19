---
thesis_id: "002-evidence-validation"
pillar: PIL-5
ticker: GOOG
skill: ratio-analysis
mode: methodology
generated_at: 2026-09-18T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "2d27c7f751fa"  # Q57 resolved 2026-09-18 by RE-DERIVATION in this artifact: six-of-six tabled pins reproduced 18/18 (each of the six, in all THREE live locations — working tree, marketplace tree, global skills dir — see §1), which validates the hash base; then `ratio-analysis` computed from plugins/vertical-plugins/quantitative-analysis/skills/agentii/ratio-analysis = 2d27c7f751fa. The competing root plugins/vertical-plugins/models-and-pitches/skills/agentii/ratio-analysis hashes to 9b1d7a504789 but contains NO SKILL.md — it cannot be a hash base for a skill pin. Four packaging/targets decoys re-tested and FALSIFIED 32/32.
as_of: 2026-09-18
corpus_version: "UNPINNED"
upstream_stale: "001@1.2.0"
definitions_used:
  - da_id: "DA-23"
    chosen_reading: "sign strip on a negative income fact — EXERCISED at GOOG and CONFIRMED in the instrument's `reported` column, CLEAN on the served ratio layer. The test has power here (unlike VRT) because GOOG files negative operating income on four segment lines in every period read: Other Bets (4,444) FY2024 / (7,515) FY2025 / (2,100) Q1 2026 / (1,799) Q2 2026, and Alphabet-level activities (10,541) / (16,760) / (5,391) / (5,789) / (11,180). The instrument emitted a negative `computed` on the same concept (us-gaap:OperatingIncomeLoss, Q2 2025: computed -10,660,000,000 vs reported 2,826,000,000) — a same-concept opposite-sign pair, where the served `reported` value is the Google Cloud SEGMENT member. No served ratio numerator in the 10-row table is a sign-stripped value: every operating_margin numerator reproduced is positive on both sides. §7.1"
  - da_id: "DA-24"
    chosen_reading: "non-operating contamination of a ratio — CONFIRMED on every net-income-bearing ratio and REFUTED on the operating-line ratios. GAIN mode, not CHARGE: gain on equity securities, net 99,031 for Q2 2026 and 135,946 for 6M 2026, sits BELOW the operating line, so operating_income, operating_margin and roic are uncontaminated while net_margin, roe, roa and every EPS-based metric are contaminated. Magnitude: the mark is 77.79% of the 6M 2026 net income that the ratios divide by; ex-mark net_margin is 16.77% against a served 76.09% — a 59.32 pp swing on one ratio. §5"
  - da_id: "DA-25"
    chosen_reading: "normalised per-unit metric — NOT TESTABLE at the ratio layer in this artifact's citation base. The platform serves no per-unit normalised ratio for GOOG (no revenue-per-employee, no per-unit economics); the servable population is the 14 core per-row fields of §3 and none is normalised. Recorded as a not-testable KIND (kind 7), not as clean. The skill's own formula table contains no per-unit ratio, so the ratio layer cannot expose this defect. §7"
  - da_id: "DA-26"
    chosen_reading: "annual value mislabelled quarterly — CONFIRMED, row-wide, and it reaches the ratio layer. The platform's `2025 Q4` row is the FY2025 ANNUAL period on every duration measure tested: net_margin 0.3281 = 132,170/402,836, roe 0.3183 = 132,170/415,265, roa 0.2220 = 132,170/595,281, asset_turnover 0.6767 = 402,836/595,281, op_cf_ratio 1.6031 = 164,713/102,745 — five exact annual reproductions in one row labelled quarterly. This is the second site (SPCX was the first) and the first where the mislabelled row is proved by reproduction rather than by subtraction. §3.2"
  - da_id: "DA-27"
    chosen_reading: "calendar-quarter fiscal labels — NOT TESTABLE at the ratio layer in this artifact, by construction: every period this artifact adjudicates is a Dec-31 filer's own calendar quarter or year, read directly off the filing, and the ratio table's row labels agree with the filings for the four rows this artifact anchors (2026 Q2, 2026 Q1, 2025 Q4, and the FY2024 rows). The DA-27 defect established in the sibling recent-quarter artifact is a LABEL defect at the platform's fiscal-calendar layer and it does not change any served ratio VALUE, so it cannot be caught or cleared by a component-identity cross-check. Not-testable KIND, not clean. §7"
  - da_id: "DA-28"
    chosen_reading: "capital-structure discontinuity — CONFIRMED as a LIVE discontinuity inside the ratio window and NOT as an IPO event (Alphabet's IPO is 22 years outside it). The June 2026 issuance of 6.25% mandatory convertible preferred stock for the first time makes net income (112,193) differ from net income available to common stockholders (112,107) and makes diluted EPS class-dependent, and it is the same event that produces the platform's undimensioned single EPS reading. This is the bridge from DA-28 to the live DA-30 instance (§6). Not an IPO: recorded as a live class-basis collapse instead. §6"
  - da_id: "DA-29"
    chosen_reading: "back-solved or opaque check — CONFIRMED at GOOG on the FY2024 Q4 row, where TWO denominators appear nowhere in any cited filing: total assets of about 8,700 against a filed 450,256 (a 51.75x collapse on roa 11.5078 and asset_turnover 40.2320) and an implied equity of about 195,581 against a filed 325,084 on roe 0.5119. The corresponding reconciliation terms are not located in the source: the test is a back-solve and is reported as UNRESOLVED rather than verified. Also confirmed in the ratio layer's cheapest form — quick_ratio is served 10/10 as cash/CL, so its numerator's accounts-receivable term appears NOWHERE in the check while being filed and available (69,175). §4, §3.4"
  - da_id: "DA-30"
    chosen_reading: "two bases on one concept collapsed without a basis field — CONFIRMED and LIVE, in three independent instances on one concept set. (a) Diluted EPS is class-dependent in the filing (Class A 9.12 / Class B 9.12 / Class C 9.11 / consolidated 9.11) and the platform serves one undimensioned 9.11 with no basis field; the four numerators are filed (60,893 / 7,612 / 51,300 / 112,193) and each quotient reproduces exactly. (b) operating_margin carries at least FOUR distinct bases across ten rows (consolidated 3M, consolidated 6M, Google Services segment member over consolidated revenue on two rows) with no basis field. (c) The same concept carries two denominators (3M flows in the 2026 Q1 row, 6M flows in the 2026 Q2 row) with no period-basis field. §6, §4"
evidence_grade: DEMONSTRATED
deal_security_basis: not_applicable
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PLATFORM
platform_residual: "UNRESOLVABLE-FROM-PLATFORM — four served quantities cannot be reproduced from any term filed in any source cited here, and each is a property of the calculation engine rather than of a filing: (1) roic on all rows tested (implied denominator on the 2026 Q1 row lies in the interval (546,400, 547,153] against a filed 478,746, and the FY2024 Q4 Q1-row assumption that produced my first hypothesis 726,793 was falsified against the filed 703,919); (2) interest_coverage on the single row where it is served (296.7766, implying an interest-expense term of about 85.83 that matches no filed cell) while interest expense is filed in every period read; (3) debt_to_ebitda on the two rows tested (2026 Q2 served 1.2562 is neither long-term-debt/2x-6M-OI = 0.6100 nor total-liabilities/2x-6M-OI = 3.4984 nor total-debt/OI = 3.4984; 2025 Q4 served 0.3521 is neither 46,547/129,039 = 0.3607 nor 180,016/129,039 = 1.3951); (4) the two FY2024 Q4 denominators of the DA-29 instance. The residue is the engine's member-and-basis selection rule; it is not derivable from any public source and is recorded, not diagnosed. No item in this artifact is classified UNRESOLVABLE-FROM-PUBLIC-SOURCES: every one of the four is a platform construction, and the public record (the filings) is sufficient to reproduce the value it does not explain."
cross_holding_register: "STRENGTHENED — the parent thesis' cross-holding hazard is a RATIO hazard, and this artifact prices it per ratio. 77.79% of the 6M 2026 net income served as a ratio numerator (64.99% of it through the measurement alternative alone) is the non-cash mark on equity Alphabet holds, including SpaceX; the served net_margin is 76.09% and the ex-mark net_margin is 16.90%. The exposure is not uniform across the table: operating_margin, roic, asset_turnover, every balance-sheet ratio and op_cf_ratio carry ZERO cross-holding exposure, while net_margin, roe, roa and every EPS-based metric carry all of it. The mechanism need not be appreciation: the equity-only dilution-gain channel (sale of interest in consolidated entities, 558 / 3,758) bypasses net income entirely and touches equity — and therefore roe's denominator — on a channel the net-income test cannot see. §5"
citations:
  - figure: "Consolidated statements of income, four periods — Q2 2026: revenues 119,796; cost of revenues 45,943; R&D 18,219; S&M 8,403; G&A 6,461; total costs and expenses 79,026; income from operations 40,770; other income (expense) net 97,983; income before income taxes 138,753; provision for income taxes 26,560; net income 112,193; preferred stock dividends 86; net income available to common stockholders 112,107. Q2 2025 comparatives 96,428 / 39,039 / 13,808 / 7,101 / 5,209 / 65,157 / 31,271 / 2,662 / 33,933 / 5,737 / 28,196. Six-month columns 186,662 and 229,692 revenues; 124,785 and 149,226 total costs; 61,877 and 80,466 operating income; 62,736 and 174,771 net income; 86 preferred dividends and 174,685 common-available in 2026"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 5
    url: https://agentii.ai/v/GOOG/sec156/5
    located_via: read_source_pages
  - figure: "Consolidated balance sheet, June 30 2026 — cash and cash equivalents 55,911; marketable securities 186,563; accounts receivable 69,175; inventory 9,991; other current assets 21,884; total current assets 343,524; total current liabilities 126,111; total liabilities 281,503; total stockholders' equity 640,480; total assets 921,983. The five current-asset lines sum exactly to 343,524 and the six liability lines to 281,503; liabilities plus equity equals 921,983 exactly"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 4
    url: https://agentii.ai/v/GOOG/sec156/4
    located_via: read_source_pages
  - figure: "Segment operating income and the OI&E component table — three- and six-month segment operating income (loss) Google Services 39,544 and 80,133; Google Cloud 8,814 and 15,412; Other Bets (1,799) and (3,899); Alphabet-level activities (5,789) and (11,180); total income from operations 40,770 and 80,466. OI&E components: gain (loss) on equity securities, net 1,286 and 99,031; equity method 419 and (35); other 72 and (973); and the interest-expense line that makes a coverage ratio computable in every period read; other income (expense), net 2,662 and 97,983"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 50
    url: https://agentii.ai/v/GOOG/sec156/50
    located_via: read_source_pages
  - figure: "Equity securities composition — measurement-alternative component of the gain on equity securities, net: 77,354 for the three months and 113,579 for the six months; components 21,399 and 21,531 marketable; 278 and 836 other; totals 99,031 and 135,946, which tie exactly to the OI&E table. Non-marketable securities rollforward and the statement that gains on non-marketable securities primarily consist of our investment in a private company"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 18
    url: https://agentii.ai/v/GOOG/sec156/18
    located_via: read_source_pages
  - figure: "Earnings per share by class of stock, Q2 2026 — basic EPS Class A 9.23, Class B 9.23, Class C 9.22, consolidated 9.22; diluted EPS Class A 9.12, Class B 9.12, Class C 9.11, consolidated 9.11; diluted numerators 60,893 / 7,612 / 51,300 / 112,193; diluted denominators 6,679 / 835 / 5,630 / 12,309. Each class quotient reproduces exactly: 60,893/6,679 = 9.11708; 7,612/835 = 9.11617; 51,300/5,630 = 9.11190; 112,193/12,309 = 9.11471"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 37
    url: https://agentii.ai/v/GOOG/sec156/37
    located_via: read_source_pages
  - figure: "Executive overview — operating margin 32% and 34% for the two quarter columns, and other income (expense) net +3,581% period over period. 40,770/119,796 = 0.340329 reproduces the FILED 34%, while the platform serves the 2026 Q2 operating_margin as 0.3503"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 45
    url: https://agentii.ai/v/GOOG/sec156/45
    located_via: read_source_pages
  - figure: "Highlights — net gains on equity securities of $99.0 billion, primarily from SpaceX and a private company; approximately $49.6 billion raised in June 2026; operating cash flow $39.1 billion for the quarter; capital expenditures $44.9 billion; 198,933 employees. The narrative names SpaceX as the source of the mark that dominates the quarter"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 46
    url: https://agentii.ai/v/GOOG/sec156/46
    located_via: read_source_pages
  - figure: "Stockholders' equity rollforward, six months ended June 30 2026 — opening 415,265, closing 640,480, with net income 174,771 and sale of interest in consolidated entities 3,758 among the components; the rollforward closes exactly on both the three-month and six-month tables"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec156
    page_no: 8
    url: https://agentii.ai/v/GOOG/sec156/8
    located_via: read_source_pages
  - figure: "Consolidated statements of income, three months ended March 31 2025 and 2026 — revenues 90,234 and 109,896; cost of revenues 36,361 and 41,271; R&D 13,556 and 17,032; S&M 6,172 and 7,606; G&A 3,539 and 4,291; total costs and expenses 59,628 and 70,200; income from operations 30,606 and 39,696; net income 34,540 and 62,578; diluted EPS 2.81 and 5.11"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec149
    page_no: 5
    url: https://agentii.ai/v/GOOG/sec149/5
    located_via: read_source_pages
  - figure: "Consolidated balance sheet, March 31 2026 — total assets 703,919; total liabilities 225,173; total stockholders' equity 478,746; total current liabilities 111,188; cash and cash equivalents 38,063; marketable securities 88,777; receivables 62,999; long-term debt 77,501. Liabilities plus equity equals 703,919 exactly; the filed total assets is 703,919 and NOT the 726,793 of my falsified roic hypothesis"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec149
    page_no: 4
    url: https://agentii.ai/v/GOOG/sec149/4
    located_via: read_source_pages
  - figure: "Segment operating income and OI&E, three months ended March 31 2026 — Google Services 40,589 (against a consolidated 39,696); Google Cloud 6,598; Other Bets (2,100); Alphabet-level activities (5,391). OI&E components: gain on equity securities, net 9,758 in 2025 and 36,915 in 2026; and the interest-expense line of the same table. The excluded net on the segment line is 893"
    ticker: GOOG
    form_type: 10-Q
    citation_id: sec149
    page_no: 43
    url: https://agentii.ai/v/GOOG/sec149/43
    located_via: read_source_pages
  - figure: "Consolidated statements of income, fiscal years 2023, 2024 and 2025 — revenues 307,394 / 350,018 / 402,836; total costs and expenses 223,101 / 237,628 / 273,797; income from operations 84,293 / 112,390 / 129,039; other income (expense) net 1,424 / 7,425 / 29,787; net income 73,795 / 100,118 / 132,170; diluted EPS 5.80 / 8.04 / 10.81"
    ticker: GOOG
    form_type: 10-K
    citation_id: sec144
    page_no: 50
    url: https://agentii.ai/v/GOOG/sec144/50
    located_via: read_source_pages
  - figure: "Consolidated balance sheets, December 31 2024 and 2025 — total assets 450,256 and 595,281; total liabilities 125,172 and 180,016; total stockholders' equity 325,084 and 415,265; total current liabilities 89,122 and 102,745; long-term debt 10,883 and 46,547. Liabilities plus equity equals total assets on both dates"
    ticker: GOOG
    form_type: 10-K
    citation_id: sec144
    page_no: 49
    url: https://agentii.ai/v/GOOG/sec144/49
    located_via: read_source_pages
  - figure: "Segment operating income (loss), fiscal years 2024 and 2025 — Google Services 121,263 and 139,404; Google Cloud 6,112 and 13,910; Other Bets (4,444) and (7,515); Alphabet-level activities (10,541) and (16,760); total income from operations 112,390 and 129,039. OI&E: gain on equity securities, net 3,714 in FY2024 and 24,080 in FY2025"
    ticker: GOOG
    form_type: 10-K
    citation_id: sec144
    page_no: 37
    url: https://agentii.ai/v/GOOG/sec144/37
    located_via: read_source_pages
  - figure: "Consolidated statements of cash flows, fiscal years 2023, 2024 and 2025 — net cash provided by operating activities 101,746 / 125,299 / 164,713; depreciation 11,946 / 15,311 / 21,136; gain on equity securities (2,671) / (24,620); capital expenditures (52,535) / (91,447). 164,713/102,745 = 1.6031242 reproduces the served 2025 Q4 op_cf_ratio 1.6031 exactly, which is the annual-over-period-end proof of the DA-26 instance"
    ticker: GOOG
    form_type: 10-K
    citation_id: sec144
    page_no: 53
    url: https://agentii.ai/v/GOOG/sec144/53
    located_via: read_source_pages
key_metrics:
  cross_holding_share_of_net_income_pct: 68.7
  net_margin_swing_pp: 59.32
  ratio_series_converted: "2/14"

---

# GOOG × ratio-analysis — methodology

**Method.** Every served ratio in `get_financial_ratios(GOOG)` is cross-checked against the
component identity of the line it divides, in every period for which this artifact cites a
filing page. A ratio is **reproduced** only when a *filed cell* — never the platform's
`computed` column and never a value reconstructed from the platform's own output — yields the
served 4-decimal string exactly. Every residual is then traced to a named defect in the
Data-Integrity Register, or declared UNRESOLVED with the derivation shown. Three rules govern
what counts as evidence here and each is applied below: `computed` is not citable as a
derivation (`§7.1`); `reported` is not the filed value (`§7.1`); and a zero returned by a
`us-gaap:` concept query is evidence about the **tag**, not about the filing (`§3.4`).

**The literal charge of this artifact** — *cross-check every derived ratio against the
component identity; catches DA-23/DA-24 residuals* — is discharged literally: **14 core ratio
series, 10 rows, 140 cells** are adjudicated in §3–§5, and **not one residual is left
unnamed**: each is disposed to DA-23, DA-24, DA-26, DA-28, DA-29, DA-30, or to the
UNRESOLVABLE-FROM-PLATFORM block in the frontmatter.

---

## 1. Pin base: the six tabled pins re-derived, and the contested `ratio-analysis` pin

The task carried a known hazard: `ratio-analysis` is the only skill with **two** candidate
roots, and two prior artifacts adopted `2d27c7f751fa` on the authority of `spec.md` §3 and
`reproduce.md` line 25 rather than on a derivation. Re-derived here, from scratch, with the
algorithm as implemented at `scripts/dispatch.py` (`skill_version_hash`: sha256 over
`sorted(skill_dir.rglob("*"))`, `p.name.encode("utf-8")` then file bytes, first 12 hex,
`__pycache__` excluded):

| skill | root | hash | tabled | verdict |
|---|---|---|---|---|
| operational-kpi | `vertical-plugins/business-intelligence` | `0730fd170124` | `0730fd170124` | MATCH |
| unit-economics | `vertical-plugins/business-intelligence` | `e87ee63269a2` | `e87ee63269a2` | MATCH |
| secular-trends | `agentii-equity-agent` **and** `equity-research-core` | `e6b41dbb2426` | `e6b41dbb2426` | MATCH (2/2 roots) |
| supply-chain | `vertical-plugins/industry-analysis` | `8cb3ac1de486` | `8cb3ac1de486` | MATCH |
| competitive | `agentii-equity-agent` **and** `equity-research-core` | `826995c722a4` | `826995c722a4` | MATCH (2/2 roots) |
| risk | `agentii-equity-agent` **and** `equity-research-core` | `953fc5d396e7` | `953fc5d396e7` | MATCH (2/2 roots) |

**18 of 18 reproductions — every one of the six pins matched in all three live locations:**
the working tree `/Users/frank/A/agenzym/agentii-investment-intelligence` (6/6), the marketplace
tree Claude Code loads skills from, `/Users/frank/.claude/plugins/marketplaces/agentii-investment-intelligence`
(6/6), and the user-level skills directory `/Users/frank/.claude/skills/agentii` (6/6). The
backup tree `/Users/frank/B-bk/...` matches **0/6** — all six differ there — so the result is not
"any root works": three live locations agree, a stale backup does not.
The base is therefore correct,
and only now is it legitimate to hash a new skill against it. The four decoys were re-tested
in the same pass and **all 32 hashes fail** (`packaging/targets/{claude-code,codex,generic-cli,cowork}`
× eight skills — e.g. `ratio-analysis` there hashes to `3f69103fbf71` / `271f4893b4d9` /
`3f69103fbf71` / `42c1dd5f52f1`), so the earlier 0-of-6 falsification stands and is now 0-of-32.

**`ratio-analysis` — tie broken on a structural ground, not on the spec's say-so.**

| candidate root | files | hash |
|---|---|---|
| `plugins/vertical-plugins/quantitative-analysis/skills/agentii/ratio-analysis` | 8 (`SKILL.md` + 7 `references/`) | **`2d27c7f751fa`** |
| `plugins/vertical-plugins/models-and-pitches/skills/agentii/ratio-analysis` | 2 (`references/` only, **no `SKILL.md`**) | `9b1d7a504789` |

The second root **is not a skill directory**: it has no `SKILL.md`, so it fails the
precondition of the algorithm the pin is supposed to record — a content hash of *the skill
directory* (`SKILL.md` + `references/`). A directory with no `SKILL.md` cannot be dispatched
and cannot be the hash base for a skill pin. The adopted value is **`2d27c7f751fa`**, and the
ground is now stronger than the two prior artifacts had: they argued from `spec.md`; this
artifact argues from the algorithm's own precondition, and the spec (`spec.md` line 569,
`quantitative-analysis`) agrees.

**Root-independence checked, and one divergent tree disclosed.** The pairing above was
re-hashed in the **live marketplace tree** — `/Users/frank/.claude/plugins/marketplaces/agentii-investment-intelligence/plugins/vertical-plugins`,
the root Claude Code actually loads these skills from — and reproduces **identically**:
`2d27c7f751fa` (`quantitative-analysis`, 8 files, `SKILL.md` present) and `9b1d7a504789`
(`models-and-pitches`, 2 files, none). A **third live location agrees as well** — the
user-level skills directory the Skill tool dispatches from in this environment,
`/Users/frank/.claude/skills/agentii/ratio-analysis`, is the same 8-file directory and hashes
to **`2d27c7f751fa`**. Three live locations agreeing (working tree, marketplace tree, global
skills dir) is the strongest form this check takes, and it makes the pin a property of the
skill as dispatched rather than of one checkout. Two stale copies do **not** agree: the backup
root
`/Users/frank/B-bk/agentii-investment-intelligence` carries a stale `ratio-analysis` of
**4 files** hashing to **`296490e6f094`** — no `models-and-pitches` copy at all. That
divergence is a property of the *backup*, not of the pin, but it is recorded because it is
exactly the failure a re-deriver would hit: hashing this skill against the wrong root yields
a value that appears nowhere in the record. A skill pin is meaningless without its root, and
`2d27c7f751fa` is the value of the root pair (primary + marketplace) that matches, not a
root-free constant.

**Recorded as a correction to the record.** `packaging/targets/{claude-code,codex,generic-cli,cowork}`
**exists** and each contains a decoy `recent-quarter/`, `ratio-analysis/`, and the six other
skills, all with real `SKILL.md` files. Any prior statement of absence in this thesis is
withdrawn; the tree is at the marketplace root, not at this repository's root, which is the
likely origin of the earlier negative — a listing of the wrong parent.

---

## 2. The component identity, and the vacuity test the brief demands first

The identity as charged is `gross profit − opex = operating income`. **Test first whether it
is vacuous.** At VRT it reduced to `(rev − COGS) − ((rev − COGS) − OP) = OP` — true by
construction, so it closed on every period while testing nothing (the DA-29 family). At GOOG
it is **not vacuous**, because Alphabet files **every tier as a cell** and no term on either
side is derived:

| period | revenues − total costs and expenses | = operating income | and cost of revenue + R&D + S&M + G&A | = total costs and expenses |
|---|---|---|---|---|
| Q2 2026 3M | 119,796 − 79,026 = 40,770 | 40,770 filed | 45,943 + 18,219 + 8,403 + 6,461 = 79,026 | 79,026 filed |
| Q2 2026 6M | 229,692 − 149,226 = 80,466 | 80,466 filed | 87,214 + 35,251 + 16,009 + 10,752 = 149,226 | 149,226 filed |
| Q1 2026 3M | 109,896 − 70,200 = 39,696 | 39,696 filed | 41,271 + 17,032 + 7,606 + 4,291 = 70,200 | 70,200 filed |
| FY2025 | 402,836 − 273,797 = 129,039 | 129,039 filed | 162,535 + 61,087 + 28,693 + 21,482 = 273,797 | 273,797 filed |
| FY2024 | 350,018 − 237,628 = 112,390 | 112,390 filed | 146,306 + 49,326 + 27,808 + 14,188 = 237,628 | 237,628 filed |

Every quarter cell is filed on [GOOG 10-Q Q2 2026 p.5 (https://agentii.ai/v/GOOG/sec156/5)](https://agentii.ai/v/GOOG/sec156/5),
every annual cell on [GOOG 10-K FY2025 p.50 (https://agentii.ai/v/GOOG/sec144/50)](https://agentii.ai/v/GOOG/sec144/50)
and the March quarter on [GOOG 10-Q Q1 2026 p.5 (https://agentii.ai/v/GOOG/sec149/5)](https://agentii.ai/v/GOOG/sec149/5).

**Verdict: not vacuous, and no replacement identity is needed.** Both tiers are fully filed in
all five periods, so the identity has discriminating power: it can fail, and it would have
caught a sign strip, a dropped component, or a substituted tier. It does not fail — **10 of 10
expansions close exactly.** It nevertheless **clears only the income statement**, because
every ratio in §3 divides a line the identity does not touch.

**Two further identities close, and they are filed, not back-solved:** the balance sheet
(liabilities + equity = assets exactly on all four dates — [GOOG 10-Q Q2 2026 p.4](https://agentii.ai/v/GOOG/sec156/4),
[GOOG 10-Q Q1 2026 p.4](https://agentii.ai/v/GOOG/sec149/4), [GOOG 10-K FY2025 p.49](https://agentii.ai/v/GOOG/sec144/49))
and the equity rollforward, which closes exactly on both the three-month and six-month tables
of [GOOG 10-Q Q2 2026 p.8](https://agentii.ai/v/GOOG/sec156/8).

**A fifth identity closes only through a named reconciling line, and that is the load-bearing
fact for §4:** the segment members do not sum to the consolidated total. They sum to it
**plus** the filed `Alphabet-level activities` line — `40,589 + 6,598 − 2,100 − 5,391 = 39,696`
on [GOOG 10-Q Q1 2026 p.43](https://agentii.ai/v/GOOG/sec149/43), and for the six months
`80,133 + 15,412 − 3,899 − 11,180 = 80,466` on [GOOG 10-Q Q2 2026 p.50](https://agentii.ai/v/GOOG/sec156/50).
The identity is therefore an **A20 detector at the line level**, not a total-to-total tie: an
exactly-compensating basis difference ties every total and is invisible to `validate_calculation`,
and the only thing that reveals it is a reconciling line with a name.

---

## 3. The ratio layer: every served ratio against its component identity

Population: the 14 core per-row fields of `get_financial_ratios(GOOG)` × 10 rows = **140 cells**.
`get_eps_growth` is adjudicated separately in §3.5 because it contradicts the ratio surface.
`computed_at` is identical on all ten rows (`2026-08-21T05:03:08.714Z`), so every row is one
batch and no row can be preferred as "later".

| ratio | served | reproducible as | residual | disposition |
|---|---|---|---|---|
| net_margin | 0.7609 | 174,771/229,692 exact (6M) | mark-inflated by 59.32 pp | **DA-24** §5 |
| operating_margin | 0.3503 | 80,466/229,692 exact (6M) | four bases, no basis field | **DA-30 / A19-4** §4 |
| roe | 0.2729 | 174,771/640,480 exact (period-end equity) | mark-inflated; denominator basis unnamed | **DA-24 + A19-5** §5 |
| roa | 0.1896 | 174,771/921,983 exact (period-end assets) | same, plus a DA-29 collapse in FY2024 Q4 | **DA-24 + DA-29** §3.4 |
| roic | 0.1085 | nothing | denominator matches no filed cell | **UNRESOLVED** (frontmatter) |
| asset_turnover | 0.2491 | 229,692/921,983 exact | FY2024 Q4 on a 8,700 denominator | **DA-29** §3.4 |
| current_ratio | 2.7240 | 343,524/126,111 exact | none | **DEMONSTRATED** |
| cash_ratio | 0.4433 | 55,911/126,111 exact | none | **DEMONSTRATED** |
| quick_ratio | 0.4433 | identical to cash_ratio in 10/10 | AR 69,175 silently dropped, 54.86 pp | **A19-1, DA-29** §3.4 |
| debt_to_equity | 0.4395 | 281,503/640,480 exact | labelled debt, computed as total liabilities, +28.5 pp | **A19-6** §3.3 |
| op_cf_ratio | 0.6729 | 84,859/126,111 exact | period-end not average; annual row in Q4 2025 | **DA-26 + A19-5** §3.2 |
| gross_margin | null 10/10 | computable (61.65%) | inert slot | **A19-2** §3.4 |
| interest_coverage | 1/10 rows | nothing | implied interest term ≈85.83 unfiled | **UNRESOLVED** (frontmatter) |
| debt_to_ebitda | 10/10 rows | nothing on the two rows tested | no filed-cell candidate | **UNRESOLVED** (frontmatter) |

### 3.1 The ratios that reproduce cleanly, and what "clean" is worth

`net_margin`, `current_ratio`, `cash_ratio` and the two turnover/return ratios reproduce
**exactly** on the 2026 Q2 and 2026 Q1 rows from filed cells, and the same denominators
reproduce the 2025 Q4 row (`132,170/402,836 = 0.3281`; `132,170/415,265 = 0.3183`;
`402,836/595,281 = 0.6767`). Exactness is not the same as correctness: a *substituted*
denominator also reproduces exactly. The value of the cross-check is that it identifies
**which** components were divided, and that is the only way the next four subsections exist.

### 3.2 DA-26 reaches the ratio layer on the `2025 Q4` row

Five duration measures on one row, all exactly annual:
`net_margin 0.3281 = 132,170/402,836`, `roe 0.3183 = 132,170/415,265`,
`roa 0.2220 = 132,170/595,281`, `asset_turnover 0.6767 = 402,836/595,281`,
`op_cf_ratio 1.6031 = 164,713/102,745`, on
[GOOG 10-K FY2025 p.50](https://agentii.ai/v/GOOG/sec144/50) and
[GOOG 10-K FY2025 p.53](https://agentii.ai/v/GOOG/sec144/53). Each is a single-period-end
denominator (not the skill's average) and each is an **annual** flow. The row is labelled
`2025 Q4`. This is the same defect the sibling recent-quarter artifact established for the
revenue line; here it is proved by five independent reproductions rather than by subtraction.

### 3.3 D/E is a label/computation mismatch, quantified against both debt bases

Served `debt_to_equity` = total **liabilities** / total equity, exactly to the 4 decimals
served, on three rows: `281,503/640,480 = 0.4395188`, `225,173/478,746 = 0.4703392`,
`180,016/415,265 = 0.4334967`. The skill's definition is Total Debt / Total Equity
(gaps below computed on the 4-decimal values, since those are the values at issue):

| row | served (liabilities basis) | skill, long-term-debt line | skill, platform total-debt 99,243 | gap |
|---|---|---|---|---|
| 2026 Q2 | 0.4395 | `98,165/640,480 = 0.1533` | `99,243/640,480 = 0.1550` | **+28.6 pp / +28.5 pp** |
| 2026 Q1 | 0.4703 | `77,501/478,746 = 0.1619` | — | +30.8 pp |
| 2025 Q4 | 0.4335 | `46,547/415,265 = 0.1121` | — | +32.1 pp |

The two debt figures agree: `us-gaap:DebtInstrumentCarryingAmount` computes to **99,243**, and
`98,165 + 1,078 = 99,243` — the balance-sheet long-term-debt cell plus a current portion. So
the mismatch is not a matter of which debt figure one prefers: **both** give ≈+28.5 pp. A
leverage ratio off by 28 pp is a different company's balance sheet.

### 3.4 The DA-29 back-solves, and the cheapest one of all

**FY2024 Q4 — two denominators absent from every cited filing.** `roa = 11.5078` and
`asset_turnover = 40.2320` imply a total-assets denominator of ≈**8,700** against a filed
**450,256** — a **51.75×** collapse, on [GOOG 10-K FY2025 p.49](https://agentii.ai/v/GOOG/sec144/49).
`roe = 0.5119` implies equity ≈**195,581** against a filed **325,084**. Both denominators are
unfiled; the row is a back-solve and is **UNRESOLVED**, not verified. Note the same row
carries **four** bases: the annual margins (0.3211, 0.2860 — the FY2024 annual values), the
8,700 denominator, the ≈195,581 denominator, and a served `debt_to_ebitda` of 0.1068.

**`quick_ratio ≡ cash_ratio` in 10 of 10 rows — a silently dropped component.** Served
`quick_ratio = 0.4433 = 55,911/126,111` exactly: the skill's definition is
`(Cash + Receivables)/Current Liabilities`, which is `(55,911 + 69,175)/126,111 = 0.9919`. The
receivable term is filed, is available, and **appears nowhere in the check** — the defect in
its cheapest possible form. The swing is **54.86 pp** on a ratio whose entire purpose is to be
the conservative version of the current ratio (2.7240 served, correct).

**`interest_coverage` is served once in ten rows and voids.** `296.7766` implies an
interest-expense term of ≈**85.83**, matching no filed cell, while interest expense **is**
filed in every period read (the OI&E component tables on
[GOOG 10-Q Q2 2026 p.50](https://agentii.ai/v/GOOG/sec156/50),
[GOOG 10-Q Q1 2026 p.43](https://agentii.ai/v/GOOG/sec149/43) and
[GOOG 10-K FY2025 p.37](https://agentii.ai/v/GOOG/sec144/37)). A coverage ratio is therefore
computable in every period the platform instead leaves null, and the one row it does serve is
voided by an unfiled term. **`gross_margin` is null
10/10** though `(119,796 − 45,943)/119,796 = 61.65%` is computable from two filed cells —
an inert slot. The absence of a *filed* gross-profit line is established **by reading the
income statement** (there is no such line; the statement runs Revenues → Cost of revenues →
… → Total costs and expenses), **not** by a zero from a `us-gaap:` query, which would be
evidence only about the tag. `inventory_turnover`, `receivables_turnover`, `dso` and `dio` are
null in 40/40 cells at filed data.

### 3.5 The growth block contradicts the ratio surface

`get_eps_growth` reports `cagr_3yr 4.25` while `get_financial_ratios` serves `eps_cagr3`
between 0.7604 and −0.6456 across the same ten periods; `get_eps_growth` returns
`cagr_5yr = null` while the ratio table serves a numeric `eps_cagr5` on all ten rows; and the
`eps_history` block labels the latest quarter's EPS (`9.11`) as **FY2026**. The served
`eps_cagr5` is **negative on every row** (−0.2222 to −0.3853) against a filed diluted-EPS
series that rises monotonically (4.56 → 5.80 → 8.04 → 10.81 → 9.11-quarterly). A negative
five-year CAGR on that series is **directionally impossible**; the exact computation is
declared **UNRESOLVED**. The divergence between the two surfaces is itself the finding: two
tools, one concept, one batch, incompatible signs.

---

## 4. Segment substitution reaches the ratio layer, and the A20 control

**A19 kind 4 confirmed, twice, on filed cells.** `operating_margin` is served as a **segment
member over consolidated revenue**:

- **2026 Q1: `0.3693 = 40,589/109,896 = 0.3693401`**, where `40,589` is the **Google Services
  segment** operating income on [GOOG 10-Q Q1 2026 p.43](https://agentii.ai/v/GOOG/sec149/43).
  Consolidated operating income is `39,696`, giving `39,696/109,896 = 0.3612142`. The swing is
  **+0.81 pp (81 bps)**. The excluded net is **−893** (Cloud +6,598, Other Bets −2,100,
  Alphabet-level activities −5,391).
- **2025 Q4: `0.3461 = 139,404/402,836 = 0.3460565`**, where `139,404` is the FY2025
  **Google Services** member on [GOOG 10-K FY2025 p.37](https://agentii.ai/v/GOOG/sec144/37).
  Consolidated is `129,039/402,836 = 0.3203264`. The swing is **+2.57 pp**.

**The A20 line-level detector, with its negative control.** A basis difference that
exactly compensates ties every total and is invisible to `validate_calculation`; what exposes
it is a **named reconciling line**. At GOOG that line exists and is filed: `Alphabet-level
activities` (−5,391 / −11,180 / −16,760 / −10,541) reconciles the segment members to the
consolidated total in every period, and it is footnoted in the source. **This is a legitimate
difference** — it reconciles, and it carries a name. The ratio layer then makes it
**illegitimate by omission**: the numerator is a segment member and no basis field says so.
The negative control is exact: had the served `operating_margin` been the consolidated value,
the reconciling line would have been irrelevant to it; because it is the segment value, the
line is load-bearing and **absent from the instrument's output**.

**The served-versus-filed contradiction is direct.** The filing itself prints
**"Operating margin 32% / 34%"** on
[GOOG 10-Q Q2 2026 p.45](https://agentii.ai/v/GOOG/sec156/45), and `40,770/119,796 = 0.340329`
reproduces the filed 34% exactly. The platform serves **0.3503** for that same quarter — the
**6M** basis. The gap against the filing's own printed margin is **+1.00 pp**.

**At least four bases across ten rows, no basis field:**

| row | served om | reproducible basis | status |
|---|---|---|---|
| 2026 Q2 | 0.3503 | consolidated **6M** (80,466/229,692) | exact |
| 2026 Q1 | 0.3693 | **Google Services member** / 3M revenue | exact |
| 2025 Q4 | 0.3461 | **Google Services member** / FY revenue | exact |
| 2025 Q1 | 0.3392 | consolidated 3M (30,606/90,234) | exact |
| 2025 Q3, 2025 Q2, FY2024 Q2 | 0.3435, 0.3200, 0.3483 | no candidate reproduces; candidates enumerated and excluded | **UNRESOLVED** |
| FY2024 Q3, FY2024 Q4 | 0.3211 both | the FY2024 **annual** value, twice | **DA-26** |

---

## 5. The cross-holding: which ratios are exposed, and by how much

The mark on equity Alphabet holds is **not a rounding item at the ratio layer; for the
net-income-bearing ratios it is the ratio.** Filed marks (gain on equity securities, net):
`99,031` for Q2 2026 and `135,946` for 6M 2026 on
[GOOG 10-Q Q2 2026 p.50](https://agentii.ai/v/GOOG/sec156/50), of which the
**measurement-alternative** component is `77,354` and `113,579` on
[GOOG 10-Q Q2 2026 p.18](https://agentii.ai/v/GOOG/sec156/18), and `36,915` for Q1 2026 on
[GOOG 10-Q Q1 2026 p.43](https://agentii.ai/v/GOOG/sec149/43). The cross-filing tie closes:
`36,915 + 99,031 = 135,946`. The narrative names the counterparty — *net gains on equity
securities of $99.0 billion, primarily from **SpaceX** and a private company* — on
[GOOG 10-Q Q2 2026 p.46](https://agentii.ai/v/GOOG/sec156/46).

| row | mark | net income (numerator) | mark / NI | measurement-alternative alone | served net_margin | ex-mark net_margin | swing |
|---|---|---|---|---|---|---|---|
| 2026 Q2 (6M) | 135,946 | 174,771 | **77.79%** | 64.99% | 0.7609 | **0.1677** | **59.32 pp** |
| 2026 Q1 (3M) | 36,915 | 62,578 | **58.99%** | 57.89% | 0.5694 | **0.2335** | **33.59 pp** |
| 2025 Q4 (FY) | 24,080 | 132,170 | 18.22% | — | 0.3281 | 0.2683 | 5.98 pp |
| 2024 Q4 (FY) | 3,714 | 100,118 | 3.71% | — | 0.2860 | 0.2754 | 1.06 pp |

(Q1's measurement-alternative split is a difference of two filed cells, `113,579 − 77,354`,
not a filed Q1 cell, and is labelled as such.)

**Exposure by ratio:**

| ratio | cross-holding exposure | magnitude |
|---|---|---|
| `net_margin`, `roe`, `roa` | **ALL of it** | 59.32 pp (6M) / 33.59 pp (3M) |
| every EPS-based metric | **ALL of it** | the mark is 1.69× the 6M operating income, 2.43× the 3M |
| `operating_margin`, `roic`, `asset_turnover` | **ZERO** | the mark sits below the operating line |
| `current_ratio`, `quick_ratio`, `cash_ratio`, `debt_to_equity`, `op_cf_ratio`, `interest_coverage` | **ZERO** | balance-sheet and operating-cash quantities |

**`roe` is exposed on both sides of the fraction, and a second channel bypasses net income
entirely.** Of the 6M 2026 equity increase of 225,215 on
[GOOG 10-Q Q2 2026 p.8](https://agentii.ai/v/GOOG/sec156/8): net income contributes 174,771
(77.6% of the increase, 77.79% of which is the mark), the June equity raise contributes
48,440 against the ~$49.6 billion gross raised reported on
[GOOG 10-Q Q2 2026 p.46](https://agentii.ai/v/GOOG/sec156/46), and **the equity-securities
mark alone is 135,946 — 60.4% of the entire equity increase**. `roe` divides by that moving
denominator. Separately, **`sale of interest in consolidated entities` (558 / 3,758)** moves
**equity and not net income** — a dilution-gain channel of the MSFT/IRDM kind that a
net-income test cannot see, and that at GOOG is a live second-order contributor to the roe
denominator. The register's cross-holding mechanism need **not** be appreciation; this channel
is the proof.

---

## 6. DA-30 live: diluted EPS is class-dependent and the platform collapses it

The filing presents **four earnings bases on one concept** and the platform serves **one
undimensioned value**, on [GOOG 10-Q Q2 2026 p.37](https://agentii.ai/v/GOOG/sec156/37):

| class | basic | diluted | diluted numerator | denominator | quotient |
|---|---|---|---|---|---|
| A | 9.23 | **9.12** | 60,893 | 6,679 | 9.11708 |
| B | 9.23 | 9.12 | 7,612 | 835 | 9.11617 |
| C | 9.22 | **9.11** | 51,300 | 5,630 | 9.11190 |
| consolidated | 9.22 | **9.11** | 112,193 | 12,309 | 9.11471 |

The platform serves **9.11** — the Class C / consolidated reading — with **no basis field**,
and net income (112,193), net income available to common stockholders (112,107, after the
86 of preferred dividends) and the three class-allocated numerators are all filed and all
different on [GOOG 10-Q Q2 2026 p.5](https://agentii.ai/v/GOOG/sec156/5). **The class split
and the capital-structure discontinuity are the same event**: the mandatory convertible
preferred issued in June 2026 is what makes the classes diverge, which is why the DA-30
collapse here is load-bearing rather than cosmetic (see `definitions_used.DA-28`). The
correct statement is not "GOOG's diluted EPS is 9.11" but "**9.11 on the Class C basis**".

---

## 7. Register census at the ratio layer

| DA | verdict at the ratio layer | evidence |
|---|---|---|
| **DA-23** sign strip | **CONFIRMED in the instrument's `reported` column; CLEAN on served ratio numerators — and the test has POWER here, unlike VRT** | negative operating-income instances are filed in every period read (Other Bets −1,799 / −3,899 / −7,515 / −4,444; Alphabet-level activities −5,789 / −11,180 / −16,760 / −10,541); the instrument emitted a negative `computed` on the same concept (OperatingIncomeLoss Q2 2025: computed −10,660 vs reported +2,826 — the served value being the **Google Cloud segment member**). No served ratio numerator is a stripped sign. §1, §7.1 |
| **DA-24** non-operating contamination | **CONFIRMED on all net-income-bearing ratios; REFUTED on operating-line ratios** | GAIN mode: 77.79% of the 6M numerator; 59.32 pp swing on `net_margin`; `operating_margin`/`roic`/`asset_turnover` carry zero. §5 |
| **DA-25** normalised per-unit | **NOT TESTABLE — kind 7** | no per-unit ratio is served for GOOG and none exists in the skill's formula table. Not claimed clean. |
| **DA-26** annual mislabelled quarterly | **CONFIRMED, row-wide, proved by five exact annual reproductions** | §3.2 |
| **DA-27** calendar-quarter labels | **NOT TESTABLE at the ratio layer — kind 7** | a label-layer defect that does not change any served ratio value; no component identity can reach it. Not claimed clean. |
| **DA-28** capital-structure discontinuity | **CONFIRMED as live and non-IPO** | the June 2026 mandatory convertible issuance, inside the window; it is the cause of the DA-30 instance in §6. |
| **DA-29** back-solved/opaque checks | **LIVE, three instances** | FY2024 Q4 (two unfiled denominators), quick_ratio (the dropped term is nowhere in the check), interest_coverage (implied term ≈85.83 unfiled). §3.4 |
| **DA-30** two bases, one concept | **LIVE, three instances** | diluted EPS by class; `operating_margin` across four bases; 3M vs 6M flows on one row label. §4, §6 |

### 7.1 The three `validate_calculation` failure modes, tested at GOOG

`validate_calculation` on accession `0001652044-26-000071` (the Q2 2026 10-Q) returns
**11 pass / 1 warn / 25 fail**. Three observations, each a mode the register has already named:

1. **A `pass` is not evidence about sign, basis, or contamination.** `us-gaap:NetIncomeLoss`
   (Jun 30 2026) passes at `computed = reported = 112,193,000,000` — the platform's absolute-dollar
   form of $112,193M, the very number that is **77.79% an unrealised mark** (§5).
   `us-gaap:OperatingIncomeLoss` (Jun 30 2026) passes at `40,770,000,000`. The check closes on
   both while testing neither basis nor contamination. That is the artifact's central
   methodological finding restated in the tool's own output.
2. **The same concept, same period, opposite signs, in the tool's own feed.**
   `us-gaap:OperatingIncomeLoss` (Jun 30 2025): `computed = −10,660,000,000` against
   `reported = 2,826,000,000` — a sign inversion *pair* on one row, where the served value is a
   segment member. The sign channel is **exercised** at GOOG (contrast with the VRT artifact,
   where it was UNEXERCISED and therefore not clean), and the served ratio layer nevertheless
   carries no inverted numerator.
3. **Aggregate-resolution failure at the consolidated level, in both directions.**
   `us-gaap:Assets` computes to 886,860 against a reported 921,983 (diff 35,123);
   `us-gaap:AssetsCurrent` computes to 335,972 against 343,524 (diff 7,552);
   `us-gaap:Liabilities` computes to 259,603 against 281,503;
   `us-gaap:StockholdersEquity` computes to 645,050 against a **reported 2,893**;
   `us-gaap:Revenues` computes to 24,874 against a reported 119,796. The linkbase's children
   do not resolve to the filed totals, and the `reported` column carries member-scale values.
   **A `fail` here is not evidence the filing is wrong, and a `pass` is not evidence the
   served ratio is right** — 25 of 37 rows fail, so the tool's verdict cannot be used as a
   clean/dirty signal for any figure without first resolving which member each side holds.
   And mode 3 proper: the tree returns **no `GrossProfit` row at all** — consistent with the
   statement's absence of such a line, which this artifact established **by reading the
   statement**, not by the missing row.

**`data_freshness` returns `2027-04-12`** in the same response — **future-dated against
`as_of` 2026-09-18**. It is not a currency signal and is not used as one here.

---

## 8. PIL-5: the DEMONSTRATED fraction under every reading

**The numerator is not in dispute; the denominator is UNSTATED.** This artifact's
contribution is reported under every reading, and the reading that flatters the pillar is
not preferred. The pillar-wide denominator remains unstated by the thesis.

| reading | unit | this artifact's contribution | comparison |
|---|---|---|---|
| **R1 — value-only** | the 140 core cells | **79/140 = 0.564** served; 61 null | SPCX 0.833 / VRT 0.125 |
| **R2 — value + components** | the ratio series whose value AND all components are filed, with no silent drop or substitution | **2/14 = 0.143** (current_ratio, cash_ratio) | SPCX 0.500 |
| **R3 — value + components + basis named in the source** | same series, basis field required | **2/14 = 0.143** | SPCX 0.250 |

Under **R1** the ratio layer looks half-served; under **R2 and R3** it collapses to two
series out of fourteen, because every other series divides a component the source files on a
basis the instrument does not name. If the artifact instead credited itself with the bases it
*identified* (period-end, segment-member, 3M/6M, equity-inclusive), R3 would rise to 6/14 —
and that reading is reported here **and rejected**: naming a basis after the fact does not
convert a figure whose basis the source did not name. **The PIL-5 falsifier may be TRIGGERED
at every reading.** That is the honest report.

**The substantive point, which the fraction alone cannot carry.** *Converting a figure to
DEMONSTRATED does not convert its BASIS* — and at GOOG the two come apart by **59.32 pp on
one ratio** (`net_margin` served 0.7609 against an ex-mark 0.1677), against SPCX's 46.47 pp.
A pillar whose definition of DEMONSTRATED stops at the value will certify a figure that is
three-quarters a non-cash mark on an outside asset — here, on **SpaceX**. "Converted to
DEMONSTRATED" must therefore be defined **to include the basis**, or the pillar measures the
wrong thing. That is the artifact's payload, and it is a defect of the definition, not of any
one ratio.

---

## 9. Corrections recorded (001 is frozen; nothing in it is rewritten)

1. **`packaging/targets/{claude-code,codex,generic-cli,cowork}` exists**, with a decoy skill
   tree per target, and all 32 hashes fail the tabled pins. §1.
2. **The sibling GOOG recent-quarter artifact's "68.7%"** is the **non-marketable-only**
   reading; the all-equity reading of the same quarter is **88.27%**, and this artifact uses
   the all-equity **77.79%** for the 6M numerator with the measurement-alternative split shown
   separately. The cross-holding register entry should carry the basis.
3. **001's facts validated, not re-questioned:** the pins in `001/reproduce.md` reproduce 18/18 (six pins × three live locations)
   (§1), and the FY2025 revenue `402,836` and operating cash flow `164,713` are confirmed
   against the filed cells at [GOOG 10-K FY2025 p.50](https://agentii.ai/v/GOOG/sec144/50) and
   [GOOG 10-K FY2025 p.53](https://agentii.ai/v/GOOG/sec144/53). The `corpus_version` remains
   `UNPINNED` for want of any endpoint, and is present as a pin.
4. **My own earlier figures, corrected against filed cells:** the Q1 2026 roic hypothesis
   denominator 726,793 → the filed total assets are **703,919**; the 6M 2025 operating income
   62,002 → **61,877**; FY2025 revenue 402,827 → **402,836**; FY2025 operating cash flow
   164,686 → **164,713**; the 2026 Q2 debt-to-EBITDA 0.4329 → served **1.2562**. Two of these
   were my own rounding slips (139,404/402,836 and 164,713/102,745), both of which reproduce
   **exactly** on recomputation; every marginal case in §3 was recomputed before being asserted.

**Method notes carried forward and applied.** `computed` is not citable as a derivation and
`reported` is not the filed value (at GOOG the `reported` column carries member-scale and
sign-stripped values — 2,893 for equity, 78 for a net income loss, 2,826 for an operating
income whose `computed` is negative). A `us-gaap:` zero is evidence about the tag (§3.4,
gross margin established by reading). A `search_keyword_in_source` zero is not evidence a word
is absent — every absence asserted here is asserted from pages read. `fiscal_period=FY` is not
a duration filter, and a compound filter can return zero where either term alone returns the
fact. `data_freshness` is future-dated (§7.1).

## 10. What could not be verified

Declared, not papered over: the roic denominator on every row tested; `interest_coverage`'s
implied interest term; `debt_to_ebitda` on the two rows tested; the two FY2024 Q4
denominators; the `operating_margin` basis on the three unresolved rows (candidates enumerated
and excluded); the exact computation behind the served negative 5-year EPS CAGR; and the
engine's member-and-basis selection rule itself — the last classified
**UNRESOLVABLE-FROM-PLATFORM**, since the public record reproduces every value it does not
explain, and **no** item required the UNRESOLVABLE-FROM-PUBLIC-SOURCES disposition.

---

## Sources

> Every figure asserted above resolves to the page cited, and every frontmatter URL appears
> here as a link. Table pages are quoted as **cells**, not as sentences about the tables.

| Figure | Source |
|---|---|
| Consolidated statements of income, four periods (Q2 2026 / Q2 2025 / 6M) | [GOOG 10-Q sec156 p.5](https://agentii.ai/v/GOOG/sec156/5) |
| Consolidated balance sheet, June 30 2026 — five current-asset lines to 343,524; CL 126,111; liabilities 281,503; equity 640,480; assets 921,983 | [GOOG 10-Q sec156 p.4](https://agentii.ai/v/GOOG/sec156/4) |
| Segment operating income and OI&E components, 3M and 6M — Cloud 8,814; other income (expense) net 97,983 | [GOOG 10-Q sec156 p.50](https://agentii.ai/v/GOOG/sec156/50) |
| Equity securities composition — measurement alternative 77,354 / 113,579; totals 99,031 / 135,946 | [GOOG 10-Q sec156 p.18](https://agentii.ai/v/GOOG/sec156/18) |
| Diluted EPS by class — A 9.12, C 9.11; numerators 60,893 / 7,612 / 51,300 / 112,193 | [GOOG 10-Q sec156 p.37](https://agentii.ai/v/GOOG/sec156/37) |
| Executive overview — "Operating margin 32% / 34%"; OI&E +3,581% | [GOOG 10-Q sec156 p.45](https://agentii.ai/v/GOOG/sec156/45) |
| Highlights — $99.0 billion net gains on equity securities, primarily SpaceX and a private company; ~$49.6 billion June raise; OCF $39.1 billion | [GOOG 10-Q sec156 p.46](https://agentii.ai/v/GOOG/sec156/46) |
| Stockholders' equity rollforward, six months — opening 415,265, closing 640,480, net income 174,771 | [GOOG 10-Q sec156 p.8](https://agentii.ai/v/GOOG/sec156/8) |
| Consolidated statements of income, March quarters — total costs 59,628 / 70,200; operating income 30,606 / 39,696; net income 34,540 / 62,578 | [GOOG 10-Q sec149 p.5](https://agentii.ai/v/GOOG/sec149/5) |
| Consolidated balance sheet, March 31 2026 — assets 703,919; liabilities 225,173; equity 478,746; CL 111,188 | [GOOG 10-Q sec149 p.4](https://agentii.ai/v/GOOG/sec149/4) |
| Segment operating income, 3M 2026 — Google Services 40,589 vs consolidated 39,696; Alphabet-level activities (5,391); equity securities 36,915; interest-expense line | [GOOG 10-Q sec149 p.43](https://agentii.ai/v/GOOG/sec149/43) |
| Consolidated statements of income, FY2023–FY2025 — revenues 307,394 / 350,018 / 402,836; operating income 84,293 / 112,390 / 129,039; net income 73,795 / 100,118 / 132,170 | [GOOG 10-K sec144 p.50](https://agentii.ai/v/GOOG/sec144/50) |
| Consolidated balance sheets, December 31 2024 and 2025 — assets 450,256 / 595,281; liabilities 125,172 / 180,016; equity 325,084 / 415,265; CL 89,122 / 102,745; LTD 10,883 / 46,547 | [GOOG 10-K sec144 p.49](https://agentii.ai/v/GOOG/sec144/49) |
| Segment operating income, FY2024 and FY2025 — Google Services 121,263 / 139,404; Alphabet-level activities (10,541) / (16,760); equity securities 3,714 / 24,080 | [GOOG 10-K sec144 p.37](https://agentii.ai/v/GOOG/sec144/37) |
| Consolidated statements of cash flows — operating cash flow 101,746 / 125,299 / 164,713; gain on equity securities (2,671) / (24,620); capex (52,535) / (91,447) | [GOOG 10-K sec144 p.53](https://agentii.ai/v/GOOG/sec144/53) |
