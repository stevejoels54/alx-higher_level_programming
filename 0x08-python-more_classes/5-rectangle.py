#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class definition"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle object.

        Parameters:
           width (int, optional): The width of the rectangle. Defaults to 0.
           height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
           TypeError: If the width or height is not an integer.
           ValueError: If the width or height is less than 0.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns area of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns printable representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for _ in range(self.__height):
                rectangle += "#" * self.__width + "\n"
            return rectangle.rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
