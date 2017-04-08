# -*- coding: utf-8 -*-
""" Test file for controllers. """
from unittest import TestCase, main
from places import get_place_data
from controllers import filter_essential_data


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


if __name__ == '__main__':
    main()
