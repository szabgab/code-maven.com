from flask import Flask
from flask.templating import render_template
from echo import echo_app

app = Flask(__name__)
app.register_blueprint(echo_app, url_prefix='/echo')


@app.route('/')
def main():
    return render_template('main.html')
