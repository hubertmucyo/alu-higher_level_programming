#!/usr/bin/python3
""" student to json filter """


class Student:
    """ this is a student class """

    def __init__(self, first_name, last_name, age):
        """ just doing init for variables """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method converts to json """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
