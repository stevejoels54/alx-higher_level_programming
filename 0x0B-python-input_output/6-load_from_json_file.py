#!/usr/bin/python3
"""Function that creates Object from JSON file"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file

    Args:
        filename: Name of the JSON file

    Returns:
        Object created from the JSON file
    """
    with open(filename, 'r') as file:
        return json.load(file)
