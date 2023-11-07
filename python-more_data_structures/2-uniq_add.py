#!/usr/bin/python3
# adds all unique integers in a list


def uniq_add(my_list=[]):
    sum_us = 0
    temp_list = []
    for i in my_list:
        if i not in temp_list:
            temp_list.append(i)
    for temp in temp_list:
        sum_us += temp
    return sum_us
