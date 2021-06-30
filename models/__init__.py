#!/bin/usr/python3
"""
Creates an unique FileStorage instance for our application
"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
           "State": State, "Place": Place, "Review": Review,
           "User": User}

storage = FileStorage()
storage.reload()
