#!/usr/bin/python3
"""Function writes json to file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: Object to be written.
        filename: Name of the file to write to
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
