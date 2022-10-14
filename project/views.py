from django.http import HttpResponse
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import *
from django.shortcuts import redirect
# Create your views here.

#Función para guardar los datos de la desarrolladora

class DeveloperView(TemplateView):
    template_name = 'home_desarrolladora.html'

class CreateDeveloper(TemplateView):
    template_name = 'form_desarrolladora.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        image_developer = IMG_Form(request.POST, request.FILES)
        if image_developer.is_valid():
         developer = Developer()
         developer.name = request.POST['name']
         developer.description = request.POST['description']
         developer.image = request.FILES['image']
         networks = {"twitter": "twitter", "facebook": "facebook"}
         developer.social_networks = networks
         developer.save()
         return render(request,self.template_name)



class ProjectView(TemplateView):
    template_name = 'home_proyecto.html'
