#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for r in my_string:
        if r is not 'c' and r is not 'C':
            new_str += r
    return (new_str)
