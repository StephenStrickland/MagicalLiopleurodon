__author__ = 'Stephen Strickland'
from MLIotLibrary.Entities import Audit
class NodeTelemetry:
    def __init__(self):
        self.Id = ''
        self.NodeId = ''
        self.Audit = Audit
        self.Data = {}