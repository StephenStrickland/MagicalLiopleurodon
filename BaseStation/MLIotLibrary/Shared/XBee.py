__author__ = 'Stephen Strickland'
from xbee import XBee,ZigBee, python2to3
import serial, threading
from serial import SerialException
from xbee.python2to3 import stringToBytes, intToByte
import configparser
import time
from queue import Queue
from MLIotLibrary.Shared.Singleton import singleton
from ..Shared.Schema.Node import *
from MLIotLibrary.Shared.Services.NodeService import NodeService
from collections import namedtuple
from .Messages import ReceivedMessage


class XBeeService:
    def __init__(self):
        self.service = NodeService()

    def sendXbeeMessage(self, addr, data):
        """ Method used to send a message to a node
        Args:
            addr (int): the address of the node
            data (dict): this is the JSON payload that will be sent to the node

        Returns:
            bool: True for successful message send, False otherwise.

        """
        node = get_node_by_address(addr)




    def broadCastMessage(self, data):
        """ Broadcasts a message to every node within the network, regardless of communication method (802.15.4, MQTT,...)
        Args:
            data (dict): this is the JSON payload that will be sent to the node

        Returns:
            bool: True for successful message send, False otherwise.

        """
        return None

@singleton
class XBeeRadioManager:
    def __init__(self):
        print('configuring XBeeRadioManager')
        config = configparser.ConfigParser()
        config.read('lio.config')
        self._serial_port = None
        try:
            self._serial_port = serial.Serial(str(config['serial']['XBeePort']), int(config['serial']['BaudRate']))
        except SerialException:
            print('XBeeRadioManager.init: unable to connect to Serial Device, ensure that the XBeePort is correct in Lio.config')
        self._serial_connected = self._serial_port is not None
        self._xbee = XBee(self._serial_port, escaped=True, callback=self.handleReceivedMessages)
        # self.setMy()
        self.shouldContinue = False
        self.init_queues()
       # self.turn_off_encryption()

    def setup_queues(self, rec_q, send_q):
        self.receive_queue = rec_q


    def turn_off_encryption(self):
        self._xbee.send('at', command='EE', parameter=b'\x00')

    def init_queues(self):
        self.receiveQ = Queue()
        self.sendQ = Queue()

    def set_message_queue(self, q, send_q):
        self.receive_queue = q
        self.message_queue = send_q

    def set_received_worker_callback(self, clb):
        self.r_worker = clb

    def getSendQueue(self):
        return self.sendQ

    def getReceiveQueue(self):
        return self.receiveQ

    def handleReceivedMessages(self, data):
        print('XBeeRadioManager: received message', data)
        parsedMessage = self._parseReceivedMessage(data)
        print(data)
        self.receive_queue.put(ReceivedMessage(type=0, msg=data))


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
        print('xbee worker starting')
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
            # use tx
            tx_type = 'tx'
        self._xbee.send(tx_type, dest_addr=stringToBytes(addr), data=stringToBytes(msg))
