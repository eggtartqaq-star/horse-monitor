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


def live_mode():
    C.check_config()
    return "B_PRIME" if (C.CAP_MODE == "B_PRIME" and C.B_PRIME_ENABLED) else "A"
