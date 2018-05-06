#!/usr/bin/python3
'''

A method that adds two integers

'''


def print_square(size):
    '''function that adds two integers with exception handling'''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
