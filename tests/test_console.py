#!/usr/bin/python3
"""
Unit testing for console.py
"""
from console import HBNBCommand
import sys
from io import StringIO
import console
import unittest
from models import classes
from unittest.mock import patch, create_autospec
import os
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    test console code with unit testing
    """

    def setUp(self):
        """ Move json file if it exists """
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """ Delete test json file and put original file back """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_basemodel(self):
        """ Test BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_user(self):
        """ Test user """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_state(self):
        """ Test user """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_city(self):
        """ Test city """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_amenity(self):
        """ Test amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_place(self):
        """ Test place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Place " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_review(self):
        """ Test review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Review " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_create(self):
        """ Test create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Banu")
            self.assertEqual(f.getvalue().strip(),
                             "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)
            self.assertEqual(len(id), 36)

    def test_show(self):
        """ Test show """
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

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(" + str(id) + ")")
            self.assertEqual(f.getvalue().strip(), "")
            self.assertTrue(type(f), str)
            self.assertTrue("[BaseModel]" in f.getvalue().strip())
            self.assertTrue("created_at" in f.getvalue().strip())
            self.assertTrue("updated_at" in f.getvalue().strip())
            self.assertTrue("id" in f.getvalue().strip())
        """

    def test_destroy(self):
        """ Test destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Banu")
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
        """ Test all """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertTrue("[User]" in f.getvalue().strip())
            self.assertTrue("[State]" in f.getvalue().strip())
            self.assertTrue("[City]" in f.getvalue().strip())
            self.assertTrue("[Amenity]" in f.getvalue().strip())
            self.assertTrue("[Place]" in f.getvalue().strip())
            self.assertTrue("[Review]" in f.getvalue().strip())
            self.assertTrue("created_at" in f.getvalue().strip())
            self.assertTrue("updated_at" in f.getvalue().strip())
            self.assertTrue("id" in f.getvalue().strip())

    def test_update(self):
        """ Test update """
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
            HBNBCommand().onecmd("update User Banu")
            self.assertEqual(f.getvalue().strip(),
                             "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id))
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + str(id) + " name Banu")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("Banu" in f.getvalue().strip())

    def test_newline_spaces(self):
        """ Test newline and spaces input """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" ")
            self.assertEqual(f.getvalue().strip(), "")


if __name__ == '__main__':
    unittest.main()
