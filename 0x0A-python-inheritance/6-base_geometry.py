#!/usr/bin/python3
"""Defines empty class BaseGeometry"""


class BaseGeometry:
    """
    Base class for geometry.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message
        "area() is not implemented"
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")
