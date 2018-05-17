#!/usr/bin/python3
'''
   A function that creates an Object from a “JSON file”
'''
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            return json.loads(line)
