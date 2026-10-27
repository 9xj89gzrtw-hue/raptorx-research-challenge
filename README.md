# RaptorX Research Challenge — entry

**Asset:** PUMP (Pump.fun), Solana — `pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn`
**Report generated in RaptorX:** 2026-10-27 21:45 UTC (RexScreener → Solana → Pump → *Full Report*)
**Follow-up questions asked to REX AI:** 2026-10-27 21:46 UTC, 4 questions, same thread (`Rex Pilot → PUMP (Pump)`)
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
| `evidence/api-chat-response.json` | raw `POST /api/chat` response — see platform note below |
| `report/pump-report.md` | full text of the generated PUMP report (the artefact under questioning) |
| `report/jup-report.md` | full text of the earlier JUP report |
| `checks.py` / `checks.txt` | every number in Q1–Q4 recomputed from report inputs |

---

## Platform note (disclosed, not used as an excuse)

While this entry was being prepared, REX AI replies were unavailable for every prompt —
the chat endpoint returns HTTP 500 with an upstream provider error:

```
POST https://www.raptorx.trade/api/chat  ->  500
{"error":"Failed to process AI chat","details":"API error occurred: Status 403 Body:
 {\"error\":{\"message\":\"Key limit exceeded (total limit). ... $20.00 of $20.00 used;
 does not reset.\" ...}}"}
```

The same failure reproduced on the Claw AI 5.0 tab (question accepted, spinner ends, no
answer), so the questions are stored in the thread but no model answer exists to quote.
The full raw response is kept in `evidence/api-chat-response.json`. Report generation itself
worked normally throughout (PUMP report generated 21:45 UTC, JUP 21:22 UTC, SOL 21:35 UTC).

The questions are written so that they stand on their own as analysis: each states the
conflict, the arithmetic that resolves it, and the observable that would settle it.

---

## Reproduction

1. `https://www.raptorx.trade` → account **Dragon9194** → RexScreener → Solana → Pump → **Full Report** (21:45 UTC).
2. Same panel → type each question into *"Ask any follow-up questions!"* → Enter.
3. Thread: Rex Pilot → PUMP (Pump) → *Report History* to re-open.
