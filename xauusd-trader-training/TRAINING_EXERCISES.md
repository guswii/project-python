# XAUUSD Trading AI Agent — Training Exercises

Latihan progresif untuk melatih AI agent supaya paham **SMC + ICT methodology** untuk trading XAUUSD (Gold).

**Total: 8 modul × latihan, ~15 minggu** (1-2 minggu per modul)

> **Catatan:** File ini hanya kumpulan latihan. Untuk theory lengkap + PRD + behavior contract, lihat repo lain atau dokumentasi original.

---

## 📚 Module Overview

| # | Module | Topik | Latihan |
|---|--------|-------|---------|
| 1 | SMC Vocabulary | Liquidity, OB, FVG, BOS, CHoCH | 5 latihan |
| 2 | ICT Framework | IPDA, AMD, Kill Zones, Silver Bullet | 4 latihan |
| 3 | Multi-TF Analysis | Daily → 4H → 1H → 15M cascade | 3 latihan |
| 4 | XAUUSD Specifics | DXY correlation, volatility, news | 3 latihan |
| 5 | Validation & Risk | 12-point checklist, R:R, position size | 4 latihan |
| 6 | Journaling | Format jurnal, weekly review | 3 latihan |
| 7 | AI Co-Pilot | Prompt engineering, refusal patterns | 3 latihan |
| 8 | Live Application | Daily/weekly routine, edge measurement | 3 latihan |

---

# Modul 1: SMC Vocabulary

**Tujuan:** Agent bisa identify setiap konsep SMC di chart XAUUSD.

## Latihan 1.1 — Liquidity Pools

**Setup:** Buka 30 historical XAUUSD chart di timeframe Daily / 4H.

**Tugas:**
- Mark semua BSL (Buy-Side Liquidity) di atas swing high
- Mark semua SSL (Sell-Side Liquidity) di bawah swing low
- Identifikasi equal highs / equal lows (clusters)
- Tandai ERL (di luar range) vs IRL (di dalam range)

**Pass criteria:** Bisa mark 25+ BSL/SSL dengan benar.

**Quiz (5 pertanyaan):**
1. Apa beda BSL vs SSL?
2. Di mana equal highs biasanya jadi BSL?
3. Liquidity pool untuk retail trader stop loss di atas swing high namanya apa?
4. Apa beda ERL vs IRL?
5. Kenapa institusi tertarik ke liquidity pool?

**Expected answers:**
1. BSL = Buy-Side Liquidity (di atas swing high, stop loss卖家), SSL = Sell-Side Liquidity (di bawah swing low, stop loss买家)
2. Equal highs = swing high yang levelnya sama, jadi cluster BSL
3. BSL (Buy-Side Liquidity)
4. ERL = External Range Liquidity (di luar range, biasanya swing high/low utama); IRL = Internal Range Liquidity (di dalam range, seperti FVG atau OB)
5. Counterparty volume — institusi butuh lawan untuk fill large order, dan stop loss cluster = volume

## Latihan 1.2 — Order Blocks

**Setup:** 50 XAUUSD charts (mix 4H + 1H).

**Tugas:**
- Identify bullish OB (last down candle before strong up impulse)
- Identify bearish OB (last up candle before strong down impulse)
- Untuk setiap OB, cek: apakah ada strong displacement + BOS setelahnya?
- Valid vs invalid OB — apa yang membedakannya?

**Pass criteria:** Bisa identify 40+ valid OB.

**Quiz:**
1. Bullish OB = last candle apa sebelum impulse up?
2. 3 kondisi valid OB apa?
3. Kalau price break through OB tanpa reaksi, OB itu valid atau invalid?
4. Zone bullish OB diukur dari mana ke mana?
5. BOS apa yang harus confirm OB?

**Expected answers:**
1. Last **down** (bearish) candle
2. (a) Last opposing candle, (b) Strong impulse/displacement setelahnya, (c) BOS confirming direction
3. Invalid — OB sudah broken
4. Dari **open** candle ke **low** candle
5. BOS yang sesuai arah OB (bullish OB → bullish BOS untuk confirmation)

