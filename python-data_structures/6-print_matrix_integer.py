#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for record in matrix:
        counter = 0
        for i in record:
            if counter == (len(record) - 1):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            counter += 1
        print("")
