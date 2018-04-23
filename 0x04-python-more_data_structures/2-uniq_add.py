#!/usr/bin/python
def uniq_add(my_list=[]):
    total = 0
    for item in set(my_list):
        total += item
    return (total)
