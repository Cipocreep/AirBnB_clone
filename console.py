#!/usr/bin/python3
"""
Module containing the console for our AirBnb Clone
"""
import cmd
import models
import inspect
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
        return True

    def do_EOF(self, arg):
        """ Quits the program when EOF is called """
        return True

    def emptyline(self):
        """ Does nohting """
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
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                if len(arg) == 2:
                    print("** attribute name missing **")
                    return
                elif len(arg) == 3:
                    print("** value missing **")
                    return
                else:
                    storage.all()[key].__dict__[args[2]] = args[3]
                    storage.all()[key].save
            else:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
