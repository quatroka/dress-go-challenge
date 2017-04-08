# -*- coding: utf-8 -*-
""" File to functions of Google Places API. """
import googlemaps
from key import KEY


def get_place_data(place):
    """ Get Google Place data of a place paramter.

        Recive place paramter(string), create a googlemaps
        client, request your data, and returns your response. """
    gmaps = googlemaps.Client(key=KEY)
    place_result = gmaps.places(place)
    return place_result

