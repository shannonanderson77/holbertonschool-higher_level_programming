#!/usr/bin/python3
'''
    Module that defines a Rectangle class
'''


class Rectangle:
    '''A Rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            return "\n".join((Rectangle.print_symbol * self.width)
                             for i in range(self.height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Function that deletes a rectangle'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
