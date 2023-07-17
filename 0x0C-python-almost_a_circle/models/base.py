#!/usr/bin/python3
"""Defines base model class"""

class Base:
    """Represent base model
    Represents base for all other classes
    Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base.
        Args:
            id (int): Identity of new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects