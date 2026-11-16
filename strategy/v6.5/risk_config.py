# -*- coding: utf-8 -*-
"""
============================================================
V6.5 — 成本模型 + 硬性風險上限
============================================================
V6.4 兩樣嘢完全冇:
  1. 交易成本 —— 一蚊都冇計。所有成交價都係 Close,免費。
  2. 倉位上限 —— 「每筆風險1%」冇配任何名義金額上限或同時持倉上限,
     所以佢其實係一條無上限嘅集中度規則。

Tom (量化) 嘅裁決:
  1.325% EV × US$128 倉位 = 每筆預期毛利 US$1.70。
  來回佣金 US$0.70–4.00。三個券商情境入面有兩個,飛機票貴過隻雞。
  → 淨EV:最好 +0.53%,中位 −0.49%,港式零售 −2.06%。

John (CRO) 嘅裁決 (CL-3):
  US$128.21 以上嘅股票,一股已經超過戶口 10%。
  你嘅「買唔起」護欄喺 ~US$183 先響,應該喺 US$128.21 響。
  即係喺「跳空風險」呢個維度上鬆咗大約 43%。

★ 呢個檔案入面每一個上限都要「擋住」交易,唔係「顯示警告」。
  護欄同控制嘅分別 = 你可唔可以按掣繞過佢。
============================================================
"""
from dataclasses import dataclass, asdict


# ============================================================
# 成本 — 券商預設。★ 用你自己嘅真實收費表取代。
# ============================================================

@dataclass(frozen=True)
class CostModel:
    name: str
    min_commission_usd: float      # 每邊最低佣金
    per_share_usd: float           # 每股佣金
    pct_of_notional: float         # 按金額百分比(%)
    half_spread_bp: float          # 半個買賣差價(基點)
    slippage_bp: float             # 滑價(基點,每邊)
    fx_flat_usd: float = 0.0       # 港元換美元,每次轉換

    def one_side(self, notional: float, shares: int) -> float:
        commission = max(
            self.min_commission_usd,
            self.per_share_usd * shares,
            self.pct_of_notional / 100.0 * notional,
        )
        friction = (self.half_spread_bp + self.slippage_bp) / 10000.0 * notional
        return commission + friction

    def round_trip(self, entry_notional: float, exit_notional: float, shares: int) -> float:
        return (self.one_side(entry_notional, shares)
                + self.one_side(exit_notional, shares))


# ★ 佣金數字係說明性假設,唔係查證過嘅收費表。用之前要換成你自己嘅。
BROKERS = {
    "free": CostModel("免費(V6.4 隱含假設)", 0, 0, 0, 0, 0),
    "ibkr_tiered": CostModel("IBKR 分層", 0.35, 0.0035, 0.0, 2.5, 7.0, 2.0),
    "ibkr_fixed": CostModel("IBKR 固定", 1.00, 0.005, 0.0, 2.5, 7.0, 2.0),
    "hk_retail": CostModel("港式零售(富途/老虎類)", 2.00, 0.0, 0.0, 2.5, 10.0, 0.0),
}


# ============================================================
# 硬性上限 — John 嘅 CL-3
# ============================================================

@dataclass(frozen=True)
class RiskLimits:
    account_hkd: float = 10_000.0
    usd_hkd: float = 7.8
    risk_pct: float = 1.0              # 每筆風險
    max_position_notional_pct: float = 10.0   # ★ V6.4 完全冇呢條
    max_open_positions: int = 5              # ★ V6.4 完全冇呢條
    max_portfolio_heat_pct: float = 5.0      # ★ V6.4 完全冇呢條
    max_per_sector: int = 2                  # ★ V6.4 完全冇呢條
    cash_floor_pct: float = 10.0             # ★ V6.4 完全冇呢條
    drawdown_budget_pct: float = 20.0        # 超過就停手,唔係建議
    allow_leverage: bool = False             # 現金戶口。CL-1。

    @property
    def account_usd(self) -> float:
        return self.account_hkd / self.usd_hkd

    @property
    def risk_usd(self) -> float:
        return self.account_usd * self.risk_pct / 100.0

    @property
    def max_notional_usd(self) -> float:
        return self.account_usd * self.max_position_notional_pct / 100.0

    @property
    def max_affordable_price(self) -> float:
        """一股都已經超過集中度上限嘅價位。V6.4 對呢個數字一無所知。"""
        return self.max_notional_usd


LIMITS = RiskLimits()


# ============================================================
# 倉位計算 —— 會「擋」,唔係「提。示」
# ============================================================

class Blocked(Exception):
    """倉位被硬性上限擋住。呢個係正常運作,唔係錯誤。"""
    def __init__(self, reason: str, detail: str = ""):
        self.reason, self.detail = reason, detail
        super().__init__(f"{reason}: {detail}" if detail else reason)


