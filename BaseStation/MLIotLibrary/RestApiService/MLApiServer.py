
from bottle import route, run, template, Bottle, static_file, get
from MLIotLibrary.RestApiService import app
import os


class MLApiServer:
    app = Bottle()
    def __init__(self, port):

        self.port = 8080
        if port > 0:
            self.port = port

    def setup(self):
        print("setup here, or not")




    @app.route('/hello/<name>')
    def index(self, name):
        return template('<b>Hello {{name}}</b>!', name=name)

    @app.get('/')
    def index(self):
      return static_file('index.tpl', root='/MLIotLibrary/RestApiService/')

    def start(self):
        print(os.getcwd())
        print('hello world')
        run(host='localhost', port=self.port)
