#!/usr/bin/python3
'''

A method that adds two integers

'''


def text_indentation(text):
    '''function that adds two integers with exception handling'''
    for i in range(len(text)):
        if type(text) is not str:
            raise TypeError("text must be a string")
        if text[i] is '?':
            print("")
            print("")
        elif text[i] is ':':
            print("")
            print("")
        elif text[i] is '.':
            print("")
            print("")
        else:
            print("{:s}".format(text[i]), end="")
