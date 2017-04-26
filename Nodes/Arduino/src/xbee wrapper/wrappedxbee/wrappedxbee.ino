#include <Arduino.h>

#include <Printers.h>
#include <XBee.h>

void setup() {

}
void sendMessage(uint8_t[] message, XBeeAddress64 addr1, XBeeAddress64 addr2)
{
XBee xbee = XBee();

// Start the serial port
Serial.begin(9600);
// Tell XBee to use Hardware Serial. It's also possible to use SoftwareSerial
xbee.setSerial(Serial);

// Create an array for holding the data you want to send.
//uint8_t payload[] = { 'H', 'i' };

// Specify the address of the remote XBee (this is the SH + SL)
XBeeAddress64 addr64 = XBeeAddress64(addr1, addr2);

// Create a TX Request
ZBTxRequest zbTx = ZBTxRequest(addr64, message, sizeof(message));

// Send your request
xbee.send(zbTx);
  
}
void loop() {
  // put your main code here, to run repeatedly:

}
