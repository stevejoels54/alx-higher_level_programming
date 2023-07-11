#!/usr/bin/python3
"""Function that text file text replacement"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line
    containing a specific string in a file

    Args:
        filename (str): name of the file.
        search_string (str): string to search for
        new_string (str): line of text to insert
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()
