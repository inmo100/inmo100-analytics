from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime 
from core.models import BaseModel, AbstractModel
from project.models import Project

class Finishing(BaseModel): # Acabados en el MER
    description = models.TextField(verbose_name=_("Description"))

class PropertyType(BaseModel):
    '''
    Refers to:
    Loft
    Casa
    Duplex
    Departamento
    Etc.
    '''
    description = models.TextField(verbose_name=_("Description"))

class Equipment(BaseModel):
    '''
    Refers to:
    Baño
    Habitación
    Cochera

    '''
    class EquipmentType(models.TextChoices):
        # Choice menu
        interior = "INT", _("Interior")# enum for interior equipment
        exterior = "EXT", _("Exterior")# enum for exterior equipment

    type = models.CharField(verbose_name=_("Type"), choices=EquipmentType.choices, default=EquipmentType.interior, max_length=100)
    # add new entity to handle relation quantities between prototype and equipment

class Segment(BaseModel): 
    description = models.TextField(verbose_name=_("Description"))

class Prototype(BaseModel):
    project_field = models.ForeignKey(Project, on_delete=models.PROTECT)
    segment_field = models.ForeignKey(Segment, on_delete=models.PROTECT)
    propertyType = models.ForeignKey(PropertyType, on_delete=models.PROTECT)
    equipments = models.ManyToManyField(Equipment)# add new entity to handle relation quantities between prototype and equipment
    finishings = models.ManyToManyField(Finishing)

    price = models.IntegerField(verbose_name=_("Price"))
    total_units = models.IntegerField(verbose_name=_("Total units"))
    sold_units = models.IntegerField(verbose_name=_("Sold units"))
    m2_terrain = models.FloatField(verbose_name=("Terrain in square meters"))
    m2_constructed = models.FloatField(verbose_name=("Constructed area in square meters"))
    m2_habitable = models.FloatField(verbose_name=("Habiable area in square meters"))
    floors = models.SmallIntegerField(verbose_name=("Pisos"), default=1)

# Handles prototype sales
class Transaction(AbstractModel):# Transactions only need abstract model
    class TransactionType(models.TextChoices):
        # Choice menu
        sell = "S", _("Sell")
        refund = "D", _("Refund")
    
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)
    type = models.CharField(verbose_name=_("Type"), choices=TransactionType.choices, default=TransactionType.sell, max_length=100)
    date = models.DateField(verbose_name=_("Date"), default=datetime.now)
    quantity = models.IntegerField(verbose_name=_("Quantity"))
