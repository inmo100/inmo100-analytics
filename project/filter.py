import django_filters
from .models import Developer, Project
from django.forms import NumberInput
from django_filters.widgets import DateRangeWidget, RangeWidget
from django.db.models import Q


class ProjectFilter(django_filters.FilterSet):
    initial_date = django_filters.DateFromToRangeFilter(
        field_name='initial_date',
        label='Fecha de Inicio',
        widget=DateRangeWidget(attrs={'type': 'date'}))

    # description = django_filters.CharFilter(
    #     field_name='description',
    #     label='Descripción',
    #     lookup_expr='icontains')

    latitude = django_filters.RangeFilter(
        field_name='latitud',
        label='Latitud',
        widget=RangeWidget(attrs={'type': 'number', 'step': "0.1"}))

    longitude = django_filters.RangeFilter(
        field_name='longitude',
        label='Longitud',
        widget=RangeWidget(attrs={'type': 'number', 'step': "0.1"}))

    # address = django_filters.CharFilter(
    #     field_name='address',
    #     label='Dirección',
    #     lookup_expr='icontains')

    # phone = django_filters.CharFilter(
    #     field_name='phone',
    #     label='Teléfono',
    #     lookup_expr='icontains')

    levels = django_filters.NumberFilter(
        field_name='levels',
        label='Niveles',
        lookup_expr='exact',
        widget=NumberInput(attrs={'type': 'number', 'min' : '0', 'max' : '15'}))

    developer = django_filters.ModelMultipleChoiceFilter(
        field_name='developer_field',
        label='Desarrolladora',
        queryset=Developer.objects.all())

    name = django_filters.ModelMultipleChoiceFilter(
        field_name='name',
        label='Proyecto',
        queryset=Project.objects.all())
