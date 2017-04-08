# -*- coding: utf-8 -*-
""" Test file for Google Places API. """
from unittest import TestCase, main
from places import get_place_data


class TestGoogleMaps(TestCase):
    """ Test class for Google Places API. """


    def test_get_place_data(self):
        """ Test for get_place_data method. """
        data = get_place_data('Dress & Go')
        self.assertEqual('Dress & Go', data['results'][0]['name'])
        self.assertEqual('OK', data['status'])
        self.assertEqual(-23.5949847, data['results'][0]['geometry']['location']['lat'])
        self.assertEqual(-46.6764695, data['results'][0]['geometry']['location']['lng'])


if __name__ == '__main__':
    main()
