from distutils.log import debug
from pickle import TRUE
from threading import Lock
from unittest import result
from flask import Flask, render_template, request
from flask_socketio import SocketIO,emit
import requests
import json
import time
# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

key = "https://api.binance.com/api/v3/ticker/price?symbol="
def background_thread():
    currencies = ["BTCUSDT","ETHUSDT","DOGEUSDT"]
    while TRUE:
        j = 0
        price=[]
        for i in currencies:
            url = key+currencies[j]  
            data = requests.get(url)
            data = data.json()
            price.append(float(data['price']))
            j= j+1
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)
        price.append(time_string)
        socketio.emit('my_response',price)      
@app.route('/',methods=['GET'])
def index():
    name=request.form.get('Crypto')
    print(name)
    return render_template('crypto.html', async_mode=socketio.async_mode)

@socketio.on('test_connect')
def connect(message):
    print(message)
    global thread
    with thread_lock:
        if thread is None:
        # Open a separate thread to send data to clients
            thread = socketio.start_background_task(target=background_thread)
    socketio.emit('connected', {'data': 'Connected'})
if __name__ == '__main__':
    socketio.run(app,debug=True)