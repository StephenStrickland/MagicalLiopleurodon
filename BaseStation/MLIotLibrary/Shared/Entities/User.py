from MLIotLibrary.Shared.Entities import Audit

__author__ = 'Stephen Strickland'


class User:
    def __init__(self):
        self.Id = ''
        self.Audit = Audit
        self.FirstName = ''
        self.LastName = ''
        self.UserName = ''
        self.Password = ''
        self.PasswordSalt = ''
        self.AuthToken = ''
        self.AuthTokenExpiration = ''
        self.IsBot = False
