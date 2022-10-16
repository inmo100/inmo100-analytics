from django.http import HttpResponse
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import *
from django.shortcuts import redirect
# Create your views here.
from .models import *
import pandas as pd
from os import remove

"""class CreateDeveloper(TemplateView):
    template_name = 'form_prototipo.html'
    def get(self, request, *args, **kwargs):
        project_id = self.kwargs['id']
        return render(request, self.template_name,context={'prueba':project_id})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)"""


"""class CreateDeveloper(CreateView):
    template_name = 'form_prototipo.html'
    model = Project
    form_class = PrototypeForm
    def get(self,request,*args,**kwargs):

    def post(self,request,*args,**kwargs):
        project_field = self.kwargs['id']
        segment_field = request.POST['segment_field']
        project_field = request.POST['project_field']
        return render(request,self.template_name,context={'project_field':project_field})"""



def guardar_datos_csv(arr,sf,pf):
    segment = Segment.objects.get(id=sf)
    project = Project.objects.get(id=pf)
    for i in arr:
        prototipo = Prototype()
        prototipo.segment_field = segment
        prototipo.project_field = project
        prototipo.name = i[0]
        prototipo.price = i[1]
        prototipo.total_units = i[2]
        prototipo.sold_units = i[3]
        prototipo.m2_terrain = i[4]
        prototipo.m2_constructed = i[5]
        prototipo.m2_habitable = i[6]
        prototipo.save()

def handle_uploaded_file(f,sf,pf):  
    with open('static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    valores = pd.read_csv('static/'+f.name)
    valores = valores.fillna("null")
    valores = valores.values.tolist()
    guardar_datos_csv(valores,sf,pf)
    remove('static/'+f.name)

class CreatePrototype(ListView):
    template_name = 'form_prototipo.html'
    model = Segment
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,context={
            'list_segment':Segment.objects.all(),
            'id':self.kwargs['id']
            })
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        segment_field = request.POST['segment_field']
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],segment_field,project_field)
                return render(request,self.template_name,context={'Prueba':'Se pudo'})
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})
