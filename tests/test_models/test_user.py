#!/usr/bin/python3
"""Unit test for UserModel class."""

import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """A unittest test case class for testing the User class.

    This class contains tests for the following attributes of the User class:
    - email
    - password
    - first_name
    - last_name

    Each test method checks that the attribute is of the correct type (string).

    Attributes:
    - user1 (User): A User object used for testing.

    Methods:
    - setUp: Sets up a User object for testing.
    - test_email_type: Tests that the email attribute is a string.
    - test_password_type: Tests that the password attribute is a string.
    - test_first_name_type: Tests that the first_name attribute is a string.
    - test_last_name_type: Tests that the last_name attribute is a string.
    """

    def setUp(self):
        self.user1 = User()

    def test_email_type(self):
        self.assertIsInstance(self.user1.email, str)

    def test_password_type(self):
        self.assertIsInstance(self.user1.password, str)

    def test_first_name_type(self):
        self.assertIsInstance(self.user1.first_name, str)

    def test_last_name_type(self):
        self.assertIsInstance(self.user1.last_name, str)
