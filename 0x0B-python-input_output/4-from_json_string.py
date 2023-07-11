#!/usr/bin/python3
"""Function converts json to object func"""


import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string

    Args:
        my_str: The JSON string representing the object

    Returns:
        The Python data structure represented by JSON string
    """
    return json.loads(my_str)
