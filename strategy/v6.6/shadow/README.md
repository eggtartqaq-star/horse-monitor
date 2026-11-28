# 雲端影子記錄(shadow log)

**係咩:** 每個美股交易日收市後,雲端用 **Webull 唯讀日線** 跑一次同你部電腦一樣嘅 V6.6.9 掃描,記低「系統會做咩」。
呢個係研究記錄,**唔係落單訊息**:AI 唔會落單,亦唔會傳 Telegram。

**用途:**
1. **前向證據。** 回測以外,呢個係唯一嘅樣本外記錄。
2. **對照數據源。** 你嘅 Telegram 用 Yahoo 數據,呢度用 Webull。同一日兩邊嘅訊號、限價、止蝕應該一樣;唔一樣就話 AI 知。

## 檔案

| 檔案 | 內容 |
|---|---|
| `shadow_log.csv` | 每個收市日一行:牛 / 熊、SPY 對 200 日平均、交易清單(股、引擎、股數、限價上限、止蝕) |
| `YYYY-MM-DD.txt` | 當日完整訊息(同 Telegram 格式一樣,頂行標明「雲端影子記錄」) |
| `ledger/` | 影子記錄簿(signals、runs)。**唔係你嘅 `ledger/`**:程式會拒絕寫入你嘅記錄簿。 |

## 同你 Telegram 唔同嘅地方

- **財報檢查:off。** 雲端冇 Yahoo,所以影子清單可能包括你 Telegram 因為財報而擋咗嘅股。
- **數據:** Webull 日線已調整拆股,同 `data/` 重疊嘅日子完全一樣(2026-11-27 檢查)。

## 點樣跑

- **人手跑:** `python shadow_run.py --webull-json 檔1 檔2 檔3`(Webull `get_stock_bars` 嘅結果)。
  也可以 `--data CSV資料夾`。
- **自我審計:** 程式自己個源碼入面有傳訊息、讀 token 或者落單嘅呼叫,就拒絕執行(exit 2)。2026-11-27 測試過。
- **排程(雲端定時工作):** 「V6.6 cloud shadow log (Webull read-only)」,ID `trig_01SyUEo4RbQgSLndoGEqjRxa`。
  - 星期二至六,香港時間朝早 7:10;用「horse-monitor」環境。
  - **而家暫停。** 呢個組織唔准 AI 幫定時工作加 Webull 連接器,冇咗佢,每次都只會報「Webull not available」。

## 要重新開:你要做一步

1. 喺 claude.ai 開「Scheduled tasks」(定時工作)。
2. 揀「V6.6 cloud shadow log (Webull read-only)」。
3. 加 **Webull** 連接器。
4. 話 AI 知。AI 會開返佢,即刻試跑一次,確認有記錄寫入。

## 記錄

- 2026-11-25(第一次,人手跑):熊市,SPY 對 200 日平均 −1.93%,冇交易清單。
