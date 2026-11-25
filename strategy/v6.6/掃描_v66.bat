@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
echo ========================================
echo   Swing V6.6 每日掃描
echo   第一步:自我測試,唔過關唔會掃描
echo ========================================
python selftest.py > selftest_last.log 2>&1
if errorlevel 1 goto FAILED
echo 自我測試通過。
echo.
python daily_scan_v66.py
if errorlevel 1 goto SCANFAILED
echo.
echo 掃描完成,按任意鍵關閉
pause
exit /b 0

:FAILED
echo.
echo [X] 自我測試失敗 —— 今日唔好交易。
echo     將 selftest_last.log 畀 AI 睇,修好之前唔好用任何版本落單。
pause
exit /b 1

:SCANFAILED
echo.
echo [X] 掃描出錯 —— 今日唔好交易。
echo     將上面嘅錯誤訊息畀 AI 睇。
pause
exit /b 1
