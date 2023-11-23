#!/usr/bin/python3
""" student to json """


class Student:
    """ empty class """

    def __init__(self, first_name, last_name, age):
        """ just init public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return json format """
        return self.__dict__
