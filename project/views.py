from django.http import HttpResponse
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import *
from django.shortcuts import redirect
# Create your views here.
from .models import *
import json
from django.db.models import Q, Count

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


class ProjectDetail(DetailView):
    model = Project


class FilterView(ListView):
    template_name = 'filters/filters.html'
    model = Developer
    # def get(self,request,*args,**kwargs):
    #     developers = Developer.objects.all()
    #     # developers = Developer.objects.filter(query)
    #     return render(request,self.template_name,context={
    #         'developers': developers,
    #         'args':kwargs
    #         })
    form_class = DeveloperForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            developer = Developer()
            developer.pk = request.POST['pk']
            form.save()
        else:
            context = {
            'form': form,
            }
            return render(request, self.template_name, context)


def is_valid_queryparam(param):
    return param != '' and param is not None

def filter_view(request):
    query = Developer.objects.all()
    developers_check = request.GET.get('developers')
    
    query = Q()

    developers = Developer.objects.filter(query)

    context = {
        'developers': developers,
    }

    if request.GET.keys():
        if request.method == "GET":
            ids = []
            for key, value in request.GET.lists():
                ids.append(value)
            num = ids[0]
            ids_list = len(num)
            arr_ids = []
            for i in range(ids_list):
                arr_ids.insert(0,ids[0][i])   
            arr = [int(item) for item in arr_ids]
            projects=Project.objects.filter(developer_field__in=arr) 
            context = {
                'developers': developers,
                'projects' : projects
            } 
            return render(request, 'filters/filters.html', context)
    return render(request, 'filters/filters.html', context)