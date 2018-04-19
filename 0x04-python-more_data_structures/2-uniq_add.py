#!/usr/bin/python
def uniq_add(my_list=[]):
    total = 0
    unique_list = list(set(my_list))
    if not my_list:
        return (0)
    for i in range(len(unique_list)):
        total += unique_list[i]
    return (total)
