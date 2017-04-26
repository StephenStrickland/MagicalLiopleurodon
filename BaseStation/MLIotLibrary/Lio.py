__author__ = 'Stephen'

from mongoengine import connect

from .Shared.Singleton import singleton
from .Shared.Services.NodeService import NodeService
from.Shared.Services.SecurityProfileService import SecurityProfileService
from .Shared.Messages import MessageConsumer
from multiprocessing import Manager
from multiprocessing import Queue
from .Shared.Config import Config
from .Shared.XBee import XBeeRadioManager


@singleton
class Lio:
    def __init__(self):
        self._msg_queue = Queue()
        self._send_queue = Queue()
        self.nodes = NodeService(self._send_queue)
        self.manager = Manager()
        self.security_profiles = SecurityProfileService()
        config = Config()
        connect('Lio', alias='default', host=config.ConnectionString)
        config.update_host_id()

    def setup(self, **kwargs):
         self._setup_consumer(kwargs)

    def _setup_consumer(self, kwargs):
        self._node_cache = self.manager.dict()
        self._profile_cache = self.manager.dict()
        self._xbee_manager = XBeeRadioManager()
        self._xbee_manager.set_message_queue(self._msg_queue, self._send_queue)
        self._xbee_manager.start()
        consumer = MessageConsumer(self._msg_queue, self._node_cache, self._profile_cache, kwargs.get('message_queue'))
        consumer.start()




