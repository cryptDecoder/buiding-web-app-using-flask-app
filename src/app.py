"""
@title: app.py
@description: This is a sample python flask app.
"""
# standard python modules import here
from flask import Flask

app = Flask(__name__)


# default route
@app.route("/")
def index():
    return "Hello Python flask application"


@app.route("/about")
def about():
    return "<h1 style='color:red'>Welcome to about page !!! </h1>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
