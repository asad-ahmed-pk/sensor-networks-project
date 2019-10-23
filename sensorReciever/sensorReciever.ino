#include<SoftwareSerial.h>

short xBeeTx = 12;
short xBeeRx = 11;
String temperature;

char data[3]; 

SoftwareSerial xBeeSerial(xBeeRx, xBeeTx);

void setup() {
  Serial.begin(9600);
  xBeeSerial.begin(9600);
}

void loop() 
{
  if(xBeeSerial.available() > 0)
  {
    //temperature = xBeeSerial.readStringUntil('\n');
    //int tempint = temperature.toInt();
    int val = 0;
    int i = 0;
    while (val != 13)
    {
      val = xBeeSerial.read();
      Serial.println(val);
      if (val != 13) {
        data[i] = val;
        i++;
      }
      else {
        data[2] = '\0';
      }
    }

    // string built convert from ASCII
    for (int i = 0; i < 3; i++) {
      //Serial.println(data[i]);
    }

    // discard useless newline
    xBeeSerial.read();
    
    Serial.println();
  }
}
