#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [y for y in my_string if y != 'c' and y != 'C']
    return ("".join(copy))
