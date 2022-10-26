from django.http import HttpResponse
from pipes import Template
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import *
from django.shortcuts import redirect
# Create your views here.
from .models import *
import pandas as pd
from os import remove
import os.path

def delete_prototypes(project_fields):
    project_prototypes = Prototype.objects.filter(project_field = project_fields)
    project_prototypes.delete()

def save_data_csv(arr,project_field):
    iterable = 10
    helper = []
    project = Project.objects.get(id=project_field)
    for i in arr:
        if(i[8] == 'null'):
            segment = Segment.objects.get(name='No existe')    
        else:
            if(Segment.objects.filter(name=i[8]).exists() == False):
                segment = Segment.objects.get(name="No existe")
            else:
                segment = Segment.objects.get(name=i[8])
        
        if(i[9] == 'null'):
            property_type = PropertyType.objects.get(name='No existe')
        else:
            if(PropertyType.objects.filter(name=i[9]).exists() == False):
                property_type = PropertyType.objects.get(name='No existe')
            else:
                property_type = PropertyType.objects.get(name=i[9])
         
        if(i[10] == 'null'):
            finishing = Finishing.objects.get(name='No existe')
            helper.append(finishing)
        else:
            if(Finishing.objects.filter(name=i[10]).exists() == False):
                finishing = Finishing.objects.get(name='No existe')
                helper.append(finishing)
            else:
                finishing = Finishing.objects.get(name=i[10])
                helper.append(finishing)
        if(i[11] == 'null'):
            finishing = Finishing.objects.get(name='No existe')
            helper.append(finishing)
        else:
            if(Finishing.objects.filter(name=i[11]).exists() == False):
                finishing = Finishing.objects.get(name='No existe')
                helper.append(finishing)
            else:
                finishing = Finishing.objects.get(name=i[11])
                helper.append(finishing)
        if(i[12] == 'null'):
            finishing = Finishing.objects.get(name='No existe')
            helper.append(finishing)
        else:
            if(Finishing.objects.filter(name=i[12]).exists() == False):
                finishing = Finishing.objects.get(name='No existe')
                helper.append(finishing)
            else:
                finishing = Finishing.objects.get(name=i[12])
                helper.append(finishing)
        if(i[13] == 'null'):
            finishing = Finishing.objects.get(name='No existe')
            helper.append(finishing)
        else:
            if(Finishing.objects.filter(name=i[13]).exists() == False):
                finishing = Finishing.objects.get(name='No existe')
                helper.append(finishing)
            else:
                finishing = Finishing.objects.get(name=i[13])
                helper.append(finishing)
        if(i[14] == 'null'):
            finishing = Finishing.objects.get(name='No existe')
            helper.append(finishing)
        else:
            if(Finishing.objects.filter(name=i[14]).exists() == False):
                finishing = Finishing.objects.get(name='No existe')
                helper.append(finishing)
            else:
                finishing = Finishing.objects.get(name=i[14])
                helper.append(finishing)
        if(i[15] == 'null'):
            finishing = Finishing.objects.get(name='No existe')
            helper.append(finishing)
        else:
            if(Finishing.objects.filter(name=i[15]).exists() == False):
                finishing = Finishing.objects.get(name='No existe')
                helper.append(finishing)
            else:
                finishing = Finishing.objects.get(name=i[15])
                helper.append(finishing)
        
        prototype = Prototype()
        prototype.segment_field = segment
        prototype.project_field = project
        prototype.name = i[0]
        prototype.price = i[1]
        prototype.total_units = i[2]
        prototype.sold_units = i[3]
        prototype.m2_terrain = i[4]
        prototype.m2_constructed = i[5]
        prototype.m2_habitable = i[6]
        prototype.propertyType = property_type
        prototype.save()
        prototype = Prototype.objects.get(name=i[0])
        prototype.finishings.set(helper)
        helper.clear()

def handle_uploaded_file(f,project_field,action):  
    with open('static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    valores = pd.read_csv('static/'+f.name)
    valores = valores.fillna("null")
    valores = valores.values.tolist()
    if(action=='c'):
        save_data_csv(valores,project_field)
    elif(action=='u'):
        delete_prototypes(project_field)
        save_data_csv(valores,project_field)
    remove('static/'+f.name)

class CreatePrototype(ListView):
    template_name = 'pages/form_prototype.html'
    model = Segment
    def get(self,request,*args,**kwargs):
        download_csv()
        return render(request,self.template_name,context={
            'list_segment':Segment.objects.all(),
            'id':self.kwargs['id']
            })
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],project_field,'c')
                return redirect("prototypes")
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})


class PrototypesListView(ListView):
    template_name = 'pages/prototypes.html'
    model = Prototype
    def get(self, request, *args,**kwargs):
        return render(request,self.template_name,context={
            'prototype_list': Prototype.objects.all(),
        })


class UpdatePrototype(ListView):
    template_name = 'update_prototypes.html'
    model = Segment
    def get(self,request,*args,**kwargs):
        download_csv()
        return render(request,self.template_name,context={
            'id':self.kwargs['id']
            })
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],project_field,'u')
                return redirect("prototypes")
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})


def download_csv():
    if(os.path.isfile("static/plantilla_prototipos2.csv")):
        remove("static/plantilla_prototipos2.csv")
    equipments = Equipment.objects.all()
    template = pd.read_csv("static/plantilla_prototipos.csv")
    arr = [""]
    for equipment in equipments:
        template[equipment.name] = arr
    template = template.drop(0)
    template.to_csv("static/plantilla_prototipos2.csv",sep=",",index=False,encoding="utf-8")
