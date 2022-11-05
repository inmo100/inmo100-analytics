from enum import unique
from lib2to3.pytree import Base
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime 
from core.models import BaseModel, AbstractModel
from project.models import Project

class Finishing(BaseModel): # Acabados en el MER
    finishing_type = models.ForeignKey(FinishingType, on_delete=models.PROTECT)
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

class Segment(BaseModel): 
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

class Prototype(BaseModel):
    project_field = models.ForeignKey(Project, on_delete=models.PROTECT)
    segment_field = models.ForeignKey(Segment, on_delete=models.PROTECT)
    propertyType = models.ForeignKey(PropertyType, on_delete=models.PROTECT,null=True)
    equipments = models.ManyToManyField(Equipment, through='EquipmentQuantity', null=True)
    finishings = models.ManyToManyField(Finishing,through='FinishingType', null=True)

    price = models.IntegerField(verbose_name=_("Price"),null=True)
    total_units = models.IntegerField(verbose_name=_("Total units"),null=True)
    sold_units = models.IntegerField(verbose_name=_("Sold units"),null=True)
    m2_terrain = models.FloatField(verbose_name=("Terrain in square meters"),null=True)
    m2_constructed = models.FloatField(verbose_name=("Constructed area in square meters"),null=True)
    m2_habitable = models.FloatField(verbose_name=("Habiable area in square meters"),null=True)
    floors = models.SmallIntegerField(verbose_name=("Pisos"), default=1,null=True)

class EquipmentQuantity(AbstractModel):
    equipment = models.ForeignKey(Equipment, on_delete=models.PROTECT)
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name=("Equipment quantity per prototype"),null=True)

class FinishingType(AbstractModel):
    finishing = models.ForeignKey(Finishing, on_delete=models.PROTECT)
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)

    class Types(models.TextChoices):
        # Choice menu
        sistemaConstructivo = "SC", _("Sistema Constructivo")
        pisos = "P", _("Pisos")
        muros = "M", _("Muros")
        canceleriaVentanas = "CV", _("Cancelería Ventanas")
        cubiertaCocina = "CC", _("Cubierta Cocina")
        carpinteria = "C", _("Carpintería")
    
    type = models.CharField(verbose_name=_("Types"), choices=Types.choices, default=Types.pisos, max_length=100)

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
