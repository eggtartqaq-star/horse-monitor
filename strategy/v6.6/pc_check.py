# -*- coding: utf-8 -*-
"""
V6.6 電腦檢查 —— 喺你部電腦雙擊「電腦檢查_v66.bat」
====================================================
一次過做晒,寫一份報告(pc_report_日期.txt)畀你傳畀 AI:
  1. 環境:Python、pandas、numpy、yfinance、ta 版本
  2. 版本同規則指紋(對照 results/release_stamp.txt)
  3. owner_settings.json 自檢
  4. 記錄簿(ledger/)有咩檔、幾多行、有冇未向 CRO 解釋嘅 S2
  5. 自我測試 selftest.py(關卡 V-2)
  6. 對照測試 parity_check.py(關卡 V-3)—— 要有 dual_engine_v6_4.py 同 ta
  7. 試掃描 daily_scan_v66.py --dry-run(用 yfinance 真數據,唔寫記錄簿)

安全:
  - 唔會落單、唔會連券商(呢個資料夾冇任何落單代碼)
  - 唔會讀 Telegram token 檔、唔會改 owner_settings.json(關卡要你睇完報告、AI/CRO 確認之後自己改)
  - 報告入面你電腦嘅用戶路徑會變成 ~
"""
import glob
import importlib
import os
import platform
import re
import subprocess
import sys
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN_RE = re.compile(r"\d{6,}(:|%3A)[A-Za-z0-9_-]{25,}")


def redact(text, home=None):
    """將用戶路徑變做 ~,同埋(以防萬一)遮住任何似 Telegram token 嘅字串。"""
    home = home or os.path.expanduser("~")
    out = str(text)
    if home and len(home) > 3:
        for h in {home, home.replace("\\", "/"), home.replace("/", "\\")}:
            out = out.replace(h, "~")
    return TOKEN_RE.sub("<TOKEN>", out)


def versions():
    rows = [("Python", platform.python_version()), ("系統", f"{platform.system()} {platform.release()}")]
    for mod in ("pandas", "numpy", "yfinance", "ta"):
        try:
            m = importlib.import_module(mod)
            rows.append((mod, getattr(m, "__version__", "已裝")))
        except Exception:
            rows.append((mod, "未裝"))
    return rows


def stamp():
    sys.path.insert(0, HERE)
    import config_v66 as C
    exp = ""
    p = os.path.join(HERE, "results", "release_stamp.txt")
    if os.path.exists(p):
        exp = open(p, encoding="utf-8").read().strip()
    got = f"{C.VERSION} {C.RELEASE_DATE} {C.fingerprint()}"
    try:
        C.check_config()
        cfg = "✅ 設定自檢通過"
    except BaseException as e:              # ConfigError / SystemExit 都要報
        cfg = f"❌ 設定自檢唔過:{e}"
    return {"got": got, "expected": exp, "match": bool(exp) and got == exp, "config": cfg,
            "settings": C.settings_line()}


