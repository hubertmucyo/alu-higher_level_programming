#!/usr/bin/python3
""" print sqaure
with characters
"""


def print_square(size):
    """just the function body
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    length = size
    while size > 0:
        print("#" * length)
        size -= 1
