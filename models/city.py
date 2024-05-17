#!/usr/bin/python3
"""
This module defines the city model for the AirBnB data table.
"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city entity, encapsulating its attributes and behaviors.

Attributes:
- state_id (str): The ID of the state to which the city belongs.
- name (str): The name of the city.

Description:
This class provides a foundation for city data management and interactions within the application.
It inherits from BaseModel, which provides basic database functionality.

Notes:
- Additional attributes and methods can be added as needed to support specific use cases.
- This class can be used to store and manage city-related data, such as geographic locations or municipal information.

Examples:
- Create a city object: City(name="New York", state_id="123")
- Access city attributes: city.name, city.state_id
    """
    state_id =""
    name =  ""