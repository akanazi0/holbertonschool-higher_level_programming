#!/usr/bin/env python3
"""Module for serializing and deserializing data using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary containing data to serialize.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes XML data from a file into a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: The reconstructed Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    deserialized_data = {}
    for child in root:
        deserialized_data[child.tag] = child.text

    return deserialized_data
