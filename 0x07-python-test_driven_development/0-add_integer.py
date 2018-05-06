#!/usr/bin/python3
'''

A method that adds two integers

'''


def add_integer(a, b=98):
    '''function that adds two integers with exception handling'''
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return (a + b)
