#!/usr/bin/python3
'''
   A function that writes a text to file and returns
   number of characters written
'''


def write_file(filename="", text=""):
    count = 0
    with open(filename, "w", encoding="utf8") as file:
        for char in text:
            count += 1
            file.write(char)
    return count
