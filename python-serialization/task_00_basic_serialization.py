#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Parameters:
    data (dict): The Python dictionary to be serialized.
    filename (str): The name of the file to save the JSON data.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
        
def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.
    
    Parameters:
    filename (str): The name of the JSON file to load.
    
    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
