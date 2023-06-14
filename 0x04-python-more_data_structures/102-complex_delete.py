#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delete_keys.append(key)

    for key in delete_keys:
        a_dictionary.pop(key, None)

    return a_dictionary
