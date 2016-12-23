
from bottle import route, run, template, Bottle



class Server:
    def __init__(self):
        self.app = Bottle()

    def setup(self):
        print("setup here, or not")




@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)