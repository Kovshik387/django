from django.db import models

class SurveyResponse(models.Model):
    name = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    preferred_cuisine = models.CharField(max_length=100)
