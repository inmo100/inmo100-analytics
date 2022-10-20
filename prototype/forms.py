from django import forms
from django.forms import ModelForm
from .models import Prototype


class CSV_Form(forms.Form):
    csv = forms.FileField()
