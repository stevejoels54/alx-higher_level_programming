#!/usr/bin/python3
"""Square class"""


class Square:
    """square class representation"""

    def __init__(self, size=0, position=(0, 0)):
        """init new square
        Args:
            size (int): size of new square
            position (int, int): position
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """set square position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
