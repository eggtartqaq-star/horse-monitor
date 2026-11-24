# V6.6 — 用你真正嘅 V6.4.2 代碼,以「你實際點交易」嘅方式量度

**唔係新策略。V6.4.2 嘅訊號規則一個數都冇改。**
今次做嘅係:用真代碼(唔係由 PDF 還原嗰版)喺真數據上,模擬你真正嘅執行方式。

---

## 檔案

| 檔案 | 做咩 |
|---|---|
| `rules_v642.py` | 由你 2026-11-24 交嘅 `dual_engine_v6_4.py` 逐行搬過嚟嘅規則(評分、止蝕、止盈、分流、倉位) |
| `indicators.py` | 指標(RSI/ADX/ATR/OBV),純 pandas,照 `ta` 嘅寫法 |
| `lab.py` | 回測實驗室:組合層、聽日開市成交、1%偏離重計、成本、月熔斷、拆股還原、IS/OOS、敏感度 |
| `parity_check.py` | **喺你部電腦跑**:對比 `ta` 版同呢度嘅指標/訊號。一致率 ≥99% 先信 V6.6 結果 |
| `selftest.py` | 合成數據自我測試,唔使上網 |
| `results/` | 2026-11-24 用 Webull 數據跑出嚟嘅結果 |

## 點行(你部電腦)

```cmd
cd 你放 V6.6 嘅資料夾
python selftest.py                    REM 1. 確認模擬器冇 bug
copy dual_engine_v6_4.py .            REM 2. parity_check 要 import 你嘅真引擎
python parity_check.py                REM 3. 確認指標同你每日用嘅一致
python lab.py --source yf             REM 4. A/B 實驗(約1分鐘)
python lab.py --source yf --mode sens REM 5. 每個鎖死參數 ±20%
python lab.py --source yf --mode caps REM 6. 名義上限 × 持倉數取捨
```

## 三種量度,點解數字差咁遠

| 模式 | 假設 | 用途 |
|---|---|---|
| `as_tested` | 收市判斷 + 同一收市價成交 + 零成本 + 冇倉位上限 | 對返你舊 OOS 數字 |
| `per_trade` | 聽日開市成交 + 偏離>1%重計 + 10bp/邊 | 每筆優勢嘅誠實估計 |
| `as_traded` | 上面全部 + 最多2倉 + 名義≤10% + 整數股 + 月熔斷 + HK$10,000 | **你真正會拎到嘅結果** |

## 已修正

1. **V6.5 走樣**:V6.5 `mr_target()` 先揀最近目標再檢查 R≥2;真 V6.4.2 係先篩 R≥2 再揀最近。
   V6.5 會錯拒「MA50 太近、60日高合格」嘅交易。`selftest.py` 有測試。
2. **倉位 bug(Tom 搵到)**:買唔起嘅訊號會霸住一個倉位一晚,令買得起嘅訊號被拒。已修正。
3. **拆股**:歷史價係拆股調整過(WMT 2023 年顯示 ~$48,其實 ~$145)。
   名義上限同「買唔買得起」要用當時真實股價 —— `lab.py` 嘅 `SPLITS` 表已還原。
   Tom 補咗 MSTR(2024-08-08,10拆1)。★ 2026 年 6 月之後嘅拆股要自己加入呢張表。

## 已測試、**唔採納**(手冊第十二節:兩段都要好先採納)

| 假設 | 結果 |
|---|---|
| A1 只做引擎二(引擎一 OOS 弱,唔好佔倉位) | 年化 0.25% / −0.28%(基準 1.82% / 2.62%),兩段都差 → 否決 |
| A2 引擎二只做126日動能前50%(動能池嘅縮細版) | 年化 1.37% / 2.30%,兩段都差 → 否決 |

## ★ 最重要:你每日用嘅掃描器同驗證過嘅系統唔一樣(Tom F-3)

手冊第三節引擎二入場條件第3條:「當日最高價 ≥ 20日高位(突破觸發)」。
所有回測(`run_trend_backtest`、`oos_validation`、`momentum_pit`)都有呢條。
但 `daily_strong_signals.py`(第124–137行)同 `dual_engine_v6_4.run_scan()` **冇**。
即係「OOS畢業」嗰個引擎二,唔係你每日掃描出嚟嗰個。

**修正(還原手冊規則,唔係優化)** —— 兩個掃描器入面,引擎二嗰句改做:

```python
if sc >= TREND_SCORE_MIN and plan and row["High"] >= row["high_20d"]:
```

`lab.py` 兩個版本都量咗:`AS_TRADED`(回測版)同 `SCANNER`(掃描器版)。

## 名義上限 —— 未改(要 Owner + CRO 決定)

修正咗 Tom 搵到嘅倉位 bug 之後,證據係「近兩年(2025–26)10% 上限多數蝕錢,之前唔清楚」,
唔係第一版講嘅「兩段都最差」。CRO 裁決見 `reports/risk/2026-11-24-swing-notional-cap-cro.md`。

## 建議加入你每日掃描嘅版本印章(唔影響任何訊號)

9月嘅截圖顯示 CVX(US$209)同 PFE 8股(US$229)出現喺掃描 —— 即係嗰陣跑緊 V6.4.2 之前嘅版本。
喺 `daily_strong_signals.py` 開頭加:

```python
import dual_engine_v6_4 as E
print(f"版本檢查: 名義上限={E.MAX_POSITION_PCT}%  引擎二止蝕上限={E.MAX_STOP_PCT_TREND}%  "
      f"資金=HKD{E.ACCOUNT_HKD:,}")
assert E.MAX_POSITION_PCT == 10.0, "★ 你跑緊舊版 dual_engine_v6_4.py!"
```

*研究同決策支援,唔係投資建議。冇任何 agent 會落單。*
