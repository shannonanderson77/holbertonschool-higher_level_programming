#!/usr/bin/python3
'''
   A module that defines a Base class
'''
import json


class Base(object):
    ''' A Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        ''' A function that returns a JSON string of a dictionary'''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
