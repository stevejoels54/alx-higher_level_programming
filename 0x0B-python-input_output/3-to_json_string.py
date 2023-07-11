#!/usr/bin/python3
"""Function converts string to json"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of an object (string)

    Args:
        my_obj: The object to be converted to JSON

    Returns:
        A string representing the JSON serialization of the object
    """
    return json.dumps(my_obj)
