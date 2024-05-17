#!/usr/bin/python3
"""
This module defines the amenity model for the AirBnB data table.
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity entity, encapsulating its attributes and behaviors.

Attributes:
- name (str): The name of the amenity.

Description:
This class provides a foundation for amenity data management and interactions within the application.
It inherits from BaseModel, which provides basic database functionality.

Notes:
- Additional attributes and methods can be added as needed to support specific use cases.
- This class can be used to store and manage amenity-related data, such as hotel amenities (e.g. gym, pool, restaurant) or property features (e.g. air conditioning, Wi-Fi, parking).

Examples:
- Create an amenity object: Amenity(name="Free Wi-Fi")
- Access amenity name: amenity.name
    """
    name =  ""