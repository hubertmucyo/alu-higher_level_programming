#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp_list = list()
    for temp in my_list:
        if temp % 2 == 0:
            temp_list.append(True)
        else:
            temp_list.append(False)
    return temp_list