def ledger_inventory(folder):
    """記錄簿有咩檔、幾多行;有冇 .bak(舊版升級留低);有冇未解釋 S2。唔改任何檔。"""
    sys.path.insert(0, HERE)
    import ledger_v66 as L
    rows = []
    if not os.path.isdir(folder):
        return {"exists": False, "files": [], "backups": [], "uncleared_s2": []}
    for name in ("signals.csv", "runs.csv", "fills.csv", "s2_clearances.csv", "results.csv"):
        p = os.path.join(folder, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8-sig", errors="replace") as f:
                n = max(sum(1 for _ in f) - 1, 0)
            rows.append((name, n))
    baks = sorted(os.path.basename(b) for b in glob.glob(os.path.join(folder, "*.bak-*")))
    try:
        hold = L.uncleared_s2(folder)
    except BaseException as e:
        hold = [f"讀唔到 fills.csv:{type(e).__name__}"]
    return {"exists": True, "files": rows, "backups": baks, "uncleared_s2": hold}


def run(args, timeout=900, tail=30):
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    try:
        r = subprocess.run([sys.executable] + args, cwd=HERE, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout, env=env)
        out = (r.stdout or "") + (r.stderr or "")
        return r.returncode, out, "\n".join(out.strip().splitlines()[-tail:])
    except subprocess.TimeoutExpired:
        return 124, "", f"超時({timeout} 秒)"


def main():
    now = datetime.now()
    R = []
    say = R.append
    say(f"Swing V6.6 電腦檢查報告  {now:%Y-%m-%d %H:%M}")
    say("=" * 64)

    say("\n【1】環境")
    vs = versions()
    for k, v in vs:
        say(f"  {k:9} {v}")
    vd = dict(vs)
    if vd.get("yfinance") == "未裝":
        say("  ⚠️ 未裝 yfinance → 喺 CMD 打:pip install yfinance pandas numpy requests")
    if vd.get("ta") == "未裝":
        say("  ⚠️ 未裝 ta(對照測試要用)→ 喺 CMD 打:pip install ta")

    say("\n【2】版本同規則指紋")
    st = stamp()
    say(f"  而家:{st['got']}")
    say(f"  應該:{st['expected'] or '(冇 results/release_stamp.txt)'}")
    say(f"  {'✅ 一致' if st['match'] else '❌ 唔一致 —— 代碼唔係呢個版本,先問 AI'}")

    say("\n【3】設定(owner_settings.json)")
    say(f"  {st['config']}")
    say(f"  {st['settings']}")

    say("\n【4】記錄簿(ledger/)")
    inv = ledger_inventory(os.path.join(HERE, "ledger"))
    if not inv["exists"]:
        say("  未有 ledger/ 資料夾(第一次用係正常)")
    for name, n in inv["files"]:
        say(f"  {name:18} {n} 行")
    if inv["backups"]:
        say(f"  舊版升級備份:{', '.join(inv['backups'])}")
    say(f"  未向 CRO 解釋嘅 S2:{', '.join(inv['uncleared_s2']) or '冇'}")

    say("\n【5】自我測試 selftest.py(關卡 V-2)")
    print("自我測試中(大約 1 分鐘)……")
    rc, out, tail = run(["selftest.py"], tail=8)
    n_ok, n_bad = out.count("✅"), out.count("❌")
    v2 = rc == 0 and "全部通過" in out
    say(f"  結果:{'✅ 全部通過' if v2 else '❌ 唔過'}({n_ok} 項過,{n_bad} 項唔過,exit {rc})")
    if not v2:
        say("  ---- 最後幾行 ----")
        say("\n".join("  " + x for x in [ln for ln in out.splitlines() if "❌" in ln][:20] + tail.splitlines()))

    say("\n【6】對照測試 parity_check.py(關卡 V-3)")
    v3 = None
    if not os.path.exists(os.path.join(HERE, "dual_engine_v6_4.py")):
        say("  未做:資料夾入面冇 dual_engine_v6_4.py。")
        say("  做法:將你 V6.4.2 資料夾嘅 dual_engine_v6_4.py 複製入嚟(唔好改佢),再雙擊一次。")
    elif vd.get("ta") == "未裝" or vd.get("yfinance") == "未裝":
        say("  未做:要先裝 ta 同 yfinance(見【1】)。")
    else:
        print("對照測試中(要下載 3 年數據,大約 2 至 5 分鐘)……")
        rc, out, tail = run(["parity_check.py"], tail=30)
        v3 = rc == 0
        say(f"  結果:{'✅ 過關' if v3 else '❌ 唔過'}(exit {rc})")
        say("\n".join("  " + x for x in tail.splitlines()))

    say("\n【7】試掃描 daily_scan_v66.py --dry-run(真數據,唔寫記錄簿)")
    if vd.get("yfinance") == "未裝":
        say("  未做:未裝 yfinance。")
        scan_ok = None
    else:
        print("試掃描中(大約 1 至 2 分鐘)……")
        rc, out, tail = run(["daily_scan_v66.py", "--dry-run"], tail=40)
        scan_ok = rc == 0
        say(f"  結果:{'✅ 完成' if scan_ok else '❌ 出錯'}(exit {rc})")
        say("\n".join("  " + x for x in tail.splitlines()))

    say("\n" + "=" * 64)
    say("總結")
    say(f"  V-2 自我測試:{'✅' if v2 else '❌'}   V-3 對照測試:{'✅' if v3 else ('❌' if v3 is False else '未做')}   "
        f"試掃描:{'✅' if scan_ok else ('❌' if scan_ok is False else '未做')}   指紋:{'✅' if st['match'] else '❌'}")
    say("  下一步:將呢份報告傳畀 AI。AI / CRO 睇完確認之後,先喺 owner_settings.json 將")
    say('  "V2_代碼測試"(同埋過咗嘅話 "V3_對照測試")改做 true(唔好加引號)。唔好改 config_v66.py。')
    say("  呢個程式冇落單、冇連券商、冇讀 Telegram token、冇改任何設定。")

    text = redact("\n".join(R))
    path = os.path.join(HERE, f"pc_report_{now:%Y%m%d-%H%M}.txt")
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(text + "\n")
    print(text)
    print(f"\n報告已寫入:{redact(path)}  —— 將呢個檔傳畀 AI。")
    return 0 if (v2 and st["match"]) else 1


if __name__ == "__main__":
    sys.exit(main())
