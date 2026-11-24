# -*- coding: utf-8 -*-
"""
V6.6 設定 —— 全系統唯一嘅設定檔
================================
★ 改呢度任何嘢,掃描器頂部嘅「指紋」就會變。你一眼就知自己跑緊邊個版本。

決定紀錄(2026-11-24,Owner):
  1. 兩條路徑都跑、都記錄:回測版("bt")= 真正交易清單;舊掃描器版("scan")= 只記錄。
  2. 引擎一按回測版交易:評分≥0.55、R≥2、所有級別;引擎二優先佔倉位。
  3. 名義上限 = A(10%)。B′(引擎二單股可去到15%)要 CRO 書面批准 + 四個關卡全過先開。
"""
import hashlib
import os

VERSION = "V6.6.0"
RELEASE_DATE = "2026-11-24"

# ---- 資金(同 V6.4.2 一致) ----
ACCOUNT_HKD = 10000
RISK_PCT = 1.0
USD_HKD = 7.8
MAX_POSITIONS = 2
MONTH_BREAKER_PCT = 10.0

# ---- 路徑 ----
LIVE_PATH = "bt"                 # 真正交易:回測驗證過嘅規則(引擎二要突破20日高)
SHADOW_PATHS = ("scan",)         # 只記錄:舊 daily_strong_signals 嘅規則
E1_LIVE = "as_backtested"        # 引擎一:評分≥0.55 + R≥2,所有級別

# ---- 名義上限(CRO 2026-11-24 裁決) ----
CAP_MODE = "A"                   # A = 10% 一律
B_PRIME_ENABLED = False          # B′:引擎二、1股、名義 ≤15%、1股風險 ≤1% → 准。要 CRO 書面批准先改 True
B_PRIME_CRO_NOTE = ""            # 開 B′ 時填:CRO 批准文件路徑 + 日期
CAP_A_PCT = 10.0
CAP_BPRIME_PCT = 15.0
CAP_D_PCT = 15.0                 # D = 15% 一律(只係影子記錄,未批准)

# ---- 關卡(全部 True 先可以開 B′) ----
GATES = {
    "G1_路徑已定": True,           # 2026-11-24 Owner 揀咗:回測版交易、掃描器版記錄
    "V1_真實收費已核": False,       # 要一張微牛成交單據(佣金/平台費/SEC/TAF/匯兌)
    "V2_代碼測試": False,          # selftest.py 全過 —— 由掃描.bat 每次自動跑,呢度係人手確認
    "V3_對照測試": False,          # parity_check.py 喺你部電腦過關
}

CORE_FILES = ("rules_v642.py", "indicators.py", "signals_v66.py", "sizing_v66.py",
              "guardrails_v66.py", "config_v66.py")


def fingerprint(folder=None) -> str:
    """核心原始碼嘅 SHA-256(行尾統一做 LF)。任何規則/設定改動都會令佢變。"""
    here = folder or os.path.dirname(os.path.abspath(__file__))
    h = hashlib.sha256()
    for fn in CORE_FILES:
        with open(os.path.join(here, fn), "rb") as f:
            h.update(fn.encode())
            h.update(f.read().replace(b"\r\n", b"\n"))
    return h.hexdigest()[:12]


def gates_outstanding():
    return [k for k, v in GATES.items() if not v]


def check_config():
    """設定自檢。違規即刻停 —— 呢個係結構性控制,唔係提示。"""
    assert CAP_MODE in ("A", "B_PRIME"), f"CAP_MODE 只可以係 A 或 B_PRIME,而家係 {CAP_MODE}"
    assert CAP_A_PCT == 10.0, "名義上限 A 必須係 10%(CRO 2026-11-24)"
    assert CAP_BPRIME_PCT <= 15.0, "B′ 上限唔可以超過 15%(CRO:20% 同無上限已否決)"
    assert MAX_POSITIONS == 2 and RISK_PCT == 1.0, "倉位數/每筆風險係鎖死參數"
    if CAP_MODE == "B_PRIME" or B_PRIME_ENABLED:
        assert B_PRIME_ENABLED and CAP_MODE == "B_PRIME", "B′ 要 CAP_MODE 同 B_PRIME_ENABLED 一齊改"
        assert not gates_outstanding(), f"B′ 未可以開:關卡未過 {gates_outstanding()}"
        assert B_PRIME_CRO_NOTE, "B′ 要填 CRO 批准文件(B_PRIME_CRO_NOTE)"
    assert LIVE_PATH == "bt", "交易路徑必須係回測驗證版(bt)"
    return True
