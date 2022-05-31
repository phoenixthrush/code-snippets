cd %userprofile%\Desktop
certutil -decode "%~1" "%~1".decoded
del "%~1"
