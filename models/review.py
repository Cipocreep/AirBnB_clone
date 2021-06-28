#!/usr/bin/python3
"""
Module for Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class ineriting from BaseModel """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
