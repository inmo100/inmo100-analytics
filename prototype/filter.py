import django_filters
from .models import Prototype, Project, Segment, PropertyType, EquipmentQuantity, Equipment
from django.forms import NumberInput, CheckboxSelectMultiple
from django_filters.widgets import DateRangeWidget, RangeWidget
from django.db.models import Q
from .views import *

class PrototypeFilter(django_filters.FilterSet):
    name = django_filters.ModelMultipleChoiceFilter(
        field_name='name',
        label='Prototipo',
        widget=CheckboxSelectMultiple(),
        queryset=Prototype.objects.all())

    total_units = django_filters.RangeFilter(
        field_name='total_units',
        label='Unidades Totales',
        widget=RangeWidget(attrs={'type': 'number', 'step': "1"}))
    
    sold_units = django_filters.RangeFilter(
        field_name='sold_units',
        label='Unidades Vendidas',
        widget=RangeWidget(attrs={'type': 'number', 'step': "1"}))
    
    m2_terrain = django_filters.RangeFilter(
        field_name='m2_terrain',
        label='Metros cuadrados de Terreno',
        widget=RangeWidget(attrs={'type': 'number', 'step': "0.1", 'min' : '0'}))
    
    m2_constructed = django_filters.RangeFilter(
        field_name='m2_constructed',
        label='Metros cuadrados construidos',
        widget=RangeWidget(attrs={'type': 'number', 'step': "0.1", 'min' : '0'}))
    
    m2_habitable = django_filters.RangeFilter(
        field_name='m2_habitable',
        label='Metros cuadrados habitables',
        widget=RangeWidget(attrs={'type': 'number', 'step': "0.1", 'min' : '0'}))
    
    floors = django_filters.NumberFilter(
        field_name='floors',
        label='Pisos',
        lookup_expr='exact',
        widget=NumberInput(attrs={'type': 'number', 'min' : '0'}))

    project = django_filters.ModelMultipleChoiceFilter(
        field_name='project_field',
        label='Proyecto',
        widget=CheckboxSelectMultiple(),
        queryset=Project.objects.all())

    property_type = django_filters.ModelMultipleChoiceFilter(
        field_name='propertyType',
        label='Tipo de propiedad',
        widget=CheckboxSelectMultiple(),
        queryset=PropertyType.objects.all())

    segment = django_filters.ModelMultipleChoiceFilter(
        field_name='segment_field',
        label='Segmento',
        widget=CheckboxSelectMultiple(),
        queryset=Segment.objects.all())

    """ equipment = django_filters.ModelMultipleChoiceFilter(
        field_name='equipment',
        label='Equipamiento',
        widget=CheckboxSelectMultiple(),
        queryset=Equioment.objects.exclude(equipment=0))  """

    equipment = django_filters.ModelMultipleChoiceFilter(
        field_name='equipment',
        label='Equipamiento',
        widget=CheckboxSelectMultiple(),
        queryset=EquipmentQuantity.objects.all().select_related('equipment', 'prototype'))   


    """ equipments = django_filters.ModelMultipleChoiceFilter(
        field_name='equipments',
        label='Equipamiento',
        widget=CheckboxSelectMultiple(),
        queryset=EquipmentQuantity.objects.all().select_related('equipment'))  """
