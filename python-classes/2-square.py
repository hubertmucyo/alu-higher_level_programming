#!/usr/bin/python3
"""
NO MODULE USE
"""


class Square:
    """
    CLASS THAT ASSIGNS SIZE OF SQUARE
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
