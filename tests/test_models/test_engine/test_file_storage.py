#!/usr/bin/python3
"""This module is uses unittest to test the file storage model / storage engine.
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
import json
class TestFileStorage(unittest.TestCase):
    # Test class atrribute: __file_path, __objects.
    # Test all method
    # Test new method
    # Test save method
    # Test reload method
    def setUp(self):
        self.file_storage = FileStorage()
        
        
    def test_file_path(self):
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))
        
    def test_objects(self):
        self.assertIsInstance(self.file_storage._FileStorage__objects, dict)
        
    def test_all_method(self):
        allObjects = self.file_storage.all()
        self.assertIsInstance(allObjects, dict)
        Objectlength = len(allObjects)
        
        # Testing that all() updates with  new object
        self.newObject = User()
        self.assertIn(self.newObject, allObjects.values())
        self.assertTrue(len(allObjects) == Objectlength + 1)
        
       
        self.newObject2 = User()
        self.assertIn(self.newObject2, allObjects.values())
        self.assertTrue(len(allObjects) == Objectlength + 2)
        
        # Testing if the object returned by all() is same as the value in __objects 
        self.assertEqual(self.file_storage.all(), self.file_storage._FileStorage__objects)
    
    def test_new_method(self):
        self.newObj = BaseModel()
        self.file_storage.new(self.newObj)
        
        __object_dict = {}
        objValue = self.newObj.to_dict()
        obj_key = '{}.{}'.format(self.newObj.__class__.__name__, str(self.newObj.id))
        __object_dict[obj_key] = objValue
        
        self.assertIn(obj_key, self.file_storage.all())
        self.assertIsInstance(__object_dict, dict)
        
    def test_save_method(self):
        self.new_Object = BaseModel()
        
        newObj_dict = {}
        obj_key = f"{self.__class__.__name__}.{str(self.new_Object.id)}"
        obj_value = self.new_Object.to_dict()
        newObj_dict[obj_key] = obj_value
        
        with open(self.file_storage._FileStorage__file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(newObj_dict, jsonfile)

        with open(self.file_storage._FileStorage__file_path, 'r') as jsonfile:
            jsonfile_obj = jsonfile.read()
            self.assertIn(json.dumps(newObj_dict), jsonfile_obj)