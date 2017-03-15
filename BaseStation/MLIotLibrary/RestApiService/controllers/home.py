__author__ = 'Stephen'
from MLIotLibrary.RestApiService import app
from bottle import template, request
import glob

@app.route('/', method='GET')
def index():
    return template('home/index', message='', scripts=_getAngularFileNames())


def _getAngularFileNames():
    return [ '/ngscripts/' + x[32:] for x in glob.glob('MLIotLibrary/RestApiService/app/**/*.js', recursive=True)]
