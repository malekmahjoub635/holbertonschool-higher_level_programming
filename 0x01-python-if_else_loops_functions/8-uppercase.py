#!/usr/bin/python3
def uppercase(str):
    for C in str:
        if 123 > ord(C) > 96:
            C = chr(ord(C) - 32)
        print("{}".format(C), end="")
    print('')
