#!/usr/bin/python3
'''
   A function that writes an Object to a text file, using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf8") as file:
        file.write(json.dumps(my_obj))
