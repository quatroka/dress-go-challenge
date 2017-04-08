""" Main file to start the project """
import logging
from flask import Flask, jsonify, request
from places import get_place_data
from controllers import filter_essential_data
from models import save_place

APP = Flask(__name__)

@APP.route('/api/places', methods=['POST'])
def create_place():
    """ Insert a place on database.

        Receive a json with place value, get Googla Places
        data of value, filter the necessary information of
        that and insert on database."""
    if request.method == 'POST':
        place = request.json['place']
        place = get_place_data(place)
        place = filter_essential_data(place)
        save_place(place)
        return jsonify(place)


if __name__ == '__main__':
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('access.log')
    logger.addHandler(handler)
    APP.logger.addHandler(handler)
    APP.run(debug=True, port=5000)
