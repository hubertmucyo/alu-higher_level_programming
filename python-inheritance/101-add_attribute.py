#!/usr/bin/python3
""" module has one function """


def add_attribute(ob, attr, value):
    """
    adding attribute to class
    """
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, value)
    else:
        raise TypeError("can't add new attribute")
