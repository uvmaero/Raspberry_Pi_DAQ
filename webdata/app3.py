import json
import random
import time
import can_logger as can
from datetime import datetime

from flask import Flask, render_template, request, Response

app = Flask(__name__)

def get_message_value(can_id):
        while True:
            json_data = json.dumps(
                    {'time':datetime.now().strftime('%y-%m-%d %H:%M:%S'), 'value': can.get_can_message(can_id)})
            yield f"data:{json_data}\n\n"
            time.sleep(.25)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/rideHeight')
def rideHeightTemp():
    return render_template("rideHeight.html")

@app.route('/rideHeightData')
def rideHeightData():
    return Response(get_message_value(0x0C0), mimetype='text/event-stream')

@app.route('/throttle')
def throttleTemp():
    return render_template('throttle.html')

@app.route('/throttleData')
def throttleData():
    return Response(get_message_value(0x0C0), mimetype='text/event-stream')

@app.route('/steer')
def steerTemp():
    return render_template('steer.html')

@app.route('/steerData')
def steerData():
    return Response(get_message_value(0x0C0), mimetype='text/event-stream')


if __name__ == '__main__':
	application.run(debug==True, threaded=True)
