#!/usr/bin/python3
"""
This module defines the user model for the AirBnB data table.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """This class represents a user entity, encapsulating its attributes and behaviors.
It provides a foundation for user data management and interactions within the application.

Attributes:
- email (str): The user's email address.
- password (str): The user's password (stored securely).
- first_name (str): The user's first name.
- last_name (str): The user's last name.

Notes:
- This class inherits from BaseModel, which provides basic database functionality.
- Additional attributes and methods can be added as needed to support specific use cases.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    