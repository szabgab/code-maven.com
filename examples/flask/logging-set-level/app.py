from flask import Flask
import datetime
import logging

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    log_level = logging.INFO
    app.logger.setLevel(log_level)


@app.route("/")
def main():
    app.logger.debug("main debug")
    app.logger.info("main info")
    app.logger.warning("main warning")
    app.logger.error("main error")
    app.logger.critical("main critical")
    return "Hello " + str(datetime.datetime.now())

