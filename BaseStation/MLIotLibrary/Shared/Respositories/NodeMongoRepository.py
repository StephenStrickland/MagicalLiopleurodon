
__author__ = 'Stephen Strickland'
from MLIotLibrary.Shared.Respositories.INodeRepo import INodeRepo
from pymongo import MongoClient
from bson.objectid import ObjectId
import configparser
from bson.json_util import dumps


class NodeMongoRepository(INodeRepo):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self.ConnectionString = config['database']['MongoConnectionString']
        self.NodeCollection = MongoClient(self.ConnectionString).Lio.Nodes

    def get_all_nodes(self):
        return self.NodeCollection.find()

    def get_node_by_id(self, id):
        print(id)
        return self.NodeCollection.find_one({'_id': ObjectId(id)})

    def archive_node(self, node):
        self.NodeCollection.update({'_id': id}, {'$set': {'Audit.IsActive': False}})
        return True

    def save_node(self, node):
        result = self.NodeCollection.insert_one(node)
        return {'id':str(result.inserted_id)}


