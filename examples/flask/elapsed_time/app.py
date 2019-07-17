import time
from flask import Flask, request, render_template, g
app = Flask(__name__)


@app.before_request
def before_request():
   g.request_start_time = time.time()
   g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


@app.route("/")
def main():
    return render_template('main.html')

