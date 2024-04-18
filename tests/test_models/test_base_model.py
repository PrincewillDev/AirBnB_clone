
#import unittest module
import unittest

# import module to test
from models.base_model import BaseModel

class  TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model1 = BaseModel()
    
    def test_save_method(self):
        """Check if created_at is equal to updated_at """
        self.assertGreaterEqual(self.model1.updated_at, self.model1.created_at)

    def test_to_dict_method(self):
        """Testing the to_dict method: To ensure it returns data as dictionary"""
        baseModelDict = self.model1.to_dict()
        self.assertIsInstance(baseModelDict, dict)

    def test_id_attribute(self):
        baseModelId = self.model1.id
        self.assertTrue(baseModelId)

    def test_created_at_attribute(self):
        baseModelInstance = self.model1.created_at
        self.assertTrue(baseModelInstance)
    
    def test_str_method(self):
        baseModelInstance = self.model1.__str__
        self.assertTrue(baseModelInstance)

if __name__ == "__main__":
    unittest.main()