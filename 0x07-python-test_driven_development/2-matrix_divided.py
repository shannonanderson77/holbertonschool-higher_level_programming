#!/usr/bin/python3
'''

A method that adds two integers

'''


def matrix_divided(matrix, div):
    '''function that adds two integers with exception handling'''
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for column in row:
            if len(matrix[0]) != len(matrix[1]):
                raise TypeError("Each row of the matrix must have the same size")
            if type(row) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    return [[round(column / div, 2) for column in row] for row in matrix]
