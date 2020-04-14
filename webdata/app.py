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
    return render_template('main.html', name='Main Page')

if __name__=="__main__":
    app.run(host='10.0.1.20', port=80, debug=False)
