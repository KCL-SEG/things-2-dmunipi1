"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your forms here.


class ThingForm(forms.Form):
    name = forms.CharField(label="Name", max_length=35)
    description = forms.CharField(widget=forms.Textarea(attrs={'name':'description'}), max_length=120)
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'quantity'}), validators=[MinValueValidator(0),MaxValueValidator(50)])
