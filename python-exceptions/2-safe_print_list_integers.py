#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    num = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            num += 1
        except (TypeError, ValueError):
            pass
        count += 1
    print()
    return num
