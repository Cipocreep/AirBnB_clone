#!/usr/bin/python3
"""
Module for Amenity Class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Class ineriting from BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
