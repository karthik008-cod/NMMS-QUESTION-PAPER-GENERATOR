@echo off
title NMMS 180-Question Paper Generator Web Interface
cd /d "%~dp0"
echo ======================================================================
echo   NMMS MENTAL ABILITY TEST - 180 QUESTION PAPER GENERATOR WEB APP
echo ======================================================================
echo Starting server and launching browser at http://127.0.0.1:5000 ...
echo Press Ctrl+C in this window anytime to stop the server.
echo ======================================================================
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:5000
python nmms_webapp.py
pause
