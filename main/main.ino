#include <Servo.h>
Servo servo;
int stop = 0;
void setup() {
  servo.attach(3);
  servo.write(90);
  digitalWrite(7, HIGH);
  delay(3000);
  digitalWrite(2, HIGH);
}

void loop() {
  if (stop != 1) {
    if (digitalRead(4) == HIGH) {
      stop = 1;
      digitalWrite(7, LOW);
      digitalWrite(2, LOW);
    }
    servo.write(70);
    delay(512);
    servo.write(110);
    delay(512);
  } else {
    delay(1024);
    if (digitalRead(4) == HIGH) {
      stop = 0;
      digitalWrite(8, HIGH);
      digitalWrite(2, HIGH);
    }
  }
}
