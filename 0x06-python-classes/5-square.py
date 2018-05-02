#!/usr/bin/python3
'''
An empty class Square
'''


class Square():
    def __init__(self, size=0):
        '''Instantiation of private instance attribute size
        '''
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''A method that returns the area of a square
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''A method that prints a square
        '''
        if self.__size is 0:
            print ("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
