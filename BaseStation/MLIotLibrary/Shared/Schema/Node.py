from mongoengine import Document, DateTimeField, StringField, ObjectIdField, EmbeddedDocumentField, PointField, IntField
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from mongoengine import signals
import datetime
Base = declarative_base()

from .Audit import Audit
from .Group import MGroup
from ..Config import Config
from collections import namedtuple
#
# def handler(event):
#     """Signal decorator to allow use of callback functions as class decorators."""
#
#     def decorator(fn):
#         def apply(cls):
#             event.connect(fn, sender=cls)
#             return cls
#
#         fn.apply = apply
#         return fn
#
#     return decorator
#
#
# @handler(signals.pre_init)
# def handle_init(sender, document, **kwargs):
#     document.Audit = Audit()
#
# @handler(signals.pre_save)
# def handle_pre_save(sender, document, **kwargs):
#     document.Audit.ModDate = datetime.datetime.utcnow()



#MongoDB mongoengine schema
class MNode(Document):
    meta = {'collection': 'Nodes', 'strict': False}
    HostId = ObjectIdField(required=False)
    Audit = EmbeddedDocumentField(Audit)
    NodeType = IntField(required=True, default=1)
    Name = StringField(required=True)
    Location = StringField()
    GpsCoordinates = PointField()
   # OptionalPrivateKey =
    Group = EmbeddedDocumentField(MGroup)
    LastHeartbeat = DateTimeField()
    NetworkAddress = IntField(required=True)
    IpAddress = StringField()


#SQL sqlalchemy schema
class SNode():
    def __init__(self):
        return
   # __tablename__ = 'Nodes'
   # Name = Column(String)


def get_all_nodes():
    return MNode.objects()


def get_node_by_id(id):
        return MNode.objects(id=id).first()


def get_node_by_address(addr):
    return MNode.objects(NetworkAddress=addr).first()


def archive_node(id):
    node = MNode.objects(id=id).first()
    node.Audit.IsActive = False
    node.save()


def save_node(n):
    node = MNode(n)
    node.save()


def create_node(n):
    node = MNode(**n)
    node.Audit = Audit()
    node.save()
    return node.id


CachedNode = namedtuple('CachedNode', ['node', 'profile', 'valid'])




