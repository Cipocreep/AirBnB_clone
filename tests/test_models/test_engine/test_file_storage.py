#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import json
import os
import shutil
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestForFileStorage(unittest.TestCase):
    """ Test class for FileStorage """

    @classmethod
    def SetUp(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def teardown(cls):
        del cls.rev1

    def teardown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """ Testing .all()"""
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        """ Testing new """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        melissa = User()
        melissa.id = 999999
        melissa.name = "Melissa"
        m_storage.new(melissa)
        key = melissa.__class__.__name__ + "." + str(melissa.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload_empty(self):
        """ testing reload when empty"""
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_reload(self):
        """ testing reload"""
        self.maxDiff = None
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        shutil.copy("./tests/test_models/test_engine/dump.txt", "./file.json")
        with open("./file.json") as f:
            dicts = json.load(f)
        a_storage.reload()
        objs = a_storage.all()
        for key in dicts:
            self.assertEqual(objs[key].to_dict(), dicts[key])

    def test_save(self):
        """ testing save """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")
        self.brba = FileStorage()
        self.my_model = BaseModel()
        storage.reload()
        self.brba.new(BaseModel())
        self.brba.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue("BaseModel" in str(self.brba.all()))
