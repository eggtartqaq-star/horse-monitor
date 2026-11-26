@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ========================================
echo   建立每日 Telegram 訊息排程
echo   星期二至六 早上 06:30 香港時間 = 美股收市後
echo ========================================
schtasks /Create /TN SwingV66Morning /SC WEEKLY /D TUE,WED,THU,FRI,SAT /ST 06:30 /TR "\"%~dp0notify_v66.bat\"" /F
if errorlevel 1 goto FAILED
echo.
echo 完成。之後喺「工作排程器」搵 SwingV66Morning,剔:
echo   1. 喚醒電腦以執行此工作
echo   2. 錯過排程時間之後盡快執行
echo 想刪除:schtasks /Delete /TN SwingV66Morning /F
pause
exit /b 0

:FAILED
echo.
echo [X] 建立排程失敗 —— 用「工作排程器」手動建立,步驟見 電腦待辦清單.md G 部分。
pause
exit /b 1
