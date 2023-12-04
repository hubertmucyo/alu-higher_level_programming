#!/usr/bin/python3
"""
module prints out details
of name
"""


def say_my_name(first_name, last_name=""):
    """
    function does simple checking of type
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
