goto check_Permissions

:check_Permissions
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo hi > C:\Users\hentai\Downloads\admin.txt
    ) else (
        echo hi > C:\Users\hentai\Downloads\no-admin.txt
    )