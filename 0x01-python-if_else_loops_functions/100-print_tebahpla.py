#!/usr/bin/python3
for alph in range(25, -1, -1):
    if (alph % 2 == 0):
         letter = chr(ord('a') + alph - 32)
    else:
        letter = chr(ord('a') + alph)
    print("{:s}".format(letter), end="")
