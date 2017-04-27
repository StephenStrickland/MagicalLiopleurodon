#include "Arduino.h"
#include "EEPROM.h"
#include <ArduinoJson.h>
#include <Printers.h>
#include <XBee.h>

#define CONFIG_TRIGGER_PIN 5

/** Struct of the JSON config file
 *
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

XBee xbee;


ConfigFile config;

int freeRam ()
{
  extern int __heap_start, *__brkval;
  int v;
  return (int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval);
}

void printFreeRam()
{
  Serial.print("free ram: ");
  Serial.print(freeRam());
  Serial.println("");
}


void writeEEPROMConfig(uint8_t* json, uint16_t jsonDataSize)
{
  printFreeRam();
	DynamicJsonBuffer jsonBuffer(jsonDataSize);
  printFreeRam();
	JsonObject& root = jsonBuffer.parseObject(json);
  printFreeRam();
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

	// config.ni = root["ni"];

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

void readEEPROMConfig()
{
	EEPROM.get(0, config);
}

void handleConfig()
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
	writeEEPROMConfig((uint8_t*)&c, c.length());

	Serial.println("File ending acknowledged, writing to non-volatile memory");
	Serial.println(length);
  Serial.println(config.i);

	Serial.println("complete");
}


/**
 * The only way that this can work is if we first
 * serialize message then add that as a nested object to root
 * @param message [description]
 * @param length  [description]
 */
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

/**
 * Send an integer to the Base Station
 * @param val The integer to send
 */
void sendInt(int val)
{
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  JsonObject&  data = root.createNestedObject("d");
  data["v"] = val;
  JsonArray& recipients = root.createNestedArray("r");
  recipients.add(0);
  root["t"] = 1;
  uint8_t payload[root.measureLength()];
  root.printTo((char*) payload, root.measureLength());
  XBeeAddress64 baseStationAddress = XBeeAddress64(0x0013a200, 0x4103dc72);
  Tx64Request req = Tx64Request(baseStationAddress, payload, sizeof(payload));
  xbee.send(req);
}

/**
 * Sends the specified request to the xbee radio
 * @param req : the request to send
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
  xbee.setSerial(Serial);
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

/**
 * Sets up the library
 * @param triggerConfig if true, reads config from Serial
 */
void lioSetup(bool triggerConfig)
{
  if(triggerConfig)
    handleConfig();
  else
  {
    readEEPROMConfig();

    configureXBee();
  }
}





/**
 * Arduini setup func
 */
void setup()
{

	// initialize LED digital pin as an output.
	pinMode(LED_BUILTIN, OUTPUT);

	//init our serial setup
	Serial.begin(9600);
  delay(500);
  Serial.println("spun up");
  printFreeRam();

	//if this pin is low, trigger handleConfig()
	pinMode(CONFIG_TRIGGER_PIN, INPUT_PULLUP);
  lioSetup(digitalRead(CONFIG_TRIGGER_PIN) == LOW);


  Serial.println("config stuff");
  Serial.println(sizeof(config.i));
  Serial.println(config.i);
  Serial.println(config.ph);
  Serial.println(config.pl);
  Serial.println(config.nk[0]);

}

/**
 * data loop here
 */
void loop()
{
  if(digitalRead(CONFIG_TRIGGER_PIN) == HIGH)
  {
    sendInt(123);
    delay(200);
  }
}
