from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
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


    
    
    

    
