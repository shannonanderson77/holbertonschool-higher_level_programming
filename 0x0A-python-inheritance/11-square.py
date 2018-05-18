#!/usr/bin/python3
'''
   A subclass Square that inherits from Rectangle
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A Square class '''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[{}] {}/{}".format(
           type(self).__name__, self.__size, self.__size))
