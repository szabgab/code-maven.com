from flask import Flask, abort
import datetime

app = Flask(__name__)

@app.after_request
def after_request(response):
    app.logger.info("after_request")
    return response

@app.route("/")
def main():
    app.logger.info("main route")
    return "Hello " + str(datetime.datetime.now())

@app.route("/crash")
def crash():
    app.logger.info("crash route")
    a = 0
    b = 3 / a
