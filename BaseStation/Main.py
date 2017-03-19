from symbol import parameters
from xbee import XBee,ZigBee, python2to3
import serial, threading
from xbee.python2to3 import stringToBytes, intToByte
from MLIotLibrary.MLServer import MLServer
from MLIotLibrary.Shared.Entities.NodeTelemetry import NodeTelemetry
from pymongo import MongoClient
import threading

__author__ = 'Stephen'
print("hello world, we gonna do some cool stuff")

server = MLServer()
server.start()

#spin up xbee handler

#spin up rest thread

#spin up ui thread
#
# def startRestAPI():
#     server = MLServer()
#     server.start()
# thread = threading.Thread(target=startRestAPI)
# thread.start()
#
#
# def foo():
#     #do something here
#     print('from foo')
#
#
# #
# #
# #
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client.Lio
# telemCollection = db.telemetry
#
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
