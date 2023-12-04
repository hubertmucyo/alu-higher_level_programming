#!/usr/bin/python3
"""
module for text indentation
"""


def text_indentation(text):
    """ just the function
    here """

    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for c in text:
        line += c
        if c in ['.', '?', ':']:
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end="")
