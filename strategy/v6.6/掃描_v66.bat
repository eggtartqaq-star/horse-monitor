@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
echo ========================================
echo   Swing V6.6 每日掃描
echo   (第一步:自我測試;唔過關唔會掃描)
echo ========================================
python selftest.py > selftest_last.log 2>&1
if errorlevel 1 (
  echo.
  echo [X] 自我測試失敗 —— 今日唔掃描。打開 selftest_last.log 睇原因,畀 AI 睇。
  echo     臨時可以用返舊版:掃描.bat(V6.4.2)
  pause
  exit /b 1
)
echo 自我測試通過。
echo.
python daily_scan_v66.py
echo.
echo (掃描完成,按任意鍵關閉)
pause
