#!/usr/bin/python3
"""
    TestConsole module
"""
import unittest
import sys
from io import StringIO
import re
from unittest.mock import patch
from console import HBNBCommand
import random
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.city import City
from models import storage



class TestConsoleFunction(unittest.TestCase):
    classes = ["User", "State", "Review", "Place", "City", "BaseModel"]
    actual_obj = None
    actual_id = ""
    actual_class = ""

    def test_create_new_obj(self):
        if len(storage.all()) != 6:
            for class_name in self.classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd("create {}".format(class_name))
                    instance_after = len(storage.all())
                    self.actual_class = class_name
                    self.actual_id = f.getvalue()[:-1]
                    key_id = class_name + "." + self.actual_id
                    self.actual_obj = storage.all()[key_id]
                    self.assertNotEqual(self.actual_obj, None)
                    self.assertIn(self.actual_class, self.classes)

    def test_count_obj(self):
        """
            <class name>.count()
        """
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.count()".format(class_name))
                count = 0
                for key, obj in storage.all().items():
                    if type(obj) is eval(class_name):
                        count += 1
                self.assertEqual(eval(f.getvalue()[:-1]), count)

    @staticmethod
    def get_first_occurence_by_class_name(class_name):
        """
            :return first occurence found
        """

        for key, val in storage.all().items():
            if type(val) is eval(class_name):
                return val

    @staticmethod
    def get_all_obj_by_classname(class_name):
        """
        :return all object found in storage
        """
        res = []
        for key, val in storage.all().items():
            if type(val) is eval(class_name):
                res.append(str(val))
        return res

    def test_all_obj(self):
        """
            <class name>.all()
        """
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                all_class_name = self.get_all_obj_by_classname(class_name)
                HBNBCommand().onecmd("{}.all()".format(class_name))
                self.assertEqual(all_class_name, eval(f.getvalue()))
