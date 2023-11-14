#!/usr/bin/python3
"""
NO MODULE USED
"""


class Square:
    """
    SQUARE CLASS
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        return self._Square__size**2
