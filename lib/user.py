#!/usr/bin/env python

class User:
    """
    Base class – every person has a first and last name.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name