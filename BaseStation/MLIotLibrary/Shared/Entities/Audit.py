import datetime

__author__ = 'Stephen'

class Audit:
    def __init__(self):
        self.CreateDate = datetime.datetime.utc()
        self.CreateUser = ''
        self.ModDate = datetime.datetime.utc()
        self.ModUser = ''
        self.IsActive = True