## Latihan 1.3 — Fair Value Gap (FVG)

**Setup:** 50+ XAUUSD charts.

**Tugas:**
- Mark semua 3-candle pattern dimana wick candle 1 & 3 gak overlap
- Identifikasi bullish FVG (gap up) vs bearish FVG (gap down)
- Track mana yang ke-mitigate (filled) vs yang masih unmitigated
- Timeframe cascade: daily FVG > 4H FVG > 1H FVG > 15M FVG (weight)

**Pass criteria:** Bisa mark 45+ FVG.

**Quiz:**
1. Apa beda FVG dengan gap biasa?
2. Bullish FVG diukur dari mana ke mana?
3. Apa yang terjadi kalau FVG sudah ke-mitigate?
4. FVG di timeframe mana yang paling reliable?
5. Kapan FVG biasanya jadi entry zone?

**Expected answers:**
1. FVG = 3-candle pattern dimana middle candle terlalu agresif sampai wick candle 1 & 3 gak overlap. Biasa = gap yang memang gak ke-trade. FVG itu inefficiency, price cenderung revisit.
2. Wick candle 1.high → candle 3.low (lower bound of gap)
3. Filled — sudah ke-retrace, kemungkinan besar gak jadi area reaction lagi
4. Higher timeframe (Daily > 4H > 1H > 15M). Daily FVG weight-nya paling kuat.
5. Entry zone: tunggu price retrace ke 50% FVG (the equilibrium of the gap), terus cari LTF confirmation (CHoCH, displacement)

## Latihan 1.4 — Market Structure (BOS vs CHoCH)

**Setup:** 20 XAUUSD 4H charts.

**Tugas:**
- Untuk setiap chart: tentukan bullish atau bearish structure
- Mark semua HH/HL (bullish) atau LH/LL (bearish)
- Identifikasi setiap BOS (continuation)
- Identifikasi setiap CHoCH atau MSS (reversal)

**Pass criteria:** Bisa klasifikasikan 18+ structures dengan benar.

**Quiz:**
1. Bullish structure = apa?
2. BOS continuation di bullish structure: price break apa?
3. CHoCH di uptrend: price break apa?
4. Apa beda CHoCH vs MSS?
5. Timeframe mana yang BOS-nya paling signifikan?

**Expected answers:**
1. Higher Highs (HH) + Higher Lows (HL)
2. Break last swing high (in direction of trend)
3. Break last higher low (against prevailing trend) — first warning of reversal
4. MSS = stronger CHoCH, dengan displacement candle & stronger momentum
5. Higher TF — Daily BOS > 4H BOS > 1H BOS (significance)

## Latihan 1.5 — Premium/Discount & OTE

**Setup:** 30 XAUUSD ranges (between swing high & low).

**Tugas:**
- Untuk setiap range: hitung 50% equilibrium
- Identifikasi zona premium (above 50%) vs discount (below 50%)
- Mark OTE zone (62-79% Fibonacci retracement)
- Tentukan: di discount = look for buy, di premium = look for sell

**Pass criteria:** 25+ zones correct.

**Quiz:**
1. Above 50% = apa?
2. OTE zone diukur dari mana?
3. Kalau harga di discount, look for apa?
4. Fibonacci mana yang jadi OTE entry sweet spot?
5. Kenapa entry di OTE lebih baik dari random entry?

**Expected answers:**
1. Premium (sell zone)
2. 62-79% retracement of expansion leg (atau 61.8-76.4% classic)
3. Look for buy (long)
4. 62-79% (atau 61.8% - 76.4%)
5. Di OTE = institutional re-entry zone, risk:reward lebih bagus karena dekat dengan invalidation (swing low/high) tapi target jauh (DOL = HTF liquidity)

---

# Modul 2: ICT Framework

**Tujuan:** Paham ICT-exclusive concepts & kill zone timing.

## Latihan 2.1 — IPDA & 4 Market Phases

**Setup:** 10 XAUUSD daily charts.

