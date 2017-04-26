#include <ArduinoJson.h>

#include <SoftwareSerial.h>

#include <EEPROM.h>

#include <Printers.h>
#include <XBee.h>

#include <AESLib.h>
byte incomingByte = 0;
volatile bool cm=false;
JsonObject* confJ = NULL;
XBee xbee = XBee();
AtCommandRequest atRequest = AtCommandRequest();
AtCommandResponse atResponse = AtCommandResponse();
uint8_t ssRX = 8;
// Connect Arduino pin 9 to RX of usb-serial device
uint8_t ssTX = 9;
// Remember to connect all devices to a common Ground: XBee, Arduino and USB-Serial device
//SoftwareSerial nss(ssRX, ssTX);
/*void configCrypt()
{
  //Serial.begin(9600);
  //randomSeed(analogRead(0));
  uint8_t key[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
  uint8_t iv[] = {(uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255)};
  char data[] = "0123456789012345384729834723895798327598798759837423987589759759723957329857290472907109375923753094730948093490750947230970925723907530975slkflkfenl;kgngjkrhfkrhfjkshfkehfekfhekjfhhrslkedkfhkgeklejilfjlrifjelfewkfhehekgjkghukghuhfughreughrkhrkheukgrhkuuhgkehrhgihfihfoihfoihgeoifhiohewoighweioewrhewioheoi09237329075"; //16 chars == 16 bytes
  Serial.println(data);
  int len = (sizeof(data) / sizeof(char));
  int origlen = len;
  Serial.println(len);
  int padding = 16 - (len % 16);
  if (padding > 0)
  {
    len += padding;
  }
  Serial.println(len);
  char paddedData[len];
  for (int i = 0; i < len; i++)
  {
    if (i < origlen)
    {
      paddedData[i] = data[i];
    }
    else
    {
      paddedData[i] = 'F';
    }
  }
  Serial.println(paddedData);
  unsigned long starttime = millis();
  aes128_cbc_enc(key, iv, paddedData, len);
  Serial.print("encrypted:");
  Serial.println(paddedData);
  unsigned long elapsed;
  elapsed = millis() - starttime;
  String Str1 = "Operation time: ";
  Str1 += (int)elapsed;
  Serial.println(Str1);
  starttime = millis();
  aes128_cbc_dec(key, iv, paddedData, len);
  Serial.print("decrypted:");
  Serial.println(paddedData);
  elapsed = millis() - starttime;
  String Str2 = "Operation time: ";
  Str2 += (int)elapsed;
  Serial.println(Str2);

}
*/
void sendMessage(uint8_t message[], int leng)
{
  char msgCpy[leng];
  for(int i=0;i<leng;i++)
  {
    msgCpy[i]=message[i];
  }
  StaticJsonBuffer<200> jsonBuffer;
JsonObject& root = jsonBuffer.createObject();
JsonObject& data = jsonBuffer.createObject();
data["dataString"] = msgCpy;
//JsonObject& prof = *confJ;
Serial.println("");
(*confJ).printTo(Serial);
Serial.println("");
(*confJ)["n"].printTo(Serial);
data["nonce"] = (int)(&(*confJ)["n"]);
String output;

Serial.println("\ngetting to data");
data.printTo(output);
Serial.println(output);
char buf[output.length()+1];
output.toCharArray(buf,output.length()+1); 

Serial.println(sizeof(buf));
//root["d"]= encMsg(buf,sizeof(buf));
root["d"]=output;

root["i"]="this is an iv456";
root["sg"]="na";
String sId;
(*confJ)["s"].printTo(sId);
root["s"]=sId;
//String ph;
//String pl;
//ph+=pl;
root["r"] ="0";
String payloadstr;
root.printTo(payloadstr);
char payload[payloadstr.length()];
payloadstr.toCharArray(payload, payloadstr.length());




  
}
void writeConfig()
{
  //noInterrupts();
  int index = 0;
  Serial.println("Entered configuration mode");
  Serial.println("Waiting on config file...");
  uint8_t cfg[EEPROM.length()];
  //Serial.begin(9600);
  //Serial2.begin(9600);
  // Serial.println("goodbye cruel world");

  while (true)
  {
    if (Serial.available() > 0) {
      // read the incoming byte:
      incomingByte = Serial.read();
      Serial.print((char)incomingByte);
      // say what you got:
      if (incomingByte == '\r')
      {
        Serial.println("szechuan sauce");
        delay(100);
        break;
      }
      else
      {
        cfg[index] = (uint8_t)incomingByte;
        index++;
      }
      //Serial.println("I received: ");
      //Serial.println(incomingByte);

    }
  }
  Serial.println("File ending acknowledged, writing to non-volatile memory");
  delay(100);
  Serial.println(index);
  delay(100);
  
  //byte pt1=
  EEPROM.write(0, (index + 1));
  for (int i = 1; i < index + 2; i++)
  {
    EEPROM.write(i, cfg[i - 1]);
  }
  int leng =329;
  delay(100);
  Serial.println(leng);
  for (int i = 1; i <leng+1; i++)
  {
    //Serial.println(i);
    Serial.print((char)EEPROM.read(i));
  }
  Serial.print("\r\n");
  //Serial.println("meh");
  //Serial.println(leng);
  Serial.println("complete");
  //int leng = EEPROM.read(0);
  //Serial.println(conf);
  //interrupts();
  //delay(3000);
  //exit(0);
}

