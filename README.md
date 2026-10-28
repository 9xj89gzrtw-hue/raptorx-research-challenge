# RaptorX Research Challenge — entry

**Asset:** PUMP (Pump.fun), Solana — `pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn`
**Report generated in RaptorX:** 2026-10-27 21:45 UTC (RexScreener → Solana → Pump → *Full Report*)
**Follow-up questions asked to REX AI:** 2026-10-27 21:46 UTC, 4 questions, same thread (`Rex Pilot → PUMP (Pump)`)
**REX AI answers received:** 2026-10-28 02:41–02:56 UTC, all four, same thread — transcript in `answers/`, screenshots `evidence/08`–`11`
**Second asset for range:** JUP (Jupiter) — report 21:22 UTC + 1 question (cached report, *not* used for the main argument)

The four questions below are not generic prompts. Each one takes two numbers that the
generated report states in different sections — numbers that cannot both be true — and
forces the model to reconcile them with arithmetic that a reader can check by hand.
`checks.py` / `checks.txt` in this repo recomputes every figure.

---

## Q1 — The report publishes four 24h volumes that differ by 146x. Revenue pins which one is real.

> Section 6 lists four incompatible 24h volume figures — $452M (KOL @lbexplorer), $146.19M
> (CoinGecko aggregate), $37.59M (the Solana volume leaderboard) and $3.09M (the single
> PumpSwap PUMP/USDC pair). The $1.68M daily revenue actually lets us back out which one is
> real: $1.68M/$452M = 0.37% blended take rate, $1.68M/$146.19M = 1.15%, $1.68M/$37.59M =
> 4.5%. Since pump.fun's fee schedule sits near 1%, only the $146M figure is consistent. If
> that is the real number, the 24h volume-to-market-cap ratio is 7.3% rather than 22.6%, and
> the $839.6K/day buyback implies a 15.3% annualized yield on the $2.0B cap. Which volume do
> you actually stand behind, and does that buyback yield survive once treasury-funded burns
> are netted out of market buybacks?

**Why it is a hard question:** revenue ÷ volume is a take rate, and a take rate is a
*known constant* of the business model. That constraint collapses a 146x spread of
unverified numbers onto a single admissible value, and the choice changes two headline
conclusions of the report (volume/mcap "health" and the buyback yield) at once.

| volume used | implied blended take rate | volume / market cap | buyback yield (annualised) |
|---|---|---|---|
| $452M (KOL) | 0.37% | 22.6% | 15.3% |
| **$146.19M (CoinGecko)** | **1.15%** | **7.3%** | **15.3%** |
| $37.59M (leaderboard) | 4.47% | 1.9% | 15.3% |
| $3.09M (single pair) | 54.3% | 0.15% | 15.3% |

---

## Q2 — The valuation denominator is TVL the token does not own; revenue is the one it does.

> You price PUMP at 5.98x market-cap-to-TVL and 10.72x FDV-to-TVL, but that $334M of TVL is
> liquidity providers' capital inside PumpSwap, not a claim that PUMP holders own. The same
> report gives daily revenue of $1.68M, i.e. roughly $613M annualized, which puts the token at
> ~3.3x sales and ~5.8x FDV/sales. Which denominator should a holder actually underwrite —
> TVL, which the token does not own, or revenue, which the platform does? And if revenue is
> the right lens, what fee decay rate is a 3.3x P/S multiple implicitly assuming as memecoin
> launchpad volumes normalise?

**Why it is a hard question:** it separates *capital that passes through* a protocol from
*cash flow that accrues* to the token, then converts the answer into an explicit market
expectation (a 3.3x P/S on a fee stream that is structurally tied to memecoin launch
activity). This is the difference between a metric and a thesis.

`$1.6792M × 365 = $612.9M` → `mcap/revenue = 3.26x`, `FDV/revenue = 5.84x`, versus
`mcap/TVL = 5.98x` and `FDV/TVL = 10.72x` quoted by the report.

---

## Q3 — The report repeats an unverified "89% of SOL trading" while its own data implies 28%.

> The report repeats an unverified claim that Pump.fun holds "89% of SOL trading" from a
> single KOL, while its own leaderboard sample puts PUMP at $37.59M out of $133.5M — about
> 28%. Both numbers cannot be true in the same 24 hours. What evidence would settle it
> (PumpSwap fee-account inflows, Jupiter or aggregate Solana DEX volume, unique-trader
> counts), and how much of the dominance thesis survives if the real share is closer to 28%
> than 89%?

**Why it is a hard question:** it refuses an appealing headline number and replaces it with
the report's own arithmetic — a 60.8 percentage-point contradiction — then asks for the
specific data source that would arbitrate. A model that just agrees with the KOL fails;
a model that reconciles them has to explain which denominator each figure uses.

---

## Q4 — A 4-sigma five-minute sell skew, in a token whose marginal buyer is also the burner.

> Buy/sell counts are buyer-favoring on every window except the last five minutes: 23 buys
> against 61 sells out of 84 transactions, which is about four standard deviations from
> balanced and therefore probably not noise, while the 24h tape is 7,960 versus 6,892. At the
> same time 0.02% of total supply is burned daily (~7.3% a year) yet the float is still only
> 46% of max supply. How would you tell a routine post-bounce flush from the start of
> distribution by an entity that is also the marginal buyer, and which on-chain series —
> burn-wallet inflows, PumpSwap LP removals, or CEX deposit addresses — would break first?

