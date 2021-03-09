void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(2)==LOW){
    Serial.print("01");
    while(digitalRead(2)==LOW) {}
    delay(100);
  } else if (digitalRead(3)==LOW){
    Serial.print("02");
    while(digitalRead(3)==LOW) {}
    delay(100);
  } else if (digitalRead(4)==LOW){
    Serial.print("03");
    while(digitalRead(4)==LOW) {}
    delay(100);
  } else if (digitalRead(5)==LOW){
    Serial.print("04");
    while(digitalRead(5)==LOW) {}
    delay(100);
  }
}
