#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    if my_list is None:
        return (None)
    for i in range(len(my_list) - 1):
        if my_list[i + 1] > my_list[i]:
            maximum = my_list[i + 1]
        else:
            maximum = my_list[i]
    return (maximum)
