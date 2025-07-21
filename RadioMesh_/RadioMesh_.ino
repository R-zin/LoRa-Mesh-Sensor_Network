#include <RadioHead.h>
#include <RH_SX126x.h>
#include <RHMesh.h>
/*
#CAUTION: Have not adjust default value of driver class 

*/


RH_SX126x LoRa = new RH_SX126x(, // Slave pin
                               , //interupt pn
                               , // LoRa busypin
                               , // LoRa reset pin
                               );
RHMesh manager(LoRa,); // address to be filled 
void setup() {
  Serial.begin(9600);
  manager.setFrequency(868.0); // set the LoRa module to 868 Indian Frequency 
  boolean LoRa_initialization_status = manager.init();
  if (LoRa_initialization_status  == true) {
    Serial.print("LoRa initalized successfully");
  }

}

void loop() {
  while(true) {
    uint8_t data[] = "hi";
    if(manager.sendtoWait(data,sizeof(data),/* Final address of end node here */) == RH_ROUTER_ERROR_NONE) {
      Serial.print("Packet Send Successfully");
    }
  }

}

