"""
route method of flask with '/add' as the page to list all recipes
"""
from flask import render_template
from flask.views import MethodView
import requests
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        
        """dictionary of list and sqlite."""
        lang1='zh'
        lang2='ru'
        lang3='ja'

        recipes = [dict(title=row[0],
                        author=row[1], 
                        ingredient=row[2],
                        time=row[3], 
                        skill=row[4], 
                        description=row[5],
                        url=row[6],
                        url_description=self.detect_labels_uri(row[6]),
                        t_title=self.translate(row[0],lang1),
                        t_author=self.translate(row[1],lang1),
                        t_ingredient=self.translate(row[2],lang1),
                        t_time=self.translate(row[3],lang1),
                        t_skill=self.translate(row[4],lang1),
                        t_description=self.translate(row[5],lang1),
                        t2_title=self.translate(row[0],lang2),
                        t2_author=self.translate(row[1],lang2),
                        t2_ingredient=self.translate(row[2],lang2),
                        t2_time=self.translate(row[3],lang2),
                        t2_skill=self.translate(row[4],lang2),
                        t2_description=self.translate(row[5],lang2),
                        t3_title=self.translate(row[0],lang3),
                        t3_author=self.translate(row[1],lang3),
                        t3_ingredient=self.translate(row[2],lang3),
                        t3_time=self.translate(row[3],lang3),
                        t3_skill=self.translate(row[4],lang3),
                        t3_description=self.translate(row[5],lang3),
                        nutrition = self.nutritionix(row[2]),
                        yelp = self.yelpSearch(row[0])) for row in model.select()]

        return render_template('index.html', rps=recipes)

    def translate(self,text,target):

        from google.cloud import translate
        translate_client = translate.Client()
        
        result = translate_client.translate(text,target_language=target)

        return result['translatedText']

    def detect_labels_uri(self,uri):

        from google.cloud import vision
        client = vision.ImageAnnotatorClient()

        image = vision.types.Image()
        image.source.image_uri = uri

        response = client.label_detection(image=image)
        labels = response.label_annotations

        label_descriptions=[]
        for label in labels:
            label_descriptions.append(label.description)

        return label_descriptions

    def nutritionix(self, ingredient):
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        headers = {"Content-Type":"application/json", "x-app-id":"8a719e54", "x-app-key":"d530d0e7c2e68deffe4b5c625100ea99"}
        body = {"query":ingredient,"timezone": "US/Eastern"}
        response = requests.post(url, headers= headers, json = body)
        return response.json()

    def yelpSearch(self, title):
        url = 'https://api.yelp.com/v3/businesses/search?term=' + title + '&location=portland&limit=3'
        headers={'Authorization': "Bearer T7zsAtPs89Md-UJVSSUpzGGPxljUmlU914d994tSlhL5v98RnTEmDvPEfHgwwNp5FooWOpWp45ciFSX2ON8HnDFRbojwEBMbyW1SslpL9VcL3o2gAwvLTXFBW-7rW3Yx"}
        response = requests.get(url, headers=headers)
        return response.json()