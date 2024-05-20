#!/usr/bin/python3
"""This module is uses unittest to test the file storage model / storage engine.
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
import json
from models.place import Place
class TestFileStorage(unittest.TestCase):
    # Test class atrribute: __file_path, __objects.
    # Test all method
    # Test new method
    # Test save method
    # Test reload method
    def setUp(self):
        self.file_storage = FileStorage()
        # self.file_path = "file.json"
        
        self.place = Place()
        
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
        self.file_storage.save()
        self.obj_key = f"BaseModel.{str(self.new_Object.id)}"
        
        with open(self.file_storage._FileStorage__file_path, 'r') as jsonfile:
            jsonfile_content = jsonfile.read()
        
        self.assertIn(self.obj_key, jsonfile_content)
        
    def test_reload_method(self):
        self.file_storage.reload()
        self.obj_key = f"Place.{str(self.place.id)}"
        
        self.assertTrue(self.obj_key, self.file_storage._FileStorage__objects[self.obj_key])