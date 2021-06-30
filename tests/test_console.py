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
from os import system


class TestConsole(unittest.TestCase):
    """ Class for our console tests """

    def setUp(self):
        """  Setting up for our tests """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def session(self):
        """
        creates a console instance
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_basemodel(self):
        """ Testing BaseModel """
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

    def test_user2(self):
        """ Testing user """
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

    def test_state2(self):
        """ Testing state """
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

    def test_city2(self):
        """ Testing city """
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

    def test_amenity2(self):
        """ Testing amenity """
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

    def test_place2(self):
        """ Testing place """
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

    def test_review2(self):
        """ Testing review """
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

    def test_create2(self):
        """ Testing create """
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

    def test_show2(self):
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

    def test_destroy2(self):
        """ Testing destroy """
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

    def test_all2(self):
        """ Testing all """
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

    def test_update2(self):
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

    def test_newline_space2(self):
        """ Testing newline and spaces input """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(" ")
            self.assertEqual(f.getvalue().strip(), "")

    def testEOF(self):
        """ Testing EOF """
        my_console = self.session()
        assert HBNBCommand().onecmd("EOF")

    def test_all(self):
        """ Testing all """
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

    def test_create(self):
        """ Testing create """
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create asgshsd"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("create {}".format(cls))
                self.assertTrue(len(str(out.getvalue())) == 37)

    def testDestroy(self):
        """ testing destroy """
        my_console = self.session()
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy Jared"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy BaseModel"))
            self.assertEqual(out.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy BaseModel 555-ddd"))
            self.assertEqual(out.getvalue(), "** no instance found **\n")
        for cls in classes.keys():
            obj = classes[cls]()
            key = ".".join([cls, obj.id])
            storage.all()[key] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("destroy {} {}".format(cls, obj.id))
                self.assertEqual(out.getvalue(), '')
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(cls, obj.id))
                self.assertEqual("** no instance found **\n", out.getvalue())
        for cls in classes.keys():
            obj = classes[cls]()
            key = ".".join([cls, obj.id])
            storage.all()[key] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd('{}.destroy("{}")'.format(cls, obj.id))
                self.assertEqual(out.getvalue(), '')
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(cls, obj.id))
                self.assertEqual("** no instance found **\n", out.getvalue())



    def testCount(self):
        """ Test count """
        for k in classes.keys():
            count = 0
            for c in storage.all():
                if k in c:
                    count += 1
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("{}.count()".format(k))
                self.assertEqual(int(out.getvalue().strip()), count)

    @staticmethod
    def get_all_obj_by_classname(class_name):
        """ Statiuc method """
        res = []
        for key, val in storage.all().items():
            if type(val) is eval(class_name):
                res.append(str(val))
        return res

    def test_all(self):
        """ testing all """
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                all_class_name = self.get_all_obj_by_classname(class_name)
                HBNBCommand().onecmd("{}.all()".format(class_name))
                self.assertEqual(all_class_name, eval(f.getvalue()))

    def testShow(self):
        """ testing show """
        for k in classes.keys():
            obj = classes[k]()
            storage.all()[".".join([k, obj.id])] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(k, obj.id))
                self.assertEqual(str(obj) + '\n', out.getvalue())
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd('{}.show("{}")'.format(k, obj.id))
                self.assertEqual(str(obj) + '\n', out.getvalue())

    def test_update_BaseModel(self):
        """ Test BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(\"" + str(id) + "\", \"name\", \"John\")")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("John" in f.getvalue().strip())

    def test_update_User(self):
        """ Test User Update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(\"" + str(id) + "\", \"first_name\", \"John\")")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + str(id))
            self.assertTrue("first_name" in f.getvalue().strip())
            self.assertTrue("John" in f.getvalue().strip())

    def test_update_State(self):
        """ Test State Update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.update(\"" + str(id) + "\", \"name\", \"John\")")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("John" in f.getvalue().strip())

    def test_update_City(self):
        """ Test State Update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.update(\"" + str(id) + "\", \"name\", \"John\")")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("John" in f.getvalue().strip())

    def test_update_Amenity(self):
        """ Test Anemity Update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.update(\"" + str(id) + "\", \"name\", \"John\")")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("John" in f.getvalue().strip())

    def test_update_Place(self):
        """ Test Place Update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.update(\"" + str(id) + "\", \"name\", \"John\")")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place " + str(id))
            self.assertTrue("name" in f.getvalue().strip())
            self.assertTrue("John" in f.getvalue().strip())

    def test_update_Review(self):
        """ Test Review Update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            self.assertTrue(type(f), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.update(\"" + str(id) + "\", \"text\", \"John\")")
            self.assertTrue(type(f), str)
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review " + str(id))
            self.assertTrue("text" in f.getvalue().strip())
            self.assertTrue("John" in f.getvalue().strip())

    def test_help_console_cmd(self):
        """ testing help command """
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
\n"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, f.getvalue())

    def test_quit(self):
        """ testing quit """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")
