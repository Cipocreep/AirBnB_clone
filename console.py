#!/usr/bin/python3
"""
Module containing the console for our AirBnb Clone
"""
import cmd
import models
import inspect
import ast
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


storage = models.storage


class HBNBCommand(cmd.Cmd):
    """ Class for our AirBnb console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quits the program when quit is called """
        raise SystemExit

    def do_EOF(self, arg):
        """ Quits the program when EOF is called """
        return True

    def emptyline(self):
        """ Does nothing """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            try:
                new = eval(args[0] + "()")
                new.save()
                print(new.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation instance based on class name """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + "." + args[1]
                print(storage.all()[key])
            except Exception:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + "." + args[1]
                del storage.all()[key]
                storage.save()
            except Exception:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """ Prints all string representation instances based on class name """
        args = arg.split()
        list_inst = []
        if len(args) == 0:
            list_inst = [str(value) for key, value in storage.all().items()]
            if len(list_inst) != 0:
                print(list_inst)
                return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if str(key.split(".")[0]) == args[0]:
                list_inst.append(str(value))
        if len(list_inst) != 0:
            print(list_inst)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = arg.split()
        list_inst = []
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        try:
            storage.all()[key]
        except Exception:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            try:
                if '.' in args[3]:
                    value = float(args[3])
                else:
                    value = int(args[3])
            except ValueError:
                value = str(args[3]).strip("\"':")
                value = str(value)
            setattr(storage.all()[key], args[2].strip("\"':"), value)
            storage.save()

    def count(self, arg):
        """ Returns the total quantity of instances of the Class"""
        count = 0
        args = arg.split()
        if eval(args[0]):
            for key in storage.all():
                if arg in key:
                    count += 1
            print(count)

    def dict_update(self, arg, class_name):
        """ Updates for dicts """
        args = arg.split(",", 1)
        obj = storage.get_object(args[0].strip("'\""))
        dicti = ast.literal_eval(args[1].strip())
        if obj is None or obj.__class__.__name__ != class_name:
            print("** no instance found **")
            return
        for attr in dicti:
            setattr(obj, attr, dicti[attr])

    def default(self, arg):
        """ Attempts to parse unfound command """
        funcs = {"all": HBNBCommand.do_all, "count": HBNBCommand.count}
        other_funcs = {"show": HBNBCommand.do_show,
                       "destroy": HBNBCommand.do_destroy}
        args = arg.split(".")
        func_name = ""
        func_id = ""
        if len(args) > 1:
            for index, char in enumerate(args[1]):
                if char == "(":
                    func_name = args[1][0:index]
                    break

        if func_name in funcs:
            funcs[func_name](self, args[0])
        elif func_name in other_funcs:
            arg = args[0] + " " + args[1][index + 2:-2]
            other_funcs[func_name](self, arg)
        elif func_name == "update":
            method_name = args[1].split("(")
            method_name[1] = method_name[1].strip()
            method_splitted = method_name[1][:-1]
            argsplit = method_splitted.split(",", 1)
            if argsplit[1].strip()[0] == "{":
                return self.dict_update(method_splitted, args[0])
            else:
                method_splitted = method_splitted.split(",")
                stripped_string = " ".join([args[0]] +
                                           method_splitted).replace('"', "")
                return self.do_update(stripped_string)
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
