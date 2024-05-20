#!/usr/bin/python3
"""The FileStorage module is a class that handles the serialization and deserialization of objects to and from a JSON file. It is used to store and retrieve objects, ensuring data persistence.
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
import json
import os

class_list = {
    "BaseModel" : BaseModel,
    "User" : User,
    "Amenity" : Amenity,
    "City" : City,
    "State" : State,
    "Review" : Review,
    "Place" : Place,
}
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
                    classname = value['__class__']
                    obj = value
                    FileStorage.__objects[key] = class_list[classname](**obj)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                raise Exception("An error occurred while processing the file") from e