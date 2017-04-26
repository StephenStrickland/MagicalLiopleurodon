__author__ = 'Stephen'

from bottle import Bottle, TEMPLATE_PATH
app = Bottle()
TEMPLATE_PATH.append("./MLIotLibrary/RestApiService/views/")
TEMPLATE_PATH.remove("./views/")
# from MLIotLibrary.Shared.Services.NodeService import NodeService
# NodeService = NodeService()
from MLIotLibrary.RestApiService.controllers import *

