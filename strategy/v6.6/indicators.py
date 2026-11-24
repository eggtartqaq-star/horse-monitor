# -*- coding: utf-8 -*-
"""
V6.6 指標 —— 純 pandas,唔使裝 `ta`
====================================
目標:同 V6.4.2 `dual_engine_v6_4.calc_indicators()` 產生一模一樣嘅欄位。

點解唔直接用 `ta`:
  1. 雲端環境裝唔到 `ta`(被封鎖)。
  2. `ta` 一升版本,止蝕位可以靜靜雞變 —— 自己實作 = 鎖死。

★ 數值同 `ta` 可能有細微差異(主要係 ADX 頭幾十條 bar 嘅初始化方法)。
  喺你部電腦跑 `python parity_check.py` 就會逐欄比較 —— 差異大就唔好信呢度嘅回測。

RSI / ATR 嘅公式係照 `ta` 0.10–0.11 嘅寫法:
  RSI = Wilder EWM(alpha=1/n, adjust=False, min_periods=n),avg_loss=0 → 100
  ATR = 首 n 條 TR 平均做種子,之後 (prev*(n-1)+TR)/n;種子之前 = 0(同 ta 一樣係 0,唔係 NaN)
ADX = 標準 Wilder:DM/TR 用 Wilder 平滑,DX 首 n 個平均做種子。
OBV = 照 ta:收市 < 前收市 → −成交量,其他(包括持平)→ +成交量。
"""
import numpy as np
import pandas as pd


def rsi_ta(close: pd.Series, n: int) -> pd.Series:
    diff = close.diff(1)
    up = diff.where(diff > 0, 0.0)
    dn = -diff.where(diff < 0, 0.0)
    emaup = up.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    emadn = dn.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    rs = emaup / emadn
    out = pd.Series(np.where(emadn == 0, 100.0, 100.0 - 100.0 / (1.0 + rs)), index=close.index)
    out[emaup.isna()] = np.nan
    return out


def _tr(df: pd.DataFrame) -> pd.Series:
    pc = df["Close"].shift(1)
    return pd.concat([df["High"] - df["Low"], (df["High"] - pc).abs(), (df["Low"] - pc).abs()],
                     axis=1).max(axis=1)


def atr_ta(df: pd.DataFrame, n: int = 14) -> pd.Series:
    tr = _tr(df).to_numpy()
    out = np.zeros(len(tr))
    if len(tr) >= n:
        out[n - 1] = tr[:n].mean()
        for i in range(n, len(tr)):
            out[i] = (out[i - 1] * (n - 1) + tr[i]) / n
    return pd.Series(out, index=df.index)


def adx_wilder(df: pd.DataFrame, n: int = 14):
    h, l = df["High"], df["Low"]
    up = h - h.shift(1)
    dn = l.shift(1) - l
    pdm = (((up > dn) & (up > 0)) * up).fillna(0.0).to_numpy()
    ndm = (((dn > up) & (dn > 0)) * dn).fillna(0.0).to_numpy()
    tr = _tr(df).to_numpy()
    N = len(tr)
    adx = np.full(N, np.nan); dip = np.full(N, np.nan); din = np.full(N, np.nan)
    if N <= 2 * n:
        return (pd.Series(adx, index=df.index), pd.Series(dip, index=df.index),
                pd.Series(din, index=df.index))
    # Wilder 累計和:種子 = bar 1..n 嘅和(bar 0 冇前收市)
    s_tr = tr[1:n + 1].sum(); s_p = pdm[1:n + 1].sum(); s_n = ndm[1:n + 1].sum()
    dx = np.full(N, np.nan)
    for i in range(n, N):
        if i > n:
            s_tr = s_tr - s_tr / n + tr[i]
            s_p = s_p - s_p / n + pdm[i]
            s_n = s_n - s_n / n + ndm[i]
        if s_tr > 0:
            dip[i] = 100 * s_p / s_tr
            din[i] = 100 * s_n / s_tr
            tot = dip[i] + din[i]
            dx[i] = 100 * abs(dip[i] - din[i]) / tot if tot > 0 else 0.0
    first = 2 * n - 1
    adx[first] = np.nanmean(dx[n:first + 1])
    for i in range(first + 1, N):
        adx[i] = (adx[i - 1] * (n - 1) + dx[i]) / n
    return (pd.Series(adx, index=df.index), pd.Series(dip, index=df.index),
            pd.Series(din, index=df.index))


def obv_ta(close: pd.Series, volume: pd.Series) -> pd.Series:
    return pd.Series(np.where(close < close.shift(1), -volume, volume), index=close.index).cumsum()


def calc_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """欄位名、公式同 V6.4.2 calc_indicators() 一致。"""
    df = df.copy()
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df["RSI14"] = rsi_ta(df["Close"], 14)
    df["RSI2"] = rsi_ta(df["Close"], 2)
    df["ADX"], df["DI_PLUS"], df["DI_MINUS"] = adx_wilder(df, 14)
    df["ATR"] = atr_ta(df, 14)
    df["price_vs_ma20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100
    df["ma20_vs_ma50"] = (df["MA20"] - df["MA50"]) / df["MA50"] * 100
    df["ret_5d"] = df["Close"].pct_change(5) * 100
    df["ret_10d"] = df["Close"].pct_change(10) * 100
    df["vol_ratio"] = df["Volume"].rolling(5).mean() / df["Volume"].rolling(20).mean()
    o = obv_ta(df["Close"], df["Volume"])
    df["OBV"] = o
    df["OBV_Div"] = (df["Close"] < df["Close"].shift(5)) & (o > o.shift(5))
    df["low_10d"] = df["Low"].rolling(10).min()
    df["high_20d"] = df["High"].rolling(20).max()
    df["high_60d"] = df["High"].rolling(60).max()
    df["dist_60h"] = (df["high_60d"] - df["Close"]) / df["Close"] * 100
    # V6.6 新增(只供升級實驗用,V6.4.2 規則唔會讀):
    df["mom_126"] = df["Close"].pct_change(126) * 100
    return df
