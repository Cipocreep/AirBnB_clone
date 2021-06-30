#!/usr/bin/python3
"""
Unittests for the project
"""

import os
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.city import City
from models import storage
import inspect
import time
import datetime
import models
from os import path


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
        '''Test upload method'''
        if not path.exists("file.json"):
            new_file = FileStorage()
            new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.86",
                                 updated_at="2021-02-17T22:46:38.86")
            new_city = City()
            new_file.new(new_base)
            new_file.new(new_city)
            new_file.save()
        with open("file.json", "r") as f:
            obj = json.load(f)
        self.assertEqual(type(obj), dict)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)
