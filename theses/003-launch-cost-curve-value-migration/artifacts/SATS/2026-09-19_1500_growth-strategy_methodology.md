---
thesis_id: "003-launch-cost-curve-value-migration"
pillar: PIL-6
ticker: SATS
skill: growth-strategy
mode: methodology
generated_at: 2026-09-19T15:00:00-04:00
constitution_pin: "1.5.0"
assumption_pin: "2"
skill_pin: "ab94b90ee0ff"
as_of: 2026-09-19
corpus_version: agentii-2026-09-18
definitions_used:
  - da_id: DA-24
    chosen_reading: >
      SATS is the register's DEFINING DA-24 instance, and its mechanism is an INVERTED impairment charge,
      not a gain. In the Q1 2026 statement of operations the line "impairments and other" carries
      $(66,159)K — a NEGATIVE number inside the cost block — so it REDUCES total costs and expenses and
      INCREASES operating income. `thesis.md` `known-open` describes SATS as "DA-24 contaminated
      (asset-sale gain through operating_income)"; that description is WRONG and this artifact corrects it.
      Chosen reading: the $(66,159)K is treated as a cost-block credit, not as an operating result, and
      the operating income of $392,847K is reported as inclusive of it — i.e. as
      $459,006K of operating income from operations before the inverted charge. Both figures are stated;
      neither is quoted alone.
  - da_id: DA-23
    chosen_reading: >
      SATS is the ONE issuer in this task where the served `OperatingIncomeLoss` sign cannot distinguish a
      filed positive from a stripped negative. Q1 2026 serves +392,847,000 and the filed figure IS
      +$392,847K — CLEAN, with the identity 3,667,489 − 3,274,642 = 392,847 closing exactly. Q1 2025
      serves +88,132,000 against a filed $(88,132)K — a HIT. Same issuer, same concept, same served sign,
      opposite filed signs. Chosen reading: every SATS operating result is read from the filed statement
      on the page cited, and the served value is never used. This within-issuer contrast is the strongest
      available demonstration that DA-23 is not detectable from the served value at all.
  - da_id: DA-30
    chosen_reading: >
      Two collisions are reported on both sides. (1) "Cash": the going-concern note states Cash on Hand of
      $1.516 billion as of March 31, 2026 while the Q2 2026 call states "about $14 billion or $15 billion
      in cash" — a ~9.6x gap on one concept, one filed and one CLAIMED, with no basis field. (2) The
      consideration on the two spectrum transactions is stated on a cash basis ($22.650 billion) and a
      mixed cash-and-stock basis (~$20 billion, of which up to $11 billion in SpaceX Class A at $212 per
      share). Chosen reading: both bases are reported, neither is summed without saying so, and the
      ~$42.65 billion total is labelled as cash-plus-stock rather than as cash.
  - da_id: DA-21
    chosen_reading: >
      SATS is the multi-segment issuer of this task (Pay-TV, Wireless, Broadband and Satellite Services,
      Other) and the launch-relevant capital sits in at least TWO of them — DBS satellites in Pay-TV and
      broadband satellites in Broadband and Satellite Services. Chosen reading: no SATS ratio is formed by
      combining segments, and the segment operating results are reported per segment with the residual to
      consolidated stated. The reason a launch share is non-formable at SATS is NOT the segment boundary
      (DA-21 is satisfied and the segments reconcile); it is that neither the launch price nor the
      satellite construction price is disclosed for either satellite in the current programme.
  - da_id: DA-29
    chosen_reading: >
      SATS files two income-statement identities that both close and a segment table whose operating
      results sum to $392,674K against consolidated operating income of $392,847K — a $173K residual, or
      0.04%. Chosen reading: closure is used only as corroboration that the segments read here are the
      right set; it is not treated as a check on anything. Where SATS asserts a reconciliation whose terms
      are not filed — the transaction pro-formas — this artifact refuses the back-solve and reports the
      filed consideration instead.
