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

    def test_doc(self):
        """ Testing for docstring """
        self.assertIsNotNone(("models.engine.file_storage".__doc__))
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_attributes(self):
        """ Testing for attributes """
        s1 = FileStorage()
        self.assertTrue(hasattr(s1, "_FileStorage__objects"))
        self.assertTrue(hasattr(s1, "_FileStorage__file_path"))

    def test_class(self):
        """ Testing Class """
        s1 = FileStorage()
        self.assertTrue(type(s1), FileStorage)

    def test_new(self):
        """ Testing new """
        setattr(storage, "_FileStorage__objects", dict())
        m1 = BaseModel()
        m2 = BaseModel()
        new_dict = dict()
        new_dict["BaseModel." + m1.id] = m1
        new_dict["BaseModel." + m2.id] = m2
        thing = storage.all()
        self.assertDictEqual(thing, new_dict)

    def test_save(self):
        """ Testing save and reload """
        os.remove('file.json')
        b1 = BaseModel()
        b1.save()
        storage.reload()
        new = storage.all()
        self.assertDictEqual(new["BaseModel." + b1.id].to_dict(), b1.to_dict())

    def test_sleep(self):
        """ Testing sleep """
        o = BaseModel()
        time.sleep(1)
        n = datetime.datetime.now().replace(microsecond=0)
        o.save()
        self.assertEqual(o.updated_at.replace(microsecond=0), n)
