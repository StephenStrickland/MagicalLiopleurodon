__author__ = 'Stephen Strickland'
import datetime
from MLIotLibrary.Entities import Audit


class Node:
    def __init__(self):
        self.Id = ''
        self.Audit = Audit
        self.Name = ''
        self.Location = ''
        self.GpsCoordinates = ''
        self.OptionalPrivateKey = ''
        self.LastCheckInDateTimeUTC = datetime.utc()