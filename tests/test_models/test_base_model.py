""" Unittest for the base models class

    Class: TestBaseModel

"""

#import unittest module
import unittest

# import module to test
from models.base_model import BaseModel

class  TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model1 = BaseModel()
    
    def test_save_method(self):
        """Check if to updated_at is greater than created_at after calling the save method: This ensures that when an item is saved the time is updated """
        # self.assertEqual(self.model1.created_at, self.model1.updated_at)
        self.model1.name = "Model"
        self.model1.save()

        self.assertNotEqual(self.model1.created_at, self.model1.updated_at)
        self.assertGreaterEqual(self.model1.updated_at, self.model1.created_at)

    def test_to_dict_method(self):
        """Testing the to_dict method: To ensure it returns data as dictionary"""
        baseModelDict = self.model1.to_dict()
        # Check that value of __class__ key is class name of object
        self.assertEqual(baseModelDict['__class__'], 'BaseModel')
        self.assertIsInstance(baseModelDict, dict)      

    def test_id_attribute(self):
        """Testing if the right uuid is generated"""
        baseModelId = self.model1.id
        self.assertTrue(baseModelId)

    def test_created_at_attribute(self):
        """Testing if the right time is generated when an instance is created"""

        baseModelInstance = self.model1.created_at
        self.assertTrue(baseModelInstance)
    
    def test_str_method(self):
        """Testing the str method to ensure that instance of the class is returned correctly in str format"""

        baseModelInstance = self.model1.__str__
        self.assertTrue(baseModelInstance)

if __name__ == "__main__":
    unittest.main()