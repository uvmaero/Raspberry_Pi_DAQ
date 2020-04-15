# Python file for FLASK web server

from flask import *
import json
import sys

import can_logger as can

app = Flask(__name__)

@app.route('/temp', methods=['GET'])
def temp():
    print('hello world')

@app.route('/', methods=['GET'])
def default():
    msg = can.get_can_message(0x0C0)
    if msg is None:
        msg = "No Data"
    return render_template('main.html', name='Main Page', value=msg)

if __name__=="__main__":
    app.run(host='10.0.1.20', port=80, debug=False)
