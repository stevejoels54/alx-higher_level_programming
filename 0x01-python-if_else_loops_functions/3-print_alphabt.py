#!/usr/bin/python3
for alph in range(26):
    if ((chr(ord('a') + alph) != 'e') and (chr(ord('a') + alph) != 'q')):
        print("{:s}".format(chr(ord('a') + alph)), end="")

