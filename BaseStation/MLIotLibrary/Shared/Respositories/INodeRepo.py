class INodeRepo:
    def get_node_by_id(self, id):
        raise NotImplementedError()
    def get_all_nodes(self):
        raise NotImplementedError()
    def save_node(self, node):
        raise NotImplementedError()
    def delete_node(self, node):
        raise NotImplementedError()

    #simply marks node as inactive
    def archive_node(self, node):
        raise NotImplementedError()
