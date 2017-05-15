# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Person, FoodType
from .forms import RecommenderForm
import random
import json

def index(request):
    return render(request, 'recommender/index.html', {})

def results(request):
    food_type = FoodType(type=request.session['type'][0])
    food_type_array = []
    for item in request.session['type']:
        food_type_array.append(FoodType(type=item).get_type_display())
    content = {
        'food_type': food_type.get_type_display(),
        'food_type_array': food_type_array
    }
    return render(request, 'recommender/results.html', content)

def createPerson(request):
    if request.method == "POST":
        form = RecommenderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person = Person(primary_mood=data['primary_mood'], secondary_mood=data['secondary_mood'])
            food_type = getFoodType(person)
            request.session['type'] = food_type
            return HttpResponseRedirect('/recommender/results')
    else:
        form = RecommenderForm()
    return render(request, 'recommender/index.html', {'form': form})

def getFoodType(person):
    p_mood = person.primary_mood
    s_mood = person.secondary_mood
    if p_mood == 1 or p_mood == 2 or p_mood == 3:
        p_list = [1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 20, 22]
    elif p_mood == 4 or p_mood == 5 or p_mood == 6:
        p_list = [1, 4, 5, 6, 7, 8, 9, 11, 13, 16, 17, 18, 19, 21, 23]
    elif p_mood == 7 or p_mood == 8 or p_mood == 9:
        p_list = [2, 3, 4, 6, 10, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23]
    else:
        p_list = range(1, 24)

    if s_mood == 1 or s_mood == 2 or s_mood == 3:
        s_list = [1, 6, 9, 11, 17, 23]
    elif s_mood == 4 or s_mood == 5 or s_mood == 6:
        s_list = [2, 7, 13, 15, 16, 20]
    elif s_mood == 7 or s_mood == 8:
        s_list = [3, 4, 5, 8, 10, 14]
    elif s_mood == 9 or s_mood == 10:
        s_list = [12, 18, 19, 21, 22]

    food_type = getOverlapTypes(p_list, s_list)
    return food_type

def getOverlapTypes(a, b):
    overlap = list(set(a) & set(b))
    if not overlap:
        overlap.extend(a)
        overlap.extend(b)
    random.shuffle(overlap)
    return overlap

def newSuggestion(request):
    if request.method == 'POST':
        food_type_array = request.POST.getlist('food_type_array')
        if len(food_type_array) > 1:
            food_type_array.remove(request.POST['food_type'])
            food_type = FoodType(type=food_type_array[0])
        else:
            food_type = FoodType(type=random.randint(1,24))

        content = {
            'food_type': food_type.get_type_display(),
            'food_type_array': food_type_array
        }
        return render(request, 'recommender/newresults.html', content)
