__author__ = 'Stephen Strickland'

from MLIotLibrary.Shared.Respositories.IUserRepo import IUserRepo
from pymongo import MongoClient
from bson.objectid import ObjectId
import configparser

class UserMongoRepository(IUserRepo):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('lio.config')
        self.ConnectionString = config['database']['MongoConnectionString']
        self.UserCollection = MongoClient(self.ConnectionString).Lio.Users

    def get_user_by_id(self, id):
        return self.UserCollection.find_one({'_id': ObjectId(id)})

    def get_user_by_username(self, username):
        return self.UserCollection.find_one({'UserName': username})

    def get_user_by_auth_token(self, token):
        return self.UserCollection.find_one({'AuthToken': token})
