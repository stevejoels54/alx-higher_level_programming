#!/usr/bin/python3
"""Defines function to read text files"""


def read_file(filename=""):
    """
    Reads text file in (UTF-8) and print contents to stdout

    Args:
        filename: The name of the file to read (optional)
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
