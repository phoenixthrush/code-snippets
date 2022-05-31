Set WshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep(2500)

Dim x
x=1
Do Until x=5

WScript.Sleep(1250)
WshShell.SendKeys "https://youtu.be/yd7AAPyWfsY"
WScript.Sleep(100)
WshShell.SendKeys "{ENTER}"
WScript.Sleep(1250)
WshShell.SendKeys "https://youtu.be/8Lr8b3D3-Ew"
WScript.Sleep(100)
WshShell.SendKeys "{ENTER}"
WScript.Sleep(1250)
WshShell.SendKeys "https://youtu.be/GChzKEeOIxU"
WScript.Sleep(100)
WshShell.SendKeys "{ENTER}"
WScript.Sleep(1250)
WshShell.SendKeys "https://youtu.be/HTKo1pdmg1U"
WScript.Sleep(100)
WshShell.SendKeys "{ENTER}"
WScript.Sleep(1250)
WshShell.SendKeys "https://youtu.be/mdVWUnBDCdQ"
WScript.Sleep(100)
WshShell.SendKeys "{ENTER}"

x=x+1
Loop