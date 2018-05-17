#!/usr/bin/python3
'''
   A function that appends a text to file and returns
   number of characters written
'''


def append_write(filename="", text=""):
    count = 0
    with open(filename, "a", encoding="utf8") as file:
        for char in text:
            count += 1
            file.write(char)
    return count
