__author__ = 'Stephen Strickland'

from MLIotLibrary.Shared.Comm.XBeeService import XBeeService

class CommunicationService:
    def __init__(self):
        self.XBee = XBeeService()
        self.MQTT = None
        #add mqtt and other relevant services here
