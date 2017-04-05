from xbee import XBee,ZigBee, python2to3
import serial, threading
from xbee.python2to3 import stringToBytes, intToByte
import configparser
from queue import Queue
from MLIotLibrary.Shared.Singleton import singleton


@singleton
class XBeeService:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self._serial_port = serial.Serial(config['serial']['XBeePort'], int(config['serial']['BaudRate']))
        self._xbee = XBee(self.serial_port, shorthand=True, escaped=True, callback=self.handleReceivedMessages)
        self.setMy()
        self.initQueues()
        self.shouldContinue = False

    def initQueues(self):
        self.receiveQ = Queue()
        self.sendQ = Queue()

    def setMy(self):
        self._xbee.at(frame='A', command=stringToBytes('MY'))
        self.at( frame_id=stringToBytes('A'), command=stringToBytes('MY'), parameter=b'\x00\x04')
        response = self._xbee.wait_read_frame()

    def getSendQueue(self):
        return self.sendQ

    def getReceiveQueue(self):
        return self.receiveQ


    def handleReceivedMessages(self, data):
        parsedMessage = self._parseReceivedMessage(data)
        print(data)
        self.receiveQ.put(parsedMessage)


    def start(self):
        self.shouldContinue = True
        while self.shouldContinue:
            try:
                while not self.sendQ.empty():
                    messageToSend = self._parseSendMessage(self.sendQ.get())
                    self._xbee.send('api', ) # more to this

            except KeyboardInterrupt:
                break

        self._serial_port.close()

    def _parseReceivedMessage(self, msg):
        return {}

    def _parseSendMessage(self, msg):
        return {}







    #
# serial_port = serial.Serial('/dev/cu.usbserial-DN01IOL6', 9600)
# xbee = XBee(serial_port, shorthand=True, escaped=True)
#
# #xbee.at(frame='A', command=stringToBytes('MY'))
# xbee.at( frame_id=stringToBytes('A'), command=stringToBytes('MY'), parameter=b'\x00\x04')
#
# response = xbee.wait_read_frame()
# print(response)
#
# while True:
#     try:
#         print(xbee.wait_read_frame())
#         telem = NodeTelemetry()
#         telem.Data['open'] = 1
#         telemCollection.insert_one(telem.__dict__)
#     except KeyboardInterrupt:
#         break
#
# serial_port.close()