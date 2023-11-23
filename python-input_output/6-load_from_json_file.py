#!/usr/bin/python3
""" use json module """
import json
""" read and load with json module """


def load_from_json_file(filename):
    """ read json from file and convert to object """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
