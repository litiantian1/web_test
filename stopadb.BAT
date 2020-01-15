@echo off
title 
tasklist /V|find "adb">nul
if %errorlevel%==0 (
::¹Ø±Õadb·þÎñ
taskkill /F /IM adb.exe
)
