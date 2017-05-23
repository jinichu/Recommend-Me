# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Chinese'), (2, 'Taiwanese'), (3, 'Malaysian'), (4, 'Japanese'), (5, 'Sushi'), (6, 'Ramen'), (7, 'Korean'), (8, 'Vietnamese'), (9, 'Indian'), (10, 'Thai'), (11, 'Mexican'), (12, 'Italian'), (13, 'French'), (14, 'Greek'), (15, 'Mediterranean'), (16, 'American'), (17, 'Cafe'), (18, 'Diner'), (19, 'Burgers'), (20, 'Pizza'), (21, 'Seafood'), (22, 'Steakhouse'), (23, 'Pubs'), (24, 'Cocktail Bars')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_mood', models.IntegerField(choices=[(1, 'Happy'), (2, 'Excited'), (3, 'Angry'), (4, 'Frustrated'), (5, 'Worried'), (6, 'Stressed'), (7, 'Bored'), (8, 'Neutral'), (9, 'Sad'), (10, 'Lazy'), (11, 'Tired'), (12, 'Relaxed')], default=1)),
                ('food_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recommender.FoodType')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
            ],
        ),
    ]
