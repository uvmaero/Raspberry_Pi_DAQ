# Python file for FLASK web server

from flask import *
import json
import sys

app = Flask(__name__)

@app.route('/temp', methods=['GET'])
def temp():
    print('hello world')

@app.route('/', methods=['GET'])
def default():
    return render_template('index.html', name='Main Page')

