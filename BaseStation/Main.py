from symbol import parameters
from xbee import XBee,ZigBee, python2to3
import serial, threading
from xbee.python2to3 import stringToBytes, intToByte
from MLIotLibrary.MLServer import MLServer

__author__ = 'Stephen'
print("hello world, we gonna do some cool stuff")

server = MLServer()
server.start()

#spin up xbee handler

#spin up rest thread

#spin up ui thread


#
#
#
# serial_port = serial.Serial('/dev/cu.usbserial-DN01IUNK', 9600)
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
#     except KeyboardInterrupt:
#         break
#
# serial_port.close()