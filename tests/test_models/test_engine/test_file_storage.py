#!/usr/bin/python3
"""
Unittests for the project
"""

import unittest
import os.path
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestsForFileStorage(unittest.TestCase):
    """ Tests for the Base Class """

    def setUp(self):
        """ Move json file if it exists """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")
        self.brba = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """ Delete test json file and put original file back """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_all(self):
        """ type of dictionary """
        my_user = User()
        my_state = State()
        my_city = City()
        my_amenity = Amenity()
        my_place = Place()
        my_review = Review()
        storage.reload()
        self.assertEqual(type(self.brba.all()), dict)
        self.assertTrue("BaseModel" in str(self.brba.all()))
        self.assertTrue("User" in str(self.brba.all()))
        self.assertTrue("State" in str(self.brba.all()))
        self.assertTrue("City" in str(self.brba.all()))
        self.assertTrue("Amenity" in str(self.brba.all()))
        self.assertTrue("Place" in str(self.brba.all()))
        self.assertTrue("Review" in str(self.brba.all()))

    def test_new(self):
        """ new method """
        storage.reload()
        self.brba.new(BaseModel())
        self.assertTrue(self.brba.all())

    def test_save(self):
        """ json file check """
        storage.reload()
        self.brba.new(BaseModel())
        self.brba.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue("BaseModel" in str(self.brba.all()))

    def test_reload(self):
        """ reload method """
        storage.reload()
        key = "BaseModel" + "." + self.my_model.id
        self.brba.new(self.my_model)
        self.brba.save()
        self.brba.reload()
        self.assertTrue(self.brba.all()[key])
        self.assertTrue("BaseModel" in str(self.brba.all()))
