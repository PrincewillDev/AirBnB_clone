#!/usr/bin/python3
"""
This module defines the base model for the AirBnB data.
"""
import uuid
import datetime
import models
class BaseModel:
    """
        This class defines the BaseModel class which is the parent class
        for all child class that will be created for the AirBnB data set.

        Attributes:
            id: This attribute is responsible for creating a unique id
            when an instance is created.
            
            created_at: This attribute is responsible for getting the
            current date and time an instance is created.

            updated_at: This attribute is responsible for getting the
            current date and time an instance is created.

    """
    def __init__(self, *args, **kwargs):
        """
        The initialization method
        """

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")

                if key != "__class__":
                    try:
                        setattr(self, key, value)
                    except:
                        raise ValueError

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        This method return/prints the class details in a string format.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        This method updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """
        This method returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        baseModel_dict = self.__dict__.copy()
        baseModel_dict["__class__"] = self.__class__.__name__
        baseModel_dict["created_at"] = self.created_at.isoformat()
        baseModel_dict["updated_at"] = self.updated_at.isoformat()
        return baseModel_dict