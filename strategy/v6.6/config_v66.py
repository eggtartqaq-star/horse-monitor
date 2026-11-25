# -*- coding: utf-8 -*-
"""
V6.6 設定
=========
兩部分:
  1. 呢個檔:規則常數(鎖死)。改咗 → 掃描器頂部「規則指紋」會變。
  2. owner_settings.json:你自己會改嘅嘢(戶口金額、關卡、B′ 開關)。
     改佢唔會令規則指紋變;掃描器會另外印出「設定」一行。

決定紀錄(2026-11-24,Owner):
  1. 兩條路徑都跑、都記錄:回測版("bt")= 真正交易清單;舊掃描器版("scan")= 只記錄。
  2. 引擎一按回測版交易:評分≥0.55、R≥2、所有級別;引擎二優先佔倉位。
  3. 名義上限 = A(10%)。B′(引擎二單股可去到15%)要 CRO 書面批准 + 四個關卡全過先開。
"""
import hashlib
import json
import os
import re

VERSION = "V6.6.3"
RELEASE_DATE = "2026-11-25"
HERE = os.path.dirname(os.path.abspath(__file__))
SETTINGS_FILE = os.path.join(HERE, "owner_settings.json")

# ---- 鎖死參數(同 V6.4.2 一致) ----
RISK_PCT = 1.0
USD_HKD = 7.8
MAX_POSITIONS = 2
MONTH_BREAKER_PCT = 10.0

# ---- 路徑 ----
LIVE_PATH = "bt"                 # 真正交易:回測驗證過嘅規則(引擎二要突破20日高)
SHADOW_PATHS = ("scan",)         # 只記錄:舊 daily_strong_signals 嘅規則
E1_LIVE = "as_backtested"        # 引擎一:評分≥0.55 + R≥2,所有級別

# ---- 名義上限(CRO 2026-11-24 裁決) ----
CAP_A_PCT = 10.0
CAP_BPRIME_PCT = 15.0
CAP_D_PCT = 15.0                 # D = 15% 一律(只係影子記錄,未批准)

# ---- B′ 批准文件(CRO B-4,2026-11-25)----
# 開 B′ 要 owner_settings.json 嘅 b_prime_cro_note 等於下面其中一個。
# 呢個係代碼 → 加入 = 改規則指紋 → CRO 要重新核對。淨係改設定檔開唔到 B′。
APPROVED_BPRIME_NOTES = ()

# ---- 你嘅設定(預設值;實際由 owner_settings.json 讀) ----
DEFAULT_SETTINGS = {
    "account_hkd": 10000,
    "cap_mode": "A",
    "b_prime_enabled": False,
    "b_prime_cro_note": "",
    "gates": {
        "G1_路徑已定": True,        # 2026-11-24 Owner 揀咗:回測版交易、掃描器版記錄
        "V1_真實收費已核": False,    # 要一張微牛成交單據(佣金/平台費/SEC/TAF/匯兌)
        "V2_代碼測試": False,       # selftest.py 喺你部電腦全過
        "V3_對照測試": False,       # parity_check.py 喺你部電腦過關
    },
    "real_fee": {"min_per_side_usd": None, "bp_per_side": None},   # V-1 之後填
}


class ConfigError(AssertionError):
    """設定違規。用 raise 而唔係 assert —— python -O 都關唔到。"""


def _load_settings():
    s = json.loads(json.dumps(DEFAULT_SETTINGS))
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, encoding="utf-8-sig") as f:
            user = json.load(f)
        for k, v in user.items():
            if k == "gates":
                s["gates"].update(v)
            elif k == "real_fee":
                s["real_fee"].update(v)
            elif not k.startswith("_"):
                s[k] = v
    return s


_S = _load_settings()
ACCOUNT_HKD = float(_S["account_hkd"])
CAP_MODE = _S["cap_mode"]
_B_PRIME_RAW = _S["b_prime_enabled"]
B_PRIME_ENABLED = _B_PRIME_RAW is True          # CRO N-7:"false"(有引號)唔可以當開
B_PRIME_CRO_NOTE = _S["b_prime_cro_note"]
GATES = dict(_S["gates"])
REAL_FEE = dict(_S["real_fee"])

