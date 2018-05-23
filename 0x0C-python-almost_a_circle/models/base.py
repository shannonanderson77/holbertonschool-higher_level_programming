#!/usr/bin/python3
'''
   A module that defines a Base class
'''
import json


class Base():
    ''' A Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' A function that returns a JSON string of a dictionary'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        ''' A function that returns the list of the
            JSON string representation json_string'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' A function that writes a JSON string to file'''
        filename = cls.__name__ + ".json"
        json_string = Base.to_json_string(cls.to_dictionary(list_objs))
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write([])
            else:
                file.write(json_string)
        file.close()

    @classmethod
    def create(cls, **dictionary):
        ''' A function that returns an instance with all attribbutes set'''
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        return dummy.update(**dictionary)
