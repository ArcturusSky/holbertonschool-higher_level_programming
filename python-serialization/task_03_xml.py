#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data to.

    Example:
        dictionary = {'name': 'John', 'age': '28', 'city': 'New York'}
        serialize_to_xml(dictionary, 'data.xml')
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The name of the file to read the XML data from.

    Returns:
        dict: The deserialized dictionary containing data from the XML file.

    Example:
        deserialized_data = deserialize_from_xml('data.xml')
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dictionary = {}
    
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary

if __name__ == "__main__":
    """
    Test the XML serialization and deserialization functions.

    Creates a sample dictionary, serializes it to an XML file, then
    deserializes the XML file back into a dictionary and prints the result.

    Example:
        Output:
        Dictionary serialized to data.xml
        Deserialized Data:
        {'name': 'John', 'age': '28', 'city': 'New York'}
    """
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
