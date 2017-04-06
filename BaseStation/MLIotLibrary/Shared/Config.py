__author__ = 'Stephen'
import configparser
from .Singleton import singleton

@singleton
class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self.baudRate = int(config['serial']['BaudRate'])
        self.radioUsbPort = config['serial']['UsbPort']
        self.port = int(config['api']['Port'])
        self.enableApi = bool(config['api']['EnableApi'])
        self.logMode = int(config['logging']['LogMode'])
        self.useMongo = False
        self.useSql = False
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