#!/usr/bin/python3
"""
    Module for storing files
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import json


class FileStorage:
    """ Class for storing files """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        new = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[new] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        json_o = {}
        for key, value in self.__objects.items():
            json_o[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_o, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as file:
                read = file.read()
                dict_file = {}
                if read != "":
                    dict_file = json.loads(read)

                for key, value in dict_file.items():
                    if key not in FileStorage.__objects.keys():
                        class_name = value["__class__"]
                        new = eval("{}(**value)".format(class_name))
                        self.new(new)
        except FileNotFoundError:
            return

    @classmethod
    def get_object(cls, id=''):
        '''Returns an object based on id
        Return:
        returns an object that matches id or prints an error on failure
        '''
        objects = cls.__objects
        for obj in objects.values():
            if obj.id == id:
                return obj
        print("id could not be matched")
