from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    app.logger.debug("main debug")
    app.logger.info("main info")
    app.logger.warning("main warning")
    app.logger.error("main error")
    app.logger.critical("main critical")
    return "Hello " + str(datetime.datetime.now())

