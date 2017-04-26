__author__ = 'Stephen'
from threading import Thread
import json
from .Crypto import Crypt
from collections import namedtuple
from .Schema import Node
from .Schema import SecurityProfile


class MessageConsumer(Thread):
    def __init__(self, msg_q, node_dict, profile_dict, consumer_q=None):
        Thread.__init__(self)
        # setup message consumer
        print('configuring MessageConsumer')
        self._msgq = msg_q
        self._consumer_q = consumer_q
        self.hasConsumer = consumer_q is None
        self.node_dict = node_dict
        self.profile_dict = profile_dict
        self.crypto_manager = Crypt.CryptoManager()

    def run(self):
        while True:
            msg = self._msgq.get()
            self.process_message(msg)

    def process_message(self, msg):
        print('processing message', msg)
        node = self.get_node(msg.msg.get('rf_data'))
        profile = self.get_node(node.id)
        decrypted = self.get_decrypted_data(msg, profile)

    def get_decrypted_data(self, msg, profile):
        return self.crypto_manager.decrypt_message(message=msg.msg['d'], iv=msg.msg['i'], profile=profile)

    def get_node(self, address):
        node = self.node_dict.get(address)
        if node is None:
            node = Node.get_node_by_address(address)
            self.node_dict[address] = node
        return node

    def get_node_profile(self, node_id):
        p = self.profile_dict.get(node_id)
        if p is None:
            p = SecurityProfile.get_security_profile_by_parent_id(node_id)
            self.profile_dict[node_id] = p
        return p


ReceivedMessage = namedtuple('ReceivedMessage', ['type', 'msg'])
ConsumerMessage = namedtuple('ConsumerMessage', ['type', 'origin', 'msg'])
MESSAGE_FIELD = ['iv', 'data', 'signature', 'sender', 'recipients']


class Message:
    def __init__(self, dataIv, dataString, dataSignedHash, senderId, recipientList, nonce):
        self.iv = dataIv
        self.data = {"dataString": dataString, "nonce": nonce, type: 0}
        self.encData = ""
        self.signature = dataSignedHash
        self.sender = senderId
        self.recipients = recipientList

    def validate(self):
        return True

    def getDict(self):
        return {
            'i': self.iv,
            'd': self.encData,
            'sg': self.signature,
            's': self.sender,
            'r': self.recipients

        }

    def prepMessage(self, recipient):
        self.encData = Crypt.CryptoManager.encrypt_message(json.dumps(self.data), recipient)

    def processMessage(self):
        self.data = json.loads(Crypt.CryptoManager.decrypt_message(self.encData, self.iv, self.sender))
