#include "DigiKeyboard_new.h"

void setup() {

  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_D, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("powershell Start");
  DigiKeyboard.delay(50);
  DigiKeyboard.sendKeyStroke(KEY_KPAD_MINUS);
  DigiKeyboard.delay(50);
  DigiKeyboard.print("Process powershell ");
  DigiKeyboard.delay(50);
  DigiKeyboard.sendKeyStroke(KEY_KPAD_MINUS);
  DigiKeyboard.delay(50);
  DigiKeyboard.print("Verb runAs");
  DigiKeyboard.delay(50);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
  DigiKeyboard.delay(50);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);

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

}

void loop() {

  DigiKeyboard.delay(250);
  digitalWrite(0, HIGH);
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(250);
  digitalWrite(0, LOW);
  digitalWrite(1, LOW);

}
