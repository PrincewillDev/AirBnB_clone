#!/usr/bin/python3
"""Unit test for StateModel class."""

import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    """
    This class contains tests for the State class.
    """

    def setUp(self):
        """
        Sets up the test fixture.
        This method is called before each test method.
        It creates a new instance of the State class.
        """
        self.state = State()

    def test_state_name_type(self):
        """
        Tests that the name attribute of the State class is a string.
        """
        self.assertIsInstance(self.state.name, str)
