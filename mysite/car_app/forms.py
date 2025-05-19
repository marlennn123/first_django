from django import forms
from .models import Car


class CarForms(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_name', 'brand', 'model', 'price',
                  'year', 'mileage', 'color', 'city', 'description',
                  'image']