evidence_grade: DEMONSTRATED
deal_security_basis: standalone_pre_merger
unresolvable: true
unresolvable_class: UNRESOLVABLE-FROM-PUBLIC-SOURCES
citations:
  - figure: "Q1 2026 condensed consolidated statements of operations — total revenue $3,667,489K; service revenue $3,375,540K; equipment sales and other $291,949K; cost of services $1,998,268K; cost of sales-equipment $536,907K; SG&A $639,025K; D&A $166,601K; impairments and other $(66,159)K; total costs and expenses $3,274,642K; operating income $392,847K"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 11
    url: https://agentii.ai/v/SATS/sec121/11
    located_via: search_keyword_in_source
  - figure: "Note 1 — principal business segments (Pay-TV, Wireless, Broadband and Satellite Services, Other); AT&T License Purchase Agreement to sell 3.45 GHz and 600 MHz spectrum for $22.650 billion in cash"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 14
    url: https://agentii.ai/v/SATS/sec121/14
    located_via: search_keyword_in_source
  - figure: "MD&A Recent Developments — AT&T License Purchase Agreement, $22.650 billion, with repayment of intercompany loans and redemption of senior secured notes"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 78
    url: https://agentii.ai/v/SATS/sec121/78
    located_via: search_keyword_in_source
  - figure: "SpaceX License Purchase Agreement — AWS-4 and H-Block spectrum for $17 billion total consideration, proceeds to pay off Senior Secured Notes and Convertible Notes"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 79
    url: https://agentii.ai/v/SATS/sec121/79
    located_via: search_keyword_in_source
  - figure: "Amended and Restated SpaceX License Purchase Agreement, November 5, 2025 — total consideration increased to approximately $20 billion with up to $11 billion in SpaceX Class A Common Stock at $212 per share"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 81
    url: https://agentii.ai/v/SATS/sec121/81
    located_via: search_keyword_in_source
  - figure: "SpaceX consideration structure — up to $8.5 billion in SpaceX Class A at $212 per share, Seller Notes of $9.821 billion secured by AWS-4 and AWS-3 licences, Credit Agreement for Interim Debt Service of approximately $2 billion"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 80
    url: https://agentii.ai/v/SATS/sec121/80
    located_via: search_keyword_in_source
  - figure: "Wireless spectrum licences carrying amount $34,550,802 thousand including capitalized interest and impairment"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 46
    url: https://agentii.ai/v/SATS/sec121/46
    located_via: search_keyword_in_source
  - figure: "Restructuring Support Agreement and going concern — substantial doubt, Cash on Hand of $1.516 billion"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 82
    url: https://agentii.ai/v/SATS/sec121/82
    located_via: search_keyword_in_source
  - figure: "Segmental income statement for the three months ended March 31, 2026 — revenue, operating expenses, OIBDA and operating income (loss) by segment"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 71
    url: https://agentii.ai/v/SATS/sec121/71
    located_via: read_source_outline
  - figure: "Pay-TV segment — revenue $2.294 billion (down 9.6%), operating income $471.6 million, OIBDA $527 million, ARPU $110.19, pay-TV subscribers 6.632 million"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 93
    url: https://agentii.ai/v/SATS/sec121/93
    located_via: read_source_outline
  - figure: "Pay-TV variance analysis — service revenue down 10.4% to $2.262 billion, ARPU down 0.4% to $110.19, cost of services down 9.1% to $1.416 billion, depreciation down 26.9%"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 95
    url: https://agentii.ai/v/SATS/sec121/95
    located_via: read_source_outline
  - figure: "Broadband and Satellite Services segment results of operations, Q1 2026 vs Q1 2025 — revenue declines and subscriber losses"
    ticker: SATS
    form_type: 10-Q
    citation_id: sec121
    page_no: 101
    url: https://agentii.ai/v/SATS/sec121/101
    located_via: read_source_outline
  - figure: "Pay-TV satellite fleet with launch dates and orbital locations, plus satellite construction contracts — EchoStar XXV (Lanteris Space LLC construction; SpaceX launch services) and EchoStar XXVI, with no dollar amount disclosed for either contract"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 191
    url: https://agentii.ai/v/SATS/sec85/191
    located_via: read_source_pages
  - figure: "Pay-TV subscriber trends — 636,000 net DISH TV losses and 167,000 net SLING losses for 2025; gross activations down 28.4%; DISH churn rate 1.31%"
    ticker: SATS
    form_type: 10-K
    citation_id: sec85
    page_no: 89
    url: https://agentii.ai/v/SATS/sec85/89
    located_via: search_keyword_in_source
  - figure: "Q2 2026 earnings call — $1.5 billion Hughes bond maturity on August 1 and the Hughes Chapter 11 filing; $2.4 billion escrow for the FCC-mandated network shutdown"
    ticker: SATS
    form_type: earnings_call_transcript
    citation_id: ect78
    page_no: 1
    url: https://agentii.ai/v/SATS/ect78/1
    located_via: read_source_pages
  - figure: "Q2 2026 earnings call — 261.8 million SpaceX shares held; $14-15 billion in cash stated; $5-7 billion of network termination and tax cost; DISH DBS stalking horse bid 'potentially $300 million, somewhat less than that'"
    ticker: SATS
    form_type: earnings_call_transcript
    citation_id: ect78
    page_no: 2
    url: https://agentii.ai/v/SATS/ect78/2
    located_via: read_source_pages
key_metrics:
  regulatory_asset_realisation_usd_billions: 42.65
  operating_dbs_value_usd_billions: 0.3
  realisation_to_operating_dbs_multiple_x: 142
  spacex_shares_held_millions: 261.8
---

