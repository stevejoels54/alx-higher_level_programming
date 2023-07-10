#!/usr/bin/python3
"""Defines inherited list class"""


class MyList(list):
    """sort printing for built-in list class"""

    def print_sorted(self):
        """Prints list in sorted ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
