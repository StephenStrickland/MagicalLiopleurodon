import datetime
from mongoengine import EmbeddedDocument, DateTimeField, StringField, BooleanField
__author__ = 'Stephen'

class Audit(EmbeddedDocument):
    CreateDate = DateTimeField(default=datetime.datetime.utcnow())
    CreateUser = StringField()
    ModDate = DateTimeField(default=datetime.datetime.utcnow())
    ModUser = StringField()
    IsActive = BooleanField(default=True)