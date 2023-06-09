#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for row in matrix:
        if not row:
            print()
            continue
        for col in range(len(row)):
            if col != len(row) - 1:
                print("{:d} ".format(row[col]), end="")
            else:
                print("{:d}".format(row[col]))
