#!/usr/bin/python3
"""
Module for State Class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State Class ineriting from BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
