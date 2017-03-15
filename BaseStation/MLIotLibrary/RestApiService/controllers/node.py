__author__ = 'Stephen Strickland'
from MLIotLibrary.RestApiService import app
from bottle import request
from MLIotLibrary.Shared.Services.NodeService import NodeService
from bson.json_util import dumps
from MLIotLibrary.Shared.Services.AuthService import authentication_wrapper as authenticate


@app.get('/api/nodes')
def get_all_nodes():
    return dumps(NodeService().get_all_nodes())



@app.get('/api/nodes/:id')
def get_node_by_id(id):
    print(request.url_args, 'args')
    return dumps(NodeService().get_node_by_id(id))

@app.put('/api/nodes/:id')
def update_node_by_id(id):
    return {'success': True}

@app.post('/api/nodes')
def create_node():
    return NodeService().save_node(request.json)

@app.post('/api/nodes/:id/cmd')
def send_command_to_node(id):
    return {}

##node telemetry

@app.get('/api/nodes/:id/telemetry/')
def get_all_telemetry_for_node(id):
    return NotImplementedError()


@app.get('/api/nodes/:id/telemetry/:telemId')
def get_all_telemetry_for_node(id, telemId):
    return NotImplementedError()



