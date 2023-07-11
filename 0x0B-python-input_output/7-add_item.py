#!/usr/bin/python3
"""Adds arguments to Python list and saves to a file"""
import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_arguments_to_list():
    """
    Add all arguments to a Python list and save them to a file.
    """

    filename = 'add_item.json'

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    add_arguments_to_list()
