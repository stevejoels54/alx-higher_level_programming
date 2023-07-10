#!/usr/bin/python3
"""Function that adds attributes to objects"""


def add_attribute(obj, attr, value):
    """
    Add new attribute to an object if possible.

    Args:
        obj: Object to add the attribute to.
        attr: Name of the attribute.
        value: Value of the attribute.

    Raises:
        TypeError: If the object can't have new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
