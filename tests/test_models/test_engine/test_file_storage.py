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
from datetime import datetime
import models
from os import path


class TestsForFileStorage(unittest.TestCase):
    """ Tests for the Base Class """

    def test_atr(self):
        """ Tests for attributes """
        s1 = FileStorage()
        self.assertTrue(hasattr(s1, "_FileStorage__objects"))
        self.assertTrue(hasattr(s1, "_FileStorage__file_path"))

    def test_class(self):
        """ Makes sure we're making the class """
        s1 = FileStorage()
        self.assertTrue(type(s1), FileStorage)

    def test_all_new(self):
        """ Tests the functionality of new and all """
        setattr(storage, "_FileStorage__objects", dict())
        m1 = BaseModel()
        m2 = BaseModel()
        new_dict = dict()
        new_dict["BaseModel." + m1.id] = m1
        new_dict["BaseModel." + m2.id] = m2
        thing = storage.all()
        self.assertDictEqual(thing, new_dict)

    def test_save_reload(self):
        """ Test save and reload """
        os.remove('file.json')
        b1 = BaseModel()
        b1.save()
        storage.reload()
        new = storage.all()
        self.assertDictEqual(new["BaseModel." + b1.id].to_dict(), b1.to_dict())
