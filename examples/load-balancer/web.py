from flask import Flask, request, jsonify
import sys
from datetime import datetime
import socket
import json

app = Flask(__name__)

version = 1

def myconverter(o):
   if isinstance(o, datetime):
       return o.__str__()


@app.route("/")
def hello():
   logfile = '/tmp/echo.log'
   data = {
       'client': request.remote_addr,
       'hostname': socket.gethostname(),
       'port': port,
       'now': datetime.now(),
       'version': version,
   }
   with open(logfile, 'a') as fh:
       fh.write(json.dumps(data, default = myconverter))
       fh.write("\n")
   return jsonify(data)


if __name__ == "__main__":
   if len(sys.argv) < 2:
       exit("Need port number")
   port = int(sys.argv[1])
   app.run(port = port, host='0.0.0.0')

