#!/usr/bin/env python3
""" module level doc"""
from flask import Flask, render_template, request
from flask_babel import Babel

setup = __import__('1-app').Config
app = Flask(__name__)
app.config.from_object(setup)
babel = Babel(app)

@babel.localselector
def get_locale():
    """Doc doc"""
    return request.accept_languages.best_match(app.setup.["LANGUAGES"])
