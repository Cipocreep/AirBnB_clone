#!/usr/bin/python3
"""
Unittests for the project
"""

import os
import unittest
import json
from models.base_model import BaseModel
import inspect
import time
from datetime import datetime
import models
from models import storage


class TestsForBase(unittest.TestCase):
    """ Tests for the Base Class """

    def test_save(self):
        """ Testing save() """
        instance = BaseModel()
        time_created = instance.updated_at
        instance.save()
        time_updated = instance.updated_at
        self.assertNotEqual(time_updated, time_created)
        self.assertGreater(time_updated, time_created)

    def test_save_storage(self):
        """ Testing the save method """
        m1 = BaseModel()
        m1.save()
        with open("file.json", mode="r", encoding="UTF-8") as f:
            d = json.load(f)
        for item in d:
            if m1.id in item:
                d = d[item]
        self.assertDictEqual(d, m1.to_dict())

    def test_to_dict(self):
        """ Testing to_dict """
        instance = BaseModel()
        dict_instance = instance.to_dict()
        self.assertNotEqual(instance.__dict__, instance.to_dict())
        self.assertEqual(type(dict_instance["created_at"]), str)
        self.assertEqual(type(dict_instance["updated_at"]), str)
        self.assertTrue("__class__" in dict_instance)
        self.assertEqual(dict_instance["__class__"], "BaseModel")

    def test_self_id(self):
        """ Testing id of BaseClass class """
        instance = BaseModel()
        instance2 = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertNotEqual(instance, instance2)
        self.assertNotEqual(instance.id, instance2.id)
        self.assertEqual(type(instance.id), str)

    def test_str(self):
        """ Testing method str """
        instance = BaseModel()
        self.assertEqual(instance.__str__(), "[{}] ({}) {}".format
                         (instance.__class__.__name__,
                         instance.id, instance.__dict__))
        self.assertTrue(type(instance.__str__()), str)
        self.assertTrue(len(instance.__str__()))
