import django_filters
from .models import Developer, Project, Colony
from django.forms import NumberInput, CheckboxSelectMultiple
from django_filters.widgets import DateRangeWidget, RangeWidget
from django.db.models import Q


class ProjectFilter(django_filters.FilterSet):
    initial_date = django_filters.DateFromToRangeFilter(
        field_name='initial_date',
        label='Fecha de Inicio',
        widget=DateRangeWidget(attrs={'type': 'date', 'class': 'input'}))

#    latitude = django_filters.RangeFilter(
#        field_name='latitude',
#        label='Latitud',
#        widget=RangeWidget(attrs={'type': 'number', 'step': "0.0000000000000001", 'class': 'input'}))

#    longitude = django_filters.RangeFilter(
#        field_name='longitude',
#        label='Longitud',
#        widget=RangeWidget(attrs={'type': 'number', 'step': "0.0000000000000001", 'class': 'input'}))

    levels = django_filters.NumberFilter(
        field_name='levels',
        label='Niveles',
        lookup_expr='exact',
        widget=NumberInput(attrs={'type': 'number', 'min': '0', 'class': 'input'}))

    developer = django_filters.ModelMultipleChoiceFilter(
        field_name='developer_field',
        label='Desarrolladora',
        widget=CheckboxSelectMultiple(attrs={'checked': 'true'}),
        queryset=Developer.objects.all().order_by('name'))

    name = django_filters.ModelMultipleChoiceFilter(
        field_name='name',
        label='Proyecto',
        widget=CheckboxSelectMultiple(attrs={'checked': 'true'}),
        queryset=Project.objects.all().order_by('name'))

    colony = django_filters.ModelMultipleChoiceFilter(
        field_name='colony_field',
        label='Colonia',
        widget=CheckboxSelectMultiple(attrs={'checked': 'true'}),
        queryset=Colony.objects.all().order_by('name'))
