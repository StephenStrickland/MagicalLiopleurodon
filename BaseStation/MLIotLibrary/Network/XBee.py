__author__ = 'Stephen Strickland'

from ..Shared.Schema.Node import *

from MLIotLibrary.Shared.Services.NodeService import NodeService
class XBeeCommService:
    def __init__(self):
        self.service = NodeService()

    def sendXbeeMessage(self, addr, data):
        """ Method used to send a message to a node
        Args:
            addr (int): the address of the node
            data (dict): this is the JSON payload that will be sent to the node

        Returns:
            bool: True for successful message send, False otherwise.

        """
        node = get_node_by_address(addr)




    def broadCastMessage(self, data):
        """ Broadcasts a message to every node within the network, regardless of communication method (802.15.4, MQTT,...)
        Args:
            data (dict): this is the JSON payload that will be sent to the node

        Returns:
            bool: True for successful message send, False otherwise.

        """
        return None