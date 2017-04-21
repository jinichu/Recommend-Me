# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    P_MOODS = (
        (1, 'Happy'),
        (2, 'Excited'),
        (3, 'Content'),
        (4, 'Angry'),
        (5, 'Worried'),
        (6, 'Frustrated'),
        (7, 'Bored'),
        (8, 'Lonely'),
        (9, 'Sad'),
        (10, 'Indifferent'),
    )
    S_MOODS = (
        (1, 'Energetic'),
        (2, 'Motivated'),
        (3, 'Refreshed'),
        (4, 'Neutral'),
        (5, 'Relaxed'),
        (6, 'Lazy'),
        (7, 'Tired'),
        (8, 'Exhausted'),
        (9, 'Stressed'),
        (10, 'Anxious'),
    )
    primary_mood = models.IntegerField(choices=P_MOODS, default=1)
    secondary_mood = models.IntegerField(choices=S_MOODS, default=1)

class FoodType(models.Model):
    TYPES = (
        (1, 'Chinese'),
        (2, 'Taiwanese'),
        (3, 'Malaysian'),
        (4, 'Japanese'),
        (5, 'Sushi'),
        (6, 'Ramen'),
        (7, 'Korean'),
        (8, 'Vietnamese'),
        (9, 'Indian'),
        (10, 'Thai'),
        (11, 'Mexican'),
        (12, 'Italian'),
        (13, 'French'),
        (14, 'Greek'),
        (15, 'Mediterranean'),
        (16, 'Cafe'),
        (17, 'Diner'),
        (18, 'Burgers'),
        (19, 'Pizza'),
        (20, 'Seafood'),
        (21, 'Steakhouse'),
        (22, 'Pubs'),
        (23, 'Cocktail Bars'),
    )
    type = models.IntegerField(choices=TYPES, default=1)

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
