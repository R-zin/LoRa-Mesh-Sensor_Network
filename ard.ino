#include <RadioLib.h>
#include <SPI.h>

#define MASTER_SYNC_NODE_ID 0
#define CURRENT_NODE  //add node number here

#define SLOT_DURATION 200
#define TOTAL_NODES  //total no of nodes in the mesh Network
#define RESYNC_TIME 5000 mus

SX1262 radio = new Module(7,6,4,5,SPI);
boolean transmittedflag = false;

void setup() {
  Serial.begin(9600);
  SPI.begin(8,17,18,7);
  int state = radio.begin(
    868.0,
    125,
    7,
    7,
    0x34,
    22,
    8,
    3.3
  );
  if(state == RADIOLIB_ERR_NONE) {
    Serial.println("LoRa initiation successful");
  }
}
void loop() {

}
