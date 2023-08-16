from django import forms
from .models import Restaurants

class RestaurantaCreateForm(forms.ModelForm):
    class Meta:
        model=Restaurants
        fields=('name','description','location','image')
    