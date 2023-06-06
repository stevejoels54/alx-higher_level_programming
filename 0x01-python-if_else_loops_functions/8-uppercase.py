#!/usr/bin/python3
def uppercase(str):
    for alph in str:
        if ord('a') <= ord(alph) <= ord('z'):
            print("{:s}".format(chr(ord(alph) - 32)), end="")
        else:
            print(alph, end='')
