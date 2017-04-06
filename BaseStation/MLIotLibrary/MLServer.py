__author__ = 'Stephen'
import configparser
from MLIotLibrary.RadioService.MLRadioServer import MLRadioServer
from MLIotLibrary.RestApiService.MLApiServer import MLApiServer
import os
from .Shared.Config import Config
from MLIotLibrary.RestApiService import app
from bottle import debug, run
class MLServer:
    def __init__(self):
        self.port = 8080
        self.radioUsbPort = '/dev/cu.usbserial-DN01IUNK'
        self.baudRate = 9600
        self.enableApi = True
        self.logMode = 0
        self.config = Config()




    def start(self):
        #start api
        self.startApi()

        #start radio
        self.startRadio()

    def startApi(self):
        if self.enableApi:
            print('starting rest api on port {}'.format(self.port))
            #start rest api in new thread
            debug(True)
           # if __name__ == '__main__':
            #port = int(os.environ.get("PORT", self.port))
            port = self.port
            run(app, reloader=True, host='localhost', port=port)

            # apiServer = MLApiServer(self.port)
            # apiServer.start()

    def startRadio(self):
        try:
            print('connecting to radio at {}'.format(self.radioUsbPort))
        except IOError:
            print('error connecting to radio at {}'.format(self.radioUsbPort))