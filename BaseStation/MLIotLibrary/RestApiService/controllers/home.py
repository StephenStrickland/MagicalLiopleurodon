__author__ = 'Stephen'
from MLIotLibrary.RestApiService import app
from bottle import template, request

@app.route('/', method='GET')
def index():
    return template('home/index', message='')