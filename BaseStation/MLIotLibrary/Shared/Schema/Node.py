from MLIotLibrary.Shared.Schema.Audit import Audit
from mongoengine import Document, DateTimeField, StringField, ObjectIdField, EmbeddedDocumentField, PointField, IntField
import datetime
from MLIotLibrary.Shared.Schema.Group import Group
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#MongoDB mongoengine schema
class MNode(Document):
    HostId = ObjectIdField(required=True)
    Audit = EmbeddedDocumentField(Audit)
    Name = StringField(required=True)
    Location = StringField()
    GpsCoordinates = PointField()
   # OptionalPrivateKey =
    Group = EmbeddedDocumentField(Group)
    LastHeartbeat = DateTimeField()
    Address = IntField(required=True)

#SQL sqlalchemy schema
class SNode(Base):
    __tablename__ = 'Nodes'
    Name = Column(String)
