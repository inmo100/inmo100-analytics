from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View
from .forms import IMG_Form, ProjectForm, DeveloperForm
# Create your views here.
from .models import Developer, Project, Colony
import json
from django.db.models import Q
from .filter import ProjectFilter

# Función para guardar los datos de la desarrolladora


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
         fb = request.POST['fb']
         yb = request.POST['yb']
         arr = {}
         if(yb!=None):
            arr['youtube'] = yb
         if(fb!=None):
            arr['facebook'] = fb
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
    template_name = 'pages/projects_home.html'
    model = Project
    queryset: Developer.objects.all()
    context_object_name = 'list_projects'


class ProjectDetail(DetailView):
    model = Project

def filter_view(request):
    context = {
        'developers': Developer.objects.filter(),
        'colonies' : Colony.objects.filter(),
    }

    projects_filter = get_filter_queryset(request, Project.objects.all())
    context['projects_filter'] = projects_filter

    return render(request, 'pages/projects.html', context)

def get_filter_queryset(request, projects):
    return ProjectFilter(request.GET, queryset=projects)

def is_valid_queryparam(param):
    return param != '' and param is not None
