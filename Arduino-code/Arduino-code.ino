#include <Keypad.h>

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
  Serial.begin(9600);
}
  
void loop(){
  char customKey = customKeypad.getKey();
  
  if (customKey){
    Serial.print(customKey);
  }
}