# SATS — Growth Strategy: The Counter-Case, Where Launch Cost Is Not a Variable in the Transaction That Realises the Value

## The finding

**SATS is `NON-FORMABLE`, and it is non-formable in the strongest possible form: both the numerator and
the denominator are unfiled.** SATS is a **launch customer** for exactly two satellites in its current
programme, and both are described in its own annual report by counterparty and by date and by nothing
else:

> *"**EchoStar XXV.** On March 20, 2023, we entered into a contract with **Lanteris Space LLC** for the
> construction of EchoStar XXV … During the fourth quarter of 2023, we entered into an agreement with
> **SpaceX for launch services** for this satellite, which is expected to be launched during the first
> quarter of 2026."*
>
> *"**EchoStar XXVI.** On May 15, 2025, we entered into a contract with Lanteris Space LLC for the
> construction of EchoStar XXVI … During the third quarter of 2025, we entered into an agreement with
> SpaceX for launch services for this satellite, which is expected to be launched during 2028."*
> — [📄 SATS 10-K p.191](https://agentii.ai/v/SATS/sec85/191)

**No dollar amount is disclosed for either contract — not the construction price, not the launch price.**
At PL and YSS the launch term is non-formable because it is unquantified inside a cost aggregate. At SATS
it is non-formable because **the entire programme cost is unquantified**, and the programme is precisely
the two-item set on which a launch share could otherwise be computed. That is a narrower and a cleaner
failure than a missing cost-line, and it removes any possibility of a substitute denominator.

**The counter-case is now quantified, and it is more extreme than the brief's framing suggests.**
EchoStar is realising its value by **selling the regulatory asset**, not by operating:

| Value realisation | Amount | Basis |
|---|---|---|
| AT&T License Purchase Agreement — 3.45 GHz and 600 MHz spectrum | **$22.650 billion** | **cash**, closed ([📄 SATS 10-Q p.14](https://agentii.ai/v/SATS/sec121/14), [📄 SATS 10-Q p.78](https://agentii.ai/v/SATS/sec121/78)) |
| SpaceX (Amended and Restated) License Purchase Agreement — AWS-4 and H-Block | **~$20 billion** ($17 billion as originally struck, increased on 5 November 2025), of which up to **$11 billion in SpaceX Class A at $212 per share** | **cash plus stock** ([📄 SATS 10-Q p.79](https://agentii.ai/v/SATS/sec121/79), [📄 SATS 10-Q p.81](https://agentii.ai/v/SATS/sec121/81)) |
| **Total regulatory-asset realisation** | **~$42.65 billion** | **cash plus stock — not a cash figure** |
| DISH DBS stalking horse bid | *"potentially $300 million, somewhat less than that"* | `CLAIMED` ([📄 SATS Q2 2026 call p.2](https://agentii.ai/v/SATS/ect78/2)) |

**Ratio: ~$42.65 billion of regulatory-asset realisation against ~$0.3 billion for the operating DBS
satellite business — approximately 142x.** The value did not migrate to the integrator, and it certainly
did not migrate to the launcher. **It migrated to the holder of a spectrum licence.** And the launch
variable does not enter the transaction at all: even if launch were free, the ~$42.65 billion is
unchanged.

**Two register-calibrating findings, both new.**

1. **The DA-24 mechanism at SATS is an INVERTED IMPAIRMENT, not a gain.** `thesis.md` `known-open` states
   that SATS is "DA-24 contaminated (asset-sale gain through operating_income)." **That description is
   wrong**, and the brief's own wording is the correct one: SATS' defining instance is a **negative**
   `impairments and other` line of **$(66,159)K** sitting inside the cost block, which *reduces* total
   costs and expenses and *increases* operating income. Corrected below.
2. **DA-23's served sign is not merely unhelpful at SATS — it is actively ambiguous within one issuer.**
   Q1 2026 serves `OperatingIncomeLoss` as **+392,847,000** against a filed **+$392,847K** — clean, and the
   identity closes exactly. Q1 2025 serves **+88,132,000** against a filed **$(88,132)K** — a hit. **Same
   issuer, same concept, same served sign, opposite filed signs.** No property of the served value
   separates them; only the filed statement does.

## Sources.

This artifact reads the SATS Q1 2026 Form 10-Q (three months ended March 31, 2026; accession
0001104659-26-058150), the FY2025 Form 10-K (accession 0001104659-26-021817) and the Q2 2026 earnings
call transcript, page-by-page. Pages are cited inline as
`[📄 SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11)`. No figure is taken from an XBRL `LABEL`, a
metrics block, or a served fact value. `get_segment_data` and `data_freshness` are unusable in this
workspace and were not used. **Basis note, per the task's mandate:** `deal_security_basis:
standalone_pre_merger` — the DBS and Hughes operating figures in this artifact describe businesses that
are contractually ceasing to exist (a prepackaged sale of DISH DBS with a stalking-horse bidder, and a
Hughes Chapter 11 filing), so they are read as standalone pre-disposal results; the spectrum and
SpaceX-share figures are **consideration**, not operating results, and are not combined with them.

## §1. Component identity first — DA-24 and DA-23, the two register defects SATS defines

Rule 5 requires `gross_profit − opex = operating_income` in-line with the opex definition named. SATS is
why rule 5 exists.

**Q1 2026 (three months ended March 31, 2026), per
[📄 SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11):**

| Line | Value | Basis |
|---|---|---|
| Service revenue | $3,375,540K | filed |
| Equipment sales and other | $291,949K | filed |
| **Total revenue** | **$3,667,489K** | filed |
| Cost of services | $1,998,268K | filed |
| Cost of sales — equipment | $536,907K | filed |
| Selling, general and administrative | $639,025K | filed |
| Depreciation and amortisation | $166,601K | filed |
| **Impairments and other** | **$(66,159)K** | filed — a NEGATIVE inside the cost block |
| **Total costs and expenses (INCLUSIVE)** | **$3,274,642K** | filed |
| **Operating income** | **$392,847K** | filed |
| Identity 1 — cost-block composition | 1,998,268 + 536,907 + 639,025 + 166,601 + (66,159) credit = **3,274,642** | closes exactly |
| Identity 2 — statement | 3,667,489 − 3,274,642 = **392,847** | closes exactly |
| Interest expense, net | $(592,660)K | filed — entirely below the operating line |
| Net loss | $(147,300)K; $(146.9)M attributable to EchoStar | filed |

**The DA-24 finding, precisely stated.** The `impairments and other` line is **$(66,159)K — a negative
number inside the cost block.** It is not a gain recorded above the line; it is a **reversal-shaped credit
that reduces total costs and expenses** and therefore **increases** operating income. Read on both bases:

- **As filed:** operating income **$392,847K**, inclusive of the $(66,159)K credit.
- **Excluding the credit, i.e. operating income from the operating lines:** $392,847K + $66,159K =
  **$459,006K**.

The two differ by **16.8%** of the as-filed operating income. **Both are reported here; neither is quoted
alone.** The correction to `thesis.md` is directional as well as numerical: the register describes SATS'
DA-24 as a *gain through operating_income*, and it is the opposite — a cost-block credit whose mechanism
is a **negative impairment**. An artifact looking for an asset-sale gain at SATS would not have found
this, because there is no gain. **This is the class `thesis.md` asked to be closed, and the register's
characterisation of its own defining instance was wrong.**

**The DA-23 within-issuer contrast — the register's cleanest demonstration that the served sign is
useless.**

| Period | Served `OperatingIncomeLoss` | Filed | Verdict |
|---|---|---|---|
| Q1 2026 | +392,847,000 | **+$392,847K** | **CLEAN** — same sign, same magnitude |
| Q1 2025 | +88,132,000 | **$(88,132)K** | **HIT** — magnitude identical, sign inverted |

**The served value cannot distinguish these two.** Both are positive; one is right and one is wrong. An
heuristic that flags SATS Q1 2025 as stripped would have to explain why it does not flag Q1 2026. The only
reliable detector remains the component identity, which closes on the filed figures in both periods. This
is a stronger statement than the register's current DA-23 note, which rests on the *frequency* of the
strip (14 of 17 issuers, 12 of 12 periods at RKLB); SATS shows the strip and the clean case **inside one
issuer's comparable quarter pair**.

**Net loss, and the basis it sits on.** Operating income $392,847K is entirely consumed below the line by
interest expense of $(592,660)K, producing a net loss of $(147,300)K. **This is a debt-structure result on
a profitable operating business**, and it is why the counter-case is about balance-sheet assets rather
than about operations.

## §2. growth-strategy-assessment — the programme-cost base, and why neither side exists

**The programme-cost base, stated, and it is the reason SATS is the strongest of the three NON-FORMABLE
verdicts.** For EchoStar XXV and EchoStar XXVI the programme cost has exactly two components — satellite
construction (Lanteris Space LLC) and launch services (SpaceX) — and **SATS discloses the price of
neither**, in the annual report or in any quarterly report
([📄 SATS 10-K p.191](https://agentii.ai/v/SATS/sec85/191)). A launch share cannot be formed because:

1. **The numerator is unfiled.** No launch price appears for either satellite.
2. **The denominator is unfiled.** No construction price appears for either satellite.
3. **No substitute denominator is available.** The programme is two satellites, so there is no segment,
   no cost-of-revenue line and no capital-expenditure caption that isolates them.

This is `NON-FORMABLE` in the register's third disposition — **not PASS, not FAIL** — and it is the
disposition the register reserves for a quantity that cannot be drawn at all rather than one that is
missing. **A band that cannot be drawn is not a band within ±50%.**

**A cross-issuer link worth carrying.** Lanteris Space LLC — SATS' satellite construction contractor for
both current platforms — is the entity LUNR acquired in January 2026 and now operates as a subsidiary.
**Two issuers in this task are counterparties on the same two satellites.** SATS is the launch customer;
LUNR is the builder; SpaceX is the launch provider. LUNR's launch-cost share is formable and (on FY2025
bases) above the bar; SATS' is non-formable. **The same two satellites generate a formable ratio at the
supplier and an unformable one at the customer**, which is a property of disclosure rather than of
economics.

**DA-21 is satisfied and is not the failure.** SATS reports four segments and they reconcile:

| Segment | Revenue | Operating income / (loss) | Margin |
|---|---|---|---|
| Pay-TV | $2,294,264K (down 9.6%) | $471,567K | 20.55% |
| Wireless | $962,491K (down 0.7%) | $(35,782)K | −3.72% |
| Broadband and Satellite Services | $329,656K (down 11.1%) | $44,184K | 13.40% |
| Other | $90,983K | $(87,295)K | — |
| **Segment sum** | **$3,677,394K** | **$392,674K** | vs consolidated **$392,847K** |
| Residual vs consolidated | **$9,905K (0.27%)** | **$173K (0.04%)** | intercompany eliminations and unallocated items |

Sources: [📄 SATS 10-Q p.71](https://agentii.ai/v/SATS/sec121/71),
[📄 SATS 10-Q p.93](https://agentii.ai/v/SATS/sec121/93),
[📄 SATS 10-Q p.101](https://agentii.ai/v/SATS/sec121/101). **The segment operating results sum to
$392,674K against consolidated operating income of $392,847K — a $173K residual, 0.04% of the total.** Per
DA-29 that closure is corroboration that this is the right segment set, not a check on anything; every
term in it is a filed figure on the same basis, which is the standard DA-29 actually sets.

**The launch-relevant capital sits in two of those segments** — DBS satellites in Pay-TV, broadband
satellites in Broadband and Satellite Services — and neither segment discloses a launch cost. **So the
non-formability is not a segment-boundary failure.** Stating this matters because the two failures have
different remedies: a boundary failure is fixed by a segment disclosure, and this one is not.

## §3. organic-growth-drivers-analysis — the counter-case, and a 9.6x collision on "cash"

**SATS is not a growth story on any operating line, and it is not trying to be.** Every segment is
shrinking: Pay-TV down 9.6%, Wireless down 0.7%, Broadband and Satellite Services down 11.1%
([📄 SATS 10-Q p.71](https://agentii.ai/v/SATS/sec121/71)). The Pay-TV decline is **volume, not price**:
ARPU is essentially flat at **$110.19, down 0.4%**, while 2025 saw **636,000 net DISH TV losses and
167,000 net SLING losses, with gross activations down 28.4%** and DISH churn at 1.31%
([📄 SATS 10-Q p.95](https://agentii.ai/v/SATS/sec121/95),
[📄 SATS 10-K p.89](https://agentii.ai/v/SATS/sec85/89)). Pay-TV operating income of $471,567K is held at a
20.55% margin by cost reduction — cost of services down 9.1% and depreciation down 26.9% — not by pricing.

**The realisation strategy, and the distress that forces it.**

- AT&T closed: **$22.650 billion in cash** for 3.45 GHz and 600 MHz
  ([📄 SATS 10-Q p.14](https://agentii.ai/v/SATS/sec121/14), [📄 SATS 10-Q p.78](https://agentii.ai/v/SATS/sec121/78)).
- SpaceX transaction: **~$20 billion**, structured as up to **$11 billion in SpaceX Class A Common Stock
  at $212 per share** plus cash, with **$9.821 billion of Seller Notes** secured by the AWS-4 and AWS-3
  licences and a Credit Agreement for Interim Debt Service of about **$2 billion**
  ([📄 SATS 10-Q p.81](https://agentii.ai/v/SATS/sec121/81), [📄 SATS 10-Q p.80](https://agentii.ai/v/SATS/sec121/80)).
  **SATS is taking payment in the equity of the launcher whose cost curve PIL-6 is about.** That is worth
  isolating: the launcher's shares are the *currency* of the transaction, and the retained holding is
  **261.8 million SpaceX shares** ([📄 SATS Q2 2026 call p.2](https://agentii.ai/v/SATS/ect78/2)).
- The filings assert **substantial doubt about going concern**, with Cash on Hand of **$1.516 billion**
  ([📄 SATS 10-Q p.82](https://agentii.ai/v/SATS/sec121/82)), and the wireless spectrum licences are
  carried at **$34,550,802 thousand** ([📄 SATS 10-Q p.46](https://agentii.ai/v/SATS/sec121/46)).
- **Hughes filed for Chapter 11.** On the Q2 2026 call: *"August 1, we had a $1.5 billion bond maturity
  for Hughes Corporation … So we filed **Chapter 11 bankruptcy** this morning for Hughes"*
  ([📄 SATS Q2 2026 call p.1](https://agentii.ai/v/SATS/ect78/1)), with **$2.4 billion going into escrow**
  for the FCC-mandated network shutdown ([📄 SATS Q2 2026 call p.1](https://agentii.ai/v/SATS/ect78/1)).

**DA-30 instance — "cash" is reported on two bases 9.6x apart, with no basis field.** The filed
going-concern note states **Cash on Hand of $1.516 billion** as of March 31, 2026
([📄 SATS 10-Q p.82](https://agentii.ai/v/SATS/sec121/82)). The Q2 2026 call states *"we have about
**$14 billion or $15 billion in cash**"* ([📄 SATS Q2 2026 call p.2](https://agentii.ai/v/SATS/ect78/2)).
**$14–15 billion against $1.516 billion is a ~9.6x gap on one word**, one figure `DEMONSTRATED` and one
`CLAIMED`, in consecutive reporting periods. The plausible explanation — the $22.650 billion AT&T cash
closing between the two dates — is **not filed and is not used**: applying DA-29, a term that appears
nowhere in the source makes any reconciliation a back-solve. **Both figures are reported; the
discrepancy is recorded as UNRESOLVED.** This matters for the counter-case because the two figures have
opposite implications about solvency, and an artifact quoting only Ergen's "$14 to $15 billion" would
read a company in substantial doubt as comfortably liquid.

## §4. organic-growth-driver-execution-assessment — VRT's reusable test

**VRT's reusable test: check whether price improvements coexist with flat or falling margin.** SATS is the
one issuer in this task where the **price leg is EXERCISED** — and it resolves negatively at the
precondition rather than at the comparison.

| Leg | Reading | Direction |
|---|---|---|
| **Price** | Pay-TV ARPU **$110.19, down 0.4%** ([📄 SATS 10-Q p.95](https://agentii.ai/v/SATS/sec121/95)) | **FLAT TO LOWER** |
| **Volume** | 636,000 net DISH TV losses and 167,000 net SLING losses in 2025; gross activations down 28.4% ([📄 SATS 10-K p.89](https://agentii.ai/v/SATS/sec85/89)) | **FALLING** |
| **Pay-TV margin** | Operating income $471,567K on revenue $2,294,264K = **20.55%** ([📄 SATS 10-Q p.93](https://agentii.ai/v/SATS/sec121/93)) | held **by cost reduction** |
| **Cost lines doing the work** | Cost of services down 9.1%; depreciation down 26.9% ([📄 SATS 10-Q p.95](https://agentii.ai/v/SATS/sec121/95)) | **COST-LED, not price-led** |

**Result: the test's precondition FAILS — there is no price improvement at SATS to coexist with anything.**
ARPU is down 0.4%, i.e. flat-to-lower, while volume falls at double-digit rates. A margin held by cutting
cost of services and depreciation is not a margin receiving a pass-through. **Disposition: EXERCISED,
NEGATIVE — and the distinction from the other three issuers matters.** PL and YSS have no price metric, so
their price leg is `UNEXERCISED`; SATS has one, it is filed, and it shows no improvement. **An unengaged
check is not a passed check, and here the check engaged and did not pass.**

## §5. Where PIL-6's claim bites at SATS

**The falsifier's first condition — "a demonstrated fall in revenue per launch at least as large as the
fall in cost per launch" — is `UNEXERCISED` at SATS.** SATS files no launch count, no per-launch revenue
and no mass-to-orbit metric.

**The falsifier's second condition — "a launch share of programme cost above 10%" — is `NON-FORMABLE` at
SATS, with both numerator and denominator unfiled.** Not above, not below: undrawable for either of the
two satellites in the current programme.

**SATS is the counter-case, and the quantification now supports the framing rather than merely asserting
it.** The operating DBS satellite business liquidates for **~$0.3 billion** on the stalking-horse bid
while the regulatory assets realise **~$42.65 billion** — approximately **142x**. The value in this name
was never in operating satellites and never in launch. It was in a spectrum licence that became more
valuable than the business that held it, and in the equity of the launcher, which is being used as the
**purchase consideration** for the licence. **Launch cost is not a variable in the transaction that
realises SATS' value**: the consideration is spectrum-for-cash plus spectrum-for-SpaceX-shares, and the
two satellites SATS is launching are immaterial to it. Even at a zero launch price the ~$42.65 billion is
unchanged.

**The one place the curve could touch SATS is as a holder, not as a customer.** SATS holds **261.8 million
SpaceX shares** ([📄 SATS Q2 2026 call p.2](https://agentii.ai/v/SATS/ect78/2)) and is receiving up to
**$11 billion** more at **$212 per share** ([📄 SATS 10-Q p.81](https://agentii.ai/v/SATS/sec121/81)).
**SATS' exposure to the launch cost curve is therefore an equity exposure to the launcher, not a cost
exposure as a launch buyer** — the exact inversion of a pass-through thesis, and a fact that belongs in
PIL-2's migration accounting rather than in PIL-6's demand-side leg. It is `CLAIMED` as to the holding
(the call), `DEMONSTRATED` as to the equity consideration (the 10-Q), and it is carried as a bound.

## §6. What could NOT be verified

| Item | Disposition | Class |
|---|---|---|
| Launch cost as a share of programme cost, EchoStar XXV and XXVI | **NON-FORMABLE** — neither the launch price nor the construction price is disclosed for either satellite; the programme is two satellites, so no substitute denominator exists | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Revenue per launch and cost per launch | **UNEXERCISED** — no launch count or mass metric is filed in any period | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| "Cash" — $1.516 billion (filed, March 31, 2026) vs "$14 billion or $15 billion" (call) | **UNRESOLVED** — a ~9.6x gap on one concept; the plausible timing explanation is not filed and per DA-29 is not used | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| The DISH DBS stalking-horse bid | **`CLAIMED`** — *"potentially $300 million, somewhat less than that"*; no filed figure | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Whether the ~$20 billion SpaceX consideration closes in full | **CONDITIONAL** — subject to FCC and DOJ approvals per the filings | UNRESOLVABLE-FROM-PUBLIC-SOURCES |
| Served `OperatingIncomeLoss` sign at SATS | **UNRESOLVED — platform defect, and ambiguous WITHIN the issuer**: Q1 2026 serves a genuine positive, Q1 2025 serves a stripped negative, both as `+`. Detector is the component identity shown in §1 | UNRESOLVABLE-FROM-PLATFORM |
| `thesis.md`'s description of SATS' DA-24 as an "asset-sale gain through operating_income" | **FALSIFIED** — the mechanism is an inverted impairment charge of $(66,159)K inside the cost block, which increases operating income rather than recording a gain | corrected in this artifact |

**Specific disclosure that would resolve the primary item:** the contract value of either the Lanteris
construction agreement or the SpaceX launch services agreement for EchoStar XXV or EchoStar XXVI. **Either
one alone would still be insufficient** — a launch share needs both — so the resolving disclosure is a
programme-level cost disclosure for the two satellites, or a launch-services purchase commitment captioned
to them. Unlike PL and YSS, where the cost structure exists and the launch term is unquantified, at SATS
the programme itself is unpriced.

## §7. Corrections inherited and carried

- **CORRECTION to `thesis.md` `known-open` — SATS' DA-24 mechanism.** The open item states "SATS is DA-24
  contaminated (asset-sale gain through operating_income)." **There is no asset-sale gain in SATS'
  operating income.** The mechanism is `impairments and other` of **$(66,159)K** — a negative inside the
  cost block — which reduces total costs and expenses from $3,340,801K to $3,274,642K and raises operating
  income from $326,688K to $392,847K. The register's own defining instance is an **inverted impairment**,
  which is what the brief says and what the filings show.
- **DA-23's served sign is ambiguous WITHIN a single issuer.** The register currently establishes DA-23 via
  frequency across issuers and periods (14 of 17 issuers; 12 of 12 at RKLB; 6 of 6 at YSS; 4 of 4 at LUNR;
  4 of 4 at PL). **SATS supplies the stronger form: one issuer, two comparable quarters, identical served
  signs, opposite filed signs.** Any detector based on the served value is refuted by this pair alone.
- **A `CLAIMED` figure is admissible to bound, never to populate.** Applied here to the stalking-horse bid,
  the "$14 to $15 billion in cash", and the 261.8 million SpaceX share count.
- **`+$1,824M` at SPCX is not evidence of migration.** SATS is the terminal counter-example in the same
  register: **~$42.65 billion of value realised, none of it from operating, and none of it from launch.**
- **The DA-30 "cash" collision is a new instance class** — one word, two figures, 9.6x apart, opposite
  solvency implications, neither carrying a basis field.

## §8. Carry-forwards

1. **SATS' DA-24 characterisation in `thesis.md` should be amended to "inverted impairment charge".** The
   current wording would send a reader looking for a gain, and there is none.
2. **`NON-FORMABLE` at SATS is the strongest of the three, because BOTH sides of the ratio are unfiled.**
   PL and YSS have a filed cost structure with an unquantified launch term; SATS has no programme cost at
   all. The three should be reported as one class with a graded severity, and SATS ranked highest.
3. **The SATS/LUNR/SpaceX triangle should be carried into the thesis.** The same two satellites produce a
   formable launch share at the builder (LUNR) and an unformable one at the customer (SATS), with the
   launcher's shares serving as the customer's payment. **Disclosure, not economics, decides which
   issuers can be measured — and that is a finding about the corpus, not about the sector.**
4. **SATS' true PIL-6 exposure is as a SpaceX shareholder, not as a launch customer.** 261.8 million shares
   plus up to $11 billion more at $212. This belongs in PIL-2's migration accounting: the value that did
   not pass through to the satellite operator was, at this issuer, **taken in the launcher's equity**.
5. **The ~142x ratio is a useful calibrating number for the thesis.** The operating satellite business is
   ~0.7% of the regulatory-asset realisation. Any framing that treats SATS as an operating space company
   is reading the wrong 0.7%.

## Sources

| Figure | Citation |
|---|---|
| Q1 2026 statements of operations — total revenue $3,667,489K; total costs and expenses $3,274,642K; impairments and other $(66,159)K; operating income $392,847K; net loss $(147,300)K | [📄 SATS 10-Q p.11](https://agentii.ai/v/SATS/sec121/11) |
| Note 1 — segments; AT&T License Purchase Agreement, $22.650 billion in cash for 3.45 GHz and 600 MHz | [📄 SATS 10-Q p.14](https://agentii.ai/v/SATS/sec121/14) |
| MD&A Recent Developments — AT&T License Purchase Agreement, $22.650 billion | [📄 SATS 10-Q p.78](https://agentii.ai/v/SATS/sec121/78) |
| SpaceX License Purchase Agreement — AWS-4 and H-Block for $17 billion | [📄 SATS 10-Q p.79](https://agentii.ai/v/SATS/sec121/79) |
| Amended and Restated SpaceX agreement — ~$20 billion total, up to $11 billion in SpaceX Class A at $212 per share | [📄 SATS 10-Q p.81](https://agentii.ai/v/SATS/sec121/81) |
| SpaceX consideration structure — up to $8.5 billion in Class A at $212; Seller Notes $9.821 billion; Interim Debt Service ~$2 billion | [📄 SATS 10-Q p.80](https://agentii.ai/v/SATS/sec121/80) |
| Wireless spectrum licences carrying amount $34,550,802 thousand | [📄 SATS 10-Q p.46](https://agentii.ai/v/SATS/sec121/46) |
| Going concern — Cash on Hand of $1.516 billion | [📄 SATS 10-Q p.82](https://agentii.ai/v/SATS/sec121/82) |
| Segmental income statement, three months ended March 31, 2026 | [📄 SATS 10-Q p.71](https://agentii.ai/v/SATS/sec121/71) |
| Pay-TV segment — revenue $2.294 billion (down 9.6%); operating income $471.6 million; ARPU $110.19; subscribers 6.632 million | [📄 SATS 10-Q p.93](https://agentii.ai/v/SATS/sec121/93) |
| Pay-TV variance analysis — ARPU down 0.4%; cost of services down 9.1%; depreciation down 26.9% | [📄 SATS 10-Q p.95](https://agentii.ai/v/SATS/sec121/95) |
| Broadband and Satellite Services segment results of operations, Q1 2026 vs Q1 2025 | [📄 SATS 10-Q p.101](https://agentii.ai/v/SATS/sec121/101) |
| EchoStar XXV and EchoStar XXVI — Lanteris Space LLC construction contracts and SpaceX launch services agreements, with no dollar amount disclosed for either | [📄 SATS 10-K p.191](https://agentii.ai/v/SATS/sec85/191) |
| Pay-TV subscriber trends — 636,000 net DISH TV losses; 167,000 net SLING losses; gross activations down 28.4%; churn 1.31% | [📄 SATS 10-K p.89](https://agentii.ai/v/SATS/sec85/89) |
| Hughes $1.5 billion bond maturity and the Chapter 11 filing; $2.4 billion escrow for the FCC-mandated network shutdown | [📄 SATS Q2 2026 call p.1](https://agentii.ai/v/SATS/ect78/1) |
| 261.8 million SpaceX shares; "$14 billion or $15 billion in cash"; $5–7 billion termination and tax cost; DISH DBS stalking horse "potentially $300 million, somewhat less than that" | [📄 SATS Q2 2026 call p.2](https://agentii.ai/v/SATS/ect78/2) |

*Grades: the Q1 2026 income statement, the segment table, the transaction consideration and the fleet
disclosure are `DEMONSTRATED` — filed cells with arithmetic that closes. The stalking-horse bid, the
261.8 million SpaceX share count, the "$14 to $15 billion in cash" and the $2.4 billion escrow are
`CLAIMED`. The segment sum residual ($173K) and the ~142x value ratio are `DERIVED`. `skill_pin:
ab94b90ee0ff` · `pillar: PIL-6`.*
