#!/usr/bin/python3
"""
Module for User Class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User Class inheriting from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
