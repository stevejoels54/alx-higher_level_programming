#!/usr/bin/python3
"""Function that writes to file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and
    return the number of characters written

    Args:
        filename: The name of the file to write (optional)
        text: The string to write to the file (optional)

    Returns:
        The number of chars written to the file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
