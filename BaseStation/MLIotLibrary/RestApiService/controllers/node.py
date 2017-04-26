__author__ = 'Stephen Strickland'
from MLIotLibrary.RestApiService import app
from bottle import request, response
from json import dumps
import time
import serial.tools.list_ports
from MLIotLibrary.Shared.Services.AuthService import authentication_wrapper as authenticate
from MLIotLibrary.Shared.Entities.NodeTelemetry import NodeTelemetry
from . import Lio
from . import SSEMsgs
from gevent.queue import Queue


@app.get('/api/nodes')
def get_all_nodes():
    return Lio.nodes.get_all_nodes().to_json()



@app.get('/api/nodes/:id')
def get_node_by_id(id):
    print(request.url_args, 'args')
    return dumps(Lio.nodes.get_node_by_id(id))

@app.put('/api/nodes/:id')
def update_node_by_id(id):
    return {'success': True}

@app.post('/api/nodes')
def create_node():
    req = request.body
    json = request.json
    return dumps({ id: Lio.nodes.create_node(json)})


@app.post('/api/nodes/:id/msg')
def send_command_to_node(id):
    return {}

##node telemetry

@app.get('/api/nodes/:id/telemetry/')
def get_all_telemetry_for_node(id):
    return dumps({})


@app.get('/api/nodes/:id/telemetry/:telemId')
def get_all_telemetry_for_node(id, telemId):
    return NotImplementedError()





@app.get('/api/nodes/:id/program')
def program_node(id):
    return Lio.nodes.program_node(id)


@app.get('api/traffic')
def sub_to_network_traffic():
    # Keep event IDs consistent
    event_id = 0
    if 'Last-Event-Id' in request.headers:
        event_id = int(request.headers['Last-Event-Id']) + 1

    # Set up our message payload with a retry value in case of connection failure
    # (that's also the polling interval to be used as fallback by our polyfill)
    msg = {
        'retry': '2000'
    }

    # Provide an initial data dump to each new client
    response.headers['content-type'] = 'text/event-stream'
    response.headers['Access-Control-Allow-Origin'] = '*'
    msg.update({
        'event': 'init',
        'data': {},
        'id': event_id
    })
    yield _sse_pack(msg)

    # Now give them deltas as they arrive (say, from a message broker)
    event_id += 1
    msg['event'] = 'delta'
    while True:
        # block until you get new data (from a queue, pub/sub, zmq, etc.)
        msg.update({
            'event': 'delta',
            'data': dumps(SSEMsgs.get()),
            'id': event_id
        })
        yield _sse_pack(msg)
        event_id += 1


def _sse_pack(d):
    """Pack data in SSE format"""
    buffer = ''
    for k in ['retry','id','event','data']:
        if k in d.keys():
            buffer += '%s: %s\n' % (k, d[k])
    return buffer + '\n'


