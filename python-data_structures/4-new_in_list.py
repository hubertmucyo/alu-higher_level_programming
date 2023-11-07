#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        if idx < 0:
        copy_lt = my_list[:]
        return copy_lt
    elif idx >= len(my_list):
        return copy_lt
    else:
        copy_lt = copy_2
        copy_2[idx] = element
        return copy_2
