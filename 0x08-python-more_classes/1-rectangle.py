#!/usr/bin/python3
'''
    Module that defines a Rectangle class
'''


class Rectangle:
    '''A Rectangle class'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Width property'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an ineger")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Height property'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an ineger")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
