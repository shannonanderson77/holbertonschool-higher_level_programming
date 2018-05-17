#!/usr/bin/python3
'''
   A function that prints n lines of a file to stdout
'''


def read_lines(filename="", nb_lines=0):
    count = 0
    with open(filename, "r", encoding="utf8") as file:
        for count, value in enumerate(file, 1):
            if nb_lines >= count or nb_lines <= 0:
                print("{}".format(value), end="")
