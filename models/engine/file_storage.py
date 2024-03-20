import json
from os import path

class FileStorage():
    __file_path = path("/models/engine/file.json")
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj): 
        pass

    def save(self):
        pass

    def reload(self):
        pass