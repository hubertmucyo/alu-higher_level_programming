#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return "None"
    else:
        big_so_far = my_list[0]
        for i in my_list:
            if i > big_so_far:
                big_so_far = i
        return big_so_far
