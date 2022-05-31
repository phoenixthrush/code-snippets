set WshShell = wscript.createobject("WScript.shell")
WshShell.run """.\trigger.bat"" ", 0, true
