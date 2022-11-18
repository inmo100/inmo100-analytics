from django.contrib import admin
from .models import *
from .forms import *
from .helpers import *

@admin.register(Historical)
class HistoricalAdmin(admin.ModelAdmin):
    list_display = ('prototype', 'price', 'available_units', 'date')

@admin.register(Triangulo)
class TriangleAdmin(admin.ModelAdmin):
    list_display = ('prototype', 'finishings', 'material')

@admin.register(EquipmentQuantity)
class EquipmentQuantityAdmin(admin.ModelAdmin):
    list_display = ('prototype', 'equipment', 'quantity')

@admin.register(Prototype)
class PrototypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_field', 'segment_field', 'propertyType', 'total_units', 'm2_terrain', 'm2_constructed', 'm2_habitable', 'floors')


admin.site.register(Material)
admin.site.register(Finishing)
admin.site.register(PropertyType)
admin.site.register(Segment)
admin.site.register(Equipment)