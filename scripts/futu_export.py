#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
futu_export.py — 喺 Owner 部機度行,將 Futu 嘅數據導出成檔案。

點解要有呢個:
  CEO 嘅 session 行喺一個遠端 container 入面,對外網絡全部被擋(403),
  而且 container 閒置就會被回收。FutuOpenD 係行喺你部機度嘅,
  兩者之間根本冇路。所以唔係「唔肯連」,係「連唔到」。
  呢個腳本就係條橋:你部機行,出檔案,你傳返畀 CEO。

呢個腳本**只讀**。冇任何落單、改單、撤單嘅功能,而且開頭有個自我審計,
  一發現自己個源碼入面有落單嘅字眼就會拒絕行。
  (CLAUDE.md 規則 1:冇任何 agent 可以連券商 API 落單。)

你嘅密碼永遠唔會經過呢個腳本 —— 登入係 FutuOpenD 自己處理。

用法:
    pip install futu-api
    # 先開 FutuOpenD 並登入
    python futu_export.py                 # 模擬倉(預設,最安全)
    python futu_export.py --real          # 真倉持倉(只讀)
    python futu_export.py --real --kline HK.03416 HK.06160 US.MSFT
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

# ── 輸出用 UTF-8,Windows 經 pipe 會 fallback 去 cp1252 ──
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

# ============================================================
# 自我審計 —— 證明呢個檔案落唔到單
# ============================================================
FORBIDDEN = ("place_order", "modify_order", "cancel_order", "unlock_trade",
             "acctradinginfo_query", "OpenFutureTradeContext")


def self_audit() -> None:
    """讀自己個源碼,確認冇落單嘅呼叫。唔係擺設 —— 有就即刻死。"""
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    body = src.split("FORBIDDEN = (", 1)[1].split(")", 1)[1]      # 跳過定義自己嗰行
    hits = [w for w in FORBIDDEN if re.search(rf"\b{w}\s*\(", body)]
    if hits:
        print(f"★ 自我審計失敗:呢個檔案入面有落單嘅呼叫 {hits}。拒絕執行。")
        sys.exit(2)
    print("自我審計 OK —— 呢個腳本只讀,落唔到單。")


# ============================================================
def connect(host: str, port: int):
    try:
        from futu import OpenQuoteContext, OpenSecTradeContext, RET_OK, TrdMarket, SecurityFirm
    except ImportError:
        print("★ 搵唔到 futu-api。裝法:  pip install futu-api")
        sys.exit(1)
    return OpenQuoteContext, OpenSecTradeContext, RET_OK, TrdMarket, SecurityFirm


def dump_account(trd_ctx, RET_OK, trd_env, out: dict) -> None:
    """資金 + 持倉。兩樣都係只讀,唔使 unlock。"""
    ret, funds = trd_ctx.accinfo_query(trd_env=trd_env, acc_index=0)
    out["funds"] = funds.to_dict("records") if ret == RET_OK else {"error": str(funds)}
    if ret != RET_OK:
        print(f"  資金查詢失敗:{funds}")

    ret, pos = trd_ctx.position_list_query(trd_env=trd_env, acc_index=0)
    if ret == RET_OK:
        out["positions"] = pos.to_dict("records")
        print(f"  持倉 {len(pos)} 隻")
    else:
        out["positions"] = {"error": str(pos)}
        print(f"  持倉查詢失敗:{pos}")


def dump_klines(quote_ctx, RET_OK, codes, start, end, out: dict) -> None:
    """日線。每隻獨立 try —— 一隻冇報價權唔應該搞死成個導出。"""
    out["klines"] = {}
    for code in codes:
        try:
            ret, df, _page = quote_ctx.request_history_kline(
                code, start=start, end=end, max_count=None)
        except Exception as e:                       # noqa: BLE001
            print(f"  {code}: 例外 {e}")
            out["klines"][code] = {"error": str(e)}
            continue
        if ret == RET_OK and len(df):
            out["klines"][code] = df.to_dict("records")
            print(f"  {code}: {len(df)} 條")
        else:
            # 多數係冇嗰個市場嘅報價權,唔係代碼錯
            print(f"  {code}: 攞唔到 ({df})")
            out["klines"][code] = {"error": str(df)}


def write_portfolio_fragment(positions, path: pathlib.Path) -> None:
    """寫一份 config/portfolio.yaml 嘅草稿畀 Owner 自己睇過先貼。
    ★ 唔會直接改 repo 入面嘅 config —— Owner 係最終權力(規則 2)。"""
    if not isinstance(positions, list) or not positions:
        return
    lines = ["# 由 futu_export.py 產生 —— Owner 睇過先好貼入 config/portfolio.yaml",
             f"# 導出時間:{dt.datetime.now().isoformat(timespec='seconds')}",
             "holdings:"]
    for p in positions:
        code = p.get("code", "?")
        qty = p.get("qty", p.get("can_sell_qty", "?"))
        cost = p.get("cost_price", "?")
        val = p.get("market_val", "?")
        lines.append(f"  - ticker: {code}")
        lines.append(f"    quantity: {qty}")
        lines.append(f"    cost_price: {cost}")
        lines.append(f"    market_value: {val}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  → 持倉草稿寫咗落 {path.name}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Futu 只讀數據導出")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=11111)
    ap.add_argument("--real", action="store_true",
                    help="讀真倉持倉(只讀)。唔加就用模擬倉。")
    ap.add_argument("--kline", nargs="*", default=[],
                    help="要日線嘅代碼,例如 HK.03416 US.MSFT")
    ap.add_argument("--start", default="2019-01-01")
    ap.add_argument("--end", default=dt.date.today().isoformat())
    a = ap.parse_args()

    self_audit()

    OpenQuoteContext, OpenSecTradeContext, RET_OK, TrdMarket, SecurityFirm = connect(a.host, a.port)
    from futu import TrdEnv
    trd_env = TrdEnv.REAL if a.real else TrdEnv.SIMULATE
    print(f"帳戶環境:{'真倉(只讀)' if a.real else '模擬倉'}")

    stamp = dt.date.today().isoformat()
    out: dict = {"exported_at": dt.datetime.now().isoformat(timespec="seconds"),
                 "trd_env": "REAL" if a.real else "SIMULATE",
                 "start": a.start, "end": a.end}

    print("\n[1/2] 帳戶")
    trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK,
                                  host=a.host, port=a.port,
                                  security_firm=SecurityFirm.FUTUSECURITIES)
    try:
        dump_account(trd_ctx, RET_OK, trd_env, out)
    finally:
        trd_ctx.close()

    if a.kline:
        print(f"\n[2/2] 日線 —— {len(a.kline)} 隻")
        quote_ctx = OpenQuoteContext(host=a.host, port=a.port)
        try:
            dump_klines(quote_ctx, RET_OK, a.kline, a.start, a.end, out)
        finally:
            quote_ctx.close()
    else:
        print("\n[2/2] 冇指定 --kline,跳過")

    jpath = pathlib.Path(f"futu_export_{stamp}.json")
    jpath.write_text(json.dumps(out, ensure_ascii=False, indent=2, default=str),
                     encoding="utf-8")
    print(f"\n完成。寫咗:{jpath.name}")
    write_portfolio_fragment(out.get("positions"), pathlib.Path(f"portfolio_draft_{stamp}.yaml"))
    print("將呢啲檔案傳返畀 CEO。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
