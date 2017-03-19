from MLIotLibrary.Shared.Schema.Audit import Audit

from mongoengine import Document, ObjectIdField, EmbeddedDocumentField, DictField


class NodeTelemetry(Document):
    NodeId = ObjectIdField(required=True)
    Audit = EmbeddedDocumentField(Audit)
    Data = DictField(required=True)

