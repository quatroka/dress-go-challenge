# -*- coding: utf-8 -*-
""" Test file for controllers. """
from unittest import TestCase, main
from models.models import save_place, delete_one_place
from controllers.places import get_place_data
from controllers.controllers import filter_essential_data, is_exists


class TestControllers(TestCase):
    """ Test class for controllers. """


    def test_filter_essential_data(self):
        """ Test for filter_essential_data method. """
        data = get_place_data('Dress & Go')
        expect = {
            'local_name': 'Dress & Go',
            'full_address': 'R. Santa Justina, 352 - Vila Olimpia, ' \
            'São Paulo - SP, 04545-041, Brazil',
            'latitude': -23.5949847,
            'longitude': -46.6764695,
            'place_id': 'ChIJNZZ3QVFXzpQRzj3sZ9iA8gg'
            }
        self.assertEqual(expect, filter_essential_data(data))


    def test_is_exists_place(self):
        """ Test for is_exists method. """
        delete_one_place('Claro')
        self.assertEqual(False, is_exists('Claro'))
        self.assertEqual(False, is_exists('Claro'))
        place = get_place_data('Claro')
        place = filter_essential_data(place)
        save_place(place)
        self.assertEqual('Claro', is_exists('Claro')['local_name'])


if __name__ == '__main__':
    main()
