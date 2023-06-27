#!/usr/bin/python3
class Square:
    """square class representation"""

    def __init__(self, size=0):
        """init new square
        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
