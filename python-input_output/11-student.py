#!/usr/bin/python3
"""
A Student class that defines a Studen (module)
"""


<<<<<<< HEAD
class Student:
    """ 
    this is a student class 
    """

    def __init__(self, first_name, last_name, age):
        """
        just doing init for variables
=======
class Student():
    """
        A Student class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """
            INIT
>>>>>>> 6427b0b5935bbdf2227a51d2669076a7153f394f
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
<<<<<<< HEAD
        method converts to json 
=======
            retrieves a dictionary representation
            of a Student instance
>>>>>>> 6427b0b5935bbdf2227a51d2669076a7153f394f
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return(self.__dict__)

    def reload_from_json(self, json):
        """
<<<<<<< HEAD
        return json 
        """
        for i,j in json.items():
            self.__dict__(i) = j
=======
        """
        for i, j in json.items():
            self.__dict__[i] = j
>>>>>>> 6427b0b5935bbdf2227a51d2669076a7153f394f
