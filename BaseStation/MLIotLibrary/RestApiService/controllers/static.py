__author__ = 'Stephen'
from MLIotLibrary.RestApiService import app
from bottle import static_file


@app.route('/:file#(favicon.ico|humans.txt)#')
def favicon(file):
    return static_file(file, root='MLIotLibrary/RestApiService/static/misc')


@app.route('/:path#(images|css|js|fonts|libs)\/.+#')
def server_static(path):
    return static_file(path, root='MLIotLibrary/RestApiService/static')

@app.route('/ngscripts/<file:path>')
def scripts_static(file):
    return static_file(file, root='MLIotLibrary/RestApiService/app/')

@app.route('/ngviews/<templatePath>')
def views_static(templatePath):
    return static_file(templatePath + '.html', root='MLIotLibrary/RestApiService/app/')
