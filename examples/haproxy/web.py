from flask import Flask, request
import sys
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
   return 'Hello <br>Running on port {}<br>Loaded at {}'.format(port, datetime.now())


if __name__ == "__main__":
   if len(sys.argv) < 2:
       exit("Need port number")
   port = int(sys.argv[1])
   app.run(port = port)

