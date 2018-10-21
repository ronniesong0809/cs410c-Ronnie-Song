"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.recipesentries = []

    def select(self):
        """
        Returns recipesentries list of lists
        Each list in recipesentries contains: name, email, date, message
        :return: List of lists
        """
        return self.recipesentries

    def insert(self, title, author, ingredient, time, skill, description):
        """
        Appends a new list of values representing new message into guestentries
        :param title: String
        :param author: String
        :param ingredient: String
        :param time: String
        :param skill: String
        :param description: String
        :return: True
        """
        params = [title, author, ingredient, time, skill, description]
        self.recipesentries.append(params)
        return True
