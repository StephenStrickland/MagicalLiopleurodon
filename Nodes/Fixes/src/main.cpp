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
    handleConfig();
  }

}
