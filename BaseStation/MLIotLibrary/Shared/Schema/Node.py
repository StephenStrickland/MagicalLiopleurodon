from mongoengine import Document, DateTimeField, StringField, ObjectIdField, EmbeddedDocumentField, PointField, IntField
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import sessionmaker

from .Audit import Audit
from .Group import Group
from ..Config import Config

#MongoDB mongoengine schema
class MNode(Document):
    HostId = ObjectIdField(required=True)
    Audit = EmbeddedDocumentField(Audit)
    NodeType = IntField(required=True, default=1)
    Name = StringField(required=True)
    Location = StringField()
    GpsCoordinates = PointField()
   # OptionalPrivateKey =
    Group = EmbeddedDocumentField(Group)
    LastHeartbeat = DateTimeField()
    NetworkAddress = IntField(required=True)
    IpAddress = StringField(required=True)

#SQL sqlalchemy schema
class SNode(Base):
    __tablename__ = 'Nodes'
    Name = Column(String)




def get_node_by_id(id):
    if Config.useMongo:
        return MNode.objects(id=id)[0]
    elif Config.useSql:
        return None

