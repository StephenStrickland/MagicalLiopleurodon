#include "Arduino.h"
#include "EEPROM.h"
#include <ArduinoJson.h>
#include <Printers.h>
#include <XBee.h>

#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif

#define CONFIG_TRIGGER_PIN 5

/** Struct of the JSON config file
 *
 */
typedef struct
{
	uint8_t i[24];
	uint8_t ph[8];
	uint8_t pl[8];
	uint8_t nk[5][16];
	uint8_t ni;
	uint8_t mk[5][16];
	uint8_t mi;
	uint8_t np;
	uint8_t mp;
	uint8_t n;
} ConfigFile;

XBee xbee;

ConfigFile config;

void writeEEPROMConfig(uint8_t* json, uint16_t jsonDataSize)
{
	DynamicJsonBuffer jsonBuffer(jsonDataSize);

	JsonObject& root = jsonBuffer.parseObject(json);


  JsonArray& i = root["i"];
  root["i"].printTo(Serial);
  i.copyTo((char)config.i);
  for (size_t i = 0; i < 24; i++) {
    Serial.print(config.i[i]);
  }
  JsonArray& ph = root["ph"];
  ph.copyTo(config.ph);
  JsonArray& pl = root["pl"];
  pl.copyTo(config.pl);
  // config.i = root["i"];
	// config.ph = root["ph"];
	// config.pl = root["pl"];

	JsonArray& nk = root["nk"];
	nk.copyTo(config.nk[0]);
	nk.copyTo(config.nk[1]);
	nk.copyTo(config.nk[2]);
	nk.copyTo(config.nk[3]);

	config.ni = root["ni"];

	JsonArray& mk = root["mk"];
	mk.copyTo(config.mk[0]);
	mk.copyTo(config.mk[1]);
	mk.copyTo(config.mk[2]);
	mk.copyTo(config.mk[3]);

	config.mi = root["mi"];
	config.np = root["np"];
	config.mp = root["mp"];
	config.n = root["n"];

	//write the EEPROM data.
	EEPROM.put(0, config);
}

ConfigFile readEEPROMConfig()
{
	ConfigFile configFile;

	EEPROM.get(0, configFile);

	return configFile;
}

void handleConfig()
{
	uint16_t length = 0;

	// uint8_t incomingChar = 0;
	Serial.println("Entered configuration mode");
	Serial.println("Waiting on config file...");

	String config;

	while(true)
	{
		if(Serial.available() > 0)
		{
        config = Serial.readStringUntil('\r');
        break;
			// char incomingChar = Serial.read();
      // delay(1);
			// //carriage return is the last char in the config stream, exit loop
			// if(incomingChar == '\r')
			// 	break;
			// else
			// {
      //   Serial.println("got it");
			// 	//write the uint8_t to config to be passed into the deserialization handler
			// 	config += incomingChar;
      //   length++;
      //   delay(10);
      //   Serial.println(incomingChar);
			// 	//make the max size of the code to be 0xffff in size.
			// 	if(length+1 > 0xFFFF)
			// 	{
			// 		Serial.println("Error! The config file is to large! Needs to be less than 65535 bytes.");
			// 		return;
			// 	}
			// }
		}
	}
  length = config.length();
	writeEEPROMConfig((uint8_t*)&config[0],length);

	Serial.println("File ending acknowledged, writing to non-volatile memory");
	Serial.println(length);

	Serial.println("complete");
}

void sendMessage(uint8_t message[], int length)
{
  // char msgCpy[length];
  //   for(int i=0;i<length;i++)
  //   {
  //     msgCpy[i]=message[i];
  //   }
  //   StaticJsonBuffer<200> jsonBuffer;
//create json object

//manually set each object
//if message level encryption, encrypt message
//else, set d: {d:message, n:nonce, type: 0system, 1user}
//{i:iv, d:^^^, sg:signature, s:sender, r:recipients [0 for system, list for multiple recipients]}

  //  JsonObject& root = jsonBuffer.createObject();
  //  JsonObject& data = root.createNestedObject("d");
  // data['d'] = message;

  // JsonObject& data = jsonBuffer.createObject();
  // data["dataString"] = msgCpy;
  // //JsonObject& prof = *confJ;
  // Serial.println("");
  // (*confJ).printTo(Serial);
  // Serial.println("");
  // (*confJ)["n"].printTo(Serial);
  // data["nonce"] = (int)(&(*confJ)["n"]);
  // String output;
  //
  // Serial.println("\ngetting to data");
  // data.printTo(output);
  // Serial.println(output);
  // char buf[output.length()+1];
  // output.toCharArray(buf,output.length()+1);
  //
  // Serial.println(sizeof(buf));
  // //root["d"]= encMsg(buf,sizeof(buf));
  // root["d"]=output;
  //
  // root["i"]="this is an iv456";
  // root["sg"]="na";
  // String sId;
  // (*confJ)["s"].printTo(sId);
  // root["s"]=sId;
  // //String ph;
  // //String pl;
  // //ph+=pl;
  // root["r"] ="0";
  // String payloadstr;
  // root.printTo(payloadstr);
  // char payload[payloadstr.length()];
  // payloadstr.toCharArray(payload, payloadstr.length());

}

