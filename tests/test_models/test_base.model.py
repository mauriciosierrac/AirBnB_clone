#!/usr/bin/python3
"""
Define unittests for console scrit and HBNBCommand class (console.py)
"""
import unittest
from io import StringIO
from unittest.mock import patch
import os

# Import console
from console import HBNBCommand

# Import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Import storage
from models.engine.file_storage import FileStorage
from models import storage


class TestConsole_config(unittest.TestCase):
    """Test console's configurations"""

    def test_promt(self):
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_empty_line(self):
        exp = ""
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("\n")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_default_unexisting_command(self):
        exp = "*** Unknown syntax: unexisting-command\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("unexisting-command")
            real = output.getvalue()
            self.assertEqual(exp, real)


class TestConsole_exit(unittest.TestCase):
    """Test quit and EOF methods of HBNBCommand class"""

    def test_help_quit(self):
        exp = "Quit command to exit the program\n        \n"
        with patch('sys.stdout', new = StringIO()) as output: 
            HBNBCommand().onecmd("help quit")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_quit(self):
        exp = ""
        with patch('sys.stdout', new = StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_help_EOF(self):
        exp = "Exit with 'EOF' signal.\n        \n"
        with patch('sys.stdout', new = StringIO()) as output: 
            HBNBCommand().onecmd("help EOF")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_EOF(self):
        exp = "\n"
        with patch('sys.stdout', new = StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            real = output.getvalue()
            self.assertEqual(exp, real)


class TestConsole_create(unittest.TestCase):
    """Test create method of HBNBCommand class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "original")
        except:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass
        try:
            os.rename("original", "file.json")
        except:
            pass

    def test_create_missing_class(self):
        exp = "** class name missing **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("create")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_create_unexisting_class(self):
        exp = "** class doesn't exist **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("create MyClass")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_create(self):
        k_cls = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
        ]

        for c_name in k_cls:
            command = "create " + c_name
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                obj_key = c_name + "." + output.getvalue().strip()
                self.assertIn(obj_key, storage.all().keys())


class TestConsole_show(unittest.TestCase):
    """Test show method of HBNBCommand class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "original")
        except:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass
        try:
            os.rename("original", "file.json")
        except:
            pass

    def test_show_missing_class(self):
        exp = "** class name missing **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("show")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_show_unexisting_class(self):
        exp = "** class doesn't exist **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("show MyClass")
            real = output.getvalue()
            self.assertEqual(exp, real)

        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("MyClass.show(1)")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_show_missing_instance(self):
        exp = "** instance id missing **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            real = output.getvalue()
            self.assertEqual(exp, real)

        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.show()")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_show_unexisting_instance(self):
        exp = "** no instance found **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel unexisting_id")
            real = output.getvalue()
            self.assertEqual(exp, real)

        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.show(unexisting_id)")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_show(self):
        k_cls = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
        ]

        for c_name in k_cls:

            # Create object
            c_create = "create " + c_name
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(c_create)
                obj_id = output.getvalue().strip()

            # Test space notation
            with patch("sys.stdout", new=StringIO()) as output:
                command = "show {} {}".format(c_name, obj_id)
                HBNBCommand().onecmd(command)
                real = output.getvalue().strip()

                obj_key = c_name + "." + obj_id
                obj = storage.all()[obj_key]
                exp = str(obj)

                self.assertEqual(exp, real)

            # Test dot notation
            with patch("sys.stdout", new=StringIO()) as output:
                command = "{}.show({})".format(c_name, obj_id)
                HBNBCommand().onecmd(command)
                real = output.getvalue().strip()

                obj_key = c_name + "." + obj_id
                obj = storage.all()[obj_key]
                exp = str(obj)

                self.assertEqual(exp, real)

class TestConsole_destroy(unittest.TestCase):
    """Test destroy method of HBNBCommand class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "original")
        except:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass
        try:
            os.rename("original", "file.json")
        except:
            pass

    def test_destroy_missing_class(self):
        exp = "** class name missing **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_destroy_unexisting_class(self):
        exp = "** class doesn't exist **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("destroy MyClass")
            real = output.getvalue()
            self.assertEqual(exp, real)

        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("MyClass.destroy(1)")
            real = output.getvalue()
            self.assertEqual(exp, real)


    def test_destroy_missing_instance(self):
        exp = "** instance id missing **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
            real = output.getvalue()
            self.assertEqual(exp, real)

        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.destroy()")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_destroy_unexisting_instance(self):
        exp = "** no instance found **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel unexisting_id")
            real = output.getvalue()
            self.assertEqual(exp, real)

        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.destroy(unexisting_id)")
            real = output.getvalue()
            self.assertEqual(exp, real)


    def test_destroy(self):
        k_cls = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
        ]

        for c_name in k_cls:

            # Create objects
            c_create = "create " + c_name
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(c_create)
                obj_id_1 = output.getvalue().strip()
                obj_key_1 = c_name + "." + obj_id_1
                HBNBCommand().onecmd(c_create)
                obj_id_2 = output.getvalue().strip()
                obj_key_2 = c_name + "." + obj_id_2

            keys = storage.all().keys()

            # Test space notation
            with patch("sys.stdout", new=StringIO()) as output:
                command = "destroy {} {}".format(c_name, obj_id_1)
                HBNBCommand().onecmd(command)

                self.assertNotIn(obj_key_1, keys)

            # Test dot notation
            with patch("sys.stdout", new=StringIO()) as output:
                command = "{}.destroy({})".format(c_name, obj_id_2)
                HBNBCommand().onecmd(command)

                self.assertNotIn(obj_key_2, keys)


class TestConsole_all(unittest.TestCase):
    """Test all method of HBNBCommand class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "original")
        except:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass
        try:
            os.rename("original", "file.json")
        except:
            pass

    def test_all_unexisting_class(self):
        exp = "** class doesn't exist **\n"
        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("all MyClass")
            real = output.getvalue()
            self.assertEqual(exp, real)

        with patch('sys.stdout', new = StringIO()) as output:
            HBNBCommand().onecmd("MyClass.all()")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_all(self):
        k_cls = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
        ]

        l_obj_id = []
        for c_name in k_cls:

            # Create object
            c_create = "create " + c_name
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(c_create)
                obj_id = "(" + output.getvalue().strip() + ")"
                l_obj_id.append(obj_id)

        with patch("sys.stdout", new=StringIO()) as output:
            command = "all"
            HBNBCommand().onecmd(command)
            text_all = output.getvalue().strip()

        for obj_id in l_obj_id:
            self.assertIn(obj_id, text_all)

    def test_all_class(self):
        k_cls = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
        ]

        l_obj_id = []
        for c_name in k_cls:

            # Create object
            c_create = "create " + c_name
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(c_create)

            with patch("sys.stdout", new=StringIO()) as output:
                command = "all {}".format(c_name)
                HBNBCommand().onecmd(command)
                text_all_1 = output.getvalue().strip()

            with patch("sys.stdout", new=StringIO()) as output:
                command = "{}.all()".format(c_name)
                HBNBCommand().onecmd(command)
                text_all_2 = output.getvalue().strip()

            self.assertIn(c_name, text_all_1)
            self.assertIn(c_name, text_all_2)

            ignore_classes = k_cls.copy()
            ignore_classes.remove(c_name)
            for ic in ignore_classes:
                self.assertNotIn(ic, text_all_1)
                self.assertNotIn(ic, text_all_2)