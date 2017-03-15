from MLIotLibrary.Shared.Entities import Audit

__author__ = 'Stephen Strickland'


class NodeTelemetry:
    def __init__(self):
        self.Id = ''
        self.NodeId = ''
        self.Audit = Audit
        self.Data = {}