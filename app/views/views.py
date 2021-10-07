"""
@title: views.py
@description: In this python views file create request/response viiews
                to end user
"""
# standard module import


# relative module import
from app import app
from app.utils import logger

log = logger.logger()


# define default route
@app.route("/", methods=['GET'])
def index():
    log.debug("application started . . .")
    return "Welcome to flask application"


@app.route("/about", methods=['GET'])
def about():
    log.debug("about page execution . . .")
    return "Welcome to about page"
