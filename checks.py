#!/usr/bin/env python3
"""Recompute every number quoted in the four RaptorX questions.

All inputs are taken verbatim from the RaptorX PUMP report (report/pump-report.md,
section 6 Coin-O-Metry and the community-quote figures it cites).

Run:  python3 checks.py
"""
from decimal import Decimal as D

# --- inputs from the report ---------------------------------------------------
price = D("0.00433265")          # CoinGecko price
mcap = D("1999074975")           # CoinGecko market cap
fdv = D("3582279643")            # CoinGecko fully diluted valuation
circ = D("460733934469.21")      # circulating supply
total = D("825620756998.18")     # total supply
maxs = D("1000000000000")        # max supply
tvl = D("334049277")             # protocol TVL
vol_cg = D("146190000")          # CoinGecko aggregate 24h volume
vol_kol = D("452000000")         # @lbexplorer "daily trading volume"
vol_board = D("37590000")        # @solanaxscout PUMP row
vol_dex = D("3090000")           # DexScreener single pair
board_total = D("133500000")     # @solanaxscout leaderboard total
rev_day = D("1679200")           # @lbexplorer daily revenue
buyback = D("839600")            # @lbexplorer spend on buybacks
buys24, sells24 = 7960, 6892
buys5m, sells5m = 23, 61

def pct(x):
    return f"{x * 100:.2f}%"

print("=== 1. Volume triangulation via implied take rate ===")
for name, v in [("KOL $452M", vol_kol), ("CoinGecko $146.19M", vol_cg), ("Leaderboard $37.59M", vol_board), ("Single pair $3.09M", vol_dex)]:
    print(f"  {name:22s} implied take rate = {pct(rev_day / v)}")
print(f"  volume / market cap at $146.19M = {pct(vol_cg / mcap)}")
print(f"  volume / market cap at $452M     = {pct(vol_kol / mcap)}")
print(f"  buyback annualised              = ${buyback * 365 / 1_000_000:.1f}M")
print(f"  buyback yield on market cap     = {pct(buyback * 365 / mcap)}")
burn_tokens = maxs * D('0.0002')
print(f"  0.02% of max supply burned/day  = {float(burn_tokens) / 1e9:.1f}B PUMP = ${float(burn_tokens) * float(price) / 1e6:.2f}M at spot")
print(f"  annualised burn rate            = {pct(D('0.0002') * 365)} of max supply")

print("\n=== 2. TVL vs revenue as denominator ===")
rev_yr = float(rev_day) * 365
print(f"  annualised revenue   = ${rev_yr / 1e6:.1f}M")
print(f"  market cap / revenue = {float(mcap) / rev_yr:.2f}x")
print(f"  FDV / revenue        = {float(fdv) / rev_yr:.2f}x")
print(f"  market cap / TVL     = {float(mcap) / float(tvl):.2f}x")
print(f"  FDV / TVL            = {float(fdv) / float(tvl):.2f}x")

print("\n=== 3. Market-share claim ===")
print(f"  '89% of SOL trading' (KOL claim)      = 89.00%")
print(f"  PUMP share of leaderboard sample      = {pct(vol_board / board_total)}")
print(f"  gap between the two claims            = {89 - float(vol_board / board_total * 100):.1f} pp")

print("\n=== 4. Five-minute sell skew ===")
n = buys5m + sells5m
p = buys5m / n
import math
sd = math.sqrt(n * 0.25)
z = (buys5m - n / 2) / sd
print(f"  5m transactions            = {n}")
print(f"  5m buy ratio               = {pct(D(p))}")
print(f"  z-score vs balanced 50/50  = {z:.2f} sigma")
print(f"  24h buy ratio              = {pct(D(buys24 / (buys24 + sells24)))}")
print(f"  float / max supply         = {pct(circ / maxs)}")
print(f"  float / total supply       = {pct(circ / total)}")
