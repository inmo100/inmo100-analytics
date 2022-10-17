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
from .models import Prototype
from django.db.models import Q, Count

# Create your views here.

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter_view(request, project_id = 0):
    query = Prototype.objects.all()
    total_units_check = request.GET.get('totalUnits')
    sold_units_check = request.GET.get('soldUnits')
    stock_check = request.GET.get('stock')

    price_range_min = request.GET.get('priceMin')
    price_range_max = request.GET.get('priceMax')
    m2_terrain_min = request.GET.get('m2TerrainMin')
    m2_terrain_max = request.GET.get('m2TerrainMax')
    m2_constructed_min = request.GET.get('m2ConstructedMin')
    m2_constructed_max = request.GET.get('m2ConstructedMax')
    m2_habitable_min = request.GET.get('m2HabitableMin')
    m2_habitable_max = request.GET.get('m2HabitableMax')
    
    query = Q()

    # if total_units_check == 'on':
    #     qs = qs.raw('SELECT total_units FROM prototype_prototype')
    
    # if sold_units_check == 'on':
    #     qs = qs.raw('SELECT sold_units FROM prototype_prototype')
    
    # if stock_check == 'on':
    #     qs = qs.raw('SELECT (SUM(total_units) -  SUM(sold_units)) FROM prototype_prototype')

    print(project_id)
    if is_valid_queryparam(project_id):
        query &= Q(project_field=project_id)

    if is_valid_queryparam(price_range_min):
        query &= Q(price__gte=price_range_min)

    if is_valid_queryparam(price_range_max):
        query &= Q(price__lt=price_range_max)
    
    if is_valid_queryparam(m2_terrain_min):
        query &= Q(m2_terrain__gte=m2_terrain_min)

    if is_valid_queryparam(m2_terrain_max):
        query &= Q(m2_terrain__lt=m2_terrain_max)
    
    if is_valid_queryparam(m2_constructed_min):
        query &= Q(m2_constructed__gte=m2_constructed_min)

    if is_valid_queryparam(m2_constructed_max):
        query &= Q(m2_constructed__lt=m2_constructed_max)
    
    if is_valid_queryparam(m2_habitable_min):
        query &= Q(m2_habitable__gte=m2_habitable_min)

    if is_valid_queryparam(m2_habitable_max):
        query &= Q(m2_habitable__lt=m2_habitable_max)

    prototypes = Prototype.objects.filter(query)

    context = {
        'queryset': prototypes,
    }

    return render(request, "filters/filters.html", context)

def guardar_datos_csv(arr,pf):
    project = Project.objects.get(id=pf)
    for i in arr:
        if(i[8] == 'null'):
            segment = Segment.objects.get(name='No existe')    
        else:
            segment = Segment.objects.get(name=i[8])
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
        prototipo.floors = i[7]
        prototipo.save()

def handle_uploaded_file(f,pf):  
    with open('static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    valores = pd.read_csv('static/'+f.name)
    valores = valores.fillna("null")
    valores = valores.values.tolist()
    guardar_datos_csv(valores,pf)
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
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],project_field)
                return render(request,'prototype_uploaded.html', context={'project_id': project_field})
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})


class PrototypeView(ListView):
    template_name = 'table.html'
    model = Prototype
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,context={
            'list_prototype':Prototype.objects.all(),
            'project_id':self.kwargs['id']
            })



