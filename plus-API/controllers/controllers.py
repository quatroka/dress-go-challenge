# -*- coding: utf-8 -*-
""" Controller file for all remaining methods. """
from models.models import get_one_place


def filter_essential_data(place_data):
    """ Receive a data and returns your essential data. """
    essential_data = {}
    essential_data['local_name'] = place_data['results'][0]['name']
    essential_data['full_address'] = place_data['results'][0]['formatted_address']
    essential_data['latitude'] = place_data['results'][0]['geometry']['location']['lat']
    essential_data['longitude'] = place_data['results'][0]['geometry']['location']['lng']
    essential_data['place_id'] = place_data['results'][0]['place_id']
    return essential_data


def is_exists(place):
    """ Request if place exists in database. """
    place = get_one_place(place)
    if len(place) == 0:
        return False
    return place[0]
