# -*- coding: utf-8 -*-
""" Main file to start the project """
import logging
from flask import Flask, request, Blueprint
from views.views import PLACES

APP = Flask(__name__)

# Blueprints
APP.register_blueprint(PLACES)

if __name__ == '__main__':
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('access.log')
    logger.addHandler(handler)
    APP.logger.addHandler(handler)
    APP.run(debug=True, port=5000)
