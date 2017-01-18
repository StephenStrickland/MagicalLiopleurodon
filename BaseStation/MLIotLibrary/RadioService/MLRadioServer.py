__author__ = 'Stephen'
from symbol import parameters
from xbee import XBee,ZigBee, python2to3
import serial, threading
from xbee.python2to3 import stringToBytes, intToByte
class MLRadioServer:
    def __init__(self, usbPort, baudRate):
        self.baudRate = 9600
        if baudRate > 0:
            self.baudRate = baudRate
        self.usbRadioPort = usbPort
        self.serial_port = serial.Serial(self.usbRadioPort, 9600)
        self.xbee = XBee(self.serial_port, shorthand=True, escaped=True)
        print('initializing radio server')

    def start(self):

        print('starting radio server')

