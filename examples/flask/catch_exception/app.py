from flask import Flask
import datetime

app = Flask(__name__)

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

@app.route("/")
def main():
    app.logger.info("main route")
    return "Hello " + str(datetime.datetime.now())

@app.route("/crash")
def crash():
    app.logger.info("crash route")
    a = 0
    b = 3 / a
