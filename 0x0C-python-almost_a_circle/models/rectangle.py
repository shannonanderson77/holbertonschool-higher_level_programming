#!/usr/bin/python3
'''
   A module that defines a Rectangle class

'''
from models.base import Base
from sys import argv


class Rectangle(Base):
    ''' A Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        ''' A function that prints a "#" Rectangle'''
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def area(self):
        ''' A function that returns the area of a rectangle'''
        return self.width * self.height

    def __str__(self):
        ''' A string representation of a Rectangle object'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
          self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        ''' A function that assigns an argument to each attribute'''
        for i in range(len(args)):
            try:
                setattr(self, id, args[0])
                setattr(self, width, args[1])
                setattr(self, height, args[2])
                setattr(self, x, args[3])
                setattr(self, y, args[4])
            except IndexError:
                pass
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' A function that returns a dictionary representation of a Square'''
        return {'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y, 'id': self.id}
