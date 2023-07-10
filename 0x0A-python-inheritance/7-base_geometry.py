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

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
