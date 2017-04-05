__author__ = 'Stephen Strickland'

import configparser
from MLIotLibrary.Shared.Respositories.NodeMongoRepository import NodeMongoRepository


class NodeService:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self.db = NodeMongoRepository()
        if True:
            print('stuff')

    def get_all_nodes(self):
        return self.db.get_all_nodes()

    def get_node_by_id(self, id):
        return self.db.get_node_by_id(id)

    def get_node_by_network_address(self, address):
        return self.db.get_node_by_network_address(address)

    def archive_node(self, id):
        return self.db.archive_node(id)

    def save_node(self, node):
        return self.db.save_node(node)

