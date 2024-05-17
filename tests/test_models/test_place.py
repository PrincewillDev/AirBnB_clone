#!/usr/bin/python3
"""Unit test for PlaceModel class."""

import unittest
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """
    This class contains tests for the Place class.
    It verifies the data types of various attributes.
    """

    def setUp(self):
        """
        Sets up the test fixture.
        This method is called before each test method.
        It creates a new instance of the Place class.
        """
        self.place = Place()

    def test_cityId_attribute(self):
        """
        Tests that the city_id attribute of the Place class is a string.
        """
        self.assertIsInstance(self.place.city_id, str)

    def test_userId_attribute(self):
        """
        Tests that the user_id attribute of the Place class is a string.
        """
        self.assertIsInstance(self.place.user_id, str)

    def test_name_attribute(self):
        """
        Tests that the name attribute of the Place class is a string.
        """
        self.assertIsInstance(self.place.name, str)

    def test_description_attribute(self):
        """
        Tests that the description attribute of the Place class is a string.
        """
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_attribute(self):
        """
        Tests that the number_rooms attribute of the Place class is an integer.
        """
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_attribute(self):
        """
        Tests that the number_bathrooms attribute is an integer.
        """
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_attribute(self):
        """
        Tests that the max_guest attribute of the Place class is an integer.
        """
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_attribute(self):
        """
        Tests that the price_by_night attribute is an integer.
        """
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_attribute(self):
        """
        Tests that the latitude attribute of the Place class is a float.
        """
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_attribute(self):
        """
        Tests that the longitude attribute of the Place class is a float.
        """
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_attribute(self):
        """
        Tests that the amenity_ids attribute of the Place class is a list.
        """
        self.assertIsInstance(self.place.amenity_ids, list)
