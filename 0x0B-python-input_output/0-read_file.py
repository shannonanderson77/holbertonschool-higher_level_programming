#!/usr/bin/python3
'''
   A function that prints contents of a file to stdout
'''


def read_file(filename=""):
    with open(filename, "r",  encoding="utf8") as file:
        text = file.read()
        print("{}".format(text), end="")
