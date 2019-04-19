from flask import Flask, render_template, request, redirect, session, url_for, g, jsonify
import time
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

