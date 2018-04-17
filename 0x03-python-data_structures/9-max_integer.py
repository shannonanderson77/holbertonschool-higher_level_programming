#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list is None:
        return (None)
    for number in my_list:
        if max > number:
            max = max
        else:
            max = number
    return (max)
