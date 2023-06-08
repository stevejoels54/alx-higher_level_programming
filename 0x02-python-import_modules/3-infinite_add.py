#!/usr/bin/python3
def sum_args(args):
    num_of_args = len(args) - 1
    if num_of_args == 0:
        print("{:d}".format(num_of_args))
    else:
        sum = 0
        for arg in args[1:]:
            sum += int(arg)
        print(sum)


if __name__ == "__main__":
    import sys
    sum_args(sys.argv)
