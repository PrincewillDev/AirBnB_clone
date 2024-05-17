#!/usr/bin/python3
"""
This module defines the place model for the AirBnB data table.
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place entity, encapsulating its attributes and behaviors.

Attributes:
- city_id (str): The ID of the city where the place is located.
- user_id (str): The ID of the user who owns the place.
- name (str): The name of the place.
- description (str): A brief description of the place.
- number_rooms (int): The number of rooms in the place.
- number_bathrooms (int): The number of bathrooms in the place.
- max_guest (int): The maximum number of guests the place can accommodate.
- price_by_night (int): The price per night for the place.
- latitude (float): The latitude coordinate of the place's location.
- longitude (float): The longitude coordinate of the place's location.
- amenity_ids (list): A list of IDs of amenities available at the place.

Description:
This class provides a foundation for place data management and interactions within the application.
It inherits from BaseModel, which provides basic database functionality.

Notes:
- Additional attributes and methods can be added as needed to support specific use cases.
- This class can be used to store and manage place-related data, such as hotel rooms, apartments, or vacation rentals.

Examples:
- Create a place object: Place(name="Cozy Apartment", city_id="123", user_id="456", ...)
- Access place attributes: place.name, place.number_rooms, place.amenity_ids, etc.
    """
    city_id =  ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []