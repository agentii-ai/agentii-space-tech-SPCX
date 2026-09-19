/agentii:specify @theses/001-*/ thesis 001 是初步的landscape 调研，big picture
  @theses/002-*/ thesis 002 是对001的validation
  @theses/003-*/ thesis 003 是核心板块，也就是火箭发射，以spacex为主要company，也覆盖了其他一些这个板块的公司
  @theses/004-*/ thesis 004 是对spacex的深入研究

  我们之前还规划了thesis 005~011

  /Users/frank/B/agentii-space-tech-SPCX/theses/005-tier1-space-pure-plays
  /Users/frank/B/agentii-space-tech-SPCX/theses/006-tier2-connectivity-spectrum
  /Users/frank/B/agentii-space-tech-SPCX/theses/007-tier3a-diversified-primes
  /Users/frank/B/agentii-space-tech-SPCX/theses/008-tier3b-supply-chain
  /Users/frank/B/agentii-space-tech-SPCX/theses/011-idea-generation

  这次我需要你根据已经完成的001-004结果，再次评估之前设立的thesis 005-011，他们的设计是否合理，内容的划分如何？

  think globally and carefully

  Thought for 4s (ctrl+o to expand)

⏺ Skill(/agentii:specify)
  ⎿  Successfully loaded skill

  Thought for 8s, read 1 file (ctrl+o to expand)

⏺ Now let me survey what actually exists — both what 001–004 produced and what 005–011 currently hold:

