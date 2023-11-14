#!/usr/bin/python3
"""
This module defines a class - Rectangle
"""


class Rectangle:
    """
    This class has two attributes
    """

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        function to return width if setter checks have passed
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter validates if value is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        function to return height if setter checks have passed
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter validates if value is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        counter = 0
        output = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            while counter < self.__height:
                output += "#"*self.__width
                if counter == (self.__height - 1):
                    break
                output += "\n"
                counter += 1
        return output

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
