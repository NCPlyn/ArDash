#include <Keypad.h>

int layout = 0;

const byte ROWS = 6;
const byte COLS = 5;

char hexaKeys[ROWS][COLS] = {
  {'N','/','*','|','|'},  //{'N','/','*','|','|'},
  {'1','2','3','E','|'},  //{'1','2','3','E','|'},
  {'4','5','6','|','B'},  //{'4','5','6','|','B'},
  {'7','8','9','+','|'},  //{'7','8','9','+','|'},
  {'|','0','.','|','|'},  //{'|','0','.','|','|'},
  {'|','|','-','|','|'}   //{'|','|','-','|','|'}
};
byte rowPins[ROWS] = {3, 5, 6, 7, 4, 2};
byte colPins[COLS] = {9, 10, 11, 12, 8};

Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){
  pinMode(13,OUTPUT);
  digitalWrite(13, LOW);
  Serial.begin(9600);
}
  
void loop(){
  char customKey = customKeypad.getKey();

  if (customKey){
    Serial.print(customKey);
  }

  if (Serial.available() > 0) {
    if(Serial.read() == 49){
      Serial.print("K");
      if(layout == 0) {
        digitalWrite(13, LOW);
        layout = 1;
      } else {
        digitalWrite(13, HIGH);
        layout = 0;
      }
    }
  }
}
