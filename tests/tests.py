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
