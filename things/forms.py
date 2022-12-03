"""Forms of the project."""
from django import forms
from .models import Thing
# Create your forms here.


class ThingForm(forms.Form):
    name = forms.CharField(label="name")
    description = forms.TextArea(label="description")
    quantity = forms.NumberInput(label="quantity")
