#!/usr/bin/env python3
import typing
from flask import Flask

app = Flask(__name__)

app.route("/")
def welcome():
    return render_template("0-index.html")
