__author__ = 'Stephen'
import configparser
from MLIotLibrary.RadioService.MLRadioServer import MLRadioServer
from MLIotLibrary.RestApiService.MLApiServer import MLApiServer
import os
from MLIotLibrary.RestApiService import app
from bottle import debug, run
class MLServer:
    def __init__(self):
        self.port = 8080
        self.radioUsbPort = '/dev/cu.usbserial-DN01IUNK'
        self.baudRate = 9600
        self.enableApi = True
        self.logMode = 0
        self.config()

    def config(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self.baudRate = int(config['radio']['BaudRate'])
        self.radioUsbPort = config['radio']['UsbPort']
        self.port = int(config['api']['Port'])
        self.enableApi = bool(config['api']['EnableApi'])
        self.logMode = int(config['logging']['LogMode'])
        try:
            self.useMongo = bool(config['database']['UseMongo'])
        except KeyError as err:
            print('')
        try:
            self.useSql = bool(config['database']['UseSql'])
        except KeyError as err:
            print('missing sql database keys' if not self.useMongo else '')
        try:
            self.ConnectionString = config['database']['MongoConnectionString'] if self.useMongo else config['database']['SqlConnectionString']
        except KeyError as err:
            print('missing database connection key')


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