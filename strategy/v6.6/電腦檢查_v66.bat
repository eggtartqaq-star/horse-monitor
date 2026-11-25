@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
echo ========================================
echo   Swing V6.6 電腦檢查:自我測試、對照測試、試掃描
echo   大約 3 至 8 分鐘。唔會落單,唔會改設定。
echo ========================================
python pc_check.py
if errorlevel 1 goto FAILED
echo.
echo 完成。將上面寫住嘅 pc_report 檔傳畀 AI。
pause
exit /b 0

:FAILED
echo.
echo [X] 有項目唔過 —— 今日唔好交易,修好之前唔好用任何版本落單;券商已有嘅止蝕單照留。
echo     將上面寫住嘅 pc_report 檔傳畀 AI;冇 pc_report 檔就將呢個視窗影相傳畀 AI。
pause
exit /b 1
