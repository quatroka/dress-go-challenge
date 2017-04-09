# -*- coding: utf-8 -*-
""" Controller file for all remaining methods. """


def filter_essential_data(place_data):
    """ Receive a data and returns your essential data. """
    essential_data = {}
    essential_data['local_name'] = place_data['results'][0]['name']
    essential_data['full_address'] = place_data['results'][0]['formatted_address']
    essential_data['latitude'] = place_data['results'][0]['geometry']['location']['lat']
    essential_data['longitude'] = place_data['results'][0]['geometry']['location']['lng']
    essential_data['place_id'] = place_data['results'][0]['place_id']
    return essential_data
