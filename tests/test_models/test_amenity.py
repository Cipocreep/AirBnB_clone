#!/usr/bin/python3
"""
Unittests for the project
"""

import os
import unittest
import json
from models.base_model import BaseModel
from models.amenity import Amenity
import inspect
import time
from datetime import datetime
import models
from models import storage


class TestsForAmenity(unittest.TestCase):
    """ Tests for the Amenity Class """

    def test_parameters(self):
        """ Testing parameters of the Amenity class """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(type(amenity.updated_at), datetime)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertEqual(type(amenity.id), str)
        self.assertEqual(type(amenity.name), str)
        self.assertFalse(hasattr(amenity, "brent"))
