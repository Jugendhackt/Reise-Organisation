import bahn_api
import wetter_api
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hallo Welt'

@app.route('/zug')
def zug():
    return bahn_api.anJson()

@app.route('/zug2/<stadt1>/<stadt2>')
def zug2(stadt1, stadt2):
    return bahn_api.anJson(stadt1, stadt2)

@app.route('/wetter')
def wetter():
    return wetter_api.wettervorhersage()
