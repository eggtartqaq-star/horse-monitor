# -*- coding: utf-8 -*-
"""
V6.6 倉位 —— 名義上限只喺呢度存在(CRO V-2:結構性控制)
==========================================================
A   10% 一律(V6.4.2,現行)
B′  10% 一律;例外:引擎二、只限1股、名義 ≤15%、1股風險 ≤ 每筆風險預算 → 准
D   15% 一律(只係影子記錄,CRO 唔建議)

任何模式都係整數股(冇碎股),每筆風險 ≤ 1%。
"""
import config_v66 as C
import rules_v642 as R


def _budget(currency):
    risk_hkd = C.ACCOUNT_HKD * C.RISK_PCT / 100
    if currency == "HKD":
        return risk_hkd, C.ACCOUNT_HKD
    return risk_hkd / C.USD_HKD, C.ACCOUNT_HKD / C.USD_HKD


def size(entry, stop, engine, mode="A", currency="USD"):
    """回傳 dict(shares, notional, pct_of_account, rule)。shares=0 即係唔准。
    entry/stop 一定要係「當日真實股價」(唔好用拆股調整後嘅歷史價)。"""
    risk_budget, acct = _budget(currency)
    out = {"shares": 0, "notional": 0.0, "pct_of_account": 0.0, "rule": "block"}
    if entry <= 0 or entry - stop <= 0:
        out["rule"] = "invalid"
        return out
    if mode == "D":
        sh, _ = R.position_plan_ccy(entry, stop, currency, C.ACCOUNT_HKD, C.USD_HKD, C.RISK_PCT, C.CAP_D_PCT)
        rule = "D15"
    else:
        sh, _ = R.position_plan_ccy(entry, stop, currency, C.ACCOUNT_HKD, C.USD_HKD, C.RISK_PCT, C.CAP_A_PCT)
        rule = "A10"
        if mode == "B_PRIME" and sh == 0 and engine == "E2":
            one_share_risk = entry - stop
            if entry <= acct * C.CAP_BPRIME_PCT / 100 and one_share_risk <= risk_budget:
                sh, rule = 1, "B'1share"
    if sh > 0:
        out.update(shares=sh, notional=round(sh * entry, 2),
                   pct_of_account=round(sh * entry / acct * 100, 2), rule=rule)
    return out


def max_limit(close, stop, shares, engine, target=None, mode="A", currency="USD"):
    """CRO N-15(2026-11-25):限價上限 = 「用同一個 size() 計,仍然買得到 shares 股」嘅最高價(去到仙),
    而且唔高過收市 +1%;引擎一另外要 R ≥ 2(限價 ≤ (止盈 + 2×止蝕) ÷ 3)。
    用呢個做限價 → 成交價嘅名義、風險、股數檢查一定過。close/stop/target 一定要係真實股價。"""
    if shares is None or shares < 1 or close <= stop:
        return None
    lo = int(close * 100)                                   # 收市價(向下取到仙)
    hi = int(close * 1.01 * 100)
    if engine == "E1" and target is not None:
        hi = min(hi, int((target + 2 * stop) / 3 * 100))
    if hi < lo or size(lo / 100, stop, engine, mode, currency)["shares"] < shares:
        return None
    while lo < hi:                                          # 買得到嘅價係「由低至高」一段 → 二分法
        mid = (lo + hi + 1) // 2
        if size(mid / 100, stop, engine, mode, currency)["shares"] >= shares:
            lo = mid
        else:
            hi = mid - 1
    return lo / 100


def live_mode():
    C.check_config()
    return "B_PRIME" if (C.CAP_MODE == "B_PRIME" and C.B_PRIME_ENABLED) else "A"
