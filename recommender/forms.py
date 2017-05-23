from django import forms

from .models import Person

class RecommenderForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('primary_mood',)
        labels = {
            'primary_mood': 'How are you feeling?',
        }
