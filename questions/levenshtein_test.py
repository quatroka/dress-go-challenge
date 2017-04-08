# -*- coding: utf-8 -*-
""" Test file to Levenshtein algorithm """
from unittest import TestCase, main
from levenshtein import levenshtein

class TestPermutation(TestCase):
    """ Test class for testing a Levenshtein distance algorithm. """

    def test_levenshtein(self):
        """ Test algorithm to """
        self.assertEqual(4, levenshtein('teste', 'casa'))
        self.assertEqual(0, levenshtein('abcdefg', 'abcdefg'))
        self.assertEqual(0, levenshtein('', ''))

if __name__ == '__main__':
    main()
