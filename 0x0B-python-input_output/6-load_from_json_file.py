#!/usr/bin/python3
"""Function that creates Object from JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation

    Args:
        my_obj: The object to be written
        filename: The name of the file to write to
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
