#include <BluetoothSerial.h>
BluetoothSerial bt;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(19,OUTPUT);
  if(!bt.begin("ESP32_BT"))
  {
    Serial.println("bluetooth failed to start");
  }
  else{
  Serial.println("bluetooth started");
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available())
  {
    bt.write(Serial.read());
  }
  if(bt.available())
  {
    char c=bt.read();                                                                                                                                                                                                                                                                                           
    if (c=='1')
  {
    digitalWrite(19,HIGH);
  }
  else if(c=='0')
  {
    digitalWrite(19,LOW);

  }
  }
}
