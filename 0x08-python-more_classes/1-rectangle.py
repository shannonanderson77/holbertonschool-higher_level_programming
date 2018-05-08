#!/usr/bin/python3
'''
    Module that defines a Rectangle class
'''


class Rectangle:
    '''A Rectangle class'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Width property'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''Height property'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
