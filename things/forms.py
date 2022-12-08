"""Forms of the project."""
from django import forms
from .models import Thing
# Create your forms here.


class ThingForm(forms.Form):
    name = forms.CharField(label="Name")
    description = forms.CharField(widget=forms.TextInput(attrs={'name':'description'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'quantity'}))
