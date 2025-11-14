#!/usr/bin/env python

from user import User

class Student(User):
    """
    A student can learn new facts.
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []      

    def learn(self, fact: str):
        """Add a string to the student's knowledge list."""
        self.knowledge.append(fact)