**Tugas:**
- Identifikasi 4 phase: Expansion, Retracement, Reversal, Consolidation
- Tandai transisi antar phase
- Setiap phase: cari OB/FVG/liquidity pool yang relevan

**Quiz:**
1. 4 phase ICT apa?
2. Phase mana yang jadi entry zone terbaik?
3. Consolidation biasanya di session mana?
4. Expansion identik dengan apa?
5. Reversal phase: apa yang harus di-confirm?

**Expected answers:**
1. Expansion, Retracement, Reversal, Consolidation
2. Retracement ke OB/FVG HTF (setelah expansion move)
3. Asian session (low volume, range)
4. Displacement candle / strong move
5. CHoCH atau MSS di lower timeframe

## Latihan 2.2 — Power of 3 (AMD)

**Setup:** 20 XAUUSD intraday charts (15M-1H).

**Tugas:**
- Untuk setiap chart: identifikasi Accumulation, Manipulation, Distribution
- Tandai Judas Swing di phase Manipulation
- Cek: harga di distribution bergerak ke arah bias HTF?

**Quiz:**
1. 3 phase Power of 3 apa?
2. Phase mana yang **bukan** tradable?
3. Manipulation identik dengan apa?
4. Accumulation biasanya kapan?
5. Setelah distribution, fase apa selanjutnya?

**Expected answers:**
1. Accumulation, Manipulation, Distribution
2. Accumulation (preparation) & Manipulation (trap)
3. Judas Swing (false move untuk trap retail)
4. Asian session / pre-market (low volume, range)
5. Bisa Expansion lagi, atau Consolidation (kalau exhausted)

## Latihan 2.3 — Kill Zone Observation (5 Hari)

**Setup:** Live trading 5 hari.

**Tugas:**
- Catat XAUUSD behavior di setiap kill zone:
  - Asian (08:00-12:00 WIB)
  - London (14:00-17:00 WIB)
  - NY AM (19:00-22:00 WIB)
  - NY Lunch (00:00-01:30 WIB)
  - NY PM (01:30-04:00 WIB)
- Note: range size, volume, momentum direction, fakeout frequency
- Conclusion: session mana yang terbaik untuk XAUUSD?

**Pass criteria:** 5 hari observasi lengkap.

**Expected findings:**
- Asian: range sempit, low volume, sering fakeout
- London: range melebar, sering jadi manipulation phase
- NY AM: best for continuation, big moves
- NY Lunch: choppy, hindari
- NY PM: secondary, reversal opportunity

## Latihan 2.4 — Silver Bullet Setup

**Setup:** 30 historical Silver Bullet windows (22:00-23:00 WIB).

**Tugas:**
- Identifikasi morning impulse + FVG
- Cek: apakah price retrace ke FVG di 22:00-23:00 WIB?
- Track win rate kalau entry di 50% FVG dengan SL beyond FVG

**Pass criteria:** Track 20+ setups, identify win rate.

---

# Modul 3: Multi-Timeframe Analysis

## Latihan 3.1 — MTF Cascade (30 Charts)

**Setup:** 30 XAUUSD charts.

**Tugas:** Untuk setiap chart:
1. Daily → tentukan bias
2. 4H → confirm, mark primary OB/FVG
3. 1H → BOS/CHoCH?
4. 15M → CHoCH + entry zone?

**Output format:**
```
Chart #X
- Daily bias: [bullish/bearish]
- 4H primary zone: [OB/FVG, level]
- 1H confirmation: [BOS/CHoCH, level]
- 15M entry: [FVG 50% / OB]
- Trade?: [yes/no, why]
```

## Latihan 3.2 — MTF Confluence Scoring

**Setup:** 30 XAUUSD setups.

**Tugas:** Apply scoring system (max 8 confluence points):
- +1 HTF support (Daily + 4H aligned)
- +1 BOS/CHoCH aligned across TFs
- +1 Sweep + reversal di LTF
- +1 Kill zone timing
- +1 HTF OB/FVG sebagai POI
- +1 Displacement candle
- +1 1:3+ R:R
- +1 News confirming bias

