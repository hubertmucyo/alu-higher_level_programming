#!/usr/bin/python3
""" module for opening file """


def read_file(filename=""):
    """ funciton opens and read file passed by name """
    with open(filename, encoding="utf-8") as f:
        out_data = f.read()
        print("{}".format(out_data), end="")
