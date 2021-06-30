#!/usr/bin/python3
"""
Unittests for the project
"""

import os
import unittest
import json
from models.base_model import BaseModel
from models.place import Place
import inspect
import time
from datetime import datetime
import models
from models import storage


class TestsForPlace(unittest.TestCase):
    """ Tests for the Place Class """

    def test_parameters(self):
        """ Testing parameters of the Place class """
        place = Place()
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(type(place.updated_at), datetime)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.name), str)
        self.assertFalse(hasattr(place, "brent"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(type(place.city_id), str)
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(type(place.user_id), str)
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(type(place.description), str)
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
