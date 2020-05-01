import json
import random
import time
import can_logger as can
import datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def rideHeight():
	def chart_data():
    def get_message_value(can_id):
        while True:
            json_data = json.dumps(
                    {'time':datetime.now().strftime('%y-%m-%d %H:%M:%S'), 'value': can.get_can_message(can_id)})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(get_message_value(0x0C0), mimetype='text/event-stream'), render_template('rideHeight.html')

@app.route('/VandC/')
def VandC():
	def chart_data():
    def get_message_value(can_id):
        while True:
            json_data = json.dumps(
                    {'time':datetime.now().strftime('%y-%m-%d %H:%M:%S'), 'value': can.get_can_message(can_id)})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(get_message_value(0x0C0), mimetype='text/event-stream'), render_template('VandC.html')

@app.route('/temp/')
def temp():
	def chart_data():
    def get_message_value(can_id):
        while True:
            json_data = json.dumps(
                    {'time':datetime.now().strftime('%y-%m-%d %H:%M:%S'), 'value': can.get_can_message(can_id)})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(get_message_value(0x0C0), mimetype='text/event-stream'), render_template('temp.html')


if __name__ == '__main__'
	application.run(debug==True, threaded=True)