void setup() {
 

  Serial.begin(9600);
  //configCrypt();
  int interruptPin = 5;
  //interrupts();
  pinMode(interruptPin, INPUT_PULLUP);
  if (digitalRead(interruptPin) == LOW)
  {
      for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
  }
    cm=true;
    writeConfig();

  }
  else
  {
  xbee.setSerial(Serial);
  //attachInterrupt(digitalPinToInterrupt(interruptPin), writeConfig, RISING);
  //Serial.println("the program ran at least to the interrupt config");
  const int leng = 320;

  char conf[320];

  for (int i = 1; i < leng + 1; i++)
  {
    conf[i-1] = EEPROM.read(i);
    Serial.print(conf[i-1]);
  }
  delay(100);
  Serial.println("");
  //conf[leng]=NULL;
  delay(100);
  Serial.println(sizeof(conf));
  String strconfs(conf);
  delay(100);
  Serial.println(conf);
  delay(100);
  DynamicJsonBuffer jsonBuffer;
  confJ = &jsonBuffer.parseObject(conf);
  Serial.println("the object");
  (*confJ).printTo(Serial);
  //delete *jsonBuffer;


  uint8_t eeCmd[] = {'E', 'E'};
  
  
  uint8_t eeVal[] = {1};
  uint8_t kyCmd[] = {'K', 'Y'};
  uint8_t wrCmd[] = {'W', 'R'};
  //uint8_t[] key= conf["NK"][(int)conf["NI"]];
  uint8_t key[] = {'t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'k', 'e', 'y', '1', '2', '3'};
  atRequest = AtCommandRequest();
  delay(5000);
  atRequest.setCommand(eeCmd);
  atRequest.setCommandValue(eeVal);
  atRequest.setCommandValueLength(1);
  sendAtCommand();
  atRequest.clearCommandValue();
  atRequest.setCommand(kyCmd);
  atRequest.setCommandValue(key);
  atRequest.setCommandValueLength(16);
  sendAtCommand();
  atRequest.clearCommandValue();

  atRequest.setCommand(wrCmd);
  sendAtCommand();
//  delete atRequest;
  
  }

}

