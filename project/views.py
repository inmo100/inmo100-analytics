from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import *

# Create your views here.

class DeveloperView(TemplateView):
    template_name = 'home_desarrolladora.html'

class CreateDeveloper(CreateView):
    template_name = 'home_desarrolladora.html'
    model=Developer
    form_class = DeveloperForm
    success_url = '/'


class ProjectView(TemplateView):
    template_name = 'home_proyecto.html'
