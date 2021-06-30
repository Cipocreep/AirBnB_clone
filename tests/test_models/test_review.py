#!/usr/bin/python3
"""
Unittests for the project
"""

import os
import unittest
import json
from models.base_model import BaseModel
from models.review import Review
import inspect
import time
from datetime import datetime
import models
from models import storage


class TestsForReview(unittest.TestCase):
    """ Tests for the Review Class """

    def test_parameters(self):
        """ Testing parameters of the Review class """
        review = Review()
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "id"))
        self.assertEqual(type(review.updated_at), datetime)
        self.assertEqual(type(review.created_at), datetime)
        self.assertEqual(type(review.id), str)
        self.assertFalse(hasattr(review, "brent"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(type(review.text), str)
