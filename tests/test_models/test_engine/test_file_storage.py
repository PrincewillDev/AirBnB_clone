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
        """Set up a test environment before each test."""
        self.file_storage = FileStorage()
        self.file_path = self.file_storage._FileStorage__file_path
        # Clear the file storage before each test
        with open(self.file_path, 'w') as file:
            file.write('{}')
        self.file_storage.reload()

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path(self):
        self.assertTrue(os.path.exists(self.file_path))

    def test_objects(self):
        self.assertIsInstance(self.file_storage._FileStorage__objects, dict)

    def test_all_method(self):
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)
        object_length = len(all_objects)

        # Create a new User object and save it
        new_object = User()
        self.file_storage.new(new_object)
        self.file_storage.save()

        all_objects = self.file_storage.all()
        self.assertIn(new_object, all_objects.values())
        self.assertEqual(len(all_objects), object_length + 1)

    def test_new_method(self):
        new_obj = BaseModel()
        self.file_storage.new(new_obj)

        obj_key = f"{new_obj.__class__.__name__}.{new_obj.id}"
        all_objects = self.file_storage.all()
        self.assertIn(obj_key, all_objects)

    def test_save_method(self):
        new_object = BaseModel()
        self.file_storage.new(new_object)
        self.file_storage.save()

        with open(self.file_storage._FileStorage__file_path, 'r') as jsonfile:
            jsonfile_content = json.load(jsonfile)

        obj_key = f"BaseModel.{new_object.id}"
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
        reloaded_obj = all_objects[f"Place.{place.id}"]

        self.assertEqual(place.id, reloaded_obj.id)
        self.assertEqual(place.created_at, reloaded_obj.created_at)
        self.assertEqual(place.updated_at, reloaded_obj.updated_at)

if __name__ == "__main__":
    unittest.main()
