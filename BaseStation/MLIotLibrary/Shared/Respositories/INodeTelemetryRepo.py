__author__ = 'Stephen Strickland'


class INodeTelemetryRepo:
    def get_node_telem_for_node(self, nodeId, startDateTime, endDateTime):
        return NotImplementedError()

    def get_node_telem_by_id(self, id):
        return NotImplementedError()

    def save_node_telem(self, telem):
        return NotImplementedError()

    def archive_node_telem(self, id):
        return NotImplementedError()
    def archive_all_node_telem(self, nodeId):
        return NotImplementedError()

    def delete_node_telem(self, id):
        return NotImplementedError()
    def delete_all_node_telem(self, nodeId):
        return NotImplementedError()