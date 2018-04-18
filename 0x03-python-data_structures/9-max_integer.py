#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return (None)
    return (sorted(my_list)[-1])
