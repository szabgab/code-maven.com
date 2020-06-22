from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    app.logger.info("before_first_request")


@app.route("/")
def main():
    app.logger.info("main route")
    return "Hello World!"

