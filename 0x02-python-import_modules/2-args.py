#!/usr/bin/python3
def print_args(args):
    num_of_args = len(args) - 1
    if num_of_args == 0:
        print("{:d} arguments.".format(num_of_args))
    else:
        if num_of_args == 1:
            print("{:d} argument:".format(num_of_args))
        else:
            print("{:d} arguments:".format(num_of_args))
        for num in range(1, num_of_args + 1):
            print("{:d}: {:s}".format(num, args[num]))


if __name__ == "__main__":
    import sys
    print_args(sys.argv)
