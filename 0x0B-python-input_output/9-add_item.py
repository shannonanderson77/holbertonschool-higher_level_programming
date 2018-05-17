#!/usr/bin/python3
'''
   A script that adds all arguments to a Python list,
   and then save them to a file
'''
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


argv = sys.argv[1:]
try:
    new_object = load_from_json_file("add_item.json")
    save_to_json_file(new_object + argv, "add_item.json")
except Exception:
    save_to_json_file(argv, "add_item.json")
