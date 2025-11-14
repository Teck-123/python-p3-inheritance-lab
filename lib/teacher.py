#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    """
    A teacher knows a few things and can teach one of them.
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Python is fun",
            "Inheritance is powerful",
            "Tests drive design"
        ]

    def teach(self):
        """Return a random item from self.knowledge."""
        import random
        return random.choice(self.knowledge)