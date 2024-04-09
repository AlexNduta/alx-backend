#!/usr/bin/env python3
import typing
from flask import Flask

app = Flask(__name__)

app.route("/")


def welcome():
    """Serve the 0-index.html on the route / """
    return render_template("0-index.html")
