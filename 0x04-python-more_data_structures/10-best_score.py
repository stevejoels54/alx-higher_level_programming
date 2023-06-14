#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = None
    prev_val = float('-inf')

    for key in a_dictionary:
        if a_dictionary[key] > prev_val:
            max_key = key
            prev_val = a_dictionary[key]

    return max_key
