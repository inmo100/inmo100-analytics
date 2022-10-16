from django import forms
from django.forms import ModelForm
from .models import Project, Developer

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ('name','description', 'image')


class IMG_Form(forms.Form):
    image = forms.FileField()


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'image', 'logo', 'initial_date', 'longitude', 'latitud', 'address', 'phone', 'brochure', 'social_networks')