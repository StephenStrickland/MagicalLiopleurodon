from symbol import parameters
from xbee import XBee,ZigBee, python2to3
import serial, threading
# from MLIotLibrary.Shared.Comm.XBeeService import XBeeService
from xbee.python2to3 import stringToBytes, intToByte
from MLIotLibrary.Shared.Entities.NodeProfile import NodeProfile
from MLIotLibrary.MLServer import MLServer
# from MLIotLibrary.Shared.Entities.NodeTelemetry import NodeTelemetry
# from pymongo import MongoClient
# import threading
# from mongoengine import *
# from MLIotLibrary.Shared.Config import Config
# from MLIotLibrary.Shared.Schema import Node

# config = Config()
# connect('Lio', alias='default', host=config.ConnectionString)
# node = Node.MNode(NodeType=1, Name='Test Node', NetworkAddress=1,)
# node.save()


__author__ = 'Stephen'
print("hello world, we gonna do some cool stuff")


n = NodeProfile()
print(n.__dict__)
print(len(str(n.__dict__).replace(" ", "").encode('utf-8')))


SH = "13A200"
SL = "4103DC85"
SHSL = SH + SL

#
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

# serial_port = serial.Serial('/dev/tty.usbserial-DN01IOL6', 9600)
# xbee = XBee(serial_port, shorthand=True, escaped=True)
#
# xbee.at(frame_id=stringToBytes('A'), command=stringToBytes('MY'))
# # xbee.at( frame_id=stringToBytes('A'), command=stringToBytes('MY'), parameter=b'\x00\x04')
# # xbee.send('tx_long_addr', dest_addr=b'\x00\x41\x03\xDC\x85\x13\xA2\x00', data=b'{ping=1}', frame_id=stringToBytes('A'))
# response = xbee.wait_read_frame()
# print(response)
#
# while True:
#     try:
#         print(xbee.wait_read_frame())
#
#     except KeyboardInterrupt:
#         break
#
# serial_port.close()



#
# xbee = XBeeService()
# xbee.start()

#
# msg = ""
# while msg !=  "q":
#     msg = input('Message to send')
#
