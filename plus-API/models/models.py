# -*- coding: utf-8 -*-
""" Models file for all remaining methods. """
import sqlite3

def save_place(place):
    """ Receive a place and insert on database. """
    conn = sqlite3.connect('places.db')
    cursor = conn.cursor()

    sql = 'INSERT INTO places(local_name, full_address, latitude, longitude, place_id)' \
          'VALUES(?, ?, ?, ?, ?)'

    cursor.execute(sql, (place['local_name'],
                         place['full_address'],
                         place['latitude'],
                         place['longitude'],
                         place['place_id']
                        )
                  )
    conn.commit()
    conn.close()
