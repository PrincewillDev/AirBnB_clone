#!/usr/bin/python3
"""This module uses unittest to test the file storage model / storage engine."""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
import json
from models.place import Place
from datetime import datetime

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.file_path = "file.json"
        # Clear the file storage before each test
        with open(self.file_path, 'w') as file:
            file.write('{}')

    def test_file_path(self):
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))

    def test_objects(self):
        self.assertIsInstance(self.file_storage._FileStorage__objects, dict)

    # def test_all_method(self):
    #     all_objects = self.file_storage.all()
    #     self.assertIsInstance(all_objects, dict)

    #     new_object = User()
    #     self.file_storage.new(new_object)
    #     all_objects = self.file_storage.all()
    #     self.assertIn(new_object.to_dict(), all_objects.values())

    #     new_object2 = User()
    #     self.file_storage.new(new_object2)
    #     all_objects = self.file_storage.all()
    #     self.assertIn(new_object2.to_dict(), all_objects.values())

    #     self.assertEqual(self.file_storage.all(), self.file_storage._FileStorage__objects)
    
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
        new_obj = BaseModel()
        self.file_storage.new(new_obj)

        obj_key = f"{new_obj.__class__.__name__}.{str(new_obj.id)}"
        all_objects = self.file_storage.all()
        self.assertIn(obj_key, all_objects)

    def test_save_method(self):
        new_object = BaseModel()
        self.file_storage.new(new_object)
        self.file_storage.save()

        with open(self.file_storage._FileStorage__file_path, 'r') as jsonfile:
            jsonfile_content = jsonfile.read()

        obj_key = f"BaseModel.{str(new_object.id)}"
        self.assertIn(obj_key, jsonfile_content)

    def test_save(self):
        new_obj = BaseModel()
        new_obj.save()

        self.assertIsInstance(new_obj.created_at, datetime)

    def test_reload_method(self):
        place = Place()
        self.file_storage.new(place)
        self.file_storage.save()
        self.file_storage.reload()

        all_objects = self.file_storage.all()
        reloaded_obj = all_objects[f"Place.{str(place.id)}"]

        self.assertEqual(place.id, reloaded_obj.id)
        self.assertEqual(place.created_at, reloaded_obj.created_at)
        self.assertEqual(place.updated_at, reloaded_obj.updated_at)