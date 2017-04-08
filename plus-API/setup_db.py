# -*- coding: utf-8 -*-
""" Setup file to create sqlite db. """
import sqlite3

CONN = sqlite3.connect('places.db')
CURSOR = CONN.cursor()

CURSOR.execute('CREATE TABLE places( id INT PRIMARY KEY NOT NULL, \
                                     local_name CHAR(100) NOT NULL, \
                                     full_address  CHAR(500) NOT NULL,\
                                     latitude REAL NOT NULL, \
                                     longitude REAL NOT NULL, \
                                     place_id CHAR(100) NOT NULL )')

CONN.close()
