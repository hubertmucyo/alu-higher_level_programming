#!/usr/bin/python3
""" import json module to access json functions """
import json
""" returns json representation of object """


def to_json_string(my_obj):
    """ converts object to json object """
    return json.dumps(my_obj)
