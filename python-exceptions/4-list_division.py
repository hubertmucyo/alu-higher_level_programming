#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    counter = 0
    result = 0
    while counter < list_length:
        try:
            result = 0
            result = my_list_1[counter]/my_list_2[counter]
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(result)
        except IndexError:
            print("out of range")
            new_list.append(result)
        finally:
            counter += 1
    return new_list
