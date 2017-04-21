from django import forms

from .models import Person

class RecommenderForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('primary_mood', 'secondary_mood')
