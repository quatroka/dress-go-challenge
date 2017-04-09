""" Blueprint for views of app """
from flask import jsonify, request, Blueprint
from controllers.places import get_place_data
from controllers.controllers import filter_essential_data
from models.models import save_place

PLACES = Blueprint('places', __name__)

@PLACES.route('/api/places', methods=['POST'])
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
