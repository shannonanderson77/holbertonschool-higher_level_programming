#!/usr/bin/python3
'''

A method that adds two integers

'''


def say_my_name(first_name, last_name=""):
    '''function that adds two integers with exception handling'''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
