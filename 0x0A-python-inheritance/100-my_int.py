#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """
    MyInt class, inherits from int.

    Methods:
        __eq__(self, other): Implement the inverted == operator.
        __ne__(self, other): Implement the inverted != operator.
    """

    def __eq__(self, other):
        """
        Implement inverted == operator.

        Args:
            other: The value to compare with.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Implement inverted != operator.

        Args:
            other: The value to compare with..
        """
        return super().__eq__(other)