def plan_position(price: float,
                  stop: float,
                  equity_usd: float,
                  open_positions: int,
                  current_heat_pct: float,
                  cash_usd: float,
                  sector_count: int = 0,
                  limits: RiskLimits = LIMITS,
                  risk_pct_override: float = None):
    """
    回傳 dict(shares, notional, risk_usd, risk_pct_of_equity)
    或者 raise Blocked。

    ★ 同 V6.4 嘅分別:V6.4 只會喺 shares < 1 嗰陣拒絕。
      呢度有六個獨立嘅擋位,而且每個都會話你知係邊個擋。
    """
    if price <= 0 or stop <= 0 or stop >= price:
        raise Blocked("止蝕無效", f"price={price:.2f} stop={stop:.2f}")

    if open_positions >= limits.max_open_positions:
        raise Blocked("同時持倉已滿",
                      f"{open_positions}/{limits.max_open_positions}")

    if sector_count >= limits.max_per_sector:
        raise Blocked("同板塊已滿",
                      f"{sector_count}/{limits.max_per_sector}")

    risk_pct = limits.risk_pct if risk_pct_override is None else risk_pct_override
    if current_heat_pct + risk_pct > limits.max_portfolio_heat_pct:
        raise Blocked("組合總熱度超標",
                      f"{current_heat_pct:.2f}%+{risk_pct:.2f}% > "
                      f"{limits.max_portfolio_heat_pct:.2f}%")

    risk_budget = equity_usd * risk_pct / 100.0
    per_share_risk = price - stop
    shares = int(risk_budget // per_share_risk)

    if shares < 1:
        raise Blocked("買唔起",
                      f"每股風險 ${per_share_risk:.2f} > 預算 ${risk_budget:.2f}")

    notional = shares * price
    max_notional = equity_usd * limits.max_position_notional_pct / 100.0

    # ★ 呢個係 V6.4 完全冇嘅檢查 —— 集中度,唔係負擔能力。
    if notional > max_notional:
        shares = int(max_notional // price)
        if shares < 1:
            raise Blocked("單一倉位集中度超標",
                          f"一股 ${price:.2f} > 上限 ${max_notional:.2f} "
                          f"({limits.max_position_notional_pct:.0f}% of equity)")
        notional = shares * price

    if not limits.allow_leverage:
        cash_after = cash_usd - notional
        floor = equity_usd * limits.cash_floor_pct / 100.0
        if cash_after < floor:
            raise Blocked("現金低於下限",
                          f"買入後 ${cash_after:.2f} < 下限 ${floor:.2f}")

    actual_risk = shares * per_share_risk
    return {
        "shares": shares,
        "notional": notional,
        "risk_usd": actual_risk,
        "risk_pct_of_equity": actual_risk / equity_usd * 100.0,
        # 取整之後真正用到嘅風險預算比例 —— Tom 話呢度可以蝕高達 45%
        "budget_used_pct": actual_risk / risk_budget * 100.0,
    }


def price_ceiling_table(limits: RiskLimits = LIMITS):
    """
    John §4.3 嘅表:唔同止蝕闊度之下,最高買得起嘅股價。
    ★ 重點唔係「買唔買得起」,係「集中度」—— 見 max_affordable_price。
    """
    rows = []
    for stop_pct in (5, 7, 8, 10, 12):
        for rp in (limits.risk_pct, limits.risk_pct / 2):
            budget = limits.account_usd * rp / 100.0
            rows.append({
                "stop_width_pct": stop_pct,
                "risk_pct": rp,
                "max_price_affordable": budget / (stop_pct / 100.0),
            })
    return rows


if __name__ == "__main__":
    L = LIMITS
    print("V6.5 風險上限")
    print("=" * 66)
    print(f"  戶口          HK${L.account_hkd:,.0f}  =  US${L.account_usd:,.2f}")
    print(f"  每筆風險      {L.risk_pct}%  =  US${L.risk_usd:.2f}")
    print(f"  單倉名義上限  {L.max_position_notional_pct}%  =  US${L.max_notional_usd:.2f}")
    print(f"  ★ 一股已超集中度上限嘅價位: US${L.max_affordable_price:.2f}")
    print(f"     (V6.4 嘅「買唔起」護欄要到 ~US$183 先響 —— 鬆咗約 43%)")
    print()
    print("  價位上限表(負擔能力):")
    print(f"  {'止蝕闊度':>10}{'風險%':>8}{'最高股價':>14}")
    for r in price_ceiling_table():
        flag = "  ← 已超集中度上限" if r["max_price_affordable"] > L.max_notional_usd else ""
        print(f"  {r['stop_width_pct']:>9}%{r['risk_pct']:>7.1f}%"
              f"{r['max_price_affordable']:>13.2f}{flag}")
    print()
    print("  券商成本情境 — US$128 倉位,來回:")
    for key, cm in BROKERS.items():
        shares = max(1, int(128 / 50))
        rt = cm.round_trip(128.0, 128.0, shares)
        print(f"  {key:14} {cm.name:24} US${rt:5.2f}  = {rt/128*100:5.2f}% 名義")
    print()
    print("  ★ 每筆預期毛利(EV +1.325% × US$128) = US$1.70")
    print("    以上有幾多個情境嘅來回成本大過 US$1.70,就有幾多個情境你係喺度做義工。")
