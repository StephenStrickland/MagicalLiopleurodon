__author__ = 'Stephen Strickland'
from mongoengine import StringField, EmbeddedDocument, ObjectIdField
from MLIotLibrary.Shared.Schema.Audit import Audit

class MGroup(EmbeddedDocument):
    HostId = ObjectIdField(required=True)
    GroupName = StringField(required=True)
    GroupLocation = StringField()


