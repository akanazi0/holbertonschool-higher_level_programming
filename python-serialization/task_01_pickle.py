#!/usr/bin/env python3
"""Module that defines a CustomObject class with pickling support."""
import pickle


class CustomObject:
    """Class representing a custom object that can be serialized/deserialized."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes a new CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the attributes of the CustomObject."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance to a file using pickle.

        Args:
            filename (str): The filename where the object will be saved.

        Returns:
            None if an exception occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an instance of CustomObject from a file.

        Args:
            filename (str): The filename from which to load the object.

        Returns:
            CustomObject instance if successful, None otherwise.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
