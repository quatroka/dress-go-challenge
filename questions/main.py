# -*- coding: utf-8 -*-
""" Main file to Levenshtein distance algorithm problem """
from levenshtein import levenshtein

SEQ1 = input('Enter the first sequence:')
SEQ2 = input('Enter the second sequence:')

print('Levenshtein distance: {}'.format(levenshtein(SEQ1, SEQ2)))
