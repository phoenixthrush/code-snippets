cd %userprofile%\Desktop
certutil -encode "%~1" tmp.b64 && findstr /v /c:- tmp.b64 > "%~1".b64
del tmp.b64
