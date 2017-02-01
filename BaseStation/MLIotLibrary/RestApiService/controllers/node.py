__author__ = 'Stephen'
from MLIotLibrary.RestApiService import app


@app.get('/api/nodes')
def get_all_nodes():
    return [{'id':0}, {'id':1},{'id':2}]

@app.get('/api/nodes/:id')
def get_node_by_id(id):
    return {'id':int(id)}

@app.put('/api/nodes/:id')
def get_node_by_id(id):
    return {'id':'1234'}

@app.post('/api/nodes/:id')
def create_node(id):
    return {}

@app.post('/api/nodes/:id/cmd')
def send_command_to_node(id):
    return {}