⏺ Bash(T=/Users/frank/B/agentii-space-tech-SPCX/theses; echo "=== all theses ==="; ls -d $T/*/ 2>/dev/null | sed "s|$T/||"; echo; echo
      "=== contents of 004-011 ==="; f…)
  ⎿  === all theses ===
     001-technology-baseline/
     002-evidence-validation/
     … +20 lines (ctrl+o to expand)

  Thought for 4s (ctrl+o to expand)

⏺ 005–011 are stubs — spec, thesis, checklists, contracts, but zero artifacts. 004 is live (21 artifacts). So this is an evaluation of
  planned designs against realised results. Let me read what each thesis claims to cover:

⏺ Bash(T=/Users/frank/B/agentii-space-tech-SPCX/theses; for d in $T/005-* $T/006-* $T/007-* $T/008-* $T/009-* $T/010-* $T/011-*; do
        echo "════════ $(basename $d)  ($…)
  ⎿  ════════ 005-tier1-space-pure-plays  (632 lines)
     # Research Thesis: 005 — Tier 1: Listed Space Pure-Plays
     ## 0. Inherited baseline — what this thesis does NOT re-derive
     … +76 lines (ctrl+o to expand)

  Thought for 7s (ctrl+o to expand)

⏺ Now I can see the shape — and an immediate anomaly worth chasing. Let me parallelise the deep reading:

⏺ 2 background agents launched (↓ to manage)
   ├ Analyse 005 and 006 scope overlap
   └ Analyse 007-010 stub plans

  Thought for 8s (ctrl+o to expand)

      echo; echo "=== 004 spec structure ==…)
  ⎿  === workspace root ===
     assumptions.yaml
     constitution.md
     … +45 lines (ctrl+o to expand)

  Thought for 4s (ctrl+o to expand)

⏺ 004 covers Space / Connectivity / AI as an SOTP — and there's no AI thesis in 005–011 at all. Let me read the taxonomy, which should
  hold the tier design rationale:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== taxonomy.yaml ($(wc -l < $W/taxonomy.yaml | tr -d ' ') lines) ==="; head
      -70 $W/taxonomy.yaml)
  ⎿  === taxonomy.yaml (11 lines) ===
     # taxonomy.yaml — workspace copy of the closed classification axes (spec 046 Q76/Q78/Q83).
     # Scaffolded by agentii.constitution. The authoritative versioned declaration lives in
     … +11 lines (ctrl+o to expand)

  Thought for 3s (ctrl+o to expand)

⏺ The taxonomy is the classification axes, not the tier design. Let me find where the tier structure is actually defined:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== tier definitions in the constitution ==="; grep -n "Tier 0\|Tier 1\|Tier
      2\|Tier 3\|Tier 4\|Tier 5\|tier0\|t…)
  ⎿  === tier definitions in the constitution ===
     276:   Globalstar (~$11.57B, announced 2026-04-14, close expected 2027). Several Tier 1–2
     402:The universe is tiered by *role in the value chain*, not by market cap. Tier 0 is
     … +11 lines (ctrl+o to expand)

  Thought for 3s (ctrl+o to expand)

⏺ Found it — the design lives in constitution.md, and the organising principle is stated explicitly: "The universe is tiered by role
  in the value chain, not by market cap." Let me read the full tier definitions:

  Thought for 5s, read 1 file (ctrl+o to expand)

⏺ Now the design is clear, and two structural problems are already visible. Let me read the remaining tiers:

  Thought for 5s, read 1 file (ctrl+o to expand)

⏺ Tier 4 spans at least five unrelated industries, and Tier 5's tickers are pharma companies. Let me read the portfolio framework and
  004's inherited baseline:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== concentration / risk framework ==="; sed -n '1135,1165p'

  Thought for 5s, read 1 file (ctrl+o to expand)

⏺ Tier 4 spans at least five unrelated industries, and Tier 5's tickers are pharma companies. Let me read the portfolio framework and
  004's inherited baseline:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== concentration / risk framework ==="; sed -n '1135,1165p'
      $W/constitution.md; echo; echo "=== 004 spec §0 inh…)
  ⎿  === concentration / risk framework ===
     - **Sub-Sector Concentration**: ≤ 25% of NAV in any single sub-sector from the Sector
       Preferences table
     … +61 lines (ctrl+o to expand)

  Thought for 3s (ctrl+o to expand)

⏺ 004's §0 is a model inherited-baseline table — while 007–010 all say "(to be completed on activation)". Let me read 011's
  dependencies, since it's the capstone:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== 011 research question + dependencies ==="; sed -n '/^## 1\. Research
      Question/,/^## 1b\./p' $W/theses/011-id…)
  ⎿  === 011 research question + dependencies ===
     ## 1. Research Question
     … +54 lines (ctrl+o to expand)

  Thought for 11s (ctrl+o to expand)

⏺ 011's main line is "Space is a cost curve, not a value pool" — which 003 has since substantially refined. One more thing to check:
  the private-company layer, which your original brief said later theses would cover:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== Private-Company Coverage Rule ==="; grep -n "Private-Company Coverage Rule"
      -A 14 $W/constitution.md | head…)
  ⎿  === Private-Company Coverage Rule ===
     303:| P6 | Private-Company Coverage Rule | §Private-Company Coverage Rule | section |
     304-| P7 | Launch-Cost Floor Discipline | §F5a / §F5b | **facet** |
     … +23 lines (ctrl+o to expand)

  Thought for 3s (ctrl+o to expand)

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== the rule's body ==="; grep -n "Private-Company Coverage" $W/constitution.md
      | head; echo "---"; awk '/^#+.*P…)
  ⎿  === the rule's body ===
     303:| P6 | Private-Company Coverage Rule | §Private-Company Coverage Rule | section |
     563:before citing. Coverage is governed by the Private-Company Coverage Rule (P6).
     … +22 lines (ctrl+o to expand)

  Thought for 5s (ctrl+o to expand)

⏺ Important correction to my own hypothesis: the constitution rules that private companies are never standalone theses — so their
  absence from 005–011 is by design, not a gap. Let me check whether 003's corrections reached the constitution:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== constitution version + recent amendments ==="; grep -n "^version:\|^##
      Changelog\|^- added:\|^- corrected:\|…)
  ⎿  === constitution version + recent amendments ===
⏺ Important correction to my own hypothesis: the constitution rules that private companies are never standalone theses — so their
  absence from 005–011 is by design, not a gap. Let me check whether 003's corrections reached the constitution:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== constitution version + recent amendments ==="; grep -n "^version:\|^##
      Changelog\|^- added:\|^- corrected:\|…)
  ⎿  === constitution version + recent amendments ===

     === does it record 003's DA-26 falsification? ===
     … +10 lines (ctrl+o to expand)

  Thought for 5s (ctrl+o to expand)

⏺ Confirmed: the constitution still states DA-26 as "universal, 19 of 19" in five places (lines 135, 315, 1017, 1236) — but 003
  falsified it: 20 tested, 19 exhibiting, FLY the counterexample. 003's correction never propagated. Let me check one more
  cross-thesis dependency:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX/theses; echo "=== do 006 and 009 share companies? ==="; for t in
      006-tier2-connectivity-spectrum 009-tier4-enabling-lay…)
  ⎿  === do 006 and 009 share companies? ===
     --- 006-tier2-connectivity-spectrum universe:
     ACHR ADR AMZN AST ASTS AWS DA DEAL FCC GEO GILT GSAT IRDM JOBY JSAT LEO MDA MEO MSS OTC READY RKLB SATS SES SGBAF SKY SPCX T
     … +8 lines (ctrl+o to expand)

  Thought for 6s (ctrl+o to expand)

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX/theses; echo "=== is §0 (inherited baseline) filled per thesis? ==="; for d in
      $W/00{5,6,7,8,9}-* $W/010-* $W/011-*; do…)
  ⎿  === is §0 (inherited baseline) filled per thesis? ===
       005-tier1-space-pure-plays           §0 =  55 lines  written
       006-tier2-connectivity-spectrum      §0 =  62 lines  written
     … +5 lines (ctrl+o to expand)

  Thought for 4s (ctrl+o to expand)

⏺ Clear maturity split: 005 / 006 / 011 are designed; 007–010 are placeholders. Let me check whether the kit's own gate can score
  their design quality:

⏺ Bash(cd /Users/frank/A/agenzym/agentii-investment-intelligence && python3 scripts/agentii_cmd.py --help 2>&1 | head -25; echo "===
      ==="; python3 scripts/agentii_cmd.…)
  ⎿  usage: agentii_cmd.py [-h]
                           {specify,clarify,tasks,constitution,singleskill,converge,challenge,implement,status}
                           ...
     … +22 lines (ctrl+o to expand)
                           {specify,clarify,tasks,constitution,singleskill,converge,challenge,implement,status}
                           ...
     … +22 lines (ctrl+o to expand)
  ⎿  Shell cwd was reset to /Users/frank/B/agentii-space-tech-SPCX

  Thought for 3s (ctrl+o to expand)

⏺ Bash(cd /Users/frank/A/agenzym/agentii-investment-intelligence && timeout 90 python3 scripts/agentii_cmd.py status --workspace
      /Users/frank/B/agentii-space-tech-SPCX…)
  ⎿  (eval):1: command not found: timeout
  ⎿  Shell cwd was reset to /Users/frank/B/agentii-space-tech-SPCX

⏺ Bash(cd /Users/frank/A/agenzym/agentii-investment-intelligence && python3 scripts/agentii_cmd.py status --workspace
      /Users/frank/B/agentii-space-tech-SPCX 2>&1 | hea…)
  ⎿  <!-- GENERATED by agentii.status — DO NOT EDIT -->

     | thesis | present | tickers | known-open | pending_review |
     … +14 lines (ctrl+o to expand)
  ⎿  Shell cwd was reset to /Users/frank/B/agentii-space-tech-SPCX

  Thought for 7s (ctrl+o to expand)

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== the axioms 011's main line rests on ==="; grep -n "A1a\|A1b\|A2\b"
      $W/constitution.md | head -12; echo; echo…)
  ⎿  === the axioms 011's main line rests on ===
     62:  amended: §Sector Preferences — three rows restated. The v1.3.0 A1a/A1b split was not
     65:           A1b — the axiom v1.3.0 declared falsified. Space Infrastructure & Components
     … +24 lines (ctrl+o to expand)

  Thought for 5s (ctrl+o to expand)

⏺ I have enough to answer, though two deeper reads are still running (005/006 overlap, and 007–010 coherence) — I'll fold those in
  when they land. Here's what the survey establishes.

  The organising principle is contradicted by its own tier table

  The constitution states at line 402: "The universe is tiered by role in the value chain, not by market cap."

  Tier 1 does not satisfy that. Its twelve names span at least nine distinct value-chain roles — launch (RKLB, FLY), lunar services
  (LUNR), Earth observation (PL, BKSY), components (KRMN), stations (VOYG), satellite manufacturing (YSS), RF/SIGINT (HAWK), space
  data (SPIR), suborbital tourism (SPCE). What they actually share is being small, listed and space-focused — a maturity cohort, which
  is the axis the constitution says it isn't using.

  Tier 4 is worse: Vertiv (data-centre cooling), NVIDIA (silicon), Alphabet and Microsoft (hyperscale cloud), Amazon (satellite
  broadband), Apple (consumer devices), Amprius/EnerSys (batteries), T-Mobile (telecom). The constitution's own note concedes the
  platform files VRT under industrial.machinery and TER under tech.semiconductors. That is a theme, not a sector, and it has no single
  research question.

  So the tiers are not one taxonomy — Tier 0 is one company, Tier 1 is a size cohort, Tier 2 and 3 are functions, Tier 4 is a theme,
  Tier 5 is an activity.

  Three concrete content-division problems

  1. Vertical integrators span tiers, and 005 absorbs the overflow. RKLB is Tier 1, is acquiring into Tier 2 ($8B Iridium), and owns a
  Tier 3b asset (SolAero, solar cells). Its spec has grown three pillars that belong elsewhere: Pillar 5 is the space-grade
  solar-cell duopoly (008's subject), Pillar 6 is the RKLB/Iridium combined entity (006's), and 006's own Pillar 1 is IRDM margin
  decay. IRDM is a pillar in two theses, reached from opposite directions.

  2. AMZN is load-bearing in both 006 and 009 — for the same reason (Amazon Leo, and the Globalstar acquisition). So a Tier-2 deal
  question and a Tier-4 demand question rest on one company's filings, with no stated precedence.

  3. Tier 3 is split into two theses against the constitution's single tier (007 primes, 008 supply chain). The split is defensible on
  tractability — 20+ names is too many for one spec — but it means the tier model and the thesis model have silently diverged, six
  tiers becoming eight artefacts.

  Maturity is sharply uneven

  ┌────────────────────┬─────────────────────────────────┬───────────────────────────┐
  │                    │           §0 baseline           │          Pillars          │
  ├────────────────────┼─────────────────────────────────┼───────────────────────────┤
  │ 005, 006, 011      │ written (55–62 lines)           │ 6–7 each, fully specified │
  ├────────────────────┼─────────────────────────────────┼───────────────────────────┤
  │ 007, 008, 009, 010 │ "to be completed on activation" │ none                      │
  └────────────────────┴─────────────────────────────────┴───────────────────────────┘

  007–010 aren't under-designed, they're undesigned — and their §0 can now be written, because 001–004 exist. 004's §0 is the model: a
  table of inherited results, each citing the artifact and carrying its grade.

  A propagation gap, now demonstrable at the third thesis

  003 falsified DA-26's universality (20 tested, 19 exhibiting, FLY the counterexample). The constitution still states "universal, 19
  of 19" in five places — lines 135, 315, 1017, 1236. Its report presents this as correction #4 of five.

  That's the same defect 002 documented as "3 of 32 corrections propagated — recorded, correct, consumed by none." Nothing in the
  corpus→constitution path moves a correction into the register, and it has now failed twice.

  What is sound

  The tier→thesis coverage is complete — every constitution tier has a home, and 011 as the cross-cutting capstone with a stated
  "blocked on 004–010" dependency is the right shape. And the private-company layer being absent from 005–011 is correct by design,
  not a gap: the constitution's P6 rules that private companies are never standalone theses, only value-chain nodes, listed proxies,
  or feasibility comparators. I checked that expecting a hole and found a rule.

  Want me to write this up as a formal revision proposal — specifically, re-cutting the tier axis and moving the three off-tier
  pillars out of 005 — once the two pending reads land?

✻ Waiting for 2 background agents to finish

⏺ Agent "Analyse 005 and 006 scope overlap" finished · 1m 49s

  Thought for 5s (ctrl+o to expand)

⏺ That report is substantive, and it surfaced something concrete I want to verify before repeating it. It says 011's inherited ladder
  places GSAT at 7.4% — but 003 established GSAT's filed value is −7.37%, that being the DA-23 strip:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== GSAT operating margin: what each artifact says ==="; grep -rn
      "7\.4%\|7\.37\|−7\.37\|-7\.37" $W/theses/011-i…)
  ⎿  === GSAT operating margin: what each artifact says ===
     /Users/frank/B/agentii-space-tech-SPCX/theses/011-idea-generation/spec.md:24:| **The margin ladder**: operating margin monot
     one in distance from programme risk across 8 issuers — HEI 25.5%, KRMN 19.1%, WWD ~17%, LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC
     … +14 lines (ctrl+o to expand)

  Thought for 5s (ctrl+o to expand)

⏺ Confirmed, and this is the sharpest finding of the evaluation. Let me trace where the stripped value originates:

⏺ Bash(W=/Users/frank/B/agentii-space-tech-SPCX; echo "=== 001's synthesis §4.1 — the ladder's source ==="; grep -n "GSAT"
      $W/theses/001-technology-baseline/_cross/tec…)
  ⎿  === 001's synthesis §4.1 — the ladder's source ===
     520:  - claim: "GSAT is the purest monopsony in the universe: one buyer, 7.4% operating margin."
     522:    source: "GSAT 10-Q Q2 2026; constellation capacity dedicated to a single customer"
     … +12 lines (ctrl+o to expand)

  Thought for 6s (ctrl+o to expand)

⏺ Fully traced, and it's the most consequential thing I found. Let me give you the assessment — one deep read is still running
  (007–010 coherence), which I'll add when it lands.

  The GSAT sign: the inheritance chain is broken, and here is the proof

  011 carries, graded DEMONSTRATED and sourced to 001:

  ▎ "The margin ladder: operating margin monotone in distance from programme risk across 8 issuers — HEI 25.5%, KRMN 19.1%, WWD ~17%,
  ▎ LMT 12.4%, RTX 11.4%, LHX 11.1%, NOC 10.1%, GSAT 7.4%"

  GSAT's filed operating margin is −7.37%. That +7.4 is the DA-23 sign strip — the exact defect 003 spent its length documenting.
  Traced end to end:

  ┌────────┬─────────────────────────────────────────────────────────────────────────────────────────┬────────────────────────────┐
  │ Thesis │                                      What it says                                       │                            │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────┼────────────────────────────┤
  │ 001    │ "GSAT is the purest monopsony in the universe: one buyer, 7.4% operating margin" — and  │ origin of the defect       │
  │        │ a ladder row GSAT | 7.4%                                                                │                            │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────┼────────────────────────────┤
  │ 002    │ zero GSAT hits in its synthesis                                                         │ missed by the validation   │
  │        │                                                                                         │ thesis                     │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────┼────────────────────────────┤
  │ 003    │ −7.37%, with the "thinnest positive" reading explicitly withdrawn                       │ corrected                  │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────┼────────────────────────────┤
  │ 011    │ 7.4%, DEMONSTRATED, cited to 001                                                        │ still carrying it          │
  └────────┴─────────────────────────────────────────────────────────────────────────────────────────┴────────────────────────────┘

  It's load-bearing: 001's sentence "the thinnest operating margin of any network operator — 7.4%, below even…" describes a thin
  positive margin. The truth is a loss — a categorically different fact, and one that makes the monopsony claim stronger, not weaker.

  This is the third propagation failure in the programme: 002's "3 of 32 corrections propagated"; 003's DA-26 falsification, which the
  constitution still states as "universal, 19 of 19" in five places; and now a sign-flipped figure surviving four theses. Nothing in
  the corpus→corpus or corpus→constitution path moves a correction.

  The tier axis is three different axes wearing one name

  The constitution says "tiered by role in the value chain, not by market cap." Its own table contradicts that:

  - Tier 1 spans ≥9 distinct value-chain roles across 12 names — launch, lunar, EO, components (KRMN), stations, satellite
    manufacturing, RF/SIGINT, space data, tourism. What they share is being small, listed and space-focused. That is a maturity
    cohort.
  - Tier 4 spans ≥5 unrelated industries — data-centre cooling, silicon, hyperscale cloud, satellite broadband, batteries, telecom.
    The constitution concedes the platform files VRT under industrial.machinery.

  So Tier 0 is a company, Tiers 2–3 are functions, Tier 4 is a theme, and Tier 5 is an activity. A taxonomy that mixes axes cannot
  tell you whether a new name belongs in a thesis — which is exactly the failure mode below.

  005 is titled "pure-plays" and is mostly not about pure-plays

  Reading all six pillars against their own text (only P2 survives):

  ┌────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ Pillar │                                           What it actually is                                           │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ P1     │ a financing question — the spec says so: "it is a financing question wearing one"                       │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ P2     │ ✅ the one true cohort pillar                                                                           │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ P3     │ collapses into P1 — its own text reframes it as "which names can close the gap before funding runs out" │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ P4     │ self-declared: "a characterisation of three discrete events, not a property of the cohort"              │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ P5     │ supply chain — cedes the BA leg to 007, files under supply-chain, hands its result to 008               │
  ├────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ P6     │ self-declared: "a single-name, single-deal model"                                                       │
  └────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────┘

  And the deal duplication is three-fold. 005 P6, 006 P4 and 006 P5 each independently declare "what this adds is the date" for the
  same FCC → ITU → DCSA gate chain on the same IRDM/RKLB transaction, sourced from the same document (RKLB's risk factors). 005 P6
  even repeats 006 P4's break sentence verbatim: "the standalone case is not the pre-announcement case."

  Also: 005 needs BA, IRDM and TER — none in its universe. And it has an internal 8-vs-9 name count conflict, where BKSY's conditional
  row makes its own matrix subscription void.

  011 is the largest overlap in the programme

  Its universe holds 8 of 005's 9 names and all 5 of 006's. Its P3 uses the same instrument and the same worked numbers ("PL 1.69×,
  YSS 2.86×") as 005 P2. And the "does this concentrated supplier carry pricing power?" question is claimed by five artefacts — 005
  P5, 007, 008, 011 P6 — all pointing at the same dispositions. 011 disclaims re-research, but its matrix still lists tickers 005 and
  006 own.

  What is sound

  Coverage is complete — every tier has a home. Private companies being absent is correct by design, not a gap: constitution P6 rules
  they are never standalone theses. 004's §0 is the model the others should copy — an inherited-results table with artifact paths and
  grades.

  Maturity

  ┌────────────────────┬─────────────────────────────────┬──────────┐
  │                    │           §0 baseline           │ Pillars  │
  ├────────────────────┼─────────────────────────────────┼──────────┤
  │ 005, 006, 011      │ written                         │ 6–7 each │
  ├────────────────────┼─────────────────────────────────┼──────────┤
  │ 007, 008, 009, 010 │ "to be completed on activation" │ none     │
  └────────────────────┴─────────────────────────────────┴──────────┘

  007–010 aren't under-designed, they're undesigned — and their §0 is now writable, because 001–004 exist.

  What I'd recommend

  Three changes, in dependency order:

  1. Fix the propagation path first — a correction that lands in a thesis but not in the corpus it came from is not a correction. The
     GSAT figure is the proof, and it's live.
  2. Re-cut the tier axis so each thesis is one function with one research question, rather than one size cohort or one theme.
  3. Move the off-tier pillars out of 005 — the solar duopoly to 008, the RKLB/Iridium deal to 006, keeping the financing screen as
     005's spine.

  Want me to write this up as a formal revision proposal — with the specific pillar moves and the tier re-cut — and file it against
  005/006/011? I'd wait for the 007–010 read before finalising, since those four may re-absorb some of what I'm proposing to move.

✻ Waiting for 1 background agent to finish

⏺ Agent "Analyse 007-010 stub plans" finished · 6m 31s

  Thought for 9s (ctrl+o to expand)

⏺ Both reads are in. Here's the complete assessment.

  The taxonomy is the design — and that's the root problem

  007–010's universes are verbatim copies of the constitution's tier tables — the same coverage strings ("READY — 76 filings" for BA,
  "READY — 90" for VRT) appear in both. So the thesis boundaries are the tier boundaries, and every incoherence in the tier axis is
  inherited as a thesis. 005/006/011 were hand-designed, and their scopes drifted because there is no functional principle holding
  them in place.

  That single fact explains most of what follows.

  007–010 are scope reservations, not specifications

  Not one of the four names a single skill. Each §3 is titled "Skill Deployment Matrix" and contains prose workstreams — no skill, no
  depth, no ticker, no market-data stage (contrast 005's real matrix). No pillars, no {metric, threshold, source} falsifiers.

  And their §0 sections — the "do not re-derive" baselines — are empty, while 001–004 now exist to fill them.

  Ownership is now unassignable — five separate leaks

  ┌────────────────────────────┬─────────────────────────────────────────────────────┬────────────────────────────────────────────┐
  │          Question          │                    Who claims it                    │                  Verdict                   │
  ├────────────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────┤
  │ BA / Spectrolab (solar     │ 003 says "007/008 own it"; 005 says "belongs to     │ three owners, no home — and 007's RQ is    │
  │ cells)                     │ 007"; 008 omits BA from its universe entirely       │ multiple dilution, not solar rent          │
  ├────────────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────┤
  │ The IRDM/RKLB deal gate    │ 005 P6, 006 P4, 006 P5 — each declaring "what this  │ 3 pillars, 1 answer                        │
  │ chain                      │ adds is the date", from the same document           │                                            │
  ├────────────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────┤
  │ Pricing power of           │ 005 P5, 007, 008, 011 P6                            │ 5 artefacts, same dispositions             │
  │ concentrated suppliers     │                                                     │                                            │
  ├────────────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────┤
  │ KRMN                       │ 005 (9%) and 008 (full row)                         │ declared, resolved                         │
  ├────────────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────┤
  │ The deal counterparties    │ 006 uses AMZN, AAPL, RKLB, SPCX — none in its       │ unflagged                                  │
  │                            │ universe                                            │                                            │
  └────────────────────────────┴─────────────────────────────────────────────────────┴────────────────────────────────────────────┘

  Two dependency claims in the stubs are factually false. 008 says "some names sit in both" the supply chain and enabling layer — 008
  ∩ 009 = 0. 007 calls 006's names "the incumbent satcom competition" — 007 ∩ 006 = 0. 009 is 006's declared consumer — 009 ∩ 006 = 0.
  The four stubs are mutually disjoint, so the cross-references describe relationships that don't exist.

  Two stubs contradict themselves in-file

  009 fails the coherence test outright. Its universe spans four to five unrelated industries (data-centre thermal, GPU silicon,
  hyperscale cloud, batteries, D2D telecom) — and its own §3 calls the hyperscalers "the alternative the orbital case must beat." A
  thesis cannot hold its subject and its control in the same universe. Its MULTI constraint declaration concedes the point: "These do
  not reduce to one constraint" — three constraints are three sub-questions.

  Worse: §0 was never reconciled with the 002 notifications appended below it in the same file. §0 still asserts VRT's "scarcity
  pricing, which is what a functioning market produces" and "the GPU is not the dominant cost term" — the exact two claims those
  notifications refute ("its pricing-power evidence does not [survive]"; "THE COST-STACK CLAIM IS INVERTED").

  010's premise is also wrong. Varda is not in its universe — all five names are listed pharma, and Varda appears only in §0 as a P6
  value-chain node. And the subject isn't researchable from the filings: the agent checked UTHR's Q2 2026 10-Q — filed after the May
  2026 Varda announcement — plus its earnings call and FY2025 10-K, and MRK's 10-K. No mention. 001 had already recorded "no mention
  of Varda in the XBRL extract at all." 010's honest output is a watch-list (its own words), which makes it a disposition study, not a
  demand study.

  001 has already answered 007 — and 007's §0 hides it

  007's baseline says only "not pure-plays." But 001 found: "Primes cluster at 10–12% operating margin regardless of space exposure —
  prime margin carries no information about space leverage" and "RTX's inclusion tests whether adding primes adds information; on this
  evidence, it does not." 007's research question is substantially pre-answered negatively, and its inherited baseline omits the
  prior against it.

  An actionable correction: the PARTIAL labels are wrong

  The constitution defers 9 names as PARTIAL on a null sector. Measured directly: LLY has 75,248 XBRL facts, 81 documents, 19
  transcripts; AMZN 22,062 / 86 / 19; AAPL 16,450 / 77 / 19 — all completed_pct: 86. Only the sec_filings counter reads 0. They are
  researchable today; the label is the bulk-list partial-view artifact the constitution itself warns about at line 427.

  What's sound

  Coverage is complete — every tier has a thesis. 007's and 008's research questions are genuinely single (007: is minority space
  exposure diluted below the threshold that moves the multiple; 008: does anyone convert a bottleneck into pricing power). 010's
  honest output is right even though its framing isn't. Private companies being absent is correct by design.

  ┌────────────────────┬─────────┬─────────┬────────┐
  │                    │   §0    │ Pillars │ Skills │
  ├────────────────────┼─────────┼─────────┼────────┤
  │ 005, 006, 011      │ written │ 6–7     │ yes    │
  ├────────────────────┼─────────┼─────────┼────────┤
  │ 007, 008, 009, 010 │ stub    │ none    │ none   │
  └────────────────────┴─────────┴─────────┴────────┘

  What I'd recommend, in dependency order

  1. Fix propagation before anything else. Three failures now: 002's "3 of 32 corrections propagated"; 003's DA-26 falsification still
     reading "universal, 19 of 19" in five constitution lines; and GSAT's sign surviving four theses. A correction that doesn't reach
     the corpus it came from isn't a correction. This needs a mechanism, not a note.
  2. Re-cut the axis to one function per thesis, with a testable boundary rule: can the thesis's question be answered from a named
     ticker set without leaving it? 005 and 006 both fail today; 007–010 fail by construction.
  3. Then assign the orphans explicitly — BA/Spectrolab, the deal gate chain, the pricing-power question — one owner each.
  4. Re-derive 007–010's §0 from 001–004 using 004's table as the model, and reconcile 009's §0 against its own appended notifications
     before it is ever activated.

  I've kept this to analysis — nothing written. If you want, I can turn 1–3 into a concrete revision proposal with the specific pillar
  moves and the tier re-cut, and file it against 005/006/011.