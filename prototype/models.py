from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime 
from core.models import BaseModel, AbstractModel
from project.models import Project

class Finishing(BaseModel):
    description = models.TextField(verbose_name=_("Description"))

class PropertyType(BaseModel):
    description = models.TextField(verbose_name=_("Description"))

class Equipment(BaseModel):
    class EquipmentType(models.TextChoices):
        interior = "INT", _("Interior")
        exterior = "EXT", _("Exterior")

    type = models.CharField(verbose_name=_("Type"), choices=EquipmentType.choices, default=EquipmentType.interior)

class Segment(BaseModel): 
    description = models.TextField(verbose_name=_("Description"))

class Prototype(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    segment = models.ForeignKey(Segment, on_delete=models.PROTECT)
    propertyType = models.ForeignKey(PropertyType, on_delete=models.PROTECT)
    equipments = models.ManyToManyField(Equipment)
    finishings = models.ManyToManyField(Finishing)

    price = models.IntegerField(verbose_name=_("Price"))
    total_units = models.IntegerField(verbose_name=_("Total units"))
    sold_units = models.IntegerField(verbose_name=_("Sold units"))
    m2_terrain = models.FloatField(verbose_name=("Terrain in square meters"))
    m2_constructed = models.FloatField(verbose_name=("Constructed area in square meters"))
    m2_habitable = models.FloatField(verbose_name=("Habiable area in square meters"))
    floors = models.SmallIntegerField(verbose_name=("Pisos"), default=1)

class Transaction(AbstractModel):
    class TransactionType(models.TextChoices):
        sell = "S", _("Sell")
        devolution = "D", _("Devolution")
    
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)
    type = models.CharField(verbose_name=_("Type"), choices=TransactionType.choices, default=TransactionType.sell)
    date = models.DateField(verbose_name=_("Date"), default=datetime.now)
    quantity = models.IntegerField(verbose_name=_("Quantity"))
