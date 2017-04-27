#include "lio.hpp"

/**
 * Send an integer to the Base Station
 * @param val The integer to send
 */
void Lio::sendInt(int val)
{
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  JsonObject&  data = root.createNestedObject("d");
  data["v"] = val;
  JsonArray& recipients = root.createNestedArray("r");
  recipients.add(0);
  root["t"] = 1;
  uint8_t payload[root.measureLength() + 1];
  root.printTo((char*) payload, root.measureLength() + 1);
  XBeeAddress64 baseStationAddress = XBeeAddress64(0x0013a200, 0x4103dc72);
  Tx64Request req = Tx64Request(baseStationAddress, payload, sizeof(payload));
  xbee.send(req);
}

/**
 * Send an integer to the Base Station
 * @param val The integer to send
 */
void Lio::sendDouble(double val)
{
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  JsonObject&  data = root.createNestedObject("d");
  data["v"] = val;
  JsonArray& recipients = root.createNestedArray("r");
  recipients.add(0);
  root["t"] = 1;
  uint8_t payload[root.measureLength() + 1];
  root.printTo((char*) payload, root.measureLength() + 1);
  XBeeAddress64 baseStationAddress = XBeeAddress64(0x0013a200, 0x4103dc72);
  Tx64Request req = Tx64Request(baseStationAddress, payload, sizeof(payload));
  xbee.send(req);
}


void Lio::sendId()
{
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  root["i"] = config.i;
  root["t"] = 0;
  uint8_t payload[root.measureLength() + 1];
  root.printTo((char*) payload, root.measureLength() + 1);
  XBeeAddress64 baseStationAddress = XBeeAddress64(0x0013a200, 0x4103dc72);
  Tx64Request req = Tx64Request(baseStationAddress, payload, sizeof(payload));
  xbee.send(req);
}

/**
 * Sets up the library
 * @param triggerConfig if true, reads config from Serial
 */