void loop() {
  // Create an XBee object at the top of your sketch



  // Start the serial port
  if(!cm)
  {
  //Serial.begin(9600);
  delay(1000);
  //Serial.println("beep");
  // Tell XBee to use Hardware Serial. It's also possible to use SoftwareSerial


  // Create an array for holding the data you want to send.
  uint8_t payload[] = { 'H', 'i' };

/*XBeeAddress64 addr64 = XBeeAddress64(0x0013a200, 0x4103dc72);
  // Create a TX Request
  Tx64Request zbTx = Tx64Request(addr64, payload, sizeof(payload));

  // Send your request
  xbee.send(zbTx);*/
    sendMessage(payload, 2);
    


  }

}



void sendAtCommand() {
  Serial.println("Sending command to the XBee");

  // send the command
  xbee.send(atRequest);

  // wait up to 5 seconds for the status response
  if (xbee.readPacket(5000)) {
    // got a response!

    // should be an AT command response
    if (xbee.getResponse().getApiId() == AT_COMMAND_RESPONSE) {
      xbee.getResponse().getAtCommandResponse(atResponse);

      if (atResponse.isOk()) {
        Serial.print("Command [");
        Serial.print(atResponse.getCommand()[0]);
        Serial.print(atResponse.getCommand()[1]);
        Serial.println("] was successful!");

        if (atResponse.getValueLength() > 0) {
          Serial.print("Command value length is ");
          Serial.println(atResponse.getValueLength(), DEC);

          Serial.print("Command value: ");

          for (int i = 0; i < atResponse.getValueLength(); i++) {
            Serial.print(atResponse.getValue()[i], HEX);
            Serial.print(" ");
          }

          Serial.println("");
        }
      }
      else {
        Serial.print("Command return error code: ");
        Serial.println(atResponse.getStatus(), HEX);
      }
    } else {
      Serial.print("Expected AT response but got ");
      Serial.print(xbee.getResponse().getApiId(), HEX);
    }
  } else {
    // at command failed
    if (xbee.getResponse().isError()) {
      Serial.print("Error reading packet.  Error code: ");
      Serial.println(xbee.getResponse().getErrorCode());
    }
    else {
      Serial.print("No response from radio");
    }
  }
}
/*uint8_t* encMsg(char data[], int leng)
{
  
  randomSeed(analogRead(0));
 String strkey= *(&(*confJ)["mk"][0].as<String>());
 Serial.println(strkey);
 char key[16];
  strkey.toCharArray(key, 17);
  Serial.println(key);
  uint8_t iv[] = {(uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255), (uint8_t)random(255)};
  Serial.println(data);
  int len = leng;
  int origlen = len;
  Serial.println(len);
  int padding = 16 - (len % 16);
  Serial.println(padding);
  if (padding > 0)
  {
    len += padding;
  }
  Serial.println(len);

  
  
    //char data1[] = "0123456789012345384729834723895798327598798759837423987589759759723957329857290472907109375923753094730948093490750947230970925723907530975slkflkfenl;kgngjkrhfkrhfjkshfkehfekfhekjfhhrslkedkfhkgeklejilfjlrifjelfewkfhehekgjkghukghuhfughreughrkhrkheukgrhkuuhgkehrhgihfihfoihfoihgeoifhiohewoighweioewrhewioheoi09237329075"; //16 chars == 16 bytes
  

  
  char paddedData[len];
  for (int i = 0; i < len; i++)
  {
    if (i < origlen)
    {
      paddedData[i] = data[i];
    }
    else
    {
      paddedData[i] = 'F';
      Serial.println(paddedData[i]);
    }
  }
  Serial.println(origlen);
  Serial.println(paddedData[origlen-1]);
  paddedData[origlen-1]='F';
  paddedData[len]=NULL;
  Serial.println(sizeof(paddedData));
  Serial.println(paddedData);
          Serial.println("1");
  
 delay(5000);
  unsigned long starttime = millis();

  aes128_cbc_enc(key, iv, paddedData, len);
  Serial.println(paddedData);    
  delay(5000);
  return paddedData;
}

*/

