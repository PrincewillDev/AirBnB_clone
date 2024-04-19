#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os

class FileStorage:
    """
    FileStorage class for serializing and deserializing objects to and from
    json file.
    """
    __file_path = os.path.join("./models/engine","file.json")
    __objects = {}

    def __init__(self):
        """init method for FileStorage class
        """
        pass

    def all(self):
        """returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Attributes:
            obj (Python object): The entered object to set
        """
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = dict()
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects ONLY if the JSON file
        exists, otherwise, do nothing.  If the file doesn't exist, exceptions
        should be raised
        """
        if os.path.exists("./models/engine/file.json"):
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                    json_load = json.load(file)
                for key, value in json_load.items():
                    FileStorage.__objects[key] = BaseModel(**value)
            except (FileNotFoundError, json.JSONDecodeError):
                pass