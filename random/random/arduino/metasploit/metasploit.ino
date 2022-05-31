#include <Keyboard.h>

void setup() {
  // put your setup code here, to run once:
  Keyboard.press(KEY_LEFT_GUI);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(250);
  digitalWrite(0, HIGH);
  digitalWrite(1, HIGH);
  delay(250);
  digitalWrite(0, LOW);
  digitalWrite(1, LOW);
}
