if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
rmdir "%programdata%\Microsoft\Windows Defender\Scans\History\Service" /S /Q