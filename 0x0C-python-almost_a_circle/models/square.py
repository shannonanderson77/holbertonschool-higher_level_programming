#!/usr/bin/python3
'''
   A module that defines a Square class that inherits from Rectangle

'''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' A Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        ''' A string representation of a Square object'''
        return "[Square] ({}) {}/{} - {}".format(
           self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        ''' A function that assigns an argument to each attribute'''
        for i in range(len(args)):
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' A function that returns a dictionary representation of a Square'''
        return {'size': self.width, 'x': self.x, 'y': self.y, 'id': self.id}
