import os
from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def status():
    return {
        "status": "running"
    }

@app.route('/rax30/power', methods=['POST'])
def send_key_power():
    os.system("/usr/bin/irsend SEND_ONCE RAX30 KEY_POWER")
    return {}

@app.route('/rax30/input', methods=['PUT'])
def select_input():
    input = request.json['src'].upper()
    os.system(f"/usr/bin/irsend SEND_ONCE RAX30 KEY_{input}")
    return {}

def change_volume(command):
    for _ in range(5):
        os.system(f"/usr/bin/irsend SEND_ONCE RAX30 {command}")
        time.sleep(0.25)

@app.route('/rax30/volume/up', methods=['POST'])
def increase_volume():
    change_volume("KEY_VOLUMEUP")
    return {}

@app.route('/rax30/volume/down', methods=['POST'])
def decrease_volume():
    change_volume("KEY_VOLUMEDOWN")
    return {}
