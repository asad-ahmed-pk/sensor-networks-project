#include<SoftwareSerial.h>

int TMP36 = A0;
int temperature = 0;
int wait_ms = 500;
short xBeeTx = 12;
short xBeeRx = 11;


SoftwareSerial xBeeSerial (xBeeRx, xBeeTx);
void setup() {
  Serial.begin(9600);
  xBeeSerial.begin(9600);
}

void loop() {
  temperature = map(analogRead(TMP36), 0 ,410, -50, 150);
  xBeeSerial.println(temperature);
  Serial.println(temperature);
  delay(wait_ms);
}