**Grade:** A (7-8), B (5-6), C (3-4), Skip (<3)

## Latihan 3.3 — Common MTF Mistakes

**Tugas:** Dari 20 trade history, identifikasi:
- Berapa yang trade LTF tanpa HTF bias?
- Berapa yang skip step cascade?
- Berapa yang counter-trend?

**Lesson:** Filter = quality. Skip > 50% setups.

---

# Modul 4: XAUUSD-Specific Behavior

## Latihan 4.1 — DXY Correlation

**Setup:** Plot XAUUSD vs DXY 6 bulan terakhir.

**Tugas:**
- Hitung correlation coefficient
- Identifikasi episode divergence (XAUUSD naik sementara DXY juga naik)
- Note news events yang cause divergence

**Expected:** Correlation -0.7 to -0.9 typical, divergence = rare & important

## Latihan 4.2 — News Event Impact

**Setup:** 10 high-impact news releases (CPI, FOMC, NFP).

**Tugas:**
- Mark harga 15 menit sebelum & sesudah release
- Hitung range (pips) per event
- Conclusion: volatility pattern per event

**Expected:**
- CPI: 200-400 pips range dalam 1 jam pertama
- FOMC: 300-600 pips, bisa trending atau whipsaw
- NFP: 200-500 pips

## Latihan 4.3 — Round Number Psychology

**Setup:** Mark $1900, $1950, $2000, $2050, $2100 di historical charts.

**Tugas:**
- Track reaction di setiap round number
- Note: lebih sering bounce atau break?

**Expected:** Round numbers = psychological levels, sering jadi reaction zones. Tapi gak 100% reliable.

---

# Modul 5: Validation & Risk Management

## Latihan 5.1 — Apply 12-Point Checklist

**Setup:** 30 user-presented XAUUSD setups.

**Tugas:** Apply checklist:
```
HTF Analysis:
□ 1. HTF bias confirmed?
□ 2. DOL identified?

Timing:
□ 3. Kill zone respected?
□ 4. No high-impact news?

Price Action:
□ 5. Liquidity sweep occurred?
□ 6. CHoCH on LTF confirmed?
□ 7. Displacement candle present?
□ 8. FVG/OB on LTF identified?

Execution:
□ 9. Entry at FVG 50% / OB?
□ 10. SL beyond sweep wick?
□ 11. R:R minimum 1:2?
□ 12. Position size calculated?

Grade: A (11-12) / B (9-10) / C (7-8) / Invalid (<7)
```

**Output:** Grade per setup + reasoning.

## Latihan 5.2 — Position Sizing Calculator

**5 scenarios:**

| Scenario | Account | Risk% | SL (pips) | Pip Value | Position Size |
|----------|---------|-------|-----------|-----------|---------------|
| 1 | $10,000 | 1% | 50 | $1 | ? |
| 2 | $5,000 | 2% | 30 | $1 | ? |
| 3 | $25,000 | 1% | 100 | $1 | ? |
| 4 | $2,000 | 0.5% | 25 | $1 | ? |
| 5 | $50,000 | 1.5% | 75 | $1 | ? |

**Formula:** Lot = (Account × Risk%) / (SL × Pip Value)

**Expected answers:**
1. ($10,000 × 0.01) / (50 × $1) = 0.2 lot (mini)
2. ($5,000 × 0.02) / (30 × $1) = 0.33 lot
3. ($25,000 × 0.01) / (100 × $1) = 0.25 lot
4. ($2,000 × 0.005) / (25 × $1) = 0.04 lot (micro)
5. ($50,000 × 0.015) / (75 × $1) = 0.1 lot

## Latihan 5.3 — R:R Filter

**Setup:** 20 setups dengan berbagai R:R.

**Tugas:** Tentukan mana yang layak trade (R:R ≥ 1:2).

| Setup | Entry | SL | TP | R:R | Trade? |
|-------|-------|----|----|-----|--------|
| 1 | 2000 | 1990 | 2030 | 1:3 | ? |
| 2 | 2000 | 1990 | 2010 | 1:1 | ? |
| 3 | 2000 | 1980 | 2060 | 1:3 | ? |
| 4 | 2000 | 1995 | 2015 | 1:1.5 | ? |
| 5 | 2000 | 1985 | 2060 | 1:4 | ? |

