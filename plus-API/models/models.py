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


def get_all_places():
    """ Retrieve a list of all places on database. """
    places = {'places': []}

    conn = sqlite3.connect('places.db')
    cursor = conn.cursor()

    sql = 'SELECT local_name, full_address, latitude, longitude, place_id FROM places'

    for place in cursor.execute(sql):
        place_modal = {}
        place_modal['local_name'] = place[0]
        place_modal['full_address'] = place[1]
        place_modal['latitude'] = place[2]
        place_modal['longitude'] = place[3]
        place_modal['place_id'] = place[4]
        places['places'].append(place_modal)

    conn.close()
    return places


def get_one_place(place):
    """ Retrieve a list of all places on database. """
    places = {'places': []}

    conn = sqlite3.connect('places.db')
    cursor = conn.cursor()

    sql = 'SELECT local_name, full_address, latitude, longitude, place_id ' \
          'FROM places WHERE local_name LIKE ?'
    param = '%' + place + '%'

    for place in cursor.execute(sql, (param,)):
        place_modal = {}
        place_modal['local_name'] = place[0]
        place_modal['full_address'] = place[1]
        place_modal['latitude'] = place[2]
        place_modal['longitude'] = place[3]
        place_modal['place_id'] = place[4]
        places['places'].append(place_modal)

    conn.close()
    return places['places'][0]


def delete_one_place(place):
    """ Delete one place on database. """
    conn = sqlite3.connect('places.db')
    cursor = conn.cursor()

    param = '%' + place + '%'
    sql = 'DELETE FROM places WHERE local_name LIKE ?'
    cursor.execute(sql, (param,))
    conn.commit()

    conn.close()
