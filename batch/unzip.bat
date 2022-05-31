@echo off

:: setting the password
set /p pass="enter the password: "
cls

:: unzipping the zip file via 7z
.\data\7z\7za.exe x ".\data\zip\v3.zip" -p"%pass%" -o./container >nul 2>&1
IF ERRORLEVEL 1 goto wrongpass

:: opening the folder via explorer
start .\container\340301.mp4
start .\container\340302.mp4
start .\container\340305.mp4
start .\container\340306.mp4
start .\container\345888.mp4
start .\container\345889.mp4
start .\container\345896.mp4
start .\container\348292.mp4
start .\container\348293.mp4
start .\container\348294.mp4
start .\container\348296.mp4
start .\container\367927.mp4
start .\container\367928.mp4
start .\container\367932.mp4

echo waiting until you closed the photo app to clean up
timeout 3 >nul

:: checking if the photo viewer process runs
:loop
tasklist | find /i "Microsoft.Photos.exe" >nul 2>&1
if ERRORLEVEL 1 (
	del /s /q ".\container" >nul 2>&1
	rmdir ".\container" >nul 2>&1
	exit
) else (
  goto loop
)

:wrongpass

del /s /q ".\container" >nul 2>&1
rmdir ".\container" >nul 2>&1

echo wrong password
pause >nul
exit