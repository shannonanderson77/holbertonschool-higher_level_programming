#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        s = ord(str[i])
        if 97 <= s <= 123:
            s = s - 32
        print("{}".format(chr(s)), end="")
    print("")
