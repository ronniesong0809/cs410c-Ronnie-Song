"""
route method of flask with '/add' as the page to list all recipes
"""
from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()

        """dictionary of list. The blow was comment out because im using a dictionary of dictionary"""
        """
        recipes = [dict(title=row[0], 
                        author=row[1], 
                        ingredient=row[2],
                        time=row[3], 
                        skill=row[4], 
                        description=row[5]) for row in model.select()]
        """
        """dictionary of dictionary"""
        recipes = model.select()
        return render_template('index.html', rps=recipes)
