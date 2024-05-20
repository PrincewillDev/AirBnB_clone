#!/usr/bin/python3
"""This module is uses unittest to test the file storage model / storage engine.
"""
import unittest
import os
from models.engine.file_storage import FileStorage

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