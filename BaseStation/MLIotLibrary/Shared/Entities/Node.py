from MLIotLibrary.Shared.Entities import Audit

__author__ = 'Stephen Strickland'
import datetime
from MLIotLibrary.Shared.Entities.Group import Group

class Node:
    def __init__(self):
        self.Id = ''
        self.Audit = Audit
        self.Name = ''
        self.Location = ''
        self.GpsCoordinates = ''
        self.OptionalPrivateKey = ''
        self.Group = Group()
        self.LastCheckInDateTimeUTC = datetime.datetime.utcnow()
