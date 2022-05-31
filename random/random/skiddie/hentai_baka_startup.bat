@echo off

cd %userprofile%\AppData\Roaming\Microsoft\Windows\Start^ Menu\Programs\Startup\

if exist "uh.bat" (
  del .\uh.bat > nul
  echo Deleted!
  echo Press Enter to exit!
  pause > nul
  exit
) else (
  del .\uh.bat > nul
  echo start ^"^" ^"https://www.youtube.com/watch?v=5TGgJQgDf68^" > .\uh.bat
  exit
)