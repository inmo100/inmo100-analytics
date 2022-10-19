from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Project, Developer

class DeveloperForm(forms.ModelForm ):
    choice = forms.ModelChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Developer.objects.all())
    class Meta:
        model = Developer
        fields = ('hidden',)


class IMG_Form(forms.Form):
    image = forms.FileField()


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'image', 'logo', 'initial_date', 'longitude', 'latitud', 'address', 'phone', 'brochure', 'social_networks')