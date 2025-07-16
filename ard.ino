#include <RadioLib.h>
#include <SPI.h>

#define MASTER_SYNC_NODE_ID  // This can dynamically change by 
#define CURRENT_NODE_ID  //add node number here

#define SLOT_DURATION 200
#define TOTAL_NODES  //total no of nodes in the mesh Network
#define RESYNC_TIME 5000 // after how much time does the node have to send the resync



SX1262 LoRa = new Module(7,6,4,5,SPI); // pins are set to default of LR1262 module

void setup() {
  Serial.begin(9600);
  SPI.begin(8,17,18,7);
  int state = LoRa.begin( 
    868.0, //Frequency set to Indian standard of 868.0 MHz
    125, //Bandwidth 
    12, //SpreadFactor set to 12 to increase maximum range 
    7, // coding rate
    0x34, // SYNC word for loRa
    22, //output power
    8, //Preamble length
    3.3 //Use TCX0
  );
  if(state == RADIOLIB_ERR_NONE) {
    Serial.println("LoRa initiation successful");
  }
}
void loop() {

}
