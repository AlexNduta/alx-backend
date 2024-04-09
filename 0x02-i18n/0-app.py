#!/usr/bin/env python3
import typing
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    """Serve the 0-index.html on the route / """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
