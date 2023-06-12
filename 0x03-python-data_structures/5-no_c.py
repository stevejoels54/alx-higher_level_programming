#!/usr/bin/python3
def no_c(my_string):
    checked_string = ""
    for alph in my_string:
        if alph != 'c' and alph != 'C':
            checked_string += alph
    return checked_string
