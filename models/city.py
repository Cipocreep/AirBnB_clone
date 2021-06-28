#!/usr/bin/python3
"""
Module for City Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ State City ineriting from BaseModel """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