/** sends AT Command to XBee radio
 *
 */
// void sendAtCommand(AtCommandRequest req)
// {
// 	Serial.println("Sending command to the XBee");
// 	AtCommandResponse atResponse = AtCommandResponse();
// 	// send the command
// 	xbee.send(req);
//
// 	// wait up to 5 seconds for the status response
// 	if(xbee.readPacket(5000))
// 	{
// 		// got a response!
//
// 		// should be an AT command response
// 		if(xbee.getResponse().getApiId() == AT_COMMAND_RESPONSE)
// 		{
// 			xbee.getResponse().getAtCommandResponse(atResponse);
//
// 			if(atResponse.isOk())
// 			{
// 				Serial.print("Command [");
// 				Serial.print(atResponse.getCommand()[0]);
// 				Serial.print(atResponse.getCommand()[1]);
// 				Serial.println("] was successful!");
//
// 				if(atResponse.getValueLength() > 0)
// 				{
// 					Serial.print("Command value length is ");
// 					Serial.println(atResponse.getValueLength(), DEC);
//
// 					Serial.print("Command value: ");
//
// 					for(int i = 0; i < atResponse.getValueLength(); i++)
// 					{
// 						Serial.print(atResponse.getValue()[i], HEX);
// 						Serial.print(" ");
// 					}
//
// 					Serial.println("");
// 				}
// 			}
// 			else
// 			{
// 				Serial.print("Command return error code: ");
// 				Serial.println(atResponse.getStatus(), HEX);
// 			}
// 		}
// 		else
// 		{
// 			Serial.print("Expected AT response but got ");
// 			Serial.print(xbee.getResponse().getApiId(), HEX);
// 		}
// 	}
// 	else
// 	{
// 		// at command failed
// 		if(xbee.getResponse().isError())
// 		{
// 			Serial.print("Error reading packet.  Error code: ");
// 			Serial.println(xbee.getResponse().getErrorCode());
// 		}
// 		else
// 			Serial.print("No response from radio");
// 	}
// }
//
// /** configures XBee radio
//  * sets up radio level encryption
//  */
// void configureXBee()
// {
//   //Encryption Enable
//   uint8_t eeCmd[] = {'E', 'E'};
//   //Turn on EE
//   uint8_t eeVal[] = {1};
//   //Encryption Key
//   uint8_t kyCmd[] = {'K', 'Y'};
//   //Write commands to non-volatile memory
//   uint8_t wrCmd[] = {'W', 'R'};
//   //Default key, for now.
//   uint8_t key[] = {'t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'k', 'e', 'y', '1', '2', '3'};
//   AtCommandRequest atRequest = AtCommandRequest();
//   //turn on encryption
//   atRequest.setCommand(eeCmd);
//   atRequest.setCommandValue(eeVal);
//   atRequest.setCommandValueLength(1);
//   sendAtCommand(atRequest);
//   //set encryption key
//   atRequest.clearCommandValue();
//   atRequest.setCommand(kyCmd);
//   atRequest.setCommandValue(key);
//   atRequest.setCommandValueLength(16);
//   sendAtCommand(atRequest);
//   atRequest.clearCommandValue();
//   //tell xbee to write vals to non-volatile memory
//   atRequest.setCommand(wrCmd);
//   sendAtCommand(atRequest);
// }

void setup()
{
	// initialize LED digital pin as an output.
	pinMode(LED_BUILTIN, OUTPUT);

	//init our serial setup
	Serial.begin(9600);
  delay(500);
  Serial.println("spun up");

	//if this pin is low, trigger handleConfig()
	pinMode(CONFIG_TRIGGER_PIN, INPUT_PULLUP);
  Serial.println(digitalRead(CONFIG_TRIGGER_PIN) == LOW);
  if(digitalRead(CONFIG_TRIGGER_PIN) == LOW)
    handleConfig();
  ConfigFile conf = readEEPROMConfig();
  Serial.println("config stuff");
  for (size_t i = 0; i < 20; i++) {
    Serial.print(config.i[i]);
    /* code */
  }

}

void loop()
{


    // Serial.println("spun up");
}
