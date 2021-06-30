#!/usr/bin/python3
'''
Defines the FileStorage class
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''Class that stores objects in JSON strings
    Attributes:
    file_path (str): path to the JSON file
    objects (dict): stores all objects by class
    '''

    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review}

    def all(self):
        '''Returns the dictionary __objects
        Return:
            returns __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets new object in __objects dictionary
        '''
        k = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        '''Serializes __objects to the JSON file
        '''
        save_dict = {}
        for k, v in FileStorage.__objects.items():
            v_dict = v.to_dict()
            save_dict[k] = v_dict
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(save_dict, f)

    def reload(self):
        '''Deserialize the JSON file to __objects
        '''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dicts = json.load(f)
                FileStorage.__objects = {}
                for k, v in dicts.items():
                    obj = FileStorage.class_dict[v['__class__']](**v)
                    FileStorage.__objects[k] = obj
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
