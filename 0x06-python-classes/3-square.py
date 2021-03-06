#!/usr/bin/python3
'''
An empty class Square
'''


class Square():
    def __init__(self, size=0):
        '''Instantiation of private instance attribute size
        '''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''A method that returns the area of a square
        '''
        return (self.__size * self.__size)
