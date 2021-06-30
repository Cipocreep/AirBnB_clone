#!/usr/bin/python3
"""
Unittests for the project
"""

import os
import unittest
import json
from models.base_model import BaseModel
from models.city import City
import inspect
import time
from datetime import datetime
import models
from models import storage


class TestsForCity(unittest.TestCase):
    """ Tests for the City Class """

    def test_parameters(self):
        """ Testing parameters of the City class """
        city = City()
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(type(city.updated_at), datetime)
        self.assertEqual(type(city.created_at), datetime)
        self.assertEqual(type(city.id), str)
        self.assertFalse(hasattr(city, "brent"))
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(type(city.name), str)
