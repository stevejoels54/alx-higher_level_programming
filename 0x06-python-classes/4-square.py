#!/usr/bin/python3
"""Square class"""


class Square:
    """square class representation"""

    def __init__(self, size=0):
        """init new square
        Args:
            size (int): size of new square
        """

        self.size = size

    @property
    def size(self):
        """set current size to square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns current square area"""
        return self.__size * self.__size
