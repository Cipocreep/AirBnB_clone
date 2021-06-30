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
import inspect
import time
from datetime import datetime
import models
from os import path


class TestsForFileStorage(unittest.TestCase):
    """ Tests for the Base Class """

    def test_file_path(self):
        """ Testing file path """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_all(self):
        """ Testing all() """
        new_file = FileStorage()
        new_base = BaseModel(id="564778",
                             created_at="2021-07-02T22:46:38.849900",
                             updated_at="2021-07-02T22:46:38.849900")
        self.assertIsInstance(new_file, FileStorage)
        self.assertIs(type(new_file), FileStorage)
        objects = new_file.all()
        self.assertIs(type(objects), dict)

    def test_new(self):
        """ Testing new() """
        new_file = FileStorage()
        new_base = BaseModel(id="564778",
                             created_at="2021-07-02T22:46:38.849900",
                             updated_at="2021-07-02T22:46:38.849900")
        new_city = City()
        new_amenity = Amenity()
        new_user = User()
        new_place = Place()
        new_review = Review()
        new_state = State()

        new_file.new(new_base)
        new_file.new(new_city)
        new_file.new(new_amenity)
        new_file.new(new_place)
        new_file.new(new_state)
        new_file.new(new_user)
        new_file.new(new_review)

        objects = new_file.all()

        key = new_base.__class__.__name__ + "." + new_base.__dict__["id"]
        key_city = new_city.__class__.__name__ + "." + new_city.__dict__["id"]
        key_user = new_user.__class__.__name__ + "." + new_user.__dict__["id"]
        key_review = new_review.__class__.__name__ + "." + new_review.__dict__["id"]

        key_place = new_place.__class__.__name__ + "." + new_place.__dict__["id"]

        key_state = new_state.__class__.__name__ + "." + new_state.__dict__["id"]

        key_amenity = new_amenity.__class__.__name__ + "." + new_amenity.__dict__["id"]

        self.assertIn(key, objects)
        self.assertIn(key_city, objects)
        self.assertIn(key_user, objects)
        self.assertIn(key_review, objects)
        self.assertIn(key_place, objects)
        self.assertIn(key_state, objects)
        self.assertIn(key_amenity, objects)

    def test_save(self):
        """ Testing save() """
        objects = models.storage

        new_base = BaseModel()
        new_user = User()
        new_state = State()
        new_place = Place()
        new_city = City()
        new_amenity = Amenity()
        new_review = Review()

        objects.new(new_base)
        objects.new(new_user)
        objects.new(new_state)
        objects.new(new_place)
        objects.new(new_city)
        objects.new(new_amenity)
        objects.new(new_review)
        objects.save()

        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + new_base.id, save_text)
            self.assertIn("User." + new_user.id, save_text)
            self.assertIn("State." + new_state.id, save_text)
            self.assertIn("Place." + new_place.id, save_text)
            self.assertIn("City." + new_city.id, save_text)
            self.assertIn("Amenity." + new_amenity.id, save_text)
            self.assertIn("Review." + new_review.id, save_text)

    def test_reload(self):
        """ Testing reload() """
        if not path.exists("file.json"):
            new_file = FileStorage()
            new_base = BaseModel(id="564778",
                                 created_at="2021-07-02T22:46:38.849900",
                                 updated_at="2021-07-02T22:46:38.849900")
            new_city = City()
            new_file.new(new_base)
            new_file.new(new_city)
            new_file.save()
        with open("file.json", "r") as f:
            objects = json.load(f)
        self.assertEqual(type(objects), dict)

        with self.assertRaises(TypeError):
            models.storage.reload(None)
