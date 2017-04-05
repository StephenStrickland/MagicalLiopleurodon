
__author__ = 'Stephen Strickland'
from MLIotLibrary.Shared.Respositories.INodeRepo import INodeRepo
from pymongo import MongoClient
from bson.objectid import ObjectId
import configparser
from bson.json_util import dumps
from mongoengine import  connect
from MLIotLibrary.Shared.Schema.Node import MNode


class NodeMongoRepository(INodeRepo):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self.ConnectionString = config['database']['MongoConnectionString']

        connect('Lio', host=self.ConnectionString)

    def get_all_nodes(self):
        return MNode.objects()

    def get_node_by_id(self, id):
        print(id)
        return self.NodeCollection.find_one({'_id': ObjectId(id)})

    def get_node_by_network_address(self, addr):
        return MNode.objects(NetworkAddress=addr);


    def archive_node(self, node):
        self.NodeCollection.update({'_id': id}, {'$set': {'Audit.IsActive': False}})
        return True

    def save_node(self, node):
        result = self.NodeCollection.insert_one(node)
        return {'id':str(result.inserted_id)}


