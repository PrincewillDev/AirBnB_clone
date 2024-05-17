#!/usr/bin/python3
"""Unit test for CityModel class."""

import unittest
from models.city import City


class TestCityClass(unittest.TestCase):
    """
    This class contains tests for the City class.
    It verifies the data types of various attributes.
    """

    def setUp(self):
        """
        Sets up the test fixture.
        This method is called before each test method.
        It creates a new instance of the City class.
        """
        self.city = City()

    def test_stateId_attribute(self):
        """
        Tests that the state_id attribute of the City class is a string.
        This attribute represents the unique identifier of the state
        that the city belongs to.
        """
        self.assertIsInstance(self.city.state_id, str)

    def test_city_name_attribute(self):
        """
        Tests that the name attribute of the City class is a string.
        This attribute represents the name of the city.
        """
        self.assertIsInstance(self.city.name, str)
