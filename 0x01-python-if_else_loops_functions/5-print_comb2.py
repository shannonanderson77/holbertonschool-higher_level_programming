#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j != 9 or i != 9:
            print("{}{}, ".format(i, j), end="")
        else:
            print("{}{}".format(i, j))
