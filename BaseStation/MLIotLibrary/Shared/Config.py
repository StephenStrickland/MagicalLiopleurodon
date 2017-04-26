__author__ = 'Stephen'
import configparser
from .Singleton import singleton
import json
from .Schema import Host
from .Schema import SecurityProfile

@singleton
class Config:
    def __init__(self):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read('lio.config')
        self.baudRate = int(config['serial']['BaudRate'])
        self.radioUsbPort = config['serial']['XBeePort']
        self.xbee_sh = config['serial']['XBeeSH']
        self.xbee_sl = config['serial']['XBeeSL']
        self.port = int(config['api']['Port'])
        self.enableApi = bool(config['api']['EnableApi'])
        self.logMode = int(config['logging']['LogMode'])
        self.useMongo = False
        self.useSql = False
        self.host_id = config['host']['Id']
        self.has_host_id = self.host_id is not None
        self.enable_radio_aes = config.getboolean(section='host', option='EnableRadioAES')
        self.radio_keys = json.loads(config['host']['RadioKeys'])
        self.enable_message_aes = config.getboolean(section='host', option='EnableRadioAES')
        self.message_keys = json.loads(config['host']['RadioKeys'])
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



    def updateId(self, id):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read('lio.config')
        id_str = str(id)
        config.set('host', 'Id', id_str)
        with open(r'lio.config', 'w') as configFile:
            config.write(configFile)

    def update_host_id(self):
        host = Host.get_hosts().first()
        if host is None:
            h = {'Name': 'LioHost',
                 'EnableApi': self.enableApi,
                 'Port': self.port,
                 'BaudRate': self.baudRate,
                 'XBeePort':self.radioUsbPort}
            # write host config
            id = Host.create_host(h)
            self.updateId(id)

            profile = {
                'ParentId': id,
                'ParentType': 2,
                'NetworkEncryptionMethod': 1,
                'MessageEncryptionMethod': 1,
                'NetworkKeys': self.radio_keys,
                'NetworkIndex': 0,
                'MessageKeys': self.message_keys,
                'MessageIndex': 0,
                'PreviousMessageIndex': 0,
                'PreviousNetworkIndex': 0,
                'PublicKey': '',
                'PrivateKey': '',
                'RSAEnabled': True,
                'CurrentNonce': 0
            }
            sec_p = SecurityProfile.get_security_profile_by_parent_id(id)

            if sec_p is None:
                SecurityProfile.create_security_profile(profile)

        elif not self.has_host_id and self.host_id != host.id:
            self.updateId(host.id)
