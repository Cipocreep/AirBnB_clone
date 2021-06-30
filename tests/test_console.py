#!/usr/bin/python3
""" Unittests for the project """
import unittest
import os
from os import path
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.city import City


class TestForConsole(unittest.TestCase):
    """ Test for the Console """
    classes = ["User", "State", "Review", "Place", "City", "BaseModel"]

    def setUp(self):
        """ Setting up """
        if path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """ Delete test json file and put original file back """
        if path.isfile("file.json"):
            os.remove("file.json")
        if path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_basemodel(self):
        """ Testing BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())

    def test_user(self):
        """ Testing user """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())

    def test_state(self):
        """ Testing state """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())

    def test_city(self):
        """ Testing city """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())

    def test_amenity(self):
        """ Test amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())

    def test_place(self):
        """ Test place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Place " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())

    def test_review(self):
        """ Test review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Review " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())

    def test_create(self):
        """ Testing create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Ray")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

    def test_show(self):
        """ Testing show """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Brent")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + str(id))
            self.assertTrue(type(f), str)
            self.assertTrue("[BaseModel]" in f.getvalue().strip())
            self.assertTrue("created_at" in f.getvalue().strip())
            self.assertTrue("updated_at" in f.getvalue().strip())
            self.assertTrue("id" in f.getvalue().strip())

    def test_destroy(self):
        """ Testing destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Ray")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel " + str(id))
            self.assertEqual(f.getvalue().strip(), "")

    def test_all(self):
        """ testing all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            res = []
            for key, val in storage.all().items():
                res.append(str(val))
            self.assertEqual(eval(f.getvalue()), res)
        for className in TestForConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all {}".format(className))
                res = []
                for key, val in storage.all().items():
                    if val.__class__.__name__ == className:
                        res.append(str(val))
                self.assertEqual(eval(f.getvalue()), res)

    def test_new(self):
        '''Test new method'''
        new_file = FileStorage()
        new_base = BaseModel(id="123", created_at="2021-02-17T22:46:38.883036",
                             updated_at="2021-02-17T22:46:38.883036")
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
        objs = new_file.all()
        key = new_base.__class__.__name__ + "." + new_base.__dict__["id"]
        key_2 = new_city.__class__.__name__ + "." + new_city.__dict__["id"]
        key_user = new_user.__class__.__name__ + "." + new_user.__dict__["id"]
        key_review = new_review.__class__.__name__ + "." + new_review.__dict__["id"]
        key_place = new_place.__class__.__name__ + "." + new_place.__dict__["id"]
        key_state = new_state.__class__.__name__ + "." + new_state.__dict__["id"]
        key_amenity = new_amenity.__class__.__name__ + "." + new_amenity.__dict__["id"]
        self.assertIn(key, objs)
        self.assertIn(key_2, objs)
        self.assertIn(key_user, objs)
        self.assertIn(key_review, objs)
        self.assertIn(key_place, objs)
        self.assertIn(key_state, objs)
        self.assertIn(key_amenity, objs)


    def test_update(self):
        """ Testing update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Brent")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User Ray")
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id))
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id) + " name Ray")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Ray" in f.getvalue().strip())
