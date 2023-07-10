#!/usr/bin/python3
"""Class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class; False otherwise.
    """
    return isinstance(obj, a_class)
