# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.db.models import Count
from .models import Person, FoodType
from .forms import RecommenderForm
import random
import json

def index(request):
    return render(request, 'recommender/index.html', {})

def results(request):
    food_type = FoodType(type=request.session['type'][0])
    food_type_array = []
    rejected = []
    for item in request.session['type']:
        food_type_array.append(FoodType(type=item).type)
    content = {
        'person_id': request.session['id'],
        'food_type': food_type,
        'food_type_array': food_type_array,
        'rejected': rejected
    }
    return render(request, 'recommender/results.html', content)

def createPerson(request):
    if request.method == "POST":
        form = RecommenderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            food_type = getFoodType(data['primary_mood'])
            food_type_obj = FoodType.objects.get_or_create(type=food_type[0])[0]
            food_type_obj.save()
            person = Person(primary_mood=data['primary_mood'], food_type=food_type_obj)
            # Save person to database
            person.save()
            request.session['type'] = food_type
            request.session['id'] = person.id
            return HttpResponseRedirect('/recommender/results')
    else:
        form = RecommenderForm()
    return render(request, 'recommender/index.html', {'form': form})

def getFoodType(mood):
    print 'mood'
    print mood
    food_type = []
    filtered_by_mood = Person.objects.filter(primary_mood=mood)
    # No data exists for this mood yet; use naive recommendation
    if (filtered_by_mood.count() == 0):
        if mood == 1:
            food_type = [3, 5, 7, 22]
        elif mood == 2:
            food_type = [2, 6, 11, 23]
        elif mood == 3:
            food_type = [1, 21, 22, 24]
        elif mood == 4:
            food_type = [2, 8, 12, 14]
        elif mood == 5:
            food_type = [7, 17, 18, 23]
        elif mood == 6:
            food_type = [1, 15, 19, 20]
        elif mood == 7:
            food_type = [3, 9, 10, 11]
        elif mood == 8:
            food_type = [5, 9, 10, 15]
        elif mood == 9:
            food_type = [13, 16, 20, 24]
        elif mood == 10:
            food_type = [4, 17, 18, 19]
        elif mood == 11:
            food_type = [4, 6, 12, 21]
        elif mood == 12:
            food_type = [8, 13, 14, 16]
        random.shuffle(food_type)
    else:
        # Group by food_type, order from most popular to least
        grouped_food_type = filtered_by_mood.values('food_type__type').annotate(count=Count('food_type__type')).order_by('-count')
        print grouped_food_type
        for item in grouped_food_type:
            food_type.append(item.get('food_type__type'))
        print food_type
    return food_type

def newSuggestion(request):
    if request.method == 'POST':
        type = int(request.POST['food_type'])
        food_type = FoodType(type=type)
        food_type_array = request.POST.getlist('food_type_array')
        print food_type_array
        rejected = request.POST.getlist('rejected')
        if len(food_type_array) > 1:
            food_type_array.remove(str(food_type.type))
            rejected.append(str(food_type.type))
            food_type = FoodType(type=int(food_type_array[0]))
        else:
            rejected.append(str(food_type.type))
            print rejected
            if len(rejected) == 24:
                rejected = []
                food_type = FoodType(type=random.randint(1,24))
            else:
                food_type = FoodType(type=random.randint(1,24))
                while str(food_type.type) in rejected:
                    food_type = FoodType(type=random.randint(1,24))

        print food_type.type
        print food_type.get_type_display()
        content = {
            'person_id': request.POST['person_id'],
            'food_type': food_type,
            'food_type_array': food_type_array,
            'rejected': rejected
        }
        return render(request, 'recommender/newresults.html', content)
