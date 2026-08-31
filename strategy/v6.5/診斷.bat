@echo off
chcp 65001 >nul
cd /d "%~dp0"
setlocal enabledelayedexpansion

REM ── 輸出經 pipe 嗰陣,Python 唔會用 console code page,而係 fallback 去
REM    locale 預設(英文版 Windows = cp1252),一 print 中文即刻炒。
REM    .py 入面已經有 reconfigure 做保險,呢兩行係雙保險。
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

echo ============================================================
echo  V6.5 免費診斷 —— Tom 話跑呢個行先
echo ============================================================
echo.
echo  工作資料夾: %CD%
echo.

REM ── 預檢 ──────────────────────────────────────────────
REM 上次就係喺呢度炒:.bat 喺 Downloads,但係 .py 唔喺同一個資料夾,
REM 結果 PowerShell 掉返一堆睇唔明嘅嘢出嚟。而家自己查清楚先。
set MISSING=
for %%F in (rules.py risk_config.py portfolio_sim.py selftest.py) do (
  if not exist "%%F" (
    if exist "%%F.txt" (
      echo   自動改名: %%F.txt  ^-^>  %%F
      ren "%%F.txt" "%%F"
    ) else (
      set MISSING=!MISSING! %%F
    )
  )
)

if not "!MISSING!"=="" (
  echo ★ 呢個資料夾入面搵唔到呢啲檔案:
  echo    !MISSING!
  echo.
  echo   五個檔案要放晒喺**同一個資料夾**入面。
  echo   而家呢個資料夾入面有:
  echo   ------------------------------------------------------
  dir /b *.py 2>nul
  dir /b *.txt 2>nul
  dir /b *.bat 2>nul
  echo   ------------------------------------------------------
  echo.
  echo   最穩陣嘅做法:開一個新資料夾,例如 C:\v65\
  echo   將六個檔案全部放入去,再喺嗰度撳 run_diagnostics.bat。
  echo   唔好留喺 Downloads —— 嗰度好易有「selftest (1).py」呢類重複檔案。
  echo.
  pause
  exit /b 1
)

REM 用 python 產生檔名 —— %DATE% 嘅格式跟系統地區設定變,靠唔住。
for /f %%i in ('python -c "import datetime;print(datetime.date.today().isoformat())" 2^>nul') do set STAMP=%%i
if "%STAMP%"=="" set STAMP=undated
set OUT=v65_diagnostics_%STAMP%.txt

echo  輸出會同時寫入:  %OUT%
echo  跑完之後將呢個檔案傳返畀 CEO 就得,唔使喺 console 度抄。
echo.

python --version >nul 2>&1
if errorlevel 1 (
  echo ★ 搵唔到 python。請先裝 Python 3,安裝時記得剔 "Add to PATH"。
  pause
  exit /b 1
)

python -c "import yfinance,pandas,numpy" 2>nul
if errorlevel 1 (
  echo 第一次跑,裝緊套件...
  python -m pip install -U yfinance pandas numpy
  echo.
)

echo [1/2] 自我測試 —— 確認個模擬器本身冇 bug
echo.
powershell -NoProfile -Command "python selftest.py 2>&1 | Tee-Object -FilePath '%OUT%'; exit $LASTEXITCODE"
if errorlevel 1 (
  echo.
  echo ★ 自我測試失敗 —— 唔好用呢個版本跑真數據。
  echo   請將 %OUT% 傳返畀 CEO。
  pause
  exit /b 1
)

echo.
echo [2/2] 診斷 —— 大約 5 分鐘,download 緊 7 年數據
echo.
powershell -NoProfile -Command "python portfolio_sim.py --mode diagnostics 2>&1 | Tee-Object -FilePath '%OUT%' -Append"

echo.
echo ============================================================
echo  完成。全部輸出喺:  %OUT%
echo.
echo  ★ 睇兩樣嘢:
echo    1) 牛市日數佔比 —— 如果超過 80%%,你嘅「4年數據」其實只係
echo       一個環境嘅4年,獨立證據遠少過你以為。
echo    2) 訊號集中度 —— 如果訊號集中喺三四隻股身上,生存者偏差
echo       就係全部答案。唔使再建其他嘢,直接去買 point-in-time 數據。
echo.
echo  下一步(睇完覺得值得跑先好跑):
echo    python portfolio_sim.py --mode compare
echo ============================================================
pause
