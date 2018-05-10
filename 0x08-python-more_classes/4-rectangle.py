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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Height property'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Function that returns the area of a square'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Function that returns the perimeter of a square'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        '''Function that returns the informal string
           representation of a square'''
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(("#" * self.width) for i in range(self.height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