# 規則指紋涵蓋嘅檔(唔包括 owner_settings.json)
# CRO B-11(2026-11-25):加入 lab.py —— ledger resolve 用佢嘅 simulate 計結果
CORE_FILES = ("rules_v642.py", "indicators.py", "signals_v66.py", "sizing_v66.py",
              "guardrails_v66.py", "config_v66.py", "daily_scan_v66.py", "ledger_v66.py",
              "telegram_bot_v66.py", "lab.py")


def fingerprint(folder=None) -> str:
    """規則/代碼嘅 SHA-256(行尾統一做 LF)。改任何核心檔 → 變;改 owner_settings.json → 唔變。"""
    here = folder or HERE
    h = hashlib.sha256()
    for fn in CORE_FILES:
        p = os.path.join(here, fn)
        if not os.path.exists(p):
            continue
        with open(p, "rb") as f:
            h.update(fn.encode())
            h.update(f.read().replace(b"\r\n", b"\n"))
    return h.hexdigest()[:12]


def settings_line() -> str:
    g = "".join("✓" if v else "✗" for v in GATES.values())
    return (f"設定: 戶口 HK${ACCOUNT_HKD:,.0f}  上限 {CAP_MODE}  B′ {'開' if B_PRIME_ENABLED else '關'}  "
            f"關卡 G1/V1/V2/V3 = {g}")


def gates_outstanding():
    return [k for k, v in GATES.items() if v is not True]


def _fail(msg):
    raise ConfigError(msg)


def check_config():
    """設定自檢。違規即刻停 —— 結構性控制,唔係提示。"""
    if CAP_MODE not in ("A", "B_PRIME"):
        _fail(f"cap_mode 只可以係 A 或 B_PRIME,而家係 {CAP_MODE}")
    if CAP_A_PCT != 10.0:
        _fail("名義上限 A 必須係 10%(CRO 2026-11-24)")
    if CAP_BPRIME_PCT > 15.0 or CAP_D_PCT > 15.0:
        _fail("上限唔可以超過 15%(CRO:20% 同無上限已否決)")
    if MAX_POSITIONS != 2 or RISK_PCT != 1.0:
        _fail("倉位數/每筆風險係鎖死參數")
    if not (1000 <= ACCOUNT_HKD <= 10_000_000):
        _fail(f"account_hkd 唔合理:{ACCOUNT_HKD}")
    # CRO N-7:開關同關卡一定要係 JSON 嘅 true/false(冇引號)。"false" 係文字,唔係「關」。
    if not isinstance(_B_PRIME_RAW, bool):
        _fail(f"owner_settings.json 嘅 b_prime_enabled 要寫 true 或 false(唔好加引號),而家係 {_B_PRIME_RAW!r}")
    bad = {k: v for k, v in GATES.items() if not isinstance(v, bool)}
    if bad:
        _fail(f"owner_settings.json 嘅關卡要寫 true 或 false(唔好加引號):{bad}")
    if CAP_MODE == "B_PRIME" or B_PRIME_ENABLED:
        if not (B_PRIME_ENABLED and CAP_MODE == "B_PRIME"):
            _fail("B′ 要 cap_mode 同 b_prime_enabled 一齊改")
        if gates_outstanding():
            _fail(f"B′ 未可以開:關卡未過 {gates_outstanding()}")
        note = str(B_PRIME_CRO_NOTE or "")
        if not (re.search(r"\d{4}-\d{2}-\d{2}", note) and "reports/risk/" in note):
            _fail("b_prime_cro_note 要寫 CRO 批准文件路徑(reports/risk/...)同日期(YYYY-MM-DD)")
        if note not in APPROVED_BPRIME_NOTES:
            _fail("b_prime_cro_note 唔喺 config_v66.APPROVED_BPRIME_NOTES —— CRO 批准要經代碼改動(會改指紋)")
    if LIVE_PATH != "bt":
        _fail("交易路徑必須係回測驗證版(bt)")
    return True
