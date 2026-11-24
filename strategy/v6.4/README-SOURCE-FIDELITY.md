# ⚠ 呢個資料夾嘅代碼係「有損還原」,唔係原始檔案

**發現日期:2026-08-03。發現者:一個做評估用嘅基準 agent(冇用 audit skill 嗰個)。**

## 發生咗咩事

Owner 交嘅係 **5 個 PDF**,唔係 `.py` 檔案。CEO 用 PyMuPDF 抽文字還原成代碼。
但 PDF 本身喺右邊界**截斷咗**代碼 —— 超過大約第 80 個字元嘅字根本冇 render 出嚟。

驗證過:PDF 頁面闊 612pt,最右邊嘅文字去到 544pt,**冇任何文字喺頁面範圍外**。
即係啲字元喺造 PDF 嗰陣就已經冇咗,唔係抽取方法嘅問題 —— **喺呢啲 PDF 度救唔返**。

後果:**呢個資料夾入面四個 `.py` 檔案全部 parse 唔到。**

```
daily_strong_signals.py    SyntaxError: unterminated string literal (line 40)
momentum_pit_backtest.py   SyntaxError: unterminated string literal (line 73)
oos_validation.py          SyntaxError: unterminated string literal (line 304)
telegram_swing_bot.py      SyntaxError: unterminated string literal (line 79)
```

例子(`oos_validation.py`,兩行都斷咗尾):

```python
adx_ind = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window=14   ← 冇 )
atr = ta.volatility.AverageTrueRange(df["High"], df["Low"], df["Close"], wind   ← 斷咗
```

**Owner 部機上面嘅原始代碼好可能完全正常。** 壞咗嘅係還原版本,唔係佢寫嘅嘢。

## 咁之前嗰啲審計仲算唔算數?

分開兩類講,唔好一竹篙打一船人。

### 仍然成立 —— 證據喺冇被截斷嘅文字入面直接見到

| 發現 | 證據 | 狀態 |
|---|---|---|
| F-01 生存者偏差:個池係「今日」嘅標普500 | `momentum_pit_backtest.py:73` 個 URL 睇得一清二楚 | ✅ 成立 |
| F-02 Pine 同 Python 揀唔同止盈目標 | Python `oos_validation.py:211` `target = min(valid, ...)` vs Pine `:66` `high60 > close ? high60 : ...` —— 兩行都完整 | ✅ 成立 |
| F-03 `COOLDOWN = 10` 宣告咗冇用過 | `oos_validation.py:49` 宣告完整;「冇用過」係全檔搜尋結果 | ✅ 成立 |
| F-04 邊界截斷丟失未平倉 | `oos_validation.py:246` 連廣東話註釋「OOS邊界:未平倉交易棄掉」都完整 | ✅ 成立 |
| F-05 零成本模型 | 5 個檔 1,660 行完全搵唔到 commission/slippage/spread/fee | ✅ 成立 * |
| D-02 冇計過任何回撤 | 同上,全檔搜尋 | ✅ 成立 * |
| D-01 Pine 只實作引擎一 | 成個檔案結構,唔係單行 | ✅ 成立 |

\* 呢兩個係「不存在」嘅結論。理論上一個 cost 詞可以啱啱好每次都出現喺第 80 字元之後
而被截走 —— 但要喺 1,660 行入面每一個實例都咁,唔合理。**當佢成立,但唔係鐵證。**

### 需要用真檔案重驗

- **任何引用行號嘅嘢** —— 行號係還原版嘅,唔一定同原檔對得上。
- **任何關於長行尾段嘅結論** —— 嗰啲字根本冇喺度。
- **Tom 數過嘅 ~20 個手調門檻** —— 部分條件可能被截,數目可能唔準。
- **成本計算嘅倉位大細** —— 用 Owner 自己講嘅戶口參數計,唔係從代碼抽,所以唔受影響。

## 要點樣先修好

**Owner:直接畀返 `.py` 同 `.pine` 原始檔案**(用 zip、gist、或者直接 commit 上 repo),
唔好用 PDF。PDF 睇得,但 parse 唔到,亦都跑唔到。

有咗真檔案之後:

```bash
python3 .claude/skills/backtest-audit/scripts/scan_backtest.py strategy/v6.4
```

再對返上面張表,睇下有冇結論要改。

## 教訓

CEO 由 PDF 抽完代碼,冇跑過 `ast.parse()` 就當佢係代碼嚟審。
**一個 syntax check 就會即刻捉到 —— 成本係一秒。**

呢個同 L-005(「commit message 唔等於檔案存在」)係同一種病:
**冇驗證就當成功**。已記錄為 L-006。

諷刺嘅係:呢個發現嚟自一個**冇用 audit skill** 嘅基準 agent。
評估嘅意義就喺呢度 —— 唔係證明個 skill 叻,係搵出邊度有錯。
