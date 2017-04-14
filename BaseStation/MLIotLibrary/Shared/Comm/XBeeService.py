from xbee import XBee,ZigBee, python2to3
import serial, threading
from xbee.python2to3 import stringToBytes, intToByte
import configparser
from queue import Queue
from MLIotLibrary.Shared.Singleton import singleton


@singleton
class XBeeService:
    def __init__(self):
        print('configuring XBeeService')
        config = configparser.ConfigParser()
        config.read('lio.config')
        self._serial_port = None
        self._serial_port = serial.Serial(str(config['serial']['XBeePort']), int(config['serial']['BaudRate']))
        self._xbee = XBee(self._serial_port, shorthand=True, escaped=True, callback=self.handleReceivedMessages)
        # self.setMy()
        self.initQueues()
        self.shouldContinue = False

    def initQueues(self):
        self.receiveQ = Queue()
        self.sendQ = Queue()

    def setMy(self):
        self._xbee.at(frame='A', command=stringToBytes('MY'))
        self._xbee.at( frame_id=stringToBytes('A'), command=stringToBytes('MY'), parameter=b'\x00\x04')
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
        print('Starting XBeeService')
        self.shouldContinue = True
        t = threading.Thread(target=self._worker)
        t.start()

    def stop(self):
        self.shouldContinue = False


    def _parseReceivedMessage(self, msg):
        return {}

    def _parseSendMessage(self, msg):
        return str(msg)

    def _worker(self):
        while self.shouldContinue:
            try:
                while not self.sendQ.empty():
                    messageToSend = self._parseSendMessage(self.sendQ.get())
                    self.sendMessage(2, '{ping:1}')

            except KeyboardInterrupt:
                break

        self._serial_port.close()


    def sendMessage(self, addr, msg):
        tx_type = 'tx_long_addr'
        addr = "00" + addr
        addr = addr.decode('hex')
        if len(addr) == 2:
            #use tx
            tx_type = 'tx'
        self._xbee.send(tx_type, dest_addr=stringToBytes(addr), data=stringToBytes(msg), frame_id=stringToBytes('A'))
