"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.recipeset = []

    def select(self):
        """
        Returns recipeset list of lists
        Each list in recipeset contains: title, author, ingredient, time, skill, description
        :return: List of lists
        """
        return self.recipeset

    def insert(self, title, author, ingredient, time, skill, description):
        """
        Appends a new list of values representing new message into recipeset
        :param title: String
        :param author: String
        :param ingredient: String
        :param time: String
        :param skill: String
        :param description: String
        :return: True
        """
        params = [title, author, ingredient, time, skill, description]
        self.recipeset.append(params)
        return True
