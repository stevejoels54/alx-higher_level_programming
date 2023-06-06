#!/usr/bin/python3
def uppercase(str):
    for alph in str:
        if ord('a') <= ord(alph) <= ord('z'):
            alph = chr(ord(alph) - 32)
        else:
            alph = chr(ord(alph))
        print("{:s}".format(alph), end="")
    print()
