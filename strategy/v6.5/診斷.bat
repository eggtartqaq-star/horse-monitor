@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================================
echo  V6.5 免費診斷 —— Tom 話跑呢個行先
echo ============================================================
echo.

python -c "import yfinance,pandas,numpy" 2>nul
if errorlevel 1 (
  echo 第一次跑,裝緊套件...
  python -m pip install -U yfinance pandas numpy
  echo.
)

echo [1/2] 自我測試 —— 確認個模擬器本身冇 bug
echo.
python selftest.py
if errorlevel 1 (
  echo.
  echo ★ 自我測試失敗。唔好用呢個版本跑真數據。
  pause
  exit /b 1
)

echo.
echo [2/2] 診斷 —— 大約 5 分鐘,download 緊 7 年數據
echo.
python portfolio_sim.py --mode diagnostics

echo.
echo ============================================================
echo  睇完先決定使唔使跑模擬。
echo  如果訊號同 EV 集中喺三四隻股身上,生存者偏差就係全部答案。
echo.
echo  下一步(想跑就打):
echo    python portfolio_sim.py --mode sim --broker ibkr_fixed
echo    python portfolio_sim.py --mode sim --broker free
echo ============================================================
pause
