__author__ = 'Stephen Strickland'
from  MLIotLibrary.Entities import Audit


class User:
    def __init__(self):
        self.Id = ''
        self.Audit = Audit
        self.FirstName = ''
        self.LastName = ''
        self.UserName = ''
        self.Password = ''
        self.PasswordSalt = ''
        self.ApiKey = ''
        self.ApiKeyExpiration = ''
        self.IsBot = False
