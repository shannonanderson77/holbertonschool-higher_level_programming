#!/usr/bin/python3
'''
An empty class Square
'''


class Square():
    def __init__(self, size=0, position=(0, 0)):
        '''Instantiation of private instance attribute size
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(self.__position) is not tuple\
                or self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        '''A method that returns the area of a square
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''A method that prints a square
        '''
        if self.__size == 0:
            print("" * self.__position[1])
        else:
            for i in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
