# -*- coding: utf-8 -*-
""" Blueprint for views of app """
from flask import jsonify, request, Blueprint
from controllers.places import get_place_data
from controllers.controllers import filter_essential_data, is_exists
from models.models import save_place, get_all_places, get_one_place
from models.models import delete_one_place

PLACES = Blueprint('places', __name__)

@PLACES.route('/api/places', methods=['POST'])
def places_create_one():
    """ Insert a place of database.

        Receive a json with place value, get Googla Places
        data of value, filter the necessary information of
        that and insert on database."""
    if request.method == 'POST':
        place = request.json['place']
        place = get_place_data(place)
        place = filter_essential_data(place)
        save_place(place)
        data = is_exists(place['local_name'])
        if data is False:
            return jsonify({'response': 'Not save.'}), 406
        return jsonify(place), 200


@PLACES.route('/api/places', methods=['GET'])
def places_get_all():
    """ Receive all places in database. """
    if request.method == 'GET':
        data = get_all_places()
        if len(data['places']) == 0:
            return jsonify({'response': 'Not have places.'}), 404
        return jsonify(data), 200


@PLACES.route('/api/places/<string:place>', methods=['GET'])
def places_get_one(place):
    """ Receive one place of database.

        Receive a place paramter in url and get
        your data in database. """
    place = place.replace('-', ' ')
    if request.method == 'GET':
        data = is_exists(place)
        if data is False:
            return jsonify({'response': 'Place not found.'}), 404
        return jsonify(data), 200


@PLACES.route('/api/places/<string:place>', methods=['DELETE'])
def places_delete_one(place):
    """ Delete one place on database.

        Receive a place paramter in url and delete
        your repective place in database. """
    place = place.replace('-', ' ')
    if request.method == 'DELETE':
        delete_one_place(place)
        data = is_exists(place)
        if data is True:
            return jsonify({'response': 'Not deleted.'}), 406
        return jsonify({'response': 'Deleted.'}), 204
