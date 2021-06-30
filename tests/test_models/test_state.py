#!/usr/bin/python3
"""
Unittests for the project
"""

import os
import unittest
import json
from models.base_model import BaseModel
from models.state import State
import inspect
import time
from datetime import datetime
import models
from models import storage


class TestsForState(unittest.TestCase):
    """ Tests for the State Class """

    def test_parameters(self):
        """ Testing parameters of the State class """
        state = State()
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(type(state.updated_at), datetime)
        self.assertEqual(type(state.created_at), datetime)
        self.assertEqual(type(state.id), str)
        self.assertFalse(hasattr(state, "brent"))
        self.assertEqual(type(state.name), str)
