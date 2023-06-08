#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calc(args):
    num_of_args = len(args) - 1
    if num_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    operator = args[2]
    b = int(args[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, result))


if __name__ == "__main__":
    import sys
    calc(sys.argv)
