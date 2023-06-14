#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_number = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for i in range(len(roman_string) - 1, -1, -1):
        numeral = roman_string[i]
        value = roman_number[numeral]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    return total
