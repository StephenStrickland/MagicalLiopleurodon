__author__ = 'Stephen Strickland'
from mongoengine import StringField, EmbeddedDocument, ObjectIdField

class Group(EmbeddedDocument):
    HostId = ObjectIdField(required=True)
    GroupName = StringField(required=True)
    GroupLocation = StringField()


