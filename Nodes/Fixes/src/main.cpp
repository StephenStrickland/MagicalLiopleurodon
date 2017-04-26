/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"
#include "EEPROM.h"
#include <ArduinoJson.h>
#include <Printers.h>
#include <XBee.h>


#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif

#define CONFIG_TRIGGER_PIN 5

XBee xbee;

ConfigFile config;

/** Struct of the JSON config file
 *
 */
typedef struct
{
	uint8_t i[256];
	uint8_t ph[136];
	uint8_t pl[136];
	uint8_t nk[5][168];
	uint8_t ni;
	uint8_t mk[5][168];
	uint8_t mi;
	uint8_t np;
	uint8_t mp;
	uint8_t n;
} ConfigFile;

void handleConfig()
{
	uint16_t length = 0;

	uint8_t incomingChar = 0;
	Serial.println("Entered configuration mode");
	Serial.println("Waiting on config file...");

	uint8_t config[320];

	while(true)
	{
		if(Serial.available() > 0)
		{
			incomingChar = Serial.read();
			//carriage return is the last char in the config stream, exit loop
			if(incomingChar == '\r')
				break;
			else
			{
				//write the uint8_t to config to be passed into the deserialization handler
				config[length++] = incomingChar;
				//make the max size of the code to be 0xffff in size.
				if(length+1 > 0xFFFF)
				{
					Serial.println("Error! The config file is to large! Needs to be less than 65535 bytes.");
					return;
				}
			}
		}
	}

	writeEEPROMConfig(config,length);

	Serial.println("File ending acknowledged, writing to non-volatile memory");
	Serial.println(length);

	Serial.println("complete");
}

void sendMessage()
{

}

void sendATCommand()
{

}

/** sends AT Command to XBee radio
 *
 */
void sendAtCommand(AtCommandRequest req)
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

/** configures XBee radio
 * sets up radio level encryption
 */
void configureXBee()
{
	//Encryption Enable
	uint8_t eeCmd[] = {'E', 'E'};
	//Turn on EE
	uint8_t eeVal[] = {1};
	//Encryption Key
	uint8_t kyCmd[] = {'K', 'Y'};
	//Write commands to non-volatile memory
	uint8_t wrCmd[] = {'W', 'R'};
	//Default key, for now.
	uint8_t key[] = {'t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'k', 'e', 'y', '1', '2', '3'};

	AtCommandRequest atRequest = AtCommandRequest();
	delay(5000);
	atRequest.setCommand(eeCmd);
	atRequest.setCommandValue(eeVal);
	atRequest.setCommandValueLength(1);
	sendAtCommand(atRequest);
	atRequest.clearCommandValue();
	atRequest.setCommand(kyCmd);
	atRequest.setCommandValue(key);
	atRequest.setCommandValueLength(16);
	sendAtCommand(atRequest);
	atRequest.clearCommandValue();

	atRequest.setCommand(wrCmd);
	sendAtCommand(atRequest);
	//  delete atRequest;

}

void writeEEPROMConfig(uint8_t* json, uint16_t jsonDataSize)
{
	DynamicJsonBuffer jsonBuffer(jsonDataSize);

	JsonObject& root = jsonBuffer.parseObject(json);

	config.i = root["i"];
	config.ph = root["ph"];
	config.pl = root["pl"];

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

void readEEPROMConfig()
{
	EEPROM.get(0, configFile);
}

void setup()
{
	// initialize LED digital pin as an output.
	pinMode(LED_BUILTIN, OUTPUT);

	//init our serial setup
	Serial.begin(9600);

	//if this pin is low, trigger handleConfig()
	pinMode(CONFIG_TRIGGER_PIN, INPUT_PULLUP);
	if(digitalRead(CONFIG_TRIGGER_PIN) == LOW)
		handleConfig();
}

void loop()
{
}
