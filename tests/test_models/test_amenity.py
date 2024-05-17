#!/usr/bin/python3
"""Unit test for AmenityModel class."""

import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """
    This class contains tests for the Amenity class.
    It verifies the data types of various attributes.
    """

    def setUp(self):
        """
        Sets up the test fixture.
        This method is called before each test method.
        It creates a new instance of the Amenity class.
        """
        self.amenity = Amenity()

    def test_state_name_type(self):
        """
        Tests that the name attribute of the Amenity class is a string.
        This represents the name of the amenity, such as 'Wi-Fi' or 'TV'.
        """
        self.assertIsInstance(self.amenity.name, str)
