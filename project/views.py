from django.http import HttpResponse
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import *
from django.shortcuts import redirect
# Create your views here.
from .models import *
import json

#Función para guardar los datos de la desarrolladora

class DeveloperView(ListView):
    template_name = 'home_desarrolladora.html'
    model = Developer
    queryset: Developer.objects.all()
    context_object_name = 'list_developers'

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
         ig = request.POST['ig']
         wp = request.POST['wp']
         arr = {}
         if(ig!=None):
            arr['instagram'] = ig
         if(wp!=None):
            arr['pagina_web'] = wp
         networks = json.dumps(arr)
         developer.social_networks = networks
         developer.save()
         return render(request,self.template_name)


class CreateProject(CreateView):
    template_name = 'form_proyectos.html'
    model = Project
    form_class = ProjectForm
    success_url = '/proyectos'

class ProjectView(ListView):
    template_name = 'home_proyecto.html'
    model = Project
    queryset: Developer.objects.all()
    context_object_name = 'list_projects'
