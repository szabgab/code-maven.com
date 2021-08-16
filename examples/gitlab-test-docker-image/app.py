from flask import Flask
from datetime import datetime
import os
import socket

version = 1

app = Flask('Demo')

@app.route("/")
def main():
    return f"""
        Version {version}<br>
        At {datetime.now()}<br>
        PID {os.getpid()}<br>
        Hostname {socket.gethostname()}<br>
    """
