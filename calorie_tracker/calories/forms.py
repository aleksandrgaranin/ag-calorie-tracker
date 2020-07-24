from django import forms
from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['user', 'name', 'carbs', 'protein', 'fat', 'calories']