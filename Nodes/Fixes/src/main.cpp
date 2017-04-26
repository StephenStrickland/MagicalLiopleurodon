/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"
#include <ArduinoJson.h>
#include "EEPROM.h"

#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif


#define CONFIG_TRIGGER_PIN 5

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

uint16_t getConfigLength()
{
  int configLength = 0;
  EEPROM.get(0, configLength);
  return configLength;
}

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
      {
        break;
      }
      else
      {
        //write the uint8_t to config to be passed into the deserialization handler
        config[length] = incomingChar;
        incomingChar++;

				//make the max size of the code to be 0xffff in size.
				if(length+1 > 0xFFFF)
				{
					Serial.println("Error! The config file is to large! Needs to be less than 65535 bytes.");
					return;
				}
      }
    }
  }

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

void setup()
{
  // initialize LED digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);

	//init our serial setup
	Serial.begin(9600);

	//grab the length t
}

void loop()
{
  pinMode(CONFIG_TRIGGER_PIN, INPUT_PULLUP);

  //if this pin is low, trigger handleConfig()
  if(digitalRead(CONFIG_TRIGGER_PIN) == LOW)
  {
    handleConfig();
  }

}