void Lio::configureXBee()
{
  xbee.setSerial(Serial);
  //Encryption Enable
  uint8_t eeCmd[] = {'E', 'E'};
  //Turn on EE
  uint8_t eeVal[] = {1};
  //Set MY, so that the radio will use 64bit address or SH + SL
  uint8_t myCmd[] = {'M', 'Y'};
  //Turn on EE
  uint8_t myVal[] = {'F', 'F', 'F', 'F'};
  //Encryption Key
  uint8_t kyCmd[] = {'K', 'Y'};
  //Write commands to non-volatile memory
  uint8_t wrCmd[] = {'W', 'R'};
  //Default key, for now.
  uint8_t key[] = {'t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'k', 'e', 'y', '1', '2', '3'};
  AtCommandRequest atRequest = AtCommandRequest();
  //set MY key
  Serial.println("sending MY");
  atRequest.setCommand(myCmd);
  atRequest.setCommandValue(myVal);
  atRequest.setCommandValueLength(4);
  sendAtCommand(atRequest);
  atRequest.clearCommandValue();
  //turn on encryption
  Serial.println("sending EE");
  atRequest.setCommand(eeCmd);
  atRequest.setCommandValue(eeVal);
  atRequest.setCommandValueLength(1);
  sendAtCommand(atRequest);
  //set encryption key
  atRequest.clearCommandValue();
  Serial.println("sending KY");
  atRequest.setCommand(kyCmd);
  atRequest.setCommandValue(key);
  atRequest.setCommandValueLength(16);
  sendAtCommand(atRequest);
  atRequest.clearCommandValue();
  //tell xbee to write vals to non-volatile memory
  //Serial.println("sending WR");
  atRequest.setCommand(wrCmd);
  sendAtCommand(atRequest);
}

void Lio::handleConfig()
{
	uint16_t length = 0;

	// uint8_t incomingChar = 0;
	Serial.println("Entered configuration mode");
	Serial.println("Waiting on config file...");

	String c;
	while(true)
	{
		if(Serial.available() > 0)
		{
        c = Serial.readStringUntil('\r');
				break;
		}
	}
  Serial.println(c);
	writeEEPROMConfig((uint8_t*)&c[0], c.length());

	Serial.println("File ending acknowledged, writing to non-volatile memory");
	Serial.println(length);
  Serial.println(config.i);

	Serial.println("complete");
}


void Lio::setup(bool triggerSerialRead)
{
  if(triggerSerialRead)
  {
    handleConfig();
  }
  else
  {
    readEEPROMConfig();
    configureXBee();
    sendId();
  }
}


/**
 * Sends the specified request to the xbee radio
 * @param req : the request to send
 */
void Lio::sendAtCommand(AtCommandRequest req)
{
	Serial.println("Sending command to the XBee");
	AtCommandResponse atResponse = AtCommandResponse();
	// send the command
	xbee.send(req);

	// wait up to 5 seconds for the status response
	if(xbee.readPacket(5000))
	{
		// got a response!

		// should be an AT command response
		if(xbee.getResponse().getApiId() == AT_COMMAND_RESPONSE)
		{
			xbee.getResponse().getAtCommandResponse(atResponse);

			if(atResponse.isOk())
			{
				Serial.print("Command [");
				Serial.print(atResponse.getCommand()[0]);
				Serial.print(atResponse.getCommand()[1]);
				Serial.println("] was successful!");

				if(atResponse.getValueLength() > 0)
				{
					Serial.print("Command value length is ");
					Serial.println(atResponse.getValueLength(), DEC);

					Serial.print("Command value: ");

					for(int i = 0; i < atResponse.getValueLength(); i++)
					{
						Serial.print(atResponse.getValue()[i], HEX);
						Serial.print(" ");
					}

					Serial.println("");
				}
			}
			else
			{
				Serial.print("Command return error code: ");
				Serial.println(atResponse.getStatus(), HEX);
			}
		}
		else
		{
			Serial.print("Expected AT response but got ");
			Serial.print(xbee.getResponse().getApiId(), HEX);
		}
	}
	else
	{
		// at command failed
		if(xbee.getResponse().isError())
		{
			Serial.print("Error reading packet.  Error code: ");
			Serial.println(xbee.getResponse().getErrorCode());
		}
		else
			Serial.print("No response from radio");
	}
}

void Lio::readEEPROMConfig()
{
	EEPROM.get(0, config);
}

void Lio::writeEEPROMConfig(uint8_t *json, uint16_t jsonDataSize)
{
	DynamicJsonBuffer jsonBuffer(jsonDataSize);
	JsonObject& root = jsonBuffer.parseObject(json);
  char temp[26];
  Serial.println("hello world");
  Serial.println(root.success());
  root["i"].printTo(temp);
  char * s = temp;
  s++;
  strcpy(config.i, s);
  char t[10];

  root["ph"].printTo(t, 10);
  s = t;
  s++;
  strcpy(config.ph, s);
  root["pl"].printTo(t, 10);
  s = t;
  s++;
  strcpy(config.pl, s);
  delete s;


	JsonArray& nk = root["nk"];
	nk.copyTo(config.nk[0]);
	// nk.copyTo(config.nk[1]);
	// nk.copyTo(config.nk[2]);
	// nk.copyTo(config.nk[3]);
  //
	// config.ni = root["ni"];
  //
	// JsonArray& mk = root["mk"];
	// mk.copyTo(config.mk[0]);
	// mk.copyTo(config.mk[1]);
	// mk.copyTo(config.mk[2]);
	// mk.copyTo(config.mk[3]);
  //
	// config.mi = root["mi"];
	// config.np = root["np"];
	// config.mp = root["mp"];
	// config.n = root["n"];
  // Serial.println(config.i);

	//write the EEPROM data.
	EEPROM.put(0, config);
  Serial.println(config.i);
}
