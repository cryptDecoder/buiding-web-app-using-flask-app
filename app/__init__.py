"""
@title: __init__.py
@description: The python constructor file uses for import flask
"""
# Standard modules import
from flask import Flask

app = Flask(__name__)

# relative module import
from app.views import views
