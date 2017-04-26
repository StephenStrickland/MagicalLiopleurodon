from json import dumps, loads
from ..Schema import Node
from ..Schema import SecurityProfile
from ..Config import Config
from ..Schema import NodeTelemetry
import serial
import time

__author__ = 'Stephen Strickland'


class NodeService:
    def __init__(self, send_q):
        self.send_q = send_q


    def get_all_nodes(self):
        return Node.get_all_nodes()

    def get_node_by_id(self, id):
        return Node.get_node_by_id(id)

    def get_node_by_network_address(self, address):
        return Node.get_node_by_address(address)

    def archive_node(self, id):
        return Node.archive_node(id)

    def update_node(self, node):
        return Node.save_node(node)

    def create_node(self, node):
        return Node.create_node(node)

    def get_all_node_telemtry_by_node_id(self, node_id):
        return NodeTelemetry.get_all_telem_by_node_id(node_id)

    def get_node_telemetry_by_id(self, telem_id):
        return NodeTelemetry.get_telem_by_id(telem_id)

    def create_node_telemetry(self, node_id, data):
        return NodeTelemetry.create_telemetry(node_id, data)

    def send_msg(self, id, msg):
        """ This method handles sending messages to nodes"""
        node = Node.get_node_by_id(id)
        if node is None:
            raise ValueError('Invalid node id')

        profile = SecurityProfile.get_security_profile_by_parent_id(node.id)
        # encrypt message and pipe it to the corresponding queue

    def program_node(self, id):
        node = self.get_node_by_id(id)

        if node is None:
            raise ValueError('NodeService.program_node(), invalid id: ' + str(id))
        sec_profile = SecurityProfile.get_security_profile_by_parent_id(id)
        if sec_profile is None:
            raise ValueError('NodeService.program_node(), node ' + str(id) + ' does not have a SecurityProfile')
        config = Config()

        def dict_to_binary(the_dict):
            str = dumps(the_dict)
            binary = ' '.join(format(ord(letter), 'b') for letter in str)

            return binary

        bports = {x.device: x for x in list(serial.tools.list_ports.comports())}
        print('please plug in device')
        time.sleep(3)
        print('looking for device...')
        aports = {x.device: x for x in list(serial.tools.list_ports.comports())}
        ind = -1
        available = set(aports.keys()) - set(bports.keys())
        print(aports.keys())
        if len(available) == 0:
            print('no device found')
        elif len(available) == 1:
            ind = available.pop()
            print('using', ind, 'port')
        else:
            print('There are {} devices available'.format(len(available)))
            print('\n'.join(available))
            i = input('please enter the index of device')
            ind = list(available)[i]

            # msg = Message('asdf', 'asdf', 'adsf', 'adsf',[1,2,3], 0)

            # profile = Lio.security_profiles.get_security_profile_config_by_parent_id(id)
        # profile['p'] = '0013A2004103DC85'
        profile = {
            'i': id,
            'ph': config.xbee_sh,
            'pl': config.xbee_sl,
            'nk': config.radio_keys,
            'ni': 0,
            'mk': config.message_keys,
            'mi': 0,
            'np': 0,
            'mp': 0,
            'n': 0}
        print('connecting to serial...')
        ser = serial.Serial(ind, 9600)
        print('NODE: ', ser.readline().strip())
        print('NODE: ', ser.readline().strip())
        print('fetching config')
        j = dict_to_binary(profile)
        # input('Execute config write? <Press Enter>')
        print('writing to serial', dumps(profile, separators=(',',':')).strip(" "))
        ser.write(dumps(profile, separators=(',',':')).strip(" ").encode('ascii'))
        ser.flush()
        print('kill code')
        # print(b'\x\r')
        ser.write(b'\r')
        ser.flush()

        print('killing stream', str(b'4'))
        # ser.write(b'4')
        i = 0
        while i < 5:
            line = ser.readline().strip()
            print(line)
            i += 1
            # if line != b'I received:':
            # print(line)
            # print(chr(int(line)))





