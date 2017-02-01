import datetime

__author__ = 'Stephen'

class Audit:
    def __init__(self):
        self.CreateDate = datetime.utc()
        self.CreateUser = ''
        self.ModDate = datetime.utc()
        self.ModUser = ''