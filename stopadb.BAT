@echo off
title 
tasklist /V|find "adb">nul
if %errorlevel%==0 (
::�ر�adb����
taskkill /F /IM adb.exe
)
