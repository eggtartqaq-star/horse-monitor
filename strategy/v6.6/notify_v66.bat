@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
rem Swing V6.6 每日 Telegram 訊息 —— 由 Windows 工作排程器喺美股收市後自動行,唔使撳任何掣
rem 第一步:自我測試;唔過關就傳「今日唔好交易」,唔掃描
python selftest.py > selftest_last.log 2>&1
if errorlevel 1 goto FAILED
python notify_v66.py > notify_last.log 2>&1
if errorlevel 1 goto SCANFAILED
exit /b 0

:FAILED
python notify_v66.py --alert selftest > notify_last.log 2>&1
exit /b 1

:SCANFAILED
rem notify_v66.py 掃描出錯會自己傳警告;冇收到任何訊息 = 當出錯,雙擊 掃描_v66.bat 睇錯誤
exit /b 1
