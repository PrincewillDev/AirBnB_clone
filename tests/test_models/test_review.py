#!/usr/bin/python3
"""Unit test for ReviewModel class."""

import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """
    This class contains tests for the Review class.
    It verifies the data types of various attributes.
    """

    def setUp(self):
        """
        Sets up the test fixture.
        This method is called before each test method.
        It creates a new instance of the Review class.
        """
        self.review = Review()

    def test_placeId_type(self):
        """
        Tests that the place_id attribute of the Review class is a string.
        """
        self.assertIsInstance(self.review.place_id, str)

    def test_userId_type(self):
        """
        Tests that the user_id attribute of the Review class is a string.
        """
        self.assertIsInstance(self.review.user_id, str)

    def test_text_type(self):
        """
        Tests that the text attribute of the Review class is a string.
        """
        self.assertIsInstance(self.review.text, str)