**Why it is a hard question:** the report dismisses the 5-minute window as "a very recent
burst of profit-taking", but 23/84 is a z-score of **−4.15** — it is not noise. Meanwhile the
buyback-and-burn programme makes the issuer simultaneously the largest reported buyer and the
entity reducing float, which destroys the usual buy/sell-count interpretation. The question
asks for *discriminating* observables instead of a directional opinion.

RaptorX's own Coin-O-Metry panel makes the conflict visible: buy ratio **27%** on 5m versus
**54%** on 24h (evidence image 02).

---

## Evidence

| file | what it shows |
|---|---|
| `evidence/01-report-top.png` | Rex Pilot panel: PUMP (Pump), report header, chain + contract, "Updated 2 min ago" |
| `evidence/02-report-coinometry-orderflow.png` | Coin-O-Metry + Order Flow: 5m buy ratio 27% vs 24h 54% |
| `evidence/03-report-technical.png` | Technical Analysis section of the same report |
| `evidence/04-questions-1-2.png` | Q1 and Q2 as posted in the thread |
| `evidence/05-questions-3-4.png` | Q3 and Q4 as posted in the thread |
| `evidence/06-thread-fullpage.png` | full RaptorX window: token page + Rex Pilot thread with the question |
| `evidence/07-jup-thread.png` | the earlier JUP report thread with a supply-denominator question |
| `evidence/08-answer-1-volume.png` | Q1 answered: $146.19M, 7.31% turnover, 15.32% buyback yield |
| `evidence/09-answer-2-denominator.png` | Q2 answered: TVL rejected, 3.3x P/S / 5.8x FDV-sales |
| `evidence/10-answer-3-market-share.png` | Q3 answered: 89% launchpad vs 28% leaderboard, arbiters ranked |
| `evidence/11-answer-4-flow.png` | Q4 answered: CEX deposits → LP removals → burn inflows |
| `answers/q1-volume.md` … `answers/q4-flow.md` | full verbatim REX AI answer text for all four questions |
| `evidence/api-chat-response.json` | raw `POST /api/chat` response — see platform note below |
| `report/pump-report.md` | full text of the generated PUMP report (the artefact under questioning) |
| `report/jup-report.md` | full text of the earlier JUP report |
| `checks.py` / `checks.txt` | every number in Q1–Q4 recomputed from report inputs |

---

## What REX AI answered (28 Oct, 02:41–02:56 UTC)

The questions were first posted at 21:46 UTC and the chat endpoint was hard-down at that
moment (HTTP 500, upstream key limit — raw response kept in `evidence/api-chat-response.json`).
The thread held the questions, and once the key recovered all four were answered in the same
thread. Full text in [`answers/`](answers), captured screenshots `evidence/08`–`11`.

| # | what the report claimed | what REX AI now says | effect on the entry's arithmetic |
|---|---|---|---|
| Q1 | four 24h volumes, 146x apart | stands behind **$146.19M**; $452M is *"total activity on the Pump.fun platform across all memecoins"* | turnover **7.31%**, not 22.6%; buyback **$306.45M/yr = 15.32%** on $2.0B cap, **8.56%** on $3.58B FDV |
| Q2 | prices the token at 5.98x mcap/TVL | rejects TVL: *"liquidity provider capital… PUMP holders receive zero claim"*; underwrites revenue instead | **3.3x** circulating P/S, **5.8x** FDV/sales; decay drivers: 1.25%→0.30% fee tiers, cyclicality, 50% reinvestment (**6.6x** cap / **11.7x** FDV on burn cash flow) |
| Q3 | "89% of SOL trading" | 89% = launchpad-sector share (80–92%+ of launches/fees); 28% = $PUMP's share of the top-traded leaderboard | arbiters ranked: fee-account inflows → aggregate DEX volume (Jupiter routing) → unique-trader counts |
| Q4 | 23-buy/61-sell print is routine profit-taking | cannot be classified from counts alone; lead-lag is **CEX deposits → PumpSwap LP removals → burn-wallet inflows** | burn inflows are *"an entirely mechanical downstream output"* — a lagging metric, not an early warning |

Two honest limits in the answers themselves, left in rather than smoothed over:

- On Q1 REX never addresses the second half of my question — it treats the whole $839.6K/day
  as open-market buybacks and does not net out treasury-funded burns, so 15.32% stays an
  upper bound rather than a settled figure.
- On Q2 it answers the multiple but gives decay as three named drivers plus a Gordon-growth
  identity, not as a single calibrated decay rate; the −4.7%/−9.7% range in `checks.py` is the
  boundary implied by the 6.53x price/buyback multiple, which REX's answer is consistent with.

The questions are written so that they stand on their own as analysis: each states the
conflict, the arithmetic that resolves it, and the observable that would settle it.

---

## Reproduction

1. `https://www.raptorx.trade` → account **Dragon9194** → RexScreener → Solana → Pump → **Full Report** (21:45 UTC).
2. Same panel → type each question into *"Ask any follow-up questions!"* → Enter.
3. Thread: Rex Pilot → PUMP (Pump) → *Report History* to re-open.
