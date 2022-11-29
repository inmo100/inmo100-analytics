from tabnanny import check
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import redirect
from .filter import PrototypeFilter
from .forms import *
from .models import *
from .helpers import *

# List prototypes class view
# Use Case: 12, 24, 25, 26, 27, 28, 29, 30
class PrototypesList(ListView):
    template_name = 'pages/prototypes/home.html'
    def get(self, request, *args, **kwargs):
        #------------------------------------------------------------------------
        # This is for the select form
        prototypes_form = Prototype.objects.all().order_by('name')
        projects_form = Project.objects.all().order_by('name')
        segment_form = Segment.objects.all().order_by('name')
        propertyType_form = PropertyType.objects.all().order_by('name')
        equipments_form = Equipment.objects.all().order_by('name')
        materials_form  = Material.objects.all().order_by('name')
        #------------------------------------------------------------------------
        prototypes_id = request.GET.getlist('prototype')
        prototypes_id = check_arguments(prototypes_id)
        projects_id = request.GET.getlist('project')
        projects_id = check_arguments(projects_id)
        segments_id = request.GET.getlist('segment')
        segments_id = check_arguments(segments_id)
        propertyTypes = request.GET.getlist('propertyType')
        propertyTypes = check_arguments(propertyTypes)
        total_units = [request.GET.get('total_units_min',''),request.GET.get('total_units_max','')]
        total_units = check_arguments(total_units)
        sold_units = [request.GET.get('sold_units_min',''),request.GET.get('sold_units_max','')]
        sold_units = check_arguments(sold_units)
        m2_terrain = [request.GET.get('m2_terrain_min',''),request.GET.get('m2_terrain_max','')]
        m2_terrain = check_arguments(m2_terrain)
        m2_constructed = [request.GET.get('m2_constructed_min',''),request.GET.get('m2_constructed_max','')]
        m2_constructed = check_arguments(m2_constructed)
        m2_habitable = [request.GET.get('m2_habitable_min',''),request.GET.get('m2_habitable_max','')]
        m2_habitable = check_arguments(m2_habitable)
        floors = [request.GET.get('floors_min',''),request.GET.get('floors_max','')]
        floors = check_arguments(floors)
        equipments_id = request.GET.getlist('equipment')
        equipments_id = check_arguments(equipments_id)
        materials_id = request.GET.getlist('material')
        materials_id = check_arguments(materials_id)
        #------------------------------------------------------------------------
        # This are the filters
        prototypes = Prototype.objects.project_filter(projects_id)
        prototypes = Prototype.objects.prototype_filter(prototypes,prototypes_id)
        if prototypes == 1:
            return render(request, self.template_name)
        prototypes = Prototype.objects.segment_filter(segments_id,prototypes)
        prototypes = Prototype.objects.propertyType_filter(propertyTypes,prototypes)
        prototypes = Prototype.objects.total_units_filter(total_units,prototypes)
        prototypes = Prototype.objects.total_units(prototypes)
        prototypes = Historical.objects.available_units_filter(sold_units,prototypes)
        prototypes = Prototype.objects.m2_terrain_filter(m2_terrain,prototypes)
        prototypes = Prototype.objects.m2_constructed_filter(m2_constructed,prototypes)
        prototypes = Prototype.objects.m2_habitable_filter(m2_habitable,prototypes)
        prototypes = Prototype.objects.floors_filter(floors,prototypes)
        prototypes = EquipmentQuantity.objects.equipment_filter(equipments_id,prototypes)
        prototypes = Triangulo.objects.triangulo_filter(materials_id,prototypes)
        #------------------------------------------------------------------------
        #This line needs to be at the end of the filtering section
        prototypes = Prototype.objects.get_prototypes(prototypes)
        #------------------------------------------------------------------------
        
        equipments = Equipment.objects.all().order_by('id')
        finishings = Finishing.objects.all().order_by('id')
        prototypes_list = bring_prototypes(prototypes)
        return render(request, self.template_name, context={
            'prototypes_list':prototypes_list,
            'equipments':equipments,
            'finishings':finishings,
            'prototypes_form':prototypes_form,
            'projects_form':projects_form,
            'segment_form':segment_form,
            'propertyType_form':propertyType_form,
            'equipments_form':equipments_form,
            'materials_form':materials_form,
        })
