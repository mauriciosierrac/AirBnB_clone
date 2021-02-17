'''
module containt test
for amenity
'''
import unittest
import os
import pep8
from models.amenity import amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.am = Amenity()
        cls.am.name = 'StringTesting'

    @classmethod
    def tearDownClass(cls):
        del cls.am
        try:
            am.remove("file.json")
        except FileNotFoundError
        pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass(self):
        self.assertTrue(issubclass(self.am.__class__, BaseModel), True)

    def test_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attr(self):
        self.assertTrue('id' in self.am.__dict__)
        self.assertTrue('created_at' in self.am.__dict__)
        self.assertTrue('updated_at' in self.am.__dict__)
        self.assertTrue('name' in self.am.__dict__)

    def test__strings(self):
        self.assertEqual(type(self.am.name), str)

    def test_save(self):
        self.am.save()
        self.assertNotEqual(self.am.created_at, self.am.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.am), True)


if __name__ == "__main__":
    unittest.main()
