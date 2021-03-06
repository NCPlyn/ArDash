void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(2)==LOW){
    Serial.print("1");
    while(digitalRead(2)==LOW) {}
    delay(100);
  } else if (digitalRead(3)==LOW){
    Serial.print("2");
    while(digitalRead(3)==LOW) {}
    delay(100);
  } else if (digitalRead(4)==LOW){
    Serial.print("3");
    while(digitalRead(4)==LOW) {}
    delay(100);
  } else if (digitalRead(5)==LOW){
    Serial.print("4");
    while(digitalRead(5)==LOW) {}
    delay(100);
  }
}
