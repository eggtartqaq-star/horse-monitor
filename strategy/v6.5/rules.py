# -*- coding: utf-8 -*-
"""
============================================================
V6.5 — 單一規則來源 (Single Source of Truth)
============================================================
點解要有呢個檔案:
  V6.4 嘅同一個規則喺唔同檔案有唔同數值 ——
    止蝕闊度上限: Pine 15% / bot 12% / 回測 12%
    COOLDOWN=10 喺 oos_validation.py 宣告咗但從來冇用過
  規則散落 = 你睇嘅圖同你測嘅引擎唔係同一個策略。

  由今日起:所有規則喺呢度定義一次。回測、掃描器、bot 全部 import 呢度。
  Pine 冇得 import Python,所以 PINE_PARITY 表要人手對 —— 但至少有一張表可以對。

★ 唔好喺其他檔案改呢啲數。改咗 = 要重跑驗證。
============================================================
"""
from dataclasses import dataclass, field, asdict


# ============================================================
# 指標 — 自己實作,唔用 `ta` library
# ============================================================
# 點解:`ta` 嘅版本一變,你嘅止蝕位就會靜靜雞變,唔會報錯。
# 呢個係 V6.4 審計findings之一(單一供應商 / 未鎖版本)。
# 全部用 Wilder smoothing,同 `ta` 預設一致。
# 注意:數值可能同 `ta` 有微細差異 —— 呢個係預期之內,而家至少係鎖死嘅。

import numpy as np
import pandas as pd


def _wilder(series: pd.Series, n: int) -> pd.Series:
    """Wilder 平滑 = EWM alpha=1/n。ta library 內部用同一個做法。"""
    return series.ewm(alpha=1.0 / n, adjust=False).mean()


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = _wilder(gain, n)
    avg_loss = _wilder(loss, n)
    rs = avg_gain / avg_loss.replace(0.0, np.nan)
    out = 100.0 - (100.0 / (1.0 + rs))
    # 邊界:avg_loss 為 0(連續升)→ RSI 100;avg_gain 為 0(連續跌)→ RSI 0
    out = out.where(avg_loss != 0.0, 100.0)
    out = out.where(~((avg_gain == 0.0) & (avg_loss != 0.0)), 0.0)
    return out


def true_range(df: pd.DataFrame) -> pd.Series:
    prev_close = df["Close"].shift(1)
    return pd.concat([
        df["High"] - df["Low"],
        (df["High"] - prev_close).abs(),
        (df["Low"] - prev_close).abs(),
    ], axis=1).max(axis=1)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    return _wilder(true_range(df), n)


def adx_di(df: pd.DataFrame, n: int = 14):
    """回傳 (adx, di_plus, di_minus)。Wilder 原版。"""
    up = df["High"].diff()
    down = -df["Low"].diff()
    plus_dm = ((up > down) & (up > 0)) * up.fillna(0.0)
    minus_dm = ((down > up) & (down > 0)) * down.fillna(0.0)

    tr_n = _wilder(true_range(df), n)
    plus_di = 100.0 * _wilder(plus_dm, n) / tr_n.replace(0.0, np.nan)
    minus_di = 100.0 * _wilder(minus_dm, n) / tr_n.replace(0.0, np.nan)

    dx = 100.0 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0.0, np.nan)
    return _wilder(dx.fillna(0.0), n), plus_di, minus_di


def obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    direction = np.sign(close.diff().fillna(0.0))
    return (direction * volume).cumsum()


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """V6.4 用到嘅全部指標。輸入要有 Open/High/Low/Close/Volume。"""
    df = df.copy()
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df["RSI14"] = rsi(df["Close"], 14)
    df["RSI2"] = rsi(df["Close"], 2)
    a, dp, dm = adx_di(df, 14)
    df["ADX"], df["DI_PLUS"], df["DI_MINUS"] = a, dp, dm
    df["ATR"] = atr(df, 14)
    df["price_vs_ma20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100
    df["ma20_vs_ma50"] = (df["MA20"] - df["MA50"]) / df["MA50"] * 100
    df["ret_5d"] = df["Close"].pct_change(5) * 100
    df["ret_10d"] = df["Close"].pct_change(10) * 100
    df["vol_ratio"] = df["Volume"].rolling(5).mean() / df["Volume"].rolling(20).mean()
    o = obv(df["Close"], df["Volume"])
    df["OBV"] = o
    df["OBV_Div"] = (df["Close"] < df["Close"].shift(5)) & (o > o.shift(5))
    df["low_10d"] = df["Low"].rolling(10).min()
    df["high_20d"] = df["High"].rolling(20).max()
    df["high_60d"] = df["High"].rolling(60).max()
    df["dist_60h"] = (df["high_60d"] - df["Close"]) / df["Close"] * 100
    df["mom_126"] = df["Close"].pct_change(126) * 100
    return df


# ============================================================
# 規則參數 — 改呢度 = 要重跑驗證
# ============================================================

@dataclass(frozen=True)
class EngineRules:
    # --- 引擎一:均值回歸 ---
    MR_SCORE_MIN: float = 0.55
    MR_MIN_R: float = 2.0
    MR_MAX_HOLD: int = 10
    MR_ATR_STOP_MULT: float = 2.0
    MR_STOP_WIDTH_MAX_PCT: float = 15.0   # ← V6.4 分歧點。見下面 NOTE_STOP_WIDTH。
    MR_COOLDOWN: int = 10                 # ← V6.4 宣告咗但冇實作。V6.5 真係執行。

    # --- 引擎二:趨勢 ---
    TREND_SCORE_MIN: float = 0.65
    TREND_ATR_TRAIL_MULT: float = 3.0
    TREND_MAX_HOLD: int = 60
    TREND_STOP_WIDTH_MAX_PCT: float = 12.0
    TREND_COOLDOWN: int = 0

    # --- 路由 / 環境 ---
    ADX_RANGE_MAX: float = 25.0           # < 呢個 → 引擎一
    ADX_TREND_MIN: float = 25.0           # >= 呢個 + DI+>DI- → 引擎二
    REGIME_MA: int = 200                  # SPY > MA200 先做多
    REGIME_LAG_BARS: int = 1              # ← 新增。見 NOTE_REGIME_LAG。

    # --- 投機股護欄 ---
    SPEC_LOOKBACK: int = 126
    SPEC_HIGH_LOW_MULT: float = 2.0

    # --- 動能池 ---
    MOMENTUM_LOOKBACK: int = 126
    MOMENTUM_TOP_N: int = 50


NOTE_STOP_WIDTH = """
V6.4 有四個唔同值:Pine 15% / bot trend_plan 12% / 兩個回測 12% /
bot 入面仲有一段永遠行唔到嘅 15% dead code。

John (CRO) 嘅裁決:
  - 引擎二 12% 係「已驗證」嘅 —— 兩個回測都用 12,live 亦係 12。保留。
  - 引擎一 15% 係「live 但未驗證」 —— run_engine1() 根本冇止蝕闊度過濾。
    即係回測入面包含咗 live 會拒絕嘅闊止蝕交易,而過濾後嗰批從來冇單獨量度過。
  - 所以 MR_STOP_WIDTH_MAX_PCT = 15.0 係暫定值,唔係已驗證值。
    ★ 用 portfolio_sim.py 重跑引擎一(加 15% 過濾)之後先可以當佢已驗證。
"""

NOTE_REGIME_LAG = """
V6.4: spy_bull = Close > MA200,而 MA200 包含當日收市價,入場亦係同日收市。
呢個只有喺你真係喺收市價成交先成立。

V6.5 預設 REGIME_LAG_BARS = 1 —— 用「尋日」嘅環境判斷今日可唔可以入場,
入場價用「聽日開市」。呢個組合完全冇前視偏差,任何人都執行得到。

★ 你可以設 0 去對比。如果 0 同 1 之間 EV 差好遠,即係你嘅優勢有一部分
  係嚟自同日資訊 —— 呢個係要知道嘅事。
"""

NOTE_PINE_PARITY = """
Pine 冇得 import 呢個檔案。以下係人手對照表,每次改規則都要同步。

| 規則              | rules.py                    | Pine 現況 (V6.4)        | 狀態      |
|-------------------|-----------------------------|-------------------------|-----------|
| 止蝕闊度上限 E1   | 15%                         | 15%                     | 一致      |
| 止蝕闊度上限 E2   | 12%                         | 冇實作(Pine 冇 E2)     | ★ 缺失    |
| 止盈目標選擇      | 最近嘅合格目標 (min)        | 優先 high60 (較遠)      | ★ 分歧    |
| Cooldown          | 10 日                       | 冇                      | ★ 分歧    |
| 引擎二            | 有                          | 冇                      | ★ 缺失    |

John: Pine 要麼實作引擎二,要麼改名講明佢淨係引擎一、淨係觀察用。
Tom: 用 golden-file test —— 導出 N 條歷史 bar 嘅 tier/stop/target/R,
     要求 Pine 重現。呢個係唯一令兩邊唔會再漂移嘅方法。
"""

RULES = EngineRules()


# ============================================================
# 評分 — 同 V6.4 完全一致(刻意唔改)
# ============================================================
# ★ 呢兩個函數係 V6.4 原版逐行搬過嚟,一個數都冇改。
#   點解:呢次升級係修正「量度方法」,唔係改策略。
#   如果連策略都改埋,你就分唔清 EV 變化係邊個原因造成。
#   要調呢啲門檻,等 portfolio_sim 有咗 baseline 之後先算。

def mr_score(row) -> float:
    score = 0.0
    rsi14 = row["RSI14"]
    if pd.notna(rsi14):
        if 35 <= rsi14 <= 45:   rs = 1.0
        elif 45 < rsi14 <= 55:  rs = 0.8
        elif 30 <= rsi14 < 35:  rs = 0.6
        elif 55 < rsi14 <= 65:  rs = 0.4
        elif rsi14 > 65:        rs = 0.1
        else:                   rs = 0.3
        score += rs * 0.20
    rsi2 = row["RSI2"]
    if pd.notna(rsi2):
        if rsi2 < 5:    r2 = 1.0
        elif rsi2 < 10: r2 = 0.85
        elif rsi2 < 20: r2 = 0.70
        elif rsi2 < 30: r2 = 0.50
        else:           r2 = 0.20
        score += r2 * 0.15
    pma20, ma_t = row["price_vs_ma20"], row["ma20_vs_ma50"]
    if pd.notna(pma20) and pd.notna(ma_t):
        if -5 <= pma20 <= 0 and ma_t > 0:    ss = 1.0
        elif -10 <= pma20 < -5 and ma_t > 0: ss = 0.8
        elif 0 < pma20 <= 3 and ma_t > 0:    ss = 0.7
        elif pma20 < -10 and ma_t > 0:       ss = 0.4
        else:                                ss = 0.2
        score += ss * 0.20
    ret10 = row["ret_10d"]
    if pd.notna(ret10):
        if -15 <= ret10 <= -5:   r3 = 1.0
        elif -20 <= ret10 < -15: r3 = 0.7
        elif -5 < ret10 <= -2:   r3 = 0.5
        elif ret10 > 0:          r3 = 0.1
        else:                    r3 = 0.3
        score += r3 * 0.20
    vr, ret5 = row["vol_ratio"], row["ret_5d"]
    if pd.notna(vr) and pd.notna(ret5):
        if ret5 < 0 and vr > 1.3:    vs = 1.0
        elif ret5 < 0 and vr > 1.1:  vs = 0.8
        elif ret5 < 0 and vr > 0.9:  vs = 0.5
        elif ret5 >= 0 and vr > 1.2: vs = 0.6
        else:                        vs = 0.2
        score += vs * 0.15
    if bool(row.get("OBV_Div", False)):
        score += 0.10
    return round(min(score, 1.0), 4)


def trend_score(row) -> float:
    score = 0.0
    adx = row["ADX"]
    ts = 0.0
    if pd.notna(adx):
        if adx >= 40:   ts = 1.0
        elif adx >= 30: ts = 0.85
        elif adx >= 25: ts = 0.6
    score += ts * 0.25
    ma = 0.3
    c, m20, m50, m200 = row["Close"], row["MA20"], row["MA50"], row["MA200"]
    if pd.notna(m20) and pd.notna(m50):
        if pd.notna(m200) and c > m20 > m50 > m200: ma = 1.0
        elif c > m20 > m50: ma = 0.8
        elif c > m20:       ma = 0.5
        else:               ma = 0.1
    score += ma * 0.25
    ph, d = 0.0, row["dist_60h"]
    if pd.notna(d):
        if d <= 1:    ph = 1.0
        elif d <= 3:  ph = 0.85
        elif d <= 5:  ph = 0.6
        elif d <= 10: ph = 0.35
        else:         ph = 0.1
    score += ph * 0.25
    vs, vr = 0.4, row["vol_ratio"]
    if pd.notna(vr):
        vs = 1.0 if vr > 1.2 else (0.7 if vr > 1.0 else 0.4)
    score += vs * 0.15
    if pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"]:
        score += 0.10
    return round(min(score, 1.0), 4)


def mr_target(row, rules: EngineRules = RULES):
    """引擎一止盈:最近嘅合格目標。★ 呢個係回測用嘅版本,Pine 目前唔一致。"""
    close = row["Close"]
    cands = []
    if pd.notna(row["MA50"]) and row["MA50"] > close:
        cands.append(row["MA50"])
    if pd.notna(row["high_60d"]) and row["high_60d"] > close:
        cands.append(row["high_60d"])
    return min(cands) if cands else None


def mr_stop(row, rules: EngineRules = RULES):
    close, a = row["Close"], row["ATR"]
    if pd.isna(a) or a <= 0 or pd.isna(row["low_10d"]):
        return None
    return min(row["low_10d"] * 0.995, close - rules.MR_ATR_STOP_MULT * a)


def is_speculative(df: pd.DataFrame, i: int, rules: EngineRules = RULES) -> bool:
    n = rules.SPEC_LOOKBACK
    if i < n:
        return False
    win = df.iloc[i - n + 1:i + 1]
    lo = win["Low"].min()
    return bool(lo > 0 and (win["High"].max() / lo) >= rules.SPEC_HIGH_LOW_MULT)


if __name__ == "__main__":
    print("V6.5 規則 —— 單一來源")
    print("=" * 60)
    for k, v in asdict(RULES).items():
        print(f"  {k:28} {v}")
    print(NOTE_STOP_WIDTH)
    print(NOTE_REGIME_LAG)
    print(NOTE_PINE_PARITY)
