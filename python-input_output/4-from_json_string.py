#!/usr/bin/python3
""" using json module to access use """
import json
""" module converts json string to object """


def from_json_string(my_str):
    """ convert obj to json """
    return json.loads(my_str)
