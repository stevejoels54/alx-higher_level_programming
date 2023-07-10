#!/usr/bin/python3
"""Defines class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Methods:
        __init__(self, size): Initialize a Square instance.
        area(self): Calculate and return the area of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
