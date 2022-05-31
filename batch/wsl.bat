@echo off
title WSL Installer Script - Phoenixthrush

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo This tool will install WSL for you!
echo The PC will restart after the installation!
echo After the restart an admin prompt will pop up again, click on "Yes", after that Debian will be getting installed!
echo.
echo It will ask you for a UNIX name, just insert anything you want lmao!
echo Insert the password you want for 2 times and yeah it will be blank if you type!
echo Paste the phoenixsploit install command for linux from the site that will pop up!
echo.
echo Press enter to continue or close the window to exit...

pause >nul

powershell -command "set-executionpolicy remotesigned" >nul

echo aWYgbm90ICIlMSI9PSJhbV9hZG1pbiIgKHBvd2Vyc2hlbGwgc3RhcnQgLXZlcmIgcnVuYXMgJyUwJyBhbV9hZG1pbiAmIGV4aXQgL2IpDQpkZWwgQzpcVXNlcnNcUHVibGljXG1haW4ucHMxDQpzdGFydCAiIiAiaHR0cHM6Ly9naXRodWIuY29tL1Bob2VuaXh0aHJ1c2gvcGhvZW5peHRocnVzaC5naXRodWIuaW8jd2luZG93cyINCndzbCAtLWluc3RhbGwgLWQgRGViaWFuDQpzdGFydCAvYiAiIiBjbWQgL2MgZGVsICIlfmYwIiZleGl0IC9i > start.b64
certutil -decode "start.b64" "start".bat >nul
del start.b64

copy "start.bat" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start.bat" >nul

echo Enable-WindowsOptionalFeature -FeatureName Microsoft-Windows-Subsystem-Linux -Online -NoRestart -OutVariable results > C:\Users\Public\main.ps1
echo if ($results.RestartNeeded -eq $true) { >> C:\Users\Public\main.ps1
echo   Restart-Computer -Force >> C:\Users\Public\main.ps1
echo } >> C:\Users\Public\main.ps1

powershell.exe -ExecutionPolicy Unrestricted -Command ". 'C:\Users\Public\main.ps1'"
