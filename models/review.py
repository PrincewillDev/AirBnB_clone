#!/usr/bin/python3
"""
This module defines the review model for the AirBnB data table.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review entity, encapsulating its attributes and behaviors.

Attributes:
- place_id (str): The ID of the place being reviewed.
- user_id (str): The ID of the user who wrote the review.
- text (str): The text content of the review.

Description:
This class provides a foundation for review data management and interactions within the application.
It inherits from BaseModel, which provides basic database functionality.

Notes:
- Additional attributes and methods can be added as needed to support specific use cases.
- This class can be used to store and manage review-related data, such as user feedback or ratings for places.

Examples:
- Create a review object: Review(place_id="123", user_id="456", text="Great experience!")
- Access review attributes: review.text, review.place_id, review.user_id
    """
    place_id = ""
    user_id = ""
    text = ""