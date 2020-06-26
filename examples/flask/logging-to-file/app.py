from flask import Flask
import datetime
import logging
import os

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    log_level = logging.INFO

    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)

    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    log_file = os.path.join(logdir, 'app.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    app.logger.addHandler(handler)

    app.logger.setLevel(log_level)


@app.route("/")
def main():
    app.logger.debug("main debug")
    app.logger.info("main info")
    app.logger.warning("main warning")
    app.logger.error("main error")
    app.logger.critical("main critical")
    return "Hello " + str(datetime.datetime.now())

