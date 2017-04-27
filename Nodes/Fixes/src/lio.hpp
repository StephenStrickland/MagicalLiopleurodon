#ifndef LIO_HPP
#define LIO_HPP

#include "EEPROM.h"
#include <ArduinoJson.h>
#include <XBee.h>

/**
 * Struct of the JSON config file
 */
typedef struct
{
	char i[27];
	char ph[11];
	char pl[11];
	char nk[5][16];
	uint8_t ni;
	char mk[5][16];
	uint8_t mi;
	uint8_t np;
	uint8_t mp;
	uint8_t n;
} ConfigFile;


/**
 * This is the amazing lio library
 * Lio was built for security, simplicity, and extensibility
 */
class Lio
{
public:
  void sendInt(int val);
  void sendDouble(double val);
	void sendId();
  void setup(bool triggerSerialRead);
private:
  void configureXBee();
  void sendAtCommand(AtCommandRequest req);
  void readEEPROMConfig();
  void writeEEPROMConfig(uint8_t* json, uint16_t jsonDataSize);
  void handleConfig();
  XBee xbee;
	ConfigFile config;


};



#endif
