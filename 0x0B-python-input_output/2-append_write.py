#!/usr/bin/python3
"""Defines function that appends to file"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF-8) and
    return the number of characters added.

    Args:
        filename: The name of the file to append (optional)
        text: The string to append to the file (optional)

    Returns:
        The number of characters added to the file
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
