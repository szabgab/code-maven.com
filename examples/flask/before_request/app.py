from flask import Flask

app = Flask(__name__)

@app.before_request
def before_request():
    app.logger.info("before_request")


@app.route("/")
def main():
    app.logger.info("main route")
    return "Hello World!"

