from MLIotLibrary.Shared.Schema.Audit import Audit

from mongoengine import Document, ObjectIdField, EmbeddedDocumentField, DictField


class NodeTelemetry(Document):
    NodeId = ObjectIdField(required=True)
    Audit = EmbeddedDocumentField(Audit)
    Data = DictField(required=True)

def get_telem_by_id(id):
    return NodeTelemetry.objects(id=id).first()

def get_all_telem_by_node_id(node_id):
    return NodeTelemetry.objects(NodeId=node_id)

def create_telemetry(node_id, data):
    telem = NodeTelemetry()
    telem.NodeId = node_id
    telem.Data = data
    telem.save()
    return telem.id
