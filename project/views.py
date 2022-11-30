from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import IMG_Form, ProjectForm
from .models import Developer, Project
import json
from django_filters.views import FilterView
from .filter import ProjectFilter
from django.contrib.auth.mixins import LoginRequiredMixin

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
            if (yb != None):
                arr['youtube'] = yb
            if (fb != None):
                arr['facebook'] = fb
            if (ig != None):
                arr['instagram'] = ig
            if (wp != None):
                arr['pagina_web'] = wp
            networks = json.dumps(arr)
            developer.social_networks = networks
            developer.save()
            return render(request, self.template_name)


class CreateProject(CreateView):
    template_name = 'form_proyectos.html'
    model = Project
    form_class = ProjectForm
    success_url = 'projects'


class DevelopersList(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = 'pages/developers/home.html'
    model = Developer
    queryset = Developer.objects.all()
    context_object_name = 'developers_list'
    login_url = 'login'
    redirect_field_name = 'redirect_to'


class ProjectDetail(DetailView):
    template_name = 'pages/projects/single.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prototypes'] = context['project'].prototype_set.all()
        return context


class ProjectsList(LoginRequiredMixin, FilterView):
    model = Project
    template_name: str = 'pages/projects/home.html'
    filterset_class = ProjectFilter
    context_object_name = 'projects_list'
    login_url = 'login'
    redirect_field_name = 'redirect_to'


def is_valid_queryparam(param):
    return param != '' and param is not None
