from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime 
from core.models import BaseModel, AbstractModel
from project.models import Project

#arreglar el MER y MR
class Material(BaseModel):
    pass

class Finishing(BaseModel): # Acabados en el MER
    pass

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

    #available_units = models.IntegerField(verbose_name=_("Available Units"),null=True)
    total_units = models.IntegerField(verbose_name=_("Total units"),null=True)
    m2_terrain = models.FloatField(verbose_name=("Terrain in square meters"),null=True)
    m2_constructed = models.FloatField(verbose_name=("Constructed area in square meters"),null=True)
    m2_habitable = models.FloatField(verbose_name=("Habiable area in square meters"),null=True)
    floors = models.SmallIntegerField(verbose_name=("Pisos"), default=1,null=True)

class EquipmentQuantity(AbstractModel):
    equipment = models.ForeignKey(Equipment, on_delete=models.PROTECT)
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name=("Equipment quantity per prototype"),null=True)

class Triangulo(AbstractModel):
    finishings = models.ForeignKey(Finishing, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)

# Handles prototype historical data
class Historical(models.Model):# Historical only needs abstract model
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)

    date = models.DateField(verbose_name=_("Date"), default=datetime.now)
    price = models.IntegerField(verbose_name=_("Price"),null=True)
    available_units = models.IntegerField(verbose_name=_("Available Units"),null=True)