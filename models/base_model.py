#!/usr/bin/python3
"""
Base Module for AirBnB Project
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Base Class for  AirBnb Project """

    def __init__(self, *args, **kwargs):
      if len(kwargs) == 0:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)
        models.storage.save()
      else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)

    def __str__(self):
        """ Print a formated reresentation of our Base Class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing __dict__"""
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dic
