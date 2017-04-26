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



void handleConfig()
{
  int endingIndex = 1;
  byte incomingByte = 0;
  Serial.println("Entered configuration mode");
  Serial.println("Waiting on config file...");

  while(true)
  {
    if(Serial.available() > 0)
    {
      incomingByte = Serial.read();
      //carriage return is the last char in the config stream, exit loop
      if(incomingByte == '\r')
      {
        delay(50);
        break;
      }
      else
      {
        //write the byte as a uint8_t to EEPROM
        EEPROM.write(endingIndex, (uint8_t)incomingByte);
        endingIndex++;
      }
    }
  }

  Serial.println("File ending acknowledged, writing to non-volatile memory");
  Serial.println(endingIndex);
  int remaining = (endingIndex + 1) - 255 > 0 ? (endingIndex + 1) - 255 : 0;
  //write out the length to the first two bytes in EEPROM
  EEPROM.write(0, remaining == 0 ? (endingIndex + 1) : 255);
  EEPROM.write(1, remaining);
  Serial.println("calculating length");
  int configLength = 0;
  configLength = (int)EEPROM.read(0) + (int)EEPROM.read(1);
  Serial.println("bout to print");
  Serial.println(configLength);
  for (int i = 0; i < configLength; i++)
  {
    // print out each char to serial, basically confirms the config file to the
    // Base Station
    Serial.print((char)EEPROM.read(i + 2));
  }
  Serial.print("\r\n");

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
}

void loop()
{
  Serial.begin(9600);
  pinMode(CONFIG_TRIGGER_PIN, INPUT_PULLUP);

  //if this pin is low, trigger handleConfig()
  if(digitalRead(CONFIG_TRIGGER_PIN) == LOW)
  {
    Serial.println("Handling Config");
    handleConfig();
  }

}
