#!/usr/bin/python3
#print elements at index
def element_at(my_list, idx):
    if idx < 0:
        print("None")
    elif idx > len(my_list):
        print("None")
    else:
        return my_list[idx]
