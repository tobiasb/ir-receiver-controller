import os
from flask import Flask

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
