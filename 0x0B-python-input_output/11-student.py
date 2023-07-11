#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve (optional).

        Returns:
            dict: Dictionary representing the attributes
            of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of Student instance with values from dictionary.

        Args:
            json (dict): Dictionary containing attribute-value pairs
        """
        for attr, value in json.items():
            setattr(self, attr, value)
