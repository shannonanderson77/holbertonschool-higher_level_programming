#!/usr/bin/python3
'''
   A function that returns the number of lines in a file
'''


def number_of_lines(filename=""):
    count = 0
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            count += 1
    file.close()
    return count
