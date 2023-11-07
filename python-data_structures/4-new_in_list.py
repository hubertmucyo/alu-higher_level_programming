#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy_lt = my_list[:]
        return copy_lt
    elif idx >= len(my_list):
        copy_l = my_list[:]
        return copy_l
    else:
        copy_two = my_list[:]
        copy_two[idx] = element
        return copy_two
