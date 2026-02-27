#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from .view import page

app = Flask(__name__)

def create_app():
    app.secret_key = '1'
    app.register_blueprint(page)
    return app