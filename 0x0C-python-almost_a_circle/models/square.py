#!/usr/bin/python3
"""Module containing Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate square. Defaults to 0.
            y (int, optional): y-coordinate square. Defaults to 0.
            id (int, optional): ID of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not positive.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the Square instance attributes.

        Args:
            *args: Variable length arguments containing id, size, x, and y.
            **kwargs: Dictionary containing the attributes to update.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