**Expected:**
1. 1:3 → Trade
2. 1:1 → Skip
3. 1:3 (SL 20, TP 60) → Trade
4. 1:1.5 → Skip (under 1:2)
5. 1:4 → Strong trade

## Latihan 5.4 — Trade Management Rules

**Tugas:** Kapan move SL ke BE? Close sebagian di TP1 vs TP2?

**Rules:**
- Move SL ke BE setelah TP1 hit (50% position closed)
- TP2 = close 30% lagi, trail remaining
- TP3 = final target (HTF liquidity)

**Latihan:** Apply ke 10 historical trades.

---

# Modul 6: Trade Journaling

## Latihan 6.1 — Journal 5 Sample Trades

**Format:**
```
TRADE JOURNAL ENTRY
━━━━━━━━━━━━━━━━━━━━
Date: YYYY-MM-DD
Asset: XAUUSD
Direction: Buy / Sell
HTF Bias: Bullish / Bearish
Kill Zone: London / NY AM / etc
Setup Grade: A / B / C / Invalid

Entry:
- Time: HH:MM
- Price: X.XXX
- Trigger: [FVG fill / OB reaction / etc]
- Confluence: [List factors]

Risk:
- SL: X.XXX (X pips)
- TP1: X.XXX (1:X R:R)
- TP2: X.XXX (1:X R:R)
- TP3: X.XXX (1:X R:R)
- Position size: X lot
- Risk amount: $X

Exit:
- Time: HH:MM
- Price: X.XXX
- Closed at: TP1 / TP2 / TP3 / SL / Manual
- P/L: +X pips / -X% / +X%

Review:
- What went well: [2-3 poin]
- What to improve: [2-3 poin]
- Concept gap: [SMC/ICT missed]
- Notes: [free text]
```

## Latihan 6.2 — Pattern Recognition (10 Trades)

**Tugas:** Dari 10 trade history:
- Losing streak pattern? (overtrading setelah loss?)
- Best session? (highest win rate)
- Best setup type? (A vs B vs C grade)
- Common mistake? (skip checklist, wrong kill zone, etc)

## Latihan 6.3 — Weekly Review Template

```
WEEKLY REVIEW - Week [N]
━━━━━━━━━━━━━━━━━━━━
Total trades: X
Win: X (X%)
Loss: X (X%)
Net P/L: +X pips / -X% / +X%
Avg R:R: 1:X

Best trade: [link/screenshot]
Worst trade: [link/screenshot]

Patterns observed:
- [Pattern 1]
- [Pattern 2]

Action items next week:
- [Action 1]
- [Action 2]

Discipline score: X/10
```

---

# Modul 7: AI Co-Pilot Skills

## Latihan 7.1 — Setup Presentation Format

**Tugas:** User harus bisa present setup dengan format standard:
```
Setup gw:
- HTF bias: [Daily 4H aligned]
- Time: [HH:MM, session]
- DOL: [target liquidity]
- Liquidity swept: [BSL/SSL level]
- CHoCH di: [LTF timeframe]
- Displacement: [ya/tidak, description]
- FVG/OB: [zona, level]
- Entry plan: [price zone]
- SL: [price + pips]
- TP1/2/3: [prices + R:R]
- Risk: 1% / 2%
- News: [ada/tidak]
```

**Latihan:** Latih 20 setup dengan format ini.

## Latihan 7.2 — Agent Response Patterns

**Tugas:** Agent harus bisa respond dengan format standard:

**Setup Review Format:**
```
📊 SETUP REVIEW
━━━━━━━━━━━━━━━━━━━━
Asset: XAUUSD
Timeframe: [user's]
HTF Bias: [bullish/bearish]
DOL: [target liquidity]

✅ Checklist (X/12):
[List setiap poin + status]

📈 Grade: [A/B/C/INVALID]
💡 Rationale: [1-2 kalimat]
🎯 Entry Plan:
   - Entry: [price zone]
   - SL: [price + pips]
   - TP1/2/3: [prices + R:R]
⚠️ Risks: [2-3 hal]
❓ Questions: [kalau ada missing]
```

**Post-Trade Review Format:**
```
📋 TRADE REVIEW
━━━━━━━━━━━━━━━━━━━━
Trade: [buy/sell] XAUUSD
Entry: [time + price]
Exit: [time + price]
Result: [win/loss] (+X pips / -X%)

✅ What went well: [2-3 poin]
⚠️ What to improve: [2-3 poin]
📚 Concept gap: [SMC/ICT missed]
🎯 Next time: [action item]
```

## Latihan 7.3 — Refusal Scenarios

**5 scenarios untuk refusal training:**

1. User: "Kasih sinyal buy/sell dong"
   - Agent: "Gak bisa kasih naked signal. Present setup lo dulu, gw validate."

2. User: "Position size berapa?"
   - Agent: "Tergantung account size & risk tolerance lo. Risk 1-2% per trade standard."

3. User: "Pasti profit gak?"
   - Agent: "Gak ada yang pasti di trading. SMC/ICT probabilistic."

4. User: "Auto-trade dong"
   - Agent: "Gw gak konek ke broker. Lo eksekusi sendiri."

5. User: "Leverage berapa?"
   - Agent: "Tergantung broker & prop firm rules. Default 1:100 umum tapi risk 1-2% per trade."

**Latihan:** Drill 20 refusal scenarios sampai agent bisa respond gracefully.

---

# Modul 8: Live Application

## Latihan 8.1 — Daily Routine (1 Minggu)

**Setiap hari (5 hari), apply:**

```
PRE-MARKET (30 min before London):
- Mark Asian High/Low
- Identify HTF bias
- Mark key levels (PDH/PDL, OB, FVG)

LONDON SESSION:
- Watch for Judas Swing (early London)
- Look for setups dengan full confluence
- Apply 12-point checklist

NY AM:
- Same as London
- Watch Silver Bullet window (22:00-23:00 WIB)

POST-SESSION:
- Journal setiap trade (real-time)
- Update progress tracker
- Note patterns/insights
```

## Latihan 8.2 — Weekly Routine (4 Minggu)

**Setiap minggu (4 minggu):**

- **Sunday:** Plan week — news, levels, bias
- **Daily:** Trade + journal
- **Friday:** Weekly review + next week prep

**Track:**
- Win rate per week
- Total P/L
- Discipline score
- Improvement notes

## Latihan 8.3 — Edge Measurement (30 Hari)

**Tugas:** Trade live 30 hari dengan metrics:
- Win rate
- R:R average
- Profit factor (gross profit / gross loss)
- Sharpe ratio (advanced)
- Max drawdown

**Final Assessment:**
- 30 hari live trading
- Minimum 20 trades
- Win rate > 55%
- R:R > 1:2 average
- Journal completeness: 100%

---

# 📊 Final Quiz (Semua Modul)

**50 pertanyaan pilihan ganda, mix dari semua modul.**

Pass: ≥40/50 (80%)

Topik:
- 10 SMC vocabulary
- 10 ICT framework
- 10 Multi-timeframe
- 5 XAUUSD-specific
- 10 Validation & risk
- 5 Journaling & co-pilot

---

# 📚 Resources

### Buku
- "Trading in the Zone" — Mark Douglas
- "The Art and Science of Technical Analysis" — Adam Grimes

### YouTube
- ICT official
- Michael Huddleston
- Smarter Money (TTrades)

### Platform
- TradingView (charting)
- MT4/MT5 (execution)
- Forex Factory (calendar)
- Myfxbook / Edgewonk (journaling)

### Reference
- ICT official: theinnercircletraders.com
- Michael Huddleston notes: michaeljhuddleston.org
- Quantum Algo XAUUSD: quantum-algo.com/markets/gold

---

**END OF TRAINING EXERCISES**
**Total: 8 modul × latihan, ~15 minggu**
