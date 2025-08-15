void setup() {
  Serial.begin(9600);
  Serial1.setTX(0); // TX(2040) -> TX(LR1262)
  Serial1.setRX(1); // RX(2040) -> TX(LR1262) 
  Serial1.begin(9600);
  //Raspeberry Pi Pico board should be used along with new version of board manager
  //Set Serial monitor baud 
}

void loop() {
  if(Serial.available()) {
    Serial1.write(Serial.read());
  }
  if(Serial1.available()){
    Serial.write(Serial1.read());
  }

}
